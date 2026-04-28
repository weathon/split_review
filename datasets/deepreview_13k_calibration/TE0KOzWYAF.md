# VLM2Vec: Training Vision-Language Models for Massive Multimodal Embedding Tasks

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 3, 8

## Abstract
Embedding models have been crucial in enabling various downstream tasks such as semantic similarity, information retrieval, and clustering. Recently, there has been a surge of interest in developing universal text embedding models that can generalize across tasks (e.g., MTEB). However, progress in learning universal multimodal embedding models has been relatively slow despite their importance. In this work, we aim to explore the potential for building universal embeddings capable of handling a wide range of downstream tasks. Our contributions are twofold: (1) MMEB (Massive Multimodal Embedding Benchmark), which covers 4 meta-tasks (i.e. classification, visual question answering, multimodal retrieval, and visual grounding) and 36 datasets, including 20 training and 16 evaluation datasets, and (2) \model (Vision-Language Model $\rightarrow$ Vector), a contrastive training framework that converts any state-of-the-art vision-language model into an embedding model via training on MMEB. Unlike previous models such as CLIP and BLIP, \model can process any combination of images and text to generate a fixed-dimensional vector based on task instructions. We build a series of \model models on Phi-3.5-V and evaluate them on MMEB's evaluation split. Our results show that \model achieves an absolute average improvement of 10\% to 20\% over existing multimodal embedding models on both in-distribution and out-of-distribution datasets in MMEB.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents to learn universal multimodal embedding models and introduces a novel benchmark (massive multimodal embedding benchmark, MMEB) to evaluate multimodal embedding.
The proposed VLM2VEC framework makes any state-of-the-art vision-language models (VLMs) multimodal embedding models through contrastive learning.
The MMEB dataset is collected from 36 public datasets (e.g. ImageNet, MSCOCO), covering 4 meta-tasks (e.g. VQA, retrieval).
Extensive experiments provide several baselines for multimodal embeddings and validate the effectiveness of the proposed VLM2VEC framework.

### Strengths
**[S1]** This paper is well-motivated and well-written.

**[S2]** I strongly agree with the requirement for a benchmark for evaluating multimodal embedding. The MMEB benchmark covers a wide range of tasks and is therefore sufficient to assess multimodal embeddings' capability appropriately.

**[S3]** This paper presents extensive experimental results with several baselines for multimodal embedding, providing a good benchmark for the following research.

### Weaknesses
 **[W1] Novelty of VLM2VEC.**
The main concern is the limited novelty of the proposed VLM2VEC framework.
The proposed framework is significantly similar to the recent works that ground LLMs to visual data with pretrained image models and large language models, such as [1, 2].
In other words, projecting visual representations into LLM's input space and tuning the whole or partial model with text generation or contrastive objectives is a typical approach for the recent multimodal large language models.
Although I acknowledge the contribution to the purpose and necessity of this work, it would be good to emphasize the difference that the proposed framework is exclusive only for multimodal embedding.

### Questions
**[Q1] About [EOS] token in the learning objective.** VLM2VEC applies the InfoNCE loss to [EOS] tokens. I understand that the output [EOS] token reflects information gathered through the model’s attention over all preceding input tokens. Could the [EOS] token be replaced by a class token or learnable token? I expect that there will not be a big difference in performance. I wonder if the authors have a valid reason for taking [EOS] tokens or can provide results regarding output token selection.

**[Q2] Inference procedure.** [EOS] token of the output may be used as a single multimodal embedding. Although the inference procedure for each meta-task is well known, it would be good to explain the inference procedure through multimodal embedding. Specifically, I think that classification, VQA, and retrieval can be performed by measuring the similarity between outputs. However, it is not easy to guess how the inference of visual grounding is done.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel framework called VLM2Vec for training vision-language models into embedding models capable of handling massive multimodal embedding tasks. This paper proposes MMEB, a benchmark with 36 datasets spanning classification, visual question answering, retrieval, and visual grounding. VLM2Vec deeply integrates visual and textual features, enabling it to capture cross-modal relationships more effectively.

### Strengths
1. Extensive experiments are conducted using multiple datasets and baselines, demonstrating the effectiveness of the proposed framework.
2. The development of the MMEB is original, as it provides a comprehensive framework for training and evaluating embedding models across diverse tasks and modalities.
3. Detailed ablation studies are performed to analyze the impact of various hyperparameters and training strategies on the model's performance.

### Weaknesses
Here are my constructive insights on how the paper could improve:
1. Benchmark Design: The number of candidates for each retrieval task in the MMEB benchmark is limited to 1000, which may not accurately reflect real-world scenarios where the number of candidates could be much larger. Increasing the number of candidates would make the benchmark more realistic and challenging.
2. Instead of randomly selecting 1000 candidates for each task, the standard test sets provided by the original datasets should be used. This would ensure a fairer comparison with other methods that have been evaluated on these datasets.
3. Fair Comparison: Table 2 compares VLM2Vec with baseline methods that have not been trained on the MMEB training sets. For a more accurate comparison, it would be insightful to retrain the baseline methods on the same training sets and then compare their performance with VLM2Vec. 
4. Baseline Evaluation: The paper mentions UniIR but does not include results for the UniIR-CLIP version, which according to the UniIR paper, performs better than the UniIR-BLIP version. Including these results would provide a more comprehensive comparison.
5. The MMEB benchmark reformulates classification, VQA, retrieval, and visual grounding tasks as ranking problems. While ranking-based formulations can be useful for classification and retrieval tasks, applying the same approach to VQA and visual grounding might not be ideal. These tasks often require more nuanced understanding and reasoning. Considering alternative formulations, such as direct answer generation for VQA and object localization for visual grounding, might yield more meaningful results and better reflect the nature of these tasks.

### Questions
Refer to weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper focuses on the development of universal multimodal embedding models. The authors introduce the Massive Multimodal Embedding Benchmark (MMEB), which comprises classification, visual question answering (VQA), retrieval, and grounding tasks. They propose a contrastive training framework, VLM2Vec, to transform VLM into an embedding model. Experimental results demonstrate that VLM2Vec achieves promising performance on the MMEB.

### Strengths
1. The writing is clear and easy to understand. This paper is easy to follow.
2. The constructed benchmark, MMEB, covers a wide range of tasks and is valuable.

### Weaknesses
1. The experiments presented are insufficient, as the authors limit their evaluation to the proposed MMEB benchmarks using only the precision metric. To provide a more comprehensive comparison with other clip-like models, it is crucial to assess the embedding model on some traditional benchmarks, such as ELEVATER and zero-shot retrieval on COCO and Flickr30k. The lack of standard retrieval metrics like Recall@K, MRR, and NDCG further limits the evaluation's completeness.
2. The evaluation of out-of-distribution may be unfair. Current MLLMs are usually fine-tuned on various downstream datasets. Most of datasets that construct MMEB are usually used in the fine-tuning stage of MLLMs. Since Phi-3.5-V doesn't provide details of fine-tuning datasets,  it is hard to evaluate the out-of-distribution capabilities of VLM2Vec. The potential for data leakage from pretraining datasets into the MMEB benchmark, especially for retrieval tasks, raises concerns about the validity of the OOD evaluation. This overlap could inflate performance metrics and not accurately reflect true generalization.
3. Lack of some experimental details. The authors need to provide details of the training of the comparative models on the MMEB in-domain datasets. Additionally, it is unfair to compare CLIP without instructions. Although the authors claim that based on other related work, introducting instructions to CLIP would not perform well, Table 4 shows that instructions have a significant impact, and the CLIP model should also have experimental results under the same settings.

### Questions
1. What do the x-axis and legend in Figure 5 represent? What do the three subplots represent respectively?
2. Does this training method affect the original capabilities of MLLM? I'm curious about the performance of VLM2Vec on MLLM-related benchmarks, such as MMBench and MME.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a multimodal embedding framework and introduces a comprehensive dataset, MMEB, which includes 36 datasets across four meta-task categories, specifically designed for training and evaluating embedding models. Additionally, the paper proposes VLM2VEC, a contrastive training framework that adapts an existing vision-language model into an embedding model. Experimental results indicate that the proposed model achieves 10%~20% improvement over previous multimodal embedding models, on both in-distribution and out-of-distribution datasets.

### Strengths
1. The method introduced in this paper is robust. With the authors' commitment to open- sourcing both the model and data, the proposed approach will to be valuable for a wide range of applications.
2. The experiments are thorough, effectively demonstrating the model's efficacy.
3. The paper is well-structured and clearly written.

### Weaknesses
1. The method proposed in this paper is relatively straightforward. Its performance, however, varies significantly across different tasks. Would suggest including more comparative experiments to explore and clarify the reasons behind these performance differences across tasks.

### Questions
n/a

### Soundness
3

### Presentation
4

### Contribution
3
