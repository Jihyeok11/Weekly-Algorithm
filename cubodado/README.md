# cubodado

## 🗓️ week3

### 2022.03.14 - 2022.03.21

### 🏷️ Data Structure

|                   문제 번호                    |          문제 이름          |                            난이도                            |                          문제 풀이                           | 풀이 날짜  |
| :--------------------------------------------: | :-------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :--------: |
|  [1620](https://www.acmicpc.net/problem/1620)  | 나는야 포켓몬 마스터 이다솜 | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [1620.py](https://github.com/cubodado/Weekly-Algorithm/blob/cubodado/cubodado/week3/1620.py) | 2022-03-15 |
| [14425](https://www.acmicpc.net/problem/14425) |         문자열 집합         | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [14425.py](https://github.com/cubodado/Weekly-Algorithm/blob/cubodado/cubodado/week3/14425.py) | 2022-03-15 |
|  [1269](https://www.acmicpc.net/problem/1269)  |         대칭 차집합         | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [1269.py](https://github.com/cubodado/Weekly-Algorithm/blob/cubodado/cubodado/week3/1269.py) | 2022-03-15 |
|  [1927](https://www.acmicpc.net/problem/1927)  |           최소 힙           | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | [1927.py](https://github.com/cubodado/Weekly-Algorithm/blob/cubodado/cubodado/week3/1927.py) | 2022-03-16 |

#### `1620`

* 딕셔너리로 key, value 사용해서 풀었다가 시간 초과
* 그러고 곰곰히 생각해보니 그냥 리스트의 인덱스만 사용해도 되는 문제
* 딕셔너리 전부 없애고 입력값으로 받은 리스트로만 사용하니 통과

#### `1269`

* 이전에 어떤 자료형으로는 빼기 더하기가 가능했던 거 같아서 tuple인가 싶어서 했는데 실패
* 그래서 for문으로 체크해서 하니 시간 초과
* tuple이 아니라 set이었고... set으로 하니 통과

#### `1927`

* [리스트의 min 값 찾기 -> 해당 min 값의 인덱스 찾기 -> 해당 인덱스 리스트에서 pop 하기 -> 리스트 인덱스 재정렬] 순서 거치게 코드 짜니 시간 초과
* heapq 모듈 사용해서 빠르게 사용/통과

## 🗓️ week2

### ~~2022.02.28 - 2022.03.13~~

### 🏷️ Data Structure

|                   문제 번호                    |   문제 이름   |                            난이도                            |                          문제 풀이                           | 풀이 날짜  |
| :--------------------------------------------: | :-----------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :--------: |
|  [4949](https://www.acmicpc.net/problem/4949)  | 균형잡힌 세상 | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [4949.py](https://github.com/cubodado/Weekly-Algorithm/blob/cubodado/cubodado/week2/4949.py) | 2022-03-11 |
|  [3986](https://www.acmicpc.net/problem/3986)  |   좋은 단어   | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [3986.py](https://github.com/cubodado/Weekly-Algorithm/blob/cubodado/cubodado/week2/3986.py) | 2022-03-11 |
| [10799](https://www.acmicpc.net/problem/10799) |   쇠막대기    | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [10799.py](https://github.com/cubodado/Weekly-Algorithm/blob/cubodado/cubodado/week2/10799.py) | 2022-03-11 |
|  [1966](https://www.acmicpc.net/problem/1966)  |   프린터 큐   | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [1966.py](https://github.com/cubodado/Weekly-Algorithm/blob/cubodado/cubodado/week2/1966.py) | 2022-03-11 |
|  [2346](https://www.acmicpc.net/problem/2346)  | 풍선 터뜨리기 | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [2346.py](https://github.com/cubodado/Weekly-Algorithm/commit/e9e3bcb8c8494d1e897c9a7e0438b65d816f871d) | 2022-03-12 |
|  [5397](https://www.acmicpc.net/problem/5397)  |    키로거     | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [5397.py](https://github.com/cubodado/Weekly-Algorithm/commit/7b325615fd274dc842cf635ad6c8975c60e76092) | 2022-03-12 |

#### `4949` 

* for 반복문을 통해 입력값 문자열을 하나씩 돌면서, 괄호에 해당하면 조건문 실행
  * 여는 괄호일 경우 스택에 추가
  * 닫는 괄호일 경우, 스택의 마지막 값과 짝이 맞는 경우에 한해서만 pop
  * 해당하지 않으면 break
* 반복문 수행 후 스택에 값이 남아 있다면 짝이 맞지 않는 것이므로 해당하는 결과값으로 처리

#### `3986`

* while 반복문을 통해 입력값 문자열 확인
  * 시작값과 다음값을 비교해 실행
    * 같지 않은 경우 다시 스택에 시작값과 다음값 추가
    * 같다면 현재 인덱스가 (문자열 길이 - 1) 보다 작고 스택이 비어 있지 않는 경우에 한해, 현재 인덱스의 다음값을 스택에 추가
* 반복문 수행 후 스택에 값이 남아 있다면 짝이 맞지 않는 것이므로 해당하는 결과값으로 처리

#### `10799`

* 스택에 들어 있는 막대 시작의 개수를 이용해, 레이저 조건에 걸리면 해당 스택의 길이로 잘린 개수 추가
* "(" 일 경우 스택에 추가
* ")" 일 경우 막대가 끝나는 것이므로 잘린 개수가 1 더하기, 스택에 들어 있는 막대 시작 pop

#### `1966`

* enumerate 사용해 현재 인덱스와 해당하는 값 쌍으로 만들어 사용
* 시작값 pop, 그 이후 원소들을 반복문 돌며 값 비교
  * 하나라도 중요도가 높은 게 있다면 다시 큐에 추가, break
  * 반복문을 끝까지 돌았다면 중요도가 제일 높으므로 출력 체크 변수에 1 더하기
    * 찾고자 했던 인덱스값에 해당한다면 정답, break

#### `2346`

* enumerate 사용해 현재 인덱스와 해당하는 값 쌍으로 만들어 사용
* 시작값 pop, 인덱스에 1 더해 answer에 정답값 추가
* roate 함수 사용해 값에 해당하는 만큼 배열 위치 이동시키기
* while문 종료 때까지 반복, answer 출력

#### `5397`

> 처음에 시간 초과 걸렸던 문제...😇 

* 왼쪽과 오른쪽 스택을 각각 두어 방향키 변환이 나올 때마다 이 스택들에 있는 값들을 옮기는 식으로 로직 변경

* 기본적으로 왼쪽 스택에 문자열 추가

* ">" 오른쪽으로 커서 이동 시, 오른쪽 스택에 있는 값을 왼쪽 스택에 추가

* "<" 왼쪽으로 커서 이동 시, 왼쪽 스택에 있는 값을 오른쪽 스택에 추가

* 오른쪽 스택은 순서와 반대로 쌓이기 때문에

  Ex) "apple" => [e, l, p, p, a]

  결과값으로 출력할 때는 reversed 해야 함

<br/>

## 🗓️ week1

### ~~2022.02.21 - 2022.02.27~~

### 🏷️ Data Structure

|                   문제 번호                    |                       문제 이름                       |                            난이도                            |                          문제 풀이                           | 풀이 날짜  |
| :--------------------------------------------: | :---------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :--------: |
|  [1158](https://www.acmicpc.net/problem/1158)  | [요세푸스 문제](https://www.acmicpc.net/problem/1158) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | [1158.py](https://github.com/cubodado/Weekly-Algorithm/blob/main/cubodado/week1/1158.py) | 2022-02-21 |
| [18258](https://www.acmicpc.net/problem/18258) |     [큐 2](https://www.acmicpc.net/problem/18258)     | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [18258.py](https://github.com/cubodado/Weekly-Algorithm/blob/main/cubodado/week1/18258.py) | 2022-02-21 |
|  [2164](https://www.acmicpc.net/problem/2164)  |    [카드 2](https://www.acmicpc.net/problem/2164)     | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [2164.py](https://github.com/cubodado/Weekly-Algorithm/blob/main/cubodado/week1/2164.py) | 2022-02-21 |
|  [1874](https://www.acmicpc.net/problem/1874)  |   [스택 수열](https://www.acmicpc.net/problem/1874)   | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [1874.py](https://github.com/cubodado/Weekly-Algorithm/blob/main/cubodado/week1/1874.py) | 2022-02-21 |
| [10828](https://www.acmicpc.net/problem/10828) |     [스택](https://www.acmicpc.net/problem/10828)     | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [10828.py](https://github.com/cubodado/Weekly-Algorithm/blob/main/cubodado/week1/10828.py) | 2022-02-22 |
|  [9012](https://www.acmicpc.net/problem/9012)  |     [괄호](https://www.acmicpc.net/problem/9012)      | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [9012.py](https://github.com/cubodado/Weekly-Algorithm/blob/cubodado/cubodado/week1/9012.py) | 2022-02-22 |
| [10866](https://www.acmicpc.net/problem/10866) |      [덱](https://www.acmicpc.net/problem/10866)      | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [10866.py](https://github.com/cubodado/Weekly-Algorithm/commit/0af75e4078186657fd7a45755dff1be8c0dcda74) | 2022-02-22 |
|  [1935](https://www.acmicpc.net/problem/1935)  | [후위 표기식2](https://www.acmicpc.net/problem/1935)  | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [1935.py](https://github.com/cubodado/Weekly-Algorithm/blob/cubodado/cubodado/week1/1935.py) | 2022-02-24 |



