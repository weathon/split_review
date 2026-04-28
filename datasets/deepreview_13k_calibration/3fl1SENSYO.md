# Unleashing the Potential of Diffusion Models for Incomplete Data Imputation

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
This paper introduces \modelname, an iterative method for missing data imputation that leverages the Expectation-Maximization (EM) algorithm and Diffusion Models. By treating missing data as hidden variables that can be updated during model training, we frame the missing data imputation task as an EM problem. During the M-step, \modelname employs a diffusion model to learn the joint distribution of both the observed and currently estimated missing data. In the E-step, \modelname re-estimates the missing data based on the conditional probability given the observed data, utilizing the diffusion model learned in the M-step. Starting with an initial imputation, \modelname alternates between the M-step and E-step until convergence. Through this iterative process, \modelname progressively refines the complete data distribution, yielding increasingly accurate estimations of the missing data. Our theoretical analysis demonstrates that the unconditional training and conditional sampling processes of the diffusion model align precisely with the objectives of the M-step and E-step, respectively. Empirical evaluations across 10 diverse datasets and comparisons with 16 different imputation methods highlight \modelname's superior performance. Notably, \modelname achieves an average improvement of 8.10\% in MAE and 5.64\% in RMSE compared to the most competitive existing method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the imputation of data missing completely at random (MCAR) in tabular data, handling both continuous and categorical variables. The authors propose an EM procedure with a conditional diffusion model for imputation, featuring a novel adaptation of the annealing process for better conditioning on observed values. The paper demonstrates strong results across multiple datasets in comparison with leading methods.

### Strengths
* The paper is well-written with a clear, thorough, and concise introduction that effectively summarizes key points from previous works
* The authors specifically address the challenges of the problem and provide clever solution to mitigate them
* The paper's main novelty is supported by theoretical proof
* The evaluations are comprehensive, with thorough and convincing ablation studies

### Weaknesses
 * A major concern regarding evaluations - while the paper claims to use a single hyperparameter setting throughout, it's unclear how hyperparameters for other methods were selected and their sensitivity to these HP. For me, this concern significantly impacts the overall assessment of the paper.

* While the results are impressive, their importance is not clear. A more convincing evaluation would include the effect on downstream tasks, given imputation is only a first step in most pipelines. 

* Another point regarding evaluations, is the sole focus on data missing completely at random. While the MER assumption is important, it is the MNER which is a primary focus in many imputation methods.

* The 0/1 continuous encoding of categorical data is unusual, given that binary data is a known challenge for diffusion models (for example in fields like graph generation). Also, the use of mean is inherently problematic due to common multi-modality in the data

* The novelty of the method compared to other approaches is not clearly articulated in the related works section

### Smaller Issues
* Given the method's novelty isn't specific to tabular data, the related work should include other imputation methods (e.g., image inpainting)
* A simulation study with multiple modes would be valuable, particularly as diffusion-based models should excel in such scenarios
* Despite highlighting the importance of initialization in the EM procedure, the paper doesn't address this point. (Particularly relevant given the naive initial imputation approach)
* It would be interesting to analyze the relationship between delta_t size and ML solution approximation.
* Figure 4 lacks clarity

### Questions
In biology, missing values are often represented as 0 (or another "limit of detection" (LOD) value), making it difficult to distinguish between actual LOD values and data missing at random (which can comprise 30% of data in cases like proteomics and single-cell analysis). Do you have any ideas about how this problem could be addressed? Note that the fraction of missing values might be known and could potentially be conditioned on.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The missing value imputation is a very important problem in both machine learning and statistics. Although deep generative imputation methods have shown promise, there is still substantial room for improvement, even for matching the performance of some traditional machine learning approaches. This paper introduces DIFFPUTER, a tailored diffusion model combined with the Expectation-Maximization (EM) algorithm for missing data imputation, and shows its promising performance on a variety of datasets,

### Strengths
1. Theoretical analysis: DIFFPUTER’s training step corresponds to the maximum likelihood estimation of data density (M-step), and its sampling step represents the Expected A Posteriori estimation of missing values (E-step). 
2. Extensive experiments that demonstrate the good performance, as compared with existing baselines, of the proposed method across various datasets.

### Weaknesses
the computational complexity is not explicitely discussed or compared on the numerical experiments, see details below.

### Questions
This paper is well-written and easy to understand. This work combines EM with the diffusion model to improve the potential inconsistency caused by missing values in the training process of diffusion models. Since EM is used with K iterations and N number of samples in the E-step, it would be beneficial to also compare the computational complexity (time complexity) of the proposed method with other diffusion-type methods, either in the discussion of the number of operations or comparing the running time in some of the numerical experiments. This would offer more insights into the proposed methods' performance from different perspectives.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an adaptation of the EM algorithm for missing data imputation, leveraging advanced diffusion-based models to perform precise density estimation in the M-step and provide robust imputations in the E-step, inspired by the RePaint algorithm. The authors reference theoretical analyses from prior work to support the use of diffusion models for density estimation and prove a theorem demonstrating that E-step samples can be drawn from the true conditional distribution. Extensive empirical evaluations highlight the proposed method’s robustness and superiority over various baseline approaches, many of which do not incorporate the EM algorithm.

### Strengths
- Robust imputation method based on EM. 
- Well written and structured. 
- The method is theoretically grounded. 
- The empirical analysis is extensive.

### Weaknesses
 - Motivation appears to overlook recent work.

- The two main issues presented as motivation for this work are unclear. The paper claims that generative imputation methods (i) require joint estimation of observed and missing data distributions and (ii) struggle with conditional inference. I find both statements questionable. Numerous studies adapt deep generative models to estimate only the observed data distribution [1-5], which could serve in the M-step of an EM algorithm. Some of these are even referenced in this paper. Moreover, all of these methods allow for straightforward Monte Carlo estimation of $\mathbb{E}[p(\mathbf{x}_m | \mathbf{x}_o)]$ for the E-step, similar to the proposed diffusion-based model. For instance, a more robust importance-weighted estimator is proposed in [4] (see Eq. (12)).

- This brings me to a second point: if multiple DGMs could, indeed, replace diffusion models within the EM framework, how is diffusion specifically justified for tabular data? This approach might be advantageous for high-dimensional data, where diffusion models effectively approximate $p(\mathbf{x})$ and avoid lossy compression (as in VAEs). However, given the lower-dimensional datasets studied here, it remains unclear why a VAE-based approach, for example, wouldn’t perform as well as diffusion.

- Experimental section lacks fair comparison and clarity.

- Based on my earlier points, I would expect an ablation study comparing different DGMs within the EM algorithm. The baselines in the current experiments appear to rely on simple placeholder values for missing data (e.g., zero or mean imputation), effectively completing only one M-step. This is likely to produce suboptimal results, so a performance gap seems unsurprising.

- The assertion "Traditional machine learning methods are still powerful imputers" would benefit from supporting references. I am skeptical, as optimal validation could be harder to achieve in probabilistic settings.

- The claim that generative methods excel on continuous data requires clarification. Here, the diffusion model seems to assume Gaussianity across all dimensions, using $argmax$ as a proxy to obtain discrete outputs, which is not the optimal to model heterogeneous data [2, 3, 5]. 

- The statement "imputation methods are specifically designed for in-sample imputation and cannot be applied to the out-of-sample setting" also needs elaboration. As mentioned, many DGMs designed for missing data can perform out-of-sample imputation.

- In Figure 2, MissDiff appears to fail or encounter out-of-memory issues. This is surprising, as MissDiff’s architecture is similar to the diffusion network used here.

- Discussion of limitations is lacking.

- The main text does not discuss limitations, particularly the high computational cost. A brief note is found in the Appendix, but this isn’t referenced within the primary text. DiffPuter’s approach requires retraining the diffusion model $k$ times, so application to high-dimensional data (e.g., images) would be computationally intense relative to alternatives. I am also curious if the M-step converges faster with higher values of $k$, as this could enhance efficiency.

- Other minor questions

- Figure 6: Why does error decrease as observed data ratio drops? I found the final paragraph of Section 5 somewhat unclear; further clarification here would be helpful.

- Typos
- Line 515: Change ", Reducing" to ", reducing".

### Questions
### Motivation appears to overlook recent work

- The two main issues presented as motivation for this work are unclear. The paper claims that generative imputation methods (i) require joint estimation of observed and missing data distributions and (ii) struggle with conditional inference. I find both statements questionable. Numerous studies adapt deep generative models to estimate only the observed data distribution [1-5], which could serve in the M-step of an EM algorithm. Some of these are even referenced in this paper. Moreover, all of these methods allow for straightforward Monte Carlo estimation of $\mathbb{E}[p(\mathbf{x}_m | \mathbf{x}_o)]$ for the E-step, similar to the proposed diffusion-based model. For instance, a more robust importance-weighted estimator is proposed in [4] (see Eq. (12)).

- This brings me to a second point: if multiple DGMs could, indeed, replace diffusion models within the EM framework, how is diffusion specifically justified for tabular data? This approach might be advantageous for high-dimensional data, where diffusion models effectively approximate $p(\mathbf{x})$ and avoid lossy compression (as in VAEs). However, given the lower-dimensional datasets studied here, it remains unclear why a VAE-based approach, for example, wouldn’t perform as well as diffusion.

### Experimental section lacks fair comparison and clarity

- Based on my earlier points, I would expect an ablation study comparing different DGMs within the EM algorithm. The baselines in the current experiments appear to rely on simple placeholder values for missing data (e.g., zero or mean imputation), effectively completing only one M-step. This is likely to produce suboptimal results, so a performance gap seems unsurprising.

- The assertion "Traditional machine learning methods are still powerful imputers" would benefit from supporting references. I am skeptical, as optimal validation could be harder to achieve in probabilistic settings.

- The claim that generative methods excel on continuous data requires clarification. Here, the diffusion model seems to assume Gaussianity across all dimensions, using $argmax$ as a proxy to obtain discrete outputs, which is not the optimal to model heterogeneous data [2, 3, 5]. 

- The statement "imputation methods are specifically designed for in-sample imputation and cannot be applied to the out-of-sample setting" also needs elaboration. As mentioned, many DGMs designed for missing data can perform out-of-sample imputation.

- In Figure 2, MissDiff appears to fail or encounter out-of-memory issues. This is surprising, as MissDiff’s architecture is similar to the diffusion network used here.

### Discussion of limitations is lacking

- The main text does not discuss limitations, particularly the high computational cost. A brief note is found in the Appendix, but this isn’t referenced within the primary text. DiffPuter’s approach requires retraining the diffusion model $k$ times, so application to high-dimensional data (e.g., images) would be computationally intense relative to alternatives. I am also curious if the M-step converges faster with higher values of $k$, as this could enhance efficiency.

### Other minor questions

- Figure 6: Why does error decrease as observed data ratio drops? I found the final paragraph of Section 5 somewhat unclear; further clarification here would be helpful.

### Typos
- Line 515: Change *", Reducing"* to *", reducing"*.


### References

[1] Ma, Chao, et al. "EDDI: Efficient Dynamic Discovery of High-Value Information with Partial VAE." International Conference on Machine Learning. PMLR, 2019.

[2] Ma, Chao, et al. "VAEM: a deep generative model for heterogeneous mixed type data." Advances in Neural Information Processing Systems 33 (2020): 11237-11247.

[3] Peis, Ignacio, Chao Ma, and José Miguel Hernández-Lobato. "Missing data imputation and acquisition with deep hierarchical models and hamiltonian monte carlo." Advances in Neural Information Processing Systems 35 (2022): 35839-35851.

[4] Mattei, Pierre-Alexandre, and Jes Frellsen. "MIWAE: Deep generative modelling and imputation of incomplete data sets." International conference on machine learning. PMLR, 2019.

[5] Nazabal, Alfredo, et al. "Handling incomplete heterogeneous data using VAEs." Pattern Recognition 107 (2020): 107501.

### Soundness
2

### Presentation
3

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
The authors combine diffusion processes and Expectation-Maximization (EM) algorithms to propose a novel way to impute missing data when both training and tests sets contain missing data. The proposed solution is shown to target the correct conditional distribution (distribution of missing data conditional on observed ones). Imputation values are computed by taken the expectation with respect to this distribution, which is approximated by the sample mean. Experiments on ten real-world data sets show the benefit of the proposed method, compared to various state-of-the-art imputation algorithms (machine and deep learning algorithms).

### Strengths
The authors propose a new method to impute missing data for continuous and discrete inputs. The proposed method appears to be new, with excellent performances. An extensive literature review has been done to present and explain the previous approaches to deal with missing values via imputation. The method is clearly explained, the paper well-written, and the experiments show the benefit of the proposed method.

### Weaknesses
I only have three remarks: 
- RMSE and MAE are measures that encourage the imputation to target the (conditional) mean or median. In both cases, the target is not a distribution but a single quantity. Recent works (https://arxiv.org/abs/2002.03860) have shown that such measures do not properly evaluate the correctness of an imputation method. Imputation score (https://arxiv.org/pdf/2106.03742) can be used instead to assess the quality of imputations. As the proposed method generates a distribution and not a single point estimate, it is likely that its performance will be higher with respect to this metric, showing that it is able to recover the underlying distribution of the data. Presenting imputation scores in the tables would definitely improve the strength of the paper, in my opinion.
- The computational performances of DiffPuter should be discussed in the main text. Table 4 is interesting, as it shows that the training time is larger, but not too important. However, the two considered data sets have few features. It would be appealing to consider larger data sets with (i) more observations and/or (ii) more variables to see how the predictive performances and the training time behave. 
- I have trouble understanding the proof of Theorem 1. Notations are confused to me. Adding a table of notations, with exact definitions at the beginning of the Appendix would help. Besides, many approximations are done in the proof : l.730, 731, 750, 753. This results in the theorem being imprecise. For example, nothing is assumed about the quality of the neural network $\varepsilon_{\theta}$. What type of convergence is required for Theorem 1 to be valid? Similarly, in Theorem 1, $\sigma(T)$ is not assumed to be large, whereas it is required in the proof. Please clarify the different assumptions and the proof.

### Questions
- l.197: could you specify the choice of $\sigma(t)$? 
- l.225-227: the paragraph does not correspond to the equation: the negative log likelihood is upper bounded by the loss plus a constant, which does not imply that optimizing the first leads to optimizing the second.
- Section 5.1, how does the method behave when different masks are present in the training and test set? Does it degrade the performances? 
- Section 5.1, how were the hyperparameter chosen for the different baselines? Are these baselines comparable (in terms of number of parameters for example) with the proposed method? Could you add such a discussion in the Appendix? Could you also describe in details the missing data mechanisms used for the different settings (MAR and MNAR encapsulate a lot of data generating processes)?
- l.366-367, Can you explain the good performances of the proposed method compared to MissDiff and TabCSDI?


l.399 : "Imputaing"
l. 468 : "Gestrue"

### Soundness
3

### Presentation
3

### Contribution
3
