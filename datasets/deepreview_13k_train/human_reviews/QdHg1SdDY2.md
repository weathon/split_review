# LEA: Learning Latent Embedding Alignment Model for fMRI Decoding and Encoding

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
The connection between brain activity and  visual stimuli is crucial to understand the human brain. While deep generative models have exhibited advances in recovering brain recordings by generating images conditioned on fMRI signals, it is still challenge to  generate consistent semantics. Moreover, the prediction of fMRI signal from visual stimuli remains a hard problem. In this paper, we introduce a unified framework that addresses both fMRI decoding and encoding. With training two latent spaces capable of representing and reconstructing fMRI signals and visual images, respectively, we align the fMRI signals and visual images within the latent space, thereby enabling a bidirectional transformation between the two domains. Our Latent Embedding Alignment (LEA) model concurrently recovers visual stimuli from fMRI signals and predicts brain activity from images within a unified framework under user-specified direction. The performance of LEA surpasses that of existing methods on multiple benchmark fMRI decoding and encoding datasets. LEA offers a comprehensive solution for modeling the relationship between fMRI signal and visual stimuli.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper aims to build connection between brain activity (from fMRI) and visual stimuli through a latent embedding alignment (LEA) model. The LEA model trains two latent spaces that is used to reconstruct both the fMRI signal and the visual images, and uses a linear layer to align the latent spaces. The proposed architecture is evaluated on many tasks of two datasets, and the authors show that LEA consistently outperforms existing methods on many tasks.

### Strengths
The proposed method/framework demonstrated good empirical performance on the studied datasets across many different downstream tasks.

### Weaknesses
- The presentation of the paper isn’t clear, which not only posts challenge to its readability but also undermines its methodological contributions.

1. Weird terminology and unclear contributions. Encoding typically refer to extracting meaningful representation from the input data; and decoding typically refer to generating realistic data from meaningful representations. In this paper, however, the first paragraph and the related work section seems to define ‘decoding’ as using fMRI to generate images; and ‘encoding’ as generating fMRI from images. However, in later paragraphs, the authors continue to use the original definition of encoding and decoding by referring MAE as “encoder-decoder architecture training”. Thus, the major contribution of the work “simultaneously tackling the tasks of fMRI decoding and encoding” reads unclear based on the not-clearly defined terminology.

2. Unclear math definitions. For example, Equation 1 shows the loss for the model training. What are the parameters trained and why they are not inside the equations? What are the architecture of the referred layers, e.g. RoI Project layer? For the latent embedding alignment, how is the linear model trained? It is challenging to decipher the correctness of the approach without such methodological details.

3. Grammar issues. e.g. “Through extensive experiments on benchmark datasets, we demonstrate that LEA not only exhibits superiority in the domains of fMRI decoding and encoding.” “the totally amount of training fMRI data”.


- Lack of ablation experiments. The work lack methodological insights if it is unclear which part of the model is taking an effect. Is the method better because the alignment is through a linear model regression? Is the backbone architecture better or more complex (contains more parameters)? Is the RoI module taking an effect? The Table 6 in appendix (the only ablation I found through the text) reveals very little information.

- Unclear experimental details. What are the backbone architecture of the baselines? Are the comparison fair in terms of the amount of parameters? The authors should justify as such by providing necessary details.

Overall, I believe the presented paper lacks necessary details in the introduction section; methodology section; as well as the experimental results section. It is challenging to valid the effectiveness and novelty of the proposed approach without such details. I'd open to raise my score if the authors could provide such details during rebuttal.

### Questions
See above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript proposed a bidirectional encoder-decoder framework for fMRI and images. The fMRI architecture employs a Masked Autoencoder (MAE) with a CLS token, which is the only token used for the reconstruction of the fMRI. The image encoder leverages a pre-trained CLIP encoder, while the decoder utilizes class-conditional MaskGIT architecture. Then, the embeddings of the fMRI and images are connected using ridge regression. The experiments were performed on two datasets: BOLD5000 and GOD. The performance of the proposed model improves over previous baselines.

### Strengths
- The experiments were performed on two datasets.
- The models have been compared to multiple baselines.

### Weaknesses
- Using the test subset of the dataset via reconstruction task creates data leakage during pre-training. Please use the test dataset only to report final performance, and do not use it in any part of your experiments. It does not matter if the previous paper used it. Furthermore, you should not use a test set to find hyperparameters or select checkpoints. For this, you should have a validation set. I did not find details for the cross-validation.
- It is not clear whether you split your data subject-wise. If you have not divided the dataset subject-wise, it also creates data leakage, typical for models trained with task data. Please consider leave-one-subject-out strategy. Furthermore, using an fMRI time series connected to the 50 left images might create data leakage. Overall, it would be best if you considered all the cases from easiest to hardest. It is essential to reduce any possible data leakage, as fMRI is quite undersampled and noisy. Hence, fMRI can be some form of noise that matches images to some noisy targets, as in the Noise-as-Targets (NAT) approach (Bojanowski et al., 2017).
- Tables 1, 2, 3, and 4 do not show variability of the approaches. Please run multiple times or use other strategies to calculate STD, SE, or IQR. Additionally, perform statistical analysis to compare model performance and run correction for multiple comparisons.
- Missing related work: MindEye (Scotti et al., 2023), in which the authors also use the NSD dataset and demonstrate that contrastive loss can be used as alignment similar to proposed non-contrastive regression. The authors also use voxels and not ROI. Do you have ablations for the strategies?

Bojanowski, Piotr, and Armand Joulin. "Unsupervised learning by predicting noise." International Conference on Machine Learning. PMLR, 2017.

Scotti, Paul S., et al. "Reconstructing the Mind's Eye: fMRI-to-Image with Contrastive Learning and Diffusion Priors." arXiv preprint arXiv:2305.18274 (2023).

### Questions
- How has the FMRI been preprocessed? It would be great if you reference it or include it in the appendix.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces LEA, a model that aligns fMRI signals and visual images within a latent space, enabling bidirectional transformation between the two.

Their method consists of two steps:
1. Training an transformer auto-encoder with a single token bottleneck, where the inputs are chunked at a ROI level.
2. An alignment step using ridge regression.

They validate their results on both encoding (evaluated using pearson correlation) and decoding (evaluated using CLIP and n-way classification).

Concretely, these are the claimed contributions:
1. Specialized encoder-decoder architectures for fMRI signals and images.
2. ROI-Induced Embedding Layer for feature extraction.
3. Latent Space Alignment for joint fMRI decoding and encoding.
4. Superior performance on multiple benchmark datasets (Page 3).

### Strengths
They propose the use of a unified framework called LEA, that tackles both fMRI decoding and encoding. This is a step forward in the field, which often treats these tasks separately. They also introduce an innovative ROI-induced embedding layer that addresses the issue of varying dimensions in fMRI signals.

Their qualitative results seem largely sound.

### Weaknesses
I have serious concerns about the presentation and the scope of claims of the paper. 
1. The authors claim that `Our method begins by side-stepping the necessity for paired image-fMRI data`, and in the contributions section they relax it to `without the need for extensive paired training data`. 
2. The authors claim that `these encoder-decoder architectures can be trained via self-supervised learning techniques` as in denoising autoencoder fashion or MoCo (Momentum Contrast) which they cite. The authors don't demonstrate the claimed self-supervised learning techniques, opting instead for a basic auto-encoder architecture with a single token bottleneck, as shown in Figure 2.
3. It is unclear how exactly they perform alignment between the fMRI latent space and image latent space. This is a very important step but section 3.3 includes very few details.
4. Your zero-shot classification of brain activations relies on CLIP, which is different from the zero-shot results presented for CADA-VAE etc. which rely on a SVM (as the results in Table 1 for baseline methods are from Liu et al., which are in turn taken from Du's BraVL paper). Please note this in the paper. 
5. From what I can tell, their broad high level approach is similar to what was proposed in BrainCLIP, and their key novelty lies in the ROI-level transformer auto-encoder. In my view this is not sufficiently novel.

**Data presentation issues:**
1. Figure 2 is very misleading. In the paper it is unclear if you are working with time series data (as in GOD) or the fMRI betas (as in BOLD5000). Regardless of what form of data you are using, it would be deeply misleading to present the fMRI time-series across different regions of interest as one continuous time-series data.
2. Table 2, where you measure pearson R, it is unclear how you get values greater than 1. It is also unusual to use use pearson R to evaluate encoding models, using explained variance is the more common approach [1].
3. There are many claims about building accurate encoding models, but the paper does not include any visualization of the cortical surface and how the R or explained variance varies. It is higher in ROIs that are strongly explained by visual stimuli?

There are also many small typos and oddly phrased sentences. I would not typically identify this as an issue, but in this paper the problem is serious enough that it is difficult to read. 

I do not believe the writing quality currently is ICLR level. Hopefully the authors can closely read through their paper and fix all the issues. I will not list them all here.

**Minor typos:**
* Abstract line 1 `is crucial to understand` -> `is crucial to understanding`
* Abstract line 4 `is still challenge` -> `is still challenging`
* Abstract line 6~7 `With training` -> `By training`
* Abstract line 12 `under user-specified direction` -> `under a user-specified direction`
* Intro ` Identifying and categorizing ... is a crucial step to understand...` -> `Identifying and categorizing ... is a crucial step for understanding...`
* Intro `Since ... the brain may not fully capture, it is not necessary to reconstruct` -> `Since ... the brain may not fully capture, it is not possible to reconstruct`
* Intro `pairs is limited` -> `pairs are limited`
* Intro `Recent researches` -> `Recent research`
* Methodology `both fMRI decoding` -> `both the fMRI decoding`
* Methodology `that recovering the observed image` -> `that can recover the observed image`
* Methodology `as well as fMRI encoding` -> `as well as the fMRI encoding`
* Methodology ` that predicting the brain activity` -> `that predicts the brain activity`

There are many more, but I cannot list them all.

**Serious typos:**
* Abstract line 3 `in recovering brain recordings by generating images conditioned on fMRI signals`. Can you clarify what you are trying to say here? Are you trying to recover the stimulus? You are already conditioned on fMRI signals, so it is not clear why you are trying to recover brain recordings

[1] Neural Encoding and Decoding with Deep Learning for Dynamic Natural Vision (2017)

### Questions
1. In the Intro, you cite the BOLD5000 paper to support your statement that `the semantic information contained in fMRI data is sparsely distributed and highly correlated between neighboring elements`. 

    However, this statement is not substantiated by the cited BOLD5000 paper. The authors of BOLD5000 did not really analyze semantics in any significant sense. The authors of BOLD5000 neither discuss voxel-wise correlations as a function of voxel distance nor address the sparsity of semantic representations in the brain. This claim about sparsity appears to conflict with evidence [1,2], which indicates that multiple visual regions in the brain are activated by various visual categories. 

2. Could you clarify what the ROI Embedding Layer on page 4 is convolving over? You have an input of shape $N \times 1$ and then you describe your method to have a convolution outputs of $N \times 32$. How is the convolution happening in this case? Over which dimensions is the convolution occurring?



[1] The “visual word form area” is involved in successful memory encoding of both words and faces (Neuroimage 2010)

[2] FFA: a flexible fusiform area for subordinate-level visual processing automatized by expertise (Nature Neuroscience 2000)

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
