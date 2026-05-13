## Summary
The paper introduces Similarity Group Equivariant CNNs (SECNNs), which use a refined Analytical Fourier-Mellin Transform (AFMT) basis—made approximately shiftable, steerable, and scalable—to parameterize 5D convolution kernels over the similarity group Sim(2) ≅ ℝ² ⋊ (SO(2) × ℝ⁺ × {±1}). The authors extend the basis to handle horizontal reflection, build a tractable 5D steerable construction via orthogonalized coordinates, and evaluate on TRS-MNIST (where they report strong gains) and CIFAR10/100.

## Strengths
- **Novel 5D steerable construction.** The decomposition in Eq. 13, expressing the 5D basis as a product of two 2D AFMT bases over orthogonalized coordinates, is a non-trivial reduction that makes a full-similarity-group steerable parameterization computationally tractable.
- **Strong TRS-MNIST result.** SECNN-Mix attains 0.64% error on translated+rotated+scaled MNIST, vs. 2.13% for Sim2CNN and 16.81% for E2CNN (Table 2), directly supporting the claim that the shiftable basis helps under simultaneous continuous transformations.
- **Reflection/Dihedral extension.** Eqs. 11–12 cleanly extend the basis to include horizontal reflection, enabling full discrete similarity (Dihedral × continuous trans/scale) equivariance.
- **Candid negative finding on frequency-domain ReLU.** Section 4 honestly reports that frequency-domain nonlinearity is sub-optimal and gives a mechanistic explanation (Cauchy-Riemann), rather than burying the result.

## Weaknesses

### Fatal
None.

### Major
- **No direct measurement of equivariance error.** The central technical claim is (approximate) continuous similarity equivariance, yet nowhere in the paper is feature-map equivariance error measured as a function of continuous rotation, scale, or sub-pixel translation. Classification accuracy on TRS-MNIST is a weak proxy: gains there can also come from kernel parameterization, augmentation-like effects, or architectural choices. Without an equivariance-error curve compared against E2CNN/SESN/SREN, the headline claim is supported only indirectly.
- **CIFAR results do not cleanly support the abstract's claim of "comparable to leading group equivariant networks."** Section 5 itself concedes SECNN ranked third on CIFAR100 and that the comparison is confounded by widen-factor=1 vs. wider baselines. The authors should either run parameter-matched baselines (WRN16-8 with widen-factor 1) or soften the abstract.
- **Uncontrolled 3D-vs-4D-weight ablation.** The paper attributes SECNN-4D's worse performance to channel count, not to weight dimensionality, but channels and weight dimensionality vary together. This is the only ablation isolating the value of higher-dimensional weights, and as it stands it cannot adjudicate the central design choice.

### Minor
- **Differentiation from B-spline/MLP work is partly at the parameterization level, not the operator level.** The argument in Sec. 1.1 that prior work only achieves discrete translation equivariance applies primarily because the convolution is performed on a uniform grid. SECNN's implementation (Eq. 16, PyTorch unfold per Sec. 6) is also a standard discrete grid convolution with a spatially cropped 5×5 kernel, so the *operator* delivers only discrete translation equivariance; the shiftable property is a kernel-parameterization advantage. A more careful framing would help.
- **Locally-compact extension of Kondor & Trivedi (2018) is asserted rather than established.** The paper notes Sim(2) is only locally compact and that a Haar measure exists, but does not formally argue the convolution-equivariance correspondence carries over. A brief justification or citation would close this gap.
- **Equivariance loss at domain conversions is unquantified.** Frequency↔spatial domain hops around ReLU/BN necessarily incur resampling/IAFMT error on finite grids, compounding the approximate equivariance — how much is lost is not measured.
- **No analysis of the impact of $X$, $S$, and the 5×5 spatial crop** on equivariance fidelity at varying scales/rotations, nor any aliasing analysis beyond stating the 1024×1024 precomputation grid.
- **Scalability is a real limitation.** ~154 GB memory and 20 hours for a CIFAR run on 4×A100 (Sec. 5) materially limits the method's reach; the simConv-as-4D-conv cost (Sec. 6) is acknowledged honestly but unresolved.

### Trivial
- Table 1's binary checkmarks for "continuous" equivariance without a tolerance or measurement criterion are misleading given that SECNN itself is only approximately shiftable/scalable.

## Nice-to-Haves
- An evaluation on a dataset where continuous scale equivariance genuinely matters (aerial/medical imagery, feature matching as motivated in Sec. 1) — CIFAR has essentially no scale variation, so the scale machinery is largely untested where it should matter most.
- Visualizations of learned kernels under continuous rotation and scaling from the same learned $G$ coefficients, demonstrating faithful transformation.
- A controlled 3D-vs-4D-weight ablation at matched channel/parameter count.

## Removed Points
These points are flagged as removed; treat them with caution.
- *Harsh critic's complaint about Table 1 / CIFAR10 numbers being PDF images.* — Parser artifact, not a paper defect.
- *Complaints about non-orthogonal coordinate change in Eq. 13 not being "proven."* — The paper provides the algebraic decomposition; demanding a formal proof is borderline scope creep for an empirical systems paper and is partially addressed in the construction.
- *Strength: "addresses an important problem of unifying rotation, scale, reflection."* — Generic framing; subsumed by the more concrete strength about the 5D construction.
- *Strength: "competitive CIFAR10/100 accuracy."* — Conflicts with the verified weakness that CIFAR100 is not actually competitive by the authors' own description; weakness wins.

## Novel Insights
None beyond the paper's own contributions. The principal novelty is the orthogonalized 5D steerable AFMT construction (Eq. 13) and its reflection extension.

## Suggestions
- Add an equivariance-error experiment: plot feature-map L2 error vs. continuous rotation angle, scale factor, and sub-pixel shift for SECNN vs. E2CNN/SESN/SREN.
- Rerun a parameter-/FLOP-matched CIFAR comparison, or weaken the abstract's CIFAR claim to match Section 5's framing.
- Provide a controlled 3D vs. 4D weight ablation with matched channel counts.
- Quantify equivariance degradation at each spatial↔frequency conversion.
- Soften the differentiation argument vs. B-spline/MLP methods: the advantage is at the kernel-parameterization level, not at the convolution operator level (which is still discrete-grid).

## Evaluation
- **Originality:** Solid. The 5D AFMT-based steerable parameterization with reflection extension is a real contribution.
- **Importance:** Moderate. Full similarity-group equivariance is a recognized open problem.
- **Claim support:** Weak on the central equivariance claim (no direct measurement) and overstated on CIFAR.
- **Soundness of experiments:** Mixed. TRS-MNIST is convincing; CIFAR is confounded; the key ablation is uncontrolled.
- **Clarity:** Reasonable, with candid acknowledgments of limitations.
- **Value to community:** A useful construction worth exposing, but the empirical case as presented is incomplete.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>