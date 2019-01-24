# Illumio_Project

README:

Steps to run file:
1. Save the files illumio.py and net_data.csv on the same destination. 
2. In code line 11, change the directory accordingly.
3. Make sure all the libraries mentioned in code are vaialble.
4. On the terminal, run the python file illumio.py. 

File “net_data.csv” is a file having valid rules.
File “illumio.py” is the code file .

I have used a dataframe and pandasql implementation to parse the data and evaluate results accordingly.

The code first reads the csv file and interpret data, i.e, it will try to find out when the range in port and IP address. 
The SQL query will further divide the port and IP address into parts: start_port and end_port and start_ip_1, start_ip_2, start_ip_3, start_ip_4, end_ip_1, end_ip_2, end_ip_3, end_ip_4

Eg: 192.168.1.1   => start_ip_1 : 192,  start_ip_2 : 168, start_ip_3 : 1,  start_ip_4 : 1

If the format matches which the given formats, the result will be printed as “True” else “False”.

I tried this approach keepng in mind the time and space complexity. Plus, this method allows us to evaluate theports and IP address properly as we know the lexical order of the inputs,ie, we know the sequence: direction, protocol, port and IP address. 

If the data wasn't in a particular order, machine learning approach would have to applied to recognize the inputs accordingly and put them in an order in the dataframe. 

Later on, we can use Spark SQL for fast implementation on large datasets. Spark SQL is used for structred data processing.

I tried to solve the problem in about an hour. Apart from 2 sample inputs given in the code, I tried changing the port and IP address values of the inputs and it gave results accordingly.
