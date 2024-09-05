import requests
import os

LOCAL = os.getenv("LOCAL")
if LOCAL == "1":
    from alibaba1688api.constants import accessToken, appKey, productSearchKeywordQueryAPI
    from alibaba1688api.constants import productSearchQueryProductDetailAPI, appSecret

from alibaba1688api.util import requestBuilder, parseProductSearchQueryProductDetailSkuInfos, parseProductSearchKeywordQuery

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

    preparedRequestUrl = requestBuilder(params, productSearchKeywordQueryAPI, appKey, appSecret)

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

    preparedRequestUrl = requestBuilder(params, productSearchQueryProductDetailAPI, appKey, appSecret)

    ## Return json
    response = requests.get(preparedRequestUrl).json()

    return response


def returnKeywordAndDetails(keyWord, beginPage, pageSize):
    """
    Function that uses a keyword and params to return a product and skuinfo
    """

    KeywordAndDetails = ""

    productSearchKeywordQueryAPIRunnerResult = productSearchKeywordQueryAPIRunner(keyWord, beginPage, pageSize, "en")
    productSearchKeywordQueryResult = parseProductSearchKeywordQuery(productSearchKeywordQueryAPIRunnerResult)
    productSearchKeywordQueryResult = [productSearchKeywordQueryResult.iloc[[i]] for i in
                                       range(len(productSearchKeywordQueryResult))]

    for eachProductSearchKeywordQueryResult in productSearchKeywordQueryResult:
        productId = str(eachProductSearchKeywordQueryResult.iloc[0]["产品号码"])
        productSearchQueryProductDetailAPIRunnerResult = productSearchQueryProductDetailAPIRunner(productId, "en")
        parseProductSearchQueryProductDetailResult = parseProductSearchQueryProductDetailSkuInfos(
            productSearchQueryProductDetailAPIRunnerResult)

        KeywordAndDetails += "<H3> 名称和编号 </H3>"
        KeywordAndDetails += eachProductSearchKeywordQueryResult.to_html(classes='table table-striped', index=False)
        KeywordAndDetails += "<H3> SKU信息 </H3>"
        KeywordAndDetails += parseProductSearchQueryProductDetailResult
        KeywordAndDetails += """<div style="height: 50px;"></div><hr><div style="height: 50px;"></div>"""

    return KeywordAndDetails
