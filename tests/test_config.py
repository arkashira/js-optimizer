import pytest
import json
from src.config import load_config, validate_config, Config

def test_load_config_valid():
    config_data = {
        'criticalPathThreshold': 0.5,
        'treeShake': True,
        'rewriteRules': {'rule1': 'value1'}
    }
    with open('fastjs.config.json', 'w') as file:
        json.dump(config_data, file)
    config = load_config('fastjs.config.json')
    assert config.critical_path_threshold == 0.5
    assert config.tree_shake is True
    assert config.rewrite_rules == {'rule1': 'value1'}

def test_load_config_invalid_json():
    with open('fastjs.config.json', 'w') as file:
        file.write('invalid json')
    with pytest.raises(ValueError) as e:
        load_config('fastjs.config.json')
    assert 'Invalid JSON in config file' in str(e.value)

def test_load_config_file_not_found():
    with pytest.raises(ValueError) as e:
        load_config('non_existent_file.json')
    assert 'Config file not found' in str(e.value)

def test_validate_config_valid():
    config = Config(critical_path_threshold=0.5, tree_shake=True, rewrite_rules={'rule1': 'value1'})
    validate_config(config)

def test_validate_config_invalid_critical_path_threshold():
    config = Config(critical_path_threshold='invalid')
    with pytest.raises(ValueError) as e:
        validate_config(config)
    assert 'criticalPathThreshold must be a number' in str(e.value)

def test_validate_config_invalid_tree_shake():
    config = Config(tree_shake='invalid')
    with pytest.raises(ValueError) as e:
        validate_config(config)
    assert 'treeShake must be a boolean' in str(e.value)

def test_validate_config_invalid_rewrite_rules():
    config = Config(rewrite_rules='invalid')
    with pytest.raises(ValueError) as e:
        validate_config(config)
    assert 'rewriteRules must be a dictionary' in str(e.value)
