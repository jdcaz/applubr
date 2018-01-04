init python:
    from time import time    
    import datetime    

    class cl_utility:
        def convert_ap_to_time(self, i_ap):
            if i_ap == 48:
                return "07:00"
            elif i_ap == 47:
                return "07:30"
            elif i_ap == 46:
                return "08:00"
            elif i_ap == 45:
                return "08:30"
            elif i_ap == 44:
                return "09:00"
            elif i_ap == 43:
                return "09:30"
            elif i_ap == 42:
                return "10:00"  
            elif i_ap == 41:
                return "10:30"
            elif i_ap == 40:
                return "11:00"
            elif i_ap == 39:
                return "11:30"
            elif i_ap == 38:
                return "12:00"
            elif i_ap == 37:
                return "12:30"
            elif i_ap == 36:
                return "13:00"    
            elif i_ap == 35:
                return "13:30"
            elif i_ap == 34:
                return "14:00"
            elif i_ap == 33:
                return "14:30"
            elif i_ap == 32:
                return "15:00"
            elif i_ap == 31:
                return "15:30"
            elif i_ap == 30:
                return "16:00"  
            elif i_ap == 29:
                return "16:30"
            elif i_ap == 28:
                return "17:00"
            elif i_ap == 27:
                return "17:30"
            elif i_ap == 26:
                return "18:00"
            elif i_ap == 25:
                return "18:30"
            elif i_ap == 24:
                return "19:00"   
            elif i_ap == 23:
                return "19:30"  
            elif i_ap == 22:
                return "20:00"
            elif i_ap == 21:
                return "20:30"
            elif i_ap == 20:
                return "21:00"
            elif i_ap == 19:
                return "21:30"
            elif i_ap == 18:
                return "22:00"
            elif i_ap == 17:
                return "22:30"      
            elif i_ap == 16:
                return "23:00"
            elif i_ap == 15:
                return "23:30"
            elif i_ap == 14:
                return "00:00"
            elif i_ap == 13:
                return "00:30"
            elif i_ap == 12:
                return "01:00"   
            elif i_ap == 11:
                return "01:30"  
            elif i_ap == 10:
                return "02:00"
            elif i_ap == 9:
                return "02:30"
            elif i_ap == 8:
                return "03:00"
            elif i_ap == 7:
                return "03:30"
            elif i_ap == 6:
                return "04:00"
            elif i_ap == 5:
                return "04:30"  
            elif i_ap == 4:
                return "05:00"
            elif i_ap == 3:
                return "05:30"
            elif i_ap == 2:
                return "06:00"
            elif i_ap == 1:
                return "06:30"  
            else:
                return "07:00"
        
        def get_location_text(self, location1, char1):
            if location1==char1.fname + "_room":
                return "my room"
            elif location1=="pool":
                return "the pool"
            elif location1=="beach":
                return "the beach" 
            elif location1=="workout":
                return "the gym"
            else:
                return location1





    class cl_data_topics:   
        
        def __init__(self):
            self.topics = []
            
            l_topic_lines = cl_topic_lines_new("films")                        
            self.topics.append(l_topic_lines)             
            
            l_topic_lines = cl_topic_lines_new("shopping")                        
            self.topics.append(l_topic_lines)            
            
            l_topic_lines = cl_topic_lines_new("sports")                      
            self.topics.append(l_topic_lines)
            
            l_topic_lines = cl_topic_lines_new("music")                        
            self.topics.append(l_topic_lines)   
            
            l_topic_lines = cl_topic_lines_new("gossip")                        
            self.topics.append(l_topic_lines) 
            
            l_topic_lines = cl_topic_lines_new("politics")                        
            self.topics.append(l_topic_lines) 
            
            l_topic_lines = cl_topic_lines_new("science")                        
            self.topics.append(l_topic_lines) 
            
            l_topic_lines = cl_topic_lines_new("island")                        
            self.topics.append(l_topic_lines) 
            
            l_topic_lines = cl_topic_lines_new("herself")                        
            self.topics.append(l_topic_lines)  
            
            l_topic_lines = cl_topic_lines_new("yourself")                        
            self.topics.append(l_topic_lines)  
            
            l_topic_lines = cl_topic_lines_new("herself_Amy")            
            self.topics.append(l_topic_lines)  
            
            l_topic_lines = cl_topic_lines_new("herself_Alice")            
            self.topics.append(l_topic_lines)   
            
            l_topic_lines = cl_topic_lines_new("herself_Jessica")            
            self.topics.append(l_topic_lines)              
        
        
        def get_topic(self, i_name, i_char1):
            l_topics = self.topics[:]
            for l_topic in l_topics:
                if l_topic.name == i_name:
                    l_content = renpy.random.choice(l_topic.content)                
                    l_content.init = l_content.init.replace("[char1.fname]", i_char1.fname)
                    l_content.init = l_content.init.replace("[char1.playername]", i_char1.playername)                    
                    l_content.good = l_content.good.replace("[char1.fname]", i_char1.fname)
                    l_content.good = l_content.good.replace("[char1.playername]", i_char1.playername) 
                    l_content.neutral = l_content.neutral.replace("[char1.fname]", i_char1.fname)
                    l_content.neutral = l_content.neutral.replace("[char1.playername]", i_char1.playername) 
                    l_content.bad = l_content.bad.replace("[char1.fname]", i_char1.fname)
                    l_content.bad = l_content.bad.replace("[char1.playername]", i_char1.playername)    
                    return l_content




    class cl_topic_lines:
        
        def __init__(self, i_name, i_language):   
            self.name = i_name
            self.content = []
            
            l_filename = "resources/" + i_language + "/chat_" + i_name +".cht"
            
            chat_file = open(renpy.loader.transfn(l_filename),"r")
            counter = 1
            l_topic_line = cl_topic_line()                
            for l_line in chat_file:
                l_line = l_line.rstrip('\n')
                l_line2 = l_line.replace(" ", "")
                if l_line2 == "":
                    continue
                if counter == 1:
                    l_topic_line.init = l_line
                elif counter == 2:
                    if l_line.startswith("[lust"):
                        l_line = l_line.replace("[lust","")
                        l_index = l_line.find("]")
                        if l_index > 0:
                            l_line = l_line.replace("]","")                                                    
                            l_topic_line.lust_good = int(l_line[0:l_index])
                            l_line = l_line[l_index:len(l_line)]
                    l_topic_line.good = l_line                                                   
                elif counter == 3:
                    if l_line.startswith("[lust"):                    
                        l_line = l_line.replace("[lust","")
                        l_index = l_line.find("]")
                        if l_index > 0:
                            l_line = l_line.replace("]","")      
                            
                            l_topic_line.lust_bad = int(l_line[0:l_index]) 
                            l_line = l_line[l_index:len(l_line)]
                    
                    l_topic_line.bad = l_line                             
                elif counter == 4:
                    if l_line.startswith("[lust"):                 
                        l_line = l_line.replace("[lust","")
                        l_index = l_line.find("]")
                        if l_index > 0:
                            l_line = l_line.replace("]","")                                                    
                            l_topic_line.lust_neutral = int(l_line[0:l_index])                       
                            l_line = l_line[l_index:len(l_line)]
                    l_topic_line.neutral = l_line                             
                    self.content.append(l_topic_line)
                    l_topic_line = cl_topic_line()  
                    counter = 0
                counter += 1   
            chat_file.close()




    class cl_topic_line:
        
        def __init__(self):        
            self.init = ""
            self.good = ""
            self.bad = ""
            self.neutral = ""
            self.lust_good = 0
            self.lust_bad = 0            
            self.lust_neutral = 0            
        
        
        def get_answer(self, i_inclination):
            if i_inclination == 1:
                return self.good             
            elif i_inclination == 0:
                return self.neutral
            elif i_inclination == -1:
                return self.bad  
        
        
        def get_lust_change(self, i_inclination):
            if i_inclination == 1:
                return self.lust_good             
            elif i_inclination == 0:
                return self.lust_neutral
            elif i_inclination == -1:
                return self.lust_bad              


    



label incrementPlayerAttraction(actorObj, points):
    python:
        Player.interRelation.eval(actorObj.fname).attraction += points
        actorObj.interRelation.Player.attraction += points
    return
label gotoLocation:
    call processTime
    if location == "boxingGym":
        $ A = 1
        
    return
            
label processTime():
    return
    
label generateSchedule:
    python:
        for character in charList:
            eval(character).location = "Boxing gym"
            
    return
            

label updateSchedule:
        return
        
label incrementTime:
    $ gameTime[1] += incrementTime
    if gameTime[1] > 24:
        $ gameTime[1] -= 24
        $ gameTime[0] += 1
    return

label update_character_events_available:
    $ counter = 0
    while len(list_of_all_characters) > counter:
        $ list_of_all_characters[counter].events_available = []
        $ l_fname = list_of_all_characters[counter].fname

        if renpy.loadable("events/[l_fname]/[l_fname]_event_masturbate2.jpg"):
            $ list_of_all_characters[counter].events_available.append("event_masturbate")

        if renpy.loadable("events/[l_fname]/[l_fname]_event_room_service1.png"):
            $ list_of_all_characters[counter].events_available.append("event_roomservice")

        if renpy.loadable("events/[l_fname]/[l_fname]_event_shower1.jpg"):
            $ list_of_all_characters[counter].events_available.append("event_shower")

        if renpy.loadable("events/[l_fname]/[l_fname]_event_breast_bump1.jpg"):
            $ list_of_all_characters[counter].events_available.append("event_breast_bump")

        if renpy.loadable("events/[l_fname]/[l_fname]_event_reception1.jpg"):
            $ list_of_all_characters[counter].events_available.append("event_reception_night")

        $ counter +=1

    return "nothing"





label update_character_appointments_available:
    $ counter = 0
    while len(list_of_all_characters) > counter:
        $ list_of_all_characters[counter].appointments_available = []
        $ l_fname = list_of_all_characters[counter].fname

        if renpy.loadable("appointments/[l_fname]/[l_fname]_dinner1.jpg"):
            $ list_of_all_characters[counter].appointments_available.append("appointment_dinner")

        if renpy.loadable("appointments/[l_fname]/[l_fname]_reward1.jpg"):
            $ list_of_all_characters[counter].appointments_available.append("appointment_reward")

        if renpy.loadable("appointments/[l_fname]/[l_fname]_strength_training1.jpg"):
            $ list_of_all_characters[counter].appointments_available.append("appointment_strength_training")

        $ counter +=1

    return "nothing"

label event_check(ap, i_return):
    if actions_event_checked == ap:
        return i_return
    $ counter = 0
    $ action_event = ""

    if location == "player_room" and _return <> "goto_player_room":
        while len(roomservice_schedule) > counter:
            if roomservice_schedule[counter].actionpoints==ap:
                if roomservice_schedule[counter].char_room.id==0:
                    $ actions_event_checked = ap
                    $ action_event = "event_room_service"
                    $ event_char = jobs.roomservice
                    $ counter = 999
            $ counter += 1


    if _return == "goto_player_room" or _return == "goto_reception":
        $ actions_event_checked = ap


    if _return == "goto_reception" and jobs.reception.id == yvette.id:
        if yvette.lust >= 80 and yvette.rsm[0].affection >= 50 and yvette.get_action_allowed("event_reception_night") == True:
            if ap == 14 or ap == 13:
                $ action_event = "event_reception_night"
                $ event_char = yvette
                return i_return


    if _return == "goto_player_room" and amy in list_of_characters:
        if amy.locations[ap-1] == "Amy_room" and jobs.roomservice.id <> amy.id and ap > 14:
            if (amy.lust >= 90 and renpy.random.randint(1,10) <= 5) or (amy.lust >= 75 and renpy.random.randint(1,10) <= 2):
                $ action_event = "event_masturbate"
                $ event_char = amy
                return i_return


    if _return == "goto_player_room" and yvette in list_of_characters:
        if yvette.locations[ap-1] == "Yvette_room" and ((jobs.roomservice.id <> yvette.id and ap > 14) or (ap < 34 and ap > 14)):
            if renpy.random.randint(1,10) <= 2:
                $ action_event = "event_shower"
                $ event_char = yvette
                return i_return


    if _return == "goto_player_room" and desire in list_of_characters:
        if desire.locations[ap-1] == "Desire_room" and ((jobs.roomservice.id <> desire.id and ap > 14) or (ap < 34 and ap > 14)):
            if renpy.random.randint(1,10) <= 2:
                $ action_event = "event_shower"
                $ event_char = desire
                return i_return


    if _return == "goto_player_room" and amy in list_of_characters:
        if amy.locations[ap-1] == "Amy_room" and ((jobs.roomservice.id <> amy.id and ap > 14) or (ap < 34 and ap > 14)):
            if renpy.random.randint(1,10) <= 2:
                $ action_event = "event_shower"
                $ event_char = amy
                return i_return


    if _return == "goto_player_room" and ivy in list_of_characters:
        if ivy.locations[ap-1] == "Ivy_room" and ivy.locations[ap] <> "Ivy_room" and ivy.swimwear == 0:
            if renpy.random.randint(1,10) <= 2:
                $ action_event = "event_breast_bump"
                $ event_char = ivy
                return i_return


    if not _return is None and _return.startswith("goto_date_"):
        $ l_id = int(_return[10:len(_return)])
        $ event_char = player.appointments_today[l_id].with_char
        $ active_char = player.appointments_today[l_id].with_char
        $ action_event = gl_appointment_pool[player.appointments_today[l_id].id].action_event
        if actions_left > player.appointments_today[l_id].actionpoints:
            call advance_time (actions_left - player.appointments_today[l_id].actionpoints) from _call_advance_time_5

    return i_return





label create_conversation(i_return):

    if amy.phone_number_known == True:
        if amy.rsm[0].affection >= 60 and amy.get_action_allowed("appointment_pool") == True:
            if renpy.random.randint(1,10) <= 10:
                $ l_ap_message = 32 + renpy.random.choice([0, 2, 4, 6])
                $ l_message = amy.create_message(0, l_ap_message)
                $ player.add_conversation(l_message)
                $ amy.add_action_cooldown("appointment_pool", actions_left + 48*2, "")
        if amy.rsm[0].love >= 60 and amy.get_action_allowed("appointment_dinner") == True:
            $ l_ap_message = 18 + renpy.random.choice([0, 2, 4])
            $ l_message = amy.create_message(1, 20)
            $ player.add_conversation(l_message)
            $ amy.add_action_cooldown("appointment_dinner", actions_left + 48*2, "")

    if faye.phone_number_known == True:
        if faye.rsm[0].affection >= 60 and faye.get_action_allowed("appointment_pool") == True:
            $ l_ap_message = 26 + renpy.random.choice([0, 2, 4])
            $ l_message = faye.create_message(0, l_ap_message)
            $ player.add_conversation(l_message)
            $ faye.add_action_cooldown("appointment_pool", actions_left + 48*2, "")

    if yvette.phone_number_known == True:
        if yvette.rsm[0].affection >= 60 and yvette.get_action_allowed("appointment_pool") == True:
            $ l_ap_message = 40 + renpy.random.choice([0, 2, 4])
            $ l_message = yvette.create_message(0, l_ap_message)
            $ player.add_conversation(l_message)
            $ yvette.add_action_cooldown("appointment_pool", actions_left + 48*2, "")

    if player.get_quest_state("yvette_strength", yvette) > 0 and player.get_quest_state("yvette_strength", yvette) < 100:
        if renpy.random.randint(1,3) > 1:
            $ l_ap_message = 24
            $ l_message = yvette.create_message(2, l_ap_message)
            $ player.add_conversation(l_message)

    return i_return





label initiative_check(ap, i_return):
    if location == "pool" and amy in list_of_characters and amy.swimwear > 0 and current_action == "goto_pool" and amy.locations[ap-1] == location:
        $ action_initiative = "initiative_pool_lotion"
        $ initiative_char = amy

    return i_return





label create_roomservice_schedule():
    $ char_roomservice = list(list_of_characters)
    $ char_roomservice.append(player)
    $ ap = 44
    $ roomservice_schedule = []

    while len(char_roomservice) > 0:
        $ char_room = renpy.random.choice(char_roomservice)
        $ roomservice = cl_roomservice(char_room, jobs.roomservice, ap)
        $ roomservice_schedule.append(roomservice)
        $ char_roomservice.remove(char_room)

        $ jobs.roomservice.locations[ap] = char_room.fname + "_room"
        $ ap -= 1

    return





label create_jobs():
    $ roomservice_list = list(jobs.roomservice_list)
    $ reception_list = list(jobs.reception_list)
    $ massage_list = list(jobs.massage_list)

    $ max_len = 1
    while len(jobs.doctor_list) > max_len:
        $ l_doctor = renpy.random.choice(jobs.doctor_list)
        if l_doctor <> jobs.doctor:
            $ jobs.doctor = l_doctor
            $ max_len = 1000
    if jobs.doctor in roomservice_list and len(roomservice_list) > 1:
        $ roomservice_list.remove(jobs.doctor)
    if jobs.doctor in reception_list:
        $ reception_list.remove(jobs.doctor)
    if jobs.doctor in massage_list and len(massage_list) > 1:
        $ massage_list.remove(jobs.doctor)

    $ jobs.roomservice = renpy.random.choice(roomservice_list)
    if jobs.roomservice in reception_list:
        $ reception_list.remove(jobs.roomservice)
    if jobs.roomservice in massage_list and len(massage_list) > 1:
        $ massage_list.remove(jobs.roomservice)

    $ jobs.reception1 = renpy.random.choice(reception_list)
    $ reception_list.remove(jobs.reception1)
    if len(reception_list) > 0:
        $ jobs.reception2 = renpy.random.choice(reception_list)
    else:
        $ jobs.reception2 = jobs.reception1

    if jobs.reception == "":
        $ jobs.reception = jobs.reception1
    return





label change_pl_lust(val_change):
    if val_change == 0:
        return

    if player.lust + val_change > 100:
        $ val_change = 100 - player.lust

    if player.lust + val_change < 0:
        $ val_change = - player.lust

    if player.lust == 100 and val_change >= 0:
        $ disp_text = "Your lust is at its maximum value of 100 already."
    elif player.lust == 0 and val_change <= 0:
        $ disp_text = "Your lust is at its minimum value of 0 already."
    else:
        $ disp_text = "Your lust has been changed by: [val_change]"

    call show_attribute_change (player.lust, disp_text, val_change) from _call_show_attribute_change

    $ player.lust += val_change

    if player.lust >= 60 and val_change > 0:
        if player.get_effect_state("erection")==0:
            $ erection_data = player.lust // 3
            $ erection_rd = renpy.random.randint(1,100)
            if erection_data > erection_rd:
                $ player.add_effect("erection")
                "You can feel an erection building up."
    elif val_change < 0:
        $ player.rem_effect("erection")

    if player.lust >=90:
        $ player.set_effect("horny", 3)
    elif player.lust >= 70:
        $ player.set_effect("horny", 2)
    elif player.lust >= 50:
        $ player.set_effect("horny", 1)
    else:
        $ player.rem_effect("horny")
    return





label change_pl_endurance(val_change):

    if player.endurance + val_change > player.endurance_max:
        $ val_change = player.endurance_max - player.endurance

    if player.endurance + val_change < 0:
        $ val_change = - player.endurance

    if player.endurance == player.endurance_max and val_change >= 0:
        $ disp_text = "Your endurance is at its maximum value of [player.endurance_max] already."
    elif player.endurance == 0 and val_change <= 0:
        $ disp_text = "Your endurance is at its minimum value of 0 already."
    else:
        $ disp_text = "Your endurance has been changed by: [val_change]"

    call show_attribute_change (player.endurance, disp_text, val_change) from _call_show_attribute_change_6

    $ player.endurance += val_change
    return





label show_attribute_change(attribute, description, val_change, max_value=100):
    $ textbox_version = "4"
    show text "" with Pause(0.1)
    show screen attribute_change(attribute, description, val_change, max_value)
    $ renpy.pause(2)
    hide screen attribute_change  
    $ textbox_version = "2"
    return





label change_char_lust(char1, val_change, silent=False):

    if val_change > 0:
        $ val_change <= val_change + char1.relationship_type
        if val_change <= 0:
            $ val_change = 1
    elif val_change < 0:
        $ val_change = val_change + char1.relationship_type
        if val_change >= 0:
            $ val_change = -1

    if char1.lust + val_change > 100:
        $ val_change = 100 - char1.lust

    if char1.lust + val_change < 0:
        $ val_change = - char1.lust

    if char1.lust == 100 and val_change >= 0:
        $ disp_text = "[char1.fname]'s lust is at its maximum value of 100 already."
    elif char1.lust == 0 and val_change <= 0:
        $ disp_text = "[char1.fname]'s lust is at its minimum value of 0 already."
    else:
        $ disp_text = "[char1.fname]'s lust has been changed by: [val_change]"

    if silent == False:
        call show_attribute_change (char1.lust, disp_text, val_change) from _call_show_attribute_change_1

    $ char1.lust += val_change
    return





label change_char_endurance(char1, val_change):

    if char1.endurance + val_change > char1.endurance_max:
        $ val_change = char1.endurance_max - char1.endurance

    if char1.endurance+ val_change < 0:
        $ val_change = - char1.endurance

    if char1.endurance == char1.endurance_max and val_change >= 0:
        $ disp_text = "[char1.fname]'s endurance is at its maximum value of 100 already."
    elif char1.endurance == 0 and val_change <= 0:
        $ disp_text = "[char1.fname]'s endurance is at its minimum value of 0 already."
    else:
        $ disp_text = "[char1.fname]'s endurance has been changed by: [val_change]"

    call show_attribute_change (char1.endurance, disp_text, val_change) from _call_show_attribute_change_8

    $ char1.endurance += val_change
    return





label change_char_affection(char1, val_change, silent=False, index=0):

    if val_change > 0:
        if val_change == 3 and char1.relationship_type == -2:
            $ val_change = 2
        else:
            $ val_change = val_change + char1.relationship_type
        if val_change <= 0:
            $ val_change = 1
    elif val_change < 0:
        $ val_change = val_change + char1.relationship_type
        if val_change >= 0:
            $ val_change = -1

    if char1.rsm[index].affection + val_change > 100:
        $ val_change = 100 - char1.rsm[index].affection

    if char1.rsm[index].affection + val_change < 0:
        $ val_change = - char1.rsm[index].affection

    if char1.rsm[index].affection == 100 and val_change >= 0:
        $ disp_text = "[char1.fname]'s affection is at its maximum value of 100 already."
    elif char1.rsm[index].affection == 0 and val_change <= 0:
        $ disp_text = "[char1.fname]'s affection is at its minimum value of 0 already."
    else:
        $ disp_text = "[char1.fname]'s affection has been changed by: [val_change]"

    if silent == False:
        call show_attribute_change (char1.rsm[index].affection, disp_text, val_change) from _call_show_attribute_change_2

    $ char1.rsm[index].affection += val_change
    return





label player_change_company_favor(val_change):

    if player.company_favor + val_change > 500:
        $ val_change = 500 - player.company_favor

    if player.company_favor + val_change < 0:
        $ val_change = - player.company_favor

    if player.company_favor == 500 and val_change >= 0:
        $ disp_text = "Your HI company favor is at its maximum value of 500 already."
    elif player.company_favor == 0 and val_change <= 0:
        $ disp_text = "Your HI company favor is at its minimum value of 0 already."
    else:
        $ disp_text = "Your HI company favor has been changed by: [val_change]"

    call show_attribute_change (player.company_favor, disp_text, val_change, 500) from _call_show_attribute_change_7

    $ player.company_favor += val_change
    return





label change_char_favor(char1, val_change, index=0):

    if val_change > 0:
        $ val_change = val_change + char1.relationship_type
        if val_change <= 0:
            $ val_change = 1
    elif val_change < 0:
        $ val_change = val_change + char1.relationship_type
        if val_change >= 0:
            $ val_change = -1

    if char1.rsm[index].favor + val_change > 100:
        $ val_change = 100 - char1.rsm[index].favor

    if char1.rsm[index].favor + val_change < 0:
        $ val_change = - char1.rsm[index].favor

    if char1.rsm[index].favor == 100 and val_change >= 0:
        $ disp_text = "[char1.fname]'s favor is at its maximum value of 100 already."
    elif char1.rsm[index].favor == 0 and val_change <= 0:
        $ disp_text = "[char1.fname]'s favor is at its minimum value of 0 already."
    else:
        $ disp_text = "[char1.fname]'s favor has been changed by: [val_change]"

    call show_attribute_change (char1.rsm[index].favor, disp_text, val_change) from _call_show_attribute_change_4

    $ char1.rsm[index].favor += val_change
    return





label change_char_love(char1, val_change, index=0):

    if val_change > 0:
        if val_change == 3 and char1.relationship_type == -2:
            $ val_change = 2
        else:
            $ val_change = val_change + char1.relationship_type
        if val_change <= 0:
            $ val_change = 1
    elif val_change < 0:
        $ val_change = val_change + char1.relationship_type
        if val_change >=0:
            $ val_change = -1

    if char1.rsm[index].love + val_change > 100:
        $ val_change = 100 - char1.rsm[index].love

    if char1.rsm[index].love + val_change < 0:
        $ val_change = - char1.rsm[index].love

    if char1.rsm[index].love == 100 and val_change >= 0:
        $ disp_text = "[char1.fname]'s love is at its maximum value of 100 already."
    elif char1.rsm[index].love == 0 and val_change <= 0:
        $ disp_text = "[char1.fname]'s love is at its minimum value of 0 already."
    else:
        $ disp_text = "[char1.fname]'s love has been changed by: [val_change]"

    call show_attribute_change (char1.rsm[index].love, disp_text, val_change) from _call_show_attribute_change_3

    $ char1.rsm[index].love += val_change
    return




label change_char_anger(char1, val_change, index=0):

    if val_change > 0:
        $ val_change = val_change - char1.relationship_type
        if val_change <= 0:
            $ val_change = 1
    elif val_change < 0:
        $ val_change = val_change - char1.relationship_type
        if val_change >= 0:
            $ val_change = -1

    if char1.rsm[index].anger + val_change > 100:
        $ val_change = 100 - char1.rsm[index].anger

    if char1.rsm[index].anger + val_change < 0:
        $ val_change = - char1.rsm[index].anger

    if char1.rsm[index].anger == 100 and val_change >= 0:
        $ disp_text = "[char1.fname]'s anger is at its maximum value of 100 already."
    elif char1.rsm[index].anger == 0 and val_change <= 0:
        $ disp_text = "[char1.fname]'s anger is at its minimum value of 0 already."
    else:
        $ disp_text = "[char1.fname]'s anger has been changed by: [val_change]"

    call show_attribute_change (char1.rsm[index].anger, disp_text, val_change) from _call_show_attribute_change_5

    $ char1.rsm[index].anger += val_change
    return




label check_lust(char1, level, repercussions=True):
    $ check_ok = False
    $ lust_change = 0
    if level == 0:
        if char1.lust >= 20:
            $ check_ok = True
        else:
            if repercussions:
                $ lust_change = -2

    elif level == 1:
        if char1.lust >= 40:
            $ check_ok = True
        else:
            if repercussions:
                $ lust_change = -4

    elif level == 2:
        if char1.lust >= 60:
            $ check_ok = True
        else:
            if repercussions:
                $ lust_change = -6

    elif level == 3:
        if char1.lust >= 80:
            $ check_ok = True
        else:
            if repercussions:
                $ lust_change = -8

    elif level == 4:
        if char1.lust >= 100:
            $ check_ok = True
        else:
            if repercussions:
                $ lust_change = -10

    $ disp_text = char1.fname + " lust"
    call display_check_result (disp_text , check_ok) from _call_display_check_result_4
    if lust_change <> 0:
        call change_char_lust (char1, lust_change) from _call_change_char_lust_14
    return check_ok





label check_love_affection(char1, level, index=0):
    $ check_ok = False
    $ l_affection = char1.rsm[index].affection - char1.rsm[index].anger
    $ l_love = char1.rsm[index].love - char1.rsm[index].anger

    if level == 0:
        if l_affection >= 40:
            $ check_ok = True

    elif level == 1:
        if l_affection >= 60:
            $ check_ok = True

    elif level == 2:
        if l_affection >= 60 and l_love >= 30:
            $ check_ok = True

    elif level == 3:
        if l_affection >= 80 and l_love >= 40:
            $ check_ok = True

    elif level == 4:
        if l_affection >= 100 and l_love >= 60:
            $ check_ok = True

    $ disp_text = char1.fname + " love/affection"
    call display_check_result (disp_text , check_ok) from _call_display_check_result_5

    return check_ok





label check_affection(char1, level, index=0, repercussions=True):
    $ check_ok = False
    $ affection_change = 0
    if level == 0:
        if char1.rsm[index].affection >= 20:
            $ check_ok = True
        else:
            if repercussions:
                $ affection_change = -2

    elif level == 1:
        if char1.rsm[index].affection >= 40:
            $ check_ok = True
        else:
            if repercussions:
                $ affection_change = -4

    elif level == 2:
        if char1.rsm[index].affection >= 60:
            $ check_ok = True
        else:
            if repercussions:
                $ affection_change = -6

    elif level == 3:
        if char1.rsm[index].affection >= 80:
            $ check_ok = True
        else:
            if repercussions:
                $ affection_change = -8

    elif level == 4:
        if char1.rsm[index].affection >= 100:
            $ check_ok = True
        else:
            if repercussions:
                $ affection_change = -10

    $ disp_text = char1.fname + " affection"
    call display_check_result (disp_text , check_ok) from _call_display_check_result
    if affection_change <> 0:
        call change_char_affection (char1, affection_change, index) from _call_change_char_affection
    return check_ok





label check_love(char1, level, index=0, repercussions=True):
    $ check_ok = False
    $ love_change = 0
    if level == 0:
        if char1.rsm[index].love >= 20:
            $ check_ok = True
        else:
            if repercussions:
                $ love_change = -2

    elif level == 1:
        if char1.rsm[index].love >= 40:
            $ check_ok = True
        else:
            if repercussions:
                $ love_change = -4

    elif level == 2:
        if char1.rsm[index].love >= 60:
            $ check_ok = True
        else:
            if repercussions:
                $ love_change = -6

    elif level == 3:
        if char1.rsm[index].love >= 80:
            $ check_ok = True
        else:
            if repercussions:
                $ love_change = -8

    elif level == 4:
        if char1.rsm[index].love >= 100:
            $ check_ok = True
        else:
            if repercussions:
                $ love_change = -10

    $ disp_text = char1.fname + " love"
    call display_check_result (disp_text , check_ok) from _call_display_check_result_7
    if love_change <> 0:
        call change_char_love (char1, love_change, index) from _call_change_char_love_9
    return check_ok





label check_tease_sexual(char1, level, index=0, repercussions=True, silent=False):
    $ check_ok = False
    $ affection_change = 0
    $ lust_change = 0

    if level == 0:
        $ check_value_combined = 10 + (2 - player.looks) * 1
        $ check_value_lust = 20 + (2 - player.looks) * 2
    elif level == 1:
        $ check_value_combined = 20 + (2 - player.looks) * 2
        $ check_value_lust = 40 + (2 - player.looks) * 4
    elif level == 2:
        $ check_value_combined = 40 + (2 - player.looks) * 4
        $ check_value_lust = 60 + (2 - player.looks) * 6
    elif level == 3:
        $ check_value_combined = 60 + (2 - player.looks) * 6
        $ check_value_lust = 80 + (2 - player.looks) * 8
    elif level == 4:
        $ check_value_combined = 80 + (2 - player.looks) * 8
        $ check_value_lust = 100 + (2 - player.looks) * 10
        if check_value_lust > 100:
            $ check_value_lust = 100

    if char1.rsm[index].affection >= check_value_combined and char1.lust >= check_value_combined:
        $ check_ok = True
    elif char1.lust >= check_value_lust:
        $ check_ok = True
    else:
        $ check_ok = False
        if repercussions:
            $ affection_change = -level -1
            $ lust_change = -level -1

    if silent == False:
        $ disp_text = char1.fname + " affection/lust"
        call display_check_result (disp_text , check_ok) from _call_display_check_result_1

    if affection_change <> 0:
        call change_char_affection (char1, affection_change, silent, index) from _call_change_char_affection_1
    if lust_change <> 0:
        call change_char_lust (char1, lust_change, silent) from _call_change_char_lust

    return check_ok




label check_favor(char1, i_favor, index=0):
    $ check_ok = False

    $ l_favor = i_favor - char1.relationship_type
    if l_favor <= 0:
        $ l_favor = 1

    if char1.rsm[0].favor >= l_favor:
        char1.talk "Sure I can do that, but it will cost you [l_favor] favor."
        menu:
            "Ok, great":
                call change_char_favor (char1, -i_favor) from _call_change_char_favor_5
                $ check_ok = True
            "I changed my mind":
                pass
    else:
        call display_favor_result (char1, l_favor) from _call_display_favor_result

    return check_ok




label create_list_of_chars_display(i_create_masseuses=False):
    $ list_of_chars_display_3 = []
    $ list_of_chars_display_5 = []
    $ counter = 0

    while counter < len(list_of_characters):
        if list_of_characters[counter].locations[actions_left-1] == location:
            $ list_of_chars_display_3.append(list_of_characters[counter])
            $ list_of_chars_display_5.append(list_of_characters[counter])
        $ counter += 1

    while len(list_of_chars_display_3) > 3:
        $ randchar = renpy.random.choice(list_of_chars_display_3)
        $ list_of_chars_display_3.remove(randchar)

    while len(list_of_chars_display_5) > 5:
        $ randchar = renpy.random.choice(list_of_chars_display_5)
        $ list_of_chars_display_5.remove(randchar)

    if i_create_masseuses == True:
        $ list_of_chars_massage = list(jobs.massage_list)
        $ max_nr_of_masseuses = renpy.random.choice([0,0,0,1,1,1,2])
        while len(list_of_chars_massage) > max_nr_of_masseuses:
            $ l_char = renpy.random.choice(list_of_chars_massage)
            $ list_of_chars_massage.remove(l_char)

    return





label get_char_present(np_char, location, actionpoints):
    $ index = actionpoints - 1
    if np_char.locations[index] == location:
        $ np_char.present = True
    else:
        $ np_char.present = False
    return





label player_charm_check(check_level, variation=0):
    $ check_ok = False
    if player.get_charm() > check_level:
        $ check_ok = True
    elif player.get_charm() == check_level:
        $ rand_int = renpy.random.randint(1, 2)
        if rand_int==1:
            $ check_ok = True
    elif player.get_charm() == check_level - 1:
        $ rand_int = renpy.random.randint(1, 4)
        if rand_int==1:
            $ check_ok = True

    call display_check_result ("Player charm", check_ok) from _call_display_check_result_2
    return check_ok





label player_hacking_check(check_level, variation=0):
    $ check_ok = False

    if player.get_hacking() > check_level:
        $ check_ok = True
    elif player.get_hacking() == check_level:
        $ rand_int = renpy.random.randint(1, 2)
        if rand_int==1:
            $ check_ok = True
    elif player.get_hacking() == check_level - 1:
        $ rand_int = renpy.random.randint(1, 4)
        if rand_int==1:
            $ check_ok = True

    call display_check_result ("Player hacking/sneeking", check_ok) from _call_display_check_result_6
    return check_ok




label player_strength_check(check_level, variation=0):
    $ check_ok = False
    if player.get_strength() > check_level:
        $ check_ok = True
    elif player.get_strength() == check_level:
        $ rand_int = renpy.random.randint(1, 2)
        if rand_int==1:
            $ check_ok = True
    elif player.get_strength() == check_level - 1:
        $ rand_int = renpy.random.randint(1, 4)
        if rand_int==1:
            $ check_ok = True

    call display_check_result ("Player strength", check_ok) from _call_display_check_result_3
    return check_ok





label display_check_result(attribute, check_result):
    $ textbox_version = "4"
    show text "" with Pause(0.1)
    show screen show_check_result(attribute, check_result)
    $ renpy.pause(1.5)
    hide screen show_check_result
    $ textbox_version = "2"
    return "nothing"





label display_favor_result(char1, i_favor_req):
    $ l_text = "You do not have " + str(i_favor_req) + " favor with " + char1.fname
    $ textbox_version = "4"
    show text "" with Pause(0.1)
    show screen show_favor_result(l_text)
    $ renpy.pause(1.5)
    hide screen show_favor_result
    $ textbox_version = "2"
    return "nothing"





label display_inventory_change(i_item, i_quantity):
    $ textbox_version = "4"
    show text "" with Pause(0.1)
    show screen show_inventory_change(i_item, i_quantity)
    $ renpy.pause(2.0)
    hide screen show_inventory_change
    $ textbox_version = "2"
    return "nothing"




label calculate_weekly_endurance_training_effect():
    if player.endurance_trainings_week >= 3 and player.endurance_trainings_week <=5:
        $ player.endurance_train_points += 3
    elif player.endurance_trainings_week > 5 or player.endurance_trainings_week == 2:
        $ player.endurance_train_points += 1
    elif player.endurance_trainings_week == 0:
        $ player.endurance_train_points -= 1


    if player.endurance_max <= 50 and player.endurance_train_points >= 9:
        $ player.endurance_max += 10
        $ player.endurance_train_points = 0
    elif player.endurance_max == 60 and player.endurance_train_points >= 12:
        $ player.endurance_max += 10
        $ player.endurance_train_points = 0
    elif player.endurance_max == 70 and player.endurance_train_points >= 15:
        $ player.endurance_max += 10
        $ player.endurance_train_points = 0
    elif player.endurance_max == 80 and player.endurance_train_points >= 18:
        $ player.endurance_max += 10
        $ player.endurance_train_points = 0
    elif player.endurance_max == 90 and player.endurance_train_points >= 21:
        $ player.endurance_max += 10
        $ player.endurance_train_points = 0

    if player.endurance_max > 50 and player.endurance_train_points <= -3:
        $ player.endurance_max -= 10
        $ player.endurance_train_points = 0

    if player.endurance_max > 100:
        $ player.endurance_max = 100

    return "nothing"




label calculate_weekly_strength_training_effect():
    $ l_pl_strength_delta = 0
    if player.strength_trainings_week >= 3 and player.strength_trainings_week <=5:
        $ player.strength_train_points += 3
    elif player.strength_trainings_week > 5 or player.strength_trainings_week == 2:
        $ player.strength_train_points += 1
    elif player.strength_trainings_week == 0:
        $ player.strength_train_points -= 1

    if player.strength <= 2 and player.strength_train_points >= 3:
        $ l_pl_strength_delta += 1
        $ player.strength_train_points = 0
    elif player.strength >= 3 and player.strength <= 4 and player.strength_train_points >= 6:
        $ l_pl_strength_delta += 1
        $ player.strength_train_points = 0
    elif player.strength >= 5 and player.strength <= 6 and player.strength_train_points >= 9:
        $ l_pl_strength_delta += 1
        $ player.strength_train_points = 0
    elif player.strength == 7 and player.strength_train_points >= 12:
        $ l_pl_strength_delta += 1
        $ player.strength_train_points = 0
    elif player.strength >= 8 and player.strength_train_points >= 15:
        $ l_pl_strength_delta += 1
        $ player.strength_train_points = 0

    if player.strength >= 6 and player.strength_train_points <= -4:
        $ l_pl_strength_delta -= 1
        $ player.strength_train_points = 0
    elif player.strength < 6 and player.strength_train_points < 0:
        $ player.strength_train_points = 0

    $ player.strength += l_pl_strength_delta
    if l_pl_strength_delta > 0:
        "Congratulations, your training paid off.\nYour strength has been changed by [l_pl_strength_delta]. Your new strength is [player.strength]."
    elif l_pl_strength_delta < 0:
        "You are pretty strong, but without traing it won't last forever. Your strength has been changed by [l_pl_strength_delta]. Your new strength is [player.strength]."

    if player.strength > 10:
        $ player.strength = 10

    return "nothing"





label calculate_weekly_charm_training_effect():
    $ l_success = False
    if player.charm == 1 and player.charm_train_points >= 6:
        $ l_success = True
    elif player.charm == 2 and player.charm_train_points >= 8:
        $ l_success = True
    elif player.charm == 3 and player.charm_train_points >= 12:
        $ l_success = True
    elif player.charm == 4 and player.charm_train_points >= 16:
        $ l_success = True

    if l_success == True:
        $ player.charm_train_points = 0
        $ player.charm += 1
        "Congratulations, your reading paid off.\nYour charm has been increased by 1.\nYour new charm is [player.charm]."

    return "nothing"





label calculate_weekly_hacking_training_effect():
    $ l_success = False
    if player.hacking == 0 and player.hacking_train_points >= 4:
        $ l_success = True
    elif player.hacking == 1 and player.hacking_train_points >= 6:
        $ l_success = True
    elif player.hacking == 2 and player.hacking_train_points >= 8:
        $ l_success = True
    elif player.hacking == 3 and player.hacking_train_points >= 12:
        $ l_success = True
    elif player.hacking == 4 and player.hacking_train_points >= 16:
        $ l_success = True

    if l_success == True:
        $ player.hacking_train_points = 0
        $ player.hacking += 1
        "Congratulations, your reading paid off.\nYour hacking/sneaking skill has been increased by 1.\nYour new hacking/sneaking skill is [player.hacking]."

    return "nothing"




label calculate_weekly_affection_love_reduction():

    if gameday < 4:
        return "nothing"
    $ counter =  0
    $ val_change = 0
    while len(list_of_characters) > counter:

        if list_of_characters[counter].get_total_interactions_week() == 0:
            if list_of_characters[counter].rsm[0].affection > 20:
                $ val_change = - int((list_of_characters[counter].rsm[0].affection - 20) * 0.5)
                call change_char_affection (list_of_characters[counter], val_change) from _call_change_char_affection_47

        elif list_of_characters[counter].get_total_interactions_week() == 1:
            if list_of_characters[counter].rsm[0].affection > 40:
                $ val_change = - int((list_of_characters[counter].rsm[0].affection - 40) * 0.4)
                call change_char_affection (list_of_characters[counter], val_change) from _call_change_char_affection_48

        elif list_of_characters[counter].get_total_interactions_week() == 2:
            if list_of_characters[counter].rsm[0].affection > 60:
                $ val_change = - int((list_of_characters[counter].rsm[0].affection - 60) * 0.3)
                call change_char_affection (list_of_characters[counter], val_change) from _call_change_char_affection_49

        elif list_of_characters[counter].get_total_interactions_week() <= 4:
            if list_of_characters[counter].rsm[0].affection > 60:
                $ val_change = - int((list_of_characters[counter].rsm[0].affection - 60) * 0.2)
                call change_char_affection (list_of_characters[counter], val_change) from _call_change_char_affection_50


        if list_of_characters[counter].get_total_interactions_week() == 0:
            if list_of_characters[counter].rsm[0].love > 20:
                $ val_change = - int((list_of_characters[counter].rsm[0].love - 20) * 0.5)
                call change_char_love (list_of_characters[counter], val_change) from _call_change_char_love_3

        elif list_of_characters[counter].get_total_interactions_week() == 1:
            if list_of_characters[counter].rsm[0].love > 40:
                $ val_change = - int((list_of_characters[counter].rsm[0].love - 40) * 0.4)
                call change_char_love (list_of_characters[counter], val_change) from _call_change_char_love_4

        elif list_of_characters[counter].get_total_interactions_week() == 2:
            if list_of_characters[counter].rsm[0].love > 60:
                $ val_change = - int((list_of_characters[counter].rsm[0].love - 60) * 0.3)
                call change_char_love (list_of_characters[counter], val_change) from _call_change_char_love_5

        elif list_of_characters[counter].get_total_interactions_week() <= 4:
            if list_of_characters[counter].rsm[0].love > 60:
                $ val_change = - int((list_of_characters[counter].rsm[0].love - 60) * 0.2)
                call change_char_love (list_of_characters[counter], val_change) from _call_change_char_love_10

        $ counter += 1

    return "nothing"





label advance_day:
    show screen main_game(location)

    $ mydate += datetime.timedelta(days=1)
    $ cur_weekday = mydate.strftime("%A")
    $ cur_month = mydate.strftime("%B")
    $ cur_day = mydate.strftime("%d")
    $ gameday += 1


    $ counter = 0
    while len(list_of_characters) > counter:
        if list_of_characters[counter].get_total_interactions_today() == 0:
            if list_of_characters[counter].rsm[0].affection > 80:
                call change_char_affection (list_of_characters[counter], -6) from _call_change_char_affection_28
            if list_of_characters[counter].rsm[0].love > 80:
                call change_char_love (list_of_characters[counter], -3) from _call_change_char_love_6

        $ list_of_characters[counter].init_interactions_today()
        $ counter += 1

    if cur_weekday == "Monday":
        call create_jobs () from _call_create_jobs
        call add_girl_to_island () from _call_add_girl_to_island
        call calculate_weekly_strength_training_effect () from _call_calculate_weekly_strength_training_effect
        call calculate_weekly_endurance_training_effect () from _call_calculate_weekly_endurance_training_effect
        call calculate_weekly_charm_training_effect () from _call_calculate_weekly_charm_training_effect
        call calculate_weekly_hacking_training_effect () from _call_calculate_weekly_hacking_training_effect
        call calculate_weekly_affection_love_reduction () from _call_calculate_weekly_affection_love_reduction
        $ counter = 0
        while len(list_of_characters) > counter:
            $ list_of_characters[counter].init_interactions_week()
            $ counter += 1


    $ player.appointments_today  = list(player.appointments_tomorrow)
    $ player.appointments_tomorrow = []
    return "nothing"


    call create_appointment_pool () from _call_create_appointment_pool_3
    call create_message_pool () from _call_create_message_pool_1





label advance_time(actionpoints, i_return=""):
    $ actions_left_before = actions_left
    $ actions_left -= actionpoints
    if actions_left <= 14 and actions_left_before > 14:
        call advance_day from _call_advance_day

    if actions_left <= 14:
        $ daytime = 7
    elif actions_left <= 20:
        $ daytime = 6
    elif actions_left <= 26:
        $ daytime = 5
    elif actions_left <= 32:
        $ daytime = 4
    elif actions_left <= 38:
        $ daytime = 3
    elif actions_left <= 44:
        $ daytime = 2
    else:
        $ daytime = 1

    if actions_left <= 48 and actions_left > 0:
        $ cur_time = cl_utility().convert_ap_to_time(actions_left)
    else:

        if cur_weekday == "Wednesday":
            $ l_message = no_char.create_message(4, 34)
            $ player.add_conversation(l_message)

        $ cur_time = "07:00"
        $ actions_left = 48
        $ daytime = 1
        hide screen main_game
        scene
        show screen left_menu        
        scene wait


        call create_conversation (i_return) from _call_create_conversation


        call create_char_schedules from _call_create_char_schedules


        call create_roomservice_schedule from _call_create_roomservice_schedule


        $ player.max_masturbations_per_day = player.endurance_max // 10
        if player.max_masturbations_per_day < 3:
            $ player.max_masturbations_per_day = 3
        elif player.max_masturbations_per_day > 6:
            $ player.max_masturbations_per_day = 6


        if player.sleep_last_night == 0:
            $ player.add_effect("tired")
            $ player.add_effect("tired")
        if player.sleep_last_night == 1:
            $ player.add_effect("tired")


        if player.eaten_today == 1:
            $ player.add_effect("hungry")
        elif player.eaten_today == 0:
            $ player.add_effect("hungry")
            $ player.add_effect("hungry")


        $ player.trained_today = False
        $ player.eaten_today = 0
        $ player.sleep_last_night = 0
        $ player.masturbations_today = 0


    $ player.endurance += (player.endurance_max // 10)* actionpoints
    if player.endurance > player.endurance_max:
        $ player.endurance = player.endurance_max
    $ counter = 0
    while len(list_of_characters) > counter:
        $ list_of_characters[counter].endurance += (list_of_characters[counter].endurance_max // 10) * actionpoints
        if list_of_characters[counter].endurance > list_of_characters[counter].endurance_max:
            $ list_of_characters[counter].endurance = list_of_characters[counter].endurance_max
        $ counter += 1


    $ player.pass_time_effects(actionpoints)

    if actions_left <= 30:
        $ jobs.reception = jobs.reception2
    else:
        $ jobs.reception = jobs.reception1


    $ counter = 0
    while len(list_of_characters) > counter:
        $ list_of_characters[counter].adjust_topics_talk_timer(actionpoints)
        $ counter += 1


    $ counter = 0
    while len(list_of_characters) > counter:
        $ list_of_characters[counter].adjust_action_cooldown_timer(actionpoints)
        $ counter += 1

    $ player.adjust_action_cooldown_timer(actionpoints)




    scene

    return i_return





label create_char_schedules():
    $ t_start = time()
    show text "Please be patient, creating character schedule for today." at top
    with dissolve
    pause 0.7
    hide text
    with dissolve

    $ counter = 0
    while counter < len(list_of_characters):
        call create_char_schedule (list_of_characters[counter]) from _call_create_char_schedule
        $ counter += 1

    $ t_end = time()
    $ t_dur = t_end - t_start - 0.7
    show text "Schedule creation finished, took: [t_dur:.3] seconds." at top
    with dissolve
    pause 0.7
    hide text
    with dissolve

    return "nothing"





label create_char_schedule(char1):
    $ char1.locations=[]
    $ loopcount = 49


    $ own_room = char1.fname + "_room"
    while loopcount > 0:
        $ char1.locations.append(own_room)
        $ loopcount -= 1


    $ massage_from = 32
    $ massage_to = 26


    $ pool_from = 42
    $ pool_to = 27


    $ beach_from = 42
    $ beach_to = 25


    $ workout_from = 48
    $ workout_to = 29


    $ g_points = 48
    $ g_points_old = 48
    $ location1 = "empty"
    $ loops = 0
    $ loops2 = 0
    $ massage_length = 0
    $ pool_length = 0
    $ beach_length = 0
    $ workout_length = 0
    $ massage_count = 0
    $ pool_count = 0
    $ beach_count = 0
    $ workout_count = 0
    $ open = False
    $ t_res0 = 0.0
    $ t_res1 = 0.0
    $ t_res2 = 0.0
    $ l_reception2_done = False

    while g_points > 0:
        $ g_points_old = g_points
        $ location1_last = location1
        $ loops += 1
        $ max_count = 0
        $ t0 = time()

        if jobs.doctor == char1 and g_points == 48:
            call create_single_schedule (char1, "doctor", 18, 48, 0) from _call_create_single_schedule_4
        elif jobs.reception1 == char1 and g_points == 48:
            call create_single_schedule (char1, "reception", 18, 48, 0) from _call_create_single_schedule_5
        elif jobs.reception2 == char1 and g_points <= 30 and not l_reception2_done:
            $ g_points = 30
            $ l_reception2_done = True
            call create_single_schedule (char1, "reception", 18, 30, 0) from _call_create_single_schedule_6
        else:
            if (massage_from>= g_points and massage_to <= g_points) or (pool_from>= g_points and pool_to <= g_points) or (beach_from>= g_points and beach_to <= g_points) or (workout_from>= g_points and workout_to <= g_points):
                while location1_last==location1 or open==False:
                    $ location1 = renpy.random.choice(char1.location_preferences)
                    $ open = False
                    $ loops2 +=1
                    $ max_count += 1
                    if max_count >=3:
                        $ location1_last = "empty"
                    if location1=="massage":
                        if massage_from>= g_points and massage_to <= g_points:
                            $ open = True
                    elif location1=="pool":
                        if pool_from>= g_points and pool_to <= g_points:
                            $ open =  True
                    elif location1=="beach":
                        if beach_from>= g_points and beach_to <= g_points:
                            $ open =  True
                    elif location1=="workout":
                        if workout_from>= g_points and workout_to <= g_points:
                            $ open =  True
            else:
                $ location1 = own_room

            $ t1 = time()
            $ t_res0 = t_res0 + t1-t0

            if location1 == "massage":
                $ massage_count += 1
                $ t1 = time()
                $ massage_length = renpy.random.randint(1,2)
                $ t2 = time()
                call create_single_schedule (char1, location1, massage_length, massage_from, massage_to) from _call_create_single_schedule
                $ t3 = time()
                $ t_res1 = t_res1 + t2-t1
                $ t_res2 = t_res2 + t3-t2
            elif location1 == "pool":
                $ pool_count += 1
                $ t1 = time()
                $ pool_length = renpy.random.choice([3,3,4,4,5,5,6,7,8])
                $ t2 = time()
                call create_single_schedule (char1, location1, pool_length, pool_from, pool_to) from _call_create_single_schedule_1
                $ t3 = time()
                $ t_res1 = t_res1 + t2-t1
                $ t_res2 = t_res2 + t3-t2
            elif location1 == "beach":
                $ beach_count += 1
                $ t1 = time()
                $ beach_length = renpy.random.choice([3,3,4,4,5,5,6,7,8])
                $ t2 = time()
                call create_single_schedule (char1, location1, beach_length, beach_from, beach_to) from _call_create_single_schedule_2
                $ t3 = time()
                $ t_res1 = t_res1 + t2-t1
                $ t_res2 = t_res2 + t3-t2
            elif location1 == "workout":
                $ workout_count += 1
                $ t1 = time()
                $ workout_length = renpy.random.choice([0,2,3,3,4,4])
                $ t2 = time()
                call create_single_schedule (char1, location1, workout_length, workout_from, workout_to) from _call_create_single_schedule_3
                $ t3 = time()
                $ t_res1 = t_res1 + t2-t1
                $ t_res2 = t_res2 + t3-t2

            if g_points <= 14:
                $ g_points = 0
            elif g_points==g_points_old:
                $ g_points -= 1

    $ t2 = time()


    if char1 == jobs.doctor:
        $ breakfast = 48
    elif char1 == jobs.reception1:
        $ breakfast = 46
    else:
        $ breakfast = renpy.random.choice([48, 46])
    $ char1.locations[breakfast] = "restaurant"
    $ char1.locations[breakfast-1] = "restaurant"


    if char1 <> jobs.doctor and char1 <> jobs.reception1:
        $ lunch = renpy.random.choice([38, 36])
        $ lunch_length = renpy.random.choice([0,2])
        while lunch_length > 0:
            $ char1.locations[lunch] = "restaurant"
            $ lunch_length -= 1
            $ lunch -= 1


    if char1 <> jobs.reception2:
        $ dinner = renpy.random.choice([26, 25, 24, 23])
        $ dinner_length = 3
        $ char1.locations[dinner] = "restaurant"
        $ char1.locations[dinner-1] = "restaurant"
        $ char1.locations[dinner-2] = "restaurant"

        $ char1.locations[dinner+1] = own_room


    $ nightbar = renpy.random.choice([0, 18, 17 , 16, 15, 14, 13])
    if nightbar == 18:
        $ nightbar_length = renpy.random.randint(2,5)
    elif nightbar == 17:
        $ nightbar_length = renpy.random.randint(2,5)
    elif nightbar == 16:
        $ nightbar_length = renpy.random.randint(2,4)
    elif nightbar == 15:
        $ nightbar_length = renpy.random.randint(1,3)
    elif nightbar == 14:
        $ nightbar_length = renpy.random.randint(1,2)
    elif nightbar == 13:
        $ nightbar_length = 1
    else:
        $ nightbar_length = 0
    while nightbar_length > 0:
        $ char1.locations[nightbar] = "nightbar"
        $ nightbar_length -= 1
        $ nightbar -= 1


    if char1 <> jobs.reception1:
        $ volleyball = renpy.random.randint(1,4)
        if char1.volleyball >= volleyball:
            $ char1.locations[32] = "volleyball"


    $ l_counter = 0
    while l_counter < len(player.appointments_today):
        if player.appointments_today[l_counter].with_char.id == char1.id:
            $ char1.locations[player.appointments_today[l_counter].actionpoints] = player.appointments_today[l_counter].location
        $ l_counter += 1


    $ char1.locations.pop(0)

    return "nothing"





label create_single_schedule(char1, location1, duration1, ok_from, ok_to):
    while duration1 > 0:
        if ok_from >= g_points and ok_to <= g_points:
            $ char1.locations[g_points] = location1
            $ g_points -= 1
        $ duration1 -= 1
    return "nothing"





label set_phone_char(char1):
    $ phone_char = char1
    return "do_pl_phone_contacts"





label set_cheats():
    $ counter = 0





    call create_appointment_pool () from _call_create_appointment_pool_1
    call create_message_pool () from _call_create_message_pool

    $ player.appointments_today = []
    $ player.appointments_tomorrow = []

    if amy in list_of_characters:
        $ l_message = amy.create_message(0, 36)
        $ player.add_conversation(l_message)
        $ l_message = amy.create_message(1, 20)
        $ player.add_conversation(l_message)

    if faye in list_of_characters:
        $ l_message = faye.create_message(0, 30)
        $ player.add_conversation(l_message)






    $ player.strength = 10
    $ player.hacking = 5
    $ player.monitoring_sub_dermal_app = True
    while len(list_of_characters) > counter:
        $ list_of_characters[counter].rsm[0].love = 95
        $ list_of_characters[counter].rsm[0].affection = 100
        $ list_of_characters[counter].rsm[0].favor = 99
        $ list_of_characters[counter].rsm[0].anger = 2
        $ list_of_characters[counter].lust = 90
        $ list_of_characters[counter].phone_number_known = True
        $ list_of_characters[counter].room_number_known = True
        $ list_of_characters[counter].monitoring_sub_dermal_hacked = True
        $ list_of_characters[counter].monitoring_sub_dermal = 2
        $ counter +=1
    return "nothing"





label show_screen():
    $ textbox_version = "4"
    ""
    $ textbox_version = "2"
    return "nothing"


label show_text(i_text, i_time, i_who=None):
    if i_who is None:
        show screen say2(i_who, i_text)
        $ textbox_version = "4"
        pause i_time 
        $ textbox_version = "2"
        hide screen say2           
    else:
        $ i_who.talk("[i_text]", interact=False)



    return "nothing"










screen attribute_change(attribute, description, val_change, max_value=100):
    zorder 2000
    $ attribute_new = attribute + val_change

    imagebutton idle "gui/textbox4.png"
    text [description] xpos 540 ypos 35 color "#0099cc" size 15

    if val_change >= 0:
        $ xsize_change = val_change * 200 / max_value
        if xsize_change == 0 and val_change > 0:
            $ xsize_change = 1
        $ xpos_change = 540 + attribute * 200 / max_value
        bar value StaticValue(attribute, max_value) xpos 540 ypos 15 xsize 200 ysize 12 left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
        bar value StaticValue(val_change, val_change) xpos xpos_change ypos 15 xsize xsize_change ysize 12 left_bar Frame("gui/bar/left_yellow.png", gui.bar_borders, tile=gui.bar_tile)
    else:
        $ xsize_change = -val_change * 200 / max_value
        if xsize_change == 0:
            $ xsize_change = -1
        $ xpos_change = 540 + attribute * 200 / max_value + val_change * 200 / max_value
        bar value StaticValue(attribute_new, max_value) xpos 540 ypos 15 xsize 200 ysize 12 left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
        bar value StaticValue(-val_change, -val_change) xpos xpos_change ypos 15 xsize xsize_change ysize 12 left_bar Frame("gui/bar/left_red.png", gui.bar_borders, tile=gui.bar_tile)
    text "[attribute_new] / [max_value]" xpos 750 ypos 15 color "#ffffff" size 15





screen show_check_result(attribute, check_result):
    zorder 1000
    imagebutton idle "gui/textbox4.png"
    if check_result==True:
        text "[attribute] check succeeded!" xpos 540 ypos 25 color "#008000" size 15
        add "icon_happy" xpos 460 ypos 12
    else:
        text "[attribute] check failed!" xpos 540 ypos 25 color "#ff0000" size 15
        add "icon_sad" xpos 460 ypos 12





screen show_favor_result(i_text):
    zorder 1000
    imagebutton idle "gui/textbox4.png"
    text "[i_text]" xpos 540 ypos 25 color "#ff0000" size 15
    add "icon_sad" xpos 460 ypos 12





screen show_inventory_change(i_item, i_quantity):
    zorder 1000
    imagebutton idle "gui/textbox4.png"
    if i_quantity > 0:
        text "Your inventory for [i_item](s) has been increased by [i_quantity]" xpos 400 ypos 25 color "#ffffff" size 16
    else:
        $ l_quantity = - i_quantity
        text "Your inventory for [i_item](s) has been reduced by [l_quantity]" xpos 400 ypos 25 color "#ffffff" size 16
    
    
