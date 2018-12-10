# SRRMS
#### SR Railway Management System
## Setup instructions

### Server

  - #### Step 1 (optional but recommended)

     Create a python virtual environment by using virtualenv or conda
     ```bash
     conda create -n environment python3.6
     ```
     or

     ```bash
     python -m venv venv && source venv/bin/activate
     ```
  - #### Step 2
    Clone this repo
    ```bash
    git clone https://github.com/Vishnu44d/SRRMS.git && cd environment
    ```

  - #### Step 3
    Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
  - #### Step 4
    - initialize database
      ```bash
        python manage.py db init
      ```
    - migrate database
       ```bash
        python manage.py db migrate
      ```
    - update database
      ```bash
        python manage.py db upgrade
      ```
    - tsting the system
      ```bash
        python manage.py test
      ```
    - running the server
      ```bash
        python manage.py run
      ```



## Api
  The Api end points are `'\'`