# dewApiTrading

dew api trading using python.<br>
欢迎使用 35%佣金返佣链：
https://act.dew.one/borker/index.html?code=69604741<br>
微信联系：313751369<br>
dew 官方聊天室联系：快乐交易或记住是交易全世界

# API请求流程示例
## 1.MD5 单重签名请求流程示例
    #以下为java
    Long current = System.currentTimeMillis();
    Map<String,String> params =  new HashMap<String, String>() ;
    params.put("apiKey", apiKey) ;    // API_KEY
    params.put("a", a);               //业务参数。。。
    params.put("b", b);
    ......
    params.put("tonce", current.toString());
    #以下为python
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

### b.参数 k-v 字符串生成

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

### c.基于 UTF-8 编码的 MD5 加密，生成校验字符串 sign

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
    from hashlib import md5
    sign = ""
    try:
        bytes_signString = bytes(signString,'utf-8')
        digest = md5(bytes_signString).digest()
        HEX_DIGITS = "0123456789abcdef"
        ret = ""
        for item in range(len(bytes_signString)):
            ret = ret + HEX_DIGITS[(bytes_signString[item] >> 4 & 0x0f)]
            ret = ret + HEX_DIGITS[bytes_signString[item] & 0x0f]
        sign = ret

### d. 封装参数发起 POST 请求

    #以下为java代码
    Map<String,String> reqParams =  new HashMap<String, String>() ;
    reqParams.put("apiKey", apiKey) ;    // API_KEY
    reqParams.put("a", a) ;              //业务参数。。。
    reqParams.put("b", b) ;
    ......
    reqParams.put("tonce", current.toString());
    reqParams.put("sign",sign) ;         //MD5签名
    String result = send(url,reqParams, "UTF-8");
    #以下为python代码
    #import requests 暂时不需要这个库，send是自已写的请求函数。
    reqParams = {"apiKey": apiKey,"a":a,"b":b,"tonce":str(current_milli_time()),"sign":sign}
    result = send(url,reqParams,"UTF-8")

## ETH私钥签名请求流程

### a.参数字典排序
    #以下为java
    Long current = System.currentTimeMillis();
    Map<String,String> params =  new HashMap<String, String>() ;
    params.put("apiKey", apiKey) ;    // API_KEY
    params.put("a", a);               //业务参数。。。
    params.put("b", b);
    ......
    params.put("tonce", current.toString());
    Collection<String> keyset= params.keySet();  
    List<String> list=new ArrayList<String>(keyset); 
    Collections.sort(list);
    #以下为python
    import time
    current_milli_time = lambda: int(round(time.time() * 1000))
    params = {"apiKey":apiKey,"a",a,"b":b,"tonce":str(current_milli_time())}
    #a,b为业务参数。
    keyset = params.keys()
    list_keyset = list(keyset)
    list_keyset.sort()

### b.参数字符串生成
    #以下为java
    String signString = "" ;     
    for( String key : list ){
	    String split = "".equals(signString)?"":"&" ;
	    signString += split+ key+"="+params.get(key) ;
    }
    #以下为python
    signString = ""
    for key in list_keyset:
        split = "" if signString == "" else "&"
        signString += split + key + "=" + params.get(key)

### c.基于eth私钥加密，生成私钥加密串，并设置到参数map中
    #以下为java
    String presign = ethSign(password, keystore, signString) ;    //具体方法在后面列出
    param.put("presign", presign);
    #以下为python
    presign = ethSign(password,keystore,signString) #具体方法在后面列出
    params = {"apiKey":apiKey,"a",a,"b":b,"tonce":str(current_milli_time()),"presign":presign}

### d.对照步骤a、b，对param再次进行字典排序并生成字符串
    #以下为java
    Collection<String> keyset1= params.keySet();  
    List<String> list1=new ArrayList<String>(keyset1); 
    Collections.sort(list1); 
    String signString1 = "" ;     
    for( String key : list1 ){
	    String split = "".equals(signString1)?"":"&" ;
	    signString1 += split+ key+"="+params.get(key) ;
    }
    signString1 = signString1+"&secretKey="+apiSecret;   //API_SECRET
    #以下为python
    keyset1 = params.keys()
    list1_keyset = list(keyset1)
    list1_keyset.sort()
    signString1 = ""
    for key in list1_keyset:
        split = "" if signString1 == "" else "&"
        signString1 += split + key + "=" + params.get(key)
    signString1 = signString1+"&secretKey="+apiSecret #API_SECRET

### e.基于UTF-8编码的MD5
    #以下为java
    String sign = "";
    try {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] bytes = md.digest(signString1.getBytes("utf-8"));
        final char[] HEX_DIGITS = "0123456789abcdef".toCharArray();
	    StringBuilder ret = new StringBuilder(bytes.length * 2);
	    for (int i=0; i<bytes.length; i++) {
		ret.append(HEX_DIGITS[(bytes[i] >> 4) & 0x0f]);
		ret.append(HEX_DIGITS[bytes[i] & 0x0f]);
	}
	    sign =  ret.toString();
    }
    #以下为python
    from hashlib import md5
    sign = ""
    try:
        bytes_signString1 = bytes(signString1,'utf-8')
        digest = md5(bytes_signString1).digest()
        HEX_DIGITS = "0123456789abcdef"
        ret = ""
        for item in range(len(bytes_signString1)):
            ret = ret + HEX_DIGITS[(bytes_signString1[item] >> 4 & 0x0f)]
            ret = ret + HEX_DIGITS[bytes_signString1[item] & 0x0f]
        sign = ret
    
### f.封装参数发起POST请求
    #以下为java
    Map<String,String> reqParams =  new HashMap<String, String>() ;
    reqParams.put("apiKey", apiKey) ;    // API_KEY
    reqParams.put("a", a) ;              //业务参数。。。
    reqParams.put("b", b) ; 
    ...... 
    reqParams.put("tonce", current.toString());
    reqParams.put("presign",presign);     //ETH私钥签名 
    reqParams.put("sign",sign) ;          //MD5签名
    String result = send(url,reqParams, "UTF-8");


    // ETH私钥验证，需要用到web3j包
    public  static String  ethSign(String passPhrase,String keystore,String signString){
	try {
		ObjectMapper objectMapper = ObjectMapperFactory.getObjectMapper();
		JsonParser parser = objectMapper.getFactory().createParser(keystore);
		WalletFile walletFile = objectMapper.readValue(parser, WalletFile.class);
		Credentials cred = Credentials.create(Wallet.decrypt(passPhrase, walletFile));
		ECKeyPair ecKeyPair = cred.getEcKeyPair() ;
		SignatureData sd = Sign.signMessage( signString.getBytes() , ecKeyPair ) ;
		byte[] bytes = new byte[1+32+32];
		bytes[0] = sd.getV();
		System.arraycopy( sd.getR() , 0, bytes, 1, 32);
		System.arraycopy(sd.getS(), 0, bytes, 33, 32);
		String sign = Hex.toHexString(bytes);
		return sign ;
	} catch (IOException e) {
		e.printStackTrace();
	} catch (CipherException e) {
		e.printStackTrace();
	}
	return null ;
    }

    // 发起HTTP POST请求
    public static String send(String url, Map<String, String> map, String encoding){
		String body = "";
		CloseableHttpResponse response = null;
		try {
			CloseableHttpClient client = HttpClients.createDefault();
			HttpPost httpPost = new HttpPost(url);
			List<NameValuePair> nvps = new ArrayList<NameValuePair>();
			if (map != null) {
				for (Entry<String, String> entry : map.entrySet()) {
					nvps.add(new BasicNameValuePair(entry.getKey(), entry.getValue()));
				}
			}
			httpPost.setEntity(new UrlEncodedFormEntity(nvps, encoding));
			httpPost.setHeader("Content-type", "application/x-www-form-urlencoded");
			httpPost.setHeader("User-Agent", "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt)");

			response = client.execute(httpPost);
			HttpEntity entity = response.getEntity();
			if (entity != null) {
				body = EntityUtils.toString(entity, encoding);
			}
			EntityUtils.consume(entity);
		} catch (IOException e) {

		} finally {
			if (response != null) {
				try {
					response.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		return body;
    }  
    #以下为python
    reqParams = {"apiKey":apiKey,"a":a,"b":b,"tonce":str(current_milli_time()),"presign":presign,"sign":sign}
    result = send(url,reqParams,"UTF-8")
    
    #// ETH私钥验证，需要用到web3.py包
    from web3 import Web3,HTTPProvider
    import web3
    def ethSign(passPhrase,keystore,signString):
        
