Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the consolidated review.

## Summary

This paper proposes NCL-SR, which it claims is the first Non-Contrastive Learning (NCL) framework for Sequential Recommendation (SR). The framework uses a differential privacy-inspired augmentation to generate positive user profile pairs, then trains with matrix cross-entropy-based uniformity and alignment losses without negative samples. Empirical results on six datasets show strong improvements over both ID-based and text-based baselines.

## Strengths

- **First NCL framework for SR, filling a clear gap.** The paper correctly identifies that existing NCL methods have been applied to CV and NLP but not to recommendation. Building an NCL framework for SR — where data sparsity makes representation collapse a real concern — is a genuine and timely contribution.

- **Strong and consistent empirical results.** Table 1 shows an average improvement of 11.93% over the best baseline across six datasets, and Table 2 shows 12.48% improvement over five CL-based SR methods using the same E5 text backbone. The gains are particularly pronounced on sparse datasets (33.2% Recall@10 on Sports), which aligns with the paper's motivation that NCL helps in sparse settings.

- **Ablation study isolates the contribution of each component.** Table 3 shows that removing the alignment loss drops Recall@10 by 6.10% on average, removing uniformity drops it by 4.00%, and replacing either the DP augmentation or the NCL loss degrades performance. This provides meaningful evidence that each design choice contributes.

- **Computational complexity analysis of the augmentation.** The paper notes that a naive user-level DP augmentation would cost O(k^l), and proposes an item-level variant reducing this to O(k·l). This practical engineering consideration is useful.

## Weaknesses

### Major

1. **The differential privacy guarantee is not correctly established.** This undermines a central claim. Three distinct issues:

   (a) **Theorem 1's premise is not satisfied.** The theorem requires the recommendation mechanism M to be ε-DP. The paper claims (line 109) that post-processing makes the recommender DP ("if the augmentation operation is DP, then recommendation process based on the augmented user profile is also DP"). This is incorrect — post-processing applies to a *specific output* of a DP mechanism; it does *not* make a separately trained model (which was not trained with DP-SGD) ε-DP. The recommender M does not satisfy the theorem's condition.

   (b) **The implementation replaces random sampling with a deterministic expectation.** The exponential mechanism's DP guarantee comes from randomized sampling. The paper instead computes a deterministic weighted sum (Equation 8), which is a function of the raw data, not a randomized mechanism output. The "expected output stability property" invoked to justify this (line 109) is not a standard DP property and is not referenced to any source — it appears to be the authors' invention.

   (c) **The margin condition is unverified.** Even setting aside the above issues, the theorem requires a strong margin condition (score for correct item > e^{2ε} × runner-up score). The paper provides no evidence that this holds for real recommender outputs, and for typical softmax-based models with many items it is unlikely to hold for most users.

   **Impact:** Without a correct theoretical guarantee, the augmentation method reduces to a heuristic synonym-based perturbation weighted by cosine similarity. The paper's claimed differentiator — "provable" preference preservation — is not supported. A major revision is needed to either fix the theoretical argument or honestly reframe the contribution.

2. **Computational efficiency is claimed as a motivation but never measured.** The paper repeatedly motivates NCL by the "high computational costs" of negative sampling in CL, yet provides zero wall-clock time, GPU memory, or FLOPs comparisons. The proposed augmentation itself adds overhead (synonym retrieval, exponential mechanism scoring over k·l candidates per user). Without quantitative evidence, the efficiency argument remains rhetorical and the paper's main motivation is unsubstantiated.

3. **No error bars or statistical significance.** All results are reported from what appears to be a single run. Given the non-standard 2:2:6 train/validation/test split (only 20% of data for training), results may be highly variable. The ablation study finds small differences (4–6%) that could fall within noise without variance estimates. This is a serious concern for a paper making strong improvement claims (33.2% on Sports).

### Minor

4. **Key implementation details are missing, impeding reproducibility.** The paper does not report the synonym dictionary size k, the privacy parameter ε used in the exponential mechanism, the number of items perturbed (only says "3 items" — which is useful), or the hyperparameters for the recommended task loss L_task. These are needed to reproduce the results.

5. **No comparison to "no augmentation" baseline.** The ablation replaces the DP augmentation with random augmentations from CL baselines, but does not include a baseline that uses no augmentation at all (i.e., only L_task). This would clarify whether the NCL losses themselves add value beyond the text backbone.

6. **No comparison to simple NCL baselines adapted to SR.** Since the paper claims to be the first NCL framework for SR, a natural baseline would be adapting BYOL or SimSiam to recommendation (e.g., feeding the same user profile twice through an asymmetric network). This would disentangle the effect of the augmentation from the NCL loss architecture and would strengthen the claim of novelty.

7. **The preference-preservation definition uses top-1, but optimization is over rankings.** Definition 1 defines preference preservation in terms of the top-1 predicted item. However, the model is trained to rank all items, and evaluation uses Recall/NDCG@N. The gap between the theoretical definition and practical optimization is not addressed.

### Trivial

- The paper refers to "expected output stability property of DP" without citation — this appears to be a non-standard concept the authors introduce but do not formally define or prove.

## Nice-to-Haves

- Measure alignment and uniformity directly using the metrics from Wang & Isola (2020) to complement the downstream performance results.
- Provide theoretical analysis or diagnostics for potential collapse in the alignment loss (negative trace term).
- Isolate the contribution of the E5 text backbone by including a version with a weaker text encoder or comparing ID-based NCL-SR variants.

## Removed Points

These points were flagged by the reviewers but are removed or downgraded for the following reasons:

- **Strength about "provable DP guarantee":** Removed because it conflicts with the verified weakness that the DP guarantee is not correctly established.
- **Criticism about contribution not being isolated from E5 backbone:** Partially valid but the paper does compare CL baselines using the same E5 backbone (Table 2), so the NCL advantage over CL is fairly isolated. The point is kept as a minor note but the severity is downgraded.
- **Criticism about the alignment loss potentially causing collapse:** While theoretically reasonable, this is speculative without experimental evidence. Moved to Nice-to-Haves as a diagnostic suggestion.

## Novel Insights

The most interesting observation from the reviews is the structural gap between the paper's two main claims. The NCL framework itself (first NCL for SR) is a genuine contribution with strong empirical support. But the paper tries to pair it with a "provable" DP-based augmentation that does not actually deliver the promised guarantee. The empirical success of the method despite the flawed theory suggests either (a) the augmentation works well as a heuristic for reasons unrelated to DP, or (b) there is a different, correct theoretical story to be told about why the weighted cosine-similarity substitution is effective. Neither the paper nor the reviewers resolve this, but it points toward a more honest and potentially stronger paper if the authors drop the "provably" language and analyze why their heuristic augmentation works.

## Suggestions

1. **Either fix the DP claim or drop it.** If the theoretical guarantee is kept, the recommender must be trained with DP-SGD and the augmentation must actually sample from the exponential mechanism rather than computing a deterministic expectation. If not, reframe the paper to present the augmentation as a principled heuristic inspired by DP, remove "provably" language, and compare directly against heuristic augmentations (e.g., CoSeRec's substitution).

2. **Report wall-clock time and GPU memory** for NCL-SR vs. the best contrastive baselines under the same batch size and hardware. Without this, the computational motivation for the entire framework is unsubstantiated.

3. **Run experiments with at least 3–5 random seeds** and report mean and standard deviation. This is especially important given the small training set (20% split). Without this, the reported improvements cannot be evaluated for statistical significance.

4. **Disclose the missing implementation details:** synonym dictionary size k, ε value used in the exponential mechanism, and key hyperparameters for the task loss.

## Score and Decision

**Originality:** Good — first NCL framework for SR is novel. The DP-based augmentation is creative even if the theoretical guarantee is flawed.

**Importance of research question:** High — reducing computational costs of contrastive methods in SR is a well-motivated problem.

**Claims support:** Weak — the central theoretical claim (provable preference preservation) is not correctly established, and the computational efficiency claim has no supporting evidence.

**Soundness of experiments:** Moderate — the empirical results are strong but lack statistical reliability (no error bars) and key baselines are missing (no-augmentation, simple NCL baselines).

**Clarity of writing:** Fair — the method description is generally clear, but the DP theoretical argument contains incorrect reasoning.

**Value to community:** Moderate — if the theoretical issues are addressed (or honestly reframed), the NCL framework and the strong empirical results would be useful to the SR community. In its current form, the overclaimed guarantees undermine credibility.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>