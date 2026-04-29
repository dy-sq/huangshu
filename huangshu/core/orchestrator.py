from agents.parser_agent import ParserAgent
from agents.reasoning_agent import ReasoningAgent
from agents.optimization_agent import OptimizationAgent
from agents.validation_agent import ValidationAgent

class Orchestrator:
    def __init__(self):
        self.parser = ParserAgent()
        self.reasoner = ReasoningAgent()
        self.optimizer = OptimizationAgent()
        self.validator = ValidationAgent()

    def run(self, code):
        parsed = self.parser.analyze_file(code)
        issues = self.reasoner.evaluate(parsed)
        optimized = self.optimizer.optimize(code, issues)
        test_result = self.validator.run_tests()

        return {
            "issues": issues,
            "optimized_code": optimized,
            "test_result": test_result
        }
