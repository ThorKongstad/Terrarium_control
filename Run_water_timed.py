from tenacity import retry, wait_fixed
from subprocess import call
import argparse
import time


@retry(wait=wait_fixed(1))
def water_start(kas_name: str) -> None: call(['kasa', '--alias', kas_name, 'on'])


@retry(wait=wait_fixed(1))
def water_stop(kas_name: str) -> None: call(['kasa', '--alias', kas_name, 'off'])


def main(kasa_name, run_time):
    water_start(kasa_name)
    time.sleep(run_time)
    water_stop(kasa_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('kasa_name')
    parser.add_argument('run_time', type=int)
    args = parser.parse_args()

    main(
        kasa_name=args.kasa_name,
        run_time=args.run_time
    )
