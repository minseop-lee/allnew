select * from membertbl where memberaddress like '경기%';

select * from membertbl where membername = '지운이';

create view hr.membertbl_view
as
    select membername, memberaddress
    from hr.membertbl;
    
select * from membertbl_view;


select count(*) from membertbl;

select count(*) from producttbl;

create procedure hr.myProc as
var1 int;
var2 int;
begin
    select count(*) into var1 from hr.membertbl;
    select count(*) into var2 from hr.producttbl;
    DBMS_OUTPUT.PUT_LINE(var1+var2);
end;