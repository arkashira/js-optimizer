import json
import argparse
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Module:
    name: str
    exports: List[str]
    critical_path: bool

class JSOptimizer:
    def __init__(self, modules: List[Module]):
        self.modules = modules

    def tree_shaking(self) -> List[Module]:
        used_exports = set()
        for module in self.modules:
            if module.critical_path:
                used_exports.update(module.exports)
        optimized_modules = []
        for module in self.modules:
            if any(export in used_exports for export in module.exports):
                optimized_modules.append(module)
        return optimized_modules

    def critical_path_pre_compilation(self) -> List[Module]:
        pre_compiled_modules = []
        for module in self.modules:
            if module.critical_path:
                pre_compiled_modules.append(module)
        return pre_compiled_modules

    def generate_source_maps(self) -> Dict[str, str]:
        source_maps = {}
        for module in self.modules:
            source_maps[module.name] = module.name
        return source_maps

    def dry_run(self) -> str:
        optimized_modules = self.tree_shaking()
        removed_modules = [module for module in self.modules if module not in optimized_modules]
        size_savings = len(removed_modules)
        report = f"Removed {size_savings} modules"
        return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    modules = [
        Module("module1", ["export1", "export2"], True),
        Module("module2", ["export3", "export4"], False),
        Module("module3", ["export5", "export6"], True),
    ]
    optimizer = JSOptimizer(modules)
    if args.dry_run:
        print(optimizer.dry_run())
    else:
        optimized_modules = optimizer.tree_shaking()
        pre_compiled_modules = optimizer.critical_path_pre_compilation()
        source_maps = optimizer.generate_source_maps()
        print("Optimized modules:")
        for module in optimized_modules:
            print(module.name)
        print("Pre-compiled modules:")
        for module in pre_compiled_modules:
            print(module.name)
        print("Source maps:")
        print(json.dumps(source_maps))

if __name__ == "__main__":
    main()
