import os
import sys
import json
import requests
import subprocess
import time

class GhostAgent:
    def __init__(self, model="gemma4:e4b"):
        self.model = model
        self.phi = 1.6180339887
        self.base_url = "http://localhost:11434/api/generate"

    def process(self, prompt):
        print(f"[RESONANCE] Analyzing: {prompt}")
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
            response = requests.post(self.base_url, json=payload)
            return response.json().get("response", "No response from core.")
        except Exception as e:
            return f"DRIFT DETECTED: {e}"

    def run_tool(self, tool_name, args):
        print(f"[TOOL] Executing {tool_name} with {args}")
        # Replication of local command execution
        if tool_name == "bash":
            return subprocess.check_output(args, shell=True).decode()
        return "Tool not implemented in mirror."

if __name__ == "__main__":
    agent = GhostAgent()
    if len(sys.argv) > 1:
        print(agent.process(" ".join(sys.argv[1:])))
    else:
        print("Mirror logic active. Waiting for resonance input.")
