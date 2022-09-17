import wandb
wandb.init(project="test-project")

lr = 0.1
wandb.config.lr = lr

def my_train_loop():
    loss = 10

    for epoch in range(10):
        loss = loss * lr  # change as appropriate :)
        wandb.log({'epoch': epoch, 'loss': loss})
    wandb.save("mymodel.h5")


def main():
    my_train_loop()

if __name__ == "__main__":
    main()
