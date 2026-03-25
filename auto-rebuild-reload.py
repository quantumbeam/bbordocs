from watchfiles import watch
from subprocess import run
from livereload import Server
import threading

HOME_DIR = '/home/suzuki/work/bbordocs/'
BUILD_DIR = HOME_DIR + '_build/ja/'
WATCH_TARGETS = (
    HOME_DIR+ 'index.rst',
    HOME_DIR+ 'conf.py',
    HOME_DIR+ 'docs/',
    HOME_DIR+ '_static/',
    HOME_DIR+ '_templates/',
)
EXCLUDES = (
    HOME_DIR+ 'docs/vars/locale.rst'
)

def autobuild():
    print("=== Watching for updates ===")
    for changes in watch(HOME_DIR, recursive=True):
        files = [path for (_type, path) in changes]
        if any(
            f.startswith(WATCH_TARGETS) and not f.startswith(EXCLUDES)
            for f in files
        ):
            print("=== Detected changes, rebuilding... ===")
            run(["make", "ja"])
        else:
            print("=== Detected changes, but no building. ===")
            continue
def main():
    run(["make", "ja"])

    t = threading.Thread(target=autobuild, daemon=True)
    t.start()

    server = Server()
    server.watch(BUILD_DIR + '**/*')
    server.serve(root=BUILD_DIR, host="localhost", port=3000)

if __name__ == "__main__":
    main()
