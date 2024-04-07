# Pharma_Finda
ALX Portfolio Project

A web based application for locating nearest pharmacy or drug stores which have the queried drug in stock.

## Usage
To get started with Pharma_Finda, you can run the following command:
```
python3 -m api.v1.app
or
flask run
```

## Features
### User Registration and Login
PharmaFinda offers a secure and personalized user experience through user registration and login functionality. This feature enhances the security of the platform and allows users to access personalized services.

### Search Results
With PharmaFinda, users can register and search for drugs and get results of pharmacy stores around them with the drugs in stock.


## Configuration Options
Before running PharmaFinda, you need to set up the following environment variables. Create a .flaskenv file in the project directory and populate it with the variables and their respective values as shown below. Replace the placeholder values with your actual configuration.

```
PHARMACY_MYSQL_USER='root'               # MySQL database user
PHARMACY_MYSQL_PWD='pharmacy_dev_pwd'    # MySQL database password
PHARMACY_MYSQL_HOST='localhost'          # MySQL database host
PHARMACY_MYSQL_DB='pharmacy_dev_db'      # MySQL database name
PHARMACY_TYPE_STORAGE='db'               # Storage type (e.g., 'db' or 'file')
PHARMACY_API_HOST='0.0.0.0'              # API host (0.0.0.0 for all network     interfaces)
PHARMACY_API_PORT=5000                   # API port
PHARMACY_SESSION_KEY='anynumbersorletters'           # Session encryption key
```

## Setting Environment Variables
To set the environment variables, follow these steps on a Unix-based system (Linux or macOS):

1. Create a .env file in your project's root directory:
```
touch .flaskenv
```

2. Open the .env file in a text editor and add the environment variables with their values as shown above.

3. Save the file.

4. Before running your project, load the environment variables from the .env file using a tool like python-dotenv or by running:

```
source .flaskenv
```

If you're using a different platform or development environment, consult its documentation for guidance on setting environment variables.

PharmaFinda simplifies the process of helping users find drugs from pharmacy stores close to them. Use the provided instructions to configure the project and get started quickly. Enjoy streamlined container management with SwiftDeploy!

Contributors:
1. https://github.com/Nne85 - nneukamaka@gmail.com


