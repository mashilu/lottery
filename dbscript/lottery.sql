create table LotteryCombination (
 	red1 char(2), 
 	red2 char(2), 
 	red3 char(2), 
 	red4 char(2), 
 	red5 char(2), 
 	red6 char(2), 
 	blue char(2),
 	sum char(3),          # 和值
	oddCnt char(1),       # 奇数个数
	evenCnt char(1),      # 偶数个数
	span char(2),         # 跨度
        serial2Cnt char(1),   # 两连环个数
        serial3Cnt char(1),   # 三连环个数
	serial4Cnt char(1),   # 四连环个数
        serial5Cnt char(1),   # 五连环个数
	serial6Cnt char(1),   # 六连环个数
	redDirect1Cnt char(1),# 红球1区个数(1-11)
	redDirect2Cnt char(1),# 红球2区个数(12-22)
	redDirect3Cnt char(2),# 红球3区个数(23-33)
	blueDirect1Cnt char(1), # 蓝球1区个数(1-8)
	blueDirect2Cnt char(2)  # 蓝球2区个数(9-16)  
);
