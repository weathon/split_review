# Learning Stackable and Skippable LEGO Bricks for Efficient, Reconfigurable, and Variable-Resolution Diffusion Modeling

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Diffusion models excel at generating photo-realistic images but come with significant computational costs in both training and sampling. While various techniques address these computational challenges, a less-explored issue is designing an efficient and adaptable network backbone for iterative refinement. Current options like U-Net and Vision Transformer often rely on resource-intensive deep networks and lack the flexibility needed for generating images at variable resolutions or with a smaller network than used in training.
This study introduces LEGO bricks, which seamlessly integrate Local-feature Enrichment and Global-content Orchestration. These bricks can be stacked to create a test-time reconfigurable diffusion backbone, allowing selective skipping of bricks to reduce sampling costs and generate higher-resolution images than the training data. LEGO bricks enrich local regions with an MLP and transform them using a Transformer block while maintaining a consistent full-resolution image across all bricks. Experimental results demonstrate that LEGO bricks enhance training efficiency, expedite convergence, and facilitate variable-resolution image generation while maintaining strong generative performance. Moreover, LEGO significantly reduces sampling time compared to other methods, establishing it as a valuable enhancement for diffusion models. Our code and project page are available at \url{https://jegzheng.io/LEGODiffusion}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is concerned with diffusion-based image generation and proposes Local-feature Enrichment and Global-content Orchestration (LEGO) blocks. These blocks can be flexibly arranged to process local patches of different sizes, thereby implementing a hierarchical structure. The authors also envision skipping and recombining these blocks at training and inference time, as well as incorporating pretrained diffusion models into the structure of blocks. The proposed approach is evaluated on Celeb-A face generation and ImageNet class-conditional generation and compared with popular methods from the literature.

### Strengths
The paper is well written and generally easy to follow. To my knowledge, the idea of splitting the image into patches and to process with a hierarchy of modules has not been explored in the diffusion literature before. The skipping and mixing of modules envisioned by the authors is interesting. The method seems to train more efficiently than recent diffusion methods and has lower inference FLOPs than those at the same sample quality.

### Weaknesses
It seems the authors in essence propose a block-based hierarchical architecture which is not very different from a UNet. While there is lots of talk on modularity and skipping of blocks, these aspects are only explored in the appendix on 64x64 CelebA images, i.e. an easy data set at a resolution where inference speed ups are not very interesting. The aspect of incorporating a pretrained diffusion model is only explored as an ablation. Further, generating images larger than the training resolution is demonstrated with a few examples, which might also be obtained by cleverly leveraging prior works.

Given all these points it feels like the contribution is not as significant as suggested at the beginning of the paper. Experiments where skipping blocks at inference time yield substantial wallclock-time speedups for class conditional ImageNet generation at 256 or 512 pixels resolution would be more convincing.

Minor: Page 6 typo: LEBO

### Questions
- How is the FID computed? FID numbers can differ substantially depending on the implementation, and whether the train or validation set is used as a reference. For example DiT and ADM both use the ADM Tensorflow evaluation suite.
- What is a “linear MLP” (page 7)? How does it differ from a linear layer?
- How do the parameter counts of the proposed model compare with the baselines for the ImageNet 256 and 512 pixels experiments? I could only find parameter counts for the 64 pixel models.
- Are the bricks of a given stage shared across space, or are they specialized per patch?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents LEGO, Local-feature Enrichment and Global-content Orchestration, an architectural tweak to transformer-based diffusion models for unconditional and class-conditional image generation.
The core idea behind LEGO lies in applying self-attention blocks with varying patch sizes across the transformer, thereby allowing different blocks (called LEGO brick) to focus on different scales of reconstruction / image generation, e.g. blocks with small patches will naturally focus more on local reconstruction, while larger patch sizes encourage enforcing global consistency. Furthermore, each LEGO brick can be applied to a subset of local patches, thereby increasing compute efficiency. Another way in which LEGO allows more efficient generation at test time is to selectively disable some LEGO bricks at specific time steps: For example, the contribution of very local LEGO bricks with small patch sizes is negligible for early t-steps during inference as the local structure of the pixels will still vary heavily in subsequent time steps -- similarly, transformations with a wider receptive field can be dropped at later t-steps since the global structure of the image to be generated has already been decided in earlier time steps. Finally, the method allows variable-size (and aspect ratio) image generation, even after being trained on a fixed-sized image dataset.
Overall, this method achieves competitive results with favourable compute cost.

### Strengths
- The proposed method appears to be original and is intuitive.

- The authors present sensible experiments that ablate over several design choices of their method. Especially the choice of dropping specific LEGO blocks during inference is quite interesting.

- The authors clearly state several limitations of their work, none of which are a major concern for this submission -- the paper is well-scoped.

- The writing style is good, and the authors always try to simplify and add intuition to design choices.

### Weaknesses
 - The method presentation could be improved. Intro, Section 3.1 and Figure 3 provide some high-level intuition which is helpful for the start. Meanwhile the remaining sections obfuscate major questions, e.g. whether a LEGO brick is applied densely or sparsely or how the patches are selected.

- The majority of the experiments and results are placed in the appendix, while a very large portion of the main paper is dedicated on an extensive introduction, related works, and more context setting at the start of the method section. The authors should strongly consider making the first 4 pages of the main paper significantly more concise, thereby allowing the main findings to move from the appdix to the experimental section of the main paper.

- The graphic shown in right panel in Figure 1 is interesting, but there may be a better choice of representing the same data. Drawing circles with FLOPs as their radius makes differences between models appear much more significant than they are (since the difference in circle size == circle area grows with the square of the radius), making the plot somewhat misleading. A more common choice is a plot showing FID on the y-axis and FLOPs on the x-axis, where each model would be a single dot.

### Questions
- How many patches are selected (for a single LEGO brick)? During training time & inference.

- Page 1: "This requirement arises from the model's need to learn how to predict the mean of clean images conditioned on noisy inputs [...]". Could the authors provide a citation for this claim?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes LEGO bricks, which can be stacked to create a test-time reconfigurable diffusion backbone, so that at run time one can selectively skip some of the bricks to reduce sampling cost and generate images with higher resolution than the training data.

### Strengths
* The idea of designing a run-time configurable backbone for diffusion model is interesting and timely. 
* The design within LEGO bricks makes sense, and the performance also looks good. 
* The paper is well-written with clear structure. The training and sampling details are presented in a clear way.

### Weaknesses
 * It seems that the design of LEGO bricks borrows a lot from DiT, so it is a bit unclear to me how much additional contribution w.r.t. network design made in this work.
* It is also clear if the idea of LEGO (skippable and stackable backbone),  is specific to DiT, or it is general enough to be applied to other types of backbone for diffusion models?

### Questions
* It is mentioned that the optimization of patch sizes for the LEGO bricks can be future work: can you give some intuition on how to choose the right patch sizes?
* There are two spatial refinement settings mentioned in the paper: PG and PR. So does that mean a model can only take one of these two configurations? or they can be used interchangeably in one model?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
