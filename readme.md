

# Asynchronous API requests 
----

### This script is used to test the speed of API request calls asynchronously. 


#### The tests include:
1. 10 API requests
2. 100 API requests
3. 1,000 API requests
4. 10,000 API requests



#### The async API requests are tested against:
- VMware 15 Ubuntu 22.04 image
- localhost server (gunicorn - defaults)
- MySQL database (1 table, 50 inserts, 7 columns)



#### Test results:

1.
![10test](https://user-images.githubusercontent.com/52839097/217370474-33dda992-3a24-49a9-8378-74f51a523c1d.PNG)

2.
![100test](https://user-images.githubusercontent.com/52839097/217370521-40628c48-20cb-4a18-9e1b-b885b3f57071.PNG)

3.
![1000test](https://user-images.githubusercontent.com/52839097/217370570-d0a1b4a2-1e19-45ad-8520-3f93382955bb.PNG)

4.
![10000test](https://user-images.githubusercontent.com/52839097/217370625-ec11cf08-38fd-4a9e-9800-2170e75ddf78.PNG)

---
---

## Hardware resource metrics:

#### Normal load:
![norm_htop](https://user-images.githubusercontent.com/52839097/217370999-c3f275c5-4d8a-45fa-8787-77ea1aa1f050.PNG)


#### Highest test (10,000 requests):
![100000_hi_htop2](https://user-images.githubusercontent.com/52839097/217371784-df3f803a-1d90-4859-83aa-f3ce04230a16.PNG)


