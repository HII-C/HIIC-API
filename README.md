# HIIC-API
API for the HII-C project running on Flask

This is the first version of the HII-C API running on an AWS server with Python Flask. The goal is to be able to create an API to access the database containing associations of medical concepts. This will interact with the Patient Viewer App. So far the API has the following endpoints:

/get_items - returns all items in the associations database

/ - provides a search box to view current items in the association
