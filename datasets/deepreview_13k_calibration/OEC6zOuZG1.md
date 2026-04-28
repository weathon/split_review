# Random Features Outperform Linear Models: Effect of Strong Input-Label Correlation in Spiked Covariance Data

- Decision: Reject
- Avg Score: 4.83
- Scores: 3, 3, 6, 6, 5, 6

## Abstract
Random Feature Model (RFM) with a nonlinear activation function is instrumental in understanding training and generalization performance in high-dimensional learning. While existing research has established an asymptotic equivalence in performance between the RFM and noisy linear models under isotropic data assumptions, empirical observations indicate that the RFM frequently surpasses linear models in practical applications. To address this gap, we ask, \textit{"When and how does the RFM outperform linear models?"} In practice, inputs often have additional structures that significantly influence learning. Therefore, we explore the RFM under anisotropic input data characterized by spiked covariance in the proportional asymptotic limit, where dimensions diverge jointly while maintaining finite ratios. Our analysis reveals that a high correlation between inputs and labels is a critical factor enabling the RFM to outperform linear models. Moreover, we show that the RFM performs equivalent to noisy polynomial models, where the polynomial degree depends on the strength of the correlation between inputs and labels. Our numerical simulations validate these theoretical insights, confirming the performance-wise superiority of RFM in scenarios characterized by strong input-label correlation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work examines Random Feature Models (RFMs) under the assumption of spiked covariance for the input data. The authors establish a Gaussian Equivalence (GE) principle for the errors achieved by RFMs in this setting by revealing an equivalence with noisy polynomial equivalent models. When the alignment between the spike and the target is small, the classical GE principle holds, but for larger alignments, an extended version is required. The analysis is supported by numerical simulations that validate the theoretical findings.

### Strengths
The paper is nicely written and the authors provide a nice introduction to the related literature.

### Weaknesses
The main weakness for this work is the strong relationship with already publsihed works, namely [Moniri et al. 2024, Cui et al. 2024]. The authors overclaim the depth of their contribution in different parts of the manuscript.

My main concern for the present submission is the lack of clear elements of novelty that do not meet the high ICLR standards. 

As the auhtors correctly report, (Moniri et al. 2024) have already provided the rigorous Random Matrix Theory characterization when the spike appears in the weights of the Random Feature map. These results have been extended up to the maximal learning rate scaling regime by (Cui et al. 2024) which describes the emergence of a fully non-polynomial equivalent feature map in this regime. 

I fail to see notable differences between the setting of the present submission and the one in the above-mentioned works. 

In different parts of the manuscript, the authors significantly overclaim their contribution. For example, on page 5 "new universality theorem", "this result is notably more general than previous findings". Could the authors clarify what are the novel aspect in their contribution and distinguish them clearly from the results in (Moniri et al. 2024)?

### Questions
My main concern for the present submission is the lack of clear elements of novelty that do not meet the high ICLR standards. 

As the auhtors correctly report, (Moniri et al. 2024) have already provided the rigorous Random Matrix Theory characterization when the spike appears in the weights of the Random Feature map. These results have been extended up to the maximal learning rate scaling regime by (Cui et al. 2024) which describes the emergence of a fully non-polynomial equivalent feature map in this regime. 

I fail to see notable differences between the setting of the present submission and the one in the above-mentioned works. 

In different parts of the manuscript, the authors significantly overclaim their contribution. For example, on page 5 "new universality theorem", "this result is notably more general than previous findings". Could the authors clarify what are the novel aspect in their contribution and distinguish them clearly from the results in (Moniri et al. 2024)?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies a random features (RF) model trained using ridge regression on a data with a spiked covariance matrix where the covariance is aligned to the target function. Conditions under which such alignment break the gaussian university  (and hence, RF outperforms linear models) is studied.

### Strengths
- The paper is well written and well organized.

- Theorem 1 is something new and interesting. Although the proof technique is not novel, and is similar to the approach of Hu and Lu, the such universality across models is not something explicitly studied before (to the best of my knowledge). It can be of independent interest.

### Weaknesses
1- Although the analysis of RF models with a spiked covariance assumption for the covariates is new, unlike what is stated in line 143-144, it can still be seen as "feature-learning": One can think of spiked covariance as a model for feature learning in the first layers of a deep neural network where the second-to-last layer is random (i.e., the matrix F) and the last layer is trained with ridge regression (i.e., the vector \omega). In particular, the connections to the following papers should be discussed. These papers study layer-wise updates for a three-layer neural network.

- [R1] Eshaan Nichani, Alex Damian, Jason D. Lee, Provable Guarantees for Nonlinear Feature Learning in Three-Layer Neural Networks.

- [R2] Zihao Wang, Eshaan Nichani, Jason D Lee, Learning hierarchical polynomials with three-layer neural networks

2- Ba et al, (2023); Mousavi-Hosseini et al. (2023) study a problem similar to the one studied here, but for kernel ridge regression instead of random features regression. There needs to be a detailed comparison of the results presented here to the results of these two papers

3- What happens when we set \beta = 1/2 in Assumption A.2? Also, as the paper studies squared losses, there is probably no need to make the odd activation function assumption (A.6); there can be a easier direct proof of universality using Lindeberg exchange without the need to use the results of Hu & Lu.

4- A precise characterization of the training/test errors will improve the quality of this work significantly.

### Questions
Please see the weakness section.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studied whether, and if so under what conditions, the performance of the random feature method (RFM) is better than that of a 
 simpler linear model. The authors considered the spiked covariance data model, where the anisotropic characteristics of $x$ relax the previous work based on a more restrictive isotropic data assumption, thereby broadening the applicability of their established results. One important discovery in this paper is that in the case of a strong correlation between inputs and labels, the RFM outperforms the linear model in the sense that the latter has worse generalization performance.

### Strengths
This paper solidly verified an interesting phenomenon within the framework of the random feature model that the performance of a learning algorithm has essential dependence on the input or the input-label correlation.  I find it interesting that in the case of a strong correlation between inputs and labels, the RFM outperforms the linear model.

### Weaknesses
 **Writing:**

 I strongly suggest that the authors include some definitions, symbols, and notations (e.g. the training and generalization errors) in the main text so that the paper can be easily followed. I think that there is significant room for improvement in the paper's arrangement.

**Typographical remarks:**

The first expectation in Eq.(10) should not be taken over $(x,y)$ since the quantity involved does not contain $y$.  Some similar concerns also appear elsewhere.

### Questions
I am a bit confused about why the RFM outperforms the linear model in mathematical expression. Could the authors provide a clear comparison of their learning rates in the presence of strong input-label correlation?

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper targets to address the question of "When and how does the RFM outperform linear models?". To this end, the paper considers the setting where the data are distributed according to a spike covariance model, which is more general than the isotropic setting existing analyses based on. The author(s) show that RFM can outperform linear models when there is a high correlation between inputs and labels. They also show that RFM is equivalent to noisy polynomial models, where the polynomial degree depends on the input-output correlations.

### Strengths
- The paper is clearly written and motivated
- The topic of study is important, since RFMs are closely related to other machine learning models like neural networks. 
- The work extents existing studies by performing analysis on a more general data distribution, which is a step toward more general analysis.
- The theoretical analysis is derived in detail.
- The theoretical analysis is verified with numerical experiments

### Weaknesses
 - Is it unclear how realistic the assumptions in p.4 are. It would be helpful to verify them using real data and compare the assumptions with the ones used in related analyses
- It seems that every single equation in the paper is numbered. It would be more readable to remove the numbers of the unreferenced equations.

### Questions
- How realistic is the spike covariance model? Are there any datasets that (approximately) follow such distribution?
- For the assumptions (equation 10) and (equation 11), do existing datasets satisfy them? If so, is there any references or empirical plots? Also, how does these assumptions compared to those of Hu and Lu (2023)'s?
- In (10), is the equation independent of y?
- It is stated in the literature review that RFMs are used in explaining the double descent phenomenon. Can this study on generalization performance provide information about the double descent phenomenon for data drawn from the spike covariance model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the conditions when and how random feature models (RFM) outperform linear models, focusing on the anisotropic conditions with spiked covariance data with strong input-label correlations. Specifically, they prove that RFM performs equivalent to noisy polynomial models with polynomial degrees influenced by input-label correlation. Numerical simulations are conducted to validate the theoretical results.

### Strengths
1. This paper looks good and well-written. Random features model and its connection to neural networks is of interest in machine learning theory.
2. The main contribution is its theoretical aspect, which extends the previous work in [1] to the anisotropic data structure. The universality theorem extends the understanding of RFMs, demonstrating their performance across different activation functions.
3.  Authors suggest that exploiting the non-linearities of RFMs could lead to significant performance gains in high correlation scenarios, which is interesting and confirms practitioners’ intuition.

### Weaknesses
1. **Assumptions**: The author only discusses these assumptions from a technical or the math proof aspect, the practical aspects and their limitations should be clarified. And it seems hard to verify these assumptions in practice. Specifically, the spiked covariance model, while capturing some aspects of real-world data, is a strong assumption that needs further justification. The paper should discuss the sensitivity of the results to deviations from this specific covariance structure. For instance, how would the performance of RFMs be affected if the data exhibited a more complex, multi-modal structure or if the low-rank component was not strictly rank-one? Furthermore, the assumption of strong input-label correlations, while theoretically interesting, needs more discussion about how to measure or identify such correlations in real-world datasets and what the implications are if this assumption is violated.
2. **Comparisons with previous work**:  The comparison with previous work is not enough, the proof technique in this paper is based on [1], and more comparisons and detailed differences should be remarked in the paper. The paper should explicitly highlight the novel aspects of the proof technique compared to [1], beyond just the change in data assumptions. For example, what specific mathematical tools or arguments are introduced to handle the anisotropic data structure that were not present in the original work? A more detailed comparison of the mathematical derivations would be beneficial.
3.  **Limited experiments**:  While the focus of this paper is theory, the experiments in this paper are not adequate, only evaluated in some simulated data, while the real data application with unknown data structure is missing. The detailed setup of the experiment is not clearly presented in this paper, which should be put in a separate section. The experiments should include a more thorough analysis of the parameter sensitivity, such as the impact of the random feature dimension and the choice of activation function. The current experiments only validate the theoretical results under specific conditions, but do not explore the robustness of the findings. Furthermore, the paper should include a discussion of the computational cost of the experiments and how it scales with the dimensionality of the data and the number of random features.
3.  **Scope of Application**: While detailed, the focus is specifically on spiked covariance data, which may not generalize to all data structures and might not hold in all real-world scenarios. The paper should acknowledge the limitations of the spiked covariance model and discuss potential avenues for future research that could extend the results to more general data distributions. It would be beneficial to include a discussion on the types of real-world scenarios where the spiked covariance model is likely to be a good approximation and where it might fail.

### Questions
1. While the authors say *"it is noteworthy that while ReLU (9) does not conform to the odd function assumptions stipulated in(A.6)"* in line 208, the simulation uses ReLU as an activation function and gets good results, can you explain it more intuitively?
2. The alignment parameter $\alpha$ seems to be a simple multiplication of two parameters in the structure of x and y, what is the real meaning of the input-label correlation in practice?
3. The main theorem in this paper is only an asymptotic results, i.e., equation (56), can you provide some non-asymptotic results such as the converge speed between the corresponding generalization errors $G_{\sigma}$ and $G_{\hat{\sigma}}$? 
4. While this paper is the extension to [1], and [1] considers a general loss function, can the framework from square loss extend to a general loss?

[1]  *Universality Laws for High-Dimensional Learning with Random Features*. (2023), Hu and Lu, TIT.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper examines the performance of random feature models (RFMs) with anisotropic input data, characterised by spiked covariance. Whilst RFMs and linear models are asymptotically equivalent for isotropic data, RFMs tend to perform better in practical applications – an observation that the authors put down to the structured, anisotropic nature of real world data. They establish a ‘universality theorem’, extending the work of Hu and Lu (2023) to prove that there exists two different activation functions with equivalent performances if the first two statistical moments of $\sigma(\mathbf{F} \mathbf{x},y)$ match. They use this result to show that higher-order polynomial models are equivalent to RFMs for spiked covariance data, and show that in particular limits for this data linear models become sufficient (roughly, when input correlations and covariance spiking becomes small). Input-label correlation is found to be crucial in determining whether RFMs outperform linear models. The authors provide detailed theoretical guarantees and experimental validation on synthetic data.

### Strengths
The paper makes solid technical contributions, making a careful detailed case that, for spiked covariance data (Eq. 6), RFMs will perform better except when the spike magnitude, alignment parameter, or cosine similarity between the rows of $\mathbf{F}$ and $\gamma$ are sufficiently small (how should I interpret the last condition?). It provides a nice extension to the work of Hu (2023) beyond the linear regime, and it seems possible that this type of data structure/anisotropy might be responsible for the superior performance of RFMs in the wild. The experiments (especially, measuring generalisation error vs. number of samples, alignment and spike magnitude for different models in Fig. 3) appear to back up the authors’ central claims.

### Weaknesses
1. *Applicability to real-world data.* The paper provides a detailed analysis of the performance of random feature models (RFMs) with anisotropic input data characterized by spiked covariance, as defined in Eq. 6. However, the practical relevance of this specific parameterization to real-world datasets remains unclear. While the theoretical analysis is valuable, demonstrating that similar behavior holds on real-world data would significantly strengthen the paper's impact. For instance, the authors could evaluate the performance of polynomial kernels on a real dataset, ablating over different $l$ and observing when performance approaches that of RFMs. Furthermore, it would be beneficial to investigate whether any properties of real-world distributions roughly correspond to $\theta$ and $\alpha$, spike magnitude, and alignment. Exploring the performance gap between RFMs and linear models on datasets with varying degrees of these properties could provide valuable insights. Additionally, the paper could benefit from a more in-depth discussion of the relationship between the presented work and the phenomenon of double descent, beyond the empirical observations around line 490. Similarly, exploring the potential connection to feature learning in neural networks could further contextualize the findings within the broader machine learning literature.
2. *Other points.*
- *Thm 1*. The claim that Theorem 1 represents a "key advancement" (line 263) seems overstated. While the theorem establishes an equivalence between activation functions under matched statistical moments, it is based on the understanding that the Hermite basis is complete. Given suitable asymptotic conditions to bound higher-order terms, it is not entirely surprising that considering only the first two terms becomes sufficient. This aspect could be rephrased to better position the theorem's contribution within the broader context of the paper.
- *Assumption 7*. Assumption A.7, which ensures the convexity of the perturbed objective (line 742), appears crucial for the validity of Theorem 1 and subsequent claims about generalization error. However, its practical implications and whether it holds in real-world scenarios are not thoroughly discussed. Given its importance, it would be beneficial to include this assumption in the main text and investigate its validity in the experimental section.
- *Odd activation functions*. The paper assumes odd activation functions (Assumption A.6), but the empirical validation includes non-odd functions like ReLU. It would be helpful to clarify where the theoretical arguments break down for non-odd activation functions and why the proof only holds for odd functions. Additionally, since the proof relies on this assumption, it would be valuable to include odd activation functions, such as tanh, in Figure 3 to assess their performance.

### Questions
1. To what extent would these findings generalise to other anisotropic data settings, and to what extent are they expected to be particular to the spiked covariance model?
2. Are there any practical implications from this work for model selection, given access to a labelled dataset? 
3. Given the odd activation function assumption (A.6), do the authors see any empirical difference in results depending on the parity of $\sigma$? As mentioned above, including $\tanh$ in Fig. 3 might help answer this question.

I sincerely thank the authors for their time and efforts. It’s great to see such detailed, careful mathematical work, which is sometimes lacking in the field! If they can convince me of the broader applicability of their findings (especially, relating to real-world datasets) and clarify assumption A.7 I will be happy to raise my score.

### Soundness
3

### Presentation
2

### Contribution
2
