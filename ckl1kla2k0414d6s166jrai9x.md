## Which Programming Language To Learn as a Trader?

#### Introduction 
Hi There 😀
I know what you must be thinking right now; this is a "Python For Traders" blog. Clearly the answer to this article will be "Python" 🤦
Nope, let me stop you right there; the idea of this article is to give you the pros and cons of the most famous languages used in the Trading World so you can make that decision for yourselves because everyone is unique and there is no defined path to success and no specific programming language will print you endless 💸 (even if you get dreams about it, I do! I am sure you secretly do as well)

You'll find this post insightful if you are:
1. A trader who is trying to automate your strategies but not sure which language to learn.
2. A student or someone who would like to pursue a quant developer/analyst role.

**So before taking up any more of your precious time, let's dive right in!**

### Python
Sorry, but I couldn't resist starting with the language that gave me wings in my professional career. 
Python was born in 1980; it has witnessed unimaginable growth and has a library to do almost anything. Python is the most wanted language according to the [Stack Overflow Developer Survey
](https://insights.stackoverflow.com/survey/2020#technology-most-loved-dreaded-and-wanted-languages-wanted) 

#### Pros of Python
- Extremely easy to learn with tons of resources available.
- Many statistical libraries (Pandas, Numpy, Backtrader, TA-Lib) act as a backbone for all trading algos.
- Has a vast developer community for support when you are stuck or need new ideas.
- Every major stock broker/data vendor will have an API that Python can use.
- Cross-Platform Language, You can run your algos on Windows, Linux, Raspberry Pi, etc.
- Quick development speed to build a prototype and generally fewer code lines involved compared to other languages.
- Interactive Interpreter to write programs quickly.

#### Cons of Python
- It is not the fastest performing language out there, especially when speed execution matters a lot to your algos.
- It uses a lot of memory to do tasks due to its object-oriented approach. So if you are working with large datasets with lots of variables, you may run out of memory on a low spec laptop.
- Once you get used to Python, you get hooked to it, and it isn't easy to transition to another language with the same level of community and extensive libraries.
- MultiThreading does not work like a charm as you would except for financial algorithms.

### Java
Like Python, Java is also a solid veteran in the programming space. Java also has a wealth of open source projects which everyone can use for free. Java is meant to be a WORA (Write Once Run Anywhere) Language.

#### Pros of Java
- Has a wide variety of statistical and financial libraries.
- Generally faster and efficient than Python since it is a compiled language.
- Every major stock broker/data vendor will have an API that Java can use via Java.
- Cross-Platform Language, You can run your algos on Windows, Linux, Raspberry Pi, etc.
- Has a huge developer community for support when you are stuck or need new ideas.

#### Cons of Java
- It is a relatively complex language, and there is a learning curve involved.
- It does not have very intuitive GUI development libraries (a key metric if you are developing strategies for someone else who doesn't code)
- It also requires significant memory space, which adversely affects the performance of the code.

### C#/C++
C# (pronounced: see sharp) was developed by Microsoft and was launched within the .Net framework; for the sake of demonstrating different types of languages, I will combine C# and C++, although there are notable differences between the two. C# is generally considered a modern version of C++.

#### Pros of C#/C++
- C++ is the fastest language considered in trading algorithms and is generally used by enterprises to develop scalable models. This is also heavily used in High-Frequency Trading, whereas the other modules wouldn't do that great. 
- C# can leverage the full power of the .NET Framework developed by Microsoft.
- Every major stock broker/data vendor will have an API that C# can use.
- It is very memory efficient as compare to other modern alternatives.

#### Cons of C#/C++
- C++ is a very complicated language to learn.
- C++/C# requires much more code lines; hence the time to development will also be much larger when creating strategies.
- C# being developed by Microsoft is heavily dependent on the Windows framework, and now more companies are hosting their programs on a Linux environment since it's cheap.

### Julia
Julia is a high-level, high-performance, dynamic programming language. While it is a general-purpose language and can be used to write any application, many of its features are well suited for numerical analysis and computational science. (Source:  [Wikipedia](https://en.wikipedia.org/wiki/Julia_(programming_language))

Although I have never used Julia personally, the consensus is that it combines both Python and C++, which is considered as best of both worlds.

#### Pros of Julia
- Solves the Two Language Problem, i.e., you can create scalable algorithms/applications which can be developed quickly and deployed without worrying about performance and efficiency.
- Julia is written in Julia and C, so there are no dependencies to run it anywhere; it can run even on the smallest computers out there.

#### Cons of Julia
- It being still a relatively new language, the developer community is far smaller than the other languages mentioned in this article.
- Less number of packages and libraries available to create algorithms/programs.
- Most of the major stock brokers/data vendors do not support it at the moment. 

*There is an excellent article on algorithmic trading by Julia Computing, I would recommend checking it out  [here](https://juliacomputing.com/blog/2017/08/algorithmic-trading/)*

These were the programming languages I had wanted to discuss, although **I am nobody** to tell you which language to use, your choice should depend on your use-case. Here are some closing points on why I would choose each language.

- I would use Python or Java if I am a beginner and want to explore algorithmic trading and data science since they have vast communities and lots of packages and libraries for each use case.
- I would use C++/C# purely if I am developing enterprise-level algorithms for someone developing an HFT Algo as speed is of the essence.
- I would use Julia to explore what it can offer as I think it will be much more widely used in the future since it can quickly build scalable products without compromising speed. Julia is still 5-10 years behind where Python is, but it would be good to learn as a future skill.

I hope you enjoyed the article, do let me know which languages you use for trading and financial purposes. *All constructive criticism welcome in comments*🧐

If you liked this article, consider buying me a coffee ☕ by  [clicking here](https://www.buymeacoffee.com/tradewithyash)  or the button below.

%%[buymeacoffee-btn]

