## Summary

This paper proposes SparseFW, a layer-wise LLM pruning method that relaxes the binary mask constraint to its convex hull and solves the resulting convex program with the Frank-Wolfe (FW) algorithm. The core idea is to account for weight interactions that greedy methods (Wanda, RIA) ignore. The authors show that SparseFW reduces per-layer pruning error by up to 80% (Figure 2) and produces consistent zero-shot accuracy gains across five LLM families (LLaMA-3, Gemma-2, Yi-1.5, DeepSeek, Qwen2.5) at 50%, 60%, and 2:4 sparsity, alongside mostly-improved perplexity.

## Strengths

1. **Principled formulation with weight interaction awareness.** Unlike Wanda and RIA, which prune weights independently based on saliency scores, SparseFW relaxes the combinatorial mask constraint to its convex hull and optimizes the resulting quadratic program with FW. This explicitly captures second-order interactions between weights. The per-layer pruning error reduction of up to 80% (Figure 2) directly validates that accounting for interactions produces better local masks.

2. **Consistent zero-shot accuracy improvements.** Across all 18 model×sparsity configurations in Table 1 (5 models × 3 sparsity regimes, each compared against its warm-start baseline), SparseFW delivers higher zero-shot accuracy than the corresponding baseline in the large majority of cases. This demonstrates that the improved local masks reliably translate to better downstream task performance — a non-trivial result given that local loss reduction does not always transfer globally.

3. **Favorable scaling with calibration data.** Figure 3 shows that SparseFW continues to benefit from additional calibration samples (perplexity dropping from ~22→19.5 when going from 64→512 samples), whereas Wanda's performance plateaus. This is a genuine advantage of the optimization-based approach over heuristic methods.

4. **Computational efficiency via precomputation.** By precomputing $G = XX^\top$ and $H = WG$, the per-iteration cost of FW becomes independent of the calibration sequence length and sample count. The LMO is a top-$k$ selection, and the algorithm is projection-free.

5. **Honest treatment of limitations.** The paper transparently reports that full SparseFW ($\alpha=0.0$) consistently underperforms baselines, and that fixing 90% of high-saliency weights from the warm-start is necessary for good results. It also acknowledges the local-global objective mismatch. This candor is commendable.

## Weaknesses

### Major

1. **Central narrative contradicted by the method's actual behavior.** The title *"Don't be greedy, just relax!"* and the abstract's framing present convex relaxation + FW as a superior, principled *alternative* to greedy heuristics. The experiments directly refute this: SparseFW with $\alpha=0.0$ (full FW, no warm-start fixed weights) *"consistently yields worse results than the baselines."* The method only works when 90% of the mask is frozen according to the **greedy baseline's** decisions ($\alpha=0.9$). This means SparseFW is not a replacement for greedy methods but a refinement layer operating on the remaining 10% of decisions. The paper's own theoretical motivation and headline claim are at odds with its empirical findings, and this is acknowledged only as a caveat rather than treated as the central fact about the method.

2. **Inconsistent and often marginal perplexity improvements.** While zero-shot accuracy improves consistently, the perplexity results are mixed. At 50% sparsity, SparseFW underperforms the best baseline in 2 of 6 model comparisons (DeepSeek: 7.89 vs 7.79; LLaMA-3: 9.95 vs 9.88). Even where SparseFW wins, the gains are typically 0.1–0.5 PPL — modest for a method that requires ~2000 FW iterations per layer. At 2:4 sparsity, the method underperforms RIA on Qwen2.5-14B (11.20 vs 10.98). The strongest claim that can be made from the perplexity data is "on par or better in most settings," not "strong empirical performance."

### Minor

3. **Missing statistical precision.** Table 1 omits standard deviations ("for legibility"). Given that many comparisons are within 0.1–0.5 PPL, and the authors run multiple random seeds for Figure 3, the absence of any variance estimate in the main results table makes it impossible to assess whether the claimed improvements are statistically robust.

4. **No comparison to SparseGPT.** The paper restricts comparisons to Wanda and RIA because SparseGPT involves a reconstruction step. This is a defensible scope choice — the paper's contribution is about mask selection — but it limits practical significance. A practitioner evaluating which pruning method to use cares about final model quality regardless of whether the method includes reconstruction. Showing that SparseFW masks, when combined with the same reconstruction procedure as SparseGPT, yield better final models would directly demonstrate practical advantage. Without this, the paper's central claim of "outperforming state-of-the-art" methods is only with respect to a subset of baselines.

5. **Theoretical guarantee is too loose to be informative at scale.** Lemma 1's bound contains a $\sqrt{2 d_{in} d_{out} k}$ term, which at LLM scale (e.g., $d_{in}=d_{out}=4096$) dominates the bound, making it vacuous as a numerical guarantee. The paper uses it to qualitatively explain Figure 4, which is fine, but it does not provide meaningful control over solution quality as claimed. The "strong theoretical justification" advertised in the abstract is overstated.

6. **Algorithm 1 omits the critical $\alpha$ parameter.** The algorithm box presents SparseFW as optimizing the full mask, but all experiments rely on fixing a fraction $\alpha=0.9$ of weights from the warm-start baseline. This detail is only mentioned in the text and appendix. A reader skimming the paper would get a misleading picture of what the method actually does.

### Trivial

- "up to 70%" (abstract/contributions) vs "up to 80%" (elsewhere for Figure 2) — minor inconsistency.

## Nice-to-Haves

- Adding a comparison to SparseGPT (or SparseFW + reconstruction vs SparseGPT + reconstruction) would substantially strengthen the practical claims.
- Analyzing the 10% of weights where SparseFW changes decisions relative to the warm-start mask — what characterizes these weights? — would provide mechanistic insight beyond the empirical results.
- Reporting Table 1 with error bars (or at least showing the min-max range as in Figure 3) would address the statistical precision concern.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **"Strategic omission of SparseGPT" as a fatal flaw (Harsh Critic #2):** The paper explicitly scopes its contribution to mask selection and justifies excluding methods with reconstruction steps. While a comparison would strengthen the paper, this is a reasonable scope choice, not a fatal omission. Demoted to Minor.

- **"The theory is presented as a key advantage but is vacuous" (Harsh Critic #3, strong version):** The bound is indeed loose at scale, but the paper uses it to explain empirical behavior (Figure 4), and any theoretical guarantee is more than greedy methods provide. The claim that the theory is presented as a "key advantage" is accurate but the severity was overstated. Demoted to Minor.

- **"Algorithm 1 omits the fixing detail" (Harsh Critic, Section 2.3 note):** The paper explicitly flags this ("we did not detail in Algorithm 1 for the sake of simplicity, exact details are in the appendix"). It's a presentation choice, not a hidden detail. Still worth noting as a Minor weakness since the omission is significant for understanding the method.

- **Various formatting/style nitpicks:** Removed per policy.

- **"The paper shows cases where SparseFW underperforms" (Harsh Critic, Section 3 note):** This is factually correct but the paper acknowledges this ("more consistent improvements at higher sparsity"). It's captured in weakness #2 (Major).

## Novel Insights

The key novel insight from the reviews is the framing dissonance: the paper's most honest paragraph is in the conclusion (local-global mismatch, inductive biases still necessary), yet the title and contribution list tell a different story. The actual contribution — using convex optimization to *refine* the tail of a greedy mask — is a reasonable incremental contribution, but the paper presents itself as offering a *replacement* for greedy methods. This gap between contribution and packaging is the single issue that most needs addressing. Also notable is the finding that increasing calibration data helps SparseFW but not Wanda (Figure 3), which suggests that optimization-based methods can extract more signal from data — this is a genuinely interesting empirical finding worth further investigation.

## Suggestions

1. **Reframe the paper honestly.** The title, abstract, and introduction should position SparseFW as a *refinement* method that improves upon existing masks (e.g., "Refining LLM Pruning Masks via Frank-Wolfe Optimization"), rather than a replacement for greedy heuristics. The method's reliance on fixing the bulk of the mask per a greedy baseline should be presented as a core design feature, not a caveat.
2. **Add SparseGPT to the comparison** or, at minimum, show that SparseFW masks + reconstruction outperform SparseGPT. This would directly establish practical relevance.
3. **Include error bars** in Table 1 for the main comparisons.
4. **Make the $\alpha$ parameter explicit** in Algorithm 1 and the main exposition.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Source | Comparison |
|--------|-----------|--------|------------|
| FISTAPruner (BINwUtUGuq) | 5.25 | round1-topic-mid, round2 | Similar convex-optimization LLM pruning approach; stronger reported results but also rejected; SparseFW is more novel in formulation but weaker in results |
| OWL (pOBvr1PxFd) | 6.00 | round1-weakness-SparseGPT | Polarizing; very strong PPL gains at high sparsity but criticized for impractical sparsity focus; much stronger empirical results than SparseFW |
| You Only Prune Once (5RZoYIT3u6) | 6.00 | round2 | Accepted calibration-free pruning; similar score consensus (all 6s); cleaner story |
| Reassessing Layer Pruning (EjHtQlKEzV) | 4.50 | round2 | Empirical study, limited novelty; SparseFW has a stronger methods contribution but also has a narrative problem |
| MoreauPruner (Y0qmwm6tgy) | 4.80 | round1-topic-mid | Structured pruning; similar rejection profile |

**Round-1 Bracket:** I initially bracketed this paper between 4.0 and 6.0 based on comparison with FISTAPruner (5.25, similar convex-optimization pruning approach) and the weakness-anchored queries. FISTAPruner sat at the upper end of the bracket with stronger reported results but similar structural issues (missing SparseGPT comparison, modest improvements). The weakness queries confirmed that papers with narrative-claim vs evidence gaps and missing SparseGPT comparisons tend to score in the 4–5 range.

**Round-2 Narrowing:** I pulled three additional anchor groups inside the bracket. Reassessing Layer Pruning (4.50) — also rejected, with comparable scores to what SparseFW would likely receive given its narrative issue — provided a lower anchor. You Only Prune Once (6.00, accepted) provided an upper anchor: that paper had a clean, honest narrative and stronger empirical evidence. SparseFW sits below this anchor due to the narrative disjunction and more modest results. Comparing directly to FISTAPruner (5.25), SparseFW is weaker on empirical margins but more novel in formulation and more transparent about limitations. I place it slightly below FISTAPruner, at 4.5.

The low-band anchors (3.0–4.5) typically failed on: (a) narrative/claim mismatch, (b) modest improvements not commensurate with compute, (c) missing comparisons that leave practical significance unclear. The paper under review shares all three of these failure modes. The method has genuine merit — the zero-shot results are real, and the formulation is principled — but the gap between what is claimed and what is shown, combined with the modest scale of improvements, prevents acceptance.

Final score: 4.5 (Weak Reject).

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>