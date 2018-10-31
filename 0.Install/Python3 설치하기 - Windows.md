# **Python3 설치하기 - Windows**

## 1. 내 시스템 확인하기.

윈도우에는 두가지 아키텍쳐 32비트와 64비트가 존재합니다. 어떤 아키텍처에서 작동하는 지 확인하기 위해서 

1. 윈도우 버튼 -> Computer 마우스 우 클릭
   ![computer_prop](/Users/grace/Documents/TA/python_database_class/misc/resource/computer_prop.jpg)
2. 속성 화면에서 시스템 타입 확인
   ![system_type](/Users/grace/Documents/TA/python_database_class/misc/resource/system_type.jpg)

## 2. Anaconda 설치

파이썬을 설치하게 되면 파이썬 패키지 관리가 어렵고 여러가지 다양한 추가 도구를 설치해야 하기 때문에 배포판으로 설치하는 하는 것이 좋다. 배포판에는 패키지 관리 시스템, 콘솔 등을 포함하고 있다. 다양한 배포판 중에 아나콘다를 설치하도록 하겠다.

1. https://www.anaconda.com/download/에서 -> windows 용 찾기 -> 다운로드
  ![image-20181031235747129](/Users/grace/Documents/TA/python_database_class/misc/resource/image-20181031235747129.png)

2. 다운로드 받은 exe 파일을 실행 -> 전체 설정은 디폴트 값으로 진행해도 무방하다.
   ![image-20181101001406240](/Users/grace/Documents/TA/python_database_class/misc/resource/image-20181101001406240.png)

   ![image-20181101001445572](/Users/grace/Documents/TA/python_database_class/misc/resource/image-20181101001445572.png)


   Microsoft Visual Studio Code는 설치할 필요가 없다.

   ![image-20181101002138424](/Users/grace/Documents/TA/python_database_class/misc/resource/image-20181101002138424.png)

3. 원도우 버튼 -> 아나콘다3 폴더 선택 -> Anaconda Prompt를 실행한다.

   ![image-20181101002557355](/Users/grace/Library/Application Support/typora-user-images/image-20181101002557355.png)

4. 실행된 콘솔 창에 python을 입력하여 정상적으로 파이썬 인터프리터가 실행되는 것을 확인한다.
   파이썬을 종료하려면 exit() 명령을 실행한다.
   ![image-20181101003055937](/Users/grace/Documents/TA/python_database_class/misc/resource/image-20181101003055937.png)

5. 윈도우 버튼 -> 아나콘다3 폴더 선택 -> Jupyter Notebook을 실행한다.
   실행 시 웹서버 프로세스가 실행되는 콘솔 창이 실행되고 동시에 http://localhost:8888/tree 주소로 웹 브라우저가 가동된다. 
   웹서버 프로세스가 돌아가는 콘솔 창을 닫으며 주피터 노트북 웹서버가 중지되므로 주피터 노트북 사용이 끝날 때까지 콘솔 창을 닫으면 안된다.
   ![image-20181101003355114](/Users/grace/Documents/TA/python_database_class/misc/resource/image-20181101003355114.png)





참고자료 : https://datascienceschool.net/view-notebook/5e52b7c4b5754f2585844c8d9b26cdb5/

