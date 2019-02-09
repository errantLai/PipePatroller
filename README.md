# PipePatroller
Pipe Patroller is an IoT system that looks at deploying sensors along stretches of water pipes, providing a wealth of data about humidity, temperature, and gas pressure about the pipe and its surrounding area. This up-to-date time-series information allows for more accurate predictions of a pipe’s lifespan, changing along with the environment. We can use this data to evaluate the condition of pipes new and old, and opens the door for a proactive approach to repair rather than being simply reactive. It was submitted to Hackatown 2019, and won 3rd place (as well as best domain name). 
 
We read sensor data from an arduino sensor package, processing that information and rendering it with Grafana. We then write queries and displays that take advantage of the time-series nature of the data to slice data across time, and identify the nodes most at risk. 

Full details at: [https://devpost.com/software/pipepatroller](https://devpost.com/software/pipepatroller)
