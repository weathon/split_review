# OMNIBAL: TOWARDS FAST INSTRUCT-TUNING FOR VISION-LANGUAGE MODELS VIA OMNIVERSE COMPUTATION BALANCE

- Decision: Reject
- Scores: 3, 6, 6

## Abstract
Recently, vision-language instruct-tuning models have made significant progress due to their more comprehensive understanding of the world. In this work, we discovered that large-scale 3D parallel training on those models leads to an imbalanced computation load across different devices. The vision and language parts are inherently heterogeneous: their data distribution and model architecture differ significantly, which affects distributed training efficiency. We rebalanced the computational loads from data, model, and memory perspectives to address this issue, achieving more balanced computation across devices. These three components are not independent but are closely connected, forming an omniverse balanced training framework. Specifically, for the data, we grouped instances into new balanced mini-batches within and across devices. For the model, we employed a search-based method to achieve a more balanced partitioning. For memory optimization, we adaptively adjusted the re-computation strategy for each partition to utilize the available memory fully. We conducted extensive experiments to validate the effectiveness of our method. Compared with the open-source training code of InternVL-Chat, we significantly reduced GPU days, achieving about 1.8x speed-up. Our method's efficacy and generalizability were further demonstrated across various models and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces OmniBal, a training framework that addresses computational imbalances in large-scale Vision-Language Models (VLMs) during 3D parallel distributed training. OmniBal improves efficiency by balancing data, model, and memory across devices. For data, the framework forms balanced mini-batches that reduce padding and minimize computational idle times. For the model, a search-based method is used to optimally partition vision and language components, addressing their inherent structural differences. For memory, adaptive re-computation maximizes memory utilization, enhancing training speed. Experiments show OmniBal reduces training time significantly.

### Strengths
1. This paper addresses a critical issue: accelerating distributed training for large-scale vision-language models (VLMs).

2. The authors present a comprehensive optimization framework that targets VLM distributed training from three perspectives: data, model, and memory balance.

### Weaknesses
1. The paper lacks sufficient motivation data to illustrate the imbalance problem quantitatively.

2. The contributions of this paper seems incremental.

3. Some figures have fonts that are too small, making them challenging to read and interpret.

### Questions
This paper propose OmniBal, which improves efficiency by balancing data, model, and memory across devices. It achieves significant improvements over baselines. However, I have following questions/concerns:

1. The data partitioning approach in this paper appears to offer limited novelty. Numerous adaptive data batching methods, such as [1] and [2], have already addressed similar issues, albeit without specific evaluations on VLMs. However, applying these techniques to VLMs does not seem particularly challenging, given that (i) the primary goal—balancing computation both within and across batches—is quite similar, and (ii) the methodology, which involves batching based on profiled or predicted latency, closely resembles the existing works. Could the authors clarify the unique contributions of their data partitioning method in comparison to these established batching approaches?

2.  The novelty of the model partitioning and re-computation strategies also seems limited. The AdaPipe framework, as referenced in the paper, performs layer-wise partitioning and adaptive re-computation based on computation and memory costs. Since the information needed for partitioning VLMs can also be easily profiled, could the authors explain the specific advantages of their approach over extending AdaPipe for VLMs?

3. The motivation for addressing data imbalance would be stronger with quantitative results from real datasets illustrating variation in sample sizes or computational demands. The simplified example in Figure 2 does not adequately demonstrate the scope of the issue.

4. The section on memory imbalance in Section 3 lacks clarity. While it states the need for aggressive re-computation, it would benefit from a discussion on potential opportunities to mitigate memory imbalance.

5. The figure in Appendix A.1.2 does not clearly illustrate how computation is balanced, making it difficult to assess the efficacy of the approach.

6. Section 4 introduces Q'v and Q't to reduce Pad Ratio and Dist Ratio, but the paper lacks a clear formula or explanation of how these values affect the ratios. This makes it challenging to understand how Q values are chosen to achieve the intended balance.

7. In Section 5, Q′v is set equal to Qv, while Q′t is defined as Qt − 128. Could the authors provide an intuition or rationale behind these choices?

8. The partitioning approach begins with an anchor partition strategy. What is the computational overhead for generating this anchor partition, and how close is it to the optimal partition? If it is far from optimal, what steps are taken to improve upon it? Conversely, if it is close, is it necessary to generate multiple new candidate partitions?

minor point(s):
1. The fonts in some figures are too small, particularly in Figure 3, where the axis labels and legends are difficult to read.


[1] Yu, Gyeong-In, Joo Seong Jeong, Geon-Woo Kim, Soojeong Kim, and Byung-Gon Chun. "Orca: A distributed serving system for {Transformer-Based} generative models." In 16th USENIX Symposium on Operating Systems Design and Implementation (OSDI 22), pp. 521-538. 2022.

[2] Choi, Yujeong, Yunseong Kim, and Minsoo Rhu. "Lazy batching: An sla-aware batching system for cloud machine learning inference." In 2021 IEEE International Symposium on High-Performance Computer Architecture (HPCA), pp. 493-506. IEEE, 2021.

### Soundness
2

### Presentation
2

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
This paper focuses on the 3D parallel training of MLLMs. The approach to balancing the computational load concerning data, model, and memory distribution both in-device and cross-device is straightforward yet effective. The proposed method demonstrates significant time reduction while maintaining the model's capabilities.

### Strengths
+ The paper centers on the efficient parallel training of MLLMs particularly focusing on balancing the computational load concerning data, model, and memory distribution both in-device and cross-device. 

+ The multi-modal sample balancing strategy stands out for its simplicity, offering a straightforward approach to load management. Despite its simplicity, the method proves to be effective, yielding significant reductions in training GPU hours while preserving the model’s capabilities. TItmakes the approach both accessible for large-scale applications.

+ It is comprehensively validated across different datasets, tasks, resolutions and hardware archs etc

### Weaknesses
 - Results on other MLLM architectures, especially those commonly used in the community such as the LLaVA series, are expected in a technical report style work.

### Questions
See weaknesses.

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
This paper aims at addressing the issue of imbalanced computation loads in large-scale 3D parallel training of vision-language models. It rebalances across data, model, and memory dimensions. Experimental results demonstrate that this method can effectively speed up training on many open-source models.

### Strengths
Strength：

1. Extensive experiments demonstrate the approach's effectiveness for rebalancing computation for MLLMs.
2. The motivation is clear and the in-depth analysis and ablations are convincing.
3. This paper is well-organized and clearly-written.

### Weaknesses
N/A

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3
