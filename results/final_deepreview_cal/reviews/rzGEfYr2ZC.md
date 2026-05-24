Now I have enough information to write the final review. Let me synthesize everything.

## Summary

This paper introduces SparseFW, a layerwise LLM pruning method that relaxes the combinatorial mask-selection problem into a convex program over the convex hull of binary masks and solves it with the Frank-Wolfe (FW) algorithm. The key insight is that by optimizing over the continuous relaxation, the method can account for weight interactions that greedy heuristics (Wanda, RIA) ignore. The method is evaluated on five modern GPT model families (LLaMA-3.1, Gemma-2, Yi-1.5, DeepSeek, Qwen2.5) across unstructured and 2:4 semi-structured sparsity.

## Strengths

- **Clean methodological contribution with solid theoretical grounding.** The convex relaxation of mask selection to the convex hull \(\mathcal{C}_k\) (Equation 10) is well-motivated and transforms an intractable combinatorial problem into a tractable convex program. The use of Frank-Wolfe is apt: it is projection-free, the LMO (Equation 12) is a simple Top-\(k\) operation, and each iteration requires only cheap matrix operations after the one-time precomputation of \(G = XX^\top\) and \(H = WG\). Lemma 1 provides a convergence-plus-thresholding error bound that connects the relaxed solution to the original combinatorial problem — a theoretical contribution lacking in competing mask-selection methods.

- **Strong empirical gains at higher sparsity levels.** Table 1 shows consistent perplexity and zero-shot accuracy improvements at 60% unstructured and 2:4 semi-structured sparsity across most model families. For example, LLaMA-3.1-8B at 60% sparsity improves from 21.53 (Wanda) to 17.97 perplexity, a ~16.5% reduction. Zero-shot accuracy gains at 60% sparsity are consistent across models (e.g., LLaMA-3.1-8B from 48.08% to 51.92%). Figure 2 shows per-layer pruning error reductions of up to 80% compared to Wanda warmstarts, directly validating that FW successfully optimizes the local objective.

- **Memory-efficient design enabling LLM scale.** Precomputing \(G = XX^\top\) (size \(d_{in} \times d_{in}\)) decouples per-iteration cost from the calibration data size — critical when \(X\) can be \(4096 \times 524,288\). The gradient computation in Algorithm 1 requires only two elementwise multiplications and one matrix multiplication.

- **Broad model coverage.** Evaluation spans five distinct GPT architectures (LLaMA-3.1-8B, Gemma-2-9B, Yi-1.5-9B, DeepSeek-7B, Qwen2.5-7B), and the method supports both unstructured and 2:4 semi-structured sparsity with simple LMO adaptations.

## Weaknesses

### Major

- **The working method is a hybrid that depends critically on the greedy baseline it aims to replace.** As disclosed in §2.3, vanilla FW (\(\alpha=0\), full mask optimization) consistently *worsens* perplexity relative to Wanda. The method that produces the reported gains fixes 90% of the mask using Wanda saliency scores (\(\alpha=0.9\)) and runs FW only on the remaining 10% of weights. The abstract and introduction present the convex-relaxation approach as a clean advance over greedy heuristics without mentioning this dependence. While the paper is honest about this limitation (§2.3 and §5), the framing inflates the contribution: the actual algorithm is Wanda + local refinement, and the claim that convex relaxation "outperforms state-of-the-art mask selection methods" conflates the hybrid with the pure approach. This does not invalidate the contribution — FW does meaningful work on its assigned subset, and even small \(\alpha\) values yield improvements — but the paper should be more upfront that the headline method requires a greedy warmstart to succeed.

- **Mixed results at 50% sparsity.** Table 1 shows that at 50% unstructured sparsity, SparseFW sometimes degrades perplexity relative to baselines (LLaMA-3: Wanda 10.09 vs. SparseFW 10.21; DeepSeek: Wanda 7.79 vs. SparseFW 7.89). The paper acknowledges this ("much more consistent and bigger improvements in the higher sparsity regimes than for 50% sparsity," §3) but the abstract's claim of consistent gains requires qualification. At lower sparsity, the benefit of mask refinement shrinks and may not justify the added compute.

### Minor

- **No variance estimates for main results.** Table 1 omits standard deviations "for legibility." While the 60% and 2:4 gains are large enough to be convincing without them, the marginal 50% cases (e.g., Yi-1.5: 6.58 vs. 6.58) are uninterpretable without variance. Figure 3 shows min-max ranges for one setting, confirming the authors can compute them.

- **Theoretical guarantees do not incorporate the \(\alpha\) constraint.** Lemma 1 and the accompanying analysis apply to the full FW optimization (Algorithm 1), not the \(\alpha\)-constrained variant used in practice. The theory correctly characterizes the core algorithmic approach, and the authors are transparent about the practical modification, but the gap between theory and deployed method should be explicitly noted.

- **SparseGPT comparison omitted by scope but would strengthen the paper.** The paper explicitly scopes itself to mask-selection-only methods (§3), excluding SparseGPT which also reconstructs remaining weights. This is defensible, but a natural question is whether SparseFW's mask improvements persist after a reconstruction step — a comparison that would significantly strengthen the practical case.

### Trivial

- Figure 3 reports min-max range but Figure 2 and Table 1 do not, creating inconsistency in reporting.
- The paper claims "reduces the per-layer pruning error by up to 70%" in the contributions list (§1) but Figure 2 shows up to 80%; the abstract says 80% — a minor inconsistency.

## Nice-to-Haves

- A comparison where SparseFW masks are combined with a closed-form weight reconstruction (à la SparseGPT) and benchmarked against SparseGPT's end-to-end pipeline would clarify whether the mask improvements translate beyond the mask-selection-only setting.
- A diagnostic investigation into *why* full FW (\(\alpha=0\)) harms global perplexity despite reducing per-layer error (e.g., analyzing which types of weights FW erroneously prunes) would turn a limitation into a scientific insight and potentially yield a principled fix.
- Wall-clock time and memory comparisons against Wanda/SparseGPT would help practitioners assess the cost-benefit tradeoff of 2000 FW iterations per layer.
- Standard deviations or confidence intervals for all main table results.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that the comparison ignores SparseGPT as a critical missing baseline:** The paper explicitly states (§3) that it compares against mask-selection-only methods (Wanda, RIA) and not methods that combine mask selection with weight reconstruction. This is a legitimate scope decision. Removed as a weakness; moved to Nice-to-Haves.

- **Harsh Critic claim that empirical gains are "modest" and evidence is "too weak":** At 60% and 2:4 sparsity, gains are substantial and consistent across models (e.g., LLaMA-3.1-8B at 60%: 21.53 → 17.97). The claim of weakness is exaggerated. The variance concern is retained as Minor.

- **Harsh Critic claim that the core method "does not succeed at the task it was designed for":** The method does succeed — just within a constrained search space. The α=0.1 case (only 10% fixed) still shows improvements, and FW demonstrably reduces per-layer error. The claim overstates the problem. Retained as a Major weakness with accurate framing.

- **Strength Finder's claim of "consistent improvements in perplexity ... across five LLM families and three sparsity regimes":** This overstates — the 50% sparsity results are mixed. Qualified in the Strengths section.

## Novel Insights

Beyond the paper's own contributions, the review process surfaces an interesting tension: the paper shows that better optimization of the *local* (per-layer) pruning objective can harm the *global* (end-to-end) perplexity — a finding that is underappreciated in the layerwise pruning literature. The α-constraint fix reveals that Wanda's greedy saliency scores are surprisingly good at identifying globally important weights, even when a more thorough local optimization would prune them. This observation — that local optimality and global performance can be at odds, and that a hybrid approach leveraging both greedy priors and convex optimization navigates this tension — is a genuinely useful insight for future work in this space.

## Suggestions

- Reframe the abstract and introduction to be upfront about the α-constraint. Rather than presenting SparseFW as replacing greedy heuristics, present it as *refining* them — a hybrid that uses a greedy warmstart to identify high-confidence weights and convex optimization to improve the rest.
- Extend the theoretical analysis to cover the α-constrained case, even informally, to close the theory-practice gap.
- Add standard deviations to Table 1. Even a footnote with average variance across runs would suffice and remove a distracting omission.
- Investigate and report which specific layers or weight types benefit most from FW refinement vs. the Wanda warmstart — this could illuminate the local-global mismatch.

## Score and Decision

**Round 1 Bracket:** Based on anchors, the paper sits between ~5.0 and ~6.5. FISTAPruner (5.25) provides the closest lower bound — also a convex-optimization approach to LLM pruning, rejected for novelty concerns and insufficient differentiation. OWL (6.00, Rejected) and PruneNet (6.00, Accepted) bracket the upper end.

**Round 2 Narrowing:** SparseFW is stronger than FISTAPruner (5.25) — it has cleaner theoretical guarantees, more modern model coverage, better-motivated methodology, and more honest limitations. It is comparable to but slightly below PruneNet (6.00) — PruneNet's calibration-free idea was more novel, though SparseFW has broader evaluation. The α-constraint limitation and mixed 50% results prevent the paper from reaching 6.0.

**Final Score: 5.5**

**Anchor comparison summary:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| BINwUtUGuq (FISTAPruner) | 5.25 | R1/R2 | SparseFW is stronger: better theory, more modern models, more honest limitations |
| Y0qmwm6tgy (MoreauPruner) | 4.80 | R1 | SparseFW is clearly stronger: broader evaluation, more substantive contributions |
| D9GoWJJxS5 (Policy Gradient Pruning) | 5.00 | R2 | SparseFW is stronger: cleaner method, better empirical results |
| LCrm1FSl26 (Mecon) | 5.60 | R2 | Comparable quality; SparseFW has better theoretical grounding |
| pOBvr1PxFd (OWL) | 6.00 | R2 | OWL had stronger high-sparsity results but fundamental motivation issues; SparseFW is slightly below |
| 5RZoYIT3u6 (PruneNet) | 6.00 | R1/R2 | PruneNet's calibration-free idea was more novel; SparseFW is comparable but slightly below |
| ud8FtE1N4N (Sparse Scaling) | 6.67 | R2 | Different problem domain; not directly comparable |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>