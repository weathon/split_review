Now I have all the information I need. Let me produce the final consolidated review.

## Summary

The paper investigates why deep neural networks trained with heavily shuffled labels generalize poorly. It proposes a Minimum Angle Subspace Classifier (MASC) applied to hidden layer outputs and demonstrates a striking finding: even when the model itself achieves near-chance test accuracy, MASC using the same corrupted training labels recovers dramatically better test accuracy (e.g., >80% vs. 34% for MLP-MNIST at 80% label corruption). The paper also shows that using true labels post-hoc yields even stronger results, and it examines the reverse direction (inducing memorization in generalized models). The core contribution is evidence that hidden representations of memorized networks retain substantial latent generalization ability.

## Strengths

- **Genuinely surprising and non-obvious finding.** The paper demonstrates across multiple architectures (MLP, CNN, AlexNet) and datasets (MNIST, Fashion-MNIST, CIFAR-10, CIFAR-100, Tiny ImageNet) that hidden-layer representations from models trained with heavily shuffled labels support far better generalization than the model itself, using only the same corrupted labels. The MLP-MNIST example at 80% corruption (MASC >80% test accuracy vs. model 34%) is particularly striking.

- **Simple, transparent methodology.** MASC is straightforward — class-wise PCA subspaces on hidden layer outputs, followed by minimum-angle classification. This simplicity makes the surprising results easy to trust and reproduce, and avoids the opaque complexity that sometimes clouds representational analyses.

- **Systematic experimental scope.** The paper tests across corruption levels (0%–100%), multiple architectures (MLP, CNN, AlexNet), and multiple datasets, with results averaged over 3 runs. The consistency of the pattern across settings strengthens the generality of the claim.

- **Bidirectional investigation provides a complete picture.** Beyond the main finding (Section 4), Section 5 probes representational fidelity using true labels post-hoc, and Section 6 reverses the question by inducing memorization in generalized models. This symmetry adds depth even if Section 6 is less impactful.

- **The paper explicitly acknowledges its own limitations.** The discussion (line 74) notes that other classifiers may outperform MASC and that this is a "proof of principle" — a refreshing level of intellectual honesty.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison to standard probing methods (linear classifiers).** This is the most significant gap. The paper claims that MASC reveals latent generalization ability, but never compares against a simple linear probe (e.g., logistic regression or linear SVM) trained on the same hidden-layer outputs with the same corrupted labels. Prior work (Alain & Bengio, 2018) explicitly used linear probes on hidden layers but avoided memorized networks because they expected overfitting. The paper mentions this but does not run the comparison. Without this baseline, it is unclear whether the improvement is a special property of MASC's subspace geometry or simply reflects the fact that *any* reasonable classifier applied to hidden layers of a memorized network recovers generalization. This does not invalidate the core finding (the representations do preserve generalization ability), but it limits what can be claimed about MASC specifically and about the mechanism of the effect.

### Minor

- **Section 5's framing blurs the line between two distinct findings.** The paper clearly states that Section 5 uses true labels known post-hoc (line 25, line 49), but the paper's overarching narrative of "decoding generalization from memorization" somewhat conflates the Section 4 result (using only corrupted labels — genuinely decoding from the memorization process) with the Section 5 result (using privileged true label information — a proof of representational fidelity). The paper would benefit from a more explicit demarcation: e.g., Section 4 shows the *model could have generalized*, while Section 5 shows that *representations preserve class structure to a remarkable degree*. This distinction matters for interpreting what is being "decoded" and from what information.

- **No ablation on the PCA variance threshold.** The paper uses 99% variance explained universally without testing sensitivity (e.g., 90%, 95%, 99.9%). Since the number of PCA components directly affects both overfitting risk and the geometry of the angular classification, an ablation study (even a brief one) would strengthen confidence in the results.

- **No analysis of *why* MASC works.** The paper does not examine the underlying geometry (e.g., principal angles between class subspaces, whether subspaces become more or less separated under corruption). A measure of subspace similarity or angular separation across classes could help explain why the angle-based classifier succeeds and what changes in the representation space as corruption increases.

- **Section 6 (inducing memorization in generalized models) is the least impactful part of the paper.** The finding that MASC on a well-trained generalized model's layers can achieve high accuracy on corrupted labels is not particularly surprising — the representations are known to be high-quality. The paper would not lose much by abbreviating or omitting this section to make room for more substantive analyses.

### Trivial

- Numerical values that support key claims (e.g., exact test accuracies at specific layers) are only presented in plots, not stated explicitly in the text. The shading in figures conveys range over 3 runs, but explicit numbers with variance in the text would improve readability.
- The neuroscience analogy in the discussion (line 76) is evocative but purely speculative — acceptable in a discussion section but adds little substance.

## Nice-to-Haves

- t-SNE or UMAP visualizations of hidden layer outputs colored by true vs. corrupted labels for a high-corruption model would visually reinforce the claim that representations cluster by true class.
- A plot of MASC test accuracy vs. training epoch (for a fixed layer) would help connect to the known early-learning phenomenon (Arpit et al., 2017) and show whether the subspace organization degrades over training.
- Testing on non-uniform label noise (e.g., asymmetric or instance-dependent noise) would generalize the findings beyond the uniform shuffling setting.

## Removed Points

These points from the reviewers were flagged for removal; treat them with caution.

- **"Central claim conflates two logically distinct findings"** (Harsh Critic Point 1): The paper explicitly distinguishes Section 4 (corrupted labels) from Section 5 (true labels) in the methodology (line 25) and contributions (line 16). Overstated — reduced to a minor framing issue above.
- **"The true-label experiment does not support the claimed contribution"** (Harsh Critic Point 3): Overlaps with Point 1. The paper's framing of Section 5 is transparent about using true labels. Reduced to a minor issue.
- **"Introduction — dramatic language not quantified"**: A presentation nitpick about numbers not appearing until later. Trivial and applies to most papers.
- **"No discussion of why subspaces vs affine spaces"**: The paper does address this (line 22 — adding negative copies to force zero mean and obtain subspaces rather than affine spaces). Partially addressed.
- **"Variance/range not reported in text"**: Range IS conveyed via shading in plots (line 27). Sufficient.
- **"Discussion neuroscience comparison is unsupported"**: Appropriate for a discussion section; not a weakness.
- **"PCA implementation not specified"**: Trivial implementation detail.
- **"Number of training samples per class not discussed"**: Academic nitpick.
- **"Section 6 is weak/tangential"**: The paper frames it as Contribution 3; adding symmetry has value even if results are less surprising. This is an opinion, not a weakness.
- **All strengths from the Strength Finder that conflict with verified weaknesses**: No conflicts — the strengths are about the phenomenon itself, not about methodological claims that the weaknesses challenge.

## Novel Insights

The most interesting insight emerging from this review that goes beyond the paper's own contributions is about the asymmetry between representation quality and readout quality in memorized networks. The paper shows (Section 4) that a simple subspace classifier on hidden layers using the *same* corrupted labels available to the model can far outperform the model itself. This suggests that the model's final readout layer is the bottleneck, not the representations — the network's architecture learns class-conditional subspaces that preserve more true-label structure than the model can leverage. Combined with the missing linear probe baseline, this raises the possibility that the phenomenon is even more general than MASC: perhaps any reasonable decoder applied to these hidden layers would recover generalization, implying the representations are remarkably robust while only the learned classifier collapses. The fact that this happens even as the model's own readout degrades to near-chance performance is a strong hint about where inductive biases break down under label noise.

## Suggestions

1. **Add linear probe baselines.** Train logistic regression or linear SVM on the same hidden-layer outputs using corrupted training labels. If these also outperform the model, the core finding is strengthened — it shows the representations themselves retain generalization ability, not just MASC's specific geometry. If they do not, it highlights MASC's unique advantage. Either outcome is informative.

2. **Restructure the narrative to foreground Section 4 as the primary contribution.** Make Section 5 explicitly a "representational fidelity" demonstration rather than "decoding generalization." The current presentation blurs two logically distinct claims and dilutes the paper's sharpest result.

3. **Add a brief ablation on the PCA variance threshold** (90%, 95%, 99%, 99.9%) for at least one model/dataset pair to demonstrate robustness.

4. **Add a geometric analysis** — compute principal angles between class subspaces under different corruption levels to explain why the angle-based classifier succeeds.

5. **Report explicit numerical values with variance** in the text for the key results, rather than relying solely on figures.

## Score and Decision

The paper reports a genuinely surprising and well-demonstrated finding that challenges conventional wisdom about the relationship between memorization and generalization in overparameterized networks. The experimental scope is adequate, the methodology is transparent, and the core result (Section 4) is robust across architectures and datasets. The main weakness — absence of linear probing baselines — limits mechanistic interpretation but does not invalidate the empirical phenomenon. The narrative could be better structured to avoid conflation of two distinct results. With moderate revisions (adding baselines, clearer framing), the paper makes a solid contribution.

**Originality**: High — the finding that hidden representations of heavily memorized networks support far better generalization than the model itself is surprising and not predicted by existing theories.  
**Importance**: High — sheds light on the memorization-generalization tension in overparameterized models, a central issue in deep learning theory.  
**Claims supported**: Mostly — Section 4 is well-supported; Section 5's framing somewhat overreaches.  
**Experiments**: Broad in scope but missing key baselines (linear probes).  
**Clarity**: Clear methodology and figures; narrative framing could be crispier.  
**Value to community**: The paper will likely stimulate follow-up work on representational analysis of memorized networks and subspace-based decoding methods.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>