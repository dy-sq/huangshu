import subprocess

class ValidationAgent:
    def run_tests(self):
        result = subprocess.run(["pytest"], capture_output=True, text=True)
        return result.stdout
