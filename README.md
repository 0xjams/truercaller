# TruerCaller Tasker

This project uses Tasker and termux-tasker to automate calls to the Truecaller API and present a pop up while a call is ringing.

## Installing and configuring our environment

Inside Termux we need to do the following:

Install truecallerjs with:

```
npm install -g truecallerjs
```

When we install packages with npm, the shebang is `/usr/bin/env`. However, that path does not exist in Termux, so we need to adjust it. Luckily, Termux has a helper script for that:

```
termux-fix-shebang /data/data/com.termux/files/usr/bin/truecallerjs
```

Then, we need to put the contents of this repo to `/data/data/com.termux/files/home/tasker`

With everything in place, we need to configure truecallerjs. To do that, we need to execute:

```
truecallerjs login
```

That command will send an SMS or a WhatsApp message with a code, if we enter it correctly, we should be ready to test our setup.

## Executing our script

To verify if everything works, let's execute the following command. 

(Keep in mind that you need to set the PHONE_NUMBER variable or replace it with a value)

```
/data/data/com.termux/files/home/.termux/tasker/parse.sh ${PHONE_NUMBER}
```

With that, we are ready to configure Tasker.

## Importing the profile to tasker

Follow [this](https://www.reddit.com/r/tasker/comments/7g7694/how_to_import_a_file_into_tasker_a_quick_easy/) guide to import the file tasker_profile.prf.xml to Tasker.

## To Do

Add error handling everywhere