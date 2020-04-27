#!/bin/bash
cat $HOME/kubeflow-easy-deploy/images.txt | xargs -I {} -- sh -c 'docker pull {}'