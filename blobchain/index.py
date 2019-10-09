import subprocess
import process

def get_current_commit():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()


def main():
    current_commit = get_current_commit()

    # It's run in the root dir, so these paths are correct
    old_path = './previous.png'
    new_path = './' + current_commit + '.png'

    process.process(old_path, new_path)


main()
