def add_label_to_external_id (glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import GlueGremlinCsvTransforms
    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, 'CustomerID')
    return(DynamicFrameCollection({"external_id_vertex_transform": df_withlabel}, glueContext))