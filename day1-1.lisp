(let ((in (open "./day1")))
  (let ((myfloor 1)) ; Initialize myfloor
    (loop for znak = (read-char in nil) ; Read characters in a loop
          while znak ; Continue loop until znak is non-nil (end of file)
          do (setq myfloor (if (char= znak #\() ; Compare character using char=
                                (+ myfloor 1) ; Increment if '('
                                (- myfloor 1))) ; Decrement otherwise
          ) ; End of loop
    (format t "~a~%" myfloor) ; Print final value of myfloor
    (close in))) ; Close the file
