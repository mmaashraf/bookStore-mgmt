# bookStore-mgmt
As of now ,it allows the user to manage (Create,Read,Delete,Update )his inventory details. The file is stored on the local machine.

<h1>What Inspired this?</h1>
<p>
I was already familiar with creating web applications, but I was curious to experiment with creating desktop applications. I chose Tkinter because it is cross-compatible with popular operating systems like macOS, Windows, and Linux.

Another reason I wanted to explore desktop applications is that they allow data to be stored locally, rather than in the cloud. I wanted to demonstrate that CRUD (Create, Read, Update, Delete) operations are possible with desktop applications.

<h1>What it does?</h1>
For this project, I targeted a simple use case: storing records of books, which would include the author, title, ISBN, and year published.
At the time of creating this, I incorporated the following functionalities, 
Create Records, Update Record, Delete Record, View All records, and Search for matching records.

</p>
<br><hr>

  
<h1>This is how the Application looks like ! </h1>

**1. On Lauch**

<img width="745" alt="Screenshot 2023-08-22 at 5 33 09 PM" src="https://github.com/mmaashraf/bookStore-mgmt/assets/37049007/9afa8190-52d6-40fe-9a70-5a825c0e767c">
<hr>
**2. View All records **

Click "View All" button to retrieve all the records from DB.
<img width="770" alt="Screenshot 2023-08-22 at 5 34 02 PM" src="https://github.com/mmaashraf/bookStore-mgmt/assets/37049007/4ee6cff5-722a-4963-9a9e-b80093f0c5ea">
<hr>
**3. Search for matching record**

Can query using the Title or author or year or ISBN. Used a OR matching for different fields. It will return records whose fields match the input.
<br>
For sake of demonstration, I added the following record. 

<img width="763" alt="Screenshot 2023-08-22 at 5 43 39 PM" src="https://github.com/mmaashraf/bookStore-mgmt/assets/37049007/4b7416ce-2559-4c6b-868e-aa6b1ab1fb5b">
<br>
Let's search for author "charles". 

<img width="763" alt="Screenshot 2023-08-22 at 5 44 49 PM" src="https://github.com/mmaashraf/bookStore-mgmt/assets/37049007/46b68ce5-2008-49c2-bc34-5c6ebd89f6dd">
<hr>
**4. Add a record**

Enter the details using the fields provided
<img width="763" alt="Screenshot 2023-08-22 at 5 37 35 PM" src="https://github.com/mmaashraf/bookStore-mgmt/assets/37049007/f39ad3fe-2826-4a80-9744-30b24c097c31">
<br>
Click on "add a book" button to save to DB.
<img width="763" alt="Screenshot 2023-08-22 at 5 37 51 PM" src="https://github.com/mmaashraf/bookStore-mgmt/assets/37049007/39ffabdb-58ff-4e9b-b484-8f1ae3ccbded">
<br>
It commits to the db, and refresh the list on the left to show the updated records.

<hr>
**5. Update a record**

Let's update the record of the book i added in point number 4. 
Select the records from the text box on the left; And Change the title to Sample Edition-2. 
and hit the "update selected" button.

<img width="763" alt="Screenshot 2023-08-22 at 5 47 38 PM" src="https://github.com/mmaashraf/bookStore-mgmt/assets/37049007/0378d3fb-5bf7-4f4a-ad95-2bcabadb9247">

<br>
<img width="763" alt="Screenshot 2023-08-22 at 5 47 49 PM" src="https://github.com/mmaashraf/bookStore-mgmt/assets/37049007/79167dbc-6d5c-46a8-802f-0c4259664f6b">

<hr>
**6. Delete a record**

Let's delete by selecting the John Doe record.
<img width="763" alt="Screenshot 2023-08-22 at 5 52 08 PM" src="https://github.com/mmaashraf/bookStore-mgmt/assets/37049007/0c7afe22-0c12-4e21-8591-b7401c55da4e">

As you can see, it no longer exists.
<img width="763" alt="Screenshot 2023-08-22 at 5 52 17 PM" src="https://github.com/mmaashraf/bookStore-mgmt/assets/37049007/44f8e854-982e-4379-9a4e-d56c129756e6">

<br><hr>
<h1> How to run?</h1>

Just clone the repository, and run the command in your terminal "python frontend.py"
