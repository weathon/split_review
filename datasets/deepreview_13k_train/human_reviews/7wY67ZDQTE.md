# Cauchy-Schwarz Divergence Information Bottleneck for Regression

- Decision: Accept
- Scores: 6, 6, 5, 6, 6

## Abstract
The information bottleneck (IB) approach is popular to improve the generalization, robustness and explainability of deep neural networks. Essentially, it aims to find a minimum sufficient representation $\mathbf{t}$ by striking a trade-off between a compression term $I(\mathbf{x};\mathbf{t})$ and a prediction term $I(y;\mathbf{t})$, where $I(\cdot;\cdot)$ refers to the mutual information (MI). MI is for the IB for the most part expressed in terms of the Kullback-Leibler (KL) divergence, which in the regression case corresponds to prediction based on mean squared error (MSE) loss with Gaussian assumption and compression approximated by variational inference.
  In this paper, we study the IB principle for the regression problem and develop a new way to parameterize the IB with deep neural networks by exploiting favorable properties of the Cauchy-Schwarz (CS) divergence. By doing so, we move away from MSE-based regression and ease estimation by avoiding variational approximations or distributional assumptions. We investigate the improved generalization ability of our proposed CS-IB and demonstrate strong adversarial robustness guarantees. We demonstrate its superior performance on six real-world regression tasks over other popular deep IB approaches. We additionally observe that the solutions discovered by CS-IB always achieve the best trade-off between prediction accuracy and compression ratio in the information plane.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors of this paper introduce a novel approach to regression using the IB principle, leveraging the Cauchy-Schwarz divergence for parameterization. This departure from MSE-based regression eliminates the need for variational approximations or distributional assumptions, leading to improved generalization and strong adversarial robustness. Their CS-IB method outperforms other deep IB approaches across six real-world regression tasks, achieving an optimal balance between prediction accuracy and compression ratio in the information plane.

### Strengths
- The authors show the connections between CS divergence to MMD and HSIC. 
- The effect of CS divergence to generalization and adversarial robustness is well quantified. 
- Thorough discussions are provided for most of remarks or theoretic findings.

### Weaknesses
 - The CS divergence estimation is based on the Gaussian kernel assumption, which will depend on the parameter $\sigma$. What is the effect of $\sigma$ to the IB performance is not shown clearly. Specifically, the paper lacks a rigorous exploration of how different $\sigma$ values influence the trade-off between compression and prediction accuracy. While a Gaussian kernel is a common choice, the sensitivity of the results to this parameter and how to choose it optimally for different datasets is a critical concern that needs further investigation. The absence of a clear guideline for selecting $\sigma$ makes the method less practical.
- The KL IB using variational approach is friendly to optimization based methods (gradient-based approaches). On the other hand, CS IB method is based on Gaussian kernel assumption, which may require the tuning of $\sigma$. This tuning process could be computationally expensive and may not scale well to large datasets. The paper should discuss the computational overhead of tuning $\sigma$ and how it compares to the optimization of variational parameters in KL-based IB methods. Furthermore, the paper needs to address the potential for the CS-IB method to get stuck in local minima due to the non-convex nature of the kernel parameter optimization.
- I think it’s better to have a section of identifying what are some potential disadvantages of CS-IB method compared to KL-IB method. For instance, the lack of a dual representation for CS divergence, unlike the KL divergence with its Donsker-Varadhan representation, could be a significant limitation. This dual representation allows for neural network-based divergence estimation, which is particularly useful in high-dimensional spaces. The paper should explicitly state this limitation and discuss the potential impact on the scalability and applicability of the CS-IB method.

### Questions
The complexity of CS-divergence estimation approach is O(N^2). How is it compared to that of the traditional KL divergence based IB method?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study information bottleneck (IB) methods for regression tasks using a new divergence (Cauchy-Schwarz). The authors showed how to algorithmically design an IB approach based on this new divergence, analyzed the theoretical properties of the new divergence, and numerically demonstrated a visible advantage over existing approaches.

### Strengths
The use of Cauchy-Schwarz divergence in information bottleneck approaches is reasonable and novel to my understanding.

The authors derived an efficient algorithm for training IB approaches based on the Cauchy-Schwarz divergence.

The authors demonstrate visible improvement over existing approaches.

### Weaknesses
The improvement over existing approaches is fairly limited. In many tasks, the improvement is as small as 0.1 RMSE (where the relative improvement is close to 0.01~0.04). I am not sure if the limited improvement on these datasets is particularly meaningful. It is unclear whether this marginal gain justifies the increased complexity of using the Cauchy-Schwarz divergence. Furthermore, the experiments should include a more diverse set of datasets, particularly those where the data distributions are known to be complex or non-Gaussian, to better demonstrate the advantages of the proposed method. 

It remains conceptually unclear to me why we want to use the Cauchy-Schwarz divergence. It is shown to be always <= KL divergence, but it is not clear how much smaller would this be (maybe only minimally). The paper does not provide sufficient intuition on the specific scenarios where the Cauchy-Schwarz divergence would be significantly more advantageous than the KL divergence. The theoretical analysis should also delve deeper into the properties of the Cauchy-Schwarz divergence, particularly in relation to its behavior when the supports of the distributions have minimal overlap, and how this impacts the optimization process.

### Questions
- Could the authors provide a high-level idea/motivation in the Introduction to describe why one should consider the Cauchy-Schwarz divergence instead of the more traditional KL divergence? Why is it better to avoid variational approximations?

- Are there toy problems where Cauchy-Schwarz divergence performs significantly better than other traditional approaches?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The authors considered using the Couchy--Schwarz (CS) divergence to parameterize the information-bottleneck (IB) with deep neural networks (DNNs), which is beyond the MSE (or MAE) loss based on Gaussian (or Laplace) variational distribution.
- Furthermore, they proposed using the non-parametric estimation by plugging in the output of DNNs through the kernel density estimator (KDE) for the following two terms in their objective: the prediction term (CS divergence) $D_{\mathrm{CS}}(p(y|x); q_{\theta}(\widehat{y}|x))$ and the compression term (CS-QMI) $I_{\mathrm{CS}}$, which allows us directly estimate the MI instead of its upper bound as in existing approaches.
- They also provided a discussion regarding the relationship between CS and MMD-based estimators.
- They offered theoretical and empirical analyses for generalization error and adversarial robustness based on the work of [Kawaguchi et al. in 2023] and [Wang et al. in 2021].
- They empirically confirmed the predictive and robustness performance of their CS-IB method.

### Strengths
- They introduced a new choice of loss function based on CS divergence for the IB method, which was often used with MSE based on Gaussian settings or MAE loss based on Laplace distribution.
- They pointed out the challenges in estimating MI and the adoption of indirect methods, such as estimating upper bounds. They proposed an IB framework based on direct estimation by performing non-parametric estimation using KDE.
- They pointed out that existing methods adopt indirect methods for MI estimation, such as estimating upper bounds, and they proposed an IB framework based on direct estimation by performing non-parametric estimation using KDE.
- They attempted empirical verification regarding the correlation between CS-QMI and generalization error, providing insights into the generalization analysis of the IB method based on CS divergence.
- They conducted performance evaluation experiments on a wide range of real-world data, including California Housing, MNIST, Beijing PM2.5, and UTKFace.

### Weaknesses
I would like to express my sincere respect for all the efforts the authors have invested in this paper. Unfortunately, however, I cannot strongly recommend this paper as an ICLR 2024 accepted paper for the following reasons: (1) a misalignment between the claims of contribution, the assumptions of theoretical analysis, and the content of theoretical analysis; (2) a lack of theoretical guarantees on the properties of the proposed estimations, and the unclear discussion of the pros and cons between direct estimation and upper bound estimation approaches, or the absence of sufficient comparative experiments to complement it; and (3) concerns regarding the reliability of the experimental results. The details are provided below. If there are any misunderstandings, I apologize, and I would appreciate it if you could explain them to me.

## A misalignment between the claims of contribution, the assumptions of theoretical analysis, and the content of theoretical analysis
- The authors claim that by leveraging the CS divergence, they can perform non-linear IB regression for any distribution $p(x, y)$ without heavy reliance on variational approximations and without making distribution assumptions. How accurate is this claim? The independence from the variational distribution seems to be achieved not so much due to the properties of the CS divergence but rather through non-parametric estimation using Kernel Density Estimation (KDE) on the outputs from neural networks, treating them as samples from the training data. Therefore, the motivation for introducing the CS divergence may lack a clear and solid rationale, leaving room for discussion regarding its validity in the context of this presentation. The core of the method appears to be the KDE, not the CS divergence itself, which raises questions about the necessity of using CS divergence over other divergence measures that could also be estimated non-parametrically.
- Furthermore, while the authors claim that their contribution lies in the ability to estimate without making distribution assumptions, the actual theoretical analysis deals with a limited setting where both the model distribution and variational distribution are assumed to be normal distributions. This limitation is acknowledged as a one of limitations in Appendix D. However, it can be considered a significant weakness that the proposed method's theoretical guarantees are limited, given the broad claim of removing the necessity of distribution assumptions. This disparity should ideally be addressed in the main part of the paper. The theoretical results are thus not aligned with the claims of the method's generality.
- For one of the contributions mentioned, I believe the explanation of the adversarial robustness aspect is rather too concise. Besides Lemma 1, there should be a proper proof for [Wang et al., 2021] Theorem 2's Corollary as well. In the current presentation, while one may vaguely understand the content being discussed, the explanations are too informal, making it difficult to accurately determine whether the validity is established. The theoretical part of the proof should ideally be self-contained within the main paper, rather than relying on related literature. The connection between the proposed CS-QMI and the robustness bound is not clearly established, and the reliance on external results makes the argument less convincing.
- The assumptions underlying generalization analysis and adversarial robustness have not been well-organized. It is recommended to consolidate these assumptions.

## A lack of theoretical guarantees on the properties of the proposed estimations, and the unclear discussion of the pros and cons between direct estimation and upper bound estimation approaches, or the absence of sufficient comparative experiments to complement it
- When constructing nonparametric estimators, a critical concern always revolves around whether (asymptotic) unbiasedness or (asymptotic) consistency is guaranteed. This theoretical assurance holds true for nonparametric estimations like Kernel Density Estimation (KDE) and k-Nearest Neighbors (k-NN) based on KL divergence [1,2], among others. In the context of the IB method under focus here, I presume that unbiasedness and consistency play a significant role in determining its performance. The importance of analyzing this aspect lies in the bias introduced by parameter estimation in variational approaches dependent on the variational distribution, as well as the bias in the estimators of the proposed method. Deciding which of these biases is smaller - the one induced by parameter estimation or the one introduced by the proposed method - is a crucial perspective in determining whether a direct estimation approach, like the proposed method, or a variational estimation approach is more useful. Unfortunately, this paper lacks comprehensive discussions on this aspect. The lack of convincing arguments on why a direct estimation approach like the proposed method is effective. This issue holds immense significance in the comparison between the proposed method and conventional methods, and it remains one of the unresolved problems in this paper, marked as a limitation. Relevant questions pertaining to this matter are summarized in the Question section. The paper does not provide a clear comparison of the bias-variance trade-off between the proposed method and variational approaches.
- When comparing the bias introduced by the variational approach with that introduced by nonparametric estimations such as the proposed method, it would be beneficial to investigate a toy example with an increased sample size to determine which approach exhibits higher estimation accuracy. Unfortunately, this paper did not provide such experimental confirmations. A controlled experiment comparing the estimation accuracy of the proposed method and variational methods with varying sample sizes is needed to support the claims.
- The authors, I believe, are understood, but the theory in Section 3.2.1 assumes that the generalization error upper bound is derived in a manner that includes the objective function of the proposed method, which alone does not guarantee generalization performance, as is evident. As mentioned in the Strength section, the attempt to experimentally verify this aspect is a fascinating endeavor. However, the empirical correlations have only been validated on toy data. To increase the persuasiveness of the empirical evidence regarding the correlation with generalization performance, it would have been necessary to confirm the experimental results on benchmark data adopted in Section 4. The generalization analysis lacks empirical validation on real-world datasets, limiting its practical relevance.

## Concerns regarding the reliability of the experimental results.
- Due to the absence of reports on measures of dispersion, such as standard deviations, for all the experimental results in this paper, it is difficult to determine whether the proposed method consistently achieves superior performance compared to other methods. This raises concerns about the validity of the claim made by the authors as one of their contributions, that CS-IB outperforms other methods. Since the proposed method is built on nonparametric estimation, it is conceivable that the variance of the estimates can become large when there are not enough samples, leading to increased variability in performance. In essence, to support the claim that the proposed method is superior, it would be challenging to agree without considering factors such as the randomness of model initialization, mini-batch datasets, and adversarial perturbations. It is advisable to repeat the experiments several times, report the average and standard error of the obtained prediction accuracy, and evaluate performance while taking variability into account. The lack of standard deviations makes it impossible to assess the statistical significance of the results.
- I find it puzzling that some of the reported numerical values in the experiments are identical in every aspect. For instance, in Table 2, the RMSE for the existing methods when $r=0$ is a complete match across all experimental settings. This further emphasizes the need for reporting both the average prediction accuracy and the standard error. While the average prediction accuracy may be the same, the standard error might differ between methods. If they do indeed match perfectly, it is advisable to check for any implementation bugs. At the very least, there are concerns regarding the credibility of the currently reported numerical values. The identical results across different settings for existing methods raise serious concerns about the experimental setup and potential implementation errors.
- I apologize if I missed any details earlier, but it does appear that there is a lack of explanation regarding hyperparameter settings, such as in Table 4. This omission can give the impression that there might be arbitrariness in the experimental results. If you have indeed eliminated arbitrariness, it would be beneficial to provide more detailed explanations about how you selected the reported hyperparameters. This would help enhance the transparency and credibility of your findings. The absence of a clear hyperparameter selection process undermines the reproducibility and reliability of the experimental results.

### Questions
In connection with the weaknesses mentioned above, I would like to pose several questions related to the concerns raised. I would appreciate your responses.

- It seems that this nonparametric approach could also be applicable to the conventional objective function based on KL divergence. Why was it not discussed, proposed, or included as a subject for comparative experiments?
- As mentioned in Remark 1, CS divergence is a special case of Rényi divergence. Under this premise, it could have been considered as a generalization of the conventional KL-based methods using Rényi divergence, especially from the perspective that it converges to KL divergence as α approaches. Why was the emphasis placed on this particular special case?
- The uniqueness of the KDE estimator in CS divergence has already been provided by [3]. I understand the need to construct an estimator consisting of three elements: predictions, input data, and label data, in the context of the IB method. However, it seems that there might not be such a fundamental difference between the basic nonparametric estimation and the proposed method. If these aspects are positioned as variations based on the ideas from related research, it would be beneficial to explicitly state this and discuss the differences, if any. What are your thoughts on this?
- Can you guarantee the asymptotic properties of the two estimation methods in the proposed approach? For instance, is asymptotic unbiasedness or consistency ensured?
- Why do the performance values for existing methods in Table 2 match perfectly? 
- Why was it not considered to conduct repeated experiments and report the mean and standard deviation?
- How were the hyperparameters selected?

## Citation
(Note: I am not the author of the following papers)

[1]: Q. Wang, S. R. Kulkarni, and S. Verdú. Divergence estimation for multidimensional densities via k-nearestneighbor distances. IEEE Transactions on Information Theory, 55(5), 2009.
https://www.princeton.edu/~kulkarni/Papers/Journals/j068_2009_WangKulVer_TransIT.pdf

[2]: F. Perez-Cruz, Kullback-Leibler divergence estimation of continuous distributions. 2008 IEEE International Symposium on Information Theory, Toronto, ON, Canada, 2008, pp. 1666-1670, doi: 10.1109/ISIT.2008.4595271.
https://www.tsc.uc3m.es/~fernando/bare_conf3.pdf

[3]: R. Jenssen, J. C. Principe, D. Erdogmus, T. Eltoft, The Cauchy–Schwarz divergence and parzen windowing: Connections to graph theory and mercer kernels, Journal of the Franklin Institute 343 (6) (2006) 614–629.
https://www.sciencedirect.com/science/article/abs/pii/S0016003206000767


================ AFTER REBUTTAL & DISCUSSION ================

The authors diligently worked to enhance their paper, successfully addressing certain concerns, such as the comparison of a non-parametric estimator.
Considering the substantial revisions and additional analysis, I am of the opinion that the manuscript should undergo another round of peer review to validate these changes.
I raised my score, but with the perspective that it is just below the acceptance borderline.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
I’m unfamiliar with entropy-based methods. So my reviews are purely based on reading the paper without comparison to the related literature.

This paper uses the CS divergence of IB for regression estimation. It can be regarded as empirical CS divergence minimization on the conditional distribution $p(y|x)$ with a regularization term on $I(x,t)$. This problem can be efficiently estimated via kernel density estimator. The effectiveness of this metric is demonstrated on four benchmark datasets and two image datasets.

### Strengths
- the CS divergence is smaller than KL divergence under Gaussian distribution as well as some relatively general setting (e.g., $p$ and $q$ are sufficiently small)
- The rationality of the regularization term is verified on generalization and adversarial robustness

### Weaknesses
Since I’m not an expert in this community, it appears difficult for me to evaluate the contribution. I only have few questions on this work:

- The CS divergence is based on the Cauchy-Schwartz inequality, a special case of Holder inequality. Does this metric can be extended in the general $L_p$ space?
- Theorem 1 is restricted to Gaussian distribution. Though this assumption can be relaxed if $p$ and $q$ are sufficiently small, it would be possible to extend to the sub-Gaussian, sub-exponential case?
- For the generalization bound, the authors obtain a tighter bound but $I_{CS}(x;t)$ and $I(x;t)$ are still in the same constant order?

### Questions
See the above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses an information bottleneck (IB) approach for neural network-based regression, using Cauchy-Schwarz divergence in place of Kullback-Leibler divergences and estimating these using kernel methods. The authors connect their approach to several methods from the literature (MMD, HSIC, etc.) and illustrate in their results that their approach is able to outperform IB approaches based on other approximations of (KL-based) mutual information.

### Strengths
The paper belongs to an interesting branch of literature, namely deep learning with information-theoretic cost functions. While the use of kernel methods in this regard is not new, the usage of Cauchy-Schwarz divergence is novel as far as I know. The paper is written quite accessibly, and important connections are made between the proposed approach and the existing related work. The results seem to indicate that the proposed methods can outperform existing approaches based on IB and its approximations.

### Weaknesses
There are a few aspects of the work that prevent me from recommending publication at this stage. I look forward to reading the authors replies to my concerns, upon which I may improve my score.
* In Remark 3, the authors clearly state that a kernel width of $\sigma=0$ reduces the CS divergence between the true posterior and the decoder distribution to classical MSE. With this in light, it is not clear in what respect CS divergence is fundamentally different from estimating $I(y;t)$ using a Gaussian variational distribution (limits novelty). Also, it is not clear why the CS-IB outperforms other methods also for $r=0$.
* In Remark 4, the authors claim that the use of KL divergence combined with a Gaussian assumption is "likely to induce inductive bias". The same can be said about using CS divergence with Gaussian kernels (which resonates with Remark 3, for which CS divergence reduces to MSE for $\sigma=0$). Specifically, at a very superficial glance it appears that the inductive biases of KL+Gauss and CS+Gauss are not too different. I would appreciate a paragraph explaining the fundamental differences (from the perspective of inductive bias).
* While I agree that CS-QMI is a rigorous definition, I do not agree that the proposed estimator measures mutual dependence in bits. As has been known for some time (see, e.g., Th. 1 in Amjad and Geiger or the work of Goldfeld et al.), for deterministic networks true MI between $x$ and $t$ is infinite. I doubt that $D_{CS}$ remains finite in such a setting (e.g., Renyi divergence is infinite if the joint and product of marginal distributions are singular w.r.t. each other, cf. Th. 24 in van Erven and Harremoes). From that perspective, I do not see how your estimators based on CS divergence have substantial mathematical advantages over existing estimators (although I acknowledge that the estimation may still be useful from a practical perspective; also, I understand that your networks are stochastic, because $t$ is obtained by adding Gaussian noise to a decoder output).
* One of my main concerns is the comparison of methods in Table 2 and Fig. 2. As far as I can see, $r$ is defined via the respective estimators (i.e., CS divergences for CS-IB, variational costs for VIB, etc.). This makes a comparison difficult, as the same $r$ indeed may lead to different compression ratios when compression is measured in a common currency (e.g., CS divergence for all methods). While this is problematic only for Table 2, in Fig. 2 the same holds for $I(y,t)$. Specifically, CS-IB is the only method that does not use the MSE, for the estimation of $I(y;t)$ which explains the difference at $r=0$. Essentially, the red line may be just above all others because $I(y;t)$ is measured differently (namely, using CS divergence). Also here a common currency would be better, such as MSE or RMSE. (Further, using the RMSE would allow for a better comparison with Table 2.)

### Questions
See above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
