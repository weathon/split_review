# Crafting Zero-Cost Proxy Metrics for Neural Architecture Search via Symbolic Regression

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
Using zero-cost (ZC) metrics to estimate network performance instead of relying on expensive training processes has proven both its efficiency and efficacy in Neural Architecture Search (NAS). However, a significant limitation of most ZC proxies is their inconsistency, as reflected by the substantial variation in their performance across different problems. Additionally, the design of current ZC metrics is manual, which is a lengthy trial-and-error process and requires expert knowledge to develop ZC metrics effectively. These challenges raise two questions: (1) Can we automate the design of ZC metrics? and (2) Can we utilize the existing hand-crafted ZC metrics to synthesize a better one? In this study, we propose a framework based on Symbolic Regression to automate the design of ZC metrics. Our framework is not only highly extensible but also capable of quickly producing a ZC metric with a strong positive rank correlation to network performance across multiple problems within just a few minutes. Extensive experiments on 13 problems in NAS-Bench-Suite-Zero, covering various search spaces and tasks, demonstrate the superiority of our automatically designed proxies over hand-crafted ones. By integrating our proxy metrics into an evolutionary algorithm, we could identify a network architecture with comparable performance on the CIFAR-10 dataset within 15 minutes using a single GeForce RTX 3090 GPU.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors proposed a framework based on Symbolic Regression to automate the design of ZC metrics, whch is not only highly extensible but also capable of quickly producing a ZC metric with a strong positive rank correlation to network performance across multiple problems within just a few minutes.

### Strengths
1.The approach of using symbolic regression to combine hand-crafted metrics into a superior proxy metric is innovative, setting it apart from previous methods, such as those requiring manual crafting of each metric.

2.The study have comprehensive experiments on multiple NAS benchmarks and comparisons with state-of-the-art ZC metrics.

3. The paper is generally well-structured and clear, with a logical flow from problem statement to methodology, experiments, and conclusions.

4. The proposed approach can evaluate network architectures quickly and accurately without intensive computational resources.

### Weaknesses
1. The innovation of the paper is limited, the framework is a common symbolic regression to search the best mathematical expressions of ZC metrics.

2. The paper focuses on the performance of the designed ZC metrics but does not provide insights into why certain combinations of metrics work better than others.

3. While the paper claims generalizability across various NAS problems, the evaluation is primarily based on a limited set of benchmarks.

### Questions
1. the Eq.1 is essentially a normalization, It also looks like giving each question the same weight.

2. Why specific metrics (e.g., FLOPs, Snip, ZiCo, etc.) that frequently appear in high-performing combinations? Are there theoretical or empirical reasons?

3. What is the multiple problems in dataset? Are they different tasks?

4. There seems to be a typo in the annotation of Figure 2. NWOT should be MeCo.

5. In Figure 4, what do SS^i and T^j in the data set represent?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a higher-level zero-cost metric for neural architecture search based on symbolic regression of hand-designed zero-cost metrics. The proposed framework is extensible, consistent, and achieves a high positive rank correlation across multiple problems. Results are reported on NAS-Bench-101/201/301 and TransNAS-Bench-101-Micro/Macro as well as NAS on CIFAR-10 demonstrating competitive rank correlation.

### Strengths
+ The use of rank correlation across multiple ZC metrics and problems is interesting and addresses some of the common criticism of ZC metrics.

### Weaknesses
 - Limited Novelty. Most contributions, e.g., the use of symbolic regression or the use of high-level ZC metrics, were proposed in earlier work. Their combination is somewhat novel but in light of the following points may not be sufficient.
- The claim "Our framework can synthesize a new ZC metric within only 10 minutes" is incorrect because the framework requires the calculation of the high-level ZC metrics which serve as input features, and therefore, the actual total time is the time required by each high-level ZC metric plus 10 mins. The same comment applies to the results in Table 4.
- The proposed ZC metric, while using existing ZC metrics, doesn't outright outperform these metrics (see Fig. 6), and in NAS, is outperformed by a number of existing NAS methods based on ZC metrics (see Table 4)
- No ImageNet results reported.

### Questions
- Why was symbolic regression chosen?
- Why was the proposed ZC metric (SR-NAS) not evaluated on ImageNet?
- If the proposed ZC on average ranks better than existing ZC metrics, why does it not outperform these metrics in NAS?

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
This work proposes an extensible framework for the automatic discovery of ZC metrics, where SR is used to guide the production of new metrics.

### Strengths
The author clearly expresses the proposed method and demonstrates the advantages of the proposed method through numerous experiments.
It makes sense that many new ZC methods (e.g., ZiCo and MeCo) are integrated into the SR model.

### Weaknesses
I think testing on Imagenet using the DARTS search space is necessary.
The proposed method is not advantageous compared to AZ-NAS.

### Questions
Regarding the automatic design of ZC agents, some works have been left out [r1-r3].
[r1] Robustifying and Boosting Training-Free Neural Architecture Search
[r2] AZ-NAS: Assembling Zero-Cost Proxies for Network Architecture Search
[r3] Dynamic ensemble of low-fidelity experts: Mitigating nas “cold-start”.

### Soundness
2

### Presentation
3

### Contribution
2
