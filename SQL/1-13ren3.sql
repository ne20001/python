select referer as ホームページ,COUNT(*) as アクセス数,
	case
		when COUNT(*)>=50 then 'A'
		when COUNT(*)>=10 then 'B'
		else 'C'
	end as ランク
from access_log group by referer having COUNT(*)>=3
order by COUNT(*) desc;
