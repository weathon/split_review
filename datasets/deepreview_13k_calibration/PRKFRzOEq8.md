# Estimating the conformal prediction threshold from noisy labels

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 3, 5, 8, 6

## Abstract
Conformal Prediction (CP) is a method to control prediction uncertainty by producing a small prediction set,   ensuring a predetermined probability that the true class lies within this set.   This is commonly done by defining a score, based on the model predictions, and setting a threshold on this score using a validation set. In this study, we address the problem of CP calibration when we only have access to a validation set with noisy labels. We show how we can estimate the noise-free conformal threshold based on the noisy labeled data.   Our solution is flexible and can accommodate various modeling assumptions regarding the label contamination process, without needing any information about the underlying data distribution or the internal mechanisms of the machine learning classifier.    We develop a coverage guarantee for uniform noise that is effective even in tasks with a large number of classes. We dub our approach Noise-Aware Conformal Prediction (NACP) and show on several natural and medical image classification datasets, including ImageNet, that it significantly outperforms current noisy label methods and achieves results comparable to those obtained with a clean validation set.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new conformal prediction framework for classification that is able to handle label noise. Specifically, given known uniform label noise, the authors present an algorithm that can achieve the desired coverage for the underlying unobserved clean data. They also extend their approach to handle general noise using a known noise matrix. Through various experiments, they demonstrate that their approach outperforms existing methods for managing label noise in CP.

### Strengths
The paper is well-structured and easy to follow and understand, addressing the intriguing problem of conformal prediction sets in the presence of noisy data.

### Weaknesses
1. My primary concern relates to the noise assumption. Firstly, it's unclear how realistic the assumption of uniform label noise is in practical applications. Additionally, assuming that the noise parameter is known or can be accurately estimated in real-world scenarios doesn't seem entirely realistic (for both uniform and general noise). The uniform noise assumption, while mathematically convenient, rarely manifests in real-world datasets where label noise is often class-dependent or instance-specific. Furthermore, the method's reliance on a known noise matrix is a significant limitation, as accurately estimating this matrix, especially for high-dimensional data, is a challenging problem in itself, potentially introducing further inaccuracies. The paper does not discuss the sensitivity of the method to errors in the estimated noise matrix, which is a critical aspect for practical applicability.

2. In the experiments, different values of the noise parameter weren't tested to show how the model performs under varying noise levels (e.g., extending beyond $\epsilon > 0.2$). This limits the understanding of the method's robustness and its performance across a spectrum of noise conditions. Specifically, it is important to assess how the method behaves under low noise conditions (e.g., $\epsilon < 0.1$) and under extreme noise scenarios (e.g., $\epsilon > 0.5$) to fully characterize its applicability. The choice of $\epsilon = 0.2$ seems somewhat arbitrary without a clear justification for why this particular noise level is representative of real-world scenarios.

3. For the results of the general noise model presented in Table 5, it would be fairer—particularly for the NR-CP approach—to include NACP with $\Delta$ as well, as these two methods are specifically aimed at recovering finite-sample coverage guarantees under noise. The comparison as it stands does not provide a complete picture of the relative performance of methods designed to handle noisy labels. By omitting the finite-sample correction term for NACP, the comparison is biased against NACP, as this term is specifically designed to address the challenges of finite sample sizes. A more comprehensive comparison would include both versions of NACP to provide a clearer understanding of the trade-offs between the different approaches.

### Questions
1. Does the grid search for finding q in [q_1, q_2] yield a unique result? If yes, why? If not, what might this imply?


2. According to the experimental results, it appears that NACP without $\Delta$ performs best—achieving the required coverage while maintaining the smallest average set size in almost all experiments. Could the authors elaborate on why this is the case?

3. While it’s valuable to see where the proposed method is effective, in what situations does it fail?

### Soundness
2

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
3

### Summary
This paper proposes a new method for calibrating conformal predictions when using a validation set with noisy labels. While conformity scores are based on previous research, the authors introduce a novel approach to calibrate these scores in the presence of noisy-labeled data in the validation set. This paper mainly addresses the cases where the noise distribution and its parameters are known. The main idea is to utilize the known noise distribution to reconstruct the clean distribution of the conformity scores.

### Strengths
- The proposed calibration method is applicable to a wide range of conformity scores.
- The authors provide a proof that the proposed calibration method meets coverage guarantees.
- Experimental results show that the prediction sets produced by the proposed method are significantly smaller than those generated by other existing methods on the given dataset and in the specified conditions.

### Weaknesses
 - The main assumptions are highly restrictive. The authors assume that both the noise distribution and its parameters are known, and that the training data is either clean or uses pre-trained checkpoints without noisy data, while only the validation data contains noise. This scenario seems uncommon, which may limit the practical applicability of the proposed method. This is a significant limitation as real-world noisy data often does not conform to a known distribution, and the noise parameters are rarely available. Furthermore, the assumption of clean training data is also unrealistic in many practical situations. The method's reliance on these assumptions severely limits its usefulness in practical scenarios where noise is often complex and unknown.
- Additional real-world experimental studies could strengthen the motivation behind the proposed method. For example, clarifying real-world scenarios where the validation dataset is noisy or intentionally corrupted with the known noise distribution would be beneficial. Although the authors conducted experiments on popular classification datasets, the approach remains somewhat unconvincing, since these experiments could be considered as simulations with artificially injected noise. While the method demonstrates superior performance on these datasets, it would be more compelling if there were real-world examples in which the validation data is noisy with a known distribution and parameters. Without such context, the motivation for this method remains somewhat unclear. The experiments, while demonstrating the method's performance under the assumed conditions, do not address the core issue of its applicability to real-world scenarios with unknown or complex noise distributions. The lack of real-world validation significantly weakens the practical relevance of the proposed method.
- While the meaning of $|C_q|$ and $C_q$ can be inferred from the context, a clear definition of these notations would improve readability.
- Although $\widehat{F}^c$ becomes more complex in the noisy case, it still depends only on the indicator function and the count of elements in $C_q$. It also appears to be piecewise constant, with potentially multiple values of $q$ satisfying $\widehat{F}^c(q)=1-\alpha$. In such cases how do you select $q$?
- If the authors intended that the clean label is corrupted into another label with probability of $\varepsilon$, equation (4) might need correction. Currently, equation (4) leads to a noisy label with probability of $\frac{k-1}{k}\varepsilon$ and clean label with probability of $1-\frac{k-1}{k}\varepsilon$. This discrepancy could lead to incorrect calibration, as the noise model used in the calibration process would not accurately reflect the actual noise present in the data.

### Questions
- While the meaning of $|C_q|$ and $C_q$ can be inferred from the context, a clear definition of these notations would improve readability.
- Although $\widehat{F}^c$ becomes more complex in the noisy case, it still depends only on the indicator function and the count of elements in $C_q$. It also appears to be piecewise constant, with potentially multiple values of $q$ satisfying $\widehat{F}^c(q)=1-\alpha$. In such cases how do you select $q$?
- If the authors intended that the clean label is corrupted into another label with probability of $\varepsilon$, equation (4) might need correction. Currently, equation (4) leads to a noisy label with probability of $\frac{k-1}{k}\varepsilon$ and clean label with probability of $1-\frac{k-1}{k}\varepsilon$.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the behavior of conformal prediction in the case of validation data with noisy labels and develop a method for estimating the noise-free CP threshold in the context of noisy validation data. The noise-aware conformal prediction achieves better performance in average set size than other state-of-the-art algorithms.

### Strengths
Extensive experiments for performance comparison to show the advantage of NACP in reducing the average set size while strictly maintaining the validity of coverage;
Consideration of several noise models, including random noise and noise matrix, and this greatly expands the potential application of the proposed method. 
Establishement of an end-to-end CP for estimating noise level in the training of neural network.

### Weaknesses
If you can demonstrate NACP in a more practical setting rather than a simulated environment, this will make the implication of the theorectical contribution of this paper more convincing. 
What is the connection between the two noise models (uniform noise distribution, noise matrix) and practical learning tasks? How should I choose which noise model I should use in practical problems, by trial and error or other approaches?
in Fig. 2, can you also include the set size assocaited with each conformal predictors as this is also an important aspect to evaluate CP performance.

### Questions
See above.

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
3

### Summary
This paper addresses the problem of conformal prediction when the validation set has noisy labels. Algorithms are proposed for two different types of label noises: a uniform noise level $\epsilon$ or a more general noise matrix. In both cases, the noise condition (level/matrix) are assumed to be known. The algorithms will depend on such noise condition.  The paper analyzes the coverage and sample size required from the validation set, and shows the superiority of the proposed method compared with existing ones, e.g., (Sesia et al. 2023), especially regarding data with large label set and small sizes per class. 

Overall, the paper is well written with well justified algorithms and strong empirical results. However, I do have the following concerns/questions that need to be clarified. 

1, I have some concerns over the problem setup. If I am not mistaken, the algorithms assume a good model, i.e., the model is trained on clean labels. But if the validation set is already noisy, it is hard to assume the training data is clean, right? So ideally, the method should be discussing a conformal prediction training and validating on noisy labels. Even if this is too much to ask, there should be experimental evaluation on how the proposed algorithm (and the baselines) perform on the validation set when the model is trained on equally noisy training set. 

2, The proposed methods assume a known noise condition. This is unrealistic. The paper justifies by saying that one could estimate the noise level or the noise matrix through training set. But this would assume a noisy training set in the first place. If the noise condition is estimated through the validation set, there is a question of how reliable the noise condition estimation. In particular, the smaller the sample size is per class, the less reliable these noise condition estimation will be. 

3, the above concern should be discussed regarding other baselines. For example, does SoTA methods (e.g., Sesia et al. 2023) depend on the oracle noise condition? In experiments, if one has to estimate noise using the noisy validation set, how will the proposed method compare with Sesia et al. 2023, and compare with a vanilla conformal prediction?

4, the statement that the second algorithm can handle general noise is an over-statement. Even with the noise matrix, the paper is still assuming the noise is iid. There are plenty of research on label noise problem assuming the noise is not iid, e.g., feature dependent. I understand this is still early stage of the problem, so it is OK not tackling such noise models. But it would be important to mention this in the paper.

Minor errors:
Line 88 – C(x) --> C_q(x)
Equation 16, minor typo?

### Strengths
Solid algorithm and analysis. 

Strong empirical results.

### Weaknesses
1, I have some concerns over the problem setup. If I am not mistaken, the algorithms assume a good model, i.e., the model is trained on clean labels. But if the validation set is already noisy, it is hard to assume the training data is clean, right? So ideally, the method should be discussing a conformal prediction training and validating on noisy labels. Even if this is too much to ask, there should be experimental evaluation on how the proposed algorithm (and the baselines) perform on the validation set when the model is trained on equally noisy training set. 

2, The proposed methods assume a known noise condition. This is unrealistic. The paper justifies by saying that one could estimate the noise level or the noise matrix through training set. But this would assume a noisy training set in the first place. If the noise condition is estimated through the validation set, there is a question of how reliable the noise condition estimation. In particular, the smaller the sample size is per class, the less reliable these noise condition estimation will be. 

3, the above concern should be discussed regarding other baselines. For example, does SoTA methods (e.g., Sesia et al. 2023) depend on the oracle noise condition? In experiments, if one has to estimate noise using the noisy validation set, how will the proposed method compare with Sesia et al. 2023, and compare with a vanilla conformal prediction?

4, the statement that the second algorithm can handle general noise is an over-statement. Even with the noise matrix, the paper is still assuming the noise is iid. There are plenty of research on label noise problem assuming the noise is not iid, e.g., feature dependent. I understand this is still early stage of the problem, so it is OK not tackling such noise models. But it would be important to mention this in the paper.

Minor errors:
Line 88 – C(x) --> C_q(x)
Equation 16, minor typo?

### Questions
See Summary for details.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new method called Noise-Aware Conformal Prediction (NACP) to address the calibration issue when only noisy-labeled validation data is available. The method can estimate noise-free conformal thresholds from noisy data without requiring information about the underlying data distribution or classifier mechanisms. Experiments on medical and natural image datasets demonstrate that NACP significantly outperforms existing methods, especially for large-scale classification tasks.

### Strengths
- The paper is well-written. The authors provide theoretical coverage guarantees for their approach, particularly for uniform noise cases, and extend the framework to general noise transition matrices.
- The extensive experiments demonstrate superior performance of NACP on various classification tasks, where prior methods fail to maintain reasonable prediction set sizes.

### Weaknesses
 - The work lacks analysis on calibration set sizes, particularly for large-scale datasets like ImageNet. It remains unclear how the method performs with different validation set sizes and what is the minimum required samples per class for reliable performance.
- The experiments were conducted only with ResNet-18 architecture, leaving it unclear whether the method's effectiveness generalizes across different network architectures such as deeper ResNets or Vision Transformers.

### Questions
Could you further explain how the noise transition matrices would be obtained in practice? While the paper shows promising results with different noise matrices, it would be helpful to clarify whether additional data is needed for estimation and how estimation errors might affect performance.

### Soundness
3

### Presentation
3

### Contribution
3
