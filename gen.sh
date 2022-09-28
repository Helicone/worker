python3 -m sgqlc.introspection \
    http://localhost:3000/api/worker/graphql \
    worker.json

sgqlc-codegen schema worker.json worker.py