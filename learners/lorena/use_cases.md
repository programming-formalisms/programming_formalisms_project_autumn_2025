- As a researcher I want to see temperature by time and by region.
- Users can select a time range (e.g., past 24 hours, last 7 days).
- Users can select a region from a map or dropdown.
- The app displays a time-series chart of temperature for the selected region.
- Data updates correctly when filters are changed
- 

| Requirement ID | Requirement Description | Acceptance Criteria |
|----------------|--------------------------|---------------------|
| REQ-001 | The app shall allow researchers to view temperature data by time and region | The plot should be rendered in less than 5 seconds |
| REQ-002 | Users shall be able to select a time range (e.g. past 24 hours) | Time range selector is available and functional |
| REQ-003 | Users shall be able to select a region from a map or dropdown | Region selector is intuitive and functional |
| REQ-004 | The app shall display a time-series chart of temperature for the selected region | Chart renders correctly with labeled axes and data points |
| REQ-005 | Data shall update correctly when filters (time or region) are changed | Data refreshes within 5 seconds of filter change |
| REQ-007 | Load the data into a database | The dataframe should not contain any missing value |