# Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory

- Decision: Accept
- Scores: 8, 3, 6, 5

## Abstract
Synthetic data has gained attention for training large language models, but poor-quality data can harm performance (see, e.g., \cite{shumailov2023curse, seddik2024bad}). A potential solution is data pruning, which retains only high-quality data based on a score function (human or machine feedback). Previous work \cite{feng2024beyond} analyzed models trained on synthetic data as sample size increases.

Using random matrix theory, we generalize this analysis and derive the performance of a binary classifier trained on a mix of real and pruned synthetic data in a high dimensional setting. Our findings identify conditions where synthetic data could improve performance, focusing on the quality of the generative model and verification strategy. We also show a smooth phase transition in synthetic label noise, contrasting with prior works on sharp transition in infinite sample limits. Our extensive experimental setup validates our theoretical results.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work considers the problem of maximizing the usefulness of synthetic data in the modern era of generative modelling whereby at least part of the training data is not from the real data distribution, but synthesized from another AI model. In the solvable setting of a mixture of isotropic Gaussians, the authors consider a linear model whose weights vector is a regression-style ridge estimator. The synthetic data distribution is taken as yet another Gaussian mixture whose parameters (i.e shape) is given by empirical estimates of the ground-truth Gaussian mixture: the amount of data on which these parameters are estimated serves as a proxy for the quality of the synthetic data. Optiinally, this synthetic data is mixed with data from the real data distribution.

In the "proportionate" high-dimensional scaling limit, the authors use classical tools from random matrix theory (RMT) to obtain exact analytic expressions for the classifier and its accuracy. In particular, they paper recovers the theoretical results of Feng. et al (2024) as special case (corresponding to training only on synthetic data).

### Strengths
- A nice theoretical setup for analysing the impact of synthetic data and pruning strategies is introduced.
- A complete analytic theory for this toy setting is obtained and its phenomological clearly discussed.
- Theoretical results from previous work Feng et al. (2024) are recovered as special cases.
- The calculations provided in the appendix could be of independent usefulness, beyond the specific problem considered in the paper. I should however immediately nuance this praise by noting that similar calculations have been done in  Liao and Couillet (2019) "A Large Dimensional Analysis of Least Squares Support Vector Machines", for more general kernel-based models.
- The paper is very clearly written.

### Weaknesses
 - **The setup.** Fitting a regression model to use its weights as a linear classifier, nobody does this in practice. The authors should justify why such a model is reasonable / relevant, beyond the fact that it leads to a tractable analysis. Note that the underlying estimator is a linear version of the so-called least-squares support vector machine (LS-SVM) which was analyzed in Liao and Couillet (2019) "A Large Dimensional Analysis of Least Squares Support Vector Machines".
- **(Ir)relevance to practice.** In the asymptotic regime considered in this paper, mixing real and synthetic data only helps when the proportion of real data is bounded-away from zero. Also, the practitional needs to know which samples are real and which samples are synthetic. These constraints might not match what happens in practice. This observations have also been made in Dohmatob et al. (2024) "Strong Model Collapse".
- **Non-optimal mixing.** The weights in mixing strategy considered is a bit naive / sub-optimal. The right thing to do would be to consider a general mixing constant $\alpha \in (0,1)$ (the papers uses $\alpha=1-\alpha=1/2$), and derive a theory as a function of $\alpha$, alongside the other  constants in the theory, namely $\pi$, etc.. In general the optimal value of $\alpha$ will depend on the other constants. See Jain et al. (2024) "Scaling laws for learning with real and surrogate data" and Dohmatob et al. (2024) "Strong Model Collapse"

### Questions
Though I think the paper is potentially a very good paper, I still have a few worries as outlined in the **Weaknesses** section of this review and also the questions listed below (I'm open to changing my mind if addressed).

- Clarify relevance of the consider model (see **Wicknesses** section above)
- Clarify connection to literature, especially Jain et al. (2024) "Scaling laws for learning with real and surrogate data" and Dohmatob et al. (2024) "Strong Model Collapse" (see **Wicknesses** section above)
- Can you instantiate your results on a concrete setup and show the corresponding scaling laws (perhaps with some approximations of Gaussian CDF) ?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Synthetic data has been used in training large language models, but concerns about its quality have emerged in practical applications. This paper works on data pruning to select high-quality data and analyzing the performance of trained on a mixture of real and synthetic data in a high-dimensional setting. The authors provide both theoretical and experimental results for the benefits of using and verifying synthetic data.

### Strengths
1. This work presents analysis and insights with theoretical justification. 
2. Through multiple tasks, the approach is shown its empirical effectiveness.

### Weaknesses
1. The paper lacks a clear definition of the quality of synthetic data. 
2. The derived theory in the paper is strongly assumed based on Gaussian distribution, however, non-Gaussian data are common in text or image data used for LLMs.
3. The paper only focuses on label verification for synthetic data. In real-world applications, synthetic data generation often struggles with feature fidelity, addressing feature consistency or the quality of synthetic data in feature space is more beneficial.

### Questions
1.Figure 1: $\hat{\eta}$ = 0.1, $p$ = 500, and $\hat{n}$ = 500, given that $\hat{\eta}$ = $\frac{p}{\hat{n}}$, is this a typo?              
2. Figure 3, in the figure of weak supervision, when the proportion of synthetic data is higher than 0.8, the performance increases, what is the reason for this? This trend is opposite to that when the proportion of synthetic data is lower than 0.8.  Similar observations also happen in Figure 6.      
3. Can authors explain why $\hat{\eta}$ can represent a distribution shift?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper extends important work by Feng et al. 24 and studies the effect of synthetesized data as part of the training data of models. It has two parts, a theoretical part that significantly extends the analysis of a mixture of two isotropic Gaussians from Feng et al. 24 from the case of infinite data at finite dimension to the case where both dimension and data tend to infinity with fixed ratio. Using tools from RMT they thus uncover a richer structure of transitions in a parameter space defined by the quality of synthetic data, the generator, label noise and verifier strength. A key novel element (which facilitates the analysis) is the assumption that the synthetic data comes from a model that estimates the mean and covariance matrix from initial (real) data (as opposed to a more general estimator). This allows to nicely study distribution shift of the features (not just the labels). Another extension over Feng et al.24 is the analysis of mixtures of real and synthetic data (though this is also done in "Strong Model Collapse" by Dohmatob et al., in a different and more general setting). 4 experiments nicely support the theory.

### Strengths
The paper lays out a coherent program and goes ahead to prove it with relatively sophisticated tools. The message is conveyed very clearly, the extensions over prior work, and in particular Feng et al 24 are clearly demarcated. 
The consequences of theorems are explained well, despite the necessarily heavy math. This paper thus provides further evidence to what was laid out in Feng et al 2024: synthetic data can only boost performance when coupled with verification (pruning).
The paper does a masterful job of presenting the results and the experiments are a nice addition. The paper is also well written and is fun to read.

### Weaknesses
The main weakness is that a few crucial references are missing. In particular there are three papers mixing real and synthetic data that should be cited, [1] and [2], and [3], a more recent one (there is no fault in not citing the latter, as it is recent, 
but the former date back over 8 months). In particular, a careful brief comparison to the [1] setting and results should be added, and [2] should be mentioned. Another paper that should be cited among the theoretical works for model collapse is [4]. On the other hand, 
your reference to [5] should probably be completely removed as it is misleading (the analysis of combination of real and synthetic data doesn't compare to adding the same amount of real data properly - this has been debunked on several occasions and should not be propagated).

Specifics (mostly minor):
1. line 252: typo "usefull"
2. line 402: "emphasize on" - sounds wrong, reformulate
3. line 406 use \citep for Malartic
4. line 408: "from the the Antropic's" --> "from Antropic's"
5. line 483-484: discuss Llama versus Gemma to make clear that you regard one as a weaker supervisor than the other
6. line 518: "Conclusionn" - typo
7. line 527-28: you might want to discuss that label pruning can induce a distribution shift in the features (because the pruning could be biased towards keeping certain features alive) - see (and cite) the discussion in Feng et al. 2024 (https://arxiv.org/pdf/2406.07515 version bottom of p. 10 - top p 11)

### Questions
1) How does your work compare to Jain et al. [1] specifically? (It’s a different data model, of course, but qualitatively, are there similarities/differences and how do the methods differ?)
2) I am confused about the "No supervision" case in Fig. 6 (the Amazon data). While in all other experiments more synthetic data doesn't help, here the U-shape of the curve stands out. Can you discuss a little more why in this case the red curve starts going up?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper builds upon Feng et al. that examined how using synthetic data with selection impacts final performance. Here, the authors extend that research to a setting that considers both distribution shifts in the feature space and the combination of real and synthetic data. This approach provides precise results without requiring an infinite number of synthetic samples. The experiments corroborate some theoretical insights.

### Strengths
1. The theoretical section is well-written, offering strong motivations and clear explanations.
2. Analyzing distribution shifts in the feature space is a valuable contribution compared with the previous work.
3. The paper provides a precise analysis of performance when training on mixed real and (selected) synthetic data with random matrix theory, expanding beyond previous work.

### Weaknesses
My primary concern is the applicability of the theoretical insights in practical settings. The theoretical predictions are based on binary Gaussian mixture data, with synthetic data generated by fitting another Gaussian mixture. While the authors provide performance predictions for models trained on mixed data, it is unclear how well these predictions, derived from Gaussian mixture models, will generalize to real-world data. Specifically, how can we estimate some of the key theoretical variables, such as the degree of feature distribution shift between real and synthetic data? How can we ensure that the supervision quality is sufficient to mitigate the negative effects of distribution shift, especially when this shift is not easily quantifiable? Furthermore, the paper does not provide clear guidance on how to measure or control the feature distribution shift in practical scenarios.

Currently, the experimental section could be improved by drawing more explicit connections to the theoretical insights. It is generally expected that better supervision and a more accurate generator would lead to improved performance with selected data. However, what practical insights does the theory provide? Can the theoretical findings be leveraged to inform the design of good data selection methods? For instance, the theory should provide guidance on how to choose the verification parameters $(\rho, \phi)$ given a specific feature distribution shift. The paper lacks a discussion on how to use the theoretical framework to optimize these parameters in practice. The experiment part is not well-written, with lots of details missing. I will elaborate more in the questions.

In Equation (2), the generative model assumes a prior with symmetric data sharing the same $\hat{\mu}$. How would the theory change if one Gaussian per class was fit instead? On line 129, label noise is introduced as purely random noise. What if the label error depended on the input? For instance, in safety applications, a generative model might introduce label errors in specific regions of the distribution due to bias. Could such input-dependent noise be analyzed? It would be helpful to discuss how label noise and feature noise correspond to various types of errors and shifts in real settings.

Missing details from the experiment:

What value of $\hat{n}$ is used across all experiments? The authors mention $\hat{n}$ varies in the MNIST experiment (line 400) but don’t provide further details. In the LLM Safety experiment (line 411), it is stated, "we focus only on label noise." However, since data is generated by another language model, feature noise is likely present. In Figure 7 (left), both feature noise and label noise should be included, as data are generated by a Gaussian fitted to the distribution. Could the authors provide error bars here? Given the simplicity of the MNIST setup with two-layer networks, this should be feasible. In Figure 8, why does using $(\rho, \phi) = (0.5, 0.5)$ as weak supervision? According to the definition in Equation (5), the data selection remains random regardless of label accuracy, which seems equivalent to no supervision. In the LLM Q&A Safety Generation experiment, is accuracy evaluated by the Llama-Guard-3.1 model? What weak supervision method is employed here? Why do the authors use two models to annotate labels? It would be helpful to include the evaluation results comparing the two labeling models with the “ground truth” from Llama-Guard-3.1 to assess the quality of synthetic labels. Additionally, how is supervised fine-tuning conducted with data containing both safe and unsafe answers?

My primary concern remains: could the author summarize the insights from this theoretical paper that could directly benefit practitioners? While I appreciate the theoretical contributions of this paper and understand that some results are derived under Gaussian data assumptions—which may approximate real high-dimensional data in certain cases—I feel the connection between theory and practical scenarios could be developed further. For example, the author states, "Our findings identify conditions where synthetic data could improve performance, focusing on the quality of the generative model and verification strategy." Could some of these conditions be verified in practice? Mixing real and synthetic data might lead to a U-shaped performance curve due to distribution shift. Could we predict whether such a U-shape would occur? Furthermore, with the random matrix analysis, what new insights are obtained compared to prior work by Feng et al. (2024)?

From my understanding, the theoretical framework in Feng et al. (2024) encompasses input-dependent errors, whereas the current setting considers only input-independent noise. While the author provides stronger theoretical results, this seems to narrow the scope compared to previous work. As the author notes, "Label noise can arise from misannotations or errors in the labeling process", if the synthetic data are annotated using the same pipeline as the real data, the noise levels should be similar. However, if synthetic labels are generated by another model, input-dependent errors would arise. In the experiments, the authors write, "We used two models to annotate labels to introduce variability and potential label noise," implying that the introduced noise should also be input-dependent. This limitation should be explicitly discussed.

In Figure 7 (left), both feature noise and label noise are included. However, the subtitles of the two plots are somewhat misleading. The right plot is labeled "Feature Noise," while the left plot is labeled "Label noise $\epsilon=0.3$." This gives the impression that there is no feature noise in the left plot, which is incorrect. I suggest the author revise the subtitles for clarity.

Could the author clarify the meaning of the proportion of synthetic data, which is used as the x-axis in all figures? Is it the proportion of synthetic data in the entire training set before verification and selection? The paper assumes knowledge of which data are synthetic and which are real and the verification apply only to the synthetic portion then. If so, different lines with varying verification methods but the same proportion of synthetic data involve different total amounts of data being used for training. Why not control for the total number of training samples in each case? Initially, I assumed that the proportion of synthetic data referred to the training set after verification. Under that assumption, $(\rho, \phi) = (0.5, 0.5)$ would correspond to no supervision, i.e., $(\rho, \phi) = (1, 1)$. Even if verification applies only to synthetic data, the "weak supervision" here is actually randomly using half the synthetic data. Why is this termed supervision? Isn't it simply a way of altering the ratio between real and synthetic data, given the assumed knowledge of data sources?

In the caption of Figure 3, the authors write "The parameter $\epsilon$ is variable depending on the proportion of synthetic data by taking it equal to the misclassification error corresponding to training a classifier on synthetic data only". What does it mean?

### Questions
1. In Equation (2), the generative model assumes a prior with symmetric data sharing the same $\hat{\mu}$. How would the theory change if one Gaussian per class was fit instead?
2. On line 129, label noise is introduced as purely random noise. What if the label error depended on the input? For instance, in safety applications, a generative model might introduce label errors in specific regions of the distribution due to bias. Could such input-dependent noise be analyzed?
3. It would be helpful to discuss how label noise and feature noise correspond to various types of errors and shifts in real settings.

Missing details from the experiment:

4. What value of $\hat{n}$ is used across all experiments? The authors mention $\hat{n}$ varies in the MNIST experiment (line 400) but don’t provide further details.
5. In the LLM Safety experiment (line 411), it is stated, "we focus only on label noise." However, since data is generated by another language model, feature noise is likely present. 
6. In Figure 7 (left), both feature noise and label noise should be included, as data are generated by a Gaussian fitted to the distribution. Could the authors provide error bars here? Given the simplicity of the MNIST setup with two-layer networks, this should be feasible.
7. In Figure 8, why does using $(\rho, \phi) = (0.5, 0.5)$ as weak supervision? According to the definition in Equation (5), the data selection remains random regardless of label accuracy, which seems equivalent to no supervision.
8. In the LLM Q&A Safety Generation experiment, is accuracy evaluated by the Llama-Guard-3.1 model? What weak supervision method is employed here? Why do the authors use two models to annotate labels? It would be helpful to include the evaluation results comparing the two labeling models with the “ground truth” from Llama-Guard-3.1 to assess the quality of synthetic labels. Additionally, how is supervised fine-tuning conducted with data containing both safe and unsafe answers?

### Soundness
3

### Presentation
2

### Contribution
2
