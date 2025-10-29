# The Uppsala Weather package

Analysis on data from an Uppsala weather station.

## About
This project is based of the works of [Bergström and Moberg Bergström and Moberg 2002](https://www.smhi.se/download/18.6ae791dc18fc9e7539e1121c/1717658901728/Bergstr%C3%B6m_Moberg_Uppsala.pdf), using the [Uppsala "dygnsvärdes" temperature data](https://www.smhi.se/data/temperatur-och-vind/temperatur/uppsalas-temperaturserie).

With this package, you'll be able to compute statistics such as median, mean, standard deviation, etc., as well as produce charts of temporal changes in temperature in Uppsala, from the 1st of December 1722 to the 31st of December 2022. You can also download the data and implement different filtering schemes. 

## Getting started

First follow the [Installation instructions](). 

To find the data in this repository you can go [here](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2025/tree/about/data). The program can take either `csv` or `dat` formats.

The most common arguments used would be:

- `--input` the input data
- `--output` the path and base name of the output file.
- `--temp` path to a temporary folder
- `--version` current version
- `--filter` here you give a string of filtering parameters. For example, if you want from year 1800 to 1900, you can say `--filter x1800,y1900`.

```
$ uppweather -h

$ uppweather --input data/uppsala_tm_1722-2022.dat --output results/myresults --temp temp --filter
```
