---
job_id: 0c3dcaea-dff3-4e76-b218-c6f5deb4e525
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: DB2KJKFX0d.pdf
paper: BDSB: Brain Disk Schrödinger Bridge for Enhancing 3T BOLD fMRI Using Unpaired 7T Data for Visual Retinotopic Decoding
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a generative-modeling and geometry-aware learning method for neuroscience data, combining unpaired image translation, Schrödinger Bridge diffusion, and cortical surface parameterization for an fMRI enhancement task.

## Minimum Quality
Pass ✅. The paper includes the necessary components, abstract, introduction, methodology, experiments/results, and conclusion/discussion, and it presents a coherent empirical study. There are, however, notable concerns about technical justification, mathematical precision, and evaluation rigor, but these do not rise to desk-reject level.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to reviewers, or other manipulative content in the provided manuscript text and figures.

# Expected Review Outcome:
## Summary
This paper proposes BDSB, a pipeline for enhancing low-quality 3T BOLD fMRI using unpaired 7T data for retinotopic decoding. The method first maps cortical ROI surfaces to a shared 2D brain-disk domain via conformal parameterization, then applies an unpaired Schrödinger Bridge style generative model to translate 3T brain disks toward the 7T distribution, and finally resamples the enhanced signals back to the cortical surface for downstream pRF analysis. The paper evaluates the approach on a synthetic setting derived from NSD, a cross-dataset real setting using NOD to NSD, and a small paired 3T/7T TDM setting.

## Strengths
1. The paper tackles a meaningful and difficult problem. Enhancing low-field fMRI for downstream retinotopic analysis is practically important, and the focus on functional utility rather than just image-level similarity is a good choice.

2. The overall pipeline is reasonably creative. Combining cortical surface flattening into a shared disk parameterization with an unpaired Schrödinger Bridge style model is an interesting design, especially for handling the lack of paired 3T/7T acquisitions.

3. I appreciated that the paper evaluates not only synthetic data but also two real-data settings with different supervision regimes. The synthetic experiment gives a controlled test bed, while the TDM experiment at least partially checks whether the method transfers to genuinely paired 3T/7T data.

4. The qualitative visualizations are useful. In **Figure 2**, the disk parameterization process is explained clearly enough to understand how 3D cortical vertices become 2D training samples, and this helps motivate why a common domain is needed for cross-subject and cross-dataset learning. Likewise, **Figure 4** gives a direct visual sense that the proposed outputs are sharper and closer to the HQ target than the down-sampled inputs, at least in the synthetic setting.

5. The downstream pRF evaluation is a better-than-usual choice for this type of medical image translation paper. The inclusion of pRF goodness-of-fit as a functional metric is a real strength, because it pushes the paper beyond generic enhancement claims.

6. **Table 2** shows consistent gains for the proposed method over the listed baselines on the synthetic setting, especially in SSIM, PSNR, FID, and the reported average \(R^2\). Even though I have reservations about how much to trust these numbers scientifically, the table does suggest that the approach is doing something nontrivial rather than collapsing to a cosmetic sharpening effect.

7. The ablation in **Table 3** is directionally useful. It suggests that the cortical mapping choice matters substantially, and it also indicates that the added regularization terms affect different metrics differently, which is valuable for understanding the pipeline.

## Weaknesses
1. **The central scientific claim, “making 3T comparable to 7T quality,” is stated too strongly relative to the evidence presented.**  
   The abstract and conclusion repeatedly frame the method as making enhanced 3T data “comparable to 7T quality,” but the main evidence is limited. In the synthetic setting of **Table 2**, the method improves against degraded NSD inputs, but that is not the same as demonstrating equivalence to true 7T acquisitions. In the cross-dataset real setting, there is no subject-matched ground truth at all, so the evidence is indirect. In the TDM setting, which is the most relevant real paired evaluation, the gains over strong baselines are much smaller: the proposed method reaches PSNR 19.24 vs 19.18 for OTT-GAN and SSIM 0.718 vs 0.727 for OTT-GAN in **Table 2**. That is not the profile of a result that justifies broad claims of closing the 3T-to-7T gap. This matters because the paper’s headline message is much stronger than what the paired-data evidence actually supports.

2. **The empirical comparison is not as convincing as the narrative suggests, especially on the only paired real setting.**  
   The paper states on Pages 6 to 9 that the proposed pipeline “achieves the best performance” and “significantly” enhances LQ fMRI across all experiments, but **Table 2** is more mixed than the text admits. On TDM Real, the proposed method is best on PSNR and FID, but not on SSIM, where OTT-GAN is slightly better. More importantly, the margins are small enough that statistical uncertainty should be reported, especially with only two subjects and a run split. The paper gives no confidence intervals or significance tests in the main paper. Since TDM is the only real paired 3T/7T experiment, these small margins matter a lot. Without uncertainty estimates, it is hard to know whether the improvements are robust or within noise.

3. **There are important methodological confounds in the cross-dataset real experiment, which make attribution difficult.**  
   In Section 2.1, the real unpaired experiment maps NOD 3T data to the NSD 7T distribution. But this comparison entangles field strength, scanner differences, acquisition protocol, stimulus details, preprocessing pipelines, subject population, and dataset-specific idiosyncrasies. The paper acknowledges the absence of paired data, but the main claims still implicitly attribute learned differences to 3T versus 7T quality. That is too optimistic. The method may simply learn the NSD style in the shared disk domain. **Figure 6** is visually appealing, but it cannot resolve this confound, because there is no ground-truth 7T target for the NOD subject. This matters scientifically, because the paper positions itself as field-strength enhancement rather than cross-dataset domain stylization.

4. **The mathematical exposition around the Schrödinger Bridge objective is too loose, and some equations are underspecified or not fully consistent with the training description.**  
   In **Equation (1)**, the notation \(T_{t_a}\) and \(T_{t_b}\) is used as if these are marginal distributions, but earlier \(T^\star\) denotes a stochastic process. The distinction between process, path measure, and marginals is not handled carefully. In **Equation (3)**, the loss is written as  
   \[
   \mathbb{L}_{\mathrm{SB}}(\phi,t_i)=\mathbb{E}_{q_\phi(x_{t_i},x_1)}\|x_{t_i}-x_1\|^2-2\tau(1-t_i)H(q_\phi(x_{t_i},x_1)),
   \]
   subject to \(D_{\mathrm{KL}}(q_\phi(x_1)\|p(x_1))=0\). But the paper never explains how the entropy term \(H(q_\phi(\cdot))\) is computed or estimated for a neural conditional generator, nor how the KL constraint is operationalized in practice beyond saying there is an adversarial loss. Replacing an exact distributional constraint with a GAN objective is a major step, and the text glosses over it. **Equation (4)** then claims that solving the Lagrangian yields \(q_\phi(x_1\mid x_{t_i})=p(x_1\mid x_{t_i})\), which is much too strong without assumptions about model capacity, optimization, and discriminator optimality. This is not just a theoretical nicety, it affects whether the method is truly an SB approximation or mainly a GAN with SB-inspired interpolation.

5. **The bridge dynamics and sampling procedure are not specified precisely enough to reproduce or validate the claimed Markov trajectory.**  
   Section 2.3 says the joint distribution \(p(x_1,x_{t_i})\) is iteratively approximated using **Equation (2)** under the Markov assumption, and **Figure 3** sketches a recursive generation process. But the exact training-time and test-time sampling steps are not clearly defined in the main paper. For example: how is \(x_{t_i}\) sampled during training, is it sampled from the Gaussian bridge using a real \(x_1\), a generated \(\hat{x}_1\), or both? When they say the generator “can be directly utilized to sample the next BD \(x_{t_{i+1}}\),” what is the actual update rule, since the generator predicts \(x_1\mid x_{t_i}\), not \(x_{t_{i+1}}\mid x_{t_i}\)? If \(x_{t_{i+1}}\) is generated via **Equation (2)**, then one needs the paired endpoints \((x_{t_i},x_1)\); but in the unpaired setting \(x_1\) is itself sampled through the model. These details are essential for understanding whether the method is coherent and what is optimized at each step.

6. **The regularization term using brain-disk structure is conceptually interesting but mathematically vague.**  
   In **Equation (5)**, the BD-SSIM term is introduced as a structural regularizer between generated BDs and the fsaverage BD structure \(x'\). But the main paper does not define what \(x'\) numerically contains, how SSIM is computed between a signal image and a “structure-only” disk, what channels are used, or why SSIM is the right functional for geometry preservation in this setting. The appendix says \(x'\) is a BD without fMRI values, encoding cortical geometry, but this still leaves open how a structural template image supervises a functional signal image. This matters because the paper claims that baseline methods distort structure while BDSB preserves it, and a lot of that claim rests on this regularizer. Right now, it reads more like an intuition than a properly specified objective.

7. **The pRF formulation contains notation issues that undermine confidence in the technical care.**  
   In **Equation (7)**, the objective is written as
   \[
   (\mathbf{c}_v,\sigma_v)=\arg\min_{\mathbf{c}_v,\sigma_v}\sum_{l\in[1,L]}\|\hat{y}_v(\mathbf{v},\sigma,l)-y_v(l)\|^2,
   \]
   which appears inconsistent with **Equation (6)**, where the predicted signal depends on \((\mathbf{c}_v,\sigma_v,l)\), not \((\mathbf{v},\sigma,l)\). This looks like a typo, but it is not isolated. There are several places where symbols drift or are overloaded. For a paper whose claimed contribution is methodological, these slips matter because they make it harder to tell which parts are informal exposition and which parts are exact definitions.

8. **The evaluation protocol around FID is not well justified for this data type.**  
   The cross-dataset real experiment relies heavily on FID because no paired target is available, as stated on Page 3 and in **Table 2**. But the paper never explains what feature extractor is used for FID, whether it is pretrained on natural images or domain-specific brain-disk images, and why that representation is meaningful for fMRI signal quality. Brain disks are not natural photographs, and FID can be highly misleading outside the feature space it was designed for. Since FID is one of the main quantitative supports for the real unpaired experiment, this omission weakens the claim substantially.

9. **The baselines are not obviously the right ones for the scientific question, and the comparison set is incomplete.**  
   Most baselines are generic 2D unpaired translation models applied after the authors’ own brain-disk parameterization. That is a reasonable engineering comparison, but it does not isolate whether the gains come from the SB model, from the conformal mapping, or from task-specific structural regularization. **Table 3** partially addresses this, but only on synthetic data and not with stronger non-generative alternatives tailored to retinotopic enhancement or registration-based refinement. If the central claim is about improving retinotopic decoding, comparisons against methods designed for retinotopic map refinement or geometry-aware registration would be more scientifically informative than yet another CycleGAN-family baseline.

10. **The presentation overstates what qualitative figures can prove.**  
    **Figure 4** does show visually sharper enhanced disks, but sharper is not necessarily more faithful, especially for functional signals. **Figure 5** is based on one high-\(R^2\) and one low-\(R^2\) vertex, which is anecdotal. **Figure 7(b)** shows tighter receptive-center scatter after enhancement, but since the enhancement model is itself trained to map toward a smoother HQ distribution, reduced variability is not automatically evidence of improved biological fidelity; it may also reflect oversmoothing or regularization-induced shrinkage. These figures are useful, but the text interprets them in a one-sided way.

11. **The dataset split and sample accounting are a bit confusing in the main text, which weakens confidence in reproducibility.**  
    In **Table 1**, the subject notation has inconsistencies, for example “s7, s9” for NSD test in the synthetic setting and “s9 ~ s9” for NOD test in cross-dataset real, which looks like a typo. Given the already small number of subjects and the importance of train/test separation in this paper, these bookkeeping issues should have been cleaned up carefully.

12. **The paper’s novelty claim is somewhat overstated relative to prior work cited by the authors themselves.**  
    The contribution statement says this is “the first approach to improve fMRI SNR and retinotopic map quality using unpaired learning across public datasets.” Even if that exact combination may be new, the paper is substantially an application-specific adaptation of existing ingredients: conformal cortical flattening from prior retinotopy work, unpaired image translation on 2D disks, and Neural Schrödinger Bridge style training borrowed from recent medical imaging papers. I do see some originality in the integration, but the framing should be toned down.

## Questions
1. The most important question for me is about the actual bridge training and inference procedure in Section 2.3. Please describe explicitly, step by step, how \(x_{t_i}\), \(x_1\), and \(x_{t_{i+1}}\) are sampled during training and testing, and how **Equation (2)** is used when the setting is unpaired. A concrete algorithm in the main paper would materially increase my confidence.

2. How exactly is the entropy term in **Equation (3)** computed or approximated, and what is the precise relationship between the “adversarial loss” and the KL constraint \(D_{\mathrm{KL}}(q_\phi(x_1)\|p(x_1))=0\)? Right now this jump is too hand-wavy. Please clarify whether the training objective is a principled SB estimator or an SB-motivated heuristic.

3. For the cross-dataset real experiment, can the authors provide stronger evidence that the model is not simply translating NOD subjects toward the stylistic statistics of NSD, rather than specifically enhancing 3T toward 7T? For example, comparisons against within-dataset controls or analyses disentangling field strength from dataset identity would help.

4. Please report uncertainty estimates in the main paper, especially for **Table 2** on TDM Real. With only two paired subjects, small differences versus OTT-GAN are not very convincing without variance estimates or subject-wise breakdowns.

5. Please clarify the FID computation for brain disks. What feature extractor is used, how is it trained, and why should that feature space be meaningful for fMRI enhancement quality?

6. Can the authors define BD-SSIM mathematically in the main paper? I would like to see a precise expression of the structural image \(x'\), how SSIM is computed, and why this quantity preserves anatomical fidelity after back-projection to the cortical mesh.

7. It would help to add a stronger ablation disentangling: (i) conformal disk mapping only, (ii) mapping plus generic unpaired translation, (iii) mapping plus SB, and (iv) mapping plus SB plus each regularizer, ideally on both synthetic and TDM. That would make it much easier to tell which piece drives the downstream \(R^2\) improvements.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper uses publicly available, de-identified neuroimaging datasets, so there is no immediate red flag regarding data collection. However, the work is still in a sensitive application domain involving brain data. The main concern is not misconduct, but overclaiming utility for neuroscience or clinical use before the evidence is strong enough. The conclusion and future work sections suggest broad applicability to clinical and low-field settings. Given that the method is generative and partly unpaired, there is a real risk that users may treat enhanced signals as more faithful than they are, especially in downstream scientific or clinical interpretation. I do not see an ethics violation that should block review, but I do think the paper should be careful to frame outputs as model-based reconstructions rather than recovered ground truth.

## Soundness Rating
2: fair. The core idea is plausible and the experiments are nontrivial, but important parts of the mathematical formulation and evaluation are underspecified, and the evidence does not fully support some of the paper’s stronger claims.

## Presentation Rating
3: good. The paper is generally readable, the motivation is clear, and the figures help. That said, the mathematical exposition and some notation are sloppier than they should be, and several claims are overstated relative to the data.

## Contribution Rating
2: fair. The integration of cortical parameterization and SB-style unpaired enhancement is interesting, but the contribution is held back by limited validation on real paired data, confounded cross-dataset evaluation, and incomplete methodological justification.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The problem is important and the pipeline is interesting, but I do not think the current submission clears the bar for ICLR main track. The strongest issue is not that the method is obviously ineffective, it is that the paper overstates what has been established. The paired real-data evidence is limited and only modestly better than strong baselines, the cross-dataset setup is heavily confounded, and the SB formulation is not presented with enough rigor for the claims made. With a cleaner technical presentation and stronger validation, especially around the only paired real setting, this could become a stronger paper.

## Reviewer Confidence
4: confident. I am confident in the overall assessment, though not absolutely certain. The topic is within my area, I checked the main equations and experimental claims carefully, and my uncertainty is mostly about missing implementation details rather than misunderstanding the paper.