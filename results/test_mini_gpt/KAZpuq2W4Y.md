## Summary

The paper proposes HOMIL, a WSI classification method that combines DBSCAN-based patch clustering with first-order attention pooling and a covariance-based second-order representation over cluster features. The method is evaluated on CAMELYON16 and TCGA-NSCLC against several MIL baselines, with reported improvements in ACC/AUC/F1 and substantial runtime reductions relative to many sequence/attention-heavy baselines.

Overall, the paper has a plausible and potentially useful idea, but the central “higher-order moment” framing is not fully aligned with the actual computation, and the empirical evidence does not yet justify the strongest claims of significant state-of-the-art improvement. Originality is moderate, the research question is relevant to computational pathology MIL, the experiments are useful but not definitive, and the writing is generally understandable but overclaims several mechanisms.

## Strengths

- **Concrete and simple architectural idea for efficient WSI MIL.** The method reduces patch bags to cluster features via PCA + DBSCAN and then performs first- and second-order aggregation over the resulting clusters. Section 4.1–4.3 gives a reasonably complete high-level pipeline: patch features from CONCH, PCA to 32 dimensions, DBSCAN clustering, cluster mean features, attention-weighted first-order pooling, covariance-based second-order pooling, and final fusion.

- **Broad baseline comparison under a shared experimental protocol.** Tables 1 and 2 compare HOMIL against Mean/Max pooling, ABMIL, CLAM-SB/MB, TransMIL, S4MIL, MambaMIL, and HMIL on CAMELYON16 and TCGA-NSCLC. Section 5.2 states that all methods use 512-dimensional patch features, patient-level 5-fold splits, and a unified codebase, which supports internal comparability.

- **The method is empirically competitive on the reported benchmarks.** HOMIL obtains the best reported ACC/AUC/F1 in Tables 1 and 2: 96.98/99.23/96.54 on CAMELYON16 and 93.24/97.41/92.93 on TCGA-NSCLC. Even if the margins are small, the method is at least competitive with strong MIL baselines.

- **The efficiency motivation is supported by reported compression and ablation evidence.** Section 5.3 reports compression ratios of 0.18 on CAMELYON16 and 0.16 on TCGA-NSCLC. Table 3 shows that removing clustering increases runtime from 310s to 530s on CAMELYON16 and lowers ACC/AUC/F1, suggesting that clustering contributes to both efficiency and performance in the reported setting.

- **Ablation partially supports the two main components.** Table 3 shows that removing the second-order module decreases CAMELYON16 performance from 96.98 ACC / 99.23 AUC / 96.54 F1 to 95.98 / 98.51 / 94.94, while removing clustering also degrades performance and runtime. This does not fully explain why the design works, but it is useful evidence that the proposed components are not obviously redundant.

## Weaknesses

### Fatal

None.

### Major

- **The “attention-weighted second-order moment” formulation is inconsistent with the actual covariance computation.** Section 4.3.3 says the second-order representation is derived from an “attention-weighted covariance matrix,” but the equation is  
  \[
  \mathbf{C}=\sum_{k=1}^K \tilde{\mathbf{g}}_k\tilde{\mathbf{g}}_k^\top,
  \quad \tilde{\mathbf{g}}_k=\mathbf{g}_k-\mathbf{v}^{(1)}.
  \]  
  The attention weights \(a_k\) are used in the mean \(\mathbf{v}^{(1)}=\sum_k a_k\mathbf{g}_k\), but not in the covariance summation, and there is no normalization by \(K\), by attention mass, or by cluster size. This makes the representation not a standard second central moment of the same attention distribution used for the mean. Since the paper’s core conceptual claim is that HOMIL extends ABMIL from first-order to second-order moment estimation, this mismatch weakens the method’s stated statistical interpretation.

- **The covariance is computed over equally weighted cluster means, not over the original patch distribution, yet the paper often describes it as slide-wide patch covariance.** The abstract says the method computes “the covariance matrix of the patch representation vectors across the entire slide,” while Section 1 later states that “both moments are computed based on cluster representations rather than individual patches.” In Section 4.3.3, the covariance is over \(\mathbf{g}_k\), the mean feature of each cluster. Thus a singleton cluster and a large cluster contribute equally to \(\mathbf{C}\), regardless of the number of patches represented. This could be a deliberate cluster-balanced design, but then the paper should present it as such rather than as a covariance of the WSI patch distribution.

- **The DBSCAN pathology-preservation mechanism is asserted more strongly than demonstrated.** The paper repeatedly claims that DBSCAN forms “large clusters for abundant normal tissues and small clusters for rare pathological regions” (Abstract, Section 2.2, Section 4.2). DBSCAN clusters by density in PCA-reduced feature space, not directly by diagnostic relevance. The paper does not provide cluster visualizations, lesion-overlap analysis on CAMELYON16, cluster-size distributions by tissue/pathology type, or other evidence that rare tumor regions are indeed preserved at finer granularity. The empirical results show clustering can help, but they do not validate the biological/pathological explanation used to motivate the method.

- **The empirical improvements are often small relative to the reported variability, so “significantly improves state-of-the-art performance” is not supported as written.** On CAMELYON16, HOMIL improves over MambaMIL by 0.50 ACC points and over S4MIL by 0.21 AUC points, while reported variability values are larger than these margins. On TCGA-NSCLC, HOMIL improves over HMIL by 0.35 ACC points and 0.10 F1 points. No paired fold-level results, confidence intervals, or statistical tests are reported. The evidence supports “competitive and slightly better under this protocol,” but not a strong claim of significant SOTA improvement.

- **The covariance vectorization module is under-justified.** Section 4.3.3 compresses each row of the \(d \times d\) covariance matrix using row-wise 1-D convolution and max pooling. This imposes locality/order over the coordinates of a learned 512-dimensional feature embedding, but the paper does not justify why adjacent embedding coordinates should have meaningful local structure. It also does not compare this design against simpler alternatives such as diagonal variance, normalized covariance with an MLP, low-rank bilinear pooling, vectorized upper-triangular covariance, or cluster-size-weighted covariance. Since this module is central to the claimed second-order modeling, the lack of focused ablation limits confidence in the design.

### Minor

- **Important clustering implementation details remain somewhat underspecified.** Section 5.2 states \(d'=32\), \(\epsilon\) is the 65th percentile of nearest-neighbor distances, and minPts = 4. However, it is not fully explicit whether PCA is fit per slide, on the training set, or globally; whether \(\epsilon\) is computed per slide or across a dataset; and what nearest-neighbor convention is used. Since clustering is a core component, these details matter for interpretation and reproduction.

- **The CAMELYON16 evaluation protocol should distinguish official split performance from 5-fold cross-validation.** Section 5.1 describes the official 270/129 train/test split, while Section 5.2 uses unified patient-level 5-fold cross-validation. This is internally fine for comparing methods in the paper, but it should be made explicit that these numbers are not directly comparable to results using the official train/test split unless the same protocol is used.

- **The ablation study is useful but narrow.** Table 3 only reports ablations on CAMELYON16 and only removes the clustering module and the second-order module. It does not isolate key design choices raised by the method itself: weighted vs. unweighted covariance, normalized vs. unnormalized covariance, equal-cluster vs. cluster-size weighting, DBSCAN vs. simpler clustering or random compression at matched compression ratio, and Conv1D compression vs. simpler covariance summaries.

- **Claims about spatial correlations are overstated.** Section 3.2 says second-order statistics help with “spatial and feature correlations,” and Section 5.4 says clustering helps with “spatial context preservation.” However, the described method clusters in feature space after PCA and computes covariance over feature dimensions; it does not explicitly use patch coordinates or spatial adjacency. The method may indirectly preserve some spatial/tissue information through feature similarity, but explicit spatial modeling is not demonstrated.

### Trivial

None that should affect evaluation.

## Nice-to-Haves

- Provide visual examples of DBSCAN clusters overlaid on WSIs, especially for CAMELYON16 tumor regions, to verify the adaptive-granularity story.
- Report the distribution of \(K\), compression ratios, and runtime per slide/dataset, not only average compression ratios.
- Add fold-level paired comparisons or confidence intervals for the main results, since the performance gaps are small.
- Add ablations for covariance normalization, attention weighting, cluster-size weighting, and alternative covariance compression methods.
- Reframe the statistical interpretation if the intended method is cluster-balanced aggregation rather than estimating a conventional patch-level second moment.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Runtime unfairness as a major flaw.** The harsh review suggested the runtime comparison may be unclear or unfair. The paper does specify in Section 5.2 that runtime includes clustering for HOMIL and “training+inference only” for other methods. If anything, this inclusion of clustering makes the comparison less favorable to HOMIL, not more favorable. It is still useful to clarify exactly whether PCA fitting and feature loading are included, but this should not be treated as a major weakness.

- **Pure formatting, typo, grammar, or parser-artifact issues.** Any issues involving spacing, captions duplicated by extraction, line breaks, or rendering artifacts are removed under the review instructions.

- **Availability/release concerns for cited models, datasets, baselines, or references.** The paper cites CONCH, HMIL, MambaMIL, and other resources. Per instruction, these are to be treated as existing and available; no criticism should be based on doubting their existence or release status.

- **Missing related-work demands.** The harsh review’s concern that other MIL methods also model interactions is useful as a scope clarification, but I do not include demands for specific additional related works because external related-work omissions cannot be verified here. The retained point is only that the paper should avoid implying that prior MIL methods capture no dependencies at all.

- **“The covariance representation is computationally usable through Conv1D” as a standalone strength.** This is true in a narrow engineering sense, but it conflicts with the verified weakness that the Conv1D compression is under-justified for unordered learned feature dimensions. I therefore do not count it as a main strength.

- **“Fusion weights are interpretable” as a strong strength.** Figure 2(b) shows learned weights for first- vs. second-order branches, but this only indicates the relative branch weights during training. It does not by itself explain pathological decisions or prove that second-order statistics provide structural cues. This is better treated as a descriptive diagnostic than a substantive interpretability strength.

- **Generic importance of WSI classification / computational pathology.** The problem is important, but generic importance alone is not a paper-specific strength and is therefore omitted from the main strengths.

## Novel Insights

The most important synthesis is that the paper may actually be proposing a cluster-balanced representation rather than a conventional higher-order moment estimator. Equal weighting of cluster means, unweighted covariance around an attention-weighted mean, and singleton handling for non-core DBSCAN points could be a coherent strategy for upweighting rare phenotypes after compression. However, that is not the same as estimating the first and second moments of the patch distribution. Recasting the method around “adaptive cluster-balanced first/second-order aggregation” would make the contribution more honest and could turn a current conceptual inconsistency into a deliberate design choice.

## Suggestions

- Correct the mathematical formulation: either use a properly weighted and normalized covariance consistent with the attention distribution, or explicitly state that the method uses an unnormalized cluster-balanced scatter matrix rather than a covariance.
- Clarify whether cluster-size weighting is intentionally omitted to avoid domination by abundant normal tissue; if so, motivate and test this choice.
- Add a small but focused ablation table comparing unweighted scatter, normalized covariance, attention-weighted covariance, and cluster-size-weighted covariance.
- Justify or replace the row-wise Conv1D covariance compression. At minimum, compare it with diagonal variance, vectorized upper-triangular covariance + MLP, and a low-rank bilinear projection.
- Validate the DBSCAN mechanism with cluster visualizations and quantitative overlap with tumor annotations on CAMELYON16.
- Tone down “significantly improves state-of-the-art performance” to “achieves competitive or slightly improved performance with improved computational efficiency,” unless statistical tests support significance.
- Explicitly distinguish the 5-fold cross-validation protocol from the official CAMELYON16 train/test split.
- Report fold-level results and paired significance tests for comparisons to the strongest baselines.

## Score and Decision

### Calibration process

**Round-1 bracket.** I searched for anchors around WSI/MIL/histopathology/clustering/covariance across weak, middle, and strong score bands. The weak anchors around 2.5–3.4 were generally papers with severe novelty, clarity, or contribution failures. The middle anchors around 4.5–6.0 included medical imaging or WSI papers with plausible ideas and experiments but with important conceptual or validation gaps. The strong anchors around 8.0 were substantially more complete, broadly validated, and clearly justified. Based on this, the initial bracket for HOMIL was **4.5 to 5.5**: the paper is more coherent and better evaluated than the weak anchors, but its central statistical framing and evidence are not strong enough for the 6+ range.

**Round-2 narrowing.** I then searched within the 4–6.5 range for medical imaging/MIL papers with overclaiming, insufficient ablation, and unclear justification. Compared with these anchors, HOMIL is similar to papers around 4.5–5.0: it has a real idea and useful experiments, but the core claimed mechanism is not fully established. It is weaker than the 5.7–6.0 computational pathology anchors that had broader or more clearly motivated contributions, despite their own limitations. I therefore assign **5.0**.

### Retrieved anchors and comparison

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0yVP49SDg0.md` — avg 3.25, Round 1. This WSI MIL anchor had much more severe novelty/clarity concerns; HOMIL is clearer and better grounded, so it scores higher.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TUUjIWntkU.md` — avg 2.50, Round 1. This weak medical clustering anchor appears substantially less developed; HOMIL is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/i4ouG6Kc8M.md` — avg 2.50, Round 1. This histopathology representation anchor was judged weak; HOMIL has more direct task evidence.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Ng4HaH4L6P.md` — avg 3.40, Round 1. This WSI VLM anchor had broad feasibility/data concerns; HOMIL is more focused and empirically cleaner.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6xrDPHhwD3.md` — avg 6.00, Rounds 1 and 2. This WSI pathology method had stronger perceived novelty/validation by some reviewers despite technical concerns; HOMIL is weaker due to the central moment-formulation mismatch and smaller gains.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AZW3qlCGTe.md` — avg 5.67, Round 1. This set-label learning anchor appears somewhat more theoretically motivated; HOMIL is slightly below it.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/trj2Jq8riA.md` — avg 5.67, Round 1 and Round 2. This computational pathology survival paper had important baseline/fairness concerns but a broader VLM survival framework; HOMIL is comparable but somewhat weaker in conceptual soundness.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lo9HMoGNwQ.md` — avg 4.50, Rounds 1 and 2. This medical MIL paper had a core motivation/use-case mismatch; HOMIL has a less severe application mismatch but a significant formulation mismatch, so it is slightly above or similar.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fV0t65OBUu.md` — avg 8.00, Round 1. Strong covariance/moment-method anchor; HOMIL is far less theoretically and empirically established.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xriGRsoAza.md` — avg 8.00, Round 1. Strong MIL/interpretable time-series anchor with broad evaluation; HOMIL is substantially weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/kbjJ9ZOakb.md` — avg 8.00, Round 1. Strong neuroscience representation anchor; not topically close but clearly above HOMIL in completeness.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3i13Gev2hV.md` — avg 8.00, Round 1. Strong vision-language anchor; much more convincing than HOMIL.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zi3MEZRCqd.md` — avg 4.60, Round 2. This medical pretraining paper had interesting ideas but major disentanglement and clarity issues; HOMIL is somewhat more focused but has a comparable level of unresolved evidence.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EtJWnTnqku.md` — avg 5.00, Round 2. This medical generalist anchor had a broad contribution but important validation concerns; HOMIL is comparable in overall acceptance strength.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8g5Ye3c3oR.md` — avg 4.50, Round 2. This weakly supervised medical segmentation anchor had notable mechanism/evidence gaps; HOMIL is slightly stronger but not decisively.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/qtqvuBmhxU.md` — avg 5.75, Round 2. This medical benchmark paper had strong practical value but concerns about insight and evaluation; HOMIL has less community-value breadth and is below it.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/niywLsa54R.md` — avg 5.25, Round 2. This biological representation paper had scale and ambition but unresolved validation; HOMIL is comparable but slightly below due to its central formulation issue.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OPpqmSp0wK.md` — avg 5.00, Round 2. This clustering/representation anchor sits near the appropriate level: plausible idea, but insufficiently convincing.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/PhRYDGqiee.md` — avg 5.40, Round 2. This clustering-related anchor seems somewhat broader; HOMIL is slightly below.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/SPu6k4OZkj.md` — avg 5.25, Round 2. This clustering method anchor had technical ambition but mixed validation; HOMIL is comparable but not stronger.

### Final assessment

HOMIL is a reasonable, focused, and potentially useful WSI MIL method with promising efficiency and competitive results. However, the main statistical claim is not technically precise, the adaptive pathology-preservation mechanism is not validated, and the reported performance improvements are too small relative to variability to support strong SOTA claims. I would recommend rejection in its current form, with a path to acceptance if the formulation is corrected and the component-level evidence is strengthened.

## Score and Decision

Score: **5.0 / 10**  
Decision: **Reject**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>