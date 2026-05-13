# Federated Learning, Lessons from Generalization Study: Communicate Less, Learn More

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
We investigate the generalization error of statistical learning models in a Federated Learning (FL) setting. Specifically, we study the evolution of the generalization error with the number of communication rounds between the clients and the parameter server, i.e., the effect on the generalization error of how often the local models as computed by the clients are aggregated at the parameter server. We establish PAC-Bayes and rate-distortion theoretic bounds on the generalization error that account explicitly for the effect of the number of rounds, say $R \in \mathbb{N}^*$, in addition to the number of participating devices $K$ and individual datasets size $n$. The bounds, which apply in their generality for a large class of loss functions and learning algorithms, appear to be the first of their kind for the FL setting. Furthermore, we apply our bounds to FL-type Support Vector Machines (FSVM); and we derive (more) explicit bounds on the generalization error in this case. In particular, we show that the generalization bound of FSVM increases with $R$, suggesting that more frequent communication with the parameter server diminishes the generalization power of such learning algorithms. Combined with the fact that the empirical risk generally decreases for larger values of $R$, this indicates that $R$ might be a parameter to optimize to minimize the population risk of FSVM. Moreover, our bound suggests that for any $R$, the generalization error of the FSVM setting decreases faster than that of centralized learning by a factor of $\mathcal{O}(\sqrt{\log(K)/K})$, thereby generalizing recent findings in this direction for $R=1$ (sometimes referred to as ``one-shot'' FL or distributed learning) to any arbitrary number of rounds. Furthermore, we also provide results of experiments that are obtained using neural networks (ResNet-56), and which suggest that our observations for FSVM may hold true more generally.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper examines the impact of the number of rounds on generalization errors in a federated learning setting. It presents generalization errors in the form of PAC-Bayes bounds and rate-distortion theoretic bounds and applies these results to federated learning support vector machines. The authors argue that the generalization errors increase with more rounds of communication (R).

### Strengths
1) It's a really interesting problem. There are many papers studying the convergence properties of FL algorithms, however, little work is done in terms of the generalization of these algorithms.

2) This paper proves three new bounds that explicitly have the number of rounds (R) in their bounds which allows the study of its effect on generalization.

3) They apply the bounds to FL-SVM to get an explicit result and have experiments validating their bound.

### Weaknesses
1) The assumption that R < N and each data point is only visited in one round is not realistic and doesn't capture what happens for FL in practice. In most settings in FL, the number of samples per client (N) is small, and the number of rounds is much higher. Additionally, I don't see if the current analysis is possible to extend to these cases. This assumption severely limits the applicability of the results. The analysis does not account for the common scenario where clients use their local data multiple times across different rounds, which is a fundamental aspect of many FL algorithms. This discrepancy between the theoretical setup and practical FL scenarios raises concerns about the relevance of the derived bounds.

2) Generally in FL papers with a focus on optimization, they report the curves about the loss and accuracy of the test set during the training, and it's common that the performance on the test set improves over more rounds, so the results can't extend to the more general cases, beyond FL-SVM. The paper's focus on generalization bounds, while valuable, does not align with the typical empirical evaluation of FL algorithms, where test set performance is a primary metric. The observation that test set performance often improves with more rounds contradicts the paper's claim that generalization error increases with R, suggesting a disconnect between the theoretical findings and practical observations in more general FL settings.

3) The quantity of interest in ML is the true risk (population risk) and not the generalization. Even with the current assumptions, If the speed of decrease of training loss is more than the increase of generalization, it's not possible to argue the smaller number of rounds is better. In Fig 4. and Fig 8. of the appendix we can't see the increase in the population risk with the number of rounds for FL-SVM. The paper's focus on generalization error, while important, does not directly address the population risk, which is the ultimate goal in machine learning. The analysis does not provide a clear picture of how the population risk changes with the number of rounds, and the experimental results for FL-SVM do not show a clear increase in population risk with R, which is a key claim of the paper. The trade-off between training loss and generalization error is not sufficiently explored, and the paper does not provide a clear argument for why a smaller number of rounds is always preferable.

4) As mentioned in the paper, another approach would be to just apply basic PAC-Bayes bounds such as McAllester's without explicitly considering the dynamics of FL. Some numerical comparison of these bounds is needed. It's not clear to me that the bound in theorem 1 gives a better guarantee. McAllester's bound doesn't have the structure of the FL explicitly, however, it would be applied to the output of the algorithm and that might be enough. Also, it doesn't require the assumptions mentioned in the weakness 1. The paper does not provide a clear justification for why the proposed bounds are superior to existing PAC-Bayes bounds, such as McAllester's. A numerical comparison of the proposed bounds with these existing bounds is necessary to demonstrate the practical advantages of the new approach. The paper needs to clarify why the explicit modeling of the FL structure leads to better generalization guarantees than simply applying a general PAC-Bayes bound to the output of the FL algorithm.

5) Based on my understanding of the analysis, I assume that the same approach can be applied to the number of local steps per round if each data point would participate in just one local round. As a result, the number of local steps would also appear in the bound. It would be interesting to see its effect, as in the experiments of the paper, the total number of SGD steps is fixed, and with the increase of R, the number of local steps decreases. The analysis does not consider the impact of the number of local steps per round on the generalization error. The paper should explore whether the same analysis can be extended to incorporate the number of local steps and how this affects the derived bounds. The current experimental setup, where the total number of SGD steps is fixed, does not allow for a clear understanding of the effect of the number of local steps on the generalization error.

### Questions
Please discuss the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work provides novel PAC-Bayesian and rate-distortion typed generalisation bounds tailored for federated learning. Contrary to classical bounds designed for batch learning, authors take into account the evolution of the learning phase through successive rounds and now consider the number of rounds as an hyperparameter to optimise to ensure a good tradeoff between empirical performances and generalisation ability. They particularise their results to the case of federated SVMs and provide associated experiments.

### Strengths
Having such theoretical bounds tailored for federated learning is novel and provide exciting new leads to understand the efficiency of FL.

### Weaknesses
I have concerns about correctness of Theorem 1, some presentation issues and the conclusion of the experiments, see the 'Questions' section.

-  The definition of $P_{\mathbf{W},\mathbf{S}}$ is unclear. Is it a distribution over $\mathcal{W}^{(K+1)R}$ and then, is the use of the product $\Pi$ equivalent to $\otimes$ ? Otherwise, if it is a distribution over $\mathcal{W}$ can you make this explicit? 
- Given the way $S_k$ is partitioned for any $k$, users are not allowed to use their whole dataset at each round but only a smaller fraction $n_R$. Is it a realistic in practice? For instance take the instance of federated learning between hospital to better detect a rare disease (i.e. each user has few data), is it reasonable in this case to force the users not to use their whole dataset each round? Furthermore, this would imply that if $n$ is small, then one would not be allowed to perform many training rounds.  What can the authors say about this?  
- In section 2, you said that 'the aggregation function at the PS is set to be deterministic and arbitrary' while in Theorem 1,  $\bar{W}^{[r-1]}$ is drawn according to a probability distribution, what did I miss? Furthermore, how costful is this additional expectation in terms of computational time as it does not appear in many classical PAC-Bayes bounds?
- I found Theorem 1's proof poorly organised, for instance,  $\mathbf{\nu}_{S}$ is defined in Lemma 1's proof, which has been put on another appendix. Similarly, I did not find a definition of $\mathcal{G}_S^{\delta}$ although somewhat inferable from context.
- I don't understand the use of the subgausiannity assumption at the end of page 2022. Let rename $X= gen(s_k^{(r)}, \bar{W}^{(R)})$, then you affirm that because $X$ is $\sigma_{k,r}:= \sqrt{\frac{R}{4n}}$ subgaussian we have $\mathbb{E}[e^{\lambda X^2}]\leq \frac{2n}{R}$.  This is highly non-standard, how do you prove it?  To me, subgaussianity would only imply $\mathbb{E}[e^{\lambda X}]\leq \exp(\frac{\lambda^2 \sigma_{k,r}^2}{2})$.    
- About the experiments, I am not convinced that communicating less implies a better learning phase, at least for FVSM. Indeed, this conclusion appears to be true for $K=10,20$ (not the case $K=50$ as the short decrease in the end of the curve exhibits more a stabilisation than a deterioration) and holds when considering the generalisation gap, instead of observing directly the population risk . Thus, if we focus on the notion of population risk, Figure 4 shows that increasing the number of rounds only leads to positive outcomes as the empirical risk continues to decrease while the population risk either decreases or stabilises. A similar conclusion can be derived from Figure 6. I acknowledge that you affirm in section D.2 that 'fewer rounds may be needed, if one can effectively take the “estimated” generalisation error into account', but a practitioner does not have access to this information and see only benefits to continue its training as the empirical risk decreases, and the test error does not vary: there is no stopping criterion in practice. 
To me, the interest of a tradeoff in $R$, only appears in Figure 3, which is not covered by Theorem 4.

In conclusion, although my enthusiasm about having PAC-Bayesian guarantees tailored to FL, I believe this paper needs to be rewritten before its acceptance, given my current concerns about the correctness of Theorem 1 and the shift between the message conveyed by the paper (starting from its title) and the proposed experiments.

### Questions
-  The definition of $P_{\mathbf{W},\mathbf{S}}$ is unclear. Is it a distribution over $\mathcal{W}^{(K+1)R}$ and then, is the use of the product $\Pi$ equivalent to $\otimes$ ? Otherwise, if it is a distribution over $\mathcal{W}$ can you make this explicit? 
- Given the way $S_k$ is partitioned for any $k$, users are not allowed to use their whole dataset at each round but only a smaller fraction $n_R$. Is it a realistic in practice? For instance take the instance of federated learning between hospital to better detect a rare disease (i.e. each user has few data), is it reasonable in this case to force the users not to use their whole dataset each round? Furthermore, this would imply that if $n$ is small, then one would not be allowed to perform many training rounds.  What can the authors say about this?  
- In section 2, you said that 'the aggregation function at the PS is set to be deterministic and arbitrary' while in Theorem 1,  $\bar{W}^{[r-1]}$ is drawn according to a probability distribution, what did I miss? Furthermore, how costful is this additional expectation in terms of computational time as it does not appear in many classical PAC-Bayes bounds?
- I found Theorem 1's proof poorly organised, for instance,  $\mathbf{\nu}_{S}$ is defined in Lemma 1's proof, which has been put on another appendix. Similarly, I did not find a definition of $\mathcal{G}_S^{\delta}$ although somewhat inferable from context.
- I don't understand the use of the subgausiannity assumption at the end of page 2022. Let rename $X= gen(s_k^{(r)}, \bar{W}^{(R)})$, then you affirm that because $X$ is $\sigma_{k,r}:= \sqrt{\frac{R}{4n}}$ subgaussian we have $\mathbb{E}[e^{\lambda X^2}]\leq \frac{2n}{R}$.  This is highly non-standard, how do you prove it?  To me, subgaussianity would only imply $\mathbb{E}[e^{\lambda X}]\leq \exp(\frac{\lambda^2 \sigma_{k,r}^2}{2})$.    
- About the experiments, I am not convinced that communicating less implies a better learning phase, at least for FVSM. Indeed, this conclusion appears to be true for $K=10,20$ (not the case $K=50$ as the short decrease in the end of the curve exhibits more a stabilisation than a deterioration) and holds when considering the generalisation gap, instead of observing directly the population risk . Thus, if we focus on the notion of population risk, Figure 4 shows that increasing the number of rounds only leads to positive outcomes as the empirical risk continues to decrease while the population risk either decreases or stabilises. A similar conclusion can be derived from Figure 6. I acknowledge that you affirm in section D.2 that 'fewer rounds may be needed, if one can effectively take the “estimated” generalisation error into account', but a practitioner does not have access to this information and see only benefits to continue its training as the empirical risk decreases, and the test error does not vary: there is no stopping criterion in practice. 
To me, the interest of a tradeoff in $R$, only appears in Figure 3, which is not covered by Theorem 4.


In conclusion, although my enthusiasm about having PAC-Bayesian guarantees tailored to FL, I believe this paper needs to be rewritten before its acceptance, given my current concerns about the correctness of Theorem 1 and the shift between the message conveyed by the paper (starting from its title) and the proposed experiments.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper examines generalization error in Federated Learning (FL) and focuses on the impact of communication rounds (R) on this error. It introduces PAC-Bayes and rate-distortion bounds for FL and applies them to Federated Support Vector Machines (FSVM). The study finds that as R increases, the generalization error of FSVM worsens, suggesting that more frequent communication with the parameter server diminishes its generalization power. The paper also shows that, for any R, FL outperforms centralized learning by a factor proportional to O(log(K)/K). Experiments with neural networks support these findings.

### Strengths
The strengths of this paper are as follows:

1. **Novel Bounds**: The paper introduces novel PAC-Bayes and rate-distortion theoretic bounds that explicitly consider the influence of the number of communication rounds (R), the number of participating devices (K), and dataset size (n) on generalization error. These bounds are the first of their kind for the problem addressed in the study.
2. **Modeling Contributions**: The research provides insight into the structure of distributed interactive learning algorithms, showing how each client's contribution at each round affects the generalization error of the final model. 
3. **Applicability to FSVM**: The paper applies these theoretical bounds to Federated Support Vector Machines (FSVM) and derives explicit bounds for generalization error. Notably, it reveals that more frequent communication with the parameter server reduces the generalization power of FSVM algorithms. This suggests that the parameter R can be optimized to minimize the population risk of FSVM.
4. **Generalization of Findings**: The research demonstrates that the generalization error of the FSVM setting decreases faster than that of centralized learning by a factor proportional to O(log(K)/K) for any value of R. This generalizes recent findings for "one-shot" Federated Learning to any arbitrary number of rounds.

### Weaknesses
1.  **Problem Setting**: The paper assumes a partitioning of data (n samples) into R disjoint subsets for each client, with each subset used in one communication round. This assumption may be considered strong and unrealistic, as many Federated Learning (FL) approaches typically use the entire batch for training in each round. Furthermore, in real-world scenarios, a mix of old and new data is often present in an online approach. This strict partitioning, where each client uses a completely new subset of data in each round, does not reflect common FL practices and limits the practical applicability of the theoretical results. Specifically, the analysis does not account for the common scenario where clients iteratively refine their models using the same local data across multiple communication rounds, which is a fundamental aspect of many FL algorithms.

2.  **Counter-Intuitive Observation**: Moreover, if we consider a fixed n, each client ends up with n/R data for each communication round. To illustrate this with a special case, let's take R=1, which essentially reduces the scenario to a single round of aggregation across clients. Surprisingly, based on the results presented in the paper, which indicate that the generalization error increases with R, it might suggest that R=1 should be chosen. This finding appears counter-intuitive and raises questions about the practicality and relevance of the assumed setting for real-world federated learning applications. The theoretical result suggests that more communication rounds lead to worse generalization, which contradicts the common intuition that more iterative updates should lead to better model convergence and generalization. This discrepancy needs further clarification and justification.

### Questions
I suggest that the author undertake a more extensive exploration of the practical implications stemming from the theoretical findings. It is imperative to conduct an exhaustive examination of the interdependencies between key parameters across various scenarios. Such an in-depth analysis holds the potential to offer invaluable insights into the development of real-world federated learning algorithms. Personally, I hold the theoretical contribution of this paper in high regard, despite my reservations about the underlying settings. A more comprehensive analysis would significantly enhance the overall quality of this paper and can be translated into guidance for the refinement and enhancement of federated learning systems.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
