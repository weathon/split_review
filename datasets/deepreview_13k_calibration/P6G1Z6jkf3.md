# Modeling Fine-Grained Hand-Object Dynamics for Egocentric Video Representation Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In egocentric video understanding, the motion of hands and objects as well as their interactions play a significant role by nature.
However, existing egocentric video representation learning methods mainly focus on aligning video representation with high-level narrations, overlooking the intricate dynamics between hands and objects.
In this work, we aim to integrate the modeling of fine-grained hand-object dynamics into the video representation learning process.
Since no suitable data is available, we introduce HOD, a novel pipeline employing a hand-object detector and a large language model to generate high-quality narrations with detailed descriptions of hand-object dynamics. 
To learn these fine-grained dynamics, we propose EgoVideo, a model with a new lightweight motion adapter to capture fine-grained hand-object motion information. 
Through our co-training strategy, EgoVideo effectively and efficiently leverages the fine-grained hand-object dynamics in the HOD data. 
Extensive experiments demonstrate that our method achieves state-of-the-art performance across multiple egocentric downstream tasks, including improvements of 6.3% in EK-100 multi-instance retrieval, 5.7% in EK-100 classification, and 16.3% in EGTEA classification in zero-shot settings. Furthermore, our model exhibits robust generalization capabilities in hand-object interaction and robot manipulation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to enhance the understanding of complex hand-object interactions in egocentric video-text learning. To accomplish this, the authors introduce a pipeline called HOD, which combines a hand-object detector with a large language model (LLM) to generate high-quality, detailed descriptions of hand-object dynamics. Additionally, they propose a model named EgoVideo, which utilizes a lightweight motion adapter to capture fine-grained hand-object motion information. Through a co-training strategy, EgoVideo effectively and efficiently leverages the detailed hand-object dynamics provided by HOD data. Extensive experiments demonstrate that this approach achieves state-of-the-art performance across various egocentric downstream tasks.

### Strengths
This paper has good writing and is easy-to-follow, the idea is straightforward and the experiments shows remarkable improvement. Unlike some previous works who simply rely on extracting additional data of hand-object interaction, this paper provide an effective component (motion adapter) to utilize the data.

### Weaknesses
(1) While the motion adapter proves useful, it is not a novel approach, as similar techniques have been explored in numerous prior works. This does not lower my current rating, but it is the primary reason I have not assigned a score of 8. Specifically, the use of adapters for adapting pre-trained models to new tasks has become quite common, and the paper does not sufficiently articulate how their motion adapter differs fundamentally from existing adapter architectures or how it introduces a novel mechanism for capturing motion information beyond what is already achievable with standard temporal modeling approaches. (2) The experiments could be more comprehensive. For instance, it would be insightful to see performance results without any adapter, using only a single branch. This would help isolate the contribution of the motion adapter. Additionally, I am interested in the model's performance on more challenging tasks, such as robotic manipulation, which would demonstrate the generalizability of the approach to more complex scenarios. Providing such additional results could positively impact my rating.

### Questions
Please refer to my weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new method for learning from egocentric videos by focusing on hand-object interactions, which are vital for understanding these videos. The authors propose HOD (Hand-Object Dynamics), a system that generates detailed video captions using hand-object detectors and large language models. To leverage this enriched data, they present EgoVideo, a model with a lightweight motion adapter and a co-training strategy that effectively captures hand-object dynamics. EgoVideo outperforms other models in various egocentric video tasks and adapts well to applications like robot manipulation. Because my research field is somewhat distant from this article, I can only give a relatively general judgment. For more detailed judgments, please refer to the analysis of other reviewers.

### Strengths
1. The data generation pipeline creates high-quality video-language pairs, enhanced with detailed descriptions of hand-object interactions, enabling effective pretraining for video-language tasks.
2. The proposed methods demonstrate promise for real-world applications in augmented reality, robotic manipulation, and personalized assistants by achieving exceptional results in egocentric tasks.

### Weaknesses
1. The author should be more careful in writing. One of the most obvious mistakes is that the title of Figure 3 is wrong. Here, the author uses the title in Figure 6.
2. When the author obtains a better language description, they should also present the underlying semantic rules to clarify its rationale. Furthermore, evaluating the description's quality is essential to ensure standardization and scientific rigor.
3. I think the author could do some further qualitative analysis, starting with the good cases and bad cases. These examples could be considered to be put in the main text instead of the appendix to help readers better understand.

### Questions
Please see weakness

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
The paper presents a new method for egocentric video representation learning that integrates fine-grained hand-object dynamics. It introduces the HOD data pipeline for generating detailed captions and the EgoVideo model, which uses a lightweight motion adapter for efficient learning. The approach achieves state-of-the-art performance across various tasks.

### Strengths
1. The HOD pipeline effectively enriches video annotations with hand-object dynamics, capturing interactions more realistically than prior approaches.
2. By using a lightweight motion adapter and co-training strategy, EgoVideo is effective in capturing detailed movements.

### Weaknesses
1. Adding a figure to introduce the “Motion Adapter” would make it more intuitive.
2. The proposed method lacks comparison with other methods in terms of parameter and computational complexity.

### Questions
1. What is the inference process of the proposed method? If it still relies on both the hand-object detector and LLM as in training, will it significantly increase inference time?
2. The HOD framework uses the original caption as input; what should be done if the dataset lacks corresponding annotation information?

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
The authors introduce a new video-language model that learns video representations from fine-grained hand-object interaction descriptions. Unlike previous works that learn from abstract short texts with a fixed number of frames, they propose HOD and EgoVideo. HOD generates detailed descriptions by prompting a large language model (LLM) using noisy HOI bounding boxes, while EgoVideo incorporates a dual-branch video architecture that adopts a backbone and a lightweight adapter to handle inputs with different frame sampling rates. The authors conduct comprehensive experiments across various benchmarks to demonstrate the strength of their pretrained model.

### Strengths
- **Good Paper Writing**: The paper is well-organized, clear, and easy to follow.
- **Useful Architecture for Egocentric Video Understanding**: The architecture effectively improves performance in the egocentric domain, though the core idea of learning from varying frame sampling rates originates from SlowFast. The proposal of using the lightweight adapter increase only a few parameters.
- **Extensive Experiments and SoTA Performance**: The proposed EgoVideo-G (their largest model) achieves state-of-the-art performance across all benchmarks. The experiments cover a wide range of datasets and domains, including commonly used evaluation datasets in egocentric contexts like Epic-Kitchens-MIR and EgoMCQ, as well as evaluations in robotic manipulation. I appreciate the additional focus on robotic applications.

### Weaknesses
 - **Lack of Analyses on HOD Data Corpus or Quality**: This paper lacks thorough analyses of the data corpus, especially considering the data generation pipeline is simple and naive. From the motivation of HOD, the authors claim to create 'HOI dynamics' using an HOI detector. However, since the HOI detector is image-based, there is no guarantee that the generated texts will capture temporal information. While I acknowledge the robustness of the HOI detector, I am unsure if this robustness ensures consistent temporal information and how much noise would impact the final model. From the data corpus, the authors do not analyze the data statistics of the generated texts at any perspective except for the experimental results. As a result, I have limited insight into the quality of the pretraining dataset. To illustrate the significance, take what LaViLa has done as an example. To demonstrate the effectiveness of generated sentences, LaViLa's Narrator evaluates their model on the validation set of Ego4D. I think similar experiments are essential to validate the usefulness of HOD. For instance, it is important to determine whether the original information is remained in the generated text and whether there are unreliable hallucinations present from Yi-34B.
- **Inadequate Analyses at Inference Time**: While mainstream video-language models use 4 frames during inference, EgoVideo requires sampling both 4 and 16 frames, leading to slower inference speeds and also potential unfair comparisons. Although Table 4 demonstrates the effectiveness of training EgoVideo jointly with 4 and 16 frames, another straightforward baseline of other models incorporating test-time augmentation, e.g., simply aggregating outputs of AVION-4f from both 4 and 16 frames, would enhance the evaluation. Besides, I think the comparison on GFLOPS during inference between models should also be provided.
- **Lack of Citation**: The key idea in EgoVideo is closely related to the well-known SlowFast Network [SlowFastNetworks for Video Recognition](https://arxiv.org/abs/1812.03982) (ICCV 2019), but the authors do not cite it. Although their implementation ways are different, I recommend including this citation and adding a proper discuss.
- **Lack of Parameter Comparisons in Table 1**: In addition to dataset sizes, I suggest adding information on trainable parameters, as models like Helping Hands have significantly fewer trainable parameters than other methods.
- **Improper Comparison of EgoVideo-G**: One problem is the unfair comparisons involving EgoVideo-G with other models. While the Giant model demonstrates impressive performance, it lacks a fair comparison with other models that primarily use smaller variants. Besides, other backbones mainly leverage CLIP for initialization, whereas EgoVideo-G is initialized with the state-of-the-art InterVideo2 (L313). This not only means a larger model size but also a different initialization method. There is a lack of a straightforward ablation study or adequate explanation the choices.
- **Improper Comparison in Robot Manipulation**: While I appreciate the emphasis on robot manipulation, the comparison is unfair, as EgoVideo-G (2B) is significantly larger than other methods (e.g., MPI-Base, which is only 86M). The authors should include control speed and parameter sizes, as EgoVideo-G is likely slower and larger than the other methods, which impacts the evaluation.
- **Input to the Manipulation Model**: During the manipulation process, EgoVideo relies on multiple frames as input, whereas methods like MPI use only a single observed frame. I'm curious about how the authors address this difference.

### Questions
- **Lack of Citation**: The key idea in EgoVideo is closely related to the well-known SlowFast Network [SlowFastNetworks for Video Recognition](https://arxiv.org/abs/1812.03982) (ICCV 2019), but the authors do not cite it. Although their implementation ways are different, I recommend including this citation and adding a proper discuss.
- **Lack of Parameter Comparisons in Table 1**: In addition to dataset sizes, I suggest adding information on trainable parameters, as models like Helping Hands have significantly fewer trainable parameters than other methods.
- **Improper Comparison of EgoVideo-G**: One problem is the unfair comparisons involving EgoVideo-G with other models. While the Giant model demonstrates impressive performance, it lacks a fair comparison with other models that primarily use smaller variants. Besides, other backbones mainly leverage CLIP for initialization, whereas EgoVideo-G is initialized with the state-of-the-art InterVideo2 (L313). This not only means a larger model size but also a different initialization method. There is a lack of a straightforward ablation study or adequate explanation the choices.
- **Improper Comparison in Robot Manipulation**: While I appreciate the emphasis on robot manipulation, the comparison is unfair, as EgoVideo-G (2B) is significantly larger than other methods (e.g., MPI-Base, which is only 86M). The authors should include control speed and parameter sizes, as EgoVideo-G is likely slower and larger than the other methods, which impacts the evaluation.
- **Input to the Manipulation Model**: During the manipulation process, EgoVideo relies on multiple frames as input, whereas methods like MPI use only a single observed frame. I'm curious about how the authors address this difference.

### Soundness
3

### Presentation
3

### Contribution
3
