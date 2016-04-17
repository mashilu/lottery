create table dltCombination (
  id int NOT NULL,
	red1 char(2) NOT NULL,
	red2 char(2) NOT NULL,
	red3 char(2) NOT NULL,
	red4 char(2) NOT NULL,
	red5 char(2) NOT NULL,
	blue1 char(2) NOT NULL,
	blue2 char(2) NOT NULL,
	redSum char(3),          	# 红球和值
	redOddCnt char(1),       	# 红球奇数个数
	redEvenCnt char(1),      	# 红球偶数个数
	redSpan char(2),         	# 红球跨度
	redSerial2Cnt char(1),   	# 红球两连环个数
	redSerial3Cnt char(1),   	# 红球三连环个数
	redSerial4Cnt char(1),   	# 红球四连环个数
	redSerial5Cnt char(1),   	# 红球五连环个数
	redDirect1Cnt char(1),	# 红球1区个数(1-12)
	redDirect2Cnt char(1),	# 红球2区个数(13-24)
	redDirect3Cnt char(2),	# 红球3区个数(25-35)
	blueSum char(3),        # 蓝球和值
	blueOddCnt char(1),     # 蓝球奇数个数
	blueEvenCnt char(1),    # 蓝球偶数个数
	blueSpan char(2),       # 蓝球跨度
	blueSerial2Cnt char(1), # 蓝球两连环个数
	blueDirect1Cnt char(1), # 蓝球1区个数(1-6)
	blueDirect2Cnt char(2)  # 蓝球2区个数(6-12)
);

create table dltHistory (
	id int NOT NULL,
	no char(7) NOT NULL,
	red1 char(2) NOT NULL,
	red2 char(2) NOT NULL,
	red3 char(2) NOT NULL,
	red4 char(2) NOT NULL,
	red5 char(2) NOT NULL,
	blue1 char(2) NOT NULL,
	blue2 char(2) NOT NULL,
	redSum char(3),          	# 红球和值
	redOddCnt char(1),       	# 红球奇数个数
	redEvenCnt char(1),      	# 红球偶数个数
	redSpan char(2),         	# 红球跨度
	redSerial2Cnt char(1),   	# 红球两连环个数
	redSerial3Cnt char(1),   	# 红球三连环个数
	redSerial4Cnt char(1),   	# 红球四连环个数
	redSerial5Cnt char(1),   	# 红球五连环个数
	redDirect1Cnt char(1),	# 红球1区个数(1-12)
	redDirect2Cnt char(1),	# 红球2区个数(13-24)
	redDirect3Cnt char(2),	# 红球3区个数(25-35)
	blueSum char(3),        # 蓝球和值
	blueOddCnt char(1),     # 蓝球奇数个数
	blueEvenCnt char(1),    # 蓝球偶数个数
	blueSpan char(2),       # 蓝球跨度
	blueSerial2Cnt char(1), # 蓝球两连环个数
	blueDirect1Cnt char(1), # 蓝球1区个数(1-6)
	blueDirect2Cnt char(2)  # 蓝球2区个数(6-12)
);

