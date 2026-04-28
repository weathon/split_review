# Emerging Tracking from Video Diffusion

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 6, 8, 5

## Abstract
We find video diffusion models, renowned for their generative capabilities, surprisingly excel at pixel-level object tracking without any explicit training for this task. We introduce a simple and effective method to extract motion representations from video diffusion models, achieving state-of-the-art tracking results. Our approach enables the tracking of identical objects, overcoming limitations of previous methods reliant on intra-frame appearance correspondence. Visualizations and empirical results show that our approach outperforms recent self-supervised tracking methods, including the state-of-the-art, by up to 6 points. Our work demonstrates video generative models can learn intrinsic temporal dynamics of video, and excel in tracking tasks beyond original video synthesis.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates using features from a generative video diffusion model for the task of label propagation in videos. The findings appear to point to using a combination of the image diffusion model and video diffusion model to yield good results.

### Strengths
(1) The reported results show improvement over prior works

(2) The motivating toy example is a great way to show the lack of temporal information that the paper is investigating.

### Weaknesses
#### Presentation
The paper is lacking in key details, specifically:
 1. What is the method? The closest paper that comes to the actual description of how the label is propagated is probably on L312, "recurrently predict labels for subsequent frames". Appendix A.1 is not much more helpful in explaining how tracking is performed; however, it suggests that the actual method is DIFT with just appended video features. The description lacks crucial details on how the pixel similarity is computed and how the labels are aggregated from previous frames. The paper should clarify if this is a nearest neighbor search in the feature space, or some other form of label propagation.
  2. What are the evaluation datasets? The paper mentions DAVIS, Kubric-Similar and Youtube-Similar; however, these datasets are not detailed, especially Kubric-Similar and Youtube-Similar, which seem to be new. Please include details of these datasets and how they were made/curated, including examples. For Davis, please indicate clearly which year and which "task" flavour (semi-supervised, probably) is being used. It is also unclear if the same splits are used as in prior work, which makes comparison difficult.

#### Contributions
 3. Some of the provided answers do not seem to be well supported. E.g. on L453 (Fig. 7 caption), it is stated that given the lack of appearance at a high noise level, Rv must capture temporal cues useful for tracking. However, temporal cues must be derived from appearance, which is obfuscated with noise. Similarly, it does not explain why it performs worse when there is no noise. Temporal ques are still available. It is also not clear how these experiments were performed, given the randomness involved; how many trials does each point in the graph represent? What are the variance bounds? The claim that motion cues are learned at high noise levels is not sufficiently justified. The paper needs to explain the mechanism by which the diffusion model learns to encode motion information from noisy inputs, and why this is more prominent at higher noise levels.
 4. It is also not clear what are the results in Fig. 9? Does each point correspond to the video or average over a dataset? Why does this positive correlation imply that training new video diffusion models will improve tracking? Does this hold for both SDV and I2V models? The paper should clarify if this correlation is consistent across different architectures and datasets, or if it is specific to the I2V model and the datasets used.
 5. The methods reported in Table 2 for supervised are rather old and might leave a false impression of the difference in the performance of supervised vs unsupervised. Looking at the DAVIS 2020 challenge [1] (Davis 2017 is a subset) results, it is clear that supervised performance is in 80+ region. The paper needs to include more recent supervised baselines to provide a fair comparison and accurately represent the state-of-the-art in supervised video object segmentation.
 6. Given that the contribution of the work is to append video diffusion features to the image of DIFT. There is arguably lack of significant learnings or exploration presented, as only 2 video diffusion models are tested. For example,  why is I2V better than SDV? Would time-tuned self-supervised features work instead [2]? Why only stop at 2 models? Are there better combinations for image features, as shown in [3]? Why are video features so much worse in isolation? The paper should explore a wider range of video diffusion models and feature combinations, and provide a more thorough analysis of the strengths and weaknesses of each approach. It should also investigate why video features perform poorly in isolation, and if this can be mitigated with different training strategies or feature extraction techniques.
 7. The performance constraints/cost are not mentioned, but they are usually key considerations in tracking settings, as systems need to be real-time due to safety critical (e.g. self-driving) or UX (e.g. film editing) concerns. What are the performance characteristics, e.g. FPS, GPU memory, to run this method?

### Questions
Please see weaknesses section for all questions. It is critical to consider and address the issues with the presentation, and better explain the experimental details.

### Soundness
2

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
5

### Summary
Uses video diffusion models to extract exact motion representations for strong appearances for visual tracking.

### Strengths
The paper presents an interesting idea in leveraging visual diffusion for strong appearance correspondence and how it can be used for visual tracking with multiple objects.

### Weaknesses
I am not exactly sure how this proposed paper differs from the DIFT method?  They appear to be the same except for perhaps different training data.
I understand that you are leveraging the latent representations from visual diffusion however no where in the paper do you explicitly give the visual tracking algorithm in terms of a flow chart or pseudo code, this would be helpful.
The ablation study refers to t which is the tilmestep in diffusion however when it appears, you also use t for time, so this is confusing to the reader.

### Questions
How does this method proposed differ from DIFT (Tang 2023)?, this is not clear?
What is the computational cost to compute the video diffusion model if we wanted to use this method for real time tracking?, or can we do tracking in real time with this step included?  How and in what manner do we include windowing for the video diffusion and how does this blend in for a real time algorithm for visual tracking.
Table 2, it would be good if the datasets were the same for a fair comparison.  The results for your approach and DIFT appear the same and sometimes DIFT is better, comment please?  
It appears that the method is dependent on the dataset used?  I am curious on if the same dataset is used, how does DIFT differ from your algorithm in terms of results

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
The authors leverage latent representations from video diffusion models to capture the temporal information for pixel-level tracking. Without additional training, the proposed method improves tracking performance in various video scenarios, even enabling tracking of similar-looking objects where previous methods struggle. The authors also introduce a new benchmark, Youtube-Similar,  to evaluate the complex scenario of tracking multiple similar-looking objects in real-world videos. The proposed method, TED, is evaluated on several benchmarks and achieves better tracking results.

### Strengths
1. TED extracts the temporal information of tracking targets from the video diffusion models to assist in tracking.
2. TED introduce a new benchmark, Youtube-Similar, to evaluate the complex scenario of tracking multiple similar-looking objects in real-world videos. 
3. TED achieves good tracking results, especially on the Youtube-Similar benchmark, to show the better tracking ability to tackle the complex scenario of multiple similar-looking objects.

### Weaknesses
1. The tracking results, which only train on ImageNet, are suggested to be provided for fare comparison.
2. The tracking speed and computation cost are suggested to be provided.
3. The authors are suggested to discuss the benefits of the temporal information extracted from diffusion compared with other models like transformers.

### Questions
Please see the weakness.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a method from video diffusion, TED, to extract motion representations for object-level tracking tasks. By leveraging diffusion representation and existing label propagation methods, the proposed method shows a very robust identification in similar appearance matching. The experiments demonstrate its effectiveness in tracking tasks and achieving SOTA results.

### Strengths
- The paper is well written. It is easy to follow the key idea of the paper.
- the experiments are comprehensive and the results are quite good. Especially, the demos, ie. fig 5, on identical appearance object matching.
- the findings along with understanding are interesting. how to deal with the similar appearance of objects in label propagation is very fundamental in the field. 
- helping understand diffusion models and latent representation from another perspective. It can benefit a board of readers in tracking and diffusion groups.

### Weaknesses
 - Several improvements can be achieved. It would be better if more metrics were provided to understand the proposed method, i.e. the time-consuming. the details of the proposed framework can be provided in supplementary for readers to replicate the method.

### Questions
- What about the time cost of the method? Considering the diffusion model often takes time to infer, how much time it will cost to track, for example, 100 frames? 
- And if the video sequence is very long, would the results decline? 
- as the method is built on standard Unet diffusion models, would some inference speed-up methods in the diffusion model help TED faster?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a simple method of extracting diffusion features from small clips to perform the object tracking task. It enables tracking similar objects, overcoming limitations of per-frame processing proposed in previous works. The performances are quite improved on segmentation-, pixel- and pose-level tracking.

### Strengths
- The technical statements are quite clear and compelling.
- The PCA analysis seems interesting.
- The performances are quite improved on three input levels.

### Weaknesses
 - The progression from per-frame processing to batch processing seems natural, with no leap leading the methodology forward.
- The methodology of using generative models in simple understanding tasks was quite interesting when first DIFT was proposed. However, simply making incremental improvements to these models for marginal performance gains may not fully realize their power. The core idea of leveraging diffusion models for feature extraction, while effective, lacks a strong justification for why these specific features are optimal for tracking, beyond empirical success. A more in-depth analysis of the feature space and its properties would be beneficial.
- Data statistics are missing, how is the number of samples/frames/objects? Why is the dataset claimed as a contribution while reusing from Youtube-VOS?

### Questions
- I could not get from Fig.5 whether the feature visualization is a heatmap or something else. If it is a heatmap ranging from 0 to 1, how can one object be distinguished from another?

### Soundness
3

### Presentation
3

### Contribution
2
