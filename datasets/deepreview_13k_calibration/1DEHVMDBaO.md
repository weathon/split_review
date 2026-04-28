# Adaptive Memory Mechanism in Vision Transformer for Long-form Video Understanding

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 5, 3, 5

## Abstract
In long-form video understanding, selecting an optimal Temporal Receptive Field (TRF) is crucial for Vision Transformer (ViT) models due to the dynamic nature of diverse video motion contents, which varies in duration and velocity. A short TRF can result in loss of critical information, while a long TRF may decrease ViT's performance and computational efficiency caused by the unrelated contents in videos and the quadratic complexity of the attention mechanism. To tackle this issue, we introduce Adaptive Memory Mechanism (AMM) that enables ViT to adjust its TRF dynamically in response to the video's dynamic contents. Instead of discarding Key-Value (KV) Cache from the earliest inference when the settings limit is reached, our approach uses a Memory Bank (MB) to retain the most important embeddings from the Key-Value Cache that would otherwise be discarded in memory-augmented methods. The selection is based on the attention score calculated between the Class Token (CLS) in current iteration and the KV Cache in previous iterations. We demonstrate that Adaptive Memory Vision Transformer (AMViT) outperforms existing methods across a diverse array of tasks (action recognition, action anticipation, and action detection).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses a solution for better long-form video understanding using a method named Adaptive Memory Mechanism (AMM). This method enables the Vision Transformer (ViT) to adjust its temporal receptive field dynamically depending on the input video. A memory bank is utilized to save the most important Key-Value when temporally processing the videos. The proposed method is tested on AVA and Epic-Kitchens datasets for action detection, recognition, and anticipation tasks. Experiment results show performance improvement to the ViT baselines without additional cost.

### Strengths
1. The method have better performance than baselines without additional cost.

### Weaknesses
1. The paper lacks SoTA comparisons. Is the task different from common action recognition and action detection? Multiple methods such as VideoMAE, Omnivore, or MMT have been tested on these datasets. It would be helpful if the authors could explain the difference between previous SoTAs with the proposed method, for example in parameter count or GFLOP difference.
2. The improvement to ViT and MeMVit baselines is marginal.
3. There is no difference in the FLOPs and Param(M) numbers compared to the baselines. Can the authors explain further the efficiency advantage achieved by the proposed method?

### Questions
1. Will there be a significant performance difference if the model is not pre-trained with UMT?

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
4

### Summary
This paper presents an adaptive memory method to improve the existing memory-augmented methods for long-form video understanding. The method is based on MeMViT but makes the memory bank adaptive to support the adaptive temporal receptive field. The experiments are conducted on Ava and Epic-Kitchens dataset with the comparison with ViT and MeMViT.

### Strengths
* Long-form video understanding is an important video research topic and the idea of using an adaptive memory bank sounds reasonable and promising. 
* Compared to MeMViT, the results show consistent improvements though some datasets only have marginal gain.

### Weaknesses
 * One of the main motivations of the paper is to retain embeddings instead of discarding memory when the memory limit is reached. However, based on the experiments, it's unclear if the effective receptive field of AMViT is indeed larger than MeMViT through the proposed adaptive memory module. Are they still using the same memory bank size? It's crucial to understand how the adaptive memory mechanism translates to a demonstrably larger effective receptive field, especially since the core idea is to retain potentially useful information that would otherwise be discarded. The paper lacks a clear analysis showing that the retained memory is actually contributing to a larger temporal context and improved performance, rather than just adding computational overhead.
* In the model section, the paper presents two new modules, including Input-aware selective module (ISM) and Adaptive Memory mechanism(AMM). However, there are no ablations to validate the individual effectiveness of these modules. It is necessary to isolate the contribution of each module to understand their individual impact on the overall performance. Without ablations, it's difficult to ascertain whether both modules are necessary or if one is more crucial than the other. Furthermore, it's unclear if the ISM module is truly selecting the most relevant information or if it's just performing a random selection, which could be detrimental to the performance.
* How do we select parameters for MeMViT? Some parameters for MeMViT (Table 6) are not defined, e.g, memory bank size. Is it the same as AMViT? Given the authors are reproducing MeMViT with a different backbone, how the results compare to the original paper. The lack of clarity on the memory bank size for MeMViT makes it difficult to assess the fairness of the comparison. It's also important to understand how the performance of the reproduced MeMViT compares to the original implementation to ensure that the baseline is properly established. This is particularly important since the authors are using a different backbone, which could impact the results.
* In Table 1, it's unclear why all the three methods are having the same FLOPs and parameters given MeMviT and AMViT has additional memory bank modules. It's also better to conduct run-time comparison. The fact that all three methods have the same FLOPs and parameters is counterintuitive, especially considering that MeMViT and AMViT have additional memory modules. This raises questions about the accuracy of the reported numbers. A run-time comparison would provide a more practical understanding of the computational overhead of the proposed method.
* The experiments are also missing a system-level comparison with the current SOTA results on the benchmarks. The lack of comparison with state-of-the-art methods makes it difficult to assess the significance of the proposed approach. It's important to compare the performance of AMViT with other leading methods to understand its relative strengths and weaknesses.

### Questions
Please see weaknesses

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper aims to enhance ViT for long-term video understanding. The authors design a memory bank to store historical information and develop input-aware adaptive memory selection to retrieve the relevant information to assist long-term analysis. The experiments show that the architecture demonstrates satisfactory performance with high efficiency.

### Strengths
1. The analysis of the limited temporal receptive field in long-term video understanding makes sense, and the motivation is clear.
2. The method is simple and intuitive.

### Weaknesses
1. The experiments are limited. Only AVA and Epic-Kitchens are reported. Results on more video datasets are required to verify the effectiveness of the adaptive memory design. Besides, the performance improvements are marginal.
2. The memory bank is recurrently updated by adaptive selection. Is it possible that in a long video, the content in the middle of the video is not closely related to the beginning, and only relevant content appears towards the end? However, during the memory bank update process, the tokens of the earlier video content were already discarded.

### Questions
1. Does the KV Cache in this paper retain the gradient?
2. This paper focuses on a pure vision model with enhanced memory design. However, the ViT-only architecture is capable of a limited range of video-related tasks. Is it possible to integrate it with video-language models to achieve wider range of video tasks to exert more impact on the community?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes an Adaptive Memory Mechanism (AMM) for Vision Transformer (ViT) in long-form video understanding. It addresses the issue of selecting an optimal Temporal Receptive Field by allowing ViT to adjust TRF dynamically. Instead of directly discarding early Key-Value cache, AMM uses a Memory Bank to retain important embeddings from the Key-Value cache based on attention scores. Experiments on AVA and Epic-Kitchens show the advantages of AMM in action recognition, anticipation, and detection tasks.

### Strengths
1.Long-form video understanding is an important research task, and the author has provided a reasonable solution.

2.The paper is well-written, making it easy to read.

### Weaknesses
1.The novelty of memory bank is limited. Many studies have explored how to utilize memory to retain important historical information and how to dynamically update memory. For example, Xmem[1] prioritizes retaining the most frequently used candidates. MA-LLM[2] and MovieChat[3] merge the two most similar candidates based on similarity once the memory bank capacity is exceeded. The innovations and advantages of the memory bank proposed in this paper compared to these methods are unclear.

2.The fairness of the experiment is in question. When comparing with the baseline model MeMViT, the authors replaced the backbone of MeMViT from MViT to UMT. This seems to have led to a decline in the performance of the baseline model. For example, in the EPIC-KITCHEN-100 action recognition task, the performance reported in the original paper on MeMViT was 48.4%, while the performance presented in this paper is 43.03%. The authors should maintain the same settings as MeMViT for the experiments to make the results more credible.

3.The performance improvement is limited. Compared to the baseline model MeMViT, the performance improvement is less than 1% in all experiments.

4.Lacks of comparison with the latest methods. This article only presents comparisons with ViT and MeMViT. Some recent methods are missing, such as MAT[4] and MC-ViT[5].

5.Lacks of necessary ablation studies. (2) This paper uses an input-aware selective module to prevent redundant embeddings from being retained, and uses a memory bank to retain useful embeddings. However, there are no ablation experiments to demonstrate the effectiveness of these two components individually. (2) The lack of ablation experiments on the memory bank update method. For example, comparing the update of the memory bank using attention score of class tokens proposed in this paper with previous methods (see weakness 1) and First-In-First-Out (FIFO).

### Questions
When comparing with MeMViT, your model uses the memory bank and the selected Q-V cache, while MeMViT only uses Q-V cache. Have you ensured that the number of embeddings in both model is consistent? Specifically, does the size of the memory bank plus the size of the selected Q-V cache match the size of the unselected Q-V cache?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces an Adaptive Memory Mechanism (AMM) to improve Vision Transformers (ViT) for long-form video understanding. AMM dynamically adjusts the Temporal Receptive Field (TRF) based on video content, overcoming limitations of fixed TRF approaches that either lose key information or increase computational costs. Experiments show that AMViT, integrating AMM, outperforms existing models like MeMViT in tasks such as action recognition, anticipation, and detection, while reducing computational overhead, validated on datasets like AVA and Epic-Kitchens.

### Strengths
1. Long-form video understanding is an important task, and efficiency is indeed a crucial metric in this context.

2. The proposed method can reduce both training and inference costs.

3. Introducing a memory bank to handle long sequence inputs is intuitive and reasonable.

### Weaknesses
1. (important) The number of benchmarks (only 2) and baselines (also only 2) compared seems somewhat limited. Adding more experiments would make the paper more convincing. Specifically, the paper should include a more comprehensive set of baselines, including both transformer-based and non-transformer-based methods for long-form video understanding. Furthermore, the current benchmarks, AVA and Epic-Kitchens, while popular, might not fully capture the nuances of extremely long videos. A more diverse set of benchmarks, including those with varying video lengths and complexities, would strengthen the paper's claims.

2. (important) Although the authors emphasize that the new architecture is designed for long-form video, this aspect is not discussed in the experimental section. Are the benchmarks presented in the paper truly for long videos, and what is the average input length? It would have been better if the authors had conducted more detailed evaluations on benchmarks like MovieChat-1K [1] or LongVideoBench [2]. The paper lacks a detailed analysis of how the proposed AMM handles varying lengths of video inputs. For example, how does the memory mechanism scale with longer videos, and what are the computational trade-offs? The paper should include experiments that specifically evaluate the performance of AMViT on videos of different lengths to demonstrate its effectiveness for long-form video understanding.

3. The writing and figures in the paper need improvement, especially regarding the notation for memory. There are too many subscripts and superscripts, along with the extensive use of qkv notations, which made it take me three times longer to understand the entire paper. The paper should simplify the notation and provide a clearer explanation of the memory mechanism. The figures should also be improved to better illustrate the architecture and the flow of information. For example, a diagram showing how the memory is updated and accessed would be beneficial. The current presentation makes it difficult to grasp the core ideas of the proposed method.

### Questions
Please revise the Weaknesses section point by point. This is a paper with great potential. If the authors can provide additional responses to certain issues, discuss related work more thoroughly, and include more experiments and observations, I would be very happy to raise my score.

### Soundness
3

### Presentation
2

### Contribution
3
