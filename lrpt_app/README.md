# Implement of the dash app for DTL Project

## Codes Structrue and Purpose 

<details><summary> Codes Structure </summary>
  
| Folder   | File             | href on web           | Purpose                                                               |
|----------|------------------|-----------------------|-----------------------------------------------------------------------|
| ./       | application.py   |                       | The major app script                                                  |
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
1. Set up a [!conda envrionment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) and activate it 

2. Install all required moduels by 
`$pip install -r requirements.txt`

3. change the workding dictionary to the folder dictionary by 
`$cd \mycomputer\dtl\app\folder_path`

4. run the `application.py` script by `$python3 application.py`

The terminal would show some comments as below. Just go to the website to check the results.

![command results]("/assets/terminal_results.pnd")

## How to deplot it on AWS 
