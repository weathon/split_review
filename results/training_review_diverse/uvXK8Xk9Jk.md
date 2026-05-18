I now have a complete understanding of the paper and the reviews. Let me produce the final consolidated review.

---

## Summary

This paper identifies a previously unreported training instability in deep networks that use shifted ReLU (relutau) and soft-thresholding (st) sparsifying activation functions. It proves that at Edge-of-Chaos (EoC) initialization, these activations yield a variance map derivative V'=1 with positive curvature V''>0, causing the layerwise variance to diverge under finite-width stochasticity. The paper proposes magnitude-clipped variants (crelu, cst) and proves analytically that clipping ensures V' < 1 at the EoC, restoring stability. Proof-of-concept experiments on 100-layer DNNs (MNIST) and 50-layer CNNs (CIFAR-10) validate the theory and demonstrate trainability up to 85% activation sparsity with accuracy comparable to the ReLU baseline.

## Strengths

- **Identifies a genuine, theoretically characterized instability for sparsifying activations.** The paper proves that shifted ReLU and soft thresholding have V'_φ(q*) = χ_{1,φ} at the fixed point, so EoC initialization forces V'=1, and that V'' > 0 makes the fixed point unstable from the right. This is a clean theoretical result that explains why these natural sparsifying activations fail to train. Table 1 (lines 119-126) gives explicit closed-form derivatives.

- **Proposes a simple clipping fix with analytical proof of restored stability.** The clipped variants (crelu, cst) ensure χ₁ > V'(q*) (Equations 14-16, lines 164-167), so at the EoC (χ₁=1) we have V'(q*) < 1, making q* locally stable. The analysis connects the second derivative V''(q*) to practical training failure via variance map bifurcation (Figures 4-5).

- **Demonstrates high activation sparsity with retained accuracy in both DNNs and CNNs.** Table 2 (lines 217-262) shows that clipped activations achieve ~94% test accuracy on MNIST (DNN) and ~70% on CIFAR-10 (CNN) with sparsity up to 85%, while unclipped variants fail to train at sparsities above 50-60%. The ReLU baseline is reported in the same table (relutau, τ=0, s=0.5: accuracy 0.94 for DNN, 0.70 for CNN), confirming the "close to full accuracy" claim.

- **Provides explicit formulae and practical guidance for choosing τ and m.** Table 1 (lines 119-126) gives τ as a function of target sparsity (τ̂_φ(s,q*)), and Figure 3 (lines 171-176) plots V'(m) and V''(m) for different sparsities, enabling practitioners to select m. The paper identifies two distinct failure modes (large m → gradient explosion; small m at very high sparsity → reduced capacity).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Equation typo in Section 3 (line 155).** The equation reads `V'_{\cst}(q) = 2 V'_{\cst}(q)`, which is self-referential and incorrect. From context and the analogous χ₁ relationship (line 161, which is correct), it should read `V'_{\cst}(q) = 2 V'_{\crelu}(q)`. The logical argument is unaffected because the key inequality (lines 164-167) uses the correct relationship, but this typo could confuse readers and should be corrected.

- **"Optimal τ" phrasing is ambiguous (line 134).** The paper states "The optimal (smallest) τ...for activation sparsity s." For a given target sparsity s, τ is uniquely determined by inverting the sparsity formula (Φ(-τ/√q*) for shifted ReLU). "Optimal" suggests a free optimization that does not exist; "required" or "the τ that achieves sparsity s" would be clearer.

- **"Previously unreported" claim could be softened.** The paper's claim (abstract, Section 1) that this instability is "previously unreported" is defensible but the paper does not discuss related phenomena for activations with zero-gradient regions (e.g., hard tanh, hard sigmoid) in the ordered/chaotic regime literature. A brief acknowledgment of this context — clarifying that what is new is the *combination* of V'=1 and V''>0 at the EoC for these specific activations, plus the clipping fix — would strengthen the framing.

- **Second failure mode receives only brief mention in the main text.** The failure at very high sparsity (85%) with small m (reduced accuracy despite stable gradients) is discussed in one paragraph (lines 277-278) and deferred to the appendix. This second mode may be as practically important as the gradient-explosion mode, and a slightly expanded discussion in the main text connecting it to the theory (small m caps activation magnitudes, limiting effective network capacity) would improve the paper.

### Trivial
- **The ReLU baseline in Table 2 could be explicitly labeled.** The first row (relutau, τ=0, s=0.5) is standard ReLU, and its accuracy (0.94 DNN, 0.70 CNN) serves as the baseline for the "close to full accuracy" claims. While the data is present and the paper states on line 64 and line 86 that relutau with τ=0 is ReLU and serves as the baseline, adding an explicit "ReLU baseline" label in the table would prevent reader confusion.

## Nice-to-Haves
- A short one-sentence practical guideline in Section 3.2 for choosing m (e.g., "choose m such that V'(q*) ≤ 0.7 and V''(q*) is sufficiently negative to avoid bifurcation"), summarizing the discussion.

## Removed Points
These points are flagged by the reviewer but are factually incorrect, misunderstand the paper, or violate the review rules. Treat with caution.

- **"Missing ReLU baseline"** (Critic's Critical Issue #1): Removed because it is factually incorrect. The paper *does* report the ReLU baseline accuracy. The first row of Table 2 (relutau with τ=0, s=0.5) IS standard ReLU — the paper explicitly states on line 64 that "ReLU (i.e. relutau with τ=0)" and references "full test accuracy of a standard ReLU network baseline" on line 86. The baseline values are 0.94 (DNN on MNIST) and 0.70 (CNN on CIFAR-10). The "close to full accuracy" claim (e.g., 0.93-0.94 for DNNs at 85% sparsity vs. 0.94 baseline) is directly verifiable from the table. The critic's assumption that the ReLU baseline might be 0.98 is speculative and unsupported.

- **"CNN architecture details missing"**: Removed because the paper states depth=50, channels=300, 1D-style CNN (line 267). Further architectural specifics (pooling, strides) are standard implementation details that belong in the appendix, which the parser strips from all submissions. Per review rules, criticisms about missing appendix content are removed.

- **"Add more benchmarks (ResNet, CIFAR-100, transformer)"**: Removed as scope creep. The paper is explicitly a proof-of-concept (line 267: "The absolute accuracy of the networks is not the focus of these experiments, rather it is the ability to retain trainability and approximately the accuracy of standard ReLU networks"). Demanding a broader benchmark suite would turn this into a different, more engineering-oriented paper rather than a stronger version of the theoretical contribution presented.

- **"Missing discussion of dynamical isometry"**: Removed because the paper already addresses this — line 134 states that the EoC σ_w² independent of q* "makes achieving approximate dynamical isometry...impossible," and line 169 notes that clipping does not change this ("unfortunately still does not enable us to achieve approximate dynamical isometry"). The paper explicitly flags what its approach does *not* accomplish.

## Novel Insights

None beyond the paper's own contributions. The review process did not uncover any perspective on the contribution that the authors themselves have not already articulated.

## Suggestions
1. Correct the equation typo on line 155 (`V'_{\cst}(q) = 2 V'_{\crelu}(q)` rather than `V'_{\cst}(q) = 2 V'_{\cst}(q)`).
2. Replace "optimal (smallest) τ" with "required τ" or "the τ that achieves sparsity s" on line 134.
3. Soften the "previously unreported" claim by briefly acknowledging related EoC phenomena for activations with zero-gradient regions (e.g., hard tanh) and clarifying what is new: the specific V'=1 with V''>0 combination and the clipping fix.
4. Label the ReLU baseline row in Table 2 explicitly (e.g., add a note that relutau with τ=0 is standard ReLU and serves as the accuracy baseline).

## Score and Decision

The paper makes a genuinely novel theoretical contribution — identifying and explaining a previously unrecognized initialization instability for sparsifying activations — and proposes a simple, effective fix grounded in the analysis. The theoretical derivations are rigorous and well-structured. The experiments, while limited in scope (two architectures, two datasets), cleanly validate the theoretical predictions. The weaknesses are presentation-level issues (one equation typo, ambiguous phrasing, minor framing) that do not threaten the core claims. The ReLU baseline, contrary to one reviewer's claim, is present in the table and supports the paper's accuracy claims.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>