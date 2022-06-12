def add_label_to_product (glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import GlueGremlinCsvTransforms
    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, 'Product')
    return(DynamicFrameCollection({"produc_vertex_transform": df_withlabel}, glueContext))