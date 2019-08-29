#How to make upload your model to the BGH atlas?
 
 
#What do you need?
·       Your github login details
·       A short and sweet description of what your model does
·       An animation of your model
·       A figure of your model setup
·       A table or a figure of the conditions for your model
·       A figure showing the main results of your model
·       A descriptive close caption for the fig/tables/animations listed above


#Prepare your .md file in the text editor of your choice following the template XXX
 
Download the repo by typing the following command in the terminal
git clone https://github.com/basin-genesis-hub/bgh_atlas.git

You should now have a directory in your computer called bgh_atlas

Add the .md file (the file that has the model information) to the _posts directory

To view the post in action do the following:
Make sure that docker desktop is running (that’s the whale icon)

In the terminal go to the bgh_atlas directory (that’s cd bgh_atlas/)  

Run the following command in the terminal at the bgh_atlas directory level

docker run --rm --volume="$PWD:/srv/jekyll" \
-p 9999:4000 -it julesg/atlas               \
jekyll serve

(wait 1 minute for the docker to download)
Then in your web browser type https://localhost:9999

You can make changes to the post and refresh the browser to see them.

Once you are satisfied with the post it’s time to commit it. Let’s assume the post is called 2019-07-01-foobar.md

In another terminal go to the bgh_atlas directory level and run the following commands

To Get the latest changes run 
git pull 
To see what has changed run
git status
To stage the new post run 
git add _posts/2019-07-01-foobar.md
To commit the new post run 
git commit -m “Your message about the post”
To upload the local changes to the remote repository 
git push

Et voilà! your model should appear in https://basin-genesis-hub.github.io/bgh_atlas/ under the category you have chosen (e.g. Underworld, Badlands, Badlands-Underworld, Badlands-Underworld-Gplates-Citcom). 


If the following steps are not working for you do not fear! 

Login into your github
Go to https://github.com/basin-genesis-hub/bgh_atlas/tree/master/_posts
Upload your .md file by clicking on the upload files tab and dragging the file
Commit the file by clicking on commit changes 
Your changes will be accepted by the BGH-Atlas team, but you won’t be able to see your model post straight the way.
