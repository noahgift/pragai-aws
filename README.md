# pragia-aws
Chapter on AWS for Pragmatic AI


## Devops Essentials

### CloudFormation

Template in JSON or Template

What is DevOps?

Feedback Loop:

Developers -- Customers (Feedback Loop)

build -- test -- release 
plan  <-- Monitor

DevOps Teams:
How organisations process information:
Pathologica -- Bureacratic -- Generative

Traditional Teams:
* Previously, changes could take 4-6 weeks.

Modern Teams:  Autonomous Teams
* Build, Test, Deploy, Run, Support

Continous Delivery:

* A lot like a factory/assembly
* Software is always ready to release

### Setup of IAM User

devops-test-user


### Static Website


### Code Pipeline

* Automate your release process
* establish a consistent release process
* speed up delivery while improving quality
* use your favorite tools
* View progress at-a-glance


### Spot Instances

https://aws.amazon.com/ec2/spot/spot-tutorials/

- Typically between 50-60% savings.
- Need to

* Scientific Researchers
* Financial Services
* Video/Image processing companies
* Web Crawling/data processing
* Spot for Testing, Load testing, etc

- Queue based architectures or checkpointing
- Batch Processing

Bidding for On-Demand price is most common.

## How to Manage Interruptions

Architectures:

- Hadoop/EMR based
- Checkpointing
    * Write state out to a location
- Grid
    * Starcluster

- Queue-Based
    * requeue a job
