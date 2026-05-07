# Git Commands

## 1. Clone a Git repo
```bash
git clone <repo_url>
```

Example:
```bash
git clone https://github.com/Nkosikk/ndosiautomationdevbasics.git
```
	
## 2. Check which user is in that repo
```bash
git config user.name
```

## 3. To check your name:
```bash
git config user.name "YOUR NAME"
```

## 4. To change your name globally:
```bash
git config --global user.name "YOUR NAME"
```

## 5. To change your email:
```bash
git config user.email "YOUR EMAIL"
```

## 6. High-level summary of the status of your local repo 
```bash
git status
```
> High-level summary of your working directory which shows the current branch name, new files, and staged files. 

## 7. Create a new branch
```bash
git branch BRANCH_NAME
```
(no spaces in your branch name)

## 8. To get a list of all branches
```bash
git branch
``` 
> `*` indicates your current branch 

## 9. To go to your branch:
````bash
git checkout BRANCH_NAME
````

## 10. To move to the remote repo:
```bash
git push
``` 
	
## 11. To undo everything on your working directory 
```bash
git restore .
```
	
## 12. To commit your code with a message
```bash
git commit -m "MESSAGE"
``` 

## 13. To add files from your working directory to the local repo
```bash
git add FILE_NAME
```

## 14. To add all files from your working directory to the local repo
```bash
git add .
```
