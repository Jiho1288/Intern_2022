from youtube_transcript_api import YouTubeTranscriptApi              # youtube_transcript_api library import
url = input('자막을 추출할 유튜브 URL입력하세요:').split('=')          # 유튜브 url주소를 입력 받은 후 등호를 기준으로 분리 후 url에 저장
srt = YouTubeTranscriptApi.get_transcript(url[1], languages=['ko'])  # get_transcript 함수를 사용하여 해당 주소의 자막에 관한 데이터를  
                                                                     # 크롤링 해온 후 srt에 저장
with open("subtitles.txt", "w", encoding='utf-8') as f:              # subtitles.txt라는 이름으로 파일 생성 및 인코딩 언어 설정

    for i in range(len(srt)):                                        
        f.write(f"{srt[i]['text']}\n")                               # for문을 이용하여 srt내의 자막만을 text파일에 작성









# 뉴진스 https://www.youtube.com/watch?v=pSUydWEqKwE
