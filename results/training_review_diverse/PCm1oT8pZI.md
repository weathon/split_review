Now I have a thorough understanding of the paper and can construct the final review. Let me build it systematically.

## Summary
This paper proposes a DNN watermarking method that uses a single out-of-distribution (OoD) image — augmented into diverse patches — as a secret trigger set, and employs adversarial weight perturbation during fine-tuning to resist removal attacks. The key advantage is that no original training data (i.i.d. data) is needed for watermark injection or verification.

## Strengths
1. **Data-free backdoor injection demonstrated convincingly.** The method successfully injects persistent watermarks without using any in-distribution training data. Table 1 shows OoDWSR of 95.66% on CIFAR-10 (trojan_wm) and 87.61% on CIFAR-100, with standard accuracy degradation under 3%, confirming that a single OoD image suffices.

2. **Empirical robustness across three attack types.** The watermarks survive fine-tuning (FT-AL, FT-LL, RT-AL), pruning (20%–50%), and model extraction across all datasets. For CIFAR-10 trojan_wm, OoDWSR remains above 96% after FT-AL and pruning-50%. For CIFAR-10 and GTSRB, OoDWSR stays ≥ 90% after model extraction (Table 3).

3. **Weight perturbation clearly improves robustness.** Table 4 (tab:wp) shows that after RT-AL on CIFAR-10, OoDWSR for trojan_wm rises from 19.94% (w/o WP) to 57.52% (w/ WP), while standard accuracy is nearly unchanged.

4. **Direct comparison showing OoD injection outlasts i.i.d. poisoning.** Table 2 directly compares OoD-based injection against conventional i.i.d.-based backdoor injection under RT-AL. ID poison's WSR drops to ~4% while OoD poison maintains 24%–57%, demonstrating the inherent robustness benefit of OoD triggers.

5. **Practical efficiency.** The method requires only one OoD image and fine-tunes for 20–30 epochs, making it feasible for real-world deployment scenarios (e.g., federated learning server, third-party IP protection).

6. **Ablation on OoD image quality.** Table 5 (tab:ood_image) shows that dense images (City, Animals) achieve ≥94% OoDWSR while a sparse image (Bridge) yields ~71%, providing practical guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **Verification logic conflates "different" with "stolen copy."** The paper uses both OoDWSR and a T-test for verification. The T-test's null hypothesis is that the suspect model's logits distribution is identical to a non-watermarked model's. Rejecting this null means the suspect model is *different* from a non-watermarked model — not that it is a *copy* of the watermarked model. A model with a completely different architecture or trained on a different dataset would also yield low p-values. The paper does not establish a false-positive rate (e.g., how often an independently trained model of a different architecture would be flagged) or compare against a baseline distribution of p-values for unrelated models. While the OoDWSR criterion (WSR > random guess and far above non-watermarked baseline) partially mitigates this — since an unrelated model would likely have low OoDWSR on the secret trigger set — the paper should explicitly test this scenario and report the combined decision rule's specificity.

2. **Robustness evaluation covers a narrow attack space.** The paper evaluates removal attacks under a single adversary setting: 10% of training data, 50 fine-tuning/pruning epochs. This is a reasonable baseline, but the paper does not explore stronger or adaptive adversaries who could (a) use more i.i.d. data (e.g., 50%–100%), (b) fine-tune for more epochs, (c) apply the same OoD image (or similar OoD images) during fine-tuning, or (d) use larger pruning ratios. Without exploring the attacker's design space, the robustness claims — while valid for the tested regime — are preliminary and could be overstated. The paper should bound where the watermark breaks rather than only showing where it works.

### Minor

3. **No experimental comparison against li2022knowledge (data-free watermarking).** The paper mentions li2022knowledge (data-free distillation-based watermarking) in related work as "time-consuming" but provides no experimental comparison. Since li2022knowledge is also data-free (no training data needed), a direct comparison on the same datasets/models/attacks would substantiate the claimed efficiency and robustness advantages over the most directly comparable baseline. The omission weakens the novelty claims about filling the "gap" of data-free backdoor-based IP protection.

4. **Lack of analysis of the OoD image key space.** The paper states the OoD image is "publicly available" but "only known to the model owner." The augmentation recipe provides some secrecy, but the paper provides no analysis of the effective key space (how many possible images × augmentation configurations) or whether an adversary who suspects watermarking could feasibly enumerate and fine-tune against candidate images. This is a practical security concern for the "safe" framing.

### Trivial

5. **Trigger selection via top-2 OoDWSR from 6 patterns.** The paper selects the best-performing triggers based on OoDWSR on the same evaluation setup, which risks overfitting to the evaluation conditions. Reporting results for all 6 patterns or pre-specifying triggers would be cleaner.

6. **Qualitative distribution analysis.** Figure 4 visualizes OoD/ID sample distributions qualitatively. Quantitative metrics (e.g., Wasserstein distance, distribution overlap before/after injection) would strengthen the analysis.

## Nice-to-Haves
- Report wall-clock time or relative training cost of the weight perturbation optimization compared to standard fine-tuning without WP.
- Test whether a statistical test (e.g., Kolmogorov-Smirnov on weight distributions) can detect the watermark after injection, to substantiate the claim that the model is "safe" (undetectable).
- Compare against standard sharpness-aware minimization (SAM) as an alternative robustification strategy, since the weight perturbation approach is conceptually related.

## Removed Points
- **"No comparison with zhang2018protecting and wang2022free":** These methods still require i.i.d. training data to maintain utility, so a head-to-head comparison would test different settings. The paper's core claim is operating *without* training data, making a direct comparison against methods that need it not apples-to-apples. The critic's demand for this comparison evaluates the paper against the wrong class of expectations.
- **"Weight perturbation is conceptually similar to SAM":** The paper already cites he2023sharpness and acknowledges the connection. This is an observation, not a weakness.
- **"Model extraction results show large accuracy drops, weakening the threat scenario":** The paper's claim is about watermark *persistence under attack*, not about the extracted model being a perfect copy. Reporting honest results is a strength, not a weakness. The critic misunderstands the paper's focus.
- **"The T-test alone is insufficient for verification":** While the critic's point about the T-test's null hypothesis is valid and kept above, the paper does NOT rely solely on the T-test. It uses OoDWSR as the primary criterion (line 142: "if the WSR is larger than a random guess, and also far exceeds the probability of a non-watermarked model... then Ms will be considered as a copy") and the T-test as a supplementary metric. The criticism in its original form overstates the paper's reliance on the T-test alone.

## Novel Insights
The harsh critic's most valuable insight is the verification logic problem — that rejecting the T-test's null hypothesis establishes that two models are *different*, not that one is a *copy*. This is a subtle but important distinction that many watermarking papers overlook. The paper partially addresses this through the OoDWSR criterion but does not fully resolve the concern. The critic's point about exploring adaptive attacks (particularly fine-tuning on the same OoD image) is also useful and not obvious from the paper's current evaluation design.

## Suggestions
1. Add a false-positive analysis: compare p-values and OoDWSR for watermarked models vs. independently trained models (different architectures, different datasets) to establish the combined decision rule's specificity.
2. Compare experimentally against li2022knowledge's data-free watermarking approach on the same datasets, models, and attacks to substantiate efficiency/robustness claims.
3. Expand the attack evaluation to include stronger adversaries (50%–100% fine-tuning data, longer training, fine-tuning on OoD-like images) to bound where the watermark breaks.
4. Analyze the OoD image key space and discuss how the augmentation recipe provides security against an attacker who knows the general approach.

## Score and Decision
The paper proposes a genuinely novel and practical approach — single-image OoD watermarking with adversarial weight perturbation — that addresses a real gap in data-free DNN protection. The core experimental evidence (Tables 1–4) convincingly demonstrates the method works and that weight perturbation helps. The verification logic gap and the narrow attack space are notable concerns but do not invalidate the central contribution. The missing comparison against li2022knowledge is the most significant omission.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>