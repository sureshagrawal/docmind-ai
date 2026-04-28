"""RAGAS metric computation logic."""

import uuid
from datetime import datetime, timezone

from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from datasets import Dataset


def run_evaluation(qa_pairs: list[dict]) -> dict:
    """Run RAGAS evaluation on a list of Q&A pairs.

    Each pair should have: question, answer, contexts (list of strings)

    Returns: { run_id, results: [...], averages: { faithfulness, answer_relevancy, context_precision } }
    """
    run_id = str(uuid.uuid4())

    # Build dataset for RAGAS
    data = {
        "question": [p["question"] for p in qa_pairs],
        "answer": [p["answer"] for p in qa_pairs],
        "contexts": [p["contexts"] for p in qa_pairs],
    }
    dataset = Dataset.from_dict(data)

    # Run evaluation
    result = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision],
    )

    df = result.to_pandas()

    results = []
    for _, row in df.iterrows():
        results.append({
            "run_id": run_id,
            "question": row["question"],
            "answer": row["answer"],
            "faithfulness": float(row.get("faithfulness", 0)),
            "answer_relevancy": float(row.get("answer_relevancy", 0)),
            "context_precision": float(row.get("context_precision", 0)),
        })

    averages = {
        "faithfulness": df["faithfulness"].mean() if "faithfulness" in df else 0,
        "answer_relevancy": df["answer_relevancy"].mean() if "answer_relevancy" in df else 0,
        "context_precision": df["context_precision"].mean() if "context_precision" in df else 0,
    }

    return {"run_id": run_id, "results": results, "averages": averages}
