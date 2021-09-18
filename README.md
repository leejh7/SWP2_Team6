# Software Project 2

Repository for SWP2 class assignments and code reviews

## Members

20160176 송영진
20181675 이준호
20185290 이하영
20190406 이현지
20191670 조나영
20170228 한윤서

## Guide

1. fork this repository to your own github storage &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(github)

2. clone from your own storage created by fork to your local storage&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(git)

3. config remote storage in the cloned storage&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(git)

4. make a branch for PR(=pull request)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(git)

5. commit & push your assignment code in branch where you made it step4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(git)

6. click 'Compare & pull request' button to approve and merge your proposal&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(github)

7. delete your PR branch&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(git)

8. Synchronize your fork storage (=pull or fetch original storage to your storage)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(git)

9. go back to step4

### More Info

Details of step2

    $ git clone https://github.com/leejh123/SWP2_Team6.git
    $ git remote -v
    origin https://github.com/leejh123/SWP2_Team6.git (fetch)
    origin https://github.com/leejh123/SWP2_Team6.git (push)

    # url must be your fork repository's url

Details of step3

    $ git remote add origin-leejh7 https://github.com/leejh7/SWP2_Team6.git
    $ git remote -v
    origin https://github.com/leejh123/SWP2_Team6.git (fetch)
    origin https://github.com/leejh123/SWP2_Team6.git (push)
    --- above: your remote repository's address
    --- under: origin remote repository's address
    origin-leejh7 https://github.com/leejh7/SWP2_Team6.git (fetch)
    origin-leejh7 https://github.com/leejh7/SWP2_Team6.git (push)

    # url must be original repository's url

Details of step8

    $ git checkout master
    $ git pull origin-leejh7

If you need more info leave a message on kakaotalk.

### Useful Web site

- [Github 외부 저장소 fork, pull request, 동기화 하기](https://brownbears.tistory.com/466)
- [Pull Request 보내는 방법](https://chanhuiseok.github.io/posts/git-3/)
- [생활코딩님의 Visual Studio Code로 다루는 Git](https://www.youtube.com/watch?v=M_0vwGlz5EM&list=PLuHgQVnccGMAQvSVKdXFiOo51HUD8iQQm)
- [생활코딩님의 Github](https://www.youtube.com/watch?v=tocFib6Ytls&list=PLuHgQVnccGMDWjb0TWItMCfDWDs8Y3Oo7)

## Format

ex)
_hw_01.py_

    # 20160176 송영진
    '''
    송영진 학우분의 코드 영역
    '''

    # 20181675 이준호
    '''
    이준호 학우분의 코드 영역
    '''

    # 20185290 이하영
    '''
    이하영 학우분의 코드 영역
    '''

    # 20190406 이현지
    '''
    이현지 학우분의 코드 영역
    '''

    # 20191670 조나영
    '''
    조나영 학우분의 코드 영역
    '''

    # 20170228 한윤서
    '''
    한윤서 학우분의 코드 영역
    '''

Write your code on your own area.

Conflicts of merge can be avoided by not invading other students's code areas.
