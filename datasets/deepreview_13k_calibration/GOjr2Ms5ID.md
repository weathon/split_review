# Cascaded Learned Bloom filter for Optimal Model-Filter Size Balance and Fast Rejection

- Decision: Reject
- Avg Score: 3.25
- Scores: 3, 6, 3, 1

## Abstract
Recent studies have demonstrated that learned Bloom filters, which combine machine learning with the classical Bloom filter, can achieve superior memory efficiency. However, existing learned Bloom filters face two critical unresolved challenges: the balance between the machine learning model size and the Bloom filter size is not optimal, and the reject time cannot be minimized effectively. We propose the Cascaded Learned Bloom Filter (CLBF) to address these issues. Our optimization approach based on dynamic programming automatically selects configurations that achieve an optimal balance between the model and filter sizes while minimizing reject time. Experiments with real-world datasets show that CLBF reduces memory usage by up to 24% and decreases reject time by up to 14 times compared to the state-of-the-art learned Bloom filter.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes Cascaded Learned Bloom Filter (CLBF) to address the balance between the machine learning model size of learned Bloom filters and the Bloom filter size of classical Bloom filters.  The authors formulate an optimization approach based on dynamic programming to select configurations, with the reject time also part of the optimization objective. . Experiments using two benchmark datasets show that CLBF reduces memory usage by up to 24% and decreases reject time by up to 14 times compared to the state-of-the-art learned Bloom filter.

### Strengths
A cascading (learned) Bloom filter (LBF)  architecture that combines both sandwiched LBFs and partitioned LBFs (PLBFs), with classical BFs (as branch BFs).

### Weaknesses
 The paper claims that the "optimization approach based on dynamic programming automatically selects configurations
that achieve an optimal balance between the model and filter sizes while minimizing reject time."  This claim is not substantiated at all.
You aim to optimize eq.(4), which seems to make sense, but which is largely meaningless.  First of all, unlike the classical BF where one can derive a low bound on the relation between false positive rate and filter size, what is the relation between the false positive rate of a LBF, $f^{(t})_i$ and the model size?    Second, given the cascading architecture, $\prod f^{(t})_i$ is not the overall false positive rate of the entire CLBF.  Most of section 3.3 makes little sense to me.

### Questions
See the weakness above.

1.  What is the relation between the false positive rate of a LBF, $f^{(t})_i$ and the model size?  Without an explicit expression, how do you optimize eq.(4) using dynamic programing?  

2. Please justify that  $\prod f^{(t})_i$  yields the overall false positive rate of the entire CLBF. 

3. In Section 3.3, You never establish the optimality of your dynamic programming formulation. Please formally establish the optimality of your solution.

4. How does the "depth" of your cascade, i.e., d, affect the overall balance between the model and filter sizes

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
4

### Summary
This article introduces a Cascaded Learned Bloom Filter (CLBF). CLBF combines the advantages of machine learning and traditional Bloom filters, aiming to address two critical issues in existing Learned Bloom Filters (LBF): the optimal balance between the size of the machine learning model and the Bloom filter, and the effective minimization of rejection time. CLBF employs a cascade structure with multiple machine learning models and multiple Bloom filters arranged alternately. The goal is to minimize memory usage and rejection time under the constraint that the false positive rate does not exceed F. CLBF uses dynamic programming optimization methods to automatically select configurations, achieving an optimal balance between model and filter sizes, and minimizing rejection time. Experiments show that CLBF reduces memory usage by 24% and rejection time by 14 times compared to the state-of-the-art Learned Bloom Filter (PLBF).

### Strengths
1. The article proposes a novel structure of CLBF that optimizes memory usage and query performance by cascading multiple machine learning models and Bloom filters. It utilizes dynamic programming to automatically select the optimal configuration, reducing the manual parameter tuning effort and potentially finding better solutions.
2. By adjusting hyperparameters, CLBF can trade off between memory efficiency and rejection time to adapt to different application scenarios. The article conducts extensive experiments with real-world datasets, validating the effectiveness of CLBF.
3. The paper provides a clear description of the CLBF's implementation, accompanied by a thorough theoretical analysis.

### Weaknesses
1. The article primarily focuses on the application of a single machine learning model, XGBoost, which limits the exploration of how different models might contribute to the performance of CLBF. A comparison with a variety of machine learning models, such as Support Vector Machines, Random Forests, or even simpler models like logistic regression, could provide a more comprehensive understanding of CLBF's versatility and robustness across different algorithmic approaches. This is particularly important because the optimal model choice may depend on the underlying data distribution and the desired trade-off between model complexity and performance.
2. While the article effectively demonstrates the benefits of CLBF, it would be beneficial to explore whether fine-tuning the hyperparameters of the machine learning model, such as the learning rate, regularization parameters, or tree depth in the case of XGBoost, or alternative constructions of cascaded Bloom filters, such as varying the number of hash functions or the size of the bit arrays at each level, could yield similar or superior optimization results. This discussion could offer additional insights into the factors that contribute to the overall performance of CLBF and whether the gains are primarily due to the cascaded structure or other optimization strategies.

### Questions
1. Is it possible that, instead of employing a cascaded structure, optimizing the hyperparameters of the machine learning model within a Learned Bloom Filter could also achieve similar performance enhancements? 

2. It raises an interesting question whether embedding a multi-layer deep learning model within the initial machine learning framework could further enhance optimization. Could such a multi-layer structure, potentially through algorithms like Bayesian Optimization, or Adam, autonomously identify optimal network parameters to achieve enhanced model optimization?

3. Is it possible to use a combination of a machine learning model with hierarchical Bloom filters for optimization? For example, using one Bloom filter to filter out most elements, and then using a second, more precise Bloom filter for final verification.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents the Cascaded Learned Bloom Filter (CLBF), a learned Bloom filter design aiming to optimize the balance between memory usage and reject time. The CLBF achieves these goals using dynamic programming and by designing a cascaded structure combining machine learning models and Bloom filters. Experimental evaluations on real-world datasets demonstrate CLBF’s improvements in reject time and memory efficiency compared to previous state-of-the-art methods.

### Strengths
1- The paper effectively summarizes and describes prior research on learned Bloom filters, providing a clear understanding of existing work and where CLBF differs. For example, CLBF introduces a unique combination of sandwiched BF and PLBF structures in a cascade, allowing a flexible balance between model and filter sizes and distinguishing it from prior approaches.

2- The experiments cover multiple datasets and baselines, which provides a well-rounded analysis of CLBF's effectiveness and limitations across diverse configurations.

### Weaknesses
1- The paper’s primary contribution seems minimal, as it largely combines established techniques from sandwiched Bloom filters and PLBF within a cascade structure. This approach suggests an incremental rather than a groundbreaking contribution.

2- The emphasis on optimizing reject time raises applicability concerns. There is a lack of discussion about real-world applications where reduced reject time is crucial, as well as cases where it might be less relevant. More critically, the cascade structure may increase query time for elements in the set, impacting overall efficiency. A fair comparison would benefit from including average query time metrics across different query types.

3- The dynamic programming approach, while effective, is computationally intensive. Any change in parameters would require re-optimization, and even without changes, the initial construction time is high (as illustrated in Figure 6). This may limit the scalability and practicality of CLBF in time-sensitive applications.

### Questions
1- Could the design be made general for any learning-augmented application, extending beyond Bloom filters?

2- What are real-world applications where reduced reject time is prioritized over faster query times for present keys? How could the cascade depth be controlled based on the target query time for these applications?

3- Given the variety of ML models with diverse performance profiles (e.g., different sizes or query times), how adaptable is the proposed design? Would the structure or configuration require major adjustments for different ML model types?

Minor typos:

(1) line 266 includes extra "

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
In this paper the authors present a new method for the set membership query that combines Bloom filters with machine learning models. Unlike the earlier definitions of learned Bloom filters (LBF) that typically combine a single learned model with a few Bloom filters, this paper uses an alternating sequence of learned models and Bloom filters to answer a query. The stated goals that the authors seek to achieve are the reduction of the memory footprint of the LBF and also reduction of the time to rejection of a negative query.

### Strengths
S1. The key strength of the paper is that the ML models are assumed to be weak learners. Since the use case of Bloom filters is generally in distributed databases and filesystems, often there are no strong patterns in the keys and so it is difficult to expect high accuracy (this conclusion is based on some work that has been done in my own group over the years). This comment highlights the significance of this work under review.

### Weaknesses
W1. Perhaps the most important weakness here is that the introduction of a multi-layered structure with great coding complexity and many learning models adds so much complexity to the structure that there is little to no chance that such a proposal will ever find its way into an actual file system. A quick look at Fig 1 and Fig 2 that have been placed side by side will show why.

W2. The tremendous increase in complexity of the solution is reflected in the construction time jump (see Fig 6). The authors need to ask themselves if such a massive increase over simple Bloom filters is justifiable. In the aftermath of Kraska's paper we seem to have forgotten that Bloom's idea was a lightweight and quick data structure to speed up set membership. In distributed filesystems there is a need to periodically rebuild all the set membership structures, once too many writes have been logged. I don't think the kind of construction times being shown here are acceptable.

W3. Important baselines are missing. The authors have not compared with the following methods that are competitors to Vaidya's PLBF:
- Zhenwei Dai and Anshumali Shrivastava. Adaptive Learned Bloom Filter
(Ada-BF): Efficient Utilization of the Classifier with Application to Real-Time
Information Filtering on the Web, NeurIPS 2020
- Arindam Bhattacharya, Chathur Gudesa, Amitabha Bagchi, Srikanta Bedathur.
New wine in an old bottle: Data-aware Hash Functions for Bloom Filters, VLDB 2022.

Both these papers measure memory used. While it can be argued that Vaidya et. al. have compared against Ada-BF already and beaten it on memory (but not comprehensively), the latter paper shows improved memory utilization over both Vaidya and Ada-BF. So there is no reason why it should not have been used as a baseline. The authors have cited the first paper but not the second.

W4. Memory-learning tradeoff not explored adequately. The authors mention that there has to be a tradeoff between memory and learning in terms of model size, but there is no experiment that investigates this tradeoff.

W5. Mathematica quantities not properly defined. For example, is Reject Time defined in terms of clock time?

### Questions
Q1. How would your method perform in a dynamic case where the set membership structures need to be reconstructed periodically?

Q2. How did you decide how much memory it to be assigned to Bloom filters and how much is to be kept for ML models?

### Soundness
3

### Presentation
1

### Contribution
1
