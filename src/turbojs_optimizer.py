import json
from dataclasses import dataclass
from typing import List

@dataclass
class TurboJSConfig:
    entry_point: str
    output_file: str

def generate_webpack_config(turbojs_config: TurboJSConfig) -> str:
    return f"""
module.exports = {{
  entry: '{turbojs_config.entry_point}',
  output: {{
    filename: '{turbojs_config.output_file}'
  }},
  module: {{
    rules: [
      {{
        test: /\.js$/,
        use: 'turbojs-loader'
      }}
    ]
  }}
}};
"""

def process_js_files(js_files: List[str]) -> List[str]:
    # Simulate TurboJS processing
    return [f"processed_{file}" for file in js_files]

def integrate_turbojs_with_webpack(turbojs_config: TurboJSConfig, js_files: List[str]) -> str:
    processed_js_files = process_js_files(js_files)
    return generate_webpack_config(turbojs_config)
