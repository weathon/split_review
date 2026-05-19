- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8
Now I have all the verification I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes CP-Fuse, an inference-time method for copyright protection that adaptively fuses outputs from two language models trained on disjoint copyrighted datasets. The key idea is a token-level optimization that enforces a **balancing property** — neither base model dominates the generation, preventing regurgitation of memorized samples. Experiments on abstract generation, story-telling, and code generation (with 7B-parameter models) show that CP-Fuse reduces exact-match copying by >20× compared to overfitted models, outperforms inference-time baselines (system prompts, MemFree, token-wise CpDelta), preserves utility on coding benchmarks and fluency metrics, composes well with training-time defenses like goldfish loss, and resists prefix-prompting extraction attacks.

## Strengths

- **Large and consistent reduction in verbatim copying.** Table 1 shows exact-match (EM) substring lengths drop from >1300 for overfitted models to ~55–70 for CP-Fuse across all three datasets and both splits — a >20× reduction. The JPlag plagiarism score for code drops from ~1.0 (clear infringement) to 0.03 (near-zero). These are the paper's core quantitative claims and are thoroughly supported.

- **Balancing property provides a principled mechanism.** Lemma 5 (balancing property) proves that CP-Fuse adaptively weights the two base models so that neither dominates the generation, and Figure 2 empirically shows that CP-Fuse maintains nearly equal cumulative log-likelihoods under both models while the fixed-weight cpdelta alternative does not. This directly explains why CP-Fuse outperforms cpdelta.

- **Utility is preserved.** Table 2 shows that CP-Fuse achieves pass@1 on APPS (0.47), MBPP (0.43), and HumanEval (0.28) that is comparable to or better than the overfitted models (0.43, 0.44, 0.29), and fluency on WritingPrompts (2.17) is identical to the overfitted baseline. MemFree, by contrast, degrades utility — a known issue with filtering-based approaches that the paper identifies and illustrates with concrete code examples (Figure 4).

- **Composability with training-time methods.** Table 3a demonstrates that applying CP-Fuse on top of goldfish-loss-trained models further reduces EM from 84.68→20.68 (split 1) and 120.28→25.50 (split 2), showing that CP-Fuse is orthogonal to and enhances existing memorization-mitigation techniques.

- **Robustness to prefix-prompting extraction.** Figure 3b shows that CP-Fuse's exact-match length remains low (~20–30) and stable as the prefix length increases, indicating that an adversary cannot easily guide the fused model back to memorized sequences by providing longer prefixes.

- **Thorough evaluation across domains and metrics.** Experiments cover four datasets (MathAbstracts, WritingPrompts, Python instructions, APPS), multiple memorization metrics (EM, BLEU, Levenshtein, JPlag, Dolos), and utility metrics (pass@1 with unit tests, Prometheus-v2 fluency). The 95th-percentile reporting focus is appropriate for the copyright setting, where concern is about long extractions rather than average behavior.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Grid search computational overhead is not quantified.** Section 3.2 states that the optimization "can be solved efficiently by performing a grid search" over 19 discretization points. However, no runtime, per-token latency, or throughput comparison against the base models or baselines is provided anywhere in the paper. Since this is the first practical implementation of the NAF-inspired fusion, readers cannot assess whether the overhead is acceptable for real-time deployment. A brief quantification (e.g., tokens/second vs. baseline, or wall-clock time per generation) would resolve this.

### Trivial

None.

## Nice-to-Haves

- **Clarify the relationship between the balancing property and the k-NAF guarantee.** The paper derives the balancing property (Lemma 5) from a k-NAF-inspired objective, but does not explicitly state that the balancing property itself does **not** imply the full-sequence k-NAF guarantee from Definition 1 — the algorithm is an "efficient approximate algorithm" as noted, but a reader may over-interpret the theoretical support. The paper would benefit from a brief remark clarifying that the balancing property provides intuition but does not constitute a formal k-NAF certificate.

- **Discuss how separability could be achieved in practice.** The paper acknowledges the separability assumption and tests it in the ideal case. A brief discussion of how real deployments could achieve approximate separability (e.g., partitioning by publisher, author, or license type) would strengthen the practical framing.

- **Report text-generation utility on non-copyrighted test sets with human evaluation or overlap metrics.** The fluency scores (~2.17/5) are low for all methods (including the overfitted baseline), which may reflect a strict rubric rather than poor quality. A complementary human evaluation or a text-overlap metric (e.g., self-BLEU on non-copyrighted outputs) would strengthen the utility claim beyond the current pass@1/fluency reporting.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Prometheus-v2 scores are low (~2.17 out of 5)"** (from harsh critic). The scores are low for **all** methods uniformly, indicating a strict rubric rather than CP-Fuse-specific degradation. The comparison is fair and the cited rubric is standard. Critics referencing this as a weakness misread the paper's fair comparison design.

- **"Separability assumption tested only in ideal case" / "real-world applicability."** The paper explicitly acknowledges this as a limitation and scopes it as future work in the conclusion. This is proper scientific scoping, not a weakness.

- **Theoretical gap between balancing property and k-NAF framed as a weakness.** The harsh critic explicitly states this is "not a flaw" and the paper is "honest about this being an 'efficient approximate algorithm'." This point belongs in Nice-to-Haves as a clarification suggestion, not in Weaknesses.

## Novel Insights

None beyond the paper's own contributions. The two-reviewer synthesis did not surface any observation about the method's mechanism or implications that is not already present in the paper's own discussion.

## Suggestions

1. **Add a brief computational cost analysis** (per-token forward passes or wall-clock time relative to greedy decoding) to help practitioners judge deployability. This addresses the only verifiable gap in the paper's presentation.
2. **Add one sentence after Lemma 5** clarifying that the balancing property provides intuition for why CP-Fuse mitigates regurgitation but does not constitute a formal k-NAF certificate for the full sequence — this preempts a natural reader question.
3. **Include a paragraph in the conclusion or future work** discussing how the separability assumption could be approximated in practice (e.g., partitioning by publisher, license type, or author).
