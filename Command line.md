## Calling from the command line
**`python`** `{`_`options`_`}` `[``-`**`c`** _`command`_ `|` `-`**`m`** _`module`_ `|` _`file`_ `|` `-``]` `{`_`args`_`}`

**python** accepts only options that start with a hyphen (-)
-v -> verbosely traces module import and cleanup actions
-V -> prints the Python verson number, then terminates
-B -> Don't save cached bytecode to disk

Use **-i** when you want to get an interactive session immediately after running some script, with top-level variables still intact and available for inspection

Another way to specify which Python script to run is with **-m** _module_. This option tells Python to load and run a module named **_module_** (or the ___main__.py_ member of a package or ZIP file named _module_) from some directory that is part of Python’s sys.path; this is useful with several modules from Python’s standard library. For example, as covered in [“The timeit module”](https://learning.oreilly.com/library/view/python-in-a/9781098113544/ch17.html#the_timeit_module), **-m timeit** is often the best way to perform micro-benchmarking of Python statements

_args_ are arbitrary strings; the Python you run can access these strings as items of the list `sys.argv`

## Best practices
- Always call `#!/usr/bin/env python`