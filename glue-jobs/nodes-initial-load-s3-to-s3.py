import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrameCollection
from awsglue.dynamicframe import DynamicFrame
import re

# Script generated for node device_id_vertex_transform
def add_label_to_device_id(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "DeviceID")
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, "df_deduplicated")
    return DynamicFrameCollection(
        {"device_id_vertex_transform": df_deduplicated}, glueContext
    )


# Script generated for node user_agent_vertex_transform
def add_label_to_user_agent(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "UserAgent")
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, "df_deduplicated")
    return DynamicFrameCollection(
        {"user_agent_vertex_transform": df_deduplicated}, glueContext
    )


# Script generated for node product_vertex_transform
def add_label_to_product(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "Product")
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, "df_deduplicated")
    return DynamicFrameCollection(
        {"produc_vertex_transform": df_deduplicated}, glueContext
    )


# Script generated for node external_id_vertex_transform
def add_label_to_external_id(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "CustomerID")
    return DynamicFrameCollection(
        {"external_id_vertex_transform": df_withlabel}, glueContext
    )


# Script generated for node client_ip_vertex_transform
def add_label_to_client_ip(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "ClientIP")
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, "df_deduplicated")
    return DynamicFrameCollection(
        {"client_ip_vertex_transform": df_deduplicated}, glueContext
    )


# Script generated for node phone_number_vertex_transform
def add_label_to_phone_number(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "PhoneNumber")
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, "df_deduplicated")
    return DynamicFrameCollection(
        {"phone_number_vertex_transform": df_deduplicated}, glueContext
    )


# Script generated for node loyalty_vertex_transform
def add_label_to_loyalty(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "LoyaltyLevel")
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, "df_deduplicated")
    return DynamicFrameCollection(
        {"loyalty_vertex_transform": df_deduplicated}, glueContext
    )


# Script generated for node city_vertex_transform
def add_label_to_city(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "City")
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, "df_deduplicated")
    return DynamicFrameCollection(
        {"city_vertex_transform": df_deduplicated}, glueContext
    )


# Script generated for node email_vertex_transform
def add_label_to_email(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "Email")
    return DynamicFrameCollection({"email_vertex_transform": df_withlabel}, glueContext)


# Script generated for node username_vertex_transform
def add_label_to_username(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "User")
    return DynamicFrameCollection(
        {"username_vertex_transform": df_withlabel}, glueContext
    )


# Script generated for node postcode_vertex_transform
def add_label_to_postcode(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "PostCode")
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, "df_deduplicated")
    return DynamicFrameCollection(
        {"postcode_vertex_transform": df_deduplicated}, glueContext
    )


# Script generated for node domain_name_vertex_transform
def add_label_to_domain_name(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "DomainName")
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, "df_deduplicated")
    return DynamicFrameCollection(
        {"domain_name_vertex_transform": df_deduplicated}, glueContext
    )


# Script generated for node country_vertex_transform
def add_label_to_country(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "Country")
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, "df_deduplicated")
    return DynamicFrameCollection(
        {"country_vertex_transform": df_deduplicated}, glueContext
    )


# Script generated for node product_category_vertex_transform
def add_label_to_product_category(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "ProductCategory")
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, "df_deduplicated")
    return DynamicFrameCollection(
        {"product_category_vertex_transform": df_deduplicated}, glueContext
    )


# Script generated for node cookie_vertex_transform
def add_label_to_cookie(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "Cookie")
    return DynamicFrameCollection(
        {"cookie_vertex_transform": df_withlabel}, glueContext
    )


# Script generated for node session_vertex_transform
def add_label_to_session(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, "SessionID")
    return DynamicFrameCollection(
        {"session_vertex_transform": df_withlabel}, glueContext
    )


args = getResolvedOptions(sys.argv, ["JOB_NAME", "DATABASE_NAME", "TABLE_PREFIX", "S3_TARGET_PATH"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
s3_target_path = args["S3_TARGET_PATH"]
job.init(args["JOB_NAME"], args)

# Script generated for node cookie_source_dataset
cookie_source_dataset_node1654982654728 = glueContext.create_dynamic_frame.from_catalog(
    database=args["DATABASE_NAME"],
    table_name="{}cookie".format(args["TABLE_PREFIX"]),
    transformation_ctx="cookie_source_dataset_node1654982654728",
)

# Script generated for node first_party_source_dataset
first_party_source_dataset_node1 = glueContext.create_dynamic_frame.from_catalog(
    database=args['DATABASE_NAME'],
    table_name="{}first_party".format(args["TABLE_PREFIX"]),
    transformation_ctx="first_party_source_dataset_node1",
)

# Script generated for node clickstream_source_dataset
clickstream_source_dataset_node1654982749940 = (
    glueContext.create_dynamic_frame.from_catalog(
        database=args["DATABASE_NAME"],
        table_name="{}clickstream".format(args["TABLE_PREFIX"]),
        transformation_ctx="clickstream_source_dataset_node1654982749940",
    )
)

# Script generated for node transactional_source_dataset
transactional_source_dataset_node1654975865526 = (
    glueContext.create_dynamic_frame.from_catalog(
        database=args["DATABASE_NAME"],
        table_name="{}transactional".format(args["TABLE_PREFIX"]),
        transformation_ctx="transactional_source_dataset_node1654975865526",
    )
)

# Script generated for node cookie_vertex_mapping
cookie_vertex_mapping_node1654985041513 = ApplyMapping.apply(
    frame=cookie_source_dataset_node1654982654728,
    mappings=[
        ("cookie_id", "string", "~id", "string"),
        ("last_action", "string", "last_action:String", "string"),
        ("conversion_id", "string", "conversion_id:String", "string"),
        ("session_duration_sec", "long", "session_duration_sec:Long", "long"),
    ],
    transformation_ctx="cookie_vertex_mapping_node1654985041513",
)

# Script generated for node email_vertex_mapping
email_vertex_mapping_node1654897155773 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[("email", "string", "~id", "string")],
    transformation_ctx="email_vertex_mapping_node1654897155773",
)

# Script generated for node country_vertex_mapping
country_vertex_mapping_node1655149201992 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[("country", "string", "~id", "string")],
    transformation_ctx="country_vertex_mapping_node1655149201992",
)

# Script generated for node username_vertex_mapping
username_vertex_mapping_node2 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[
        ("user_name", "string", "~id", "string"),
        ("street_address", "string", "address:String", "string"),
        ("birthday", "string", "birthday:Date", "string"),
    ],
    transformation_ctx="username_vertex_mapping_node2",
)

# Script generated for node loyalty_vertex_mapping
loyalty_vertex_mapping_node1655149452851 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[("loyalty_level", "string", "~id", "string")],
    transformation_ctx="loyalty_vertex_mapping_node1655149452851",
)

# Script generated for node external_id_vertex_mapping
external_id_vertex_mapping_node1654975315785 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[("external_id", "string", "~id", "string")],
    transformation_ctx="external_id_vertex_mapping_node1654975315785",
)

# Script generated for node phone_number_vertex_mapping
phone_number_vertex_mapping_node1655080508755 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[("phone_number", "string", "~id", "string")],
    transformation_ctx="phone_number_vertex_mapping_node1655080508755",
)

# Script generated for node city_vertex_mapping
city_vertex_mapping_node1655148992656 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[("city", "string", "~id", "string")],
    transformation_ctx="city_vertex_mapping_node1655148992656",
)

# Script generated for node postcode_vertex_mapping
postcode_vertex_mapping_node1655148662826 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[("postcode", "long", "~id", "string")],
    transformation_ctx="postcode_vertex_mapping_node1655148662826",
)

# Script generated for node device_id_vertex_mapping
device_id_vertex_mapping_node1655150040373 = ApplyMapping.apply(
    frame=clickstream_source_dataset_node1654982749940,
    mappings=[("device_id", "string", "~id", "string")],
    transformation_ctx="device_id_vertex_mapping_node1655150040373",
)

# Script generated for node client_ip_vertex_mapping
client_ip_vertex_mapping_node1655149732703 = ApplyMapping.apply(
    frame=clickstream_source_dataset_node1654982749940,
    mappings=[("client_ip", "string", "~id", "string")],
    transformation_ctx="client_ip_vertex_mapping_node1655149732703",
)

# Script generated for node domain_name_vertex_mapping
domain_name_vertex_mapping_node1655151955046 = ApplyMapping.apply(
    frame=clickstream_source_dataset_node1654982749940,
    mappings=[("domain_name", "string", "~id", "string")],
    transformation_ctx="domain_name_vertex_mapping_node1655151955046",
)

# Script generated for node session_vertex_mapping
session_vertex_mapping_node1654985198507 = ApplyMapping.apply(
    frame=clickstream_source_dataset_node1654982749940,
    mappings=[
        ("session_id", "string", "~id", "string"),
        ("client_platform", "string", "client_platform:String", "string"),
        ("canonical_url", "string", "canonical_url:String", "string"),
        ("app_id", "string", "app_id:String", "string"),
        ("events", "long", "events:Long", "long"),
        ("start_timestamp", "string", "start_timestamp:String", "string"),
        ("start_event", "string", "start_event:String", "string"),
        ("end_timestamp", "string", "end_timestamp:String", "string"),
        ("end_event", "string", "end_event:String", "string"),
        ("session_duration_sec", "long", "session_duration_sec:Long", "long"),
    ],
    transformation_ctx="session_vertex_mapping_node1654985198507",
)

# Script generated for node user_agent_vertex_mapping
user_agent_vertex_mapping_node1655151682890 = ApplyMapping.apply(
    frame=clickstream_source_dataset_node1654982749940,
    mappings=[("user-agent", "string", "~id", "string")],
    transformation_ctx="user_agent_vertex_mapping_node1655151682890",
)

# Script generated for node product_category_vertex_mapping
product_category_vertex_mapping_node1655082105547 = ApplyMapping.apply(
    frame=transactional_source_dataset_node1654975865526,
    mappings=[("product_category", "string", "~id", "string")],
    transformation_ctx="product_category_vertex_mapping_node1655082105547",
)

# Script generated for node product_vertex_mapping
product_vertex_mapping_node1654988661554 = ApplyMapping.apply(
    frame=transactional_source_dataset_node1654975865526,
    mappings=[
        ("product_name", "string", "~id", "string"),
    ],
    transformation_ctx="product_vertex_mapping_node1654988661554",
)

# Script generated for node cookie_vertex_transform
cookie_vertex_transform_node1654993688196 = add_label_to_cookie(
    glueContext,
    DynamicFrameCollection(
        {
            "cookie_vertex_mapping_node1654985041513": cookie_vertex_mapping_node1654985041513
        },
        glueContext,
    ),
)

# Script generated for node email_vertex_transform
email_vertex_transform_node1655060516874 = add_label_to_email(
    glueContext,
    DynamicFrameCollection(
        {
            "email_vertex_mapping_node1654897155773": email_vertex_mapping_node1654897155773
        },
        glueContext,
    ),
)

# Script generated for node country_vertex_transform
country_vertex_transform_node1655149250019 = add_label_to_country(
    glueContext,
    DynamicFrameCollection(
        {
            "country_vertex_mapping_node1655149201992": country_vertex_mapping_node1655149201992
        },
        glueContext,
    ),
)

# Script generated for node username_vertex_transform
username_vertex_transform_node1655060400630 = add_label_to_username(
    glueContext,
    DynamicFrameCollection(
        {"username_vertex_mapping_node2": username_vertex_mapping_node2}, glueContext
    ),
)

# Script generated for node loyalty_vertex_transform
loyalty_vertex_transform_node1655149507206 = add_label_to_loyalty(
    glueContext,
    DynamicFrameCollection(
        {
            "loyalty_vertex_mapping_node1655149452851": loyalty_vertex_mapping_node1655149452851
        },
        glueContext,
    ),
)

# Script generated for node external_id_vertex_transform
external_id_vertex_transform_node1655060694932 = add_label_to_external_id(
    glueContext,
    DynamicFrameCollection(
        {
            "external_id_vertex_mapping_node1654975315785": external_id_vertex_mapping_node1654975315785
        },
        glueContext,
    ),
)

# Script generated for node phone_number_vertex_transform
phone_number_vertex_transform_node1655081719023 = add_label_to_phone_number(
    glueContext,
    DynamicFrameCollection(
        {
            "phone_number_vertex_mapping_node1655080508755": phone_number_vertex_mapping_node1655080508755
        },
        glueContext,
    ),
)

# Script generated for node city_vertex_transform
city_vertex_transform_node1655149037979 = add_label_to_city(
    glueContext,
    DynamicFrameCollection(
        {
            "city_vertex_mapping_node1655148992656": city_vertex_mapping_node1655148992656
        },
        glueContext,
    ),
)

# Script generated for node postcode_vertex_transform
postcode_vertex_transform_node1655148746892 = add_label_to_postcode(
    glueContext,
    DynamicFrameCollection(
        {
            "postcode_vertex_mapping_node1655148662826": postcode_vertex_mapping_node1655148662826
        },
        glueContext,
    ),
)

# Script generated for node device_id_vertex_filter
device_id_vertex_filter_node1655325348057 = Filter.apply(
    frame=device_id_vertex_mapping_node1655150040373,
    f=lambda row: (bool(re.match("[a-f0-9A-F]+", row["~id"]))),
    transformation_ctx="device_id_vertex_filter_node1655325348057",
)

# Script generated for node client_ip_vertex_transform
client_ip_vertex_transform_node1655149818363 = add_label_to_client_ip(
    glueContext,
    DynamicFrameCollection(
        {
            "client_ip_vertex_mapping_node1655149732703": client_ip_vertex_mapping_node1655149732703
        },
        glueContext,
    ),
)

# Script generated for node domain_name_vertex_transform
domain_name_vertex_transform_node1655152009388 = add_label_to_domain_name(
    glueContext,
    DynamicFrameCollection(
        {
            "domain_name_vertex_mapping_node1655151955046": domain_name_vertex_mapping_node1655151955046
        },
        glueContext,
    ),
)

# Script generated for node session_vertex_transform
session_vertex_transform_node1655060889182 = add_label_to_session(
    glueContext,
    DynamicFrameCollection(
        {
            "session_vertex_mapping_node1654985198507": session_vertex_mapping_node1654985198507
        },
        glueContext,
    ),
)

# Script generated for node user_agent_vertex_transform
user_agent_vertex_transform_node1655151749931 = add_label_to_user_agent(
    glueContext,
    DynamicFrameCollection(
        {
            "user_agent_vertex_mapping_node1655151682890": user_agent_vertex_mapping_node1655151682890
        },
        glueContext,
    ),
)

# Script generated for node product_category_vertex_transform
product_category_vertex_transform_node1655082297230 = add_label_to_product_category(
    glueContext,
    DynamicFrameCollection(
        {
            "product_category_vertex_mapping_node1655082105547": product_category_vertex_mapping_node1655082105547
        },
        glueContext,
    ),
)

# Script generated for node product_vertex_transform
product_vertex_transform_node1655061140254 = add_label_to_product(
    glueContext,
    DynamicFrameCollection(
        {
            "product_vertex_mapping_node1654988661554": product_vertex_mapping_node1654988661554
        },
        glueContext,
    ),
)

# Script generated for node cookie_vertex_select
cookie_vertex_select_node1655057687818 = SelectFromCollection.apply(
    dfc=cookie_vertex_transform_node1654993688196,
    key=list(cookie_vertex_transform_node1654993688196.keys())[0],
    transformation_ctx="cookie_vertex_select_node1655057687818",
)

# Script generated for node email_vertex_select
email_vertex_select_node1655060643195 = SelectFromCollection.apply(
    dfc=email_vertex_transform_node1655060516874,
    key=list(email_vertex_transform_node1655060516874.keys())[0],
    transformation_ctx="email_vertex_select_node1655060643195",
)

# Script generated for node country_vertex_select
country_vertex_select_node1655149318340 = SelectFromCollection.apply(
    dfc=country_vertex_transform_node1655149250019,
    key=list(country_vertex_transform_node1655149250019.keys())[0],
    transformation_ctx="country_vertex_select_node1655149318340",
)

# Script generated for node username_vertex_select
username_vertex_select_node1655060459538 = SelectFromCollection.apply(
    dfc=username_vertex_transform_node1655060400630,
    key=list(username_vertex_transform_node1655060400630.keys())[0],
    transformation_ctx="username_vertex_select_node1655060459538",
)

# Script generated for node loyalty_vertex_select
loyalty_vertex_select_node1655149579749 = SelectFromCollection.apply(
    dfc=loyalty_vertex_transform_node1655149507206,
    key=list(loyalty_vertex_transform_node1655149507206.keys())[0],
    transformation_ctx="loyalty_vertex_select_node1655149579749",
)

# Script generated for node external_id_vertex_select
external_id_vertex_select_node1655060821325 = SelectFromCollection.apply(
    dfc=external_id_vertex_transform_node1655060694932,
    key=list(external_id_vertex_transform_node1655060694932.keys())[0],
    transformation_ctx="external_id_vertex_select_node1655060821325",
)

# Script generated for node phone_number_vertex_select
phone_number_vertex_select_node1655081843552 = SelectFromCollection.apply(
    dfc=phone_number_vertex_transform_node1655081719023,
    key=list(phone_number_vertex_transform_node1655081719023.keys())[0],
    transformation_ctx="phone_number_vertex_select_node1655081843552",
)

# Script generated for node city_vertex_select
city_vertex_select_node1655149117885 = SelectFromCollection.apply(
    dfc=city_vertex_transform_node1655149037979,
    key=list(city_vertex_transform_node1655149037979.keys())[0],
    transformation_ctx="city_vertex_select_node1655149117885",
)

# Script generated for node postcode_vertex_select
postcode_vertex_select_node1655148797012 = SelectFromCollection.apply(
    dfc=postcode_vertex_transform_node1655148746892,
    key=list(postcode_vertex_transform_node1655148746892.keys())[0],
    transformation_ctx="postcode_vertex_select_node1655148797012",
)

# Script generated for node device_id_vertex_transform
device_id_vertex_transform_node1655150089769 = add_label_to_device_id(
    glueContext,
    DynamicFrameCollection(
        {
            "device_id_vertex_filter_node1655325348057": device_id_vertex_filter_node1655325348057
        },
        glueContext,
    ),
)

# Script generated for node client_ip_vertex_select
client_ip_vertex_select_node1655149916982 = SelectFromCollection.apply(
    dfc=client_ip_vertex_transform_node1655149818363,
    key=list(client_ip_vertex_transform_node1655149818363.keys())[0],
    transformation_ctx="client_ip_vertex_select_node1655149916982",
)

# Script generated for node domain_name_vertex_select
domain_name_vertex_select_node1655152087374 = SelectFromCollection.apply(
    dfc=domain_name_vertex_transform_node1655152009388,
    key=list(domain_name_vertex_transform_node1655152009388.keys())[0],
    transformation_ctx="domain_name_vertex_select_node1655152087374",
)

# Script generated for node session_vertex_select
session_vertex_select_node1655061059090 = SelectFromCollection.apply(
    dfc=session_vertex_transform_node1655060889182,
    key=list(session_vertex_transform_node1655060889182.keys())[0],
    transformation_ctx="session_vertex_select_node1655061059090",
)

# Script generated for node user_agent_vertex_select
user_agent_vertex_select_node1655151835693 = SelectFromCollection.apply(
    dfc=user_agent_vertex_transform_node1655151749931,
    key=list(user_agent_vertex_transform_node1655151749931.keys())[0],
    transformation_ctx="user_agent_vertex_select_node1655151835693",
)

# Script generated for node product_category_vertex_select
product_category_vertex_select_node1655082425707 = SelectFromCollection.apply(
    dfc=product_category_vertex_transform_node1655082297230,
    key=list(product_category_vertex_transform_node1655082297230.keys())[0],
    transformation_ctx="product_category_vertex_select_node1655082425707",
)

# Script generated for node product_vertex_select
product_vertex_select_node1655061245321 = SelectFromCollection.apply(
    dfc=product_vertex_transform_node1655061140254,
    key=list(product_vertex_transform_node1655061140254.keys())[0],
    transformation_ctx="product_vertex_select_node1655061245321",
)

# Script generated for node device_id_vertex_select
device_id_vertex_select_node1655150108453 = SelectFromCollection.apply(
    dfc=device_id_vertex_transform_node1655150089769,
    key=list(device_id_vertex_transform_node1655150089769.keys())[0],
    transformation_ctx="device_id_vertex_select_node1655150108453",
)

# Script generated for node cookie_graph_nodes
cookie_graph_nodes_node1654988804553 = glueContext.write_dynamic_frame.from_options(
    frame=cookie_vertex_select_node1655057687818,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="cookie_graph_nodes_node1654988804553",
)

# Script generated for node email_graph_nodes
email_graph_nodes_node1654897497572 = glueContext.write_dynamic_frame.from_options(
    frame=email_vertex_select_node1655060643195,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="email_graph_nodes_node1654897497572",
)

# Script generated for node country_graph_nodes
country_graph_nodes_node1655149334174 = glueContext.write_dynamic_frame.from_options(
    frame=country_vertex_select_node1655149318340,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="country_graph_nodes_node1655149334174",
)

# Script generated for node username_graph_nodes
username_graph_nodes_node3 = glueContext.write_dynamic_frame.from_options(
    frame=username_vertex_select_node1655060459538,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="username_graph_nodes_node3",
)

# Script generated for node loyalty_graph_nodes
loyalty_graph_nodes_node1655149596261 = glueContext.write_dynamic_frame.from_options(
    frame=loyalty_vertex_select_node1655149579749,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="loyalty_graph_nodes_node1655149596261",
)

# Script generated for node external_id_nodes
external_id_nodes_node1654975456060 = glueContext.write_dynamic_frame.from_options(
    frame=external_id_vertex_select_node1655060821325,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="external_id_nodes_node1654975456060",
)

# Script generated for node phone_number_graph_nodes
phone_number_graph_nodes_node1655081879359 = (
    glueContext.write_dynamic_frame.from_options(
        frame=phone_number_vertex_select_node1655081843552,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": s3_target_path,
            "partitionKeys": [],
        },
        transformation_ctx="phone_number_graph_nodes_node1655081879359",
    )
)

# Script generated for node city_graph_nodes
city_graph_nodes_node1655149131913 = glueContext.write_dynamic_frame.from_options(
    frame=city_vertex_select_node1655149117885,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="city_graph_nodes_node1655149131913",
)

# Script generated for node postcode_graph_nodes
postcode_graph_nodes_node1655148942084 = glueContext.write_dynamic_frame.from_options(
    frame=postcode_vertex_select_node1655148797012,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="postcode_graph_nodes_node1655148942084",
)

# Script generated for node client_ip_graph_nodes
client_ip_graph_nodes_node1655149937474 = glueContext.write_dynamic_frame.from_options(
    frame=client_ip_vertex_select_node1655149916982,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="client_ip_graph_nodes_node1655149937474",
)

# Script generated for node domain_name_graph_nodes
domain_name_graph_nodes_node1655152102844 = (
    glueContext.write_dynamic_frame.from_options(
        frame=domain_name_vertex_select_node1655152087374,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": s3_target_path,
            "partitionKeys": [],
        },
        transformation_ctx="domain_name_graph_nodes_node1655152102844",
    )
)

# Script generated for node session_graph_nodes
session_graph_nodes_node1654988858372 = glueContext.write_dynamic_frame.from_options(
    frame=session_vertex_select_node1655061059090,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="session_graph_nodes_node1654988858372",
)

# Script generated for node user_agent_graph_nodes
user_agent_graph_nodes_node1655151859097 = glueContext.write_dynamic_frame.from_options(
    frame=user_agent_vertex_select_node1655151835693,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="user_agent_graph_nodes_node1655151859097",
)

# Script generated for node product_category_graph_nodes
product_category_graph_nodes_node1655082455459 = (
    glueContext.write_dynamic_frame.from_options(
        frame=product_category_vertex_select_node1655082425707,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": s3_target_path,
            "partitionKeys": [],
        },
        transformation_ctx="product_category_graph_nodes_node1655082455459",
    )
)

# Script generated for node product_graph_nodes
product_graph_nodes_node1654988774055 = glueContext.write_dynamic_frame.from_options(
    frame=product_vertex_select_node1655061245321,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="product_graph_nodes_node1654988774055",
)

# Script generated for node device_id_graph_nodes
device_id_graph_nodes_node1655150126685 = glueContext.write_dynamic_frame.from_options(
    frame=device_id_vertex_select_node1655150108453,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": s3_target_path,
        "partitionKeys": [],
    },
    transformation_ctx="device_id_graph_nodes_node1655150126685",
)

job.commit()
