from util import createAOPSignature


def testCreateAOPSignature():
    clientSecret = "test123"
    urlPath = "param2/1/system/currentTime/1000000"
    params = {"b": "2", "a": "1"}
    _aop_signature = createAOPSignature(clientSecret, urlPath, params)
    expectedAOPSignature = "33E54F4F7B989E3E0E912D3FBD2F1A03CA7CCE88"

    assert _aop_signature == expectedAOPSignature
