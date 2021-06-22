# CSC-462-Project
Group project for CSC 462, distributed computing course at UVic

### Built with Python, gRPC, rasterio

### Architecture
- Intial tiling of input files is sequential

- Processing of tiles NDVI/NDSI is done in parallel

- Since I didn't set up a distributed file system and shared managed drives that can have more than 2 simultaneous connections are large and expensive I used base64 encoding and decoding to store images inside gRPC messages

- Can run on Azure free Ubuntu VMs but takes over 35 minutes to complete with 1 master, 2 workers and 2 input Sentinel-2 files to calculate NDVI/NDSI

- Currently, processing is done on Arbutus inside Docker containers with 1 master and 2 works but can scale up

### Running the System

- To run with docker: docker-compose up d

- When running in Docker, files are output to a shared volume located in the /Output/processed sub-directory in the main directory

- To run locally first run master from master/master.py then start workers from worker/worker.py

- When running locally files are saved into master/Output/processed directory


#### Notes:
- Requires Python3 and modules grpcio, grpcio-tools, Pillow and rasterio to be installed
- Requires /Output/results directory on machine running worker.py and /Output/processed/ and /Output/tiles1 and /Output/tiles2 directories on machine running master.py
- IP address can be changed from localhost to run on servers, I used internal 10. IP addresses and all my machines were on the same Azure vnet
- worker.py is designed to run continuously requesting tasks, master.py blocks until it is ready to assign and send tasks to the worker
- NotGeoreferencedWarning appears in worker process, this might be an issue with the current tiling function
- Recovering from failures and stalled or stuck workers can be improved 
- Protocol Buffers are compiled with

```python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. dist_processing.proto```

