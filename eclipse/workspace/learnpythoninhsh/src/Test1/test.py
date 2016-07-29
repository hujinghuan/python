# -*- coding: utf-8 -*-

wordlist=['scala','akka','play framework','sbt','typesafe']
tweet='this is an example tweet talking about scala and sbt'
print(map(lambda x:x in tweet.split(),wordlist))