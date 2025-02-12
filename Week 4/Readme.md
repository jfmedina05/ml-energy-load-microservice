# Week 04 Lab: Defining APIs with OpenAPI 3.0 Spec  

## So far, we have done the following in previous labs:

1) ID data: done

2) Select a model [Sci-kit Docs](https://scikit-learn.org/stable/index.html)

3) Train/Build the model

4) Serialize the model

5) Documented all preprocessing and pipeline steps


**In this lab you will:** learn how to use Swagger, learn how to define an API endpoint

**The goals of this lab are:**  
1)	To set up a simple directory for our first application
2)	To create our first OpenAPI specification file using the Swagger Editor tool. 
3)	To get introduced to JetStream2, the cloud-based infrastructure will use to deploy our service.
 
## Part I. Directory Set-Up
Keeping organized is crucial. Let’s setup a workspace for our first application deployment. This should be included in the Week 4 Github folder. For now, you should create a myFirstApp folder with an src folder inside. At the end of the day, the following items will be in your workspace:

## Part  II OpenAPI 3.0 (Swagger)

In this lab we are introducing OpenAPI 3.0 specification to define an API. We'll be using SwaggerHub for the specification development.

1. Create an account on [SwaggerHub](http://swagger.io/)
2. Create a new API in your account.
```
Note: You can only have 3  APIs created in a free SwaggerHub account. Make sure to delete any if you don't use them.
```
3. Use the 'Create New' button and create a new api.

   Owner should be you.

   Project --None--

   Specification OpenAPI 3.0.x
   
   Template should be set to None

   Name is required name it something clever

   Version is required (e.g., 1.0)
   
   Visibility should read Public

   Everything else can be left blank for now

4. Build out the specification file

   Discuss the [OpenAPI Object](https://swagger.io/specification/) 

5. Identify the different APIs endpoints in the API specification.

## Part II JetStream2 Deployment

Create an instance (VM) on JetStream2. The next screen will ask you to choose the specifications for your virtual machine. Enter your name (vm_LASTNAME), choose m3.tiny, 20 GB Root Disk Size, 1 instance and YES for the web desktop.

Take a moment to explore Desktop Interaction mode and Shell Interaction mode.

In Shell Interaction mode:

```bash
cd Documents/
mkdir work
cd work/
```
Then, connect your Github repositories here as well:
```bash
git clone link-to-E222-student-repo
git clone link-to-your-student-repo
```
Navigate into your personal repo to your myFirstApp folder. What happens when you try to run server.py?
```bash
python3 server.py
```
You probably received some dependency errors – packages were not installed. Remember this is a fresh machine! BUT before we start installing the required packages, lets create a virtual environment to “enclose” our python project.  

IMPORTANT SIDE BAR! Add to gitignore file: .venv/

```bash
python3 -m venv .venv
source .venv/bin/activate
```
You should have a different prefix in your command line now (.venv).  Ok, now let’s do the pip installs needed for this project.
```bash
pip install Flask
pip install connexion[flask, swagger-ui, uvicorn]
```

What happens if you need to recreate your VM instance? You loose ALL of these installs! Let's save them somewhere so we know what we had to install to make this app work.
```bash
pip freeze > requirements.txt
```
Later, we can run
```bash
pip install -r requirements.txt
```
Cool, eh?

## Student Task

At this point we should know how to define an API endpoint (e.g., /paths). We should also know how the operationID ties the python function to the endpoint.

Your task is to create a python function that will return a string that details your model information. Edit your API specification file to include an endpoint for your application.

Take a look here at the sum function, and keep in mind for us to use python within our API we have to make functions. As we think about our project we need to think about what functions we will need to create.

```python
def model_info():
    details = "The model used .... include hyper parameters, libraries, etc..."
    return str(details)

```
Make sure you put in another GET request with the appropriate path and operationID.