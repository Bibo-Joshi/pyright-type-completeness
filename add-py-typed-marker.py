"""
Add a py.typed marker to the package specified as the first command-line arg.
"""
from importlib.util import find_spec
from pathlib import Path
from sys import argv

package_name = argv[1]
spec = find_spec(package_name)
package_dirs = spec.submodule_search_locations

if len(package_dirs) < 1:
  raise RuntimeError(
    f"Could not find installed location of package {package_name}."
  )
if len(package_dirs) > 1:
  raise RuntimeError(
    f"Found more than one location for package {package_name}. "
    "It's not currently clear how to handle this, so please file an issue "
    "with pyright-type-completeness explaining what you were trying to do "
    "and what you think should happen."
  )

package_dir = package_dirs[0]

(Path(package_dir) / "py.typed").touch()
print(f"Added py.typed to {package_dir}.")
