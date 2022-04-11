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

[데이터 2 Wikipedia - List of equipment of the Russian Ground Forces](https://en.wikipedia.org/wiki/List_of_equipment_of_the_Russian_Ground_Forces)

[데이터 3 Wikipedia - List of active Russian military aircraft](https://en.wikipedia.org/wiki/List_of_active_Russian_military_aircraft) 
- 육군 (Russian Ground Forces)
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
    - 기동차량(military auto)
        - 러시아의 주 모델은 tigr. 약 6만달러 추정 (https://en.wikipedia.org/wiki/Tigr_(Russian_military_vehicle))
    - anti-aircraft (대공방어포)
        - 러시아의 주력 모델은 S-300 family. 시리아에 팔렸을 때를 추산하면 시스템만 $115M 이며 미사일만 해도 $1M이 넘는다고 함 (https://defense-update.com/20130518_how-dangerous-is-the-s-300.html)
    - 단거리 탄도미사일(mobile SRBM Short-range tactical ballistic missile)
        - 주력 모델은 2006년 생산된 9K720 Iskander-M. 혹은 SS-26임. 아르메니아에서 ss-26을 구매할 때 추산했던 금액이 1대당 약 $16M~25M 정도. 중간값인 20M으로 잡겠음 (https://www.aravot-en.am/2016/09/27/181582/)
    - fuel tank, special equipment, drone은 추산하기 너무 어려운 점이 있고 편제를 가르기 애매하기 때문에 제외하겠음.
- 공군
    - 전투기(Aircraft)는 한 항목으로 통합이 되어있어서, 우크라이나는 공격의 대상이고 주로 요격하는 대상은 전투기 혹은 다목적 전투기일 확률이 높으므로 두 카테고리의 최빈값의 중간값으로 정하겠음.
        - 다목적 전투기에서 가장 많은 종류는 Su-27과 MiG-29. Su-30 가격은 1대당 약 $40M (https://en.wikipedia.org/wiki/Sukhoi_Su-30#India) Su-27의 가격은 $37M (https://aerocorner.com/aircraft/sukhoi-su-27/) MiG-29의 가격은 $5~8M임. 가장 많이 있는 3대의 전투기 평균값은 $23.88M.
        - 전투기에서 Su-24는 약 $24M. Su-25는 $11M이다. 평균값은 $18.63M
        - 두 카테고리의 중간값은 $21.43M (그냥 전체 전투기 값 더하고 숫자 나눴음)
    - 헬리콥터는 Mi-8 / Mi-17이 주로 사용됨. Mi-8은 $9M, 17은 인도에게 2008년 계약 채결 당시 대당 $16.7M정도에 계약된듯 하다 (https://www.helicopterspecs.com/2019/09/mil-mi-8-hip.html) 중간값인 $12.8M으로 계산하겠음.
- 해군
    - 뒤져본 결과 3월 24일 격침시킨 사라토프, 오르스크의 종류는 앨리게이터급 상륙함임. 2020년 건조된 프로젝트23900 상륙작전함의 건설비용 $688M (https://en.wikipedia.org/wiki/Project_23900_amphibious_assault_ship). 그 전에 건조됐으므로 $600M 급으로 생각 하겠음.