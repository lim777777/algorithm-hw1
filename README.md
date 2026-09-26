# 정렬 알고리즘 비교 과제

삽입 정렬, 병합 정렬, 힙 정렬을 Python으로 구현하고 비교하는 과제 저장소입니다.
힙 정렬은 수업에서 배우지 않은 정렬로 선택했습니다.

이 저장소는 2026-2 **고급알고리즘**(SIT2001-01)의 실습 환경 template에서
시작했습니다.

- 측정 원본: [`report/results.csv`](report/results.csv)

- 강의 자료: [lec-algorithm.github.io/lecture](https://lec-algorithm.github.io/lecture/)
- 강의 예제 코드: [lec-algorithm/algorithm-code](https://github.com/lec-algorithm/algorithm-code)
- 시각화 자료: [lec-algorithm/algorithm-viz](https://github.com/lec-algorithm/algorithm-viz)

## 언제 쓰나

이 저장소는 **새 저장소의 출발점**입니다. 상단의 **Use this template**을 눌러
자기 계정에 사본을 만들고 거기서 작업하세요.

- **과제**를 낼 때
- **개인프로젝트**를 시작할 때 (수업계획서상 GitHub 저장소 제출이 필수입니다)
- 알고리즘 코드를 돌려 볼 환경이 필요할 때

수업에서 다루는 예제 코드는 여기가 아니라 `algorithm-code`에 있습니다.
그쪽은 매주 새 주제가 추가되므로, 복사하지 말고 저장소에서 바로 Codespace를
만들거나 클론해서 `git pull`로 받으세요.

## 준비물

**GitHub 계정 하나면 됩니다.** 로컬에서 돌리려면 Git과 Docker가 필요합니다.
Python은 컨테이너 이미지 안에 들어 있어 따로 설치하지 않습니다.

## 시작하기 (권장): Codespaces

1. 이 저장소 상단의 **Use this template** → **Create a new repository**
2. 저장소 이름을 정합니다 (예: `algorithms-hw1`, `my-algorithm-project`)
3. 만들어진 **내 저장소**에서 **Code** → **Codespaces** 탭
4. **Create codespace on main**

잠시 기다리면 브라우저에 VS Code가 뜹니다. **그 터미널이 곧 컨테이너 안**이므로
바로 아래 [돌려보기](#돌려보기)로 넘어가면 됩니다.

## 로컬에서 하기

위와 같이 **내 저장소를 먼저 만든 뒤** 그것을 클론합니다.

```sh
git clone https://github.com/<본인 계정>/<내 저장소>.git
cd <내 저장소>
docker compose up -d
docker compose exec lab bash
```

처음 한 번은 이미지를 받느라 몇 분 걸립니다. 이후에는 몇 초면 뜹니다.
**이후 모든 `docker compose` 명령은 이 폴더에서 칩니다.**

VS Code를 쓴다면 Dev Containers 확장의 **Reopen in Container**를 골라도
됩니다. Codespaces와 같은 설정을 씁니다.

## 돌려보기

컨테이너 안에서 `make` 한 단어면 됩니다.

- 실행

```sh
make run
```

- 결과

```console
insertion_sort: 1 2 3 4 5 6 7 8 9 10
merge_sort    : 1 2 3 4 5 6 7 8 9 10
heap_sort     : 1 2 3 4 5 6 7 8 9 10
```

세 구현이 모두 같은 정렬 결과를 냅니다.

## 테스트

- 실행

```sh
make test
```

- 결과

```console
test_sorting_cases (test_sort.TestSortingAlgorithms.test_sorting_cases) ... ok

OK
```

테스트가 하나라도 실패하면 `make`가 0이 아닌 코드로 끝납니다. 과제를 내기
전에 이 명령이 통과하는지 확인하세요.

| 명령 | 하는 일 |
| --- | --- |
| `make run` | Python 예제 실행 |
| `make test` | Python 유닛 테스트 |
| `make bench` | Python 구현을 측정해 `report/results.csv` 생성 |
| `make charts` | 측정 결과에서 SVG 그래프 생성 |
| `make clean` | 빌드 산출물 정리 |

## VS Code에서 실행·디버그

Codespaces나 Dev Containers로 열었다면 편집기에서 바로 됩니다.

| 하고 싶은 것 | 방법 |
| --- | --- |
| 파일 하나 실행 | 편집기 오른쪽 위 **▶ 버튼** (Code Runner) |
| 전체 실행 | `Cmd/Ctrl + Shift + B` (기본 빌드 작업이 `make run`) |
| 테스트 | 명령 팔레트 → **Tasks: Run Test Task** |
| Python 디버그 | `F5` → **Python 디버그 (현재 파일)** |

`F5`로 현재 Python 파일에 중단점을 걸고 변수를 확인할 수 있습니다.

### ▶ 버튼에 대해

편집기 오른쪽 위의 ▶ 버튼은 Code Runner 확장이 제공합니다. Python 파일은
`python3`로 실행되며 출력은 통합 터미널에 표시됩니다.


## 저장소 구조

```plaintext
algorithm-hw1/
├── .devcontainer/devcontainer.json  # Codespaces · Dev Containers 설정
├── compose.yml                      # 실습 컨테이너 (서비스 이름: lab)
├── Dockerfile                       # Python · git 실행 환경
├── .vscode/                         # 빌드·디버그 설정 (F5, Cmd+Shift+B)
├── Makefile                         # run · test · bench · charts
├── report/                          # 보고서 · 측정값 · 그래프
├── tools/                           # 성능 측정기 · 그래프 생성기
├── src/
│   ├── sort.py                      # 세 정렬 구현
│   └── main.py                      # 실행 예제
└── tests/
    └── test_sort.py                 # 단위 테스트
```

## 규약

- 외부 라이브러리 없이 Python 표준 라이브러리만 사용합니다.
- 함수 이름은 snake_case(`heap_sort`)를 사용합니다.

## 변경 기록

버전과 변경 내역은 [CHANGELOG.md](CHANGELOG.md)에 있습니다.

## 정리

```sh
docker compose down
```

컨테이너를 지워도 코드는 그대로 남습니다.
