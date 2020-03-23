#### PyRTM
##### Direct Module
____

+ Consumer
    + Server -> Client
    + Client -> Server

+ Producer
    + Server -> Client
    + Client -> Server


#### Steps
____________
+ **Exchange and Queue Setup**
    + Create exchanges, unique queues and binding setup:

    ```bash
        $ python client_setup.py  --agent 12-
        Server to client queue name : amq.gen-0BkL9KkVhptD2Xh1JhJ-sA
        Client to server queue name : amq.gen-iO0aR2fRPppfGOeo3-6gyA    
    ```

    + Start consumers instances (server and client)
        + Remote instance (agent)   
            + python consumer.py --queue amq.gen-0BkL9KkVhptD2Xh1JhJ-sA
        
        + Callback instance (server)
            + python consumer.py --queue amq.gen-iO0aR2fRPppfGOeo3-6gyA

    + Perform consumer smoke test
        + Send a message from server to the client:
        ```bash
            python producer.py --exchange direct.server.client --routing 12
        ```

        + Send a message from the client to the server:
        ```bash
            python producer.py --exchange direct.client.server --routing 12
        ```



+ **Links**
    + https://pypi.org/project/PyInstaller/
    + https://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python
    + https://www.journaldev.com/22513/python-exec
    + https://www.programiz.com/python-programming/methods/built-in/exec
    + https://restrictedpython.readthedocs.io/
    + http://skulpt.org/
    + https://pypi.org/project/django-admin-shell/
    + https://pypi.org/project/python-shell/1.0.0/
    + https://www.edureka.co/community/55115/how-import-json-file-and-encrypt-using-ase-mode-cbc-encryption
    + https://janakiev.com/blog/python-pickle-json/
    + https://www.bogotobogo.com/python/python_serialization_pickle_json.php
    + https://jsonpickle.github.io/