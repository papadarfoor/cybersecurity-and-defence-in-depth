import random, string,  uuid, os, sys , subprocess
###################### test_samples #########
def random_string():
    str_len=8
    letters = string.ascii_lowercase+ string.digits
    str_temp=''.join(random.choice(letters) for i in range(str_len))
    return str_temp
################## marks #####################
error_massage_mark=1
correct_store_verify_mark=4
correct_notfound_mark=1
############### correct_output_counter ########
num_of_test_cases=5
not_found_cases=3
error_massage_num=[0,3]
correct_store_verify_num=[0,num_of_test_cases*2]
correct_notfound_num=[0,not_found_cases]
################################################
cases=[]
for i in range(num_of_test_cases):
    password=random_string()
    key=random_string()
    secret=random_string()
    result=None
    proc = subprocess.Popen(["python", "porridge_a2.py",
                             "store", password , key, secret] ,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT , stdin=subprocess.PIPE)
    process_output = proc.communicate()[0].decode('utf8').replace('\r\n', '')
    #print(process_output)
    if process_output=="Success":
        result='store'
    cases.append([password,key,secret , result])

########################## verification ########
for i in range(len(cases)):
    itm=cases[i]
    if itm[3]=='store':
        password=itm[0]
        key=itm[1]
        secret=itm[2]
        proc = subprocess.Popen(["python", "porridge_a2.py",
                                 "verify", password, key, secret],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        process_output = proc.communicate()[0].decode('utf8').replace('\r\n', '')
        #print(process_output)
        if process_output == "Verified":
            cases[i][3]="verify"

############# calculate store_verify marks ###########
for itm in cases:
    if itm[3]=='verify':
        correct_store_verify_num[0]=correct_store_verify_num[0] + 2
    if itm[3] == 'store':
        correct_store_verify_num[0]=correct_store_verify_num[0] + 1

############# calculate not_found marks ###########
for i in range(not_found_cases):
    password=random_string()
    key=random_string()
    secret=random_string()
    proc = subprocess.Popen(["python", "porridge_a2.py",
                             "verify", password, key, secret],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process_output = proc.communicate()[0].decode('utf8').replace('\r\n', '')
    if process_output=='Not Found':
        correct_notfound_num[0] = correct_notfound_num[0] + 1

############# calculate error marks ###########

########## ErrorCase1
proc = subprocess.Popen(["python", "porridge_a2.py",
                         "store", key, secret],
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
process_output = proc.communicate()[0].decode('utf8').replace('\r\n', '')
if process_output not in ["Success", "Verified", "Not Found"]:
    error_massage_num[0] = error_massage_num[0] + 1
########## ErrorCase2
proc = subprocess.Popen(["python", "porridge_a2.py",
                         "verify22", password, key, secret],
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
process_output = proc.communicate()[0].decode('utf8').replace('\r\n', '')
if process_output not in ["Success", "Verified", "Not Found"]:
    error_massage_num[0] = error_massage_num[0] + 1
########## ErrorCase3
proc = subprocess.Popen(["python", "porridge_a2.py",
                         "verify", password, key, secret , password],
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
process_output = proc.communicate()[0].decode('utf8').replace('\r\n', '')
if process_output not in ["Success", "Verified", "Not Found"]:
    error_massage_num[0] = error_massage_num[0] + 1
############### calculate final marks ##################
final_mark= correct_store_verify_num[0]/correct_store_verify_num[1] * correct_store_verify_mark \
            + correct_notfound_num[0]/correct_notfound_num[1] * correct_notfound_mark \
            + error_massage_num[0]/error_massage_num[1] * error_massage_mark

print( " Your Store/Verify mark is %d out of %d"%(correct_store_verify_num[0],correct_store_verify_num[1]))
print( " Your Not Found mark is %d out of %d"%(correct_notfound_num[0], correct_notfound_num[1]))
print( " Your Error Handling mark is %d out of %d"%(error_massage_num[0],error_massage_num[1] ))
print("###############################################")

print( "\t Your final mark is %f out of %d"%(final_mark , error_massage_mark +  correct_store_verify_mark + correct_notfound_mark ))

#print(cases)





