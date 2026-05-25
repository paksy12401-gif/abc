# import requests
# from bs4 import BeautifulSoup
# import re

# BASE_URL = "https://qss.seoul.kr"

# headers = {
#     "User-Agent": "Mozilla/5.0"
# }


# def calculate_score(shoulder, chest, length):

#     TARGET_SHOULDER = 54
#     TARGET_CHEST = 58
#     TARGET_LENGTH = 68

#     score = 100

#     if shoulder != 0:
#         score -= abs(shoulder - TARGET_SHOULDER) * 3

#     score -= abs(chest - TARGET_CHEST) * 2
#     score -= abs(length - TARGET_LENGTH) * 2

#     return round(score, 1)


# def search_qss(keyword, pages=1):

#     products = []

#     for page in range(1, pages + 1):

#         url = (
#             f"{BASE_URL}/product/search.html?"
#             f"keyword={keyword}&page={page}"
#         )

#         # =========================
#         # 목록 페이지 요청
#         # =========================
#         res = requests.get(
#             url,
#             headers=headers
#         )

#         soup = BeautifulSoup(
#             res.text,
#             "html.parser"
#         )

#         # 상품 카드
#         items = soup.find_all(
#             "div",
#             class_="description"
#         )

#         if not items:
#             continue

#         # =========================
#         # 상품 반복
#         # =========================
#         for item in items:

#             try:

#                 # =========================
#                 # 상품명
#                 # =========================
#                 name_tag = item.find(
#                     "div",
#                     class_="name"
#                 )

#                 if not name_tag:
#                     continue

#                 brand_name = (
#                     name_tag.text.strip()
#                 )

#                 # =========================
#                 # 상품 설명
#                 # =========================
#                 title = ""

#                 summary = item.find(
#                     "li",
#                     class_="summary_desc"
#                 )

#                 if summary:

#                     spans = summary.find_all(
#                         "span"
#                     )

#                     if len(spans) >= 2:

#                         title = (
#                             spans[-1]
#                             .text
#                             .strip()
#                         )

#                 # =========================
#                 # 가격
#                 # =========================
#                 price = 0

#                 for span in item.find_all("span"):

#                     style = span.get(
#                         "style",
#                         ""
#                     )

#                     text = span.get_text(
#                         strip=True
#                     )

#                     # 할인 가격
#                     if (
#                         "#000000" in style
#                         and "원" in text
#                         and "line-through"
#                         not in style
#                     ):

#                         m = re.search(
#                             r"\d[\d,]*",
#                             text
#                         )

#                         if m:

#                             price = m.group()

#                         break

#                 # =========================
#                 # 링크
#                 # =========================
#                 a_tag = item.find("a")

#                 if not a_tag:
#                     continue

#                 href = a_tag.get("href")

#                 if href.startswith("http"):

#                     link = href

#                 else:

#                     link = BASE_URL + href

#                 # =========================
#                 # 이미지
#                 # =========================
#                 img = ""

#                 img_tag = item.parent.find(
#                     "img"
#                 )

#                 if img_tag:

#                     img = img_tag.get(
#                         "src",
#                         ""
#                     )

#                     if img.startswith("//"):

#                         img = "https:" + img

#                     elif img.startswith("/"):

#                         img = BASE_URL + img

#                 # =========================
#                 # 상세페이지 요청
#                 # =========================
#                 detail = requests.get(
#                     link,
#                     headers=headers
#                 )

#                 detail_soup = BeautifulSoup(
#                     detail.text,
#                     "html.parser"
#                 )

#                 text = detail_soup.get_text(
#                     "\n"
#                 )

#                 lines = text.split("\n")

#                 shoulder = chest = length = 0

#                 is_raglan = False

#                 # =========================
#                 # 실측 찾기
#                 # =========================
#                 for line in lines:

#                     line = line.strip()

#                     if (
#                         "어깨" in line
#                         and "가슴" in line
#                         and "총장" in line
#                     ):

#                         # 레글런 체크
#                         if "레글런" in line:

#                             is_raglan = True

#                         # 어깨
#                         m = re.search(
#                             r"어깨\s*(\d+\.?\d*)",
#                             line
#                         )

#                         shoulder = (
#                             float(m.group(1))
#                             if m else 0
#                         )

#                         # 가슴
#                         m = re.search(
#                             r"가슴\s*(\d+\.?\d*)",
#                             line
#                         )

#                         chest = (
#                             float(m.group(1))
#                             if m else 0
#                         )

#                         # 총장
#                         m = re.search(
#                             r"총장\s*(\d+\.?\d*)",
#                             line
#                         )

#                         length = (
#                             float(m.group(1))
#                             if m else 0
#                         )

#                         break

#                 # =========================
#                 # 점수 계산
#                 # =========================
#                 score = calculate_score(
#                     shoulder,
#                     chest,
#                     length
#                 )

#                 # =========================
#                 # 저장
#                 # =========================
#                 products.append({

#                     "brand_name": brand_name,

#                     "title": title,

#                     "price": price,

#                     "shoulder": shoulder,

#                     "chest": chest,

#                     "length": length,

#                     "score": score,

#                     "raglan": is_raglan,

#                     "link": link,

#                     "image": img
#                 })

#             except Exception as e:

#                 print("error:", e)

#                 continue

#     # =========================
#     # 점수 정렬
#     # =========================
#     products.sort(
#         key=lambda x: x["score"],
#         reverse=True
#     )

#     return products