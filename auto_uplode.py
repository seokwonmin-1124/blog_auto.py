# lesh
import time
import datetime
from pytz import timezone

time_now = datetime.datetime.now(timezone('Asia/Seoul'))
time_now = str(time_now)
simple_time_now = (time_now)[:16]
print(f"작성 시간 : {simple_time_now}")

html_name = input("html 파일 이름 : ")
wpahr = input("글 제목 : ")
wkrtjdwk = "LESH"  # 작성자
sodyd = input("글 내용 : ")
print(f"글 제목: {wpahr}")
print(f"글 내용: {sodyd}")

html_form = f""" <!-- auto-uploded-by-lesh -->
<!DOCTYPE html>
<html lang="en" class="global-width">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="src/style.css">
    <title>LESH | {wpahr}</title>
</head>
<body>
<div class="wrap">
    <div>
        <header class="page-header">
            <h1 class="content-title">{wpahr}</h1>
                <p class="page-information">
                    <span>{wkrtjdwk} | {simple_time_now}</span>
                    <span>
                        <input type="button" value="라이트 모드" onclick="daynight();" class="daynight">
                        <input type="button" value="다크 모드" onclick="nightday();" class="nightday"
                            style="display: none;">

                    </span>
                </p>
        </header>
        <hr class="title-hr">
        <section class="page-preview">
            <div class="page-content">
                <div class="content-each">
                    <p class="content-body">
                        <span>{sodyd}</span>
                    </p>
                </div> 
            </div>
        </section>
    <footer>
        <hr class="footer-hr">
        <p class="footer-text">
            <div class="other">
            <span onclick="location.href=''" class="blog">Blog</span>
            <span>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;</span>
            <span onclick="location.href='https://github.com/seokwonmin-1124'" class="github">Github</span><br>                
            </div>
            <span>저자: LESH</span><br>
            <span>이메일: seokwonmin@naver.com</span><br>
            <span>Copyright 2022. LESH all rights reserved.</span>
        </p>
    </footer>
    </div>        
</div>
    <script src="src/index.js"></script>
</body>
</html>
"""

html_file = open(f'{html_name}.html', 'w')
html_file.write(html_form)
html_file.close()
