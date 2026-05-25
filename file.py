# import csv
# from test2 import search_a
# def save_to_csv(jobs):
#     with open("downloads.csv","w",encoding="utf-8-sig") as file:
#         csv_writer = csv.writer(file)
#         csv_writer.writerow(["No","회사","제목","지역","상세보기 페이지"])
#         for i ,job in enumerate(jobs):
#             csv_writer.writerow([i+1,job["company"],job["title"],job["location"],job["link"]])
# import csv


# def save_to_csv(products):

#     with open(
#         "downloads.csv",
#         "w",
#         encoding="utf-8-sig",
#         newline=""
#     ) as file:

#         csv_writer = csv.writer(file)

#         # 헤더
#         csv_writer.writerow([

#             "No",

#             "브랜드",

#             "가격",

#             "어깨",

#             "가슴",

#             "총장",

#             "링크"
#         ])

#         # 데이터 저장
#         for i, product in enumerate(products):

#             csv_writer.writerow([

#                 i + 1,

#                 product["brand_name"],

#                 product["price"],

#                 product["shoulder"],

#                 product["chest"],

#                 product["length"],

#                 product["link"]
#             ])

import csv

def save_to_csv(products):

    with open(
        "downloads.csv",
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        csv_writer = csv.writer(file)

        # 헤더
        csv_writer.writerow([
            "No",
            "브랜드",
            "가격",
            "어깨",
            "가슴",
            "총장",
            "점수",
            "링크"
        ])

        # 데이터
        for i, product in enumerate(products):

            csv_writer.writerow([

                i + 1,
                product.get("brand_name", ""),
                product.get("price", ""),
                product.get("shoulder", 0),
                product.get("chest", 0),
                product.get("length", 0),
                product.get("score", 0),
                product.get("link", "")
            ])