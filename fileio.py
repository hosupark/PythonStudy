
# testfile = open("hello.py", "r", encoding = "utf8")
# lines = testfile.readlines()
# for line in lines:
#     print(line, end="")
    
# testfile.close() 


# import pickle

# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["골프", "수영", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()


# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
    
    
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("열심히 공부하자.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())