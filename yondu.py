members = "hello"
while True :
    if members.isdigit() != True :
        members = input("How many many pirates: \n")
    else :
        tokens = input("How many units: \n")
        if (tokens.isdigit() == True):
            members = int(members)
            tokens = int(tokens)
            break

tokens = tokens - ((members - 2) * 3 )
yondu_cut = round(tokens * 0.13, 2)
tokens = tokens - yondu_cut
quill_cut = round(tokens * 0.11, 2)
tokens = tokens - quill_cut
individual_split = round(tokens / members, 2) 
yondu_cut = yondu_cut + individual_split
quill_cut = quill_cut + individual_split
individual_split = individual_split  + 3
print("\nYondu's share: " + '%.2f' %yondu_cut)
print("Peter's share: " + '%.2f' %quill_cut)
print("Crew's share: " + '%.2f' %individual_split)