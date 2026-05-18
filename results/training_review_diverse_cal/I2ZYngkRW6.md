Now I have a thorough understanding of the paper and can verify each claim. Let me synthesize the final review.

## Summary

CrossNovo proposes distilling bidirectional knowledge from a Non-Autoregressive Transformer (NAT) decoder into an Autoregressive Transformer (AT) decoder for de novo peptide sequencing. The method uses joint training with a shared encoder and importance annealing (Section 3.3), followed by a cross-decoder attention mechanism with gradient blocking (Section 3.4) to transfer the NAT's learned representations into the AT model. Results on 9-species-v1 and 9-species-v2 benchmarks show improvements over both AT and NAT baselines.

## Strengths

1. **Novel cross-decoder attention with gradient blocking enables principled NAT→AT distillation.** The paper replaces the AT decoder's standard cross-attention with one that attends to both encoder outputs and NAT decoder latent embeddings, while blocking gradients to prevent the AT loss from corrupting the NAT's CTC-trained representations (Section 3.4). This design is well-motivated: the paper reports degradation when gradient blocking is removed.

2. **Joint training with importance annealing balances dual objectives.** The shared-encoder multitask framework (Section 3.3) linearly anneals the NAT loss weight from 1.0 to 0.0, allowing the NAT to provide bidirectional signal early while letting the AT objective dominate later. This is a principled solution to the competing optimization goals.

3. **State-of-the-art results on two widely-used benchmarks.** On 9-species-v1, CrossNovo achieves average AA recall 0.811 and peptide recall 0.654, outperforming all prior autoregressive and non-autoregressive models (Table 1). On 9-species-v2, it attains average precision 0.906 and peptide recall 0.786 (Table 2).

4. **Empirical evidence of combining AT and NAT strengths.** The paper shows (Section 4.3) that on Human/Mouse where AT excels, CrossNovo extends that advantage (up to 9% over NAT), while on species where NAT was superior, CrossNovo improves AT by 1–3%. This directly supports the claim of synthesizing both inductive biases.

## Weaknesses

### Major

- **Inference-time architecture is unclear, making the comparison with baselines unverifiable.** The paper states that the cross-attention in the AT decoder is *replaced* with one that concatenates NAT decoder latents $\mathbf{V}^{(L)}$ with encoder outputs (Section 3.4, Equation 2). The paper never states whether the NAT decoder must execute at test time to produce these vectors. If the NAT decoder is required during inference, the model has roughly 2× the decoder parameters and compute of single-decoder baselines — a comparison that is not apples-to-apples. If the NAT decoder is *not* needed, the paper must explain how the AT decoder attends to non-existent NAT latents during deployment. This omission undermines a fair evaluation of the results. The authors should explicitly state the inference-time setup and report wall-clock time and parameter counts alongside accuracy numbers.

### Minor

- **No variance or uncertainty reported.** All results in Tables 1 and 2 are point estimates. Given that improvements over strong baselines are modest (e.g., +0.026 AA recall on 9-species-v1), the reader cannot assess statistical significance. While single-run evaluation is common practice in this field, adding at least standard deviation across 3 runs for the primary comparison would substantially strengthen confidence in the reported gains.

- **The interaction between importance annealing and the distillation phase is not analyzed.** During joint training, $\lambda_{AT}$ is annealed to 1.0, meaning the NAT loss is effectively zero by the end. The NAT decoder is then frozen and its latents are used in the distillation phase. The paper does not investigate whether the NAT representations degrade once the CTC loss is turned off, or whether re-adding a small NAT loss during distillation would help. This is a reasonable concern given the annealing schedule and warrants analysis.

- **No dedicated limitations or discussion section.** The paper concludes without discussing limitations. For instance, the NAT decoder adds training complexity and optimization difficulty (acknowledged in the introduction for NAT models generally), the fixed generation length of 40 for the NAT imposes a constraint on peptide length, and the reliance on CTC loss may limit scaling. A brief discussion of these would improve the paper.

### Trivial

- The notation for the sinusoidal positional encoding in Section 3.2 is difficult to parse as presented. The authors should provide a cleaner standard formulation.

## Nice-to-Haves

- An error analysis showing what kinds of errors CrossNovo reduces (e.g., improvements on long peptides, modified residues, or low-intensity spectra) would strengthen the biological relevance.
- A comparison of inference speed and parameter count against baselines would be useful regardless of whether the NAT decoder is retained at test time.
- The "Can we reverse the direction" discussion (Section 3.5) is thoughtful but speculative; testing this direction (even with a simple experiment showing degradation) would add value.

## Removed Points

These points from the reviews are flagged for removal; treat them with caution:

1. **Missing ablation studies (Harsh Critic #1).** The paper claims "comprehensive ablation studies validate our key contributions" in both the abstract and conclusion. The absence of these results in the parsed text is consistent with the parser stripping appendix/supplementary sections, which is a known artifact and not an author error. Per the rules, weaknesses about missing appendix content are removed.

2. **"First-ever" claim for cross-decoder attention.** The reviewer questions whether this is truly the first-ever such module. Per the rules, I cannot verify claims about missing related works and must not penalize the paper for making a novelty claim that I cannot refute with external sources.

3. **Formatting/notation complaints about sinusoidal encoding.** The garbled appearance of the positional encoding equation is a parser artifact, not an author error.

4. **"The paper should also cover Y" items** (e.g., more detailed species breakdown, additional downstream tasks). The paper already provides species-level discussion and the scope is appropriately bounded.

## Novel Insights

The key insight that emerges from the reviews is that the paper presents a genuinely interesting architectural idea (NAT→AT distillation via cross-decoder attention with gradient blocking) and obtains strong empirical results, but its presentation omits a critical detail: whether the NAT decoder is required at inference time. This single ambiguity, rather than any methodological flaw, is the review's central concern. The other issues (variance, annealing analysis) are secondary and typical of early-stage work. The cross-attention design itself is thoughtful — the positional encoding scheme (0–40 for NAT latents, 41–41+k for spectrum features, Section 3.4) cleanly separates the two information sources, and the gradient blocking is well-motivated by the observed degradation. The paper would benefit most from clarifying the inference setup rather than adding more experiments.

## Suggestions

1. **Explicitly state the inference-time architecture.** In a single sentence: "At inference time, the NAT decoder [is / is not] executed. The AT decoder's cross-attention attends to [both encoder outputs and NAT latents / only encoder outputs via ...]." If the NAT decoder is needed, report runtime and parameter counts alongside accuracy. If not, explain the mechanism.
2. **Run at least 3 random seeds** for the primary 9-species-v1 experiment and report mean ± std for the key metrics.
3. **Add a brief limitations section** (can be short, 3–5 sentences) discussing training complexity, the fixed NAT generation length constraint, and when the method may not help.
4. **Investigate the NAT latent quality** during the annealing schedule — a simple analysis showing whether representations degrade as λ_AT approaches 1.0 would address the distillation-phase concern.
5. Clarify the sinusoidal encoding notation in Section 3.2 using a standard formulation.

## Score and Decision

**Originality:** 7/10 — the cross-decoder attention with gradient blocking for NAT→AT distillation is novel in this domain.  
**Importance of research question:** 7/10 — improving de novo peptide sequencing has practical value in proteomics.  
**Claims well-supported:** 5/10 — the inference ambiguity prevents full verification of the comparison fairness.  
**Soundness of experiments:** 6/10 — solid baseline comparisons but missing variance and ablation details.  
**Clarity of writing:** 5/10 — the method description is mostly clear, but the critical inference-time setup is undefined.  
**Value to community:** 7/10 — the approach and code release are useful to researchers in computational proteomics.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>