# :rocket: G.Lean :rocket:

>  :memo: [팀문서 바로가기](https://www.notion.so/bff205392c824a1483daded64c6bc6a0)

# 목차

- [서비스 개요](#1-서비스-개요)
- [기능](#2-기능)
- [실행 방법](#3-실행-방법)
- [작업 목록](#4-작업-목록)
- [기술 스택](#5-기술-스택)
- [팀 소개](#6-팀-소개)

## :one: 서비스 개요 :unlock:

> **'우울증 화상상담 서비스'**
>
> 코로나19로 사회적 불안이 증가하며 우울증 환자가 늘어나고 있다. 이러한 사회적 현상을 코로나19와 우울증(blue)가 합쳐진 '코로나블루' 라는 신조어로 명명하고 있다. 소아청소년과는 작년대비 진료수가 36.9% 감소한 반면 정신건강의학과의 진료건수는 작년대비 14% 증가했다. 우울증은 초기에 진료시 완치율이 70~80%로 높기 때문에 이런 사회적 불안감을 해소하고자 서비스를 기획하게 되었다. G.Lean 서비스는 우울증이라는 키워드에 초점을 둔 '우울증 화상상담 서비스'로 우울증 자가진단, 상담사 매칭, 상담일지 작성, 화상상담기능, 가까운 병원 찾기 등의 기능을 제공한다.


## :two: 기능 :pushpin:

[기능명세 바로가기](https://docs.google.com/spreadsheets/d/1EBdgfwf9YY9ZuJqzH5YAIjKZJgPpBEUIhQwHyspVMMM/edit#gid=0)

- 우울증 자가진단 서비스

- 화상상담 서비스

- 랜덤채팅 기능

- 추후 추가예정

## :three: 실행 방법 :computer:

- [프론트]

  1 ) yarn install  
  2 ) yarn serve

- [백엔드]

  1 ) backend 폴더의 디렉토리로 이동  
  2 ) pip install -r requirements.txt 로 필요 라이브러리 설치  
  3 ) python managy.py makemigrations 입력  
  4 ) python managy.py migrate 입력  
  5 ) python managy.py runserver 로 백엔드 서버 실행

## :four: 작업 목록 :pencil:

추후 추가 예정 

## :five: 기술 스택 :game_die:

- 백엔드
  - Python, Django, SQLite
- 프론트엔드
  - HTML, CSS, JS, React, WebRTC, face-api.js

## :six: 팀 소개 :thumbsup:

1. 팀명 : 미정

| 이름   | 역할             | 비고                                                        |
| :----- | ---------------- | ----------------------------------------------------------- |
| 서상원 | 팀장, 백엔드     | 상담일지 암호화, 상담 및 모임 기능 구현                     |
| 박석우 | 백엔드           | 유저, 상담사 모델링 도움받아 작성, 이메일 인증, 자격증 인증 |
| 이창윤 | 프론트엔드       | 메인페이지 디자인 , 회원관리 기능 구현                      | 
| 이태희 | 프론트엔드       | 채팅기능 구현, 상담사 리스트, 상담사 정보, 상담예약, 디자인 |                                                           |
| 차동우 | 서기, 프론트엔드 | 화상상담 페이지, 디자인, 배포, CI/CD, 발표                  |

