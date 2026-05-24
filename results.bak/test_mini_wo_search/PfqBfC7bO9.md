Now I have all the information needed to verify reviewer claims against the actual paper. Let me synthesize the final consolidated review.

---

## Summary

This paper proposes CAUSE, a framework for unsupervised semantic segmentation that constructs a discretized "concept clusterbook" via modularity maximization (serving as a mediator in a causal model), then performs concept-wise contrastive learning using distances in that clusterbook to define positive/negative pairs. The method achieves state-of-the-art results across COCO-Stuff (41.9 mIoU), Cityscapes (28.0 mIoU), and Pascal VOC (47.5 mIoU), substantially outperforming prior work like STEGO and HP. The paper also includes thorough ablations on clustering methods, hyperparameters, concept bank, and backbone generalization.

---

## Strengths

1. **Substantial and consistent SOTA improvements across multiple benchmarks.** On COCO-Stuff, CAUSE-TR achieves 41.9 mIoU vs. 28.3 (STEGO) and 30.9 (HP) — large, convincing margins. Similar gains hold on Cityscapes and Pascal VOC. The categorical analysis (Fig. 5a, log-scale IoU per category) shows the method particularly improves "thing" categories that prior methods struggle with, directly supporting the claim that it addresses the granularity-targeting problem. This is not incremental progress; the gains are striking for an unsupervised method.

2. **Well-designed ablation study isolating each design component.** Table 3 systematically compares modularity maximization against K-Means++, Spectral Clustering, Agglomerative Clustering, and Ward-Hierarchical Clustering, showing clear (though moderate) advantages for modularity. The ablation also teases apart the contributions of the concept bank and CRF. This goes beyond what most USS papers provide and allows readers to assess each component's contribution.

3. **Generalization across backbones and label granularities.** Table 1(c) shows CAUSE works with DINOv2, iBOT, MSN, and MAE encoders, not just DINO. The COCO-81/COCO-171 results (Table extending beyond main table) demonstrate the method scales to larger category sets without modification beyond relaxation parameters.

4. **Novel technical combination for USS.** The idea of building an overcomplete vocabulary (k=2048 >> number of semantic classes) via modularity maximization, then using distances within that vocabulary to drive contrastive learning, is a genuinely new technical approach to the USS problem — distinct from prior work that relies on simpler clustering or direct feature correspondence.

---

## Weaknesses

### Major

1. **The causal framing (frontdoor adjustment) is asserted, not established, and the paper's central claims rely on it being more than a narrative device.** The paper claims the conditions for frontdoor adjustment are satisfied — specifically that mediator \(M\) is "independent with the unobserved confounder \(U\)" (line 73). But the paper never demonstrates this independence formally. \(U\) is defined as "indetermination during clustering (what and how to cluster)," yet the construction of \(M\) via modularity maximization with a chosen \(k=2048\) and optimizer involves precisely the kind of algorithmic choices that could be seen as part of that indetermination. The causal diagram (Fig. 2) omits a discussion of whether the clustering procedure itself introduces confounding. The footnote 1 (line 35) and footnote 3 (line 138) contain the paper's argument for the causal reasoning, but these are heuristic analogies and approximations (sharpening the assignment, assuming uniform \(p(t')\)), not a rigorous SCM. This does *not* invalidate the method — the method may work well independently of whether the causal justification is complete — but it means the paper's advertised contribution ("integrating causal inference into USS") is overstated. A reader who cares about the causal claim will find it unsupported; a reader who ignores the causal framing will still find an empirically strong method.

2. **The empirical results do not test whether the causal perspective itself contributes anything beyond the specific technical recipe.** The paper never compares "CAUSE with the causal motivation" against "the same two-step algorithm described without invoking causality." Since the claim to novelty centers on bridging causal inference into USS, the experiments should isolate whether the causal framing changes any design decisions or hyperparameters. Currently, the causal language motivates the two-step design post-hoc, but the method would be equally publishable if described as a modular two-stage pipeline (overcomplete clustering → distance-thresholded contrastive learning) without the frontdoor terminology. This is a framing issue: the paper claims more than its evidence supports.

### Minor

3. **The claim that the clusterbook represents concepts "at different levels of granularity" (abstract, lines 33, 73) is imprecise.** The clusterbook is a single fixed-size (\(k=2048\)) partition of the patch-feature space via modularity maximization. It does not have a hierarchical or multi-scale structure that explicitly encodes granularity. What the paper likely means is that because \(k \gg\) the number of target semantic classes, some prototypes correspond to fine parts and others to whole objects — which is a reasonable interpretation — but the phrase "different levels of granularity" suggests a multi-resolution structure that the method does not provide. This is a presentation overclaim rather than a technical flaw.

4. **No error bars or variance estimates are reported.** Given the stochastic elements (clusterbook initialization, batch sampling, modularity optimization), single-run results leave uncertainty about the stability of the claimed improvements. The margins over baselines are large enough that noise is unlikely to flip rankings, but the absence of variance reporting is a gap in experimental rigor.

5. **The modularity maximization algorithm (Algorithm 1) omits important implementation details.** The algorithm uses \(\tanh(\mathcal{C}\mathcal{C}^T/\tau)\) in the trace expression (line 93) — a non-standard formulation — but does not explain how the soft assignment is reconciled with the eventual discretization, how batch size interacts with the \(hw \times hw\) affinity matrix, or how image resolution affects memory. The paper mentions "only one epoch with Adam," but the actual optimization dynamics for an NP-hard problem are nontrivial. The paper is reproducible in principle given the equations, but the lack of detail will make implementation difficult for others.

### Trivial

None.

---

## Nice-to-Haves

- A runtime/memory complexity analysis, since the affinity matrix \(\mathcal{A} \in \mathbb{R}^{hw \times hw}\) scales quadratically with patch count.
- A discussion of how the concept bank size (\(k \times b \times r = 2048 \times 100 \times 90\)) was chosen and its memory footprint.
- Clarification on how relaxation thresholds \(\phi^+,\phi^-\) were selected (the ablation shows sensitivity, but no search strategy is described).

---

## Removed Points

These points were raised by reviewers but either misread the paper, are factually incorrect, or are speculations about missing appendices/information the parser stripped.

- **"The causal diagram should have an edge U→M"**: The paper's causal model asserts that \(M\) is a function of \(T\) only (via modularity maximization with fixed \(k\) and algorithm). Whether a clustering *algorithm choice* counts as part of the "indetermination" \(U\) is a modeling assumption, not an omission. The paper is transparent about its assumption; a reviewer disagreeing with the assumption is a different critique. Since the paper states the assumption explicitly (line 73: "directly relying on \(T\) while being independent with the unobserved confounder \(U\)"), this criticism is a modeling debate rather than an error.
- **"Frontdoor derivation in footnote 3 not rigorous"**: The paper explicitly calls this an "approximation" and "simplification" (footnote 3), using sharpening and uniform \(p(t')\) assumptions. The critic demands more rigor than the paper claims to provide. This is scope creep; the causal framing is used as motivation/analogy, not as a formal theorem.
- **"Missing comparison to baselines"** broadly construed: The paper actually includes extensive baselines (STEGO, HP, TransFGU, ReCo+, HSG) and ablates clustering methods. The "missing" comparison is specifically a version of CAUSE *without* the causal story — which is a fair but high bar (what would a "non-causal version" even look like given the method is literally the two-step design the causal story produced?).
- **"Not yet released / cannot be independently verified" style claims**: Removed per hard rule (all cited models, benchmarks, and datasets are assumed to exist).
- **Missing related work, missing appendix content, formatting nitpicks**: All removed per hard rules.
- **Strength Finder generic strengths**: Removed generic praise ("important problem," "well-addressed question") that lacked specific evidence or conflicted with verified weaknesses. Kept only strengths that are concrete, evidence-grounded, and specific to this paper.

---

## Novel Insights

Both reviewers recognized the same core tension: the paper has genuinely strong empirical results and an interesting technical design (modularity-based overcomplete vocabulary + distance-thresholded contrastive learning), but the causal framing is invoked at the level of analogy rather than rigorous structural causal modeling. This creates a mismatch between how the paper sells itself ("bridging causal inference into USS") and what it actually demonstrates (a well-engineered two-stage pipeline that works very well). The more interesting observation is that the method's actual novelty — using modularity maximization to build an overcomplete mediator vocabulary, then using distances within that vocabulary to define contrastive positives/negatives — stands on its own as a contribution. The paper could be strengthened by either (a) substantially formalizing the SCM and testing its assumptions, or (b) reframing the contribution around the concrete technical design while keeping the causal motivation as intuition.

---

## Suggestions

- **Reframe the contribution.** Consider presenting the method as "a two-stage USS pipeline: (1) overcomplete discretization via modularity maximization, (2) vocabulary-distance-thresholded contrastive learning" with the causal perspective as motivating intuition rather than a claimed theoretical contribution. This would eliminate the mismatch between claims and evidence.
- **Add variance estimates** (at least 3 seeds) to the main results table.
- **Add implementation details for Algorithm 1**: specify how soft assignments are binarized, how the affinity matrix is feasibly computed for high-resolution images, and provide the exact optimizer configuration.
- **Tone down the "different levels of granularity" language** or clarify that the clusterbook is a single flat partition with \(k\) much larger than the number of target classes, so that different prototypes naturally capture finer/coarser patterns.

---

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>