# grpc_check

### run server:

``````
docker-compose up --build
``````

### generate protofiles:

``````
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/server.proto
``````