select referer as �z�[���y�[�W,COUNT(*) as �A�N�Z�X��,
	case
		when COUNT(*)>=50 then 'A'
		when COUNT(*)>=10 then 'B'
		else 'C'
	end as �����N
from access_log group by referer having COUNT(*)>=3
order by COUNT(*) desc;
