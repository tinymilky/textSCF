import torch

from models.brainTextSCFComplex import brainTextSCFComplex

def getModel(opt):

    model_name = opt['model']
    nkwargs = opt['nkwargs']
    model = None

    if 'brainTextSCFComplex' in model_name:
        model = brainTextSCFComplex(**nkwargs)

    model = model.cuda()

    print("----->>>> Model %s is built ..." % model_name)

    return model
