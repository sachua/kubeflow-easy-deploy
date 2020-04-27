#!/bin/bash
echo "Enter your private registry URL"
read PRIVATE_REGISTRY
grep -Ril '${HOME}' $HOME/kubeflow-easy-deploy | xargs sed -i 's|${HOME}|'"$HOME"'|g'
grep -Ril '${PRIVATE_REGISTRY}' $HOME/kubeflow-easy-deploy/manifests | xargs sed -i 's|${PRIVATE_REGISTRY}|'"$PRIVATE_REGISTRY"'|g'
cat $HOME/kubeflow-easy-deploy/images.txt | xargs -I {} -- sh -c 'docker tag {} '"$PRIVATE_REGISTRY"'/{} && docker push '"$PRIVATE_REGISTRY"'/kubeflow/{}'