begin tran

select top 20 * from email_reci
order by 6 desc

;with recis as(
select reci_id 
from email_reci 
where email_id in (select email_id from rep_proc where rep_code like '%123456%')),
find_person as(
select DISTINCT re.reci_id, rp.email_id
from reci as re
cross join rep_proc as rp where rp.rep_code like  '%123456%' and re.email_add like  '%megvagy%' )
INSERT INTO email_reci
select fp.reci_id, fp.email_id, 1, dateadd(day, -10, GETDATE()), 'lics-locs-admin', GETDATE()
from find_person as fp
where reci_id not in (select * from recis)

select top 20 * from email_reci
order by 6 desc

rollback tran
