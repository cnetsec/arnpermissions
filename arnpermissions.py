import re

def get_arn_permissions():
    try:
        arn = input("Digite o ARN que deseja analisar: ")
        arn_parts = arn.split(":")
        arn_type = arn_parts[2]
        resource_parts = arn_parts[-1].split("/")
        resource_type = resource_parts[0]
        resource_name = resource_parts[-1]

        print("Tipo do ARN:", arn_type)

        if arn_type == "iam":
            print("- Identificado como um ARN de usuário IAM")
            if resource_name != "*":
                print("Nome do usuário:", resource_name)
            else:
                print("Permissão para todos os usuários")
            permissions = ["iam:GetUser", "iam:CreateUser", "iam:ListAccessKeys"]
        elif arn_type == "s3":
            print("- Identificado como um ARN de bucket do Amazon S3")
            if resource_type != "" and resource_name != "":
                print("ARN do bucket Amazon S3:", arn)
                print("Permissões do bucket Amazon S3:")
                permissions = ["s3:GetObject", "s3:PutObject", "s3:ListBucket"]
            else:
                print("ARN inválido para análise de bucket do Amazon S3")
                return
        else:
            print("ARN não suportado:", arn)
            return

        if permissions:
            print("Permissões:")
            for permission in permissions:
                print("-", permission)

    except Exception as e:
        print("Ocorreu um erro ao processar o ARN:", str(e))

get_arn_permissions()
