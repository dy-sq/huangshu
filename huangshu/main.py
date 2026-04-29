from core.orchestrator import Orchestrator

if __name__ == "__main__":
    with open("example.py", "r") as f:
        code = f.read()

    orchestrator = Orchestrator()
    result = orchestrator.run(code)

    print("问题:", result["issues"])
    print("优化建议:", result["optimized_code"])
    print("测试结果:", result["test_result"])
