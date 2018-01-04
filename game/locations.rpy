init python:
    class LocationClass:
        def __init__(self):
            self.public = True
            self.privateArea = True
            self.openTime = 0
            self.closeTime = 24
            self.name = ""
            self.unlock = True

    class FightVenueClass:
        def __init__(self, name, public=True):
            self.name = ""
            self.public = public
            self.positions = list()
            self.terrainHazards = dict()
            
            
label createLocations:
    python:
        boxingGym = LocationClass()
        workoutGym = LocationClass()
        playerApartment = LocationClass()
        stripClub = LocationClass()
        seedyBar  = LocationClass()
        yacht = LocationClass()
        wrestlingVenue = LocationClass()
        beach = LocationClass()
        hotelRoom = LocationClass()
        shop = LocationClass()
        park = LocationClass()
        
        locationList = [("Boxing gym","Boxing gym"), ("Workout gym","Workout gym"), ("Player apartment","Workout gym"), ("Strip club","Strip club"), ("Seedy bar","Seedy bar"), ("Yacht","Yacht"), ("Wrestling venue","Wrestling venue"), ("Beach","Beach"), ("Hotel Room","Hotel Room"), ("Shop","Shop"), ("Park","Park")]
    return
            
            

        
label setUpLocations:
    call setUpBoxingGym
    call setUpWorkoutGym
    call setUpPlayerApartment
    call setUpStripClub
    call setUpSeedyBar
    call setUpYacht
    call setUpWrestlingVenue
    call setUpBeach
    call setUpHotelRoom
    call setUpShop
    call setUpPark
    return
    
    
label setUpBoxingGym:
    $ boxingGym.public = True
    $ boxingGym.privateArea = True
    $ boxingGym.openTime = 6
    $ boxingGym.closeTime = 20
    $ boxingGym.name = locationList[0][0]
    return
    
label setUpWorkoutGym:
    $ workoutGym.public = True
    $ workoutGym.privateArea = True
    $ workoutGym.openTime = 0
    $ workoutGym.closeTime = 24
    $ workoutGym.name = locationList[1][0]
    return

label setUpPlayerApartment:
    $ playerApartment.public = False
    $ playerApartment.privateArea = True
    $ playerApartment.openTime = 0
    $ playerApartment.closeTime = 24
    $ playerApartment.name = locationList[2][0]
    return
    
label setUpStripClub:
    $ stripClub.public = True
    $ stripClub.privateArea = True
    $ stripClub.openTime = 18
    $ stripClub.closeTime = 6
    $ stripClub.name = locationList[3][0]
    return
    
label setUpSeedyBar:
    $ playerApartment.public = True
    $ playerApartment.privateArea = True
    $ playerApartment.openTime = 18
    $ playerApartment.closeTime = 6
    $ playerApartment.name = locationList[4][0]
    return
    
label setUpYacht:
    $ yacht.public = False
    $ yacht.privateArea = True
    $ yacht.openTime = 0
    $ yacht.closeTime = 24
    $ yacht.name = locationList[5][0]
    $ yacht.unlock = False
    return

label setUpWrestlingVenue:    
    $ wrestlingVenue.public = False
    $ wrestlingVenue.privateArea = True
    $ wrestlingVenue.openTime = 0
    $ wrestlingVenue.closeTime = 24
    $ wrestlingVenue.name = locationList[6][0]
    $ wrestlingVenue.unlock = False
    return
    
label setUpBeach:
    $ beach.public = True
    $ beach.privateArea = True
    $ beach.openTime = 18
    $ beach.closeTime = 6
    $ beach.name = locationList[7][0]
    return
    
label setUpHotelRoom:
    $ hotelRoom.public = True
    $ hotelRoom.privateArea = True
    $ hotelRoom.openTime = 18
    $ hotelRoom.closeTime = 6
    $ hotelRoom.name = locationList[8][0]
    return
    
label setUpShop:
    $ shop.public = True
    $ shop.privateArea = True
    $ shop.openTime = 18
    $ shop.closeTime = 6
    $ shop.name = locationList[9][0]
    return
    
label setUpPark:
    $ park.public = True
    $ park.privateArea = True
    $ park.openTime = 18
    $ park.closeTime = 6
    $ park.name = locationList[10][0]
    return

