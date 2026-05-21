---
job_id: 962ff725-f6fa-4986-9df0-dacd4fde84aa
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: piylyBPSau.pdf
paper: GENCOGS: Generative Completion-Based 3D Gaussian Splatting for High-Fidelity Few-Shot Novel View Synthesis
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining generative models, 3D Gaussian Splatting, and few-shot novel view synthesis for representation learning in vision.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, method, experiments, quantitative and qualitative results, and conclusion. While I have substantial concerns about rigor, positioning, and clarity, these are review-level issues rather than desk-reject-level omissions or fatal incompleteness.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious reviewer-targeting text, or other signs of prompt injection or manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes GenCoGS, a few-shot novel view synthesis method built on 3D Gaussian Splatting that adds two generative completion components: a generative point cloud completion and filtering pipeline for Gaussian initialization, and a generative pseudo-view completion strategy based on an image-to-video diffusion model for Gaussian optimization. The method is evaluated on LLFF, DTU, and Shiny, with the authors reporting improvements over several prior NeRF-based, 3DGS-based, and diffusion-based baselines under sparse-view settings.

## Strengths
The paper tackles a real pain point in sparse-view 3DGS, namely that existing methods often fail badly in under-observed regions, either by leaving hollows or producing floaters. That motivation is easy to buy, and **Figure 1** does a reasonable job illustrating the two concrete failure modes the paper wants to address, incomplete initialization and artifact-prone pseudo-view supervision.

The overall design is fairly intuitive and modular. The split into GCGI for initialization and GCGO for optimization makes the proposal easy to follow conceptually, and **Figure 2** is helpful in conveying this end-to-end pipeline. In particular, the idea of not just generating complementary points, but then explicitly filtering them before Gaussian initialization, is sensible. Likewise, the effort to constrain pseudo-view guidance via a confidence mask and a consistency loss addresses an obvious concern with generative priors, namely hallucination.

There is some empirical evidence that both components contribute. **Table 4** shows additive gains from GCGI and GCGO on LLFF 3-view, with the full model improving over the baseline in all reported metrics. **Table 6** is also useful because it separates the point generation and point filtering components; the fact that CPF improves over CPG-alone is consistent with the paper’s central claim that naive completion introduces harmful outliers. I appreciated that the paper did not stop at a single “full vs. baseline” comparison.

The qualitative examples are directionally aligned with the claimed behavior. In **Figure 3**, the complete point cloud after filtering appears cleaner than the naive merged cloud, which supports the motivation for CPF. In **Figure 6**, the proposed method appears to recover some missing structure more cleanly than the compared methods in the highlighted regions. The ablation visualization in **Figure 7** also supports the claim that the two modules address somewhat different failure modes.

The paper is also reasonably broad in evaluation across scene types, at least within the chosen benchmarks. The reported results in **Tables 1, 2, and 3** are consistently strong, especially on DTU and Shiny, where the margins are non-trivial.

## Weaknesses
I have several concerns, and taken together they keep this below the bar for me.

1. **The technical novelty is narrower than the paper claims, and the positioning against prior art is not convincing enough.**  
   The paper repeatedly frames the method as a unified generative completion framework for 3DGS few-shot NVS, but in substance it is a combination of known ingredients: point cloud completion, point filtering, pseudo-view supervision, diffusion-based completion, and consistency regularization. The specific combination may be useful, but the manuscript oversells the originality. For example, the claims in the introduction on **Pages 1-2** and the contribution bullets suggest a major conceptual shift, while the actual method is much closer to an engineering integration of existing families of ideas. The related work in **Section 2** discusses diffusion-guided NVS and few-shot 3DGS, but the manuscript does not sharply articulate what is genuinely new algorithmically beyond putting completion on both the initialization and optimization stages. That matters because for ICLR, good performance alone is usually not enough if the methodological step is incremental and the paper does not clearly isolate the new principle.

2. **The mathematical exposition has multiple places where the notation is incorrect, ambiguous, or underspecified, and some equations are simply not well formed.**  
   This is not cosmetic, because the paper’s core contributions rely on these formulations.
   - In **Equation (5)** on Page 4, the expression  
     \[
     p_{i,k} = k - \min_{p \in (\mathbf{P}_0 \cap t_i)} \|p_i' - p\|
     \]
     is not a valid definition of the \(k\)-nearest reference points. It appears to confuse an index, an operator, and a distance value. The text says the module samples \(k=3\) nearest points \(\{p_{i,1},\dots,p_{i,k}\}\), but the equation defines neither the set nor the selection rule correctly. This is a central step in CPF, so this needs to be rewritten precisely, for example as a nearest-neighbor set selection operator.
   - In **Equation (6)**, the summation index is reused as \(i\), which conflicts with the outer point index \(p_i'\). This makes the formula ambiguous. The intended form is probably something like
     \[
     y_i = \frac{1}{k}\sum_{j=1}^{k}\|p_i' - p_{i,j}\|.
     \]
   - In **Equation (7)**, \(\mu(\mathbf{P}_0)\) is defined as the mean pairwise distance over the full sparse cloud, which is a very global statistic for thresholding local outliers. This choice is plausible as a heuristic, but the paper provides no justification for why a global mean pairwise distance should be the right scaling for local completion outlier detection across scenes of very different density and scale.
   - In **Equation (16)**, \(\mathcal{L}_{reg}\) is written as an \(L_1\) difference multiplied by a mask,
     \[
     \|I_p - \hat I_p\|_1 \odot \hat M_r,
     \]
     but the paper does not specify whether this is summed, averaged over masked pixels, normalized by mask area, or left as a map. This matters because the magnitude of this loss depends strongly on the size of the mask.
   - **Equations (18)-(20)** are also conceptually muddy. \(\mathcal{L}_{GC}\) is defined using \(I_p\) and \(\hat I_p\), where \(I_p\) is called the “initial pseudo view” and \(\hat I_p\) is the complete pseudo view. But in **Section 3.2.3**, the training loss for Gaussian optimization is then given using \(\mathcal{L}_{img}\) and \(\mathcal{L}_{GC}\) without clearly stating whether \(I_p\) is a rendered view from current Gaussians, an interpolated pseudo-render, or something generated independently from the 3DGS. Right now the supervision loop is underspecified.
   
   In short, the math needs a real cleanup. I do not think the current version is precise enough for a method paper centered on these modules.

3. **The GCGO formulation relies on fairly strong assumptions about consistency that are asserted rather than demonstrated.**  
   In **Section 3.2**, the paper suggests that CLIP-derived conditioning and an image-to-video diffusion model can generate “complete pseudo views” with useful multi-view consistency. But temporal consistency in an I2V model is not the same thing as geometric or cross-view consistency for 3D reconstruction. The manuscript acknowledges hallucination, yet still treats these generated pseudo views as reliable optimization signals after masking and LPIPS-based regularization. What is missing is evidence that the generated pseudo-views are geometrically aligned enough to improve 3DGS rather than just acting as an image prior. This is important because the entire second half of the method rests on using a 2D generative model as a 3D supervision source. The current paper gives empirical gains, but it does not convincingly explain why this supervision should be trusted or under what conditions it fails.

4. **The experimental baseline set is not strong enough for the claims being made, especially on the 3DGS few-shot side.**  
   The paper compares with FSGS, DNGaussian, BinoGS, IPSM, CAT3D, etc., which is a decent start, but the claim of state-of-the-art performance in few-shot 3DGS is stronger than the evidence provided in the main paper. Several very relevant recent sparse-view 3DGS approaches are not discussed or compared. This weakens the novelty and significance claims, because the reader cannot tell whether the gain is over the actual frontier or over a selective subset. For a paper that positions itself as a new top-performing few-shot 3DGS framework, stronger coverage of contemporary baselines is not optional.

5. **The comparison protocol raises fairness questions because the method leverages substantial external generative priors, while some baselines do not.**  
   The method uses a pretrained I2V diffusion model and CLIP features in GCGO, but the comparisons in **Tables 1-3** mix together methods with very different levels of pretrained external knowledge. That is not inherently unfair, but then the paper should explicitly discuss this axis. Otherwise, the comparison risks conflating “better sparse-view reconstruction algorithm” with “more powerful external generative prior.” This matters scientifically because the claimed contribution is about few-shot NVS quality, yet the gains may partly come from injecting a strong pretrained visual prior rather than from the 3DGS machinery per se.

6. **The quantitative evidence is encouraging but still too thin to fully support the stronger claims about mechanism.**  
   The main gains in **Table 1** on LLFF are modest relative to the best competing method. For example, compared with BinoGS, the improvements are real but not dramatic, and on LPIPS at 9 views the methods are tied at 0.090. The paper claims strong superiority, but the LLFF margins look more like competitive improvements than a decisive step. On DTU in **Table 2**, the gains are much larger, which is promising, but there is little analysis of *why* the method helps more there than on LLFF. That missing analysis matters, because it could reveal where the method is actually effective, object-centric scenes, forward-facing scenes, shiny surfaces, or only some subset.

7. **The ablations are useful but not deep enough to validate the core design choices.**  
   **Table 5** studies random sampling vs. camera trajectory plus \(\mathcal{L}_{GC}\), but it does not disentangle the contribution of the I2V completion model itself from the camera perturbation or the loss. Likewise, **Table 6** validates CPG and CPF, but it does not compare against simpler non-generative alternatives for densifying the initialization, such as local geometric interpolation or depth-based expansion. If the paper wants to argue that generative completion is the right solution, then comparisons against simpler completion or regularization heuristics are needed. Right now the ablations mostly show that the proposed modules help relative to an internal baseline, not that the proposed design is the most justified one.

8. **Some visual evidence is less conclusive than the text suggests.**  
   **Figure 5** compares against only BinoGS on DTU, and **Figure 6** compares against DNGaussian, BinoGS, and ViewCrafter, but the figure layout and crop choices make it hard to judge whether the improvements are structural or mostly texture-level. In particular, the highlighted regions support the claim of fewer artifacts, but they do not establish that the recovered unseen geometry is actually correct. This is the central issue for a completion-based method. The figures are consistent with improved perceptual quality, but they do not fully validate the claimed “accurate and coherent scene completion.”

9. **Some claimed robustness/generalization conclusions are overstated relative to the presented evidence.**  
   In **Page 9**, the paper says **Table 6** demonstrates “strong generalization capability and robustness” of GCGI because performance still improves when only a quarter of \(\mathbf{P}_0\) is used. That is too strong. This is a single synthetic degradation experiment on one dataset/setting, not a broad robustness study across scene types or noise conditions. Similar overstatement appears in the broader conclusion language.

10. **Presentation quality is uneven, with several wording and naming inconsistencies that make the method harder to parse than necessary.**  
   One example is in **Section 3.2**, where the text calls GCGO “Generative point cloud Completion-based Gaussian Optimization,” which is clearly inconsistent with the actual pseudo-view-based optimization module. There are also repeated grammar issues, awkward phrasing, and notation reuse. These may sound minor, but when combined with the equation issues above, they materially reduce confidence that the method is specified precisely enough to be reproduced from the main paper alone.

11. **There is limited discussion of compute cost versus benefit in the main paper.**  
   The limitation section in the appendix admits extra overhead, and **Table 10** shows training time increasing from 30 minutes for BinoGS to 40 minutes for GenCoGS, with memory also increasing. That overhead is not enormous, but the main paper does not discuss whether the gain justifies the added complexity, pretrained dependencies, and implementation burden. For a method that already relies on a large generative prior, this trade-off deserves a clearer discussion in the main text.

## Questions
1. Please precisely define the supervision loop in GCGO. In **Equations (18)-(20)**, what exactly are \(I_p\) and \(\hat I_p\) during optimization? Is \(I_p\) a rendered image from the current Gaussians at a pseudo pose, an interpolated pseudo-view from observed frames, or an input frame to the diffusion model? A clean algorithmic description would substantially increase confidence.

2. Please correct and clarify **Equation (5)** and the full CPF procedure. How are the \(k\)-nearest anchors selected exactly, and is the thresholding based on local density or only the global mean pairwise distance \(\mu(\mathbf{P}_0)\)? If you have stronger intuition or derivation for this threshold, that would help.

3. Can the authors provide stronger evidence that the I2V-generated pseudo views are geometrically useful rather than merely visually plausible? For example, any measurement of cross-view consistency, re-projection consistency, or pose-conditioned alignment would strengthen the central claim behind GCGO.

4. Why does the method help much more on DTU than on LLFF, judging from **Tables 1 and 2**? Is the method particularly suited to object-centric scenes, or scenes with larger unobserved regions, or scenes where generative priors better match the data distribution?

5. Can the authors compare against more recent sparse-view 3DGS baselines and/or simpler non-generative alternatives for the two modules? In particular, I would like to know whether the gains come from the specific generative-completion design or from adding almost any stronger prior at initialization and optimization.

6. For **Equation (16)**, how is the masked loss normalized? If it is not normalized by the number of active pixels, how is training stability preserved across samples with very different mask sizes?

7. **Figure 8** and the corresponding discussion suggest a trade-off between exploration and hallucination through the perturbation amplitude \(A\). Could the authors quantify this more directly, for example by reporting the fraction of masked pixels or an inconsistency score as \(A\) changes, rather than only final rendering metrics?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper itself. The work uses standard benchmark datasets and focuses on scene reconstruction quality. My concerns are scientific rather than ethical.

## Soundness Rating
2: fair. The empirical results are promising, but the technical specification has important ambiguities, especially around the CPF equations and the GCGO supervision loop, and several central claims are supported more by intuition than by rigorous validation.

## Presentation Rating
2: fair. The overall structure is understandable and the figures help, but the paper has enough notation issues, naming inconsistencies, and underspecified equations that clarity is meaningfully affected.

## Contribution Rating
2: fair. The paper addresses an important problem and combines reasonable ideas in a useful way, but the conceptual advance over prior sparse-view 3DGS and diffusion-guided methods feels moderate, and the experimental positioning is not yet strong enough for a higher score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper is promising and attacks a real problem with a sensible two-stage design, and the empirical results are better than I expected in some settings, especially DTU. Still, the current version has too many issues in technical precision, positioning, and experimental justification for me to support acceptance at ICLR. With a cleaner formulation, stronger baseline coverage, and more direct validation of the pseudo-view consistency assumptions, this could become a much stronger submission.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The topic is within my area, I checked the main equations and experiments carefully, and my main uncertainty is not about what the paper does, but about whether some missing clarifications could partially resolve the specification issues.