; Auto-generated. Do not edit!


(cl:in-package conveyor-srv)


;//! \htmlinclude SetCommand-request.msg.html

(cl:defclass <SetCommand-request> (roslisp-msg-protocol:ros-message)
  ((command
    :reader command
    :initarg :command
    :type cl:string
    :initform ""))
)

(cl:defclass SetCommand-request (<SetCommand-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetCommand-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetCommand-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name conveyor-srv:<SetCommand-request> is deprecated: use conveyor-srv:SetCommand-request instead.")))

(cl:ensure-generic-function 'command-val :lambda-list '(m))
(cl:defmethod command-val ((m <SetCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader conveyor-srv:command-val is deprecated.  Use conveyor-srv:command instead.")
  (command m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetCommand-request>) ostream)
  "Serializes a message object of type '<SetCommand-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'command))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'command))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetCommand-request>) istream)
  "Deserializes a message object of type '<SetCommand-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'command) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'command) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetCommand-request>)))
  "Returns string type for a service object of type '<SetCommand-request>"
  "conveyor/SetCommandRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetCommand-request)))
  "Returns string type for a service object of type 'SetCommand-request"
  "conveyor/SetCommandRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetCommand-request>)))
  "Returns md5sum for a message object of type '<SetCommand-request>"
  "c348f8d8cd3a80f54328aa4159009109")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetCommand-request)))
  "Returns md5sum for a message object of type 'SetCommand-request"
  "c348f8d8cd3a80f54328aa4159009109")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetCommand-request>)))
  "Returns full string definition for message of type '<SetCommand-request>"
  (cl:format cl:nil "string command~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetCommand-request)))
  "Returns full string definition for message of type 'SetCommand-request"
  (cl:format cl:nil "string command~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetCommand-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'command))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetCommand-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetCommand-request
    (cl:cons ':command (command msg))
))
;//! \htmlinclude SetCommand-response.msg.html

(cl:defclass <SetCommand-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil)
   (message
    :reader message
    :initarg :message
    :type cl:string
    :initform ""))
)

(cl:defclass SetCommand-response (<SetCommand-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetCommand-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetCommand-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name conveyor-srv:<SetCommand-response> is deprecated: use conveyor-srv:SetCommand-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetCommand-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader conveyor-srv:success-val is deprecated.  Use conveyor-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <SetCommand-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader conveyor-srv:message-val is deprecated.  Use conveyor-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetCommand-response>) ostream)
  "Serializes a message object of type '<SetCommand-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetCommand-response>) istream)
  "Deserializes a message object of type '<SetCommand-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetCommand-response>)))
  "Returns string type for a service object of type '<SetCommand-response>"
  "conveyor/SetCommandResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetCommand-response)))
  "Returns string type for a service object of type 'SetCommand-response"
  "conveyor/SetCommandResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetCommand-response>)))
  "Returns md5sum for a message object of type '<SetCommand-response>"
  "c348f8d8cd3a80f54328aa4159009109")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetCommand-response)))
  "Returns md5sum for a message object of type 'SetCommand-response"
  "c348f8d8cd3a80f54328aa4159009109")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetCommand-response>)))
  "Returns full string definition for message of type '<SetCommand-response>"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetCommand-response)))
  "Returns full string definition for message of type 'SetCommand-response"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetCommand-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetCommand-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetCommand-response
    (cl:cons ':success (success msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetCommand)))
  'SetCommand-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetCommand)))
  'SetCommand-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetCommand)))
  "Returns string type for a service object of type '<SetCommand>"
  "conveyor/SetCommand")