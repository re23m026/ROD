;; Auto-generated. Do not edit!


(when (boundp 'conveyor::SetCommand)
  (if (not (find-package "CONVEYOR"))
    (make-package "CONVEYOR"))
  (shadow 'SetCommand (find-package "CONVEYOR")))
(unless (find-package "CONVEYOR::SETCOMMAND")
  (make-package "CONVEYOR::SETCOMMAND"))
(unless (find-package "CONVEYOR::SETCOMMANDREQUEST")
  (make-package "CONVEYOR::SETCOMMANDREQUEST"))
(unless (find-package "CONVEYOR::SETCOMMANDRESPONSE")
  (make-package "CONVEYOR::SETCOMMANDRESPONSE"))

(in-package "ROS")





(defclass conveyor::SetCommandRequest
  :super ros::object
  :slots (_command ))

(defmethod conveyor::SetCommandRequest
  (:init
   (&key
    ((:command __command) "")
    )
   (send-super :init)
   (setq _command (string __command))
   self)
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:serialization-length
   ()
   (+
    ;; string _command
    4 (length _command)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _command
       (write-long (length _command) s) (princ _command s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _command
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass conveyor::SetCommandResponse
  :super ros::object
  :slots (_success _message ))

(defmethod conveyor::SetCommandResponse
  (:init
   (&key
    ((:success __success) nil)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _success __success)
   (setq _message (string __message))
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass conveyor::SetCommand
  :super ros::object
  :slots ())

(setf (get conveyor::SetCommand :md5sum-) "c348f8d8cd3a80f54328aa4159009109")
(setf (get conveyor::SetCommand :datatype-) "conveyor/SetCommand")
(setf (get conveyor::SetCommand :request) conveyor::SetCommandRequest)
(setf (get conveyor::SetCommand :response) conveyor::SetCommandResponse)

(defmethod conveyor::SetCommandRequest
  (:response () (instance conveyor::SetCommandResponse :init)))

(setf (get conveyor::SetCommandRequest :md5sum-) "c348f8d8cd3a80f54328aa4159009109")
(setf (get conveyor::SetCommandRequest :datatype-) "conveyor/SetCommandRequest")
(setf (get conveyor::SetCommandRequest :definition-)
      "string command
---
bool success
string message
")

(setf (get conveyor::SetCommandResponse :md5sum-) "c348f8d8cd3a80f54328aa4159009109")
(setf (get conveyor::SetCommandResponse :datatype-) "conveyor/SetCommandResponse")
(setf (get conveyor::SetCommandResponse :definition-)
      "string command
---
bool success
string message
")



(provide :conveyor/SetCommand "c348f8d8cd3a80f54328aa4159009109")


