# Zendesk Melbourne - Coding Challenge # 

- How to run the application
- How to run tests
- Assumptions
- Limitation & potential improvements

## How to run the application ##

1. Check the python version:  
   This application was written in Python 3.8.3 under windows env, any version above should work.  
   If your Python is lower than 3.8.3, I would suggest to download the latest Python at:  
   https://www.python.org/downloads/
3. Clone the project to local:
   ```
   git clone https://github.com/dpan968/zendesk_challenge.git
   ```
2. CD to the directionary and install necessary pacakges:
   ```
   cd zendesk_challenge
   pip install -r requirements.txt
   ```
3. Run the search application:
   ```
   python main.py
   ```

## How to run tests ##

At project root directory

   ```
   pytest
   ```

## Assumptions & potential improvements ##

1. Both input files can be read in memory on a single machine.
2. _id field is unique in both user and ticket entity.
3. Some records can miss certain fields, such as type field in ticket entity, verified field in user entity.

## Limitations & potential improvements ##

1. All input files, and assisting search tables including index tables are maintained in memory. In a production
   environment, all these info will be loaded into a database.
2. Search feature is string based, the input needs to be exact match and case sensitive.  
   e.g. type in first name only won't return any results, if search by created_at, the exact timestamp string needs to
   be type in, including the timezone info.
3. Search module contains some user interaction logics and search functions. In prod env, they should get separated.
4. Current user interaction logic uses multiple if-else statement and manual validations, some alternatives and
   mitigations:
    - explore the new feature match-case in Python 3.10 to replace if-else
    - use cli library to give the user multiple options intead of asking for manual input, to save if not avoid manual
      validation at all.