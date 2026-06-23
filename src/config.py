import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    critical_path_threshold: Optional[float] = None
    tree_shake: Optional[bool] = None
    rewrite_rules: Optional[dict] = None

def load_config(file_path: str) -> Config:
    try:
        with open(file_path, 'r') as file:
            config_data = json.load(file)
        return Config(
            critical_path_threshold=config_data.get('criticalPathThreshold'),
            tree_shake=config_data.get('treeShake'),
            rewrite_rules=config_data.get('rewriteRules')
        )
    except FileNotFoundError:
        raise ValueError(f"Config file not found: {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config file: {e}")

def validate_config(config: Config) -> None:
    if config.critical_path_threshold is not None and not isinstance(config.critical_path_threshold, (int, float)):
        raise ValueError("criticalPathThreshold must be a number")
    if config.tree_shake is not None and not isinstance(config.tree_shake, bool):
        raise ValueError("treeShake must be a boolean")
    if config.rewrite_rules is not None and not isinstance(config.rewrite_rules, dict):
        raise ValueError("rewriteRules must be a dictionary")
