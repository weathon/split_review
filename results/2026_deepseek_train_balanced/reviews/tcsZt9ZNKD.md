## Summary

This paper proposes using TopK (k-sparse) autoencoders for language model interpretability, showing they outperform L1-penalized ReLU autoencoders on the reconstruction-sparsity frontier. The authors train autoencoders up to 16 million latents on GPT-4, report scaling laws relating autoencoder size, sparsity, and subject model size, and introduce several evaluation metrics (downstream loss, probe loss, N2G explainability, ablation sparsity). Key results include: TopK avoids L1 activation shrinkage, achieves only 7% dead latents at scale via encoder-decoder initialization and an auxiliary loss, and exhibits clean scaling laws with a joint dependence on n and k.

## Strengths

1. **TopK achieves a strictly better reconstruction-sparsity frontier than ReLU/ProLU, and the gap grows at scale.** Figure 2a shows TopK dominating ReLU and ProLU on MSE-vs-L0 at fixed n=32768, and Figure 2b demonstrates a steeper scaling exponent for TopK. Both quantitative results (lines 100, 107) are backed by empirical comparison at multiple scales.

2. **Only 7% dead latents in a 16M-latent GPT-4 autoencoder, a massive improvement over prior work.** The paper reports that Templeton et al. (2024) had ~65% dead latents at comparable scale, while the authors achieve 93% alive latents through two concrete modifications: encoder initialized to decoder transpose, and an auxiliary loss using top-kₐᵤₓ dead latents (line 120).

3. **Controlled experiment demonstrating that TopK eliminates L1 activation shrinkage while ReLU does not.** The refinement experiment (Section 5.1, Figure 6) directly measures bias in latent magnitudes: for ReLU models, refinement shifts activations systematically upward (confirming L1 shrinkage); for TopK models, refinement is unbiased and smaller in magnitude.

4. **A joint scaling law L(n,k) with explicit interaction term between number of latents and sparsity.** The fitted coefficients (line 183) are reported transparently: βₙ = −0.017, βₖ = 0.26, γ = −0.042. The negative γ shows that scaling with n steepens as k increases, going beyond prior work (Lindsey et al. 2024) which studied a combined reconstruction-sparsity loss.

5. **Multi-TopK enables progressive recovery at test time.** The paper identifies that standard TopK overfits to the training k value (line 462) and proposes summing multiple TopK losses with different k values, yielding a progressive code across all sparsity levels (lines 464–467) with clear empirical support (Figure 7).

6. **Subject-model scaling across the GPT-4 family.** Section 3.2 explicitly tests how required autoencoder size grows with LM size at fixed k=32, finding that larger models need more latents and the exponent worsens (Figure 4b)—directly relevant for practitioners.

## Weaknesses

### Fatal
None.

### Major

- **The "10% of GPT-4 pretraining compute" claim lacks any supporting derivation (line 247).** The paper states: "when our 16 million latent autoencoder is substituted into GPT-4, we get a language modeling loss corresponding to 10% of the pretraining compute of GPT-4." This is a striking quantitative claim—10% of GPT-4's pretraining compute is an enormous figure—presented without any methodology explaining how downstream loss maps to equivalent compute. What scaling law is used (Kaplan et al. 2020 or Hoffmann et al. 2022, which yield very different answers)? What is the reference curve? Without this, the number cannot be verified or reproduced. The concept of reframing downstream loss as compute-equivalent is interesting, but the specific 10% figure needs either a clear derivation (with cited scaling law and assumptions) or removal.

### Minor

- **The abstract's claim that "these metrics all generally improve with autoencoder size" oversimplifies the body's findings.** The abstract (line 5) presents the metrics as uniformly improving, but the paper body (line 232) acknowledges more complex, regime-dependent behavior: "The impact of the number of active latents L₀ is more complicated. Increasing L₀ makes explanations based on token patterns worse, but makes probe loss and ablation sparsity better." Additionally, ablation sparsity reverses trend at k=512 (line 404), and probe score peaks then declines as k increases (line 279). The word "generally" provides some hedge, but the framing still downplays the nuanced picture the body correctly documents.

- **The probe loss metric has an inherent limitation that constrains the conclusions drawn from it.** The metric only tests recovery of 61 features the authors hypothesized a priori (Section 3.2). The paper acknowledges this (line 282) but then uses probe loss as evidence that "larger sparse autoencoders are generally better" (line 27, via contribution 3) and that TopK beats ReLU (line 279). A metric that only measures recovery of *known* features cannot assess whether an autoencoder discovers *new, meaningful* features—which is a primary motivation for SAEs. The limitation is disclosed but its implications for the conclusions are not fully reckoned with.

- **The near-zero βₙ coefficient in the joint scaling law is under-discussed.** βₙ = −0.017 (line 183) means that holding k fixed, increasing n barely reduces MSE. The interaction term γ = −0.042 is larger in magnitude, suggesting that n primarily helps through enabling sparser k. This has practical implications for how practitioners should allocate compute between n and k, which the paper should address directly rather than simply reporting the coefficients.

- **Hyperparameter tuning for baseline activation functions (ReLU λ, Gated, ProLU) is not described.** The paper claims TopK Pareto-dominates ReLU, ProLU, and Gated (Figure 2a), but the main text only mentions sweeping learning rates (line 62) without describing how the λ penalty for ReLU (or equivalent hyperparameters for ProLU/Gated) was tuned. If baselines were not tuned to a comparable level of effort, the Pareto-dominance claim is less convincing.

### Trivial
None.

## Nice-to-Haves
- Validating one or more metrics against a downstream application (e.g., circuit discovery or model steering) would ground the evaluation framework beyond standalone proxies. The paper acknowledges this as future work (line 488).
- Testing multiple layers per model and longer context windows would improve generality; both are noted by the authors as limitations (with appendix discussion stripped by the parser).
- Confidence intervals on scaling law coefficients would strengthen the quantitative claims, though single-run experiments at this scale are standard.

## Removed Points
*These are points from the input reviews that were filtered out. Treat with caution.*

- **"Dead latents subsection too brief"**: Removed per hard rule—the paper references Appendix §sec:aux-loss for details that were stripped by the PDF parser.
- **"Only one layer per model"**: Removed per hard rule—the paper references Appendix §sec:layer_location_impact.
- **"No discussion of metric misalignment with downstream applications"**: Removed—the Limitations section (line 488) says: "Much more could be done to understand what metrics best track relevance to downstream applications, and to study those applications themselves."
- **"N2G conflates autoencoder quality with explanation quality" overplayed as a major weakness**: Removed—the paper explicitly positions N2G as "an initial exploration" using "a substantially less expressive but much cheaper method" (lines 359–360) and acknowledges the issue. The critic's framing overstates the severity relative to the paper's own cautious positioning.
- **"Strengthening the Paper on Its Own Terms" suggestions**: These are helpful suggestions, not weaknesses. Incorporated into Suggestions and Nice-to-Haves.
- **Strength 5 (downstream loss reframed as pretraining compute equivalent)**: Removed from strengths because the actual instantiation (the 10% claim) is unsupported. The conceptual framing is interesting but the implementation is the subject of a verified weakness.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a limitation, implication, or reinterpretation that the paper itself does not already discuss or acknowledge.

## Suggestions
1. **Substantiate or remove the 10% GPT-4 compute claim.** Provide the scaling law, reference curve, and assumptions used to map downstream loss to compute equivalent. If this cannot be done with the same rigor as the rest of the paper, remove the specific number and keep only the conceptual framing.
2. **Discuss the practical implications of βₙ ≈ 0.** What does the near-zero coefficient on n mean for practitioners deciding how to allocate compute between wider autoencoders and sparser activations?
3. **Recalibrate the abstract's metric claims.** The body's more nuanced, regime-dependent characterization should be reflected in the abstract.
4. **Describe baseline hyperparameter tuning.** A brief statement on how λ was chosen for ReLU and how Gated/ProLU hyperparameters were tuned would strengthen the Pareto-dominance claims.

## Score and Decision

This is a solid empirical paper with meaningful contributions: the TopK adaptation for LM autoencoders is well-motivated and empirically superior, the dead-latent mitigation is effective, the scaling laws are informative, and the evaluation metrics—while exploratory—are honestly presented with limitations discussed. The main weakness is the unsupported 10% compute-equivalent claim, which is notable but not fatal to the paper's core contributions. With reasonable revisions (substantiate or remove the claim, calibrate the abstract, and address the minor points), this paper meets the ICLR bar.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>