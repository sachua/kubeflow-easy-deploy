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
    wget https://raw.githubusercontent.com/sachua/kubeflow-manifests/master/kfdef/kfctl_k8s_istio.v1.0.2.yaml
    export PATH=$PATH:"${KF_DIR}"
    export CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.2.yaml
    kfctl apply -V -f ${CONFIG_FILE}
    ```

## Kubeflow On-Premise Air-Gapped Deployment

### How to run

#### While connected to the Internet

1. Clone(download) this repository to your `${HOME}` directory

    ```bash
    git clone https://github.com/sachua/kubeflow-easy-deploy.git
    ```
    
2. Run the shell script to pull the Docker images from public Docker registries

    ```bash
    sh $HOME/kubeflow-easy-deploy/pull_images.sh
    ```
    
#### While connected to your on-premise air-gapped Kubernetes cluster

3. Run the shell script to tag and push the Docker images to your private Docker registry

    ```bash
    sh $HOME/kubeflow-easy-deploy/push_images.sh
    ```
    
4. Replace ${HOME} in kfctl_k8s_istio.v1.0.2.yaml repos uri to your `${HOME}` directory

5. Choose and deploy the type of Kubeflow deployment you want:

    1. Basic, no-auth Kubeflow

        ```bash
        export KF_NAME=kubeflow-easy-deploy
        export BASE_DIR=${HOME}
        export KF_DIR=${BASE_DIR}/${KF_NAME}
        export PATH=$PATH:"${BASE_DIR}"
        export CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.2.yaml
        kfctl apply -V -f ${CONFIG_FILE}
        ```
    2. Multi-user, auth-enabled Kubeflow

        ```bash
        export KF_NAME=kubeflow-easy-deploy
        export BASE_DIR=${HOME}
        export KF_DIR=${BASE_DIR}/${KF_NAME}
        export PATH=$PATH:"${BASE_DIR}"
        export CONFIG_FILE=${KF_DIR}/kfctl_istio_dex.v1.0.2.yaml
        kfctl apply -V -f ${CONFIG_FILE}
        ```
    3. Multi-user, auth-enabled Kubeflow (Try this if 2nd option does not work)

        ```bash
        export KF_NAME=kubeflow-easy-deploy
        export BASE_DIR=${HOME}
        export KF_DIR=${BASE_DIR}/${KF_NAME}
        export PATH=$PATH:"${BASE_DIR}"
        export CONFIG_FILE=${KF_DIR}/kfctl_istio_nosds_dex.v1.0.2.yaml
        kfctl apply -V -f ${CONFIG_FILE}
        ```

## Multi-user, auth-enabled Kubeflow configuration

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

## Deleting Kubeflow

```bash
cd ${KF_DIR}
kfctl delete -f ${CONFIG_FILE}
```
