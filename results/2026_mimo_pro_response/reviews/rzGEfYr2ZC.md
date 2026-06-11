Now I'll write the final consolidated review.

---

## Summary

This paper introduces SparseFW, a layerwise LLM pruning method that formulates the mask selection problem as a convex relaxation over the convex hull of binary masks and solves it via the Frank-Wolfe algorithm. The paper unifies Wanda and RIA as greedy single-weight approximations to the same combinatorial objective, provides theoretical approximation guarantees for the rounded relaxed solution, and demonstrates empirical improvements across five modern LLMs (Gemma-2, Yi-1.5, DeepSeek-7B, Qwen2.5-7B/14B, LLaMA-3) at 50%, 60%, and 2:4 sparsity.

## Strengths

- **Principled convex relaxation with efficient LMO**: The reformulation of mask selection as a convex program (Eq. 11) with a top-k Linear Minimization Oracle (Eq. 12) is technically elegant. The precomputation of G=XX^T and H=WG (Algorithm 1, line 1) reduces the dominant data structure from O(d_in · N·L) to O(d_in^2), decoupling cost from sequence length and sample count—a 128× reduction for typical LLaMA-2-7B settings. This makes the method practical at LLM scale.

- **Theoretical approximation guarantees unique among competing methods**: Lemma 1 (Section 4) decomposes the gap between the rounded solution and the optimal combinatorial mask into optimization error (controllable via T iterations) and thresholding error (bounded by curvature and mask dimension). This provides formal justification that greedy methods like Wanda and RIA lack.

- **Substantial per-layer error reductions**: Figure 2 shows up to 80% relative pruning error reduction over Wanda on LLaMA-3.1-8B at 60% sparsity, with consistent 20–40% average reductions across layers, models, and sparsity regimes. This directly validates the convex relaxation's superiority on the local objective.

- **Consistent improvements at high sparsity regimes**: At 60% unstructured sparsity, SparseFW(Wanda) improves perplexity on 5/6 models (e.g., Gemma-2-9B: 16.46→14.83, LLaMA-3-8B: 21.53→17.97) and achieves the best zero-shot accuracy in 6/6 cases. At 2:4 semi-structured sparsity, similar patterns hold. The gains are most pronounced at the high-sparsity regimes that motivate practical deployment.

- **Better exploitation of calibration data**: Figure 3 (right) shows SparseFW perplexity drops from ~22 to ~19.5 when increasing calibration samples from 64 to 512, while Wanda barely moves (25.1→24.6). This demonstrates that the convex relaxation extracts substantially more information from additional calibration data—a practically important finding.

- **Novel unification of existing pruning methods**: Section 2.1 cleanly derives Wanda's saliency score as the optimal single-weight pruning criterion (Eq. 5) and shows RIA is equivalent to Wanda applied to a rescaled weight matrix (Eqs. 6–7). This reframing elevates the contribution beyond "another pruning method" to a principled critique of the greedy paradigm.

## Weaknesses

### Fatal

None.

### Major

- **The α=0.9 dependence substantially narrows the actual contribution relative to the framing**: The paper's central narrative is that greedy methods ignore weight interactions while the convex relaxation captures them. However, the paper states that "setting α = 0.0 (full FW without any fixed weights) consistently yields worse results than the baselines" (Section 2.3, line 157). The method requires fixing 90% of weights using the Wanda saliency heuristic, with FW optimizing only the remaining 10%. This means SparseFW functionally operates as a local refinement on top of the greedy heuristic it claims to improve upon, not a replacement. The abstract's claim that SparseFW "outperforms strong baselines" does not mention this dependence, creating a misleading impression of the contribution's nature. While the conclusion is honest ("Without fixing part of the mask, it tends to prune weights crucial for overall performance"), the body and abstract should foreground this.

- **Inconsistent results at 50% sparsity and select regressions at higher sparsity**: At 50% unstructured sparsity, SparseFW(Wanda) loses to plain Wanda on DeepSeek-7B (7.89 vs. 7.79) and LLaMA-3 (10.21 vs. 10.09). At 60% sparsity, DeepSeek-7B regresses under both warmstarts (11.99 vs. 11.44; 12.41 vs. 11.87). At 2:4, Qwen2.5-14B regresses under both warmstarts (11.82 vs. 11.37; 11.20 vs. 10.98). The claim of "generally performs on par with or better" is defensible only by aggregating across all regimes. With standard deviations omitted ("for legibility"), it is unclear whether the small gains at 50% (often < 0.1 perplexity) are statistically meaningful.

- **No wall-clock compute cost reported anywhere**: The paper acknowledges SparseFW is "clearly more compute-intensive" than Wanda and RIA (line 240) but provides zero timing data. For a method that trades compute for model quality, practitioners need to know whether pruning takes minutes or hours per model. The argument that cost is "worthwhile for deployed models" needs quantitative support.

### Minor

- **80% vs. 70% inconsistency**: The abstract (line 39) claims "up to 80%" per-layer pruning error reduction; the contributions section (line 44) says "up to 70%." The 80% figure is the peak for specific layer-matrix combinations in Figure 2; the paper itself states the average is 20–40% (line 196). Using the peak in the abstract overstates the representative result.

- **SparseGPT comparison omitted**: The paper excludes SparseGPT because it "involves a reconstruction step" (line 192). While this is technically accurate and the scope is stated, SparseGPT is described in the paper itself as "arguably the most popular approach." Even a single reference row in Table 1 would help contextualize the results for practitioners choosing among all available methods.

- **The α ablation (Table 2) is deferred to the appendix**: This table showing the effect of the α ratio on perplexity is critical to understanding the method's core design decision. Its placement in the appendix rather than the main text means readers must navigate to the supplement to evaluate the central trade-off.

### Trivial

None.

## Nice-to-Haves

- Include standard deviations or confidence intervals for Table 1, especially at 50% sparsity where margins are small.
- Discuss the scaling behavior of FW iterations (T=2000) relative to problem dimensions—for a method motivated by tractability, this would strengthen the paper.
- The theoretical bound in Lemma 1 grows as k + sqrt(2·d_in·d_out·k), which is very large for LLM layer dimensions (e.g., d_in × d_out = 4096 × 14336 for LLaMA-3-8B). A brief practical tightness discussion would be useful.

## Removed Points

These points are flagged to be removed, treat them with caution.

None—all weaknesses were verified against the paper text.

## Novel Insights

The paper's most novel intellectual contribution is the unification showing that Wanda and RIA are both single-weight greedy approximations to the same combinatorial mask selection objective (Eqs. 4–7), combined with the convex relaxation that accounts for weight interactions the greedy methods miss. The empirical finding that SparseFW dramatically benefits from more calibration data (Figure 3, right) while Wanda does not is a genuinely new observation with practical implications: it suggests that convex relaxation better exploits available calibration information, which matters in deployment settings where more data can be collected.

## Suggestions

- **Reframe the contribution honestly**: The abstract and introduction should clearly state that SparseFW improves existing methods by applying FW to a constrained subset of weights identified by a warmstart heuristic. This is still a valuable contribution—principled, theoretically grounded, and empirically effective—but it is a different (and more honest) story than "solving mask selection via convex relaxation."
- **Add a wall-clock timing table** comparing SparseFW, Wanda, and RIA for at least one model (e.g., LLaMA-3-8B) at all sparsity levels.
- **Move the α ablation (Table 2)** from the appendix to the main text.
- **Resolve the 80%/70% inconsistency** in the abstract vs. contributions.
- **Add at least a SparseGPT reference row** to Table 1 for context.

## Score and Decision

**Anchor comparison:**

| Anchor Paper | Avg Score | Decision | Round | Comparison |
|---|---|---|---|---|
| CVXQ (convex opt. quantization) | 3.0 | Reject | 1 | SparseFW has far better theory, evaluation, and practical grounding |
| Pruning Aggregation Parameters | 4.8 | Reject | 1 | SparseFW has stronger theory, cleaner formulation, broader models |
| FISTAPruner (LASSO convex pruning) | 5.25 | 2 | Very relevant—also uses convex opt for LLM pruning. SparseFW has cleaner formulation and theoretical guarantees, but FISTAPruner lacks the α dependence issue |
| OWL (non-uniform LLM pruning) | 6.0 | Reject | 1 | Similar pattern: strong at high sparsity, questionable at moderate. SparseFW has stronger theory |
| Cost of Scaling Down | 6.0 | Accept | 1 | Empirical study, different nature but similar score territory |
| How Sparse Can We Prune | 6.0 | Reject | 1 | Theoretical pruning paper; SparseFW is more practical and evaluated on more modern LLMs |
| Sparse Weight Averaging (SWAMP) | 6.4 | Accept | 3 | Both principled pruning methods; SparseFW targets a different (post-training) setting |
| TEAL (activation sparsity) | 7.5 | Accept | 2 | More practical (wall-clock speedups), but SparseFW has theoretical guarantees TEAL lacks |
| LLM-Streamline (layer pruning) | 7.5 | Accept | 1 | More novelty (layer replacement + new metric), but SparseFW has formal guarantees |
| SFPK (probabilistic pruning) | 7.5 | Accept | 2 | Both theoretical pruning methods; SFPK is more novel in formulation |
| EfficientSkip (sparse LLMs) | 2.5 | Reject | 1 | SparseFW much stronger on all dimensions |
| SparsitySolver (RL pruning) | 3.75 | Reject | 1 | SparseFW much stronger |

**Bracketing**: Round 1 places the paper between 5.5 and 7.0. FISTAPruner (5.25, rejected) is a close analog—both use convex optimization for LLM pruning—but SparseFW has cleaner theoretical grounding and a more elegant formulation, placing it above. OWL (6.0, rejected) has a similar profile of strong high-sparsity results but issues at moderate sparsity, and SparseFW has stronger theory. TEAL and LLM-Streamline (7.5, accepted) are more practical/novel, placing an upper bound. Narrowing to 5.5–6.5.

**Final score**: 6.0. SparseFW has genuine theoretical merit (convex relaxation with approximation guarantees, novel unification of existing methods) and solid empirical results at high sparsity. However, the α=0.9 dependence means the convex relaxation alone fails without the greedy inductive bias it claims to improve upon—a significant gap between framing and substance. The regressions at 50% sparsity and missing compute costs further limit the practical case. The paper is honest about limitations in its conclusion but not in its abstract or framing. This is a borderline paper with a clean intellectual contribution that is somewhat undercut by its practical constraints.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>