I now have all the information needed to synthesize the review. Let me produce the final consolidated assessment.

---

## Summary

This paper proposes a principled theoretical framework for constructing fully connected (FC) and convolutional layers on general Riemannian manifolds, using only exponential and logarithmic maps. The framework subsumes prior manifold-specific FC layers (e.g., hyperbolic and gyro SPD) and recovers the Euclidean FC layer as a special case. Concrete closed-form instantiations are provided for five SPD metrics (LEM, AIM, PEM, LCM, BWM) and two Grassmannian perspectives (ONB and PP). Experiments on radar signal classification and human action recognition compare networks built with the proposed layers against several existing SPD and Grassmannian baselines.

## Strengths

1. **General closed-form expression for Riemannian FC layers (Theorem 4.2).** The paper provides a single formula that works for any Riemannian manifold with well-defined exponential and logarithmic maps, unlike prior work that required manifold-specific structures (gyro groups for SPD, hyperbolic geometry, etc.). This is the paper's core theoretical contribution and is clearly derived from geometric principles.

2. **Subsumes prior gyro SPD FC layers and recovers the Euclidean FC layer.** Table 1 shows that the three gyro SPD FC layers (Nguyen et al., 2024) are special cases of the proposed SPD FC layers under LEM, AIM, and LCM. Proposition 4.4 proves that the general layer reduces to the standard Euclidean FC layer when both input and output manifolds are Euclidean. This establishes coherence with the existing literature.

3. **Greater flexibility in dimensionality than prior Grassmannian layers.** Table 2 formally compares the ability to change subspace dimension, ambient dimension, and channel dimension across both ONB and PP perspectives. Only the proposed GrConv can modify all three, unlike FRMap+ReOrth, GrTrans, and scaling layers.

4. **Concrete instantiations across five SPD metrics and two Grassmannian perspectives.** Theorems 5.1, 6.1, and 6.2 provide explicit, usable formulas for five distinct SPD geometries and two Grassmannian formulations. This makes the general framework immediately applicable across multiple commonly used geometries.

5. **Intrinsic geometric interpretation of manifold embedding tricks (Proposition 7.1).** The paper shows that the common practice of mapping Euclidean features to a manifold via a linear layer followed by exponential map is exactly a Riemannian FC layer. This provides a clean theoretical justification for a widely used technique.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison with the most directly relevant prior work (gyro SPD convolutional networks).** The paper repeatedly states that its SPD FC layers subsume the gyro SPD FC layers of Nguyen et al. (2024), yet the experiments include *no comparison* against those gyro SPD networks. The baselines used (SPDNet, SPDNetBN, LieBN, RResNet, MLR) are older or architecturally different. Since the paper claims both to generalize and to *outperform* existing SPD networks, the absence of the most closely related prior work weakens the empirical contribution. It leaves unclear whether the general framework offers practical advantages over the manifold-specific gyro approach.

2. **Uncontrolled architecture differences in SPD experiments.** The proposed SPDConvNets use a *single* convolutional layer plus an MLR, while the baselines (e.g., SPDNet, SPDNetBN) typically have multiple transformation layers of different types. The paper does not report parameter counts, does not re-implement baselines to match the same architectural budget, and does not perform an ablation that isolates the effect of the proposed conv layer from the effect of overall architecture design. The observed performance gains cannot be cleanly attributed to the Riemannian framework vs. architectural differences.

3. **No variance reporting.** Results in Tables 3 and 4 are reported only as 5-fold average and maximum accuracy, without standard deviations, confidence intervals, or any measure of variance. The maximum metric is particularly fragile (the paper itself notes that RResNet's Radar accuracy fluctuates by up to 20% across epochs). Without error bars, the reliability of the claimed improvements over baselines is unclear.

### Minor

1. **Exponential map surjectivity limitation not empirically explored.** As the paper acknowledges (Remark 2.1, line 201), the exponential map at a fixed origin is not surjective for some geometries (BWM, PEM on SPD). While the paper mentions numerical workarounds (eigenvalue regularization), it does not empirically investigate whether this restriction limits model expressivity in practice. For example, one could test whether learning a different origin point changes performance. This is a known limitation that deserves at least a brief empirical note.

2. **Connection between general theorem and specific instantiations could be clearer.** The derivation jumps from the general Theorem 4.2 (using an arbitrary orthonormal basis {B_i}) to the dense expressions in Theorem 5.1 (using metric-specific scalings). The choice of orthonormal basis for each metric and how the general formula specializes is not explained intuitively — the reader must trust the algebra in the stripped appendix. A brief explanation of how the basis is constructed for each metric would improve readability.

### Trivial
None.

## Nice-to-Haves

- **Comparison with a simple Euclidean baseline** (e.g., vectorizing the SPD/Grassmannian feature and applying a standard conv net) would help isolate whether the Riemannian geometry itself provides benefit on these tasks.
- **Hyperparameter details** (learning rate, optimizer, weight decay, epochs, selection procedure) in the main text would improve reproducibility; the paper refers to the (stripped) appendix.
- **A brief discussion of computational cost or runtime** would help assess the practical cost of the framework's flexibility.

## Removed Points

- Criticism about garbled equations in Theorem 5.1: the paper text contains PDF-parser artifacts that are not present in the original submission; not a valid weakness.
- Criticism about missing appendix content (e.g., proofs, hyperparameters): the appendix exists in the original submission but is stripped by the parsing process.
- Criticism about missing discussion of implementation cost of parallel transport: the paper provides closed-form expressions for the manifolds used; the "general geometries" claim is scoped accordingly and the criticism is speculative about uninstantiated cases.
- Criticism that the paper "does not compare against a simple Euclidean baseline" (moved to Nice-to-Haves): this would strengthen the paper but is not a core flaw, as the paper primarily compares against other Riemannian methods.
- Strength Finder's generic strengths about "addressing an important problem" and "targeting an interesting question": removed as they are generic and lack specific evidence from the paper.

## Novel Insights

The harsh critic correctly identified that the experimental validation does not match the rigor of the theoretical contribution, but this does not diminish the value of the theoretical framework itself. The strength finder's observation about the framework subsuming prior gyro layers while also handling geometries that lack gyro structures (like BWM) is an insightful contrast worth highlighting: the paper's contribution is less about beating existing methods and more about providing a *unified* foundation that covers previously unaddressable geometries with no additional per-manifold engineering.

## Suggestions

1. **Add the gyro SPD convolutional network (Nguyen et al., 2024)** as a baseline in the SPD experiments. This directly tests whether the general framework offers practical advantages over the manifold-specific approach.
2. **Report parameter counts** for all models and, ideally, control for model capacity by testing a version of SPDNet with similar depth/complexity as the proposed SPDConvNet.
3. **Include standard deviations** (or similar variance measures) for all reported results.
4. **Add a brief empirical note** on the exponential map surjectivity issue: e.g., train the BWM/PEM SPDConvNet with a learned origin and check whether performance changes, to confirm the reachable set is sufficient.
5. **Improve readability** of Theorem 5.1 by explaining the orthonormal basis construction for each metric in a few sentences, bridging the gap between the general theorem and the specific expressions.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>