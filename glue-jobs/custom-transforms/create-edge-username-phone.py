def create_edge_username_phone (glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import GlueGremlinCsvTransforms
    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, 'hasPhone')
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, '~from', '~to')
    return(DynamicFrameCollection({"username_phone_edge_transform": df}, glueContext))
    