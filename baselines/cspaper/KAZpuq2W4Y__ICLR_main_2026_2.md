---
job_id: 1e9e7adc-9187-4c92-8d5f-255982b123fe
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: KAZpuq2W4Y.pdf
paper: Multi-Instance Learning for Whole-Slide Image Classification Using Higher-Order Moments
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within representation learning and supervised learning for computational pathology, using MIL for whole-slide image classification, which fits ICLR’s scope.

## Minimum Quality
Pass ✅. The paper contains the required scientific sections and presents a complete method with experiments, although there are serious concerns about novelty, mathematical specification, and experimental rigor that affect the recommendation rather than triggering desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes HOMIL, a multi-instance learning framework for whole-slide image classification that augments standard attention-based MIL with a second-order representation derived from a covariance matrix over cluster features. To reduce computational cost, the method first clusters patch features using PCA followed by DBSCAN, then computes first-order and second-order slide representations from cluster-level features, fuses them with an attention mechanism, and evaluates the approach on CAMELYON16 and TCGA-NSCLC.

## Strengths
The paper addresses a real and important practical issue in WSI classification, namely the tension between rich slide-level structure and the extreme computational burden of processing thousands of patches per slide. The motivation for going beyond pure first-order aggregation is reasonable, and the paper gives a simple statistical lens for interpreting standard ABMIL as a first-order estimator, which makes the proposed extension easy to understand at a high level.

The method is also easy to place conceptually. Figure 1 helps with this. In particular, the diagram clearly shows the two-stream design, where clustered patch features produce both a first-order vector and a second-order branch from the covariance matrix before fusion. That figure makes the intended computational story quite concrete: the authors are not merely adding another attention block, they are explicitly trading instance-level processing for cluster-level summarization and then compensating with a richer slide descriptor. Even though I have concerns about whether the implementation matches the stated statistical interpretation, the architectural idea itself is understandable and reasonably motivated from the figure.

The empirical results in Table 1 and Table 2 are promising on the two reported datasets. On both CAMELYON16 and TCGA-NSCLC, HOMIL is reported to outperform the listed baselines on ACC, AUC, and F1. The efficiency numbers are also favorable relative to several stronger baselines such as TransMIL, MambaMIL, and HMIL. If these comparisons are fully fair and reproducible, then the method would have practical appeal for large-scale WSI pipelines.

The ablation in Table 3 is useful and at least attempts to isolate the roles of the clustering module and the second-order moment module. The pattern reported there is directionally consistent with the paper’s core claim: removing clustering hurts runtime and accuracy, while removing second-order statistics hurts performance more than runtime.

## Weaknesses
1. **The core novelty is overstated and the paper is poorly positioned against closely related prior work on second-order MIL and clustering-based WSI MIL.**  
   The central idea, augmenting MIL aggregation with second-order or covariance-style statistics, is not sufficiently differentiated from prior WSI MIL literature. The related work in Section 2 mainly contrasts against first-order attention MIL, but does not seriously discuss prior second-order pooling or covariance-based MIL formulations for WSI classification, nor clustering-centric MIL pipelines for whole-slide analysis. This matters because the paper’s main conceptual pitch is precisely “MIL + second-order moments + clustering,” and without careful positioning it is difficult to judge whether HOMIL is a meaningful advance or mostly a recombination of existing ingredients. As written, the novelty claim in the Introduction and Section 2 feels too broad relative to the literature coverage.

2. **The second-order formulation is mathematically inconsistent with the paper’s own description.**  
   This is the biggest technical issue for me. In Section 4.3.3, the paper explicitly states that it computes an “attention-weighted covariance matrix,” yet the actual formula is
   \[
   \mathbf{C}=\sum_{k=1}^{K}\hat{\mathbf{g}}_{k}\hat{\mathbf{g}}_{k}^{\top},
   \]
   where \(\hat{\mathbf{g}}_k = \mathbf{g}_k - \mathbf{v}^{(1)}\). There is no attention weight \(a_k\) in this equation. The same problem already appears in Section 3.2 on Page 3, where the covariance matrix is introduced after defining a weighted mean \(\boldsymbol{\mu}=\sum_i a_i \mathbf{h}_i\), but the covariance expression again omits the weights:
   \[
   \boldsymbol{\Sigma}=\sum_{i=1}^{n}(\mathbf{h}_{i}-\boldsymbol{\mu})(\mathbf{h}_{i}-\boldsymbol{\mu})^{\top}.
   \]
   If the intended object is a weighted covariance, the natural form would be something like
   \[
   \mathbf{C}=\sum_{k=1}^{K} a_k \, (\mathbf{g}_k-\mathbf{v}^{(1)})(\mathbf{g}_k-\mathbf{v}^{(1)})^\top,
   \]
   possibly with a normalization term depending on whether the \(a_k\) already sum to 1. As written, the text says “attention-weighted,” but the equation computes an unweighted scatter matrix around an attention-weighted mean. Those are not the same thing. This ambiguity matters because it affects the semantics of the representation, the fairness of the “higher-order moment” interpretation, and reproducibility.

3. **The “covariance” is not actually a covariance in the standard statistical sense, and the omission is not cosmetic.**  
   In both Section 3.2 and Section 4.3.3, the second-order matrix is an unnormalized sum of outer products, not a covariance estimator. There is no division by \(K\), \(K-1\), or an equivalent weighted normalization. Since the number of clusters \(K\) varies by slide due to DBSCAN, the scale of \(\mathbf{C}\) will systematically depend on how many clusters are produced. That means the second-order representation is confounded by compression rate and bag size. This is scientifically important, not merely stylistic. The model may be learning slide size or cluster count effects instead of genuine covariance structure. If the authors intentionally want an unnormalized scatter matrix, they should say so and justify it. Right now the terminology and mathematics do not line up.

4. **Clustering changes the object whose moments are being computed, but this distortion is not analyzed.**  
   In Section 4.1 and Section 4.2, patches are first aggregated into cluster means
   \[
   \mathbf{g}_k=\frac{1}{|\mathcal{I}_k|}\sum_{i\in \mathcal{I}_k}\mathbf{h}_i.
   \]
   The first-order and second-order moments are then computed over \(\{\mathbf{g}_k\}_{k=1}^K\), not over the original patch features. This is a major modeling decision. Once large homogeneous regions are collapsed to a single mean vector, within-cluster variability is discarded. Yet the second-order branch is sold as a way to capture feature variability and inter-feature relations across the slide. Those two claims are in tension. The method may indeed gain efficiency, but it is not obvious that the resulting covariance over cluster means reflects the same biological heterogeneity the paper discusses in Section 1 and Section 3.2. A more careful decomposition of what information is lost versus retained would strengthen the scientific case.

5. **The claim that DBSCAN gives fine granularity to pathological regions and coarse granularity to normal tissue is asserted rather than demonstrated.**  
   The paper repeats this claim several times, including Section 2.2, Section 4.1, and Section 4.2. But DBSCAN is run on PCA-reduced patch features, not on annotated pathology labels, and apparently not on explicit spatial coordinates either. Therefore, it is not guaranteed that “rare pathological regions” become small clusters or that “abundant normal tissues” become large clusters. That is an intuition, not evidence. A qualitative visualization of clusters overlaid on slides, or statistics comparing cluster sizes for tumor versus normal regions, would be necessary to support the narrative. Figure 1 illustrates the intended behavior in cartoon form, but that does not validate the claim empirically. This matters because the efficiency and diagnostic-preservation story of the paper rests heavily on this assumption.

6. **The second-order compression module is under-justified and not clearly specified.**  
   The transformation from \(\mathbf{C}\in\mathbb{R}^{d\times d}\) to \(\mathbf{v}^{(2)}\in\mathbb{R}^{d}\) in Section 4.3.3 is one of the most unusual parts of the method, yet it is both ad hoc and notationally confusing. The paper says each row \(\mathbf{C}_i\) is convolved with kernels \(\{\mathbf{k}_i\}_{i=1}^T\), but then the equation uses \(k_{l,j}\) and refers to kernel \(\mathbf{k}_t\). The indexing is inconsistent. It is also unclear whether kernels are shared across rows, how they are parameterized, and why row-wise 1-D convolution with max-pooling is an appropriate way to summarize covariance structure. A covariance matrix has symmetry and global structure; the proposed operation ignores that structure and may destroy useful information. Without ablations comparing this design to simpler alternatives, such as flattening the upper triangle, low-rank projections, matrix square-root pooling, trace/diagonal summaries, or even an MLP over a vectorized covariance, it is hard to know whether this module is principled or just a convenient compression trick.

7. **The training objective is underspecified.**  
   Section 4 ends with the classifier output
   \[
   \hat{y}=\text{softmax}(\mathbf{W}_c\mathbf{z}+\mathbf{b}_c),
   \]
   but the actual loss function is never written down. I assume cross-entropy, but assumptions should not be left implicit in a methods paper. This omission is especially relevant here because the model has multiple attention modules, a clustering pre-processing stage, and a custom second-order branch; even small training choices can materially affect results. The lack of an explicit optimization objective reduces reproducibility.

8. **The experimental setup is unclear regarding data splits, especially for CAMELYON16.**  
   Section 5.1 states that CAMELYON16 contains 270 training WSIs and 129 testing WSIs. Section 5.2 then says, “For both datasets, we use a unified 5-fold cross-validation setup with patient-level partitioning.” It is not clear whether the official train/test split of CAMELYON16 was respected and cross-validation was performed only on the training set, or whether all slides were pooled into a new 5-fold protocol. This is not a small procedural detail. For a benchmark with a canonical split, changing the evaluation protocol can make comparisons with prior work less meaningful, and if the test portion was reused within cross-validation it would be a methodological problem. The authors need to state this unambiguously.

9. **The reported runtime comparison is not fully convincing as presented.**  
   The paper reports “Time” in Table 1 and Table 2, and notes on Page 7 that for HOMIL this includes clustering, while for the other methods it includes “training+inference only.” Even setting aside that asymmetry, runtime alone is hard to interpret without information such as number of trainable parameters, memory usage, average number of instances versus clusters per slide, and whether all baselines were equally optimized. The claim that clustering improves efficiency is plausible, but the evidence would be stronger if the paper reported the average \(n\) and \(K\), preprocessing cost, GPU memory, and per-epoch throughput. Table 3 is directionally useful, but it still does not fully disentangle where the savings come from.

10. **The tables have formatting and reporting issues that materially hurt interpretability.**  
    Table 1, Table 2, and Table 3 report entries like “96.982.43” or “99.230.62” and state that metrics are given as “meanSE (%)”. Presumably this means mean \(\pm\) SE, but the ± symbol is missing throughout. This is not a trivial typo because it makes uncertainty hard to parse at first read. More importantly, no significance testing or confidence interval discussion is given, even though several gains over stronger baselines are modest in absolute terms, especially on TCGA-NSCLC. For example, in Table 2 the gain over HMIL in ACC is only about \(0.35\%\), and the AUC gains over ABMIL are below one point. The paper should be much more careful in claiming superiority when the margins are small and uncertainty reporting is garbled.

11. **The ablation study is too narrow to support the main explanatory claims.**  
    Table 3 only studies CAMELYON16, and only removes CM and SOM. That is a start, but it is not enough. The paper’s main method has several coupled design choices: PCA dimension \(d'=32\), DBSCAN with a heuristic \(\epsilon\) defined by the 65th percentile, minPts \(=4\), cluster mean pooling, unnormalized covariance, row-wise 1-D convolution with kernel size \(m=64\), \(T=4\) kernels, and fusion attention. None of these are isolated in the main paper. A stronger ablation would test weighted versus unweighted covariance, covariance over patches versus covariance over cluster means, alternative compression modules for \(\mathbf{C}\), and whether DBSCAN itself is necessary versus simpler grouping strategies. Without this, the paper cannot really justify which component is doing the work.

12. **Figure 2 provides limited evidence for the claimed interpretation, and in one respect raises further questions.**  
    Figure 2(a) shows training and validation loss curves that stay high for a long period and then drop sharply around epoch 40 to 50 before stabilizing. This suggests there may be an unreported learning-rate schedule, warm-up, or optimization event, but Section 5.2 does not mention such details. Figure 2(b) shows the first-order fusion weight ending substantially above the second-order weight, which the authors interpret positively in Section 5.5. I read this more cautiously. If the learned fusion consistently assigns much higher mass to the first-order branch, then the second-order branch may be only marginally useful, and the paper should quantify how much additional signal it actually contributes on a per-slide basis. The figure is interesting, but it does not yet strongly validate the “higher-order moments are critical” claim.

13. **The baseline set is not sufficiently comprehensive for the paper’s exact contribution.**  
    The paper compares against common MIL models, which is good, but it does not include an explicit second-order MIL baseline or a stronger direct comparison to clustering-based WSI MIL methods. This omission is important because the claimed advance is not just “better than ABMIL,” it is “first-order + second-order + adaptive clustering.” The current comparisons therefore support competitiveness, but not clean attribution or stronger novelty claims.

## Questions
1. In Section 5.2, how exactly was CAMELYON16 evaluated? Did you preserve the official train/test split and perform cross-validation only within the training partition, or did you redefine a 5-fold split over the full dataset? Please answer this precisely, because it directly affects the validity and comparability of Table 1.

2. Please clarify the intended second-order statistic. Is Equation in Section 4.3.3 meant to be a weighted covariance, an unweighted covariance, or an unnormalized scatter matrix? If weighted, please provide the correct formula; if unweighted, please revise the terminology and explain why centering by the attention-weighted mean but omitting \(a_k\) in the outer-product sum is the right design.

3. Why is the covariance not normalized by the number of clusters or an equivalent weighted factor? Since \(K\) varies across slides due to DBSCAN, can you show that performance is not driven by scale differences induced by variable cluster counts?

4. Can you provide an ablation comparing
   \[
   \sum_k a_k(\mathbf{g}_k-\mathbf{v}^{(1)})(\mathbf{g}_k-\mathbf{v}^{(1)})^\top
   \]
   versus the current
   \[
   \sum_k(\mathbf{g}_k-\mathbf{v}^{(1)})(\mathbf{g}_k-\mathbf{v}^{(1)})^\top,
   \]
   and ideally also a normalized version? This would directly test whether the current formulation is principled or accidental.

5. The cluster-level averaging in Section 4.2 discards within-cluster variance. Can you quantify how much information is lost? For example, can you compare covariance over original patches versus covariance over cluster means at matched runtime budgets?

6. The paper repeatedly claims that DBSCAN assigns coarse granularity to normal tissue and fine granularity to pathological regions. Can you provide evidence for this claim, such as histograms of cluster sizes by tissue type, or slide visualizations showing cluster assignments overlaid on pathology regions?

7. Please clarify the 1-D convolution compression in Section 4.3.3. Are kernels shared across rows? Is the notation \(k_{l,j}\) a typo for \(k_{t,j}\)? Why is row-wise convolution with max-pooling preferable to simpler covariance summarization methods? A targeted ablation here would help.

8. What is the exact training loss and model selection criterion? Was early stopping used? Figure 2(a) suggests a training dynamic with a sharp transition around epoch 40 to 50; if there is a learning-rate schedule or warm-up, it should be described.

9. Can you add a stronger efficiency breakdown, including average number of patches \(n\), average number of clusters \(K\), memory usage, and whether clustering time is a one-time preprocessing cost or repeated each fold/epoch? Table 1 to Table 3 are suggestive but not yet sufficiently diagnostic.

10. If possible, please compare against at least one direct second-order MIL baseline and one clustering-aware WSI MIL baseline. That would substantially improve confidence that the gains come from the proposed ideas rather than from implementation or protocol differences.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper uses publicly available pathology datasets and presents a methodological contribution for slide classification. I do not see an ethics issue that requires escalation based on the main paper alone.

## Soundness Rating
2: fair. The high-level idea is plausible and the empirical results are promising, but the mathematical specification of the second-order component is inconsistent with the claims, and key experimental details remain unclear.

## Presentation Rating
2: fair. The paper is readable at a high level and Figure 1 is helpful, but there are several notation issues, underspecified equations, confusing experimental details, and table formatting problems that materially affect clarity.

## Contribution Rating
1: poor. The practical direction is relevant, but the paper does not sufficiently establish conceptual novelty relative to related second-order and clustering-based MIL work, and the main claimed contribution is weakened by the current formulation and evidence.

## Overall Rating
2: Reject, not good enough. The paper has a sensible motivation and some encouraging numbers, but in its current form it falls short of ICLR standards due to weak positioning, a mathematically muddled second-order formulation, and experimental ambiguities that prevent me from trusting the central claims as much as the paper asks me to.

## Reviewer Confidence
4: confident. I am confident in this assessment, though it is still possible that some of the concerns, especially around evaluation protocol and intended covariance formulation, could be partially resolved in rebuttal.