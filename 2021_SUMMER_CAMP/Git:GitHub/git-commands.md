# 깃 필수 명령어

### git init
> git init

로컬 폴더(Working Directory)에 깃을 적용시키는 명령어입니다. 즉 특정 폴더 내에 git init 명령어를 입력한다는 건 앞으로 해당 폴더 내 파일의 변화를 git이 기록할 수 있음을 의미합니다.

### git add

> git add [file path]

> git add .

커밋(의미있는 변화의 덩어리, 하나의 버전을 의미하기도 함)을 위해 파일들의 변화를 스테이지 공간으로 옮기는 명령어입니다. 즉 커밋에 포함시키고 싶은 변화가 있는 파일들을 고르는 명령어입니다. 명령어 뒤에 파일들의 디렉토리 경로를 넣어줄 경우 해당 파일들만을, 명령어 뒤에 . 만을 찍어줄 경우 로컬 폴더(Working Directory) 전체를 선택합니다.

### git remote add
> git remote add origin [Repository URL]

로컬 폴더(Working Directory)와 깃헙의 Repository를 연결하는 명령어입니다.
remote add 뒤의 origin은 레포지토리의 닉네임으로, 굳이 origin이라고 표기할 필요는 없습니다. 다만 다양한 레포지토리에 커밋할 경우 닉네임이 헷갈리므로 origin으로 통일하여 사용하는 것을 추천합니다.

### git commit
>git commit -m "[커밋 관련 설명]"

Staging 영역에 있는 파일 변화들을 묶어주는 명령어입니다. 하나의 커밋으로 묶인 변화들은 push(Repository에 적용)과정을 거치고 나면 하나의 버전이 됩니다. m은 메시지의 약자로, -m 뒤의 큰 따옴표 안에는 커밋에 관련한 짧은 설명을 적어주시면 됩니다.

### git push
>git push origin master

의미있는 변화들의 묶음인 커밋을 Repository에 적용하는 명령어입니다. 다만 협업의 경우 대참사가 일어날 수 있으니 push 하기 전에 꼭 한번씩 커밋 내용을 확인(git status)해보는 습관을 들이도록 합시다.

### git pull
>git pull origin master

>git pull [Repository URL]

레포지토리의 버전(커밋)을 로컬 폴더(Working Directory)에 적용해주는 명령어입니다. 보통 상대방이 커밋하여 내 로컬 폴더의 버전이 구버전이 되었을 경우 로컬 폴더 파일들을 업데이트 해주기 위해 사용합니다.

### git clone
>git clone [Repository URL]

공개된 원격 저장소를 로컬 컴퓨터에 다운로드 하는 명령어입니다. 말 그대로 모든 코드와 소스가 저장되는 Clone입니다.
혹시 만들어둔 폴더 내에 Clone 받기를 희망하는 경우 레포지토리 URL 뒤에 .을 찍어주면 됩니다. git clone [Repository URL] . 이렇게요.

### git status
> git status

레포지토리의 상태를 보여주는 명령어입니다. 현재 브랜치, 원격 브랜치, 현재 추적 중인 파일, 변경된 파일 목록 등이 표시됩니다.