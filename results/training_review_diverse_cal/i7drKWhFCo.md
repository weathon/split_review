Now I have a thorough understanding of the paper. Let me construct the final review.

---

## Summary

This paper introduces SC-VAE (Scrubbed Conditional VAE), a framework that augments conditional variational autoencoders with adversarial "scrubbers" to remove specified nuisance variability (speed, heading direction, animal identity) from latent representations of 3D animal pose sequences. The key innovation is replacing finicky adversarial neural networks (gradient reversal, neural discriminators) with parametric scrubbers—moving-average least squares (MALS), quadratic (MAQS, MACS), QDA, and kernel MI estimators—that are more reliable and require less tuning. The method is evaluated on decodability, clustering quality, motion synthesis consistency, and a real Parkinson's disease mouse model application.

## Strengths

1. **Parametric scrubbers reliably achieve specified levels of disentanglement where adversarial networks fail.** The paper shows that gradient reversal (GR) and neural discriminator (ND) methods "were unreliable in producing representations that were even linearly invariant" to heading direction (Section 4.2). In contrast, SC-VAE-MALS reliably achieves linear invariance, and SC-VAE-MAQS/MI achieve near-perfect nonlinear disentanglement matching the fully preprocessed baseline (Fig. 2). This directly addresses a practical pain point in the field.

2. **Principled demonstration that different nuisance variables require different scrubbing strengths.** The paper shows that heading direction (fully separable from behavior) can be aggressively scrubbed with MI, while speed (partially entangled with behavior) requires the weaker MALS scrubber to avoid destroying interpretable behavioral clusters (Section 4.4, Fig. 3e–g). This controlled disentanglement—not full invariance—is a genuine conceptual advance over methods that assume all nuisance factors can be treated identically.

3. **Clinically relevant validation on a Parkinson's disease dataset.** SC-VAE-QD (scrubbing animal identity) increases the effect size of healthy-vs-disease MMD from 1.48 (VAE) to 2.14, improves classification accuracy from 79.2% to 85.0%, and strengthens the correlation with dopamine denervation extent from r=0.55 to r=0.67 (Table 2). A reverse-control (scrubbing the disease label) degrades performance, confirming the method specifically removes nuisance variation. This goes beyond synthetic benchmarks to show practical utility.

4. **Comprehensive empirical scope.** The paper evaluates nine model variants across three nuisance variables, three decoding function classes (linear, quadratic, nonlinear MLP), clustering analyses, and motion synthesis—providing a systematic picture of relative strengths and weaknesses rather than cherry-picking one setup.

## Weaknesses

### Fatal

None.

### Major

1. **Limited uncertainty quantification for key results.** The paper's central quantitative evidence—decodability R² values (Fig. 2), clustering metrics (Fig. 3), and motion synthesis R² (Table 1)—is reported as single values without error bars, confidence intervals, or significance tests. Table 2 does report mean ± SEM for the effect size *d*, but the classification accuracy and Pearson *r* in the same table lack uncertainty measures, as do all other quantitative exhibits. For method comparisons where differences are modest (e.g., some R² values in Fig. 2 between SC-VAE variants), the reader cannot determine whether these differences are robust or reflect random seed variation. This weakens the paper's main evidence base substantially. *Note: the reviewer's claim of "no error bars anywhere in Section 4" overstates the case, since Table 2 does report SEM for effect size d, but the broader concern about insufficient uncertainty quantification across the majority of results is valid.*

2. **The comparison against adversarial baselines (GR, ND) lacks documentation of tuning effort.** The paper correctly identifies that adversarial methods "require careful tuning" (Section 3.4) and that this is a key motivation for parametric scrubbers. However, it does not report how many hyperparameter configurations were tried for GR/ND, the search range, or the selection criteria. If SC-VAE variants benefit from being nearly hyperparameter-free while baselines received minimal tuning, the comparison conflates method advantage with asymmetric effort. Since the paper's narrative centrally contrasts parametric reliability against adversarial finickiness, this gap needs to be addressed to make the evidence convincing.

### Minor

1. **Self-tuning EMA mechanism is presented but not validated.** The adaptive two-filter scheme for setting the EMA smoothing factor (Section 3.5) is a non-trivial algorithmic component. The paper does not ablate it against fixed smoothing factors to show it works as intended, nor does it characterize its behavior across batch sizes, training stages, or data distributions. Without this, one cannot rule out that the parametric scrubbers' performance depends on the EMA adaptivity succeeding—or that fixed EMA factors would perform equally well. The appendix reference (A.2) describes the mechanism but does not validate it.

2. **Motion synthesis evaluation (Table 1) is too narrow.** Only two metrics are reported (R² of heading/speed of generated sequences), with no reconstruction loss, diversity metric, or qualitative realism check. This leaves open the concern that improved consistency comes from the generator collapsing to trivial outputs. Including a reconstruction ELBO or a standard sample quality measure would address this.

3. **The "hyperparameter-free" claim is overstated.** The parametric scrubbers still require setting the λ penalty weight for the adversarial loss (Eq. 3) and the fixed difference between the two EMA smoothing factors. While these are fewer hyperparameters than the adversarial baselines, the method is not strictly hyperparameter-free as claimed in the conclusion (Section 5, line 181). This is a small overstatement rather than a structural flaw.

### Trivial

None.

## Nice-to-Haves

- A more principled characterization of when a variable is "fully separable" vs. "partially entangled" with behavior, to guide the choice between linear and MI scrubbers, rather than the current post-hoc description.
- A brief discussion of the method's likely sensitivity to lower frame rates, occlusions, or markerless tracking noise, since real-world applications often involve more challenging recording conditions than the 90 fps open-field setup used here.
- A reconstruction loss comparison across all models to verify that improved disentanglement does not come at the cost of losing behavioral information.

## Removed Points

- **"No error bars anywhere in Section 4"** — Factually incorrect; Table 2 reports mean ± SEM for effect size *d*. The broader concern about limited uncertainty quantification is retained as a Major weakness.
- **"Appendix A.2 is referenced but not present or visible to the reviewer"** — The parser strips appendices; they exist in the original submission.
- **Strength: "Tackles a fundamental challenge in behavioral neuroscience"** — Generic claim without specific evidence; retained implicitly in the strengths about disease validation and controlled disentanglement but dropped as a standalone overclaim.
- **"The paper does not discuss failure modes or limitations of fast head/mouse features" regarding frame rates, occlusions, etc.** — Scope creep; the paper's stated limitations are about architecture and scalability, which is appropriate for a methods paper of this scope.

## Novel Insights

The most interesting signal from the reviews is the tension between the two core claims: (1) parametric scrubbers are more *reliable* and *easier to use* than adversarial networks, versus (2) the method is thoroughly *validated* across applications. The reviews agree the first claim is well-motivated and the second is partially supported—but the lack of uncertainty quantification and baseline-tuning documentation means the evidence for reliability is weaker than the paper asserts. The disease application (Table 2) is the paper's strongest card precisely because it reports SEM and includes a reverse control; extending that standard to the other experiments would substantially strengthen the paper. The self-tuning EMA, while clever, remains the least-characterized component of the core contribution, and addressing its validation would remove a significant vulnerability.

## Suggestions

1. **Add error bars to all quantitative results.** Run each experiment with at least 5 random seeds and report mean ± SEM (or equivalent) for Fig. 2, Fig. 3, and Table 1. This single change would have the largest impact on the paper's credibility.
2. **Document the hyperparameter search for adversarial baselines.** Report the search space, number of configurations tried, and selection criteria for GR and ND to demonstrate fair comparison.
3. **Ablate the self-tuning EMA** against a grid of fixed smoothing factors to validate that the adaptive mechanism matches or exceeds the best fixed setting without manual tuning.
4. **Include reconstruction loss** (e.g., ELBO) alongside the motion synthesis metrics in Table 1 to rule out degenerate generation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>