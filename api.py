import requests
import re

def getUsrId(usr):
    try:
        return requests.get(usr).text.split("money&target=mail")[1].split("&")[0]
    except IndexError:
        print("Closed profile")

def getInfoFriend(id, token):
    infoById = requests.get("https://api.vk.com/method/users.get?user_id=" +
    id + "&" + "access_token=" + token + "&v=5.131").text.split('"')
    return(infoById[7] + " " + infoById[11])


def getStatus(id, token):
    a = requests.get("https://api.vk.com/method/status.get?user_id=" +
    id + "&" + "access_token=" + token + "&v=5.131").text.split("[")
    return(a[0][21:-3])


def getGroupsCount(id, token):
    a = requests.get("https://api.vk.com/method/groups.get?user_id=" +
    id + "&" + "access_token=" + token + "&v=5.131").text.split("[")
    regexp = re.compile("\d+")
    return(regexp.findall(a[0])[0])

        
def main():
    token = "INSERT_YOUR_TOKEN_HERE"
    usrInp = input("Write user id or user page link (for example https://vk.com/fqusl): ")
    if len(usrInp.split("/")) <= 1:
        usr = getInfoFriend(str(usrInp, token))
        usrId = usr
    else:
        usr = getInfoFriend(getUsrId(str(usrInp)), token)
        usrId = getUsrId(str(usrInp))

    print("Status of " + str(usr) + ": " + getStatus(usrId, token) + "\n")
    print("Amount of " + str(usr) + " groups: " + getGroupsCount(usrId, token))


if __name__ == "__main__":
    main()
