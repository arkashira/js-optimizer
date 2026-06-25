from turbojs_optimizer import generate_webpack_config, process_js_files, integrate_turbojs_with_webpack
from dataclasses import dataclass
import pytest

@dataclass
class TurboJSConfig:
    entry_point: str
    output_file: str

def test_generate_webpack_config():
    turbojs_config = TurboJSConfig("entry.js", "output.js")
    expected_config = """
module.exports = {
  entry: 'entry.js',
  output: {
    filename: 'output.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        use: 'turbojs-loader'
      }
    ]
  }
};
"""
    assert generate_webpack_config(turbojs_config) == expected_config

def test_process_js_files():
    js_files = ["file1.js", "file2.js"]
    expected_processed_files = ["processed_file1.js", "processed_file2.js"]
    assert process_js_files(js_files) == expected_processed_files

def test_integrate_turbojs_with_webpack():
    turbojs_config = TurboJSConfig("entry.js", "output.js")
    js_files = ["file1.js", "file2.js"]
    expected_config = """
module.exports = {
  entry: 'entry.js',
  output: {
    filename: 'output.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        use: 'turbojs-loader'
      }
    ]
  }
};
"""
    assert integrate_turbojs_with_webpack(turbojs_config, js_files) == expected_config

def test_integrate_turbojs_with_webpack_empty_js_files():
    turbojs_config = TurboJSConfig("entry.js", "output.js")
    js_files = []
    expected_config = """
module.exports = {
  entry: 'entry.js',
  output: {
    filename: 'output.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        use: 'turbojs-loader'
      }
    ]
  }
};
"""
    assert integrate_turbojs_with_webpack(turbojs_config, js_files) == expected_config
