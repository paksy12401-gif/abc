# from flask import Flask,render_template,request, send_file  #requests 랑은 다름 
# from test2 import search_a
# from file import save_to_csv

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return render_template("index.html")

# @app.route("/search")
# def search():
#     keyword = request.args.get("keyword")
#     # print(keyword)
#     jobs = search_a(keyword,1)
    
#     return render_template("search.html",jobs=enumerate(jobs),keyword = keyword)

# # @app.route("/file")
# # def file():
# #     keywords = request.args.get("keyword")
# #     jobs = search_incruit(keywords,1)
# #     save_to_csv(jobs)
# #     print(keywords)
# #     return send_file("downloads.csv",as_attachment=True)
# @app.route("/file")
# def yy():
#     keywords = request.args.get("keyword")
#     jobs = search_a(keywords,1)
#     save_to_csv(jobs)
#     print(keywords)
#     return send_file("downloads.csv",as_attachment=True)

   
# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask
# from flask import render_template
# from flask import request
# from flask import send_file

# from test2 import search_a
# from file import save_to_csv
# from ranking import ranking_products


# app = Flask(__name__)


# # ==============================
# # 메인 페이지
# # ==============================

# @app.route("/")
# def home():

#     return render_template(
#         "index.html"
#     )


# # ==============================
# # 검색 결과 페이지
# # ==============================

# @app.route("/search")
# def search():

#     keyword = request.args.get(
#         "keyword"
#     )

#     products = search_a(
#         keyword,
#         1
#     )

#     return render_template(

#         "search.html",

#         products=enumerate(products),

#         keyword=keyword
#     )


# # ==============================
# # CSV 다운로드
# # ==============================

# from flask import Flask, render_template, request
# from test2 import search_a
# from ranking import ranking_products

# app = Flask(__name__)


# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/search")
# def search():

#     keyword = request.args.get("keyword")

#     products = search_a(keyword, 1)

#     products = ranking_products(products)

#     return render_template(
#         "search.html",
#         products=products,
#         keyword=keyword
#     )


# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, request
# # from test2 import search_a
# from test3 import search_qss

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("index.html")


# @app.route("/search")
# def search():

#     keyword = request.args.get("keyword")

#     # jobs = search_a(keyword, 1)
#     jobs = search_qss(keyword, 1)

#     return render_template(
#         "search.html",
#         products=jobs,
#         keyword=keyword
#     )


# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request

# from test4 import (
#     search_vaidoh,
#     search_qss
# )

# app = Flask(__name__)


# @app.route('/')
# def home():

#     return render_template(
#         "index.html"
#     )


# @app.route("/search")
# def search():

#     keyword = request.args.get(
#         "keyword"
#     )

#     # =========================
#     # 쇼핑몰별 검색
#     # =========================
#     vaidoh_products = search_vaidoh(
#         keyword,
#         1
#     )

#     qss_products = search_qss(
#         keyword,
#         1
#     )

#     # =========================
#     # 합치기
#     # =========================
#     products = (
#         vaidoh_products
#         + qss_products
#     )

#     # =========================
#     # 점수 정렬
#     # =========================
#     products.sort(
#         key=lambda x: x["score"],
#         reverse=True
#     )

#     return render_template(

#         "search.html",

#         products=products,

#         keyword=keyword
#     )


# if __name__ == '__main__':

#     app.run(debug=True)
# from flask import (
#     Flask,
#     render_template,
#     request
# )

# from test4 import (
#     search_vaidoh,
#     search_qss
# )

# app = Flask(__name__)


# # =========================
# # 메인 페이지
# # =========================
# @app.route('/')
# def home():

#     return render_template(
#         "index.html"
#     )


# # =========================
# # 검색
# # =========================
# @app.route("/search")
# def search():

#     keyword = request.args.get(
#         "keyword"
#     )

#     # =========================
#     # 쇼핑몰별 검색
#     # =========================
#     vaidoh_products = search_vaidoh(
#         keyword,
#         1
#     )

#     qss_products = search_qss(
#         keyword,
#         1
#     )

#     # =========================
#     # 상품 합치기
#     # =========================
#     products = (
#         vaidoh_products
#         + qss_products
#     )

#     # =========================
#     # 점수순 정렬
#     # =========================
#     products.sort(

#         key=lambda x: x["score"],

#         reverse=True
#     )

#     # =========================
#     # 결과 페이지
#     # =========================
#     return render_template(

#         "search.html",

#         products=products,

#         keyword=keyword
#     )


# # =========================
# # 실행
# # =========================
# if __name__ == '__main__':

#     app.run(
#         debug=True
#     )
# =========================================
# app.py
# =========================================

from flask import (
    Flask,
    render_template,
    request
)

from test4 import (
    search_vaidoh,
    search_qss
)

from ranking import (
    ranking_products
)

app = Flask(__name__)


# =========================================
# 메인 페이지
# =========================================
@app.route('/')
def home():

    return render_template(
        "index.html"
    )


# =========================================
# 검색
# =========================================
@app.route("/search")
def search():

    keyword = request.args.get(
        "keyword"
    )

    # 사용자 실측 입력
    shoulder = float(
        request.args.get("shoulder")
    )

    chest = float(
        request.args.get("chest")
    )

    length = float(
        request.args.get("length")
    )

    # =====================================
    # 쇼핑몰 검색
    # =====================================
    vaidoh_products = search_vaidoh(
        keyword,
        4
    )

    qss_products = search_qss(
        keyword,
        4
    )

    # 상품 합치기
    products = (
        vaidoh_products
        + qss_products
    )

    # =====================================
    # 랭킹 계산
    # =====================================
    products = ranking_products(

        products,

        shoulder,

        chest,

        length
    )

    # =====================================
    # 결과 페이지
    # =====================================
    return render_template(

        "search.html",

        products=products,

        keyword=keyword
    )


# =========================================
# 실행
# =========================================
if __name__ == '__main__':

    app.run(
        debug=True
    )