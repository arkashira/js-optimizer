import pytest
from tree_shaker import TreeShaker, load_modules, load_bundle

def test_shake():
    json_data = '''
    [
        {"name": "module1", "exports": ["export1", "export2"], "used": true},
        {"name": "module2", "exports": ["export3", "export4"], "used": false},
        {"name": "module3", "exports": ["export5", "export6"], "used": true}
    ]
    '''
    modules = load_modules(json_data)
    tree_shaker = TreeShaker(modules)
    shaken_modules = tree_shaker.shake()
    assert len(shaken_modules) == 2

def test_optimize():
    json_data = '''
    [
        {"name": "module1", "exports": ["export1", "export2"], "used": true},
        {"name": "module2", "exports": ["export3", "export4"], "used": false},
        {"name": "module3", "exports": ["export5", "export6"], "used": true}
    ]
    '''
    bundle_data = '''
    [
        {"name": "module1", "exports": ["export1", "export2"]},
        {"name": "module2", "exports": ["export3", "export4"]},
        {"name": "module3", "exports": ["export5", "export6"]}
    ]
    '''
    modules = load_modules(json_data)
    bundle = load_bundle(bundle_data)
    tree_shaker = TreeShaker(modules)
    optimized_bundle = tree_shaker.optimize(bundle)
    assert len(optimized_bundle) == 2

def test_load_modules():
    json_data = '''
    [
        {"name": "module1", "exports": ["export1", "export2"], "used": true},
        {"name": "module2", "exports": ["export3", "export4"], "used": false},
        {"name": "module3", "exports": ["export5", "export6"], "used": true}
    ]
    '''
    modules = load_modules(json_data)
    assert len(modules) == 3

def test_load_bundle():
    json_data = '''
    [
        {"name": "module1", "exports": ["export1", "export2"]},
        {"name": "module2", "exports": ["export3", "export4"]},
        {"name": "module3", "exports": ["export5", "export6"]}
    ]
    '''
    bundle = load_bundle(json_data)
    assert len(bundle) == 3
