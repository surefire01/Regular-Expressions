import re
user_name = {}
Errors_dic = {}
        
def usernames(s):
    user = re.search(r" \(([\w.]*)\)$", s.strip())
    un = user.groups()[0]
    if un not in user_name:
        user_name[un] = {}
    if re.search(r"ERROR", s.strip()) == None:
        user_name[un]["info"] = user_name[un].get("info",0) + 1         
    else:
        user_name[un]["error"] = user_name[un].get("error",0) + 1
    
def errors(s):
    result = re.search(r"ERROR ([\w ']*)", s.strip())
    if result == None : pass
    else:
        a = result.groups()[0].strip()
    
        if a not in Errors_dic:
            Errors_dic[a] = 1
        else:
            Errors_dic[a] += 1
    
with open("./new.log") as log:
    for i in log.readlines()[1:]:
        usernames(i)
        errors(i)
        
user_name_items = sorted(user_name.items())
errors_items = sorted(Errors_dic.items(), key = lambda x : x[1], reverse = True)

with open("./error_message.csv","w") as ecsv:
        ecsv.write("Error,Count\n")
        for i in errors_items:
                ecsv.write(i[0]+","+str(i[1])+"\n")

with open("./user_statistics.csv","w") as u_csv:
        u_csv.write("Username,INFO,ERROR\n")
        for i in user_name_items:
                u_csv.write(i[0] + "," + str(i[1].get("info",0)) + "," +  str(i[1].get("error",0)) + "\n")
        

    
