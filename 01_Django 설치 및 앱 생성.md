# Django 설치 및 앱 생성

<br />
<br />
<br />

## [1] Django 설치

1. Pycharm 앱 실행

2. ```DjangoCRUD```이름의 새로운 프로젝트 생성

3. 터미널에서 아래 코드 실행

   - ```pip install django```

   - ```django-admin startproject crud .```

   - ```python manage.py runserver```

     

     ```
     (venv) ➜  Django pip install django
     Collecting django
       Using cached https://files.pythonhosted.org/packages/b1/1d/2476110614367adfb079a9bc718621f9fc8351e9214e1750cae1832d4090/Django-2.2.1-py3-none-any.whl
     
     # 현재 디렉토리에 crud란 이름의 django 설치
     (venv) ➜  Django django-admin startproject crud .
     
     # 서버 실행
     (venv) ➜  Django python manage.py runserver
     
     Watching for file changes with StatReloader
     Performing system checks...
     
     System check identified no issues (0 silenced).
     
     You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
     Run 'python manage.py migrate' to apply them.
     
     June 03, 2019 - 06:56:50
     Django version 2.2.1, using settings 'intro.settings'
     Starting development server at http://127.0.0.1:8000/
     Quit the server with CONTROL-C.
     [03/Jun/2019 06:56:52] "GET / HTTP/1.1" 200 16348
     [03/Jun/2019 06:56:52] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
     Not Found: /robots.txt
     [03/Jun/2019 06:56:52] "GET /robots.txt HTTP/1.1" 404 1968
     [03/Jun/2019 06:56:52] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
     [03/Jun/2019 06:56:52] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
     [03/Jun/2019 06:56:52] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
     Not Found: /favicon.ico
     [03/Jun/2019 06:56:53] "GET /favicon.ico HTTP/1.1" 404 1971
     ```

   - 서버가 실행되면 인터넷 브라우저에서 아래와 같은 화면이 뜬다.
     <img width="1123" alt="Screen Shot 2019-06-03 at 16 03 44" src="https://user-images.githubusercontent.com/46523571/58782318-356ab200-8619-11e9-9110-9862f14ac2b3.png">

<br>
<br>
<br>

## [2] .gitignore 파일 생성

1. DjangoCRUD 프로젝트에서 ```.gitignore``` 이름의 새로운 파일 생성
2. ```https://www.gitignore.io/``` 접속해서 아래와 같이 추가한 후 Create 버튼 클릭
   <img width="953" alt="Screen Shot 2019-06-03 at 16 08 26" src="https://user-images.githubusercontent.com/46523571/58782680-2cc6ab80-861a-11e9-955d-6aa0275ff0f0.png">
3. 생성된 코드를 ```.gitignore```파일에 붙여넣은 후 저장하기

<br>
<br>
<br>

## [3] boards 새로운 앱 생성

- boards란 이름으로 앱을 하나 생성하겠다 라는 의미

  - 터미널 실행
  - ```python manage.py startapp boards```

- 하나의 앱을 만들고 나면 반드시 해야할 게 있다.

  - boards 폴더 settings.py 코드 수정

  - ```python
    INSTALLED_APPS = [
        # Local apps
        'boards.apps.BoardsConfig',  # boards 폴더 - apps.py 
        															 - class BoardsConfig(AppConfig): 값을 의미
    
        # Django apps
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

  - boards 폴더 settings.py 코드 수정

    ```python
    (기존)
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    
    (변경)
    LANGUAGE_CODE = 'ko-kr'
    TIME_ZONE = 'Asia/Seoul'
    ```

  -  (참고) boards 폴더 settings.py 코드

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            # 위의 sqlite3 뿐만 아니라, 아래와 같이 다른 sql도 사용 가능하다.
            # 'ENGINE': 'django.db.backends.postgresql',
            # 'ENGINE': 'django.db.backends.mysql',
            # 'ENGINE': 'django.db.backends.oracle',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    ```

