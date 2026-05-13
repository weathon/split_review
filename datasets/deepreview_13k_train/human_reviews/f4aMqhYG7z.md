# Addressing domain shift with diffusion-based adaptation for real image dehazing

- Decision: Reject
- Scores: 6, 5, 6, 6, 5

## Abstract
Conventional supervised single-image dehazing methods, which are trained with substantial synthetic hazy-clean image pairs, have achieved promising performance. However, they often fail to tackle out-of-distribution hazy images, due to the domain shift between source and target scenarios (e.g., between indoor and outdoor, between synthetic and real). In this work, we observe the opportunity for improving such dehazing models' generalization ability without modifying the architectures or weights of conventional models by adopting the diffusion model to transfer the distribution of input images from target domain to source domain. Specifically, we train a denoising diffusion probabilistic model (DDPM) with source hazy images to capture prior probability distribution of the source domain. Then, during the test-time the obtained DDPM can adapt target hazy inputs to source domain in the reverse process from the perspective of conditional generation. The adapted inputs are fed into a certain state-of-the-art (SOTA) dehazing model pre-trained on source domain to predict the haze-free outputs. Note that, the whole proposed pipeline, termed \textbf{Diff}usion-based \textbf{AD}aptation (DiffAD), is model-agnostic and plug-and-play. Besides, to enhance the efficiency in real image dehazing, we further employ the predicted haze-free outputs as the pseudo labels to fine-tune the underlying model. Extensive experimental results demonstrate that our DiffAD is effective, achieving superior performance against SOTA dehazing methods in domain-shift scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the domain shift issue in single-image dehazing, highlighting the limitations of traditional supervised methods that rely heavily on synthetic data. The authors propose an approach utilizing DDPM to align the input image distributions of the target and source domains. By training the DDPM on haze images from the source domain, the authors can convert target domain images to a format compatible with a pre-trained state-of-the-art dehazing model during testing. Additionally, the authors employ pseudo-labeling to fine-tune the base model, further improving its efficiency.  Finally,  experimental results show that the proposed method outperforms existing dehazing techniques under domain shift conditions in real-world scenes.

### Strengths
1. DiffAD adopts an input adaptive approach, which can better utilize the existing dehazing prior knowledge in the source domain without the need to retrain the model. Besides, it introduces an adjustable quality loss function, which allows users to adjust the dehazing and color-balancing effects as needed.
2. DiffAD also provides a method to generate high-quality pseudo-labels to improve the generalization ability of the model, experiments verify the effectiveness of the proposed method in real-world image dehazing.

### Weaknesses
1. The proposed method requires training a denoising diffusion probability model as well as a state-of-the-art dehazing model, which makes the whole method very complex. Specifically, the diffusion model training adds a significant computational overhead, and the need for a separate pre-trained dehazing model introduces a dependency on existing models, potentially limiting flexibility and increasing the overall complexity of the pipeline.
2. The datasets used in this method are all synthetic or limited datasets, which may lead to poor performance in dealing with real-world dehazing tasks. The reliance on synthetic data for training the diffusion model and the dehazing model raises concerns about the generalization capability of the proposed method to real-world scenarios, where the distribution of haze and image characteristics can be significantly different. Therefore, authors need to provide more results on other datasets with greater diversity and complexity.
3.  The authors only provide non-reference metrics to evaluate the performance, however, MOS-based metrics should be provided in the paper, since non-reference metrics can not fully reveal the human preference. The absence of subjective evaluation metrics like MOS scores makes it difficult to assess the perceptual quality of the dehazed images and how well they align with human visual perception, which is crucial for real-world applications.
4.  Since the proposed method seems to be effective in real-world image dehazing, can it be extended to other tasks, such as real image super-resolution or real-world image denoising?

### Questions
Please see above weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes to tackle out-of-distribution hazy images through projecting to the source domain with diffusion model trained on source data, and then post-processed with existing dehazing model. Additionally, various loss functions are crafted for fidelity and quality. Experiments show the effectiveness of the proposed method.

### Strengths
1. This paper proposes to handle out-of-distribution hazy image with diffusion bridge to source domain.
2. Various loss functions are crafted for fidelity and quality.
3. Experiments show the Effectiveness of the proposed method.

### Weaknesses
1. Addressing the domain shift with diffusion bridge has been widely explored in literature, such as [DDBM, ICLR2024; Diffusion Schrödinger Bridge, NeurIPS2023], therefore, the contribution of this paper that projecting the out-of-distribution hazy images to source domain is somewhat less.
2. The loss functions are heavily handcrafted and yield lots of hyper-parameters, and basically build upon existing loss functions, such as grey-world-assumption loss, dcp loss, etc., which is somewhat less informative. The color consistency loss, while novel, appears to be a workaround for potential failures of MSE in the diffusion process, rather than a fundamental contribution. The white balance loss, a revision of existing color constancy, and the region-aware DCP loss, a modification of standard DCP, lack substantial novelty. The overall approach feels like a collection of existing techniques with minor adjustments.
3. It is recommended to show the captured source distribution in the trained diffusion model for verification. Additionally, according to sec. 5.1, the diffusion model is only trained for 50k iterations from scratch, is this enough for diffusion model to learn the source distribution. Some generated source domain hazy image should be presented and compared with original source image.

### Questions
1. It is unclear when to add the proposed loss functions, are there added in test time as existing zero-shot inverse problem solver, or added in the training time.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces Diffusion-based Adaptation (DiffAD), a method designed to address out-of-distribution haze images without altering the architecture or weights of traditional dehazing models. DiffAD leverages a denoising diffusion model (DDPM) to transform the distribution of input images from the target domain to the source domain. Specifically, the DDPM is trained on source haze images, and during test-time, target haze inputs are adapted to resemble source images using the reverse diffusion process. Additionally, the method refines the model using pseudo labels derived from its predictions.

### Strengths
1. The motivation of addressing the domain gaps is meaningful. 
2. The structure of the paper is clear and well-organized.
3. The proposed method achieves state-of-the-art performance on multiple datasets.

### Weaknesses
1. The experimental results are not particularly impressive. For example, the provided qualitative results only demonstrate sparse fog.

2. Some ablation studies are missing. Specifically, the effectiveness of the fidelity loss and quality loss should be discussed.

3. The proposed framework seems idealized. However, depth estimation and pseudo labels may be inaccurate. How does the proposed method address real-world fog when depth estimation and pseudo labels are unreliable?

### Questions
1. It would be beneficial to include ablation studies to evaluate the impact of the fidelity loss and quality loss.
2. In Section 4.2, depth estimation is applied to both the predicted images (J*) and real hazy images. However, the performance may degrade if the input images are not fully clear. How do you ensure the robustness of this approach?
3. In Section 4.2 (lines 349-354), why is the artifact-free pseudo label obtained using output J*? If the dehazing model is diffusion-based, there is a risk of artifacts appearing in J*. Could you clarify this?
4. The provided qualitative results seem to lack cases with dense fog. Could you include examples with denser fog conditions, both synthetic and real-world?
5. Did you use the same parameters for both synthetic and real-world evaluations?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a diffusion-based domain adaptation method aimed at enhancing image dehazing. It utilizes a pre-trained denoising diffusion probabilistic model to transform hazy images from the target domain into the source domain, where existing dehazing methods are trained and thus demonstrate superior performance. This approach not only improves the performance of previous dehazing techniques in real-world scenarios but also outperforms other real-world dehazing methods across various datasets.

### Strengths
The method demonstrates several strengths:

1. This approach effectively enhances the performance of previous dehazing techniques in both synthetic and real-world scenarios.

2. The work surpasses other real-world dehazing methods across various datasets.

3. The concept of diffusion-based domain adaptation for dehazing is novel.

### Weaknesses
1. The citation format in the manuscript should be revised. For example, "ill-posed problem Wu et al. (2021); Chen et al. (2024a)" should be formatted as "ill-posed problem (Wu et al., 2021; Chen et al., 2024a)."

2. The contributions of the work may be considered minor. The research builds on existing approaches, including controllable diffusion processes, DCP loss, and spatial consistency loss. The direct application and combination of these works suggest a lack of significant contributions. However, in my personal opinion, the idea of utilizing diffusion-based domain adaptation to enhance dehazing is both intuitive and impressive.

3. The direct masked addition between two dehazed images in Figure 5 may lead to inconsistencies. Additionally, the sky and depth masks operate within different value ranges, making their direct addition insufficient in detail.

4. The manuscript presents only a limited number of visual comparisons. It would be beneficial to include more visual results in the blank space on Page 10, potentially with additional figures in the appendix.

5. The title "ADDRESSING DOMAIN SHIFT" may be considered an overstatement, as several unresolved problems remain, and not all cases have been evaluated and compared.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a Diffusion-based Adaptation pipeline to solve the domain shift problem in image dehazing. The main contribution of this paper is to use conditional generation to ensure that no structural deformation and color distortion are introduced in the generated images. Another contribution is the use of multiple losses to ensure the fidelity and quality of the generated images.

### Strengths
This paper is well organized. The topic of the paper is very good. How to use synthetic data to improve the performance on real-world hazy images should be the research trend in the field of image dehazing in the future.

### Weaknesses
1. Using models trained on indoor datasets to handle outdoor scenes does not seem to be the focus of this paper. I think the biggest use of DiffAD is to improve the performance of models trained on synthetic hazy-clean image pairs when used to process real-world hazy images.
2. The problem with the dataset selected for the Haze Type Adaptation (between synthetic and real) experiment. The I-Haze and O-Haze datasets are haze generated using a professional haze generator and are not real-world hazy images in nature.
3. As shown in Table 2, the PSNR after using DiffAD is improved, but still very low. How does the dehazed result look like? This paper lacks qualitative results of this experiment.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
