# Testing details

This section deals the various testing techniques being carried out for this code. It covers the aspect of flexibility being offered by this code too.

## Automated testing

## First step - Test only IBAN validation algorithm

Initially the test is limited to verify the working of validation algorithm for IBAN. The four tests are,   

1. Input for valid IBAN in lower case (ro09bcyp0000001234567890). Expected output: Valid
2. Input for invalid IBAN (RO09 BCYP 0000 0012 3456 7890*00*). Expected output : Invalid.
3. Input for valid IBAN with spaces (RO09 BCYP 0000 0012 3456 7890). Expected output : Valid.
4. Input for valid IBAN without spaces (RO09BCYP0000001234567890). Expected output: Valid.

And the corresponding outputs are,    

```test_Iban_lower_case (__main__.TestIbanValidation_Standalone) ... ok```    
```test_invalidIban (__main__.TestIbanValidation_Standalone) ... ok```    
```test_validIban_with_spaces (__main__.TestIbanValidation_Standalone) ... ok```    
```test_validIban_without_spaces (__main__.TestIbanValidation_Standalone) ... ok```   

Thus this code has additional flexibility to handle IBAN in spaces format too although electronic format of IBAN requires no space. It is insenstive towards lower and upper cases while definining IBAN.

## Second step - Test IBAN validation with respect to web server
As working of validation algorithm for IBAN has been tested, now we need to verify the successfulness in integration of the above algorithm with respect to the web server.
In addition to four tests, one more test for incorrect URL also has been tested.    

For example, if any user types, ```http://localhost:80/**IBAN_VALUE**``` instead of ```http://localhost:80/IBAN/**IBAN_VALUE**```, the code is designed to provide the details of correct URL in the same localhost domain for IBAN validation. The outputs of the testing are,   

```test_Iban_lower_case (__main__.TestIbanValidation_WithWebServer) ... localhost 80 0 SocketKind.SOCK_STREAM 0 0```. ```ok```


```test_IncorrectUrl (__main__.TestIbanValidation_WithWebServer) ... localhost 80 0 SocketKind.SOCK_STREAM 0 0```. ```ok``` 


```test_invalidIban (__main__.TestIbanValidation_WithWebServer) ... localhost 80 0 SocketKind.SOCK_STREAM 0 0```. ```ok``` 


```test_validIban_with_spaces (__main__.TestIbanValidation_WithWebServer) ... localhost 80 0 SocketKind.SOCK_STREAM 0 0```. ```ok```

```test_validIban_without_spaces (__main__.TestIbanValidation_WithWebServer) ... localhost 80 0 SocketKind.SOCK_STREAM 0 0 ```. ```ok```    

## To replicate the testing details
1. Run the webserver in the background using docker container.    
```docker run --rm -d -p 80:80 --name my-docker-instance2 ramedventures/webserver-iban:workingWebserver```

2. Next step is to run the docker container which tests automatically. In case of Ubuntu,   
```docker run --rm -it --network host --name webserver-instance ramedventures/webserver-iban:webserver-iban-test "localhost"```    

3. In case of Mac OS,
``` docker run --rm -it --network host --name webserver-instance ramedventures/webserver-iban:webserver-iban-test "host.docker.internal"```   

4. A successfull tests run with Oks without any error.
