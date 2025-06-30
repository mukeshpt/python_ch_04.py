# a.get("name"): Returns the value of the specified keys (and value is returned eg. "harry" is returned here).

marks = {
      "mukesh":100,
      "mohan": 67,
      "shyam": 59,
     0: "Harry"

}
print(marks.get("mukesh"))
print(marks["mukesh"])
## the question is if 10,11 line give same result then what's the difference 
#print(marks.get("mukesh2")) ## it gives none if unkone key is put.
# print(marks["mukesh2"]) it give error if unkone key is put.
