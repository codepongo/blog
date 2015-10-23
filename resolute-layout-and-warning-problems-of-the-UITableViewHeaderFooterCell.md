Resolute the Layout and Warnning Problems of UITableViewHeaderFooterCell
================
解决UITableVIewHeaderCell的布局和警告问题
-----------------
in the custom UITableViewHeaderFooterCell, the width of the reuse view can not 
be configed in a right way. And there is a warnning 
'Setting the background color on UITableViewHeaderFooterView has been deprecated. Please use contentView.backgroundColor instead.'
during the running.


the reason that the view that is added to xib is UITableViewCell. instead of **UICollectionReusableView**, the problems are fixed.


在定制UITableView的section的Footer时，重用的模板view不能正确的布局，width总不能正确匹配并且
程序运行时，总是出现'Setting the background color on UITableViewHeaderFooterView has been deprecated. Please use contentView.backgroundColor instead.'的警告。


原因是，在向xib添加view时，使用的是UITableViewCell，用UICollectionReusableView替换即可可解决问题。
