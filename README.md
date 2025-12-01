# XS leak site for study 

## 📌 목차
- [SERVERS](#SERVERS)
- [SCENARIO](#SCENARIO)
- [EXPLOIT](#EXPLOIT)
- [LANGUAGES](#LANGUAGES)

---

## SERVERS
#### **victim_server**    
XS leak 취약점이 존재하는 타겟 서버

| route   | 기능             |
| ------- | :--------------: |
| /login  | 로그인 페이지        |
| /save   | DB에 게시글 저장     |
| /iframe | XS_leak 타겟 페이지 |
| /timing | XS_leak 타겟 페이지 |

---

#### **attacker_server**  
XS leak 취약점 익스를 위한 공격자 서버

| route   | 기능                           |
| ------- | :----------------------------: |
| /reset  | 저장했던 flag 초기화                |
| /frame  | frame counting 기반 XS leak 유도 |
| /timing | timing 기반 XS leak 유도         |

---

## SCENARIO
1. victim 서버에서 로그인 (cloud/cloud)
2. /save -> XSS 구문 DB에 저장
3. /iframe -> 저장했던 XSS 구문을 사용 -> attacker 서버 -> XS_leak
4. /timing -> 저장했던 XSS 구문을 사용 -> attacker 서버 -> XS_leak

---

## EXPLOIT
![exploit](https://github.com/user-attachments/assets/765b8dd1-c828-4921-838d-74d4f7d79cc8)

---

## LANGUAGES
Python(Flask), HTML 및 Javascript
