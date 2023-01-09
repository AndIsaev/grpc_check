# grpc_check

### run server:

``````
python3 simple_server.py
``````

### generate protofiles:

``````
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/server.proto
``````