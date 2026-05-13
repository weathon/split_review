# Toward Generalizing Visual Brain Decoding to Unseen Subjects

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Visual brain decoding aims to decode visual information from human brain activities. Despite the great progress, one critical limitation of current brain decoding research lies in the lack of generalization capability to unseen subjects. Prior works typically focus on decoding brain activity of individuals based on the observation that different subjects exhibit different brain activities, while it remains unclear whether brain decoding can be generalized to unseen subjects. This study aims to answer this question. We first consolidate an image-fMRI dataset consisting of stimulus-image and fMRI-response pairs, involving 177 subjects in the movie-viewing task of the Human Connectome Project (HCP). This dataset allows us to investigate the brain decoding performance with the increase of participants. We then present a learning paradigm that applies uniform processing across all subjects, instead of employing different network heads or tokenizers for individuals as in previous methods, which can accommodate a large number of subjects to explore the generalization capability across different subjects. A series of experiments are conducted and we have the following findings. First, the network exhibits clear generalization capabilities with the increase of training subjects. Second, the generalization capability is common to popular network architectures (MLP, CNN and Transformer). Third, the generalization performance is affected by the similarity between subjects. Our findings reveal the inherent similarities in brain activities across individuals. With the emerging of larger and more comprehensive datasets, it is possible to train a brain decoding foundation model in the future.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a new brain decoding paradigm for zero-shot brain decoding. Multiple experimental design exposes that brain decoding models can be generalized from existing subjects to unseen subjects.The effect of inter-subject similarity, such as gender, on generalization ability is discussed for the first time.

### Strengths
1. This paper is well written and easy for the reader to read.
2. The motivation for the zero-shot setting is interesting.
3. The experimental design is very rich with multiple validations. Readers are inspired by explorations of the impact of gender.
4. In a sense, integrating the new dataset breaks the routine of NSD data use and is contributory.

### Weaknesses
1. From the point of view of machine learning, the algorithms for brain decoding in this paper are basically existing methods. The use of downsampling to obtain voxels of uniform size across multiple subjects has been used, e.g. CLIP-MUSED [1] uses PCA downsampling to align different subjects, also without additional training. 
2. The methodology mentioned by the authors was not compared to any relevant studies quantitatively. The methods mentioned by the authors were not compared to any relevant studies, so it is difficult to comparatively measure whether the methods proposed by the authors are more effective or not. There are actually a subset of papers that have performed the appropriate anatomical alignment for zero-shot brain decoding[2, 3, 4]. Because of open source issues, a full reproduction may be a bit difficult, but small designs such as the use of **fsaverage** are easy to implement (fsaverage is already widely used in neuroscience). 
3. While the new integrated dataset makes sense, it seems to me that a neuroscience research task without algorithmic design requires a dataset of its own design. I think this is missing in this paper. And the decoding task is very simple, containing only the retrieval task. Although the authors mention that the method can be generalized to the reconstruction task, a glance at related papers on the same method makes it hard for me to be convinced (the same method using downsampling fails miserably on the reconstruction task).

### Questions
I don't really agree with your statement in lines 506-508 of Section 4.6 that the poor generalization of the method on the NSD dataset is due to the problem of too few subjects. It seems to me at the moment that the integrated new dataset is consistent across all visual stimuli viewed by all subjects. So even for unseen subjects, the model is trained with the images that unseen subjects 'see'. However, for the NSD dataset, the images seen by different subjects, although they are all COCO images, are not the same in the training set. Therefore, in the absence of any comparison of related methods, how can it be proved that the method proposed in this paper is better not due to the difference in dataset ?

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
3

### Summary
The paper explores cross-subject visual brain decoding, specifically focusing on scenarios where no data from unseen subjects are included in the training model. The contributions are twofold: first, the authors propose an effective, straightforward approach to generate image-fMRI data at scale using the HCP video viewing dataset. Second, they introduce a decoding method based on CLIP encoding combined with cosine similarity decoding. Although the approach is admittedly simple, it is practical and well-justified.

### Strengths
The writing is clear, and the rationale is logical. The question of alignment across subjects, which the paper addresses, is timely and aligns with topics discussed at prominent venues.

### Weaknesses
The decoding methodology is likely the paper’s most relevant contribution to ICLR, though I have identified two significant limitations in this area.

Firstly, the authors show that incorporating data from additional subjects in training improves the model's performance, interpreting this as a solution to the alignment problem in neuroAI. In this field, we frequently encounter issues with requiring identical input-output pairs across subjects. While the authors suggest that their method mitigates this problem, they do not explain how. Is it possible that the model simply learns shared noise inherent to the videos across subjects as the data pool increases? We know that functional alignment remains a challenge because brain responses vary at the voxel level, even if the encoded information is similar across the whole region. It is unclear how, if at all, the proposed method addresses this challenge. Specifically, the authors do not address the potential for overfitting to shared, non-neural features present in the video stimuli, which could explain the observed performance gains with more subjects. The model might be learning to predict aspects of the video itself, rather than the underlying neural representations, leading to spurious correlations that do not generalize well to novel stimuli or tasks.

Secondly, the paper lacks a direct comparison with other state-of-the-art methods, which the authors partially review in the introduction. Could alternative methods achieve similar or even better performance? The authors suggest that other methods are computationally expensive in terms of parameters and training, yet they do not provide specific details. Quantitative comparisons and a more in-depth analysis of parameter costs are essential to substantiate this claim. Furthermore, the absence of a comparison to methods that explicitly address inter-subject variability, such as those employing hyperalignment or representational similarity analysis, makes it difficult to assess the true novelty and effectiveness of the proposed approach. Without such benchmarks, it is unclear whether the reported improvements are significant or merely reflect the benefits of increased training data.

### Questions
Please provide a detailed rationale explaining why adding more subjects is beneficial. Specifically, how does this approach address the alignment problem? A clear explanation would help clarify the method's impact on the cross-subject variability and functional alignment issues inherent to neuroAI.

Please compare the performance of the proposed method with at least two other state-of-the-art approaches. This comparison would help establish its relative effectiveness and efficiency, particularly in terms of computational costs, accuracy, and robustness across subjects.

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
4

### Summary
The paper explores the generalization properties of visual decoding models when trained and tested on different subjects. Different model architectures (3D ConvNet, 1D ConvNet, Transformer, MLP) were trained on subsets of a dataset containing fMRI brain activity data collected while subjects watched audio-visual movies. Models were trained to recover the seen video frame out of a batch of images. The use of an upsampling step made it possible to reuse a single model across all subjects (vs. subject-specific layer in previous work). Results show that model performance increases as more subjects are seen during training, and that distribution shift between training and test subjects can negatively affect performance.

### Strengths
* Originality: While the proposed methodology is similar to previous work, the paper studies a setting (generalization across multiple subjects) which has not been explored much before. The analysis of the impact of training data composition (gender bias and of train-test set similarity) is also interesting and original.
* Quality: The paper is of good quality and presents relevant experiments to support the claims made by the authors.
* Clarity: The paper is overall well and clearly written, and the problem setting is well introduced and supported.
* Significance: The results are promising and motivate further scaling up of brain activity datasets.

### Weaknesses
1. The description of the dataset curation and test set sampling procedure lacks details (see Q1-2). As movie frames are likely correlated and do not cover the same semantic space as “standard” brain-image datasets (in which the images are selected to cover varied categories, e.g. NSD), it is unclear whether the models might in fact overfit to the specific scenes seen in the training set. This could have an impact on the absolute performance values reported in the paper. Specifically, the lack of control over scene overlap between training and test sets introduces a potential confound. If frames from the same scene are present in both training and test sets, the model's performance might be inflated due to its ability to memorize specific visual features of those scenes, rather than generalizing to unseen visual content. This is especially concerning given the relatively limited number of distinct scenes within a typical movie, which could lead to a form of scene-specific overfitting.
2. There is also missing information about the architectures (upsampling procedure, number of parameters, hyperparameter selection procedure; see Q4-5). The lack of detail regarding the upsampling method makes it difficult to assess its potential impact on the results. Bicubic interpolation, while simple, can introduce artifacts that might affect the quality of the reconstructed images. Furthermore, the absence of information on the number of parameters for each model architecture makes it challenging to compare the models fairly. The hyperparameter selection process is also crucial, as it can significantly influence the performance of the models. Without a clear description of this process, it is difficult to evaluate the robustness and reliability of the results.

### Questions
1. The use of a video dataset to define an image retrieval task is interesting, however the distribution of images obtained by sampling frames every 1 s might be biased in a way that influences the interpretation of the results. Given frames within a scene are likely significantly correlated, the level of difficulty of the retrieval task on the test set will vary a lot if examples are strictly sampled from different scenes or not. Were the test images sampled uniformly across the 3127 images? A helpful visualization might be a grid of all sampled test images.
2. Similarly, if a frame $i_j$ from was selected to be part of the test set and the surrounding frames that are part of the same scene (e.g. $i_{j-1}$ and $i_{j+1}$, which could be very similar to $i_j$ if the visual stimulus changes slowly) end up in the training set, there is a strong potential for overfitting. Could this be the case here?
3. Averaging the 4-s window after the target frame is likely suboptimal as this misses the second half of the peak response (occuring at 4-s according to the reference cited). Have the authors looked at different pooling strategies (e.g. averaging seconds 2 to 6)?
4. How many parameters do the different model configurations have? How were the hyperparameters selected? For instance I find it surprising that such a large Transformer was used (24 layers according to Suppl. Figure 4).
5. What upsampling methodology was used?
6. Previous studies on the NSD dataset relied on precomputed beta values obtained through a GLM fitting procedure that help improve SNR. Can the authors confirm whether the “whole-brain” data they used is also betas or is it BOLD signals? This could also be a more likely explanation for the discrepancy between results on NSDGeneral and “Whole-brain” data in Table 6.
7. How were the images of Suppl Figure 1 selected? Are these retrieval results representative of the other images in the test set?
8. Other comments:
- At line 39, Benchetrit et al. 2023 is cited as an example of fMRI visual decoding, however they used MEG.
- In the last sentence of the conclusion, the authors probably meant to say “a brain decoding foundation model” (instead of “encoding”) as brain encoding would instead mean reconstructing brain activity from the stimuli.

### Soundness
2

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
The paper aims to tackle the challenge of visual brain decoding with a focus on improving generalization across a broader population of subjects. The authors generate a new dataset based on the HCP dataset, where image-fMRI pairs are derived from the last frame of each second in a movie, with the fMRI signals averaged over a specific time window. To map brain signals to the CLIP embeddings of corresponding images, they employ a contrastive learning approach. The discrepancy in voxel counts among subjects is addressed through a straightforward upsampling technique. Furthermore, the authors propose a novel architecture designed to mitigate the exponentially increasing model size typically required by state-of-the-art methods when integrating additional subjects into the pipeline.

### Strengths
The paper aims to address two major challenges in the field of visual brain decoding: the scarcity of existing datasets and the potential scalability issues of current pipelines when expanding to a larger number of subjects. However, the evidence provided for the proposed method is insufficient to fully support its effectiveness in tackling these problems.

### Weaknesses
1) I have concerns regarding the dataset generation methodology. It appears that the fMRIs generated for each image may not accurately capture the brain's response to the specific features of those images. Specifically, the resulting fMRI signals seem to reflect an accumulation of activity from prior stimuli, rather than providing a clear, one-to-one representation of the neural response to individual image features. This raises questions about whether the fMRI data truly aligns with the visual stimuli as intended.

2) The validity of the generated dataset is questionable, particularly given the notable performance disparity observed between the NSD dataset and the paper's dataset (as noted in Table 2, row 1, compared to Table 6, row 2). It is unclear why there is such a significant difference, raising concerns about potential biases or inconsistencies in the data generation process that may not accurately reflect the neural representation of the images.

3) In line 485, the paper reports MindEye 1's top-1 accuracy as 84%. However, according to Scotti et al. (2024a), MindEye 1 achieved a top-1 accuracy of 93.1% for image retrieval and 90.1% for brain retrieval (Table 1, row 5). In contrast, Scotti et al. (2024b) present MindEye 1's results as an average across four individual models (Table 1, row 3). Therefore, despite the mention of "our implementation" in line 488 which is unclear, it appears that this approach does not surpass the current state-of-the-art performance.

4) Lines 51-52 suggest that hand-picking voxels is not ideal for data collection, yet the results in Table 6 (columns 5 and 7) demonstrate the superiority of this approach. This discrepancy raises questions about the claim. It is plausible that 'whole-brain' data could contain a significant amount of redundancy or noise, as suggested by prior research (Lin et al. "Redundancy and dependency in brain activities." Shared Visual Representations in Human & Machine Intelligence (2022).), which may explain the better performance of the hand-picked voxel strategy.

5) Table 6, row 7, indicates extremely poor performance, raising doubts about the pipeline’s ability to generalize effectively. In contrast, Scotti et al. (2024b), Table 1, row 7, report significantly better results even with a subset of the data. To strengthen the evaluation, a clear comparison between the proposed approach and MindEye2 is essential, as it would help clarify the relative effectiveness of the proposed method.

6) As the authors noted, previous studies have employed various methods to address the discrepancies in voxel counts across subjects, such as creating a common representational space (e.g., Scotti et al., 2024b). However, it is unclear how a simple upsampling approach effectively manages the differences in fMRI signals among subjects. More details are needed on the implementation of the upsampling process. Additionally, an in-depth analysis comparing upsampling to existing alignment methods (e.g., functional alignment, anatomical alignment, common representational space) is necessary to understand whether it can truly serve as a viable alternative.

### Questions
In addition to addressing the previously mentioned weaknesses, the following questions should be clarified to strengthen the paper:

Are there any validation checks that confirm whether the fMRI signals accurately reflect the intended neural responses to individual images?

Are there specific characteristics of whole-brain data that introduce redundancy or noise, which might explain the superior results of the hand-picked voxel approach?

In lines 66-67, it is stated that “the model becomes increasingly complex as the number of subjects increases, making it challenging to scale to a larger population,” referring to state-of-the-art architectures. It would be valuable to include a comparison of model size (in terms of the number of parameters) between the proposed approach and existing architectures. Such a comparison would help highlight the scalability advantages of the proposed model more clearly.

### Soundness
1

### Presentation
2

### Contribution
1
