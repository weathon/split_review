Here is my final consolidated review:

---

## Summary

This paper proposes GradSimCore, a coreset selection method that ranks training samples by how many other samples within the same class have similar loss gradients (computed w.r.t. the final classification layer of a randomly initialized ResNet-18). The top-ranked samples per class form the coreset. The method simplifies prior gradient-matching approaches (CRAIG, GRAD-MATCH) by avoiding per-element step sizes and iterative coreset reconstruction. The paper evaluates on CIFAR10, CIFAR100, and ImageNet-1K, and includes cross-architecture experiments.

## Strengths

- **Practical simplification over prior gradient-matching methods.** The paper clearly identifies two barriers in CRAIG (per-element step sizes that complicate mini-batch training) and GRAD-MATCH (iterative coreset reconstruction during training) and proposes a method that sidesteps both (lines 22–23, 26). This is a concrete, verifiable improvement in deployability regardless of the accuracy comparison.

- **Nearest-neighbor speedup for scaling.** Replacing the O(N²) pairwise similarity computation with a radius-based nearest-neighbor search (Section 4.2, line 85) is a sensible optimization that makes the method tractable for ImageNet-scale datasets, and the ≈10× speedup claim is a concrete algorithmic contribution.

- **Cross-architecture evaluation.** The paper tests coresets selected with ResNet-18 on VGG16 and Inception-V3 (Tables 3–4, lines 109–111). While the results are compared against DeepCore's reported numbers (which is a separate issue), the *attempt* to evaluate transferability goes beyond what many coreset papers do and is a worthwhile experimental dimension.

## Weaknesses

### Fatal

None.

### Major

- **The central claim of outperforming SOTA is unsubstantiated because the experimental comparison is not controlled.** The paper states: "We compare the mean accuracy obtained by our method with the best mean accuracy reported by DeepCore" (line 96) and "we use the results they reported to identify the state-of-the-art results" (lines 34–36). This means the baselines were not re-run under identical conditions. The paper discloses almost no training hyperparameters (only "200 epochs starting with a randomized initial seed in PyTorch," line 96) — optimizer, learning rate, batch size, weight decay, and learning rate schedule are all absent. Without knowing whether the training protocol matches DeepCore's, any accuracy difference — positive or negative — could be attributed to training configuration rather than coreset quality. Since the paper's headline claim ("outperforms the state-of-the-art coreset selection algorithms," line 4) rests on these comparisons, this is a structural weakness that prevents the reader from evaluating the method's effectiveness. This cannot be fixed with minor additions; it requires re-running all baselines under a controlled protocol.

### Minor

- **The selection procedure's own computational cost is not quantified, undermining the efficiency motivation.** The paper motivates coreset selection by the need to reduce computational cost (lines 10–18) but never reports wall-clock time or FLOPs for the selection process itself. The ≈10× speedup from the nearest-neighbor approximation (line 85) is relative, not absolute. For ImageNet-1K with 1.28M images, the forward pass + gradient computation + NN search is a significant overhead that may partially or fully offset the training savings — especially since the coreset is selected once and used for a single training run. Without accounting for this, the paper cannot substantiate its core motivation.

- **No full-dataset (100%) accuracy reported.** The paper never reports the accuracy achieved when training on the full dataset. Without this upper bound, it is impossible to contextualize how much accuracy is sacrificed at each coreset fraction. This is a standard reference point in coreset papers.

- **Cross-architecture results are presented without rationale or analysis.** The paper evaluates coresets selected with ResNet-18 on VGG16 and Inception-V3 (Tables 3–4) but provides no explanation for why gradient similarity from one architecture should transfer to another. If this works, it is an interesting empirical finding, but the paper does not engage with *why*, leaving the experiments as unexplained observations.

- **The method is underspecified in prose.** While equations 3–4 and Algorithm 1 (stripped by the parser) likely provided the exact scoring formulas in the original submission, Section 3 ("Methodology") is essentially empty — only a single sentence stating the focus on CNNs (lines 62–64). The prose does not define the similarity metric, describe how the nearest-neighbor radius is chosen (class-dependent? fixed?), or specify the scoring function that converts neighbor counts to ranks. A reader relying on the text alone cannot implement the method without reverse-engineering from the code.

- **Abstract overclaims scope.** The abstract claims evaluation "ranging from MNIST to ImageNet" (line 4), but experiments only cover CIFAR10, CIFAR100, and ImageNet-1K. MNIST, QMNIST, FashionMNIST, and SVHN are mentioned as part of the DeepCore framework (lines 34–35) but are not tested.

### Trivial

- The paper uses "againsts" (lines 103, 126, 137) instead of "against."

## Nice-to-Haves

- Reporting standard deviations alongside mean accuracies (the paper mentions 10 runs but the values are not visible in the table images).
- A simple analysis (e.g., histogram of gradient similarity distributions within and across classes) to support the paper's core intuition that same-class samples have similar gradients.
- Wall-clock time comparison of selection cost vs. training savings.
- Comparison of selection time with CRAIG/GRAD-MATCH to substantiate the claimed practical advantages.

## Removed Points

The following points from the input reviews were removed per the filtering guidelines:

- *Criticism that the method's novelty relative to gradient-matching approaches is unclear* → partially removed. The harsh critic's claim that the method is "underspecified" due to missing equations (3, 4) and Algorithm 1 is removed because these are parser-stripped artifacts that existed in the original submission. However, the prose underspecification (Section 3 being empty) is retained as a Minor weakness.

- *Criticism about missing distinction between GradSimCore and GraNd/EL2N* → removed per the rule "DO NOT mention missing related works," as the reviewer cannot independently verify whether GraNd/EL2N's relationship was discussed in a stripped section.

- *"SOTA accuracy" strength from Strength Finder* → dropped because it directly conflicts with the verified Major weakness about uncontrolled comparison (strength-weakness conflict rule).

- *Critique about parser artifacts (typos, formatting)* → removed per hard rules.

- *Criticism about not releasing code* → the paper provides an anonymous code link (line 4), so this is factually incorrect.

- *Criticism about DeepCore results being from a different experimental protocol without evidence this matters* → weakened but kept. The verifiable issue is the *absence* of training hyperparameter specification, not the *certainty* that protocols differ.

## Novel Insights

None beyond the paper's own contributions. The harsh critic correctly identifies the core structural issue (uncontrolled comparison) but does not surface a novel research opportunity or framing that the paper itself misses. The strength finder correctly notes the simplification over CRAIG/GRAD-MATCH but does not add insight beyond what the paper already articulates.

## Suggestions

1. **Run all baselines under an identical, documented protocol.** Use the DeepCore library to re-run every baseline with the same optimizer, learning rate schedule, batch size, weight decay, number of epochs, and random seeds as used for GradSimCore. Report all hyperparameters. This is the single most important change.
2. **Report the full-dataset (100%) accuracy** for each dataset and architecture as an upper-bound reference.
3. **Quantify the selection procedure's computational cost** (wall-clock time for gradient computation + NN search) and compare it against the training time saved on the coreset.
4. **Describe the scoring formula and radius selection criterion in prose**, so the method is self-contained even without the equations.
5. **Add standard deviations** to the accuracy tables to enable statistical comparison.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>