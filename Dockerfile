# New kafka image instead of confluent
# WHY : This images support JMX for  monitoring purposes
# Github : https://github.com/wurstmeister/kafka-docker

FROM wurstmeister/kafka

ADD prom-jmx-agent-config.yml /usr/app/prom-jmx-agent-config.yml
ADD https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.6/jmx_prometheus_javaagent-0.6.jar /usr/app/jmx_prometheus_javaagent.jar
