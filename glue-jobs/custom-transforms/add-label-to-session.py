def add_label_to_session (glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import GlueGremlinCsvTransforms
    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, 'SessionID')
    return(DynamicFrameCollection({"session_vertex_transform": df_withlabel}, glueContext))