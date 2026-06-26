import pytest
from js_optimizer import JsOptimizer, SourceFile, OptimizerVersion

def test_optimize():
    optimizer_version = OptimizerVersion('1.0.0')
    js_optimizer = JsOptimizer(optimizer_version)
    source_files = [SourceFile('file1.js', 'console.log("Hello World!");')]
    optimized_hash = js_optimizer.optimize(source_files)
    assert len(optimized_hash) == 64

def test_optimize_multiple_files():
    optimizer_version = OptimizerVersion('1.0.0')
    js_optimizer = JsOptimizer(optimizer_version)
    source_files = [
        SourceFile('file1.js', 'console.log("Hello World!");'),
        SourceFile('file2.js', 'console.log("Hello Again!");')
    ]
    optimized_hash = js_optimizer.optimize(source_files)
    assert len(optimized_hash) == 64

def test_optimize_same_files_different_optimizer_version():
    optimizer_version1 = OptimizerVersion('1.0.0')
    optimizer_version2 = OptimizerVersion('2.0.0')
    js_optimizer1 = JsOptimizer(optimizer_version1)
    js_optimizer2 = JsOptimizer(optimizer_version2)
    source_files = [SourceFile('file1.js', 'console.log("Hello World!");')]
    optimized_hash1 = js_optimizer1.optimize(source_files)
    optimized_hash2 = js_optimizer2.optimize(source_files)
    assert optimized_hash1 != optimized_hash2

def test_optimize_different_files_same_optimizer_version():
    optimizer_version = OptimizerVersion('1.0.0')
    js_optimizer = JsOptimizer(optimizer_version)
    source_files1 = [SourceFile('file1.js', 'console.log("Hello World!");')]
    source_files2 = [SourceFile('file2.js', 'console.log("Hello Again!");')]
    optimized_hash1 = js_optimizer.optimize(source_files1)
    optimized_hash2 = js_optimizer.optimize(source_files2)
    assert optimized_hash1 != optimized_hash2
