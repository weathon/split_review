Now I have all the information I need. Let me construct the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None

### Major
- weakness 1 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me formulate everything carefully.

---

**Summary**: This paper provides the first complete Riemannian geometric toolkit (exponential/logarithmic maps, parallel transport, geodesic distance) for the Proper Velocity (PV) model of hyperbolic space, which is unconstrained unlike the Poincaré ball or hyperboloid models. Building on this foundation, the authors develop core neural network layers (MLR, FC, convolution, activation, batch normalization) for the PV space and demonstrate numerical stability advantages and competitive performance across image classification, graph node classification, and genomic sequence learning tasks.

**Strengths**:
1. **Demonstrated numerical stability across metrics** (Tables 1–3): PV maintains zero failure rates up to r=1000 in FP32 scalar multiplication while hyperboloid reaches 100% failure by r=200; round-trip error is five orders of magnitude smaller than the Poincaré ball; and gradients remain in a safe band \([1.1\times10^{-4}, 2.1\times10^{-6}]\) whereas Poincaré gradients vanish and hyperboloid gradients explode to NaN.
2. **First complete Riemannian toolkit for the PV model** (Theorems 4.2–4.4): The paper derives closed-form Exp, Log, parallel transport, and geodesic distance for PV space, distinguishing it from prior work that had only gyro- algebraic operations for PV.
3. **Closed-form PV MLR avoiding costly gyroaddition** (Theorem 5.2): The score function depends only on Euclidean inner products, enabling efficient matrix-multiplication implementation without intermediate tensors of size \(b\times C\times n\).
4. **Guaranteed normalization via PV GyroBN** (Theorem 5.4 with ablation in Table 7): Homogeneity properties ensure centering and scaling actually normalize sample statistics, with a practical ablation comparing Fréchet, tangent, and Euclidean variants.
5. **Strong empirical outperformance on genomic sequence learning** (Table 10): PVCNN surpasses both Euclidean CNN and hyperboloid-based HCNN-S on all five TEB tasks, with gains of 5–9 MCC points (e.g., SINEs: 93.78 vs 85.45).

**Supporting strengths**: Ablation studies in Tables 6–9 systematically validate the Riemannian FC layer vs tangent-space alternatives, different normalization strategies, the effect of Exp₀ lifting, and activation variants.

**Weaknesses**:

### Major
1. **Isometry limits geometric novelty; the contribution is a numerically favorable parameterization, not a new geometry.** Theorem 4.2 explicitly establishes that PV and the Poincaré ball are Riemannian isometric — the same hyperbolic geometry in different coordinates. The paper is transparent about this, but the headline framing ("new alternative geometry") overstates what is more precisely described as a numerically stable *coordinate system* for hyperbolic space. This does not invalidate the paper's practical contributions (numerical stability is a real and important concern), but it lowers the bar for theoretical novelty and places the weight of the contribution squarely on the empirical demonstration that numerical advantages translate into consistent performance gains across tasks.

2. **Hyperparameter tuning details and baseline implementation verification are underspecified.** The paper states that all graph-learning models "share the same architecture…they differ only in the underlying hyperbolic model" (Sec. 6.3) and that genomic models "share the same backbone network architecture" (Sec. 6.4). However, no hyperparameter search ranges, learning rates, weight decay values, or tuning protocols are reported for any baseline. Without these details (or released code — the paper promises code release upon acceptance), it is difficult for readers to assess whether the reported performance gaps (e.g., 97.96 vs 92.10 on Airport) reflect genuine advantages of PV geometry rather than suboptimal baseline tuning. The main text also does not specify how the non-PV baselines (HNN, HNN++, LNN) were constructed — e.g., whether official implementations or the authors' re-implementations were used.

### Minor
1. **Image classification experiment is narrow and shows only marginal gains.** The experiment (Table 4) only replaces the final MLR of a ResNet-18 while keeping the backbone Euclidean. The improvements over the best prior MLR are small (CIFAR-100: 78.20 vs 77.96, overlapping within standard deviation). The paper's conclusion that "PV MLR matches or outperforms prior hyperbolic baselines" is accurate, but this experiment alone provides weak evidence that full PV networks are broadly effective in vision.

2. **No curvature sensitivity analysis in task experiments.** The paper fixes \(K=-1\) in numerical experiments and presumably learns or tunes it in others, but no ablation or analysis of curvature's effect on task performance is presented. Since curvature controls the "spread" of the geometry, its impact on downstream results is worth reporting.

3. **Tangent-space FC variant performs comparably or better on larger/less-hyperbolic graphs.** In Table 6, PVNN+TFC matches or exceeds PVNN on PubMed and Cora. The paper acknowledges this but does not discuss the implication that the complex Riemannian PV layers may only provide benefits on strongly hyperbolic data, while simpler tangent approximations suffice elsewhere.

### Trivial
None.

## Nice-to-Haves
- A controlled experiment comparing PVNN against a Poincaré network reparameterized through the isometry (mapping trained PVNN weights via Eq. 4) would cleanly isolate whether observed performance gains are due to numerical stability or optimization dynamics.
- Runtime comparison for the closed-form MLR (Eq. 19) vs the original parameterization would substantiate the efficiency claim.
- Comparison with the Klein model beyond graph learning (e.g., in genomic or vision tasks) would be informative since Klein is also unconstrained.

## Removed Points
These points were considered but removed with justification:
- **"The isometry also raises questions about experimental comparisons" (Harsh Critic #2)**: The critic claimed performance differences could be due to optimization dynamics or implementation differences and that the paper doesn't isolate these factors. However, the paper's *direct* numerical stability experiments (Sec 6.1) *do* isolate stability, and the task experiments are designed to evaluate *overall effectiveness* — not to decompose the sources of gains. The paper's framing positions numerical stability as the core advantage, which is directly demonstrated. Disentangling secondary factors is not required to support the paper's claims.
- **"Baseline re-implementation is underspecified" (part of Harsh Critic #4)**: The critic argued that "simply changing the underlying hyperbolic model while keeping the same architecture shape is not sufficient" and that each baseline's layer implementations must be faithfully reproduced. The paper states all models share the same *high-level architecture* (two FC layers + MLR) while each model uses its *own native layers* (Poincaré gyrovector layers for HNN, Lorentz layers for LNN, PV layers for PVNN). This is the standard and appropriate way to compare different hyperbolic models. The critic's reading that the authors merely swapped coordinate systems is incorrect.
- **Strength Finder strength about "strong empirical outperformance on genomic sequence learning"**: Kept — it is specific, grounded in Table 10, and valid.
- **Other noise from Harsh Critic**: Criticisms about missing/{appendix content, proofs in appendix, absent references} were removed per hard rules.
- **"No runtime comparison for MLR training" (Harsh Critic)**: Moved to Nice-to-Haves as a non-critical suggestion.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. In the introduction and contributions, reframe PV as a "numerically stable parameterization of hyperbolic space" rather than a "new alternative geometry," explicitly acknowledging that PV is isometric to the Poincaré ball but offers practical numerical advantages. This would avoid any perception of overclaiming.
2. Add hyperparameter search ranges and tuning details for all baselines (graph, genomic, image) in the main text or appendix, including learning rate, weight decay, hidden dimensions, and curvature initialization.
3. Include a brief curvature sensitivity analysis — even a single table showing how varying \(K\) affects accuracy on one or two datasets would be valuable.
4. Add statistical significance tests (e.g., paired bootstrap) for the image classification results in Table 4.

---

Now I need to calibrate my score. Let me write up the calibration results.

## Calibration

### Round 1 — Bracketing

I searched for anchors in three score bands using topically similar queries:

**Weak band (high_score=3.5):** Retrieved 4 papers with avg scores 1.33–3.00. These are weak, mostly unrelated papers (PINNs, Hopfield networks). Not useful as direct comparisons.

**Middle band (3.5–7.5):** Retrieved:
- "Building Transformation Layers for Riemannian Neural Networks" (avg 4.00) — a general framework for Riemannian FC/conv layers; rejected/withdrawn. Current paper has stronger empirical validation and is more focused.
- "Cartan Networks" (avg 4.00) — hyperbolic architecture via Lie groups; rejected due to limited experiments. Current paper has broader and stronger experiments.
- "Hyperbolic Implicit Equilibrium" (avg 4.00) — hyperbolic DEQ; rejected due to writing and clarity issues. Current paper is more sound.

**Strong band (low_score=7.5):** Retrieved 4 papers with avg scores 8.00–8.50. These are on rotation estimation, quantum computing, kernel methods, and matrix sign functions — topically unrelated to this paper. Not useful for comparison.

**Bracket:** 4.5–6.5 (the paper is clearly stronger than the 4.00 anchors but not at the 8.00 level).

### Round 2 — Narrowing

I searched the (4.5, 6.0) and (6.0, 7.5) bands:

- "HexFormer" (avg 5.50, rejected, scores 6,4,4,8) — hyperbolic vision transformer with marginal gains and limited novelty. Current paper has broader contributions (complete toolkit across multiple domains vs just attention), stronger numerical analysis, and more compelling real-world results (genomic). **Current paper is slightly stronger than HexFormer.**
- "The Natural Geometry of Code: Hyperbolic Representation Learning for Program Reasoning" (avg 5.50, accepted poster) — hyperbolic GNN for code. Similar scope and quality. Current paper has more domains but less deep evaluation in any single domain. **Comparable quality.**
- "Landing with the Score: Riemannian Optimization through Denoising" (avg 6.50) — not directly comparable topic.
- "Exponential-Wrapped Mechanisms" (avg 6.50) — DP on Hadamard manifolds, not comparable.

The two most comparable anchors (HexFormer at 5.50, HypeCodeNet at 5.50) both sit in the 5.5 range. The current paper is slightly stronger than HexFormer due to its broader scope and stronger numerical evidence, and comparable to HypeCodeNet. 

**Final score: 6.0**. This reflects the paper's solid contributions (complete Riemannian toolkit, numerical stability evidence, strong genomic results) tempered by the isometry limiting novelty, marginal image results, and underspecified baseline tuning.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>