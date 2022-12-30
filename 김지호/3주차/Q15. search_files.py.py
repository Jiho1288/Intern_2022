"""
-----------------  Question  -----------------
A라는 디렉토리 하위에 있는 텍스트 파일(*.txt) 중에서
LIFE IS TOO SHORT 라는 문자열을 포함하고 있는 파일들을
모두 찾을 수 있는 프로그램을 작성하시오.
단, 하위 디렉토리도 포함해서 검색해야 함.
----------------------------------------------
"""
"""
=============================================================================
과제 1. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'폴더 내에 있는
        3개의 파일명을 프린트해주는 프로그램을 작성하시오.
        - 출력되어야 하는 파일명(순서무관) : Dock_form.docx, HWP_form.hwp, TXT_form.txt
=============================================================================
"""
print("=====과제1=====")
import os                                               # 운영 체제 제어 모듈 import

file_path = os.chdir('../DATA/Q1. finding_files')       # 파일위치 변경
name = os.listdir(file_path)                            # 현재 디렉토리의 파일과 폴더 목록을 name 변수에 대입
file_list = []                                          # file_list = 파일 이름만 추가할 빈 리스트


for i in name:                                        
        if '.' in i:                                    # 반복문을 통하여 만약 파일이라면, file_list에 추가
                file_list.append(i)

print(', '.join(file_list))                             # file_list 출력
print()
   
"""
=============================================================================
과제 2. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'와 
       그 하위 폴더 내에 존재하는 모든 파일을 출력해주는 프로그램을 작성하시오.
       - 출력되어야 하는 파일명 : Docx_form.docx, HWP_form.hwp, TXT_form.txt, JI_FILE_1.txt, JI_FILE_2.hwp, JI_FILE_3.docx,
         (순서무관)             KANG_FILE_1.docx, KANG_FILE_2.txt, KANG_FILE_3.hwp, LEE_FILE_1.docx, LEE_FILE_2.hwp, LEE_FILE_3.txt,
                               [FINAL] JI_FILE_1.docx, [FINAL] JI_FILE_2.hwp, [FINAL] JI_FILE_3.txt, [FINAL] KANG_FILE_1.docx, [FINAL] KANG_FILE_2.hwp, 
                               [FINAL] KANG_FILE_3.txt, [FINAL] LEE_FILE_1.docx, [FINAL] LEE_FILE_2.hwp, [FINAL] LEE_FILE_3.txt
=============================================================================
"""

print("=====과제2=====")

import os                                               # 운영 체제 제어 모듈 import

file_path = os.chdir('../../DATA/Q1. finding_files')    # 현재 파일위치 변경
name = os.listdir(file_path)                            # name 변수에 현재 디렉토리의 파일과 폴더 목록 생성
file_list = []                                          # 파일 이름을 저장할 빈 리스트 생성

for i in name:                                          # name 내에서 반복문을 생성하고
        if '.' in i:                                    # 만약 파일이라면, file_list에 추가
                file_list.append(i)

        else:                                           # 폴더라면 name2에 폴더를 넣기 
                name2 = os.listdir(os.chdir('./' + i))
                for j in name2:                         # name2에서 name 과 마찬가지로 파일과 폴더 분류 후 파일이름을 저장  
                        if '.' in j:
                                file_list.append(j)

                        else:                           
                                name3 = os.listdir(os.chdir('./' + j))
                                for x in name3:         # name3를 전부 file_list에 추가
                                        file_list.append(x)
                                os.chdir('../../')      # 상위의 상위로 디렉토리 변경

print(', '.join(file_list))                             # file_list 출력
print()

"""
=============================================================================
과제 3. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'와 
       그 하위 폴더 내에 존재하는 모든 파일 중에서 확장자가 .txt인 파일의 이름을 출력해주는 프로그램을 작성하시오.  
       - 출력되어야 하는 파일명 : JI_FILE_1.txt, [FINAL] JI_FILE_3.txt, KANG_FILE_2.txt, [FINAL] KANG_FILE_3.txt, 
         (순서무관)             LEE_FILE_3.txt, [FINAL] LEE_FILE_3.txt, TXT_form.txt
=============================================================================
"""

print("=====과제3=====")

import os                                               

file_path = os.chdir('../../DATA/Q1. finding_files')    
name = os.listdir(file_path)                       
file_list = []                                          


for i in name:                                     
        if '.txt' in i:                                 # 과제 2와 같고 텍스트 파일만 리스트에 추가하는 조건문으로 변경
                file_list.append(i)

        elif '.' not in i:                              
                name2 = os.listdir(os.chdir('./' + i))
                for j in name2:                     
                        if '.txt' in j:\
                                file_list.append(j)

                        elif '.' not in j:              
                                name3 = os.listdir(os.chdir('./' + j))
                                for x in name3:
                                        if '.txt' in x:
                                                file_list.append(x)
                                os.chdir('../../')      

print(', '.join(file_list))                             
print()

"""
=============================================================================
과제 4. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'에 존재하는 .txt파일 중에서    (하위 폴더 포함) 
       내용에 'life is too short'이 포함되는 경우, 그 파일명을 출력해주는 프로그램을 작성하시오.
        - 출력되어야 하는 파일명 : JI_FILE_1.txt, [FINAL] JI_FILE_3.txt(순서무관)           
=============================================================================
"""

print("=====과제4=====")

import os                                               

file_path = os.chdir('../../DATA/Q1. finding_files')   
name = os.listdir(file_path)                        
file_list = []                                         


for i in name:                                     
        if '.txt' in i:                                 
                file = open(i, 'r')
                txt = file.read()                        
                if 'life is too short' in txt:          # 과제 3에서 'life is too short'문구가 txt에 들어있는지에 대한 
                        file_list.append(i)             # file_list에 추가
                        

        elif '.' not in i:                              
                name2 = os.listdir(os.chdir('./' + i))
                for j in name2:                     
                        if '.txt' in j:
                                file = open(j, 'r')
                                txt = file.read()
                                if 'life is too short' in txt:
                                        file_list.append(j)
                                os.chdir('../')         
                                
                        elif '.' not in j:              
                                name3 = os.listdir(os.chdir('./' + j))
                                for x in name3:
                                        if '.txt' in x:
                                                file = open(x, 'r')
                                                txt = file.read()
                                                if 'life is too short' in txt:
                                                        file_list.append(x)
                                os.chdir('../')         

print(', '.join(file_list))                             