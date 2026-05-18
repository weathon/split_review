Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces MONet (Multilinear Operator Networks), a polynomial network architecture whose core Poly-MLP layer captures multiplicative interactions via elementwise products of linear projections, without requiring standard activation functions (ReLU, GELU, etc.). The paper demonstrates that MONet closes a long-standing gap: prior polynomial networks without activation functions topped out at ~70% on ImageNet, while MONet achieves 81.3% (Multi-stage Small variant), matching MLP-based and transformer models of comparable size. Additional contributions include strong robustness on ImageNet-C (best mCE of 49.7 among all compared models) and a demonstration of symbolic recovery for the Lotka-Volterra ODE.

## Strengths

- **First polynomial network to close the performance gap on ImageNet.** Prior polynomial networks without activation functions (Π-Nets at 65.2%, Regularized Π-Nets at 70.2%) fell far short of modern architectures. MONet achieves 81.3% top-1 accuracy, a ~11% absolute improvement, matching MLP-Mixer variants and DeiT-S of comparable parameter count. This is a genuine empirical advance (Table 1).

- **State-of-the-art robustness on ImageNet-C.** MONet achieves the lowest mean corruption error (mCE=49.7) among all compared models, substantially outperforming CycleMLP (53.7), HireMLP (51.9), and prior polynomial networks (Π-Net at 73.8). It ranks first across all four corruption categories (Noise, Blur, Weather, Digital), often by a large margin (Table 3).

- **Ablation confirms the Poly-MLP layer is the primary driver of performance.** Replacing the Poly-MLP layer with a standard MLP layer causes accuracy to drop from 82.94% to 67.61% on ImageNet-100; removing it entirely (linear-only block) yields only 55.11%. This cleanly isolates the contribution of the multiplicative interactions (Table: Module ablation).

- **Competitive performance on small and fine-grained datasets.** MONet achieves best or tied-best accuracy on CIFAR10 (94.8%), SVHN (97.6%), and Oxford Flower (95.0%), outperforming prior polynomial networks and CNNs, demonstrating generalization beyond large-scale ImageNet (Table 2).

## Weaknesses

### Fatal

None. The paper's core empirical contribution is valid and reproducible in principle.

### Major

- **The paper's central claim of "solely multilinear operations" is contradicted by the use of layer normalization.** The abstract states the model "relies *solely* on multilinear operators"; the introduction states it is "based solely on multilinear operations"; the conclusion states it "leverages *solely* linear and multilinear operations." However, the architecture includes layer normalization (explicitly shown in Figure 1 and described in Section 3.2, line 114), which involves computing means, variances, division, and square roots — operations that are not multilinear and cannot be expressed as addition/multiplication. The FHE motivation (Section 1) specifically requires that only addition and multiplication be supported, making layer normalization equally problematic as any activation function for that use case. This does *not* invalidate the empirical results, but it means the paper overstates its architectural constraints. The authors must either remove layer norm, justify a class of permissible nonlinearities, or honestly reframe the claim to "no standard activation functions" rather than "solely multilinear."

- **The ODE symbolic recovery claim is unsubstantiated.** The paper states that MONet "can recover the equations behind the dynamic system and explicitly restore the symbolic representation" and displays learned coefficients nearly identical to the ground truth (e.g., 1.12001 vs 1.12). However, it never explains *how* the symbolic form is extracted from the trained network parameters. If the architecture's weights directly encode polynomial coefficients because the functional form matches, this mapping must be explicitly described. If the coefficients are read from specific weight matrices, which ones correspond to which terms? Without this explanation, the claim amounts to "the network fits the trajectory well and the coefficients happen to match" — which is weaker and potentially misleading. This section requires an explicit description of the extraction procedure and a discussion of what conditions (known degree, known structure) enable it.

### Minor

- **The 4^N degree claim is stated without qualification.** The paper asserts each block captures "up to 4th degree interactions" and that stacking N blocks yields "up to 4^N interactions, with N>10 in practice." While mathematically correct as a worst-case combinatorial bound, this implies degrees on the order of 4^10 ≈ 1 million without accounting for rank constraints (shrinkage ratio), bottleneck dimensions, or residual connections that limit expressivity. The paper acknowledges this as future work in a footnote and limitation section, but the unqualified claim in the main text is misleading about the model's effective capacity. An empirical analysis (e.g., testing response to input scaling) would strengthen this claim considerably.

- **The multi-stage architecture is used for ImageNet results but not described in the method section.** Table 1 presents Multi-stage variants with stage-specific hidden sizes and block counts, and these are the models that achieve the best ImageNet results (81.3%). However, Section 3.2 (Network Architecture) describes only a homogeneous stack of blocks and does not explain how stages are formed, what downsampling/pooling operation connects them, or how the pyramid patch embedding interacts with the staged design. This is a reproducibility gap.

- **The pyramid patch embedding is described too briefly for reproducibility.** The method section devotes only a few sentences (Section 3.2, lines 121) to this component, yet the ablation shows it provides meaningful gains. How are the two levels (sizes 7 and 14) combined? Are features pooled, then concatenated or summed? Is there a separate embedding for each level? The current description is insufficient to reproduce the method.

- **The novelty relative to prior polynomial networks (Π-Nets, PDC) is under-articulated.** The paper cites Π-Nets and PDC as closely related but does not clearly contrast the design assumptions or explain *why* the specific form of Eq. (1) — a low-rank factorization with two branches at different ranks, an elementwise product, and a residual — is effective. The reader is left to guess whether gains come from the multiplicative block, the token-based framework, the pyramid embedding, or scaling.

### Trivial

- The conclusion states that MONet "outperforms modern transformers models" — this is overbroad; MONet is on par with but does not uniformly outperform ViT/DeiT variants across all model sizes.

## Nice-to-Haves

- An analysis of effective polynomial degree via input scaling experiments (e.g., measuring how output changes when all input entries are scaled by a scalar).
- Extending the controlled ablation (Poly-MLP vs. standard MLP) from ImageNet-100 to the full ImageNet, to confirm the pattern holds at scale.
- A comparison against a simple linear-only MLP-Mixer baseline (no activations) on a small dataset, though the ablation already covers this direction on ImageNet-100.

## Removed Points

- **"The proposition and proof can be omitted"** — This is an editorial opinion, not a weakness of the paper. The proposition is a simple formal statement that clarifies what the layer does; its inclusion is a matter of presentation taste.
- **"The paper should compare against an MLP-Mixer with only linear layers (no activations) on ImageNet-100 or a small dataset"** — The ablation study already performs this comparison on ImageNet-100 (Linear Block at 55.11% vs. MONet at 82.94%). The suggestion to repeat on full ImageNet is a nice-to-have, not a weakness.
- **"Paper should provide a controlled comparison on ImageNet with the same token-based architecture but replacing the Poly-MLP with standard MLP"** — Already done on ImageNet-100. Extending to full ImageNet is expensive and the pattern is already clear.

## Novel Insights

The juxtaposition of reviewer criticisms reveals an interesting tension: the harsh critic's most damning point (layer normalization violates "solely multilinear") is structurally separate from the paper's strongest empirical result (closing the ImageNet gap). This means the paper's scientific contribution and its framing are decoupled — the contribution is real (competitive polynomial network without activation functions), but the framing is overstated. The practical implication is that the paper could be substantially improved by simply reframing its claims more carefully, without any additional experiments. This is a rare case where the fix is primarily in writing, not in experimentation.

## Suggestions

1. **Honestly reframe the core claim.** Replace "solely multilinear" with "no standard activation functions (ReLU, GELU, etc.)" or clearly disclose that layer normalization is a nonlinear component and discuss whether it poses practical issues for the FHE motivation. This single change would resolve the most serious weakness.

2. **Explain the symbolic extraction procedure for the ODE experiment.** Describe exactly how the displayed coefficients are read from the trained network's parameters. Without this, the interpretability claim is not reproducible.

3. **Add a description of the multi-stage architecture to Section 3.2.** Explain how downsampling/transition between stages works, how hidden sizes change, and how the pyramid patch embedding feeds into the staged design.

4. **Qualify the 4^N degree claim** with a discussion of rank and width limitations, or provide an empirical measurement of effective degree.

5. **Expand the pyramid patch embedding description** to make it reproducible.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>