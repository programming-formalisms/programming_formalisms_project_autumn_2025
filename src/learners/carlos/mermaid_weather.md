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
