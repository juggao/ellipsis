# ellipsis

ellipsis.py  (c) 2024 Rene Oudeweg 

perform basic arithmetic with ellipsis numbers

~~~


NOTE: ellipsis numbers are not p-adic numbers
(10-adic/p-adic number do not lay on the real number line)

Ellipsis calc>: 10 ++ 666
676
Ellipsis calc>: ...666
666666666666666666666
Ellipsis calc>: 10 ++ ...666
666666666666666666676
Ellipsis calc>: ...10 ++ ...666
677777777777777777776
Ellipsis calc>: ~~~10 ++ ...666
676767676767676767676
Ellipsis calc>: ~~~10 * ...666
6734006734006734006659932659932659932660
Ellipsis calc>: ~~~10 / ...666
('0', 10101010101010101010)
Ellipsis calc>: ~~~10 -- ...666
343434343434343434344
Ellipsis calc>: ~~~10 -- ~~~666
9434343434343434344
Ellipsis calc>: ~~~1234
12341234123412341234


Ellipsis calc>: intrange
current int range = 20
Enter integer size range>: 1000
Ellipsis calc>: ~~~1010
10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101
01010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
10101010101010101010101010101010101010101010101010
Ellipsis calc>: ~~~1010 ++ ~~~0101
11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
1111111111111111111111111111111111111111111111111
Ellipsis calc>: ~~~1010 / ~~~0101
('10', 0)
