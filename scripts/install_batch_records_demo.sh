#!/bin/bash
#
# Install sample batcj jobs on the nightly dev servers.
#

TENANTS+=('core' 'lhmc' 'fcart' 'anthro' 'materials' 'bonsai' 'publicart')

for tenant in ${TENANTS[*]}
do
  ./scripts/install_batch_records.sh "https://${tenant}.collectionspace.org" "$tenant.collectionspace.org"
done
