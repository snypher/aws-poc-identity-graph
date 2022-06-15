def create_edge_session_cookie (glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import GlueGremlinCsvTransforms
    df = dfc.select(list(dfc.keys())[0])
    df = GlueGremlinCsvTransforms.addLabel(df, 'hasCookie')
    df = GlueGremlinCsvTransforms.create_edge_id_column(df, '~from', '~to')
    return(DynamicFrameCollection({"session_cookie_edge_transform": df}, glueContext))
