num_entities = 2000

entity = """
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: my-db-{num}
  tags:
    - gcp
    - cloud-sql
  annotations:
    backstage.io/techdocs-ref: dir:.
    github.com/project-slug: spotify-portal-public-demo/entity-search-test-template
spec:
  type: database
  lifecycle: experimental
  owner: group:default/github
"""

entities = []
for num in range(num_entities):
    entities.append(entity.format(num=num))

print("---".join(entities))
