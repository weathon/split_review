# Flexible Heteroscedastic Count Regression with Deep Double Poisson Networks

- Decision: Reject
- Avg Score: 4.75
- Scores: 8, 3, 5, 3

## Abstract
Neural networks that can produce accurate, input-conditional uncertainty representations are critical for real-world applications. Recent progress on heteroscedastic \textit{continuous} regression has shown great promise for calibrated uncertainty quantification on complex tasks, like image regression. However, when these methods are applied to \textit{discrete} regression tasks, such as crowd counting, ratings prediction, or inventory estimation, they tend to produce predictive distributions with numerous pathologies. Moreover, discrete models based on the Generalized Linear Model (GLM) framework either cannot process complex input or are not fully heterosedastic. To address these issues we propose the Deep Double Poisson Network (DDPN). In contrast to networks trained to minimize Gaussian negative log likelihood (NLL), discrete network parameterizations (i.e., Poisson, Negative binomial), and GLMs, DDPN can produce discrete predictive distributions of arbitrary flexibility. Additionally, we propose a technique to tune the prioritization of mean fit and probabilistic calibration during training. We show DDPN 1) vastly outperforms existing discrete models; 2) meets or exceeds the accuracy and flexibility of networks trained with Gaussian NLL; 3) produces proper predictive distributions over discrete counts; and 4) exhibits superior out-of-distribution detection. DDPN can easily be applied to a variety of count regression datasets including tabular, image, point cloud, and text data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Deep Double Poisson Networks (DDPN) for heteroscedastic regression on discrete count data. 
The key contributions is using the double Poisson distribution as the output distribution, which provides more flexibility than Poisson or negative binomial distributions while maintaining proper support over integers (unlike Gaussian which has pathologies behavior because of this). 
The authors also propose a $\beta$-modification to the loss function to better balance mean fit and uncertainty calibration. 
Comprehensive experiments across tabular, image, point cloud and text data demonstrate DDPN's superior performance in terms of both prediction accuracy and uncertainty quantification.

### Strengths
- Clear motivation and principled solution to discrete regression with uncertainty estimation
- Strong theoretical analysis of the relationship between different discrete distributions and why double Poisson is more flexible
- Comprehensive empirical evaluation across diverse datasets and modalities
- Excellent ablation studies demonstrating the impact of the $\beta$ parameter
- Strong out-of-distribution detection capabilities compared to baselines
- Good reproducibility with code provided

### Weaknesses
 - Some empirical results (e.g., on Amazon review dataset) show relatively modest improvements over strong baselines
- Could benefit from more analysis of when simpler distributions might be sufficient

### Questions
1. How sensitive is the method to the choice of $\beta$? Are there heuristics for selecting it for different applications?
2. Could you elaborate on why $\beta$=0.5 seems to work particularly well for ensembles?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors proposed DDPN for heteroscedastic count data along with a $\beta$-modification to enhance prediction performance. While the introduction of heteroscedasticity into neural networks and the focus on discrete data are appreciated, there is a lack of investigation into existing methods, and one of the two presented measures seems not suitable for comparing the methods.

### Strengths
The introduction of heteroscedasticity into neural networks is a notable strength, as it enables more flexible and accurate modeling of data with varying dispersion. Additionally, the focus on discrete data addresses a gap in existing research, highlighting the method's practical relevance for count-based outcomes.

### Weaknesses
 **1. Insufficient discussion of existing methods** 

The authors identify the limitations of several approaches to representing heteroscedasticity in Poisson distributions, providing motivation for their proposed method. However, the authors did not mention Joint GLM, which has been widely discussed in the literature. For example, Chapter 10 of *Generalized Linear Models* (McCullagh and Nelder, 1989)—which the authors cited as McCullagh (2019)—discusses "Joint modeling of mean and dispersion" within the GLM family. *Generalized Linear Models with Random Effects* (Lee, Nelder, and Pawitan, 2017) also examines Joint GLM for mean and dispersion, which is a natural extension of heteroscedastic model for Gaussian cases to the GLM family. As far as I know, linear components of Joint GLM can be replaced with neural networks, but the authors did not clarify how the use of the Double Poisson distribution offers distinct advantages over this approach.

**2. Concerns with comparing likelihoods across different distributions**

There is a fundamental issue with the presentation. The authors directly compared likelihood values under different distributional assumptions. However, such comparisons are strongly discouraged as they can lead to misleading conclusions. The authors should acknowledge this and include the necessary methodological context or justification.

**3. Need for theoretical support and further investigation of $\beta$-DDPN**

The introduction of the $\beta$-DDPN and its demonstration in Figure 5 is interesting, but the method currently lacks sufficient theoretical support. A more comprehensive and foundational investigation into convergence could provide deeper insights. For instance, an ablation study on the bias and variance of weight estimates in linear models could help clarify the influence of the $\beta$ value on convergence behavior.

### Questions
**1.  On Existing Methods:**
- The authors omitted a discussion on Joint GLM, which is widely acknowledged in the literature and even appears in McCullagh (2019), cited by the authors. Clarification on this omission would be required.
- Could the authors elaborate on how the Double Poisson distribution provides distinct advantages over Joint GLM?

**2. On Comparing Likelihoods:**
- Could the authors justify comparing likelihood values across different distributional assumptions?
- If such justification is not possible, considering alternative measures for comparison would be required.
- For certain datasets, differences in MAE does not seem significant. Providing statistical test results would support the analysis.

**3. On Theoretical Support for $\beta$-DDPN:**
- An ablation study on the bias and variance of weight estimates in simpler (linear) models could provide insights into the impact of the $\beta$ value on convergence.
- It seems that the influence of the $\beta$ value might depend on whether the initial value of $\phi$ is set high or low. Could the authors explain or provide insight into this potential dependency?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work attempts to improve discrete heteroscedastic regression by predicting the parameter for a double poison distribution. 

The contributions include: 1) the method outperforms the baselines on some datasets; 2) the authors modify the NLL loss to leverage between mean and distribution prediction; 3) the method exhibits superior out-of-distribution detection functionality.

### Strengths
The paper is easy to follow, with a clear presentation.

The proposed method:
1) shows superior results regarding MAE or NLL on some of the datasets.
2) provides the $\beta$ modification to the loss to enable prioritizing either the mean or the distribution prediction.
3) exhibits superior OOD detection behavior.
4) shows how the $\beta$ trick effects the convergence of DDPN.

### Weaknesses
The novelty of the paper: the method changes the output distribution compared to previous work. For example, while previous work predicts the parameter for a Gaussian distribution, this work predicts the parameter for a Double Poison distribution. However, the connection between the new distribution and the superior performance is not clearly analyzed. It remains possible that one can try different distributions for different datasets. Thus, the method is not innovative from the methodology perspective. Other than the distribution change, the method also relies on the $\beta$ trick proposed by Seitzer et al, which further reduces the originality of the work. 

Experiment results: while the method shows superior performance for one of the metrics in most cases, it does not necessarily indicate the significance of the model. Instead, tuning and applying the $\beta$ trick to some of the baseline methods may lead to better performance. However, it is not explored. Thus, it remains unclear whether it is the introduction of a new distribution or the $\beta$ trick that leads to the improvement. I recommend the author to further explore the trick with baseline methods and make a fair comparison to show what is behind the improvement. 

For the OOD detection, the DDPN and variants indeed show better behavior compared to some of the results. However, it does not seem to be better than Immer et al.

### Questions
1. Could you explain why Double Poison is more appropriate compared to the other distributions? Or in which case, this distribution should show superior performance?

2. Could you show how $\beta$ affects the performance of the baseline methods and explore them also in the same space ($\beta \in [0,1]$)?

3. Are DDPN and the variants better in OOD detection compared to Immer et al? It is not obvious from Fig.4. Could you further illustrate the reason why you claim "DDPN shows the greatest ability of all benchmarked regression models to differentiate better ID and OOD inputs"?

4. Could you explain why some of the baselines are missing from the boosting experiments?

### Soundness
2

### Presentation
3

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
This paper presents Deep Double Poisson Network (DDPN), a probabilistic Deep Neural Network (DNN) method by predicting the mean and inverse dispersion of the Double Poisson (DP) distribution for heteroscedastic and discrete count regression problems. DPPN is trained by using the Maximum Likelihood of DP with a “tunable mean fit” parameter $\beta$. The authors show that DDPN and its ensemble version achieve lower Mean Absolute Error (MAE) and Negative Log-Likehood (NLL) than other baselines on regression data and higher predictive entropy in the Out-of-Distribution (OOD) detection setting.

### Strengths
- The paper is well-written, and it is easy to understand the important aspects of the algorithm.
- I like the motivation of this paper, the proposed method aims to contribute to discrete regression tasks, such as crowd counting, rating prediction, etc.
- The experimental results show the proposed method is better than some baselines in terms of MAE and NLL on tabular and complex datasets, as well as useful for OOD detection.

### Weaknesses
 - From my point of view, the proposed method is somewhat not novel enough. Given the literature on the heteroscedastic Gaussian distribution with DNN [1, 2, 3], DDPN simply replaces Gaussian with the DP distribution to tackle the discrete count regression problem.
- The training algorithm depends on the additional tunable parameter $\beta$. There is a trade-off between mean-focused and variance-focused regarding the selection of $\beta$. And, tunning $\beta$ is non-trivial in practice. Specifically, the method lacks a clear, principled way to choose \$\beta\$ without relying on a validation set, which can be problematic when data is scarce. The sensitivity of the model to this parameter is also not sufficiently explored, and it's unclear how much the performance varies with different values of $\beta$.
- There is no theoretical contribution in this paper. For instance, no theoretical guarantees show that DDPN can achieve better performance (e.g., generalization bound, uncertainty quality bound, etc.) than other methods. The lack of theoretical analysis makes it difficult to understand the conditions under which DDPN is expected to perform well or poorly, and how it compares to existing methods in terms of convergence and stability.
- The experiments are also not convincing. Firstly, DDPN depends on the tunable parameter $\beta$, and its results vary significantly and do not consistently outperform other baselines. Secondly, a lot of measurements to assess model uncertainty quality are missing, e.g., calibration & sharpness [4], AUPR/AUROC, ROC curve [5], etc. The use of NLL alone is insufficient to fully characterize the quality of the uncertainty estimates, as it does not directly measure the alignment between model confidence and accuracy. Furthermore, the reported Median Precision (MP) lacks context without comparisons to other methods, making it difficult to assess its significance.
- Miscellaneous: I feel some sentences are over-claimed. For instance in the abstract, "..4) exhibits superior out-of-distribution detection.". This is not convincing me when seeing the experimental evidence in OOD detection. The claim of superior OOD detection is not strongly supported by the provided evidence. The delta value, while larger than some baselines, does not provide a complete picture of OOD performance. A more comprehensive analysis, including metrics like AUPR/AUROC, is needed to substantiate this claim.

### Questions
1. In Figure 4, the density across the entropy value of DDPN is uniformly small. Why is this? Can you report the calibration and sharpness value [4] between methods?

2. There is a trade-off between mean-focused and variance-focused regarding the selection of $\beta$. Given the test set is unavailable in the world, how can we choose the best-fit $\beta$ in training to balance this trade-off?

3. Let's consider with only a single forward pass, how DDPN can estimate epistemic uncertainty? And, how DDPN can disentangle aleatoric and epistemic uncertainty?

References:

[1] Lakshminarayanan et al., Simple and scalable predictive uncertainty estimation using deep ensembles, NeurIPS, 2017.

[2] Nix et al., Estimating the mean and variance of the target probability distribution, International Conference on Neural Networks, 1994.

[3] Chua et al., Deep reinforcement learning in a handful of trials using probabilistic dynamics models, NeurIPS, 2018.

[4] Kuleshov et al., Calibrated and sharp uncertainties in deep learning via density estimation, ICML, 2022.

[5] Nado et al., Uncertainty Baselines: Benchmarks for Uncertainty & Robustness in Deep Learning, arXiv preprint arXiv:2106.04015, 2021.

### Soundness
3

### Presentation
3

### Contribution
2
