# Co$^{\mathbf{3}}$Gesture: Towards Coherent Concurrent Co-speech 3D Gesture Generation with Interactive Diffusion

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 6, 10

## Abstract
Generating gestures from human speech has gained tremendous progress in animating virtual avatars. While the existing methods enable synthesizing gestures cooperated by people self-talking, they overlook the practicality of concurrent gesture modeling with two-person interactive conversations. Moreover, the lack of high-quality datasets with concurrent co-speech gestures also limits handling this issue. To fulfill this goal, we first construct a large-scale concurrent co-speech gesture dataset that contains more than 7M frames for diverse two-person interactive posture sequences, dubbed $\textbf{GES-Inter}$. Moreover, we propose Co$^{\mathbf{3}}$Gesture, a novel framework that enables concurrent coherent co-speech gesture synthesis including two-person interactive movements. Our framework is built upon two cooperative generation branches conditioned on decomposed speaker audio. Specifically, to enhance the coordination of human postures w.r.t corresponding speaker audios while interacting with the conversational partner, we present a Temporal-Interaction Module ($\textbf{TIM}$). TIM can effectively model the temporal association representation between two speakers' gesture sequences as interaction guidance and fuse it into the concurrent gesture generation. Then, we devise a mutual attention mechanism to further boost learning dependencies of interacted concurrent motions, thereby enabling us to generate vivid and coherent gestures. Extensive experiments demonstrate that our method outperforms the state-of-the-art models on our newly collected GES-Inter dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel task: generating concurrent co-speech gestures for two interacting characters based on conversational speech audio. The authors first present a new dataset, GES-Inter, which contains full-body postures of two interacting characters reconstructed from video recordings. They then propose a co-speech gesture generation framework, Co$^3$Gesture, built upon bilateral cooperative diffusion branches with an integrated Temporal Interaction Module. Experimental results on the GES-Inter dataset demonstrate that this framework outperforms several state-of-the-art methods.

### Strengths
1. This paper introduces a novel task: generating concurrent co-speech gestures for interacting characters based on conversational speech audio.

2. The proposed Co$^3$Gesture model, featuring the specially designed Temporal Interaction Module (TIM), appears capable of generating alternating co-speech gestures for two interacting characters.

3. The authors have compiled a new dataset specifically for the concurrent co-speech gesture synthesis task.

### Weaknesses
1. The proposed Co$^3$Gesture model does not account for the spatial relationships between the two speakers. Specifically, Speaker A consistently appears on the left, and both speakers are always seated in chairs.

2. The authors report using pre-trained models for some baseline methods. However, this approach is problematic, as it is unreasonable to expect pre-trained models to produce realistic interactive co-speech gestures if they have not been trained on the new dataset. Training these models on the newly collected dataset would likely yield more reliable results.

3. In the ablation study, the authors present metrics only for models without TIM and mutual attention modules. The study would be more persuasive if the authors also included metrics using a simple fusion module, such as an MLP or a concatenation operator, rather than entirely omitting the fusion modules.

4. Qualitative results for ablated models are not provided. Including these results would strengthen the evaluation.

5. The user study and comparison videos show only a marginal improvement over InterGen.

### Questions
1. Could the authors specify which baseline methods utilized pre-trained models?

2. Could the authors provide additional ablation studies incorporating simple fusion modules?

3. Could the authors perform a significance analysis for the user study?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a novel dataset and method to tackle the problem of concurrent co-speech gesture generation for two persons in conversation. The dataset consists of about 70 hours of curated video footage consisting of various pairs of conversing people --- taken mostly from talk show videos in the public domain --- such that both their gestures are fully visible. The proposed method trains a diffusion network with a temporal interaction module (TIM) performing cross-attentions between the audio and motion features of the two persons. The output of the TIM serves as the conditioning signal for the denoising motion decoder to generate the 3D motions of the two persons from noise. The authors show the benefits of their proposed approach through quantitative and qualitative comparisons, ablation experiments, and a user study.

### Strengths
1. The authors have tackled the challenging problem of generating concurrent, two-person co-speech gestures, which is a natural expansion of the scope of current co-speech gesture generation methods, and meaningfully takes the field of human motion understanding forward.

2. The proposed dataset is carefully curated and thoughtfully designed to contain a sufficient quantity of two-person gestures, making it a good candidate for a benchmark for two-person interactive motion generation problems.

3. The proposed method is technically sound and provides a baseline on the proposed dataset.

### Weaknesses
1. Some additional dataset preprocessing details may be useful for completeness.

    (a) Do the authors manually check the three preprocessing steps for each video (Lines 794-801)? How are quality and consistency ensured across the dataset? Specifically, what criteria are used to filter out low-quality videos, and how is this process standardized across the large dataset? What specific metrics or thresholds are used in the automatic filtering steps, and how are these thresholds determined to ensure the dataset's overall quality?

    (b) How are the occlusions determined in the videos? Also, if any person in the video has a non-sitting posture, e.g., standing or walking around, are those motions tracked and filtered out? What specific pose estimation techniques are used to identify occlusions, and what are the thresholds for determining when a video segment is considered too occluded? Furthermore, how are non-sitting postures identified and what specific criteria are used to filter them out, ensuring a consistent dataset of seated interactions?

2. Some details and motivations of the proposed approach are missing.

    (a) Why do the authors use $C_{mix}$, and not a combination of the cleanly separated signals $C_a$ and $C_b$, to get the interactive motion embeddings (Line 266)? It would also be good to see any mathematical relationships, visual representations, or ablation experiments to understand how $C_a$, $C_b$, and $C_{mix}$ relate to each other (e.g., is $C_{mix} = C_a + C_b$)? What is the specific rationale for using the mixed audio signal to capture interaction, and how does this approach compare to using separate audio streams with an explicit interaction module? A more detailed explanation of the information captured by $C_{mix}$ and its relationship to $C_a$ and $C_b$ is needed.

    (b) During the generation, do the authors consider any global translation and orientation? In other words, do they consider any translation and orientation for the root joint, or is the root fixed in place? The visual results seem to suggest the latter, but it is not clear from the paper. If the root joint is fixed, what are the implications for the realism of the generated motions, and how might this limitation be addressed in future work? A discussion of the trade-offs between modeling local joint movements and global body motion would be beneficial.

    (c) Since the authors only consider upper body motions (Line 244), why are they using a foot contact loss (Eqn. 4)? Is it possible to quantify the benefits of the foot contact loss for this problem (e.g., through an ablation experiment)? What is the specific mechanism by which the foot contact loss influences upper body motion, and how is the lower body pose determined during the loss calculation given that only upper body motion is modeled? A more detailed explanation of the interaction between the foot contact loss and the upper body motion generation is needed.

3. The baseline methods the authors compare with (Sec. 4.2) are designed for single-person co-speech gestures. How do the authors adapt them for two-person co-speech gesture generation? Also, why are the authors not performing quantitative comparisons with more relevant two-person motion generation methods, such as InterGen (Liang et al. 2024b) or InterX (Xu et al. 2024)? What specific modifications are made to the single-person baseline methods to enable them to generate two-person gestures, and how might these modifications affect their performance? A more detailed discussion of the limitations of the baseline methods and the advantages of the proposed approach is needed.

4. Some user study details are also missing.

    (a) How many generated videos does each participant watch?

    (b) What is the mean and variance of the lengths of the videos they watch?

    (c) What fractions of those video lengths contain the motions of person A, and what fraction contains the motions of person B? This might be calculated by assuming a person has motion in a particular frame if the minimum difference in their joint positions from a few previous frames is above some empirically determined thresholds. What specific thresholds are used to determine motion, and how are these thresholds chosen to accurately reflect the presence of gestures? A more detailed explanation of the motion detection process and its impact on the user study results is needed.

    (d) What is the standard deviation in the participant responses? Particularly, it seems that the mean values for InterX, InterGen, and the proposed method are quite close. How does the statistical significance of the differences in user study scores compare across methods, and what are the implications for the conclusions drawn from the user study?

5. Most of the visual results only show gestures of one person while the other person is sitting idle, and most of these results are only 3-4 seconds long. It is hard to appreciate the two-person motion generation performance from these results. The one example which is longer than 10 seconds and shows the gestures of two persons also exhibits jittery motion. Have the authors investigated the source of this jitter and explored any steps to reduce or remove it? Also, it would help to see some quantification of the balance of motions between the two persons (e.g., highlighting a person when they are gesticulating, showing the number of frames the person is gesticulating for) in the generated results. What specific techniques have been explored to mitigate jitter, and how effective are these techniques in improving the visual quality of the generated motions? A more detailed analysis of the motion balance between the two persons and its impact on the perceived quality of the generated interactions is needed.

### Questions
Some typos, e.g.,

Line 258: pheromones -> phonemes

Table 3: Attetion -> Attention

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on the task of interactive motion generation in two-person dialogue scenarios. It first introduces a large-scale dataset for two-person interactive motion, which includes body and finger movements as well as facial expressions. An interactive motion generation model is proposed, along with a Temporal Interaction Module to ensure the temporal synchronization of gestures. 
Based on the proposed GES-Inter dataset, the authors benchmark the model against other state-of-the-art algorithms.

### Strengths
This paper extracts 3D data from videos, collecting a large-scale dataset. Compared to laboratory-based data collection, capturing natural interactions yields more authentic interactive motions.

The proposed method employs Bilateral Cooperative Diffusion and the Temporal Interaction Module, which shown to be effective in experiments.

The dataset separates audio for the two speakers, recognizes the text corresponding to the audio, and invites participants to review the data, which is commendable.

### Weaknesses
 **Dataset Quality**
Capturing accurate two-person interactive motions from video is inherently challenging, which raises concerns about the dataset's quality. From the GES-Inter dataset examples shown in the videos [3], there are noticeable issues, such as hand self-penetration problems for the yellow character. Additionally, the dataset's frame rate is only 15 FPS, which is lower than that of mainstream motion datasets, limiting the compatibility of this dataset with other human motion datasets.

Based on the dataset and generated examples provided, all individuals share the same shape parameters, showing no variation in body shape, and their root positions remain fixed. As a foundational dataset project, it is crucial for the authors to clarify any pre-processing or post-processing steps applied to the data and the motivations behind these decisions.

To help the authors further demonstrate the quality of GES-Interdataset and improve its compatibility with other datasets, I offer the following suggestions: **(1)** Provide more comprehensive example videos showcasing the dataset.
**(2)** Consider offering solutions to improve the dataset's frame rate, such as FPS enhancement tools or post-processing scripts.
**(3)** Further explain any pre or post processing applied to the data and clarify why there is no observable variation in human shape or root position in the dataset and generated examples.

**Comparison**
The dataset may lacks a comparison with previous [2]. The authors should consider adding a table to quantitatively compare the GES-Inter dataset with [2], highlighting differences in aspects such as size, capture equipment, diversity, and quality metrics. This comparison would provide a clearer understanding of the dataset's advantages and limitations relative to previous work.

**Interaction Metric**
The correspondence between the interactive motions and the given speech in two-person interactions appears weak. It may be helpful for the authors to identify and categorize the typical types of interactive motions and consider developing or adopting more suitable metrics for evaluating the quality of interactions. In particular, the current metrics, such as FGD, BC, and Diversity, are insufficient for this purpose, and incorporating more interaction-specific evaluation criteria would strengthen the assessment..


**Audio process**
In the methodology section, audio input (C_mix) is simply fed into the Audio Encoder without special processing for each speaker’s audio, particularly in cases where overlapping speech occurs when both speakers talk simultaneously. The authors should clarify how their method handles overlapping speech. It may be helpful to conduct an ablation study or provide examples that demonstrate the model's performance specifically in scenarios with overlapping speech.

**Ambiguous Figure**
Figure 3 make ambiguous, the authors should revise the figure to accurately represent the inputs to the Audio Encoder as described in the text. Based on the paper's description, the input to the Audio Encoder should be C_mix={c_a,c_b}, rather than the isolated representation of C_mix,c_a and c_b  shown in the figure. To clarify, placing c_a and c_b  on the left side of the audio diagram and omitting the corresponding arrows to the Audio Encoder would be more accurate.
Alternatively, if the figure is correct, you should clarify this in the text.

### Questions
**Separation of Speaker Audio** How effective is the speech separation? Could more examples be provided to illustrate the accuracy of speech segmentation, text recognition, and alignment?

**Only Upper Body**
The paper does not clearly explain why only upper body motions are generated, is it due to insufficient quality in the lower body data within the dataset?

**Body Shape and root**
Why do the body shape and root position appear to be fixed?

**Unclear Representation** 
The dimensions and composition of inputs like audio c_a ​and x_a are not clearly specified. Why x_a  only include upper body movements, and which specific joints are used?  Why do all generated results have the same shape? Does x_a include facial expressions and shape parameters?
Specifying the exact dimensions and components of each input, including which joints are used for upper body movements and whether facial expressions and shape parameters are included, would be helpful.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper explores learning conversational gesture generation from in-the-wild video data, different from previous works that focused on smaller, in-lab, or middle-scale motion-captured datasets. The authors make three key contributions:
1. **Data Collection**: 

    The paper introduces a 70-hour conversational dataset with pseudo-labels, processed with temporal smoothing and filtering to ensure data quality.

2. **Proposed Baseline Model**: 

    The authors propose a baseline model consisting of Temporal Interaction Network (TIN) and mutual attention mechanisms for conversational gesture generation.

3. **Performance**: 

    The results demonstrate that the proposed method outperforms previous single-speaker or conversational speaker methods on the newly created GES-Inter dataset.

### Strengths
Overall, I am quite positive about this paper. To the best of my knowledge, it is the first attempt to generate conversational gestures using in-the-wild video data. The key strengths include:

1. **Data Cleanup**: 

    The data processing is thorough, as mentioned in the appendix. The original collection consisted of over 1,000 hours of video, but after a 12-step filtering process, only 70 hours remained. This shows a well-designed filtering strategy, including speaker occurrence rules, to ensure data quality.
   
2. **Model Simplicity and Reproducibility**: 

    The model design is novel yet simple for a baseline approach. Instead of making the model overly complex, the authors build on strightforward diffusion models with audio inputs from two speakers. The plug-in TIN and mutual attention modules make this work easy to reproduce and extend in future studies.

3. **TIN Design**: 

    The Temporal Interaction Network captures selective features refined from either single-speaker voices or mixed voices from both speakers, aligning with the physical nature of conversational gestures.

4. **Experimental Results**: 

    The experiments compare recent baselines for both single-speaker and conversational gesture generation. The model achieves new SOTA results on the GES-Inter dataset.

### Weaknesses
While the paper is strong overall, I have one unclear point:
1.  **unclear sentence mutual attention module**: 

    Some explanation of the mutual attention module unclear, particularly in lines 280-282: "We observe that exchanging the input order ... distribution." The notion of "order" here is confused for me. does that mean switch the order of "question" and "answer", such as, "how are you, --> good. " becomes "good. --> how are you"? This will influence my understanding of the design motivation of this module.

### Questions
My primary question (will influence I raise my score or not) is the same as my weakness. 

1.  **unclear sentence mutual attention module**: 

    Some explanation of the mutual attention module unclear, particularly in lines 280-282: "We observe that exchanging the input order ... distribution." The notion of "order" here is confused for me. does that mean switch the order of "question" and "answer", such as, "how are you, --> good. " becomes "good. --> how are you"? This will influence my understanding of the design motivation of this module.

Suggestions not influence my scoring:

1. **Raw Data Release**: 

    I suggest the authors consider releasing the raw video data after the scene cuts. This would allow users to explore additional tasks, such as video generation, using the raw data.

### Soundness
4

### Presentation
4

### Contribution
4
