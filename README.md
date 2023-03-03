# Django Weather API
This project is a Django-based Weather API that enables users to retrieve weather data. It provides a step-by-step guide on how to set up the project, install the necessary dependencies, run migrations, and ingest data. Moreover, it also provides comprehensive information on accessing and utilizing the API.

# Prerequisites
The following prerequisites are required to use this API:

        Python (3.7 or higher)   
        docker

0. Create a Virtual Environment and then install the dependency using -

        pip install virtualenv
        virtualenv venv
        venv/Scripts/activate (Windows)
        source venv/bin/activate (Linux and Mac)
        pip install -r requirements.txt

1. Start the Database using 

        docker-compose up 

2. Make Migrations in Database 

        cd src && python manage.py makemigrations

        python manage.py migrate

3. Run Data Ingestion Script 

        python manage.py shell < main.py   

4. Run Django Test Cases

        python manage.py test

5. Run Django Server 

        python manage.py runserver

6. To access the API endpoints, use the following links:

        http://127.0.0.1:8000/weather
        http://127.0.0.1:8000/weather/stats
        http://127.0.0.1:8000/swagger
        http://127.0.0.1:8000/redoc


7. For AWS Deployment

To deploy the API to AWS, use the following steps:

        - Deploy Django API with AWS Elastic Beanstalk.
        - Elastic Beanstalk will create the environment, launch the instances, and install the required software.
        - You can either use an external database service like Amazon RDS or deploy a database on your Elastic Beanstalk environment.
        - After your app has been deployed, you can test it by accessing the URL of your environment.
        - If you encounter any issues, you can use the logs and monitoring data to diagnose and fix the problem.





