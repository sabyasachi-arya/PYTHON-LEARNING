sub_sci = {"Rohan", "Saby", "Dip", "Anny", "Joel", "Gordon", "Modi", "Kejriwal"}
sub_business = {"Sourav", "Ishan", "Saby", "Ellie", "Gordon", "Jeff", "Musk", "Mamata"}
# to find the similarities between two sets datas we use .intersection
both_sub = sub_sci.intersection(sub_business)
print(both_sub)
# .intersection finds similar elements or duplicate elements from two sets and
# creates a new set with those duplicate items (considering two same elements as one)
