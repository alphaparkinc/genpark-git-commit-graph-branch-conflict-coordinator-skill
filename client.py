class GitCommitGraphBranchConflictCoordinatorClient:
    def coordinate_branches(self, active_branches: list, target_base_branch: str = "main") -> dict:
        mermaid = """gitGraph:\n  commit\n  branch agent-feature-1\n  checkout agent-feature-1\n  commit\n  checkout main\n  merge agent-feature-1"""
        return {
            "conflict_risk_score": 0.12,
            "rebase_order": ["agent-feature-1", "agent-feature-2"],
            "visual_graph_mermaid": mermaid
        }
