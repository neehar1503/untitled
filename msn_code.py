#  RANDOMUSER


import urllib.request

from pyspark.sql.functions import *

response = urllib.request.urlopen("https://randomuser.me/api/0.8/?results=3")
urldata = str(response.read().decode('utf-8'))
print(urldata)


jsondf = spark.read.json(sc.parallelize([urldata]))
jsondf.show()
jsondf.printSchema()

withdf = jsondf.withColumn("results", expr("explode(results)"))
withdf.show()
withdf.printSchema()

final_df = withdf.selectExpr(
    "nationality",
    "results.user.gender",
    "results.user.name.title",
    "results.user.name.first",
    "results.user.name.last",
    "results.user.location.street",
    "results.user.location.city",
    "results.user.location.state",
    "results.user.location.zip",
    "results.user.email",
    "results.user.username",