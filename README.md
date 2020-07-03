# Welcome to the BGH atlas repo
 
 
# What do you need to upload your model to the BGH atlas?
* Your github login details
* A short and sweet description of what your model does
* An animation of your model
* A figure of your model setup
* A table or a figure of the conditions for your model
* A figure showing the main results of your model
* A descriptive close caption for the fig/tables/animations listed above


# How to upload your model to the BGH atlas?

1. First download this repo into your computer by typing the following command in the terminal
```bash
git clone https://github.com/basin-genesis-hub/bgh_atlas_member_private.git
```
(You'll only have to do this once. Once you have a local folder of the repo on your system, ignore this command.)

You should now have a directory in your computer called bgh_atlas_member_private

2. Make a copy of the template file  `_posts/Template.md`, call your copy DATE-TITLE.md
Modify your .md file in the text editor of your choice. Your time to shine! ps: FOLLOW THE TEMPLATE. Instructions are provided in the comments.

To view the post in action do the following:
Make sure that docker desktop is running (that’s the whale icon on mac OSx)

In the terminal go to the bgh_atlas directory:
```bash
cd bgh_atlas_member_private/
```

Run the following command in the terminal at the bgh_atlas directory level
```bash
docker run --rm --volume="$PWD:/srv/jekyll" \
-p 9999:4000 -it julesg/atlas               \
jekyll serve
```

(wait 1 minute for the docker to download). Once the terminal say `Server running... press ctrl-c to stop.`
The jekyll server is ready! Open your web browser and goto http://localhost:9999

You can make changes to the post and refresh the browser to see them.

Once you are satisfied with the post it’s time to commit it. Let’s assume the post is called 2019-07-01-foobar.md

In another terminal go to the bgh_atlas directory level and run the following commands

* To Get the latest changes/update your repository run 
```bash
git pull 
```
* To see what has changed run and ensure that you are on the correct and intended branch
```bash
git status
```
* To stage the new post run 
```bash
git add _posts/2019-07-01-foobar.md
```
* To commit the new post run 
```bash
git commit -m 'Your message about the post'
```
* To upload the local changes to the remote repository 
```bash
git push
```

Et voilà! your model should appear just in http://members.bgh.org.au/ if you have selected the 'private' option in the privacy attribute on the template under the category you have chosen (e.g. Underworld, Badlands, Badlands-Underworld, Badlands-Underworld-Gplates-Citcom, pyGPlates). 

However, if you would like the model to be appearing also on http://atlas.bgh.org.au/, then please select the privacy option to be 'public'.


# If the steps above are not working for you, DO NOT fear! 
Login into your github

Go to https://github.com/basin-genesis-hub/bgh_atlas_member_private/tree/master/_posts

Upload your .md file by clicking on the upload files tab and dragging the file

Commit the file by clicking on commit changes 

Your changes will be accepted by the BGH-Atlas team, but you won’t be able to see your model post straight the way.

# Comment on the animations
All the animations have to be in .mp4

To obtain a url for the all images and animations, store them in the bgh word press under media, copy the url and paste it in the yaml under the appropiate field. 
