## Back to Basics 103: What are Virtual Environments and Why do you need Them?

Hi There 😀
Now you have powered up yourself with the knowledge of how to install external open-source packages, you can now almost do anything really, but, there is a recommended way to create that software/algorithm which can make your life easier. 

Say Hi to** Virtual Environments** 🌅

For the reader's benefit, I wanted to let you know that this article is a part of the **"Back To Basics"** series. Readers can find the preceding article by clicking on the link  [here.](https://tradewithpython.com/back-to-basics-102-what-are-python-packagesmodules-and-how-to-install-them) 

#### This article will benefit the following category of readers:

- Python Beginner following the "Back to Basics" series.
- People who have used Python long back and need a refresher of how things work.

> For the purposes of this article** "virtual environment"** will be referred to as **"venv"**

#### We will be covering the following points in this article:
1. What is a venv?
2. Why venv is recommended to use?
3. How to create venv?
4. How to delete venv?

### What is a venv?
Think of a virtual environment as an isolated environment which is not dependent on anything.
Like this little fella out there, has his own island, can do whatever and nobody would care.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613512373846/KtAahFfC7.png)
[Image Source](http://earthporm.com/7-isolated-houses-world/)  
 
Now, if you have followed me from the previous article, you know `conda` also is an environment manager, it is very easy to create environments with `conda`, but before we get into that, let's first understand why you need them!

### Why venv is recommended to use?
Let's assume a venv as an app you use on your phone, let's say you are using an app to book an appointment with a medical doctor and the same app also allows you to book divorce lawyers!! I mean, why would someone pair doctors with divorce lawyers in one single app, sounds like a blunder to me. 

So similarly, when you are working on specific coding projects (e.g., creating a technical stock screener, backtesting platform, etc.) I would install a new venv everytime and only install the packages that I really want for that project. 

It may happen that your technical stock screener project requires the latest version of python to work with but your backtesting platform requires the older version of Python because of certain other package dependencies. So if there are two venv's to deal with this, both projects can work in isolation without fighting with each other like cat and mouse.

If you still have doubts over why you should use venv, hit me up on  [Linkedin.](https://uk.linkedin.com/in/yashroongta)  

### How to create venv?

If you have followed me along the series and installed Python via my recommended way, this is gonna be easy.  

Open up **Anaconda Prompt** on your machine and type in the following code  
`conda create --name myenv`  
Here, `myenv` will be the name of your new virtual environment, once you hit **Enter**, you will be shown a package plan and asked to proceed.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613514481832/pL5SkANWl.png)

Easy-peasy right? You now just need to activate the venv by entering

`conda activate myenv` and you will see that your `base` is now replaced with `myenv` which means your new environment is now active. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613514782356/vUWBHAKYX.png)

Now this is completely isolated and it does not know if python is already installed on your computer as it can't interact with anything other than that venv. You can verify this by entering `python` in the anaconda prompt, once your venv is active, it will probably do nothing or open the Microsoft Store for you to install Python manually. 

But, how do we install it via the same anaconda prompt, well its very simple.

Type `conda install python` or `conda install python=3.6`, v3.6 is just an example, you can use any version you like. Not mentioning the version would install the very latest version. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613515071018/ZNgbzFd9F.png)
![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613515099705/eYa7A4PYg.png)

> **Fun Fact:** Notice the size difference of installing the python v3.9 vs. python v3.6, shows v3.9 is dependant on a lot more other packages. 

Once your python is installed, you can go ahead and install any other packages you want as well.

Just use `conda install package-name=version_num`, if your project is not dependent on specific versions, just use `conda install package-name`

Once you are done with your work on that venv, it is always a best practice to close that venv and return back to `base` environment. This is very simple to do, just type in `conda deactivate` and that should be it. 

The detailed guide on how to deal with conda environments can be  [found here.](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) 

### How to delete venv?

The last and final section, phew, you must be tired by now. But I hope you are enjoying this. 
In the off chance that you are done with a particular environment and would like to delete it from your system, it's easy to do that as well. But first, let's get a list of all the venv's on my machine. 

Type in `conda env list` to list out all existing environments. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613515702235/tYx12TTTz.png)

As you can notice, I have a couple of venv's installed at the moment on my machine, let's say I want to delete the `useless-env` because well, its useless to me. 

Just type in `conda env remove --name useless-env` and it should do the job, to verify I will again enter `conda env list` to see an updated list. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613515891907/H9ZiX3u_R.png)

**And it's gone, Great Job**! 🎆🎉

If you have followed this series upto here, I really want to thank you for continuing to read. There is still a lot to learn, I think you are now ready to jump onto actual live coding to understand different types of Python operations. 

Since, there is already a lot of good content out there on this, I do not want to  [reinvent the wheel ](https://www.merriam-webster.com/dictionary/reinvent%20the%20wheel), so I will cover off the next article with all my recommended courses you can take to become better at this. Again, thanks very much and do subscribe at the top with your email to receive regular alerts on my future articles. 

Do let me know in the comments what you think of this article and if you had like me to cover any other points. All constructive criticism is welcome. 😎

If you liked this article, consider buying me a coffee ☕ by  [clicking here](https://www.buymeacoffee.com/tradewithyash)  or the button below.

%%[buymeacoffee-btn]




