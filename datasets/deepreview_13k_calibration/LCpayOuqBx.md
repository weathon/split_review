# DOS: Dreaming Outlier Semantics for Out-of-distribution Detection

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 8, 3

## Abstract
Detecting out-of-distribution (OOD) samples is essential when deploying machine learning models in open-world scenarios. Zero-shot OOD detection, requiring no training on in-distribution (ID) data, has been possible with the advent of vision-language models like CLIP. This scenario presents a more practical alternative than traditional OOD detection. By building a text-based classifier with only closed-set labels, the model can achieve impressive OOD detection performance. However, this largely restricts the inherent capability of CLIP to recognize samples from large, open label space, making it insufficient to detect hard OOD samples effectively. In this paper, we provide a new perspective to tackle the constraints posed by exclusively employing closed-set ID labels in zero-shot OOD detection. We propose leveraging the expert knowledge and reasoning capability of large language models (LLM) to Dream potential Outlier Semantics, termed DOS, without access to any actual OOD data. Owing to better consideration of open-world scenarios, DOS can be generalized to different OOD detection tasks, including far, near, and fine-grained OOD detection. Technically, we design (1) LLM prompts based on visual similarity to generate potential outlier class labels specialized for OOD detection, as well as (2) a new score function based on the proportionality between potential outlier and ID class labels to distinguish hard OOD samples effectively. Empirically, our method achieves new state-of-the-art performance across different OOD tasks and can be effectively scaled to the large-scale ImageNet-1K dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the problem of zero-shot OOD detection. Following the previous CLIP-based OOD detection methods (MCM), this paper finds that adding OOD label space with ID classes could boost performance. To this end, the authors propose to leverage LLM to generate prompts to dream about OOD classes. Further, a new scoring function is proposed based on the proportionality between potential outlier and ID class labels. Experiments show the performance gains compared to MCM.

### Strengths
- Using LLMs to generate prompts for OOD classes is interesting and it is based on an empirical study that using OOD classes w/ ID classes will improve the performance. 
- The proposed method is zero-shot, training-free;
- Ablation study on score function; Number of OOD classes has been conducted and explained.

### Weaknesses
Overall, I think the paper is interesting to the community for discussion. Yet, I still have some questions or concerns that want the authors to address in rebuttal.
1. For Figure 1, I get the high-level idea that adding OOD classes with/ ID classes helps the performance boost. Can you add those GT OOD classes w/ ID classes in your Table 1,2,3,4 for the Oracle experiment? It can help better understand the upper bound of your approaches.
2. For the scoring function, I don't see much motivation or justification for this scoring function design. Also, in Figure 6(a), the performance gains from S_DOS to S_MSP are minor. Can you elaborate more on this scoring function design?
- Also, it will be interesting to test your method on other well-known scoring functions such as Max logit score; Energy function; gradients, etc.
3. In table 2, the performance of the Texture dataset is not good. Do you have any insight on the reason?
4. For your generated OOD class prompts, can you conduct some similarity measures between your prompts and GTs? I would like to see how much chance LLMs can hit the GT OOD classes.

### Questions
Please refer to the weakness

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new approach to address the OOD detection problem. The author suggests that having knowledge of the categories of the OD instances can effectively improve the OOD detection performance. Furthermore, the author proposes using LLM to generate the category names for OD instances. Building upon this idea, the author designs a novel OOD detection algorithm. According to the experimental results, the method proposed in this paper demonstrates improved OOD detection performance.

### Strengths
1. The motivation of this paper is very innovative. In the rapidly developing field of LLM, introducing LLM into OOD detection tasks could indeed lead to significant improvements.

2. The author's writing is clear, explaining the starting point, specific methods, and experimental design of this article very clearly.

3. According to the author's experimental results, the proposed method in this article can indeed improve the effectiveness of OOD detection tasks.

### Weaknesses
1. Although it is a good idea to introduce LLM into the OOD detection task, the way it is introduced in this paper is somewhat rigid. The paper primarily utilizes LLM to generate names for OD samples, which are then employed for training purposes. However, there is a lack of effective measures to ensure the reasonability of the OD categories generated by LLM. This critical oversight significantly compromises the overall reliability and trustworthiness of the proposed method.

2. The analysis in this paper is insufficient. Firstly, considering the pivotal role played by LLM in the proposed method, it is crucial to explore the performance of various LLM models, rather than solely relying on a single model such as gpt-3.5. Conducting experiments with different LLM models could potentially yield diverse outcomes and provide a more comprehensive understanding of the approach's effectiveness. By limiting the analysis to just one model, the authors unintentionally overlook the possibility of alternative models delivering superior results.
Secondly, the practical implications of the categories generated by LLM for the ODs are not thoroughly examined. While these generated categories may possess semantic relevance, it is essential to assess the extent of overlap between the generated categories and the actual OD categories. Additionally, an in-depth analysis of the impact of these categories on the final accuracy of the OOD detection system is missing. Understanding the potential discrepancies and evaluating the influence of these categories on the system's overall performance is crucial for gauging the practical applicability and reliability of the proposed method.

### Questions
As shown in the weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents DOS, a method for improving zero-shot OOD detection for CLIP-like models. DOS can be summarized in two parts: firstly the generation of broad OOD labels using an existing LLM, and secondly the detection of OOD samples through a proposed DOS scoring function. Experimental results on a range of ID and OOD datasets show improvements over the baseline MCM and other commonly used OOD detection methods.

### Strengths
1. The paper is clearly written and the zero-shot OOD detection method can be easily, and widely, used in real-world applications of OOD detection.
2. The distinguishment of far, near, and fine-grain OOD label generation presents interesting and unique opportunities for future work.
3. Empirical results show impressive performance, even when compared against fine-tuned methods of OOD detection.

### Weaknesses
1. The reviewer would personally like to see additional experimental evaluations beyond CLIP models, such as ALIGN[1] or FLAVA[2].
2. Additional experiments with other standard OOD detection benchmarks such as CIFAR-10/CIFAR-100 (SVHN, LSUN, DTD, Places365) would give further empirical support for the methodology.


### Questions
The reviewer would like some additional clarification regarding the T-SNE visualization in Section 4.4. In particular, it is unclear from initial viewing why the T-SNE visualization implies improved OOD detection performances, as one can similarly argue how the singlular clustering of OOD representations may lead to better OOD detection.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper uses an LLM to generate potential OOD labels to be used alongside ID labels for score-matching with CLIP.

### Strengths
Simple method, clearly written and easy to understand.

Experiments are comprehensive with many datasets and ID/OOD setups. 

Sufficient ablation study

### Weaknesses
Though the use of LLM to generate OOD labels is distinct from previous work, this alone does not seem like a strong novelty contribution compared to related works

The experimental setting choices are unclear. For example, only the MCM baseline is tested for Zero-shot far OOD with most datasets, but for ImageNet-1K there are many more baselines. Similar problem for near-OOD.These experiments should be more consistent.

There should be more discussion around how each dataset is adapted to be ID-OOD, For example, how similar are iNet-10 and iNet-20 really? It depends on the subsets of classes chosen.

The design of the LLM prompt causes some information leakage, in that a different type of prompt is used for far-, near- and fine-grained OOD settings. This means there is an implicit assumption about what type of anomalies are likely to be seen in a given experiment. A fairer method would not have such assumption about the test data embedded into its LLM prompts.

### Questions
Why use FPR95 instead of AUPR?

In Figure 7, why are far-ood and fine-grained-ood tested with 100s of outlier class labels but near-ood only with a maximum of 10?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
