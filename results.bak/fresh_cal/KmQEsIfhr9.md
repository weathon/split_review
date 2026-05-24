Now I have a thorough understanding of the paper and can verify each claim. Let me produce the final consolidated review.

## Summary

This paper studies the detectability of poisoning backdoor attacks against CLIP, finding that backdoor-poisoned samples exhibit unusually sparse local neighborhoods in the learned representation space due to the very low poisoning rates (e.g., 0.01%). It shows that classic density-based outlier detectors (SLOF, DAO, k-dist) identify them with >97% AUC across diverse triggers and architectures, whereas existing supervised-learning backdoor detection methods (ABL, CD, SafeCLIP) often fail. The method is efficient enough to process the 3.3M-image CC3M dataset in 15 minutes on 4 A100s. The paper also reports discovering an unintentional backdoor in CC3M that has been trained into an OpenCLIP model.

## Strengths

1. **Discovery of sparse local neighborhoods as a discriminative characteristic of CLIP backdoor samples** — Figure 1b quantitatively shows that as the poisoning rate decreases, the k-dist for backdoor samples becomes substantially larger than for clean samples, while the clean distribution remains stable. This provides direct empirical evidence that backdoor representations are local outliers, which motivates the detection approach. The probabilistic argument in Section 4.2 (with 0.01% poisoning rate, a backdoor sample's k nearest neighbors are almost certainly clean) provides a clear theoretical rationale.

2. **Empirical demonstration that local outlier detectors outperform existing backdoor detection methods** — Table 1 reports AUC scores across 8 attack types and 2 architectures. SLOF, DAO, and k-dist consistently achieve >97% AUC, whereas ABL, CD, and SafeCLIP often fall below 90%, with CD dropping to 48.68% on clean-label attacks. This directly supports the claim that existing supervised backdoor detectors fail on CLIP while traditional outlier detectors succeed.

3. **Effective defense via outlier filtering with minimal clean performance loss** — Table 2 shows that removing 10% of data flagged by DAO reduces attack success rate to below 1% for 6 out of 8 attack types, while clean zero-shot accuracy on ImageNet remains nearly unchanged (e.g., from 38.1% to 37.6%). Figure 2 shows near-complete separation of DAO score distributions between backdoor and clean samples.

4. **Scalability to million-scale datasets** — The paper states that detection on the full CC3M dataset (3.3M images) can be completed within 15 minutes using 4 Nvidia A100 GPUs, which is 45× faster than CD (11.2 hours) and 16× faster than ABL (4.1 hours), demonstrating practical efficiency for real-world web data cleaning.

5. **Robustness across diverse trigger types and architectures** — Table 1 evaluates 8 attack configurations (Patch, Blend, SIG, Nashville, WaNet, BLTO, multi-trigger single-target, multi-trigger multi-target) and 2 vision encoders (RN50, ViT-B-16). Local outlier methods maintain >97% AUC across nearly all settings, while SafeCLIP's performance varies widely (e.g., 23.12% on Nashville with ViT-B-16 vs. 85.73% on Patch with RN50).

6. **Detection of unintentional backdoors in a real web dataset** — Section 5.3 identifies 798 near-identical birthday-cake images (0.03% of CC3M) that act as a natural backdoor trigger. Trigger recovery from both the authors' model and an OpenCLIP released model yields high attack success rates (92.38% and 98.92% respectively), confirming that unintentional backdoors exist in widely used open-source models.

## Weaknesses

### Fatal
None.

### Major

- **Detection procedure is underspecified in a way that affects reproducibility** — Section 4.3 states: "We randomly sample a batch of data from the dataset and then apply outlier detection methods" (line 133). This is ambiguous: are outlier scores for each point computed using a single random mini-batch as reference set, or using the full dataset's representations (e.g., via k-NN on all training points with approximate search)? The probabilistic motivation in Section 4.2 ("Consider randomly sampling a batch of the data (batch size 1024)") is clearly illustrative, but Section 4.3's repetition of "randomly sample a batch" as part of the actual procedure description creates genuine uncertainty. The 15-minute runtime on 3.3M images and the clean separation in Figure 2 are consistent with full-dataset k-NN (likely with FAISS), but the text describes a different procedure. Since the paper's central practical claim rests on the scalability of a specific detection pipeline, the exact procedure (reference set construction, use of approximate nearest neighbor search, handling of batch boundaries) must be specified for reproducibility.

### Minor

- **Target class for trigger recovery ASR is not stated** — Section 5.3 reports that the recovered trigger achieves ASR of 92.38% and 98.92% "when attached to ImageNet test images in zero-shot classification" (line 191), but never states what the target class is. In a backdoor attack, ASR is defined relative to a specific target output (e.g., classification as "birthday cake"). The context (birthday cake images, caption "the birthday cake with candles in the form of number icon") strongly implies the target, but the ASR numbers are technically uninterpretable without an explicit statement. This is a missing detail that weakens an otherwise intriguing finding.

- **Distance metric used in representation space is not specified** — The paper defines SLOF, LID, and DAO using k-dist (distance to k-th nearest neighbor) but never states whether the distance metric is Euclidean, cosine, or some other measure in the CLIP representation space. The definitions of these outlier metrics depend on the choice of distance metric.

- **Adaptive attacks designed to evade sparsity-based detection are not evaluated** — The paper evaluates detection against known, off-the-shelf triggers, but does not test attacks specifically designed to circumvent outlier detection (e.g., blending attacks that push backdoor representations toward the clean cluster, or attacks using multiple triggers at higher densities to fill the sparse region). The paper evaluates up to 10% poisoning rate, which partially addresses one dimension, but an adversary aware of the defense could potentially adapt. This limits the strength of the "systematic study" framing.

### Trivial
- Figure 1b reportedly shows poisoning rates only up to a limited range (the critic suggests 0.1%), but the paper claims detection works up to 10%. While the experimental results in Section 5 confirm that detection indeed works at 10%, the controlled experiment in the characterization section could directly show this range.

## Nice-to-Haves
- A sensitivity analysis for the choice of k in the main text (rather than deferred to the appendix) would strengthen the paper. The text mentions robustness to k but does not summarize key findings.
- The cost of training the initial CLIP model (which the 15-minute detection time excludes) should be acknowledged when positioning the method for practical use.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **"Near-perfect" is an overstatement** — AUC 97–99% is very high and "near-perfect" is a reasonable characterization; this is a stylistic nitpick.
2. **Figure 1b only shows poisoning rates up to 0.1% while claiming up to 10%** — The figure is a controlled experiment illustrating the principle; the full experimental results in Section 5 demonstrate detection at up to 10% poisoning rate. The characterization section and the experimental section serve different purposes.
3. **10% filtering rate is arbitrary** — The paper addresses this with sensitivity analysis in Figure 3a, showing the impact of varying filtering rates. The criticism ignores this analysis.
4. **ABL/CD baselines not fully justified for CLIP** — The paper explicitly acknowledges that these methods were designed for supervised learning and only includes them because they are "state-of-the-art methods that are applicable to CLIP" (line 151). This limitation is transparently stated.
5. **Missing related works** — Per policy, cannot be verified without external sources.
6. **Formatting/style nitpicks** — Parser artifacts, not author errors.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Clarify the detection pipeline** — Specify whether outlier scores are computed using the full dataset as the reference set (with exact or approximate k-NN), or using per-batch sampling, and if the latter, how scores from different batches are aggregated. This is the single most impactful revision for reproducibility.
2. **State the target class for the unintentional backdoor ASR** — Explicitly state what target class is used in the zero-shot evaluation (e.g., "birthday cake" or the specific ImageNet class) and briefly describe how Neural Cleanse was adapted for the CLIP setting.
3. **Specify the distance metric** — State whether Euclidean distance, cosine distance, or another metric is used for computing k-dist in the representation space.
4. **Extend Figure 1b to cover the full poisoning rate range** — Include the higher poisoning rates (1%, 5%, 10%) in the characterization figure to directly support the claim that sparsity persists at higher rates.

## Score and Decision

The paper makes a clearly supported and practically useful contribution: it identifies a fundamental weakness of CLIP backdoor attacks (sparse local neighborhoods) and demonstrates that simple density-based detectors can exploit it with high accuracy and efficiency. The experimental evaluation is thorough across diverse triggers, architectures, and poisoning rates. The discovery of an unintentional backdoor in CC3M is a provocative and valuable finding.

The main weaknesses are: (1) an ambiguous description of the detection procedure that undermines reproducibility, (2) a missing detail in the trigger recovery experiment, and (3) the unspecified distance metric. None of these are fatal — they are all addressable in revision. The core claim about sparsity and detectability is well-supported.
 
MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>