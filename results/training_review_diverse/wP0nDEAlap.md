Now I have all the verification I need. Let me write the final consolidated review.

---

## Summary

This paper proposes RKIQT, a no-reference IQA framework that learns comparative reference knowledge via knowledge distillation from a non-aligned reference teacher (MCD module) and injects complementary inductive biases from CNN and INN teachers (Inductive Bias Regularization). The student model requires no reference images at inference time, yet achieves state-of-the-art results on eight IQA datasets and competitive performance against some FR-IQA methods. The core technical novelty lies in the Masked Quality-Contrastive Distillation approach, which avoids direct imitation of teacher features and instead reconstructs them from partially masked student features.

## Strengths

- **Novel integration of reference-knowledge distillation into NR-IQA**: The paper makes the first attempt to transfer HQ-LQ comparison knowledge from a non-aligned reference teacher into an NR-IQA student that requires no reference at inference. This is demonstrated by outperforming several full-reference methods (LPIPS, DISTS) on synthetic datasets (Table 2) while using no reference images during inference, validating the core thesis that comparative awareness can be learned under the NR-IQA setting.

- **Masked Quality-Contrastive Distillation (MCD) is an effective and well-motivated design**: The MCD formulation addresses the misalignment between the student's LQ-only features and the teacher's HQ-LQ difference features through random masking and reconstruction, rather than direct feature imitation. Ablation in Table 4 shows MCD significantly improves over direct feature distillation (DRD) on both synthetic (KADID) and authentic (LIVEC, KonIQ) datasets, confirming the design's validity.

- **Inductive Bias Regularization with complementary teachers is shown to benefit ViT-based IQA**: The use of both a CNN teacher (spatial-agnostic, channel-specific) and an INN teacher (spatial-specific, channel-agnostic) to inject diverse inductive biases is grounded in a known limitation of ViT (lack of built-in inductive biases). Table 6 confirms performance drops when either teacher is removed, and Figure 3 demonstrates reduced overfitting. The reverse distillation strategy with a learnable intermediate layer further improves knowledge transfer (Table 7).

- **Strong empirical results**: RKIQT achieves best or second-best SRCC/PLCC on all eight datasets (Table 1) and demonstrates strong cross-dataset generalization (Table 3), outperforming comparison methods on five of six cross-dataset scenarios.

## Weaknesses

### Fatal

None.

### Major

- **The NAR-teacher is pre-trained on KADID for all target datasets, giving the student an unacknowledged information advantage over baselines.** The paper states (Sec. 4.2) that the NAR-teacher is "pre-trained exclusively on the synthetic KADID dataset" and then used to distill knowledge into the student on *every* target dataset, including authentic ones like LIVEC and KonIQ. Standard NR-IQA baselines in Table 1 are trained only on the target dataset's training split and do not receive additional supervision from a teacher pre-trained on an extra dataset. This means the experimental setup conflates the benefit of the proposed distillation method with the injection of additional data knowledge (especially on synthetic datasets like LIVE, CSIQ, TID2013 that share distortion types with KADID). The paper does not acknowledge this discrepancy, does not control for it (e.g., by also training the teacher on only the target dataset's training split, or by providing baselines with KADID pre-training), and does not discuss the likely effect. This is the most significant weakness in the paper.

- **Baseline numbers in Table 1 are likely quoted from literature under different train/test splits, making the comparison not rigorouly fair.** The paper reports results for competitor methods without stating they were re-implemented under the same protocol. RKIQT uses its own 80/20 random split repeated 10 times, but different splits, preprocessing, and cross-validation protocols can significantly alter SRCC/PLCC numbers, especially on small datasets like LIVE (29 reference scenes). Without running at least the top-performing baselines under an identical evaluation protocol, the claimed improvements over prior work are not rigorously demonstrated.

### Minor

- **No standard deviations or confidence intervals reported despite 10-run protocol.** The paper averages over 10 random splits (Sec. 4.2) but reports only point estimates in all main tables (Tables 1, 2, 3, 4, 5, 6, 7, 8, 9). Reporting standard deviations would allow readers to assess whether observed differences between methods or ablation conditions are meaningful.

- **The ablation study does not isolate the student architecture's contribution from the distillation framework.** The baseline condition "w/o MCD w/o Regularization" in Table 4 apparently still includes the student's three-token + decoder architecture. A naïve ViT-S with a standard regression head is never evaluated, making it unclear how much of the final performance comes from the stronger student backbone versus the distillation losses themselves.

- **Training cost and inference efficiency are not reported.** For a paper whose headline is "Less is More" (implying efficiency), the absence of GPU-hours, total parameter count across teachers + student, FLOPs, or inference throughput is a notable omission. The full pipeline requires a pre-trained NAR-teacher (Inception-ResNet-V2 + ViT), CNN and INN teachers (EfficientNet-b0, RedNet101), and a student ViT-S with decoder. Quantifying the computational footprint would help readers assess the practical trade-offs.

- **Design rationale for the reverse distillation's intermediate layer aggregation is not explained.** The paper selects features from three intermediate layers of the CNN/INN teachers and aggregates them via addition (Eq. 2), but provides no motivation for which layers are chosen or why additive aggregation is appropriate.

### Trivial

- The paper notes that inductive bias regularization has "a more pronounced impact on the KADID dataset" (Sec. 4.5) but does not speculate on why. The most natural explanation (the NAR-teacher is also trained on KADID) is not discussed — this is worth clarifying.

- Figure 1 caption states RKIQT "exceeds some IQA methods that do require reference images" without specifying that this is only on synthetic datasets and only for LPIPS and DISTS (Table 2), not across all FR-IQA methods or all datasets. The claim is accurate as stated but could be misread.

## Nice-to-Haves

- Running a control experiment where the NAR-teacher is trained only on the target dataset's training split (without KADID) for a subset of datasets would substantially strengthen the evidence that the distillation framework itself — rather than the extra KADID knowledge — drives the performance gains.

- Re-implementing the top-2 or top-3 competing NR-IQA methods under the same 80/10/10 split (or similar) protocol would eliminate the split-mismatch concern for the most critical comparisons.

- Ablating the student architecture by replacing the three-token + decoder design with a standard ViT-S regression head (while keeping distillation losses) would help isolate architectural contributions.

- Adding a comparison of inference speed (images/sec) between RKIQT and lightweight NR-IQA methods would support the "less is more" framing more concretely.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Less is more" framing inconsistency (Harsh Critic #3)**: The critic argues the title's "less is more" is inconsistent with the training cost. However, the paper explicitly states "eliminating the need for reference images **during inference**" — the claim is about inference input, not training cost. This is a strawman weakness that misreads the paper's own scoping. **Removed (strawman).**

- **MCD compared only to DRD (Harsh Critic, Sec. 3.2 note)**: The critic faults MCD for not being compared against other feature-alignment techniques (contrastive distillation, attention transfer). DRD is the natural and most direct baseline for evaluating whether MCD's masking strategy helps. Demanding comparisons against unrelated distillation methods is scope creep. **Removed (nice-to-have at most).**

- **Generic formatting/style nitpicks**: Any complaints about parser artifacts, missing whitespace, or minor presentation issues are parser errors, not author errors. **Removed per hard rules.**

## Novel Insights

The most interesting observation from the reviews is the structural tension in the experimental design: the method's key claim (transferring reference knowledge to NR-IQA) inherently requires a teacher that has seen reference images, but the teacher's pre-training on a separate dataset (KADID) creates an information asymmetry with baselines that is difficult to fully control. This tension is a general challenge for distillation-based methods in IQA — the very mechanism that enables knowledge transfer also introduces an uncontrolled variable. The paper would benefit from explicitly identifying this tension and designing experiments to disentangle the effect of the distillation framework from the effect of the teacher's pre-training data.

## Suggestions

1. **Address the KADID pre-training concern directly.** The simplest fix is to re-train the NAR-teacher on each target dataset's own training split (without KADID) for 2–3 representative datasets (e.g., LIVE, LIVEC, KonIQ) and show that RKIQT still outperforms NR-IQA baselines. If the margins hold, the concern is resolved.

2. **Re-implement at least the top-3 competing NR-IQA methods** under the same 80/20 split and evaluation protocol used for RKIQT, and report the comparison in a revised Table 1. This removes the split-mismatch concern.

3. **Add standard deviations** to all result tables given the 10-run protocol, and add a brief discussion of whether observed differences are within noise levels.

4. **Report training cost (GPU-hours, parameter count) and inference speed** for the full pipeline and for the student alone. Quantify the "less" in "Less is More" concretely.

## Score and Decision

The paper addresses a well-motivated problem (transferring comparative quality knowledge to the NR-IQA setting) and proposes a technically sound framework (MCD + Inductive Bias Regularization) with supporting ablations. However, the experimental validation has two significant uncontrolled variables: (1) the NAR-teacher's KADID pre-training gives the student an information advantage that is not accounted for in comparisons with NR-IQA baselines, and (2) baseline numbers are likely sourced from literature under different splits rather than re-implemented. These issues do not invalidate the core technical contribution but substantially weaken the empirical claims of state-of-the-art performance. The paper could be made publishable by addressing these concerns through controlled experiments.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>