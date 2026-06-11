Good, I now have solid calibration. Let me write the final review.

## Summary

This paper studies the effect of the L0 hyperparameter (average number of active features per token) in Sparse Autoencoders (SAEs) on feature quality. Using toy models with known ground-truth features, it demonstrates that when L0 is set too low, SAEs "cheat" by mixing correlated features to improve reconstruction — achieving better variance explained than a ground-truth SAE with correct, monosemantic latents. This directly undercuts the standard use of sparsity-reconstruction tradeoff plots as SAE evaluation tools. The paper proposes a diagnostic metric, decoder pairwise cosine similarity (c_dec), that identifies the correct L0 in toy models. LLM experiments on Gemma-2-2b and Llama-3.2-1b show qualitative alignment between the c_dec elbow and peak sparse probing performance.

## Strengths

1. **Clean causal demonstration that sparsity-reconstruction tradeoff plots are fundamentally misleading.** Figure 4 shows that at L0 below the true value, a trained SAE with corrupted, polysemantic latents achieves *better* variance explained than the ground-truth SAE with correct monosemantic latents. This is a direct counterexample to the standard evaluation assumption in the field (Cunningham et al., Gao et al., Rajamanoharan et al.).

2. **Isolation of the incentive mechanism.** Initializing a low-L0 SAE to the ground-truth solution (Section 3.1) and showing that gradient pressure drives it away from correct features rules out the local-minima hypothesis. The head-to-head MSE comparison (2.73 vs 4.88, Section 3.3) quantifies the incentive: the incorrect SAE scores nearly 2× better reconstruction.

3. **Cross-architecture and cross-model validation.** The core findings are reproduced with both BatchTopK and JumpReLU SAEs (Section 3.6, Figure 7), and on two LLM families (Gemma-2-2b and Llama-3.2-1b, Figure 8). This strengthens generalizability.

4. **Honest characterization of asymmetric failure modes.** The paper distinguishes low-L0 failures (every latent corrupted) from high-L0 failures (many correct latents remain), and Section 4.2's analysis of per-latent variation at intermediate L0 adds useful nuance that complicates the "single correct L0" framing.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **LLM validation of c_dec is qualitative, not quantitative.** The match between the c_dec "elbow" and peak sparse probing F1 is described as "coincides with" and "roughly corresponds to" without reporting precise L0 values, tolerances, or variability across layers. For Gemma-2-2b layer 5 (Figure 8), c_dec has a long shallow region where the global minimum is not the correct operating point — the authors switch to using the "elbow" heuristic. The paper is appropriately cautious, but this limits the metric's practical utility as a precise guide for LLM practitioners.

2. **The concept of a single "correct L0" does not transfer cleanly to LLMs.** In toy models, ground-truth feature sparsity defines a correct L0. In LLMs, there is no comparable ground truth. The paper's own Section 4.2 shows that at intermediate L0 (e.g., 750), some latents fire too often while others too seldom, suggesting optimal L0 may be per-latent. The paper acknowledges this but does not reconcile it with its central framing that there is a single correct L0 to find.

### Trivial
None.

## Nice-to-Haves

- A quantitative comparison table showing c_dec elbow L0 vs. peak sparse probing L0 for all layers and model families tested would substantially strengthen the LLM validation.
- Discussion of why the c_dec curve enters a "long shallow region" for Gemma-2-2b layer 5 but not for Llama-3.2-1b — understanding the metric's failure modes would help practitioners know when to trust it.
- Comparison to a simpler baseline (e.g., reconstruction variance explained plateau) would clarify whether c_dec provides information beyond what practitioners could already infer.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's concern about the ground-truth SAE at L0=5 selecting incorrect features**: This reflects a misunderstanding — with orthogonal true features, the encoder F^T correctly identifies active features by activation magnitude. Removed because factually wrong about the paper's setup.
- **Harsh critic's criticism about abstract claim ("most SAEs have L0 too low") not supported in main paper**: The paper defers the supporting analysis to Appendix A.13; the parser strips appendices from all papers. Per hard rules, this weakness is removed.
- **Strength Finder's generic claim that "this paper addressed an important problem"**: Too generic to retain; dropped.
- **Strength Finder's claim that "Finding shows SAEs fail to disentangle underlying features"**: This is duplicated by the more specific strength #1.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a compact quantitative table to Section 4 showing, for each model/layer: the c_dec elbow L0, the L0 at peak sparse probing F1, and the range of L0s within 95% of peak probing performance. This would transform the qualitative LLM validation into a precise, actionable result.

2. In Section 4.2, explicitly discuss how the observation that different latents may need different L0s squares with the paper's recommendation of a single "correct L0" for the whole SAE — or clarify that the correct L0 should be interpreted as a lower bound below which all latents are corrupted.

3. Consider adding a brief discussion of failure modes for c_dec: when does the metric produce flat/ambiguous curves, and what should practitioners do in those cases?

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Compute Optimal Inference and Provable Amortisation Gap | ghH6YYDs15 | 4.67 | 1, 2 | Weaker — weaker real-model experiments, flawed theory claims. Our paper is clearly stronger. |
| Sparse Autoencoders Find Highly Interpretable Features | F76bwRSLeK | 4.80 | 1, 2 | Comparable in quality but with one outlier reviewer score of 1 dragging avg down. Our toy-model evidence is cleaner. |
| Applying SAEs to Unlearn Knowledge | ZtvRqm6oBu | 5.25 | 2 | Weaker — limited in scope, less rigorous experimental design. Our paper is stronger. |
| An X-Ray Is Worth 15 Features | ZLAQ6Pjf9y | 5.60 | 2 | Weaker — application paper with incomplete ablation studies. Our paper has tighter experimental logic. |
| Residual Stream Analysis with Multi-Layer SAEs | XAjfjizaKs | 6.50 | 2 | Slightly stronger — introduces a new SAE variant with solid experiments. Our paper has cleaner causal identification but less methodological novelty. |
| Sparse Autoencoders Do Not Find Canonical Units | 9ca9eHNrdH | 7.00 | 1, 2 | Stronger — multiple novel methods (stitching, meta-SAEs, BatchTopK), thorough evaluation. Our paper is more focused but less ambitious in scope. |
| Towards Principled Evaluations of SAEs | 1Njl73JKjB | 7.00 | 1, 2 | Stronger — comprehensive evaluation framework with supervised ground truth. Our paper has cleaner toy experiments but narrower validation. |

**Round-1 bracket:** 5.0 – 7.0
**Round-2 narrowing:** The paper consistently outperforms all anchors at 4.67–5.60 but falls slightly short of anchors at 6.50–7.00 in terms of methodological breadth and LLM validation rigor. This places the paper in the 5.5–6.5 range. Within this range, the paper's strongest asset — a clean, causally-identified demonstration with practical implications — is weighed against its weaker LLM validation. A score of **6.0** reflects that this is a solid, publishable paper with genuine contributions and honestly-acknowledged limitations, but with room to strengthen the LLM evidence.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>