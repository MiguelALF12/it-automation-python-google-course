# Google course IT Automation using python

This repo contains the final project developed in Google's professional program IT automation with python.

Each directory contains the following:

- <strong>Scale-and-convert-images-using-PIL</strong> have basic code of how to use PIL to work with images.
- <strong>Processing-files-and-using-web-services</strong> make use of the request and json module to post information on a django web site provided by Google.
- <strong>pdfs-emails</strong> show how to create pdfs and emails with reportslabs and Email modules respectively. Also shows how to send the created email messages trhough the SMTP module. Here I used a local mail client called mailslurper in order to simulate the reception of the messages. The configuraton of the services is provided in a file called  `mailslurper-config.json`.
- <strong>final-project</strong> have all what was done in the directories above with some modifications according to the final qwiklab of the course. The whole idea was to upload images and text to a web page to display them after. Then we need to make a script that could create a report pdf and an Email message containing certain information. This will be later sended through Email using roundcube mail client service. Last, we need to make a script that takes care of the system's health (all of this was made inside a virtual machine through SSH connection povided by google). 
  For more detailed information, go [here](https://googlecoursera.qwiklabs.com/focuses/25674492?parent=lti_session) and take a red of the project.

## Some results

### Email generated

![Email generated](https://github.com/MiguelALF12/it-automation-python-google-course/blob/main/results/sended_email.png)

### PDF generated
![PDF generated](https://github.com/MiguelALF12/it-automation-python-google-course/blob/main/results/resulted_pdf.png)

### Checking system's health and sending email with the resulted analysis
![System health](https://github.com/MiguelALF12/it-automation-python-google-course/blob/main/results/healt_systems_with_cron.png)


#### Note
All the modules hosted in requirements.txt file are not used, you just need to pay attention on the imports. All that long list is because the venv inherited the globally installed packages.
