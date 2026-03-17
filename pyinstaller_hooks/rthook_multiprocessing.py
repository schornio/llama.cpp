# PyInstaller runtime hook – multiprocessing support
#
# When a PyInstaller single-file executable spawns subprocesses (e.g. via
# torch's DataLoader workers or Python's multiprocessing resource_tracker),
# the child process re-executes the frozen executable.  Without calling
# freeze_support() before any other code runs the resource_tracker
# subprocess exits immediately, producing the warning:
#
#   multiprocessing/resource_tracker.py: UserWarning:
#       resource_tracker: process died unexpectedly, relaunching.
#       Some resources might leak.
#
# freeze_support() must be the very first thing called in a frozen
# executable so that worker/helper re-invocations are handled correctly
# before application code runs.
import multiprocessing
multiprocessing.freeze_support()
