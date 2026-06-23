import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Module:
    name: str
    exports: List[str]
    used: bool

class TreeShaker:
    def __init__(self, modules: Dict[str, Module]):
        self.modules = modules

    def shake(self) -> Dict[str, Module]:
        removed = 0
        shaken_modules = {}
        for name, module in self.modules.items():
            if module.used:
                shaken_modules[name] = module
            else:
                removed += 1
        print(f"Removed {removed} modules")
        return shaken_modules

    def optimize(self, bundle: Dict[str, List[str]]) -> Dict[str, List[str]]:
        optimized_bundle = {}
        for module_name, exports in bundle.items():
            module = self.modules.get(module_name)
            if module and module.used:
                optimized_bundle[module_name] = exports
        return optimized_bundle

def load_modules(json_data: str) -> Dict[str, Module]:
    data = json.loads(json_data)
    modules = {}
    for module_data in data:
        module = Module(
            name=module_data["name"],
            exports=module_data["exports"],
            used=module_data["used"]
        )
        modules[module.name] = module
    return modules

def load_bundle(json_data: str) -> Dict[str, List[str]]:
    data = json.loads(json_data)
    bundle = {}
    for module_data in data:
        bundle[module_data["name"]] = module_data["exports"]
    return bundle
