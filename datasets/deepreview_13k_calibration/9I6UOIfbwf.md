# Video Face Re-Aging: Toward Temporally Consistent Face Re-Aging

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Video face re-aging deals with altering the apparent age of a person to the target age in videos. This problem is challenging due to the lack of paired video datasets maintaining temporal consistency in identity and age. Most re-aging methods process each image individually without considering the temporal consistency of videos. While some existing works address the issue of temporal coherence through video facial attribute manipulation in latent space, they often fail to deliver satisfactory performance in age transformation. To tackle the issues, we propose (1) a novel synthetic video dataset that features subjects across a diverse range of age groups; (2) a baseline architecture designed to validate the effectiveness of our proposed dataset, and (3) the development of novel metrics tailored explicitly for evaluating the temporal consistency of video re-aging techniques. Our comprehensive experiments on public datasets, including VFHQ and CelebA-HQ, show that our method outperforms existing approaches in age transformation accuracy and temporal consistency. Notably, in user studies, our method was preferred for temporal consistency by 48.1\% of participants for the older direction and by 39.3\% for the younger direction.

  \keywords{Face Editing \and Face Re-Aging \and Video Editing}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a novel approach to video face re-aging, focusing on altering the apparent age of individuals in videos while maintaining temporal consistency. Key contributions include the creation of a synthetic video dataset, a baseline architecture leveraging recurrent blocks for temporal coherence, and the introduction of new metrics for evaluating age transformation quality.

### Strengths
1.	Innovative Data Generation Pipeline: The authors designed a comprehensive pipeline for generating a synthetic dataset specifically for model training in video face re-aging. This pipeline addresses the challenge of obtaining paired video data with consistent identities and varying ages, thereby enhancing the quality and applicability of the training data.

2.	Introduction of New Evaluation Metrics: The development of two novel metrics, Time Region Wrinkle Consistency (TRWC) and Time-Age Preservation (T-Age), provides a more effective means of assessing the quality of age transformations in videos. These metrics focus on maintaining temporal coherence, offering a more nuanced evaluation compared to traditional methods, and contributing to the advancement of the field.

### Weaknesses
1. Lack of Detail Regarding the Synthetic Dataset: The authors provide insufficient information about their synthetic dataset. To enable a comprehensive evaluation, the authors should provide detailed information about the dataset's size, diversity (including the range of ages, facial features, and other relevant attributes), and visual samples. This would allow reviewers to assess the dataset's quality and its potential impact on the reported results. Specifically, the absence of details regarding the distribution of age ranges within the dataset makes it difficult to assess whether the model is robust across different age transitions or if it is biased towards certain age groups. Furthermore, information about the variability in facial features, such as ethnicity, face shape, and the presence of facial hair, is crucial to understand the generalizability of the proposed method.
2. Missing Information on Motion Generation: Section 3.1.3 on motion generation lacks clarity regarding the stopping condition for generating intermediate frames. A more precise explanation of this process is necessary for readers to fully understand the method. The description should clarify whether the number of intermediate frames is fixed or adaptive based on the difference between keyframes. Moreover, the method should specify how the motion is interpolated between keyframes, whether it is a linear interpolation or a more complex method, and how this interpolation affects the temporal consistency of the generated video.
3. Unclear Availability of Resources: The authors do not explicitly state their intentions regarding the availability of the proposed dataset, pipeline code, or trained models. To enhance reproducibility and facilitate further research, it is strongly recommended that the authors publicly release these resources. Providing a link to a project page or repository, even if it's currently empty, would provide a clear indication of their commitment to open science. The lack of clarity on resource availability hinders the community's ability to build upon the proposed work and verify the reported results.
4. Limited Scope of Age Progression: The generated videos primarily exhibit age-related changes in the facial area, neglecting other important regions like hair and neck skin. This inconsistency detracts from the overall realism, as subjects appear to have mismatched facial and other features. The absence of age-related changes in hair color, texture, and hairline, as well as the lack of changes in neck skin texture and wrinkles, significantly limits the perceived realism of the re-aging process. This limitation suggests that the model is not fully capturing the holistic aging process.

### Questions
1.	Did you conduct quantitative comparisons with methods such as Diffusion VAE, and did you train these methods using your own dataset to evaluate their performance? If so, could you provide the relevant experimental results and analysis?
2.	Can you add new experiments to demonstrate the effectiveness of your newly constructed dataset? For example, by using a currently common technique to conduct experiments on both the existing dataset and the dataset you provided, and using the corresponding metrics to show that your newly constructed dataset can achieve better training results.
3.	Can you clearly articulated the specific benefits of training on videos for the face age reset method, which is essential for understanding the motivation behind choosing video training over static image training? The paper seems to imply the importance of temporal consistency, but it does not explicitly state the advantages of this approach in the context of videos. Could you please elaborate on these benefits to strengthen the motivational aspect of the research and to clarify why this method is innovative and significant compared to traditional static image training methods?

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
5

### Summary
In this paper, the authors address the Temporal consistency issue in Video Face-Aging Approaches.
To tackle this issue, the authors introduce:
(1) A video data generation pipeline to obtain a synthetic video dataset;
(2) A video face aging framework with recurrent U-Net structure; and
(3) Temporal Regional Wrinkle Consistency (TRWC) and Temporally Age Preservation metrics to validate the temporal consistency factor as well as age transformation over time.

Experiments are employed on CelebV-HQ and VFHQ datasets to show the advantages of the proposed approach.

### Strengths
- The paper addresses temporal consistency factor of video face aging. This is a challenging factor in this topic.
- The paper has introduced both data generation; architecture and metrics for video face aging.

### Weaknesses
The novelty of the paper is limited as most sections are "inspired" or "motivated" from previous approaches. 
Particularly:
- For data generation process, it relied on StyleGAN and SAM to generate aging results for single frames. Then OSFV technique is adopted to generate faces at different poses and expressions for key frames and motion generation for temporal smoothing.
- For video aging architecture, it is not novel as it is just a recurrent U-Net with commonly used losses.
The structure of the paper is more on putting multiple (previous) approaches together in an engineering manner rather than emphasizing on the novelty.

1. In line 475, "SAM fails to preserve attributes such as identity, pose and expression". However, the data generation relied on images generated by SAM (Eqn. (1)) and learn from that data. Moreover, this error will be further accumulated with OSFV method when poses and expressions presented. 
- What are technical details or modifications in the proposed approach that helps to mitigate the limitation of SAM in the data generation process? 
- Moreover, the authors should provide more discussions/ analysis on how the proposed approach can improve on attribute preservation. Quantitative comparison demonstrating these improvements over SAM is recommended.

2. There is no explicit constraint for consistency between frames during learning process. How can the trained network achieve the consistency when generating age-progressed frames?
Particularly:
- How can temporal consistency be enforced in the proposed approach? The authors should discuss about the details on architecture/loss functions that maintain this factor during learning/inference stages?
- Can we adopt TRWC metric as loss function for this ? 

3. In Eqn. (8), why do we need to validate on the generate image rather than Delta image? In other words, can Delta images be used directly to validate the similarity rather than compute that similarity on \hat{I} and normalize with real image.
The authors should analyze on the choice of using generated images instead of delta images and its effect on the metric values. An ablation study to compare the similarity/difference between these choices is recommended.

### Questions
Please address the concerns in Weaknesses section

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a simple GAN-based approach to generate a video of a subject at the target age. To maintain temporal consistency, the generator employs a recurrent architecture with U-Net blocks. This structure leverages both previous hidden states and generated frames, ensuring smooth transitions between ages. The model is trained using a combination of image and video discriminators, enhancing realism and temporal coherence.  Furthermore, the authors develop a pipeline for generating synthetic aging datasets and propose two new metrics for evaluating the temporal consistency of video re-aging methods.

### Strengths
1. Establishes a Strong Baseline: It introduces a new baseline for video re-aging, with novel contributions to architecture, dataset creation, and evaluation metrics. This provides a valuable foundation for future research in this area.
2. Demonstrates the Effectiveness of Synthetic Data: The proposed approach, while architecturally simple, effectively leverages synthetic video datasets to achieve compelling results. This highlights the potential of synthetic data for training re-aging models.
3. Provides Comprehensive Evaluation: Through extensive experiments, the authors convincingly demonstrate the realism and temporal coherence of their framework, using both qualitative and quantitative analysis.

### Weaknesses
1. Lack of Detail Regarding the Synthetic Dataset: The authors provide insufficient information about their synthetic dataset. To enable a comprehensive evaluation, the authors should provide detailed information about the dataset's size, diversity (including the range of ages, facial features, and other relevant attributes), and visual samples. This would allow reviewers to assess the dataset's quality and its potential impact on the reported results.
2. Missing Information on Motion Generation: Section 3.1.3 on motion generation lacks clarity regarding the stopping condition for generating intermediate frames. A more precise explanation of this process is necessary for readers to fully understand the method.
3. Unclear Availability of Resources: The authors do not explicitly state their intentions regarding the availability of the proposed dataset, pipeline code, or trained models. To enhance reproducibility and facilitate further research, it is strongly recommended that the authors publicly release these resources. Providing a link to a project page or repository, even if it's currently empty, would provide a clear indication of their commitment to open science.
4. Limited Scope of Age Progression: The generated videos primarily exhibit age-related changes in the facial area, neglecting other important regions like hair and neck skin. This inconsistency detracts from the overall realism, as subjects appear to have mismatched facial and other features.
See more detailed questions about the above weaknesses in the next section.

### Questions
1. Synthetic Dataset Details:
    a. Could you please provide more information about the size of your synthetic dataset, specifically the number of videos it contains?
    b. What is the average length of the generated videos in the dataset?
2. Motion Generation:
    a. In Section 3.1.3, you mention generating intermediate frames between keyframes. How many intermediate frames are typically generated?
    b. Is there a specific criterion or stopping condition that determines when to stop generating intermediate frames?
3. Spatial Masks:
    a. What is the purpose of the spatial masks M^inp and M^tar?
    b. Could you provide a visual example or description of these masks?
    c. Are they the same size as the input image I_t, and do they have the same value for all pixels?
4. Limitations in Age Progression: I noticed that the generated videos primarily show age-related changes in the facial area. Why does the proposed approach not generate changes in other regions, such as hair and neck skin? How might this limitation be addressed in future work?
5. Typos: I came across a few typos in the text, such as on line 311 and some symbols in Figure 2. Please ensure a thorough proofread to correct these errors.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, authors focus on video face re-aging task considering the temporal consistency. Most re-aging methods processed each image individually without integrating temporal dimension of videos due to the lack of paired video datasets for supervised training. Thus, an important contribution from authors is a novel synthesis video dataset created via proposed pipeline, it features many subjects with covering a diverse range of age groups.  Then, a baseline video face re-aging architecture is designed to validate the effectiveness of the proposed video dataset. Last but not least, two tailored novel metrics are developed for evaluating the temporal consistency of video face re-aging task.

### Strengths
10 existing state-of-the-art re-aging methods are compared in order to validate the efficacy of proposed synthesis video dataset and baseline architecture on public datasets, such as VFHQ and CelebV-HQ, as well as necessary ablation experiments. The paper is overall well written.

### Weaknesses
Although, a new paired video face re-aging dataset is essential for enhancing face re-aging technique and motivating relevant community. Overall, lack of novelty is disadvantage of this manuscript. First, video face re-aging dataset is constructed by a pipeline with three stages. Each of them focuses on off-the-shelf method, such as Style-based Age Manipulation (SAM) is chosen for image-based face re-aging, OSFV is chosen for key frame generation and FILM is chosen for motion generation. It is a general pipeline for constructing video dataset. Second, the proposed baseline architecture of video face re-aging is composed of off-the-shelf building block stacks. Such as recurrent block (RB) and Unet-based Encoder-Decoder. Even the input fashion of the proposed architecture is borrowed from Zoss et al, such as 5 channels with age masks, let alone the discriminator with PatchGAN proposed by Isola et al. Last but not least, the proposed Temporal-Age (T-Age) metric measures the age difference between two adjacent frames utilizing an off-the-shelf age classifier from Rothe at al.  In a short, this manuscript can be considered as a regular technical report, it has a gap to meet the novelty requirement for acceptance.

### Questions
There are some questions need to be clarified from authors.
1. In line 292, for image and video discriminator loss , how to explain there is no ground truth in total objective function when updating the discriminator loss ? 
2. In Table 1,  three image-based face re-aging methods are compared, is there no comparison with SAM? and how about video-based method, such as diffusion autoencoders (Preechakul et al.) ?
3. In Figure 4 (b), how to explain there is no CUSP results ?
4. In Table 2, how to explain there is no video-based face re-aging method in user study ?
5. In line 468, please give more detailed explanation about the sentence “ the significance of a 0.18 in TRWC in Table. 1 is evident by the user’s choices”
6. Overall, I can’t find more detailed meta information about the proposed video face re-aging dataset, such as how many identities or subjects, total duration of dataset and so on.

### Soundness
2

### Presentation
3

### Contribution
2
