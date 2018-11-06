"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/export.py defines the 'export' method that
will be used to export the trained model.

"""


def export(model, path, method="default"):
    import shutil
    global_path = model[0]
    technology = model[1]
    outputed_files = model[2]
    if technology == "tensorflow" and len(outputed_files) == 2:
        if method == "default" and type(path) == list:
            for i in range(outputed_files):
                shutil.copy2(outputed_files[i], path[i])
        else if method == "tflite":

        else if method == "coreml":
            import tfcoreml as tf_converter
            tf_converter.convert(tf_model_path=outputed_files[0],
                                 mlmodel_path=path,
                                 output_feature_names=[
                                     'softmax/logits:0'],
                                 image_input_names=['Mul:0'],
                                 class_labels=outputed_files[1],
                                 red_bias=-1,
                                 green_bias=-1,
                                 blue_bias=-1,
                                 image_scale=2.0 / 255.0
                                 )
        else:
            raise ValueError(
                "[Neuron - Export] ERROR: Wrong arguments. See the wiki for help.")
            return
    else if technology == "createml" and method == "default":
        shutil.copy2(outputed_files[0], path)
    else:
        raise ValueError(
            "[Neuron - Export] ERROR: Wrong arguments. See the wiki for help.")
        return
    print("[Neuron - Export] All file where exported.")
