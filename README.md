# Webserver-Iban-Validation
Build a Web server which responds to REST API call in order to validate a given IBAN. To know about IBAN, please refer [here](https://en.wikipedia.org/wiki/International_Bank_Account_Number).  

## Coding test assumption
_You are not allowed to use someone's library_ - It is assumed that only non-standard or external libraries aren't allowed. However inbuilt libraries are permissible.

## Dependencies
* _Docker_ (Version:18.09.02 or later).   


Please ensure that the docker version is at least 18.03+ in order to avoid the issue related to networking in docker. For more details, please refer [here](https://docs.docker.com/docker-for-mac/networking/).   
    
* _Python 3+_, in case to alter / enhance the code in future.    

## Pulling docker image from docker hub
1. If docker is not available, please download docker as per the instructions given [here](https://docs.docker.com/).   
    
2. Login to docker to pull the image.       
```docker login --username=<YOUR_USER_NAME>```  

3. To pull the docker image for webserver,    
```docker pull ramedventures/webserver-iban:workingWebserver```   

4. To pull the docker image of automated testing for webserver,   
```docker pull ramedventures/webserver-iban:webserver-iban-test```  

5. To verify the successful pulling of above two image and make sure that two images are present under _TAG_,    
```docker images```     

6. To run the web server in background,     
```docker run --rm -d --name webserver-instance ramedventures/webserver-iban:workingWebserver```  

7. To connect to webserver via any of the browsers,
```http://localhost:80/IBAN/<IBAN_VALUE>``` 

8. We can also connect to webserver via mac or ubuntu terminal,        
```curl http://localhost:80/IBAN/<IBAN_VALUE>```


## Output details
## Definition   
```GET /IBAN/<VALID_IBAN>``` 

## Response
* 200 ok
* You sent a valid IBAN.

## Definition
```GET /IBAN/<INVALID_IBAN>```

## Response
* 200 ok
* You sent an invalid IBAN.

## Definition
```GET /<Other than IBAN URL>```

## Response
* 200 ok
* In order to validate IBAN, Please type http://localhost:80/IBAN/**IBAN_VALUE**

Note: Since IBAN isn't getting retrieved from database, (as we are validating IBAN), all responses are made to 'ok' with a message.   

## Test details
Testing details for this code can be found [here](https://github.com/Ramakrishnanr/Webserver-Iban-validation/blob/Ramakrishnanr-After-Tests-1/TESTING_DETAILS.md).

