class ReasoningAgent:
    def evaluate(self, parsed_data):
        issues = []

        if parsed_data["lines"] > 300:
            issues.append("文件过大，建议拆分")

        if len(parsed_data["functions"]) > 10:
            issues.append("函数过多，可能违反单一职责原则")

        return issues
