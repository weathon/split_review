Now I have all the information I need. Let me carefully construct the consolidated review, verifying each claim against the paper.

---

## Summary

This paper identifies a previously unreported instability in two natural sparsifying activation functions (shifted ReLU and soft thresholding) that prevents deep networks from training at high sparsity. The instability arises because the slope of the Gaussian process variance map at the fixed point equals the edge-of-chaos parameter χ₁, so EoC initialization forces V'(q*)=1, and the positive second derivative makes the fixed point only stable from the left. The authors propose clipped variants (CReLU and CST) that decouple χ₁ from V'(q*), guaranteeing V'(q*) < 1 at χ₁ = 1. Proof-of-concept experiments on 100-layer DNNs (MNIST) and 50-layer CNNs (CIFAR-10) demonstrate trainability at sparsities up to 85% with the clipped variants, while the original activations fail at sparsities as low as 50–60%.

## Strengths

- **Formal identification of the instability mechanism**: The paper analytically proves that for shifted ReLU and soft thresholding, V'ₚₕᵢ(q*) = χ₁,ₚₕᵢ and V''ₚₕᵢ(q*) > 0 at EoC (Table 1, Section 2). This is a previously unrecognized failure mode that explains why these natural sparsifying activations cannot train deep networks. The proof is clean and the connection between the variance map and correlation map is well explained.

- **Principled resolution via magnitude clipping**: The clipped variants CReLU and CST (Eqs. 4–5) are shown to satisfy χ₁ = V'(q*) + (positive term) (Eqs. 10–11), guaranteeing V'(q*) < 1 at χ₁ = 1. This is a simple, elegant modification that directly addresses the identified instability. The analysis of how m controls V' and V'' (Figure 4) provides practical guidance for choosing the clipping magnitude.

- **Convincing experimental validation of the fix**: Table 2 shows DNNs on MNIST with CReLU/CST achieving 92–95% test accuracy at sparsities up to 85%, with 5-run statistics. In contrast, the non-clipped variants fail to train at sparsities as low as 50–60%. The gradient-norm plots (Figure 5) confirm that the mechanism of failure (exploding gradients in the clipped variants for large m) matches the theoretical prediction.

- **Nuanced analysis of failure modes**: The paper distinguishes between failures due to large V''(q*) (first mode, matching the theory) and failures due to small m / limited expressivity (second mode). This adds depth beyond a simple "clipping fixes everything" narrative.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by theory and experiment. No weakness identified by the reviewers fundamentally undermines the contribution.

### Minor

- **The finite-width stability argument remains heuristic rather than formally proven.** The paper proves that V'(q*)=1 and V''(q*)>0 for the unclipped activations, and argues that finite-width fluctuations will push q^l above q*, where convexity causes divergence (line 68: "Due to the natural stochasticity of q^l for finite dimensional networks... q^l typically obtains a value in excess of q^* and then diverges"). This intuition is plausible and consistent with the experiments, but no formal bound on the finite-width variance or proof that divergence is inevitable is given. The experimental evidence is strong enough to carry the paper (the non-clipped activations indeed fail to train across nearly all sparsity levels), but readers expecting a theorem-level guarantee will be left wanting. The paper's own framing makes this clear — it is a plausible mechanism supported by experiments.

- **The second failure mode (high sparsity, small m) is acknowledged but not explained in the main text.** The paper notes (lines 277–278) that at 85% sparsity with small m, accuracy drops despite EoC initialization avoiding exploding gradients, and attributes this to "limited expressivity" with a reference to the appendix. While the appendix discussion exists in the original submission, the main text provides no sketch of the mechanism — e.g., whether the small clipping magnitude makes the activation nearly flat over the active region, reducing the effective gradient signal. This is listed as future work in the conclusion, which is honest, but the current analysis of this mode stops short.

- **CNN experiments lack replication.** Table 2 reports standard deviations over 5 runs for DNNs but states "a single experiment was conducted for each hyperparameter combination" for CNNs (caption, line 264). Given the high variance observed in some DNN configurations (e.g., std=0.37 for ReLUτ at s=0.6), individual CNN numbers should be interpreted cautiously. The overall trend is consistent with the theory (clipped variants train, non-clipped fail), and the DNN experiments provide the primary evidence, but the CNN results are less reliable as point estimates. Replication with even 3 runs would increase confidence, particularly for boundary cases.

### Trivial
None.

## Nice-to-Haves

- **Extension to larger-scale settings (ImageNet, transformers, ResNets).** The paper acknowledges this as future work. Demonstrating that the proposed activations work beyond MNIST/CIFAR-10 in more realistic training regimes would substantially increase the practical significance, but the paper's scope as a theoretical proof-of-concept is clearly stated and appropriately scoped.

- **Quantitative measurement of computational savings** (e.g., actual FLOPs reduction from activation sparsity). This would strengthen the applied message but is secondary to the paper's theoretical focus on initialization stability.

- **Comparison of gradient norms for successful vs. failed runs of the clipped activations.** Figure 5 shows exploding gradients for failed runs; showing the gradient norms for a successful run at the same sparsity but lower m would complete the picture.

- **Measurement of backward-pass sparsity** (nonzero gradient fraction) in addition to forward-pass activation sparsity, to strengthen the case for computational efficiency.

## Removed Points

- **Criticism about "V'_{cst}(q) = 2 V'_{cst}(q)" being an OCR error**: Removed per hard rules — this is a parser/formatting artifact, not an author error. The original submission does not contain this self-referential equation.
  
- **Criticism about missing computational cost measurements**: The critic themselves notes the omission is reasonable given the paper's focus on initialization theory. Removed as non-substantive.

- **Criticism about limited experimental scope being a defect**: The critic acknowledges "it is not a defect of the paper's own framing." The paper explicitly calls its experiments "proof-of-concept." Removed as scope-creep — evaluating against the wrong class of expectations.

- **Criticism about missing comparison of gradient norms for successful runs**: Moved to Nice-to-Haves; does not affect the core claim.

- **Criticism about missing measurement of gradient sparsity during training**: Moved to Nice-to-Haves.

## Novel Insights

The single most insightful observation across the reviews is that the paper's central contribution — that V'ₚₕᵢ(q*) = χ₁,ₚₕᵢ for these sparsifying activations — is both the source of the problem and, via the clipping modification, the lever for the solution. The reviewers correctly note that the finite-width instability argument is heuristic, but this does not diminish the theoretical contribution: the paper proves a structural property of the variance map that had not been previously recognized, and the empirical evidence across two architectures and datasets confirms the prediction. The second failure mode (performance drop at high sparsity + small m) is the most interesting unexplored direction: it suggests a fundamental trade-off between stability and expressivity that may require a more nuanced characterization than the current V' / V'' analysis provides.

## Suggestions

- Add 3-run replication for the CNN experiments (or at least for the boundary cases where accuracy drops) to improve reliability of those results.
- Provide a brief sketch of the second failure mode's mechanism in the main text, even if a full analysis is deferred to the appendix — e.g., explicitly connect small m to reduced dynamic range and consequently reduced gradient signal in the active region.
- Consider adding a heuristic bound or practical guideline that connects m, width, and sparsity to guarantee variance-map stability with high probability, strengthening the heuristic finite-width argument.

## Score and Decision

**Originality**: High. The instability identified is novel and not previously reported. The clipping fix is simple but principled.

**Importance**: Moderate to high. Sparsity-inducing activations are practically motivated, and understanding why they fail to train is valuable.

**Claims supported**: Yes, the core claims are supported by theory and the experimental evidence is consistent.

**Soundness**: Good. The theoretical derivations are correct, and the experiments match the predictions. Minor concerns about CNN single-run results.

**Clarity**: Good. The notation is clear, and the theoretical reasoning is well laid out.

**Value**: The paper provides a clean theoretical result with practical implications. It is a solid contribution to the initialization theory literature.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>