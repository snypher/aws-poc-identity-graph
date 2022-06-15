import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrameCollection
from awsglue.dynamicframe import DynamicFrame

# Script generated for node session_device_id_edge_transform
def create_edge_session_device_id(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "usedDevice")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"session_device_id_edge_transform": df}, glueContext)


# Script generated for node username_email_edge_transform
def create_edge_username_email(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "hasEmail")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"username_email_edge_transform": df}, glueContext)


# Script generated for node username_postcode_edge_transform
def create_edge_username_postcode(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "hasPostCodeAddress")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"username_postcode_edge_transform": df}, glueContext)


# Script generated for node username_phone_edge_transform
def create_edge_username_phone(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "hasPhone")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"username_phone_edge_transform": df}, glueContext)


# Script generated for node customer_product_edge_transform
def create_edge_customer_product(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "hasPurchased")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"customer_product_edge_transform": df}, glueContext)


# Script generated for node username_loyalty_edge_transform
def create_edge_username_loyalty(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "hasLoyaltyLevel")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"username_loyalty_edge_transform": df}, glueContext)


# Script generated for node username_external_id_edge_transform
def create_edge_username_external_id(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "hasExternalId")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection(
        {"username_external_id_edge_transform": df}, glueContext
    )


# Script generated for node username_city_edge_transform
def create_edge_username_city(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "hasCityAddress")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"username_city_edge_transform": df}, glueContext)


# Script generated for node cookie_username_edge_transform
def create_edge_cookie_username(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "loggedAs")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"cookie_username_edge_transform": df}, glueContext)


# Script generated for node product_category_edge_transform
def create_edge_product_category(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "inCategory")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"product_category_edge_transform": df}, glueContext)


# Script generated for node session_client_ip_edge_transform
def create_edge_session_client_ip(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "lastSeenAtIP")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"session_client_ip_edge_transform": df}, glueContext)


# Script generated for node session_username_edge_transform
def create_edge_session_username(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "loggedAs")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"session_username_edge_transform": df}, glueContext)


# Script generated for node session_useragent_edge_transform
def create_edge_session_useragent(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "usedDevice")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"session_useragent_edge_transform": df}, glueContext)


# Script generated for node session_cookie_edge_transform
def create_edge_session_cookie(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "hasCookie")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"session_cookie_edge_transform": df}, glueContext)


# Script generated for node session_client_ip_edge_transform
def create_edge_session_domain(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "lastSeenAtDomain")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"session_domain_edge_transform": df}, glueContext)


# Script generated for node city_country_edge_transform
def create_edge_city_country(glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import (
        GlueGremlinCsvTransforms,
    )

    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, "inCountry")
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, "~from", "~to")
    return DynamicFrameCollection({"city_country_edge_transform": df}, glueContext)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node clickstream_source_dataset
clickstream_source_dataset_node1655245001033 = (
    glueContext.create_dynamic_frame.from_catalog(
        database="database_poc_identity_graph",
        table_name="poc_identity_graph_clickstream",
        transformation_ctx="clickstream_source_dataset_node1655245001033",
    )
)

# Script generated for node first_party_source_dataset
first_party_source_dataset_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="database_poc_identity_graph",
    table_name="poc_identity_graph_first_party",
    transformation_ctx="first_party_source_dataset_node1",
)

# Script generated for node transactional_source_dataset
transactional_source_dataset_node1655242846478 = (
    glueContext.create_dynamic_frame.from_catalog(
        database="database_poc_identity_graph",
        table_name="poc_identity_graph_transactional",
        transformation_ctx="transactional_source_dataset_node1655242846478",
    )
)

# Script generated for node cookie_source_dataset
cookie_source_dataset_node1655250072952 = glueContext.create_dynamic_frame.from_catalog(
    database="database_poc_identity_graph",
    table_name="poc_identity_graph_cookie",
    transformation_ctx="cookie_source_dataset_node1655250072952",
)

# Script generated for node session_client_ip_edge_mapping
session_client_ip_edge_mapping_node1655246114986 = ApplyMapping.apply(
    frame=clickstream_source_dataset_node1655245001033,
    mappings=[
        ("session_id", "string", "~from", "string"),
        ("client_ip", "string", "~to", "string"),
    ],
    transformation_ctx="session_client_ip_edge_mapping_node1655246114986",
)

# Script generated for node session_username_edge_mapping
session_username_edge_mapping_node1655248699655 = ApplyMapping.apply(
    frame=clickstream_source_dataset_node1655245001033,
    mappings=[
        ("session_id", "string", "~from", "string"),
        ("user_name", "string", "~to", "string"),
    ],
    transformation_ctx="session_username_edge_mapping_node1655248699655",
)

# Script generated for node session_client_ip_edge_mapping
session_client_ip_edge_mapping_node1655248027483 = ApplyMapping.apply(
    frame=clickstream_source_dataset_node1655245001033,
    mappings=[
        ("session_id", "string", "~from", "string"),
        ("domain_name", "string", "~to", "string"),
    ],
    transformation_ctx="session_client_ip_edge_mapping_node1655248027483",
)

# Script generated for node session_device_id_edge_mapping
session_device_id_edge_mapping_node1655248355616 = ApplyMapping.apply(
    frame=clickstream_source_dataset_node1655245001033,
    mappings=[
        ("session_id", "string", "~from", "string"),
        ("device_id", "string", "~to", "string"),
    ],
    transformation_ctx="session_device_id_edge_mapping_node1655248355616",
)

# Script generated for node session_useragent_edge_mapping
session_useragent_edge_mapping_node1655249029796 = ApplyMapping.apply(
    frame=clickstream_source_dataset_node1655245001033,
    mappings=[
        ("session_id", "string", "~from", "string"),
        ("user-agent", "string", "~to", "string"),
    ],
    transformation_ctx="session_useragent_edge_mapping_node1655249029796",
)

# Script generated for node username_external_id_edge_mapping
username_external_id_edge_mapping_node1655158276159 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[
        ("user_name", "string", "~from", "string"),
        ("external_id", "string", "~to", "string"),
    ],
    transformation_ctx="username_external_id_edge_mapping_node1655158276159",
)

# Script generated for node username_phone_edge_mapping
username_phone_edge_mapping_node1655158615615 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[
        ("user_name", "string", "~from", "string"),
        ("phone_number", "string", "~to", "string"),
    ],
    transformation_ctx="username_phone_edge_mapping_node1655158615615",
)

# Script generated for node username_loyalty_edge_mapping
username_loyalty_edge_mapping_node1655159128827 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[
        ("user_name", "string", "~from", "string"),
        ("loyalty_points", "long", "loyalty_points:Long", "long"),
        ("loyalty_level", "string", "~to", "string"),
    ],
    transformation_ctx="username_loyalty_edge_mapping_node1655159128827",
)

# Script generated for node username_email_edge_mapping
username_email_edge_mapping_node2 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[
        ("user_name", "string", "~from", "string"),
        ("email", "string", "~to", "string"),
    ],
    transformation_ctx="username_email_edge_mapping_node2",
)

# Script generated for node username_postcode_edge_mapping
username_postcode_edge_mapping_node1655158856971 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[
        ("user_name", "string", "~from", "string"),
        ("postcode", "long", "~to", "string"),
    ],
    transformation_ctx="username_postcode_edge_mapping_node1655158856971",
)

# Script generated for node username_city_edge_mapping
username_city_edge_mapping_node1655159619024 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[
        ("user_name", "string", "~from", "string"),
        ("city", "string", "~to", "string"),
    ],
    transformation_ctx="username_city_edge_mapping_node1655159619024",
)

# Script generated for node city_country_edge_mapping
city_country_edge_mapping_node1655160004375 = ApplyMapping.apply(
    frame=first_party_source_dataset_node1,
    mappings=[
        ("city", "string", "~from", "string"),
        ("country", "string", "~to", "string"),
    ],
    transformation_ctx="city_country_edge_mapping_node1655160004375",
)

# Script generated for node product_category_edge_mapping
product_category_edge_mapping_node1655243948818 = ApplyMapping.apply(
    frame=transactional_source_dataset_node1655242846478,
    mappings=[
        ("product_id", "string", "~from", "string"),
        ("product_category", "string", "~to", "string"),
    ],
    transformation_ctx="product_category_edge_mapping_node1655243948818",
)

# Script generated for node customer_product_edge_mapping
customer_product_edge_mapping_node1655244735635 = ApplyMapping.apply(
    frame=transactional_source_dataset_node1655242846478,
    mappings=[
        ("product_id", "string", "~to", "string"),
        ("purchased_date", "string", "purchased_date:Date", "string"),
        ("customer_id", "string", "~from", "string"),
        ("reward_points", "long", "reward_points:Long", "long"),
    ],
    transformation_ctx="customer_product_edge_mapping_node1655244735635",
)

# Script generated for node cookie_username_edge_mapping
cookie_username_edge_mapping_node1655250853166 = ApplyMapping.apply(
    frame=cookie_source_dataset_node1655250072952,
    mappings=[
        ("cookie_id", "string", "~from", "string"),
        ("user_name", "string", "~to", "string"),
    ],
    transformation_ctx="cookie_username_edge_mapping_node1655250853166",
)

# Script generated for node session_cookie_edge_mapping
session_cookie_edge_mapping_node1655250132603 = ApplyMapping.apply(
    frame=cookie_source_dataset_node1655250072952,
    mappings=[
        ("cookie_id", "string", "~to", "string"),
        ("session_id", "string", "~from", "string"),
    ],
    transformation_ctx="session_cookie_edge_mapping_node1655250132603",
)

# Script generated for node session_client_ip_edge_transform
session_client_ip_edge_transform_node1655246790185 = create_edge_session_client_ip(
    glueContext,
    DynamicFrameCollection(
        {
            "session_client_ip_edge_mapping_node1655246114986": session_client_ip_edge_mapping_node1655246114986
        },
        glueContext,
    ),
)

# Script generated for node session_username_edge_transform
session_username_edge_transform_node1655248802533 = create_edge_session_username(
    glueContext,
    DynamicFrameCollection(
        {
            "session_username_edge_mapping_node1655248699655": session_username_edge_mapping_node1655248699655
        },
        glueContext,
    ),
)

# Script generated for node session_client_ip_edge_transform
session_client_ip_edge_transform_node1655248164018 = create_edge_session_domain(
    glueContext,
    DynamicFrameCollection(
        {
            "session_client_ip_edge_mapping_node1655248027483": session_client_ip_edge_mapping_node1655248027483
        },
        glueContext,
    ),
)

# Script generated for node session_device_id_edge_transform
session_device_id_edge_transform_node1655248481778 = create_edge_session_device_id(
    glueContext,
    DynamicFrameCollection(
        {
            "session_device_id_edge_mapping_node1655248355616": session_device_id_edge_mapping_node1655248355616
        },
        glueContext,
    ),
)

# Script generated for node session_useragent_edge_transform
session_useragent_edge_transform_node1655249102011 = create_edge_session_useragent(
    glueContext,
    DynamicFrameCollection(
        {
            "session_useragent_edge_mapping_node1655249029796": session_useragent_edge_mapping_node1655249029796
        },
        glueContext,
    ),
)

# Script generated for node username_external_id_edge_transform
username_external_id_edge_transform_node1655158449998 = create_edge_username_external_id(
    glueContext,
    DynamicFrameCollection(
        {
            "username_external_id_edge_mapping_node1655158276159": username_external_id_edge_mapping_node1655158276159
        },
        glueContext,
    ),
)

# Script generated for node username_phone_edge_transform
username_phone_edge_transform_node1655158691997 = create_edge_username_phone(
    glueContext,
    DynamicFrameCollection(
        {
            "username_phone_edge_mapping_node1655158615615": username_phone_edge_mapping_node1655158615615
        },
        glueContext,
    ),
)

# Script generated for node username_loyalty_edge_transform
username_loyalty_edge_transform_node1655159437185 = create_edge_username_loyalty(
    glueContext,
    DynamicFrameCollection(
        {
            "username_loyalty_edge_mapping_node1655159128827": username_loyalty_edge_mapping_node1655159128827
        },
        glueContext,
    ),
)

# Script generated for node username_email_edge_transform
username_email_edge_transform_node1655060400630 = create_edge_username_email(
    glueContext,
    DynamicFrameCollection(
        {"username_email_edge_mapping_node2": username_email_edge_mapping_node2},
        glueContext,
    ),
)

# Script generated for node username_postcode_edge_transform
username_postcode_edge_transform_node1655158942271 = create_edge_username_postcode(
    glueContext,
    DynamicFrameCollection(
        {
            "username_postcode_edge_mapping_node1655158856971": username_postcode_edge_mapping_node1655158856971
        },
        glueContext,
    ),
)

# Script generated for node username_city_edge_transform
username_city_edge_transform_node1655159862591 = create_edge_username_city(
    glueContext,
    DynamicFrameCollection(
        {
            "username_city_edge_mapping_node1655159619024": username_city_edge_mapping_node1655159619024
        },
        glueContext,
    ),
)

# Script generated for node city_country_edge_transform
city_country_edge_transform_node1655160076596 = create_edge_city_country(
    glueContext,
    DynamicFrameCollection(
        {
            "city_country_edge_mapping_node1655160004375": city_country_edge_mapping_node1655160004375
        },
        glueContext,
    ),
)

# Script generated for node product_category_edge_transform
product_category_edge_transform_node1655244485259 = create_edge_product_category(
    glueContext,
    DynamicFrameCollection(
        {
            "product_category_edge_mapping_node1655243948818": product_category_edge_mapping_node1655243948818
        },
        glueContext,
    ),
)

# Script generated for node customer_product_edge_transform
customer_product_edge_transform_node1655244817350 = create_edge_customer_product(
    glueContext,
    DynamicFrameCollection(
        {
            "customer_product_edge_mapping_node1655244735635": customer_product_edge_mapping_node1655244735635
        },
        glueContext,
    ),
)

# Script generated for node cookie_username_edge_transform
cookie_username_edge_transform_node1655250820742 = create_edge_cookie_username(
    glueContext,
    DynamicFrameCollection(
        {
            "cookie_username_edge_mapping_node1655250853166": cookie_username_edge_mapping_node1655250853166
        },
        glueContext,
    ),
)

# Script generated for node session_cookie_edge_transform
session_cookie_edge_transform_node1655250389355 = create_edge_session_cookie(
    glueContext,
    DynamicFrameCollection(
        {
            "session_cookie_edge_mapping_node1655250132603": session_cookie_edge_mapping_node1655250132603
        },
        glueContext,
    ),
)

# Script generated for node session_client_ip_edge_select
session_client_ip_edge_select_node1655247178187 = SelectFromCollection.apply(
    dfc=session_client_ip_edge_transform_node1655246790185,
    key=list(session_client_ip_edge_transform_node1655246790185.keys())[0],
    transformation_ctx="session_client_ip_edge_select_node1655247178187",
)

# Script generated for node session_username_edge_select
session_username_edge_select_node1655248814259 = SelectFromCollection.apply(
    dfc=session_username_edge_transform_node1655248802533,
    key=list(session_username_edge_transform_node1655248802533.keys())[0],
    transformation_ctx="session_username_edge_select_node1655248814259",
)

# Script generated for node session_client_ip_edge_select
session_client_ip_edge_select_node1655248251339 = SelectFromCollection.apply(
    dfc=session_client_ip_edge_transform_node1655248164018,
    key=list(session_client_ip_edge_transform_node1655248164018.keys())[0],
    transformation_ctx="session_client_ip_edge_select_node1655248251339",
)

# Script generated for node session_device_id_edge_select
session_device_id_edge_select_node1655248628545 = SelectFromCollection.apply(
    dfc=session_device_id_edge_transform_node1655248481778,
    key=list(session_device_id_edge_transform_node1655248481778.keys())[0],
    transformation_ctx="session_device_id_edge_select_node1655248628545",
)

# Script generated for node session_useragent_edge_select
session_useragent_edge_select_node1655249204238 = SelectFromCollection.apply(
    dfc=session_useragent_edge_transform_node1655249102011,
    key=list(session_useragent_edge_transform_node1655249102011.keys())[0],
    transformation_ctx="session_useragent_edge_select_node1655249204238",
)

# Script generated for node username_external_id_edge_select
username_external_id_edge_select_node1655158532761 = SelectFromCollection.apply(
    dfc=username_external_id_edge_transform_node1655158449998,
    key=list(username_external_id_edge_transform_node1655158449998.keys())[0],
    transformation_ctx="username_external_id_edge_select_node1655158532761",
)

# Script generated for node username_phone_edge_select
username_phone_edge_select_node1655158767674 = SelectFromCollection.apply(
    dfc=username_phone_edge_transform_node1655158691997,
    key=list(username_phone_edge_transform_node1655158691997.keys())[0],
    transformation_ctx="username_phone_edge_select_node1655158767674",
)

# Script generated for node username_loyalty_edge_select
username_loyalty_edge_select_node1655159537232 = SelectFromCollection.apply(
    dfc=username_loyalty_edge_transform_node1655159437185,
    key=list(username_loyalty_edge_transform_node1655159437185.keys())[0],
    transformation_ctx="username_loyalty_edge_select_node1655159537232",
)

# Script generated for node username_email_edge_select
username_email_edge_select_node1655060459538 = SelectFromCollection.apply(
    dfc=username_email_edge_transform_node1655060400630,
    key=list(username_email_edge_transform_node1655060400630.keys())[0],
    transformation_ctx="username_email_edge_select_node1655060459538",
)

# Script generated for node username_postcode_edge_select
username_postcode_edge_select_node1655159078677 = SelectFromCollection.apply(
    dfc=username_postcode_edge_transform_node1655158942271,
    key=list(username_postcode_edge_transform_node1655158942271.keys())[0],
    transformation_ctx="username_postcode_edge_select_node1655159078677",
)

# Script generated for node username_city_edge_select
username_city_edge_select_node1655159955100 = SelectFromCollection.apply(
    dfc=username_city_edge_transform_node1655159862591,
    key=list(username_city_edge_transform_node1655159862591.keys())[0],
    transformation_ctx="username_city_edge_select_node1655159955100",
)

# Script generated for node city_country_edge_select
city_country_edge_select_node1655160165546 = SelectFromCollection.apply(
    dfc=city_country_edge_transform_node1655160076596,
    key=list(city_country_edge_transform_node1655160076596.keys())[0],
    transformation_ctx="city_country_edge_select_node1655160165546",
)

# Script generated for node product_category_edge_select
product_category_edge_select_node1655244666619 = SelectFromCollection.apply(
    dfc=product_category_edge_transform_node1655244485259,
    key=list(product_category_edge_transform_node1655244485259.keys())[0],
    transformation_ctx="product_category_edge_select_node1655244666619",
)

# Script generated for node customer_product_edge_select
customer_product_edge_select_node1655244950238 = SelectFromCollection.apply(
    dfc=customer_product_edge_transform_node1655244817350,
    key=list(customer_product_edge_transform_node1655244817350.keys())[0],
    transformation_ctx="customer_product_edge_select_node1655244950238",
)

# Script generated for node cookie_username_edge_select
cookie_username_edge_select_node1655250927384 = SelectFromCollection.apply(
    dfc=cookie_username_edge_transform_node1655250820742,
    key=list(cookie_username_edge_transform_node1655250820742.keys())[0],
    transformation_ctx="cookie_username_edge_select_node1655250927384",
)

# Script generated for node session_cookie_edge_select
session_cookie_edge_select_node1655250518292 = SelectFromCollection.apply(
    dfc=session_cookie_edge_transform_node1655250389355,
    key=list(session_cookie_edge_transform_node1655250389355.keys())[0],
    transformation_ctx="session_cookie_edge_select_node1655250518292",
)

# Script generated for node session_client_ip_graph_edges
session_client_ip_graph_edges_node1655247196831 = (
    glueContext.write_dynamic_frame.from_options(
        frame=session_client_ip_edge_select_node1655247178187,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="session_client_ip_graph_edges_node1655247196831",
    )
)

# Script generated for node session_username_graph_edges
session_username_graph_edges_node1655248984500 = (
    glueContext.write_dynamic_frame.from_options(
        frame=session_username_edge_select_node1655248814259,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="session_username_graph_edges_node1655248984500",
    )
)

# Script generated for node session_domain_graph_edges
session_domain_graph_edges_node1655248270929 = (
    glueContext.write_dynamic_frame.from_options(
        frame=session_client_ip_edge_select_node1655248251339,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="session_domain_graph_edges_node1655248270929",
    )
)

# Script generated for node session_device_id_graph_edges
session_device_id_graph_edges_node1655248641516 = (
    glueContext.write_dynamic_frame.from_options(
        frame=session_device_id_edge_select_node1655248628545,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="session_device_id_graph_edges_node1655248641516",
    )
)

# Script generated for node session_useragent_graph_edges
session_useragent_graph_edges_node1655249219117 = (
    glueContext.write_dynamic_frame.from_options(
        frame=session_useragent_edge_select_node1655249204238,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="session_useragent_graph_edges_node1655249219117",
    )
)

# Script generated for node username_external_id_graph_edges
username_external_id_graph_edges_node1655158563340 = (
    glueContext.write_dynamic_frame.from_options(
        frame=username_external_id_edge_select_node1655158532761,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="username_external_id_graph_edges_node1655158563340",
    )
)

# Script generated for node username_phone_graph_edges
username_phone_graph_edges_node1655158811505 = (
    glueContext.write_dynamic_frame.from_options(
        frame=username_phone_edge_select_node1655158767674,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="username_phone_graph_edges_node1655158811505",
    )
)

# Script generated for node username_loyalty_gprah_edges
username_loyalty_gprah_edges_node1655159557115 = (
    glueContext.write_dynamic_frame.from_options(
        frame=username_loyalty_edge_select_node1655159537232,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="username_loyalty_gprah_edges_node1655159557115",
    )
)

# Script generated for node username_email_graph_edges
username_email_graph_edges_node3 = glueContext.write_dynamic_frame.from_options(
    frame=username_email_edge_select_node1655060459538,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
        "partitionKeys": [],
    },
    transformation_ctx="username_email_graph_edges_node3",
)

# Script generated for node username_postcode_graph_edges
username_postcode_graph_edges_node1655159093557 = (
    glueContext.write_dynamic_frame.from_options(
        frame=username_postcode_edge_select_node1655159078677,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="username_postcode_graph_edges_node1655159093557",
    )
)

# Script generated for node username_city_graph_edges
username_city_graph_edges_node1655159969396 = (
    glueContext.write_dynamic_frame.from_options(
        frame=username_city_edge_select_node1655159955100,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="username_city_graph_edges_node1655159969396",
    )
)

# Script generated for node city_country_graph_edges
city_country_graph_edges_node1655160179576 = (
    glueContext.write_dynamic_frame.from_options(
        frame=city_country_edge_select_node1655160165546,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="city_country_graph_edges_node1655160179576",
    )
)

# Script generated for node product_category_graph_edges
product_category_graph_edges_node1655244683476 = (
    glueContext.write_dynamic_frame.from_options(
        frame=product_category_edge_select_node1655244666619,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="product_category_graph_edges_node1655244683476",
    )
)

# Script generated for node customer_product_graph_edges
customer_product_graph_edges_node1655244967442 = (
    glueContext.write_dynamic_frame.from_options(
        frame=customer_product_edge_select_node1655244950238,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="customer_product_graph_edges_node1655244967442",
    )
)

# Script generated for node cookie_username_graph_edges
cookie_username_graph_edges_node1655250990201 = (
    glueContext.write_dynamic_frame.from_options(
        frame=cookie_username_edge_select_node1655250927384,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="cookie_username_graph_edges_node1655250990201",
    )
)

# Script generated for node session_cookie_graph_edges
session_cookie_graph_edges_node1655250531789 = (
    glueContext.write_dynamic_frame.from_options(
        frame=session_cookie_edge_select_node1655250518292,
        connection_type="s3",
        format="csv",
        connection_options={
            "path": "s3://poc-identity-graph-733157031621/datasets/graph/initial/",
            "partitionKeys": [],
        },
        transformation_ctx="session_cookie_graph_edges_node1655250531789",
    )
)

job.commit()
