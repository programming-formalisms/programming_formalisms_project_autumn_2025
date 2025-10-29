# Requirements Discussion
1.	Website - GitHub
2.	Filter & view options
2.1. based on time
2.2. based on date
2.3. based on region (next version)
3.	Plot - time series
3.1. Time series
3.2. Histograms with box plots
4.	Statistics
4.1. Average
4.2. Minimum
4.3. Maximum
4.4. Median
4.5. Mode
5.	Download
  5.1. Raw data
  5.2. Filtered data
  5.3. Plots
  5.4. Statistics
6. Read data
  6.1. load formatted data
  6.2. be able to read _raw data_
  6.3. choose station to analyse

<!-- markdownlint-disable MD013 -->


| Requirement ID | Requirement Description | Acceptance Criteria | Test Case |
|----------------|--------------------------|---------------------|------------|
| 1 | Website - GitHub | The website should be accessible via GitHub Pages and load without errors. The repository must contain all necessary source files, documentation, and version control history. | Verify that the site is published through GitHub Pages, loads correctly in browsers, and that all links and assets function properly. |
| 2 | Filter & view options | Users can select multiple filters and view the corresponding data without page reloads. Filters must be clearly labeled and persist during navigation. | Apply different filters and confirm that displayed data changes according to the selected options. |
| 2.1 | Filter based on time | User can filter data by specific time ranges such as hourly, daily, or monthly intervals. | Select different time intervals and ensure only data within those periods is shown. |
| 2.2 | Filter based on date | User can specify a custom date or date range to limit the dataset displayed. | Enter various date inputs and verify that the output adjusts accordingly. |
| 2.3 | Filter based on region (next version) | The system must allow users to select data based on a predefined list of regions. Disabled or hidden in current release. | In upcoming version, choose a region and confirm that only region-specific data is shown. |
| 3 | Plot - time series | The platform should present time series plots that update dynamically with filter changes. Plots must be visually clear and labeled. | Change filters and confirm that the time series plot updates and displays accurate trends. |
| 3.1 | Time series plots | Time series data should display using appropriate axes, legends, and tooltips. | Inspect the chart to ensure correct x/y axes labeling and accurate data points. |
| 3.2 | Histograms with box plots | Users can select histogram or box plot visualizations for selected metrics. | Switch between histogram and box plot modes and confirm accurate statistical representation. |
| 4 | Statistics | The system should provide key statistical metrics for selected datasets. | Verify that metrics update dynamically when filters change. |
| 4.1 | Average | The mean value of the selected dataset should be computed and displayed. | Compare computed average against manual calculation. |
| 4.2 | Minimum | Minimum value should automatically update based on filtered dataset. | Apply filters and verify minimum value accuracy. |
| 4.3 | Maximum | Maximum value should update dynamically for the current selection. | Filter dataset and check computed maximum matches raw data. |
| 4.4 | Median | Median should correctly represent the middle value within the filtered dataset. | Calculate median manually and compare against displayed result. |
| 4.5 | Mode | Most frequent value should be displayed for selected criteria. | Confirm that displayed mode matches actual data frequency. |
| 5 | Download | Users must be able to download data and visual outputs in selectable formats. | Check all download options function properly and produce valid files. |
| 5.1 | Download raw data | Provide full dataset download option (e.g., CSV format). | Click download and verify the file contents match the full dataset. |
| 5.2 | Download filtered data | Provide download of data after filters are applied. | Apply filters, download filtered data, and confirm it reflects current view. |
| 5.3 | Download plots | Enable exporting plots as image or PDF. | Export a plot and confirm correct formatting and data accuracy. |
| 5.4 | Download statistics | Enable exporting computed statistics as a text or CSV file. | Download statistics and confirm values match those shown on the interface. |
| 6 | Read data | Enable reading of source CSV files into variable names | Confirm parameters like dates and temperature with the colunmns of file | Read the file, define the variables from the right column of the resulting matrix (using the meta file)  |
| 6.1 | load data into program | Enable reading the existing Uppsala CSV file into variable names |Read the file, define the variables from the right column of the resulting matrix (using the meta file `*.txt`)  |
| 6.2 | be able to read _raw data_ | Enable reading combined meta data and columns from raw files with filename with station number, not name | Read the file, define the variables from the right column ignoring the meta data |
| 6.3 | choose station to analyse  | Enable choosing the right file by connecting station name with station number according to lookup table| Give the sation name and the correct file is loaded. |
