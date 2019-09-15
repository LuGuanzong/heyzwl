
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '于千万人之中遇见你所遇见的人，于千万年之中，时间的无涯的荒野里，没有早一步，也没有晚一步，刚巧赶上了，那也没有别的话可说，惟有轻轻地问一声：“噢，你也在这里吗？”'


if __name__ == '__main__':
    app.run()
