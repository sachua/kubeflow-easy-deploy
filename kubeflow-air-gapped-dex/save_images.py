import os

# Enter your private Docker registry 
private_registry = "enter_url_here"

original_image = [
    "argoproj/argoui:v2.3.0",
    "argoproj/workflow-controller:v2.3.0",
    "busybox"
    "docker.io/istio/proxyv2:1.3.1"
    "docker.io/kubeflowkatib/mxnet-mnist",
    "docker.io/seldonio/seldon-core-operator:1.0.1",
    "gcr.io/kfserving/kfserving-controller:0.2.2",
    "gcr.io/arrikto/kubeflow/oidc-authservice:6ac9400",
    "gcr.io/google_containers/spartakus-amd64:v1.1.0",
    "gcr.io/kfserving/alibi-explainer:0.2.2",
    "gcr.io/kfserving/logger:0.2.2",
    "gcr.io/kfserving/pytorchserver:0.2.2",
    "gcr.io/kfserving/sklearnserver:0.2.2",
    "gcr.io/kfserving/storage-initializer:0.2.2",
    "gcr.io/kfserving/storage-initializer:0.2.1",
    "gcr.io/kfserving/xgbserver:0.2.2",
    "gcr.io/knative-releases/knative.dev/serving/cmd/activator:v0.11.1",
    "gcr.io/knative-releases/knative.dev/serving/cmd/autoscaler-hpa:v0.11.1",
    "gcr.io/knative-releases/knative.dev/serving/cmd/autoscaler:v0.11.1",
    "gcr.io/knative-releases/knative.dev/serving/cmd/controller:v0.11.1",
    "gcr.io/knative-releases/knative.dev/serving/cmd/networking/istio:v0.11.1",
    "gcr.io/knative-releases/knative.dev/serving/cmd/queue:v0.11.1",
    "gcr.io/knative-releases/knative.dev/serving/cmd/webhook:v0.11.1",
    "gcr.io/kubebuilder/kube-rbac-proxy:v0.4.0",
    "gcr.io/kubeflow-images-public/admission-webhook:v1.0.0-gaf96e4e3",
    "gcr.io/kubeflow-images-public/centraldashboard:v1.0.0-g3ec0de71",
    "gcr.io/kubeflow-images-public/jupyter-web-app:v1.0.0-g2bd63238",
    "gcr.io/kubeflow-images-public/katib/v1alpha3/file-metrics-collector:v0.8.0",
    "gcr.io/kubeflow-images-public/katib/v1alpha3/katib-controller:v0.8.0",
    "gcr.io/kubeflow-images-public/katib/v1alpha3/katib-db-manager:v0.8.0",
    "gcr.io/kubeflow-images-public/katib/v1alpha3/katib-ui:v0.8.0",
    "gcr.io/kubeflow-images-public/katib/v1alpha3/suggestion-chocolate:v0.8.0",
    "gcr.io/kubeflow-images-public/katib/v1alpha3/suggestion-hyperband:v0.8.0",
    "gcr.io/kubeflow-images-public/katib/v1alpha3/suggestion-hyperopt:v0.8.0",
    "gcr.io/kubeflow-images-public/katib/v1alpha3/suggestion-nasrl:v0.8.0",
    "gcr.io/kubeflow-images-public/katib/v1alpha3/suggestion-skopt:v0.8.0",
    "gcr.io/kubeflow-images-public/katib/v1alpha3/tfevent-metrics-collector:v0.8.0",
    "gcr.io/kubeflow-images-public/kfam:v1.0.0-gf3e09203",
    "gcr.io/kubeflow-images-public/kubernetes-sigs/application:1.0-beta",
    "gcr.io/kubeflow-images-public/metadata-frontend:v0.1.8",
    "gcr.io/kubeflow-images-public/metadata:v0.1.11",
    "gcr.io/kubeflow-images-public/notebook-controller:v1.0.0-gcd65ce25",
    "gcr.io/kubeflow-images-public/profile-controller:v1.0.0-ge50a8531",
    "gcr.io/kubeflow-images-public/pytorch-operator:v1.0.0-g047cf0f",
    "gcr.io/kubeflow-images-public/tf_operator:v1.0.0-g92389064",
    "gcr.io/kubeflow-images-public/tensorflow-1.15.2-notebook-cpu:1.0.0",
    "gcr.io/kubeflow-images-public/tensorflow-1.15.2-notebook-gpu:1.0.0",
    "gcr.io/kubeflow-images-public/tensorflow-2.1.0-notebook-cpu:1.0.0",
    "gcr.io/kubeflow-images-public/tensorflow-2.1.0-notebook-gpu:1.0.0",
    "gcr.io/ml-pipeline/api-server:0.2.0",
    "gcr.io/ml-pipeline/envoy:metadata-grpc",
    "gcr.io/ml-pipeline/frontend:0.2.0",
    "gcr.io/ml-pipeline/persistenceagent:0.2.0",
    "gcr.io/ml-pipeline/scheduledworkflow:0.2.0",
    "gcr.io/ml-pipeline/viewer-crd-controller:0.2.0",
    "gcr.io/ml-pipeline/visualization-server:0.2.0",
    "gcr.io/spark-operator/spark-operator:v1beta2-1.0.0-2.4.4",
    "gcr.io/tfx-oss-public/ml_metadata_store_server:v0.21.1",
    "mcr.microsoft.com/onnxruntime/server:v0.5.1",
    "metacontroller/metacontroller:v0.3.0",
    "minio/minio:RELEASE.2018-02-09T22-40-05Z",
    "mysql:5.6",
    "mysql:8",
    "mysql:8.0.3",
    "nvcr.io/nvidia/tensorrtserver:19.05-py3",
    "quay.io/coreos/dex:v2.9.0",
    "quay.io/jetstack/cert-manager-cainjector:v0.11.0",
    "quay.io/jetstack/cert-manager-controller:v0.11.0",
    "quay.io/jetstack/cert-manager-webhook:v0.11.0",
    "seldonio/mlflowserver_grpc:0.2",
    "seldonio/mlflowserver_rest:0.2",
    "seldonio/sklearnserver_grpc:0.2",
    "seldonio/sklearnserver_rest:0.2",
    "seldonio/tfserving-proxy_grpc:0.7",
    "seldonio/tfserving-proxy_rest:0.7",
    "seldonio/xgboostserver_grpc:0.2",
    "seldonio/xgboostserver_rest:0.2",
    "tensorflow/serving:1.14.0",
    "tensorflow/serving:1.14.0-gpu",
    "tensorflow/serving:latest",
    "tensorflow/tensorflow:1.8.0"
]

# Uncomment when pulling and tagging of images(while connected to Internet)
# for i in range(len(original_image)):
#     os.system("docker pull %s"%original_image[i])
#     os.system("docker tag %s %s"%(original_image[i],private_registry+"/"+original_image[i]))

# Uncomment when pushing to private Docker registry
# for i in range(len(original_image)):
#     os.system("docker push %s"%private_registry+"/"+original_image[i])