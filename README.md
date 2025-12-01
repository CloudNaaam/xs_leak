# XS leak 공부를 위해 제작한 실습 사이트

## SERVERS
### victim_server  
XS leak 취약점이 존재하는 타겟 서버

| route   | 기능             |
| ------- | :--------------: |
| /login  | 로그인 페이지        |
| /save   | DB에 게시글 저장     |
| /iframe | XS_leak 타겟 페이지 |
| /timing | XS_leak 타겟 페이지 |

### attacker_server  
XS leak 취약점 익스를 위한 공격자 서버

| route   | 기능                           |
| ------- | :----------------------------: |
| /reset  | 저장했던 flag 초기화                |
| /frame  | frame counting 기반 XS leak 유도 |
| /timing | timing 기반 XS leak 유도         |

## SCENARIO


## EXPLOIT
