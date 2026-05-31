## Human Reviewer 1

### Summary
To address limited availability of 7T data, this paper proposes a novel method for enhancing resolution and SNR of 3T BOLD fMRI to approximate 7T data quality. It aligns both 3T and 7T data from different subjects and datasets into the same space with shared parameters. By using an unpaired Brain Disk Schrodinger Bridge (BDSB) diffusion model, the spatio-temporal resolution and SNR of 3T data could be enhanced. Experiments were performed on three public fMRI datasets and a synthetic dataset. The proposed method showed comparable results of SNR and the goodness-of-fit of the pRF in the enhanced 3T to 7T data quality.

### Strengths
1) The motivation of the paper is clear and straightforward. Given the scarcity of large-scale paired 3T-7T fMRI datasets, research for unpaired learning frameworks is necessary, and this paper handles this challenge. 

2) The method is validated on both real and synthetic datasets to demonstrate generalizability. Moreover, the results show that the proposed method outperforms GAN-based and diffusion-based approaches across 4 evaluation metrics, including $R^2$, which assesses neuroscientific interpretability.

### Weaknesses
1)	The exact and detailed formula of the regularization terms (PatchNCE and BD-SSIM) is missing. Which distance metrics were used for the regularization losses? It would be helpful to add the formulations in the supplementary material.

2)	It is mentioned that the NCE regularization loss is designed to maintain consistency with the LQ inputs in order to preserve structural details. However, how can you guarantee that this term actually preserves ‘structural ‘ information? Are there any ablation studies regarding this term with qualitative analyses and/or brain regional comparisons that support this claim? In addition, if my understanding is correct, this term reduces the discrepancy between the LQ and generated data. In that case, it seems to potentially conflict with the role of $ L_{Adv}$, which enhances resolution (i.e., the main goal of this paper). How does the proposed method address this issue?

3)	The paper does not include qualitative comparisons and neuroscientific comparisons with baseline models.

### Questions
1)	Given the small data size, how could you handle the overfitting issue in the experiments? Did authors adopt cross-validation and/or perform multiple trainings to validate the generalizability of the methods (including baselines)? 

2)	How were the hyperparameters of baseline models tuned? Could you clarify the tuning strategy and selection criteria?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
This work proposes BDSB, an Schrödinger Bridge application for 3T-to-7T cross-dataset fMRI enhancement. Experiments on synthetic dataset and real-world datasets demonstrated superior performance by BDSB over GANs and DDPM.

### Strengths
1. The paper is clear and well-organized. The way fMRI data fits into the Schrödinger Bridge framework has been clearly described, and readers can learn from it.

2. Performance on synthetic and cross-dataset experiments has shown a promising boost over baselines. While on paired data, the improvement is marginal, BDSB can still hold top-2.

### Weaknesses
1. Notations need a double check, e.g., in Fig 3 caption, shouldn't the approximating distribution $\hat x_{1|t_i}$ be derived from the neural generator $q_\phi$ instead of the joint distribution $p$? Please correct me since I'm not an expert on diffusion models, but I also think it should be the approximated $\hat x_{1|t_j}$ in $p(x_{t_{j+1}}|x_{t_j},x_{1|t_j})$ in Fig 3.

2. The first attempt of learning 3T-7T generation from unpaired data is desirable, but the real-world evaluation should be focused on paired data since the final purpose is generating ground truth 7T fMRI from 3T fMRI. In this regard, BDSB performs similarly to OTT-GAN for PSNR and even worse for SSIM.

3. The contribution of a better fMRI enhancement via learning across datasets has not been evaluated. As mentioned above, there are no experiments of training with unpaired data and testing on paired data. The ability of learning across datasets makes BDSB more fundamental than existing models, and it should lead to a model scaled from multiple datasets. However, the BDSB is trained separately for unpaired and paired experiments.

4. Technical innovation is limited. Why don't other optimal transport methods fit into the proposed framework?

### Questions
1. How's the performance of super-resolution methods on your data?

2. How's cross-session fMRI prediction scientifically sound? There are various compounds affecting the BOLD signal aside from cognition and visual stimuli, such as scanner settings and test-retest variations [2]. How to ensure the model learning from SNR differences rather than other compounds?

[1] Ding, Jiaqi, et al. "Machine Learning on Dynamic Functional Connectivity: Promise, Pitfalls, and Interpretations." arXiv preprint arXiv:2409.11377 (2024).

### Soundness
2

### Presentation
4

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper proposes a method for enhancing 3T blood-oxygenation-level-dependent (BOLD) functional magnetic resonance imaging (fMRI) by leveraging an unpaired Brain disk Schrödinger bridge (BDSB) model. The authors map 3D brain surfaces into a shared parametric domain via conformal mapping and apply an unpaired BDSB diffusion model to approximate the higher resolution of 7T scans using 3T scans. The framework is evaluated across three public datasets, of which one is synthetic, another containing only 3T scans, and a paired 3T/7T dataset. 

Experiments indicate meaningful improvements on the synthetic data and Cross-Dataset Real, while performance is essentially in line with OTT-GAN for the paired TDM Real dataset.

### Strengths
Originality. The fMRI enhancement pipeline consisting of conformal parameterization, brain disk schrödinger bridge and resample & pRG analysis appears novel. The use and application of the Schrödinger Bridge for unpaired samples is also novel in this domain.

Quality. The method is mathematically motivated and the experiments include relevant metrics (SSIM, PSNR, R^2). Evaluation across synthetic, cross-dataset, and paired data provides a reasonable spread of conditions.
	
Significance. Enhancing 3T data using unpaired 7T examples is an important and practically relevant problem. The approach could, in principle, enable higher-quality analyses without costly high-field scans. Additionally, the method performs well on synthetic and cross-dataset real compared to the provided baselines. 

Clarity. The paper is clearly written and well-structured overall. Figures 1–3 effectively illustrate the architecture and training process.

### Weaknesses
- While the method is framed as unpaired learning, the implementation and experiments do not convincingly show that unpaired samples are leveraged for learning. A meaningful test would involve partial or full training on unpaired data and evaluation on paired data to quantify the benefit of the unpaired setup.
- On the TDM Real (paired) dataset, BDSB performs similarly to OTT-GAN, contradicting the claim of superior performance “across all real and synthetic experiments.” This discrepancy should be discussed explicitly.
- Frechet Inception Distance (FID) typically relies on an ImageNet-trained network and is not meaningful for fMRI-like data, whose statistics differ drastically from natural images.
- Related methods are only briefly mentioned in the appendix; a dedicated section would improve context and clarify how baselines are chosen.
- When the authors or the publication are not included in the sentence, the citation should be in parenthesis using \citep{}, as outlined in the formatting instructions.

### Questions
- What do the authors believe explains the discrepancy between performance gains on synthetic/Cross-Dataset Real data and the parity with OTT-GAN on TDM Real?
- Why are results from fast-DDPM missing for the Cross-Dataset Real setting?
- How did the authors decide which baselines to include and which not to include?

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper presents a flow-based approach to synthesize 7T fMRI from the counterpart 3T data. The Schrodinger bridge technique is used to train the model based on the 2D disk of surface projection map. While the idea of leveraging ultra-high-field fMRI for improved spatial modeling is potentially valuable, the current paper lacks methodological rigor, critical validation experiments, and sufficient theoretical justification to establish technical credibility. Strengthening these aspects would substantially improve the impact and trustworthiness of the work.

### Strengths
The paper is technically ambitious (given a limited number of training samples and high dimensional data) and conceptually original, combining **geometric brain mapping, diffusion modeling, and validation** into a cohesive pipeline. These contributions make it a practical solution for enhancing fMRI resolution for neuroscience studies.

### Weaknesses
1) **Main Concerns**. The primary issue with this submission lies in its scientific rigor and validation design. The authors claim that BOLD signals obtained from 7T MRI can be effectively mapped to or synchronized with evolving time series from 3T scanners. However, this assumption is not convincingly supported. It remains highly questionable whether (1) temporal synchronization between 3T and 7T acquisitions can be achieved with sufficient precision, and (2) whether the spatial correspondence of voxel- or surface-level activations can be meaningfully aligned across different field strengths. From a machine learning standpoint, however, the 3T and 7T datasets should ideally be paired or co-registered at the subject level to enable cross-modality learning. Without a clear justification or evidence supporting this assumption, the technical soundness of the proposed framework is undermined.

2) **Projection Method**. The use of 2D conformal mapping to reduce fMRI data complexity is conceptually interesting, yet it raises serious concerns about potential information loss during the projection from high-dimensional cortical surfaces to a 2D representation. This approach may oversimplify the spatial geometry of the brain and distort the topological structure of functional activations. The authors should consider or at least discuss alternative representations, such as spherical harmonics (see the well-established approach by Anderson et al., NeuroImage, 2010), which preserve surface geometry while enabling efficient spectral decomposition.

3) **Replicability and Test-Retest Validation.** Given that this is a neuroimaging study, replicability testing is a crucial standard for evaluating robustness. The current manuscript lacks experiments on test–retest datasets, which are commonly used to assess the reliability of functional signals and model generalization. The authors should include such analyses or provide clear justification for their omission.

4) **Temporal Resolution Limitation**. Finally, the authors should acknowledge the inherent limitation that the proposed method primarily enhances spatial resolution and signal-to-noise ratio (SNR), but does not address the true temporal resolution gap in fMRI. The fundamental challenge remains the coarse temporal sampling (on the order of 1 s) compared to neuronal timescales (milliseconds). The paper would be stronger if it explicitly discussed this limitation and clarified whether the proposed method could, in principle, be extended to improve temporal fidelity.

5) **Limited novelties**. This work is a combination of existing components such as conformal mapping and Schrodinger bridge model.

### Questions
1. The paper projects the cortical surface into a 2D disk before applying the Schrödinger bridge model. How much geometric distortion is introduced by this mapping, and how might it affect spatial correspondence between the 3T and 7T fMRI data?
2. Why was a 2D conformal mapping chosen instead of a spherical or spectral representation (e.g., spherical harmonics)? Would the latter preserve global topology more faithfully?
3. How are the boundary conditions handled in the 2D disk representation, given that cortical manifolds are not naturally disk-like?
4. The model learns a flow between 3T and 7T BOLD signals, but are these data temporally synchronized or spatially paired? Without strict pairing, how can the model distinguish physiological differences from scanner-induced variability?
5. How does the model ensure that synthesized 7T fMRI signals retain biologically meaningful temporal and spectral properties (e.g., frequency content, signal-to-noise ratio)?
6. Although an ablation study is presented (Table 3), it primarily focuses on different surface mapping strategies and regularization terms. Was any ablation performed to isolate the contribution of the Schrödinger bridge formulation itself—e.g., by comparing with a baseline model without the bridge constraint or with a standard flow-based mapping?
7. The model is trained on a small dataset of paired 3T–7T scans. Can it generalize to other sites, scanners, or acquisition protocols?
8. What is the computational cost of solving the Schrödinger bridge compared to simpler flow-based mappings?
9. How would the approach scale to whole-brain volumetric data rather than surface-based 2D projections?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
5