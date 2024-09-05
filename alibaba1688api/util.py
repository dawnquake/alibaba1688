import hashlib
import hmac
import pandas as pd
import requests
import os

LOCAL = os.getenv("LOCAL")
if LOCAL == "1":
    from alibaba1688api.constants import appKey, appSecret

def requestBuilder(params, APIAdress, appKey, appSecret):
    """
    Build request given API address and params

    :param params:
    :param APIAdress:
    :return:
    """

    ## Build request with Params
    requestsNoParam = "{}{}".format(APIAdress, appKey)
    request = requests.Request('GET', requestsNoParam, params=params)
    prepared_request = request.prepare()

    ## Create the aop signature to add
    urlPath = requestsNoParam[requestsNoParam.find("param"):]
    _aop_signature = createAOPSignature(appSecret, urlPath, params)
    prepared_request.url = "{}&_aop_signature={}".format(prepared_request.url, _aop_signature)

    return prepared_request.url


def createAOPSignature(clientSecret, urlPath, params):
    """
    // https://open.1688.com/api/apidoclist.htm?spm=a260s.26059351.0.0.797855edMhEi8W&id=624397
    :param params:
    :return:
    """

    sortedParams = {key: params[key] for key in sorted(params)}
    dataForClientSecret = ''.join([f'{key}{value}' for key, value in sortedParams.items()])
    s = urlPath + dataForClientSecret
    _aop_signature = (hmac.new(clientSecret.encode(), s.encode(),
                               hashlib.sha1).hexdigest()).upper()

    return _aop_signature


def parseProductSearchKeywordQuery(JSONData):
    """
    Function that parses the output from ProductSearchKeywordQuery API and returns pandas DataFrame

    :param JSONData:
    :return:
    """

    productSearchKeywordQueryResultList = []
    if JSONData["result"]["code"] == "200":
        for item in JSONData["result"]["result"]["data"]:
            productSearchKeywordQueryResultList.append({"中文名称": item["subject"],
                                                        "英文名称": item["subjectTrans"],
                                                        "产品号码": item["offerId"]})
        productSearchKeywordQueryResultDf = pd.DataFrame(productSearchKeywordQueryResultList)
        return productSearchKeywordQueryResultDf

    else:
        print("Error code {}".format(JSONData["result"]["code"]))
        raise Exception("Parsing ProductSearchKeywordQuery Failed")


def parseProductSearchQueryProductDetailSkuInfos(JSONData):
    """
    Function that parses the output from ProductSearchQueryProductDetail API and returns pandas DataFrame

    :param JSONData:
    :return:
    """

    productSkuInfosListDict = []
    if JSONData["result"]["code"] == "200":

        if "productSkuInfos" in JSONData["result"]["result"].keys():

            for productSkuInfos in (JSONData["result"]["result"]["productSkuInfos"]):
                productSkuInfosDict = {}

                if "price" in productSkuInfos:
                    productSkuInfosDict["价格"] = productSkuInfos["price"]
                if "skuImageUrl" in productSkuInfos["skuAttributes"][0]:
                    imageUrl = productSkuInfos["skuAttributes"][0]["skuImageUrl"]
                    width = '"150"'
                    productSkuInfosDict["图片链接"] = "<img src={} width={}>".format(imageUrl, width)
                for attr in (productSkuInfos["skuAttributes"]):
                    productSkuInfosDict[attr["attributeName"]] = attr["value"]

                productSkuInfosListDict.append(productSkuInfosDict)

            productSkuInfosDf = pd.DataFrame(productSkuInfosListDict)
            productSkuInfosDfHtml = productSkuInfosDf.to_html(classes='table table-striped', index=False, escape=False)

            return productSkuInfosDfHtml

        else:
            return "<H3> 没有SKU信息 </H3>"


    else:
        print("Error code {}".format(JSONData["result"]["code"]))
        raise Exception("Parsing ProductSearchQueryProductDetail Failed")
