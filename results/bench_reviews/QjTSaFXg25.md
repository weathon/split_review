Now I have all the evidence I need. Let me synthesize the final review.

## Summary

This paper studies why the reparameterization trick in prefix-tuning works, arguing that it induces a *shared structure* between key and value vectors (both produced from the same underlying parameters via an MLP). The paper connects prefix-tuning to mixture-of-experts models, proves convergence rates for prompt estimation with and without shared structure, and validates empirically across vision and language tasks.

## Strengths

- **Formal connection between prefix-tuning and MoE models (Section 2.2).** The paper builds on Le et al. (2024) to give a clean, explicit mapping from attention heads to MoE models, where prefix keys serve as score-function parameters and prefix values as expert outputs. This framing provides a principled language for the theoretical analysis and is a genuine intellectual contribution.

- **Consistent and substantial empirical gains across 24 visual tasks and 3 language tasks.** Deep-share (prefix-tuning with reparameterization) outperforms No-share (without reparameterization) by large margins on nearly every dataset — e.g., +16.8% on Stanford Cars, +7.6% on XSUM ROUGE-1. The pattern is consistent across shallow and deep variants, two domains, and multiple architectures (ViT, GPT-2, BART).

- **Simple-share ablation partially isolates the effect of shared structure.** The paper goes beyond the confounded Deep-share vs. No-share comparison by including a Simple-share configuration (identity σ₁=σ₂, i.e., K=V with no MLP). On FGVC benchmarks, Simple-share also substantially outperforms No-share, providing some evidence that shared structure itself (not just the MLP) drives gains.

- **Technical rigor in the simplified theoretical setting.** The convergence analysis using Voronoi losses is technically correct within the assumed regression-MoE framework. Theorems 2 and 3 establish parametric-rate convergence for shared-structure settings under standard MoE analysis assumptions.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical comparison does not rigorously establish the claimed sample-efficiency improvement.** Theorem 1 gives a *lower bound* of order n^{-1/2} on a loss D_{1,r} that separately measures key and value errors, while Theorem 2 gives an *upper bound* of order √(log n/n) on a *different* loss D₂ that measures only shared-prompt errors. The core claim — that shared structure yields faster convergence — rests on comparing a lower bound for one loss to an upper bound for another, incomparable loss. Moreover, the non-shared model has twice as many free parameters (L keys + L values) as the shared model (L prompts), and this parameter-count confound is neither controlled for nor discussed. A proper comparison would require either (a) a matching upper bound for the shared case on the same loss D_{1,r}, or (b) a matching lower bound for the non-shared case on D₂, with parameter counts equated.

2. **The main experimental comparison (Deep-share vs. No-share) confounds reparameterization presence with shared structure.** Deep-share uses an MLP to produce both K and V from shared parameters; No-share learns K and V independently with no MLP. These differ in two ways simultaneously — (i) whether an MLP is used and (ii) whether K and V share parameters. The paper's central claim is that *shared structure* matters, but the headline numbers cannot disentangle these factors. The Simple-share ablation (Figure 2) partially addresses this by comparing identity-based sharing to no sharing, both without MLPs, but it is shown only on FGVC datasets, not on VTAB-1K or language tasks. The main tables (Tables 1 and 2), which carry the weight of the paper's empirical claims, present only the confounded comparison.

3. **The extreme theoretical simplifications create a credibility gap.** The analysis reduces to one attention head, one query position, i.i.d. data, i.i.d. data, and known pre-trained projection matrices B and C. Real prefix-tuning involves multiple heads, autoregressive sequences, unknown pre-trained weights, and non-linearities (layer norm, residual connections) that are entirely abstracted away. The paper does not discuss how the theoretical rates might transfer to the full architecture, nor does it validate the MoE-identity assumption against empirical counterexamples. While simplifications are standard, the gap here is wide and unbridged.

### Minor

4. **No standard deviations or significance tests reported.** The paper reports only "average accuracy over five runs" without standard deviations in any table or figure. This makes it impossible to assess the variability or statistical significance of the reported gains. Given that some gaps are modest (e.g., 69.9 vs 68.0 BLEU on E2E), error bars would substantially strengthen the evidence.

5. **Theory-experiment disconnect on activation functions.** Assumptions A.1 and A.2 (required for Theorem 3) are verified for tanh, but the paper's prefix-tuning MLP almost certainly uses GELU or ReLU, not tanh. Whether GELU/ReLU satisfy these assumptions is not discussed.

6. **Simple-share is under-exploited.** Simple-share (identity mapping, K=V) is the cleanest test of the paper's central hypothesis but appears only in one figure (Figure 2, FGVC). Extending it to VTAB-1K and language tasks would provide much stronger evidence for the shared-structure claim.

### Trivial
None.

## Nice-to-Haves

- A fully controlled experiment comparing: (i) shared K/V from a single MLP, (ii) separate K/V from separate MLPs (same architecture, same parameter count), (iii) no MLP with shared K/V (Simple-share), (iv) no MLP without sharing (No-share). This would cleanly separate sharing from MLP presence.
- Parameter-matched baselines (e.g., halving prompts for the non-shared case to match parameter counts).
- Comparison with other PEFT methods (Adapter, LoRA, VPT) if those results were in the appendix.
- Visualization of learned prompt parameters (PCA/t-SNE of shared vs. non-shared prompts) to illustrate the structural relationship.
- Synthetic experiments matching the theoretical regression setup to verify predicted rates.

## Removed Points

- "Theorems lack proofs (appendix stripped)." → Removed per hard rule: appendix content was stripped by the parser.
- "No comparison to Adapter/LoRA/VPT." → Removed per hard rule: these results likely reside in the appendix.
- "The prompt-tuning observation is trivial." → This is a subjective opinion rather than a verifiable weakness; the paper does not claim this as a major contribution.
- "The lower bound n^{-1/2} cannot imply 1/log n rates." → Re-checked: "slower than any polynomial" does indeed mean rates could be logarithmic. The paper hedges with "could be," which is defensible.
- "Simple-share still confounds reparameterization with sharing." → Factually incorrect: Simple-share uses identity mapping (no MLP), so vs. No-share (also no MLP), only sharing differs. This comparison does isolate sharing.

## Novel Insights

The reviews surface a subtle but important point that the paper itself does not address: the theoretical comparison is structurally asymmetric (lower bound on one loss vs. upper bound on another), and the experimental comparison is structurally confounded (MLP plus sharing vs. neither). These are not independent criticisms — they point to the same underlying issue: the paper has not cleanly separated the effect of *shared structure* from other factors (number of parameters, presence of reparameterization) in either the theory or the experiments. The Simple-share ablation is the right idea but is deployed too narrowly to carry the argument. A stronger version of this paper would need to either (a) prove a shared-structure upper bound on the *same* loss function used for the non-shared lower bound, or (b) provide a proper controlled experiment that varies only the sharing dimension while holding everything else fixed.

## Suggestions

1. Add a fully controlled experiment: a "separate-MLP" baseline where K and V each have their own MLP with different learned parameters, matched in total parameter count to Deep-share. This isolates shared structure from MLP effectiveness.
2. Prove a matching upper bound for the shared case on the same Voronoi loss D_{1,r} (or prove a matching lower bound for non-shared on D₂) so that the theoretical comparison is apples-to-apples.
3. Report standard deviations for all experimental results and run significance tests for key comparisons.
4. Extend the Simple-share ablation to all language and VTAB-1K tasks.
5. Bridge the theory-experiment gap by running synthetic experiments matching the regression framework of Eq. 10, or explicitly discuss which aspects of the theory are expected to transfer and why.

## Score and Decision

## Score and Decision

**Anchors considered (all returned by calibration_search):**

| Path | Avg Score | Comparison |
|---|---|---|
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/4xWQS2z77v.md | 8.00 | Deep rigorous theory with clear results; much stronger than this paper |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/AoraWUmpLU.md | 8.00 | Tight theory-experiment connection; substantially stronger |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/9XETcRsufZ.md | 7.00 | Strong theory+experiments with clear comparative claims; stronger |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/Pu3c0209cx.md | 7.00 | Clean theoretical results with practical insight; stronger |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/P98KMCf60l.md | 4.75 | Similar mix of theory+experiments with gaps; comparable in overall quality |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/8aKygnbEFX.md | 4.00 | Weaker theory, more trivial contributions; this paper is stronger |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/VpeAsLmcvg.md | 3.75 | Unconvincing central assumption; this paper's theory is more sound |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/vAoyZWyDEc.md | 2.50 | Fundamentally flawed logic; this paper is substantially better |

The paper has genuine value — the MoE framing of prefix-tuning is clean, the empirical gains are consistent, and the theoretical analysis is technically competent within its simplifications. However, the central claim (that **shared structure** is the causal driver of improved performance) is not adequately supported: the theoretical comparison is between incomparable loss functions, and the headline experiments confound two variables. Relative to the anchors, the paper sits around the 4.5–5.0 range — offering real contributions but with significant gaps in the core argument that preclude acceptance in current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>