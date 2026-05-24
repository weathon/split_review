Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper decouples the class label from the target concept in machine unlearning, identifying three realistic mismatch scenarios (target mismatch, model mismatch, data mismatch) beyond the conventional all-matched setting where class labels and target concepts coincide. The authors provide a representation-level analysis — formalized through Theorem 3.2 as "representation gravity" — showing that entangled or under-entangled features explain the failure of existing methods in these new regimes. They propose TARF, a three-phase framework using annealed gradient ascent on forgetting data and target-aware gradient descent on hard-to-affect remaining data, which collaboratively enables target identification, separation, and retraining approximation. Experiments across CIFAR-10/100, ImageNet-1k, Stable Diffusion, and TOFU demonstrate that TARF substantially narrows the gap to the retrained reference compared to multiple baselines.

## Strengths

- **Novel and well-motivated problem formulation**: The paper clearly defines three previously unexplored unlearning settings by decoupling label domains (Figure 1, Table 1). The motivation is grounded in practical scenarios where unlearning requests do not align with the training taxonomy (Section 1). Figure 2 convincingly demonstrates that representative methods (FT, GA, BS, L1-sparse, SCRUB) fail in these mismatched settings while performing adequately only in the conventional all-matched case.

- **Insightful representation-level analysis**: Theorem 3.2 analytically connects forgetting dynamics to representation distance, formalizing the "representation gravity" concept. The t-SNE visualizations and loss dynamics in Figure 3 directly corroborate the analysis, showing how entangled features cause spill-over (model mismatch) and under-entangled features cause insufficient forgetting (target/data mismatch). This analysis provides principled motivation for the algorithm design.

- **Effective unified algorithm with strong empirical results**: TARF integrates annealed gradient ascent and target-aware gradient descent in a coherent three-phase process. On CIFAR-10/100 (Table 3), TARF reduces the overall Gap to retrained reference dramatically: from 25.78 (FT) to 1.23 in target mismatch on CIFAR-10, from 48.41 (FT) to 0.96 in data mismatch. On ImageNet-1k (Table 4), TARF achieves the smallest Gap across all mismatch tasks. The fine-grained evaluation in Table 2 also shows TARF effectively preserves affected retaining data while forgetting the target.

- **Comprehensive evaluation across modalities**: Beyond classification benchmarks, TARF is validated on concept removal in Stable Diffusion (Figure 6) and personal information removal in LLMs (Table 5, TOFU dataset). The ablation studies (Figure 7) rigorously validate the annealed scheduling, model architecture robustness, and the choice of gradient cleaning on identified false-retaining data.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Known target-class count assumption**: The target identification phase (Phase I) assumes the number of target-concept classes in the remaining set is known (Section 2.1: "we assume that the number of classes in D_un belonging to the target concept is known in target mismatch forgetting"). While the paper acknowledges this limitation and references robustness studies under varied false-retaining set sizes in Appendix E (line 365), the assumption constrains deployment when this prior is unavailable or wrong. This does not invalidate the method but limits the scope of demonstrated applicability.

- **Theory serves as intuition rather than a tight guarantee**: Theorem 3.2 includes terms (the largest eigenvalue of the Jacobian, gradient norm of the forgetting loss) that are not controlled in the empirical analysis, and the algorithm does not directly instantiate the bound. The paper appropriately frames the theorem as providing "intuitive implication" (Remark 3.1) rather than formal guarantees, so this is not an overclaim. However, the connection between the theoretical analysis and the concrete algorithmic choices (choice of τ, k, annealing schedule) remains mostly post-hoc.

- **Preliminary LLM evaluation**: The TOFU case study (Table 5) uses only QA-probability as a metric. Given the growing importance of LLM unlearning, additional metrics such as fluency, downstream task accuracy, or more sophisticated forgetting metrics would strengthen these results. The paper acknowledges the preliminary nature of these experiments.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis for the phase-transition hyperparameters (T, t₀, t₁) in the main text would help practitioners tune the method without relying solely on appendix guidance.
- A baseline that uses class-hierarchy information (e.g., weighted fine-tuning on known target-concept classes) would strengthen the claim that TARF's benefits go beyond better utilization of available hierarchy.
- A runtime breakdown by phase (target identification vs. separation vs. retraining approximation) would help practitioners assess the cost-benefit trade-off.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh Critic: "Sensitivity of the accuracy-drop identification phase is not probed with a controlled study"** — REMOVED as a standalone weakness. The paper explicitly acknowledges this limitation in the conclusion ("we also observe a few preliminary cases where the gravity signal becomes weaker and the ranking slightly noisier") and mentions robustness studies in Appendix E. The claim that "no empirical stress-test is provided" is partially contradicted by the paper's own description of appendix content. The acknowledgment is folded into the minor weakness about the theoretical connection.

2. **Harsh Critic: "The phrase 'target concept being larger or smaller than the class unit' could be sharpened"** — REMOVED as a pure phrasing/style nitpick.

3. **Harsh Critic: "The meaning of the MIA column should be explicitly stated in the caption"** — REMOVED. The metrics are defined in Section 4.1, and the caption format is constrained by space. Not substantive.

4. **Strength Finder: "This paper addressed an important problem / targeted an interesting question"** — REMOVED as generic. The more specific novelty of the problem formulation is captured in the first retained strength.

## Novel Insights

The paper's conceptual framework — decoupling the label domains of forgetting data, model output, and target concept — generalizes prior class-wise unlearning into a richer taxonomy that captures practical deployment scenarios. The "representation gravity" lens (Theorem 3.2 + Definition 3.3), while not a tight theoretical guarantee, provides a useful diagnostic tool: it explains why some forgetting tasks succeed and others fail based on the representation structure of the pre-trained model, rather than just the amount of data or optimization procedure. This perspective could inform future unlearning method design beyond the specific TARF algorithm.

## Suggestions

- Move the robustness studies on false-retaining set size from Appendix E to the main text, even as a brief paragraph or figure, to directly address concerns about the known-class-count assumption.
- Consider whether a purely data-driven threshold selection (e.g., gap statistic on the accuracy-drop distribution) could replace the known-class-count prior, and report results if feasible.
- For the LLM experiments, add at least one additional evaluation axis (e.g., perplexity on retained data, or a standard QA benchmark) to give a more complete picture of the forgetting/retention trade-off.

## Score and Decision

**Calibration summary:**

| Anchor | Path | Score | Round | Comparison |
|--------|------|-------|-------|------------|
| Same paper (prior venue) | OHOmpkGiYK | 5.75 | R1 | Previous version of this paper; current version is improved with broader applications and refined exposition |
| Deep Unlearning | pUOesbrlw4 | 5.25 | R1 | Narrower scope (class unlearning only), less comprehensive evaluation; this paper is stronger |
| Forget Vectors at Play | 7tpMhoPXrL | 4.80 | R1 | Novel idea but limited scalability and experiments; this paper is clearly stronger |
| Label-Agnostic Forgetting | SIZWiya7FE | 6.00 | R2 | Accepted; novel problem, solid method, but narrower scope; this paper is comparable or slightly broader |
| Utility/Complexity of Unlearning | HVFMooKrHX | 6.60 | R2 | Accepted; stronger theory, weaker empirics; different contribution type |
| Oblivious Unlearning | wAemQcyWqq | 5.67 | R2 | Rejected; comparable quality but this paper has broader empirical validation |

**Round 1 bracket:** 5.0–7.0. The paper's prior version scored 5.75, and the improved version plausibly sits above 5.5.

**Round 2 narrowing:** Compared against Label-Agnostic Forgetting (6.00, accepted), this paper offers a comparably novel problem formulation with broader scope (four scenarios vs. one) and more comprehensive experiments spanning classification, generation, and LLMs. It does not reach the theoretical depth of the Utility/Complexity paper (6.60). The paper sits squarely at the 6.0 level — a solid contribution with minor but real limitations that are acknowledged and addressable.

The weaknesses are minor and well-acknowledged; the strengths (novel formulation, representation-level analysis, effective algorithm, comprehensive experiments) are substantial and well-supported.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>