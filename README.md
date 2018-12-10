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
     python -m venv environment && source venv/bin/activate
     ```
  - #### Step 2
    Clone this repo
    ```bash
    git clone https://github.com/Vishnu44d/srrmsv2.git && cd environment
    ```

  - #### Step 3
    Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
  - #### Step 4
    - running the server
      ```bash
        python manage.py run
      ```

## Api
  The Api end points are `'\'`
  - ### /user/
  ```javascript
  {
    "status": "success/fail" 
  }
  ```