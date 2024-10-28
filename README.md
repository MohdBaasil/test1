### Git and other commands used in the command prompt:
1. mkdir <file_name> to create the folder
2. cd <file name> to go inside the folder
3. git init, initializing folder as git repository
4. git add . to add all the files into git track
5. git commit -m "<message>", it commits whatever is there in the track
6. git remote add origin <GitHub repository link>, builds connection between git and github
7. git push --set-upstream origin master, sends all the files from git to github.
Docker Commands:

### docker build -t folder_name> .
1. docker run <folder_name>
Steps:
1. Create the required files such as the dataset csv file(heart.csv), training model python file, requirements txt file, Dockerfile.
2. Create a new item under Freestyle Project item type
3. Select Git in Source Code Management and paste your github repository url
4. Add Execute Windows Batch Command step in Build Steps
Save configurations
5. Build now and visualize console output
6. Now open command prompt with the path of the folder containing the required files
7. Execute the Docker commands mentioned above
8. Visualize the output in the command prompt and in the Docker Desktop app
