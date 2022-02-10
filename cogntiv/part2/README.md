# Part 2: Data pipeline System Design Document

## Background
Design the architecture (components and flows) for a data pipeline for machine learning research in the cloud. No need to implement anything, only design it. Assume this data pipeline serves only research (and not production) purposes, i.e. it has low scale, few users, no significant load or latency requirements.

## Requirements

### Functional 
- Each day 10 recording sessions occur. Each recording session results in one folder which includes binary data files and a text file that houses its meta-data. With total size of 600 MB per session.
- The data needs to be uploaded to the cloud (AWS S3), once there, the meta-data for each recording session should
be added to a database. The raw data is the most valuable, so should be stored in such a way as could be easily
accessed, but not erased mistakenly.
- Once uploaded, a data preprocessing flow should be triggered only on the new data resulting in preprocessed data.
- Clients should then be able to query the database, and should receive a list of preprocessed data files matching the query criteria. Finally these preprocessed data files must be accessible on an AWS EC2 node for use.
- Assume each recording session is stored in a local directory with a date-string of the time it was recorded (e.g.
20210229_161221)
- Assume meta-data has both numerical variables (e.g. level of subject fatigue), and text variables (e.g. hardware
model)
- Data flow
    - Define the mechanism of how data will be uploaded to S3
    - Define how metadata vs. binary data will be stored

### Non-Functional
- Database(s)
    - Select a database solution
    - Motivate your choice
    - Describe in detail how data will be stored
    - Define how and who will query the database, and how
- Error handling
    - Describe automation of all of the data pipeline steps
    - Define which steps will have “sanity checks”, and define what they will be
    - Define a system for handling errors and logging information/errors, both in the cloud and to a local client
- Deliverables
    - Diagram of your architecture.
    - Definition of each processing step along the way.
    - Short written descriptions of each choice of technology (e.g. database).

## System APIs
Reduce Complexity

## High Level Design
Define main componance and data flows 

## Detailed Design 
Design the main components (OOD can help)

## Analysis
- Cost
- Security
- Reliability
- Performance Efficiency
- Operation Excellence