# dewApiTrading
dew api trading use python.
## 1.MD5单重签名请求流程示例

    import time
    current_milli_time = lambda: int(round(time.time() * 1000))
    params = {"apiKey":apiKey,"a",a,"b":b,"tonce":str(current_milli_time())} 
    #a,b为业务参数。

### a.参数进行字典排序
    #为java代码，below为python
    #Collection<String> keyset= params.keySet();  
    keyset = params.keys()
    #List<String> list=new ArrayList<String>(keyset); 
    list_keyset = list(keyset)
    #Collections.sort(list);
    list_keyset.sort()
