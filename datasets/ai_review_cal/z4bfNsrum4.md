- Decision: Reject
- Avg Score: 3.80
- Scores: 1, 3, 6, 3, 6
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper investigates whether deep neural networks trained with shuffled (corrupted) labels retain latent generalization ability in their hidden representations, even when the model itself exhibits poor test accuracy. The authors propose a Minimum Angle Subspace Classifier (MASC) built from PCA-derived class-conditional subspaces of layer outputs, and show that MASC can achieve substantially higher test accuracy than the original model across multiple architectures (MLPs, CNNs, AlexNet) and datasets (MNIST, Fashion-MNIST, CIFAR-10/100, Tiny ImageNet). The most striking result is that when true training labels are used post hoc to construct subspaces, MASC achieves near-uncorrupted test accuracy (95% on MLP-MNIST) even for models trained with 100% label noise that themselves perform at chance.

## Strengths

- **MASC reveals hidden generalization in heavily memorized models (Section 4, Figure 1):** Using only the model's hidden-layer outputs and the same corrupted training labels that were available to the model, MASC test accuracy on MLP-MNIST with 80% corruption exceeds 80%, versus the model's 34%. This concretely demonstrates that internal representations retain generalization ability that the model's own readout does not exploit.

- **True-label subspaces recover near-uncorrupted test performance (Section 5, Figure 2):** When true training labels are known post hoc, MASC achieves 95% test accuracy on MLP-MNIST (100% corruption), 69% on CNN-Fashion-MNIST, and performance close to the uncorrupted model in several settings. This is strong evidence that latent generalization persists to a degree not previously recognized.

- **Simultaneous memorization and generalization in a single classifier (Section 6, Figure 3):** On generalized (uncorrupted) models, MASC built from corrupted-label subspaces can achieve high accuracy on both the shuffled training labels and the true test labels — showing these two abilities can coexist in the same representations.

- **Addresses a gap in prior probing literature (Section 2):** The paper explicitly contrasts with Alain & Bengio (2018), who avoided studying memorized networks because they expected probes to overfit. The results show this expectation does not hold, and also challenge the claim from Stephenson et al. (2021) that memorization is localized to later layers.

- **Simple, model-agnostic methodology validated across diverse architectures and datasets (Section 3):** MASC uses only PCA and angle-based classification yet produces consistent trends across MLPs, CNNs, and AlexNet on five datasets, supporting the generality of the findings.

## Weaknesses

### Fatal

None.

### Major

- **Missing baseline comparisons to standard probing methods weaken the central claim.** The paper never compares MASC to a standard linear probe (logistic regression on layer outputs) or a nearest-centroid classifier using the same representations. The paper discusses probing (Alain & Bengio, 2018) but does not run the obvious control. Without this comparison, it is unclear whether MASC's success reflects a specific geometric property of subspace angles or simply that representations under label noise are highly informative and *any* reasonable classifier would outperform the original model's readout. If a linear probe matches MASC, the paper's contribution reduces to "representations retain structure despite label noise" (valuable but less surprising); if MASC substantially outperforms linear probes, that would strengthen the novelty. This gap affects the interpretation of every empirical result.

- **Non-standard PCA centering procedure is unexplained and unaudited (Section 3, line 22).** The paper adds the negative of each sample to the dataset before PCA, forcing the empirical mean to zero. The stated goal is to obtain linear subspaces (passing through the origin) rather than affine spaces. While this manipulation is equivalent to uncentered PCA (computing on the second moment matrix), the paper does not state this equivalence, compare with standard mean-centering + distance-to-affine-space classification, or ablate whether the specific centering choice affects results. If the qualitative trends depend on this design decision, the interpretation of "latent generalization" becomes fragile. If they do not, the paper should demonstrate robustness.

### Minor

- **The "choice" framing is imprecise and unnecessary (Abstract, Section 1).** The paper sets up the narrative as the network "choosing" a poor readout. The scare quotes partially soften this, but the framing implies a form of agency that is not supported by the evidence. Showing that a different decoder works better than the model does not mean the network "chose" the worse one — the model optimized corrupted-label training accuracy, not test accuracy. The empirical finding (representations retain structured generalization information) is interesting on its own without this metaphor.

- **Section 6 claims are overstated relative to what is shown.** The section is titled "Inducing Memorization in Uncorrupted Models" but what is actually shown is that MASC built on corrupted subspaces from generalized representations can still achieve good test accuracy. This demonstrates robustness of representations, not "induction of memorization" in any causal sense. The results are interesting but the framing over-interprets them.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis for the PCA variance threshold (99% used throughout; testing 90%, 95%, 99.5% would demonstrate robustness).
- A sanity check applying MASC to random representations (e.g., an untrained network) to verify the test accuracy is not an artifact of the method itself.
- Reporting the typical number of PCA components retained per class for each experiment.

## Removed Points

These points from the inputs were removed, with justification:

1. **"Insufficient statistical rigor / only 3 runs"** — Removed. The paper reports 3 runs with shaded range (line 27). For this type of probing analysis with large effect sizes (e.g., 80% vs 34%), 3 runs is standard. The critic's demand for more runs or confidence intervals exceeds the community norm for this setting.

2. **"Model details / hyperparameters missing from main text"** — Removed. The paper references Section A.2 for hyperparameters. The parser strips appendix content; these details exist in the original submission.

3. **"Comparison to early stopping not shown in main text"** — Removed. References Section A.4 (appendix). Exists in original submission.

4. **"Could MASC be picking up easy examples?"** — Removed. Speculative and not a specific, verifiable weakness. No evidence this is a problem.

5. **"Neuroscience analogy is a stretch"** — Removed. This is an opinion about a speculative paragraph in the Discussion section, not a weakness of the scientific contribution.

6. **"MASC doesn't use the same information as the model"** — Removed. The paper's claim is about *information* (same dataset, same labels, same hidden outputs), not about *processing*. The critic conflates these. The paper's statement is factually correct.

7. **"Section 5 should check linear probe with true labels"** — Merged into Major weakness #1 (missing baseline comparisons). Already covered.

8. **"No discussion of why prior work feared overfitting in probes"** — Removed. The paper cites Alain & Bengio's concern (Section 2). A deeper discussion would be nice but is not a weakness.

## Novel Insights

The reviews surface one insight that goes beyond the paper's own contributions: the PCA centering procedure (adding negated samples) may be more significant than the authors acknowledge. The paper presents this as a technical detail, but it effectively computes uncentered PCA (on the second moment matrix) rather than standard mean-centered PCA. Whether the qualitative results survive standard mean-centering (using distance-to-affine-space instead of angle-to-subspace) is an open question the reviews correctly identify but the paper does not address. Apart from this, no genuinely novel synthesis emerges beyond what the paper already claims.

## Suggestions

1. **Add linear probing baselines.** Train logistic regression (or a linear SVM) on each layer's hidden outputs using the same corrupted training labels. Compare test accuracy to MASC across all corruption levels. This is the single most important control for establishing the specificity of MASC's geometric approach.

2. **Clarify and ablate the PCA centering procedure.** Either (a) explain that adding negations is equivalent to uncentered PCA and justify why uncentered PCA is appropriate, or (b) compare results with standard mean-centering followed by distance-to-affine-space classification to show robustness.

3. **Drop the "choice" narrative or substantially weaken it.** Frame the contributions as: "hidden representations in memorized models retain structure supporting generalization, which can be decoded by a simple subspace-angle classifier." The anthropomorphic framing adds confusion without explanatory power.

4. **Tighten Section 6's framing.** Rename the section to something like "Robustness of Representations to Post-Hoc Label Corruption" and explicitly state what the experiment shows versus what it does not.

5. **Conduct the MASC-on-random-representations sanity check** to rule out that the method itself produces spuriously high accuracy.
