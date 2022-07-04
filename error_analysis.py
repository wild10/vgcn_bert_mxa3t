import torch

import matplotlib.pyplot as plt 


def load_metrics(load_path):
	if load_path == None:
		return
	state_dic = torch.load(load_path, map_location = device)
	print(f'Model loaded from <=={load_path}')

	return state_dic['train_loss_list'], state_dic['valid_loss_list'], state_dic['global_step_list']

# pplot de diagram
#train_loss_list, valid_loss_list, global_step_list = 	
train_loss_list = [134.1717419908382,77.67738849204034,41.50622909372396,27.13196864408019,15.787122296000234,11.791974867103818,8.90500349264039,6.372300786380038,4.821914220674444]
valid_loss_list = [5.6438673690427095,4.118835733170272,4.838788306395145 ,5.028040693359799,5.704832530071144,6.081926847087743,5.401594551625749,5.255169277505047,5.248610385240681]

global_steps_list = [0,40,80,120,160,200,240,280,320,400,440,480,520,560,600,640,680,720,760,800,840,880,920]

list_acc_valid = [88.055,87.713,88.396,86.007,86.348,87.372,88.737,88.396]
list_acc_test = [87.457,86.844,87.389,88.003,88.207,88.480,88.003,87.935]
number_epoch= [0,1,2,3,4,5,6,7,8]
plt.plot(number_epoch, train_loss_list, label='Train')
plt.plot(number_epoch, valid_loss_list, label='Valid')
plt.xlabel('epoch')
plt.ylabel('Loss')
plt.legend()
plt.show() 