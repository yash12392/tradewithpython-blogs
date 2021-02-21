## Back to Basics 102: What are Python Packages/Modules and how to install them?

Hi There 😀  
Now that you have installed Python on your machine via **Anaconda distribution**, the next question you will ask is, okay, how do I started? 🤨 

For the reader's benefit, I wanted to let you know that this article is a part of the **"Back To Basics"** series. Readers can find the preceding article by clicking on the link  [here.](https://tradewithpython.com/back-to-basics-101-how-to-install-python-the-correct-way) 

#### This article will benefit the following category of readers:

- Python Beginner following the "Back to Basics" series.
- People who have used Python long back and need a refresher of how things work.

#### We will be covering the following points in this article:
1. What is a Python Package/Module?
2. Different Methods of installing a Python Package.
3. The recommended way of installing a Python Package.

**So let's jump in 🤹‍♂️**

### What is a Python Package/Module?
A Python **package** is a collection of **modules** and a **module** is a single *.py* file. Think of `package` as a regular bank branch on the side of your road and the different departments within that bank branch (e.g., Mortgages, Deposits, Complaints, etc.) as a `module`  
All the departments have a specific role to play, and they all together create a bank. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613430780477/AOi23AZha.png)
Source:   [RealPython](https://realpython.com/python-modules-packages/) 

You may ask, why do we need packages and different modules? Why can't we keep all the code in one `.py` file? Good question; I thought the same when I started learning, over time; it has become clear to me:

- Your code for a simple application can go up to 10,000+ lines. It's easily manageable to split your code's specific functions into different files and then import those into your one central file.
- Easier to pinpoint bugs when code is split into different files rather than scrolling 10,000+ lines of code and losing all your hair. 👱‍♀️👱‍♂️
- Easier to share with the community and much more readable for them. 

**Using the banking example**, imagine one manager managing all 200+ employees in a branch and somebody is stealing money, imagine the same person interviewing all 200+ employees instead of delegating it to the assistant managers who take a crackdown on their reporting employees. How painful will it be for that single manager to do that 😕? So consider that as an analogy to 2nd point above. 

How would you import this packages/module within your code? 
 
**Packages:** `from sklearn.ensemble import RandomForestClassifier`  
Here `sklearn` is a package and `RandomForestClassifier` is a module.  

**Modules:** `import pandas`  
Here `pandas` is a module. 

> I hope that was a little bit clearer to understand, and from my experience, if you are a trader, that's the depth you need to know, but if you still prefer to read more, here is an excellent article by  [RealPython.](https://realpython.com/python-modules-packages/)

### Different Methods of installing a Python Package/Module.
Installing a package can be considered the easiest part of all this, but there are two main ways of installing packages.  
`conda install package-name`  
`pip install package-name`

`conda` must sound familiar to you if you have installed **Anaconda Distribution**; it is basically a *cross-platform* and* environment manager*. It also checks the dependency of existing installed packages to decide which versions of new packages to install. *(For, e.g., if your company is acquiring another company and both the companies use different email tech (e.g., Gmail, Outlook), the project manager can decide whether to upgrade/downgrade the email tech to a certain level to manage everyone)*

>What's cross-platform? : It basically means that `conda` is not specifically for installing Python packages; it can be used to install packages written in other languages like C/C++/R.  

> What's environment manager? : It basically means that you can create multiple installations of Python versions within your machine. (Like numerous bank branches in one city)

`pip` can only install Python packages but has more open source packages than `conda` or `conda-forge` (another conda channel)

If you are interested in more differences between `conda` and `pip`, here is a good  [reading.](https://www.anaconda.com/blog/understanding-conda-and-pip) 

### Recommended way of installing a Python Package/Module
Now a common question would be, hey, we have two methods, which one to use?

Well, reading about the different methods above, you might have got an indication of which will be better suited for you; I hope you thought `conda`

To put it frankly, `conda` and `pip` are not competitors, and they have very different use-cases. If interested, you can read more  [here.](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/#:~:text=In%20short%2C%20pip%20is%20a,agnostic%20cross%2Dplatform%20environment%20manager.&text=Conda%20and%20pip%20are%20not,users%20and%20patterns%20of%20use.) 

But if you are a beginner, who doesn't yet intuitively understand the dependencies between modules and packages, let `conda` do the heavy weight-lifting for you. 

There are indeed some disadvantages of `conda`, like you will not find all the packages available on `pip` readily available on `conda`. In that scenario, you will still have to resort to `pip` to install.

To take two examples, I will show you the steps to install a library available on `conda` and the second one, which is not.

1. Installing `matplotlib`, which is a fantastic data visualization package.

- Open your "Anaconda Prompt" from your search menu.
- Type in `conda install matplotlib` and hit Enter.
![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613434546271/2WZeVPCmF.png)
- It will take a few seconds for `conda` to check all the dependencies of the existing packages, and then it should show you results like this asking you to enter "Y/N", just enter **"Y"**
![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613434635443/hlwFrnfhZ.png)
- Once the installation is complete, it should look like this. And that's it your package is installed, we will talk about importing this package in future articles.
![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613434719406/QjmvtKlI_.png)

2. Installing `jugaad-data`, which is an excellent library to download price data from NSE (National Stock Exchange of India) but was recently introduced and is not available via `conda`

- Type in `conda install jugaad-data` and hit Enter.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613434999475/BYbUQJbHb.png)

- As you can see, the package is not available via `conda`, so instead, we now do `pip install jugaad-data` and press Enter in the same prompt window.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613435136622/G2DtZSH6P.png)

- Hopefully, that worked for you. Don't worry if the above image's output does not match your screen; I already had the library installed on my laptop and hence the different output. 

And that's a wrap! I hope you enjoyed this article. If you have any questions, please feel free to leave a comment and consider subscribing to my mailing list for automatic updates on future articles. 📬

If you liked this article, consider buying me a coffee ☕ by  [clicking here](https://www.buymeacoffee.com/tradewithyash)  or the button below.

%%[buymeacoffee-btn]