"""wrapper for xcodebuild command line tool (OSX only)"""
import subprocess

name = 'xcodebuild'
platforms = ['Darwin']

#------------------------------------------------------------------------------
def check_exists() :
    """test if xcodebuild is in the path"""
    try :
        subprocess.check_output(['xcodebuild', '-version'])
        return True
    except OSError:
        return False

#------------------------------------------------------------------------------
def run_build(target, build_type, build_dir, num_jobs=1) :
    """build a target

    target      -- name of build target, or None
    build_type  -- CMAKE_BUILD_TYPE string (e.g. Release, Debug)
    build_dir   -- directory where xcode project file is located
    num_jobs    -- number of parallel jobs (default: 1)
    """
    cmdLine = ['xcodebuild', '-jobs', str(num_jobs), '-configuration', build_type]
    if target is not None :
        cmdLine.extend(['-target', target])
    res = subprocess.call(cmdLine, cwd=build_dir)
    return res == 0

#------------------------------------------------------------------------------
def run_clean(build_dir) :
    """run the special 'clean' target

    build_dir -- directory where the xcode project file is located
    """
    res = subprocess.call(['xcodebuild', 'clean'], cwd=build_dir)
    return res == 0

    