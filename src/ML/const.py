import torch
# Gobang
SIZE=15

# MCTS
CPUCT=5           # UCB计算系数
MCTSTIMES = 400   # MCTS模拟次数
HISTORY = 3
TEMPTRIG = 8

# Dirichlet
DLEPS = .25
DLALPHA = .03

# Net params
IND = HISTORY * 2 + 2
OUTD = SIZE**2
BLOCKS = 10
RES_BLOCK_FILLTERS = 128

# Train params
USECUDA = torch.cuda.is_available()
EPOCHS = 5
GAMETIMES = 3000
CHECKOUT = 50
EVALNUMS = 20
MINIBATCH = 512
WINRATE = .55
TRAINLEN = 10000

# Optim
LR = 0.03
L2 = 0.0001
