## Fcoin 交易平台自动化交易脚本

由于大多数”交易即挖矿”的交易平台是根据账户交易所产生的手续费用来分配相关的代币，交易资金是否需要跨平台对于挖矿本身来说影响不是很大，在此先在Fcoin交易所实验相关的可行性。

### 前期准备工作

#### 准备相关的虚拟资产

由于Fcoins目前还不支持C2C，必须要提前准备好相关的虚拟币，通过充值相关的虚拟币的方式来给账户充值。我目前使用的是ETH+imToken的方式来给Fcoins账户充值的。

#### 准备相关的api.key 和api.secret
在平台的账户下面可以找到API相关的参数。

#### 准备相关的软件环境
1. 安装相关的SDK。（pip install fcoin）
2. 修改相关的库文件
```
由于Fcoins平台还不是很完善，SDK相关API有错误，相关的API文档的例子不可用。https://developer.fcoin.com/zh.html 下面如果不修改，不影响脚本的运行。
/usr/local/lib/python2.7/dist-packages/fcoin/dataapi.py
113     def list_orders(self, **payload):
114         """get orders"""
115         #return self.signed_request(GET,'orders', **payload)
116         return self.signed_request(GET, self.http_orders, **payload)
117 
118 
119     def create_order(self, **payload):
120         """create order"""
121         #return self.signed_request(POST,'orders', **payload)
122         return self.signed_request(POST, self.http_orders, **payload)
```
### 脚本的使用

```
目前脚本直接交易的是ETH<-->FT。获取的是平台目前的最新价格，根据最新的价格来下单，每次交易五个FT。
python fcoinTx.py api.key api.secret number
number 代表来回买卖一次FT。
```