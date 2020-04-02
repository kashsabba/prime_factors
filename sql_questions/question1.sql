
--postgresql
-- question 1

CREATE TABLE track_media(
    auto_inc int PRIMARY KEY NOT NULL,
    mediaid char,
	modified date
);

INSERT INTO track_media(auto_inc, mediaid, modified)
VALUES
	(1, 'x', '2001-02-01'),
	(2, 'x', '2001-01-31'),
	(3, 'y', '2001-01-31'),
	(4, 'y', '2001-02-01'),
	(5, 'y', '2001-01-30'),
	(6, 'z', '2001-01-26');

-- query for question 1
select track_media.mediaid, track_media.auto_inc
from (select mediaid, max(modified) as latest_modified from track_media group by mediaid) as track_media_x
inner join track_media on 
((track_media.mediaid = track_media_x.mediaid) and (track_media.modified = track_media_x.latest_modified));