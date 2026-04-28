# Build your own cell: Diffusion Models for Multichannel 3D Microscopy Image Generation

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 3, 6, 8

## Abstract
Three-dimensional (3D) cellular morphology is a critical indicator of cellular function, disease states, and drug responses. However, capturing and interpreting the complex relationships between cell shape, treatment conditions, and their biological implications remains a challenge. To address this, we present "Build Your Own Cell'' (BYOC), a multichannel 3D generative framework that combines vector quantisation and diffusion models to synthesise biologically realistic 3D cell structures. BYOC captures intricate morphological changes induced by different drug treatments, enabling high-throughput in silico simulations and screening of cell shapes in response to varied conditions. This novel framework represents a significant step towards accelerating pre-clinical drug development by synthesising high-resolution, biologically realistic 3D cells, potentially reducing reliance on labour-intensive experimental studies. By ensuring phenotypic consistency between cell and nucleus volumes through joint modelling, BYOC provides high-fidelity reconstructions that could facilitate downstream analyses, including drug efficacy evaluation and mechanistic studies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors proposed BYOC (Build Your Own Cell), a framework to generate 3D cell structures consisting of both nucleus and cell channels. BYOC utilizes a VQGAN structure with a multimodal DDPM to refine the encoded latent representations and capture the inter-dependence between two channels.

### Strengths
The authors tackled an interesting problem that has not been extensively studied. The writing is clear and easy to follow. The authors provided both qualitative and some quantitative metrics in the evaluation of their framework.

### Weaknesses
Although the problem seems interesting, I am not very convinced about the significance and usefulness of generating realistic 3D cells. I would like the authors to provide more backgrounds regarding why they see this problem as important to solve. Also, the experiment section seems a bit brief and weak. The authors compared with several older GAN-based models but lacked comparison with more recent SOTA diffusion-based models. The improvement against MedicalDiffusion in Table 1 looks pretty minor especially for Blebbistatin and Binimetinib groups. The new framework is mostly combining a VQGAN with a multi-channel DDPM in the latent space, and I would like to see at least some sort of ablation study to showcase the importance of having DDPM in the latent space and the usefulness of linking the two modalities together inside the DDPM.

### Questions
See above in the "weakness" section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors combine vector quantized GANs to learn representations of microscopy images of cells and develop a denoising diffusion model for latent representations. By combining vector quantized representations and the process of diffusion, they seek to generate 3D images of cells that belong to the distribution of realistic microscopy images.

### Strengths
* Strategy: The strategy of using diffusion modeling to improve the accuracy of prediction of GANs is promising.

### Weaknesses
 * Incorrect assumptions about microscopy image data: Microscopy images often consist of more than two channels and many of them cannot be just binned into cells and nuclei. The authors seem to be familiar with medical imaging datasets but unaware of datasets such as cell painting (JUMP, CHAMMI), human protein atlas, and virtual staining. These datasets illustrate that microscopy data often consists of channels that encode multiple organelles and cellular compartments.
* Lack of 3D predictions: Although the paper claims to be the first to build a 3D generative model of microscopy images, all the presented data is 2D. The authors should show orthogonal slices of generated volumes.
* Relevance of metrics: Fre ́chet Inception Distance and Maximum Mean Discrepancy seem reasonable. However, the authors do not clarify how these metrics may be affected by the typical failure modes of GANs, such as hallucinations of spurious cellular processes. The features from a model trained with medical data cannot necessarily distinguish a real or synthetic cell images. The cell images are by definition out of distribution of Med3D dataset. Therefore, the distance between the samples or distributions of synthetic and real cell microscopy images in the embedding space of the Med3D model will most likely not be biologically meaningful. I looked through your section on Evaluation (appendix A.2) and did not find any evaluation of utility of these features/distances/metrics.


### Questions
* What is the effect of the diffusion on the quantized codebook? The way diffusion is used during inference was not apparent from the text or figures.
* Does the approach work only with a specified number of input channels?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a multi-channel 3D diffusion model designed for generating two-channel cell images from volumetric fluorescence microscopy data. By focusing on the coupling of the two channels within the diffusion process, the model aims to improve the quality of generated dual-channel 3D cell images. The results presented show an improvement over the current state-of-the-art in this area.

### Strengths
- Addresses a challenging and pertinent problem in the field of biomedical microscopy, specifically in cellular imaging.
- The overall motivation behind the proposed methodological enhancements is generally clear.
- The experimental outcomes demonstrate promising improvements over existing methods.

### Weaknesses
 - The biological rationale behind the model is not thoroughly convincing or well-articulated.
- Some concrete methodological choices lack clear motivation or detailed explanation, leading to potential confusion (e.g. a clear motivation why and how to use VQGANs would be nice).
- Some details are missing or inadequately explained in the formal equations and overall framework.
- The manuscript tends to be imprecise in its language, which affects clarity and understanding.
- The conclusion lacks specificity regarding the contributions, limitations and future directions of the methods-aspects of the work.

### Questions
1. How could biological or mechanistic understanding arise from generative models in your context? Can you expand and provide a stronger motivation for this idea?
2. You mention that "GANs often struggle with generating coherent latent representations." Since GANs do not inherently produce latent representations in the same way as e.g. Variational Autoencoders, could you clarify what "coherent latent representations" means in the context of GANs, and how this specifically relates to your proposed method's advantages?
3. The claim that multiple color channels can be treated as distinct modalities is not clearly explained in my opinion but is crucial to the suggested method. Do you have examples from related work where color channels have been treated as distinct modalities? Could you explain the biological basis for considering cell and nucleus channels as separate modalities?
4. In Equation 1, are the variables h,w,d the same dimensions as H,W,D? If not, what is their relationship? Similarly, in Equation 2, the depth dimension d seems to be omitted—was this intentional or a typo? Please add a brief explanation of these variables and their relationships directly after the equations.
5. How does the simultaneous recovery of both channels relate specifically to latent diffusion? Can you provide a specific example or illustration of how the simultaneous recovery process works in your model, and how it differs from standard latent diffusion approaches?
6. What is the reason for using unquantized embeddings in your framework? If they drift from the codebook vectors, how does this affect the model, and what is the underlying motivation?
7. In Equation 12, the variable t should be defined. Additionally, in Equation 13, what exactly is μ_θ_cn(⋅) computing—only the mean or is there an associated variance? If not, what is the variance of your Gaussian?
8. There is an existing WNet in medical imaging literature [1]. To avoid confusion, would you consider renaming your model?
9. Can you provide more precise details about your dual-channel 3D architecture, perhaps with references or a schematic in the supplementary material?
10. On page 6, you state that attention mechanisms are "strategically placed" to focus on regions of interest. Could you elaborate on the strategy behind their placement and how regions of interest are determined?
11. The numerical differences in Table 1 are hard to interpret without context. Could you explain or hint to what these differences mean in terms of image quality and their significance in your application? Can you provide a brief interpretation guide for the FID and MMD scores, perhaps indicating what range of differences would be considered significant in this context? You could also include a qualitative comparison of images corresponding to different score ranges to help readers understand the practical implications of these differences.
12. Could you provide more context about the ResNet50 model used—for instance, what type of medical images it was trained on?

**Additional Feedback for Improvement:**

- In Figure 1, please explain what the rows and columns represent to enhance understanding.
- In the introduction, you mention that "single-cell data is often high-dimensional and inconsistent in size." Could you clarify whether this inconsistency refers to the images, cells, biological structures, or image resolutions?
- In the Related Work section, the statement about discriminative frameworks needing a "deep understanding of the underlying input distribution" is unclear. Providing an example or reference could help clarify this point.
- It might be beneficial to first introduce and describe the dataset before delving into implementation details like volume padding.
- Please specify the size and resolution of the microscopy images. Are the single-cell images crops from larger stacks, or are they the direct output from the microscope?
- Consider citing relevant works such as the 3D U-Net architecture [2] to situate your work within the existing literature.
- The conclusion would be stronger if it discussed potential methodological developments and acknowledged limitations of the current approach.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents the novice Build Your Own Model (BYOL), a multichannel generative framework leveraging the diffusion model, to generate a population of simulated 3D multichannel data that shows the morphological changes in cells perturbed by drug treatments. The model captures the relation between the nuclear and cytoplasmic channels used for model training when generating the simulated images and presents a high spatial resolution of the images. The authors benchmarked the model against already available models like GAN-based models and MedicalDiffusion, useful for 3D image generation for the same test case, and found the best overall model performance.

### Strengths
The model outperforms existing models, generating nuanced morphological changes due to perturbations like drug treatments. Compared to existing models, it can also accurately capture the 3D resolved morphology of the cellular tags. The model is best at generating cellular data and matches real data.

### Weaknesses
The model captures the morphological changes associated with the perturbations it has been trained on but has not yet been shown to be generalizable to different cell types and drug treatments. This has been marked as a future prospect of the study. This is important in biological studies as tagging and imaging the markers are expensive for generating training data and a very important domain where biology communities would benefit.



### Questions
The metrics used to evaluate the model are good for evaluating the overall model performance. But do the metrics evaluate the inter- and intra-channel prediction accuracy? The authors stated that it is biologically relevant and an improvement brought by the work. But how can you evaluate this specific aspect using relevant metrics from a biological point of view?

### Soundness
3

### Presentation
4

### Contribution
2
