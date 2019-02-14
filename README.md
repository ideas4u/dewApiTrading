# dewApiTrading
dew api trading use python.
## 1.MD5单重签名请求流程

    import time
    current_milli_time = lambda: int(round(time.time() * 1000))
    params = {"apiKey":apiKey,"a",a,"b":b,"tonce":str(current_milli_time())} 

### a.参数进行字典排序
    Collection<String> keyset= params.keySet();  
    List<String> list=new ArrayList<String>(keyset); 
    Collections.sort(list);
