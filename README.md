## Table of Contents
<!-- no toc -->
- [1. Introduction](#1-introduction)
- [2. Preparing to run the sample scripts](#2-preparing-to-run-the-sample-scripts)
- [3. Sending data via REST API](#3-sending-data-via-rest-api)


## 1. Introduction
This repositoty contains the Python scripts that train a machine learning model and deploy a machine learning system that can be accessed via REST API.


## 2. Running the sample scripts
1. Clone this repository or download the repository as a zip file.
2. If the repository is downloaded as a zip file, extract the zip file into its own folder.
3. Next, open a terminal in the same folder as the extracted Python scripts.
4. Enter the following command to train the model:
   - python train_model.py
5. Launch the API app by entering the following command in the terminal:
   - python api_app.py
6. To stop the API app, press CTRL-c in the terminal.
7. 

## 3. Sending data via REST API
1. Make sure that the API app is running
2. You can run the sample script "restapi_example.py" to send the data via http POST and GET:
   - python restapi_example.py
3. You can also send the data via a web browser by typing the following URL in the address bar:
   - http://127.0.0.1:5000/rest_api?height=160&weight=50
