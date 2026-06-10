## Summary

This paper proposes TLDR (Training-Like Data Reconstruction), a network-inversion approach that uses a conditioned generator trained with a multi-term loss to reconstruct "training-like" data from trained CNN classifiers. The method exploits three hypothesized properties of training data relative to the model — higher prediction confidence, greater robustness to input perturbations, and smaller gradient norms w.r.t. model weights — combined with diversity-promoting conditioning techniques (soft vector conditioning and intermediate matrix conditioning). Experiments are conducted on MNIST, FashionMNIST, SVHN, and CIFAR-10.

---

## Strengths

- **Novel conditioning mechanism for diversity** (Sections 3.2.2–3.2.4): The paper introduces soft-vector conditioning (encoding label information into softmaxed random vectors whose argmax is the conditioning label) and intermediate matrix conditioning (a "Hot Conditioning Matrix" concatenated at spatial dimensions). This goes beyond standard label conditioning and is a concrete methodological contribution for encouraging diverse inversion outputs.

- **Extension of reconstruction to CNNs with regularization** (Sections 1, 3, 4): Prior reconstruction work (Haim et al., 2022; Buzaglo et al., 2023) focused on binary MLP classifiers. This paper explicitly targets convolutional neural networks with dropout, batch normalization, weight decay, and Leaky-ReLU trained on multi-class datasets — a harder and more realistic setting.

- **Unified loss framework integrating three theoretically-motivated signals** (Section 3.4, Equations 8–11): The paper formalizes three properties (confidence, robustness to perturbations, gradient norms) into a single differentiable reconstruction objective, going beyond prior inversion approaches that relied on a single signal.

---

## Weaknesses

### Fatal
None. The paper describes a complete method and provides visual results across four datasets. However, the evaluation gaps documented below are severe enough to prevent acceptance in current form.

### Major

- **No quantitative evaluation metrics.** The entire experimental evaluation (Section 4) is purely qualitative visual inspection. No FID scores, SSIM values, feature-space distance comparisons, membership inference accuracy, or any other numerical measurement is provided. The paper's central claim — that the method reconstructs data "semantically similar to the original training data" — cannot be assessed beyond subjective visual judgment. For ICLR, a top conference, quantitative evidence is essential.

- **No baselines or comparisons to prior work.** The Related Work section (Section 2) discusses four directly relevant reconstruction papers (Haim et al., 2022; Buzaglo et al., 2023; Balle et al., 2022; Wang et al., 2023). The experiments contain zero comparisons to any existing method. Without baselines, the reader cannot determine whether TLDR advances the state of the art, or whether simpler class-conditional generation would produce similar visual results.

- **No ablation study.** The reconstruction loss (Equation 11) has nine weighted terms (α, α', β, β', γ, δ, η₁, η₂, η₃), corresponding to KL divergence, cross-entropy (original and perturbed), cosine similarity, feature orthogonality, variational loss, pixel loss, and gradient loss. There is no experiment showing whether removing any component degrades quality, or whether the perturbed-image branches contribute anything. This is a basic expectation for any paper proposing a complex multi-term loss, and its absence means the claimed mechanisms are untested.

These three gaps — no quantitative metrics, no baselines, no ablation — compound each other. The paper provides no way for a reader to verify that the proposed signals (confidence, robustness, gradient) are responsible for the observed results, or that those results exceed what generic network inversion or class-conditional generation would produce.

### Minor

- **The "training-like" claim is not empirically distinguished from class-typical generation.** The three signals (confidence, robustness, low gradient norms) are properties of *any in-distribution sample*, not training data specifically. A model will be confident, robust, and have low gradient norms on held-out test data it has never seen. The paper never measures whether generated images are closer to actual training samples than to test samples or to outputs from an unconditional generative model. The method may be generating class-typical images rather than "training-like" ones — these are different claims, and the paper's evaluation cannot distinguish them.

- **Nine loss hyperparameters are defined but their numerical values are never reported.** The weights α, α', β, β', γ, δ, η₁, η₂, η₃ are central to the method (they control the balance of all loss terms). Without any values, the results cannot be reproduced or assessed for sensitivity.

- **Classifier and generator architectures are under-specified.** The classifier is described as "a simple multi-layer convolutional neural network consisting of convolutional layers, dropout layers, batch normalization, and leaky-relu activation followed by fully connected layers and softmax" — no number of layers, filter sizes, kernel sizes, stride, or padding. The generator description is similarly vague: "multiple layers of transposed convolutions, batch normalization and dropout layers." This is insufficient for reproducibility.

- **No classifier test accuracy reported.** If the classifier generalizes poorly, the reconstruction results may reflect memorization rather than the claimed properties. Reporting test accuracy is standard context for any reconstruction attack.

- **Training splits and data handling are unclear.** The paper reports training on "datasets of size 1000, 10000 and 60000" for MNIST and similar variants for other datasets, but does not specify how these subsets were constructed, whether models were trained from scratch on each subset, or what the train/test split was.

### Trivial

- The reconstruction loss equation uses the notation $\mathbf{\dot{\rho}}_{\mathrm{Recon}}$ (line 191) which appears to be a typographic artifact; the text later refers to it as $\mathcal{L}_{\mathrm{Recon}}$.

---

## Nice-to-Haves

- Adding quantitative metrics (FID, feature-space distance to training vs. test samples, membership inference AUC) would directly test the paper's core claims.
- Comparing against prior reconstruction methods (Haim et al., Buzaglo et al.) adapted to the CNN setting, or against an inversion-only baseline that removes the three "reconstruction signals."
- Ablating each loss component to validate the contribution of the perturbed-image branches, gradient loss, and diversity terms.
- Reporting loss weight values and a sensitivity analysis.

---

## Removed Points

These points were raised by reviewers but removed during filtering. They are flagged here for completeness and should be treated with caution:

- **"Reconstruction is a misnomer" framing as a structural/fatal issue** — The paper consistently uses "training-like" language and does not claim pixel-perfect recovery of specific training samples. The concern about whether the method generates class-typical vs. training-specific data is retained as a Minor weakness above (framed as an evidence gap rather than a structural flaw).
- **"Vector conditioning 'complicates' training reads as bug not feature"** — This is a subjective opinion about a design choice, not a concrete weakness.
- **Gradient loss computational cost discussion missing** — A minor oversight but not impactful enough to retain as a standalone weakness given the larger evaluation gaps.
- **"No discussion of limitations in conclusion"** — This is conventional but not a substantive weakness; papers can have no explicit limitations section.
- **Missing appendix/proof/content concerns** — Parser-stripped content is assumed present in original submission; not a valid criticism.
- **Reproducibility concerns about cited works** — Hard rule: all cited entities are assumed to exist.

---

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses surface the same fundamental issue: the gap between the paper's ambitious framing and its thin evaluation. No genuinely novel observation emerges that goes beyond what the paper itself says or what a straightforward reading reveals.

---

## Suggestions

1. Add quantitative evaluation: at minimum, compute FID between generated images and training images (vs. test images as control), and report feature-space nearest-neighbor distances to training samples.
2. Add at least one baseline: compare against inversion-only training (using just $\mathcal{L}_{\mathrm{Inv}}$) and against a simple class-conditional GAN to show that the reconstruction signals produce outputs closer to *training* data specifically.
3. Add an ablation study removing each of the three "reconstruction signals" (confidence enhancement via hot vectors, the perturbed-image branches, gradient loss) and reporting the quantitative effect.
4. Report all loss weight values, classifier test accuracies, and architecture details sufficient for reproduction.
5. Clarify the scope: distinguish whether the method aims to reconstruct actual training examples (which would require per-sample matching) or to generate training-like (class-typical) data. The privacy-risk framing should be calibrated to the actual capability demonstrated.

---

## Score and Decision

**MY FINAL SCORE:** <score>4.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>