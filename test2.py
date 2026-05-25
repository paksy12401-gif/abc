# import requests
# from bs4 import BeautifulSoup
# def search_a(keyword,pages):

#     jobs =[]
#     for i in range(pages):
#         page = 1

        
#         url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchword={keyword}&flag=n&searchMode=1&searchType=search&search_done=y&search_optional_item=n&recruitPage={page}&recruitSort=relation&recruitPageCount=40&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n"
#         header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"}
#         response = requests.get(url,headers = header)


#         soup = BeautifulSoup(response.text,"html.parser")

#         lis = soup.find_all("div" , class_ = "item_recruit")
#         # print(len(lis))
#         # print(lis[0])



#         for li in lis :
#             company = li.find("strong", class_="corp_name").find("a").text.strip()
#             title = li.find("h2", class_="job_tit").find("a").find("span").text.strip()
#             location = li.find("div",class_="job_condition").find("a").text.strip()
#             link = "https://www.saramin.co.kr" + li.find("a", class_="track_event data_layer").get("href")
#             job_data = {
#                 "company": company,
#                 "title": title,
#                 "location" : location,
#                 "link" : link
#             }
#             jobs.append(job_data)

#     return jobs


# import requests
# from bs4 import BeautifulSoup
# import re


# BASE_URL = "https://vaidoh.com"

# headers = {
#     "User-Agent": "Mozilla/5.0",
#     "Referer": BASE_URL
# }


# def search_a(keyword, pages=1):

#     products = []

#     for page in range(1, pages + 1):

#         url = f"{BASE_URL}/product/search.html?keyword={keyword}&page={page}"

#         res = requests.get(url, headers=headers)

#         soup = BeautifulSoup(res.text, "html.parser")

#         product_list = soup.select_one("ul.prdList")

#         if not product_list:
#             continue

#         items = product_list.find_all("li")

#         for item in items:

#             try:

#                 # ==============================
#                 # 1. 상품명
#                 # ==============================

#                 name_tag = item.select_one(".name")
#                 if not name_tag:
#                     continue

#                 brand_name = name_tag.get_text(strip=True)

#                 # ==============================
#                 # 2. 가격 (핵심 수정 부분)
#                 #    → #000000 (할인가) 기준
#                 # ==============================

#                 price = "0"

#                 spans = item.find_all("span")

#                 for span in spans:

#                     style = span.get("style", "")
#                     text = span.get_text(strip=True)

#                     if "#000000" in style and "원" in text:

#                         price = re.sub(r"[^\d]", "", text)

#                         break

#                 # ==============================
#                 # 3. 링크
#                 # ==============================

#                 a_tag = item.find("a")
#                 if not a_tag:
#                     continue

#                 link = BASE_URL + a_tag.get("href")

#                 # ==============================
#                 # 4. 상세페이지 (실측)
#                 # ==============================

#                 detail_res = requests.get(link, headers=headers)

#                 detail_soup = BeautifulSoup(
#                     detail_res.text,
#                     "html.parser"
#                 )

#                 text = detail_soup.get_text("\n")
#                 lines = text.split("\n")

#                 shoulder = chest = length = 0

#                 for line in lines:

#                     line = line.strip()

#                     if (("L(" in line or "FREE" in line)and "어깨" in line and "가슴" in line and "총장" in line):

#                         m = re.search(r"어깨\s*(\d+\.?\d*)", line)
#                         shoulder = m.group(1) if m else 0

#                         m = re.search(r"가슴\s*(\d+\.?\d*)", line)
#                         chest = m.group(1) if m else 0

#                         m = re.search(r"총장\s*(\d+\.?\d*)", line)
#                         length = m.group(1) if m else 0

#                         break

#                 # ==============================
#                 # 5. 저장
#                 # ==============================

#                 products.append({

#                     "brand_name": brand_name,
#                     "price": price,
#                     "shoulder": float(shoulder),
#                     "chest": float(chest),
#                     "length": float(length),
#                     "link": link
#                 })

#             except:
#                 continue

#     return products

# import requests
# from bs4 import BeautifulSoup
# import re

# BASE_URL = "https://vaidoh.com"

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


# def search_a(keyword, pages=1):

#     products = []

#     for page in range(1, pages + 1):

#         url = f"{BASE_URL}/product/search.html?keyword={keyword}&page={page}"

#         res = requests.get(url, headers=headers)
#         soup = BeautifulSoup(res.text, "html.parser")
        
#         product_list = soup.select_one("ul.prdList")


#         if not product_list:
#             continue

#         items = product_list.find_all("li")

#         for item in items:

#             try:

#                 # 상품명
#                 name_tag = item.select_one(".name")
#                 if not name_tag:
#                     continue

#                 brand_name = name_tag.get_text(strip=True)

#                 # 가격 (검정색 = 할인)
#                 price = 0

#                 for span in item.find_all("span"):
#                     style = span.get("style", "")
#                     text = span.get_text(strip=True)

#                     if "#000000" in style and "원" in text:
#                         price = re.sub(r"[^\    d]", "", text)
#                         break

#                 # 링크
#                 a_tag = item.find("a")
#                 if not a_tag:
#                     continue

#                 link = BASE_URL + a_tag.get("href")
#                 img = ""
#                 img_tag = item.find("img")

#                 if img_tag:
#                     img = img_tag.get("src")

#                     if img and img.startswith("//"):
#                         img = "https:" + img


#                 # 상세페이지
#                 detail = requests.get(link, headers=headers)
#                 detail_soup = BeautifulSoup(detail.text, "html.parser")

#                 text = detail_soup.get_text("\n")
#                 lines = text.split("\n")

#                 shoulder = chest = length = 0
#                 is_raglan = False

#                 for line in lines:

#                     line = line.strip()

#                     if (("L(" in line or "FREE" in line)and "어깨" in line and "가슴" in line and "총장" in line):

#                         if "레글런" in line:
#                             is_raglan = True

#                         m = re.search(r"어깨\s*(\d+\.?\d*)", line)
#                         shoulder = float(m.group(1)) if m else 0

#                         m = re.search(r"가슴\s*(\d+\.?\d*)", line)
#                         chest = float(m.group(1)) if m else 0

#                         m = re.search(r"총장\s*(\d+\.?\d*)", line)
#                         length = float(m.group(1)) if m else 0

#                         break

#                 # 점수 계산
#                 score = calculate_score(shoulder, chest, length)
#                 if shoulder == 0:
#                     continue
#                 products.append({

#                     "brand_name": brand_name,
#                     "price": price,
#                     "shoulder": shoulder,
#                     "chest": chest,
#                     "length": length,
#                     "score": score,
#                     "raglan": is_raglan,
#                     "link": link,
#                     "image": img 

#                 })
#                 products.sort(key=lambda x: x["score"], reverse=True)

#             except Exception as e:
#                 print("error:", e)
#                 continue

#     return products