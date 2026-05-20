## Summary

This paper tackles input-level black-box backdoor detection, where the defender only has access to input images and the model's prediction labels. The authors propose CaBBD (Causality-based Black-Box Backdoor Detection), which adds progressively stronger Gaussian noise to each input, records the noise level (Flip Position Score, FPS) at which the model's prediction changes, and classifies samples as clean or backdoored based on whether the FPS falls inside or outside a threshold interval. The method is motivated by a causal-graph analysis (Section 2.3, Figure 2) arguing that clean, sample-agnostic-backdoor, and sample-specific-backdoor images exhibit distinct flip behaviors under noise. Experiments on CIFAR-10, GTSRB, and ImageNet-subset against six attacks show competitive detection performance.

## Strengths

- **Practical problem setting with minimal assumptions.** The method operates using only input images and prediction labels (no model weights, no gradients, no softmax probabilities, no validation set). This is one of the most restrictive and practically relevant threat models for a downstream user of a third-party model, and CaBBD directly targets it.

- **Simple, interpretable detection score.** The FPS — the first noise-magnitude index at which the prediction flips — is both easy to compute and easy to understand. The ablations (Table 2) show that noise-based counterfactual generation outperforms alternatives (mixup, random masking), and the experiments in Figures 5 and 7 demonstrate stable performance across varying poisoning ratios (5%–20%) and trigger sizes (1%–10% of image area), which speaks to robustness.

- **Reasonable experimental breadth.** The paper evaluates six attack types (BadNet, Blend, Label-Clean, Dynamic, WaNet, ISSBA) spanning both sample-agnostic and sample-specific categories, over three datasets, and on both standard (AUC) and per-class (precision, recall) metrics. The inclusion of hard sample-specific attacks (WaNet, ISSBA) is non-trivial — many detectors fail on these.

- **Efficiency awareness.** The comparison in Figure 6 shows CaBBD ranks second fastest among the compared methods, which is relevant given the user-end deployment scenario.

## Weaknesses

### Fatal
None.

### Major

1. **The causal framing is motivational, not operational, yet it is presented as a core contribution.**  
   The paper claims "a novel causality-based perspective" and "Counterfactual Backdoor Detection Algorithm" as top-level contributions (Section 1), and the title itself is "Causality-Based Black-Box Backdoor Detection." However, the causal graphs in Figure 2 are used only as a post-hoc narrative to explain *why* noise-based detection might work. The actual detection algorithm performs no formal causal inference — no do-calculus, no intervention on a structural causal model, no counterfactual defined via the causal graph. The "counterfactual samples" are simply Gaussian-noise-corrupted inputs; there is no causal mechanism linking the noise to the variables (I, S, B, T, A, Y) in the graph. The paper itself acknowledges (lines 86–87) that "the black-box nature of DNNs and the limited available information in our setting render this direct causal analysis challenging," but then still front-loads the causal framing as a primary contribution. Removing the entire causal discussion would not change the algorithm. This overselling weakens the paper's credibility, especially when compared to works like MCCI (ho4mNiwr2n, avg 6.5) that actually derive a causal intervention (backdoor adjustment) and implement it operationally.

2. **Threshold selection is not adequately explained, which undercuts the practical claim.**  
   The detection rule requires a threshold range [α, β] to separate "clean" (FPS in middle) from "backdoor" (FPS at extremes). The paper says "the design of the magnitude set and threshold range are given in the experimental section" (line 131), but the visible portion of the paper does not specify how α and β are chosen, whether they are tuned on a labeled validation set (which would violate the problem setting's access restrictions), or whether they are set via an unsupervised heuristic such as percentiles. Since the baselines are evaluated with their own tuned thresholds (Table 1 footnotes indicate they use validation sets or probabilities), this gap makes it unclear whether CaBBD's reported performance reflects a genuine advantage or an asymmetric evaluation. The problem statement (Section 2.2) stipulates "no prior information regarding the backdoor attacks or the model" — the threshold mechanism must be compatible with this constraint.

3. **No statistical significance or variance estimates.**  
   All reported metrics (precision, recall, AUC) are point estimates with no confidence intervals, standard deviations, or replication across seeds reported in the main tables. Given the noise-based nature of the method — and the fact that FPS depends on a single noise realization per magnitude — scores may be sensitive to randomness. The absence of variance reporting makes it impossible to assess whether the differences between CaBBD and baselines are meaningful.

### Minor

4. **The "SOTA Performance" claim in the contributions list is not fully supported by the evidence.**  
   The paper's own text describes results as "promising" (line 165), which is more measured, but the contribution list states "SOTA Performance in Effectiveness and Efficiency." In Table 1, CaBBD's performance is competitive but not uniformly dominant: e.g., STRIP (which uses more information) achieves equal or higher AUC on several CIFAR-10 and GTSRB settings, and Scale-UP (same setting) outperforms CaBBD on some GTSRB rows. The main advantage is clearer on sample-specific attacks (WaNet, ISSBA), but the blanket "SOTA" claim overstates the evidence.

5. **No comparison against a trivial "single noise level" baseline.**  
   The simplest version of the method — add one fixed noise level and check whether the prediction flips — is never tested. The ablation in Table 2 compares noise against mixup and random masking as counterfactual generation strategies, but does not ablate the multi-level progressive design versus a single-level check. Such a baseline would isolate the contribution of the FPS formulation.

6. **The "trivial overhead" characterization of efficiency (line 188) is imprecise.**  
   Figure 6 suggests CaBBD adds measurable latency beyond vanilla inference. Calling a multi-query detection procedure (requiring ~10 or more forward passes per image) "trivial overhead" — especially in the abstract which mentions "not significantly increase the inference time" — is an overstatement. The method is clearly more expensive than the 1-pass baseline, even if it is faster than some alternatives.

### Trivial
None.

## Nice-to-Haves
- Discussion of how thresholds could be set without labeled data (e.g., via distribution percentiles on a large unlabeled query stream, or via a meta-learning approach).
- Adaptive attack analysis: what happens if the attacker knows the defender adds Gaussian noise and designs triggers to evade FPS-based detection (e.g., triggers that degrade gracefully under noise)?
- A failure analysis showing concrete examples where CaBBD misclassifies clean or backdoor samples.

## Removed Points

These points were flagged by reviewers but are removed or weakened after verification against the paper:

1. **"Causal framework is decorative, not operational (Structural)"** — *Kept and reframed as a Major weakness above, but softened from "decorative" to "motivational, not operational."* The causal analysis does provide useful intuition for the noise-based approach; the problem is overselling, not absence of value.

2. **"Method requires a labeled validation set to set thresholds, contradicting the problem setting"** — *Kept as Major weakness #2 above.* The concern is valid, though the paper could potentially use unsupervised percentiles. The criticism is about *lack of explanation*, not a proven contradiction.

3. **"Method is essentially a noise-sensitivity heuristic, and SOTA is not demonstrated"** — *Partially kept as Minor weakness #4.* The "noise-sensitivity heuristic" framing is fair but not a fatal flaw — many good detection methods are simple heuristics. The core issue is overclaiming SOTA status.

4. **"No confidence intervals"** — *Kept as Major weakness #3.*

5. **"The paper has not compared against a single fixed noise level baseline"** — *Kept as Minor weakness #5.*

6. **"Efficiency claim is misleading"** — *Weakened to Minor weakness #6.* Calling it "trivial overhead" is imprecise, but the method is genuinely the second-fastest among those compared.

7. **"The causal graphs are presented as a model of DNN behavior, but the DNN architecture and training are completely ignored"** — *Removed.* This is scope creep: causal graphs at this level of abstraction are not meant to model architecture details; they model information flow.

8. **"Missing related works"** — *Removed per instructions.* Cannot verify what related works exist externally.

9. **"Formatting/style nitpicks"** — *Removed per instructions.* These are parser artifacts, not author errors.

10. **"No comparison against a simple noise-only baseline" (from Harsh Critic's missing experiments)** — *Kept as Minor #5.*

11. **"STRIP achieves similar AUC with less information"** — *Removed.* The paper clearly states STRIP *requires more information* (prediction probabilities), not less. STRIP using probabilities while CaBBD uses only labels makes comparable performance *favorable* to CaBBD, not unfavorable. Additionally, the harsh critic's specific claim about GTSRB BadNet AUC (0.87 vs Scale-UP 0.93) cannot be fully verified from the available text since the table is an image.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Rebalance the claims.** Either (a) dial down the "causality-based" framing by presenting the causal graphs as intuitive motivation rather than a core technical contribution, or (b) actually ground the counterfactual generation in formal causal inference (e.g., an SCM that maps noise to the graph variables). The paper would be stronger as a practical, well-motivated heuristic than as an overclaimed causal method.

2. **Clearly specify threshold selection.** Describe exactly how α and β are set for each dataset — whether via a held-out set, an unsupervised percentile rule, or cross-validation — and discuss whether this is compatible with the stated problem constraints. If a heuristic is used, show its sensitivity (e.g., precision/recall as a function of percentile choice).

3. **Add variance estimates.** Run all main experiments over at least 3–5 random noise seeds and report mean ± std for AUC, precision, and recall. This is especially important for a noise-based method where the FPS is a function of a single noise sample.

4. **Include a single-noise-level baseline.** Compare the multi-level FPS against a simpler rule: add one moderate noise level, check if prediction flips, and classify accordingly. This would isolate the value of the multi-level progressive design.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uw5U7FfTRf.md` (BaDLoss) | 3.0 | Weaker paper: unclear method, many missing details, threshold tuning unresolved. Current paper is clearer and better organized. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6Nnni5GtK3.md` (Prompting the Unseen) | 4.33 | Similar level, but that paper has inconsistencies between text and tables. Current paper is cleaner in presentation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NI0RsRuFsW.md` (Evasive Trojans) | 4.0 | Weaker: small datasets, incremental contribution, limited evaluation. Current paper has more practical scope and better breadth. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KmQEsIfhr9.md` (Detecting Backdoor CLIP) | 6.0 | Comparable quality. Both have simple effective ideas and reasonable evaluations. The CLIP paper has an interesting discovery (unintentional backdoors) that raises its value. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1OfAO2mes1.md` (Backdoor Secrets Unveiled) | 6.0 | Comparable. Both improve on simple baselines but have limited novelty. The current paper's threshold uncertainty is a bigger weakness. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ho4mNiwr2n.md` (MCCI) | 6.5 | Stronger paper: the causal connection (backdoor adjustment via do-calculus) is actually operationalized, not just motivational. MCCI's framing is more rigorous. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/s56xikpD92.md` (BaDExpert) | 6.25 | Stronger: more comprehensive evaluation across more attacks and architectures, though it uses a less restrictive threat model (needs model access for finetuning). |

The paper addresses a well-motivated problem with a simple, practical method and reasonable experimental breadth. However, it is held back by: (1) an oversold causal framing that is not operationalized, (2) underspecified threshold selection critical to deployment, and (3) lack of variance estimates. The method itself has merit — FPS-based noise sensitivity is intuitive and works reasonably well — but the contributions as stated overreach.

MY FINAL SCORE: 5.0
MY FINAL DECISION: Reject