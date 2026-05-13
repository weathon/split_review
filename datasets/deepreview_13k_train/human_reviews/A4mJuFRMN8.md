# Dirichlet-based Per-Sample Weighting by Transition Matrix for Noisy Label Learning

- Decision: Accept
- Scores: 6, 6, 5, 6, 6, 6

## Abstract
For learning with noisy labels, the transition matrix, which explicitly models the relation between noisy label distribution and clean label distribution, has been utilized to achieve the statistical consistency of either the classifier or the risk. Previous researches have focused more on how to estimate this transition matrix well, rather than how to utilize it. We propose good utilization of the transition matrix is crucial and suggest a new utilization method based on resampling, coined RENT. Specifically, we first demonstrate current utilizations can have potential limitations for implementation. As an extension to Reweighting, we suggest the Dirichlet distribution-based per-sample Weight Sampling (DWS) framework, and compare reweighting and resampling under DWS framework. With the analyses from DWS, we propose RENT, a REsampling method with Noise Transition matrix. Empirically, RENT consistently outperforms existing transition matrix utilization methods, which includes reweighting, on various benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the crucial issue of learning from noisy labels, emphasizing the significance of the transition matrix in modeling the relationship between noisy and true labels. Rather than concentrating solely on learning this matrix, the authors propose a new approach that leverages it, drawing inspiration from reweighting and resampling concepts. They introduce a Dirichlet-based weighting method, which assigns individual weights to each sample drawn from a Dirichlet distribution. This distribution is parameterized using a base measure informed by the transition matrix. Empirical results indicate that this weighting method outperforms forward risk minimization and direct reweighing techniques.

### Strengths
Originality: The concept of imposing a Dirichlet prior on individual sample weights is well-founded. This approach naturally leverages the base measure to integrate the transition matrix, creating an informative prior. Additionally, the ability to control the concentration parameter $\alpha$ enables the fine-tuning of weight properties, including variance-based regularization and addressing noise-related issues. The practical implementation of this method is straightforward, as demonstrated in Algorithm 1.

Significance: The significance of this work is underscored by the comparison of the proposed reweighing method with forward risk minimization and an existing reweighting method based on the likelihood ratio. This comparative analysis is conducted across four datasets, and the results demonstrate the promise and potential impact of the proposed approach.

Clarity: Overall, the paper effectively conveys its central idea. However, there is room for improvement in terms of notation clarity.

### Weaknesses
The comparative analysis of RENT is limited to FL and RW, utilizing transition matrices obtained through various methods. A more comprehensive evaluation, including a broader range of noise-label learning techniques, such as the approach proposed by Lin et al. in 2022, would provide a more comprehensive assessment of RENT's performance.

### Questions
* In table 2, there are a couple of settings, where RENT does not perform as well as the other two methods, can the authors discuss the underlying reasons?
* The author said that RENT performs better when estimated T differs from True T, the reviewer wondered if one can plot the performance gap against the differences between the estimated T and True T.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper first extends the reweighting strategy used in noisy-label learning, with a Dirichlet-based framework. This framework encompasses both reweighting and resampling as the two extremes of the Dirichlet distribution. The paper provides analysis of the impact of the shape parameter to the empirical risk and discuss resampling is better than reweighting. The paper finally proposes a method called RENT (resampling utilizing the noise transition matrix). Various experiments show the superiority and characteristics of the proposed method.

### Strengths
- The proposed algorithm is simple.
- Discussions about the relationship between related work is explained in detail.
- Experimental results are encouraging: we can see the benefit of introducing RENT.

### Weaknesses
 - While reviewing the paper, I encountered some challenges in comprehending the content, primarily due to the clarity and organization of the presentation and missing notations/definitions. Some examples:
	- An explanation of $M$ seemed to be missing in page 4 but appears later on in page 6 (explained as a resampling budget.) The initial introduction of $M$ lacks context, making it difficult to understand its role in the reweighting framework. Specifically, it's unclear if $M$ refers to a fixed number of samples or a parameter controlling the amount of reweighting. The connection between $M$ and the Dirichlet distribution is also not immediately apparent. 
	- Would it be better to have Equation 3 in page 4 right after the definition of $R_{\ell, RW}$ in page 3? The current ordering disrupts the flow of the argument. The reader first encounters the definition of the reweighted risk, then the discussion of the Dirichlet distribution, and finally, the specific form of the reweighted risk using the Dirichlet distribution. This separation makes it harder to see the direct relationship between the reweighting strategy and the proposed Dirichlet framework.
	- I wasn't sure how $x_1, \ldots, x_M$ are determined in Algorithm 1 page 6. Since $\pi_N$ is a categorical distribution (and not a joint distribution of instances and labels), it seems to me that we can only sample $\tilde{y}_1, \ldots, \tilde{y}_M$ (without $x_1, \ldots x_M$)? The algorithm description is ambiguous about the sampling process. It's unclear if the categorical distribution is over the entire dataset or just the labels. The lack of clarity on how the input instances $x_i$ are associated with the sampled labels $\tilde{y}_i$ makes it difficult to understand the resampling process.
- For Proposition 3.1, it might be more clear to present the assumptions directly within the proposition rather than explaining them in the appendix. The current setup requires the reader to jump between the main text and the appendix, disrupting the reading experience and hindering a clear understanding of the proposition's scope. The assumptions are crucial for interpreting the result, and they should be readily available.
- Is Eq. 7 correct? Should we introduce a different notation for the quantity in Eq.7 instead of writing that this is equivalent with $R_{l, DWS}^{emp}$, since we are applying the CLT in the proof in Appendix C.1 and $N$ is finite? The use of $R_{l, DWS}^{emp}$ in Equation 7 is confusing, as it appears to be an empirical risk, yet the derivation involves an asymptotic argument. This suggests that the quantity in Eq. 7 is not the same as the empirical risk, and a different notation would be more appropriate to avoid confusion. It is not clear that the empirical risk is asymptotically equivalent to the quantity on the left hand side of the equation.

### Questions
I already wrote some of my questions in the previous section. Some other minor comments/questions:

- The 'et al.' in the references could be written out in full.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of improving the uilization of transition matrix in label noise learning, authors propose that due to the poor estimation of class posterior, existing approaches such as loss correction or re-weighting might easily fail. To counter this issue, the authors proposed REsampling method to utilize the Noise Transition matrix (RENT), which utilizes Dirichlet distribution based resampling to assign instance-dependent weights.

### Strengths
1. The proposition of improving the utilization of transition matrix is interesting, and shows good insight - due to factors such as complexity, estimation error in noise class posterior and so on, even with a perfectly estimated transition matrix, it might still exhibts subpar performances. 

2. The idea of re-sampling instead of re-weighting for loss correction is straight forward and intuitive.

### Weaknesses
 **Major issues:**

1. Some experimental results are inconsistent with prior works, why are the performances of learning with true $T$ worse than Cycle consistency and Dual-$T$?

2. The discussions in section B seems problematic, in $\sum_{j=1}^{C}\(max_{j} T_{\hat{y}_{i}j} \)$, are we trying to sum over all $j$, or finding the maximum $j$? It seems that you're trying to do both, can you instead give an intuitive explaination and refine your mathmatical statements?

3. The motivation of DWS is not strong enough, if we are going with the assumption that the classifier trained with noisy labels can not accurately estimate noise class posterior (poorly calibrated, high estimation error, etc.), then we can hardly assume that the transition matrix is accurate, as the transition matrix is usually estimated from the noise class posterior.

**Minor issues:**

1. More recent and SOTA $T$ estimation method is not included [1].

### Questions
1. It is well-known that instance-dependent transition matrix might exhibit high complexity when the class number increases, for instance, for cifar-100, we need to compute a tensor of size $50000 \times 100 \times 100$, which is prohibited in real-world applications, can DWS mitigate this issue? More discussions in this aspect might bring more contribution.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a resampling based training method for noisy label learning. The paper builds upon the resampling framework which has been proven to be superior to the reweighting method.  The proposed method utilizes Dirichlet distribution-based per-sample weight sampling to re-formalize reweighting and resampling, aiming to improve the utilization of the transition matrix. The experiments confirm the advantage of the resampling method.

### Strengths
The paper is well organized and clearly written. 
The paper has a good angle that focuses on utilizing the transition matrix instead of estimating the transition matrix. 
The paper formalizes the reweighting and resampling methods and provides a good analysis of both methods. 
The paper provides comprehensive evaluation results regarding the reweighting and resampling methods.

### Weaknesses
1. The paper does not propose a "new" method. Reweighting and resampling are both existing methods, and may not be considered novel contributions.
2. Although the Dirichlet based analysis provides some good angles, the theoretical results do not have a clear insight. The distance from the true weight part simply says that the distance becomes smaller as $\alpha\rightarrow0$, but this does not tell us much because $\alpha\rightarrow0$ just gives a weight assignment closer to one-hot as demonstrated. 
3. The paper lacks comparison with other means to deal with noisy label learning.
With these concerns, I have some doubt about the overall contribution of the paper.

### Questions
1. What can we get from the theoretical analysis other than resampling being better than reweighting when $\mu^*$ and $\mu$ are different, which is a conclusion from previous work (An et al. 2020)?
2. Following the last point, how different is the Dirichlet-based resampling from just setting a threshold for $\mu$ and randomly sampling?
3. Will the method work better if combined with data cleaning or abstention kind of ideas? There is one reference that I found ([1] Koziarski, Michał, Michał Woźniak, and Bartosz Krawczyk. "Combined cleaning and resampling algorithm for multi-class imbalanced data with label noise." Knowledge-Based Systems 204 (2020): 106223.). Although I'm not familiar with this work, I think it might be interesting to the authors and other reviewers.
4. Can the proposed method be compared with other noisy label learning methods (regularization, loss correction, or data cleaning)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper primarily explores the use of transition matrices in the context of noisy label learning. The authors conduct a meticulous analysis to expound upon the challenges that arise during the practical application of extant methods employing transition matrices. In response to these challenges, the authors introduce the Dirichlet-based per-sample Weight Sampling (DWS) framework. This framework effectively unifies two distinct methodologies, sample reweighting and resampling, facilitating their comparison within a comprehensive framework. Furthermore, the authors undertake an exhaustive analysis, establishing the resampling technique as supremely effective in addressing issues pertinent to noisy label learning.

### Strengths
1. The background and the motivation of the setting is well-introduced. The motivation of the work is reasonable.

2. The authors integrates sample reweighting and resampling methods into a single framework for comparative analysis, highlighting the superiority of the resampling approach.

3. The method is simple and the results on several datasets seem good.

### Weaknesses
1. I acknowledge the authors' theoretical contributions, but it must be said that the method proposed by the author lacks innovation. The approach in this paper bears similarity in concept to a significant category of noisy label learning methods based on sample selection, and their success strongly underscores the superiority of resampling methods. Specifically, the proposed method, RENT, shares conceptual overlap with sample selection techniques that aim to filter out noisy labeled samples. While RENT leverages a transition matrix for statistical consistency, the core idea of prioritizing certain samples over others based on a selection criterion is not novel. The practical implementation of RENT, which involves sampling based on the Dirichlet distribution, can be seen as a stochastic form of sample selection, which is not a significant departure from existing methods.

2. On CIFAR-10N dataset, RENT performs well on rand1-3 and worse scenarios but exhibits poor performance on aggre. In the context of crowdsourcing, aggre should be a more common noise setting. Therefore, it is essential to analyze the reasons for the subpar performance in this particular scenario. The performance degradation on the 'aggre' noise setting, which simulates a more realistic crowdsourcing scenario, raises concerns about the method's robustness. The fact that RENT does not consistently outperform other methods under this setting suggests a potential limitation in its ability to handle complex, real-world noise patterns. This is particularly concerning given that the 'aggre' setting is designed to mimic the type of label noise often encountered in practical applications.

### Questions
Why use the Dirichlet distribution to sample the weight?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Different from previous researches that focus more on how to estimate the transition matrix, which is significant for the risk estimator to achieve the statistical consistency, this paper proposes a new utilization of the transition matrix to deal with noisy labels.

### Strengths
1.This paper proposes a new approach, named RENT, a resampling method with Noise Transition Matrix.

2.The proposed approach origins from the analysis of comparing reweighting and resampling under Dirichlet distribution based per-sample Weight Sampling (DWS) framework, which is reasonable.

3.Experimental results show the effectiveness of the approach.

### Weaknesses
1.Since the final algorithm chooses resampling, my main concern is the advantage of resampling comparing to reweighting, which should be given more details about and hightlighted in some sections like Introduction. Specifically, the paper should delve deeper into why resampling, which inherently discards data, is superior to reweighting, which retains all data while adjusting its influence. The theoretical justification for this choice is not sufficiently explored, and the empirical evidence, while present, lacks a thorough analysis of the conditions under which resampling outperforms reweighting. A more detailed discussion of the bias-variance trade-off in the context of noisy labels is needed to justify the resampling approach.

2.Figure 1 should be polished up to clearly illustrate how to implement the proposed framework. Otherwise, it is difficult to understand the 4-th and 5-th paragraphs of Section Introduction. The current figure lacks the necessary detail to convey the precise steps involved in the RENT framework. A more granular depiction of the data flow, the transformation of the transition matrix, and the resampling process would greatly enhance the reader's understanding. The figure should explicitly show how the noise transition matrix is used to generate the resampling probabilities and how these probabilities are applied to the training data.

3.It is suggested to summarize the contributions at the end of Section Introduction, such as extension of DWS, the analysis of reweighting and resampling, the new resampling method.

4.Some details about the implementation of the resampling should be given in the main body of the paper. For example, the reason why $\tilde{\mu}$ and the parameters of Categorical Distribution are calculated in the way illustrated in Algorithm 1. The paper lacks a clear explanation of the mathematical derivation behind the calculation of $\tilde{\mu}$ and the parameters of the categorical distribution. The connection between the noise transition matrix and these parameters is not clearly established, leaving the reader to guess the underlying rationale. A more detailed explanation of the mathematical steps and the assumptions behind them is needed to make the algorithm transparent.

### Questions
1.As it is mentioned above, why $\tilde{\mu}$ and the parameters of Categorical Distribution are calculated in the way illustrated in Algorithm 1?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
