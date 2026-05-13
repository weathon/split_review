# Bayesian Coreset Optimization for Personalized Federated Learning

- Decision: Accept
- Scores: 6, 5, 8

## Abstract
In a distributed machine learning setting like Federated Learning where there are multiple clients involved which update their individual weights to a single central server, often training on the entire individual client's dataset for each client becomes cumbersome. To address this issue we propose CORESET-PFEDBAYES : a personalized coreset weighted federated learning setup where the training updates for each individual clients are forwarded to the central server based on only individual client coreset based representative data points instead of the entire client data. Through theoretical analysis we present how the average generalization error is minimax optimal up to logarithm bounds (upper bounded by $\mathcal{O}(n_k^{-\frac{2 \beta}{2 \beta+\boldsymbol{\Lambda}}} \log ^{2 \delta^{\prime}}(n_k))$) and lower bounds of $\mathcal{O}(n_k^{-\frac{2 \beta}{2 \beta+\boldsymbol{\Lambda}}})$, and how the overall generalization error on the data likelihood differs from a vanilla Federated Learning setup as a closed form function ${\boldsymbol{\Im}}(\boldsymbol{w}, n_k)$ of the coreset weights $\boldsymbol{w}$ and coreset sample size $n_k$. 
Our experiments on different benchmark datasets based on a variety of recent personalized federated learning architectures show significant gains as compared to random sampling on the training data followed by federated learning, thereby indicating how intelligently selecting such training samples can help in performance. Additionally, through experiments on medical datasets our proposed method showcases some gains as compared to  other submodular optimization based approaches used for subset selection on client's data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes a method to use Bayesian coresets for each individual client in a federated learning setting. Bayesian coreset can be used as proxy for full data at each individual client to estimate client-side distribution. The authors describe objective functions to incorporate the Bayesian coresets with federated learning setting. The authors give an algorithm and also give theoretical guarantees for the generalization error and its convergence. The authors support their theoretical claims with empirical results comapring their proposed approach with a number of baselines.

### Strengths
1. The paper is, for the most part, well written. There is not much work in terms of coresets for federated learning and as such the paper will be of interest to the community.
2. The authors have compared their method with a variety of baselines consisting of both - federated learning algorithms and also sampling strategies that incorporate diversity.  Their method performs well in most of the cases.
3. The algorithm is backed with theoretical guarantees. I did not check the proofs, but the statements appear sound.

### Weaknesses
1. I am not sure what is the challenge in incorporating the Bayesian coreset framework in federated learning setting. It would be better to explain clearly why this is a significant contribution. Both the algorithm and proof techniques appear to be heavily inspired from Zhang 2022b. The only modification seems to be use of Bayesian coresets. 

2. There are minor grammatical errors. Please do a grammar check.

### Questions
1. Why the prior $\pi$ in equation 1 is replaced by $\mathbf{z}$ in eq.6 - the modified client-side objective. Please clarify.

2. The subsample size is 50%. Is it not quite large? Does it give significant computational time benefits when compared with full data? Other than figure 3, there are no experiments mentioning computational efficiency.

3. Not a question but a suggestion. Algorithm 1 is not easy to follow for anyone unfamiliar with existing work or similar algorithms. How exactly is the coreset getting constructed? It would be good to give a high-level description of the same. 

Overall, the paper appears sound and I would be happy to raise my score once the doubts are cleared.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an optimization framework for personalized federated learning by incorporating Bayesian coresets into the model proposed in [1]. The author want to ensure that the accuracy performance does not deteriorate when applying coresets. To achieve this, they have made modifications to the common coreset objective. Furthermore, they provide proof of the convergence rate of generalization error using their approach and evaluate the effectiveness of their method on a range of datasets.

[1] Xu Zhang, Yinchuan Li, Wenpeng Li, Kaiyang Guo, and Yunfeng Shao. Personalized federated learning via variational bayesian inference.

### Strengths
- The integration of Bayesian coresets with federated learning is innovative.
- In the context of personalized federated learning, this work presents new ideas and considerations for defining the objective in coreset computation, which differs from the commonly used coreset definition.

### Weaknesses
 - The paper's content is a bit bloated, and the use of notations can be messy. For instance, sections 3.2 and 4 could be condensed to make them more concise. Additionally, there is potential to simplify the formulaic aspect.
- It would be beneficial if the author could emphasize their novel contribution, distinguishing it from the techniques previously proposed by others. Currently, these ideas seem to be mixed within the intricate details of the interpretations.
- The overall architecture, as well as certain smaller techniques and theoretical analysis methods, seem to be largely derived from previous work.
- The contribution on the coreset construction is limited. Although the authors introduce a new coreset objective, they do not provide sufficient NEW optimization techniques for the new objective. I could only identify some techniques borrowed from previous work.
- In my opinion, the primary contribution of this paper is the modified objective (eq. 9) tailored to personalized federated learning. However, the advantages of this modified objective are not adequately elucidated in the current presentation.

some minor problems

- In section 3, there is a confusion of n and N. For example, n in Fig 1 should be N. 
- In section 3.2 , it should be $ g_j = \mathcal{P}_\theta(\mathcal{D}_j^i) = E_{\theta\sim \hat{\pi}} P_\theta(\mathcal{D}_j^i) $.
- The subscript of the bold variable should not be bolded if it is a scalar.
- many other typos, e.g. missing equation references and confusing sentence like “For the first term in Equation 1, the authors we use a minibatch stochastic gradient descent …”

### Questions
- What is the benefits to apply coreset in the personalized federated learning? I think one of the most important is that it can reduce the communication complexity. It would be valuable to investigate and quantify the extent to which the coreset approach reduces communication complexity in the specific optimization task addressed in this work. This can be done theoretically, by providing a complexity formula, and practically, by presenting numerical results from experiments that show the reduction in communication complexity achieved.
- the intuition behind the new objective in eq. 9 is not very persuasive. If you could compute a coreset with a sufficiently small loss as defined in eq. 3, it is unecessary to add the term representing the “distance” between $\hat{q}^i(\theta, w)$ and $\hat{q}^i(\theta)$ since $\hat{q}^i(\theta, w)$ and $\hat{q}^i(\theta)$ will lead to closed losses; On the other hand, if you couldn’t make it under the constraint $\| w \|_0 \leq k$, which means there is no such small coreset with ideal error, the coreset method could not work well. It would be beneficial to clarify the merits of the new objective, such as its robustness or any other advantages it offers. Experiments that demonstrate the effectiveness of the new objective would greatly strengthen the argument.
- Does the modifications of eq. 6 consist of the following two parts: i) use the weighted likelihood. ii) replace prior distribution with global distritution. I am not sure for that.
- is there any strategy for choosing the value of k in practice?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work incorporated granular-level bayesian coresets optimization in Federated Learning. The proposed approach gave minimax convergence rate and showed good performance in empirical studies.

### Strengths
1. The idea of incorporating coreset optimization in FL is new and well-motivated.
2. Solid theoretical results are given.
3. Some optimistic empirical studies are presented.

### Weaknesses
1. The major weakness is the lack of convergence comparison in the empirical part. One of the major concerns in FL is the communication cost. Thus the number of iteration rounds is crucial in FL. The reviewer suggests not only including the comparison of the final accuracy under (maybe different levels, not only 50%) of sample complexity, but also including the convergence speed, i.e., the communication cost comparison.

2. How expensive it is to calculate the coreset samples/weights? Is there any empirical runtime results?

3. How is \hat{\pi} defined in Eq. (3) and (4)?

4. Some typo: first sentence in section 3.2 is incomplete. Different places for \hat notation in q^i(\theta, w), on q, or q^i, or q^i(theta, w).

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
