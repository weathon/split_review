# Intrinsic Explanation of Random Subspace Method for Enhanced Security Applications

- Decision: Reject
- Scores: 3, 6, 3, 6

## Abstract
Random subspace method has wide security applications such as providing certified defenses against adversarial and backdoor attacks, and building robustly aligned LLM against jailbreaking attacks. However, the explanation of random subspace method lacks sufficient exploration. Existing state-of-the-art feature attribution methods such as Shapley value and LIME are computationally impractical and lacks security guarantee when applied to random subspace method. In this work, we propose EnsembleSHAP, an intrinsically faithful and secure feature attribution for random subspace method that reuses its computational byproducts. Specifically, our feature attribution method is 1) computationally efficient, 2) maintains essential properties of effective feature attribution (such as local accuracy), and 3) offers guaranteed protection against attacks on feature attribution methods. We perform comprehensive evaluations for our explanation's effectiveness when faced with different empirical attacks. Our experimental results demonstrates that our explanation not only faithfully reports the most important features, but also certifiably detects the harmful features embedded in the input sample.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes EnsembleSHAP, a feature attribution method based on the well-known random subspace method, which is claimed to be computationally efficient and preserves fundamental properties of Shapley values. The method provides certifiable robustness against explanation-preserving attacks to language models, as theoretically shown.

### Strengths
- Relevant topic;
- Theoretical analysis;
- Rich model and attack types considered in the experiments.

### Weaknesses
 - Unclear presentation;
- No empirical evaluation of the computational complexity;
- Lack of comparison with other efficient feature attribution methods;
- The proposed algorithm is not formally stated but only described verbally.

**Comments.**

**Unclear presentation.** Presentation needs substantial improvement. One unclear point to me is that the random subspace method proposed by T. K. Ho does not work in the way it is used in this paper, as far as my understanding of this work is concerned. The random subspace method creates distinct training sets by bagging and subsampling the feature set in each round, and it's the basic method used to train random forests. I don't see how it is directly applied in this work (at least, it's unclear how it's applied at training vs test time). It was originally proposed to boost the performance of classifier ensembles, and it had nothing to do with security issues. This should also be clarified in the paper, I guess that it's only the recent developments that used that method to get certified robustness via randomization (a la randomized smoothing).

**Lack of empirical computational complexity analysis.** The authors did not provide any evaluation of the computational complexity required for computing the importance scores with the proposed method, nor they provided information on what algorithm they used for estimating the standard Shapley values. I don't buy that this method is computationally efficient, if it requires sampling as many as 10,000 different inputs before providing a prediction.

**No comparison with other efficient Shapley values estimation techniques.** Other efficient methods have been previously proposed for efficient Shapley values estimation; despite this, the authors did not provide a comparison with other methods, e.g., FastSHAP [1].

**Formal algorithm is missing.** In Sect. 4, there is no actual definition of the algorithm. Instead, a description of the used methods is given in words, such as “Monte Carlo” sampling or the approximation of the defined importance score. The approach to solving the presented optimization problem has not been reported.

**No further discussion of the certified detection rate results.** In Sect. 6.3 the plot of the certified detection rate against the top-e important features is reported. However, there is no discussion on the obtained results; there is no discussion on the total number of considered features, why the detection reaches a plateau after few “e”. This require further elaboration.
Moreover, the experiments on jailbreaking, the motivation behind the choice of the hyperparameters, and other relevant experiments are confined in the appendix. The authors should reconsider that to make the paper more self-contained.

### Questions
1. Why did the authors not provide a comparison with other efficient methods for Shapley values estimation, like FastSHAP [1]? Is it because they are still inefficient when applied to random subspace methods?

2. What approach is used for solving the optimization problem stated in Sect. 5.4?

3. What is the rationale behind selecting the ICL [2] method as a baseline? How did the authors adapt it to work as a feature attribution method?


[2] Nicholas Kroeger, Dan Ley, Satyapriya Krishna, Chirag Agarwal, and Himabindu Lakkaraju. Are large language models post hoc explainers? arXiv preprint arXiv:2310.05797, 2023

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents EnsembleSHAP, a novel feature attribution method tailored for the random subspace method. EnsembleSHAP addresses limitations in traditional feature attribution approaches, such as Shapley values and LIME, which are computationally intensive and lack security assurances against explanation-preserving attacks. EnsembleSHAP leverages computational byproducts of the random subspace method to provide efficient, accurate, and secure explanations for model predictions. This method is specifically designed to improve resilience against adversarial and backdoor attacks, as well as jailbreaking attacks on large language models. Experimental results show that EnsembleSHAP outperforms baseline attribution methods in identifying harmful features under various security threats, including certified defense and jailbreaking scenarios. The theoretical analysis demonstrates that EnsembleSHAP maintains key properties of effective feature attribution, such as local accuracy and robustness against attacks.

### Strengths
1. The paper is structured logically, moving from the problem context and related work to problem formulation, method design, theoretical analysis, and empirical validation.

2. The authors provide a theoretical basis for EnsembleSHAP.

3. EnsembleSHAP leverages the computational byproducts of random subspace methods, resulting in lower computational overhead compared to traditional methods.

4. The paper considers multiple threats - adversarial attack, backdoor attack, and jailbreaking.

### Weaknesses
1. EnsembleSHAP is designed specifically for random subspace methods, which could limit its generalizability to other ensemble methods or broader feature attribution applications that do not involve subsampling.

2. The efficiency claim is not well studied in the experimental section.

3. The certified detection theorem and detection strategy are not clearly explained, making it difficult for readers to fully understand the approach and its guarantees.

4. The method’s assumptions about limited modifications to input features may not hold for many real-world backdoor attacks, where an attacker might poison the entire input space or apply more complex poisoning strategies. This assumption restricts the generalizability of the certified detection method for a wider range of attacks.

5. The paper evaluates EnsembleSHAP using TextFooler for adversarial attacks and BadNets for backdoor attacks.These attacks are somewhat dated, and there are newer, more sophisticated adversarial and backdoor attacks in current literature. Testing against more recent attacks could better demonstrate the robustness of EnsembleSHAP. In fact, one can even design an adaptive attack.

### Questions
My major questions are included in the above weaknesses comments.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces EnsembleSHAP, a novel feature attribution method designed for random subspace methods. Compared with existing feature attribution techniques like Shapley values or LIME, the proposed EnsembleSHAP is both computationally efficient and intrinsically secure. Moreover, it provides a certified defense against various attacks.

### Strengths
1.	The proposed EnsembleSHAP addresses the security gap in existing feature attribution methods, offering certified defenses.
2.	The authors carry out empirical evaluations to assess the effectiveness of their explanations across various security applications of the feature attribution method.

### Weaknesses
 1. In section 4,  the importance scores for each feature within a given feature group are equal. This approach is overly simplistic and fails to reasonably capture the differences in importance among the various features. Specifically, if a feature group contains both highly influential and less influential features, the method will assign them the same importance score, thus losing the granularity of feature importance.
 2. In section 4, the author highlights an issue where variations in appearance frequency can lead to an unfair assessment of feature importance when the sample size N is small. However, there is no mathematical analysis of Eq. (9) to demonstrate how the designed importance score addresses this issue. The paper lacks a theoretical justification for how the normalization mitigates the bias introduced by uneven sampling frequencies, and it is unclear under what conditions this normalization is effective.
 3. In section 5.1, why not limit k < |S| instead of considering the special case that |S| < k. This special case introduces unnecessary complexity and deviates from the standard practice of subset selection where the size of the selected subset is typically smaller than the size of the original set. The rationale for including this case is not sufficiently justified.
 4. The importance score is calculated based on the frequency with which a feature is selected and the predicted label, meaning that two features that are occasionally selected together end up with the same importance score. In contrast, Shapley value calculations based on label probability would differentiate between these features. Consequently, the proposed ENSEMBLESHAP, which relies on this importance score, assigns identical values to these features, potentially overlooking the differences in their individual influences. This is a significant limitation as it fails to capture the interaction effects between features.
 5. The authors claim that the proposed method is computationally efficient. However, there is a lack of analysis regarding its complexity and the associated time costs. The paper does not provide a formal analysis of the computational complexity of the proposed method, making it difficult to assess its efficiency compared to other feature attribution techniques. A comparison of the time complexity with methods like Shapley values or LIME would be beneficial.

### Questions
Please help to check the weaknesses part.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work reveals two major issues with current state-of-the-art feature attribution methods: (1) high computational costs and (2) a lack of security guarantees against explanation-preserving attacks. To address these issues, this study proposes a computationally efficient and inherently secure feature attribution method. The key insight derives from the fact that an ensemble model’s output aggregates the prediction results of all sub-sampled inputs, with each sub-sampled input’s influence on the ensemble output further distributable to the individual features within that input. Thus, the contribution of each feature can be inferred from analyzing the prediction results of all sub-sampled inputs containing that feature.

### Strengths
A security guarantee is proposed for the explanation-preserving attack without increasing the high computational cost.

### Weaknesses
Adaptive attack discussion: Discussion and experiments on adaptive attacks could further strengthen the paper. If attackers know the defense strategy, what happens? For instance, they could adjust the attack target so that triggers do not fall within the top 10% or 20% of important features but rather within the top 30% or 40% to circumvent defenses.

1. The two works compared by the authors are not defense-oriented, so is this comparison fair? Should comparisons also include existing defenses against backdoor and adversarial attacks for large language models (LLMs) to better evaluate the proposed method’s effectiveness?
2. Without prior knowledge, if the proposed method is used to defend and 10% or 20% of the important words are deleted, can the LLM still make accurate responses? The experimental results do not indicate whether the defense proposed in this paper affects the model's responses to normal text.
3. Regarding the faithfulness comparison in Table 1: Faithfulness is defined as the percentage of label flips when the top e features with the highest importance scores are deleted. My understanding is that this metric should be as high as possible under attack, as the deleted important features likely contain adversarial elements. In the absence of an attack, if deleting these features leads to a high label flip rate, it indicates that removing important features significantly impacts model performance. How should one decide whether or not to delete these features?
4. It is recommended that the authors add a discussion on adaptive attacks to enhance the practical value of the proposed method.

### Questions
1. The two works compared by the authors are not defense-oriented, so is this comparison fair? Should comparisons also include existing defenses against backdoor and adversarial attacks for large language models (LLMs) to better evaluate the proposed method’s effectiveness?
2. Without prior knowledge, if the proposed method is used to defend and 10% or 20% of the important words are deleted, can the LLM still make accurate responses? The experimental results do not indicate whether the defense proposed in this paper affects the model's responses to normal text.
3. Regarding the faithfulness comparison in Table 1: Faithfulness is defined as the percentage of label flips when the top e features with the highest importance scores are deleted. My understanding is that this metric should be as high as possible under attack, as the deleted important features likely contain adversarial elements. In the absence of an attack, if deleting these features leads to a high label flip rate, it indicates that removing important features significantly impacts model performance. How should one decide whether or not to delete these features?
4. It is recommended that the authors add a discussion on adaptive attacks to enhance the practical value of the proposed method.

### Soundness
3

### Presentation
3

### Contribution
3
