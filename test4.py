
# import requests
# from bs4 import BeautifulSoup
# import re

# headers = {
#     "User-Agent": "Mozilla/5.0"
# }


# # =========================================
# # 공통 크롤링 함수
# # =========================================
# def crawl_shop(
#     keyword,
#     pages,
#     BASE_URL,
#     item_selector,
#     mall_name
# ):

#     products = []

#     for page in range(1, pages + 1):

#         url = (
#             f"{BASE_URL}/product/search.html?"
#             f"keyword={keyword}&page={page}"
#         )

#         # 목록 요청
#         res = requests.get(
#             url,
#             headers=headers
#         )

#         soup = BeautifulSoup(
#             res.text,
#             "html.parser"
#         )

#         # 상품 리스트
#         items = soup.select(
#             item_selector
#         )

#         if not items:
#             continue

#         # =====================================
#         # 상품 반복
#         # =====================================
#         for item in items:

#             try:

#                 # 상품명
#                 name_tag = item.select_one(
#                     ".name"
#                 )

#                 if not name_tag:
#                     continue

#                 brand_name = (
#                     name_tag.get_text(
#                         strip=True
#                     )
#                 )

#                 # 설명
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

#                 # =================================
#                 # 가격
#                 # =================================
#                 price = 0

#                 for span in item.find_all("span"):

#                     style = span.get(
#                         "style",
#                         ""
#                     )

#                     text = span.get_text(
#                         strip=True
#                     )

#                     # Vaidoh
#                     if (
#                         "#000000" in style
#                         and "원" in text
#                     ):

#                         m = re.search(
#                             r"\d[\d,]*",
#                             text
#                         )

#                         if m:

#                             price = m.group()

#                             break

#                     # QSS
#                     elif (
#                         "원" in text
#                         and "line-through"
#                         not in style
#                     ):

#                         m = re.search(
#                             r"\d[\d,]*",
#                             text
#                         )

#                         if m:

#                             price = m.group()

#                             break

#                 # =================================
#                 # 링크
#                 # =================================
#                 a_tag = item.find("a")

#                 if not a_tag:
#                     continue

#                 href = a_tag.get("href")

#                 if href.startswith("http"):

#                     link = href

#                 else:

#                     link = BASE_URL + href

#                 # =================================
#                 # 이미지
#                 # =================================
#                 img = ""

#                 img_tag = (
#                             item.find("img")
#                      or item.parent.find("img")
#                                 or item.find_previous("img")
#                                             )

#                 if img_tag:

#                     img = (
#                     img_tag.get("src")
#                         or img_tag.get("data-src")
#                         or ""
#                             )

#                 if img.startswith("//"):

#                     img = "https:" + img

#                 elif img.startswith("/"):

#                     img = BASE_URL + img
#                 # =================================
#                 # 상세페이지
#                 # =================================
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

#                 # =================================
#                 # 실측 찾기
#                 # =================================
#                 for line in lines:

#                     line = line.strip()

#                     if (
#                         "어깨" in line
#                         and "가슴" in line
#                         and "총장" in line
#                     ):

#                         # 레글런
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
#                 if shoulder == 0:

#                     continue


#                     # 레글런 제외
#                 if is_raglan:

#                     continue        
#                 # =================================
#                 # 저장
#                 # =================================
#                 products.append({

#                     "mall": mall_name,

#                     "brand_name": brand_name,

#                     "title": title,

#                     "price": price,

#                     "shoulder": shoulder,

#                     "chest": chest,

#                     "length": length,

#                     "raglan": is_raglan,

#                     "link": link,

#                     "image": img
#                 })

#             except Exception as e:

#                 print("error:", e)

#                 continue

#     return products


# # =========================================
# # Vaidoh
# # =========================================
# def search_vaidoh(keyword, pages=1):

#     return crawl_shop(

#         keyword=keyword,

#         pages=pages,

#         BASE_URL="https://vaidoh.com",

#         item_selector="ul.prdList li",

#         mall_name="Vaidoh"
#     )


# # =========================================
# # QSS
# # =========================================
# def search_qss(keyword, pages=1):

#     return crawl_shop(

#         keyword=keyword,

#         pages=pages,

#         BASE_URL="https://qss.seoul.kr",

#         item_selector="ul.prdList > li",

#         mall_name="QSS"
#     )

# import requests
# from bs4 import BeautifulSoup
# import re

# headers = {
#     "User-Agent": "Mozilla/5.0"
# }


# # =========================================
# # 공통 크롤링 함수
# # =========================================
# def crawl_shop(
#     keyword,
#     pages,
#     BASE_URL,
#     item_selector,
#     mall_name
# ):

#     products = []

#     for page in range(1, pages + 1):

#         url = (
#             f"{BASE_URL}/product/search.html?"
#             f"keyword={keyword}&page={page}"
#         )

#         # =================================
#         # 목록 요청
#         # =================================
#         try:

#             res = requests.get(
#                 url,
#                 headers=headers,
#                 timeout=10
#             )

#             if res.status_code != 200:
#                 continue

#             soup = BeautifulSoup(
#                 res.text,
#                 "lxml"
#             )

#         except Exception as e:

#             print("목록 페이지 오류 :", e)

#             continue

#         # 상품 리스트
#         items = soup.select(
#             item_selector
#         )

#         if not items:
#             continue

#         # =====================================
#         # 상품 반복
#         # =====================================
#         for item in items[:20]:

#             try:

#                 # =================================
#                 # 상품명
#                 # =================================
#                 name_tag = item.select_one(
#                     ".name"
#                 )

#                 if not name_tag:
#                     continue

#                 brand_name = (
#                     name_tag.get_text(
#                         strip=True
#                     )
#                 )

#                 # =================================
#                 # 설명
#                 # =================================
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

#                 # =================================
#                 # 가격
#                 # =================================
#                 price = 0

#                 for span in item.find_all("span"):

#                     style = span.get(
#                         "style",
#                         ""
#                     )

#                     text = span.get_text(
#                         strip=True
#                     )

#                     # Vaidoh
#                     if (
#                         "#000000" in style
#                         and "원" in text
#                     ):

#                         m = re.search(
#                             r"\d[\d,]*",
#                             text
#                         )

#                         if m:

#                             price = m.group()

#                             break

#                     # QSS
#                     elif (
#                         "원" in text
#                         and "line-through"
#                         not in style
#                     ):

#                         m = re.search(
#                             r"\d[\d,]*",
#                             text
#                         )

#                         if m:

#                             price = m.group()

#                             break

#                 # =================================
#                 # 링크
#                 # =================================
#                 a_tag = item.find("a")

#                 if not a_tag:
#                     continue

#                 href = a_tag.get("href")

#                 if href.startswith("http"):

#                     link = href

#                 else:

#                     link = BASE_URL + href

#                 # =================================
#                 # 이미지
#                 # =================================
#                 img = ""

#                 img_tag = (
#                     item.find("img")
#                     or item.parent.find("img")
#                     or item.find_previous("img")
#                 )

#                 if img_tag:

#                     img = (
#                         img_tag.get("src")
#                         or img_tag.get("data-src")
#                         or ""
#                     )

#                 if img.startswith("//"):

#                     img = "https:" + img

#                 elif img.startswith("/"):

#                     img = BASE_URL + img

#                 # =================================
#                 # 상세페이지 요청
#                 # =================================
#                 try:

#                     detail = requests.get(
#                         link,
#                         headers=headers,
#                         timeout=10
#                     )

#                     if detail.status_code != 200:
#                         continue

#                     html = detail.text

#                     # HTML 너무 크면 스킵
#                     if len(html) > 3000000:
#                         print("HTML 너무 큼 :", link)
#                         continue

#                     # 빈 HTML 스킵
#                     if not html.strip():
#                         continue

#                     detail_soup = BeautifulSoup(
#                         html,
#                         "lxml"
#                     )

#                 except Exception as e:

#                     print("상세페이지 오류 :", e)

#                     continue

#                 # =================================
#                 # 텍스트 추출
#                 # =================================
#                 text = detail_soup.get_text(
#                     separator="\n",
#                     strip=True
#                 )

#                 lines = text.split("\n")

#                 shoulder = chest = length = 0

#                 is_raglan = False

#                 # =================================
#                 # 실측 찾기
#                 # =================================
#                 for line in lines:

#                     line = line.strip()

#                     if (
#                         "어깨" in line
#                         and "가슴" in line
#                         and "총장" in line
#                     ):

#                         # 레글런
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

#                 # 어깨 없으면 제외
#                 if shoulder == 0:
#                     continue

#                 # 레글런 제외
#                 if is_raglan:
#                     continue

#                 # =================================
#                 # 저장
#                 # =================================
#                 products.append({

#                     "mall": mall_name,

#                     "brand_name": brand_name,

#                     "title": title,

#                     "price": price,

#                     "shoulder": shoulder,

#                     "chest": chest,

#                     "length": length,

#                     "raglan": is_raglan,

#                     "link": link,

#                     "image": img
#                 })

#             except Exception as e:

#                 print("상품 오류 :", e)

#                 continue

#     return products


# # =========================================
# # Vaidoh
# # =========================================
# def search_vaidoh(keyword, pages=1):

#     return crawl_shop(

#         keyword=keyword,

#         pages=pages,

#         BASE_URL="https://vaidoh.com",

#         item_selector="ul.prdList li",

#         mall_name="Vaidoh"
#     )


# # =========================================
# # QSS
# # =========================================
# def search_qss(keyword, pages=1):

#     return crawl_shop(

#         keyword=keyword,

#         pages=pages,

#         BASE_URL="https://qss.seoul.kr",

#         item_selector="ul.prdList > li",

#         mall_name="QSS"
#     )
import requests
from bs4 import BeautifulSoup
import re

# =========================================
# 세션 + 헤더
# =========================================
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/136.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ko-KR,ko;q=0.9,en;q=0.8",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive"
}

session = requests.Session()
session.headers.update(headers)


# =========================================
# 공통 크롤링 함수
# =========================================
def crawl_shop(
    keyword,
    pages,
    BASE_URL,
    item_selector,
    mall_name
):

    products = []

    for page in range(1, pages + 1):

        url = (
            f"{BASE_URL}/product/search.html?"
            f"keyword={keyword}&page={page}"
        )

        # =================================
        # 목록 요청
        # =================================
        try:

            res = session.get(
                url,
                timeout=10
            )

            print("목록 :", url, res.status_code)

            if res.status_code != 200:
                continue

            soup = BeautifulSoup(
                res.text,
                "lxml"
            )

        except Exception as e:

            print("목록 페이지 오류 :", e)

            continue

        # 상품 리스트
        items = soup.select(
            item_selector
        )

        print("상품 개수 :", len(items))

        if not items:
            continue

        # =====================================
        # 상품 반복
        # =====================================
        for item in items[:20]:

            try:

                # =================================
                # 상품명
                # =================================
                name_tag = item.select_one(".name")

                if not name_tag:
                    continue

                brand_name = (
                    name_tag.get_text(strip=True)
                )

                # =================================
                # 설명
                # =================================
                title = ""

                summary = item.find(
                    "li",
                    class_="summary_desc"
                )

                if summary:

                    spans = summary.find_all("span")

                    if len(spans) >= 2:

                        title = (
                            spans[-1]
                            .text
                            .strip()
                        )

                # =================================
                # 가격
                # =================================
                price = 0

                for span in item.find_all("span"):

                    style = span.get(
                        "style",
                        ""
                    )

                    text = span.get_text(
                        strip=True
                    )

                    # Vaidoh
                    if (
                        "#000000" in style
                        and "원" in text
                    ):

                        m = re.search(
                            r"\d[\d,]*",
                            text
                        )

                        if m:

                            price = m.group()

                            break

                    # QSS
                    elif (
                        "원" in text
                        and "line-through"
                        not in style
                    ):

                        m = re.search(
                            r"\d[\d,]*",
                            text
                        )

                        if m:

                            price = m.group()

                            break

                # =================================
                # 링크
                # =================================
                a_tag = item.find("a")

                if not a_tag:
                    continue

                href = a_tag.get("href")

                if href.startswith("http"):

                    link = href

                else:

                    link = BASE_URL + href

                # =================================
                # 이미지
                # =================================
                img = ""

                img_tag = (
                    item.find("img")
                    or item.parent.find("img")
                    or item.find_previous("img")
                )

                if img_tag:

                    img = (
                        img_tag.get("src")
                        or img_tag.get("data-src")
                        or ""
                    )

                if img.startswith("//"):

                    img = "https:" + img

                elif img.startswith("/"):

                    img = BASE_URL + img

                # =================================
                # 상세페이지 요청
                # =================================
                try:

                    detail = session.get(
                        link,
                        timeout=10
                    )

                    print("상세 :", link, detail.status_code)

                    if detail.status_code != 200:
                        continue

                    html = detail.text

                    # HTML 너무 크면 스킵
                    if len(html) > 3000000:
                        print("HTML 너무 큼 :", link)
                        continue

                    # 빈 HTML 스킵
                    if not html.strip():
                        continue

                    detail_soup = BeautifulSoup(
                        html,
                        "lxml"
                    )

                except Exception as e:

                    print("상세페이지 오류 :", e)

                    continue

                # =================================
                # 텍스트 추출
                # =================================
                text = detail_soup.get_text(
                    separator="\n",
                    strip=True
                )

                lines = text.split("\n")

                shoulder = chest = length = 0

                is_raglan = False

                # =================================
                # 실측 찾기
                # =================================
                for line in lines:

                    line = line.strip()

                    if (
                        "어깨" in line
                        and "가슴" in line
                        and "총장" in line
                    ):

                        # 레글런
                        if "레글런" in line:

                            is_raglan = True

                        # 어깨
                        m = re.search(
                            r"어깨\s*(\d+\.?\d*)",
                            line
                        )

                        shoulder = (
                            float(m.group(1))
                            if m else 0
                        )

                        # 가슴
                        m = re.search(
                            r"가슴\s*(\d+\.?\d*)",
                            line
                        )

                        chest = (
                            float(m.group(1))
                            if m else 0
                        )

                        # 총장
                        m = re.search(
                            r"총장\s*(\d+\.?\d*)",
                            line
                        )

                        length = (
                            float(m.group(1))
                            if m else 0
                        )

                        break

                # =================================
                # 조건
                # =================================
                if shoulder == 0:
                    continue

                if is_raglan:
                    continue

                # =================================
                # 저장
                # =================================
                products.append({

                    "mall": mall_name,

                    "brand_name": brand_name,

                    "title": title,

                    "price": price,

                    "shoulder": shoulder,

                    "chest": chest,

                    "length": length,

                    "raglan": is_raglan,

                    "link": link,

                    "image": img
                })

            except Exception as e:

                print("상품 오류 :", e)

                continue

    return products


# =========================================
# Vaidoh
# =========================================
def search_vaidoh(keyword, pages=1):

    return crawl_shop(

        keyword=keyword,

        pages=pages,

        BASE_URL="https://vaidoh.com",

        item_selector="ul.prdList li",

        mall_name="Vaidoh"
    )


# =========================================
# QSS
# =========================================
def search_qss(keyword, pages=1):

    return crawl_shop(

        keyword=keyword,

        pages=pages,

        BASE_URL="https://qss.seoul.kr",

        item_selector="ul.prdList > li",

        mall_name="QSS"
    )