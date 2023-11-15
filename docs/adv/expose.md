# Expose a Microservice

By default, Microservices are not exposed in, or out of
the cluster where your application is running. You can
expose a microservice internally, so other microservices
may communicate with it. And you can expose a microservice
externally, so that it can be accessed publicly.

If you are familiar with Docker, this will be familiar.
The `expose` property allows communication between
containers, while the `ports` property exposes a service
on the host.

## Internally

When microservices should communicate internally, ensure
their [deploymentData](/attributes/microservice/#service)
correctly exposes them. Other Microservices running
in the cluster can raech them using their host or service name.
See examples below:

=== "Docker-Compose"

    Use the [`expose` property](https://docs.docker.com/compose/compose-file/compose-file-v3/#expose)

    ```yaml
    version: '3.9'
    services:
        mymicros:
            image: digitbrain/codeigniter-php5
            expose: 8080
    ```
    !!! success
        This example exposes the service running on port
        8080 inside this container.<br>Other Microservices in the cluster
        can reach it at <big>mymicros:8080</big>

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
      - name: http
        port: 8080
        targetPort: 8080
      selector:
        app: mymicros    
    ```
    !!! success
        This example exposes the service running on port
        8080 inside this container.<br>Other Microservices in the cluster
        can reach it at <big>mymicros-svc:8080</big>

## Externally

When microservices should be available publicly, ensure
their [deploymentData](/attributes/microservice/#service)
correctly exposes them. You can access them via the IP
of the node they are running on. See examples below:

!!! warning
    Don't forget to add the `published` or `hostPort` to
    [opened ports](/attributes/deployment/#opened-port)
    on the node where your Microservice will run!

=== "Docker-Compose"

    Use the [`ports` property](https://docs.docker.com/compose/compose-file/compose-file-v3/#ports).

    ```yaml
    services:
      mymicros:
        image: digitbrain/codeigniter-php5
        ports:
        - "80:8080"
    ```

    !!! success
        This example exposes a service running on port
        8080 inside the container.<br>It can be reached publicly
        at <big>192.168.10.20:80</big>, where 192.168.10.20 is the
        public IP address of the node hosting the Microservice.

=== "Docker-Compose (long-syntax)"

    Use the [`ports` property](https://docs.docker.com/compose/compose-file/compose-file-v3/#ports)
    with long-syntax and `host` if you need to specify the protocol.

    ```yaml
    services:
      mymicros:
        image: digitbrain/codeigniter-php5
        ports:
        - target: 8080
          published: 80
          protocol: tcp
          mode: host
    ```

    !!! success
        This example exposes a service running on port
        8080 inside the container.<br>It can be reached publicly
        at <big>192.168.10.20:80</big>, where 192.168.10.20 is the
        public IP address of the node hosting the Microservice.

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
    !!! success
        This example exposes a service running on port
        8080 inside the container.<br>It can be reached publicly
        at <big>192.168.10.20:80</big>, where 192.168.10.20 is the
        public IP address of the node hosting the Microservice.
