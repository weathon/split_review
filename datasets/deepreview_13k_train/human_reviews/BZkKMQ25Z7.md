# fMRI-PTE: A Large-scale fMRI Pretrained Transformer Encoder for Multi-Subject Brain Activity Decoding

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
The exploration of brain activity and its decoding from fMRI data has been a longstanding pursuit, driven by its potential applications in brain-computer interfaces, medical diagnostics, and virtual reality. Previous approaches have primarily focused on individual subject analysis, highlighting the need for a more universal and adaptable framework, which is the core motivation behind our work.
In this work, we propose fMRI-PTE, an innovative auto-encoder approach for fMRI pre-training, with a focus on addressing the challenges of varying fMRI data dimensions due to individual brain differences. Our approach involves transforming fMRI signals into unified 2D representations, ensuring consistency in dimensions and preserving distinct brain activity patterns. We introduce a novel learning strategy tailored for pre-training 2D fMRI images, enhancing the quality of reconstruction. fMRI-PTE's adaptability with image generators enables the generation of well-represented fMRI features, facilitating various downstream tasks, including within-subject and cross-subject brain activity decoding. Our contributions encompass introducing fMRI-PTE, innovative data transformation, efficient training, a novel learning strategy, and the universal applicability of our approach. Extensive experiments validate and support our claims, offering a promising foundation for further research in this domain.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces fMRI-PTE, an auto-encoder-based pretraining framework for fMRI data that addresses the challenge of varying data dimensions across individuals by transforming brain signals into standardized 2D representations. This approach not only ensures dimensional consistency but also preserves the uniqueness of brain patterns, incorporating a new learning strategy that improves reconstruction quality for both within-subject and cross-subject decoding tasks. Validated by extensive experiments, fMRI-PTE stands out for its adaptability and universal application, presenting a significant step forward for research in brain activity analysis and its potential high-impact applications.

### Strengths
1. Innovative Use of Large Pretraining Datasets: The paper presents a promising and innovative approach by leveraging large pretraining datasets to enhance performance on smaller downstream tasks. This strategy is particularly interesting as it can potentially unlock new capabilities in machine learning models by exploiting the rich information present in expansive datasets to benefit tasks with limited data availability.
2. Effective Dimensionality Reduction Technique: The methodology for transforming fMRI signals into a uniform 2D format is a commendable strength of the paper. 
3. Exploration of a Cutting-edge Application: The task of decoding visual signals from fMRI data is an engaging and cutting-edge application that stands out in the paper. The pursuit of this task is highly relevant to advancing the intersection of neuroscience and artificial intelligence, and it holds significant promise for future developments in brain-computer interfaces and medical diagnostic techniques.

### Weaknesses
1. Insufficient Empirical Evaluation: The paper needs to include some important ablation experiments to validate the proposed model. For example, while the authors mention a baseline 'LR' in Sec 4.2.2, it is unclear how this directly isolates the impact of the fMRI pre-trained encoder. A more rigorous ablation would involve systematically removing components of the pre-training process (e.g., the specific loss functions or the architecture of the encoder itself) to understand their individual contributions. The current evaluation does not provide sufficient evidence to demonstrate the necessity of each design choice.
2. Unclear Methodology Description: The complexity of the training process is not adequately described in the current methodological section. The paper needs to include more detailed equations and procedural explanations to delineate the training steps precisely. For example, the specific forms of the loss functions used in both stages of training, and how they are weighted, are not provided. Furthermore, the exact mechanism of how the quantized feature indices are generated and fed into the second-stage encoder requires further clarification. The current description lacks the necessary detail for reproducibility.
3. Presentation and Terminology Issues: The paper's presentation suffers from the use of abbreviations that are not clearly defined, which can lead to confusion and misinterpretation. (See in Question 1 and 5) The use of 'L' and 'C' to represent both 'batch size' and 'the number of tokens' is confusing and needs to be clarified. The description of the second-stage encoder input is vague, lacking specific details about the feature dimensions and the quantization process.
4. Lack of Supplementary Materials: For a paper detailing a complex training process, the absence of source code is a significant drawback. The provision of the actual code would greatly aid others in replicating the study. This support material is often crucial for peer reviewers and practitioners who wish to validate the claims or extend the work.

### Questions
1. "our methodology involved an initial conversion of GLM", please provide the full name of "GLM".
2. "Here, L and C represent batch size, the number of tokens, and feature dimensions." Why do two symbols, L and C, correspond with three definitions?
3. Can you explain what the input of "the encoder \Epsilon_2" is? Please provide symbols and feature dimensions to describe the input.
4. Can you provide the code and pre-train model to enlarge the work impact?
5. In Table 4, what is the meaning of column "M" and its value, "T" and "V".

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel fMRI pre-training strategy, fMRI-PTE, for brain decoding. It entails the conversion method, which converts the volume or surface-wise fMRI image into a 2D image, and a self-supervised pre-training strategy that generates well-represented fMRI features. Additionally, this strategy facilitates various downstream tasks, including within-subject and cross-subject brain activity decoding.

### Strengths
- The authors have transformed fMRI signals into a 2D image format, potentially capturing low- and high-frequency signal variations as patterns. This method may also reduce computational costs compared to traditional approaches that linearize whole-brain voxels into 1D vectors.
- Employing the resting-state fMRI data for pre-training may enable the model to encompass a wide range of intrinsic individual brain information, which could potentially enhance the model’s performance on various downstream tasks.
- The study shows impressive reconstruction results.

### Weaknesses
 - While the authors argue that their proposed method has its advantages over the existing methods, e.g., MBM, in the field, to this reviewer, it just exploits the existing methodologies for the problem of interest, fMRI-based brain decoding. In this regard, the methodological innovation is marginal, raising concern about its suitability for presentation in ICLR.
- Their “innovative data transformation” onto 2D brain activation images seems trivial. It uses the existing mapping method.
- There should be a more rigorous explanation and analysis of the contributions of their efficient training and learning strategy. To this reviewer, those are not clear.
- In Figure 1, the GPT model is included in both the ‘foundation model training’ and ‘downstream application’ parts. While the ViT is mentioned in ‘3.2.2 Transformer compression’ as being used in the encoder, the GPT is only mentioned in the introduction and lacks details in the method part.
- The ‘downstream application’ part in Figure 1 includes the ‘image decoder’ module. It seems to be an additional pre-trained model using natural images. However, the paper does not include sufficient details about it.
- It would be beneficial to provide information about the kernel size. Some brain regions, such as V6A and LO2, are quite small (Figure 3). If the kernel size is too big, it may be difficult to get the relationships between these small regions and other regions. This is because the small regions could potentially merge with other adjacent regions. Therefore, it would be better to specify the kernel size and its significance.
- In Table 2, the authors present the one-to-one cross-subject brain decoding results for specific pairs (i.e., 7 → 1, 5 → 2, 1 → 5, and 2 → 7), but the method for choosing these pairs is not clear. It would be informative to evaluate the results for one-to-one cross-subjects by examining the reverse directions or by calculating the average values for each source across all other target cases (e.g., from 7 to 1, 2, and 5, respectively) to determine the efficacy of the model/strategy for this task.

### Questions
- In the second sentence of the third paragraph under ‘3.2.2 Transformer Compression’, the two variables ‘L’ and ‘C’ are mentioned, which seem to be related to the number of tokens and feature dimensions, respectively. However, while the batch size is also mentioned, no corresponding variable seems to be provided.
- Presenting the brain visualizations with a color scale and matching their scales for the overall comparisons may improve the clarity of the results.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript proposes an autoencoder-based approach (fMRI-PTE) to brain decoding. The experiments show improved fMRI reconstruction performance and better brain decoding results on the NSD dataset across multiple metrics compared to previous baselines. The VQGAN approach for image synthesis inspired the proposed architecture.

### Strengths
- Multiple baselines
- Multiple experiments for one upstream and one downstream task.

### Weaknesses
 - The manuscript lacks a strong baseline for the NSD dataset: MindEye (Scotti et al., 2023).
- The foundational model and universal applicability claims are not well supported, as the manuscript has not explored the model's scaling capabilities. It has been trained and evaluated on two datasets and one downstream task (brain decoding), while there are other tasks in brain studies. Furthermore, no zero-shot capabilities have been explored. Lastly, no analysis has been performed to validate whether the performance is reliable across demographics.
- Innovative Data Transformation is not novel.
   - It is a known procedure. Otherwise, the 32k_fs_LR toolboxes will not be available (https://netneurolab.github.io/neuromaps/index.html, https://github.com/DiedrichsenLab/fs_LR_32).
   - The better-performing MindEye (Scotti et al., 2023) used voxels. But there are other ways to transform 4D fMRI to 2D data by using DiFuMo (Dadi et al., 2020), Neuromark (Du et al., 2020), or Spectral Clustering (Geenjaar et al., 2022). These methodologies could be ablated. 
- Claims about preserving high-frequency signals are confusing and are not discussed with corresponding literature. Note each time point is acquired for 1.5 seconds at UKBioBank. The fMRI is highly undersampled and, most importantly, noisy. It is not that easy in general (Trapp et al., 2018). Hence, the manuscript needs to be more specific about that. For evaluation, you can ensure that you reconstruct frequency modes (e.g., Yuen et al., 2019). You can also consider the works from the speech domain to ensure frequency reconstructions (Kumar et al., 2023; Yamamoto et al., 2020).
- Additionally, you need to validate the claim about spatial interaction across brain regions. An evaluation could ensure the static/dynamic functional connectivity is preserved after reconstruction.


- References:
  - Dadi, Kamalaker, et al. "Fine-grain atlases of functional modes for fMRI analysis." NeuroImage 221 (2020): 117126. https://parietal-inria.github.io/DiFuMo/
  - Du, Yuhui, et al. "NeuroMark: An automated and adaptive ICA based pipeline to identify reproducible fMRI markers of brain disorders." NeuroImage: Clinical 28 (2020): 102375.
  - Geenjaar, Eloy, et al. "Spatio-temporally separable non-linear latent factor learning: an application to somatomotor cortex fMRI data." arXiv preprint arXiv:2205.13640 (2022).
   - Trapp, Cameron, Kishore Vakamudi, and Stefan Posse. "On the detection of high-frequency correlations in resting state fMRI." Neuroimage 164 (2018): 202-213.
   - Yuen, Nicole H., Nathaniel Osachoff, and J. Jean Chen. "Intrinsic frequencies of the resting-state fMRI signal: the frequency dependence of functional connectivity and the effect of mode mixing." Frontiers in Neuroscience 13 (2019): 900.
   - Kumar, Rithesh, et al. "High-Fidelity Audio Compression with Improved RVQGAN." arXiv preprint arXiv:2306.06546 (2023).
   - Yamamoto, Ryuichi, Eunwoo Song, and Jae-Min Kim. "Parallel WaveGAN: A fast waveform generation model based on generative adversarial networks with a multi-resolution spectrogram." ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2020.
    - Scotti, Paul S., et al. "Reconstructing the Mind's Eye: fMRI-to-Image with Contrastive Learning and Diffusion Priors." arXiv preprint arXiv:2305.18274 (2023).

### questions:
 - The MAE baseline is confusing and not comparable. In MAE, they use lighter decoders, and improving reconstruction did not improve the downstream performance; hence, they did not focus on reconstruction. In addition, a higher masking ratio leads to situations where the objects are not reconstructed. 
- I did not find details for the preprocessing of the fMRI dataset since there is no appendix. Have you applied motion correction and aligned the fMRI to the reference volume?

Rigor:
- Lack of variability (STD, SE, or IQR) in Table 2, Table 3, and Table 4.
- Lack of statistical analysis to compare models.

Clarity:
- The text is too wordy and not specific enough.

### Questions
- The MAE baseline is confusing and not comparable. In MAE, they use lighter decoders, and improving reconstruction did not improve the downstream performance; hence, they did not focus on reconstruction. In addition, a higher masking ratio leads to situations where the objects are not reconstructed. 
- I did not find details for the preprocessing of the fMRI dataset since there is no appendix. Have you applied motion correction and aligned the fMRI to the reference volume?

Rigor:
- Lack of variability (STD, SE, or IQR) in Table 2, Table 3, and Table 4.
- Lack of statistical analysis to compare models.

Clarity:
- The text is too wordy and not specific enough.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors train an autoencoder architecture in a self-supervised way on a large dataset of fMRI recordings (UK BioBank) in order to create a general model that could be readily used to solve downstream neuroinformatic tasks. They first test the reconstruction capability of their method, achieving results (in terms of correlation, SSIM and MSE) comparable to those obtained with alternative methods. They then test the proposed method using an image decoding task based on the Natural Scenes Dataset (NSD) and compare its performance with other possible architectures (e.g., MAE, LEA) using a variety of evaluation metrics, reporting favorable results.

### Strengths
-	The article is generally readable, and the research work is well-motivated.
-	Building large-scale foundation models for fMRI data would constitute a valuable asset to more effectively process neuroimaging data.

### Weaknesses
-	Though the manuscript is readable, the research goals are often unclear or framed in a general way. For example, the title puts emphasis on “brain activity”, but in fact the results only refer to “cortical activity” (surface data), and the main results more specifically focus on a visual decoding task.
-	There are several methodological details that require clarification (see questions below).
-	The proposed architecture involves the combination of several modules and training phases; more quantitative analyses (e.g., by means of ablation studies) should be performed to justify each design choice.
-	The authors should more clearly explain how their “fMRI-PTE” architecture differs from masked auto-encoder architectures used in the deep learning literature and from recent architectures specifically introduced to model neuroimaging data. In general, the authors use vague sentences such as “our proposed fMRI-PTE distinguishes itself through its unique merits and innovations” that do not allow to clearly understand why and how their two-stage architecture should work better than existing (and possibly simpler) ones. More systematic ablation studies on the fMRI-PTE architecture would help clarify this.
-	The authors should similarly explain how their “innovative approach to transform fMRI signals into unified representations by projecting them onto 2D brain activation images” differs from standard methods that allow mapping 3D fMRI volumes into 2D surface (cortical) representations. From the authors’ description, it seems they are just adopting standard preprocessing pipelines that convert MNI volumes to surface activations.
-	I do not agree that the pipeline in Fig. 1 is self-explanatory and meticulously depicted. The caption should at least explain the meaning of each model box, the reason why pre-processing using “downstream data” precedes the training of the foundation model, the meaning of the “fires” and “iced” symbols, etc. etc. Also, why is there a block named “GPT”? Such a model is never mentioned in the manuscript.
-	More details about the specific vector quantization approach are required to fully understand the feature extraction process. What happens if the features are not quantized? This should also be inspected by ablation studies.
-	The role of each loss term (perceptual, adversarial, reconstruction, and commitment) should be investigated more in detail to establish whether such combination is really required to improve performance. The authors should consider ablating each loss term individually and in combinations to assess their relative contributions.
-	Why is a Vision Transformer required to compress the quantized indices? It would be useful to also investigate simpler autoencoder architectures. The justification for this design choice is not clear and should be supported by experimental evidence, such as comparing performance with a linear layer or a simple MLP.
-	Table 1: “The subscript represents the dimension of the compression feature.” I do not see any subscript in the table. Furthermore, the differences with respect to existing methods seem quite marginal.
-	For the decoding task, the authors mention that they selected a subset of Visual ROIs. However, from the current description it is not clear how such subset of the surface data was given as input to the pre-trained model (which, from my understanding, expects as input the entire cortical image).
-	The images in Fig. 3 suggest that the input is just the subset of Visual ROIs shown in Fig. 2. However, I am a bit puzzled by the overall poor reconstruction accuracy of MAE, which suggests that such architecture has been trained in a sub-optimal fashion. It is unclear if the MAE was trained with the same data and for the same number of epochs as the proposed method, which could explain the discrepancy in performance.
-	“Implemental Details” should be described in the Methodological section, not in the Results section.
-	English phrasing and grammar could be improved. Just as an example, in the abstract the authors write that they introduce a novel learning strategy “tailored for pre-training 2D fMRI images”. It’s not the images that are pre-trained, but rather a model of these images. I strongly recommend the authors to carefully check the entire document to improve the construction of sentences, at the same time avoiding unnecessary repetitions (for example, there is also a little abuse of the terms “intricacies” and “intricate”, which are repeated several times, often within the same paragraph).
-	Some acronyms are used before being explicitly introduced.

### Questions
-	The authors should more clearly explain how their “fMRI-PTE” architecture differs from masked auto-encoder architectures used in the deep learning literature and from recent architectures specifically introduced to model neuroimaging data. In general, the authors use vague sentences such as “our proposed fMRI-PTE distinguishes itself through its unique merits and innovations” that do not allow to clearly understand why and how their two-stage architecture should work better than existing (and possibly simpler) ones. More systematic ablation studies on the fMRI-PTE architecture would help clarify this.
-	The authors should similarly explain how their “innovative approach to transform fMRI signals into unified representations by projecting them onto 2D brain activation images” differs from standard methods that allow mapping 3D fMRI volumes into 2D surface (cortical) representations. From the authors’ description, it seems they are just adopting standard preprocessing pipelines that convert MNI volumes to surface activations.
-	I do not agree that the pipeline in Fig. 1 is self-explanatory and meticulously depicted. The caption should at least explain the meaning of each model box, the reason why pre-processing using “downstream data” precedes the training of the foundation model, the meaning of the “fires” and “iced” symbols, etc. etc. Also, why is there a block named “GPT”? Such a model is never mentioned in the manuscript.
-	More details about the specific vector quantization approach are required to fully understand the feature extraction process. What happens if the features are not quantized? This should also be inspected by ablation studies.
-	The role of each loss term (perceptual, adversarial, reconstruction, and commitment) should be investigated more in detail to establish whether such combination is really required to improve performance.
-	Why is a Vision Transformer required to compress the quantized indices? It would be useful to also investigate simpler autoencoder architectures.
-	Table 1: “The subscript represents the dimension of the compression feature.” I do not see any subscript in the table. Furthermore, the differences with respect to existing methods seem quite marginal.
-	For the decoding task, the authors mention that they selected a subset of Visual ROIs. However, from the current description it is not clear how such subset of the surface data was given as input to the pre-trained model (which, from my understanding, expects as input the entire cortical image).
-	The images in Fig. 3 suggest that the input is just the subset of Visual ROIs shown in Fig. 2. However, I am a bit puzzled by the overall poor reconstruction accuracy of MAE, which suggests that such architecture has been trained in a sub-optimal fashion.
-	“Implemental Details” should be described in the Methodological section, not in the Results section.
-	English phrasing and grammar could be improved. Just as an example, in the abstract the authors write that they introduce a novel learning strategy “tailored for pre-training 2D fMRI images”. It’s not the images that are pre-trained, but rather a model of these images. I strongly recommend the authors to carefully check the entire document to improve the construction of sentences, at the same time avoiding unnecessary repetitions (for example, there is also a little abuse of the terms “intricacies” and “intricate”, which are repeated several times, often within the same paragraph).
-	Some acronyms are used before being explicitly introduced.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
