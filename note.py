gender = str(input("what's your gender")).lower()
print(gender)
if gender == "male":
    print("You are a He/Him")
elif gender == "female":
    print("You are a She/Her")
else:
    print("invalid request")