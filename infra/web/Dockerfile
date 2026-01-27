FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Basic tools
RUN apt-get update \
 && apt-get install -y \
    git \
    curl \
    sudo \
    locales \
 && rm -rf /var/lib/apt/lists/*

# Create non root user "coder"
RUN useradd -ms /bin/bash coder \
 && echo "coder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER coder

RUN mkdir -p "/home/coder"
RUN cat <<EOF > index.html
<!DOCTYPE html>
<html>
<body>

  <h1>Hello World</h1>

</body>
</html>
EOF

WORKDIR /home/coder

