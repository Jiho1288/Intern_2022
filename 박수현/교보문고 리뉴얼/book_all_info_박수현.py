# 0. 필요한 모듈 가져오기
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, json

# 0. 바코드 텍스트파일 리스트로 변환하는 프로그램 정의하기
# 오류로 인해 재시도하고자 한다면, f"{category_name[i]}_2.txt" 로 변경
def is_book_barcode(i):
    category_name = ["유아(0~7세)", "어린이(초등)"]
    with open(f"./{category_name[i]}_set.txt", "r") as f:
        book_barcode_list = f.read().splitlines()
    
    return book_barcode_list

# 0. 데이터 크롤링 프로그램 정의하기
def is_book_info():
    # book_page = 책 데이터
    book_page = BeautifulSoup(driver.page_source, "html.parser")

    # book_title = 책 제목
    book_title = book_page.select_one("span.prod_title").text.strip()
    # book_writer = 책 저자
    book_writer = book_page.select("div.author a")[0].text.strip()
    # book_info = 책 정보 (출판사·출간일(1쇄 날짜))
    book_info = book_page.select_one("div.prod_info_text.publish_date").text.split("·")
    # book_publisher = 책 출판사
    book_publisher = book_info[0].strip()
    # book_date = 책 출간일
    book_date = book_info[-1].split("출시")[0].strip()
    # book_isbn = 책 ISBN-13
    book_isbn = book_page.select_one("tbody > tr > td").text.split(" ( ")[0].strip()
    # book_keyword = 책 키워드
    book_keyword_list = []
    for book_keyword in book_page.select("div.product_detail_area.product_keyword_pick a.tab_link > span.tab_text"):
        book_keyword_list.append(book_keyword.text.strip())
    if book_keyword_list == []:
        book_keyword = "등록된 키워드가 없습니다."
    else:
        book_keyword = ', '.join(book_keyword_list)
    print(book_title, book_writer, book_publisher, book_date, book_isbn, book_keyword)

    # book_detail = 책 소개
    try:
        book_detail = book_page.select_one("div.product_detail_area.book_intro div.intro_bottom").text.strip().replace("\n", " ")
    except:
        book_detail = "등록된 책 소개가 없습니다."
    # book_review_pub = 책 출판사 서평
    try:
        book_review_pub = book_page.select_one("div.product_detail_area.book_publish_review p.info_text").text.strip().replace("\n", " ")
    except:
        book_review_pub = "등록된 서평이 없습니다."
    print(book_detail)
    print(book_review_pub)

    # book_review_text = 감성 태그
    # book_level = Klover 평점
    # book_klover = Klover 리뷰
    try:
        book_review_text = book_page.select_one("div.col_review > span.review_quotes_text").text.strip()
        try:
            book_level = book_page.select_one("div.col_review > span.review_score.feel_lucky").text.strip()
        except:
            book_level = book_page.select_one("div.col_review > span.review_score").text.strip()
        ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//*[@id='ReviewList1']/div[3]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div")).perform()
        driver.find_element(By.XPATH, "//*[@id='ReviewList1']/div[3]/div[1]/ul/li[1]/button/span").click()
        time.sleep(5)
        book_klover_list = []
        while True:
            try:
                book_page = BeautifulSoup(driver.page_source, "html.parser")
                for book_klover in book_page.select("div.comment_list div.comment_text_box div.comment_text"):
                    book_klover_list.append(book_klover.text.strip().replace("\n", " ").replace("\xa0", " "))
                book_klover_list.pop(-1)
                book_klover_list.pop(-1)
                
                ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR, "div.product_detail_area.killing_part")).perform()
                driver.find_element(By.CSS_SELECTOR, "div.tab_content div.pagination button.btn_page.next").click()
                time.sleep(5)
            except:
                break
    except:
        book_review_text = "평가된 감성태그가 없습니다."
        book_level = "-"
        book_klover_list = "등록된 리뷰가 없습니다."
        time.sleep(3)
        
    print(book_review_text)
    print(book_level)
    print(book_klover_list)

    book = {"제목":book_title, "저자":book_writer, "출판사":book_publisher, "출간일":book_date, "ISBN-13":book_isbn, "키워드":book_keyword, "소개":book_detail, "출판사 서평":book_review_pub, "감성 태그":book_review_text, "Klover 평점":book_level, "Klover 리뷰":book_klover_list}
    return book

# 0. 목록:[category_book] 딕셔너리 저장 프로그램 정의하기
def is_list_to_dic(i, category_book):
    category_name = ["유아(0~7세)", "어린이(초등)"]
    dic_key = category_name[i]
    book_dic = {dic_key:category_book}
    return book_dic

if __name__ == '__main__':
    # 1. 크롬 드라이버 설정 및 웹 페이지 열기
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://google.com")
    driver.maximize_window()

    book_info = []
    book_count = 0
    for i in range(2):
        try:
            category_book = []
            # 2. 바코드 텍스트파일 리스트로 변환하는 프로그램 실행하기
            book_barcode = is_book_barcode(i)
            for x in book_barcode:
                book_count += 1
                print(f"===== {book_count} 번째 책 =====")

                # 3. 목록에 있는 도서 페이지 진입하기
                book_link = f"https://product.kyobobook.co.kr/detail/{x}"
                driver.get(book_link)
                time.sleep(3)
            
                # 4. 데이터 크롤링 프로그램 실행하기
                category_book.append(is_book_info())

        # 5. 다양한 이유로 오류가 떴다면, 해당 바코드부터 새로운 파일에 저장한 후 그전까지의 데이터 저장        
        except:
            book_barcode = book_barcode[book_barcode.index(x):]
            category_name = ["유아(0~7세)", "어린이(초등)"]
            with open(f"./{category_name[i]}_2.txt", "w", encoding="UTF-8") as f:
                for barcode in book_barcode:
                    f.write(barcode + "\n")
            
            # 6. 목록:[category_book] 딕셔너리 저장 프로그램 실행하기
            book_info.append(is_list_to_dic(i, category_book))
            break
        
        book_info.append(is_list_to_dic(i, category_book))
    
    print("done")
    driver.quit()

    book_info_dic = {"book_info":book_info}
    # 6. book_info 리스트에 저장한 딕셔너리를 json에 저장하기
    with open("./book_all_info_박수현.json", "a", -1, "utf-8") as file:
        json.dump(book_info_dic, file, indent=4, ensure_ascii=False)