---
job_id: 1f69c459-d088-47aa-b659-c27146086c30
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 7yvz93kBw9.pdf
paper: D2GS: Depth-And-Density Guided Gaussian Splatting for Stable and Accurate Sparse-View Reconstruction
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies a machine learning method for sparse-view novel view synthesis and 3D representation learning with Gaussian splatting, including a new robustness metric for learned representations.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including Abstract, Introduction, Related Work, Method, Experiments with quantitative and qualitative results, and Conclusion/Discussion. The work is not obviously trivial or fatally flawed, and the empirical support is substantial enough to warrant full review, even though there are several technical and methodological issues that affect the final score.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious reviewer-targeted text, or other apparent manipulation attempts in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies sparse-view failure modes of 3D Gaussian Splatting, arguing that sparse supervision causes near-field overfitting with excessive Gaussian density and far-field underfitting with insufficient coverage. To address this, the authors propose D²GS, which combines a depth-and-density guided dropout module (DD-Drop) and a distance-aware fidelity enhancement loss (DAFE), and they also introduce an inter-model robustness metric (IMR) based on optimal transport between Gaussian mixtures. Experiments on LLFF and MipNeRF360, with additional results in the appendix on DTU, show improved reconstruction quality and lower instability relative to several 3DGS and NeRF baselines.

## Strengths
The paper is built around a clear and intuitive diagnosis of sparse-view 3DGS failure modes. The central observation, namely that sparse-view training creates too many Gaussians in near, texture-rich regions and too few in far regions, is easy to follow and is visually supported by **Figure 1**. That figure is one of the better parts of the paper because it does not merely show nicer renderings, it links visual artifacts to the distribution of Gaussian primitives and gives primitive counts in the highlighted boxes. This helps motivate why a uniform dropout policy may be too blunt.

The method itself is simple enough to implement and reasonably well matched to the motivating failure analysis. The combination of a local score from depth and density with a coarse depth-stratified attenuation in **Equation (2)** is conceptually straightforward, and **Figure 2** presents the full pipeline clearly. In particular, the separation between DD-Drop for overfitting control and DAFE for far-field supervision is easy to understand from the diagram.

The empirical results are generally solid. In **Table 1**, the method improves over DropGaussian on LLFF 3-view at both 1/8 and 1/4 resolution across all listed metrics, including PSNR, SSIM, LPIPS, and AVGE. The gains are not huge, but they are consistent, which matters more here than a single cherry-picked metric. The ablation in **Table 4** is also helpful: the full model outperforms the baseline and the partial variants, and the IMR number decreases steadily as components are added, which at least supports the claim that the two modules are complementary.

The paper makes a meaningful effort to evaluate robustness beyond image-space metrics. The proposed IMR is interesting because sparse-view 3DGS methods are often unstable across runs, and the left panel of **Figure 3** makes that issue concrete. Even if I have reservations about the exact formulation, I appreciate that the authors try to measure representation-level consistency rather than only report PSNR/SSIM.

The qualitative results are mostly convincing. In **Figure 4**, the proposed method tends to reduce the visible streaking or structural artifacts seen in 3DGS and sometimes in DropGaussian, especially in the highlighted crop regions. The examples are not perfectly uniform in strength, but the figure does support the claim that the method improves local fidelity in challenging sparse-view scenes.

## Weaknesses
1. **The paper’s core empirical claim depends heavily on monocular depth priors, but the framing underplays this dependence.**  
   The DAFE module in **Section 3.3** directly uses a monocular depth estimator to generate a binary far-region mask via **Equation (4)**, and the method description on **Page 4** says the model “strengthens far-field supervision using depth-derived masks predicted by a monocular depth estimator.” This is not a small side ingredient, it is one of the two main modules. Yet the paper still frames the contribution primarily as a sparse-view 3DGS regularization scheme rather than a depth-prior-assisted method. This matters scientifically because part of the reported gain may come from importing a strong pretrained depth prior rather than from the proposed Gaussian regularization itself. **Table 6** does show that different depth estimators change performance, which actually reinforces this concern. I would have liked a more explicit decomposition of “gain from better dropout” versus “gain from external monocular depth prior.” As written, the attribution of improvements is too optimistic.

2. **Several methodological details of DD-Drop are underspecified, especially the camera-dependent depth definition and the actual sampling mechanism.**  
   In **Section 3.2**, the depth of Gaussian \(d_i\) is defined as Euclidean distance to “the camera,” but this is ambiguous in multi-view training. The appendix later states on **Page 14** that depth is defined relative to a randomly selected training camera per iteration. That is a very consequential detail and should be in the main paper. If the same Gaussian gets different depth values depending on the sampled camera, then the dropout probability \(P_i\) in **Equation (2)** is not an intrinsic scene property but a stochastic view-conditioned quantity. That may be fine, but it changes the interpretation of the method substantially, and the main paper does not discuss the implications. Similarly, the paper says high-scoring Gaussians “would be dropped with a higher probability,” but it never clearly states whether Bernoulli sampling is done independently for each Gaussian, whether dropout is applied before or after densification/pruning, and how this interacts with opacity reset and Gaussian growth. Since the method’s main contribution is dropout, these implementation details are not cosmetic.

3. **The proposed IMR metric is interesting but not fully convincing as a robustness measure, and the mathematical formulation raises unanswered questions.**  
   The metric in **Section 3.4** abstracts each 3DGS model as a Gaussian mixture with weights \(w_{i,j} \propto \alpha_{i,j}\) in **Equation (9)**. This assumes opacity is an appropriate proxy for component importance, which is plausible but far from obvious, especially because rendered contribution also depends on visibility, depth ordering, covariance, and color. A highly opaque Gaussian that is rarely visible is treated as highly important in the model-level distribution, while a lower-opacity but broadly visible Gaussian is discounted. The paper does not justify why opacity-only weighting is the right choice. This matters because the validity of IMR hinges on the representation abstraction.  
   There is also an asymmetry issue in the approximated pairwise distance of **Equation (11)**, where the shape term uses \(\Sigma_2^{-1}\) rather than a symmetric function of \(\Sigma_1\) and \(\Sigma_2\). The exact \(W_2\) distance in **Equation (10)** is symmetric, but the approximation shown in **Equation (11)** is not obviously symmetric. Then **Equation (12)** and **Equation (13)** build an OT distance on top of that approximation. If the ground cost is asymmetric, it is not clear whether the induced mixture discrepancy behaves as a proper distance in the way the text suggests. At minimum, the paper should discuss this explicitly.  
   Finally, **Table 3** reports IMR differences such as 3.162 to 3.039. Without any notion of variance or sensitivity to the 10-model sampling procedure, it is difficult to know whether these are substantial or just modest numerical shifts. The idea is promising, but the evidence is not yet strong enough to establish IMR as a reliable evaluation metric.

4. **The approximation and theory around the Wasserstein/Bures term are presented too confidently relative to what is actually established in the main paper.**  
   The main text introduces **Equation (11)** as a first-order Taylor approximation to the Bures shape term in **Equation (10)**, but the resulting expression is second-order in \(\Sigma_1-\Sigma_2\). The appendix derivation on **Pages 13-14** clarifies this, yet the main paper does not state the approximation regime clearly. The quality of the approximation will depend on \(\|\Sigma_1-\Sigma_2\|\) being small after whitening by \(\Sigma_2\), but this assumption is nowhere tied to actual learned Gaussian covariances in 3DGS. In other words, the paper introduces a mathematically convenient surrogate, then uses it operationally at scale, but does not show that the surrogate is accurate for the distributions encountered in practice. Since IMR is one of the claimed contributions, this gap matters. A simple empirical correlation between exact pairwise Bures costs and the approximation on a manageable subset would have gone a long way.

5. **The experimental evidence is good but not yet exhaustive enough to fully substantiate the claimed mechanism.**  
   The ablations in **Table 4** are useful, but they still leave some causal ambiguity. For example, the row with density score plus layering and the row with depth score plus layering are compared, but there is no direct ablation isolating DAFE with and without DD-Drop in a way that shows whether DAFE mainly improves far-field structure or merely adds another weighted reconstruction loss. Similarly, **Table 5** tunes \(\omega_{\text{depth}}, \omega_{\text{density}}, r_{\min}, r_{\max}, \tau,\lambda_{\text{DAFE}}\), but these are all local hyperparameter sweeps near the final model. What is still missing is a stronger diagnostic experiment validating the central narrative of the paper, namely that DD-Drop reduces near-field primitive overpopulation while DAFE increases far-field coverage. The paper motivates this with **Figure 1**, but it does not report a quantitative before/after analysis of Gaussian counts or density stratified by depth for the proposed method itself. That is a missed opportunity because the paper’s story is explicitly about spatial distribution correction.

6. **Some comparisons are not as clean as they should be, especially when the paper departs from reported baseline numbers.**  
   On **Page 15**, the authors state that for some DropGaussian settings they could not reproduce the results in the original paper and therefore report numbers from their own training. I appreciate the honesty, but this also complicates the fairness of the benchmark. If a paper claims state-of-the-art improvements and one of the strongest baselines is replaced by the authors’ own reproduction, that baseline needs extra care, more implementation detail, and ideally variance over runs. Otherwise, readers cannot easily tell whether the improvement is due to a better method or a weaker reproduction. This issue affects how strongly one should interpret the gains in **Table 1**, **Table 2**, and the appendix tables.

7. **The novelty is moderate rather than strong.**  
   At a high level, the method combines two fairly intuitive ideas: non-uniform dropout using spatial heuristics, and extra loss weighting for distant regions using monocular depth masks. That does not make the paper uninteresting, especially because engineering simplicity has value in this area, but the contribution is more of a careful integration and diagnosis paper than a deeply new algorithmic advance. The same applies to IMR, which is an interesting repackaging of OT-style comparison for Gaussian sets, but not yet a mature benchmark contribution. For ICLR main track, this level of novelty is acceptable only if the empirical and analytical support are especially convincing; here I think they are solid but not fully decisive.

8. **Presentation is generally good, but there are multiple clarity issues in notation and paper organization.**  
   The paper occasionally introduces notation or naming in a way that invites confusion. For example, the text alternates between \(\hat{W}_2^2\) and \(\tilde{W}_2^2\) for the approximate Gaussian distance, with **Equation (11)** using \(\hat{W}\) while the text around **Equation (13)** refers to \(C_{ij}=\tilde{W}_2^2(\cdot,\cdot)\). Also, **Table 2** is awkwardly placed and its captioning relative to the surrounding text is confusing on **Page 8**. These are not fatal issues, but they make the paper feel less polished than it could be.

## Questions
1. In **Equation (2)**, how exactly is dropout sampled in practice? Is each Gaussian independently dropped via a Bernoulli variable with probability \(r(t)P_i\), or is there a top-\(k\)/quota-based selection after scoring? Please state the exact stochastic rule used during training.

2. The appendix says depth is defined with respect to a randomly selected training camera each iteration. Can the authors clarify this in the main paper and discuss whether the same Gaussian can oscillate between near/middle/far layers across iterations? A small ablation comparing random-camera depth versus a camera-aggregated depth statistic would increase my confidence.

3. For IMR, can the authors provide empirical evidence that the approximation in **Equation (11)** is accurate enough for the covariances observed in trained models? Even a subsampled comparison against the exact Bures-based cost from **Equation (10)** on a smaller scene would help.

4. Why is opacity-only weighting in **Equation (9)** the right abstraction for model-level comparison? Did the authors test alternatives, for example weights incorporating rendered visibility, accumulated contribution, or normalized transmittance-aware statistics?

5. Can the authors provide a depth-stratified analysis of Gaussian population changes before and after applying DD-Drop and DAFE? The central narrative of the paper would be much stronger if there were a quantitative counterpart to **Figure 1**, not only final rendering metrics.

6. Since some baseline numbers, especially for DropGaussian, come from the authors’ own reproduction, can the authors include more detail on training settings and whether those reproduced baselines were tuned comparably to the proposed method? Reporting variance across repeated runs for the main quantitative tables would also be helpful.

7. For **Table 3**, what is the run-to-run variance of IMR itself over different sets of independent trainings? The reported differences are relatively small numerically, so uncertainty estimates would help judge significance.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics issues are apparent from the paper itself. The use of monocular depth estimators may import dataset bias or failure modes into the reconstruction pipeline, but this is a technical limitation rather than an ethics-review trigger in the current submission.

## Soundness Rating
3: good. The method is technically plausible and empirically supported, but some key claims, especially around IMR and attribution of gains to the proposed components, are not as fully validated as the paper sometimes suggests.

## Presentation Rating
3: good. The paper is readable and the main idea is understandable, with useful figures such as **Figure 1**, **Figure 2**, and **Figure 4**, but there are several notation and exposition issues that should be cleaned up.

## Contribution Rating
3: good. The paper offers a useful combination of ideas for sparse-view 3DGS and a potentially interesting robustness metric, though the conceptual novelty is moderate and the metric contribution is not yet fully convincing.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper is solid, relevant, and supported by meaningful experiments, and I can see it being useful to the community. At the same time, the contribution is somewhat incremental, the method leans heavily on external depth priors, and the new IMR metric is promising but not fully nailed down.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with sparse-view NVS / 3DGS literature and checked the main technical formulation carefully, but some implementation-specific details would still benefit from author clarification.