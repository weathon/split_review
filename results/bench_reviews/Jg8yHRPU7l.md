## Summary
The paper studies why neural networks trained on datasets with random label noise often learn clean-label structure early and fit corrupted labels later. It proposes a sample-wise/segment-gradient mechanism: within each ground-truth class, corrupted-label gradients point opposite to clean-label gradients; because clean samples are the majority, noisy gradients are initially cancelled, so early GD allegedly follows the clean-label GD direction, with this dominance disappearing near early stopping.

## Strengths
- The paper gives a concrete gradient-level lens on clean-priority learning rather than only restating the empirical observation. In Section 2 it defines sample-wise gradients and segment gradients, and in Section 3–4 uses these quantities to analyze clean/noisy segments.
- The empirical diagnostics are more mechanistic than standard train/test-error plots. Figures 4–8 examine gradient-angle distributions, clean/noisy segment errors, residual magnitudes, and clean/noisy segment-gradient norm ratios.
- The qualitative story in Section 4.2 is plausible and useful: clean residuals shrink while corrupted-label residuals grow, reducing the initial clean-gradient dominance. Figure 6 directly tracks the ratio of clean/noisy segment-gradient norms and relates its decline to the early stopping point.
- The paper attempts to connect binary theory to multi-class experiments, including MNIST/CIFAR-style settings with CNN/ResNet models in Figures 7–8. Even though the theory is not convincing, the attempt to examine internal quantities beyond final accuracy is valuable.

## Weaknesses

### Fatal
- The central “noisy-label GD equals clean-label GD” result is not valid as written. The paper’s main theoretical chain is Assumption 4.1 → Eq. (7) → Lemma 4.2 → Theorems 4.4/4.5. However, Eq. (7) does not follow from Assumption 4.1. Assumption 4.1 states that the **corrupted-label noisy segment gradient** satisfies  
  \[
  g_{\text{noise}}^{(c)}(w_t)=-\alpha_t g_{\text{clean}}^{(c)}(w_t).
  \]
  But Eq. (7) then treats the clean segment gradient as a fixed fraction of the **ground-truth-labeled** class gradient \(\hat g^{(c)}\). This requires relating the corrupted-label gradient of noisy samples to their ground-truth-label gradient. For binary cross-entropy, if a true label \(1\) is corrupted to \(0\), the corrupted-label gradient is \(f\nabla h\), whereas the ground-truth-label gradient is \((f-1)\nabla h=-(1-f)\nabla h\). These are opposite in direction but not equal in magnitude except at \(f=1/2\). The paper itself acknowledges that during training the residual factor \(f(w;x)-y\) changes in magnitude (lines 169–171, 226–227), so this mismatch is not a minor technicality. Consequently, Lemma 4.2’s claim that GD on \(\mathcal D\) follows GD on \(\hat{\mathcal D}\) with only a rescaled learning rate is not established, and this undermines the paper’s core theoretical contribution.

### Major
- Assumption 4.1 effectively assumes the crucial cancellation mechanism rather than deriving it. The paper motivates it by saying that in infinite width \(\nabla h(w_t)=\nabla h(w_0)\) and hence sample-wise gradient directions remain unchanged (lines 163–171). But fixed tangent features do not imply that sums over clean and noisy subsets remain exactly collinear and opposite as residual magnitudes evolve differently across samples. The assumption is much stronger than the NTK/fixed-feature property and is precisely the relation needed to prove the clean-gradient dominance story.
- The initialization magnitude argument in Eq. (5) is not justified. The paper writes
  \[
  g_k^{(c)}(w_0)=|D_k^{(c)}|\mathbb E[\nabla l]
  =|D_k^{(c)}|\mathbb E[f(w_0;x)-y]\mathbb E[\nabla h],
  \]
  but the factorization \(\mathbb E[(f-y)\nabla h]=\mathbb E[f-y]\mathbb E[\nabla h]\) is not generally valid because \(f(w_0;x)\) and \(\nabla h(w_0;x)\) are coupled through the same network and input. The paper also moves from population-level similarity of clean/noisy subsets to finite-dataset segment-gradient cancellation without concentration bounds.
- The multi-class extension is only heuristic. Section 5 treats a softmax classifier as “\(C\) co-existing binary classifiers” and analyzes single-logit gradients (lines 250–264). This is a useful diagnostic, but the full softmax cross-entropy gradient couples logits through the normalization and through shared hidden parameters. Showing a binary-like relation for one logit component does not establish that the full parameter gradient on the corrupted-label dataset aligns with the clean-label gradient.
- The experiments are suggestive but do not directly test the decisive theoretical claim. The paper should directly measure quantities such as \(\cos(\nabla L(w_t;\mathcal D),\nabla L(w_t;\hat{\mathcal D}))\), \(\|\nabla L(w_t;\mathcal D)-\lambda_t\nabla L(w_t;\hat{\mathcal D})\|\), and class-wise segment-gradient concentration over training. Figures 4–8 support parts of the proposed story, but they do not validate the claimed clean-label GD equivalence.

### Minor
- The mini-batch SGD discussion in Remark 4.3 is underdeveloped. Having a clean majority in a batch does not by itself ensure the class-wise clean/noisy segment-gradient cancellation relation; one would need batch-level concentration conditions.
- The connection between the disappearance of clean-gradient dominance and the exact early stopping point is mostly empirical. Figure 6 is interesting, but the paper does not systematically show across seeds, noise realizations, widths, datasets, and noise rates that the norm-ratio crossing predicts the test-error minimum rather than merely coinciding in selected runs.
- The paper would benefit from clearer separation between exact theoretical claims and approximate empirical observations. Many equations are written as exact identities even though the surrounding discussion only supports approximate geometric tendencies.

### Trivial
None.

## Nice-to-Haves
- Width-scaling experiments would be valuable because the theory is framed around infinite-width networks and fixed tangent features.
- Controlled synthetic experiments varying within-class clustering or NTK-feature separability would clarify when the proposed cancellation mechanism should succeed or fail.
- Reporting variance across seeds, class pairs, and noise realizations would make the empirical claims more convincing.
- Per-class plots of segment-gradient angles and norm ratios would help determine whether the aggregate trends hide class-specific failures.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Generic “important problem” strength** — Removed as a main strength because importance alone is generic. The paper’s relevant strength is the specific segment-gradient diagnostic approach, not merely that noisy-label early stopping is important.
- **Strength Finder claim that Lemma 4.2 directly supports the paper’s main explanation** — Removed because Lemma 4.2 is precisely where the main theoretical error occurs; the equivalence to clean-label GD is not established.
- **Strength Finder claim that the multi-class extension supports the mechanism** — Weakened/removed as a strength because Section 5’s logit-wise analysis does not establish a full-gradient softmax result. The multi-class experiments remain useful diagnostics, but the theoretical extension is not a solid contribution.
- **Pure presentation/formatting issues** — Removed because PDF extraction artifacts and minor style issues should not affect evaluation.
- **Missing appendix/proof-related complaints** — Removed by rule; the extracted text may omit appendix material. The retained criticisms concern equations and reasoning present in the main text, not absent appendices.
- **Demands for broad new settings such as sample-dependent noise or many additional architectures as core flaws** — Removed/weakened as scope creep. Such experiments would be useful but are not necessary if the paper’s stated binary/multi-class random-noise mechanism were theoretically sound.

## Novel Insights
The most important synthesized observation is that the paper’s qualitative mechanism may be directionally correct while its exact mathematical claim fails because “opposite direction” and “negative equal-magnitude gradient” are conflated. In cross-entropy, corrupted labels reverse the sign of the residual but also change its magnitude as training progresses; this is exactly the quantity the paper later uses to explain diminishing dominance. Thus the paper’s own later-stage mechanism exposes why the clean-label GD equivalence cannot hold exactly without additional error terms or a more careful residual-dynamics analysis.

## Suggestions
- Replace Lemma 4.2 with an approximate statement that explicitly accounts for the residual-magnitude mismatch between corrupted-label and ground-truth-label gradients.
- Reformulate Assumption 4.1 as a quantified approximation with an error term, e.g. \(\|g_{\text{noise}}^{(c)}+\alpha_t g_{\text{clean}}^{(c)}\|\le \epsilon_t\|g_{\text{clean}}^{(c)}\|\), and analyze how \(\epsilon_t\) affects the update direction.
- Prove or empirically quantify finite-sample concentration of segment gradients under explicit class-conditional feature assumptions.
- For multi-class classification, analyze the full softmax gradient, including all logit components and shared parameters, rather than relying on single-logit analogies.
- Add direct measurements of noisy-label vs. clean-label full-gradient alignment throughout training.
- Calibrate claims in the abstract/conclusion: the current evidence supports an interesting gradient-geometric hypothesis, not a proof that noisy samples have “minimal to no impact” in general.

## Calibration and Score Rationale

### Retrieved calibration anchors
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TroV1cbgoG.md` — Avg 5.33, Reject. Similar topic: theoretical label-noise training dynamics with clean/noisy stages; stronger than this paper because reviewers found the main theoretical results generally plausible, with concerns more about setting and novelty.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/PPazOk82Sq.md` — Avg 5.60, Reject. Similar label-noise/GD theory; despite restrictive settings and rigor concerns, it appears to contain a more substantial technical theorem than the present paper’s invalid central equivalence.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WH9NhxOeu9.md` — Avg 5.00, Reject. NTK/early-stopping theory anchor; comparable broad area but less directly tied to the present paper’s central flaw.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5EtSvYUU0v.md` — Avg 6.00, Reject. Infinite-width/kernel-regime anchor; higher because it appears to make a more coherent theoretical connection, though not necessarily accepted.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/CMzF2aOfqp.md` — Avg 5.75, Accept. Direct noisy-label early stopping anchor; more applied and apparently stronger empirically than the present paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BxHgpC6FNv.md` — Avg 5.67, Accept. Noisy-label theory anchor; likely stronger because it proves behavior in a defined model rather than relying on the disputed cancellation identity.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/x3lE88YkUl.md` — Avg 5.20, Reject. Noisy-label gradient/SAM anchor; similar mid-quality empirical/theoretical framing, but the present paper has a more central theoretical soundness problem.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6PjS5RnxeK.md` — Avg 5.00, Reject. Similar weakness pattern: interesting mechanism but core ansatz/assumption unjustified and experiments suggestive. The present paper is below this because the key algebraic step linking noisy-label GD to clean-label GD appears incorrect, not merely assumed.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7oT1X8xjIk.md` — Avg 5.80, Reject. Similar pattern of restrictive assumptions and oversold claims, but less topically close.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EsjoMaNeVo.md` — Avg 6.00, Reject. Similar overclaim/strong-assumption pattern, but off-topic and apparently technically broader.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zv9jedBExg.md` — Avg 3.75, Reject. Similar mechanism-theory paper where key assumptions are flawed and experiments are only suggestive; this is a close quality anchor for the present paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OEC6zOuZG1.md` — Avg 4.83, Reject. Similar theoretical mechanism with strong assumptions and unclear implications; the present paper is somewhat below due to the central derivation issue.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yCEf1cJDGh.md` — Avg 5.25, Reject. Similar weakness pattern but off-topic; not heavily weighted.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3aZCPl3ZvR.md` — Avg 6.00, Accept. High topical anchor on SAM robustness to label noise; stronger because reviewers found originality/clarity/importance adequate.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/P42DbV2nuV.md` — Avg 7.33, Accept. High early-stopping neural-network anchor; much stronger empirically and practically than this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wfgZc3IMqo.md` — Avg 6.00, Accept. High noisy-label method anchor; stronger empirical/methodological contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/h8GeqOxtd4.md` — Avg 6.25, Accept. High theory/early-stopping/noisy-regression anchor; stronger because reviewers saw rigorous nontrivial analysis despite limitations.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ndRkLsoQ1Q.md` — Avg 3.75, Reject. Low noisy-label anchor; weak due to misleading claims and inconclusive comparisons. The present paper is similarly low, but for theoretical soundness rather than empirical fairness.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/aXSxSu3fvg.md` — Avg 3.00, Reject. Low early-stopping/semi-supervised anchor; weaker empirically than this paper, but useful as a lower bound.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/qDeEsfAb1j.md` — Avg 4.00, Reject. Low noisy-data anchor; comparable in that the core method/claim was seen as weakly motivated.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/z4bfNsrum4.md` — Avg 3.80, Reject. Low corrupted-label/memorization anchor; broadly comparable as a weak explanation of memorization under corruption.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6PGT9OJX5N.md` — Avg 3.00, Reject. Low noisy-label data-pruning anchor; lower because it appears empirically/methodologically thin.

### Score and Decision
Relative to the calibration set, this paper is below the borderline noisy-label theory papers around 5–5.6 because its central theoretical equivalence is not merely restrictive but mathematically unsupported as written. It is closer to the low-scoring “interesting mechanism but flawed core assumptions” anchors around 3.75–4.0. The paper has useful diagnostics and a plausible hypothesis, so it is not at the very bottom, but the main theoretical claim is not sound enough for acceptance.

**Score: 3.5 / 10**  
**Decision: Reject**

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>