import re

def get_arn_info():
    try:
        arn = input("Digite o ARN que deseja analisar: ")

        arn_parts = arn.split(":")
        arn_type = arn_parts[2]
        resource_parts = arn_parts[-1].split("/")
        resource_type = resource_parts[0]
        resource_name = resource_parts[-1]

        print("Tipo do ARN:", arn_type)
        print("Permissões:")

        permissions = []

        if arn_type == "iam":
            print("- Identificado como um ARN de usuário IAM")
            if resource_name != "*":
                print("Nome do usuário:", resource_name)
            else:
                print("Permissão para todos os usuários")
            permissions = ["iam:GetUser", "iam:CreateUser", "iam:ListAccessKeys"]
        else:
            arn_regex = r'^arn:aws:([a-zA-Z0-9-]+):([a-zA-Z0-9-]+):([a-zA-Z0-9-_]+):(.+)$'
            arn_match = re.match(arn_regex, arn)

            if arn_match:
                arn_fields = arn_match.groups()
                service = arn_fields[0]
                region = arn_fields[1]
                account_id = arn_fields[2]
                resource_type = arn_fields[3].split(':')

                resource = resource_type[0]
                resource_name = None

                if len(resource_type) > 1:
                    resource_name = ':'.join(resource_type[1:])

                print("Tipo do ARN:", arn_type)
                print("Serviço:", service)
                print("Região:", region)
                print("ID da Conta:", account_id)
                print("Recurso:", resource)
                if resource_name:
                    print("Nome do Recurso:", resource_name)

                # Adicione mais tipos de ARN e suas respectivas permissões conforme necessário
                if resource == "s3":
                    print("Permissões do Bucket S3:")
                    permissions = ["s3:GetObject", "s3:PutObject", "s3:ListBucket"]
                elif resource == "lambda":
                    print("Permissões do Lambda:")
                    permissions = ["lambda:InvokeFunction", "lambda:CreateFunction", "lambda:ListFunctions"]
                elif resource == "waf":
                    print("Permissões do WAF:")
                    permissions = ["waf:GetWebACL", "waf:CreateWebACL", "waf:ListWebACLs"]
                elif resource == "firehose":
                    print("Permissões do Firehose:")
                    permissions = ["firehose:PutRecord", "firehose:CreateDeliveryStream", "firehose:ListDeliveryStreams"]

        if permissions:
            print("Permissões:")
            for permission in permissions:
                print("-", permission)

    except Exception as e:
        print("Ocorreu um erro ao processar o ARN:", str(e))

get_arn_info()
