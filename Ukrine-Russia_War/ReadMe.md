# Pytrends API
``` python 
import seaborn as sns 
```
- 구글 api를 활용하여 국가별로 검색 데이터를 가져올 수 있다.
- 키워드 별, 국가 별, 시간대 별로 추출 가능
- 필요한 패키지는 데이터 프레임을 위한 pandas, 현재 날짜를 기준잡기 위한 datetime, 나라별 분류를 위한 iso3166 이렇게 import해야함.


# Seaborn API ([참고](https://datascienceschool.net/01%20python/05.04%20%EC%8B%9C%EB%B3%B8%EC%9D%84%20%EC%82%AC%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%ED%8F%AC%20%EC%8B%9C%EA%B0%81%ED%99%94.html))
``` python 
import seaborn as sns 
```

``` python 
iris = sns.load_dataset("iris")    # 붓꽃 데이터
titanic = sns.load_dataset("titanic")    # 타이타닉호 데이터
tips = sns.load_dataset("tips")    # 팁 데이터
flights = sns.load_dataset("flights")    # 여객운송 데이터
# 예시 데이터 코드
```
- 커널 밀도 그래프를 나타낼 수 있음. 커널밀도는 커널이라는 함수를 겹치는 형태로 히스토그램보다 부드러운 형태를 보여준다.

    ``` python 
    sns.kdeplot(x)
    plt.title("Iris 데이터 중, 꽃잎의 길이에 대한 Kernel Density Plot")
    plt.show()
    ```

- Seaborn의 distplot 명령은 러그와 커널 밀도 표시 기능이 있어서 Matplotlib의 hist 명령보다 많이 사용된다.

    ``` python 
    sns.distplot(x, kde=True, rug=True)
    plt.title("Iris 데이터 중, 꽃잎의 길이에 대한 Dist Plot")
    plt.show()
    ```

# 우크라이나-러시아 전쟁
## 우크라이나는 러시아에게 얼만큼의 손해를 입혔을까?
[데이터 1 (GlobalSecurity.org)](https://www.globalsecurity.org/military/world/russia/army-equipment.htm)
- 전차
    - 2020년 전차 대수는 21,820대. 전차 평균을 가장 많은 T-72L/M으로 잡을 예정.
    - T-72 가격 : $0.5 million in 2011 = 50만달러 (https://en.wikipedia.org/wiki/T-72)
- 장갑차 (장갑수송기)(APC)
    - 가장 많이 쓰이는 수송기는 BTR-152 (총 9900대중 6천대) 가격은 	US$ 39,000.
- 자주포(field artillery)
    - 대부분의 자주포 가격을 아무리 찾아봐도 참고가격이 없음 공개안됨.
    - MSTA-SV 가격이 $3.1M. 약 300만 달러인데 하위버전이 더 많아서 약 $2M으로 추산하겠음 (https://www.deagel.com/Artillery%20Systems/MSTA-S/a000354)
- 다연장로켓(MRL)
    - 현재 러시아에서 가장 많이 쓰는 MRL은 BM-21. 근데 팔린 기록만 있지 얼마에 팔렸는지는 기록이 아예 없다. 근데 자주포보다는 비싸다는 말이 있어서 $2.3M 추산(사실 비슷하게 비교되는 미국의 M270 가격임) (https://armedforces.eu/compare/rocket_artillery_M270_MLRS_vs_BM-21_Grad)

