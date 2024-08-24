import requests
from util import requestBuilder
try:
    from constants import accessToken, productSearchKeywordQueryAPI, productSearchQueryProductDetailAPI
except:
    pass


def productSearchKeywordQueryAPIRunner(keyword, beginPage, pageSize, country, **kwargs):

    """
    Use the
    https://open.1688.com/api/apidocdetail.htm?id=com.alibaba.fenxiao.crossborder:product.search.keywordQuery-1
    Example: print(productSearchKeywordQueryAPIRunner("abcd", "1", "1", "en"))

    :param keyword:
    :param beginPage:
    :param pageSize:
    :param country:
    :param kwargs:
    :return: response
    """

    ## Prepare Params
    offerQueryParam = {"keyword": keyword,
                       "beginPage": beginPage,
                       "pageSize": pageSize,
                       "country": country}
    offerQueryParam.update(kwargs)
    offerQueryParam = str(offerQueryParam)
    params = {"offerQueryParam": offerQueryParam,
              "access_token": accessToken}

    preparedRequestUrl = requestBuilder(params, productSearchKeywordQueryAPI)

    print(preparedRequestUrl)

    ## Return json
    response = requests.get(preparedRequestUrl).json()

    return response

def productSearchQueryProductDetailAPIRunner(offerId, country, **kwargs):

    """
    https://open.1688.com/api/apidocdetail.htm?id=com.alibaba.fenxiao.crossborder:product.search.queryProductDetail-1
    Example: print(productSearchKeywordQueryAPIRunner("623787624244", "en"))

    :param offerId:
    :param country:
    :param kwargs:
    :return: response
    """

    ## Prepare Params
    offerDetailParam = {"offerId": offerId,
                        "country": country}
    offerDetailParam.update(kwargs)
    offerDetailParam = str(offerDetailParam)
    params = {"offerDetailParam": offerDetailParam,
              "access_token": accessToken,
              }

    preparedRequestUrl = requestBuilder(params, productSearchQueryProductDetailAPI)

    ## Return json
    response = requests.get(preparedRequestUrl).json()

    return response




def POC():

    jsonResponse = productSearchKeywordQueryAPIRunner("abc", "1", "10", "en")

    print(jsonResponse)

    input("按任意键退出")


POC()