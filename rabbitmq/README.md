# PyRTM Prototype
### Module: Direct
_____
**Main Objectives:**
* RabbitMQ product evaluation in order to replace custom messaging queue technology used by RTM today.
* To learn how product works and what are the main products advantages.
* Technical prototype design definition.
* Must be an abstract solution.

**Tasks**
______
+ Play with RabbitMQ tutorial examples
    + Hello World :
        + Understand how consumer, queue and producer works.
        + RTM scenario:
            + Consumer : agent
            + Producer : rtm-service

            + Consumer : callback
            + Producer : agent

            + channels : mqueue directory
            
    + Work Queue  :  
        + Round-Robin features.
        + Multiple instances for agents,callbacks.

**Problems solved**
____
+ Message hell (lost, server crash, leak, etc).
+ High-avaibility.
+ Product technology upgrade.
+ Message queue decomposition (separate from application server).


**Next Steps**
_____
+ Finish tutorials.
+ Design initial prototype.
    + API.
    + Message document definition.
    + Consumer & producer design.
    + Local Message Storage.
    + Message Object definition (request/response/header - HTTP model).
    ```json
    {
        "request": {
            "header": {
                "type": "direct"
            },
            "body": {},
            "route": {}          
            
        },
        "response": {
            "header": {
                "status_code": []
            },
            "body": {
                "stdout": {},
                "stderr": {}
            }
        }
    }
    ```







