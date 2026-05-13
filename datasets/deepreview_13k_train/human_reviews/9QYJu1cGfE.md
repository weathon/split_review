# Quo Vadis, Motion Generation? From Large Language Models to Large Motion Models

- Decision: Reject
- Scores: 8, 6, 6, 5, 5

## Abstract
Inspired by the recent success of LLMs, the field of human motion understanding has increasingly shifted towards the development of large motion models. 
Despite some progress, current state-of-the-art works remain far from achieving truly generalist models, largely due to the lack of large-scale, high-quality motion data. 
To address this, we present MotionBase, the first million-level motion generation benchmark, offering 15 times the data volume of the previous largest dataset, and featuring multimodal data with hierarchically detailed text descriptions.
By leveraging this vast dataset, our large motion model demonstrates strong performance across a broad range of motions, including unseen ones.
Through systematic investigation, we underscore the importance of scaling both data and model size, with synthetic data and pseudo labels playing a crucial role in mitigating data acquisition costs.
Moreover, our research reveals the limitations of existing evaluation metrics, particularly in handling out-of-domain text instructions --- an issue that has long been overlooked.
In addition to these, we introduce a novel 2D lookup-free approach for motion tokenization, which preserves motion information and expands codebook capacity, further enhancing the representative ability of large motion models.
The release of MotionBase and the insights gained from this study are expected to pave the way for the development of more powerful and versatile motion generation models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Paper introduce motionbase, a motion generation benchmark trained on large amount of data with focus on motion generation with LLMs.

### Strengths
The work is well motivated in terms:
 Showing the gap of prior work and lack of domain generlization 
Showing limitation of prior metrics 
A new motion codebook 


The new dataset is quite large in comparison with prior ones, which is a valuable addition to the community. It comes with a good set of text descriptions. 

Evaluation on multiple datasets and multiple models with strong baselines.
Answer to important questions like the need of scale and model size impact on the task 
Discussion on OOD behaviour 
Ablation of motion quantization

### Weaknesses
I do not see much of concerns about the work, more of questions.

### Questions
– Questions:
How did the author verify the correctness/accuracy of the pose estimation
What do authors think about properties of a new metric?

### Soundness
4

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
4

### Summary
In this paper, the authors introduce MotionBase, a large-scale human motion generation benchmark featuring over one million motion sequences, a fifteen-fold increase over previous datasets, with multimodal data and detailed text descriptions. The authors demonstrate that scaling both data and model size significantly improves motion model performance, particularly with synthetic data and pseudo labels to reduce data acquisition costs. The authors also propose a novel 2D lookup-free motion quantization approach to enhance motion information retention and expand codebook capacity. Experimental results on various datasets validate the efficacy of their approach, with notable performance on out-of-domain data.

### Strengths
1. The paper introduces MotionBase, a large-scale dataset comprising over one million human motion sequences, designed to support more comprehensive training and evaluation of motion generation models.

2. The paper identifies key factors influencing the effectiveness of large motion models, underscoring the importance of scaling both data and model size.

3. This paper proposes a 2D lookup-free motion quantization method that enhances motion representation while retaining essential information, thereby contributing to improved model performance.

### Weaknesses
1. While MotionBase is introduced as a benchmark with the potential to enhance motion model performance, the paper lacks a thorough comparative analysis across varied methods to demonstrate MotionBase's influence on model efficacy. Additional baselines and a broader selection of models trained on MotionBase would more robustly substantiate its claimed advantages. Specifically, the paper does not sufficiently explore how different model architectures respond to the increased scale of the dataset. For example, it would be beneficial to see how models with varying capacities, such as those with different numbers of parameters or transformer layers, perform when trained on MotionBase compared to smaller datasets. This would help to understand the true impact of the dataset's scale on model performance, rather than just demonstrating that larger models generally perform better.

2. The paper does not include visual comparisons of motions generated by models trained on the baseline Motion-X dataset versus those trained on the proposed MotionBase dataset. This makes it difficult to assess the qualitative improvements, if any, that MotionBase provides. A side-by-side comparison of motion sequences, perhaps with multiple examples showing different types of actions, would be much more convincing than relying solely on quantitative metrics.

3. Including the ground truth R-Precision and FID scores in relevant tables would strengthen the presentation and transparency of the results. The absence of these baseline metrics makes it harder to contextualize the performance of the models trained on MotionBase. Providing these scores would allow for a more direct comparison of the dataset's characteristics with existing benchmarks.

4. The paper would benefit from dynamic visualizations within the qualitative analysis of the motions in the proposed datasets, which could provide a clearer and more engaging illustration of the dataset's scope and quality. Static images are insufficient to convey the complexity and nuances of human motion. Dynamic visualizations, such as short video clips or interactive 3D renderings, would be much more effective in showcasing the dataset's richness and diversity.

### Questions
1. It will be interesting to see the scalability of different architectures. Have the authors explored fine-tuning existing methods, such as MotionGPT[1] or MoMask[2], with larger parameter settings on the MotionBase dataset? 

2. Regarding the automated evaluation metrics referenced by the authors, it is also noteworthy that the R-precision scores are relatively low on the proposed large-scale MotionBase dataset, potentially weakening the benchmarking results. Implementing text-motion retrieval models like TMR[3] may provide a more accurate evaluation of model performance.

[1] MotionGPT: Human Motion as a Foreign Language.

[2] MoMask: Generative Masked Modeling of 3D Human Motions.

[3] TMR: Text-to-Motion Retrieval Using Contrastive 3D Human Motion Synthesis.

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
3

### Summary
The paper is to answer the research question of "can a large motion model be a promising direction for motion generation?", and the designed a data colletion pipeline which collects multi-modal information including RGB, depth and bounding box with multi-person.
In addition the paper introduces a method to expand the codebook capacity, named lookup-free approach for motion tokenization, for better motion representation.

### Strengths
This paper presents the first large-scale dataset specifically designed for motion generation, featuring richly multi-modal data accompanied by hierarchical text descriptions. MotionBase, the dataset introduced, is expected to be highly beneficial for the advancement of future research in motion generation and to serve as a valuable resource for the computer vision community. The dataset offers researchers access to an extensive collection of motion data, enabling more robust analysis and development of large motion model.

### Weaknesses
I have minor concerns on this paper.

The layout of the paper is somewhat challenging for readers. It contains numerous messages and analyses, requiring readers to scroll up and down frequently to locate referenced tables. Additionally, due to page limitations, many explanations are placed in the Appendix. Tables and figures are positioned mid-page without aligning well with the paragraph height, disrupting the flow.

This paper was the first to introduce the concepts of partitioning body parts and 2D quantization, making it a valuable reference. (Pi, H., Peng, S., Yang, M., Zhou, X., & Bao, H. (2023). Hierarchical generation of human-object interactions with diffusion probabilistic models. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 15061-15073.)

Minor Issues and Typos:
Appendix D: "quantitative results" should be "qualitative results."
Figure 4: It may improve clarity to add a y-axis label.

### Questions
In Table 4, what is the ratio between synthetic, static, and real data? It can be brefiely explained in table caption.

I have the concern of the quality of occlusion cases or blurred images. How the authors recognize the motion is blurred or occluded?
In multi-person settings, the occlusion might be very common.

Since this is a dataset paper, I expect the more detailed explanation and instructions of the benchmark will be released once the paper upon the paper acceptance.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper collects a new large-scale text-motion dataset called MotionBase and then finetunes LLMs with different sizes. Additionally, for better scaling, the authors follow the video domain to train a new LFQ tokenizer with a large vocab size.

### Strengths
1. The authors try to scale the tokenizer vocab size and the model size.
2. The authors collect a new large-scale text-motion dataset.

### Weaknesses
1. The biggest server weakness is containing the one-frame pose data into the database. The Agora, mscoco, muco_3dhp, and other more datasets are used for 3d pose estimation, and they even occupy a large portion of the whole database, which may lead to static motion generation. The inclusion of single-frame poses, particularly from datasets primarily designed for pose estimation rather than motion, raises concerns about the temporal coherence of the generated motions.  These datasets inherently lack the temporal dynamics crucial for realistic motion synthesis, potentially biasing the model towards generating static or jerky movements. The method for converting these single-frame poses into multi-frame motions is not sufficiently detailed, making it difficult to assess the effectiveness of this approach.
2. The motion quality has not been validated. Neither the estimated motions nor the texts generated by LLM have been checked manually or by any algorithm. The video collection process is not clarified clearly. A lot of web videos are long and contain various camera shots. Which film shot boundary detection algorithm are you using? And how many frames do you insert into LLM to get the text? More details need to be added. The lack of quantitative evaluation of motion quality, especially on standard benchmarks, makes it difficult to compare the proposed method with existing approaches. The reliance on manual checks and qualitative assessments is insufficient for a rigorous scientific evaluation. The details of the video collection process, including the specific shot boundary detection algorithm and the number of frames used as input to the LLM, are crucial for reproducibility and understanding the data processing pipeline. The absence of these details makes it hard to assess the reliability of the dataset.
3. The experiments with static data ablation study are not fair. Does the validation set contain static data and synthetic data? The ablation study on static data is not convincing without a clear separation of static and synthetic data in the validation set. The inclusion of these data types in the validation set could skew the results, making it difficult to isolate the impact of static data on the model's performance. A more rigorous experimental design would involve a validation set that is free from static and synthetic data to ensure a fair evaluation.

### Questions
1. The FID in Table 6 is so wired. The FID of reconstruction is 1.76 while the generation FID in Table 3 is 0.166. This is impossible from my understanding. I suspect that the reconstruction result is not good enough. The original MPJPE calculation will subtract the root movement. If you calculate MPJPE similarly, the high reconstruction FID means the translations are not accurate. 
2. What do the authors get from scaling experiments? Did the author see any hope for emerging? The shown examples are common cases, that can be also observed in other motion generation work.
3. Did the supervised label contain only motion tokens or both text and motion tokens? 
4. Did the author try zero-shot text testing? For example, could the largest model do some texts like "The old man with a broken leg is walking forward slowly with a crane"?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper claims to propose a large motion model with a very large motion database. However, the motion quality is not well evaluated. Besides, the authors propose a motion quantization method, which is borrowed from LFQ (Mentzer et al., 2023). The authors claim a good generation quality of the generated results, which is not provided in the demo.

### Strengths
- The writing of this work is a bit fancy. 

- The statistics of the dataset are clear.

### Weaknesses
There are several fundamental concerns about this work. Each of these is fatal. 

1. **The motion collection process.** This process contains several issues. 
    - This work does not evaluate the quality of the video mocap data quality. To my knowledge, even the quality of the latest Motion-X++ suffers significant jittering and foot sliding. How can your method escape from this? **(my main concern)**
    - If the quality of the ground truth is not good enough, how can you generate good motion? Therefore, the result in L395-402 is not solid and convincing. **(my main concern)** I suggest authors read the blog [1] written by a well-known graphics scientist, Daniel Holden. 
    - The limited contribution of the dataset. The video data comes from InternViD and WebVid and the data collection process is from motion-x and other methods. The dataset contribution is limited. 

2. **The text annotation.**
    - The annotation quality of the text by Gemini-1.5-pro is not well evaluated. In my practice, it always contains some answers like "sorry...". The results should be corrected by researchers one by one. Has the >1M data been checked? 
    - The proposed contribution of hierarchical text is not discussed well. Has it been used in the model training? If I miss, please point it out. If this annotation is not used, what is the motivation for this hierarchical text contribution? Will it make the result more fine-grained? It is quite unclear. **(my main concern)** 

3. **Limited technical/evaluation contribution.** The LFQ is proposed by the original paper. The authors did not have a new understanding over this. Besides, the H2VQ proposed in Humantomato (ICML-24) is also missing for discussion or comparison. 

4. This work does not include any demo video, which is unacceptable in the animation community. The FID in Table 5 is extremely large, which strengthens my concerns about the motion quality. 

5. **Motivation.** The motivation for introducing LLM is not clear. The method misses a basic baseline of a transformer (like in T2M-GPT, CVPR-23) for comparison. Besides, it is also not clear whether the usage of pre-trained parameters of LLMs or not. Whether the fine-tuning method is LoRA or not is also not well discussed. Therefore, it is not technically sound. **This is my strong concern.**

### Questions
- The vocabulary of the LLM and motion codebooks are different. How do authors handle this issue? What is the efficiency of the LLM-based motion generation method? Please compare with the fastest motion generation method, MotionLCM (ECCV-24).

- **I would like to know why authors should cite [1].**

[1]: Zheng et al., Steve-eye: Equipping llm-based embodied agents with visual perception in open worlds.

### Soundness
1

### Presentation
2

### Contribution
1
