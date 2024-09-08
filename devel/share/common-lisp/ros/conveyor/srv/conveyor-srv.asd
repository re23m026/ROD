
(cl:in-package :asdf)

(defsystem "conveyor-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SetCommand" :depends-on ("_package_SetCommand"))
    (:file "_package_SetCommand" :depends-on ("_package"))
  ))