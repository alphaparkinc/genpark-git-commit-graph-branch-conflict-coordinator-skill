from client import GitCommitGraphBranchConflictCoordinatorClient

def main():
    client = GitCommitGraphBranchConflictCoordinatorClient()
    branches = ["feat-auth", "feat-billing", "fix-cors"]
    res = client.coordinate_branches(branches, "main")
    print(f"Conflict Risk: {res['conflict_risk_score'] * 100}%")
    print("Rebase Order:", res["rebase_order"])
    print(res["visual_graph_mermaid"])

if __name__ == "__main__":
    main()
