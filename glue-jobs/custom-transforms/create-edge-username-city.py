def create_edge_username_city (glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import GlueGremlinCsvTransforms
    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, 'hasCityAddress')
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, '~from', '~to')
    return(DynamicFrameCollection({"username_city_edge_transform": df}, glueContext))
    