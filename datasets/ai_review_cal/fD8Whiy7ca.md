- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 3, 8, 5
Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me synthesize the final review.

## Summary

This paper introduces Restricted Adaptive Feedback (RAF), a method that factorizes the feedback matrix in Feedback Alignment into two low-rank components \(Q\) and \(P\) and trains both using local, biologically plausible updates (Oja's rule for \(P\), a Hebbian-style rule for \(Q\)). The central claim is that deep networks—linear, nonlinear, fully-connected, and convolutional—can match backpropagation performance with an error dimensionality as low as the number of output classes. The paper provides a theoretical analysis for linear networks showing why training both factors is necessary under rank constraints, and connects the method to biological vision by showing that constrained error feedback yields center-surround receptive fields.

## Strengths

1. **Theoretical analysis demonstrating why both factors of the low-rank feedback matrix must be learned.** Section 3.1–3.2 derives continuous-time dynamics (eq. 5) and fixed-point conditions, then shows analytically and through simulation that when only the column space (\(Q\)) is trained (as in Kolen-Pollack style adaptive FA), the network cannot recover the correct mapping under rank constraints, whereas learning both \(Q\) and \(P\) (RAF) enables recovery (Fig. 2c–g). This goes beyond prior FA work by identifying and solving a specific failure mode of low-rank feedback.

2. **Empirical demonstration that feedback rank equal to task dimensionality matches backpropagation performance.** On CIFAR-10, constraining feedback to rank \(r=d=10\) in any layer yields test accuracy matching BP (Fig. 3a). On CIFAR-100 with varying class counts, RAF matches BP precisely when \(r\) equals the number of classes (Fig. 3c). The cleanest evidence is the task-dimensionality experiment (Fig. 3c), which directly supports the claim that minimal sufficient error dimensionality is determined by the task, not the network width.

3. **Systematic sweep of error dimensionality as a controlled experimental variable.** The paper varies rank \(r\) across individual layers (Fig. 3a), across all layers (Fig. 3b), and as a function of layer width (Fig. 4b), revealing that deeper layers compensate for tighter constraints in shallower layers. No prior FA study has performed such a controlled, layer-specific sweep of error dimensionality.

4. **Feedback weight updates are local and use a well-studied Hebbian rule (Oja's rule), enhancing biological plausibility.** The paper explicitly provides the Oja-based update for \(P\) (eq. 8) in the single-layer case, and the text describes how this extends to deep networks using local error signals, maintaining locality throughout.

## Weaknesses

### Fatal
None.

### Major

1. **Missing explicit update equation for \(P_l\) in deep nonlinear networks (reproducibility gap).** Section 3.3 states that Oja's rule is used to adjust \(P_l\) to span the principal components of \(\delta_{l+1}^\mu\), but no equation for \(\Delta P_l\) is provided—only \(\Delta W_l\) and \(\Delta Q_l\) are given in eq. (10). The single-layer case provides eq. (8), but the translation to the deep case (replacing \(\mathbf{y}^\mu\) with \(\delta_{l+1}^\mu\)) is left implicit. For a methods paper proposing a new learning rule, this is a significant reproducibility gap. The authors should provide the explicit \(\Delta P_l\) update (e.g., \(\Delta P_l^\mu = \eta P_l \delta_{l+1}^\mu \delta_{l+1}^{\mu T} (I - P_l^T P_l) - \lambda P_l\) or the correct variant) as a numbered equation and ideally in pseudocode.

2. **No comparisons to other Feedback Alignment variants.** The paper compares RAF only to backpropagation. While BP is the natural performance ceiling, the paper makes claims that prior FA methods "struggle to scale" and "fail when the matrix \(B\) is low-rank," yet provides no direct comparison to standard FA (fixed random feedback), adaptive FA with full-rank feedback (Akrout et al., 2019), Direct FA (Nøkland, 2016), or Sparse FA (Crafton et al., 2019) on the same architectures and datasets. Without these baselines, the reader cannot tell whether RAF's success comes from training the feedback weights, from the low-rank constraint, or from the specific experimental setup.

3. **No hyperparameter reporting (critical for reproducibility).** The paper does not report learning rate, batch size, number of epochs, weight decay values, or optimization algorithm (SGD vs. Adam) for any experiment. The theoretical derivation assumes full-batch SGD with infinitesimal learning rate, but the experiments almost certainly use minibatch SGD—this gap is not discussed. For an empirical paper whose central claim is matching BP performance, this is a major reproducibility failure.

4. **No statistical significance or variance reporting.** All experimental results appear to be single runs. Figures 3 and 4 show no error bars, and there is no mention of standard deviation over seeds or run-to-run variability. Given that matching BP performance is the central quantitative claim, the reader cannot determine whether observed gaps (e.g., rank-10 curves in Fig. 3a that appear a percentage point or more below BP) are meaningful or simply noise.

5. **Insufficient architectural details for the convolutional network experiments.** The paper describes a "4-block VGG-like network" without specifying filter sizes, stride, pooling, number of filters per block, or activation functions. Crucially, it does not explain how the factorized feedback \(B = QP\) is applied to convolutional layers—whether the feedback matrices operate on flattened or unrolled error signals, and whether \(Q\) and \(P\) are per-filter or per-layer. This makes the convnet experiments difficult to reproduce.

### Minor

1. **Receptive field analysis is entirely qualitative.** Section 5 shows that constraining feedback rank yields center-surround receptive fields in the retinal layer (Fig. 4d), but provides no quantitative metric (e.g., concentricity index, spatial frequency tuning, distribution statistics) to compare across feedback ranks or against the unconstrained baseline. While the observation is interesting, the claim that "error dimensionality shapes neural representations" would be substantially stronger with quantitative evidence.

2. **Limited task scope.** All experiments are on CIFAR-10/100 classification (10–100 classes, \(d\) small). Testing on a regression task, a dataset with many output classes (e.g., ImageNet with 1000 classes), or a continuous-output task would strengthen the generality of the claim that minimal rank equals task dimensionality.

3. **Missing discussion of how minibatch SGD affects the theoretical fixed-point analysis.** The continuous-time analysis in Section 3.1 assumes full-batch gradient descent; the paper acknowledges the limitation but does not discuss whether the discrete, stochastic setting used in experiments preserves the same fixed-point properties.

### Trivial
None.

## Nice-to-Haves

- A pseudocode algorithm box summarizing the forward pass, backward pass, and all three update rules (\(W\), \(Q\), \(P\)) for the deep case would resolve most specification ambiguities and is standard for papers proposing a new learning rule.
- Providing the receptive-field analysis with quantitative statistics (e.g., distribution of center-surround indices across neurons and feedback ranks) would strengthen the biological claims.
- Analysis of the rank of weight updates during training (as suggested in the discussion) would provide mechanistic support for the claim that "weight updates are confined to a lower-dimensional subspace."

## Removed Points

These points from the reviewers are removed or downgraded for the following reasons:

- **Harsh Critic Claim:** "The paper states that 'this approach [Kolen-Pollack style adaptive FA] fails when the matrix B is low-rank' without evidence." — **REMOVED** because the paper DOES support this claim in Section 3 (Fig. 2c, f) where training only \(Q\) with fixed \(P\) leads to incorrect solutions under rank constraints. The critic appears to have missed this evidence.

- **Harsh Critic Claim:** Section 3.3 "does not explain why the principal components of the *output* variable (not the error) are the correct directions to propagate" for the single-layer case. — **WEAKENED/MOVED.** The paper explains (Section 3.2) that \(P\) should span the top principal directions of the output-output correlation matrix \(\Sigma^{yy}\), and that this aligns the feedback with the most significant error directions. This is a reasonable justification, even if a deeper theoretical connection could be drawn.

- **Strength Finder Claim 3:** "Evidence that constraining error dimensionality shapes neural receptive fields, linking the method to biological visual system phenomena." — **DEMOTED** from a core strength to a minor/interesting point because the evidence is entirely qualitative (one figure showing some fields) with no quantitative validation. The claim is present, but the evidence is preliminary and not yet a strong contribution.

- **Harsh Critic Claim about dRAF/conv architecture:** "The authors also do not explain how RAF is applied to convolutional layers—do the feedback matrices operate on the flattened or unrolled error signal?" — **KEPT AS MAJOR since this is folded into Major weakness #5.**

- **Harsh Critic Suggestions about comparing to Adaptive FA:** This is kept as a Major weakness (#2) but reframed more precisely.

- **Harsh Critic's "Missing algorithm box" and similar presentation suggestions:** These are moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews affirm the paper's core findings (theoretical necessity of training both factors, empirical match at rank = task dimensionality) and identify gaps in specification and experimental rigor, but do not surface a genuinely novel observation not already present in the paper.

## Suggestions

1. Provide the explicit update equation for \(P_l\) in the deep nonlinear case (or a complete pseudocode block) in the main text. This is the single most important fix.
2. Add comparisons to standard FA and full-rank adaptive FA (Akrout et al.) on the same architectures to validate the claim that RAF's advantage goes beyond simply training the feedback pathway.
3. Report all hyperparameters (learning rate, batch size, epochs, weight decay, optimizer) for every experiment.
4. Run key experiments (especially the FC CIFAR-10 comparison and convnet results) over at least 3 random seeds and report mean ± std.
5. Provide a full layer-by-layer specification of the convolutional architecture and describe how the factorized feedback is applied to convolutional layers (e.g., using 1×1 convolutions).
6. For the receptive field experiments, add a quantitative metric (e.g., center-surround index) and show its distribution across neurons for different feedback ranks versus the unconstrained baseline.
