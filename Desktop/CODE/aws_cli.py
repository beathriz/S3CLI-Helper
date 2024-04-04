# Listar Buckets
aws s3 ls

# Criar um Novo Bucket
aws s3 mb s3://nome-do-bucket

# Remover um Bucket (vazio)
aws s3 rb s3://nome-do-bucket

# Copiar um Arquivo Local para o Bucket S3
aws s3 cp arquivo.txt s3://nome-do-bucket/caminho/

# Copiar um Arquivo do Bucket S3 para o Local
aws s3 cp s3://nome-do-bucket/caminho/arquivo.txt arquivo.txt

# Sincronizar um Diretório Local com um Bucket S3
aws s3 sync diretorio/ s3://nome-do-bucket/caminho/

# Remover um Arquivo do Bucket S3
aws s3 rm s3://nome-do-bucket/caminho/arquivo.txt

# Remover um Diretório do Bucket S3 (recursivamente)
aws s3 rm s3://nome-do-bucket/caminho --recursive

# Listar os Objetos em um Bucket S3
aws s3 ls s3://nome-do-bucket

# Listar os Objetos em um Bucket S3 Recursivamente
aws s3 ls s3://nome-do-bucket --recursive

# Obter informações sobre um Objeto S3
aws s3api head-object --bucket nome-do-bucket --key caminho/arquivo.txt

# Obter uma URL de Pré-Assinatura para um Objeto S3
aws s3 presign s3://nome-do-bucket/caminho/arquivo.txt

# Copiar um objeto do S3 para outro bucket
aws s3 cp s3://bucket-fonte/caminho/arquivo.txt s3://bucket-destino/caminho/

# Copiar um objeto do S3 para outro bucket em outra região
aws s3 cp s3://bucket-fonte/caminho/arquivo.txt s3://bucket-destino/caminho/ --region regiao-destino

# Listar os Buckets em uma região específica
aws s3api list-buckets --query "Buckets[].Name" --region regiao

# Listar as versões de um objeto S3
aws s3api list-object-versions --bucket nome-do-bucket --prefix caminho/arquivo.txt
