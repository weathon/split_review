Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes One-Step Anti-Noise (OSA), a method for mitigating noisy labels during training by leveraging a pre-trained multimodal model (e.g., CLIP) as a fixed estimator. The core idea is that high-dimensional orthogonality and the cone effect create a stable cosine-similarity boundary separating clean and noisy pairs. OSA computes cosine similarity through the estimator, applies spatial debiasing (subtracting the mean random-pair similarity β), then uses a scoring function to assign a weight to each sample's loss—near-zero for noisy samples, positive for clean. The method is tested on image-text matching (MS-COCO, Flickr30K, CC120K), image classification (WebFG-496 subsets), and image retrieval (CARS98N), showing consistent improvements over strong baselines with very low computational overhead (21 min extra vs. 226 min for NPC).

## Strengths

- **Strong and consistent empirical results across tasks, architectures, and noise levels.** OSA improves CLIP by 8.6% R@1 (i2t) and 7.0% R@1 (t2i) on MS-COCO 5K at 50% noise (Table I), and achieves 20.9%/22.3% R@1 gains on Flickr30K at 60% noise (Table II). The gains persist across image classification (+7.7% on Aircraft), image retrieval (+6.8% mAP), and on real-world noisy data (CC120K). The method also works on ResNet-152, VGG-19, and ViT backbones (Tables I, VI).

- **Exceptionally low computational overhead.** OSA adds only 21 minutes (22% overhead) over plain CLIP training (97 min), whereas NPC adds 226 min (233% overhead). The paper also estimates the cost for 1B samples (~75 hours on one RTX 3090), demonstrating practicality for large-scale training.

- **Near-optimal noise ranking.** The mean noise rank analysis (Table IV) shows OSA ranks noisy samples at 1809.1 (vs. optimal 1815.5) at 20% noise and 1520.7 (vs. optimal 1524.0) at 50% noise—within 0.5% of the theoretical optimum—directly validating the boundary's precision.

- **Zero-shot estimator works without domain adaptation.** Ablations (Table VII) show zero-shot CLIP performs comparably to domain-adapted CLIP as an estimator, simplifying deployment.

- **Orthogonal geometric intuition is well-motivated.** The observation that clean/noisy cosine-similarity distributions (Figure 1) intersect at approximately the mean of random-pair cosines is visually striking and novel. The link to high-dimensional orthogonality and the cone effect provides a clean, intuitive explanation for why this boundary exists.

## Weaknesses

### Fatal
None.

### Major

1. **The scoring function as presented does not match the described behavior.** The function (Eq. 8) defines w = -(s-β)²(s-β-1) for t = s-β > 0. This simplifies to w = t²(1-t), which peaks at t=2/3 with a maximum value of 4/27 ≈ 0.148, then **decreases** to zero at t=1. The paper states w ∈ [0, 1] (Section 3.2: "cleanliness score w_i, (0 ≤ w_i ≤ 1)") and describes a function where "the gradient should increase rapidly as the cosine similarity moves further from zero" (Section 2.3). Neither claim holds for the equation shown: the maximum weight is ≈0.148 (not 1), and for t > 2/3 the weight decreases with increasing similarity—contradicting the monotonic behavior described. This is a significant discrepancy in the paper's central formula. The authors must clarify whether this is a typographical error and, if so, state the correct function used in experiments. If the function shown was actually used, the method's strong results would survive because the relative ordering (clean > noisy) is still approximately preserved over the feasible range (t ∈ (0, 0.8] given β ≈ 0.2), but the description is misleading.

2. **The theoretical proof (Theorem 1) relies on random-weight assumptions that do not match the deployed estimator.** Theorem 1 explicitly assumes a neural network with random weight matrices and biases (elements ~ N(0,1/d_out)), then claims that "the relative relationship of pairs... will not change after transmitting to the narrow cone space of the trained model" (Section 2.2). The estimator used in practice (CLIP, ALIGN) is a heavily trained model, not a random network. The paper provides no argument bridging this gap. The empirical evidence (Figures 1a–d, Table I) convincingly demonstrates that the boundary exists in practice, so this weakness undermines the theoretical framing but not the practical contribution. The theorem should be reframed as intuitive motivation rather than a formal proof for the deployed setting.

3. **Limited analysis of the spatial debiasing step.** The method computes β as the mean cosine of K random pairs (Eq. 7), but no sensitivity analysis is provided for K (how many pairs are sufficient?), the stability of the estimate across random seeds, or how the choice of β affects the precision-recall trade-off in noise detection. A ROC-style analysis showing the relationship between β and false-positive/false-negative rates would strengthen the method.

### Minor

- **Overstated novelty claims in the conclusion.** The paper states: "this is the first work to explore anti-noise in practical large-scale training scenarios, as well as the first to propose a general anti-noise approach." Re-weighting based on an external signal has been explored in various forms (e.g., MentorNet, self-training, confidence-based filtering), and many prior methods (NPC, Co-teaching, DivideMix) are also "general" across tasks. The paper's specific contribution—using pre-trained multimodal cosine-similarity with orthogonal-boundary debiasing—is novel enough without these sweeping claims.

- **Scope is narrower than the introduction suggests.** The introduction frames this as a solution to the general noisy-label problem, but the method fundamentally requires a multimodal pre-trained model with a shared embedding space (converting labels to text for classification). This is a powerful but specific setting; the paper could be more precise about where the method applies and where it does not.

### Trivial

- None beyond issues already addressed above.

## Nice-to-Haves

- A sensitivity analysis for the number of random pairs K used in spatial debiasing (Eq. 7).
- A visualization (ROC curve or precision-recall curve) showing how the threshold β (or the scoring function's shape) affects the noise-detection trade-off.
- If the scoring function in Eq. 8 is a typo, the corrected closed-form expression with a plot over the relevant range (from β to 1) would eliminate ambiguity.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Cannot verify the appendix proof."** The harsh critic questioned the proof of Theorem 1 because the appendix is omitted. Per the rules, the appendix exists in the original submission and was stripped by the parser. This concern is removed.
- **"Reproducibility concerns about missing hyperparameters/implementation details."** The harsh critic mentioned undisclosed details. These are standard nitpicks that do not threaten the paper's claims and are removed per rules.
- **"Missing related works."** Per the rules, I cannot verify claims of missing citations, so this is not included as a weakness.
- **Several of the Strength Finder's generic strengths** were filtered (e.g., "this paper addressed an important problem") as they lack specific citations or concrete content.

## Novel Insights

The intersection between the harsh critic's detailed mathematical scrutiny and the paper's actual content reveals an interesting tension: the scoring function w = t²(1-t) is objectively not what the paper describes it to be (max weight 0.148, non-monotonic for very clean samples), yet the experimental results are strong enough that the method clearly works despite this flaw. This suggests the key to OSA's success is likely the binary-like separation achieved by the debiasing (w=0 for t≤0, w>0 for t>0) combined with the near-perfect recall (≥97%), rather than the precise shape of the scoring function for clean samples. The "scoring function" may be far less important than the spatial debiasing step and the high-quality estimator—a nuance the paper does not explore. Conversely, the theoretical gap (random-weight theorem applied to trained models) is a genuine weakness in the framing, but the strong empirical validation across diverse settings more than compensates. The paper would be stronger if it honestly acknowledged the theorem as geometric intuition backed by empirical observation rather than a formal proof.

## Suggestions

1. **Fix or clarify the scoring function.** Either correct Eq. 8 to match what was actually used in experiments (e.g., a function that increases monotonically to 1, such as a sigmoid or a polynomial that stays in [0,1]), or if Eq. 8 is correct, explicitly acknowledge that max weight is ~0.148 and explain why this does not harm training (e.g., via learning rate compensation, loss scaling, or because relative ordering is all that matters).

2. **Reframe Theorem 1 as geometric motivation, not a formal proof for trained models.** The theorem's random-weight premise is transparently different from the trained CLIP estimator. A simple statement that "the theorem provides intuition for why the boundary is preserved; empirically, Figures 1a–d verify it holds for trained models" would be honest and sufficient.

3. **Add a brief sensitivity study for the spatial debiasing parameter K** (e.g., how does β stabilize as K grows from 10 to 10,000?).

4. **Tone down the novelty claim in the conclusion** from "first to propose a general anti-noise approach" to something more measured, e.g., "first to exploit high-dimensional orthogonality and the cone effect for general noise mitigation."

## Score and Decision

Based on my assessment: the paper presents a simple, well-validated, and efficient method for noise mitigation that works across multiple tasks, architectures, and noise levels. The two major weaknesses (scoring function mismatch and theory-practice gap) are real but do not invalidate the core contribution, which is empirically substantiated. The scoring function issue is fixable (either a correction or an acknowledgment + explanation), and the theoretical framing can be adjusted. The paper makes a solid practical contribution.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>