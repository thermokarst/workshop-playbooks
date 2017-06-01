# Workshop Provisioning Playbooks

## Quickstart

### Prereqs

- Ansible
- conda
- AWS Account
- A domain to point the infrastructure to
- A tarball (`certs.tar.gz`) that contains a valid `/etc/letsencrypt` dir
  (including certs, config, etc.)

### Setup

```bash
$ conda create -n workshop-prov python=2.7
$ source activate workshop-prov
$ pip install -r requirements.txt
$ export AWS_ACCESS_KEY_ID='AK123'
$ export AWS_SECRET_ACCESS_KEY='abc123'
$ export QIIME_WORKSHOP_NAME='QIIME 2 Workshop'
$ export QIIME_EIP='1.2.3.4'
$ export QIIME_SSL_DOMAIN='workshop.example.org'
```

- `QIIME_EIP` is the AWS Elastic IP that should be associated with the jump host.
- `QIIME_SSL_DOMAIN` is the the configured DNS-target for the QIIME_EIP.

### Allocate infrastructure

```bash
$ make deploy
```

### Destroy all infrastructure (including EBS Volumes)

```bash
$ make destroy
```
