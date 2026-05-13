# Multi-Perspective Data Augmentation for Few-shot Object Detection

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Recent few-shot object detection (FSOD) methods have focused on  augmenting synthetic samples for novel classes, show promising results  to the rise of diffusion models. However, the diversity of such datasets is often limited in representativeness because they lack awareness of typical and hard samples, especially in the context of foreground and background relationships. To tackle this issue, we propose a Multi-Perspective Data Augmentation (MPAD) framework. In terms of foreground-foreground relationships, we propose in-context learning for object synthesis (ICOS) with bounding box adjustments to enhance the detail and spatial information of synthetic samples. Inspired by the large margin principle, support samples play a vital role in defining class boundaries. Therefore, we design a Harmonic Prompt Aggregation Scheduler (HPAS) to mix prompt embeddings at each time step of the generation process in diffusion models, producing hard novel samples. For foreground-background relationships, we introduce a Background Proposal method (BAP) to sample typical and hard backgrounds. Extensive experiments on multiple FSOD benchmarks demonstrate the effectiveness of our approach. Our framework significantly outperforms traditional methods, achieving an average increase of $17.5\%$ in nAP50 over the baseline on PASCAL VOC.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a Multi-Perspective Data Augmentation (MPAD) framework to improve few-shot object detection (FSOD) by generating diverse and representative synthetic samples. The framework includes three components: Chain-of-Thought Prompting for Object Synthesis (CPOS) uses large language models to enhance prompt diversity with fine-grained attributes; Harmonic Prompt Aggregation Scheduler (HPAS) mixes base and novel class features in the diffusion process, producing hard-to-classify samples; and Background Proposal (BAP) selects complex or visually similar backgrounds to improve object-background differentiation. Extensive experiments on PASCAL VOC and COCO few-shot object detection benchmarks show the effectiveness of the proposed method.

### Strengths
1: The MPAD framework leverages Chain-of-Thought Prompting to generate prompts with fine-grained attributes, enabling diverse and representative data synthesis for few-shot object detection. 

2: The proposed method is easy to follow and not limited to some specific object detection architectures, making the technique be applied in different scenarios without further modifications. 

3: The main results on PASCAL VOC and COCO few-shot datasets illustrate that the proposed method can improve non-trivial performance on many few-shot object detection benchmarks.

### Weaknesses
1: The description that "this work is the first ..." in Lines 81-83 is a little bit over-claimed. From my perspective, there is already a large amount of work exploring using large-scale pretrained diffusion models for object detection by generation (like general object detection and corner case generation for autonomous driving). Simply extending the setting to few-shot object detection isn't that significant to me.

2: Section 2.3 (CoT prompting for object synthesis) actually belongs to prompt engineering. The Chain-of-Thought emphasizes solving a problem step by step. For object synthesis discussed in this paper, the task simply needs to list all possible attributes of a category ( or use a pre-defined template). This can be regarded as in-context learning or prompt engineering rather than Chain-of-Thought. Meanwhile, the inpainting model is also modified from other previous works.

3: The overall technique contribution is limited. Continuing from point 2, the method is more like a combination of several existing verified techniques for object detection data generation without a clear logical chain. The HPAS is a prompt embedding level mixup data augmentation which is also not novel (the insight of embedding mixup is common in conditional data generation using diffusion model). It's also hard to convince me that the BAP part brings much novelty.   

4: Comparisons with deep learning methods (using large-scale pretrained models like diffusion model and CLIP, etc). In Table 3, the authors only compare their proposed method with some non-deep learning-based methods. However, given the widely used conditional diffusion model for object detection object generation, the authors also should add more baselines such as simply using the **Powerpoint** inpainting model for data generation, to further verify the effectiveness of the proposed module that is claimed to enhance the diversity.

### Questions
1: In the Introduction part (especially for Figure 1), what's the definition of typical and hard objects on the novel set? How to distinguish them?

2: Which are the novel synthetic samples and the base real samples in Novel Set 1 in Figure 1? Why do some colors (classes) only have solid circle samples without any "x" samples? (I am deeply Confused by Figure 1.) 

3: In Table 2, is it a typo that sometimes the metric is "nAP" while sometimes not?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper attempts to enhance the diversity of data generation by analyzing typical and hard samples. Specifically, a data generation architecture is proposed that comprehensively considers the typicality and difficulty of foreground and background selections, establishing the relationship between foreground and background. Experimental evidence demonstrates significant performance improvements compared to recent methods.

### Strengths
+ From the experimental data, the current data augmentation methods show a certain degree of performance improvement.
+ Integrating various mainstream generative models and zero-shot learning models, including diffusion, CLIP, etc.

### Weaknesses
 - The present approach heavily depends on utilizing pre-trained models to select typical and challenging samples, potentially causing interference when assessing the efficacy of augmentation strategies.
- Additional clarification is needed regarding the fairness of the experiments.
- The definitions of typical and hard samples lack sufficient detail, making it difficult to assess the novelty of the approach. The criteria for determining typicality and difficulty are not clearly established.
- The rationale for considering samples generated based on mixed prompt embedding as hard samples in HPAS is not fully convincing. While mixed prompts might introduce more categories, the difficulty for a model is not solely determined by the number of categories.
- The connection between the selection of challenging backgrounds and camouflaged objects is not well-established. The paper uses the concept of camouflage as inspiration but does not clearly demonstrate how the chosen backgrounds relate to actual camouflaged scenarios.
- The method for selecting typical clutter backgrounds using entropy relies heavily on the feature extractor's performance. If the feature extractor is poor, the selected backgrounds may not be useful, and if it is too good, the selection process may be too limited.

### Questions
1. What are the definitions of typical and hard samples? Detailed assessment criteria need to be further elaborated.
2. In Section 2.2, lines 159-161 mention that HPAS can generate hard samples. Strategically, it may indeed involve a wider range of categories. However, for the model, the level of difficulty in recognition is not solely dependent on the number of categories in the image. Why are samples generated based on mixed prompt embedding considered hard samples in HPAS?
3. In the last paragraph on the fifth page, it mentions the concept of camouflage targets. Camouflaged objects typically refer to objects where the foreground and background have high similarity. However, in the subsequent text, the selection of data with high similarity between the background in the base stage and the classes in the novel stage as challenging data does not explicitly demonstrate the connection between selecting difficult backgrounds and camouflaged objects. Therefore, what is the relationship between the selection of challenging backgrounds and camouflaged objects?
4. In Equation 6, it is mentioned that typical clutter background is obtained by calculating entropy. Such selection heavily relies on the performance of the feature extractor F. If the predictive results are good, few background images may be selected. However, if the predictive results are poor, do the selected background images hold any useful value?
5. The architecture of this paper incorporates various methods with pre-trained models, such as CLIP. Is the fairness of the comparison between the current augmentation strategy and previous methods lacking?

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
5

### Summary
This paper proposes a Multi-Perspective Data Augmentation (MPAD) framework aimed at enhancing few-shot object detection (FSOD) by generating diverse and challenging synthetic samples. The MPAD framework utilizes techniques such as Chain-of-Thought Prompting for Object Synthesis (CPOS), Harmonic Prompt Aggregation Scheduler (HPAS), and Background Proposal (BAP) to create representative and hard samples. The authors present results demonstrating significant performance improvements on PASCAL VOC and MS COCO benchmarks, showing an average increase of 17.5% in nAP50 over baseline methods.

### Strengths
1.	The CPOS and HPAS introduce novel ways to leverage both typical and hard samples, leading to a more representative synthetic dataset.
2.	The use of BAP to generate diverse backgrounds helps enhance detection accuracy by allowing the model to distinguish between foreground and background more effectively.
3.	The proposed framework achieves notable gains over state-of-the-art baselines on multiple FSOD benchmarks, particularly in challenging low-shot settings.

### Weaknesses
1. The framework combines multiple advanced techniques, including diffusion models, harmonic prompt scheduling, and complex background sampling, which may make it challenging for practitioners to implement effectively in real-world scenarios. At the same time, it increases the complexity of the model. Please analyze the model complexity and real-time inference of the generated model.
2. The paper demonstrates performance gains, but it would benefit from a more granular analysis comparing the effectiveness of each augmentation component (CPOS, HPAS) against similar elements in other FSOD methods. Has the pre-trained model of the generated model already seen various categories to generate more realistic new class samples when regenerated again? Can other generative models also generate samples to improve the performance of small samples, and does the proposed method have such a significant performance improvement compared to this type of method
Data Efficiency in Synthetic Generation:
3. While the method performs well, additional experiments assessing data efficiency could be valuable. Evaluating how much synthetic data is optimal or exploring the impact of different amounts of augmented data on performance could provide insights into the scalability and efficiency of the framework.

### Questions
Please refer to the Weaknesses box.

### Soundness
3

### Presentation
3

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
This paper proposes a Multi-Perspective Data Augmentation (MPAD) framework for few-shot object detection (FSOD), aiming to address the limitations of existing data augmentation methods. By considering both foreground-foreground and foreground-background relationships in MPAD, the authors provide an interesting solution to the problem of data augmentation. The experimental results on PASCAL VOC and MS COCO datasets demonstrate the effectiveness of the proposed methods, outperforming many state-of-the-art methods.

### Strengths
1. The paper is generally well-written and the idea is presented clearly. 

2. The introduction provides a good background and motivation for the research

3. The proposed methods are described in detail and mostly are easy to follow. 

4. The experimental setup and results are also presented in a clear and organized manner.

5. The authors also conduct a series of ablation studies to better understand the proposed method.

### Weaknesses
1. My main concern lies in the use of Diffusion Model (DM) and ChatGPT. From the perspective of the FSOD task, data is always the most crucial element. Consequently, it is essential to employ ChatGPT and DM to generate data as a means to address this concern, as the authors did in this study. However, the following questions arise: if ChatGPT and DM are being used, why not simply generate a substantial number of samples of the corresponding categories and conduct direct training on the generated data? Alternatively, another option could be to pre-train the detector on the generated data and subsequently perform fine-tuning on few-shot categories. Currently, the authors haven't furnished a compelling rationale to either explain, oppose, or support these viewpoints, which are of utmost significance for this paper.

    To answer these questions, I suggest the authors: 
    
    - (1)  conduct a comprehensive analysis comparing the performance of direct training on generated data with the proposed method; 

    - (2) explore the potential benefits and drawbacks of pretraining on generated data and then fine-tuning on few-shot categories. This could include experiments to determine the optimal amount of pretraining and the impact on final performance; 

    - (3) provide a detailed explanation of why the proposed approach of using ChatGPT and DM in a specific way is more advantageous than (1) and (2). 

2. Some details could be further elaborated. For example, in the description of the Harmonic Prompt Aggregation Scheduler (HPAS), the role of the momentum parameter and its impact on the generated samples could be explained more clearly. For example, the authors can provide a figure to visualize generated samples across a range of momentum values (e.g. 0.1, 0.5, 0.9) to illustrate how this parameter impacts the mixing of base and novel class features.

3. Additionally, the discussion on the limitations of the diffusion model in the appendix could be more in-depth, perhaps exploring potential solutions or future research directions. For example, (1) analyzing whether the hallucination will affect the final result of FSOD, and if so, what possible means can be used to solve it; or (2) is there any possible way to train (in a PEFT manner) an FSOD-aware DM to further improve the performance. In addition, I suggest putting the "limitation" part to the main text; With these changes, this paper becomes more inspiring to the reader.

### Questions
See "Weaknesses"

### Soundness
3

### Presentation
3

### Contribution
2
