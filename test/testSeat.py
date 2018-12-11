from SRRMSv2.api.status import get_seat

seat_avaibility = 
{
	"train_id": "13467"
}
print(get_seat(data))

############### booking a ticket
passanger = 
{
	"email": "test@test.com",
	"pname": "testtest",
	"age": "21",
	"gender": "F",
	"source": "Howrah Junction",
	"dest": "B",
	"train_id": "13467",
	"username": "test",
	"date": "10/12/2018",
	"key": "B55L5S63I8JSHHAV4YM1D4H7QAB7GCUI"
}


######### adding a user
user = 
{
	"action": "add",
	"public_id": "99",
	"email": "test@test.com",
	"username": "test",
	"password": "testpassword"
}

login = 
{
	"email": "test@test.com",
	"password": "testpassword"
}