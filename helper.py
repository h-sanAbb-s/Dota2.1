def main():
    """This is helper function. It will assist the website for authentication etc"""
    print(hashed_password("abcABZ"))

def checkuser(users, username, password):
    for i in users:
        print(i["username"], type(i["username"]), i["password"], type(i["password"]), username, password)
        if i["username"] == username and hashed_password(i["password"]) == password:
            return None, i["value"]
    
    return "Invalid username/password", 0


def get_challenges(challenges):
    my_challenge = []
    if challenges == None:
        return []
    for challenge in challenges:
        challenge_dict = {}
        challenge_dict["challenger_username"] = challenge[0]
        challenge_dict["hero_name"] = challenge[1]
        challenge_dict["hero_id"] = challenge[2]
        challenge_dict["gold"] = challenge[3]
        challenge_dict["challenger_id"] = challenge[4]
        challenge_dict["challenge_id"] = challenge[5]
        challenge_dict["item_name"] = challenge[6]
        challenge_dict["item_id"] = challenge[7]
        my_challenge.append(challenge_dict)

    return my_challenge


def merge_items_by_challenge(challenges):
    items_by_challenge = {}
    
    for challenge in challenges:
        challenge_id = challenge['challenge_id']
        if challenge_id not in items_by_challenge:
            items_by_challenge[challenge_id] = {
                'challenger_username': challenge['challenger_username'],
                'hero_name': challenge['hero_name'],
                'hero_id': challenge['hero_id'],
                'gold': challenge['gold'],
                'challenger_id': challenge['challenger_id'],
                'challenge_id': challenge_id,
                'item_1_id': challenge['item_id'],
                'item_1_name': challenge['item_name'],
                'item_2_id': None,
                'item_2_name': 'None',
                'item_3_id': None,
                'item_3_name': 'None'
            }
        else:
            if items_by_challenge[challenge_id]['item_2_id'] is None:
                items_by_challenge[challenge_id]['item_2_id'] = challenge['item_id']
                items_by_challenge[challenge_id]['item_2_name'] = challenge['item_name']
            elif items_by_challenge[challenge_id]['item_3_id'] is None:
                items_by_challenge[challenge_id]['item_3_id'] = challenge['item_id']
                items_by_challenge[challenge_id]['item_3_name'] = challenge['item_name']
    
    merged_challenges = list(items_by_challenge.values())
    
    return merged_challenges

def calculate_attributes(hero, item_1, item_2, item_3):
    """
    """
def difference_of_lists(list1, list2):
    if len(list1) == None:
        return []
    if len(list2) == None:
        return list1
    list_1 = []
    list_2 = []
    for i in list1:
        list_1.append(i[0])
    for i in list2:
        list_2.append(i[0])
        
    set2 = set(list_2)
    
    result_list = [item for item in list_1 if item not in set2]
    
    return result_list

def get_tradeOffers(offers_list):
    offers = []
    if offers_list == None:
        return offers
    for offer in offers_list:
        offer_dict = {}
        offer_dict["user_id"] = offer[0]
        offer_dict["hero_id"] = offer[1]
        offer_dict["offerer_username"] = offer[2]
        offer_dict["hero_name"]=offer[3]
        offer_dict["gold"] = offer[4]
        offer_dict["status"] = offer[5]
        offer_dict["offered_to"] = offer[6]
        offers.append(offer_dict)
    return offers

def get_users(user_list):
    users = []
    if user_list == None:
        return []
    for i in user_list:
        user_dict = {}
        user_dict["user_id"] = i[0]
        user_dict["gold"] = i[1]
        user_dict["username"] = i[2]
        users.append(user_dict)

    return users

def get_items_by_ids(items):
    itemlist = []
    if len(items) == None:
        return None, itemlist
    for i in items:
        itemlist.append(i[0])
    if isinstance(itemlist, set):
        itemlist = list(itemlist)

    placeholders = ', '.join(['%s'] * len(itemlist))
    
    query = f"SELECT * FROM items WHERE item_id IN ({placeholders})"

    return query, itemlist


def get_heroes(hero_list):
    heroes = []
    if len(hero_list) == None:
        return heroes
    for item in hero_list:
        hero_dict = {
            'hero_id':item[0],
            'heroname': item[1],
            'description': item[3],
            'health': item[4],
            'armor': item[5],
            'attackspeed': item[6],
            'damage': item[7],
            'cost': item[2]
        }
        heroes.append(hero_dict)
    return heroes
def get_items(item_list):
    items = []
    if item_list == None:
        return items
    for item in item_list:
        item_dict = {
            'item_id':item[0],
            'name': item[1],
            'description': item[5],
            'health': item[2],
            'armor': item[4],
            'attackspeed': item[7],
            'damage': item[3],
            'cost': item[6]
        }
        items.append(item_dict)
    return items
def get_list(list1):
    if list1 == None:
        return []
    list_1 = []
    for i in list1:
        list_1.append(i[0])

    return list_1
def get_history(history_list):
    duels = []
    if history_list == None:
        return []
    for item in history_list:
        duel_dict = {
            'username': item[2],
            'opponent': item[3].capitalize(),  
            'date': str(item[5]),  
            'time': item[4], 
            'result': item[7],
            'exchange': item[6]
        }
        duels.append(duel_dict)
    return duels

def get_npc(npclist):
    npc = []
    if npclist == None:
        return []
    for i in npclist:
        npc_dict = {}
        npc_dict['name'] = i[2]
        npc_dict['gold'] = i[1]
        npc_dict['time'] = i[3]

        npc.append(npc_dict)

    return npc
def hashed_password(password):
    """This will encrypt user's password"""
    mapped = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_password = ""
    for i in password:
        if i.isalpha():
            if i.isupper():
                index = alphabets.index(i.lower())
                new_password += mapped[index].upper()
            elif i.lower():
                index = alphabets.index(i)
                new_password += mapped[index]
        
        else:
            new_password += i

    return new_password
            


if __name__ == "__main__":
    main()
