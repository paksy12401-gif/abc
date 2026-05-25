# TARGET = {

#     "shoulder": 55,

#     "chest": 58,

#     "length": 70
# }


# # =========================================
# # 점수 계산
# # =========================================

# def ranking_products(products):

#     TARGET = {
#         "shoulder": 52,
#         "chest": 58,
#         "length": 68
#     }

#     def score(p):

#         s = 100

#         s -= abs(p["shoulder"] - TARGET["shoulder"]) * 3
#         s -= abs(p["chest"] - TARGET["chest"]) * 2
#         s -= abs(p["length"] - TARGET["length"]) * 2

#         return round(s, 1)

#     for p in products:
#         p["score"] = score(p)

#     products = sorted(products, key=lambda x: x["score"], reverse=True)

#     for i, p in enumerate(products):
#         p["rank"] = i + 1

#     return products
# =========================================
# ranking.py
# =========================================


# =========================================
# 점수 계산 + 정렬
# =========================================
def ranking_products(

    products,

    shoulder,

    chest,

    length
):

    TARGET = {

        "shoulder": shoulder,

        "chest": chest,

        "length": length
    }

    # =====================================
    # 점수 계산 함수
    # =====================================
    def score(p):

        s = 100

        # 어깨 차이
        s -= abs(

            p["shoulder"]

            - TARGET["shoulder"]

        ) * 3

        # 가슴 차이
        s -= abs(

            p["chest"]

            - TARGET["chest"]

        ) * 2

        # 총장 차이
        s -= abs(

            p["length"]

            - TARGET["length"]

        ) * 2

        return round(s, 1)

    # =====================================
    # 상품별 점수 저장
    # =====================================
    for p in products:

        p["score"] = score(p)

    # =====================================
    # 점수순 정렬
    # =====================================
    products = sorted(

        products,

        key=lambda x: x["score"],

        reverse=True
    )

    # =====================================
    # 순위 추가
    # =====================================
    for i, p in enumerate(products):

        p["rank"] = i + 1

    return products