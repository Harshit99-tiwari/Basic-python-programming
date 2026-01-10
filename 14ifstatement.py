is_engineer=True


if is_engineer :
    print("you are an engineer")

else:
    print("you are a student")


is_human=False
is_male=True

if is_human or is_male:
    print("he is human or he is male or both male and human")

else:
    print("he is animal")

is_human=True
is_male=True

if is_human or is_male:
    print("he is human or he is male or both male and human")

else:
    print("he is animal")


is_player=True
is_artist=False

if is_player and is_artist:
    print("he has multiple skill")
else:
    print("you are unskilled")

is_player=False
is_artist=True

if is_player and is_artist:
    print("he has multiple skill")
elif is_player and not(is_artist):
    print("he is a player only")
elif not(is_player) and is_artist:
    print("you are an artist")
elif not(is_player and is_artist): 
     print("you are looser")
else:
    print("you are unskilled")


