# 노래 일기

코인 노래방에 가는 것을 좋아해서 시작하게된 프로젝트.<br/>
먼저 오늘 자기가 노래방에서 불렀던 노래를 버튼 하나로 추가한다. 사용자는
해당 기록을 바탕으로 자신만의 노래 일기를 작성할 수 있다.<br/>
1. 카카오 로그인 api를 활용한 sns형식의 어플리케이션
2. 목록을 관리함으로써 선곡에 도움이 될 수 있다.<br/>
=> 오늘 부를만한 노래를 추천하는 것까지 바라볼 수 있다.
3. playStore 출시를 목표로 한다.

프론트엔드 : react.js<br/>
백엔드 : django<br/><br/>
Demo: http://music-diary.surge.sh<br/>

## 빌드 과정
0. develop 브랜치 커밋
1. aws 브랜치에서 develop 커밋을 cherry-pick
2. 추가된 모듈 있으면 requirements.txt에 추가
3. DEBUG=False로 변경
4. git commit
5. git push and pull
6. aws에서 디버깅

## Remote 저장소 관리
- Repository를 develop과 production으로 분리해서 push한다