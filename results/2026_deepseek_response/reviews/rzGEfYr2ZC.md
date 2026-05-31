Now I have all the information I need. Let me write the final review.

## Summary

This paper proposes SparseFW, which relaxes the combinatorial mask selection problem for LLM pruning to a convex program solved via the Frank-Wolfe (FW) algorithm. Experiments on five modern GPT architectures (LLaMA-3.1, Gemma-2, Yi-1.5, DeepSeek, Qwen2.5) show improvements in perplexity and zero-shot accuracy over Wanda and RIA, particularly at 60% and 2:4 sparsity. A theoretical bound connecting the relaxed solution to the original combinatorial problem is provided. The paper also identifies an interesting local-global objective mismatch: better local optimization of the pruning objective can harm global perplexity.

## Strengths

1. **Convex relaxation with Frank-Wolfe accounts for weight interactions.** Section 2.2 formulates mask selection as a convex program over the convex hull of binary masks and solves it with FW. The LMO (Eq. 12) is efficient (Top-k selection) and naturally yields sparse updates, addressing a genuine limitation of greedy methods that ignore weight interactions.

2. **Strong empirical gains at high sparsity on modern architectures.** Table 1 shows meaningful improvements at 60% sparsity: LLaMA-3.1-8B perplexity drops from 21.53 (Wanda) to 17.97 (SparseFW), a ~17% relative improvement. Similar gains appear on Yi-1.5 9B (10.56 vs 11.38) and Gemma-2 9B (14.83 vs 16.46). Zero-shot accuracy also consistently improves across models and sparsity regimes.

3. **Memory-efficient design that scales.** Section 2.3 precomputes G = XX^T and H = WG, making gradient computation independent of sequence length and sample count. The gradient requires only elementwise operations, one matrix multiply, and one addition.

4. **Theoretical approximation guarantee.** Lemma 1 provides a data-dependent bound decomposing the suboptimality gap into optimization error (which shrinks with FW iterations) and thresholding error. This is a genuine advantage over greedy heuristics.

5. **Honest identification of the local-global mismatch.** Section 2.3 transparently states that vanilla FW (α=0.0) "consistently yields worse results than the baselines" despite reducing per-layer error, and that fixing 90% of weights using Wanda saliency scores is necessary. This finding — that better local optimization can hurt global performance — is interesting and worth further investigation.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-experiment misalignment: the theoretical guarantee covers a different algorithm than the one that produces the reported results.** Lemma 1 bounds the suboptimality gap for Algorithm 1 (FW on all d_out × d_in variables). However, Section 2.3 states that the working version of SparseFW fixes 90% of weights using Wanda/RIA saliency scores and optimizes only the remaining 10%, because vanilla FW "consistently yields worse results than the baselines." The paper provides no theoretical analysis of the warmstarted variant. This means the available guarantee does not actually justify the empirical results. The paper acknowledges the gap (it is discussed as a "caveat") but does not bridge it.

2. **The method that actually works is a hybrid (greedy heuristic + FW refinement), not the pure convex-relaxation approach.** The headline framing ("relax the combinatorial constraints and solve with FW") implies a standalone method, but the standalone version (α=0.0) is reported to fail. The successful variant depends critically on Wanda or RIA saliency scores to decide 90% of the mask — the same greedy heuristics the paper criticizes for ignoring weight interactions. The paper's central claim ("outperform strong baselines" via convex relaxation) is misleading when the reported gains come from a hybrid that relies on those baselines' saliency scores as a warmstart. Reframing the contribution as "FW-as-refinement-on-top-of-greedy" would better match what is actually demonstrated.

3. **No standard deviations or confidence intervals for main results.** Table 1 omits variance information ("for legibility"). At 50% sparsity, many comparisons differ by only 0.1–0.2 perplexity points (e.g., LLaMA-3.1-8B: Wanda 10.09 vs SparseFW(Wanda) 10.21; DeepSeek-7B: Wanda 7.79 vs SparseFW(Wanda) 7.89). Without error bars, it is impossible to assess whether these small differences are statistically meaningful. The abstract's claim of "outperform[ing] strong baselines" is overstated for the 50% regime, where SparseFW often trails Wanda or ties within noise.

### Minor

4. **No comparison to SparseGPT, even as a reference point.** The paper scopes itself to "mask selection methods" and excludes SparseGPT because it involves a reconstruction step (Section 3). This is a defensible scope choice, but SparseGPT is the most widely-cited LLM pruning baseline and produces actual perplexity numbers. Omitting any comparison — even a single model/sparsity point with a note that it is a different category — substantially weakens the paper's positioning against "state-of-the-art" methods.

5. **Limited investigation of the local-global mismatch.** The paper identifies that vanilla FW fails despite reducing per-layer error, then fixes it with α=0.9 warmstarting. However, there is no analysis of *why* the mismatch occurs — whether FW overfits the calibration set, which layer types are most affected, or whether the mismatch correlates with specific properties of the objective. The paper states this is "likely due to a mismatch between local and global objectives" but provides no experiments to diagnose it.

### Trivial

6. The paper highlights "up to 80%" per-layer error reduction (Figure 2), but most layers show 10–40% improvement, with only a few approaching 80%. The "up to" qualifier is technically correct but the headline figure overstates typical gains.

## Nice-to-Haves

- Include the α=0.0 (pure FW) perplexity results in the main paper rather than the appendix, since this negative finding is essential context for understanding the method.
- Provide wall-clock timing or FLOPs comparison between SparseFW, Wanda, and SparseGPT.
- Investigate the causes of the local-global mismatch (e.g., does FW overfit the calibration set? Are certain layer types more susceptible?).

## Removed Points

These points from the inputs were filtered out:

- "The comparison to SparseGPT is avoided, not justified" — The original point called this a "methodological gap" and a "substantial weakening." The paper explicitly scopes to mask-selection-only methods (Section 3: "we do not compare directly to methods that involve a reconstruction step"). This is a valid scope choice; the paper's claims are about outperforming other mask selection methods. However, I've kept a minor weakness about the omission because SparseGPT's status as the dominant baseline warrants at least a reference comparison.

- "Figure 2 is misleading" — The paper says "up to 80%" which is literally true. The "20-40% average" is consistent with the figure. No misrepresentation.

- "Figure 3 improvements are not dramatic" — Subjective judgment; a ~1-point perplexity improvement with doubled samples is factually reported. Not a valid technical weakness.

- "The theoretical bound's constant may be arbitrarily large" — True of any data-dependent bound. This is an inherent property of such bounds, not a specific flaw of this paper.

- Missing related works and formatting/style nitpicks — Removed per instructions.

## Novel Insights

The most interesting finding — that optimizing the local mask selection objective more thoroughly (vanilla FW) harms global perplexity, while combining a greedy warmstart with local refinement improves it — is identified but left at the surface level. The paper does not diagnose *why* the local-global mismatch occurs. Is the mismatch due to optimization overfitting the small calibration set? Are there identifiable layer types or weight groups where the mismatch is most severe? Is the issue specific to the quadratic approximation of the loss? An empirical investigation of these questions would significantly strengthen the paper and could make the mismatch diagnosis a contribution in its own right, separate from the SparseFW method.

## Suggestions

1. Provide standard deviations or confidence intervals for perplexity results in Table 1, especially at 50% sparsity where differences are small.
2. Either adapt the theoretical analysis to cover the warmstarted variant, or explicitly reframe the theory as applying to an idealized version of the method and discuss the gap.
3. Reframe the contribution around "FW as a refinement layer on top of greedy heuristics" — this better matches what actually works and is an honest, interesting contribution.
4. Include at least one model/sparsity combination comparing to SparseGPT to anchor results to the broader literature.
5. Add experiments investigating the local-global mismatch: e.g., compare FW's selected masks on different calibration set sizes, layer types, or sparsity levels.

Score and Decision
---
### Round 1 (Bracketing)

Three queries on "LLM pruning mask selection Frank-Wolfe convex relaxation layerwise pruning":

| Band | Anchor | Avg Score | Comparison |
|------|--------|-----------|------------|
| <3.5 | 0T8vCKa7yu (CVXQ quantization) | 3.00 | Lower quality paper in a related area; SparseFW is clearly stronger |
| <3.5 | 7DY2DFDT0T (EfficientSkip) | 2.50 | Much weaker paper; SparseFW is far more rigorous |
| 3.5-7.5 | BINwUtUGuq (FISTAPruner) | 5.25 | Most directly comparable (convex optimization for LLM pruning). SparseFW has better theory, tests on more modern architectures, but has theory-practice gap |
| 3.5-7.5 | pOBvr1PxFd (OWL) | 6.00 | Stronger empirical results overall, but reviews highly mixed (scores: 5,3,8,6,8). SparseFW has more principled optimization |
| 3.5-7.5 | DwiwOcK1B7 (DSF) | 6.33 | Accept paper. Cleaner framing, fewer theory-practice contradictions |
| 3.5-7.5 | D9GoWJJxS5 (Policy Gradient) | 5.00 | Similar quality. SparseFW has stronger theoretical grounding |
| >7.5 | OfjIlbelrT (FlexPrefill) | 8.00 | Different area (attention sparsity); not comparable |

**Round-1 bracket:** 4.5 – 6.5

### Round 2 (Narrowing)

Two queries targeting the 4.5–7.5 band:

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| BINwUtUGuq (FISTAPruner) | 5.25 | SparseFW has more novel optimizer (FW vs FISTA), tests on more modern models, has theoretical guarantees. Marginally stronger paper, but the theory-practice gap is a weakness FISTAPruner doesn't have in the same way. |
| D9GoWJJxS5 (Policy Gradient) | 5.00 | Reviews highlight lack of baseline comparisons and high variance. SparseFW is cleaner and better motivated. |
| a0ftEY6puc (Multilingual Calibration) | 6.00 | Different sub-area. Similar rigor but no theory-practice misalignment issue. |
| 1GTARJhxtq (Perplexity-based Data Pruning) | 5.75 | Different problem (data pruning, not weight pruning). Not directly comparable. |

SparseFW is stronger than FISTAPruner (5.25) — better theory, more modern models — but the theory-practice misalignment is a real weakness that FISTAPruner doesn't share. It is weaker than DSF (6.33, Accept) which has a cleaner framing without contradictions between the stated method and the actual procedure.

**Final score:** 5.0 — The paper has a genuinely interesting idea and strong results at high sparsity, but the central framing is misleading (the method that works is Wanda+FW refinement, not "solving the convex relaxation"). The theoretical guarantee does not apply to the evaluated algorithm. The paper would benefit from major revisions to align its claims, theory, and experiments.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>