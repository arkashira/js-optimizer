import hashlib
import json
from dataclasses import dataclass
from typing import List

@dataclass
class SourceFile:
    name: str
    content: str

@dataclass
class OptimizerVersion:
    version: str

class JsOptimizer:
    def __init__(self, optimizer_version: OptimizerVersion):
        self.optimizer_version = optimizer_version

    def optimize(self, source_files: List[SourceFile]) -> str:
        content_hash = self._calculate_content_hash(source_files)
        optimizer_version_hash = self._calculate_optimizer_version_hash()
        combined_hash = self._combine_hashes(content_hash, optimizer_version_hash)
        return combined_hash

    def _calculate_content_hash(self, source_files: List[SourceFile]) -> str:
        combined_content = ''.join(file.content for file in source_files)
        return hashlib.sha256(combined_content.encode()).hexdigest()

    def _calculate_optimizer_version_hash(self) -> str:
        return hashlib.sha256(self.optimizer_version.version.encode()).hexdigest()

    def _combine_hashes(self, content_hash: str, optimizer_version_hash: str) -> str:
        combined_hash = hashlib.sha256((content_hash + optimizer_version_hash).encode()).hexdigest()
        return combined_hash
