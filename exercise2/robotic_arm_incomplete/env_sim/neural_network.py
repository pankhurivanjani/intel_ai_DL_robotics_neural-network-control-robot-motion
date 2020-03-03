import torch
import torch.nn as nn
import torch.nn.functional as F

'''Feed Forward Neural Network For Regression'''

############################################# FOR STUDENTS #####################################
class FullyConnectedNetwork(nn.Module):
    def __init__(self, input_dim, num_hidden_neurons, dropout_rte):
        super(FullyConnectedNetwork, self).__init__()
        ###### Define Linear Layer 0 ######

        self.h_0 = ###### Define Linear Layer 0 ######
        self.h_1 = ###### Define Linear Layer 1 ######
        self.h_2 = ###### Define Linear Layer 2 ######
        self.h_3 = ###### Define Linear Layer 3 ######
        self.h_4 = ###### Define Linear Layer 4 ######

        self.drop = ###### Define Dropout ######

    def forward(self, x):
        out_0 = torch.tanh(self.h_0(x))

        ###### Using The Defined Layers and F.tanh As The Nonlinear Function Between Layers Define Forward Function ######

        return out
#################################################################################################
