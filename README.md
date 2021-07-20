# dnac_wlc_config_diff_checker
prototype script that finds the text diff between a golden Cisco WLC configuration and a set of other Cisco WLCs to ensure the configurations among controllers are identical

## Solution Components
* PYTHON
* DNAC Python SDK
* difflib python libary


## Installation/Configuration

Make sure you are on the root of the project folder. 

1. First step will be to include the credentials of your DNAC instance inside the config.py file

```python
username=""
password=""
base_url=""
```

2. Create virtual environment and name it env, then activate it

```console
foo@bar:~$ virtualenv env
foo@bar:~$ source env/bin/activate
```

3. Install the dependencies required for the python script
```console
foo@bar(env):~$ pip install -r requirements.txt
```

4. Run the python script
```console
foo@bar(env):~$ python main.py
```

5. When the script launches, the script will ask the user to choose which WLC to be the "golden config" (compare this config to the rest selected). After, it will ask the user to select the set of WLCs to compare their configs. All the configurations files are saved uner the configs folder and the results of the difference will be under the diff_check_results folder with the hostname as the name of the files. 


## difflib python library

Here is some information on how to understand the diff output that results from comparing two config files. We are using a unified diff.

![/images/unified_diff.png](/images/unified_diff.png)

This is a quick example showing the output for the diff of two files 

![/images/diff_example.png](/images/diff_example.png)

