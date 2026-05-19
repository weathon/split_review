- Decision: Reject
- Avg Score: 6.33
- Scores: 8, 5, 6
Now I have all the information I need. Let me construct the final review.

## Summary

This paper presents Causal Relation Networks (CausalRNs), an all-MLP architecture for autoregressive sequence modeling derived from Relation Networks. The key technical contribution is showing that exponentially-activated Relation Networks can be linearized exactly (Proposition 3.2), yielding O(N) time and space complexity. The paper also discovers that applying pre-activation normalization before the exponential creates an irreducible matrix-valued memory that enables strong performance on synthetic in-context retrieval tasks. Experiments cover language modeling (WikiText-103), image classification (CIFAR-10/100), and a copying task.

## Strengths

1. **Exact linear-time proof for exponentially-activated Relation Networks**: Proposition 3.2 and the derivation in Section 3.2 provide a clean, formal guarantee that using exp(x) as the activation function reduces the quadratic pairwise-MLP computation to O(N) time and space, with no approximations. The proof is correct under the stated assumptions (single-hidden-layer MLP) and is a genuine theoretical contribution.

2. **Quadratic CausalRN matches Transformer on the copying task**: Figure 5 shows near-identical learning curves between the quadratic CausalRN (with pre-activation normalization) and a Transformer, with both achieving perfect retrieval. Figure 6 confirms that CausalRNs with pre-activation normalization converge faster than Transformers for string sizes ≤ 128, directly supporting the claim that matrix-valued states enable effective in-context retrieval in this synthetic setting.

3. **Systematic ablation study validating key design choices**: Figure 3 provides controlled evidence that (a) post-reduction normalization stabilizes training, (b) exact pre-activation normalization induces a phase-change phenomenon near the 200th iteration, and (c) exponential activation accelerates convergence over ReLU/ELU. These results validate the paper's design rationale and are informative for the community.

4. **Explicit connection to prior theoretical insights**: Section 4.2 grounds the architecture's design in established findings—exponential gating (Beck et al., 2024; Yang et al., 2023) and state expansion in SSMs (Gu et al., 2022; Zhang et al., 2024)—strengthening the coherence of the theoretical narrative.

5. **Interpretability heatmaps from a vision BiRN**: Figure 7 shows that a trained linear BiRN produces interpretable attention-like patterns that focus on the main object in an image, providing qualitative validation beyond standard accuracy metrics.

## Weaknesses

### Fatal
None.

### Major

1. **The abstract's claim of being "comparable to Linear Transformers" is not well-supported by the reported numbers.**  
   The paper reports 1.58 PPL (CausalRN) vs. 1.47 PPL (Linear Transformer) on WikiText-103. A 0.11 PPL gap without confidence intervals, significance tests, or model size comparisons does not convincingly support "comparable." The paper's body hedges appropriately ("While not competitive, they are valid ways to perform autoregressive sequence modeling"), but the abstract oversells the result. Given that the paper's main empirical evidence on standard benchmarks comes from the linear variant—which underperforms every baseline it is compared against—readers cannot assess whether the gap is meaningful without model sizes, parameter counts, or variance estimates.

2. **Missing experimental details prevent fair comparison and reproducibility.**  
   The paper does not report model sizes (parameter counts, number of layers, hidden dimension $d_e$, hidden width $d_h$, or state expansion factors) for either the proposed models or the baselines in the main experiments (Tables 1 and 2). While batch size, learning rate, and optimizer are given, core architectural specifications are absent. This makes it impossible to assess whether the comparison to Linear Transformer, Transformer, and Mamba is fair, and it hinders reproducibility and community adoption.

3. **The approximate pre-activation normalization is proposed but never empirically evaluated.**  
   Section 3.4 introduces an approximation ($\exp(\mu(x)+\mu(\bar{y}))$) that would preserve linear-time training while enabling matrix-valued memory—potentially the most practically significant variant. However, it is never tested in any experiment (not in the ablation study, not on the copying task, not on language modeling). This is a missed opportunity that weakens the paper's experimental narrative.

### Minor

1. **The quadratic variant's advantages are only demonstrated on a synthetic copying task.**  
   The quadratic CausalRN (with pre-activation normalization) that achieves perfect retrieval and fast convergence on the copying task is never evaluated on language modeling or image classification. The copying task (up to 514 tokens) is a useful diagnostic but not representative of natural language or vision tasks. The paper would be strengthened by testing this variant on a small-scale language modeling benchmark (e.g., WikiText-2 with short context) to see whether the matrix-valued memory advantage transfers—even a negative result would be informative given the paper's scientific-investigation framing.

2. **No confidence intervals, error bars, or variance reporting for any main result.**  
   Tables 1 and 2 report single-point numbers without standard deviations or confidence intervals. While single-run evaluation is common in some settings, the absence of variance information makes it harder to judge the reliability of the reported comparisons, particularly when performance gaps are small (e.g., 1.58 vs. 1.47 PPL).

### Trivial
None.

## Nice-to-Haves

- Evaluate the **approximate pre-activation normalization** variant on the copying task to determine whether it preserves the retrieval capability of the quadratic variant while maintaining linear-time training. If it works, this would be the most practically impactful result in the paper.
- Test the **quadratic CausalRN** on a small-scale language modeling benchmark (e.g., WikiText-2 with limited context) to see if the copying-task advantage carries over to more realistic settings.
- Provide wall-clock speed benchmarks to complement the theoretical O(N) complexity claim.

## Removed Points

The following criticisms from the reviewers are removed with justification:

- **"The linearization proof assumes a single-hidden-layer MLP but the architecture likely uses deeper MLPs"**: Factually incorrect. The paper explicitly defines the MLP module as a single-hidden-layer MLP (Definition 2.1), the proof in Proposition 3.2 starts with "let $f_{\theta}$ be a single-hidden-layer MLP from Eq. 1," and "state expansion" refers to increasing the width $d_h$ of the single hidden layer, not adding depth. The paper is consistent on this point.

- **"The paper's central empirical claim is not supported by the experiments"** (as framed as a fatal/structural flaw): Overstated when applied to the paper as a whole. The paper explicitly frames itself as a scientific investigation (Section 1: "We do not position the CausalRN as a replacement for Transformers or State Space Models"). The core theoretical contribution (the linearization proof) is fully supported. The main empirical weakness is a tension between the abstract's "comparable" claim and the actual numbers, which is captured in Major weakness #1 above.

- **Generic area-concern sweeps** (e.g., "could the metric be measuring a proxy?", "are confounders controlled?"): These lack concrete textual anchors and do not identify specific problems in the paper.

- **Comments about missing appendix content / stripped sections**: The supplementary materials were stripped by the PDF parser; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The key insight that emerges from the review is that the paper's value is bimodal: the theoretical linearization proof is solid and self-contained, but the empirical evaluation creates a gap between what the abstract promises and what the body demonstrates. The approximate pre-activation normalization variant (never tested) could be the bridge between these two modes, but the paper stops short of exploring it.

## Suggestions

1. Tone down the abstract's "comparable to Linear Transformers" claim to match the more measured language in the body ("While not competitive, they are valid ways to perform autoregressive sequence modeling").
2. Report model sizes (parameter counts, number of layers, hidden dimensions, state expansion factors) for all models and baselines.
3. Add confidence intervals or standard deviations to the main results.
4. Evaluate the approximate pre-activation normalization variant on the copying task and, if successful, on a small language modeling benchmark.
5. Include wall-clock speed benchmarks to substantiate the claimed efficiency advantage.
