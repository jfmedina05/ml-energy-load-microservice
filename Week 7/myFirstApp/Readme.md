# Week 06 Lab: More on Customizing APIs


**The goals of this lab are:**  
The goals of this lab are 
1) Create relevant endpoints for individualized servers using Swagger Editor
2) Create functions to complement the endpoints
3) Test the service endpoints using the virtual machines on Jetstream2

 
## Remember how to update and test your work on Jetstream2
1. Log into your ACCESS account and pull up your Jetstream2 instance (your virtual machine). 
2. Navigate to your Documents/work directory where you cloned the E222 Student repository and your individual repository.
3. Navigate to your individual Git repository and perform a git pull to update contents.
4. Navigate to the E222 Student repository and perform a git pull to update contents.
5. Copy Week 6 contents from E222 Student to your individual repository.
6. Navigate to your individual repository/Week 6 folder. You should find a folder called myFirstApp, similar to what we had last time.
7. Activate your virtual environment:	source .venv/bin/activate (you may need to create it by typing python3 -m venv ./venv)



## YOUR ENDPOINTS
### For this section, make sure you CHECK THE COMMENTS (in the model.py file) and NOTE changes to the master.yml file! 

### I have also included a data folder to easily keep track of the data files used to test your service. In that folder, you will notice there is a python script that I developed for TESTING your functions BEFORE connecting them to endpoints. I highly recommend doing this - it will eliminate weird errors stemming from mismatched data/model files.

In this section, you will work to create your own endpoints for your service. The goals is to have two – three completed today. Remember that each endpoint needs:

* Properly defined requests in the yml file
* Python scripts to execute the required function
* (Sometimes you need to install more libraries, depending on the scripts you right. If you have to install something new, update the requirements.txt file!)

1.	/model_info endpoint
    * Create a /model_info endpoint in your master.yml file. Use the appropriate syntax. I recommend you doing this in your Swagger Editor and copy/paste your VM master.yml file when complete.
    * You will note there is a model.py file in your src directory. It is UNFINISHED. Complete it with your model specifics.
    * Test your service and your endpoint.
2.	/prediction endpoint
    * Create a /prediction endpoint in your master.yml file. This file should be a POST that allows someone to upload a file to the server (like testdata.csv) and return a list of resulting predictions. Use the appropriate syntax. I recommend you doing this in your Swagger Editor and copy/paste your VM master.yml file when complete.
    * Note there a file_predict function in model.py. It is not finished as it needs YOUR model to be loaded. This means you need to make sure your pkl file is in the same directory (src folder) as this script). Make those updates. 
    * Test your service. Make sure that any installations are updated in your requirements.txt file.
   
3.	/performance endpoint
    * Create a /performance endpoint that provides accuracy or whatever performance metric you used to the user.
    * No function has been created to do this. You will need to either create a new py file OR include it in the model.py script (recommended).
    * Note, you do not have to do it EXACTLY how I did it. I did not specify if it had to be a GET/POST.


