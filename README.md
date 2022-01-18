### Steps to run
- installing dependencies
```bash
python3 -m pip install -r requirements.txt
```
- Spin up a mysql database (both docker and docker-compose should be installed and running)
```bash
docker-compose up -d 
```
- For the mailing service to work correctly, create a `.env` file and add the following :
```text
EMAIL= "<YOUR EMAIL ADDRESS>"
EMAIL_PASSWORD= "<YOUR EMAIL PASSWORD>"
// for simplicity sake i'm keeping the db env variables
DOCKER_MYSQL_ROOT_PASSWORD= "ayari"
DOCKER_MYSQL_DATABASE= "ssi_db"
```
(No worries, your data is safe with us 😅)
- start the application with 
```bash
python3 main.py 
```