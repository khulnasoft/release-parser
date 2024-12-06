# release-data

Common Release Data for various projects in a consumable format. Current format is:

* `filename` matches the corresponding filename in the products/ directory in releaselog repository.
* Top-level keys are version strings.
* Non-stable versions are not included (nightly, beta, RC etc)
* Values are release dates in YYYY-MM-DD format
* Wherever possible, dates are as per the release-timezone.

## Guiding Principles

* Scripts that update this information should be stand-alone and simple.
* Code should not rely on existing data, and built it from scratch. (In case upstream information changes, we should reflect this change)
* It should be easy to add a new script in any language.
* Run everything on GitHub Actions.

## Currently Updated

As of 2024-08-15, 258 of the 329 products tracked by releaselog have automatically tracked releases:

| Product                                       | Permalink                                                                                              | Auto | Method(s)                      |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------|------|--------------------------------|
| Akeneo PIM                                    | [`/akeneo-pim`](https://releaselog.netlify.app/akeneo-pim)                                                     | ✔️   | git, release_table             |
| Alibaba Dragonwell                            | [`/alibaba-dragonwell`](https://releaselog.netlify.app/alibaba-dragonwell)                                     | ✔️   | git, release_table             |
| AlmaLinux OS                                  | [`/almalinux`](https://releaselog.netlify.app/almalinux)                                                       | ✔️   | distrowatch                    |
| Alpine Linux                                  | [`/alpine`](https://releaselog.netlify.app/alpine)                                                             | ✔️   | git, release_table             |
| Amazon CDK                                    | [`/amazon-cdk`](https://releaselog.netlify.app/amazon-cdk)                                                     | ✔️   | git                            |
| Amazon Corretto                               | [`/amazon-corretto`](https://releaselog.netlify.app/amazon-corretto)                                           | ✔️   | github_releases, release_table |
| Amazon Glue                                   | [`/amazon-glue`](https://releaselog.netlify.app/amazon-glue)                                                   | ❌    |                                |
| Amazon Linux                                  | [`/amazon-linux`](https://releaselog.netlify.app/amazon-linux)                                                 | ✔️   | docker_hub                     |
| Amazon Neptune                                | [`/amazon-neptune`](https://releaselog.netlify.app/amazon-neptune)                                             | ✔️   | custom, release_table          |
| Amazon RDS for MySQL                          | [`/amazon-rds-mysql`](https://releaselog.netlify.app/amazon-rds-mysql)                                         | ✔️   | custom, release_table          |
| Amazon RDS for PostgreSQL                     | [`/amazon-rds-postgresql`](https://releaselog.netlify.app/amazon-rds-postgresql)                               | ✔️   | custom, release_table          |
| Android OS                                    | [`/android`](https://releaselog.netlify.app/android)                                                           | ❌    |                                |
| Angular                                       | [`/angular`](https://releaselog.netlify.app/angular)                                                           | ✔️   | git                            |
| AngularJS                                     | [`/angularjs`](https://releaselog.netlify.app/angularjs)                                                       | ✔️   | npm                            |
| Ansible-core                                  | [`/ansible-core`](https://releaselog.netlify.app/ansible-core)                                                 | ✔️   | git                            |
| Ansible                                       | [`/ansible`](https://releaselog.netlify.app/ansible)                                                           | ✔️   | pypi                           |
| antiX Linux                                   | [`/antix`](https://releaselog.netlify.app/antix)                                                               | ✔️   | distrowatch                    |
| Apache ActiveMQ                               | [`/apache-activemq`](https://releaselog.netlify.app/apache-activemq)                                           | ✔️   | git                            |
| Apache Airflow                                | [`/apache-airflow`](https://releaselog.netlify.app/apache-airflow)                                             | ✔️   | pypi, release_table            |
| Apache Camel                                  | [`/apache-camel`](https://releaselog.netlify.app/apache-camel)                                                 | ✔️   | maven                          |
| Apache Cassandra                              | [`/apache-cassandra`](https://releaselog.netlify.app/apache-cassandra)                                         | ✔️   | git                            |
| Apache Flink                                  | [`/apache-flink`](https://releaselog.netlify.app/apache-flink)                                                 | ✔️   | git                            |
| Apache Groovy                                 | [`/apache-groovy`](https://releaselog.netlify.app/apache-groovy)                                               | ✔️   | maven                          |
| Apache Hadoop                                 | [`/apache-hadoop`](https://releaselog.netlify.app/apache-hadoop)                                               | ✔️   | git                            |
| Apache Hop                                    | [`/apache-hop`](https://releaselog.netlify.app/apache-hop)                                                     | ✔️   | github_releases                |
| Apache HTTP Server                            | [`/apache`](https://releaselog.netlify.app/apache)                                                             | ✔️   | custom                         |
| Apache Kafka                                  | [`/apache-kafka`](https://releaselog.netlify.app/apache-kafka)                                                 | ✔️   | git, release_table             |
| Apache Lucene                                 | [`/apache-lucene`](https://releaselog.netlify.app/apache-lucene)                                               | ✔️   | maven                          |
| Apache Maven                                  | [`/maven`](https://releaselog.netlify.app/maven)                                                               | ✔️   | maven                          |
| Apache Spark                                  | [`/apache-spark`](https://releaselog.netlify.app/apache-spark)                                                 | ✔️   | git                            |
| Apache Struts                                 | [`/apache-struts`](https://releaselog.netlify.app/apache-struts)                                               | ✔️   | maven                          |
| API Platform                                  | [`/api-platform`](https://releaselog.netlify.app/api-platform)                                                 | ✔️   | git                            |
| Apple Watch                                   | [`/apple-watch`](https://releaselog.netlify.app/apple-watch)                                                   | ❌    |                                |
| ArangoDB                                      | [`/arangodb`](https://releaselog.netlify.app/arangodb)                                                         | ✔️   | git                            |
| Argo CD                                       | [`/argo-cd`](https://releaselog.netlify.app/argo-cd)                                                           | ✔️   | git                            |
| Artifactory                                   | [`/artifactory`](https://releaselog.netlify.app/artifactory)                                                   | ✔️   | custom                         |
| AWS Lambda                                    | [`/aws-lambda`](https://releaselog.netlify.app/aws-lambda)                                                     | ✔️   | custom                         |
| Azul Zulu                                     | [`/azul-zulu`](https://releaselog.netlify.app/azul-zulu)                                                       | ❌    |                                |
| Azure DevOps Server                           | [`/azure-devops-server`](https://releaselog.netlify.app/azure-devops-server)                                   | ❌    |                                |
| Azure Kubernetes Service                      | [`/azure-kubernetes-service`](https://releaselog.netlify.app/azure-kubernetes-service)                         | ❌    |                                |
| Bazel                                         | [`/bazel`](https://releaselog.netlify.app/bazel)                                                               | ✔️   | git, release_table             |
| Elastic Beats                                 | [`/beats`](https://releaselog.netlify.app/beats)                                                               | ✔️   | git                            |
| Bellsoft Liberica JDK                         | [`/bellsoft-liberica`](https://releaselog.netlify.app/bellsoft-liberica)                                       | ✔️   | github_releases                |
| Blender                                       | [`/blender`](https://releaselog.netlify.app/blender)                                                           | ✔️   | git                            |
| Bootstrap                                     | [`/bootstrap`](https://releaselog.netlify.app/bootstrap)                                                       | ✔️   | git                            |
| Bun                                           | [`/bun`](https://releaselog.netlify.app/bun)                                                                   | ✔️   | git                            |
| CakePHP                                       | [`/cakephp`](https://releaselog.netlify.app/cakephp)                                                           | ✔️   | git                            |
| Calico                                        | [`/calico`](https://releaselog.netlify.app/calico)                                                             | ✔️   | git                            |
| CentOS Stream                                 | [`/centos-stream`](https://releaselog.netlify.app/centos-stream)                                               | ❌    |                                |
| CentOS                                        | [`/centos`](https://releaselog.netlify.app/centos)                                                             | ❌    |                                |
| Centreon                                      | [`/centreon`](https://releaselog.netlify.app/centreon)                                                         | ✔️   | git, release_table             |
| cert-manager                                  | [`/cert-manager`](https://releaselog.netlify.app/cert-manager)                                                 | ✔️   | git                            |
| CFEngine                                      | [`/cfengine`](https://releaselog.netlify.app/cfengine)                                                         | ✔️   | git                            |
| Chef Infra Client                             | [`/chef-infra-client`](https://releaselog.netlify.app/chef-infra-client)                                       | ✔️   | custom                         |
| Chef Infra Server                             | [`/chef-infra-server`](https://releaselog.netlify.app/chef-infra-server)                                       | ✔️   | custom                         |
| Citrix Virtual Apps and Desktops              | [`/citrix-vad`](https://releaselog.netlify.app/citrix-vad)                                                     | ❌    |                                |
| CKEditor                                      | [`/ckeditor`](https://releaselog.netlify.app/ckeditor)                                                         | ❌    |                                |
| ClamAV                                        | [`/clamav`](https://releaselog.netlify.app/clamav)                                                             | ✔️   | git                            |
| CockroachDB                                   | [`/cockroachdb`](https://releaselog.netlify.app/cockroachdb)                                                   | ✔️   | git, release_table             |
| Adobe ColdFusion                              | [`/coldfusion`](https://releaselog.netlify.app/coldfusion)                                                     | ❌    |                                |
| Composer                                      | [`/composer`](https://releaselog.netlify.app/composer)                                                         | ✔️   | git                            |
| Confluence                                    | [`/confluence`](https://releaselog.netlify.app/confluence)                                                     | ✔️   | atlassian_eol, custom          |
| Hashicorp Consul                              | [`/consul`](https://releaselog.netlify.app/consul)                                                             | ✔️   | git                            |
| containerd                                    | [`/containerd`](https://releaselog.netlify.app/containerd)                                                     | ✔️   | git, release_table             |
| Contao                                        | [`/contao`](https://releaselog.netlify.app/contao)                                                             | ✔️   | git                            |
| Contour                                       | [`/contour`](https://releaselog.netlify.app/contour)                                                           | ✔️   | git                            |
| Google Container-Optimized OS (COS)           | [`/cos`](https://releaselog.netlify.app/cos)                                                                   | ✔️   | custom                         |
| Couchbase Server                              | [`/couchbase-server`](https://releaselog.netlify.app/couchbase-server)                                         | ✔️   | custom, release_table          |
| Craft CMS                                     | [`/craft-cms`](https://releaselog.netlify.app/craft-cms)                                                       | ✔️   | git, release_table             |
| dbt Core                                      | [`/dbt-core`](https://releaselog.netlify.app/dbt-core)                                                         | ✔️   | git                            |
| DaoCloud Enterprise                           | [`/dce`](https://releaselog.netlify.app/dce)                                                                   | ❌    |                                |
| Debian                                        | [`/debian`](https://releaselog.netlify.app/debian)                                                             | ✔️   | custom, release_table          |
| Dependency-Track                              | [`/dependency-track`](https://releaselog.netlify.app/dependency-track)                                         | ✔️   | git                            |
| Devuan                                        | [`/devuan`](https://releaselog.netlify.app/devuan)                                                             | ✔️   | distrowatch                    |
| Django                                        | [`/django`](https://releaselog.netlify.app/django)                                                             | ✔️   | git, release_table             |
| Docker Engine                                 | [`/docker-engine`](https://releaselog.netlify.app/docker-engine)                                               | ✔️   | git                            |
| Microsoft .NET                                | [`/dotnet`](https://releaselog.netlify.app/dotnet)                                                             | ✔️   | git, release_table             |
| Microsoft .NET Framework                      | [`/dotnetfx`](https://releaselog.netlify.app/dotnetfx)                                                         | ✔️   | release_table                  |
| Drupal                                        | [`/drupal`](https://releaselog.netlify.app/drupal)                                                             | ✔️   | git                            |
| Drush                                         | [`/drush`](https://releaselog.netlify.app/drush)                                                               | ✔️   | git, release_table             |
| Eclipse Jetty                                 | [`/eclipse-jetty`](https://releaselog.netlify.app/eclipse-jetty)                                               | ✔️   | maven                          |
| Eclipse Temurin                               | [`/eclipse-temurin`](https://releaselog.netlify.app/eclipse-temurin)                                           | ✔️   | github_releases, release_table |
| Amazon EKS                                    | [`/amazon-eks`](https://releaselog.netlify.app/amazon-eks)                                                     | ✔️   | custom, release_table          |
| Elasticsearch                                 | [`/elasticsearch`](https://releaselog.netlify.app/elasticsearch)                                               | ✔️   | git                            |
| Electron                                      | [`/electron`](https://releaselog.netlify.app/electron)                                                         | ✔️   | npm, release_table             |
| Elixir                                        | [`/elixir`](https://releaselog.netlify.app/elixir)                                                             | ✔️   | git                            |
| Ember                                         | [`/emberjs`](https://releaselog.netlify.app/emberjs)                                                           | ✔️   | npm, release_table             |
| Envoy                                         | [`/envoy`](https://releaselog.netlify.app/envoy)                                                               | ✔️   | git, release_table             |
| Erlang                                        | [`/erlang`](https://releaselog.netlify.app/erlang)                                                             | ✔️   | git                            |
| etcd                                          | [`/etcd`](https://releaselog.netlify.app/etcd)                                                                 | ✔️   | git                            |
| EuroLinux                                     | [`/eurolinux`](https://releaselog.netlify.app/eurolinux)                                                       | ✔️   | distrowatch                    |
| Exim                                          | [`/exim`](https://releaselog.netlify.app/exim)                                                                 | ✔️   | git                            |
| Fairphone                                     | [`/fairphone`](https://releaselog.netlify.app/fairphone)                                                       | ❌    |                                |
| Fedora Linux                                  | [`/fedora`](https://releaselog.netlify.app/fedora)                                                             | ✔️   | distrowatch                    |
| FFmpeg                                        | [`/ffmpeg`](https://releaselog.netlify.app/ffmpeg)                                                             | ✔️   | git                            |
| FileMaker Platform                            | [`/filemaker`](https://releaselog.netlify.app/filemaker)                                                       | ❌    |                                |
| Firefox                                       | [`/firefox`](https://releaselog.netlify.app/firefox)                                                           | ✔️   | custom                         |
| Fluent Bit                                    | [`/fluent-bit`](https://releaselog.netlify.app/fluent-bit)                                                     | ✔️   | git                            |
| Flux                                          | [`/flux`](https://releaselog.netlify.app/flux)                                                                 | ✔️   | git                            |
| FortiOS                                       | [`/fortios`](https://releaselog.netlify.app/fortios)                                                           | ❌    |                                |
| FreeBSD                                       | [`/freebsd`](https://releaselog.netlify.app/freebsd)                                                           | ❌    |                                |
| Gerrit                                        | [`/gerrit`](https://releaselog.netlify.app/gerrit)                                                             | ✔️   | git                            |
| GitLab                                        | [`/gitlab`](https://releaselog.netlify.app/gitlab)                                                             | ✔️   | git, release_table             |
| Google Kubernetes Engine                      | [`/google-kubernetes-engine`](https://releaselog.netlify.app/google-kubernetes-engine)                         | ✔️   | custom                         |
| Go                                            | [`/go`](https://releaselog.netlify.app/go)                                                                     | ✔️   | git                            |
| GoAccess                                      | [`/goaccess`](https://releaselog.netlify.app/goaccess)                                                         | ✔️   | git                            |
| Godot                                         | [`/godot`](https://releaselog.netlify.app/godot)                                                               | ✔️   | git                            |
| Google Nexus                                  | [`/google-nexus`](https://releaselog.netlify.app/google-nexus)                                                 | ❌    |                                |
| Gorilla Toolkit                               | [`/gorilla`](https://releaselog.netlify.app/gorilla)                                                           | ❌    |                                |
| GraalVM                                       | [`/graalvm`](https://releaselog.netlify.app/graalvm)                                                           | ✔️   | custom                         |
| Gradle                                        | [`/gradle`](https://releaselog.netlify.app/gradle)                                                             | ✔️   | git                            |
| Grafana                                       | [`/grafana`](https://releaselog.netlify.app/grafana)                                                           | ✔️   | git                            |
| Grails Framework                              | [`/grails`](https://releaselog.netlify.app/grails)                                                             | ✔️   | git                            |
| Graylog                                       | [`/graylog`](https://releaselog.netlify.app/graylog)                                                           | ✔️   | git                            |
| GStreamer                                     | [`/gstreamer`](https://releaselog.netlify.app/gstreamer)                                                       | ✔️   | git                            |
| HAProxy                                       | [`/haproxy`](https://releaselog.netlify.app/haproxy)                                                           | ✔️   | custom                         |
| Harbor                                        | [`/harbor`](https://releaselog.netlify.app/harbor)                                                             | ✔️   | git                            |
| Hashicorp Vault                               | [`/hashicorp-vault`](https://releaselog.netlify.app/hashicorp-vault)                                           | ✔️   | git                            |
| Apache HBase                                  | [`/hbase`](https://releaselog.netlify.app/hbase)                                                               | ✔️   | git                            |
| IBM AIX                                       | [`/ibm-aix`](https://releaselog.netlify.app/ibm-aix)                                                           | ✔️   | custom, release_table          |
| IBM iSeries                                   | [`/ibm-i`](https://releaselog.netlify.app/ibm-i)                                                               | ✔️   | release_table                  |
| IBM Semeru Runtime                            | [`/ibm-semeru-runtime`](https://releaselog.netlify.app/ibm-semeru-runtime)                                     | ✔️   | github_releases, release_table |
| Icinga Web                                    | [`/icinga-web`](https://releaselog.netlify.app/icinga-web)                                                     | ✔️   | git                            |
| Icinga                                        | [`/icinga`](https://releaselog.netlify.app/icinga)                                                             | ✔️   | git                            |
| Intel Processors                              | [`/intel-processors`](https://releaselog.netlify.app/intel-processors)                                         | ❌    |                                |
| Internet Explorer                             | [`/internet-explorer`](https://releaselog.netlify.app/internet-explorer)                                       | ❌    |                                |
| Ionic Framework                               | [`/ionic`](https://releaselog.netlify.app/ionic)                                                               | ✔️   | git, release_table             |
| Apple iOS                                     | [`/ios`](https://releaselog.netlify.app/ios)                                                                   | ✔️   | apple                          |
| Apple iPad                                    | [`/ipad`](https://releaselog.netlify.app/ipad)                                                                 | ❌    |                                |
| Apple iPadOS                                  | [`/ipados`](https://releaselog.netlify.app/ipados)                                                             | ✔️   | apple                          |
| Apple iPhone                                  | [`/iphone`](https://releaselog.netlify.app/iphone)                                                             | ❌    |                                |
| ISC DHCP                                      | [`/isc-dhcp`](https://releaselog.netlify.app/isc-dhcp)                                                         | ❌    |                                |
| Istio                                         | [`/istio`](https://releaselog.netlify.app/istio)                                                               | ✔️   | git, release_table             |
| Jekyll                                        | [`/jekyll`](https://releaselog.netlify.app/jekyll)                                                             | ✔️   | git                            |
| Jenkins                                       | [`/jenkins`](https://releaselog.netlify.app/jenkins)                                                           | ✔️   | git                            |
| JHipster                                      | [`/jhipster`](https://releaselog.netlify.app/jhipster)                                                         | ✔️   | npm                            |
| Jira Software                                 | [`/jira-software`](https://releaselog.netlify.app/jira-software)                                               | ✔️   | atlassian_eol, custom          |
| Joomla!                                       | [`/joomla`](https://releaselog.netlify.app/joomla)                                                             | ✔️   | git                            |
| jQuery                                        | [`/jquery`](https://releaselog.netlify.app/jquery)                                                             | ✔️   | git                            |
| JReleaser                                     | [`/jreleaser`](https://releaselog.netlify.app/jreleaser)                                                       | ✔️   | maven                          |
| KDE Plasma                                    | [`/kde-plasma`](https://releaselog.netlify.app/kde-plasma)                                                     | ✔️   | git                            |
| KEDA                                          | [`/keda`](https://releaselog.netlify.app/keda)                                                                 | ✔️   | git                            |
| Keycloak                                      | [`/keycloak`](https://releaselog.netlify.app/keycloak)                                                         | ✔️   | github_releases                |
| Kibana                                        | [`/kibana`](https://releaselog.netlify.app/kibana)                                                             | ✔️   | git                            |
| Amazon Kindle                                 | [`/kindle`](https://releaselog.netlify.app/kindle)                                                             | ❌    |                                |
| Kirby                                         | [`/kirby`](https://releaselog.netlify.app/kirby)                                                               | ✔️   | git                            |
| Kong Gateway                                  | [`/kong-gateway`](https://releaselog.netlify.app/kong-gateway)                                                 | ✔️   | git                            |
| Kotlin                                        | [`/kotlin`](https://releaselog.netlify.app/kotlin)                                                             | ✔️   | npm                            |
| Kubernetes CSI Node Driver Registrar          | [`/kubernetes-csi-node-driver-registrar`](https://releaselog.netlify.app/kubernetes-csi-node-driver-registrar) | ✔️   | git                            |
| Kubernetes                                    | [`/kubernetes`](https://releaselog.netlify.app/kubernetes)                                                     | ✔️   | git                            |
| Kyverno                                       | [`/kyverno`](https://releaselog.netlify.app/kyverno)                                                           | ✔️   | git                            |
| Laravel                                       | [`/laravel`](https://releaselog.netlify.app/laravel)                                                           | ✔️   | git, release_table             |
| LibreOffice                                   | [`/libreoffice`](https://releaselog.netlify.app/libreoffice)                                                   | ✔️   | custom                         |
| LineageOS                                     | [`/lineageos`](https://releaselog.netlify.app/lineageos)                                                       | ❌    |                                |
| Linux Kernel                                  | [`/linux`](https://releaselog.netlify.app/linux)                                                               | ✔️   | cgit                           |
| Linux Mint                                    | [`/linuxmint`](https://releaselog.netlify.app/linuxmint)                                                       | ✔️   | release_table                  |
| Apache Log4j                                  | [`/log4j`](https://releaselog.netlify.app/log4j)                                                               | ✔️   | maven                          |
| Logstash                                      | [`/logstash`](https://releaselog.netlify.app/logstash)                                                         | ✔️   | git                            |
| Looker                                        | [`/looker`](https://releaselog.netlify.app/looker)                                                             | ✔️   | custom                         |
| Lua                                           | [`/lua`](https://releaselog.netlify.app/lua)                                                                   | ❌    |                                |
| Apple macOS                                   | [`/macos`](https://releaselog.netlify.app/macos)                                                               | ✔️   | apple                          |
| Mageia                                        | [`/mageia`](https://releaselog.netlify.app/mageia)                                                             | ✔️   | distrowatch                    |
| Magento                                       | [`/magento`](https://releaselog.netlify.app/magento)                                                           | ✔️   | git                            |
| MariaDB                                       | [`/mariadb`](https://releaselog.netlify.app/mariadb)                                                           | ✔️   | git                            |
| Mastodon                                      | [`/mastodon`](https://releaselog.netlify.app/mastodon)                                                         | ✔️   | git                            |
| Matomo                                        | [`/matomo`](https://releaselog.netlify.app/matomo)                                                             | ✔️   | git                            |
| Mattermost                                    | [`/mattermost`](https://releaselog.netlify.app/mattermost)                                                     | ✔️   | git, release_table             |
| Mautic                                        | [`/mautic`](https://releaselog.netlify.app/mautic)                                                             | ✔️   | git, release_table             |
| MediaWiki                                     | [`/mediawiki`](https://releaselog.netlify.app/mediawiki)                                                       | ✔️   | git, release_table             |
| Meilisearch                                   | [`/meilisearch`](https://releaselog.netlify.app/meilisearch)                                                   | ✔️   | git                            |
| Memcached                                     | [`/memcached`](https://releaselog.netlify.app/memcached)                                                       | ✔️   | git                            |
| Micronaut Framework                           | [`/micronaut`](https://releaselog.netlify.app/micronaut)                                                       | ✔️   | git                            |
| Microsoft Build of OpenJDK                    | [`/microsoft-build-of-openjdk`](https://releaselog.netlify.app/microsoft-build-of-openjdk)                     | ✔️   | git, release_table             |
| MongoDB Server                                | [`/mongodb`](https://releaselog.netlify.app/mongodb)                                                           | ✔️   | git, release_table             |
| Moodle                                        | [`/moodle`](https://releaselog.netlify.app/moodle)                                                             | ✔️   | git, release_table             |
| Motorola Mobility                             | [`/motorola-mobility`](https://releaselog.netlify.app/motorola-mobility)                                       | ❌    |                                |
| Microsoft Exchange                            | [`/msexchange`](https://releaselog.netlify.app/msexchange)                                                     | ❌    |                                |
| Microsoft SharePoint                          | [`/sharepoint`](https://releaselog.netlify.app/sharepoint)                                                     | ❌    |                                |
| Microsoft SQL Server                          | [`/mssqlserver`](https://releaselog.netlify.app/mssqlserver)                                                   | ❌    |                                |
| Mule Runtime                                  | [`/mulesoft-runtime`](https://releaselog.netlify.app/mulesoft-runtime)                                         | ❌    |                                |
| MX Linux                                      | [`/mxlinux`](https://releaselog.netlify.app/mxlinux)                                                           | ✔️   | distrowatch                    |
| MySQL                                         | [`/mysql`](https://releaselog.netlify.app/mysql)                                                               | ✔️   | git                            |
| Neo4j                                         | [`/neo4j`](https://releaselog.netlify.app/neo4j)                                                               | ✔️   | git, release_table             |
| Neos                                          | [`/neos`](https://releaselog.netlify.app/neos)                                                                 | ✔️   | git                            |
| NetBSD                                        | [`/netbsd`](https://releaselog.netlify.app/netbsd)                                                             | ❌    |                                |
| Nextcloud                                     | [`/nextcloud`](https://releaselog.netlify.app/nextcloud)                                                       | ✔️   | git, release_table             |
| Next.js                                       | [`/nextjs`](https://releaselog.netlify.app/nextjs)                                                             | ✔️   | npm                            |
| Nexus Repository                              | [`/nexus`](https://releaselog.netlify.app/nexus)                                                               | ✔️   | git, release_table             |
| nginx                                         | [`/nginx`](https://releaselog.netlify.app/nginx)                                                               | ✔️   | git                            |
| nix                                           | [`/nix`](https://releaselog.netlify.app/nix)                                                                   | ✔️   | git                            |
| NixOS                                         | [`/nixos`](https://releaselog.netlify.app/nixos)                                                               | ❌    |                                |
| Kubernetes Node Feature Discovery             | [`/kubernetes-node-feature-discovery`](https://releaselog.netlify.app/kubernetes-node-feature-discovery)       | ✔️   | git                            |
| Node.js                                       | [`/nodejs`](https://releaselog.netlify.app/nodejs)                                                             | ✔️   | git                            |
| Nokia Mobile                                  | [`/nokia`](https://releaselog.netlify.app/nokia)                                                               | ❌    |                                |
| Nomad                                         | [`/nomad`](https://releaselog.netlify.app/nomad)                                                               | ✔️   | git                            |
| NumPy                                         | [`/numpy`](https://releaselog.netlify.app/numpy)                                                               | ✔️   | pypi                           |
| Nutanix AOS                                   | [`/nutanix-aos`](https://releaselog.netlify.app/nutanix-aos)                                                   | ✔️   | nutanix                        |
| Nutanix Files                                 | [`/nutanix-files`](https://releaselog.netlify.app/nutanix-files)                                               | ✔️   | nutanix                        |
| Nutanix Prism Central                         | [`/nutanix-prism`](https://releaselog.netlify.app/nutanix-prism)                                               | ✔️   | nutanix                        |
| Nuxt                                          | [`/nuxt`](https://releaselog.netlify.app/nuxt)                                                                 | ✔️   | npm, release_table             |
| NVIDIA Driver                                 | [`/nvidia`](https://releaselog.netlify.app/nvidia)                                                             | ❌    |                                |
| NVIDIA GPUs                                   | [`/nvidia-gpu`](https://releaselog.netlify.app/nvidia-gpu)                                                     | ❌    |                                |
| Microsoft Office                              | [`/office`](https://releaselog.netlify.app/office)                                                             | ❌    |                                |
| OnePlus                                       | [`/oneplus`](https://releaselog.netlify.app/oneplus)                                                           | ❌    |                                |
| OpenBSD                                       | [`/openbsd`](https://releaselog.netlify.app/openbsd)                                                           | ❌    |                                |
| OpenJDK builds from Oracle                    | [`/openjdk-builds-from-oracle`](https://releaselog.netlify.app/openjdk-builds-from-oracle)                     | ❌    |                                |
| OpenSearch                                    | [`/opensearch`](https://releaselog.netlify.app/opensearch)                                                     | ✔️   | git, release_table             |
| OpenSSL                                       | [`/openssl`](https://releaselog.netlify.app/openssl)                                                           | ✔️   | git                            |
| openSUSE                                      | [`/opensuse`](https://releaselog.netlify.app/opensuse)                                                         | ❌    |                                |
| OpenTofu                                      | [`/opentofu`](https://releaselog.netlify.app/opentofu)                                                         | ✔️   | git                            |
| OpenVPN                                       | [`/openvpn`](https://releaselog.netlify.app/openvpn)                                                           | ✔️   | git                            |
| OpenWrt                                       | [`/openwrt`](https://releaselog.netlify.app/openwrt)                                                           | ✔️   | git                            |
| OpenZFS                                       | [`/openzfs`](https://releaselog.netlify.app/openzfs)                                                           | ✔️   | git                            |
| OPNsense                                      | [`/opnsense`](https://releaselog.netlify.app/opnsense)                                                         | ✔️   | git                            |
| Oracle APEX                                   | [`/oracle-apex`](https://releaselog.netlify.app/oracle-apex)                                                   | ✔️   | release_table                  |
| Oracle Database                               | [`/oracle-database`](https://releaselog.netlify.app/oracle-database)                                           | ✔️   | release_table                  |
| Oracle JDK                                    | [`/oracle-jdk`](https://releaselog.netlify.app/oracle-jdk)                                                     | ✔️   | custom, release_table          |
| Oracle Linux                                  | [`/oracle-linux`](https://releaselog.netlify.app/oracle-linux)                                                 | ✔️   | distrowatch                    |
| Oracle Solaris                                | [`/oracle-solaris`](https://releaselog.netlify.app/oracle-solaris)                                             | ❌    |                                |
| oVirt                                         | [`/ovirt`](https://releaselog.netlify.app/ovirt)                                                               | ✔️   | git                            |
| Palo Alto Networks Cortex XDR agent           | [`/cortex-xdr`](https://releaselog.netlify.app/cortex-xdr)                                                     | ✔️   | release_table                  |
| Palo Alto Networks GlobalProtect App          | [`/pangp`](https://releaselog.netlify.app/pangp)                                                               | ✔️   | release_table                  |
| Palo Alto Networks PAN-OS                     | [`/panos`](https://releaselog.netlify.app/panos)                                                               | ✔️   | release_table                  |
| PCI-DSS                                       | [`/pci-dss`](https://releaselog.netlify.app/pci-dss)                                                           | ❌    |                                |
| Perl                                          | [`/perl`](https://releaselog.netlify.app/perl)                                                                 | ✔️   | git                            |
| PHP                                           | [`/php`](https://releaselog.netlify.app/php)                                                                   | ✔️   | custom                         |
| phpBB                                         | [`/phpbb`](https://releaselog.netlify.app/phpbb)                                                               | ✔️   | git                            |
| phpMyAdmin                                    | [`/phpmyadmin`](https://releaselog.netlify.app/phpmyadmin)                                                     | ✔️   | git                            |
| Google Pixel                                  | [`/pixel`](https://releaselog.netlify.app/pixel)                                                               | ❌    |                                |
| Plesk                                         | [`/plesk`](https://releaselog.netlify.app/plesk)                                                               | ✔️   | custom                         |
| pnpm                                          | [`/pnpm`](https://releaselog.netlify.app/pnpm)                                                                 | ✔️   | npm                            |
| Pop!_OS                                       | [`/pop-os`](https://releaselog.netlify.app/pop-os)                                                             | ❌    |                                |
| Postfix                                       | [`/postfix`](https://releaselog.netlify.app/postfix)                                                           | ✔️   | git                            |
| PostgreSQL                                    | [`/postgresql`](https://releaselog.netlify.app/postgresql)                                                     | ✔️   | git, release_table             |
| postmarketOS                                  | [`/postmarketos`](https://releaselog.netlify.app/postmarketos)                                                 | ✔️   | distrowatch                    |
| Microsoft PowerShell                          | [`/powershell`](https://releaselog.netlify.app/powershell)                                                     | ✔️   | git, release_table             |
| PrivateBin                                    | [`/privatebin`](https://releaselog.netlify.app/privatebin)                                                     | ✔️   | git                            |
| Prometheus                                    | [`/prometheus`](https://releaselog.netlify.app/prometheus)                                                     | ✔️   | git, release_table             |
| Protractor                                    | [`/protractor`](https://releaselog.netlify.app/protractor)                                                     | ✔️   | npm                            |
| Proxmox VE                                    | [`/proxmox-ve`](https://releaselog.netlify.app/proxmox-ve)                                                     | ✔️   | distrowatch, release_table     |
| Puppet                                        | [`/puppet`](https://releaselog.netlify.app/puppet)                                                             | ✔️   | git                            |
| Python                                        | [`/python`](https://releaselog.netlify.app/python)                                                             | ✔️   | git, release_table             |
| Qt                                            | [`/qt`](https://releaselog.netlify.app/qt)                                                                     | ✔️   | git                            |
| Quarkus                                       | [`/quarkus-framework`](https://releaselog.netlify.app/quarkus-framework)                                       | ✔️   | github_releases                |
| Quasar                                        | [`/quasar`](https://releaselog.netlify.app/quasar)                                                             | ✔️   | npm, release_table             |
| RabbitMQ                                      | [`/rabbitmq`](https://releaselog.netlify.app/rabbitmq)                                                         | ✔️   | git                            |
| Rancher                                       | [`/rancher`](https://releaselog.netlify.app/rancher)                                                           | ✔️   | git                            |
| Raspberry Pi                                  | [`/raspberry-pi`](https://releaselog.netlify.app/raspberry-pi)                                                 | ❌    |                                |
| React Native                                  | [`/react-native`](https://releaselog.netlify.app/react-native)                                                 | ✔️   | npm                            |
| React                                         | [`/react`](https://releaselog.netlify.app/react)                                                               | ✔️   | npm                            |
| Netgear ReadyNAS                              | [`/readynas`](https://releaselog.netlify.app/readynas)                                                         | ❌    |                                |
| Red Hat build of OpenJDK                      | [`/redhat-build-of-openjdk`](https://releaselog.netlify.app/redhat-build-of-openjdk)                           | ❌    |                                |
| Red Hat JBoss Enterprise Application Platform | [`/redhat-jboss-eap`](https://releaselog.netlify.app/redhat-jboss-eap)                                         | ❌    |                                |
| Red Hat OpenShift                             | [`/red-hat-openshift`](https://releaselog.netlify.app/red-hat-openshift)                                       | ✔️   | custom                         |
| Red Hat Satellite                             | [`/redhat-satellite`](https://releaselog.netlify.app/redhat-satellite)                                         | ✔️   | custom                         |
| Redis                                         | [`/redis`](https://releaselog.netlify.app/redis)                                                               | ✔️   | git                            |
| Redmine                                       | [`/redmine`](https://releaselog.netlify.app/redmine)                                                           | ✔️   | git                            |
| Red Hat Enterprise Linux                      | [`/rhel`](https://releaselog.netlify.app/rhel)                                                                 | ❌    |                                |
| Robo                                          | [`/robo`](https://releaselog.netlify.app/robo)                                                                 | ✔️   | git, release_table             |
| Rocket.Chat                                   | [`/rocket-chat`](https://releaselog.netlify.app/rocket-chat)                                                   | ✔️   | git, release_table             |
| Rocky Linux                                   | [`/rocky-linux`](https://releaselog.netlify.app/rocky-linux)                                                   | ✔️   | custom, release_table          |
| ROS 2                                         | [`/ros-2`](https://releaselog.netlify.app/ros-2)                                                               | ❌    |                                |
| ROS                                           | [`/ros`](https://releaselog.netlify.app/ros)                                                                   | ❌    |                                |
| Roundcube Webmail                             | [`/roundcube`](https://releaselog.netlify.app/roundcube)                                                       | ✔️   | git                            |
| Ruby on Rails                                 | [`/rails`](https://releaselog.netlify.app/rails)                                                               | ✔️   | git                            |
| Ruby                                          | [`/ruby`](https://releaselog.netlify.app/ruby)                                                                 | ✔️   | git                            |
| Rust                                          | [`/rust`](https://releaselog.netlify.app/rust)                                                                 | ✔️   | git                            |
| Salt                                          | [`/salt`](https://releaselog.netlify.app/salt)                                                                 | ✔️   | git                            |
| Samsung Mobile                                | [`/samsung-mobile`](https://releaselog.netlify.app/samsung-mobile)                                             | ❌    |                                |
| SapMachine                                    | [`/sapmachine`](https://releaselog.netlify.app/sapmachine)                                                     | ✔️   | github_releases                |
| Scala                                         | [`/scala`](https://releaselog.netlify.app/scala)                                                               | ✔️   | git                            |
| Shopware                                      | [`/shopware`](https://releaselog.netlify.app/shopware)                                                         | ✔️   | git                            |
| Silverstripe CMS                              | [`/silverstripe`](https://releaselog.netlify.app/silverstripe)                                                 | ✔️   | git, release_table             |
| Slackware Linux                               | [`/slackware`](https://releaselog.netlify.app/slackware)                                                       | ✔️   | distrowatch                    |
| SUSE Linux Enterprise Server                  | [`/sles`](https://releaselog.netlify.app/sles)                                                                 | ❌    |                                |
| Apache Solr                                   | [`/solr`](https://releaselog.netlify.app/solr)                                                                 | ✔️   | git                            |
| SonarQube                                     | [`/sonar`](https://releaselog.netlify.app/sonar)                                                               | ✔️   | git                            |
| Sourcegraph                                   | [`/sourcegraph`](https://releaselog.netlify.app/sourcegraph)                                                   | ✔️   | git                            |
| Splunk                                        | [`/splunk`](https://releaselog.netlify.app/splunk)                                                             | ✔️   | custom                         |
| Spring Boot                                   | [`/spring-boot`](https://releaselog.netlify.app/spring-boot)                                                   | ✔️   | git, release_table             |
| Spring Framework                              | [`/spring-framework`](https://releaselog.netlify.app/spring-framework)                                         | ✔️   | git, release_table             |
| SQLite                                        | [`/sqlite`](https://releaselog.netlify.app/sqlite)                                                             | ✔️   | git                            |
| Squid                                         | [`/squid`](https://releaselog.netlify.app/squid)                                                               | ✔️   | git                            |
| SteamOS                                       | [`/steamos`](https://releaselog.netlify.app/steamos)                                                           | ❌    |                                |
| Microsoft Surface                             | [`/surface`](https://releaselog.netlify.app/surface)                                                           | ❌    |                                |
| Symfony                                       | [`/symfony`](https://releaselog.netlify.app/symfony)                                                           | ✔️   | git                            |
| Tails                                         | [`/tails`](https://releaselog.netlify.app/tails)                                                               | ✔️   | distrowatch                    |
| Tarantool                                     | [`/tarantool`](https://releaselog.netlify.app/tarantool)                                                       | ✔️   | git                            |
| Telegraf                                      | [`/telegraf`](https://releaselog.netlify.app/telegraf)                                                         | ✔️   | git                            |
| Hashicorp Terraform                           | [`/terraform`](https://releaselog.netlify.app/terraform)                                                       | ✔️   | git                            |
| Apache Tomcat                                 | [`/tomcat`](https://releaselog.netlify.app/tomcat)                                                             | ✔️   | maven                          |
| Traefik                                       | [`/traefik`](https://releaselog.netlify.app/traefik)                                                           | ✔️   | git, release_table             |
| Twig                                          | [`/twig`](https://releaselog.netlify.app/twig)                                                                 | ✔️   | git                            |
| TYPO3                                         | [`/typo3`](https://releaselog.netlify.app/typo3)                                                               | ✔️   | custom                         |
| Ubuntu                                        | [`/ubuntu`](https://releaselog.netlify.app/ubuntu)                                                             | ✔️   | distrowatch                    |
| Umbraco CMS                                   | [`/umbraco`](https://releaselog.netlify.app/umbraco)                                                           | ✔️   | git, release_table             |
| Unity                                         | [`/unity`](https://releaselog.netlify.app/unity)                                                               | ❌    |                                |
| UnrealIRCd                                    | [`/unrealircd`](https://releaselog.netlify.app/unrealircd)                                                     | ✔️   | custom, release_table          |
| Varnish                                       | [`/varnish`](https://releaselog.netlify.app/varnish)                                                           | ✔️   | git, release_table             |
| Veeam Backup & Replication                    | [`/veeam-backup-and-replication`](https://releaselog.netlify.app/veeam-backup-and-replication)                 | ✔️   | custom                         |
| Apple visionOS                                | [`/visionos`](https://releaselog.netlify.app/visionos)                                                         | ✔️   | apple                          |
| Visual COBOL                                  | [`/visual-cobol`](https://releaselog.netlify.app/visual-cobol)                                                 | ❌    |                                |
| Microsoft Visual Studio                       | [`/visual-studio`](https://releaselog.netlify.app/visual-studio)                                               | ✔️   | custom                         |
| VMware Cloud Foundation                       | [`/vmware-cloud-foundation`](https://releaselog.netlify.app/vmware-cloud-foundation)                           | ❌    |                                |
| VMware ESXi                                   | [`/esxi`](https://releaselog.netlify.app/esxi)                                                                 | ❌    |                                |
| VMware Harbor Registry                        | [`/vmware-harbor-registry`](https://releaselog.netlify.app/vmware-harbor-registry)                             | ❌    |                                |
| VMware Horizon                                | [`/horizon`](https://releaselog.netlify.app/horizon)                                                           | ❌    |                                |
| VMware Photon                                 | [`/photon`](https://releaselog.netlify.app/photon)                                                             | ❌    |                                |
| VMware Site Recovery Manager                  | [`/vmware-srm`](https://releaselog.netlify.app/vmware-srm)                                                     | ❌    |                                |
| VMware vCenter Server                         | [`/vcenter`](https://releaselog.netlify.app/vcenter)                                                           | ❌    |                                |
| Vue                                           | [`/vue`](https://releaselog.netlify.app/vue)                                                                   | ✔️   | npm                            |
| Vuetify                                       | [`/vuetify`](https://releaselog.netlify.app/vuetify)                                                           | ✔️   | npm, release_table             |
| Wagtail                                       | [`/wagtail`](https://releaselog.netlify.app/wagtail)                                                           | ✔️   | pypi, release_table            |
| Apple watchOS                                 | [`/watchos`](https://releaselog.netlify.app/watchos)                                                           | ✔️   | apple                          |
| WeeChat                                       | [`/weechat`](https://releaselog.netlify.app/weechat)                                                           | ✔️   | git                            |
| Microsoft Windows Embedded                    | [`/windows-embedded`](https://releaselog.netlify.app/windows-embedded)                                         | ❌    |                                |
| Microsoft Nano Server                         | [`/windows-nano-server`](https://releaselog.netlify.app/windows-nano-server)                                   | ❌    |                                |
| Microsoft Windows Server Core                 | [`/windows-server-core`](https://releaselog.netlify.app/windows-server-core)                                   | ❌    |                                |
| Microsoft Windows Server                      | [`/windows-server`](https://releaselog.netlify.app/windows-server)                                             | ❌    |                                |
| Microsoft Windows                             | [`/windows`](https://releaselog.netlify.app/windows)                                                           | ❌    |                                |
| Wireshark                                     | [`/wireshark`](https://releaselog.netlify.app/wireshark)                                                       | ✔️   | git                            |
| WordPress                                     | [`/wordpress`](https://releaselog.netlify.app/wordpress)                                                       | ✔️   | git                            |
| XCP-ng                                        | [`/xcp-ng`](https://releaselog.netlify.app/xcp-ng)                                                             | ✔️   | git, release_table             |
| Yarn                                          | [`/yarn`](https://releaselog.netlify.app/yarn)                                                                 | ✔️   | npm                            |
| Yocto Project                                 | [`/yocto`](https://releaselog.netlify.app/yocto)                                                               | ✔️   | git                            |
| Zabbix                                        | [`/zabbix`](https://releaselog.netlify.app/zabbix)                                                             | ✔️   | git, release_table             |
| Zentyal                                       | [`/zentyal`](https://releaselog.netlify.app/zentyal)                                                           | ✔️   | release_table                  |
| Zerto                                         | [`/zerto`](https://releaselog.netlify.app/zerto)                                                               | ❌    |                                |
| Apache ZooKeeper                              | [`/zookeeper`](https://releaselog.netlify.app/zookeeper)                                                       | ✔️   | maven                          |

This table has been generated by [report.py](/report.py).
