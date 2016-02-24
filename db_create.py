from app import db
from app.models import Place

def create_places():
	place1 = Place(name='Coffee Cafe', address="123 Cafe St.", city="Englewood", state="Florida", zip_="34225", website="http://cafe.com", phone="(941)585-3099", owner="Jeff Reiher", yrs_open=1)
	db.session.add(place1)
	place2 = Place(name='Jamacian Me Crazy', address="321 Smoking Blvd", city="Englewood", state="Florida", zip_="34225", website="http://smokeup.com", phone="(941) 585-3099", owner="Bumba Clod", yrs_open=14)
	db.session.add(place2)
	place3 = Place(name='Wack Arnolds', address="2020 Wackoff Ave", city="Englewood", state="Florida", zip_="34225", website="http://www.wackarnolds.com", phone="(941)585-3099", owner="Arnold Jackson", yrs_open=7)
	db.session.add(place3)
	place4 = Place(name='Jack n Crack', address="54098 Mission Rd", city="Englewood", state="Florida", zip_="34225", website="http://www.jackcrack.com", phone="(941)585-3099", owner="Jack MeOff", yrs_open=6)
	db.session.add(place4)
	place5 = Place(name='Egg Morning', address="8am Morning St.", city="Englewood", state="Florida", zip_="34225", website="http://www.eggmorning.com", phone="(941)585-3099", owner="Mona Eggstyle", yrs_open=1)
	db.session.add(place5)
	db.session.commit()
	print "just created the restaurant table"


if __name__ == '__main__':
	db.drop_all()
	print "Just Dropped all tables"
	db.create_all()
	create_places()
