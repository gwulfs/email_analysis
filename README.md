**Email Analysis With PyData**
===================

To use the code you must include your email.json file in the cloned repo on your local machine, and create a file called secrets.py that includes the following: "key = API_KEY_FROM_PLOTLY" also change py.sign_in('gwulf', key) from plotly_script.py to include your personal plotly username.

First run count_words.py to create json metadata Then you can either run plot.py (for matplotlib png files in the plots directory) or run plotly_script.py to get scatterplots on your plotly account.

Also feel free to rm -rf * from inside the plots and results directories to remove my Data.

Notebook comparing words used in mom's emails with those in mine:
http://nbviewer.ipython.org/github/gwulfs/Email-Analysis/blob/master/mom_vs_me.ipynb
![bayes](http://i.imgur.com/6YAU6yR.png)

Filler word usage over 10,000 word bins
![fillers](http://i.imgur.com/fXufppH.png)

To get your own email.json file use:
https://eos2.io
![eos2](http://i.imgur.com/ieOrmEk.png)

#Team:
![team](http://i.imgur.com/GJqc2Q6.png)