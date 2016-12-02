[原文][1]


红黑树与哈希表比较：
* 哈希表操作不够清楚。
* 红黑树插入，删除，查找速度可均摊。
* 在最坏情况下，树有更好的性能。


这大半是因为一个历史意外。在标准规则被确定之前，标准容器（包括迭代器和算法）很晚才被加入。所以，在标准确定之前，没有充分考虑到哈希表的定义，并且也没有足够时间加入。所以标准只包括了一个基于树的map。

C++11 加入了基于hash的std::unordered_map（以及std:unordered_set)。
















[1]:http://stackoverflow.com/questions/22665902/why-stdmap-is-red-black-tree-and-not-hash-table
