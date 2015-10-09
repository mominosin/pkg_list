from fabric.api import run

def main():
    pkg_list = _pkg_list_get()
    return _pkg_version_list(pkg_list)

def _pkg_list_get():
    return run('yum list installed --color=never')

def _pkg_version_list(pkgs):
    pkg_versions = []
    for line in pkgs.split('\n'):
        pkg_versions.append(line.split()[0] + "_" + line.split()[1])
    return pkg_versions
