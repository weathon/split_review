---
job_id: 4374e2f4-504c-4fdb-bcea-6fdd9b1f1be8
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: qkKUG56s5r.pdf
paper: Automatic Complementary-Separation Pruning for Efficient CNNs
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly about neural network pruning for efficient CNNs, which fits general machine learning, optimization, and representation learning for vision.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion. While there are substantial issues in novelty, clarity, and experimental support, these are review-time weaknesses rather than desk-reject-level omissions.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes Automatic Complementary Separation Pruning (ACSP), a supervised pruning method for CNNs that represents each neuron/channel by a class-pair separability vector computed from activations, clusters these vectors to encourage complementary retained components, and uses a knee-finding procedure to automatically choose the number of components to keep per layer. The method is evaluated on several CNN architectures across CIFAR-10, CIFAR-100, and ImageNet-1K, with reported improvements in FLOPs and modest wall-clock latency reductions while largely preserving accuracy.

## Strengths
The paper tackles a practically relevant pruning question, namely how to reduce or remove manual specification of layer-wise pruning ratios. That is a real usability pain point in pruning pipelines, and the attempt to replace manual ratio tuning with an automatic layer-wise criterion is a sensible direction.

The central intuition is understandable and somewhat appealing: components should not only be individually discriminative, but also complementary. Encoding each component by a vector of pairwise class-separation scores, then trying to select representatives from different regions of that space, is a coherent way to operationalize redundancy reduction. This is more interesting than simple magnitude ranking.

Figure 1 is useful in explaining the intended pipeline. In particular, the progression from activations to per-class-pair JM scores to a layer-wise separability matrix makes the representation reasonably concrete. For a paper with a somewhat unusual pruning signal, this figure helps the reader understand what exactly is clustered.

The experimental scope is reasonably broad in terms of architectures and datasets. Table 1 includes VGG, ResNet, DenseNet, and MobileNet on CIFAR-10/100 and ImageNet, which is a better coverage than many pruning submissions that only report one or two models. The method also reports latency in Table 2 rather than only FLOPs, which is important because pruning papers often overclaim practical speedup from FLOP reductions alone.

Some of the reported numbers in Table 1 are competitive. For example, on ImageNet ResNet-50, ACSP reports the largest FLOP speed-up in the table, \(2.25\times\), while keeping pruned accuracy at 76.98, which is tied with the best listed pruned accuracy. Even if cross-paper comparisons need caution, this does suggest the method is not completely ineffective.

The paper at least acknowledges one limitation in Section 5, namely the scaling cost with the number of classes due to all-pairs class comparison. That limitation is real and central to the method, so it is good that the authors do not ignore it.

## Weaknesses
1. **The paper’s main algorithm is internally inconsistent at a crucial step, and this directly affects what method was actually evaluated.**  
   The most serious issue is the contradiction between the complementary-selection story and the actual component selection rule. In Section 3.3.2 and Section 3.4.2, the paper says the graph space is clustered with \(k\)-Medoids, and then one component is selected from each cluster, specifically the highest-weight component within that cluster. That would preserve the diversity rationale. However, **Algorithm 1, line 12 on Page 5** says: “optimal_components \(\leftarrow\) top-\(k'\) components by weight”. That is a materially different algorithm. Global top-\(k\) by weight does not enforce one-per-cluster selection and can collapse onto a single dense region of the graph space, which defeats the whole complementary-separation motivation. This is not a cosmetic wording issue, it changes the pruning rule itself. Figure 2, especially the contrast between medoids and highest-weight components, reinforces that the choice of representative matters. The authors need to state unambiguously which rule was implemented in the reported experiments, and if it was cluster-wise highest-weight selection, Algorithm 1 is wrong; if it was global top-\(k\) by weight, then much of the method narrative is misleading.

2. **There is a concrete mathematical problem in the definition of the separability score.**  
   In **Equation (2) on Page 5**, the Bhattacharyya distance for the scalar Gaussian case appears to have the wrong coefficient in the mean-difference term. The standard 1D form obtained from \(B=\frac{1}{8}(\mu_1-\mu_2)^T \Sigma^{-1}(\mu_1-\mu_2)+\frac{1}{2}\ln\frac{\det \Sigma}{\sqrt{\det\Sigma_1\det\Sigma_2}}\) with \(\Sigma=(\Sigma_1+\Sigma_2)/2\) yields
   \[
   B = \frac{(\mu_1-\mu_2)^2}{4(\sigma_1^2+\sigma_2^2)} + \frac{1}{2}\ln\left(\frac{\sigma_1^2+\sigma_2^2}{2\sigma_1\sigma_2}\right).
   \]
   The paper instead writes
   \[
   \frac{1}{8}\frac{(\mu_{i,j,c}-\mu_{i,j,\tilde c})^2}{\sigma_{i,j,c}^2+\sigma_{i,j,\tilde c}^2},
   \]
   which is smaller by a factor of 2 in the first term. Since the entire graph-space construction is built from these scores, this is not a minor typo. If the implementation used the standard formula but the paper writes the wrong one, that is a presentation and reproducibility issue. If the implementation used the paper’s formula, then the claimed use of JM distance is not technically correct.

3. **The core empirical claim about “complementary selection” is not actually validated.**  
   The paper repeatedly argues that diversity across graph-space regions is what preserves accuracy while pruning redundancy. But the experiments do not isolate this claim. What is missing are direct ablations comparing:  
   - clustering-based representative selection vs pure weight-based selection,  
   - medoid selection vs highest-weight-per-cluster selection,  
   - JM-based graph space vs simpler activation summaries,  
   - automatic \(k\) via Kneedle vs fixed pruning ratios.  
   Without these, the paper does not show that complementary separation is doing the heavy lifting rather than just a particular pruning schedule plus fine-tuning. Figure 2 visually suggests that medoids and high-weight representatives differ, but this remains anecdotal. The method’s conceptual hook is complementary coverage, so the lack of a focused ablation here is a major omission.

4. **The reported gains in Table 1 are hard to interpret as fair evidence because the comparisons are cross-paper and the baselines are not normalized to the same base accuracy or training recipe.**  
   This is a common issue in pruning papers, and it matters here. In **Table 1 on Page 8**, ACSP is compared to methods with different base model accuracies, different training protocols, and likely different fine-tuning budgets. For example, on ImageNet ResNet-50, ACSP starts from a base accuracy of 76.32, whereas several baselines are reported from 76.15, 76.20, 76.60, or 76.65. On CIFAR models, the base accuracies also vary. That makes “\(\Delta\) Accuracy” and pruned accuracy difficult to compare directly. The paper leans heavily on best-number highlighting, but a fairer comparison would require either reproducing strong baselines under one common setup or at least discussing this limitation explicitly. As written, Table 1 is suggestive, not decisive.

5. **The wall-clock latency improvements in Table 2 are much smaller than the FLOP reductions, and the paper underexplains this gap.**  
   The paper claims large speedups, such as \(2.25\times\) on ResNet-50 in Table 1, but **Table 2 on Page 9** shows only \(-6.32\%\) batch latency reduction and \(-8.07\%\) single-inference latency reduction for that same model. This is not a contradiction, but it substantially softens the practical deployment story. The paper acknowledges in one sentence that hardware utilization is not linear in FLOPs, but does not analyze which layers are pruned, whether memory bandwidth dominates, or whether the pruning pattern aligns poorly with GPU kernels. Given the title’s emphasis on “efficient CNNs” and the abstract’s emphasis on faster inference time, this discrepancy deserves much more careful treatment. Right now the practical efficiency claim reads stronger than the latency evidence justifies.

6. **The automatic pruning-volume selection is underjustified and may be brittle.**  
   The method evaluates all \(k \in \{2,\dots,N_i\}\), scores them using MSS, then uses Kneedle to pick the knee. But the paper does not explain why MSS should produce a monotone or knee-structured curve suitable for Kneedle, nor how sensitive the result is to the polynomial fit choice mentioned in Section 4.1. The line “results ... were obtained using a second-degree polynomial in the Kneedle algorithm” introduces an extra design choice that is not motivated or ablated. If a different polynomial degree changes selected \(k\) materially, the “fully automated” claim becomes weaker than advertised. This is precisely the sort of pipeline detail that needs sensitivity analysis.

7. **The method’s computational cost is likely substantial, and the paper understates it.**  
   Section 3.2 only comments that Kneedle itself has \(\mathcal{O}(N_i^2)\) time and negligible wall-clock cost for \(N_i \le 256\). But that is not the dominant expense. The expensive part is constructing the graph space by computing separability across all class pairs and, for convolutional layers, across all spatial locations. The dimensionality described in Section 3.2 and Section 3.3.1 is \(p \times p \times \binom{C}{2}\) per component, which can become large, especially for early convolutional layers and larger class counts. Figure 1 is actually helpful here, because it makes visually obvious that the method expands each component into a fairly high-dimensional object before clustering. The conclusion briefly mentions scaling with \(C\), but the paper never quantifies total pruning-time overhead across a full network, which is necessary for judging practicality.

8. **Several key implementation details are missing or underspecified, limiting reproducibility and making the method harder to assess.**  
   Examples include:  
   - How exactly activations from convolutional maps are collected before fitting per-pixel class statistics, especially under batch normalization and ReLU.  
   - Whether activations are taken pre- or post-nonlinearity.  
   - How zero or near-zero variances are handled in **Equations (1) and (2)**, since the log term and denominator can become unstable.  
   - Which distance metric is used inside \(k\)-Medoids on the separability vectors.  
   - Whether the graph-space vectors are normalized before clustering, which could materially affect cluster geometry.  
   - Whether all layers, including residual projection layers or depthwise layers in MobileNet-V2, are pruned identically.  
   These are not nitpicks. The method is defined by these representations and distances.

9. **The role of supervision and data usage in pruning is not examined critically enough.**  
   The method is explicitly supervised and uses the labeled dataset to compute class-pair separability, which is fine, but then its scope is narrower than some structured pruning methods that do not require labels. The paper mentions this at a high level in the introduction, but it does not discuss what happens under class imbalance, limited-label settings, or noisy labels. Since the separability vectors depend directly on class-conditional activation statistics, these are not peripheral concerns.

10. **The related-work positioning is somewhat incomplete for the exact claim being made.**  
    The paper positions itself against structured pruning, activation-based pruning, and automatic pruning-ratio methods, which is reasonable, but it gives limited attention to prior work studying pruning signals and redundancy reduction more systematically. Because the paper’s main contribution is not merely “another pruning method” but a specific pruning signal plus an automatic schedule, the comparison against broader analyses of channel-pruning signals and layer-adaptive pruning strategies feels thinner than it should be. This weakens the novelty case.

11. **Presentation quality is uneven, with notation and terminology occasionally sloppy enough to affect understanding.**  
    Examples include the notation around \(\mathcal{I}_i\) and \(\mathcal{I}_{i,j}\), which is inconsistently rendered on **Page 3**, and the typo “ImageNet-10” in **Table 1/Page 8** and Section 4, which presumably means ImageNet-1K. The paper also uses “graph space” in a somewhat nonstandard way; it is really a feature embedding of components, not a graph in the usual graph-learning sense. That terminology is not fatal, but it does create avoidable conceptual fog.

12. **The evidence for generality across separability metrics is weak.**  
    The paper states on **Page 5** that Hellinger and Wasserstein were also evaluated and JM worked best, but the main paper does not present these results. Since “our method is not tied to a specific separability metric” is an explicit claim, some quantitative evidence belongs in the main text, even if only as a compact ablation table.

## Questions
1. Please clarify exactly which component selection rule was used in all reported experiments. Was it:
   \[
   \text{one highest-weight component per cluster},
   \]
   or
   \[
   \text{global top-}k \text{ by weight},
   \]
   as written in Algorithm 1, line 12? This is the single most important clarification for me, because the two procedures embody very different methods.

2. Can you correct or justify **Equation (2)**? If the implementation used the standard Bhattacharyya distance,
   \[
   \frac{(\mu_1-\mu_2)^2}{4(\sigma_1^2+\sigma_2^2)} + \frac{1}{2}\ln\left(\frac{\sigma_1^2+\sigma_2^2}{2\sigma_1\sigma_2}\right),
   \]
   please state that clearly. If not, please explain the derivation of the coefficient used in the paper and whether this affects the reported results.

3. Please provide an ablation that directly tests the complementary-selection hypothesis. At minimum, I would like to see comparisons between:  
   - highest-weight-only pruning,  
   - medoid selection,  
   - highest-weight-per-cluster selection,  
   - ACSP without Kneedle but with fixed \(k\).  
   This would substantially increase confidence that the method’s gains come from the proposed idea rather than from generic fine-tuning after mild pruning.

4. How sensitive is the automatic choice of \(k\) to the Kneedle configuration, especially the second-degree polynomial smoothing mentioned in Section 4.1? A sensitivity plot over several layers would help.

5. What activation tensor is used for separability computation, exactly? Is it before or after nonlinearity, before or after batch normalization, and how do you handle nearly constant channels where \(\sigma^2 \approx 0\)?

6. Can you provide pruning-time overhead for a full network, not just the negligible runtime of Kneedle itself? The cost of graph-space construction seems likely to dominate, especially for large \(C\) and large early-layer feature maps.

7. The latency improvements in **Table 2** are much smaller than the FLOP reductions in **Table 1**. Can you break this down by layer type or stage to explain where the practical bottlenecks remain after pruning? That would make the efficiency claim much more convincing.

8. If possible, please include same-setup baseline re-runs for at least a couple of strong methods on one CIFAR model and one ImageNet model. Cross-paper comparisons in Table 1 are useful but not enough to isolate the advantage of ACSP.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper. The work is a model-efficiency method evaluated on standard vision benchmarks, and the manuscript does not introduce a dataset, human-subject protocol, or a clearly harmful application.

## Soundness Rating
2: fair. The high-level idea is plausible and some experimental evidence is provided, but there are unresolved technical inconsistencies, an apparent equation issue, and insufficient ablation support for the paper’s main causal claims.

## Presentation Rating
2: fair. The paper is readable at a high level and Figures 1 and 2 help, but several important details are underspecified, notation is occasionally sloppy, and core algorithmic steps are presented inconsistently.

## Contribution Rating
2: fair. The paper has an interesting angle on complementary component selection and automatic pruning extent, but the current evidence and positioning do not yet establish it as a strong enough contribution for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The direction is interesting and the empirical scope is decent, but the paper currently has too many unresolved methodological and validation issues, especially the algorithm inconsistency, the unclear math around the separability metric, and the lack of direct evidence that complementary selection is the source of the gains.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I checked the method description, equations, figures, and tables carefully, and my main concerns are based on concrete inconsistencies and missing validations rather than personal preference.