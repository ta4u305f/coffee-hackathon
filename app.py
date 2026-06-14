from flask import Flask, request, render_template_string
from db_roaster import RosterDBManager

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>ホームページ</h1>
    <p>'<a href="/test">登録する</a>'</p>
    <p>'<a href="/mypage">マイページを確認する</a>'</p>
"""

@app.route("/test", methods=["GET", "POST"])
def test():
    rdbm = RosterDBManager()
    if request.method == "POST":
        rdbm.create_user(request.form.to_dict())


    html_form = """
    <html>
        <form action="/test" method="post">
            <div>
                <label for="company_name">会社名</label>
                <input type="text" id="company_name" name="company_name" required>
            </div>
            <div>
                <label for="company_name_kana">会社名（かな）</label>
                <input type="text" id="company_name_kana" name="company_name_kana" required>
            </div>
            <div>
                <label for="contact_name">担当者名</label>
                <input type="text" id="contact_name" name="contact_name" required>
            </div>
            <div>
                <label for="address">住所</label>
                <textarea id="address" name="address" required></textarea>
            </div>
            <div>
                <label for="phone_number">電話番号</label>
                <input type="tel" id="phone_number" name="phone_number" required>
            </div>
            <div>
                <label for="email">メール</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div>
                <label for="prefecture">都道府県</label>
                    <select name="prefecture", id="prefecture" name="prefecture" required>
                    <option value="" selected>選択してください</option>
                    <option value="北海道">北海道</option>
                    <option value="青森県">青森県</option>
                    <option value="岩手県">岩手県</option>
                    <option value="宮城県">宮城県</option>
                    <option value="秋田県">秋田県</option>
                    <option value="山形県">山形県</option>
                    <option value="福島県">福島県</option>
                    <option value="茨城県">茨城県</option>
                    <option value="栃木県">栃木県</option>
                    <option value="群馬県">群馬県</option>
                    <option value="埼玉県">埼玉県</option>
                    <option value="千葉県">千葉県</option>
                    <option value="東京都">東京都</option>
                    <option value="神奈川県">神奈川県</option>
                    <option value="新潟県">新潟県</option>
                    <option value="富山県">富山県</option>
                    <option value="石川県">石川県</option>
                    <option value="福井県">福井県</option>
                    <option value="山梨県">山梨県</option>
                    <option value="長野県">長野県</option>
                    <option value="岐阜県">岐阜県</option>
                    <option value="静岡県">静岡県</option>
                    <option value="愛知県">愛知県</option>
                    <option value="三重県">三重県</option>
                    <option value="滋賀県">滋賀県</option>
                    <option value="京都府">京都府</option>
                    <option value="大阪府">大阪府</option>
                    <option value="兵庫県">兵庫県</option>
                    <option value="奈良県">奈良県</option>
                    <option value="和歌山県">和歌山県</option>
                    <option value="鳥取県">鳥取県</option>
                    <option value="島根県">島根県</option>
                    <option value="岡山県">岡山県</option>
                    <option value="広島県">広島県</option>
                    <option value="山口県">山口県</option>
                    <option value="徳島県">徳島県</option>
                    <option value="香川県">香川県</option>
                    <option value="愛媛県">愛媛県</option>
                    <option value="高知県">高知県</option>
                    <option value="福岡県">福岡県</option>
                    <option value="佐賀県">佐賀県</option>
                    <option value="長崎県">長崎県</option>
                    <option value="熊本県">熊本県</option>
                    <option value="大分県">大分県</option>
                    <option value="宮崎県">宮崎県</option>
                    <option value="鹿児島県">鹿児島県</option>
                    <option value="沖縄県">沖縄県</option>
                </select>
            </div>
            <input type="submit" value="送信する">
        </form>
    </html>
    """
    return html_form

@app.route("/mypage")
def mypage():
    rdbm = RosterDBManager()
    mydata: dict[str, str] = rdbm.get_all_user()[-1]

    html_mypage = """
    <!DOCTYPE html>
    <html lang="ja">
        <head>
          <meta charset="UTF-8">
          <title>マイページ</title>
        </head>
        <body>
          <h1>マイページ</h1>

          <p>[会社名]: {{ user["company_name"] }}</p>
          <p>[会社名（かな）]: {{ user["company_name_kana"] }}</p>
          <p>[担当者名]: {{ user["contact_name"] }}</p>
          <p>[住所]: {{ user["address"] }}</p>
          <p>[電話番号]: {{ user["phone_number"] }}</p>
          <p>[メール]: {{ user["email"] }}</p>
          <p>[都道府県]: {{ user["prefecture"] }}</p>
          <p>[商品名]: {{ "表示したかったです。" }}</p>
          <p>[部門]: {{ "表示したかったです。" }}</p>

          <p>
            <a href="/">メール確認ページに戻る</a>
          </p>
        </body>
    </html>
    """
    return render_template_string(html_mypage, user=mydata)
