import DECODING_PROCESS

sm_1=DECODING_PROCESS.decoded_data_1
sm_2=DECODING_PROCESS.decoded_data_2
sm_3=DECODING_PROCESS.decoded_data_3
sm_4=DECODING_PROCESS.decoded_data_4



group1=sm_1
group2=sm_2
group3=sm_3
group4=sm_4
count1=group1.count("$")
count2=group2.count("$")
count3=group3.count("$")
count4=group4.count("$")
counts=count1+count2+count3+count4
check=0
secret_message = ""
for i in range(0,counts):
    check=check+1
    #print(check)
    if(check==1):
        x=group1.find('$')
        secret_message+=group1[:x]+' '
        var=group1.replace(group1[:x+1],'')
        group1=var
    if(check==2):
        x=group2.find('$')
        secret_message+=group2[:x]+' '
        var=group2.replace(group2[:x+1],'')
        group2=var
    if(check==3):
        x=group3.find('$')
        secret_message+=group3[:x]+' '
        var=group3.replace(group3[:x+1],'')
        group3=var
    if(check==4):
        x=group4.find('$')
        secret_message+=group4[:x]+' '
        var=group4.replace(group4[:x+1],'')
        group4=var
        check=0

if(group1.endswith('#')):
    x=group1.find('#')
    secret_message+=group1[:x]
elif(group2.endswith('#')):
    x=group2.find('#')
    secret_message+=group2[:x]
elif(group3.endswith('#')):
    x=group3.find('#')
    secret_message+=group3[:x]
elif(group4.endswith('#')):
    x=group4.find('#')
    secret_message+=group4[:x]
print(secret_message)
