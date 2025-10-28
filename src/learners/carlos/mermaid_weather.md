flowchart TD
    A[Uppsala weather station] --> |?| B[Display]
    A[Uppsala weather station] --> |?| C[Graph]
    B --> D[Statistics]
    B --> E[filter options]
    E --> H[date range]
    E --> J[temperature range]
    E --> K[location]
    B --> I[button to submit]
    C --> F[pychart]
    C --> G[histogram]
    H --> C
    J --> C
    K --> C

# Extended version with classes

classDiagram
     Statistics <| -- DataLoader
     Figures <| -- Statistics
     DownLoader <| -- Statistics

     UserInterface <| -- Figures
     UserInterface <| --  Statistics
     UserInterface <| -- DownLoader




     class DataLoader {
        + read_table()
        + file_exists()
        + validate_raw_data()
     }

     class Statistics {
         + get_mean_value()
         + get_std_value()
     }

     class Figures {
        + make_lineplot()
        + make_histogram()
        + make_scatterplot()
     }

     class DownLoader {
        + write_to_disk()
     }

     class UserInterface {
        + filter_data()
        + range_data()
        + plot_data()
        + download_data()
     }
     

     
