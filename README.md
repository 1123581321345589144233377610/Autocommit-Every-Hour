# Autocommit Every Hour

## :notebook: Description

This is a python project with which you can make empty autocommits every hour to your GitHub repository! 
This way you will have activity on GitHub every hour.

## :shopping_cart: Requirements

- datetime
- requests
- schedule

## :wireless: Installation from source 

```console
git clone https://github.com/1123581321345589144233377610/Autocommit-Every-Hour.git
```
```console
cd Autocommit-Every-Hour
```
```console
pip install -r requirements.txt
```

## :rocket: Run the program

Go to the folder /autocommit_every_hour

```console
cd autocommit_every_hour
```

Open the file autocommit.py and enter your GitHub username in the USERNAME variable (For example, I have it: 1123581321345589144233377610). 
Next, in the REPOSITORY variable, write your repository in which you want to make an activity (For example, I have it: Autocommit-Every-Hour). 
Next, you need to get your token. I'll tell you about it below.

![](https://drive.google.com/uc?id=1D33JgvDwTXc3imAGa65PVyXN4aDa19cg)

To work with the GitHub API, you need to get a token, which is issued to each user in the [settings](https://github.com/settings/tokens). 
To create a new token, click on "Generate new token (classic)".

![](https://drive.google.com/uc?id=1p-nFniFd2fUeBALm9AXlSXPfANbXAhRo)

Next, you need to leave a name for the token and mark the areas of access to the key. 
For our purposes, it is enough to give access only to the repo section.

![](https://drive.google.com/uc?id=1IHAJWiXoVxSsRigrbv8CGnyhJkUQnSyM)

After that, a token will appear in the green window. You can copy it and write it to the TOKEN variable!

![](https://drive.google.com/uc?id=1vIkcBqOaFlZuEZZwTGIPQjJsDyOKof6J)

Now, following the path /Autocommit-Every-Hour/autocommit_every_hour, you can run the script.

```console
python3 main.py
```

Now, while the script is running locally, commits will be made every hour. 
If you wish, you can run the script on the server so that it always works.

## :octocat: Author

**Dima M. Shirokov**
- [GitHub](https://github.com/1123581321345589144233377610)