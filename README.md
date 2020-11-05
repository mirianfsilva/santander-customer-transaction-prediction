## Santander Customer Transaction Prediction

### Can you identify who will make a transaction?
---
This is a case study, proposed by Banco Santander in a Kaggle competition, where we need to identify which customers will make a specific transaction in the future, irrespective of the amount of money transacted. The data provided for this competition has the same structure as the real data we have available to solve this problem.

[Kaggle Dataset](https://www.kaggle.com/c/santander-customer-transaction-prediction/overview)


#### Machine Learning API
---

There are different ways to deploy your machine learning model. In that application, I used Flask, a web services framework in Python.
But many cloud providers have these services focused in provide ready-to-use APIs, that automate the deploy process a lot. In this case, after the prediction model has been trained, a `pickle` of that model was generated to be used by an API. A Python's `pickle` module exports your model in a file. 

For the flask web api and to run de model, it's required install dependencies. 
```
$ pip install -r requirements.txt
```
To run web server and use swagger: `python server/server.py`.

This server has not been published and is in development mode. I actually do not put this into production. A real production prediction API would need to handle edge cases and we would need to do model section. However, this is a basic prediction API. 

References: [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/example.html) 