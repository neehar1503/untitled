
data = """
{
    "results": [
    
        {
            "Students" : ["Archana" , "anand"],
            "user": {
                
                "gender": "female",
                "name": {
                    "title": "mrs",
                    "first": "kristin",
                    "last": "bowman"
                },
                "location": {
                    "street": "1180 school lane",
                    "city": "chester",
                    "state": "south glamorgan",
                    "zip": "W78 3AH"
                },
                "email": "kristin.bowman@example.com",
                "username": "heavyelephant949",
                "password": "zaqwsx",
                "salt": "826p8XbV",
                "md5": "8f2edae551dc76703ec2893af06c8c07",
                "sha1": "371622e217efba3d7aac5b3a5c9bca07da009807",
                "sha256": "d5a095ecbaa83ada115c290b25c16a058e03e096a70928156ed5606e83579dc2",
                "registered": 1130080155,
                "dob": 1026002093,
                "phone": "013873 42191",
                "cell": "0732-593-815",
                "picture": {
                    "large": "https://randomuser.me/api/portraits/women/73.jpg",
                    "medium": "https://randomuser.me/api/portraits/med/women/73.jpg",
                    "thumbnail": "https://randomuser.me/api/portraits/thumb/women/73.jpg"
                }
            }
        }
    ],
    "nationality": "GB",
    "seed": "f34e63ab16e6d75908",
    "version": "0.8"
}
"""





jsondf = spark.read.option("multiline","true").json(sc.parallelize([data]))
jsondf.show()
jsondf.printSchema()