**What is Platform Analytics?**



ServiceNow data can be viewed and analyzed (in real-time or over time) by you and your colleagues. Data can be visually represented in many ways, including bar charts, pie charts, dials, lists, pivot tables, donuts, and more. 



Visualizations can be run manually or scheduled to run automatically. There are a range of predefined visualizations that pertain to applications and features like Incident Management and Service Catalog requests, including Key Performance Indicator (KPI) charts. 



You can create your own visualizations by navigating to All > Platform Analytics > Analytics Center module. From there, you may select Create new dashboard or Create New visualization. 



Alternatively, you can simply select most column context menus in any list to generate a visualization directly from the data in that list. Visualizations are interactive, in that users with access can drill down into the data to view and manipulate the underlying records.



**Real world use cases**



* HR may use reports to measure average Benefits Case load by assignee during open enrollment
* An agent needs to have evidence of his performance managing cases over the last quarter in preparation for his quarterly review
* Management needs to have a report automatically generated and delivered to her division for all P1 incidents that happened overnight
* Vendor management needs to see a quarterly roll up of Service level compliance of their third-party service providers



**Types of visualizations**



In the activity below, you will see how to access the Visualization Designer and see all the different types that are available to build your visualization. You may follow along in your instance by navigating to All > Platform Analytics > Analytics Center, then select Create new visualization.



Alternatively, you can navigate to All > Platform Analytics > Library > Data Visualizations, then select New (which is the path shown in the example below). 



**Step in the activity**



1. In the Create new visualization window, select Add data source.
2. Adding a data source: Search for and select the Incident table to be the data source. To drill down into the list of incidents, select Incidents. Open under predefined conditions. Then, select Run to refine the list of open incidents. Select Add this source.
3. Configuration panel: In the configuration panel, you may select different options for headers and borders, data sources and additional settings, metrics, presentation, display settings, legend, colors, and chart interactions.
4. Select visualization type: For the visualization type, use the drop-down menu to select any of the following visualization types. Below you see an example of Pies.
5. Time Series: Visualize data over time. 
6. Multidimensional charts: Visualize data using multiple dimensions.
7. Scores: Visualize a single data point



**Advantages of the Visualization Designer**



In the next section, you will have the opportunity to explore the Visualization Designer in greater detail. Here are just a few advantages to using it! 



* Leverage visibility and available visualization types
* Use multi-level filters, filter operators, and sort order to refine data presentation
* View, create, edit, and schedule visualizations



\------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



**Data Visualization configurations**



The Data Visualizations module contains a library of visualized data which you can run and use to create your own custom visualizations. Many of these visualizations came with the Platform and others can be created by your administrators specifically for your company. 



The Data Visualizations page contains different sections for visualizations which are visible to different audiences. 



All visualizations

Here you may filter by bookmarked, certified, owned by me, shared with me, or all visualizations available to you to your groups in the Platform.



Search by name or description

Search for and select existing visualizations in the Platform.



Edit columns

Select the columns you'd like and arrange how they're ordered.



Records per page

Select the amount of records per page you would like to view. You can select 10, 15, 20, 50, or 100 rows per page. 



Create a new visualization

Select New to select data, type, configure, and style options for your visualization. 



**Create and edit visualizations**



Select New to create a new visualization or select an existing chart available to you. Each section of the Visualization Designer provides different configuration options. Below, you will see an example chart called Configuration Item Types. You may view this chart in your instance to play around with the existing data. 



Type

Type allows you to select the visualization of your report by choosing a chart type. There are scores, time series, bars, pies and donuts, multidimensional charts, and more!

There are over 20 chart types to choose from! All you have to do is select which style is appropriate for your report. 



Data

Data provides a name for the report. Here you can also select the source from where (which ServiceNow table) your data comes from. You may also select metrics, different grouping or sorting options, and additional updates. 



Collapse or expand a configuration field

Select the caret symbol to expand or collapse any label in the configuration panel. You may select from:



* Visualization type
* Header and border
* Data
* Data Sources
* Metric
* Group by
* Sorting
* Data update
* No data message
* Presentation
* Display settings
* Legend
* Data label
* Colors
* Chart interaction



**Creating charts from a list**



So far we've discussed building charts from scratch, but it is often easier to start with a filtered list or an existing visualization. Let's see how to perform this in the ServiceNow AI Platform. 



1. Define and run a filter, displaying only the data to illustrate . In the example below, we are filtering the list of all open incidents separated by Priority. Then, we ran the filter.
2. Select the Column Context Menu for the Priority field, and choose Bar Chart or Pie Chart (whichever works best for you). In the example, we chose to generate a pie chart. 



**Visualization Designer: actions and options** 



Different actions become available once the visualization has been saved and they depend on your role



Add to Dashboard

Select this button to add the chart to a dashboard.



Save

Don't forget to save your work! It's a good idea to save after changing any of the configurations.



Configuration panel

Select this icon to open or close the configuration panel for a closer look at the chart.



Details

Review details about the chart including the name, description of the chart, and information on its creator.



**Share or distribute a chart**



When distributing a visualization, sharing has the ability to make the chart visible to authenticated users within ServiceNow.



Add to Dashboard

By selecting this option, you must first Save the chart you created. Then, you may select whether to add this visualization to a new or existing dashboard.



NOTE: You first need to have access to a dashboard(s) to add a visualization to it. 



Additional sharing options

By selecting the More actions menu, you can create, duplicate, share, export, schedule, delete, or add the visualization as a bookmark.



**Advantages to modifying an existing chart**



In the last section, we reviewed some advantages to using the Visualization Designer. Below are some advantages to editing or modifying an existing chart. 



* You can start with a chart that already has the basic information and make minor changes to get what you need
* Browsing existing visualizations helps you learn which of the tables are relevant to the work you do
* Helps you learn different uses for the various chart types
* You can leverage best practices by using Key Performance Indicator (KPI) charts



\------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



**Platform Analytics vs. one-time reporting**



You may be wondering what the difference between Platform Analytics (PA) and building a one-time visualization is in the ServiceNow AI Platform. When you build a chart from data in a table, (for example, Incident or Problem), information about the current state of the Platform data displays. Platform Analytics provides information about performance iteratively, over time for data visualizations and dashboards. 



Create management dashboards, report on KPIs and metrics, and increase quality and reduce the costs of service delivery through Platform Analytics. Visit ServiceNow Product Documentation to learn more! 



**Dashboards**



Dashboards enable you to display multiple Platform Analytics, data visualizations, lists, and other widgets on a single screen. Use dashboards to create a story with data that can be shared. Dashboards can be responsive or non-responsive. Responsive dashboard functionality is enabled by default. Non-responsive dashboards have limitations including who can create, view, and edit them. 



With dashboards, you can:



* Share Platform Analytics and data visualizations on both Workspaces and Core Platform dashboards
* Create and edit Platform Analytics data and other widgets directly from the dashboard
* Use the Add new element button to quickly find and preview widgets, then add them to the dashboard
* Easily share dashboards with other users from the integrated sharing pane
* Use quick layouts to snap widgets into a predefined layout, then adjust the layout as desired
* Set dashboards as your homepage so you can quickly access information that you use frequently 



**Create a dashboard**



Navigate to All > Self-Service > Dashboards to view dashboards in the ServiceNow Platform. View recent dashboards, bookmarked or certified ones, dashboards owned by you, shared with you, or all available dashboards in your instance. You may also filter and search for certain dashboards by name. In this course instance, you can see examples of existing dashboards that were created by the System Administrator. To create your own, select Create new dashboard. 



Step 1: Name and Create New

Select In-line editor to begin, then give your dashboard a name and description (if applicable) of your choice. Then, select Create new dashboard.



Step 2: Populate your dashboard

In the next section, you will see the different parts of the dashboard interface and how to add new elements. 



**Populate your dashboard** 

Similar to the Visualization Designer, you can customize your dashboard(s).The parts of a dashboard are:



Edit dashboard name

Select this icon to modify the name of your dashboard.



Add a tab

Select Add a tab to populate your dashboard with additional tabs to section off data.



Dashboard settings

Here you can refresh the data, schedule repetition, enable data cache, show refresh information, and configure presentation settings.



View Dashboard details

Viewing dashboard details allows you to change the name, description, certification, visibility, and user access.



Save

Save your dashboard.



Edit mode

Select this button to enter or exit editing mode. Select Edit mode to be able to configure the name, settings, tabs, and elements. Select Exit editing mode to view the dashboard as a regular viewer.



Add new element

Here you may choose from a list to add:



* Data visualizations
* Filters
* Heading
* Image
* List - Simple
* Process Mining - Map
* Rich text



More actions

Select any of the following options: Create new, Duplicate, Share, Printer friendly, Clear all filters, Add to bookmarks, Open record, or Delete.



Configuring widgets

In order to configure a widget, simply select the top of it and your cursor will change into a crosshair (not pictured here). You may increase/decrease the height, refresh it, edit the widget, or remove it. You may also add elements above, below, or either side of it.

