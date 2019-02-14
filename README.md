# dewApiTrading
dew api trading use python.
## 1.MD5单重签名请求流程示例

    import time
    current_milli_time = lambda: int(round(time.time() * 1000))
    params = {"apiKey":apiKey,"a",a,"b":b,"tonce":str(current_milli_time())} 
    #a,b为业务参数。

### a.参数进行字典排序
    #为java代码，
    Collection<String> keyset= params.keySet(); 
    List<String> list=new ArrayList<String>(keyset);  
    Collections.sort(list);
    #以下为python
    keyset = params.keys()
    list_keyset = list(keyset)
    list_keyset.sort()
### b.参数k-v字符串生成
    #以下为java代码
    String signString = "" ;     
    for( String key : list ){
	    String split = "".equals(signString)?"":"&" ;
	    signString += split+ key+"="+params.get(key) ;
    }
    signString = signString+"&secretKey="+apiSecret;    //API_SECRET
    # 以下为python代码
    signString = ""
    for key in list_keyset:
        split = "" if signString == "" else "&"
        signString += split + key + "=" + params.get(key)
    signString = signString+"&secretKey="+apiSecret #API_SECRET


### c.基于UTF-8编码的MD5加密，生成校验字符串sign
    #以下为java代码
    String sign = "";
    try {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] bytes = md.digest(signString.getBytes("utf-8"));
        final char[] HEX_DIGITS = "0123456789abcdef".toCharArray();
	        StringBuilder ret = new StringBuilder(bytes.length * 2);
	        for (int i=0; i<bytes.length; i++) {
		        ret.append(HEX_DIGITS[(bytes[i] >> 4) & 0x0f]);
		        ret.append(HEX_DIGITS[bytes[i] & 0x0f]);
	        }
	        sign =  ret.toString();
    }
    #以下为python代码


        