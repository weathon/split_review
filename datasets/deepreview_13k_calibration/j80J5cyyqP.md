# SPA: Enhancing 3D Multimodal LLMs with Mask-based Streamlining Preference Alignment

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6

## Abstract
Integrating 3D features into Large Language Models (LLMs) is a rapidly evolving field, with models like 3D-LLM, Point-Bind LLM, and PointLLM making notable strides. PointLLM, pre-trained and fine-tuned on the Objaverse dataset, enhances understanding by optimizing the projector, boosting resource efficiency and consistency. However, we observed a persistent bottleneck: increasing the LLM backbone size doesn't consistently improve performance. Preliminary experiments showed that enhancing the 3D encoder or extending fine-tuning alone failed to resolve this. While post-training partially addressed the issue, it required two stages and additional text sample generation, making it inefficient. To overcome this, we propose \textbf{S}treamlining \textbf{P}reference \textbf{A}lignment \textbf{(SPA)}, a post-training stage for MLLMs with 3D encoders.  SPA leverages the 3D encoder’s inductive bias through 3D-masking, ensuring robust output while preserving consistent differences. Unlike traditional post-training, SPA maximizes the encoder's spatial reasoning by increasing the probability gap between positive and negative logits. This approach eliminates redundant text generation, greatly enhancing resource efficiency and improving the overall alignment process. In addition, we identified evaluation issues in the existing benchmarks and conducted a re-benchmark, resulting in a more robust evaluation approach. The model combined with the SPA method as post-training stage successfully overcame the performance bottleneck and achieved better results across various evaluations on current scene-level and object-level benchmarks. Code is available at~\url{https://anonymous.4open.science/r/3dmllm-dap-5A50}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Streamlining Preference Alignment (SPA), a novel one-stage post-training method for 3D multimodal large language models (MLLMs). SPA uses 3D masking for data augmentation to enhance alignment between 3D spatial features and text representations, reducing the need for multi-stage alignment processes. Additionally, the paper presents a new evaluation benchmark, 3D Choice-level Questions and Answering (3DCQA), aimed at evaluating object- and scene-level reasoning in 3D-MLLMs.

### Strengths
1. The introduction of the SPA method represents an innovative solution to the challenges faced by current MLLMs in 3D understanding.
2. The implementation of 3D masking as a data augmentation technique to improve feature alignment with text is a practical enhancement. This approach allows the model to better differentiate between spatially diverse features in 3D data, which could improve performance in 3D-based tasks requiring spatial reasoning.
3. The 3DCQA benchmark is a positive contribution that attempts to address limitations in existing 3D-MLLM evaluation frameworks. By focusing on multiple-choice questions across object- and scene-level tasks, 3DCQA provides a more structured way of assessing 3D reasoning capabilities, which could be useful for future research in the area.

### Weaknesses
1.  SPA’s generalizability beyond specific 3D datasets and tasks (such as those in 3DCQA) is unclear. The experiments lack tests on diverse 3D data types or environments, which would better support claims of SPA’s broader applicability. For instance, the paper does not explore how SPA performs on point cloud data, mesh data, or even synthetic vs. real-world 3D scans, which are all common in 3D vision. This limits the understanding of the method's robustness across different data modalities and potential real-world applications.
2.  The primary contribution, SPA, largely builds on established methods, refining the process rather than introducing fundamentally new ideas. Single-stage alignment, while practical, is not a groundbreaking advancement. The paper does not sufficiently detail how SPA's single-stage approach differs fundamentally from existing contrastive learning methods used in other multimodal models, making it difficult to assess the novelty of the approach. The reliance on 3D masking for data augmentation, while useful, is also not a novel concept in itself, and the paper lacks a detailed analysis of how this specific implementation of masking contributes uniquely to the performance gains.

### Questions
1. Conduct more granular ablations, particularly on individual components of SPA, such as the single-stage alignment and 3D masking. Directly comparing SPA’s single-stage approach to traditional multi-stage alignment methods would clarify its specific contributions.
2. Adding experiments on datasets outside the 3DCQA benchmark, such as complex real-world scenes or cross-domain 3D data, would help substantiate the claims regarding SPA’s robustness and generalizability.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work focuses on the post-training phase of 3D MLLMs, achieving results that previously required two phases through noise introduction in a single phase.

### Strengths
This work focuses on the post-training phase of 3D MLLMs, achieving results that previously required two phases through noise introduction in a single phase.

### Weaknesses
This work focuses on the post-training phase of 3D MLLMs, achieving results that previously required two phases through noise introduction in a single phase.

This work focuses on the post-training phase of 3D MLLMs, achieving results that previously required two phases through noise introduction in a single phase. However, I have the following questions:
1.The experiments have not been sufficiently validated; I need to know the performance of the latest object-level 3D MLLMs like ShapeLLM.
2.I also need to understand how this performs at the scene level. Please select several scene-level 3D MLLMs to demonstrate their effectiveness on classic datasets like Scan2Cap and ScanQA.
3.While this method appears straightforward, its theoretical support requires more visualizations for validation.

### Questions
This work focuses on the post-training phase of 3D MLLMs, achieving results that previously required two phases through noise introduction in a single phase. However, I have the following questions:
1.The experiments have not been sufficiently validated; I need to know the performance of the latest object-level 3D MLLMs like ShapeLLM.
2.I also need to understand how this performs at the scene level. Please select several scene-level 3D MLLMs to demonstrate their effectiveness on classic datasets like Scan2Cap and ScanQA.
3.While this method appears straightforward, its theoretical support requires more visualizations for validation.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies 3D multi-modal LLMs for point cloud understanding. In contrast to previous frameworks in post-training optimization via 2 stages, this paper utilizes contrastive approaches for 1-stage 3D MLLM post-training. Careful designs on robust negative data augmentation and ground-truth anchor samples are presented. The benchmark evaluation is re-designed to focus more on the key factor. Experiments on ModelNet40 and Objaverse demonstrate the effectiveness.

### Strengths
- The post-training optimization task is interesting and useful.

- The proposed SPA module is effective and improves the performance of different 3D MLLMs generally, shown in Table 1.

### Weaknesses
1. Paper writing.

- Key difference between the proposed SPA and previous methods needs to be clarified. After reading this paper, I think the method is also a 2-stage post-training method. Correct me if I am wrong. From my understanding, this paper still generates positive and negative QA pairs from multiple positive and negative point cloud pairs in advance, and then optimizes the model based on InfoNCE. This is still a 1-stage generation and 2-stage training pipeline in my opinion. I suggest the authors clarify this aspect, regarding the key difference to 2-stage methods.

- Some terminology needs to be clarified. For example, in L236, the term "improved positive ground truths" first appeared. It is unaware of the meaning of "improved", and no pre-context appears in the paper.

2. Technical novelty.

- The technical contributions listed in this paper, including contrastive technology (Eq. (3) - Eq. (6)) and the robust negative data augmentation, are extensively explored in previous 3D understanding papers [1, 2]. Also, the idea of using augmentation to generate hard in-domain negative samples are also explored in point cloud understanding [1]. Therefore, the technical contribution is limited on my side. This paper utilizes previous methodology to solve previously solved problems.

[1] PointContrast: Unsupervised Pre-training for 3D Point Cloud Understanding

[2] Masked Autoencoders for Point Cloud Self-supervised Learning

3. Motivation.

- I don't see much application potential for 3D object-level point cloud QA. In Figure 2, I can only see some visual descriptions of single objects. For robotics applications, I think object-level relations are more important so as to locate and operate on target objects. More visual examples on ScanNet related to object-level relations and locations are suggested.

4. Experiments.

- Ablations on different post-training optimization like Figure 3 and Table 4 on other datasets, like ScanQA, are suggested.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents SPA, a simplified and effective post-training optimization method to align 3D and text features in LLMs with 3D encoders. As opposed to two-stage optimizations in previous work, SPA relies on a single-stage optimization that better utilizes the input 3D+text data.

The paper also introduces a new benchmark for 3D reasoning tasks: 3D Choice-level Questions and Answering. This benchmark repurposes portions of existing benchmarks, using pre-trained LLMs to generate more useful object- and scene-level questions. This benchmark can better assess 3D understanding capabilities of LLMs.

The proposed method outperforms previous work on existing benchmarks, as well as the new benchmark.

### Strengths
The method seems novel, at least for 3D point cloud applications.

The experiments and ablations demonstrate superior 3D point cloud understanding, as compared to previous work.

The new benchmark is more sophisticated than past ones, and will help advance the field.

The code is made public.

### Weaknesses
Writing and organization could be improved to help readers better understand the work.

The abstract starts by listing a few previous works with some details and issues for one of them. Instead, it should start by saying what the addition of 3D features into LLMs actually achieves -- better understanding of the world? ability to reason-about/extract/edit 3D representations? Then it can go into the issue of LLM size not increasing performance (performance of what tasks exactly?), which enhanced 3D encoder or more training does not help with. Finally, there is enough motivation to start talking about SPA.

Related work usually follows the introduction and precedes the presentation of the proposed method, in order to give context. It looks like your related work section can easily slide up to become section 2 without rewording.

Intro: It is not clear what the "traditional two-stage posttraining methods" refers to exactly. What are the two stages (is it SFT followed by RLHF?), and how do they contrast to the proposed single-stage method?

Preliminary: you may want to rephrase this as "Preliminaries"

Figure 3: Needs to be clearer. The layout is weird, where the surrounding text all of a sudden switches to 2-column. The figure is missing a caption explaining what it shows. The graphs should probably be bar charts rather than lines, because x coordinate does not represent some continuous value. Left figure should include an x axis label "3D Encoder" and the title should say something like "ModelNet40 accuracy for different 3D encoders". What is the difference between Encoder, Encoder+7B, Encoder+13B? Right figure is also missing the x-axis label and a clearer title.

Table 1: SPA doesn't seem to improve a couple of metrics with LLaVA-7B model. What can that be attributed to?

Figure 6: Talks about images, but I thought the only inputs were point clouds and text. Is this visualizing a different experiment that doesn't involve 3D data?

### Questions
The abstract starts by listing a few previous works with some details and issues for one of them. Instead, it should start by saying what the addition of 3D features into LLMs actually achieves -- better understanding of the world? ability to reason-about/extract/edit 3D representations? Then it can go into the issue of LLM size not increasing performance (performance of what tasks exactly?), which enhanced 3D encoder or more training does not help with. Finally, there is enough motivation to start talking about SPA.

Related work usually follows the introduction and precedes the presentation of the proposed method, in order to give context. It looks like your related work section can easily slide up to become section 2 without rewording.

Intro: It is not clear what the "traditional two-stage posttraining methods" refers to exactly. What are the two stages (is it SFT followed by RLHF?), and how do they contrast to the proposed single-stage method?

Preliminary: you may want to rephrase this as "Preliminaries"

Figure 3: Needs to be clearer. The layout is weird, where the surrounding text all of a sudden switches to 2-column. The figure is missing a caption explaining what it shows. The graphs should probably be bar charts rather than lines, because x coordinate does not represent some continuous value. Left figure should include an x axis label "3D Encoder" and the title should say something like "ModelNet40 accuracy for different 3D encoders". What is the difference between Encoder, Encoder+7B, Encoder+13B? Right figure is also missing the x-axis label and a clearer title.

Table 1: SPA doesn't seem to improve a couple of metrics with LLaVA-7B model. What can that be attributed to?

Figure 6: Talks about images, but I thought the only inputs were point clouds and text. Is this visualizing a different experiment that doesn't involve 3D data?

Have you tried applying this methodology for other multimodal contrastive training (such as images)?

### Soundness
3

### Presentation
2

### Contribution
3
