# balance_6

## 1. 앱 만들기
0. crud - setting
1. accounts
2. posts

## 2. accounts
### 1. 회원가입
- forms.py -> fields : username, email, password
### 2. 로그인
### 3. 로그아웃

## 3. posts
### 0. 인덱스 페이지
### 1. 밸런스 게임 생성(create)
0. 모델
- forms.py -> fields : title, select1_content, select2_content
- 관계
    - auth_user_model - select1_user (n:n)
    - auth_user_model - select2_user (n:n)
    - auth_user_model - post_user (1:n)
- models.py -> fields : title, select1_user(ManyToMany), select1_content, select2_user(ManyToMany), select2_content, user(foreign-key)

1. url / views
2. template
### 2. 밸런스 페이지 조회(detail)
1. url / views
2. template
### 3. 밸런스 선택(answer)
1. url / views 
    - 선택지를 한 번 선택하면 취소하거나 다른 선택지를 선택할 수 없다.
    - 각 선택지 버튼에는 선택을 한 유저의 수를 출력한다.
2. template
### 4. 이미지 삽입
### 5. 댓글 기능 구현
### 6. 좋아요 기능 구현
### 7. 팔로우 기능 구현
