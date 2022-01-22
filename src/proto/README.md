
## How to compile these proto files into python code
```shell
cd ${your PROJECT path}/src/proto

python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. *.proto
```