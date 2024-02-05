# ellipsis

ellipsis.py 0.0.3 (c) 2024 Rene Oudeweg 

perform basic arthitmetic with ellipsis numbers

~~~


NOTE: ellipsis numbers are not p-adic numbers (10-adic/p-adic number do not lay on the real number line)

Ellipsis calc>: 10 ++ 666
676
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
