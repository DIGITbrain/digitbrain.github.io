# Expose a microservice

By default, microservices are not exposed in, or out of
the cluster where your application is running. You can
expose a microservice internally, so other microservices
may communicate with it. And you can expose a microservice
externally, so that it can be accessed publicly.

## Internally

When microservices should communicate internally, ensure
their [deploymentData](/attributes/microservice/#service)
correctly exposes them. See Docker-Compose and Kubernetes
examples below:

=== "Docker-Compose"

    Use the **shorthand** form of the `ports` property.

    ```json
    {
        "version": "3.9",
        "services": {
            "mymicros": {
            "image": "digitbrain/codeigniter-php5",
            "ports": [
                "80:80"
            ],
        }
    }
    ```

=== "Kubernetes"

    In addition to your `Pod`, `Deployment` or other workload,
    include a `Service`.

    ``` json
    [
        {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "labels": {
                    "app": "mymicros"
                },
            <truncated>
        },
        {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {
                "labels": {
                    "app": "mymicros"
                },
                "name": "mymicros"
            },
            "spec": {
                "ports": [
                    {
                        "name": "80",
                        "port": 80,
                        "targetPort": 80
                    }
                ],
                "selector": {
                    "app": "mymicros"
                }
            }
        }
    ]
    ```

## Externally

When microservices should be available publicly, ensure
their [deploymentData](/attributes/microservice/#service)
correctly exposes them. See Docker-Compose and Kubernetes
examples below:

=== "Docker-Compose"

    Use the **longhand** form of `ports` and specify
    `mode: host`.

    ```json
    {
        "version": "3.9",
        "services": {
            "mymicros": {
            "image": "digitbrain/codeigniter-php5",
            "ports": [
                {                
                    "target": "80",
                    "published":"80",
                    "protocol": "tcp",
                    "mode": "host"
                }
            ],
        }
    }
    ```

=== "Kubernetes"

    In your `Pod`, `Deployment` or other workload,
    include `hostPort`.

    ``` json
    [
        {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "labels": {
                    "app": "mymicros"
                },
                "name": "mymicros"
            },
            "spec": {  
                "template": {
                    "spec": {
                        "containers": [
                            {            
                                "image": "digitbrain/codeigniter-php5",
                                "name": "codeigniter",
                                "ports": [
                                    {
                                        "containerPort": 80,
                                        "hostPort": 80
                                    }
                                ],
        <truncated>
    ]
    ```