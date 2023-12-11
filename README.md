# iMoney
##### Version 0.1
##### Author - Leo Amora Sousa
### Video Demo: <https://youtu.be/8Ix4UHLUWiY>
> A simple expense tracker to manage your transactions.

![Static Badge](https://img.shields.io/badge/version-0.1.1-orange)

![](/static/model.png)
![](/static/model2.png)

## Project Overview
This project is a website expense tracker manager where can add and delete Incomes, like salary, rewards and others, and Expenses, like credit card, food, transport and others, and manage them into a historic overview.
Website has a register or login phase to set up some users to use website. Each user could add an income, some cash entrance to your account, or add an expense, some cashout to your account. For both, describe what is the income/expense item, value, when was made it and the category.
Once added, users can see a resume about your transactions, to manage better and see a global vision about it, in history page. At this page, describes all of your income and expenses. If you write something wrong of income or expense specifc, you can delete the row and add again.

## Login/Register Pages
At homepage, two buttons are showed, a Login and Register. Both works similary. If you don't have an account yet you register with an username and a password (you need confirm that field) and if you already have an account you login with username and password registered.

## Add an Income/Expense Pages
At these pages, as name says, you can add an income or an expense to history of logged user. You must complete all four fileds in these pages: description, where you describe what income or expense is; value, how much this item cost or enter to your account; date, when your did this income or expense and; category, to define which category is your income or expense. When you click at ADD button, the website get datas, add into database.

## History Page
At this page we can see all transactions made it and added into website for the specifc user. Each option (row of table) can be deleted if you wrote wrong.

## Database
The main database has two tables: one for registered users with 3 fileds: id, username and password. Last one is hashed to avoid hacker password information. second table is a tracker where get all transactions of all users, so here we have 6 columns: id of transaction; user id, an foreign key of logged user; description of item; value that costs or enter in your account; date, when this occured; category of income or expense; and type, if was an income or expense. The last one is to work in backend and organize calcs of total amount showed in history page.

## Static codes
At this project we have an style.css, to change font and other stuffs of pages; and a script.js to specifically change categories of incomes and expenses to alphabetic order.

## Requirements
This projects use Flask, a web framework. Flask-Session, to work between some users registered at website. cs50 library to manage conncetions between program and SQLite.

## Release History

* 0.1.0
    * The first proper release
* 0.0.1
    * Work in progress

## Contact
Leo Amora – leoamora94@gmail.com

