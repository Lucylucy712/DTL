# Implement of the dash app for DTL Project

## Codes Structrue and Purpose 

<details><summary> Codes Structure </summary>
  
| Folder   | File             | href on web           | Purpose                                                               |
|----------|------------------|-----------------------|-----------------------------------------------------------------------|
| ./       | application_local.py   |                 | The major app script for local run                                    |
| ./       | application.py   |                       | The major app script for aws run                                      |
|          | imports.py       |                       | to import modules at one step                                         |
|          | sidebar.py       |                       | to set up the sidebar structure                                       |
|          | style.py         |                       | to save some global style settings                                    |
|          | homepage.py      | /                     | to set up the homepage                                                |
|          | background.py    | /project/background   | to set up the background tab under **project** section                |
|          | motivation.py    | /project/motivation   | to set up the motivation tab under **project** section                |
|          | models.py        | /project/model        | to set up the model tab under **project** section                     |
|          | evaluation.py    | /results/plot         | to set up the evaluation tab under **results** section                |
|          | loaddata.py      | part of /results/plot | to load the results and set up the plot tab under **results** section |
|          | download.py      | /download/download    | to  set up the download tab under **download** section                |
|          | XX.cv            |                       | the results table                                                     |
|          | requirements.txt |                       | to collect all moduels needed for the environment                     |
| ./assets |                  |                       | to put necessary graphs                                               |

</details>

## How to run on local using terminal 
1. Set up a [conda envrionment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) and activate it 

2. Install all required moduels by 
`$pip install -r requirements.txt`

3. change the workding dictionary to the folder dictionary by 
`$cd \mycomputer\dtl\app\folder_path`

4. run the `application_loca.py` script by `$python3 application_local.py`

The terminal would show a local address for the website. Just go to the website to check the results

## How to deploy it on AWS 

Please follow the [tutorial](https://austinlasseter.medium.com/deploying-a-dash-app-with-elastic-beanstalk-console-27a834ebe91d)

Bascially, we need to compress all files, except for application_local.py and ReEADME.md, and upload it to AWS Ealstic Beanstalk. 