# Perceptogram: Visual Reconstruction from EEG Using Image Generative Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
In this work, we reconstruct viewed images from EEG recordings with state-of-the-art quantitative reconstruction performance using a linear decoder that maps the EEG to image latents. We choose latent diffusion guided by CLIP embedding as the primary method of image reconstruction as it is currently the most effective at capturing visual semantics. We also explore reconstruction results from a latent space of  PCA and ICA components, which capture luminance and hue-related information from the EEG. The linear model provides interpretable EEG features relevant for differentiating general semantic categories of the images.  We create spatiotemporal semantic maps that reflect the temporal evolution of class-relevant semantic information over time.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents Perceptogram, a novel approach for reconstructing viewed images from EEG recordings. The method utilizes a linear decoder to map EEG signals to image latents, leveraging latent diffusion guided by CLIP embeddings for image reconstruction. The study also explores reconstructions using PCA and ICA components capturing luminance and hue-related information. The linear model provides interpretable EEG features for differentiating semantic categories, and the results demonstrate state-of-the-art quantitative reconstruction performance.

### Strengths
The paper uses a liner regressor to correlate the EEG space and VAE/CLIP space and achieves good performance in EEG-based image recognition. Meaningful analysis has been conducted to provide insights, including ICA and PCA features, scalp-asymmetry effect, and spatial-temporal semantic maps.

### Weaknesses
The linear model approach is a conventional method for brain visual reconstruction, offering high interpretability. However, further clarification is needed to enhance the reliability of this work:
1. How effectively does the regressor perform in mapping EEG embeddings to CLIP embeddings? Could specific visual components represented by different tokens show higher correlations with EEG features? For instance, do certain CLIP tokens corresponding to edges, textures, or object parts exhibit stronger correlations with specific EEG patterns than others? A more granular analysis of the token-level correlations is needed to understand the specific visual features encoded in the EEG signals.
2. The study lacks key conclusions derived from performance metrics and analysis on the nature of visual information learned from EEG signals. While the paper demonstrates state-of-the-art reconstruction performance, it does not sufficiently explore what aspects of visual information are captured by the EEG signals. For example, are the reconstructions primarily capturing low-level features like color and luminance, or are they also encoding higher-level semantic information?

### Questions
1. Why not utilize whole-brain data to analyze spatial patterns? High-level information is often associated with the temporal cortex, where the EEG channels have been excluded.
2. Could you compare the contributions of the VAE, CLIP-vision, and CLIP-text components? Which component plays a more significant role in image reconstruction, and what types of features are critical? It may be useful to show reconstruction results for each module individually.
3. What insights can be drawn from Figure 3(d)? It seems that different cases yield very similar performance.
4. How was the model trained, and what objective functions were used? Did training mainly involve constraining the three regressors?
5. How were the error bars in Figure 3(a) generated if all subjects were included?
6. What information can be inferred from the spatiotemporal semantic map? Currently, the map only shows varied patterns across categories. More substantial evidence is needed to establish consistency with established neuroscience knowledge.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper adapts an fMRI brain-to-image decoding pipeline based on linear Ridge regression and frozen image latents to EEG brain data. Linear decoders are trained per-subject and token of each latent representation (CLIP-Vision, CLIP-Text and VDVAE) on the averaged trials of each 16,540 train images (repeated 4 times each). Predicted latents on a test set of 200 images (averaged over 80 trials per image) are then fed to a Versatile Diffusion model, which generates images whose similarity to the ground truth is evaluated with different image metrics. Ablations suggest using the full EEG windows (800 ms) and all three latents yield the best performance. Additional analyses show (1) reconstructions based on PCA and ICA image features, (2) the effect of changing the layout of EEG electrodes, (3) the impact of swapping out subwindows between EEG examples on the reconstruction, and (4) spatiotemporal activation maps for three different categories of images.

### Strengths
* Quality: Relevant analyses and ablations are proposed (e.g. impact of averaging trials, use of the different latents, neuroscience-inspired analyses). The time-swapping experiment yields interesting results.
* Clarity: The paper is overall clear and the different analyses are explained appropriately.
* Significance: The paper shows that a simple pipeline based on linear models can achieve good performance on an image decoding task.

### Weaknesses
1. The novelty of the work is limited. There are no new methodological contributions as the proposed approach appears to be a direct adaptation of Ozcelik & VanRullen (2023), but on EEG rather than fMRI. The proposed analyses (reconstructions based on PCA/ICA, effect of electrode layouts, etc.) appear to be new and may be interesting from a brain decoding perspective, but their significance is limited for the wider ML/AI community. The use of unCLIP, while effective, has also been explored in previous brain decoding work, further diminishing the methodological novelty. The core approach of applying linear regression to predict image latents from brain data, while effective, does not introduce a new technique or model architecture. The analyses, while thorough, are largely exploratory and do not provide a clear pathway for the development of new ML/AI tools.
2. The comparison to existing work is limited. The results of Li et al. (2024) and Benchetrit et al. (2024) were for cross-subject models, while results presented here are for subject-specific models only. I believe the proposed approach may not be straightforward to apply to a multi-subject setting given the use of linear models, but this would be a better point of comparison. Moreover, the direct comparison to the results on the THINGS-MEG dataset is not appropriate as the brain data itself is different (EEG vs. MEG) and the number of image repetitions is not the same (1 vs. 4 presentations of training images; 12 vs. 80 presentations of test images), see Q4.

### Questions
1. Why is the performance so high as compared to existing work that uses more sophisticated approaches (e.g. Li et al., 2024)? Can the authors highlight differences with other work that may explain why the proposed simpler approach works as it does?
2. What is the impact of the “shift and rescale” procedure described in lines 142-143? This would be interesting to include as an ablation too.
3. How was the regularization strength selected (line 160)? Are the models sensitive to the choice of this hyperparameter?
4. Does the proposed approach yield (or is expected to yield) similar results on the THINGS-MEG dataset? I see the shared code contains instructions on how to run on THINGS-MEG, but I don’t see matching results in the paper.
5. Figure 5: It would be interesting to see what images reconstructed from the groundtruth’s first 1000 principal components look like. This may be a better point of comparison than the groundtruth images themselves.
6. Does the data for Figures 5, 6, 7 come from subject 1 as well? Generally speaking, can the authors confirm that results (reconstructions) shown on subject 1 only generalize to other subjects too?
7. What are the + and - columns in Figure 9?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents an approach for reconstructing viewed images from EEG recordings. The authors employ a linear decoder that maps EEG signals to image latents, leveraging CLIP embeddings and latent diffusion models to achieve state-of-the-art quantitative reconstruction performance. The study explores the use of PCA and ICA components to capture luminance and hue-related information from EEG. The linear model provides interpretable EEG features for differentiating semantic categories of images and creates spatiotemporal semantic maps reflecting the temporal evolution of class-relevant semantic information.

### Strengths
The paper introduces an application of EEG in the domain of image reconstruction, which is traditionally dominated by fMRI and MEG. The use of CLIP embeddings and latent diffusion models for EEG-based image reconstruction is innovative.

The methodology is rigorous, with a clear pipeline from EEG signal processing to image reconstruction. The use of multiple metrics for performance evaluation ensures a comprehensive assessment of the reconstruction quality.

The paper is well-organized, with a clear presentation of the reconstruction pipeline and detailed explanations of the methods and results. The figures and tables effectively support the textual content.

### Weaknesses
1. The paper's main contribution is not explicitly stated. While the application of EEG to image reconstruction is interesting, the novelty of this work is unclear given the existing literature on visual image reconstruction from brain activity. The authors should clarify whether the primary contribution lies in the application of more powerful generative models or in the extraction of novel information from EEG signals that was not previously possible. A clear articulation of the specific advancements over prior work is needed.

2. The evaluation appears to focus solely on image reconstruction metrics. While these metrics are important, the absence of accuracy metrics for feature decoding from EEG signals limits the understanding of the model's performance. Reporting metrics such as classification accuracy for decoded features would provide a more comprehensive assessment of the model's ability to extract meaningful information from the EEG data.

3. The validation of the method is limited to a single EEG dataset (THINGS-EEG2). To demonstrate the robustness and generalizability of the proposed approach, it is crucial to evaluate its performance on other established datasets, such as the Natural Scenes Dataset (NSD), which has been widely used in similar studies involving fMRI or MEG. This would help establish the superiority of the method across different data modalities and experimental paradigms.

4. The paper lacks a thorough discussion on the underlying mechanisms that enable the reconstruction of visual stimulus information from EEG. Specifically, it is unclear whether the reconstructed details, such as color, shape, and texture, are genuinely derived from information encoded in the primary visual cortex and captured by EEG, or if they are primarily artifacts of the generative models' priors. A more in-depth analysis is required to elucidate the source of the reconstructed information and to determine the extent to which it reflects actual neural representations.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper highlights the method of generating images from EEG signals by CLIP embedding. In the visual representation and construction field, EEG is less frequently used and has better temporal resolution instead of spatial resolution, so it may be useful for future work related to brain-computer interface. The research regarding the scalp-asymmetry effect, time-swap effect, and spatiotemporal semantic map described some important internal mechanisms of visual reconstruction.

### Strengths
1. A simpler model that has state-of-the-art performance. Every stage of the whole model is highly modular. Multimodal extraction with different models. In 3.3 we can see that VDVAE-based reconstructions is useful to exctract the latent space from EEG signals.

2. The method of observing time-swap effect and spatiotemporal semantic map is fascinating, making full use of the characteristics of EEG's high time resolution. From the spatiotemporal semantic map (Figure 9), the trends show some consistent and universal dynamic patterns to help researchers understand the time-dependence reactions of the brain when dealing with these different categories.

### Weaknesses
1. The contribution of this paper to the community appears limited, as it does not provide new insights or innovative research directions. The repackaging of existing work—specifically the separation of CLIP embeddings into text and image components—does not signify substantial progress within the field. 

2. The absence of a detailed model explanations, and mathematical rigor undermines the paper's contribution. Key sections, particularly between lines 130 and 150, are inadequately polished; there is a pressing need for more precise mathematical formulations and clearer textual explanations to enhance comprehension and rigor. And the presentation of the results is unpolished, e.g. fig6, text size should be unified, and in fig.7 texts should be aligned, etc.

3. In line 349, it mentioned the symmetry about the vertical midline, especially the images that have strong diagonal components, but this conclusion is based on a few specific examples (such as columns 1 and 11).

4. In line 354, the analysis mentioned that the "animal nature" of animal images sometimes disappeared under mirror conditions, but it is not clearly stated whether this is consistent with the difference between the hemisphere between the hemisphere. 

5. The authors rely on a straightforward ridge regression model to align EEG embeddings with CLIP(Radford, et al., 2021), raising concerns about whether such a simplistic encoding structure can sufficiently capture the complex spatial and temporal dependencies inherent in EEG data. The reconstruction pipe used in this paper doesn't contain much of a trick, the framework failed to provide images with richer information to do some complex tasks. But it turned out to be much better than previous methods, and I doubt it.

6. The discussion of scalp-asymmetry effects is superficial, lacking the necessary depth and rigor. Furthermore, the placement of key figures, such as Figure 3(d), could be optimized for reader accessibility, as its current location disrupts the flow and readability of the analysis.

### Questions
1. I would like to see a broader range of examples demonstrating the types of reconstructions achieved by your pipeline. Could you provide additional examples or case studies that illustrate its applicability and effectiveness?

2. Asking author to justify the impressive EEG encoding performance achieved with such a simple ridge regression model? What underlying principles or characteristics of the EEG data allow this approach to succeed, despite its simplicity?

3. Can author elaborate on any theoretical insights or assumptions that guided the design of your model? A clearer connection between your method and the principle would strengthen your contributions.

### Soundness
2

### Presentation
2

### Contribution
3
