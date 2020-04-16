# Kubeflow On-Premise Deployment

Easily deploy Kubeflow v1.0.1 on existing Kubernetes clusters with 1 command.

## One-Click Deployment

### How to run

1. Clone(download) this repository to your `${HOME}` directory

    ```bash
    git clone https://github.com/sachua/kubeflow-easy-deploy.git
    ```
    
    Note: you can delete the `kubeflow-air-gapped` folder.

2. Deploy Kubeflow

    ```bash
    export KF_NAME=kubeflow-easy-deploy
    export BASE_DIR=${HOME}
    export KF_DIR=${BASE_DIR}/${KF_NAME}
    cd ${KF_DIR}
    export PATH=$PATH:"${KF_DIR}"
    export CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.1.yaml
    kfctl apply -V -f ${CONFIG_FILE}
    ```

## Kubeflow On-Premise Air-Gapped Deployment

### How to run

#### While connected to the Internet

1. Clone(download) this repository to your `${HOME}` directory

    ```bash
    git clone https://github.com/sachua/kubeflow-easy-deploy.git
    ```
    
2. Run the included python code, following the instructions in the code comments, to pull the Docker images from public Docker registries and tagging them to your private Docker registry

    ```bash
    cd kubeflow-air-gapped
    python save_images.py
    ```
    
#### While connected to your on-premise air-gapped Kubernetes cluster

3. Run the included python code, following the instructions in the code comments, to push the Docker images to your private Docker registry

    ```bash
    python save_images.py
    ```
    
4. Search and replace `$(PRIVATE_REGISTRY)` in the YAML files to your private Docker registry's URL

5. Replace ${HOME} in kfctl_k8s_istio.v1.0.1.yaml repos uri to your `${HOME}` directory

6. Deploy Kubeflow

    ```bash
    export KF_NAME=kubeflow-air-gapped
    export BASE_DIR=${HOME}/kubeflow-easy-deploy
    export KF_DIR=${BASE_DIR}/${KF_NAME}
    export PATH=$PATH:"${BASE_DIR}"
    export CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.1.yaml
    kfctl apply -V -f ${CONFIG_FILE}
    ```
## Deleting Kubeflow

```bash
cd ${KF_DIR}
kfctl delete -f ${CONFIG_FILE}
```



## Multi-user, auth-enabled Kubeflow On-Premise Air-Gapped Deployment

### How to run

#### While connected to the Internet

1. Clone(download) this repository to your `${HOME}` directory

    ```bash
    git clone https://github.com/sachua/kubeflow-easy-deploy.git
    ```
    
2. Run the included python code, following the instructions in the code comments, to pull the Docker images from public Docker registries and tagging them to your private Docker registry

    ```bash
    cd kubeflow-air-gapped-dex
    python save_images.py
    ```
    
#### While connected to your on-premise air-gapped Kubernetes cluster

3. Run the included python code, following the instructions in the code comments, to push the Docker images to your private Docker registry

    ```bash
    python save_images.py
    ```
    
4. Search and replace `$(PRIVATE_REGISTRY)` in the YAML files to your private Docker registry's URL

5. Replace ${HOME} in kfctl_istio_dex.v1.0.1.yaml repos uri to your `${HOME}` directory

6. Deploy Kubeflow

    ```bash
    export KF_NAME=kubeflow-air-gapped-dex
    export BASE_DIR=${HOME}/kubeflow-easy-deploy
    export KF_DIR=${BASE_DIR}/${KF_NAME}
    export PATH=$PATH:"${BASE_DIR}"
    export CONFIG_FILE=${KF_DIR}/kfctl_istio_dex.v1.0.1.yaml
    export ISTIO_CONFIG=${KF_DIR}/istio-manifest.yaml
    kubectl apply -f ${ISTIO_CONFIG}
    kfctl apply -V -f ${CONFIG_FILE}
    ```

### Basic authentication

- Default credentials are:

    ```ldif
    Username: admin@kubeflow.org
    Password: 12341234
    ```

- Adding static users:

    ```bash
    # Download the dex config
    kubectl get configmap dex -n auth -o jsonpath='{.data.config\.yaml}' > dex-config.yaml

    # Edit the dex config with extra users.
    # The password must be hashed with bcrypt with an at least 10 difficulty level.
    # You can use an online tool like: https://passwordhashing.com/BCrypt

    # After editing the config, update the ConfigMap
    kubectl create configmap dex --from-file=config.yaml=dex-config.yaml -n auth --dry-run -oyaml | kubectl apply -f -

    # Restart Dex to pick up the changes in the ConfigMap
    kubectl rollout restart deployment dex -n auth
    ```

### Authentication with LDAP database

Refer to [LDAP](LDAP/) folder to set up an LDAP database and use it with Dex.

## Deleting multi-user, auth-enabled Kubeflow

```bash
cd ${KF_DIR}
kubectl delete -f ${ISTIO_CONFIG}
kfctl delete -f ${CONFIG_FILE}
```
