import requests
import json
from logging import basicConfig, getLogger, DEBUG

logger = getLogger(__name__)

class Client():

    def __init__(self, url, contract_id, access_token):
        self.url = url
        self.contract_id = contract_id
        self.access_token = access_token


    def _postAPI(self, data):
        logger.debug(data)
        return requests.post(self.url,
                            headers={
                                "X_contract_id": self.contract_id,
                                "X_access_token": self.access_token,
                                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
                            },
                            data=data)

    def _post_ref(self, proc_name, params):
        return self._postAPI(
         {"proc_name" : proc_name, "params" : json.dumps(params)}
        )

    def get_category(self, fields=["categoryId","categoryName"], conditions=None, order=None, limit=10, page=None, table_name="Category" ):
        """
        処理名 部門情報参照
        処理名(物理名) category_ref
        説明 部門情報を参照する。
        """
        params = {
                "fields":fields,
                "conditions":conditions,
                "order":order,
                "limit":limit,
                "page":page,
                "table_name":table_name
            }
        params = {k:v for k,v in params.items() if v}
        return self._post_ref("category_ref",params)

    def get_product(self, fields=["productId","productName"], conditions=None, order=None, limit=10, page=None, table_name="Product"):
        """
        処理名 商品情報参照
        処理名(物理名) product_ref
        説明 商品情報を参照する。
        """
        params = {
                "fields":fields,
                "conditions":conditions,
                "order":order,
                "limit":limit,
                "page":page,
                "table_name":table_name
            }
        params = {k:v for k,v in params.items() if v}
        return self._post_ref("product_ref",params)

    def get_customer(self, fields=["customerId","customerNo"], conditions=None, order=None, limit=10, page=None, table_name="Customer"):
        """
        処理名 会員情報参照
        処理名(物理名) customer_ref
        説明 会員情報を参照する。
        """
        params = {
                "fields":fields,
                "conditions":conditions,
                "order":order,
                "limit":limit,
                "page":page,
                "table_name":table_name
            }
        params = {k:v for k,v in params.items() if v}
        return self._post_ref("customer_ref",params)

    def get_stock(self, fields=["storeId","productId"], conditions=None, order=None, limit=10, page=None, table_name="Stock"):
        """
        処理名 在庫情報参照
        処理名(物理名) stock_ref
        説明 在庫情報を参照する。
        """
        params = {
                "fields":fields,
                "conditions":conditions,
                "order":order,
                "limit":limit,
                "page":page,
                "table_name":table_name
            }
        params = {k:v for k,v in params.items() if v}
        return self._post_ref("stock_ref",params)

    def get_transaction(self, fields=["transactionHeadId","updDateTime"], conditions=None, order=None, limit=10, page=None, table_name="TransactionHead"):
        """
        処理名 在庫情報参照
        処理名(物理名) transaction_ref
        説明 在庫情報を参照する。
        """
        params = {
                "fields":fields,
                "conditions":conditions,
                "order":order,
                "limit":limit,
                "page":page,
                "table_name":table_name
            }
        params = {k:v for k,v in params.items() if v}
        return self._post_ref("transaction_ref",params)

    def get_store(self, fields=["storeId","storeName"], conditions=None, order=None, limit=10, page=None, table_name="Store"):
        """
        処理名 店舗情報参照
        処理名(物理名) store_ref
        説明 店舗情報を参照する。
        """
        params = {
                "fields":fields,
                "conditions":conditions,
                "order":order,
                "limit":limit,
                "page":page,
                "table_name":table_name
            }
        params = {k:v for k,v in params.items() if v}
        return self._post_ref("store_ref",params)

    def get_daily_sum(self, fields=["sumDate","salesTotal"], conditions=None, order=None, limit=10, page=None, table_name="DailySum"):
        """
        処理名 日次締め情報参照
        処理名(物理名) daily_sum_ref
        説明 日次締め情報を参照する。
        """
        params = {
                "fields":fields,
                "conditions":conditions,
                "order":order,
                "limit":limit,
                "page":page,
                "table_name":table_name
            }
        params = {k:v for k,v in params.items() if v}
        return self._post_ref("daily_sum_ref",params)

    def get_bargain(self, fields=["bargainId","bargainName"], conditions=None, order=None, limit=10, page=None, table_name="Bargain"):
        """
        処理名 セール情報参照
        処理名(物理名) bargain_ref
        説明 セール情報を参照する。
        """
        params = {
                "fields":fields,
                "conditions":conditions,
                "order":order,
                "limit":limit,
                "page":page,
                "table_name":table_name
            }
        params = {k:v for k,v in params.items() if v}
        return self._post_ref("bargain_ref",params)

if __name__ == "__main__":

    basicConfig(
        format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s'
        )
    logger.setLevel(DEBUG)

    f = open("config.json", encoding="utf-8")
    config = json.load(f)
    f.close()
    url = config["smaregi"]["url"]
    contract_id = config["smaregi"]["contract_id"]
    access_token = config["smaregi"]["access_token"]
    c = Client(url, contract_id, access_token)
    logger.debug(f"url :{url}, contract_id :{contract_id}, access_token:{access_token}")
    logger.debug(c.get_category().json())
    logger.debug(c.get_product().json())
    logger.debug(c.get_customer().json())
    logger.debug(c.get_stock().json())
    logger.debug(c.get_transaction().json())
    logger.debug(c.get_store().json())
    logger.debug(c.get_daily_sum().json())
    logger.debug(c.get_bargain().json())
