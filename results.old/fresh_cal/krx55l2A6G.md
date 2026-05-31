Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper studies client-side detectability of malicious server (MS) attacks in federated learning. It first introduces D-SNR, a detection metric that exposes prior example disaggregation attacks as gradient-space detectable, and argues that all prior MS attacks are detectable via principled checks. The paper then proposes **Tool**, a novel attack framework that uses a jointly-trained secret decoder to disaggregate images in a hidden space unknown to clients, evading gradient-space detection while avoiding handcrafted weight modifications. Experimental results show Tool recovers images from batches as large as 512 on CIFAR10/100 and ImageNet with high PSNR, and also reports results under secure aggregation.

## Strengths

1. **Principled detection metric for example disaggregation**: The paper introduces D-SNR (Eq. 1, Section 3) and demonstrates experimentally that successful example disaggregation attacks produce D-SNR values orders of magnitude above natural networks (Figure 1, red markers), while failing attacks produce normal D-SNR but cannot reconstruct data. This provides concrete, quantitative evidence for the claim that prior MS attacks are gradient-space detectable.

2. **Novel attack evading gradient-space detection**: The proposed Tool framework uses a secret decoder trained with SGD (Section 4.1, Eq. 2, Algorithm 1) to disaggregate gradients in a hidden space. Figure 1 (green markers) shows that Tool-trained networks have D-SNR values indistinguishable from natural networks while still reconstructing data — directly supporting the claim that it is harder to detect than prior attacks by the specific metric the paper establishes.

3. **Strong empirical results for large batches**: Tables 1–2 report high reconstruction success (up to 98.6% Rec on CIFAR10 with B=512, and 82.1% Rec on ImageNet with B=64). These results demonstrate the attack's effectiveness on realistic convolutional networks at batch sizes far beyond what honest attacks can handle, even without relying on side information like BN statistics or labels (Section 5).

4. **Local property substantially improves over global baseline**: Section 4.1 identifies that BN intertwines computational graphs, enabling local (in-batch) property thresholds that achieve P(|I_rec|=1) > 0.9 for batches up to 512 — a significant improvement over the 1/e bound of prior global approaches. This insight is leveraged to train the decoder effectively.

## Weaknesses

### Fatal

None.

### Major

1. **Unexplained discrepancy in secure aggregation results (Section 5, Table 2)**: The paper states that for secure aggregation, the combined local/global property yields P(|I_rec|=1)→1/e (line 170), yet reports Rec > 90% in those experiments (lines 271–273). Since Rec measures the fraction of batches where reconstruction PSNR > 19, and successful reconstruction requires |I_rec| to be small (ideally 1), Rec should be bounded above by P(|I_rec|=1). The offered explanations — "the model learning a restricted version of single-client reconstruction for each client" and "better estimation of the property threshold for larger batches" — are vague and do not clearly resolve why Rec can exceed the 1/e bound by such a large margin (~90% vs ~37%). This is a significant inconsistency that either undermines the theoretical claim or needs a much more detailed justification. The comparison on line 271 ("significantly higher than 1/e % of prior work") is also misleading if Tool's own theoretical bound is the same 1/e.

### Minor

1. **Detectability evaluation is limited to D-SNR (Section 3, 4)**: The paper's claim that Tool is "by design harder to detect" is well-supported for D-SNR-based gradient-space detection and weight-space inspection. However, the evaluation does not consider other potential detection methods a client could deploy (e.g., distributional tests on gradient statistics, checking for low-rank gradient structure consistent with a linear projection, or training a binary classifier on gradients from Tool vs. benign models). The paper's claim is comparative to prior attacks and specifically about avoiding prior detection pitfalls, but a broader detectability analysis would strengthen the contribution.

2. **ImageNet comparison to prior work is qualitatively stated without direct comparison table**: The paper states that ImageNet PSNR values are "higher than the state-of-the-art attack in Fishing" (line 264) but provides no direct head-to-head comparison table under identical conditions. A main-table comparison with at least one representative prior MS attack on reconstruction metrics (PSNR, Rec, success rate) under the same setup would strengthen the empirical claims.

### Trivial

- The statement that "D-SNR is always ∞ for attacks proposed by Fishing" (line 102) is left without a brief explanation; a short justification would improve readability.
- The paper excludes BN/gamma parameters from D-SNR computation (line 96) without justification — worth a brief note since a client could compute the metric over all parameters.

## Nice-to-Haves

- **Analysis of secret linear map detectability**: The paper notes the secret linear map is "not detectable in the gradient space" because it is linear and the gradient is aggregated, but a brief analysis of whether the gradient's low-rank structure could reveal the map would address a plausible concern.
- **Ablation on joint training necessity**: The paper could clarify whether the decoder can be trained with a fixed pretrained model or if joint training of f, d, and r is essential. This would strengthen understanding of the method.
- **Hyperparameter sensitivity for α**: The loss weight α (Eq. 5) is not discussed in the main text; reporting its effect on the L_rec vs. L_nul tradeoff would be helpful.
- **False-positive rate of D-SNR**: The paper notes that natural networks can rarely have high D-SNR (line 105), but does not report false-positive rates for a reasonable D-SNR threshold, which would help calibrate the severity of the vulnerability.

## Removed Points

The following points from the reviewer inputs were evaluated and removed with justification:

- **"Unrealistic assumption in the local property"** (Harsh Critic #1): REMOVED. This criticism misunderstands the paper's mechanism. The paper does not claim the server needs to know the client's batch minimum brightness at attack time. Instead, the decoder *d* is trained on the server's auxiliary data to learn a mapping that, during training, separates gradients of images satisfying P from those that do not. At attack time, the learned *d* generalizes to client batches automatically — the server applies *d* to the aggregated gradient and the trained decoder separates the images without requiring explicit knowledge of the client's batch statistics. This is a standard train-on-auxiliary-data, deploy-on-unseen-data paradigm. The BN insight (line 166) explains why the local property is learnable: BN intertwines computational graphs, making the property implicitly accessible through gradient structure.

- **"D-SNR excludes BN parameters without justification"**: REMOVED. The paper explicitly states D-SNR is computed over linear layers because these are where gradient disaggregation manifests. This is a design choice with reasonable justification for the metric's purpose.

- **"98% handcrafted weights claim assumes attacker doesn't try to hide"**: REMOVED. The paper addresses this directly (line 81): "further attempts to conceal the changes (e.g., by adding weight noise) would additionally worsen the results."

- **"Conflating training-time and attack-time knowledge"**: REMOVED. The paper's training procedure is standard — train on auxiliary data (where the server knows the property values) and deploy on client data (where the trained decoder generalizes). No conflation occurs.

- **"Tables referenced but not visible"**: REMOVED. Parser artifact; tables exist in the original submission.

- **"Secure aggregation explanation in appendix"**: REMOVED. Deferring details to the appendix is standard practice.

- **"Missing related works"**: REMOVED per instructions (cannot verify external sources).

- **Generic strengths from Strength Finder (e.g., "this paper addresses an important problem")**: REMOVED. These are generic/superficial and not specific evidence-based observations.

## Novel Insights

The harsh critic's identification of the secure aggregation inconsistency (Rec > 90% vs P(|I_rec|=1)→1/e) is the most significant novel observation across both reviews. Neither reviewer fully explored the implications: if Rec truly exceeds 1/e in the secure aggregation setting, the paper needs to either (a) demonstrate why the 1/e bound does not apply (e.g., because the "combined local/global" property differs from the global property for which the bound was proven), or (b) acknowledge that Rec and P(|I_rec|=1) measure different things and explain why reconstruction can succeed even when |I_rec|>1. This tension between the theoretical bound and empirical results is the paper's most critical unaddressed issue. Beyond this, no genuinely novel insight emerged beyond the paper's own contributions.

## Suggestions

1. **Resolve the secure aggregation discrepancy**: Provide a clear explanation of why Rec exceeds P(|I_rec|=1). If Rec measures reconstruction quality of any image (including cases where |I_rec|>1 but the decoder still outputs a recognizable image), state this explicitly. If the 1/e bound does not apply to the combined property, explain why. Consider reporting P(|I_rec|=1) empirically alongside Rec for the secure aggregation experiments.

2. **Broaden detectability evaluation**: Add at least one additional detection method (e.g., checking gradient singular value distribution, training a classifier on gradients) to support the claim of being "harder to detect." Report false-positive/true-positive rates for D-SNR at a chosen threshold.

3. **Add a direct comparison table**: Include a main-text table comparing Tool with at least one representative prior MS attack (e.g., Fishing) under identical conditions on reconstruction metrics (PSNR, Rec) and detection metrics (D-SNR).

4. **Clarify the local property mechanism**: A brief sentence clarifying that the decoder is trained on auxiliary data and generalizes at attack time without needing client batch statistics would prevent the misunderstanding seen in the review process.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>