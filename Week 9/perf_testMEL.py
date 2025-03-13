import requests         # for sending HTTP requests
import time             # for timing
import os               # for local path management

# file to upload
dir_path = os.getcwd()
filename = 'my_testdata.csv'
file_path = os.path.join(dir_path, filename)        

# service hosted ip
#http://149.165.155.241:8080/e222/
HOST_IP = "149.165.155.241"

# get the total number of requests
n_requests = int(input("Number of requests: "))

# upload_file takes in teh local filepath, the url for the appropriate endpoint
# and the filename which is a required  query parameter for the endpoint.
# The local file will be opened, the filename will be stored (dict formate) as
# a query parameter, and POST request will be issued sending params and files.
def upload_file(file_path, url, filename):
    try:
        files = {'file': open(file_path, 'rb')}
        query_params = {'filename': filename}
        response = requests.post(url, files=files, params=query_params)
        if response.status_code == 200:
            print("File uploaded successfully.")
        else:
            print("Error uploading file. Status code:", response.status_code)
            print("Response text:", response.text)  # Print response text for debugging
    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("An error occurred:", e)

#MAIN
# check if input is valid
if n_requests < 1:
    print("Please enter a valid number of requests.")
    exit(1)

# start the timer
start_time = time.time()

# send the specified number of requests
for i in range(0, n_requests):
    #Test the performance for just returning my model info
    response = requests.get('http://' + HOST_IP + ':8080/e222/model_info')
    
    #After, uploading a dataset, test the performance of my model to provide predictions only
    #response = requests.get('http://149.165.155.241:8080/e222/prediction?filename=my_testdata.csv')
    
    #Test the performance of the upload/predict operation
    #url = 'http://149.165.155.241:8080/e222/prediction'
    #headers = {'accept': '*/*', 'Content-Type': 'multipart/form-data'}
    #files = {'file': ('my_testdata.csv', open('myFirstApp/my_testdata.csv', 'rb'), 'text/csv')}
    #response = requests.post(url, headers=headers, files=files)

   
       
    
    
   
# get the final time 
end_time = time.time()

# calculate total run time
total_run_time = end_time - start_time

# calculate the avg run time
avg_run_time = total_run_time/n_requests

# print the results
print("Number of requests: ", n_requests)
print("Total run time: {}s ".format(total_run_time))
print("Average run time (per request): {}s".format(avg_run_time))

