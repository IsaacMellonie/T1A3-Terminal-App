<h1>Parking Ticket App</h1>
<h2><a href="https://github.com/IsaacMellonie/T1A3-Terminal-App">GitHub Source Control</a></h2>
<h2><a href="https://peps.python.org/pep-0008/">Style Guide</a></h2>
<h2><a href="https://github.com/users/IsaacMellonie/projects/1">Project Management</a></h2>
<br>
<h2>Purpose</h2>

This is a Python project which aims to build a terminal application for purchasing parking tickets. The application provides the user with an interactive application in which they can select different options based on screen prompts, then providing input options through the keyboard. This application receives input from the user and mostly outputs to the terminal, though it's also capable of outputting to a user provided email with built in modules. Data is also collected and stored locally in a credentials file with user email, password, first name, last name, and car registration number. 

If this app was implemented in a real world situation, its most important features would be ease of use, an app that's dependable and runs consistently. A time-saving solution for people who need to buy parking tickets in different parking zones, providing a payment solution where there's no physical option. Ideally, it could be used on any mobile device with an internet connection, working with City Councils and private businesses who need an app to manage the heavy work in creating and maintaining a ticketing system.

<h3>Feature: Ticketing and Receipts</h3>
This feature encompasses the ability to takje the user's input based on screen prompts and interpret those choices into a receipt. The key of this feature would be the ability for it to accept the amount of time the user wants to park for and providing a system for them to pay. This is done by firstly gathering the user's info, then credit card, and then gathering details about how long they'd like to park for. Once this information is gathered the application will calculate the costs based on the time chosen and output a receipt with a total cost including tax, the time the transaction was placed and the expiry time.

<h3>Feature: Signup and Registration</h3>

Registration allows the user to access the sign in and then purchase tickets. It's the first major step the user will need to take in order to use the other features on the app. Firstly, the user will be prompted to enter an email address. multiple checks are completed on teh user's email to make sure it is a usable address. Next, they must enter a password which is atleast 6 - 12 characters long. They'll need to enter it twice to make sure it's correct. Once these first two steps are complete they'll be prompted to enter their first name, last name and finally, car registration number. Once these details are input there'll be a double check prompting the user to confirm. Once confirmed the details are stored locally in the database for recall purposes. Next, the credit card details are needed and must be run through a series of checks to determins that the credite card information is correct. Step 1 in this case is to get the CC number of 16 in length,  and only numbers. Step 2, a 2 digit expiry month. and finally step 3, a 2 digit year. None of this information is stored and ofr the purpose of privacy, this app does not require legitimate CC details to pass these steps. Finally, the user is prompted to enter the amount of minutes between 5 and 120 (2hrs max). Once they've decided how long and it's rounded up or down to be within the corrent range, they'll be charged a base rate per minute, and then tax added. THis receipt is processed and sen tto the user's screen.

<h3>Feature: Data Collection, Storage and Email</h3>

This feature allows for recall of data when it's needed after signup. This is an important feature for user's that may forget their information and need to have the password sent to them. FIrstly, they'll enter the password via the terminal, and if it matches the one kept on the local file the email will go through the emailing system created to connect to an ssl port, then using an smtp gmail server, will send the password. 

<h2>Implementation Plan</h2>
This was my initial planning for the app.
<img src="./docs/implementation/flowchart_parking_app.jpeg" alt="Planning">
<img src="./docs/implementation/01.jpg" alt="Step 1">
<img src="./docs/implementation/02.jpg" alt="Step 2">
<img src="./docs/implementation/03.jpg" alt="Step 3">
<img src="./docs/implementation/04.jpg" alt="Step 4">
<img src="./docs/implementation/05.jpg" alt="Step 5">
<img src="./docs/implementation/06.jpg" alt="Step 6">
<img src="./docs/implementation/07.jpg" alt="Step 7">
<img src="./docs/implementation/08.jpg" alt="Step 8">
<img src="./docs/implementation/09.jpg" alt="Step 9">
<br>
<h2>Features</h2>
<img src="./docs/implementation/feature-datetime-checklist-02.jpg" alt="Checklist-01">
<img src="./docs/implementation/feature-Email-SSL-SMTPLIB-checklist-02.jpg" alt="Checklist-02">
<img src="./docs/implementation/feature-PaymentSystem-checklist-02.jpg" alt="Checklist-03">
<img src="./docs/implementation/feature-StoreInfo-checklist-02.jpg" alt="Checklist-04">

<h2>Requirements</h2>
<p>

- Have Python 3.10 or newer installed.
- Have pytest installed.
- Windows with Linux subsystem intalled.

</p>
<h2>Installation and Instructions</h2>
<p>
First of all, we want to create a new email acount using Gmail. This will be specificailly used for emailing from the application in Python. Then follow the steps below to complete the setup process.
</p>
<ol>
<li> 
You can use your existing gmail account or make a new gmail account depending on what you prefer. Once you've decided, you'll have to turn on 2 factor authentication and create an App Password.
<br>
<br>

- <img src="./docs/01-setup.jpg">
1. Use a Gmail account and go to "Manage your Google Account."
- <img src="./docs/02-setup.jpg">
2. Next, go into Security
- <img src="./docs/03-setup.jpg">
3. Turn on 2 step verification if it isn't already
- <img src="./docs/04-setup.jpg">
4. Go into App Passwords
- <img src="./docs/05-setup.jpg">
5. Create a new App password and name it something to do with the application.
A pop up will appear. Copy the generated password.
- <img src="./docs/06-setup.jpg">
6. Paste the password into "email_setup.py" where it says "password". Then type in your gmail adress where it says "gmail". Make sure to leave the quotation marks around your input. This will be used in the main file and without it the emailing function won't work in the app.
- <img src="./docs/07-setup.jpg" alt="step-7">
7. Download a ZIP from the GitHub repository and unpack it on your local machine. The src folder contains all of the python files and the shell script fro running the application.
- <img src="./docs/08-setup.jpg" alt="step-8">
8. Next, you'll need to have Linux installed to execute "run_python_file.sh". On windows, go to the search bar and type in Linux. Install "Windows Subsystem for Linux" on your machine.
- <img src="./docs/09-setup.jpg" alt="step-9">
9. Open up the newly installed app and navigate to where the files are located. Open up the "src" folder and locate "run_python_script.py".
10. Run Windows Subsytem for Linux
11. Make sure the project folder is located on the Windows SubSystem. Ge the location of the folder from teh finder window. You'll need this to navigate to the src folder.
This can be done by typing "cd <folder_name>/<folder_name>/IsaacEveansMellonieT1A3/src" and tehn hit enter.
12. Now that we're located in the project folder, start the app by typing "sh run_python_script.sh" into the terminal window and hit enter. The app should begin.
<h2>Final Thoughts</h2>

On reflection I would have liked to include more features but was limited for time and my own level of knowledge. I had difficulty understanding my own code toward the end of the assignment due to the structure and way I used inputs and outputs. It taught me a great deal about managing your code. I learned it's important to keep it structured so that you can easily implement changes that won't break a larger piece of the overall feature. 

<h2>References</h2>

The provided references were crucial in the development of this application.

- Super User. (n.d.). How to set the default program for opening files without an extension in Windows? [online] Available at: https://superuser.com/questions/13653/how-to-set-the-default-program-for-opening-files-without-an-extension-in-windows [Accessed 30 Oct. 2023].

- ‌Bagban, M. (2021). A Basic Login System with Python. [online] Medium. Available at: https://medium.com/@moinahmedbgbn/a-basic-login-system-with-python-746a64dc88d6.

- Training, P. (2022). Guide to Turn .py Files into .exe. [online] Pierian Training. Available at: https://pieriantraining.com/how-to-convert-a-py-script-into-a-exe-file/ [Accessed 30 Oct. 2023].

- PyPI. (n.d.). pyinstaller: PyInstaller bundles a Python application and all its dependencies into a single package. [online] Available at: https://pypi.org/project/pyinstaller/.

- Stack Overflow (2022). Stack Overflow - Where Developers Learn, Share, & Build Careers. [online] Stack Overflow. Available at: https://stackoverflow.com/.

- pyinstaller.org. (n.d.). How to Install PyInstaller — PyInstaller 5.9.0 documentation. [online] Available at: https://pyinstaller.org/en/stable/installation.html.

- Santos, A.B. (n.d.). How to Run .sh or Shell Script File in Windows 11/10. [online] SoftwareKeep. Available at: https://softwarekeep.com/help-center/how-to-run-shell-script-file-in-windows [Accessed 31 Oct. 2023].

- Mata, Y. (2021). ‘Python’ is not recognized as an internal or external command, operable program or batch file. [online] Career Karma. Available at: https://careerkarma.com/blog/python-is-not-recognized-error/#:~:text=What%20is%20causing%20the%20 [Accessed 31 Oct. 2023].

- Stack Overflow. (n.d.). ubuntu linux gmsh gives ‘sh: 1: python: not found’ error. [online] Available at: https://stackoverflow.com/questions/73221704/ubuntu-linux-gmsh-gives-sh-1-python-not-found-error [Accessed 31 Oct. 2023].

- mspoweruser.com. (2022). How to Run Shell Script in Windows. [online] Available at: https://mspoweruser.com/different-ways-to-run-shell-script-files-on-windows/ [Accessed 31 Oct. 2023].

- Mailtrap. Src=’https://Secure.gravatar.com/Avatar/4c785e9c0ddf669441d6884fc9c43624?s=57, img A., #038;d=mm and width =’57’ />Chris, 038;r=g’ class=’avatar avatar-57 photo’ height=’57’ (2022). Sending Emails in Python [2023 Guide with Code Examples]. [online] mailtrap.io. Available at: https://mailtrap.io/blog/python-send-email/.


- Emailing system for Python. https://www.youtube.com/watch?v=Sddnn6dpqk0&list=PLM2E1SwuAVipIMG_KobekbvBd9I7NvwXP&index=12&t=647s&ab_channel=TheIntriguedEngineer
‌

‌
