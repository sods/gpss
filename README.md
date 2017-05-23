# gpss
Gaussian process material for summer school teaching.

## Software and infrastructure (for Data Science Africa)
Below are instructions and advice for deploying the DSA summer school.

### Infrastructure
In previous years we've had some trouble with the bandwidth available both to the Internet and *locally* between computers. It is maybe best to develop the summer school under the assumption that there is no network, and any that exists we need to utilise when possible.

Hardware to take:
 - memory sticks for sneakernet to distribute everything. In particular anaconda is 474Mb (need a copy for windows and linux)
 - wifi access point
 - laptops (to run servers on)
 - cables (ethernet, etc)
 - video recording equipment

### Server Software
I ran an apache2 server on my laptop, and created a small webpage from which people can
 - download anaconda
 - download the jupyter notebooks and associated datafiles
 - download the lecture slides
 - create a new folder for the jupyter notebook (a small flask python script did this)
 - ran the jupyter server (from a different user account to minimise security issues)
 
I've put some of last year's files up on the repo (see inside <a href="https://github.com/sods/gpss/tree/master/dsa_hosted_files">dsa_hosted_files</a>). I've not included the anaconda installers or these two files (as they're too large for a git repo):
- malaria-classification-example.npz
- twitter_data.txt

I also wrote a small python script (called <a href="https://github.com/sods/gpss/blob/master/server.py">server.py</a>) that created a new folder for the jupyter notebooks, and copies in all the files (from the ```source_ipython``` folder) the student will need (data csv files etc).

To start the ipython server, go to the 'ipython' folder and run,
```
#I found this might be necessary if you've switched users.
#export XDG_RUNTIME_DIR="" 
jupyter notebook --no-browser --ip="*"
```
To start the little server, go to the home directory and run,
```
python server.py
```
Make sure apache2 is running. You'll also need to change the link in remoteipython.html.
```
sudo service apache2 restart
```

Switching to dsa16 account
```
su dsa16
[enter password]
```

### Information for students
Prior to the school starting we need to provide people with:
 - the notebooks and data files
 - anaconda links
 - how to get set up, get jupyter running, etc
 
### Questions
- Which version of python are we using?
- How do we distribute modules (i.e. sods, GPy) people might need.
- We're assuming most computers are going to be laptops (and thus connect via wifi)
- If we're using our own hotspot, will people not be connected to the internet at all? (I'm thinking last year people probably downloaded the sods data over the 'net when they first do the import).
