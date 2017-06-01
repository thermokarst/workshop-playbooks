CORE_VERSION := 2017.5
HOSTNAME := qiime2core2017-5

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  setup    to build and deploy a workshop cluster"
	@echo "  destroy  to tear down a workshop cluster"

.PHONY: deploy
deploy:
	ansible-playbook -i inventory playbooks/aws-workshop-allocate.yml

.PHONY: destroy
destroy:
	ansible-playbook -i inventory playbooks/aws-workshop-destroy.yml
