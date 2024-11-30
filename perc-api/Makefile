proto-authentication:
	python -m grpc_tools.protoc -I src/proto/authentication/protobufs/ --python_out=src/proto/authentication/ --grpc_python_out=src/proto/authentication/ src/proto/authentication/protobufs/authentication.proto
	protol   --create-package   --in-place   --python-out src/authentication/ protoc --proto-path=src/authentication/protobufs/ src/authentication/protobufs/*.proto

proto-admin-mails:
	python -m grpc_tools.protoc -I src/proto/admin_mails/protobufs/ --python_out=src/proto/admin_mails/ --grpc_python_out=src/proto/admin_mails/ src/proto/admin_mails/protobufs/AdminMails.proto
	protol   --create-package   --in-place   --python-out src/proto/admin_mails/ protoc --proto-path=src/proto/admin_mails/protobufs/ src/proto/admin_mails/protobufs/*.proto

proto-perc-users:
	python -m grpc_tools.protoc -I src/proto/perc_users/protobufs/ --python_out=src/proto/perc_users/ --grpc_python_out=src/proto/perc_users/ src/proto/perc_users/protobufs/PercUsers.proto
	protol   --create-package   --in-place   --python-out src/proto/perc_users/ protoc --proto-path=src/proto/perc_users/protobufs/ src/proto/perc_users/protobufs/*.proto

server:
	python main.py
