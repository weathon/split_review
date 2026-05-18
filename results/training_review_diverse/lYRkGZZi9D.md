## Summary

This paper investigates why weight matching (WM) permutations enable linear mode connectivity (LMC) between independently trained neural networks. It shows that WM does not achieve LMC by making the model weights close in L₂ distance (only 6–20% reduction), but instead by aligning the directions of singular vectors associated with large singular values across layers. This alignment propagates to the merged model and, combined with the empirical finding that inputs preferentially overlap with the top right singular vectors, explains why the merged model's behavior stays close to the originals. The paper further shows that activation matching behaves similarly to WM, while the straight-through estimator (STE) operates on a different principle that makes it less suitable for merging three or more models.

## Strengths

- **Empirical refutation of the distance-reduction hypothesis**: Table 1 shows WM reduces L₂ distance by only 6–20%, and the Taylor-approximated barrier differs significantly from the true barrier. This directly supports Contribution 1 and motivates the deeper SVD-based analysis.

- **Singular-vector alignment as a compelling mechanism**: Theorem 4.1 proves WM's objective maximizes inner products of singular vectors weighted by singular values. Figure 2 shows that with threshold γ=0.3 (large singular vectors) the alignment metric R increases substantially after WM, while with γ=0 (all vectors) it does not. Figure 3(b) shows that after merging, alignment between merged and original models exceeds 0.8 for MLP. This provides a principled explanation for why WM works.

- **Theoretical link between singular-vector alignment and layer-output similarity**: Theorem 4.2 bounds the difference in hidden-layer outputs in terms of singular-vector inner products weighted by singular values, and Figure 4 shows that inputs have large inner products with large-singular-value right singular vectors. Together, these explain why aligning large singular vectors can keep the merged model's function close even when weight distance remains substantial.

- **Principled contrast between WM and STE**: Tables 2 and 3 demonstrate that STE achieves low barriers without aligning singular vectors (R ≈ 0), and that WM yields substantially lower barriers than STE when merging three models (e.g., MLP on Fashion-MNIST: 0.74 vs. 3.47). This supports Contribution 3 and has practical implications for multi-model merging.

- **Consistency across architectures and datasets**: The claims are validated on MLP, VGG11, and ResNet20 across Fashion-MNIST, CIFAR-10, and CIFAR-100.

## Weaknesses

### Major

1. **The causal link between singular-vector alignment and LMC is not fully closed.** The paper demonstrates a clear correlation — after WM, large singular vectors align and LMC holds — and provides Theorem 4.2 bounding per-layer output differences. However, the step from "layer outputs are closer" to "the full-network loss barrier is small" is never formalized. The bound is per-layer under a fixed input, but LMC is a property of the interpolated *full network's* loss over the data distribution. The paper does not provide a bound on the barrier in terms of alignment, nor does it control for alternative explanations (e.g., joint effects across layers, bias permutations). The conclusion honestly notes "it remains unclear why our analysis can explain the phenomenon so effectively," which concedes this gap. Consequently, Contribution 2 ("Revealing the reason why WM... satisfies LMC") overstates what is actually a plausible and well-supported hypothesis rather than a proven causal mechanism. Addressing this would require either a barrier bound in terms of alignment or a controlled experiment that varies alignment while holding L₂ distance fixed.

### Minor

2. **The analysis of activation matching (AM) is superficial.** Section 5 (roughly one paragraph) notes that AM's objective relates to Theorem 4.2 and that its R values "closely resemble" those for WM. No theoretical argument connects AM to singular-vector alignment beyond this observation. The section adds length without deepening the understanding of AM — the paper's other contributions would not be materially weakened if this section were condensed.

3. **Convolutional architectures are not addressed.** The paper formally analyzes MLPs and states "our analyses in this paper can be applied to any model architectures" (line 27), yet experiments on VGG11 and ResNet20 include convolutional layers. For convolutional layers (4D weight tensors), the SVD requires reshaping into 2D matrices, and the effect of channel permutations on singular vectors differs from the fully connected case. The paper neither discusses this adaptation nor validates that the SVD-based reasoning carries through. This undercuts the claimed generality.

4. **The three-model merging experiment (Table 3) has limited scope.** Only three trials are reported, and the comparison does not explore whether a modified STE procedure (e.g., jointly optimizing permutations for three models) would close the gap with WM. The claim that WM is *intrinsically* more advantageous for ≥3 models goes beyond what the current evidence supports.

### Trivial

5. **The R metric's normalization could be explained more clearly.** The paper states R close to one indicates good alignment but does not explicitly justify why the denominator Σ_ℓ n_ℓ is the correct normalizer given the sum over i,j per layer. The reasoning relies on the orthogonality of singular vectors within each model (which zeros out cross terms when alignment is perfect) — stating this explicitly would improve clarity.

6. **The threshold γ is defined as a ratio to the largest singular value, but the paper does not discuss how sensitive the results are to this specific choice.** The binary choice (γ=0 vs. γ=0.3) is coarse; a sensitivity analysis would strengthen confidence in the claims.

## Nice-to-Haves

- A controlled experiment that *causally* isolates the effect of singular-vector alignment (e.g., constructing permutations that align large singular vectors while keeping L₂ distance unchanged, or vice versa) would transform the correlational evidence into a causal explanation.
- A bound relating the loss barrier directly to singular-vector alignment (accumulated over layers) would close the theoretical gap between Theorem 4.2 and LMC.
- An ablation varying the quality of the Sinkhorn solver (e.g., number of iterations) to check whether lower-quality permutations show weaker alignment and worse LMC would strengthen the analysis.
- A discussion of cases where WM fails to achieve LMC could sharpen the boundaries of the proposed explanation.

## Removed Points

The following points from the reviewers were removed after verification against the paper:

- **"The alignment measure R is not adequately justified / numerator could exceed denominator"** — Removed: This criticism is mathematically incorrect. When singular vectors are perfectly aligned, orthogonal singular vectors within each model make cross terms (i≠j) zero, giving R = 1. The measure is heuristically valid, though the paper could be more explicit about this reasoning (captured in Trivial #5 above).

- **"OCR artifact: Pe˜na et al."** — Removed per instructions: formatting/parser artifacts are not author errors.

- **"Taylor approximation overclaim"** — Removed: The paper's claim ("suggests that reducing the L₂ distance... is not the direct reason") is appropriately cautious; the Taylor analysis serves as a supporting negative observation, not the primary argument.

- **"Sinkhorn algorithm dependence not discussed"** — Moved to Nice-to-Haves: a reasonable suggestion but not a weakness.

- **"Generic strengths" from Strength Finder** — The strength about AM sharing the same principle was retained but qualified as superficial (Weakness #2). The suggestion about "consistency across architectures" was kept as a supporting strength.

## Novel Insights

The paper's core insight — that WM works by aligning the directions of large-singular-value singular vectors while leaving their magnitudes (and thus the L₂ distance) largely unchanged — is genuinely novel and well-supported. The finding that inputs preferentially overlap with the top right singular vectors (Figure 4) elegantly explains why aligning these particular directions is sufficient even when other singular vectors remain misaligned. The observation that indirect alignment propagates to third models (Figure 5) is a useful practical finding with implications for multi-model merging settings like federated learning. None beyond the paper's own contributions.

## Suggestions

1. **Tone down the causal claim**: Reframe Contribution 2 from "Revealing the reason" to "Providing evidence that singular-vector alignment is the mechanism" and explicitly acknowledge the gap between per-layer output similarity and full-network LMC.

2. **Address convolutions explicitly**: Add a discussion (even one paragraph) of how the SVD analysis extends to convolutional layers via reshaping and channel permutations, or clearly scope the claims to fully connected layers.

3. **Deepen or shorten the AM section**: Either provide a theoretical argument connecting AM's objective to singular-vector alignment via the input distribution, or condense it to a brief note.

4. **Add a sensitivity analysis on γ**: Show that the qualitative conclusions hold over a range of threshold values, not just γ ∈ {0, 0.3}.

## Score and Decision

This paper makes a genuine contribution by revealing a plausible mechanism for LMC via WM — singular-vector alignment — that goes well beyond the standard "permutations make weights close" narrative. The evidence is coherent, the experiments span reasonable architectures, and the contrast with STE is practically informative. However, the gap between correlational evidence and the claimed causal explanation, combined with the superficial treatment of AM and the unaddressed question of convolutions, prevents the paper from being fully convincing at the level of a top venue. The paper would benefit from a revision that either closes the causal gap or appropriately caveats the claims.

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**