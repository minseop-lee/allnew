insert into membertbl values ( 'Figure', '연아', '경기도 군포시 당정동');

select * from membertbl;

update membertbl set memberaddress = '서울 강남구 역삼동'
where membername='연아';

select * from membertbl;

Delete from membertbl
where membername='연아';

select * from membertbl;

select * from deletedmembertbl;


create table deletedmembertbl (
    memberid char(8),
    membername nchar(5),
    memberaddress nvarchar2(20),
    deleteDate date -- deleted date..
);

create trigger trg_deletedmembertbl
    after delete
    on membertbl
    for each row
begin
    insert into deletedmembertbl
    values (:old.memberid, :old.membername, :old.memberaddress, SYSDATE());
end;
