import requests

from constants import appKey, appSecret, accessToken, productSearchKeywordQueryAPI
from util import createAOPSignature

def productSearchKeywordQueryAPIRunner(keyword, beginPage, pageSize, country, **kwargs):

    """
    https://open.1688.com/api/apidocdetail.htm?id=com.alibaba.fenxiao.crossborder:product.search.keywordQuery-1
    Example: print(productSearchKeywordQueryAPIRunner("abcd", "1", "1", "en"))

    :param keyword:
    :param beginPage:
    :param pageSize:
    :param country:
    :param kwargs:
    :return:
    """

    offerQueryParam = kwargs
    offerQueryParam.update({"keyword": keyword, "beginPage": beginPage, "pageSize": pageSize, "country": country})
    offerQueryParam = str(offerQueryParam)

    requestsNoParam = "{}{}".format(productSearchKeywordQueryAPI, appKey)
    headers = {'charset': 'UTF-8'}
    params = {"offerQueryParam": offerQueryParam,
              "access_token": accessToken,
              }

    request = requests.Request('GET', requestsNoParam, params=params, headers=headers)
    prepared_request = request.prepare()
    urlPath = requestsNoParam[requestsNoParam.find("param"):]
    _aop_signature = createAOPSignature(appSecret, urlPath, params)
    prepared_request.url = prepared_request.url + "&" + "_aop_signature=" + _aop_signature
    response = requests.get(prepared_request.url).json()

    return response

def POC():

    keyword = input("输入搜索词条: ")
    beginPage = 1
    pageSize = int(input("输入结果数量: "))
    country = "en"

    return productSearchKeywordQueryAPIRunner(keyword, beginPage, pageSize, country)

print(POC())

