import torch

def convert_to_torchscript(model, example_input, script_path):
    scripted_model = torch.jit.trace(model, example_input)
    scripted_model.save(script_path)