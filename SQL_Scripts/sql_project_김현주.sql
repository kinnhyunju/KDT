use sql_project;

alter table popular_music_over10000 add primary key (지역);
alter table popular_music_to10000 add primary key (지역);
alter table popular_music_to5000 add primary key (지역);

--  티켓 가격 평균 금액 테이블 만들기
-- create table popular_avg
-- (region varchar(10),
-- small float, medium float, large float,
-- primary key(region));

select * from popular_avg;

# 공연 규모별 공연 건수
select pt5.지역, pt5.공연건수 as '5,000명 이하', pt10.공연건수 as '10,000명 이하', po10.공연건수 as '10,000명 이상'
from popular_music_to5000 pt5
inner join popular_music_to10000 pt10 on pt5.지역 = pt10.지역
inner join popular_music_over10000 po10 on pt5.지역 = po10.지역;

# 대중음악 공연 티켓가격 평균과 대중음악 공연 정보 테이블 연결하기
alter table popular_avg add foreign key (region) references popular_music_over10000 (지역);
alter table popular_avg add foreign key (region) references popular_music_to10000 (지역);
alter table popular_avg add foreign key (region) references popular_music_to5000 (지역);

# 지역 참조 테이블 만들기
create table region_ref (지역 varchar(20));
insert into region_ref
values ('서울'), ('경기/인천'), ('강원도'),('경상도'),('전라도'),('충청도'),('제주도');

insert into region_ref
values ('합계');

# 각 데이터 테이블 지역 참조 테이블과 연결 --------------------------------------------------------
# 지역별 임금 데이터
alter table region_ref add primary key (지역);
alter table region_wage add foreign key (region) references region_ref (지역);

# 대중음악
alter table popular_music_over10000 add foreign key (지역) references region_ref (지역);
alter table popular_music_to10000 add foreign key (지역) references region_ref (지역);
alter table popular_music_to5000 add foreign key (지역) references region_ref (지역);

# 뮤지컬
alter table musical_oversea add foreign key (지역) references region_ref (지역);
alter table musical_small add foreign key (지역) references region_ref (지역);
alter table musical_large add foreign key (지역) references region_ref (지역);

# 클랙식, 국악, 연극
alter table theater add foreign key (지역) references region_ref (지역);
alter table classic add foreign key (지역) references region_ref (지역);
alter table gugak add foreign key (지역) references region_ref (지역);