Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper studies why deep networks trained with heavily label-corrupted data (memorized models) generalize poorly. It proposes using a Minimum Angle Subspace Classifier (MASC) — a simple decoder that measures the angle between a layer's activations and class-conditional PCA subspaces — to probe hidden representations of memorized models. The striking empirical finding is that MASC, using only the same corrupted labels available to the model, achieves test accuracy far exceeding the model's own test accuracy across multiple architectures (MLP, CNN, AlexNet) and datasets. Even under 100% label corruption, using true labels (known post hoc) to build subspaces yields near-perfect test accuracy, showing that representations encode true class structure despite training on random pairings.

## Strengths

1. **Novel and striking empirical observation.** The paper demonstrates that hidden representations of models trained with heavily shuffled labels (e.g., 80% corruption, ~72% of labels changed) support dramatically better generalization when decoded via MASC (e.g., 80%+ test accuracy on MLP-MNIST vs. 34% model test accuracy, Section 4). This challenges the intuitive assumption that memorization destroys all generalizable structure in representations.

2. **Striking 100% corruption result via true-label subspaces.** When MASC uses subspaces built from the *true* training labels (known post hoc), it achieves remarkably high test accuracy (95% on MLP-MNIST, 69% on CNN-Fashion-MNIST) even for models trained on entirely random labels (Section 5). This is a proof-of-principle that networks trained on pure noise encode genuine true-class structure — a non-obvious and genuinely surprising result.

3. **Broad empirical scope.** Results span MLPs, CNNs, and AlexNet trained on MNIST, Fashion-MNIST, CIFAR-10, CIFAR-100, and Tiny ImageNet, with corruption levels from 20% to 100% (Sections 4–5, appendix Tables 2–3). The consistency across architectures and datasets supports the claim that this is a general property of overparameterized networks, not an artifact of a specific setup.

4. **Simple, interpretable methodology.** MASC (class-conditional PCA subspaces + minimum-angle decision) is transparent and easy to replicate. The fact that such a straightforward decoder reveals latent generalization makes the finding accessible and reproducible.

5. **Simultaneous memorization and generalization.** The paper shows that in many layers, a single MASC classifier achieves high accuracy on both the corrupted training labels (memorization) and the true test labels (generalization), providing evidence that these abilities can coexist within the same representations (Section 4).

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison to standard probing classifiers (linear probe / logistic regression).** The paper's related work (Section 2) cites Alain & Bengio (2018), noting they avoided memorized networks because "they thought such probes would inevitably overfit." The paper implicitly contrasts MASC's success against this expectation, but never actually tests whether standard linear probes (the standard tool in the probing literature) fail or succeed on these representations. Without this comparison, the central claim — that "the network retains significant latent generalization ability" in its representations — is incomplete. If linear probes also achieve high test accuracy, the claim about representations is strengthened. If they fail while MASC succeeds, the finding is specifically about MASC being an effective decoder, not about representations inherently supporting generalization, and the paper would need reframing. This gap limits the strength of the core conclusion. **(See also: the paper's own discussion in Section 7 acknowledges "it is possible that other classifiers operating on layerwise outputs have better performance than MASC — a possibility that merits further exploration." The same logic applies to standard probing baselines.)**

2. **No control for spurious subspace structure (random-label baseline).** In Section 4, MASC uses the corrupted training labels to build subspaces and achieves test accuracy above the model's. The paper does not include a control where subspaces are built from randomly permuted labels (preserving the same class-count distribution). While the failure of MASC at 100% corruption with corrupted-label subspaces partially addresses this concern (at 100% corruption, labels are essentially random and MASC fails), a direct random-permutation control at intermediate corruption levels would cleanly establish that the specific corrupted label assignments — not just geometric artifacts of having many subspaces — drive the improvement.

### Minor

3. **Section 6 (Inducing memorization in uncorrupted models) is weakly motivated and adds limited insight.** This section shows that a model trained on clean data can also support memorization via MASC with corrupted-label subspaces. This is essentially a symmetry check, but the paper does not clearly articulate what new insight it provides. The claim that MASC test accuracies "approach or exceed uncorrupted model test accuracies" is largely expected — representations learned on clean data are well-separated, so projecting corrupted-label subspaces onto them naturally preserves discriminative structure. This section does not actively harm the paper, but it distracts from the main narrative and could be trimmed or recast as a control in an appendix.

4. **Limited analysis of *why* MASC works.** The paper reports the phenomenon but does not analyze its geometric basis. For instance: Is the improvement driven by tighter subspaces, better class-mean separation, or reduced within-class variance? The paper notes the number of PCA components per layer (appendix figures) but does not discuss trends (e.g., do deeper layers require fewer components, suggesting better class separation?). A simple PCA visualization of layer outputs colored by true vs. corrupted labels would help readers develop intuition. Section 7 notes this as future work ("it would be interesting to see how much the generalization accuracy can be improved"), but some basic analysis in the main paper would strengthen the contribution.

5. **The abstract's framing slightly overclaims.** The abstract says "we provide evidence for the latter possibility" (that the network "chooses" a poor readout). The evidence shows that an *alternative* readout works better, which is consistent with this hypothesis but does not directly demonstrate that the network's own readout is the bottleneck. The paper should acknowledge more explicitly that the cause of poor model test accuracy is not identified — only that a different decoder works well.

### Trivial
None. (The paper is generally well-written with no formatting issues worth flagging.)

## Nice-to-Haves

- **Linear probe results** (as noted in Major #1). This is the highest-leverage addition and would substantially strengthen the paper.
- **Analysis of failure modes.** For models/layers where MASC does not improve over the model, discuss why. Are the representations collapsed? Are subspaces not discriminative?
- **Statistical significance.** With only 3 runs per setting, reporting significance (e.g., paired t-tests over runs for key comparisons) would add rigor.
- **Comment on optimizer choice.** MLP uses SGD while other models use Adam (noted in Section 4). A brief discussion or appendix experiment showing robustness to this choice would preempt concerns.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **100% corruption as a limitation:** The harsh critic claimed this as a significant limitation. The paper explicitly states "except those with 100% corruption degree, we find that our MASC in at least one layer has better testing accuracy than the corresponding model" — the paper is upfront about this boundary. Moreover, Section 5 shows that with true labels, even 100% corruption yields striking results. Not a weakness.
- **Missing appendix / appendix proofs / missing references:** Removed per instructions — these sections exist in the original submission.
- **Section 5 being "less surprising":** The harsh critic claimed this is expected. It is actually non-obvious: a model trained on 100% random labels could have collapsed representations, yet MASC with true labels achieves 95% accuracy on MLP-MNIST. This is a strong result.
- **Section 7 overreach claim:** The harsh critic said "the ability to memorize and generalize may not be antithetical" is overreaching. The paper's evidence supports this — MASC simultaneously achieves high corrupted training accuracy and high test accuracy. This claim is warranted.
- **"The paper should also cover Y / domain Z":** Removed per instructions — these represent scope creep.
- **Missing related works:** Removed per instructions — cannot verify existence from external sources.
- **Formatting/style nitpicks:** Removed per instructions.
- **Reproducibility nitpicks (hyperparameters, trivial details):** Removed per instructions.

## Novel Insights

The most interesting insight that emerges from connecting the reviews is that the paper's central tension — whether the finding is about MASC or about the representations themselves — actually points to a deeper question the paper does not quite articulate. Alain & Bengio (2018) *expected* linear probes to overfit on memorized networks and therefore avoided them. The present paper shows that MASC (a subspace-based probe) does *not* overfit and reveals generalization. This raises the possibility that different probing methods have fundamentally different susceptibility to memorization artifacts: linear probes may overfit because they can exploit individual dimensions, while subspace methods average over many dimensions and are more robust. If this is true, the paper's contribution is not just "representations generalize" but "the *geometry* of representations preserves generalization in a way that individual readout weights do not." This hypothesis connects naturally to the neuroscience parallel (decoders outperform behaving animals) and suggests a general principle: readout mechanisms can be the bottleneck even when representations are rich. The paper would benefit from explicitly framing this hypothesis and testing it (e.g., comparing linear probes, kernel methods, and MASC systematically).

## Suggestions

1. **(Highest priority)** Add linear probe (logistic regression) results on the same layerwise outputs, for the same models and corruption levels. This directly addresses whether the finding is about representations or about MASC specifically. If linear probes fail, the paper should reframe around MASC's unique properties. If they succeed, the claim about representations is substantially stronger.
2. Add a random-label subspace control: for a subset of models and corruption levels, randomly permute the corrupted labels (preserving class counts) before building MASC subspaces, and report test accuracy.
3. Include a basic geometric analysis: for at least one model-dataset pair, show a PCA visualization of layer outputs colored by true vs. corrupted labels to help readers develop intuition for why MASC works.
4. Tighten the framing in the abstract and introduction to acknowledge that the paper shows an *alternative readout works better*, not that the network's own readout is definitively the bottleneck.

## Score and Decision

The paper presents a genuinely interesting and non-obvious empirical finding, supported by extensive experiments across architectures and datasets. The two main gaps — the missing linear probe comparison and the random-label subspace control — are addressable and limit the strength of the conclusion but do not invalidate the core observation. The paper is clearly written, the methodology is sound for what it aims to demonstrate, and the finding itself is thought-provoking with potential implications for understanding generalization in overparameterized networks.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>