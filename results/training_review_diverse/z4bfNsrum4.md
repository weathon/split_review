I now have all the information needed to construct a thorough, verified review.

---

## Summary

This paper investigates why mem-orized deep networks (trained on label-shuffled data) generalize poorly. It proposes the Minimum Angle Subspace Classifier (MASC), which measures the angle between a hidden-layer representation and class-conditioned PCA subspaces, and shows that this simple decoder achieves dramatically higher test accuracy than the model itself across MLPs, CNNs, and AlexNet on MNIST, Fashion-MNIST, CIFAR-10/100, and Tiny ImageNet. The central empirical finding — that representations in heavily memorized networks retain substantial generalization-relevant structure — is novel and well-supported.

## Strengths

1. **Core empirical finding is novel and compelling.** The paper demonstrates that models trained with up to 80–100% label noise still contain hidden-layer representations from which a simple decoder can recover 80%+ test accuracy (e.g., MLP-MNIST at 80% corruption: MASC >80% vs. model 34%; MLP-MNIST at 100% corruption using true-label subspaces: 95% vs. chance-level model performance). This directly contradicts the tacit assumption that memorization destroys generalization-relevant structure.

2. **Memorization and generalization coexist in the same representations.** MASC simultaneously achieves high accuracy on corrupted training labels and on true test labels (e.g., CNN-Fashion-MNIST at 40% corruption: ~85% true training accuracy and improved test accuracy at the Flat layer). This is a non-obvious result — the representations encode both the noise the model was trained on and the signal it was never shown.

3. **Method is simple, architecture-agnostic, and tested across diverse settings.** The PCA+minimum-angle approach works across MLPs, CNNs, and AlexNet on datasets ranging from MNIST to Tiny ImageNet, with results at multiple corruption levels. The simplicity of the method strengthens the claim that the structure it exploits is generic, not an artifact of a complex decoder.

4. **Surprising results persist at extreme (100%) corruption.** Models whose training labels are completely shuffled have chance-level test accuracy, yet MASC using true-label subspaces recovers near-original test accuracy (95% for MLP-MNIST, 69% for CNN-Fashion-MNIST). This is the paper's most striking result and convincingly shows that generalization structure survives even when the model has no access to any correct training labels.

## Weaknesses

### Fatal
None.

### Major

1. **Missing baseline: a simple linear probe on the same layer outputs.** The paper cites Alain & Bengio (2018) as having used linear classifiers to probe hidden representations but does not include this as a baseline. Without comparing MASC to, e.g., logistic regression or a linear SVM on the same layer outputs, it is impossible to tell whether the subspace-angle classifier offers any advantage over standard probing. If a linear probe performs comparably, then the paper's *methodological* contribution (MASC as a technique) is weakened — though the core empirical finding (representations retain generalization structure) would remain intact. The paper acknowledges in the Discussion that "other classifiers operating on layerwise outputs have better performance than MASC," but this acknowledgment does not substitute for an explicit comparison. Adding this baseline would substantially strengthen the paper.

### Minor

2. **Unusual PCA procedure is not validated against standard centered PCA.** The paper adds the negative of each sample to force zero mean before PCA, rather than centering the data. This computes principal components of the second-moment matrix \(E[xx^T]\) rather than the covariance matrix, which differs when the per-class mean is non-zero. The paper explains *why* this is done (to obtain a subspace through the origin rather than an affine space), but does not compare this to standard centered PCA or show that the specific choice matters empirically. Since the entire method depends on the estimated subspaces, this should be validated or at minimum discussed.

3. **99% variance threshold for PCA is presented without motivation or sensitivity analysis.** The paper states "We have used 99% as the percentage of variance explained, unless otherwise mentioned" but does not justify this choice or show how results vary with the threshold. A brief ablation (e.g., 90%, 95%, 99%, 99.9%) would clarify whether the method is robust to this hyperparameter.

4. **Framing overstates mechanistic insight.** The paper frames two hypotheses: (i) representations are irretrievably reorganized, or (ii) the network "chooses" a poor readout. The evidence supports (ii) over (i) — a decoder on intermediate layers works well, which contradicts hypothesis (i). However, this does not reveal the *mechanism* by which the model's own readout fails (the paper does not show why the final layer weights, which are optimal for the corrupted training objective, fail to exploit the preserved structure). The paper's title ("Decoding Generalization from Memorization") and framing imply more mechanistic insight than the evidence provides. The paper should frame its contribution as demonstrating the preservation of generalization-relevant structure rather than fully "decoding the mechanism."

### Trivial

5. **MASC-on-input baseline mentioned but not systematically shown.** The paper states that "performance of the MASC on the input is a good baseline measure" and reports that input experiments were run for MLP and CNN models, but the main figures do not consistently display MASC input accuracy across all model families. Showing this baseline uniformly in the figures would strengthen the claim that subsequent layers improve upon it.

6. **Three runs per configuration are standard but limited.** The paper reports only three seeds. While this is common practice and the paper shows error ranges, the strong quantitative claims (especially the dramatic test accuracy gaps) would benefit from more seeds to improve statistical reliability.

## Nice-to-Haves

- **Control experiment: random labels for subspace construction.** Section 5 shows that true-label subspaces yield high accuracy, but a control using random labels to build subspaces would clarify whether the preserved structure is specific to the true classes or reflects a generic property of high-dimensional representations.
- **Sensitivity analysis for the 99% variance threshold** (see Weakness #3 above).
- **Comparison to early stopping** (mentioned in Appendix A.4) would be useful to discuss in the main text to contextualize how MASC's improvement compares to an alternative strategy for recovering generalization.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Claims about 'why' generalization is retained are not supported" (original framing):** The harsh critic argued the evidence is consistent with *either* hypothesis. This is incorrect: if hypothesis (i) (representations irretrievably reorganized against generalization) were true, then a simple decoder should NOT achieve dramatically better generalization. The evidence does favor hypothesis (ii) over (i). However, the toned-down version (Weakness #4 above) — that the paper's framing overstates mechanistic insight — is retained.
- **"Section 5 results are not surprising":** The harsh critic dismissed the 100% corruption results as "not surprising." This is inaccurate; that models trained on fully shuffled labels retain representations supporting 95% test accuracy is a striking and non-obvious result. Removed as a misunderstanding of the paper's contribution.
- **"Only mentions qualitatively" (input baseline):** The paper does run input experiments for MLP and CNN models (though they are not in the main figures for CNNs). The claim of pure qualitative mention is inaccurate; the criticism has been reframed as Trivial Weakness #5.

## Novel Insights

The most interesting observation that emerges across the reviews is that the paper's results reveal something asymmetrical about generalization vs. memorization in the representational geometry: generalization-relevant structure appears to be a *stable, low-dimensional feature* that persists even as the model's weights are pulled toward a high-dimensional memorization solution. This suggests that the optimization process, even under extreme label noise, does not destroy the "easy" (low-frequency, simple-pattern) subspace that supports generalization — it simply learns an additional mapping from that subspace to noisy targets, leaving the subspace itself intact for a separate decoder. This perspective is not stated in the paper but follows naturally from its results and connects to the known "simplicity bias" literature (Arpit et al., 2017; Belrose et al., 2024).

## Suggestions

1. **Add a linear probe baseline** (logistic regression or linear SVM on the same layer outputs) to every experiment in Figures 1–3. This would calibrate MASC's performance against the simplest possible decoder and either strengthen the claim that MASC's geometry is beneficial or honestly reframe the contribution if linear probes work equally well.
2. **Compare the doubling-PCA procedure to standard centered PCA** on a subset of experiments and report whether subspace directions differ materially. If they do, justify which is conceptually appropriate; if they do not, note this as a robustness check.
3. **Include a sensitivity plot** for the 99% variance threshold (e.g., 90%, 95%, 99%, 99.9%) for one representative model/dataset pair.
4. **Tone down mechanistic claims.** Replace "decoding the mechanism" language with language about "demonstrating preserved generalization-relevant structure" throughout the paper.
5. **Show the input baseline consistently** across all model families in the main figures to demonstrate the contribution of deeper layers.

## Score and Decision

The paper's core empirical finding is significant and well-supported across multiple architectures and datasets. The missing linear probe baseline is a real gap that weakens the methodological claims, but the central discovery — that memorized networks retain latent generalization structure in their hidden representations — does not depend on MASC being better than other probes. The weaknesses are addressable in revision. I recommend acceptance.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>