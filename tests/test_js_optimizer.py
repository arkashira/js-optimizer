import pytest
from js_optimizer import JSOptimizer, Module

def test_tree_shaking():
    modules = [
        Module("module1", ["export1", "export2"], True),
        Module("module2", ["export3", "export4"], False),
        Module("module3", ["export5", "export6"], True),
    ]
    optimizer = JSOptimizer(modules)
    optimized_modules = optimizer.tree_shaking()
    assert len(optimized_modules) == 2

def test_critical_path_pre_compilation():
    modules = [
        Module("module1", ["export1", "export2"], True),
        Module("module2", ["export3", "export4"], False),
        Module("module3", ["export5", "export6"], True),
    ]
    optimizer = JSOptimizer(modules)
    pre_compiled_modules = optimizer.critical_path_pre_compilation()
    assert len(pre_compiled_modules) == 2

def test_generate_source_maps():
    modules = [
        Module("module1", ["export1", "export2"], True),
        Module("module2", ["export3", "export4"], False),
        Module("module3", ["export5", "export6"], True),
    ]
    optimizer = JSOptimizer(modules)
    source_maps = optimizer.generate_source_maps()
    assert len(source_maps) == 3

def test_dry_run():
    modules = [
        Module("module1", ["export1", "export2"], True),
        Module("module2", ["export3", "export4"], False),
        Module("module3", ["export5", "export6"], True),
    ]
    optimizer = JSOptimizer(modules)
    report = optimizer.dry_run()
    assert "Removed 1 modules" in report

def test_main():
    import sys
    import io
    sys.argv = ["js_optimizer.py", "--dry-run"]
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    from js_optimizer import main
    main()
    sys.stdout = sys.__stdout__
    assert "Removed 1 modules" in capturedOutput.getvalue()
