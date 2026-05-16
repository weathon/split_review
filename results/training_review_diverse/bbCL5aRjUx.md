Now I have thoroughly verified all claims against the paper. Here is my consolidated review.

---

## Summary

This paper introduces Multilinear Operator Networks (MONet), a polynomial network whose core Poly-MLP layer uses only linear projections and elementwise products (no activation functions) to capture multiplicative interactions between token elements. The key empirical contribution is that MONet closes the large performance gap between prior polynomial networks and modern architectures on ImageNet (81.3% top-1 for MONet-S vs. 65.2% for Π-Nets, a ~16% improvement), while also demonstrating strong robustness to corruptions and an interpretable application to neural ODE recovery.

## Strengths

- **Closes the performance gap between polynomial networks and modern architectures.** Multi-stage MONet-S achieves 81.3% top-1 accuracy on ImageNet with 32.9M parameters and *no activation functions*, while the previous best pure polynomial network (Π-Nets) reaches only 65.2% with 12.3M parameters (Table 2). This ~16% improvement is the paper's strongest result and convincingly demonstrates that activation-free polynomial networks can now compete in large-scale image recognition.

- **Superior robustness across all corruption categories on ImageNet-C.** MONet achieves a mean Corruption Error of 49.7, the lowest among all compared models including CycleMLP (53.7), HireMLP (51.9), and DeiT (54.6) (Table 4). It outperforms every competitor in the "Weather" and "Digital" corruption groups, which is a genuine empirical finding.

- **Comprehensive ablation study validates each design choice.** Table 5 shows that replacing the Poly-MLP layer with a standard MLP layer drops top-1 accuracy from 82.94% to 67.61%, while removing only the spatial shift still gives 81.50%. Tables 6–9 (hidden size, depth, shrinkage ratio, patch embedding) further isolate contributions, giving strong empirical support for each architectural decision.

- **Competitive performance on small and fine-grained datasets.** On Oxford Flower, MONet achieves 95.0% top-1, outperforming S²MLP-Deep-S (93.0%) and all previous polynomial networks (Table 3). This shows the model generalizes beyond ImageNet and works in data-limited regimes.

- **Scientific computing application with interpretable ODE recovery.** In the Lotka-Volterra experiment, the learned coefficients match ground truth to five decimal places (e.g., β: 1.12 vs. 1.12001, γ: 1.21 vs. 1.21001) in under 20 epochs (Section 4.3, Figure 2). This provides a concrete demonstration that activation-free polynomial models can recover exact symbolic dynamics—an advantage unique to this approach.

## Weaknesses

### Fatal
None.

### Major
None that cannot be addressed.

### Minor

- **Imprecise claim about "solely multilinear operators."** The abstract and conclusion state that MONet "relies *solely* on multilinear operators" / "leverages *solely* linear and multilinear operations," yet the architecture uses layer normalization between Poly-MLP blocks (line 93, 114). Layer normalization in its standard form involves mean, variance, and division—operations beyond addition and multiplication. While this does *not* invalidate the core contribution (the paper's primary motivation is eliminating activation functions, and LayerNorm contains no activations), the wording is technically overclaimed. The paper would be more accurate stating that the *core computation* is multilinear and the architecture avoids activation functions.

- **ImageNet comparisons use published numbers without controlling for training recipe.** In Table 2, MONet is compared with baselines from prior papers using different training setups. The paper's training recipe (AdamW, batch size 448, 300 epochs, label smoothing, CutMix, Mixup, auto-augment—line 157) is more aggressive than what some baselines used (e.g., ResMLP-12). While this is standard practice in the vision literature and the paper's main claim (outperforming prior polynomial nets by ~10%) is unaffected, the claim of being "on par with modern architectures" would be strengthened by re-implementing a few key baselines with the same training pipeline.

- **MONet-B configuration used in robustness experiments is not specified.** The model labeled `\modelnamePMB{}` in Table 4 (achieving best mCE of 49.7) does not appear in Table 1's configuration specifications. Its parameter count, FLOPs, depth, and hidden size are unknown, making it difficult to compare fairly with the listed baselines.

- **Pyramid patch embedding is underspecified.** The description (line 121) says the scheme "operates by considering embeddings at smaller scales and subsequently extracting new patch embeddings on top" but does not explain how the scales are combined (concatenation? averaging? separate Poly-MLP?). This is a claimed contribution (line 27) but is not reproducible from the current description.

- **Neural ODE experiment is a single proof-of-concept.** The Lotka-Volterra recovery (Section 4.3) is a convincing demonstration for a 2-variable polynomial ODE with 100 training points, but the paper does not explore non-polynomial dynamics (e.g., trigonometric/exponential terms) or compare with other polynomial baselines (e.g., Pi-Nets) on this task. The paper frames this as an "illustration," but the scope is very limited relative to the claim of "interpretable" scientific computing.

- **No runtime/throughput comparison.** The paper reports FLOPs but not actual inference time. Given that multiplicative interactions can be computationally expensive, a wall-clock comparison with MLP-Mixer or ResMLP would help practitioners assess practical trade-offs.

### Trivial

- The "Limitation" section (line 436) focuses solely on theoretical characterization and does not mention the LayerNorm overclaim or the preliminary nature of the ODE experiment.

## Nice-to-Haves

- An analysis of the effective polynomial degree used in practice (e.g., via perturbation or rank analysis of learned weights) would strengthen the theoretical motivation about capturing high-degree interactions.
- Extending the ODE experiment to a non-polynomial system (e.g., damped harmonic oscillator with linear+sine terms) to explicitly test the limits of the approach.

## Removed Points

These points were flagged by reviewers but are excluded from the main assessment with justification:

- **"The 'solely multilinear' claim is a structural issue that undermines the primary motivation"** — The critic framed this as fatal. The paper's primary motivation (FHE compatibility through avoiding *activation functions*) is not invalidated by LayerNorm, which does not contain activation functions and can be handled via polynomial approximations in FHE contexts. The wording is imprecise but not structurally fatal. Moved from Fatal to Minor.

- **"Proposition 1 is trivial"** — The critic called Proposition 1 trivial. Proposition 1 states that the layer captures multiplicative interactions. While simple, it formalizes the claim and is standard for architecture papers. This is not a genuine weakness.

- **"The 4^N claim is stated without derivation"** — The paper states the proof is deferred to the appendix (line 106: "the proof of which is in \cref{sec:poly_mixer_app_proof_proposition}"). The appendix was stripped by the parser. Per Hard Rules, missing appendix content should not be flagged.

- **Missing related works** — The critic did not raise this, but per instructions, I do not add missing related works.

- Strength Finder strength about "enables interpretable recovery of symbolic ODE equations" — Retained; it is well-evidenced by the paper.

## Novel Insights

None beyond the paper's own contributions. The key insight—that polynomial networks can close the gap with modern architectures through careful design using rank-factorized multiplicative interactions—is well articulated by the paper itself.

## Suggestions

1. **Correct the "solely multilinear" overclaim** in the abstract and conclusion. Replace with language like "the core computation uses only linear and multilinear operations" or "the architecture avoids all activation functions."

2. **Specify the MONet-B configuration** used in the robustness experiments (Table 4) in a new row of Table 1 or in the caption.

3. **Provide a more detailed description of the pyramid patch embedding** sufficient for reproduction: explain how the two scales interact (concatenation, separate processing, etc.).

4. **Re-implement 1–2 MLP baselines** (e.g., ResMLP-12, CycleMLP-T) with the same training recipe and report the results side-by-side, to verify whether the "on par with modern architectures" claim holds under controlled conditions.

5. **Report inference throughput** (images/sec) for the main model configurations alongside FLOPs.

## Score and Decision

The paper makes a clear empirical contribution: it introduces a polynomial network architecture that significantly outperforms all prior polynomial networks (~16% on ImageNet) and achieves accuracy competitive with modern MLP/transformer models using *no activation functions*. The ablations convincingly attribute gains to the multiplicative interactions. The robustness results are genuinely impressive. The weaknesses are real but addressable—the most serious is an imprecise claim in the abstract, not a flaw in the method itself.

**Originality**: Good — the rank-factorized multiplicative interaction design is a principled contribution.
**Importance**: High — demonstrating that activation-free polynomial networks can compete closes an open gap.
**Claims support**: Mostly good, though the "solely multilinear" phrasing is overclaimed and the "on par with modern architectures" claim is slightly weakened by uncontrolled training recipes.
**Soundness**: Solid — the ablations and robustness experiments are thorough.
**Clarity**: Adequate but could be improved on the pyramid patch embedding and MONet-B specification.
**Value**: The paper will likely spur further work on polynomial networks and activation-free architectures.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>