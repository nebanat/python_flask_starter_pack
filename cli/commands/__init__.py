"""
    To create a cli command add a new file appended by the command
    for example:
        if I want to create a command called test:
        - I will create a file cmd_test
        - create a function cli and run my command

    To run command on cli:
     with docker: docker-compose exec your-image yourapp your-command

     without docker:
        - export FLASK_APP='/path/to/flask/app'
        - flask run your command

     To view optional parameter
        - docker: doc
"""