import sqlite3
import pandas as pd
import streamlit as st

conn = sqlite3.connect('blog.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS posts (author TEXT NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL, date DATE NOT NULL)')
conn.close()
c.close()

# Define a function to add a new post
def add_post(author, title, content, date):
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        # Create a cursor object
        c = conn.cursor()
        # Insert a new row into the posts table
        c.execute('INSERT INTO posts (author, title, content, date) VALUES (?,?,?,?)', (author, title, content, date))
        # Save the changes to the database
        conn.commit()
        # Close the connection and the cursor
        conn.close()
        c.close()
    except sqlite3.Error as e:
        # Print the error message
        print(e)


# Define a function to get all the posts
def get_all_posts():
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        # Create a cursor object
        c = conn.cursor()
        # Select all the rows from the posts table
        c.execute('SELECT * FROM posts')
        # Fetch all the results
        data = c.fetchall()
        # Close the connection and the cursor
        conn.close()
        c.close()
        # Return the data
        return data
    except sqlite3.Error as e:
        # Print the error message
        print(e)


# Define a function to get a post by title
def get_post_by_title(title):
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        # Create a cursor object
        c = conn.cursor()
        # Select the row from the posts table that matches the title
        c.execute('SELECT * FROM posts WHERE title=?', (title,))
        # Fetch the result
        data = c.fetchone()
        # Close the connection and the cursor
        conn.close()
        c.close()
        # Return the data
        return data
    except sqlite3.Error as e:
        # Print the error message
        print(e)


# Define a function to delete a post
def delete_post(title):
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        # Create a cursor object
        c = conn.cursor()
        # Delete the row from the posts table that matches the title
        c.execute('DELETE FROM posts WHERE title=?', (title,))
        # Save the changes to the database
        conn.commit()
        # Close the connection and the cursor
        conn.close()
        c.close()
    except sqlite3.Error as e:
        # Print the error message
        print(e)

# Test the functions
add_post('Alice', 'Hello World', 'This is my first post', '2021-01-01')
add_post('Bob', 'Streamlit Rocks', 'This is my second post', '2021-01-02')
add_post('Charlie', 'Python is Awesome', 'This is my third post', '2021-01-03')
print(get_all_posts())
print(get_post_by_title('Streamlit Rocks'))
delete_post('Hello World')
print(get_all_posts())



How to Create a Blog App with Python in Minutes using Streamlit
A. J. S. Raja Ravi Varman
A. J. S. Raja Ravi Varman

·
Follow

9 min read
·
Dec 8, 2023

Listen


Share

Do you have a passion for writing and sharing your thoughts and ideas with the world? Do you want to create your own blog, but don’t know how to code or set up a website? If so, you might be interested in Streamlit, a Python framework that lets you build beautiful and interactive web apps in minutes, without any front-end experience.

Streamlit is an open-source project that aims to make data exploration and visualization easy and fun. With Streamlit, you can turn your data scripts into web apps with just a few lines of code. You can also add widgets, charts, maps, tables, and more to your app with Streamlit’s simple and intuitive API. And the best part is, you don’t have to worry about writing HTML, CSS, JavaScript, or setting up a server. Streamlit handles all the web magic for you, so you can focus on your content and creativity.

In this blog post, I will show you how to create a simple and elegant blog app with Streamlit and Python. You will be able to create, view, search, and manage blog posts using a SQLite database. You will also be able to see some statistics and visualizations of the posts and authors. The blog app will look something like this:

Blog App using Streamlit
Blog App using Streamlit
You can access the demo at https://sampleblog.streamlit.app/

Prerequisites
To follow along with this tutorial, you will need the following:

Python 3.6 or higher installed on your system.
Streamlit and its dependencies installed on your system. You can install it with pip install streamlit or follow the instructions on their website.
A code editor of your choice. I recommend Visual Studio Code or PyCharm.
A basic understanding of Python and Streamlit. If you are new to Streamlit, you can check out their documentation or tutorials for more guidance.
Step 1: Create a database
The first step is to create a database to store the blog posts and their details. We will use SQLite, a lightweight and self-contained database engine that does not require any installation or configuration. SQLite stores the data in a single file, which makes it easy to manage and backup.

To create a database, we will use the sqlite3 module, which is a built-in Python library that provides an interface to SQLite. We will also use the pandas module, which is a popular Python library for data analysis and manipulation. We will import these modules at the top of our Python script:

# Import sqlite3 and pandas
import sqlite3
import pandas as pd
Next, we will create a connection object that represents the database. We will use the connect function, which takes a file name as an argument. If the file does not exist, it will be created automatically. We will name our file blog.db:

# Connect to the database
conn = sqlite3.connect('blog.db')
Then, we will create a cursor object, which allows us to execute SQL commands on the database. We will use the cursor method of the connection object:

# Create a cursor object
c = conn.cursor()
Finally, we will create a table to store the blog posts and their details. We will use the execute method of the cursor object, which takes a SQL statement as an argument. We will name our table posts, and define four columns: author, title, content, and date. We will use the TEXT and DATE data types for the columns, and specify that they cannot be NULL. We will also use the IF NOT EXISTS clause, which ensures that the table is only created if it does not exist already:

# Create a table if not exists
c.execute('CREATE TABLE IF NOT EXISTS posts (author TEXT NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL, date DATE NOT NULL)')
That’s it for creating the database. We can close the connection and the cursor objects using the close method:

# Close the connection and the cursor
conn.close()
c.close()
Step 2: Define some functions for interacting with the database
The next step is to define some functions that will allow us to interact with the database. We will need four functions: one to add a new post, one to get all the posts, one to get a post by title, and one to delete a post. We will use the same modules and objects as before, and wrap them in try-except blocks to handle any errors. We will also use the commit method of the connection object to save the changes to the database.

The first function is add_post, which takes four arguments: author, title, content, and date. It inserts a new row into the posts table with the given values, using the INSERT INTO statement:

# Define a function to add a new post
def add_post(author, title, content, date):
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        # Create a cursor object
        c = conn.cursor()
        # Insert a new row into the posts table
        c.execute('INSERT INTO posts (author, title, content, date) VALUES (?,?,?,?)', (author, title, content, date))
        # Save the changes to the database
        conn.commit()
        # Close the connection and the cursor
        conn.close()
        c.close()
    except sqlite3.Error as e:
        # Print the error message
        print(e)
The second function is get_all_posts, which takes no arguments. It returns a list of all the rows in the posts table, using the SELECT * statement:

# Define a function to get all the posts
def get_all_posts():
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        # Create a cursor object
        c = conn.cursor()
        # Select all the rows from the posts table
        c.execute('SELECT * FROM posts')
        # Fetch all the results
        data = c.fetchall()
        # Close the connection and the cursor
        conn.close()
        c.close()
        # Return the data
        return data
    except sqlite3.Error as e:
        # Print the error message
        print(e)
The third function is get_post_by_title, which takes one argument: title. It returns a single row from the posts table that matches the given title, using the WHERE clause. If no match is found, it returns None:

# Define a function to get a post by title
def get_post_by_title(title):
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        # Create a cursor object
        c = conn.cursor()
        # Select the row from the posts table that matches the title
        c.execute('SELECT * FROM posts WHERE title=?', (title,))
        # Fetch the result
        data = c.fetchone()
        # Close the connection and the cursor
        conn.close()
        c.close()
        # Return the data
        return data
    except sqlite3.Error as e:
        # Print the error message
        print(e)
The fourth function is delete_post, which takes one argument: title. It deletes the row from the posts table that matches the given title, using the DELETE statement:

# Define a function to delete a post
def delete_post(title):
    try:
        # Connect to the database
        conn = sqlite3.connect('blog.db')
        # Create a cursor object
        c = conn.cursor()
        # Delete the row from the posts table that matches the title
        c.execute('DELETE FROM posts WHERE title=?', (title,))
        # Save the changes to the database
        conn.commit()
        # Close the connection and the cursor
        conn.close()
        c.close()
    except sqlite3.Error as e:
        # Print the error message
        print(e)
That’s it for defining the functions for interacting with the database. We can test them by adding some dummy posts and printing the results:

# Test the functions
add_post('Alice', 'Hello World', 'This is my first post', '2021-01-01')
add_post('Bob', 'Streamlit Rocks', 'This is my second post', '2021-01-02')
add_post('Charlie', 'Python is Awesome', 'This is my third post', '2021-01-03')
print(get_all_posts())
print(get_post_by_title('Streamlit Rocks'))
delete_post('Hello World')
print(get_all_posts())


# Define some HTML templates for displaying the posts
title_temp = """
<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h4>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
<h6>Author: {}</h6>
<br/>
<br/>
<p style="text-align:justify"> {}</p>
</div>
"""

post_temp = """
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h4>
<h6>Author: {}</h6>
<h6>Date: {}</h6>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;">
<br/>
<br/>
<p style="text-align:justify"> {}</p>
</div>
"""


# Create a sidebar menu with different options
menu = ["Home", "View Posts", "Add Post", "Search", "Manage"]
choice = st.sidebar.selectbox("Menu", menu)

# Display the selected option
if choice == "Home":
    st.title("Welcome to my blog")
    st.write("This is a simple blog app built with streamlit and python.")
    st.write("You can view, add, search, and manage posts using the sidebar menu.")
    st.write("Enjoy!")
elif choice == "View Posts":
    st.title("View Posts")
    st.write("Here you can see all the posts in the blog.")
    # Get all the posts from the database
    posts = get_all_posts()
    # Display each post as a card
    for post in posts:
        st.markdown(title_temp.format(post[1], post[0], post[2][:50] + "..."), unsafe_allow_html=True)
        # Add a button to view the full post
        if st.button("Read More", key=post[1]):
            st.markdown(post_temp.format(post[1], post[0], post[3], post[2]), unsafe_allow_html=True)
elif choice == "Add Post":
    st.title("Add Post")
    st.write("Here you can add a new post to the blog.")
    # Create a form to get the post details
    with st.form(key="add_form"):
        author = st.text_input("Author")
        title = st.text_input("Title")
        content = st.text_area("Content")
        date = st.date_input("Date")
        submit = st.form_submit_button("Submit")
    # If the form is submitted, add the post to the database
    if submit:
        add_post(author, title, content, date)
        st.success("Post added successfully")
elif choice == "Search":
    st.title("Search")
    st.write("Here you can search for a post by title or author.")
    # Create a text input to get the search query
    query = st.text_input("Enter your query")
    # If the query is not empty, search for the matching posts
    if query:
        # Get all the posts from the database
        posts = get_all_posts()
        # Filter the posts by the query
        results = [post for post in posts if query.lower() in post[0].lower() or query.lower() in post[1].lower()]
        # Display the results
        if results:
            st.write(f"Found {len(results)} matching posts:")
            for result in results:
                st.markdown(title_temp.format(result[1], result[0], result[2][:50] + "..."), unsafe_allow_html=True)
                # Add a button to view the full post
                if st.button("Read More", key=result[1]):
                    st.markdown(post_temp.format(result[1], result[0], result[3], result[2]), unsafe_allow_html=True)
        else:
            st.write("No matching posts found")
elif choice == "Manage":
    st.title("Manage")
    st.write("Here you can delete posts or view some statistics.")
    # Create a selectbox to choose a post to delete
    titles = [post[1] for post in get_all_posts()]
    title = st.selectbox("Select a post to delete", titles)
    # Add a button to confirm the deletion
    if st.button("Delete"):
        delete_post(title)
        st.success("Post deleted successfully")
    # Create a checkbox to show some statistics
    if st.checkbox("Show statistics"):
        # Get all the posts from the database
        posts = get_all_posts()
        # Convert the posts to a dataframe
        df = pd.DataFrame(posts, columns=["author", "title", "content", "date"])
        # Display some basic statistics
        st.write("Number of posts:", len(posts))
        st.write("Number of authors:", len(df["author"].unique()))
        st.write("Most recent post:", df["date"].max())
        st.write("Oldest post:", df["date"].min())
        # Display a bar chart of posts by author
        st.write("Posts by author:")
        author_count = df["author"].value_counts()
        st.bar_chart(author_count)
