# Meta-learning Representations for Learning from Multiple Annotators

- Decision: Reject
- Scores: 6, 3, 5, 6

## Abstract
We propose a meta-learning method for learning from multiple noisy annotators. In many applications such as crowdsourcing services,
labels for supervised learning are given by multiple annotators. Since the annotators have different skills or biases, given labels can be noisy. To learn accurate classifiers, existing methods require many annotated data to deal with noisy labels. However, sufficient data might be unavailable in practice. To overcome the lack of data, the proposed method uses labeled data obtained in different but related tasks. The proposed method embeds each example in tasks to a latent space by using a neural network and constructs a probabilistic model for learning a task-specific classifier while estimating annotators' abilities on the latent space. This neural network is meta-learned to improve the expected test classification performance when the classifier is adapted to a given small amount of annotated data. This classifier adaptation is performed by maximizing the posterior probability via the expectation-maximization (EM) algorithm. Since each step in the EM algorithm is easily computed as a closed-form and is differentiable, the proposed method can efficiently backpropagate the loss through the EM algorithm to meta-learn the neural network. We demonstrate the effectiveness of the proposed method with real-world datasets with synthetic noise and real-world crowdsourcing datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a meta-learning approach to handle noisy labels from multiple annotators. Learning from multiple source tasks generalizes to new target tasks that also have noisy annotations, making it robust to labeling inconsistencies in real-world crowdsourcing settings. This paper simulates annotator noise with different noise types in the meta-training phase by introducing pseudo-annotators. These synthetic annotators add controlled noise to clean labels, enabling the model to learn to handle label noise in a simulated environment.

### Strengths
1. Unlike other meta-learning approaches like MAML, which uses second-order gradients, the proposed model uses the EM algorithm to achieve closed-form updates, making it computationally more efficient.

2. By training on multiple source tasks, the model learns how to handle new unseen noisy target tasks.

3. The pseudo-annotation strategy is interesting, where noise is artificially added to clean source data to simulate the real-world setting of noisy annotators.

### Weaknesses
1. Assumption: This paper assumes noise comes from multiple annotators with different error patterns and biases and each annotator’s behavior is consistent within a task, but for real-life data scenarios, it is not accurate, each annotator is domain-specific.

2. Novelty: The paper combines well-established methods like GMMs and annotator-specific confusion matrices within a meta-learning framework to handle noisy labels, the novelty is somewhat limited, such as GMM-based clustering has already been widely used for probabilistic class assignments and label noise mitigation.

### Questions
1. Increasing $N_s$ and $R$ significantly improves the model performance. The authors could add experiments with larger $N_s$ and $R$values to assess at what point performance stabilizes or converges.

2. How does the model perform if certain classes have significantly fewer support data points than others? How robust is it to imbalances in the number of labeled examples per class?

3. Discuss the situations if we have hundreds or thousands of annotators and each of them only label a few instances?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a meta-learning method designed to learn from multiple noisy annotators, addressing a common challenge in supervised learning where labels can vary in quality due to differences in annotator skills and biases. The proposed method aims to enhance classifier accuracy even when labeled data is limited. It achieves this by utilizing labeled data from related tasks, embedding examples into a latent space via a neural network, and constructing a probabilistic model to learn task-specific classifiers while assessing annotators' abilities.  The neural network is meta-learned to optimize test classification performance with small annotated datasets, leveraging the Expectation-Maximization (EM) algorithm for efficient adaptation. The effectiveness of the method is demonstrated through experiments on real-world datasets, including those with synthetic noise and actual crowdsourced data.

### Strengths
Originality: The paper introduces a novel approach that integrates meta-learning with the handling of noisy annotations, representing an innovative solution to a well-recognized problem in machine learning.
Quality: The methodology is technically sound, employing a clear framework and the well-established EM algorithm for parameter estimation. The approach is backed by empirical results, showcasing its effectiveness across various datasets.
Significance: This work is significant as it addresses a pressing issue in many practical applications, particularly in crowdsourcing scenarios where high-quality labeled data is hard to obtain. The proposed method could improve the robustness of machine learning models in real-world situations.

### Weaknesses
1.The description of this paper is not clear enough. For example, the description of the method proposed in this paper in the last two paragraphs of INTRODUCTION is lengthy and lacks logic. The RELATED WORK, DATA, COMPARISON METHODS sections are full of nonsense and lack structure.
2.The experimental comparison method lacks the latest methods in the last two years.
3.The datasets used in the experiment are all in the field of images and lack representativeness.

### Questions
There is an obvious challenge with this approach: how do we select and identify the source task 2? 
Beyond that, why don't we just use transfer learning?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a meta-learning approach to improve classifier performance on tasks with limited, noisy annotations from multiple annotators. By embedding examples in a latent space and modeling class probabilities with a Gaussian Mixture Model (GMM), the method effectively leverages labeled data from source tasks to inform target tasks. The EM algorithm estimates annotator reliability, allowing the technique to backpropagate loss efficiently for meta-learning. The approach is tested on real-world datasets like LabelMe and synthetic datasets like Omniglot and Miniimagenet, showing robust improvements over competing methods.

### Strengths
* **Originality:** The paper takes an interesting approach to tackling noisy annotations in a way that considers both the variability in annotator reliability and the scarcity of target task data. By simulating noisy labels during meta-training, the method closely approximates real-world challenges.

* **Quality:** The model is theoretically grounded, with empirical testing on multiple datasets to support its claims. Using the EM algorithm within meta-learning allows the model to adapt efficiently while controlling computational complexity. The comprehensive experiments add credibility to the method’s robustness across noise levels.

* **Clarity:** Overall the paper is well-organized.

* **Significance:** Although the proposed method requires additional samples from the source task, it could benefit numerous fields that rely on crowdsourced or expert-annotated data.

### Weaknesses
* **Computational Complexity:** The meta-learning phase involves training over multiple source tasks and iterative EM updates and maybe computationally demanding on larger datasets or in high-dimensional settings. 

* **Impractical Settings** Besides, such high-quality source samples in the source tasks might not be available in practice. Even in most existing test sets (i.e., CIFAR-10, CIFAR-100, ImageNet), there are a lot of label error issues as mentioned in R1. Noting that the testing phase still struggles to find high-quality annotated data, how can we assume perfect annotations are ready in so many source tasks?

* **Annotation Modeling Limitation:** By using input-independent confusion matrices, the model does not account for instance-specific annotator behavior, potentially missing nuances in how annotator quality varies by data complexity. Extending to instance-dependent matrices (R2, R3) could improve performance since real-world noise is observed to be more related to instance-dependent label noise (R3).

* **Clarity in Paper Presentation:** The paper presentation could be improved significantly by adding more clarifications. (Please refer to the "Questions")

**Reference:**

R1: Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks. Neurips 2021.

R2: Part-dependent label noise: Towards instance-dependent label noise. Neurips 2020.

R3: Learning with Instance-Dependent Label Noise: A Sample Sieve Approach. ICLR 2023.

R4: Learning with Noisy Labels Revisited: A Study Using Real-World Human Annotations. ICLR 2022.

### Questions
Q1: In Lines 14-15, the authors mentioned that:

``` To learn accurate classifiers, existing methods require many annotated data to deal with noisy labels.```

It could be better if additional revision is applied to this sentence, since the mentioned annotated data itself is often viewed as data with noisy labels, due to imperfect expertise.

Q2: The naming of the "testing phase" in Figure 1 is confusing.

The paper talks about learning from multiple noisy annotations, here "testing" refers to the testing of the meta-learned model or the testing of the model trained on adapted labels.

Q3: Clarification of the inner problem [Line 69]

Empirically, what are the task differences here? Ideally, if the tasks are disjoint, then the inner problem of the bi-level optimization results in pretty high (i.e., 1) weight to the same/similar task, and almost no weight for the rest.

Q4: Impractical assumptions

In Line 77, the authors mentioned that ```Since source tasks contain only clean labeled data,```

This seems to be a harsh assumption. Even in most existing test sets (i.e., CIFAR-10, CIFAR-100, ImageNet), there are a lot of label error issues as mentioned in R1. 

Q5: Line 82: ```Gaussian misture model (GMM)``` $\rightarrow$ Gaussian Misture Model (GMM)

Q6: In Lines (103-104), the authors mentioned that 

```However, it often does not work well because it ignores per-annotator characteristics (Raykar et al., 2010).```

Agree that label aggregation will ignore per-annotator characteristics and lose too much information. However, there is a list of solutions that consider soft labels instead of aggregated labels. It is better to include the discussion/experiment comparisons as well. (i.e., simply average the multiple labels by assuming same expertise among annotators)

Q7: In Lines 127-129, the authors mentioned that

```the proposed method can adapt to data given from noisy annotators via the closed-form EM steps, which leads to effective and efficient meta-learning.```

I partially disagrees with authors that the proposed method leads to "efficient" meta learning, cuz it requires high quality annotations from source tasks.

Q8: Typo in Line 159. ```n-the``` $\rightarrow$ n-th

Q9: In line 222, it would be more beneficial to include more explanations on the assumption of conjugate prior distributions.

Q10: In Equation 5, it would be more beneficial to include more discussions about the tightness (or the performance gap) of the inequation.

Q11: In Line 272, the input of the algorithm 1 requires the confusion matrix distribution, which is often assumed to be a quite hard condition.

Q12: In lines 382-383, the experiment result would benefit a lot if including instance-dependent noise or real-world noise as well, for the annotator's type.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a meta-learning approach that utilizes noisy labels from multiple annotators to build a classifier without relying on true labels. The authors employ a probabilistic framework where latent class representations in a Mixture of Gaussians model are optimized via EM. This approach maximizes the likelihood of observed noisy labels given the latent variables, assuming these noisy annotations can guide the learning of true underlying classes.

### Strengths
1.I find this work’s approach novel in that it uses meta-learning based on a large amount of correctly labeled source data to effectively handle task-specific noisy data and learn about annotator errors. 
2.The Bayesian model presented is well-structured and logically sound; adding a graphical model could further enhance clarity for readers.
3.I appreciate their attempt to encode annotator-specific classification offsets into prior knowledge, which, based on the experimental results, appears to be effective. This treatment convincingly demonstrates the model's potential to manage annotator noise while preserving classification accuracy.

### Weaknesses
1. The paper assumes isotropic variance in the latent space, simplifying computation but potentially limiting flexibility. Real-world data often exhibit complex, class-specific structures that may not align with uniform variance assumptions, particularly in nuanced classification tasks.
2. Modeling A as a K*K*r matrix may lead to over-parameterization, especially with limited data. Without visualization of learned matrices, it's challenging to assess whether A captures meaningful annotator patterns. Additionally, assuming A is feature-independent implies annotator errors are detached from data features, suggesting p(y|x) = p(y) . This could prevent the model from learning a classifier grounded in meaningful data representation.
3. Maximizing likelihood of noisy label data rather than true labels raises concerns. Likelihood maximization is traditionally aimed at learning distributions close to true labels; without this, it is unclear if maximizing the joint likelihood on noisy data allows meaningful inference of latent true labels. The model might be vulnerable to learning patterns in the noise rather than capturing true class structure.
4. The GMM-based approach assigns a Gaussian component per class, hindering efficiency in large class-count tasks. With high-dimensional data, EM’s complexity grows, making it computationally burdensome. Approaches like hierarchical GMMs or variational inference could enhance scalability without sacrificing interpretability.
5. The rationale and motivation behind the design of p(A) (e.g. why it utilizes the Dirichlet components) is not clearly demonstrated by the author.

### Questions
1.How does the choice of isotropic variance in the latent space affect the model's flexibility and accuracy? Would other types of covariance  provide a meaningful improvement in capturing complex data structures?
2.Can you show some of the learned Ar and demonstrate how effectively they capture the true annotation bias?
3.Can you further demonstrate why eq 3 is called a conjugate prior? I don't think the prior would have a closed analytical form as eq3. Then how can we say it is conjugate? Also, since we use an iterative method to approximate the posterior, does the conjugacy of the prior matter?

### Soundness
3

### Presentation
3

### Contribution
3
