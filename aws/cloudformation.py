# ==================================================
# This stack creates the API infrastructure.
# ==================================================
from troposphere import Template, Parameter, Ref, GetAtt, Join, Output
from troposphere.s3 import Bucket, PublicRead, WebsiteConfiguration, RedirectAllRequestsTo
import troposphere.iam as iam
import troposphere.cloudfront as cloudfront
import uuid

# ==================================================
# Template details.
# ==================================================
template = Template(
    'Create the infrastructure needed to run the One Hounslow Connect Backend')
template.add_version('2010-09-09')

# ==================================================
# Parameters.
# ==================================================
uuid_parameter = template.add_parameter(
    Parameter(
        'Uuid',
        Type='String',
        Default=str(uuid.uuid4()),
        Description='The unique ID for this stack.',
        MinLength='36',
        MaxLength='36'
    )
)

environment_parameter = template.add_parameter(
    Parameter(
        'Environment',
        Type='String',
        Description='The environment this stack is for (e.g. production or staging).',
        MinLength='1'
    )
)

cname_parameter = template.add_parameter(
    Parameter(
        'Cname',
        Type='String',
        Description='The CNAME for the site.',
        MinLength='1',
        AllowedPattern='^(?!:\/\/)([a-zA-Z0-9-_]+\.)*[a-zA-Z0-9][a-zA-Z0-9-_]+\.[a-zA-Z]{2,11}?$',
        ConstraintDescription='Must be a valid domain'
    )
)

cname_301_parameter = template.add_parameter(
    Parameter(
        'Cname301',
        Type='String',
        Description='The CNAME that should be 301 redirected to the site CNAME.',
        MinLength='1',
        AllowedPattern='^(?!:\/\/)([a-zA-Z0-9-_]+\.)*[a-zA-Z0-9][a-zA-Z0-9-_]+\.[a-zA-Z]{2,11}?$',
        ConstraintDescription='Must be a valid domain'
    )
)

certificate_arn_parameter = template.add_parameter(
    Parameter(
        'CertificateArn',
        Type='String',
        Description='The ARN for the CloudFront distribution SSL certificate (must be in us-east-1).'
    )
)

certificate_301_arn_parameter = template.add_parameter(
    Parameter(
        'Certificate301Arn',
        Type='String',
        Description='The ARN for the CloudFront distribution SSL certificate covering the domain to be 301 redirected (must be in us-east-1).'
    )
)

# ==================================================
# Variables.
# ==================================================
bucket_name_variable = Join(
    '-', ['backend', Ref(environment_parameter), Ref(uuid_parameter)])
ci_user_name_variable = Join('-', ['ci-backend', Ref(environment_parameter)])

# ==================================================
# Resources.
# ==================================================
bucket_resource = template.add_resource(
    Bucket(
        'Bucket',
        BucketName=bucket_name_variable,
        AccessControl=PublicRead
    )
)

bucket_301_resource = template.add_resource(
    Bucket(
        'Bucket301',
        BucketName=Ref(cname_301_parameter),
        AccessControl=PublicRead,
        WebsiteConfiguration=WebsiteConfiguration(
            RedirectAllRequestsTo=RedirectAllRequestsTo(
            HostName=Ref(cname_parameter),
            )
        )
    )
)

distribution_resource = template.add_resource(
    cloudfront.Distribution(
        'Distribution',
        DistributionConfig=cloudfront.DistributionConfig(
            Aliases=[
                Ref(cname_parameter)
            ],
            CacheBehaviors=[
                cloudfront.CacheBehavior(
                    AllowedMethods=['HEAD', 'GET'],
                    CachedMethods=['HEAD', 'GET'],
                    ForwardedValues=cloudfront.ForwardedValues(
                        QueryString=False
                    ),
                    PathPattern='*',
                    TargetOriginId=Join('-', ['S3', Ref(bucket_resource)]),
                    ViewerProtocolPolicy='redirect-to-https'
                )
            ],
            CustomErrorResponses=[
                cloudfront.CustomErrorResponse(
                    ErrorCode=404,
                    ResponseCode=200,
                    ResponsePagePath='/index.html'
                )
            ],
            DefaultCacheBehavior=cloudfront.DefaultCacheBehavior(
                ForwardedValues=cloudfront.ForwardedValues(
                    QueryString=False
                ),
                TargetOriginId=Join('-', ['S3', Ref(bucket_resource)]),
                ViewerProtocolPolicy='redirect-to-https'
            ),
            DefaultRootObject='index.html',
            Enabled=True,
            IPV6Enabled=True,
            Origins=[
                cloudfront.Origin(
                    DomainName=GetAtt(bucket_resource, 'DomainName'),
                    Id=Join('-', ['S3', Ref(bucket_resource)]),
                    S3OriginConfig=cloudfront.S3Origin()
                )
            ],
            ViewerCertificate=cloudfront.ViewerCertificate(
                AcmCertificateArn=Ref(certificate_arn_parameter),
                SslSupportMethod='sni-only'
            )
        )
    )
)

distribution_301_resource = template.add_resource(
    cloudfront.Distribution(
        'Distribution301',
        DistributionConfig=cloudfront.DistributionConfig(
            Aliases=[
                Ref(cname_301_parameter)
            ],
            DefaultCacheBehavior=cloudfront.DefaultCacheBehavior(
                ForwardedValues=cloudfront.ForwardedValues(
                    QueryString=False
                ),
                TargetOriginId=Join('-', ['S3', Ref(bucket_301_resource)]),
                ViewerProtocolPolicy='redirect-to-https'
            ),
            Enabled=True,
            IPV6Enabled=True,
            Origins=[
                cloudfront.Origin(
                    DomainName=Join('.', [Ref(cname_301_parameter), 's3-website', Ref('AWS::Region'),'amazonaws.com']),
                    Id=Join('-', ['S3', Ref(bucket_301_resource)]),
                    CustomOriginConfig=cloudfront.CustomOrigin(
                        OriginProtocolPolicy='http-only'
                    )
                )
            ],
            ViewerCertificate=cloudfront.ViewerCertificate(
                AcmCertificateArn=Ref(certificate_301_arn_parameter),
                SslSupportMethod='sni-only',
                MinimumProtocolVersion='TLSv1.2_2019'
            )
        )
    )
)

ci_user_resource = template.add_resource(
    iam.User(
        'CiUser',
        UserName=ci_user_name_variable,
        Policies=[
            iam.Policy(
                PolicyName='CiUserPolicy',
                PolicyDocument={
                    'Version': '2012-10-17',
                    'Statement': [
                        {
                            'Action': 's3:*',
                            'Effect': 'Allow',
                            'Resource': '*'
                        },
                        {
                            'Action': 'secretsmanager:GetSecretValue',
                            'Effect': 'Allow',
                            'Resource': '*'
                        },
                        {
                            'Action': 'cloudfront:CreateInvalidation',
                            'Effect': 'Allow',
                            'Resource': '*'
                        }
                    ]
                }
            )
        ]
    )
)

# ==================================================
# Outputs.
# ==================================================
template.add_output(
    Output(
        'BucketName',
        Description='The S3 bucket name',
        Value=bucket_name_variable
    )
)

template.add_output(
    Output(
        'CloudFrontId',
        Description='The ID of the CloudFront distribution',
        Value=Ref(distribution_resource)
    )
)

template.add_output(
    Output(
        'CloudFrontDomain',
        Description='The domain name of the CloudFront distribution',
        Value=GetAtt(distribution_resource, 'DomainName')
    )
)

# ==================================================
# Print the generated template in JSON.
# ==================================================
print(template.to_json())
