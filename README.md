# fabelio-py
 
## Application Content
This Application application contains 3 pages:
1. 1st page is on root, contains a form to insert fabelio product detail url. The form will make POST Http request to insert the given url to the database.
2. 2nd page is on `/list`, contains a table of contents from the submitted url(s). The index of each product is a clickable link. This link will bring user to the product detail page of the corresponding product index. The content consists of the following information:
  - Product Index (integer)
  - Product Url (string)
  - Product Name (string)
  - Product Description (string)
  - Product Price (integer)
  
3. 3rd page is on `/product/<index>`, contains complete information of the specific product. The content consists of the following information:
  - Product Name
  - Product Image
  - Product Price
  - Product Description


## Deployment
We are using Heroku for the cloud with directly connected to this github. The deployment will be done with the following steps:
1. Login to Heroku
2. In the selected application, go to **Deploy**
3. Establish connection to github
4. Select repository to deploy
5. We can either use automatic deployment on-push to master branch, or just manual deployment.

We also implement gitflow as the branching model. But because the application still not that big and complicated, we only use 2 branches; master and develop.


## About The Application
Stacks used for this application:
- Language: Python
- Framework: Django
- Database: SQLite
- Cloud: Heroku
- Code Versioning: Git
- Git Repository: Github
- Scraping Tool: Beautifulsoup
