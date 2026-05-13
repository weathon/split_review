# Disentangled interleaving variational encoding

- Decision: Reject
- Scores: 3, 3, 6, 3

## Abstract
Conflicting objectives present a considerable challenge in interleaving multi-task learning, necessitating the need for meticulous design and balance to ensure effective learning of a representative latent data space across all tasks without mutual negative impact. Drawing inspiration from the concept of marginal and conditional probability distributions in probability theory, we design a principled and well-founded approach to disentangle the original input into marginal and conditional probability distributions in the latent space of a variational autoencoder. Our proposed model, Deep Disentangled Interleaving Variational Encoding (DeepDIVE) learns disentangled features from the original input to form clusters in the embedding space and unifies these features via the cross-attention mechanism in the fusion stage. We theoretically prove that combining the objectives for reconstruction and forecasting fully captures the lower bound and mathematically derive a loss function for disentanglement using Naïve Bayes. Under the assumption that the prior is a mixture of log-concave distributions, we also establish that the Kullback-Leibler divergence between the prior and the posterior is upper bounded by the cross entropy loss, informing our adoption of radial basis functions (RBF) and cross entropy with interleaving training for DeepDIVE to provide a justified basis for convergence. Experiments on anonymous bidding data from the National Electricity Market of Singapore (NEMS) show that DeepDIVE disentangles the original input and yields more accurate forecasts, outperforming current state-of-the-art baselines. In the context of the power market, this study can enhance operational decisions and bidding strategies by offering insights into the embedded supply curve via the representation space.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel framework for enhancing the interpretability of representations learned from time-series prediction. The authors derive a variational evidence lower bound (ELBO) that extends the original VAE's ELBO to accommodate time-series forecasting scenarios, along with theoretical and implementation details for optimizing this learning objective. Specifically, the latent space is designed into separate marginal (denoted by "b") and conditional (denoted by "a") distributions that contribute to the calculation of the log-likelihood of both the look-back window and the forecasting window. Experiments are conducted on two time-series datasets, and both qualitative visualizations and quantitative metrics are evaluated for the proposed method.

### Strengths
(1) The detailed theoretical derivations of the proposed ELBO for time-series forecasting are solid and make sense, and it could be promising and inspiring for future research on learning disentangled representations in time-series prediction tasks. 

(2) I appreciate the authors' efforts to report the variance (standard deviation) of the model's performance, which allows readers to better evaluate the results and comparisons.

### Weaknesses
The main weakness of this paper lies in its writing and evaluations.

(1) The writing lacks consistency between the text, figures, and equations. For example: (1a) While the inference and KL divergence for q(b∣x) is well-discussed, I had difficulties to find any description for inferring q(a∣x,b). In Fig. 1, it appears that a is directly computed from x, which contradicts the equation, and I couldn't find any other text to explain this. Specifically, the relationship between the frozen weights during backpropagation and the conditioning of 'a' on 'b' is not clearly articulated. The interleaving training scheme, while mentioned, lacks a detailed explanation of how it achieves the decoupling of marginal and conditional latent dimensions. (1b) Although the "cross-attention mechanism" and "fusion stage" are mentioned in the abstract and introduction as part of this paper's contributions, they are never described or explained in the rest of this paper. It appears that the proposed framework is implemented just using an auto-encoder architecture, as suggested by Fig. 1 and line 412. The exact implementation of the fusion stage, particularly how cross-attention is applied to combine the outputs of the RBF layer with the conditional dimensions, is missing. Additionally, in line 518, the authors state, "Unlike attention maps and convolutional neural network (CNN) feature maps, DeepDIVE presents data representations in ...," which further increases the confusion about whether the proposed framework includes cross-attention. The role of cross-attention in the decoder, and how it differs from typical attention map visualizations, needs clarification. (1c) There are no descriptions or explanations in the main text for Fig. 3, and the figure caption is also limited. The connection between the density plot in Figure 3 and the scatter plot in Figure 2 is not explicitly stated, making it difficult to understand the purpose of Figure 3.

(2) Although the combined effects of a and b in the latent space are evaluated in Fig. 2, separate evaluations and comparisons of a and b are missing, which I believe is critical for evaluating the proposed framework. Readers may be interested in understanding the differences between the representations learned in a and b, and how using separate a and b is beneficial compared to using just one latent variable. The authors are encouraged to conduct comprehensive experiments to demonstrate the representations learned in the marginal and conditional distributions in the latent space, separately, and how they impact the final prediction tasks. For example, the authors could consider using t-SNE plots for a and b individually and presenting traversal results for both of them to identify any expected differences.

### Questions
(1) Total correlation is also an option for promoting the independence of the latent variables. Besides using Naive Bayes, do the authors have any experience or insights in deriving and optimizing total correlation terms within the KL divergence? Additionally, how would this affect the model performance compared to using Naive Bayes? For instance, one approach for optimizing total correlation can be found in [1].

[1] Chen, Ricky TQ, et al. "Isolating sources of disentanglement in variational autoencoders." Advances in neural information processing systems 31 (2018).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors propose to extend the use of Variational Autoencoders to generative forecasting and develop a novel objective for training.

### Strengths
- The loss function seems to be novel and theoretically grounded.

### Weaknesses
 - Presentation: The paper is not well-written, it is difficult to follow and understand the idea.
    - The abstract is not specific. Multiple concepts such as multi-task learning, disentanglement, Naive Bayes, and other technical details are presented without a clear, coherent relationship among them. I suggest focusing on a central contribution, such as developing a non-conflicting objective for multi-task learning, and clarifying how elements like disentanglement, Naive Bayes, cross-entropy, and RBF specifically contribute to this goal.
    - Line 46 of the introduction states model explainability to be the key contribution. However, the abstract does not discuss about explainability. I suggest emphasizing a central contribution and ensuring that all concepts throughout the paper align with it.
    -  Line 50 of the introduction mentions conflicting objectives, but a more detailed discussion of how multiple objectives in multi-task learning may conflict and providing examples of these conflicting objectives in the context of the paper would make this concept clearer.
- Baselines: No discussion or reference of the comparison baselines in Table 2 are AUTOCTS(-KDF/KDP), DsaNet, and MtGnn provided. Could the authors provide a brief discussion on these baselines and why they were considered for comparison? Also, why were more recent baselines such as DeepGLO, TCN, and TLAE (as discussed in section 2.1) not included in the comparison?

- The introduction has improved. However, the discussion of previous works, their limitations, and the broader context remains inadequate. I recommend expanding the first paragraph to give more context.


- The first few sentences in the abstract lack coherence. While the opening sentence discusses the effective learning of a representative latent data space, the second jumps to describing the proposed disentanglement approach. To enhance cohesion, I suggest briefly explaining how disentanglement contributes to learning an effective latent space, as this appears to be the paper’s primary contribution.

- >**Abstract: "We theoretically prove that combining the objectives for reconstruction and forecasting fully captures the lower bound and mathematically derive a loss function for disentanglement using Naive Bayes."**
    - The terms "Reconstruction and forecasting" are unclear as they have not been defined. It's better to write them as "combining multiple objectives".

- No baselines from tables 1,2 and 3 are discussed in the "Related works" section.

### Questions
- I couldn't find the paper referenced in section 2 (Wong et. al.). Is it published yet? Could the authors provide a link to the paper?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Deep-DIVE, a framework to learn disentangled features from the original input to form clusters in the embedding space and unify the classified features via the cross-attention mechanism. Experimental results on time series forecasting showcase that the proposed framework could disentangle the features and provide better forecasts than existing methods.

### Strengths
1. The paper is clearly written, easy to follow and understand.
2. Experiments compared with other baselines showcase that the proposed Deep-DIVE framework achieves better performance than existing baselines.
3. In terms of novelty, the DeepDIVE framework proposed in this work decomposes the latent space z into two distinct dimensions: marginal dimensions b and conditional dimensions a. The marginal dimensions b capture general trends and are independent of each other, while the conditional dimensions a are conditioned on b. This design enables b to capture shared patterns across conflicting tasks, while a learns task-specific features to avoid conflicts. Compared with existing methods, this approach better addresses the challenge of using a single variational encoding to model conflicting time series, resulting in improved performance and disentanglement.

### Weaknesses
1. In the introduction section, the author motivates the proposed Deep-DIVE framework by criticizing existing deep learning approaches for time series forecasting as being black-box in nature and hard to optimize. However, time series forecasting (TSF) is a well-established problem. The author should provide further explanation to better justify why the proposed framework is helpful in TSF.

2. The assumption 2 that $q_{\phi}(b_i,b_j|x) = q_{\phi}(b_i|x)q_{\phi}(b_j|x)$ for any i and j is too strong. Although I understand the author's remark that this simplifying assumption often works well in practice, some explanation or intuition about why it often works would be helpful.

### Questions
In the experiment results in section 5, Table 2, what does 'std' mean?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes the new VAE architecture that has a special latent variable structure for time series forecasting.
This paper assumes that the target variable of VAE is a combination of future and past variables, 
and that the future variables do not depend on the latent variables, but only on the past variables.
The latent variables also consist of two vectors $a$ and $b$, and the posterior distribution of $a$ depends on $b$, but that of $b$ is independent of $a$.
Furthermore, it is assumed that $b$ consists of a mixture model of K classes. Finally, the likelihood function obtained under these assumptions is the proposed objective function.
In the experiment, the forecasting accuracy is compared using two time series datasets, and the visualization of the latent variable is discussed.

### Strengths
- The proposed method is well explained using mathematical equations. 
The expansion of equations is easy to understand, and the assumptions necessary for the expansions are also clearly stated. 
However, as written in Weakness, the practical validity and motivation of the assumptions are unclear.
- In the experiments, the forecasting accuracy is higher than that of VAE and beta VAE on one dataset. 
However, if you only focus on the forecasting accuracy, it is difficult to say that VAE and beta VAE are appropriate baselines.
If the paper is a study of application, it should be compared with baselines for time series forecasting.
On the other dataset, baseline methods seem to be forecasting methods, but the proposed method does not necessarily outperform these baselines.

### Weaknesses
 - This paper does not succeed in positioning itself in the context of previous research. 
I strongly suggest that this paper should clarify whether the focus of the paper is a proposal of a method for a specific application or one of a fundamental method. The abstract seems to state that the paper solves a problem in general multi-task learning, but the introduction seems to claim that it is a technique for solving the problem of time series (or ASC?) forecasting. It is inconsistent and makes the motivation unclear. The paper needs to consistently state the research problem and clearly explain why the proposed method is effective for that problem. If this paper solves a specific problem in time series forecasting, it should justify why that problem is important and common to broad domains.

- Related to the above, it is difficult to understand the reasons and principles behind the design of the proposed method. Although the assumptions that lead to the theorem are shown, this paper does not mention the assumptions of the target tasks or the most suitable use cases of the proposed method. As a result, it is difficult to discuss the generality and importance of the task being solved by the proposed method, and the impact of this paper is unclear. The graphical models of a, b, x, and y might be useful for readers to understand the assumptions, 
and illustrations of how these variables relate to practical tasks will also help readers understand the effectiveness of the proposed method.

- The paper evaluates the visualization of latent variables but does not compare it with existing methods. I think that disentanglement of latent variables in time-series data have already been discussed in previous research such as [a]. If the claim of this paper is the importance of disentangling latent variables, the proposed method should be compared with previous methods.

- The baseline is not consistent in the evaluation on the two datasets. Why are the baselines different in Table 1 and Table 2? Is it appropriate to compare VAE and beta VAE using time series data sets?

### Questions
If I have misunderstood the paper, please point out it.

### Soundness
2

### Presentation
1

### Contribution
2
