Now I have a thorough understanding of the paper and all claims. Let me produce the consolidated review.

---

## Summary

This paper studies deep neural networks trained with shuffled (corrupted) labels — so-called "memorized models" that achieve high training accuracy on noise but poor test accuracy. The authors show, surprisingly, that the hidden-layer representations of such models retain substantial information useful for generalization, which can be decoded using a simple Minimum Angle Subspace Classifier (MASC) built from PCA-based class-conditioned subspaces. For example, an MLP trained on MNIST with 100% label corruption achieves chance-level test accuracy, yet MASC using true training labels on the final hidden layer reaches 95% test accuracy. The paper provides evidence across multiple architectures (MLP, CNN, AlexNet) and datasets (MNIST, Fashion-MNIST, CIFAR-10, CIFAR-100, Tiny ImageNet) that memorization and generalization are not antithetical — the latent generalization ability persists even when the model's own readout is severely degraded.

## Strengths

1. **Core empirical finding is striking and well-demonstrated.** The paper shows that for memorized models, MASC applied to hidden-layer outputs achieves test accuracy far exceeding the model's own test accuracy. For MLP-MNIST with 80% corruption (~72% labels changed), model test accuracy is 34% but MASC test accuracy on later layers exceeds 80% (Section 4, Figure 1). This directly supports the claim that generalization is not erased from the representations even when the model's output is poor.

2. **Using true labels post hoc produces remarkably strong results, even for 100% corruption.** For models trained with completely shuffled labels, MASC built using true (not corrupted) training labels achieves 95% test accuracy on MLP-MNIST (final FC layer) and 69% on CNN-Fashion-MNIST (Section 5, Figure 2). This is a striking proof-of-principle that even fully memorized models retain powerful generalization information in their hidden layers.

3. **Simultaneous demonstration of memorization and generalization coexistence.** In several settings, the same MASC classifier achieves both high accuracy on the corrupted training labels and strong test accuracy on true labels (e.g., CNN-Fashion-MNIST with 40% corruption: ~85% true training accuracy at the Flat(576) layer alongside strong test accuracy). This directly shows that the same layer representation supports both memorization of noise and generalization to clean data (Section 4, Figure 1).

4. **Addresses a gap in prior work.** The paper explicitly notes that Alain & Bengio (2018) avoided examining memorized networks because they believed probes would overfit. The present results directly challenge this assumption and show probing is not only feasible but reveals hidden generalization (Section 2).

5. **Systematic experimental setup across architectures and datasets.** The paper evaluates MLP, CNN, and AlexNet on MNIST, Fashion-MNIST, CIFAR-10, CIFAR-100, and Tiny ImageNet with corruption levels from 0% to 100% (Section 3). The consistent pattern across these diverse settings strengthens the claim that the phenomenon is general.

## Weaknesses

### Fatal
None.

### Major

1. **Missing standard baseline: linear probing.** The paper claims MASC achieves "dramatically better" test accuracy than the model, but never compares against the simplest and most widely-used baseline for measuring what information is linearly decodable from a layer — a linear classifier (e.g., logistic regression or SVM) trained on the same hidden-layer outputs (Alain & Bengio, 2018). Without this comparison, it is impossible to determine whether MASC's performance reflects a non-trivial geometric property or merely the fact that *any* alternative readout can exploit the representation better than the model's own final layer (which is forced to minimize loss on corrupted labels). If a linear probe achieves similar or better accuracy, the core claim is weakened (though not invalidated — the information's existence is still demonstrated). If a linear probe fails but MASC succeeds, that would substantially strengthen the paper. This omission is the single most significant weakness in an otherwise interesting study.

2. **The paper's central claim about breadth is not fully supported in the main paper.** The text asserts "for every corrupted model we have ... MASC in at least one layer has better testing accuracy than the corresponding model itself" and "Results for model with regularization are shown in Figure 29 and 31" (Section 5), but the main paper shows results for only three model/dataset combinations (MLP-MNIST, CNN-Fashion-MNIST, AlexNet-CIFAR-100). While the appendix likely contains more, the main paper should include a compact summary (e.g., an aggregated table or plot with one marker per model/layer across all conditions) so that readers can evaluate the claimed breadth without consulting external material. This is not fatal — 3 architectures × 6 corruption levels × multiple layers is substantial — but the broadness of the claim deserves a broader summary in the main text.

### Minor

1. **PCA centering procedure is a deliberate but incompletely justified design choice.** The paper adds the negation of each sample to center the data and obtain linear subspaces through the origin (Section 3). The reviewer's characterization of this as a "methodological error" is incorrect — the authors explicitly state their goal is subspaces (through the origin) rather than affine spaces, and their procedure achieves this. However, the paper never justifies *why* subspaces through the origin are preferable to affine spaces for the angle-based classifier, nor does it compare results to standard centered PCA (which would yield affine spaces). A brief justification or ablation would strengthen the methodological presentation. This does not invalidate the results (the subspaces are well-defined and the empirical findings are what they are), but greater clarity would help.

2. **No discussion of edge cases in MASC.** The angle-based decision rule could produce ties or near-zero angles when the subspace dimensionality is high (approaching the number of data points). The paper does not discuss how ties are resolved or how robust the method is when the subspace captures nearly all variance, making angles near zero for multiple classes. This is a minor technical gap.

3. **Limited analysis of the 99% variance threshold.** The paper fixes the PCA variance threshold at 99% without a sensitivity analysis. The number of components per class varies across layers and corruption levels (deferred to Figure 16/17 in the appendix). A brief sensitivity study or discussion of how results change with this threshold would strengthen the methodological contribution.

### Trivial
None.

## Nice-to-Haves

- A linear probe baseline (logistic regression on the same hidden-layer outputs) for all MASC experiments. This is the single most impactful addition the authors could make.
- A compact summary table or aggregated plot in the main paper showing MASC test accuracy vs. model test accuracy across all model/dataset/corruption combinations.
- A brief ablation comparing the paper's negation-based centering to conventional centered PCA (i.e., subtract class mean, then run PCA on that) to show robustness.
- Sensitivity analysis of the 99% variance threshold on one or two representative cases.

## Removed Points

The following criticisms from the reviewers were evaluated against the paper and found to be invalid or not applicable:

1. **"Flawed PCA centering procedure":** The reviewer claimed this is a "methodological error" that makes results "suspect." The paper explicitly states the goal is subspaces through the origin (not affine spaces), and the negation trick is a deliberate design choice to achieve this. This is a valid approach, not an error. The paper could justify the choice better (hence retained as Minor weakness #1 above), but the reviewer's characterization as a fatal flaw is incorrect.

2. **"Writing is notably sloppy in places (e.g., 'We ran ran some preliminary experiments,' 'the work has been beyond the scope'):** The phrase "We ran ran" does not appear in the paper — the paper says "We ran some preliminary experiments" (line 45). The phrase "While this has been beyond the scope of the present paper" (line 74) is grammatically standard English. These are not errors.

3. **"Over-reliance on appendix for supporting evidence":** This criticism has been substantially downgraded. The main paper presents core results for 3 architectures with 6 corruption levels each — a substantial body of evidence. Deferring additional experiments (Dropout, Adam variants, Tiny ImageNet) to the appendix is standard practice. The concern about the breadth claim lacking an aggregated summary is retained as a Minor weakness.

4. **"MASC is an unusual classifier that relies only on the angle":** This is an observation, not a weakness. The paper clearly describes the angle-based decision rule and the angle is a geometrically meaningful quantity (the sine of the angle equals normalized reconstruction error for a projected point in a subspace through the origin).

5. Various formatting/style nitpicks: removed per instructions.

## Novel Insights

The most interesting synthesis that emerges from this review is that the paper's core finding — hidden layers of memorized networks encode generalization ability — may be more fundamental than the paper itself claims. The authors frame this as a surprising phenomenon, but the neuroscience parallel they draw (decoders outperforming behavior in animals) hints that this might be a general property of overparameterized learning systems, whether biological or artificial. If correct, this suggests that "good" representations encode useful structure about the data manifold regardless of the training objective, and that memorization and generalization are not competing processes but parallel encoding pathways in the same weights. The paper's weakest link is the missing linear probe baseline, which would clarify whether this is a deep geometric insight about subspaces or simply a rediscovery that linear readout from hidden layers (standard probing) works on memorized networks — a possibility the authors should directly address.

## Suggestions

1. **Add linear probe baselines** (logistic regression or SVM) for every MASC experiment. This is critical to establish whether MASC is necessary for the effect or whether any reasonable decoder reveals the same information. If linear probes match MASC, reframe the contribution around the *existence* of decodable generalization in memorized models (still valuable). If MASC outperforms linear probes, analyze why.
2. **Add a compact summary figure** (e.g., MASC test accuracy vs. model test accuracy as a scatter plot with one marker per model/layer/corruption condition) to the main paper to visually establish the breadth of the phenomenon.
3. **Briefly justify or ablate the subspace-through-origin vs. affine space choice** to address the PCA centering concern.
4. **Add a short sensitivity study** of the 99% variance threshold on one representative model.

## Score and Decision

**Originality:** The finding that memorized networks retain strong decodable generalization is surprising and challenges common assumptions. The MASC classifier itself is a relatively simple tool, but the empirical discovery is original.

**Importance:** The question of why overparameterized networks generalize is a central open problem in deep learning. Showing that generalization information persists even under extreme memorization reframes the debate and demands explanations from generalization theory.

**Claims support:** The core claims are supported by the experiments shown, but the absence of linear probe baselines weakens the claim about MASC specifically. The breadth claim is supported by the model/dataset range but would benefit from aggregated presentation.

**Soundness:** The experimental methodology is generally sound. The PCA centering choice is deliberate and valid, though additional justification would help. The main concern is the missing baseline comparison.

**Clarity:** The paper is clearly written and the figures are informative. The methodology is well-described.

**Value:** The paper provides a compelling empirical result that will interest the deep learning theory and representation learning communities.

**Overall assessment:** The paper makes a genuinely interesting empirical finding. The most significant weakness — the absence of linear probe baselines — does not invalidate the core discovery that generalization information persists in hidden layers of memorized networks, but it limits our ability to interpret the specificity of MASC's role. With the addition of linear probe comparisons (or an honest reframing if probes match MASC), this would be a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>