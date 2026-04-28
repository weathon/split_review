# On the Effectiveness of Dataset Alignment for Fake Image Detection

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
\vspace{-5pt}

As latent diffusion models (LDMs) democratize image generation capabilities, there is a growing need to detect fake images. A good detector should focus on the generative model’s fingerprints while ignoring image properties such as semantic content, resolution, file format, etc. Fake image detectors are usually built in a data-driven way, where a model is trained to separate real from fake images. Existing works primarily investigate network architecture choices and training recipes. In this work, we argue that in addition to these algorithmic choices, we also require a well-aligned dataset of real/fake images to train a robust detector. For the family of LDMs, we propose a very simple way to achieve this: we reconstruct all the real images using the LDM's autoencoder, without any denoising operation. We then train a model to separate these real images from their reconstructions. The fakes created this way are extremely similar to the real ones in almost every aspect (e.g., size, aspect ratio, semantic content), which forces the model to look for the LDM decoder's artifacts. We empirically show that this way of creating aligned real/fake datasets, which also sidesteps the computationally expensive denoising process, helps in building a detector that focuses less on spurious correlations, something that a very popular existing method is susceptible to. Finally, to demonstrate just how effective the alignment in a dataset can be, we build a detector using images that are not natural objects, and present promising results. Overall, our work identifies the subtle but significant issues that arise when training a fake image detector and proposes a simple and inexpensive solution to address these problems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to detect fake images by improving the aspect of data alignment. The paper reconstructs all real images using the autoencoder of a latent diffusion model and then trains fake image detectors to distinguish between real and reconstructed images. The paper claims that this approach prevents the fake image detector from focusing on unwanted artifacts such as semantic content, resolution, or file format. Additionally, they argue that this method of data collection is more efficient than prior works which pair real images with generated images, as it avoids the expensive denoising process associated with generating fake images. The paper shows stronger results than prior works in detecting latent diffusion models and provides an analysis of potential pitfalls in prior works, such as detection bias stemming from resolution differences or compression artifacts between real and fake data.

### Strengths
1. The paper proposes a simple and efficient way to collect data for fake image detection.
2. The paper provides an analysis of common pitfalls of prior works, such as image resolution or compression artifacts.

### Weaknesses
1. It is unclear whether or not the proposed method would generalize well to architectures other than latent diffusion models. For example, would this generalize well to models such as VQ-VAE[1], VQ-GAN[2], or more recent models with very different autoencoder architectures? The paper mentions that it does not work well on models with vastly different architectures (e.g., FLUX.1-dev), but it is not clear to what extent of architectural changes the proposed method is robust to. Specifically, the paper lacks a systematic evaluation across a spectrum of autoencoder architectures, making it difficult to ascertain the method's limitations and general applicability. An analysis showing the performance of the proposed method on a range of models with varying autoencoder designs, such as those with discrete latent spaces or different upsampling/downsampling techniques, would be beneficial.
2. The proposed method, by design, disregards semantic content. While the paper claims that this is a desired property, in some contexts, the semantic content may matter. With proper techniques, the autoencoder artifacts may be decimated [3]. In such cases, the proposed method may fail to properly distinguish fake and real. However, prior data-driven approaches may be able to pick up on semantic cues such as over-saturation or contrast, malformed objects, or unrealistic sceneries to detect generated images. The performance differences after post-processing shown in Table 3, between detectors trained on natural images and shader images, may hint at the importance of semantics. It is concerning that the method might be vulnerable to techniques that effectively remove autoencoder artifacts while preserving semantic inconsistencies, which could be exploited by adversaries.
3. The paper lacks a detailed analysis of sensitivity to various transformations. The paper claims that their method of training detectors is more robust as it forces the detectors to focus more on autoencoder artifacts. However, the experiments do not adequately demonstrate this property, as the paper only compares the performance of a single randomized post-processing technique in Tables 2 and 3. Including a detailed, separate analysis of the robustness to various transformations, similar to those shown in Figure 2 and the figure on page 10 would better illustrate this characteristic and provide better insights for future research. The current evaluation does not sufficiently isolate the impact of each transformation, making it difficult to understand the specific strengths and weaknesses of the proposed method. A more granular analysis, including transformations such as rotation, scaling, and different types of noise, would provide a more comprehensive picture.
   - The figure on page 10 should be properly numbered and referenced in the main text.
4. Accuracy is not the best metric for showing the performance of the detectors, as it is sensitive to thresholds. I recommend the authors to consider threshold-less metrics such as average precision (AP). For example, in Tables 1 and 2, applying post-processing actually improves the accuracy of certain detectors (e.g., Cozzolino-LDM). Using threshold-less metrics such as AP may provide a more accurate picture of performance degradation caused by post-processing. The reliance on accuracy as the primary metric obscures the nuanced performance changes under various conditions, and a more robust metric like AP would provide a more reliable assessment of the detectors' capabilities.

### Questions
1. What is the rationale behind calibrating the threshold in Table 3? Why is this different than prior experiments (Tables 1 and 2), and what happens if you use the default threshold (0.5) similar to Tables 1 and 2?
2. I'm curious what the authors' intuition behind why the models trained on shaders dataset show more sensitivity to post-processing than the ones trained on natural images.
3. The Appendix A.2.1. shows that the proposed method can train the detector in a more data-efficient manner. I'm curious why this is the case. Is it because it only has to focus on single artifacts?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper is rooted in a key observation that training a naive binary classifier to detect real/fake might learn the spurious correlations, and thus cannot achieve a more robust detection result. To achieve the alignment of the training dataset, they propose a new dataset by using LDM’s autoencoder for reconstruction purposes. The authors also provide clear evidence and experiments to verify their observation.

### Strengths
1. The paper is well-written and has a very clear research motivation.

2. The dataset alignment is a critical problem that might cause the model to learn spurious correlation in the fake image detection field.

3. The authors provide reasonable evidence to validate their findings and observations. Especially the effectiveness of downsampled before and after resizing (Table 5), which is insightful to me.

### Weaknesses
 - A major limitation of this work is the generality of images generated by Latent Diffusion Models (LDM). Does the detector primarily learn LDM-specific fake patterns, rather than a broader range of patterns such as those generated by GANs? Or does it learn only method-specific fake patterns unique to a particular LDM instance, failing to generalize across the LDM family? A more robust evaluation of this generality would be beneficial. Specifically, the paper should investigate whether the detector is sensitive to variations in LDM architectures, such as changes in the VAE or UNet components, and whether it can generalize to images generated by different LDM models with different training datasets or parameters. This is crucial to determine if the detector is learning intrinsic fake patterns or just memorizing specific LDM artifacts.

- This paper defines "fake image detection" as "entire image synthesis." However, this scope does not cover other types of fake images, such as deepfakes (e.g., face-swapping) or talking-head videos. A further discussion of the results of these types of fake images would enhance the paper. The current definition limits the practical applicability of the proposed method, as many real-world scenarios involve manipulated images beyond full synthesis. The paper should acknowledge this limitation and discuss the potential challenges and adaptations needed to extend the method to these other forms of image manipulation.

- There is limited analysis of pre-trained models in this work. For instance, CLIP and ResNet-50 (trained on ImageNet) may detect fake images differently. Given CLIP’s rich knowledge, it may be less likely to focus on irrelevant patterns. A deeper analysis and discussion of these differences would strengthen the paper. The analysis should explore how different pre-training objectives and architectures influence the learned features and their sensitivity to fake image artifacts. For example, CLIP's contrastive learning might lead to different feature representations compared to ResNet-50's classification-based training, and this difference should be investigated in the context of fake image detection.

- What are the advantages of conducting online reconstruction using LDM (as in previous works, such as ref[1]) compared to offline reconstruction (as used in this work)? The paper should provide a more detailed comparison of the computational cost, memory requirements, and detection performance of online versus offline reconstruction methods. The discussion should also consider the potential impact of reconstruction quality on the final detection performance.

- The alignment issue highlighted here is not entirely new; several prior studies, especially in deepfake detection, have addressed this challenge. For example, refs [2] and [3] discuss the importance of alignment for robust detector performance. Ref [2] shows that a resolution gap between real and fake images can bias models toward interpreting higher resolution as real and lower as fake, while ref [3] demonstrates that aligning real and corresponding fake samples in training improves detector robustness. Further discussion of these relevant works would help contextualize this study’s findings on alignment. Specifically, the paper should discuss how the proposed method differs from the alignment strategies used in these prior studies and what novel contributions it offers.

### Questions
1. Does the detector primarily learn LDM-specific fake patterns, rather than a broader range of patterns such as those generated by GANs? Or does it learn only method-specific fake patterns unique to a particular LDM instance, failing to generalize across the LDM family?

2. What is the clear and accurate definition of "fake image" in this work?

3. What are the differences between CLIP and Res50 in the shortcut manner?

4. Offline reconstruction and online reconstruction.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the effectiveness of dataset alignment in fake image detection, specifically for images generated by latent diffusion models (LDMs). The authors propose a simple approach: reconstructing real images using the LDM's autoencoder and treating these reconstructions as fake images. This aligned dataset allows for training a classifier to distinguish real from fake images, focusing on the generative model's artifacts rather than spurious correlations such as resolution or content differences. Experimental results show that this alignment method improves the robustness and generalization of the detector across different generative models, while also being more computationally efficient.

### Strengths
1. The paper proposes an interesting framework for generating fake images by using only the LDM's autoencoder, rather than the full generative process, to train the detector. Experiments show this approach achieves better performance compared to using complete generated images, which is a noteworthy finding.

2. The paper reveals the impact of scaling factors on detection methods, contributing valuable insights to the field.

### Weaknesses
1. Lack of technical contribution: Although the findings are interesting, the authors did not deeply explore the reasons behind the observed phenomena or how they could further benefit existing detection methods. They only conducted shallow comparative experiments using their generated data. Overall, the contribution feels insufficient.

2. Limited comparison methods: The authors aim to prove their dataset has better generalization and performance than others, but they only compared it with two methods. These methods are not state-of-the-art (SOTA) on complex public datasets like GenImage. The lack of sufficient comparisons weakens the paper's persuasiveness. Additionally, the comparison datasets are not from AIGC detection benchmarks, making it difficult to determine a fair performance improvement.

3. The proposed method of classifying only LDM-generated data can avoid some spurious features but also ignores certain important features, such as artifacts introduced during the diffusion process. The method is mainly effective for LDM-based generation techniques and less so for traditional GAN or diffusion models. It may be that the LDM itself removes diffusion artifacts, making it easier to detect LDM-specific artifacts. Moreover, the method cannot handle semantic inconsistencies left by some generative methods, such as incorrectly generated hands.

4. The authors should conduct robustness tests, such as robustness against noise or JPEG compression, to further validate the method.

5. The paper structure could be improved, with clearer diagrams and better formatting. The dataset descriptions are somewhat disorganized, and a more structured introduction is recommended.

### Questions
See the weakness section.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper mainly focuses on detecting the fake images generated by latent diffusion models (LDMs). It states that dataset alignment plays an important part in detecting LDM-based fake images and proposes a simple method to detect LDM-based fake images by training detectors with the aligned dataset (real images and fake images created by only LDM's autoencoder). Experiments show that the proposed method is inexpensive and effective in detecting LDM-based fake images.

### Strengths
1. The proposed method is simple and can potentially be a useful baseline for LDM-based fake image detection.
2. The proposed method is more effective and efficient than the paper's major baseline (Corvi).
3. Extensive experiments provide sufficient support for the superior performance of the proposed method. 4. The paper is somewhat clear and well-written to me.

### Weaknesses
1. The title slightly disqualifies the paper's main topic since the authors pay attention to LDM-based fake images. However, many generative models can create general fake images, including AutoEncoder, GAN, VAE, and LDM. It seems more appropriate to add qualifiers in the title. 
2. Both Corvi and the proposed method remain vulnerable to minor changes. Although the proposed method shows wonderful performance against some LDM-based images, the comparison between results from Table 1 and Table 2 reveals both Corvi and the proposed method can be easily disturbed by post-processing like lossy compression. This sensitivity to post-processing significantly limits the practical applicability of both methods in real-world scenarios where images are often subject to various transformations.
3. Lack of further insights between "Ours" and "Ours-Sync". In section 4 (Our Approach), two variants "Our" and "Our-sync" are introduced but with no extra explanations. In experiments, "Ours-Sync" shows superior performance in most cases than "Ours" with almost no analysis. The absence of a clear explanation for the performance differences between these two variants makes it difficult to fully understand the proposed method's underlying mechanisms and limits the reproducibility of the results.
4. The figure in the conclusion loses its caption. Help it.

### Questions
1. Why does the performance of detectors drop a lot facing fake images with small scaling factors or real images with large factors? Are there any reasonable explanations?
2. Why does "Ours-Sync" outperform "Ours" in most cases, and why does "Ours" kick back in some special cases?
3. The combination of the proposed method and Corvi should be reasonable and available. Does it perform remarkablely in detecting LDM-based fake image detection?
4. It seems that the proposed method can enjoy a better performance with a large batch size. Would you mind a try?
5. I understand that using ResNet-50 is for alignment in the network architecture to some baselines, but more experiments on different network architectures are suggested.

### Soundness
2

### Presentation
3

### Contribution
3
