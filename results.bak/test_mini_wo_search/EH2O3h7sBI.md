Now I have all the evidence needed. Let me synthesize the final review.

## Summary

This paper combines prompt-tuning with gradient projection for continual learning. The authors derive orthogonal conditions on prompt gradients (x_t Δp^T=0, p_t Δp^T=0) from the self-attention mechanism and attempt to enforce them via SVD on a sum space s_t = x_t + p_t. They report consistent but small improvements across CIL and online CIL settings on several benchmarks.

## Strengths

1. **Novel and well-motivated combination of prompt-tuning with gradient projection.** The observation that prompt-tuning's instance-wise query mechanism can release the need for a task identifier (which limits standard gradient projection to TIL) is insightful and correctly identified (Section 2.2, lines 61–62). This frames a clear opportunity.

2. **Principled derivation of anti-forgetting conditions from the self-attention mechanism.** The paper derives Eq. (6) / (9) — x_t Δp^T = 0 and p_t Δp^T = 0 — from the condition that old and new prompt embeddings produce identical attention outputs (Section 3.1, Eqs. 2–9). *This part of the derivation is sound.* The connection to the attention mechanism goes beyond heuristic gradient projection and provides specific motivation for why prompt gradients, not just any parameter gradients, should be constrained.

3. **Systematic ablation isolating the contributions of prompt vs. key projection.** Table 4 and Figure 4 decompose the effect of projecting prompt gradients only, key gradients only, and both. On 10-Split-CIFAR100, projecting both reduces forgetting by 1.04% over L2P baseline, while prompt-only gives 0.99% and key-only gives 0.76%. This convincingly shows that the prompt projection is the main driver and that combining both is beneficial, directly supporting the design.

4. **Consistent improvements across settings and datasets.** While the gains are small, they are directionally consistent: PGP improves both accuracy and forgetting for L2P and DualPrompt across CIL (Table 1), online CIL (Table 3), and on four datasets (CIFAR-100, ImageNet-R, TinyImageNet, CUB200). The online CIL setting (single epoch per task) is particularly challenging, and the improvements hold there (e.g., L2P-PGP reduces forgetting by 2.00% on 20-Split-CIFAR100), suggesting the method is not just benefiting from more training.

5. **Training time and memory advantage over rehearsal without sacrificing performance.** Table 2 shows L2P-PGP uses 42 min vs. 70 min for L2P with rehearsal, uses no exemplar memory, and achieves better accuracy (+0.96%) and lower forgetting (−0.97%) on 10-Split-ImageNet-R. This is a practical benefit of the projection approach.

## Weaknesses

### Fatal
None.

### Major

1. **The sum-space derivation contains a logical error that undermines the claimed "rigorous theoretical guarantee."** In Section 3.1 (line 166), the paper states: "Thus we conduct SVD on s_t and therefore the obtained projection matrix V_{t,0} can realize s_t Δp^T = 0, which equals to x_t Δp^T = 0 and p_t Δp^T = 0." This is mathematically incorrect. The condition (x_t + p_t)v = 0 does **not** imply x_t v = 0 **and** p_t v = 0 individually — the nullspace of a sum is not the intersection of the nullspaces. For example, x_t v = 5 and p_t v = −5 satisfies the sum condition but violates both individual conditions. Therefore the method does **not** enforce the two required orthogonal conditions simultaneously. The approach of projecting gradients onto the nullspace of s_t is a reasonable heuristic, but the paper's central claim that it provides a "rigorous theoretical guarantee" (contributions, line 25; abstract, line 4) is unsupported by the derivation as written. This does not invalidate the method empirically, but it means the theoretical justification needs substantial correction or the theoretical claims need to be withdrawn.

2. **No statistical evidence for the reported improvements.** Across all experiments, improvements are small (0.15%–1.21% accuracy; 0.14%–2.00% forgetting). No confidence intervals, standard deviations, or multi-run results are reported anywhere. A grep for "standard deviation", "confidence interval", "multi.run", or "seed" returns zero matches. Given that many improvements are below 0.5%, the reader cannot assess whether PGP reliably outperforms baselines or if results are within noise. This is standard practice in CL and essential when effect sizes are this small.

### Minor

3. **Computational overhead of PGP itself is not isolated.** Table 2 compares L2P-PGP against L2P-R (with rehearsal), which is informative for the rehearsal trade-off but does not show the additional cost of the projection mechanism itself. The reader cannot tell how much slower L2P-PGP is vs. L2P without any modification, or what the SVD cost per task is. This makes it difficult to assess the efficiency contribution.

4. **Potential unfairness in DualPrompt baseline comparison.** The paper states (line 239) that it "train[s] DualPrompt with extra 15 epochs on CIFAR100 suggested by (Khan et al., 2023)." If the DualPrompt baseline results in Table 1 are quoted from the original paper (without extra epochs) while DualPrompt-PGP uses extra epochs, the comparison would be biased. The paper should clarify whether the baseline was re-run with the same extra epochs or report both configurations.

5. **No comparison against applying standard gradient projection (GPM-style) directly to prompts.** The paper motivates its specific sum-space design by deriving conditions from the attention mechanism, but does not compare against a simpler baseline: applying GPM's gradient projection on the prompt parameters using the input subspace directly. Such a comparison would isolate whether the sum-space design (and its theoretical flaw) matters in practice, or whether any projection on prompt gradients works.

### Trivial
None.

## Nice-to-Haves
- **Multiple runs with standard deviations** for all main results, especially given the small improvement magnitudes.
- **Ablation comparing PGP against standard GPM projection on prompt parameters** to validate the specific sum-space design choice.
- **Clarification on whether the DualPrompt (non-PGP) baseline was re-trained with the same 15 extra epochs** to ensure fair comparison.
- **Training time comparison of L2P vs. L2P-PGP** (without rehearsal) to isolate projection overhead.

## Removed Points
*These points were flagged by reviewers but are removed with justification:*
- **"No task-incremental results in main paper":** The abstract and contributions claim TIL validation. The appendix (stripped by parser from this extraction) likely contains those results. The paper's main text focuses on CIL and online CIL, which are the more challenging settings. Removing per rule about stripped appendix content.
- **"Derivation ignores softmax nonlinearity and value projection":** W_q, W_k, and W_v are frozen (stated in line 98). Focusing on QK^T is a standard simplification in attention analysis; the softmax is a monotonic function of the dot product and does not change the orthogonality reasoning qualitatively. This is not a meaningful gap.
- **"Second-order term ΔpΔp^T is dropped without justification":** The paper explicitly acknowledges this ("Here we ignore the high-order infinitesimal term of ΔpΔp^T", line 122). Dropping second-order terms in gradient-based derivations is standard practice. The critic's additional point about skew-symmetry (p_tΔp^T + Δp p_t^T = 0 not requiring p_tΔp^T = 0) is technically correct but describes a *sufficient* vs. *necessary* condition distinction — the paper imposes a sufficient condition, which is standard and not a flaw.
- **"Missing related works":** Cannot be included per hard rules — the reviewer has no external source to verify.
- **"Reproducibility details missing about SVD dimensionality":** The paper provides sufficient description for the approach (SVD on sum space, thresholding by epsilon). The exact dimensionality depends on the ViT configuration and prompt length, which are standard and can be inferred from the cited baselines.
- **"Weakness about comparing against L2P-R (rehearsal)":** This comparison is valid and informative for showing memory/time advantages. The critic's complaint is that it doesn't show overhead vs. L2P without projection. The weakness is merged into point #3 above as a separate minor issue, not about invalidity of the comparison itself.

## Novel Insights
The reviews do not surface any genuinely novel insight beyond the paper's own contributions. The core observation — that prompt-tuning's instance-wise query mechanism can serve as a natural task-identifier substitute for gradient projection — is the paper's own framing and is not challenged or refined by the reviews. The identified sum-space derivation flaw is a critique, not a new insight.

## Suggestions
1. **Fix the derivation or drop the "rigorous guarantee" claim.** Either correct the sum-space argument by (a) showing that the nullspace of the sum is a subspace of interest under some reasonable assumption (e.g., approximate orthogonality of x_t and p_t), or (b) perform two separate SVDs on x_t and p_t and intersect their nullspaces. If neither works, reframe the method as a heuristic inspired by sufficient conditions and remove the "rigorous theoretical guarantee" language.
2. **Report all main results as mean ± std over at least 3 random seeds.** The small improvements (<1%) cannot be evaluated without variance information.
3. **Add a training time comparison of L2P vs. L2P-PGP** (no rehearsal) to quantify the projection overhead.
4. **Clarify the DualPrompt baseline setup** — specify whether comparisons use DualPrompt trained with or without extra 15 epochs.
5. **Add a comparison against GPM-style projection on prompt parameters** to validate the sum-space design empirically.

## Score and Decision

The paper addresses a timely and interesting problem with a well-motivated idea (combining prompt-tuning with gradient projection). The empirical results, while small, are directionally consistent. However, two serious issues prevent acceptance in the current form: (a) the core theoretical derivation contains an error — the sum-space approach does not enforce the two required orthogonal conditions simultaneously, meaning the claimed "rigorous theoretical guarantee" is unsupported; and (b) the reported improvements are small and presented without any statistical evidence (no variance, no multi-run). These are addressable with a major revision that either corrects the theory or drops the guarantee claims and adds rigorous multi-run experiments.

**Score**: 5.0  
**Decision**: Reject

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>