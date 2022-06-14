def add_label_to_phone_number (glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import GlueGremlinCsvTransforms
    df = dfc.select(list(dfc.keys())[0])
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, 'PhoneNumber')
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, 'df_deduplicated')
    return(DynamicFrameCollection({"phone_number_vertex_transform": df_deduplicated}, glueContext))
    