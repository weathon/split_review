# Enhancing Treatment Effect Estimation with Generation-Driven Data Augmentation

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
We introduce $\texttt{GATE}$, a framework for improving the estimation of conditional average treatment effects (CATE) from observational data. Our framework leverages generative models to selectively augment datasets with synthetic potential outcomes, thus addressing the covariate shift problem inherent in CATE estimation. Crucially, $\texttt{GATE}$ enables the integration of external knowledge into downstream CATE models, by leveraging generative models trained on external data sources, such as large language models (LLMs). These models utilise rich contextual information, such as dataset metadata, to generate synthetic potential outcomes grounded in real-world contexts. While generative models can introduce bias when imperfect, we theoretically demonstrate that restricting augmentation to a carefully chosen subsets of the covariate space can allow to achieve performance gains despite these imperfections. Empirically, $\texttt{GATE}$ instantiated with LLMs consistently improves a wide range of CATE estimators, narrowing performance gaps between learners and underscoring the advantages of incorporating external knowledge through generative augmentation, particularly in small-sample regimes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel data augmentation approach for Rubin causal inference, specifically designed to address covariate shifts in Conditional Average Treatment Effect (CATE) estimation. The authors evaluate the effectiveness of augmenting only a subset of the covariate space, demonstrating that their method generally improves performance. This enhancement is attributed to the flexibility inherent in the GATE framework.

### Strengths
- The paper provides a straightforward approach for data augmentation in CATE estimation using LLM.
- It provides a comprehensive set of experiments to showcase the improvement over non-augmented approaches.

### Weaknesses
 - The theoretical analysis lacks a clear connection to the design choices made for the GATE framework.
- Lacks the results for more recent CATE learners, such as TARNet [1], BART [2].
- No clear explanation on how to set up and train the generative models or utilize the LLM for GATE framework.
- The datasets used in these experiments are mostly synthetic datasets.
- No clear improvement when using augmentation in most cases.

### Questions
- In section 4.1, how is the generative model set up when training on $D^{(obs)}_t$? Particularly, what type of generative model is used in this case? How does that affect the performance?
- Does the model only train to impute the mean outcome in that mean-imputing generative model?
- The scoring function directly influences the size of the selected set $X_t$. How exactly does this scoring function work when the generative model performs badly?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work proposes a data augmentation method GATE to improve CATE estimation. In particular, GATE first uses generative models to generate missing potential outcomes, and select only a subset of the generated outcomes to augment the observational dataset. These augmented missing potential outcomes reduces the covariate shift problem as long as the bias of the generative model can be controlled. The authors consider multiple generative models including the LLMs and demonstrate the efficacy of GATE on multiple benchmarks.

### Strengths
- CATE estimation is an important problem with numerous applications.
- The proposed method is sound, both intuitively and theoretically.
- This paper is well-written. 
- Figure 1 is very helpful for understanding the proposed method.
- The experiments are comprehensive. 
- The consideration of *external data source* generative model (i.e., LLM) is very promising

### Weaknesses
## Originality 
This work is based on the principle that **augmenting the observational dataset through potential outcome imputation on a selected subset of individuals** can reduce covariate shift, and if the bias of the imputation is small, then the augmented observational dataset can benefit any downstream CATE model. This principal is **identical** to the an one-year-old work [1] submitted to ICLR 2024 (with an arXiv version [2]), which also proposes a data augmentation method for CATE estimation.

Although this work uses different phrases, e.g., *"augmenting the observational dataset with carefully selected missing potential outcomes sampled from a generative model"* in this work vs. *"it performs imputation for the counterfactual outcomes of these selected individuals"* in [1], the principal is **exactly the same**. This can be further evidenced by the highlighted sentences in two works:
- In line 62 in this manuscript, *"benefits which can be strong enough to counterbalance the bias potentially introduced by an imperfect generative model"*.
- At the beginning of page of [1], *"the positive impact of disparity reduction will outweigh the negative impact of imputation error"*.

## Almost Identical Theoretical Result 
The whole theory section (Section 3) of this work is **uncannily similar** to the theory section (Section 4.2) of [1]. In particular, both work motivates the data augmentation methods through generalization bounds of  CATE models. Both of the generalization bounds from these two works (Theorem 3.1 in this work and Prop 3 in [1]) include three terms: 
- (i) a factual loss term (this work calls it the empirical risk and includes an extra finite-sample term established by another work); 
- (ii) a statistical distance term that measures the distance between two measures on the covariates $X$ (this work uses IPM while [1] uses Total Variation); 
- (iii) a statistical distance term involving the true potential outcome and the imputed potential outcome (this work uses IPM distance while [1] uses the L_2 distance between the true and estimated potential outcome functions).  

While it is fine for theoretical results to appear similar, given the similarity of their motivations and principles, and that they are addressing the same problem (both this work and [1] propose data augmentation methods), I think **a detailed discussion and comparison with Prop 3 in [1]** is definitely needed. Also note that this is **the only theoretical result** in this work. 

## Almost Identical Insights from the Theoretical Result

Given the similar theoretical result, it is not surprising that the insights of this work is similar to that of [1]. For example, just to name a few,
- *"tuning Q via the admissible set Xt allows to navigate the trade-off involved in data
augmentation'* in this work versus
- *"this theorem provides a rigorous illustration of the trade-off
between the statistical disparity across treatment groups and the imputation error"* in [1],

and 
- *"excluding from Xt regions where the generative model performs poorly can
further enhance performance"* in this work versus
- *"It underscores that by simultaneously minimizing disparity and imputation error, we can enhance the performance of CATE estimation model"* in [1]

## Technical Weakness: Selection of the Missing Potential Outcome
The term 2 in Theorem 3.1 is interpreted as the noise of the generator, which consists of **both bias and variance**. The author proposes to select the generated outcomes with the variance, **completely ignoring the bias**. 

[1] "Counterfactual Data Augmentation with Contrastive Learning" (https://openreview.net/forum?id=7mR83Q12cJ).

[2] Aloui, Ahmed, et al. "Counterfactual Data Augmentation with Contrastive Learning." arXiv preprint arXiv:2311.03630 (2023).

### Questions
- What percentage of the generated potential outcomes are eventually used to augment the observational dataset? If my understanding is correct, the percentage should be exactly $\alpha$.
- Are the variances of LLMs really highly correlated with their bias on all the benchmarks?
- How are the hyper parameters selected? For example, how do you choose the $\alpha$ in practice?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a generative modeling based approach to impute missing potential outcomes in a subset of the covariate space. It presents one general theoretical result supporting the general methodology of augmentation as well as empirical studies.

### Strengths
The paper presents a new generative modeling approach to impute a reliable subset of the missing potential outcomes.

### Weaknesses
The main weakness lies in the incremental nature of the contribution. While using LLMs to generate a subset of missing potential outcomes is novel, the core concept of identifying a subset of individuals within the feature space for imputation has been previously explored, as in Aloui 2023 (which is mentioned by the authors) and Nagalapatti 2024 (https://arxiv.org/pdf/2401.15447). More extensive studies on the effects of various generative models and a comparison of their performance are needed to make the work more comprehensive. Moreover, The code was not added in the supplementary materials, adding even a notebook with few experiments, would have have been helpful to assess the reproducibility of the results.

### Questions
1. How do the authors tune the parameter $\alpha$, in real world experiments only the factual data is availabe and estimating the epehe to validate is not possible, how do the authors intend to deal with this?

2. If the selected generative model (or the LLM) used has an inherent bias due its training can it bias the imputation as well?

3. Can the authors explain the variance problem? And how is it related to the imputation error? I can have deterministic imputation (by imputing 0 to every missing potential outcomes) hence it has a zero variance but what matters more is the imputation error? Shouldn't the tradeoff by between imputation error and covariate shift between treatment groups?

4. How sensitive are the imputation for changing the prompts in both the in context and no context prompts?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the estimation of conditional average treatment effects (CATE) from observational data using a framework called GATE. It employs generative models to augment datasets with synthetic potential outcomes, focusing on mitigating covariate shift. The key contribution is demonstrating that targeted data augmentation can improve CATE estimation, especially in low-data scenarios.

### Strengths
1. The experiments conducted are extensive and well-supported.

2. The main content of the paper is clearly written and easy to follow.

### Weaknesses
1. First, I have some questions about the originality of this paper; data augmentation for causal data is not a novel concept, and I do not see any significant differences from existing works in the authors' theoretical discussions and method design.

2. The paper primarily focuses on qualitative analysis regarding covariate shift but lacks quantitative assessments to substantiate the claims that the augmented data effectively mitigates covariate shift. This absence of rigorous empirical validation undermines the overall effectiveness of the proposed method.

3. The depiction and explanation of Figure 1 are quite ambiguous and do not effectively convey the key points of the method. I recommend making some revisions for clarity.

### Questions
1.	In Figure 1, it appears that the symbol \( k \) is not utilized. Is this an oversight or is there a specific reason for its absence? I kindly request clarification from the authors, as this is crucial for understanding your methodology.

2.  Can you provide a more intuitive example to explain how your causal data augmentation method differs from general data augmentation and other causal enhancement methods?

### Soundness
2

### Presentation
2

### Contribution
2
