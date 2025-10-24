- As a researcher I want to see temperature by time and by region.
- Users can select a time range (e.g., past 24 hours, last 7 days).
- Users can select a region from a map or dropdown.
- The app displays a time-series chart of temperature for the selected region.
- Data updates correctly when filters are changed
- 




| Requirement ID | Requirement Description | Acceptance Criteria | Risk Type | Risk Description | Probability (P1–P5) | Severity (S1–S5) | Risk Value (P×S) | Action |
|----------------|--------------------------|---------------------|-----------|------------------|---------------------|------------------|------------------|--------|
| REQ-001 | The app shall allow researchers to view temperature data by time and region | The plot should be rendered in less than 5 seconds | Business | Incomplete or slow data rendering | P3 | S3 | 9 | Optimize chart performance and validate data availability |
| REQ-001.1 | | Wrong time delivered | Technical | Getting e.g., pm instead of am | P3 | S4 | 12 |  |
| REQ-001.2 | | Wrong temperature | Technical |  | P | S |  |  |
| REQ-002 | Users shall be able to select a time range (e.g. past 24 hours) | Time range selector is available and functional | Technical | API may not support full historical range | P4 | S2 | 8 | Limit time range options and cache recent data |
| REQ-003 | Users shall be able to select a region from a map or dropdown | Region selector is intuitive and functional | Business | Confusing UI or selection errors | P2 | S2 | 4 | Improve UX with tooltips and onboarding |
| REQ-004 | The app shall display a time-series chart of temperature for the selected region | Chart renders correctly with labeled axes and data points | Technical | Chart rendering may lag or misrepresent data | P3 | S3 | 9 | Use efficient chart libraries and test with sample data |
| REQ-005 | Data shall update correctly when filters (time or region) are changed | Data refreshes within 5 seconds of filter change | Technical | Delayed or failed data refresh | P4 | S4 | 16 | Add fallback logic and retry mechanisms |
| REQ-006 | Load the data into a database | The dataframe should not contain any missing value | Technical | Missing or malformed data during ingestion | P3 | S4 | 12 | Validate and clean data before loading |
