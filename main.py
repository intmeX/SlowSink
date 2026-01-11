import yaml
import argparse
from slowsink.agents import create_travel_agent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='./configs/shanghai_walk.yaml', help='Agent yaml file path')
    args = parser.parse_args()
    config = yaml.load(open(args.config), Loader=yaml.FullLoader)
    agent = create_travel_agent(config)
    response = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": input('请输入你的所在地点与出行需求：')}
            ],
        },
    )
    print(response)


if __name__ == '__main__':
    main()
