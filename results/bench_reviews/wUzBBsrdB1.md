Now I have a solid understanding of the calibration landscape. Let me write the consolidated review.

## Summary

This paper studies the effect of L0 (average number of active latents per token) on Sparse Autoencoder (SAE) feature quality. Through toy model experiments, it demonstrates that setting L0 too low causes the SAE to mix correlated features to improve reconstruction MSE at the expense of feature monosemanticity — the MSE loss actively incentivizes incorrect, polysemantic latents. The paper proposes a diagnostic metric, decoder pairwise cosine similarity (c_dec), and shows that its "elbow" aligns with peak sparse probing performance on Gemma-2-2b and Llama-3.2-1b. The central message — that L0 is not a neutral hyperparameter and that too-low L0 is harmful — is important and underappreciated.

## Strengths

- **Clean toy-model demonstration of feature mixing under low L0**: Using a synthetic setup with known ground-truth features (Section 3.1-3.2), the paper directly shows that when SAE L0 is set below true L0, decoder latents mix correlated features together. The comparison between a ground-truth SAE and a trained SAE at identical L0 (Figure 4) is particularly striking: the trained SAE achieves MSE 2.73 while the ground-truth SAE gets 4.88, proving that the training objective actively pushes away from the correct solution.

- **Theoretical proof that low L0 incentivizes feature mixing**: Theorem 1 (Appendix A.5) provides a formal mathematical argument for a two-feature, two-latent toy model: when features co-occur with probability >0 and the SAE can fire at most one latent, the MSE-minimizing solution mixes the features rather than separating them. This gives rigorous grounding to the empirical observations.

- **Exposing the fallibility of sparsity-reconstruction tradeoff plots**: Figure 4 shows that at L0 values below true L0, a trained (incorrect) SAE achieves higher variance explained than the ground-truth SAE — meaning a standard tradeoff plot would rank the incorrect SAE as better. This is a clear, actionable warning for practitioners.

- **Validation of c_dec on both toy models and LLMs with sparse probing**: The decoder pairwise cosine similarity metric is minimized at the correct L0 in toy models (Figure 6), and its "elbow" roughly coincides with peak sparse probing F1 scores on Gemma-2-2b and Llama-3.2-1b (Figure 8). The paper includes both BatchTopK and JumpReLU SAEs and multiple layers, lending generality.

- **Evidence that many open-source SAEs use surprisingly low L0**: Appendix A.13 surveys Neuronpedia SAEs, finding median L0 for Gemma-2-2b around 56-61, while the paper's experiments suggest the optimal L0 for this model is ~200-250. This gives the work practical urgency.

## Weaknesses

### Fatal
None.

### Major

- **The c_dec metric does not reliably identify a unique correct L0 in real models, limiting its practical utility as a selection method.** For Gemma-2-2b layer 5 (Figure 8, left), c_dec has a long flat region from L0 ~200 to ~1750 with no clear minimum — the global minimum lies far from the "elbow" that the authors later identify as corresponding to peak probing performance. The paper resorts to identifying the "elbow just before the jump due to low L0" as the signal, but this elbow is defined post-hoc after seeing the probing results. Without a principled, quantifiable rule for detecting the elbow automatically, c_dec functions primarily as a qualitative diagnostic ("avoid very low L0") rather than a precise method for L0 selection. The paper acknowledges this limitation (Section 6: "the metric can sometimes remain nearly flat"), but this substantially weakens the claimed contribution that the metric "can help guide the search for the correct L0."

- **The claim that "most commonly used SAEs have an L0 that is too low" is broader than the evidence supports.** The paper's own experiments determine optimal L0 (~200-250) for Gemma-2-2b and Llama-3.2-1b with 32k-latent SAEs. The Neuronpedia survey (Appendix A.13) aggregates SAEs across many model families (gemma-2b, gpt2-small, Llama-3.1-8B, gemma-2-9b) with varying dictionary widths, some as small as 8k or 16k latents. Optimal L0 likely scales with model size, hidden dimension, layer depth, and dictionary width. The paper provides no argument that L0 should be comparable across these settings. The evidence supports a narrower claim: "for 32k-latent SAEs on Gemma-2-2b and Llama-3.2-1b, many existing SAEs use an L0 that appears lower than optimal."

- **The critique of sparsity-reconstruction tradeoff plots is overclaimed.** The paper argues these plots are "not a sound method of evaluating SAEs" (Section 1, Section 3.4). The toy experiment only varies L0 for a fixed architecture, showing that at low L0 a ground-truth SAE looks worse than a mixed-feature SAE. But in practice, the primary use of these plots is to compare *different SAE architectures* (e.g., TopK vs JumpReLU) at fixed sparsity levels — not to select the optimal L0 for a single architecture. The paper conflates two different uses of these plots. The core insight (reconstruction alone is insufficient) is valid, but the blanket dismissal of tradeoff plots as "misleading" goes beyond what the evidence supports.

### Minor

- **Theorem 2 assumes orthonormal underlying features and a perfectly disentangled SAE 1, which is idealized.** In real LLMs with superposition, true features are not orthogonal even in the ground truth (cosine similarities are non-zero, as shown in Figure 15 left). The paper's Remark 1 acknowledges this and argues that the systematic mixing component dominates random superposition noise. The superposition toy model (Appendix A.4.1) confirms c_dec still works, but the paper does not analyze *how much* the baseline c_dec of a "correct" SAE would be elevated due to non-orthogonal true features — making it unclear how to distinguish mixing-induced non-orthogonality from unavoidable superposition noise.

- **The toy model experiments use h=g (equal number of latents and true features), which is unrealistic.** Real SAEs are massively overcomplete (e.g., h=32k for d=2048). The paper does not test whether the feature mixing effect persists when h >> g (the overcomplete case). The superposition toy model (Appendix A.3.3) uses only 5 features with small overlap, not the overcomplete regime.

- **Only k=16 sparse probing results are shown in the main text.** k=1 results are relegated to Appendix A.12 (Figure 21). The robustness of the alignment between c_dec and probing across different k values is not well established in the main body.

- **The relationship to feature hedging (Chanin et al., 2025) is noted but not clearly differentiated.** The cited work focuses on dictionary width as the cause of hedging, while the current paper focuses on L0. The paper states "We consider our work a version of feature hedging due to low L0" but does not explain how the mechanism differs or whether both width and L0 interact.

### Trivial
- The Pytorch pseudocode in Appendix A.17 defines `index = n * dec_proj.shape[0]` in Figure 29 but the variable name `dec_proj` is a typo (should be consistent with variable naming).
- Some figure captions contain parser artifacts (e.g., table formatting in Figure 9, 20, 22) that would need cleanup in camera-ready.

## Nice-to-Haves
- A systematic comparison with existing diagnostics for feature quality (dead latent fraction, feature absorption indices from Chanin et al., 2024, or MDL-based heuristics from Ayonrinde et al., 2024) would help contextualize whether c_dec adds value beyond simpler heuristics.
- Qualitative inspection of SAE latents at different L0s (e.g., showing that a latent tracking "Harry Potter" at L0=200 also activates on unrelated tokens at L0=50) would make the feature mixing claim concrete for practitioners.
- Validation on additional models (e.g., Gemma-2-9b or a larger Llama model) would strengthen claims about generality.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **Criticism about "normalization not stated for c_dec in LLM experiments"**: The paper explicitly states in Appendix A.7 that "the decoder remains normalized" for BatchTopK SAEs, and the PyTorch code in Figure 28 normalizes the decoder before computing c_dec. This is a reviewer misreading.
- **Criticism about "tying assumption of toy model"**: The paper's Theorem 1 (Appendix A.5) explicitly uses a tied encoder for theoretical tractability. The main toy experiments (Section 3.1-3.2) use standard BatchTopK SAEs which do not require tied weights. The critic's demand to test untied encoders is about the theorem, not the core experiments.
- **Criticism about "missing confidence intervals on benchmarks"**: Single-run evaluation on large-scale SAE benchmarks is the norm in this field. The paper provides 3 seeds per L0 point (Figure 8) and 5 seeds for toy models (Figure 6), which is standard.
- **Several generic weaknesses from the harsh critic** about missing larger models, missing qualitative case studies, and suggestions for automatic L0 selection — these are nice-to-haves, not core weaknesses.

## Novel Insights

The most interesting observation beyond the paper's own contributions is the asymmetry between JumpReLU and BatchTopK SAEs at high L0 (Section 4.1, Figure 9, Appendix A.16). BatchTopK SAEs develop a "dual distribution" phenomenon at high L0 (narrow peak + hump in decoder projection histograms), suggesting some latents have too-high L0 while others have too-low L0 simultaneously. JumpReLU SAEs, by contrast, handle high L0 much better because their per-latent thresholds can adjust adaptively. This suggests that the very notion of a single "correct L0" may be an oversimplification — different latents may have different optimal firing rates, and architectures with per-latent thresholds (JumpReLU) have a meaningful advantage. The paper's toy model transition experiment (Appendix A.8), showing that starting with too-low L0 permanently damages the SAE even if L0 is later corrected, is also a practically important insight: low L0 is not just suboptimal but can create irretrievable local minima.

## Suggestions

1. **Tone down the scope of the headline claims.** Replace "most commonly used SAEs have an L0 that is too low" with a more measured claim specific to the models and widths tested. Similarly, reframe the sparsity-reconstruction tradeoff critique as "reconstruction alone is insufficient, especially at low L0" rather than "these plots are not sound."

2. **Acknowledge the ambiguity of c_dec more prominently.** The paper currently hedges (Section 6) but the abstract and introduction present c_dec as a method that "finds the correct L0" — this should be softened to reflect that c_dec is a useful diagnostic for detecting pathologically low L0, not a precise L0 selector.

3. **Test the overcomplete toy model setting** (h >> g) to verify that the feature mixing mechanism still operates when the SAE has ample dictionary capacity. This is a direct and feasible experiment that would address an obvious concern.

4. **Provide a simple heuristic for detecting the "elbow"** without downstream labels — for instance, detecting where the derivative of c_dec w.r.t. L0 exceeds a threshold, or using the L0 at which c_dec reaches some fraction of its maximum value. Even a heuristic with known failure modes would be more actionable than visual inspection.

5. **Move the k=1 sparse probing results to the main text** to show that the alignment between c_dec and probing generalizes across k values.

## Score and Decision

### Calibration Anchors

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| Feature Hedging: Correlated Features Break Narrow SAEs (7lzq9mMVxq) | 3.50 / Reject | Directly related; rejected for weak theory and unclear metrics. The current paper is substantially stronger — it has formal proofs, cleaner toy experiments, and validation via sparse probing. |
| SAEs Trained on Same Data Learn Different Features (EjInprGpk9) | 5.50 / Accept | Comparable rigor; the current paper has narrower scope but deeper analysis of a single hyperparameter. Both are empirical contributions to understanding SAE limitations. |
| On the Limits of SAEs: A Theoretical Framework (DSOTgzeH3w) | 6.00 / Accept | Stronger theory (closed-form solutions); comparable empirical validation. The current paper has better toy-model ground-truth experiments but weaker theory. |
| The Price of Amortized Inference in SAEs (33wY6AI13k) | 5.00 / Accept | Broader analysis of SAE pathologies. The current paper is more focused on a single, underappreciated issue (L0). |
| Bimodality of SAE Features (soMC0uESuz) | 5.00 / Reject | Similar structure (identify problem, propose fix). The current paper's toy experiments are cleaner and its theoretical backing is stronger. |

The paper identifies a genuine, underappreciated problem and provides clean demonstrations. The core weaknesses are (1) the c_dec metric is more of a qualitative diagnostic than a reliable L0 selection method, (2) the headline claims about "most SAEs" are overbroad, and (3) the sparsity-reconstruction critique conflates two different uses of those plots. These are addressable with revisions. Relative to the anchors, this paper sits between the rejected Feature Hedging paper (3.5) and the accepted SAE-limitations papers (5.0-6.0) — stronger than the former due to theory and validation, but with overclaiming that pulls it below the latter.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>