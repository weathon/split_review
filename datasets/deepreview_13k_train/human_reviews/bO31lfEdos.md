# Mitigating Object Hallucination in Large Vision Language Model with Human-Free Reinforcement Learning

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Large Vision-Language Models (LVLMs) have excelled in joint visual and language understanding, particularly in generating detailed image captions. However, they still struggle with object hallucination, where non-existent objects are described, especially in long captions. While fine-tuning through supervised learning with enhanced datasets or reinforcement learning from human feedback can alleviate this issue, these methods demand considerable human effort, limiting scalability. This paper addresses this challenge by introducing a human-free framework to mitigate object hallucination in LVLMs for image captioning, utilizing reinforcement learning driven exclusively by automatic natural language processing metrics. We demonstrate that the following framework can effectively mitigate hallucination: (1) caption generation is formulated as a Markov Decision Process (MDP); (2) minimizing hallucination while maintaining caption quality is guided by a reward function, combining a proposed \textit{F1Score} with a penalty on Kullback–Leibler divergence from the pre-trained model; (3) fine-tuning the LVLM within the MDP framework can be performed directly by Proximal Policy Optimization (PPO) with careful attention to architectural details. Extensive experiments demonstrate a significant reduction in hallucination by up to 41\% while preserving the caption quality compared to the baseline model, InstructBLIP, on the COCO dataset. This improvement is reflected in consistent gains in object coverage and accuracy across various models and datasets. Notably, our method achieves comparable or superior performance to alternative approaches, all without requiring any human involvement.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles the problem of object hallucination in large vision-language models for image captioning. The key technical contribution is a human-free framework based on reinforcement learning and automatic NLP metrics.  The framework formulates caption generation as a Markov Decision Process, using a reward function that balances hallucination reduction with maintaining caption quality.  Experiments show this approach significantly reduces hallucination while preserving or improving caption quality compared to baselines, without needing any human input.

### Strengths
1. This paper proposes a new reinforcement learning method for reducing the object hallucination. 

2. This work points out that the existing metric CHAIR ignores the recall and proposes the F1 metric that evaluates both precision and recall.

### Weaknesses
1. The following two relevant works are ignored in the paper. Both paper propose new benchmarks for object hallucination.
[A] Ben-Kish et al., Mitigating Open-Vocabulary Caption Hallucinations. 
[B] Petryk et al., ALOHa: A New Measure for Hallucination in Captioning Models.

2. The motivation of using reinforcement learning is not clearly explained. 

3. The paper relies pretrained an object detector to eliminate human annotations. Therefore, the performance of the model relies on and might be biased to the object detector used. There is no discussion on this point in the paper.

4. More recent baselines should be compared. The baselines (LLAVA, mPLUG-Owl) in Table 4 are from 2023. New versions of LLAVA and mPLUG-Owl are introduced in 2024.

### Questions
1. What is the reason of adopting a different metric for the Genome dataset? why not use F1 or CHAIR?

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
3

### Summary
This paper addresses the challenge of object hallucination in Large Vision Language Models (LVLMs) for image captioning by introducing a human-free framework that employs reinforcement learning driven solely by automatic natural language processing metrics. Central to this approach is the notion that the image captioning task can be effectively modeled as a Markov Decision Process (MDP), due to its inherently sequential nature, where each token generation represents a decision influenced by the current state. Building on this framework, the paper fine-tunes the existing model using a dedicated reward function alongside Proximal Policy Optimization (PPO). This method achieves performance that is comparable to or even superior to alternative approaches, all without any human involvement.

### Strengths
Framing the image captioning task as a Markov Decision Process (MDP) and utilizing reinforcement learning driven exclusively by automatic natural language processing metrics is both reasonable and intriguing.

### Weaknesses
1. This paper currently validates the effectiveness of the proposed method only based on InstructBLIP, making it difficult to verify its broader applicability. The method’s generalizability across different baselines, such as mPLUG-Owl and LLaVA, should be demonstrated.
2. The authors use the F1 Score to address object hallucination, but this approach is not well-motivated. While F1 Score balances accuracy and recall, it does not have a direct connection with the issue of object hallucination. The authors should provide more theoretical and experimental analysis to support their rationale. In lines 521-523, they mention a minor side effect of their method: the average caption length is shorter than the baseline (85 tokens compared to 110 tokens). This raises the question of whether their proposed framework reduces object hallucination simply by shortening the output length.
3. Using prompt tuning to reduce object hallucination has indeed shown some effectiveness. However, the prompts used by the authors are automatically generated without human intervention, which means these prompts themselves might contain hallucinations or errors. Thus, evaluating the accuracy and validity of these generated samples becomes a critical issue. The authors should provide additional analysis to demonstrate the reliability of these prompts to better support the effectiveness of this approach.

### Questions
See Weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a human-free RL alignment framework to mitigate object hallucinations in multimodal LLMs, where the output captions contain non-existent objects. The aim of this paper is to relieve the burden of data collection and label annotation for fine-tuning or performing RLHF. To achieve this goal, they proposed utilizing the F1 score together with KL divergence as the reward and then applying PPO for model alignment. More specifically, the F1 score encourages the output captions with fewer hallucinations, while the KL divergence maintains the quality of image captions from the base model. The experiments and quantitative comparisons are conducted on the commonly used COCO dataset.

### Strengths
1. Alleviating object hallucination issues is crucial for trustworthy model deployment in several real-world applications, such as healthcare or manufacturing. This task aims to improve the faithfulness of multimodal LLMs on image captioning tasks, which could benefit image captioning tasks requiring high standard truthfulness, like report generation from medical images.
2. The proposed reward function constructed by the F1 score and KL divergence is reasonable and technical sound.
3. The overall paper is easy to follow.

### Weaknesses
1. This paper trains and evaluates the models on the COCO dataset. While this training manner avoids additional effort for collecting and annotating human preference data, I’m wondering whether the original capabilities of LVLMs (i.e., base model) can be adequately preserved. This paper only demonstrates the results of captioning quality on the COCO dataset in Figure 5. However, does the tuned model still maintain the captioning capability of the base model compared to other datasets? My concern is whether the original generalizability of the base model would be destroyed after being tuned by the proposed method.
2. In addition, the title of this paper claims to mitigate object hallucinations in large vision language models. Can other vision-language tasks like VQA or visual chatting also benefit from the proposed RL tuning process? Only considering image captioning tasks cannot fully support the claim of mitigating object hallucinations of LVLMs.
3. From the qualitative results shown in Section I of the Appendix, the outputs from the proposed method are shorter than those of the base model. As we know, the outputs from LVLMs are generally more detailed and comprehensive than the ground truth of the COCO dataset. The results in the Appendix show that the detailed captioning properties of LVLMs are destroyed. More clarifications are encouraged.

### Questions
Please refer to the Weaknesses. The following is a minor question.

1. This paper only considers InstructBLIP to be the LVLM. Are other commonly used LVLMs, such as LLaVA or VILA, also applicable to this proposed RL tuning framework?

### Soundness
2

### Presentation
3

### Contribution
2
