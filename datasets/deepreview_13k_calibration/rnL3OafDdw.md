# Bayesian Image Regression with Soft-thresholded Conditional Autoregressive Prior

- Decision: Accept
- Avg Score: 5.75
- Scores: 3, 6, 6, 8

## Abstract
In the analysis of brain functional MRI (fMRI) data using regression models, Bayesian methods are highly valued for their flexibility and ability to quantify uncertainty. However, these methods face computational challenges in high-dimensional settings typical of brain imaging, and the often pre-specified correlation structures may not accurately capture the true spatial relationships within the brain. To address these issues, we develop a general prior specifically designed for regression models with large-scale imaging data. We introduce the Soft-Thresholded Conditional AutoRegressive (ST-CAR) prior, which reduces instability to pre-fixed correlation structures and provides inclusion probabilities to account for the uncertainty in choosing active voxels in the brain. We apply the ST-CAR prior to scalar-on-image (SonI) and image-on-scalar (IonS) regression models—both critical in brain imaging studies—and develop efficient computational algorithms using variational inference (VI) and stochastic subsampling techniques. Simulation studies demonstrate that the ST-CAR prior outperforms existing methods in identifying active brain regions with complex correlation patterns, while our VI algorithms offer superior computational performance. We further validate our approach by applying the ST-CAR to working memory fMRI data from the Adolescent Brain Cognitive Development (ABCD) study, highlighting its effectiveness in practical brain imaging applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a new Bayesian method for sparse regression. To solve the sparse regression settings, they introduce a method based on stochastic subsampling and variational inference. They verify their model using simulation data, and finally apply their model on fMRI task activation maps to predict the effect of brain regions on IQ development and how the task activation map is affected by parental education level. Throughout the paper the authors consider two regression settings; Image on Scalar (IonS) regression and Scalar on Image regression (SonI).

### Strengths
I think the authors set up an important and interesting problem both in their simulated setting and for fMRI data. Specifically, I believe that encoding spatial relationships in both regression settings is important, and I think the significance of the authors’ method can therefore be high. The authors compare their method to good baselines, and I think the comparisons are relatively fair. The idea is original and builds on the soft-thresholded Gaussian process, which the authors cite and compare against. I think the authors also do a relatively good job of explaining their method, and their results on simulated data are good. However, the clarity of the method can be improved.

### Weaknesses
Major weakness(es): 
I think the two main major weaknesses of this work are 1) that the paper lacks a thorough hyperparameter search and the method is very sensitive to hyperparameters and 2) that the fMRI analysis lacks depth.
1. First, authors describe a lot of hyperparameters on Pages 6 and 9, but none of these hyperparameters are explained or searched over. Specifically on Page 6 for the STGP model: a=0.01, b=10, 10 degrees of Hermite polynomials per sub-region, 10^4 iterations, thresholding parameter is 0.2. For ST-CAR: thresholding parameter, decay rate, number of neighbors, correlation parameter, and fixed variance parameter. The same thing applies for Page 9. It is of course not necessary to search over all of these hyperparameters, but it’s good to explain why you set them and search over the most important hyperparameters for competing methods. Especially since hyperparameters may make a big difference. Second, the method is very sensitive to its hyperparameters, as can be seen Table A2 &A3, and the training and test R^2 values do not correlate with each other. Specifically, the best training R^2 in Table A.2 (0.84 R^2) achieves the worst test R^2 (0.12). If the authors had thus used the best training model, they would have performed worse than ElasticNet and STGP on the held-out test set (0.23 and 0.28 R^2 on the test set respectively). The same behavior is found in Table A3, where the best test R^2 (0.64) is achieved at the worst training R^2 (0.22) and vice-versa (0.51 vs 0.41). In fact this to me puts into question the simulated results, and I would strongly encourage the authors to perform a hyperparameter search, pick the best hyperparameter based on validation set results (i.e. separate the data into a training, validation, and test set), and then evaluate each model (including their own) with those hyperparameters on the test set. I specifically mention this point as well because the authors select the best v and $\sigma_\beta^2$ based on the best testing performance (L443), which is bad practice, since it can lead to overfitting. Especially since there is almost an inverse relationship between the training and test performance (as described previously).
2. The authors mention throughout the paper that many of the assumptions they make in their model hold for fMRI data (L162 for example). Hence, I would assume this paper to have more of a focus on actually showing why this model works well for fMRI data. However, I think the fMRI analysis lacks depth, and the results in Figure 3a do not look convincing because of how noisy the significant regions look. The noisiness is underlined by the results in Table A2: the IQ predictions do not seem to generalize well from the training to the test set. Additionally, the authors do not show whether their method actually identifies different areas than any of the baseline methods, which would help verify that their model is a helpful tool for the neuroimaging field compared to the baseline methods. Although I understand that the authors choose not to go too in-depth about the results since this is a machine learning conference, I think given the focus on fMRI in this paper the authors should expand a lot on their current discussion of what these results indicate (i.e. why does it make sense that these regions are related to IQ and parental education level?), atleast in the Appendix. Lastly, and this is not as important to address, but I think there are additional potentially more interesting questions one can ask using the ABCD dataset, i.e. regressions to mental health assessments [1].

Minor weaknesses:
1. The authors mention that there is a sparse signal in fMRI data, the authors should expand on this claim. Similarly, on Line 162 the authors claim that the signal is assumed to be sparse and piecewise smooth, but the authors should expand on this claim and potentially provide references. I agree generally with the statement, but I do think it’s important for the authors to explain why.
2. The notation the authors use can be confusing, the authors use $I_d$ for an identity matrix of dxd dimensions, but also use $I(\cdot)$ as the indicator function. I would encourage the authors to use $\mathbb{1}_{\{\cdot\}}$ as notation for the indicator function instead. Similarly, instead of using $\mathcal{N(j)}$ for a neighborhood and $\mathbf{N}(\cdot)}$ for a Normal distribution, I would use $\mathcal{N}$ for a Normal distribution and other notation for the neighborhood. Lastly, $p_j$ is not defined in the text on Line 131.
3. The authors do not compare their model with T-LoHo on the data that is used in the T-LoHo paper. I assume because ST-CAR cannot handle non-smooth spatial flips from positive to negative values well (i.e. Line 161), but the authors do not mention this in the limitations section or show any results on these types of edge cases.
4. The authors should also and more importantly report FLOPs instead of computation time because computation time is machine-dependent.
5. The authors mention fMRI pre-processing  on Line 422, but do not explain in the paper what types of pre-processing they perform. Moreover, they do not explain how they select the subjects they use and how they split the data into a training and test set.
6. The authors only show the positive effects in their fMRI results (Figure 3) and Table 2, which they should do, since it isn’t clear why only positive effects are expected for the hypotheses they test.
7. The quality of Figure 3 is not up to par, it is hard to read the color bar numbers.

Spelling/grammar:
- L36-37: “…, and it can be time-series …, or in our particular interest, the functional Magnetic Resonance Imaging data … of human brain signal.” -> .This high-dimensional component can be a time-series, …, or in our case, functional magnetic resonance imaging (fMRI) data of the human brain.
- L39/40: “…, formulated as a scalar-on-image (SonI) regression…” -> formulated as scalar-on-image (SonI) regression
- L54/55: “… is still computationally expansive...” -> is still computationally expensive
- L109/109: “…, referred to as the…” -> called the
- L247: “… algorithm, but cannot directly give inference results …” -> algorithm, but cannot directly infer
- L271/272: “… selection accuracy in SonI setting.” -> selection accuracy in the SonI setting.
- L305: “…, we use ridge regression result …” -> we use the ridge regression result
- L371/372: “… blow 10% …” -> below 10%

### Questions
1. L102: I don’t quite understand why the authors say that the function on L101 shrinks values below $v$ to zero, since $I(\cdot)$ is the indicator function isn’t any value below $v$ zero?
2. Based on Figure 1 I was wondering whether it’s not just possible to use a different kernel to get better results both on the simulated data, i.e. reducing the variance in the exponential kernel or using a kernel like the Jump Gaussian process [1]? The authors select hyperparameters for the STGP model on L288, but do not provide any reason for these hyperparameters. I would strongly encourage the authors to do a thorough hyperparameter search on a validation set for all of the methods they compare against.
3. On Line 213/214 the authors mention the design matrix M, but isn’t M the task activation map? The design matrix normally contains regressors of interest and nuisance regressors.
4. Have the authors looked at how initialization affects each model? I understand there are differences that may make this hard for some methods, but ST-CAR is initialized differently than the other methods.
5. Why did the authors choose to look at IQ and parental education level effects in the brain? And why did the authors use the 2-back task activation map?

[1] Park, C. (2022). Jump Gaussian process model for estimating piecewise continuous regression functions. Journal of Machine Learning Research, 23(278), 1-37.

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
This paper introduces a novel prior, the Soft-Thresholded Conditional AutoRegressive (ST-CAR) prior, for handling high-dimensional imaging data in regression models, specifically for brain imaging studies. The ST-CAR prior adapts to data-driven spatial smoothness, controlling sparsity, and incorporating inclusion probabilities for selecting active voxels.

The ST-CAR prior is applied to two common regression models in neuroimaging: scalar-on-image (SonI) and image-on-scalar (IonS). In SonI, brain imaging data are used to predict scalar outcomes, such as cognitive scores, while in IonS, scalar predictors (e.g., parental education level) are used to predict imaging outcomes. The paper introduces variational inference (VI) algorithms, including Coordinate Ascent Variational Inference (CAVI) and Stochastic Subsampling VI (SSVI), to make the approach computationally feasible for large-scale datasets. Results from simulation studies and a real-data analysis using the Adolescent Brain Cognitive Development (ABCD) study demonstrate that the ST-CAR prior outperforms traditional methods in identifying active brain regions and offers improved computational efficiency.

### Strengths
The authors have made a comprehensive presentation of their method and the presented results seem convincing. They have implemented both synthetic experiments and also a real ones, which strengthens their method. Overall, I believe that this paper can have an impact on the neuroimaging domain and making inferences on high-dimensional imaging data in curated clinical studies.

### Weaknesses
### Weaknesses 
1. Dependence on Thresholding Parameter v. 
- While the paper claims that the ST-CAR prior is relatively insensitive to the choice of the thresholding parameter v, the results could still be impacted by this setting. A suboptimal threshold could lead to either excessive sparsity (losing important signal) or insufficient sparsity (resulting in noise). Without clear guidelines for tuning v, users may struggle with finding the right balance, especially across different datasets. The paper should include a more thorough sensitivity analysis demonstrating how different values of v affect the results across a range of simulated and real-world scenarios. Furthermore, the authors should explore and propose a data-driven method for choosing v, rather than relying on manual selection or cross-validation alone, which may not be robust to variations in data characteristics.

2. Limited Applicability for High Signal-to-Noise Ratios (SNR)
 - The paper notes that the ST-CAR prior performs well in low-SNR settings, particularly with SonI models. However, in settings where SNR is high, the method might not be optimal compared to other methods that handle high-SNR data more effectively. This could limit the generalizability of the model to other types of imaging data or modalities with higher SNR. The paper should provide a more detailed analysis of the performance of ST-CAR across a spectrum of SNR levels, including a comparison with methods specifically designed for high-SNR data. Additionally, the authors should discuss potential challenges or modifications needed to apply ST-CAR to noisier, lower quality data. Have they tested or plan to test the method on less processed datasets? Specific preprocessing steps or model adjustments that might be necessary for such data should be proposed.

### Questions
### Questions 

- Can you discuss how this method could be applied to other imaging modalities, such as structural MRI, DTI, and PET imaging? Would any assumptions need to be adjusted when handling these modalities instead of fMRI data?

- Is it necessary to apply IonS and SonI regressions in such high-dimensional spaces? Are there atlas-based methods that could produce ROI-level features that are more interpretable? By using such features, one might make inferences at a more aggregated level. So, my question is: is it essential to perform voxel-level inferences to determine the relationships between brain ROIs and clinical outcomes in such high-dimensional data? I would like the authors to elaborate on the need to work in this high-dimensional space.

- Clinical study data are often curated and carefully processed. Do you believe that ST-CAR could handle real imaging and clinical data that are frequently noisy and of lower quality?

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
4

### Summary
This paper presents a Soft-Thresholded Conditional AutoRegressive (ST-CAR) prior for Bayesian regression in high-dimensional brain imaging data, demonstrating its advantages in capturing complex spatial dependencies and quantifying uncertainty. The authors validate the ST-CAR model's effectiveness through simulations and real data, while employing variational inference and stochastic subsampling to enhance computational efficiency.

### Strengths
1. The ST-CAR prior introduces a novel method to handle spatial dependencies in high-dimensional imaging data, where the coefficient is assumed to be smooth and sparse across their spatial domain.

2. The proposed framework for solving the problem achieves substantial improvements in computational speed, making it more feasible for high-dimensional applications.

3. The framework is validated on both simulated data and real fMRI data from the ABCD study, demonstrating its effectiveness in identifying significant brain regions associated with cognitive development.

### Weaknesses
1. The ST-CAR model involves several tuning parameters (e.g., the number of neighbors, thresholding parameter and decay rate), it seems that they require careful designed to achieve optimal performance. Specifically, the interaction between the thresholding parameter and the initial value of \(\sigma_\beta\) needs further clarification. The current discussion does not provide sufficient guidance on how these parameters should be jointly tuned, especially when the signal-to-noise ratio (SNR) is low, which is common in high-dimensional imaging data. The lack of a systematic approach to hyperparameter selection could limit the practical applicability of the model.

2. The ST-CAR model effectively identifies significant regions of WM tasks in the ABCD dataset, but it seems that it cannot provide insights into broader brain circuits or networks, which are increasingly recognized as critical for understanding complex brain functions and disorders. The model's focus on localized spatial smoothness might overlook the importance of long-range functional connectivity and distributed patterns of activity. This limitation restricts the model's ability to capture the complex interplay between different brain regions.

### Questions
1. Given the model’s focus on identifying significant brain regions, could it be extended to analyze inter-regional connections or brain circuits in cognitive functions?

﻿2. How sensitive is the ST-CAR model to different choices of the number of neighbors, the thresholding parameter and the decay rate? Do those hyperparameters stay robust in other datasets (e.g., HCP datasets)

3. Would it be possible to consider structural connectivity among regions of interest (extracted from DTI) as the exposures or confounders？

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work, the authors present a novel prior for use in bayesian image regression from functional magnetic resonance imaging (fMRI). Motivated by limitations of previous priors which require the prior specification of a gaussian process kernel, which can lead to bias and other issues in the regression unless the true signal is known beforehand, the authors provide a novel prior which relaxes smoothness assumptions on functional parameters. The authors demonstrate that this novel prior autoperforms previous priors by a significant margin.

### Strengths
I find this work to be altogether very strong work with some omissions in the experimentation that should be easily addressed. At its core this work is well-motivated by intuition regarding the shortcomings of previous priors - the relaxation of the smoothness assumption is easy to grasp, and provides a firm foundation for the reader to follow the following, more dense theoretical work. I found no issues with the theoretical work, and appreciated the rigor taken by the authors.

The inclusion of substantial numerical and real-data experiments is a huge boon to this work. The authors do a substantial amount of experimental validation here, and demonstrate that this novel prior outperforms existing priors. 

The authors also include a substantial appendix with additional work which I think further solidifies this as a strong paper. 

Well done!

### Weaknesses
The only minor quibble I have with this work is the lack of standard deviations in most of the results. For example, in table 1 you average over 100 replications, but don't provide any standard deviation measures. These should be provided to fully solidify the performance of your approach over other methods.

### Questions
All of the questions I have regard the performance over multiple repetitions and would be addressed simply by providing those standard deviations. Every other question I had was substantially addressed in the appendix.

### Soundness
4

### Presentation
4

### Contribution
4
