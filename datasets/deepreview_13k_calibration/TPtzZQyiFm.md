# MLLM Is a Strong Reranker: Advancing Multimodal Retrieval-augmented Generation via Knowledge-enhanced Reranking and Noise-injected Training

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 6, 5, 5

## Abstract
Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in processing and generating content across multiple data modalities. However, a significant drawback of MLLMs is their reliance on static training data, leading to outdated information and limited contextual awareness. This static nature hampers their ability to provide accurate and up-to-date responses, particularly in dynamic or rapidly evolving contexts. Though integrating Multimodal Retrieval-augmented Generation (Multimodal RAG) offers a promising solution, the system would inevitably encounter the multi-granularity noisy correspondence (MNC) problem, which hinders accurate retrieval and generation. In this work, we propose \textbf{RagVL}, a novel framework with knowledge-enhanced reranking and noise-injected training, to address these limitations. We instruction-tune the MLLM with a simple yet effective instruction template to induce its ranking ability and serve it as a reranker to precisely filter the top-k retrieved images. For generation, we inject visual noise during training at the data and token levels to enhance the generator's robustness. Extensive experiments on the subsets of two datasets that require retrieving and reasoning over images to answer a given query verify the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new framework called RagVL, designed to enhance the performance of Multimodal Large Language Models (MLLMs) in retrieval-augmented generation tasks. The study addresses the common issue of multi-granularity noisy correspondence (MNC) in multimodal retrieval. To tackle this, RagVL employs two main strategies: knowledge-enhanced reranking and noise-injected training. The framework uses instruction tuning to enable the model to accurately select images relevant to the query, and it introduces visual noise during training to improve model robustness. Experimental results demonstrate that RagVL significantly improves retrieval and generation performance across multiple datasets, particularly in scenarios that require fine-grained visual understanding.

### Strengths
1. Effectively Mitigating the Multi-Granularity Noisy Correspondence (MNC) Problem: By employing the knowledge-enhanced reranking module, the paper uses instruction tuning to equip MLLMs with stronger semantic understanding and reranking capabilities, enabling more precise selection of visual information relevant to the query. This approach significantly improves retrieval accuracy.

2. Enhanced Model Robustness: Through the noise-injected training method, visual noise is introduced at both the data and token levels, which boosts the model’s robustness when handling multimodal data. Experimental results show that this method notably enhances overall performance in multimodal retrieval and generation tasks, particularly in scenarios that require fine-grained visual understanding.

### Weaknesses
1. As presented in Table 2, the two approaches introduced in reranking thresholds show improvements in most metrics but exhibit instability. Specifically, while precision generally increases with the application of thresholds, recall can decrease, suggesting a trade-off that is not consistently beneficial across all evaluation criteria. This instability indicates that the thresholding mechanism may be overly sensitive to the specific characteristics of the dataset or query, leading to unpredictable performance fluctuations.
2. Although the introduction of the MLLM reranker resulted in some performance improvement, it requires a substantial amount of additional inference time. When using only CIPL to select the top-K, the time taken is 1.23 seconds, but incorporating the reranker adds an extra 5 to 6 seconds. This significant increase in latency raises concerns about the practical applicability of the method in real-time or resource-constrained environments, where inference speed is often a critical factor. The added computational burden may outweigh the benefits of improved retrieval accuracy in many use cases.

### Questions
1. MLLM possesses strong capabilities, but using it as an additional reranker seems to introduce significant computational overhead. Please discuss scenarios where performance improvements might justify the extra computational cost.
2. The two methods introduced for reranking thresholds have shown improvements across most metrics but also exhibited instability. After incorporating the reranking thresholds, the model’s recall decreased. Please analyze the reasons behind this phenomenon.

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
2

### Summary
This paper proposes RagVL, a novel framework designed to enhance Multimodal Large Language Models (MLLMs) by addressing the multi-granularity noisy correspondence (MNC) problem in multimodal retrieval-augmented generation (RAG). RagVL achieves this through knowledge-enhanced reranking and noise-injected training. By instruction-tuning MLLMs for effective reranking, RagVL improves the accuracy of image-text relevance, allowing models to select top candidates in multimodal retrieval tasks. Additionally, the framework introduces visual noise during training at both data and token levels, bolstering robustness in generation. Extensive experiments on datasets such as WebQA and MultimodalQA demonstrate RagVL's improved retrieval precision and resilience in multimodal question answering, making it effective for scenarios that require fine-grained visual understanding and real-world noise management​.

### Strengths
1. This paper is well-motivated.
2. This paper is well-written.
3. The proposed knowledge-enhanced reranking and noise-injected training techniques seem make sense.

### Weaknesses
1. Reranking with MLLM is actually very time consuming compared to clip, and MLLM without Captions-aware IT in the Table 1 doesn't gain any performance.
2. The interpretation and analysis of the experimental results are insufficient. For example, in Table 12, why is the effect of no effect ND better in a single image scenario.
3. The performance improvement seems to depend on Image Caption. I wonder if the author's method is limited if no image caption is provided or if the image caption is poor.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this work, the authors propose the RagVL framework to enhance the performance of Multimodal Large Language Models (MLLMs) in Multimodal Retrieval-Augmented Generation (RAG). The framework filters retrieved images using a fine-tuned MLLM ranker, while a generator model, also fine-tuned on RAG tasks, references these retrieved images to produce improved outputs. During training, the generator is enhanced for robustness through both coarse- and fine-grained noise injection, addressing the challenge of handling incorrect retrievals. Experimental results demonstrate the framework’s effectiveness.

### Strengths
Addressing multimodal RAG for MLLMs tackles an important problem.
Experimental findings show the proposed framework’s effectiveness in retrieval tasks and in improving Visual Question Answering (VQA) with RAG.

### Weaknesses
The framework may lack substantial novelty. The RagVL approach appears to combine an MLLM ranker with elements from existing techniques, including Visual Contrastive Decoding ([1], for fine-grained noise injection) and Robust RAG Training ([2], for coarse-grained noise injection). Using LLMs/MLLMs as rankers (reward models) in Reinforcement Learning from Human Feedback (RLHF) is already a common approach.

### Questions
1. How does the proposed coarse-grained noise injection differ from and relate to Robust RAG Training?
2. Does noise-injected training affect the MLLM’s general performance (i.e., on standard benchmarks such as MME or MMBench?)

### Soundness
3

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
The paper aims to address the limitations of MLLMs, which struggle to maintain accurate, up-to-date responses due to their reliance on static training data. To this end, the authors introduce RagVL, a framework that integrates RAG while addressing the multi-granularity noisy correspondence issue. RagVL enhances retrieval performance through knowledge-driven reranking and noise-injected training. The authors employ instruction tuning with a specific template, enabling the model to rank retrieved images effectively and filter top-k candidates for improved retrieval quality. Additionally, noise injection at data and token levels during training further strengthens knowledge-intensive generation. Experiments across four datasets demonstrate RagVL’s effectiveness.

### Strengths
+ Study the reranking abilities of MLLMs and integrate RAG for knowledge-intensive VQA. 

+ The proposed instruction tuning methods allows for targeted ranking improvements, optimizing retrieval and filtering accuracy.

+ Experimental validation confirms RagVL’s impact on performance across diverse datasets.

### Weaknesses
 - The authors mentions that they integrate “Multimodal RAG” in the Abstract and Introduction sections, but it seems that the retrieved content is only limited to image modality, so it would be clearer to point out what type of modalities are considered in this work at the beginning.

- The title and abstract are highlighting RAG, but the main content of this manuscript focuses on re-ranking of MLLM, which is inconsistent.

- The motivation of using noise distort image is unclear.

- The authors resort to an existing method, i.e., VCD, for logit contrastive learning and propose to adopt the difference between logits as a visual correlation weight in the MLE loss, but fail to tell clearly why they do that.

- The performance comparison between the proposed method and CLIP seems unfair, since CLIP is not fine-tuned but the proposed method does. To make a fair comparison, it is recommended to fine-tune CLIP using the same training data.

- The description of the adaptive thresholding strategy in Sec. 3.3 is unclear. Besides, the authors “experiment on the validation set and utilize the intersection point ...” in this section, and “report the results on the validation set” in Sec. 4.1. This practice may not be rigorous if the hyperparameters are tuned based on the same set on which the results are reported, which may cause data or label leakage.

- In Tab 2, the two thresholds may perform differently, e.g., adaptive threshold is helpful to Precision but harmful to Recall. More explanations are expected. Besides, how do the two thresholds influence the VQA performance?

- Some unclear experimental details. For example, Do the model “InternVL2-1B w/ CLIP Top-N” undergo next-token prediction fine-tuning with the same training data used in the proposed method? If not, it may be unfair.

- After a careful comparison with existing work, the technical novelty of this work is still questionable. Specifically, the noise-injected training method (Eqn. 5-7) appears to be very similar to existing contrastive alignment methods.

- The performance gains of RagVL over RagVL w/o ND & NLC are not very significant, especially considering the increased computational cost of using a much larger MLLM (InternVL2-2B) as the re-ranker compared to CLIP-L, which has fewer than 0.5B parameters. The marginal improvement on knowledge VQA tasks does not seem to justify the increased computational overhead.

### Questions
- What does the textual query q denote in Sec. 3.2, questions in VQA scenarios? Please make it clearer. 

- Would be the proposed method harmful to the general abilities in some VQA tasks except for knowledge-intensive abilities?

### Soundness
2

### Presentation
2

### Contribution
2
