logo = """
  ____                  _   _   _                         _____                           _             
 |  _ \                | | | \ | |                       / ____|                         | |            
 | |_) | __ _ _ __   __| | |  \| | __ _ _ __ ___   ___  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  _ < / _` | '_ \ / _` | | . ` |/ _` | '_ ` _ \ / _ \ | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |_) | (_| | | | | (_| | | |\  | (_| | | | | | |  __/ | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |____/ \__,_|_| |_|\__,_| |_| \_|\__,_|_| |_| |_|\___|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                                                                                                                               
"""

print(logo)
print("Welcome to the band name generator")
town = str(input("what is the name of you'r hometown?\n"))
pet = str(input("what was the name of you'r pet growing up?\n"))
band = town + ' ' + pet
print("the name of you'r band could be '{}'.".format(band))
