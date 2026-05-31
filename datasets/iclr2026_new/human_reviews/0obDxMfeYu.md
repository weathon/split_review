## Human Reviewer 1

### Summary
This paper introduces Medix, a method for Out-of-Distribution (OOD) detection that utilizes unlabeled "in-the-wild" data. Its core contribution is a two-stage process: (1) filtering potential OOD samples from the unlabeled data by identifying points whose gradient's element-wise median deviates significantly from the In-Distribution (InD) mean gradient, and (2) training a binary OOD detector using the identified outliers and labeled InD data. The authors support their method with theoretical error bounds and extensive empirical evaluations against numerous baselines.

### Strengths
1. A solid theoretical foundation is provided, with proven bounds on both inlier and outlier misclassification rates for the median-based filtering stage. This analysis offers valuable insight into the method's robustness, particularly under the Huber contamination model.
2. The paper includes valuable investigations into hyperparameter sensitivity, pseudo-label quality, and computational efficiency, which bolster the credibility and practical understanding of the proposed approach.

### Weaknesses
1. The most significant weakness is the insufficient discussion and comparison with the most relevant prior work. The core mechanism of using gradients from an InD model to identify OOD samples in unlabeled data is the central contribution of Du et al. ("How Does Unlabeled Data Provably Help Out-of-Distribution Detection?"). While Medix employs a median-based objective instead of a mean-based one, the paper fails to compellingly argue why this constitutes a fundamental advance rather than an incremental variation. The absence of a direct, quantitative comparison with this key work (and its subsequent developments) makes it impossible to assess the true marginal contribution of the median-centric approach.
2. The empirical comparisons, while broad, overlook several recent and highly relevant state-of-the-art methods (e.g., [a,b]). This omission weakens the claim of superior performance, as it remains unclear how Medix fares against its most direct competitors.
3. The iterative, greedy filtering algorithm (Algorithm 1) is computationally intensive. Although profiling results are provided, the cost may be prohibitive for very large-scale datasets or applications requiring frequent model updates, which is a common scenario in real-world deployments.
4. The theoretical guarantees rely on assumptions such as i.i.d. samples and sub-Gaussian gradient coordinates. The practical validity of these assumptions, especially for modern deep networks and complex data distributions, is not thoroughly justified and could limit the real-world applicability of the bounds.

References:  
[a] Du et al. How does unlabeled data provably help out-of-distribution detection?. ICLR'2024.  
[b] Geng et al. LoD: Loss-difference OOD Detection by Intentionally Label-Noisifying Unlabeled Wild Data. IJCAI'2025.

### Questions
1. The mechanism of using InD model gradients to extract OOD candidates from unlabeled data is highly similar to the approach in Du et al. Could you explicitly clarify the fundamental conceptual difference between Medix and this line of work? Please provide a quantitative comparison on common benchmarks to demonstrate the advantage of using the median over other filtering criteria proposed in prior art.
2. How does the theoretical analysis, particularly the error bounds, differ from or improve upon the theoretical framework already established in Du et al.? Is the primary theoretical contribution the adaptation of the analysis to the median operator, or are there new foundational insights?
3. Why were the most directly comparable methods, specifically Du et al. and its subsequent developments, not included in the empirical comparison? Can you run these comparisons and report the results?
4. Under what conditions would the median-based filtering be expected to perform poorly? For instance, how sensitive is the method to the quality of the initial InD model or scenarios where the OOD samples do not induce a significant shift in the gradient median?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper investigates how to enhance the OOD detection performance of a type of method which utilizes unlabeled wild data to train the model to distinguish between ID and OOD data. It proposes Medix, a median-based approach that filters outliers from the unlabeled wild data and then trains an OOD detector on the identified outliers and the ID samples. The authors provide theoretical guarantees for the robustness of median-based filtering and conduct experiments on CIFAR OOD benchmarks to verify its effectiveness.

### Strengths
1. The topic of utilizing unlabeled wild data for OOD detection is interesting.
2. This paper provides a theoretical analysis of the proposed method.

### Weaknesses
1. **This paper should provide a more detailed discussion on a very important related work, SAL [1], which has only been briefly mentioned in the Related Work Section.** Both SAL and Medix share the same overall “Separate and Learn" framework, which first identifies OOD data from unlabeled wild data and then regularizes the model with them, and also leverages a similar reference gradient technique. If the reviewer understands correctly, the difference between SAL and Medix only lies in the procedures to use gradient information to identify candidate OOD data from the wild data. SAL can also be applied in the setting of dataset-level mixing. Therefore, the authors should **provide an in-depth discussion on the advantages of Medix over SAL, reinforced with additional experiment results or theoretical analysis.** 

2. **This paper omits a direct experimental comparison between SAL and Medix.** In fact, the reported results in the SAL paper indicate that SAL achieves nearly zero FPR95 on both CIFAR-10 and CIFAR-100 OOD benchmarks. But this paper claims that there are substantial opportunities for further advancement on utilizing unlabeled wild data. Therefore, the reviewer suggests that the authors **include a direct comparison with SAL and extend experiments on more challenging OOD benchmarks**, such as ImageNet-1k OOD benchmarks.

3. The reviewer suggests that the authors present a detailed mathematical formulation of the element-wise median (EWM) used in the proposed algorithm, which will make it easier for readers to understand the implementation details.

4. The process of filtering potential outliers from unlabeled wild data incurs non-negligible computational overhead, since it involves calculating the gradient of the loss function with respect to model parameters for every sample in the wild data. The reviewer suggests that the authors provide an experiment to quantitatively evaluate the actual time cost of filtering OOD data from unlabeled wild data with Medix and compare it with the time cost to train the OOD detector.

[1]. Xuefeng Du, et al. How Does Unlabeled Data Provably Help Out-of-Distribution Detection?

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
The work proposed to use median to address wild OOD detection. Median can used against noise and outliers for achieving robustness. The paper also provides error bounds to prove the effectiveness of proposed method.

### Strengths
A trivial method to address wild OOD with a strong theory.

### Weaknesses
I have not too many issues. I just want to ask why your bound has the Contamination term. It is possible to withdraw this term? In Du's work, there is not such constant. So it seems your bound is loss. Please address this issue, I will raise my score.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
5

---

## Human Reviewer 4

### Summary
The paper proposes ​​Medix​​, a median-based framework to identify OOD samples from unlabeled wild data and train robust OOD detectors. Theoretical analysis is provided along with the method to demonstrate the benifits of Medix.

### Strengths
Theoretical analysis are provided along with Medix. The authors derived an error bounds for understanding the proposed method under sub-Gaussian assumptions.

### Weaknesses
1. There is no comparison on challenging near-OOD scenarios and large-scale datasets (e.g., ImageNet), raising the concerns of the scalability of the proposed method.
2. ​​Limited novelty differentiation​​. Medix’s core design choice, i.e., (median filtering for OOD detector training) is closely related to​​OpenMatch​​[1] and ​​SAL​​[, with insufficient distinction in motivation and mechanics. The reviewer generally feel the novelty of the proposed method does not meet the bar of NeurIPS. More comprehensive comparison may be necessary.
3. ​​Inadequate evaluation​​. Strong baselines​​ are missing. Initial comparisons used outdated methods (e.g., KNN+ 2022). Some recent SOTA (e.g., CIDER[3], POEM[4]) are missing.

[1] OpenMatch: Open-set Consistency Regularization for Semi-supervised Learning with Outliers

[2] How Does Unlabeled Data Provably Help Out-of-Distribution Detection?

[3] How to Exploit Hyperspherical Embeddings for Out-of-Distribution Detection?

[4] POEM: Out-of-Distribution Detection with Posterior Sampling

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 5

### Summary
The paper proposed Medix, which leverages the unlabled wild data to build OOD detector. Medix first utilizes the graidents from the ERM loss and an element-wise median (EWM) to extract candidate outliers from the wild unlabeled data, adopting the greedy leave-one-out strategy. The OOD detector is then trained on the ID data and the extacted data. Theoretical bounds are provided to gaurantee low error rate for outlier selection.

### Strengths
1. Principled method for filtering outliers: The authors propose Medix which can cleanly extract outliers from wild dataset, being well theoretically grounded on misclassification rate, separating contamination.
2. This paper provides a new perspective for OOD detection in a more realistic scenario, additional but unlabeled data is provided during training and deployment.
3. The proposed Medix achieves strong performance across various OOD datasets.

### Weaknesses
1. Computational concern. While the gradients can be efficient for extracting outliers, it may introduce unaffordable computational cost. Time and Space complexity analysis will further justify the effect of Medix. The gradient quality may also influence the extraction, which is closely related to the amount of ID data used.
2. Modest improvement. The baselines can already achieve great performance (e.g., WOODS on CIFAR10 vs. SVHN and LSUN-C), indicating that the improvement of Medix may be dataset-based and may shrink in some other domains(harder cases).
3. Concern of greedy selection algorithm: while the leave-one-out strategy is intuitive and straightforward and the theoretical bounds are provided, there still be failure modes where ID data is wrongly removed.

### Questions
See weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3