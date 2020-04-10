# Kubeflow On-Premise Deployment

Easily deploy Kubeflow v1.0.1 on existing Kubernetes clusters

## One-Click Deployment

### How to run

1. Clone(download) this repository to your `${HOME}` directory
    ```
    git clone https://github.com/sachua/kubeflow-easy-deploy.git
    ```
    Note: you can delete the `kubeflow-air-gapped` folder.

2. Deploy Kubeflow
    ```
    export KF_NAME=kubeflow-easy-deploy
    export BASE_DIR=${HOME}
    export KF_DIR=${BASE_DIR}/${KF_NAME}
    export PATH=$PATH:"${KF_DIR}/kfctl"
    export CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.1.yaml
    kfctl apply -V -f ${CONFIG_FILE}
    ```

## Kubeflow On-Premise Air-Gapped Deployment

### How to run

#### While connected to the Internet

1. Clone(download) this repository to your `${HOME}` directory
    ```
    git clone https://github.com/sachua/kubeflow-easy-deploy.git
    ```
2. Run the included python code, following the instructions, to pull the Docker images from public Docker registries and tagging them to your private Docker registry
    ```
    cd kubeflow-air-gapped
    python save_images.py
    ```
#### While connected to your on-premise air-gapped Kubernetes cluster
3. Run the included python code, following the instructions, to push the Docker images to your private Docker registry
    ```
    python save_images.py
    ```
4. Search and replace `$(PRIVATE_REGISTRY)` in the YAML files in the kustomize directoy to your private Docker registry's URL
5. Deploy Kubeflow
    ```
    export KF_NAME=kubeflow-air-gapped
    export BASE_DIR=${HOME}/kubeflow-easy-deploy
    export KF_DIR=${BASE_DIR}/${KF_NAME}
    export PATH=$PATH:"${BASE_DIR}/kfctl"
    export CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.1.yaml
    kfctl apply -V -f ${CONFIG_FILE}
    ```


## Deleting Kubeflow
```
cd ${KF_DIR}
kfctl delete -f ${CONFIG_FILE}
```
