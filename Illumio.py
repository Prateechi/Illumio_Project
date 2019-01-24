import os
import pandasql as ps
#os.chdir("..") # Directory level goes one up

class Firewall:

    def __init__(self):
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        pass
    
    def solve(self, rules):
        df = pd.read_csv("/MyProjects/Data/net_data.csv",sep=",")
        df["start_port"] = df.apply(lambda row:row["port"].split("-")[0] if "-" in row["port"] else row["port"],axis=1)
        df["end_port"] = df.apply(lambda row:row["port"].split("-")[1] if "-" in row["port"] else row["port"],axis=1)
        df["start_ip"] = df.apply(lambda row:row["ip"].split("-")[0] if "-" in row["ip"] else row["ip"],axis=1)
        df["end_ip"] = df.apply(lambda row:row["ip"].split("-")[1] if "-" in row["ip"] else row["ip"],axis=1)
        df = df.merge(df["start_ip"].apply(lambda row: pd.Series({'start_ip_1':row.split(".")[0], 'start_ip_2':row.split(".")[1], 'start_ip_3':row.split(".")[2], 'start_ip_4':row.split(".")[3]})),left_index=True, right_index=True)

        df = df.merge(df["end_ip"].apply(lambda row: pd.Series({'end_ip_1':row.split(".")[0], 'end_ip_2':row.split(".")[1], 'end_ip_3':row.split(".")[2], 'end_ip_4':row.split(".")[3]})),left_index=True, right_index=True)
        
        for input_rule in rules:
            print(input_rule)
            q1 = self.getQuery(input_rule)
            print(q1)
            filtered_df = ps.sqldf(q1, locals())
            if(filtered_df.empty):
                print(False)
            else:
                print(True)

    def getQuery(self, input_rule):
        return """SELECT * FROM df WHERE  direction = '""" + input_rule[0] + """' and protocol = '""" + input_rule[1] + \
            """' and start_port <= '""" + str(input_rule[2]) + """' and end_port >= '""" + str(input_rule[2]) + \
            """' and start_ip_1 <= '""" + input_rule[3].split(".")[0] + """' and end_ip_1 >= '""" + input_rule[3].split(".")[0] +\
            """' and start_ip_2 <= '""" + input_rule[3].split(".")[1] + """' and end_ip_2 >= '""" + input_rule[3].split(".")[1] +\
            """' and start_ip_3 <= '""" + input_rule[3].split(".")[2] + """' and end_ip_3 >= '""" + input_rule[3].split(".")[2] +\
            """' and start_ip_4 <= '""" + input_rule[3].split(".")[3] + """' and end_ip_4 >= '""" + input_rule[3].split(".")[3] +\
            """'"""


input_rule_1 = ("outbound", "tcp", 10234, "192.168.10.11")
input_rule_2 = ("inbound", "tcp", 80, "192.168.1.2-192.168.1.2-192.168.1.2")

input_rules = [input_rule_1,input_rule_2]

obj = Firewall()
obj.solve(input_rules)
