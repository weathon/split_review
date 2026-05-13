# Optimal criterion for feature learning of two-layer linear neural network in high dimensional interpolation regime

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
Deep neural networks with feature learning have shown surprising generalization performance in high dimensional settings, but it has not been fully understood how and when they enjoy the benefit of feature learning. In this paper, we theoretically analyze the statistical properties of the benefits from feature learning in a two-layer linear neural network with multiple outputs in a high-dimensional setting. For that purpose, we propose a new criterion that allows feature learning of a two-layer linear neural network in a high-dimensional setting. Interestingly, we can show that models with smaller values of the criterion generalize even in situations where normal ridge regression fails to generalize. This is because the proposed criterion contains a proper regularization for the feature mapping and acts as an upper bound on the predictive risk. As an important characterization of the criterion, the two-layer linear neural network that minimizes this criterion can achieve the optimal Bayes risk that is determined by the distribution of the true signals across the multiple outputs. To the best of our knowledge, this is the first study to specifically identify the conditions under which a model obtained by proper feature learning can outperform normal ridge regression in a high-dimensional multiple-output linear regression problem.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies two layer linear neural networks with multiple outputs. The authors propose a penalty term (regularization) and add it to their least squares optimization problem. This penalty term is effective because it enables "feature learning" They analyze the estimator in the high-dimensional regime and show that in some scenarios, it can outperform ridge regression.

### Strengths
- Feature learning is a very important problem and is attracting a lot of attention from the deep learning theory community. The problem is very well motivated.

- The penalty term introduced is related to the classic Millow's $C_p$ and WAIC. The properties of these criteria were already studied in the classic statistical setting where dimension is fixed and the number of samples is large. The authors analyze these in the high-dimensional regime. This is interesting on its own.

- The paper is solid, the proofs seem to be correct, and the paper is well written in general.

### Weaknesses
 * The authors argue that the proposed method can beat ridge regression. However, how does it compare to ridge regression with optimally tuned regularization? For example, in figure 1, "Normal Ridge" corresponds to ridge regression with $\lambda = 1/n$ which is not the optimally tuned. More importantly, the authors consider a case where the $\beta$s are not isotropic. In that case, one might try to look at the optimization problem $\hat\beta_{\Omega} = \min_{\beta}||y - X \beta||_2^2 + ||\Omega \beta||_2^2$ where $\Omega$ is a $d\times d$ matrix. Then, try to tune $\Omega$ optimally (similar to Wu and Xu 2020). One can also use the min-norm interpolation version of this that was studied in (Sun et al., 2022), section 2.2.


  Yue Sun, Adhyyan Narang, Halil Ibrahim Gulluk, Samet Oymak, Maryam Fazel. Towards Sample-efficient Overparameterized Meta-learning, NeurIPS 2022.

 For example, setting $\Omega \asymp \Sigma_\beta^{-1}$ can exactly give the Bayes optimal in Proposition 1. It is also doing the feature learning because it regularizes the dimensions with small signal power more that the directions with strong signal. What is the benefit of the method proposed by the authors to this? How do they compare? What are the benefits?


* Right before section 2, it is mentioned that (Ba et al., 2022) studies the problem in the setting where $n\geq d$. Is this true? They consider the regime where $d$ and $n$ are in the same order but $d$ can be large or smaller than $n$. How does the results in this paper compare to the results of (Ba et al., 2022) with $O(\sqrt{n})$ gradient step size?

* How does the proposed method compare to sketched linear regression? See e.g. (Chen et al., 2023).

Xin Chen, Yicheng Zeng, Siyue Yang, Qiang Sun. Sketched ridgeless linear regression: The role of downsampling, 2023.

### Questions
Please see above.

### Soundness
4 excellent

### Presentation
4 excellent

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
In this paper, the primary objective of the authors is to understand how and why a linear two-layer neural network outperforms classical ridge regression in a multivariate output regression problem, thereby illustrating how, why and when proper feature feature learning can benefit the learning. To that end, the authors propose an optimal regularization for training a two-layer linear neural network. This loss incorporates a regularization term inspired by the Widely Applicable Information Criterion (WAIC). The authors show that this loss represents an upper bound for the predictive regression error. Moreover, the authors show that the upper bound can reach a lower bound using Bayes optimal risk. The authors compare ridge regression with the proposed optimal regularization, highlighting a set of cases and examples where optimal regularization yields better results, showing when good regularization leads to greater learning.

### Strengths
1- The purpose of the paper is quite important. Explaining theoretically why a neural network is able to outperform classical linear models through efficient feature learning is an interesting problem even in the simple framework of a linear two-layer network.

2- The proof that the proposed regularization allows us to obtain the lower bound given by the optimal Bayes is also interesting since it justifies the optimality of the approach showing that the approach allows us to obtain the best performance in this class of functions of linear two-layer networks. In addition, the comparison with ridge regression and the illustration of specific cases where feature learning can dominate a non feature learning approach is also interesting.

3- Even though few experiments have been carried out, they tend to suggest that regularization does in fact enable good performance to be achieved compared with conventional ridge regression.

### Weaknesses
1- The methodology and design of regularization in neural networks seem arbitrary. They suggest that the regularization used in previous cases is applied to neural networks, and by chance, it provides an upper bound of the true risk and constitutes a lower bound. The author postulates that this type of regularization appears implicitly in neural networks. The question is why this regularization is exploited by neural networks and not another that would also allow reaching the Bayes risk. For example, in recursive feature machines where authors apply an optimal feature learning step and a ridge regression step, one could expect results that reach the lower bound. One could say that it is possible to look for regularization that already exists in the literature or create new ones that will also show that it is an upper bound of the predictive loss and lead to a lower bound of the Bayes risk. But how can we ensure that the regularization proposed by the authors is unique and actually the one implicitly used by linear two-layer Neural Network? Otherwise, it is possible to write a lot of studies with different regularizations. The only thing we seem to be sure of is that ridge regression is not optimal.

2- Along the same lines, one could ask whether this regularization is not optimal in the restricted setting considered by the authors (hypothesis on the data, generative model considered for the data, zero mean data, etc.). In a neural network study, one would expect to study the learning dynamics that naturally bring out the learning model and the implicit regularization that could also depend on the type of data and not be generic. And probably not the reverse: propose an arbitrary regularization and showing by its properties (lower bound of Bayes risk, upper bound of predictive risk) that it is the actual regularization achieved by linear neural network.

3- Even though the theoretical contributions are important, it would have been interesting to illustrate the theoretical conclusions a bit more. In particular, it would have been interesting to compare the W learned by a linear NN network (without the regularization proposed (by a gradient descent method, for example)) and compare it to that obtained by regularization. This could represent an empirical argument that the actual learning process follows that of the proposed regularization. It would also be interesting to test the robustness of the conclusions on real data to see how dependent they are on the model considered and not obsolete for real data.

### Questions
1- The sentence: "This is because there is a difficulty in feature learning ..." in the introduction seems not to be understandable, at least to me.

2- I think the main question in the introduction is a bit confusing: "Can we design an optimal regularisation...". I think this question is interesting, but maybe it's not related to the learning process in real NN. At least, even if implicit regularisation doesn't explain all the phenomena, it is implicitly given by the learning process and the dynamics of learning. Also, this question seems a bit challenging and too broad as I would expect this regularisation term to depend on the data modelling under consideration.

3- I think some explanations would have been welcome for assumption 1. Why do you consider putting the sub-Gaussianity assumption on the rows of $X\Sigma_x^{-1/2}$ and not on the rows of $X$?

4- The explanation at the end of page 4 and the beginning of page 5 is confusing to me. A lot of information is given, sometimes without any link, and some terms are not explained. In particular, several topics are mentioned in the same paragraph which are not related to each other (decay of eigenvalues for benign overfitting, high dimensional regime considered for $d, n$, ...). Furthermore, the kernel regime is not defined.

5- In numerical experiments, it would have been fairer to tune the regularization parameter for ridge regression and take the best one. What if the poor performance of ridge is only due to a bad choice of the regularization parameter?  It would have been interesting to add the important baseline that would train a linear neural network as usual on the synthetic data and also some real data, at least to show the robustness of the approach with respect to the data distribution and the model considered.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors consider a two-layer linear network for multivariate regression. They introduce an upper bound on the standard MMSE loss, which they treat as a surrogate minimization objective for minimizing the predictive loss. They provide a thorough analysis of this bound and show that if the true regression coefficients are misaligned with the data, then a two-layer network trained using the upper bound as a loss function, outperforms ridge regression and closely matches they Bayes optimal estimator. They also provide experiments corroborating their theoretical results.

### Strengths
- Introduction of an upper bound obtained by adding a regularization term (degrees of freedom), which has previously been used in the setting where the number of samples is much larger than the dimension.
- Theoretical analysis of the proposed upper bound and the neural network trained on it, which provides insight as to how/why it works
- Characterization of a regime in which the network outperforms ridge regression and closely matches Bayes-optimal performance
- Clear presentation of the results

### Weaknesses
 - Since the bounds in the theorems only hold up to a constant, they only give quantitative results if the misalignment is strong enough for the corresponding bound to be of vanishing order. This is a significant limitation because it means the theoretical analysis does not provide precise predictions for the performance of the network in practical scenarios where the misalignment may not be extreme. The lack of precise constants makes it difficult to determine the exact conditions under which the proposed method will outperform ridge regression in real-world applications. The theoretical results are thus more qualitative than quantitative.


### Questions
- The theoretical results give sufficient conditions for the superior performance of the network over ridge regression. Do you believe these conditions are also necessary and did you try any numerical experiments in that direction?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper considers solving multi-output linear regression with two-layer linear networks. First, the authors construct $R(W)$ which serves as an (asymptotic) upper bound of the predictive risk. Next, they further bound $R(W)$ by a quantity $U_\text{NN}$ which depends on the eigenvalues of $\Sigma_\beta^\frac{1}{2} \Sigma_x \Sigma_\beta^\frac{1}{2}$. Then, it is argued that the Bayes risk can be lower bounded by the same expression. Under certain conditions, it is shown that the two-layer linear neworks obtained by minimizing $R(W)$ can outperform standard ridge regression. Results are supported by an experiment on synthetic data.

### Strengths
- Results are sound and fully justified.

- Implication of the main results are well explained.

- Comprehensive case study is provided.

### Weaknesses
- There are many additional assumptions stated inside the theorems: "for all $W$ which satisfies $R(W) - \sigma^2 \leq$..."(Theorem 1), "there exists $k\leq n$ such that .." (Theorem 2), "the rows of $X W_B^\top U_B$ are independent" (Theorem 3), "the condition number of $A_k$.." (Corollary 1). To me, the assumptions looked very artificial, and it was hard to see why it is reasonable to assume those. It would strengthen the paper if the authors could state all necessary assumptions separately before stating the theorems. For instance, the assumption in Theorem 1 implicitly restricts the scope to parameters minimizing the predictive error, which should be clarified. Similarly, the condition on the existence of 'k' in Theorem 2, related to the decay of eigenvalues of $\Sigma_\beta^{\frac{1}{2}} \Sigma_x \Sigma_\beta^{\frac{1}{2}}$, needs further justification in terms of its practical implications. Without this, it is hard to judge how non-trivial the results are.

- Although the authors have provided Example 1--4 to show the advantage of using $R(W)$ over ridge regression, the settings seem very artificial and restrictive. For instance, the specific choices made in constructing these examples are not adequately justified in terms of their relevance to real-world scenarios. The examples, as presented, do not sufficiently demonstrate the practical applicability or superiority of the proposed method over ridge regression in a general setting. I wouldn't be too surprised even if there exists a pathological setting where standard ridge regression does not generalize well and there is a quick fix for it.

- This happens again in the experiment; the authors choose a very specific parameters and argue that the proposed method improves over ridge regression. The choice of $\lambda = \frac{1}{n}$ for the ridge parameter, in particular, seems arbitrary without a clear theoretical or empirical justification. I would be interested to see further justification for considering such setting. A more thorough exploration of the parameter space, potentially through cross-validation or a sensitivity analysis, would provide a more convincing demonstration of the proposed method's effectiveness.

**Minor points**

- Theorems are hard to parse. It would be better if the authors can simplify the statement using $o(\cdot), O(\cdot)$ notation. For example, in Theorem 1, many unnecessary constants are displayed, making it hard to see why it holds with a vanishing probability.

- The authors should used a different notation for $V$ in Theorem 2 as $V$ is already used for the variance term.

### Questions
- What happens in the experiment if we use other stochastic gradient descent algorithms (SGD, Adam, etc.) instead of the Langevin dynamics? Other algorithms are also capable of escaping local minima.

- What is the justification for using $\lambda = \frac{1}{n}$ in the experiment? What happens if we optimally tune the ridge parameter?

- As mentioned above, it is hard to judge how restrictive the assumptions are and how often the suggested method improves over ridge regression. Therefore, I would like to see some experiments with real-world data.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
