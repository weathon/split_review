Now I have all the anchors I need. Let me synthesize the final review.

**Bracket from Round 1:** Between 3.5 and 6.0.
**Round 2 narrowing:** After comparing to SparseSwaps (5.0, Reject), Thanos (4.5, Reject), HyperPrune (6.0, Accept), KDP (6.5, Accept), and the Layer Pruning paper (5.0, Accept), I narrow the bracket to 4.0–5.5.

**Final score: 4.5.** The paper is most comparable to SparseSwaps (5.0, Reject) but has an additional data integrity concern (suspicious duplicate accuracy values) that pulls it slightly below that anchor. The paper is weaker than HyperPrune (6.0, Accept Poster) and KDP (6.5, Accept Poster). It is comparable to the Layer Pruning paper (5.0) in terms of overall quality but with different strengths/weaknesses.

Now let me write the review.

---

Let me carefully verify each weakness from the harsh critic against the paper, and apply the filtering rules.

**Weakness 1: Theory-practice gap.** 
- The paper states: "Constraining Sparse Frank-Wolfe (SparseFW) by fixing a fraction of very high-saliency weights (e.g., those with highest Wanda scores) as unprunable consistently improves performance."
- "Setting α = 0.0 (full FW without any fixed weights) consistently yields worse results than the baselines."
- Algorithm 1 does not show the fixing step, though the paper says "exact details are in the appendix."
- Lemma 1 provides a bound for the FW solution after T iterations and thresholding.
- The theory does not account for the fixing heuristic.
- This is a real and substantive weakness. **KEEP as Major.**

**Weakness 2: Missing SparseGPT comparison.**
- The paper explicitly scopes this out: "We hence do not compare directly to methods that involve a reconstruction step, such as SparseGPT."
- This is a scope choice. The paper frames itself as a mask-selection method.
- However, the critic raises a valid concern - the practical community cares about pruned model quality regardless of subproblems.
- This is a soft criticism. I'll keep it but weaken it. **WEAKEN to Minor.**

**Weakness 3: Results weaker than claimed + suspicious accuracy values.**
- At 50%, DeepSeek-7B: Wanda 7.79 vs SparseFW(Wanda) 7.89 - Wanda is indeed better. But the paper says "generally performs on par with or better than the baselines" which is accurate (2 models better, 2 worse, 2 tied).
- The accuracy duplication at 60% is verifiable from the paper text: lines 235-236 show identical values. **KEEP as Major.**
- No variance/confidence intervals. The paper says "We omit standard deviations for legibility." **KEEP as Minor.**

**Weakness 4: Core motivation contradicted by actual method.**
- The paper argues FW accounts for weight interactions, but then fixes 90% of weights.
- The paper acknowledges this: "we noticed that while FW often substantially reduces pruning error relative to baselines like Wanda, it can still produce worse final perplexity, likely due to a mismatch between local and global objectives."
- And: "Without fixing part of the mask, it tends to prune weights crucial for overall performance."
- The paper is transparent about this limitation. The critic's point is somewhat valid but the paper addresses it. **WEAKEN to Minor.**

**Up to 80% vs 70% inconsistency:**
- Abstract says "up to 80%"
- Contributions say "up to 70%"
- Figure 2 shows up to 80%
- This is a minor inconsistency. **KEEP as Trivial.**

**Algorithm 1 not showing weight-fixing:**
- The paper says "exact details are in the appendix" and the appendix was stripped. Algorithm 1 shows the basic FW procedure.
- This is minor. **KEEP as Trivial.**

**Theoretical bound not tight/useful:**
- The bound has O(λ_max(Q)(k/T + k + √(d_in d_out k))) terms.
- The additive terms in k and √(d_in d_out k) are potentially large.
- The paper presents this as an informal lemma and defers to appendix for formal treatment.
- This is somewhat valid but the paper is honest that it's informal. **WEAKEN to Minor.**

**Strength 1 (80% reduction):** This is verifiable from Figure 2. **KEEP.**
**Strength 2 (consistent gains):** The gains at 60% and 2:4 are generally solid. At 50% they're mixed. **KEEP but qualify.**
**Strength 3 (theoretical guarantee):** The theory has a gap with practice. **KEEP but note caveat.**
**Strength 4 (flexible sparsity):** Support for unstructured, per-row, n:m via adaptable LMO. **KEEP.**
**Strength 5 (memory-efficient):** Precomputation of G and H. **KEEP.**
**Strength 6 (mitigation of local-global mismatch):** Fixing heuristic identified through ablation. **KEEP.**

Now let me produce the final review.## Summary

This paper proposes SparseFW, a layer-wise LLM pruning method that relaxes the combinatorial binary-mask selection problem into a convex program over the convex hull of binary masks, solved via the Frank-Wolfe (FW) algorithm. The method warm-starts from Wanda or RIA masks, fixes 90% of high-saliency weights as unprunable, and optimizes the remaining mask entries. Experiments on five modern GPT architectures (LLaMA-3, Qwen2.5, Gemma-2, Yi-1.5, DeepSeek) at 50%, 60%, and 2:4 sparsity show perplexity and zero-shot accuracy improvements over baselines, particularly at higher sparsity levels. A theoretical guarantee (Lemma 1) connects the relaxed solution after thresholding to an approximate solution of the original combinatorial problem.

## Strengths

- **Principled relaxation of a combinatorial problem.** The paper correctly identifies that the mask selection objective is a hard quadratic binary optimization problem and proposes a convex relaxation over the convex hull of binary masks. This is a clean framing that distinguishes SparseFW from greedy heuristics (Wanda, RIA) and is accompanied by a theoretical approximation guarantee (Lemma 1) that bounds suboptimality after solving the relaxation and thresholding — a property that greedy methods lack.

- **Memory-efficient implementation via precomputed buffers.** Section 2.3 precomputes \( G = XX^\top \) (dimensions \( d_{in} \times d_{in} \)) and \( H = WG \), making the per-iteration gradient computation independent of sequence length and sample count. The gradient then requires only elementwise multiplications and one matrix multiplication (\( (W \odot M_t)G \)). This is a concrete engineering contribution that makes FW iterations feasible at LLM scale.

- **Consistent gains at high sparsity across multiple model families.** At 60% unstructured sparsity and 2:4 semi-structured sparsity, SparseFW improves perplexity and accuracy over both Wanda and RIA warmstarts across all five tested model families. For example, on LLaMA-3-8B at 60% sparsity, perplexity improves from 21.53 (Wanda) to 17.97 (SparseFW+Wanda) and accuracy from 48.08% to 51.92%.

- **Flexible sparsity patterns via adaptable LMO.** Section 2.2 shows that the Linear Minimization Oracle can be modified to support unstructured, per-row, or \( n:m \) semi-structured sparsity, demonstrated empirically with 2:4 results. This versatility is a practical advantage over methods targeting a single pattern.

- **Honest discussion of the local-global objective mismatch.** The paper transparently acknowledges that vanilla FW reduces per-layer reconstruction error but does not reliably improve perplexity, and that fixing 90% of high-saliency weights is necessary. This candor is uncommon and helps readers understand where the true difficulty lies.

## Weaknesses

### Fatal
None.

### Major

- **Suspicious duplicate accuracy values at 60% sparsity.** In Table 1, the accuracy column for 60% sparsity shows *identical* values for Wanda and RIA across all six model variants (Gemma-2 9B: 63.19/63.19, Yi-1.5 9B: 53.7/53.7, DeepSeek-7B: 50.51/50.51, Qwen2.5 7B: 59.44/59.44, Qwen2.5 14B: 63.58/63.58, LLaMA-3 8B: 48.08/48.08). This is extremely unlikely to reflect genuine results — at other sparsity levels (50%, 2:4) the Wanda and RIA accuracy values consistently differ, and the perplexity values at 60% also differ. The paper must explain and correct this before the data can be trusted.

- **Theory-practice gap undermines the claimed theoretical justification.** Lemma 1 provides an approximation guarantee for solving the relaxed problem *from scratch* and thresholding. However, the practical algorithm depends critically on two heuristics not covered by the theory: (a) warm-starting from Wanda or RIA masks, and (b) fixing 90% of weights as unprunable based on Wanda saliency. The paper explicitly states that "full FW without any fixed weights consistently yields worse results than the baselines" (Section 2.3). This means the theoretical guarantee does not explain why SparseFW works in practice — the success stems from the heuristics, not the convergence properties of FW. The claim of "strong theoretical justification" in the abstract is therefore misleading.

### Minor

- **No variance or confidence intervals reported.** The paper states "We omit standard deviations for legibility" (Table 1 caption), but many entries differ by less than 0.1 perplexity (e.g., DeepSeek-7B at 50%: Wanda 7.79 vs SparseFW(Wanda) 7.89). Without variance estimates, it is impossible to assess whether the observed differences are statistically meaningful or simply noise. Reporting at least min-max ranges (as done in Figure 3) for the main results would substantially strengthen the empirical claims.

- **Results at 50% sparsity are mixed.** At 50% sparsity, SparseFW(Wanda) underperforms Wanda on DeepSeek-7B (7.89 vs 7.79 perplexity) and LLaMA-3-8B (10.21 vs 10.09), and ties on Yi-1.5 (6.58 vs 6.58). The paper's claim of "generally performs on par with or better" is technically accurate but the gains are concentrated at higher sparsity — the paper would benefit from a more precise characterization of where SparseFW helps and where it does not.

- **No wall-clock time or computational cost comparison.** The paper acknowledges SparseFW is "clearly more compute-intensive than Wanda and RIA" but provides no runtime numbers. At 2000 iterations per layer across ~100 layers, the total cost is substantial. Without at least a rough timing comparison (e.g., "SparseFW takes X minutes on an A100 vs Y seconds for Wanda"), readers cannot evaluate the practical trade-off between the improved performance and the added compute.

- **The local–global objective mismatch is acknowledged but not resolved.** The paper identifies that FW optimization of the local per-layer objective does not reliably improve perplexity, necessitating the weight-fixing heuristic. This means the central motivation — that accounting for weight interactions via FW should improve pruning — is contradicted by the actual algorithm, which must *prevent* FW from optimizing over most weights to succeed. The paper's conclusion acknowledges this but does not analyze why this happens or how the fixing heuristic interacts with the relaxation.

- **Inconsistent claim in abstract vs. introduction.** The abstract claims "up to 80% reduction in per-layer pruning error," the contribution list says "up to 70%," and Figure 2 shows up to 80%. This numeric inconsistency, while minor, suggests imprecise writing.

### Trivial

- The gradient formula in Section 2.2 could be explicitly derived from the objective for completeness.
- Algorithm 1 does not show the weight-fixing step (deferred to appendix); the main text should at minimum annotate where the fixing occurs relative to the loop.

## Nice-to-Haves

- A comparison to SparseGPT at the same sparsity levels, even if the paper's focus is mask selection. The community standard for evaluating pruned LLMs compares *final model quality*, not subproblem quality. Including SparseGPT (with a clear caveat that it also reconstructs weights) would make the evaluation more actionable for practitioners.

- An ablation separating the contributions of warm-start vs. weight-fixing vs. FW optimization (e.g., (a) FW from random, (b) FW with warm-start but no fixing, (c) FW with both, (d) fixing only). This would isolate where the gains come from and could partially address the theory-practice gap.

- A discussion of the practical utility of the theoretical bound — e.g., computing \(\lambda_{\max}(Q)\) for realistic layer dimensions and evaluating whether the bound is non-vacuous.

## Removed Points

- **"Results at 50% sparsity contradict 'consistently outperforms'"**: The paper says "generally performs on par with or better" (Section 3), not "consistently outperforms." The reviewer mischaracterized the claim. The actual claim is accurate.
- **"Warm-start not in Algorithm 1"**: Algorithm 1 takes `warm-start mask M_0` as input (line "Require"). The weight-fixing is indeed deferred to the appendix but the warm-start is present. Partially inaccurate.
- **"2000 iteration choice not justified by Figure 3"**: Figure 3 (left) shows perplexity flattening after ~2000 iterations. The choice is justified.
- **"Theoretical bound not useful" (as a major weakness)**: The bound is acknowledged as informal (Lemma 1, Informal) with full details deferred. Large additive terms are common in such bounds. This is a reasonable limitation of the theory rather than a flaw. **Kept as a minor note above**.
- **"Core motivation contradicted by actual method"** (as a fatal weakness): The paper fully acknowledges this limitation in Section 5. The authors are transparent about the local-global mismatch. A weakness persists but at the minor level, as reflected above.
- **"Missing SparseGPT comparison"** (as a critical omission): The paper explicitly scopes itself as a mask-selection method and explains why SparseGPT is excluded. This is a defensible choice. It is moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the duplicate accuracy values at 60% sparsity.** This is the most urgent action. If the values are correct, explain the remarkable coincidence. If they are an error, provide the correct numbers.
2. **Add variance estimates** (standard deviations over 3-5 calibration subsets) to the main results table.
3. **Reframe the theoretical guarantee** to explicitly acknowledge that it applies to the relaxation and rounding, not to the practical algorithm with weight-fixing. Alternatively, run FW from random initialization without weight-fixing and show it still outperforms baselines (even if gains are smaller).
4. **Report wall-clock pruning time** per model on a single GPU to contextualize the compute-accuracy trade-off.
5. **Ablate \(\alpha\) (fixing ratio)** in the main paper, not only in the appendix. Show the perplexity curve as \(\alpha\) varies from 0 to 1 to demonstrate the sensitivity of the heuristic.

---

### Anchors Used for Calibration

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| oj0OhhqAGN.md (SparseSwaps) | 5.0 | 1,2 | Most similar paper — same problem (mask selection), similar experimental setup, similar weaknesses. Current paper has a more principled optimization framework but a data integrity concern SparseSwaps lacks. |
| 04Tfwy3LLC.md (Layer Pruning) | 5.0 | 1,3 | Different pruning type (depth vs. weight). Comparable overall quality but cleaner experiments. |
| 262LUKGdQn.md (KDP) | 6.5 | 1,3 | Stronger theory and cleaner experiments. Current paper is weaker. |
| lqjQs2lVNm.md (HyperPrune) | 6.0 | 2 | Focused on n:m sparsity with hypernetwork. Better experimental coverage. Current paper is weaker. |
| 4TFfiG17ec.md (Thanos) | 4.5 | 3 | Block-wise pruning. Similar scope. Current paper has a more novel approach but similar-level weaknesses. |
| 2uxuiykvA4.md (RMM) | 3.6 | 1 | Dynamic pruning, rejected. Current paper is substantially stronger. |

**Round 1 bracket:** (3.5, 6.0)  
**Round 2 narrowing:** Between 4.0 and 5.5 after comparing to SparseSwaps (5.0), Layer Pruning (5.0), Thanos (4.5), and HyperPrune (6.0).  
**Final score positioning:** Below SparseSwaps (5.0, Reject) due to the data integrity concern, above Thanos (4.5, Reject) due to a more principled approach and novel methodology. Closest comparator is SparseSwaps; the current paper is slightly weaker.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>