# Python Bridge Tools

This repository holds tools I am creating to help me check bridge structural designs and details.

## Bridge Grades

The bridge grades tool helps calculate grades along a roadway alignment. It currently accounts for horizontal alignments, vertical alignments, and superelevation transition calculations along the profile grade line. The plan is to add bridge elements to the alignment, so calculations can be made at various locations along a bridge to help establish pier geometry and aid in vertical clearance calculations.

## Seismic Ground Motion Data

This tool aids in building a web query to get sesimc response spectrum data from the [USGS Design Ground Motions Website](https://earthquake.usgs.gov/hazards/designmaps/). Currently the tool only handles queries for the 2009 AASHTO  Guide Specifications for LRFD Bridge Design and outputs basic seismic data to determine the seismic category and a plot of the response spectrum.

Documentation for the query and json output can be found on the [USGS documentation page for AASHTO 2009](https://earthquake.usgs.gov/ws/designmaps/aashto-2009.html).

![Example Response Spectrum Graph](/Documentation/Seismic/ExampleResponseSpectrumGraph.png)

[Example Response Spectrum Generated from Query Data](https://earthquake.usgs.gov/ws/designmaps/aashto-2009.json?latitude=34&longitude=-118&siteClass=C&title=Example)


## Soil Boring Analysis

I've started creating some basic tools to help me load boring log files I receive from geotechnical engineers. This will eventually lead to some basic soil classification and seismic design calculations.

## Future Tools I Would Like to Add

    1. Plate girder properties
    2. Rolled steel shapes library
    3. AASHTO LRFD steel and concrete design calculations

## Requirements

The seismic ground motion data tool uses **matplotlib** to generate the response spectrum plot. The package can be installed using pip from the command line.

```
    pip install matplotlib
```

## References
[USGS Design Ground Motions Website](https://earthquake.usgs.gov/hazards/designmaps/)