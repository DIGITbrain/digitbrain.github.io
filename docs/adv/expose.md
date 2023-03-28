# Expose a microservice

By default, microservices are not exposed in, or out of
the cluster where your application is running. You can
expose a microservice internally, so other microservices
may communicate with it. And you can expose a microservice
externally, so that it can be accessed publicly.

## Internally

When microservices should communicate internally, ensure
their [deploymentData](/attributes/microservice/#service)
correctly exposes them. Other Microservices running
in the cluster can raech them using their host or service name.
See examples below:

=== "Docker-Compose"

    Use the **shorthand** form of the `ports` property.

    ```yaml
    version: '3.9'
    services:
        mymicros:
            image: digitbrain/codeigniter-php5
            ports:
            - '80:8080'
    ```
    Exposes a service running on port 8080 inside the container at `mymicros:80` 

=== "Kubernetes"

    In addition to your `Pod`, `Deployment` or other workload,
    include a `Service`.<br>Use `---` to separate the definitions.

    ``` yaml
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: mymicros
    spec:
      <truncated>
    ---
    apiVersion: v1
    kind: Service
    metadata:
      labels:
        app: mymicros
      name: mymicros-svc
    spec:
      ports:
      - name: '80'
        port: 80
        targetPort: 8080
      selector:
        app: mymicros    
    ```
    Exposes a service running on port 8080 inside the container at `mymicros-svc:80` 

## Externally

When microservices should be available publicly, ensure
their [deploymentData](/attributes/microservice/#service)
correctly exposes them. You can access them via the IP
of the node they are running on. See examples below:

=== "Docker-Compose"

    Use the **longhand** form of `ports` and specify
    `mode: host`.

    ```yaml
    version: '3.9'
    services:
    mymicros:
      image: digitbrain/codeigniter-php5
      ports:
      - target: '8080'
        published: '80'
        protocol: tcp
        mode: host
    ```
    Exposes a service running on port 8080 inside the container at `<NODE_IP>:80` 

=== "Kubernetes"

    In your `Pod`, `Deployment` or other workload,
    include `hostPort`.

    ``` yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: mymicros
      name: mymicros
    spec:
      template:
        spec:
          containers:
          - image: digitbrain/codeigniter-php5
            name: codeigniter
            ports:
            - containerPort: 8080
              hostPort: 80
        <truncated>
    ```
    Exposes a service running on port 8080 inside the container at `<NODE_IP>:80` 