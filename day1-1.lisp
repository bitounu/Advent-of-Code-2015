(let ((in (open "./day1")))
  (format t "~a~%" (read-char in))
  (loop-for-cout dlugosc-stringa 
  	(if  (= znak \( )
		then
		(+ myfloor 1)
		else
		(- myfloor 1)
  	) 
  (close in))

