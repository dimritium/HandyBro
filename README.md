# HandyBro
A personal project aimed at automating certain day to day browser things 

# Usage
Please <b>install chromium web browser and respective webdriver</b> for this package to work correctly,
since firefox is having issues with selenium, I recommend not using it. The one click login 
will work only at Chandigarh University (Gharuan, Mohali)

Make sure you have ```python 2.7+``` installed

For installing dependencies run 

```python
pip install -r requirements.txt
```
### For one click login:

After meeting the requirements just double click ```bro.py``` file

### More functionality for command-line user:

```python
python bro.py sea items-to-be-searched
```
replace 'items-to-be-searched' with respective query and automatically 5 tabs will be opened with based on google's top 5 results
