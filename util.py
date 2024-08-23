import hashlib
import hmac


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
