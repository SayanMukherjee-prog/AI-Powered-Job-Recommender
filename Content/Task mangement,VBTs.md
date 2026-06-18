**Using Tasks in ServiceNow**



A task is any record that can be assigned to or completed by a user in the Platform. They are updated as the work defined by the task is completed (moved to a Closed state). Tasks can be assigned to specific users or user groups.  



If you can recall from the Lists \& Filters and Forms lessons, you can access data through records. Each record lives in a table in the Platform. The Task \[task] table is one of the core tables and provides a series of standard fields used on each of the tables that extend it ("child" tables that come from the "parent" table), such as the Incident \[incident] and Problem \[problem] tables. 



**Assignments**



In the Platform, you will experience task assignment through Users, Groups, and Roles. Every user (that's you!) can be assigned to a group. It's not good practice to assign roles to individual users. For organizational practices, it's best to assign roles to a group that contains users.



To gain a better understanding of who is assigned what in the Platform, select the left and right arrows below.



Users can belong to more than one group. Every user belonging to a group inherits that group's roles. They can be assigned permissions to: 



Approve, change, or resolve incidents and requests



Provide a reference for alerts and notifications



Receive email notifications



**My Work/My Groups Work**



The Service Desk application menu allows you to locate all work assigned to your group(s) or to you. 



The "itil" role (what you are assigned in the Platform for this course) is required to access the My Work (All > Service Desk > My Work) and My Groups Work (All > Service Desk > My Groups Work) modules in the Service Desk application.





My Work: list of all active tasks assigned to you, including:



Change Request



Group Approval



Incident



Knowledge Base Submission



Request



Security Case



Visual Task Boards

My Groups Work: list of all active tasks assigned to your group(s) but not yet assigned to an individual.



**User Presence**



The User Presence feature facilitates synchronous collaboration within one record. See who is online, view their current status, and what they are viewing or editing, all in real-time. 



Imagine a scenario in which you are viewing a critical issue documented in a Priority-1 record. User, Beth Anglin, needs to view and update the record simultaneously. That's where user presence comes in! The number of active viewers is listed in the form header. If only one additional user is viewing the record (as seen above), their avatar in the Platform will appear. Let's take a look and see how Beth edits the record while you are viewing it.



Real-Time Editing



Edit records in real time and see edits saved by other users, improving collaborative efforts. Real-time editing is an extension of User Presence. It allows you to work with others on the same record, indicating their state (editing or viewing). You can view the fields that are being edited, indicated by a "pulse" icon. Beth Anglin has just assigned the incident to herself. 



To keep up with what is changing in a record, select the Show Activity Stream icon to jump to the record Activity section, which includes the record history and updates by you and other viewers. You can see in the Notes section, that Beth has assigned the record to herself, and the state of the record has changed from New to In Progress.



\------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



**Work Notes and Additional Comments**



On a record, you can use the Notes tab to communicate to stakeholders and document task activities throughout the task's lifecycle. The Show all journal fields icon allows you to display multiple fields under the Notes tab, including Work notes and Additional Comments.



Once enabled, you can then select the Show one journal field icon to only display the Work notes field. If the Work notes field is the only field displayed, you may select the Additional Comments (Customer visible) checkbox (not shown below, but you may practice this in your instance). Otherwise, the customer will not be able to see what you posted. 



Work notes



This field provides a way to document all the technical and behind-the-scenes work on a task. Upon saving, Work notes are recorded in the record Activity section, where they can be viewed by users with permissions to view the record. Work notes are only visible to internal users and are not available to external users or customers.



Additional comments (Customer visible)



This field provides a way to communicate with the requester and other stakeholders directly in ServiceNow. For example, you may want the customer to stay up to date of progress on their record or request additional information. 



Upon saving, the additional comments (including updated information and comments history) are emailed directly to the requester. When the requester receives an email notification containing additional comments, they can reply to the email, and their feedback will also be documented in the Activity log of the record! Additional comments are also visible on the record in the Service Portal and Employee Center.



**Activity section** 



The Activity section located under the Notes tab provides a complete history of a record, from creation through closure. It details who made an update, what the update was, and when the update was made. Selecting the filter (funnel) icon allows activity information to be filtered, based on your desired categories of information. 



The Activity section, which is read-only, documents when a change was made and by whom. These changes include assignment and reassignment, additional comments and work notes, updated field values, state changes, and more. 



**Activity Stream inline editing** 



The Activity Stream inline editor enables users to contribute to work within a record without opening a form. Just like real-time editing on a form, inline commenting on the activity stream means you can annotate records as updates are made, allowing multiplied efforts across several pieces of work simultaneously. To do so, navigate to a list of active task records, then follow the steps below. 



1

Select the Show Activity Stream icon and it will appear in a flyout window from the list header. 



2

With the window open, scroll down to browse the records recently updated and hover over an update you wish to comment, then select Comment. 



3

Enter your comment into the text field, (select the checkbox for Work Notes or Additional comments (Customer visible) if applicable), then select the Post button. 



\------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





**Visual Task Boards**



Transform your lists and forms into an interactive graphical experience using Visual Task Boards (VTBs). Visual Task Boards allow you to: 



* Manage tasks through a visual, drag-and-drop interface
* Identify process bottlenecks at a glance, in real-time
* Track embedded activity screens to view updates all in one place



Quick panel

Displays the active participants, or assignees that appear on the board, depending on the data presented. 



Taskboard tools

The Taskboard tools area provides a way to filter tasks by title or number. It also is where you can view information about the VTB, add or view members, add or filter labels, show activity stream, and select configurations for the VTB. 



Lanes

Depending on how the data is sorted, the lanes will separate each card into different categories. You may drag and drop cards from one lane to another. 

For example, the lanes in this board are sorted by the State of the Incident. 



Cards

Task records from a list, presented with a short description, task number, when it was updated, and who it's assigned to. 



Show all / Change boards

Select this 4-square icon to show all VTBs  you own or belong to (have access to). 

Select the downward arrow to choose which board you would like to view and/or work on. 

This area also displays the title of the VTB.



VTBs can have a number of functions in the Platform. You may use them to create a personal to-do list, collaborate in real-time with group members on assignments, and more! Displayed graphically as lanes and cards, VTBs provide a landing page to view and organize work in ServiceNow. There are two types of VTBs: Freeform and Data Driven. Select the left and right arrows to view a description of each. 



**Different types of VTBs**



Freeform: Use Freeform boards as your personal organizer, creating individual tasks of any kind and freely adding, removing, and modifying cards and lanes. You may change the title of your lanes created in a Freeform board.

&#x20;

Data Driven: Allows you to add tasks to a flexible or guided task board. Create filters to display specific records from a table. You may not change the title of lanes presented in a Data Driven Board.



**Show a VTB from a list**



You may create a VTB from a list view by selecting a few records (or all records, as seen below), selecting the Actions on selected rows dropdown menu, and then selecting Add to Visual Task Board. 



You may also show a VTB from a list view, by breaking up data for whichever column the VTB is created from. All you have to do is select Column options (from any column) and select Show Visual Task Board. 



To change the title of a VTB, you may double-click the title, and hit Enter on your keyboard (or click anywhere else on the board) when done.



To get started with a VTB, navigate to All > Self-Service > Visual Task Boards and follow the displayed instructions for creating your first board. 

