# Problem-Parameter Free Federated Learning

- Decision: Accept
- Avg Score: 7.60
- Scores: 8, 8, 8, 8, 6

## Abstract
Federated learning (FL) has garnered significant attention from academia and industry in recent years due to its advantages in data privacy, scalability, and communication efficiency. However, current FL algorithms face a critical limitation: their performance heavily depends on meticulously tuned hyperparameters, particularly the learning rate or stepsize. This manual tuning process is challenging in federated settings due to data heterogeneity and limited accessibility of local datasets. Consequently, the reliance on problem-specific parameters hinders the widespread adoption of FL and potentially compromises its performance in dynamic or diverse environments. To address this issue, we introduce PAdaMFed, a novel algorithm for nonconvex FL that carefully combines adaptive stepsize and momentum techniques. PAdaMFed offers two key advantages: 1) it operates autonomously without relying on problem-specific parameters; and 2) it manages data heterogeneity and partial participation without requiring heterogeneity bounds. Despite these benefits, PAdaMFed provides several strong theoretical guarantees: 1) It achieves state-of-the-art convergence rates with a sample complexity of $\mathcal{O}(\epsilon^{-4})$ and communication complexity of $\mathcal{O}(\epsilon^{-3})$ to obtain an accuracy of $||\nabla f\left(\boldsymbol{\theta}\right)|| \leq \epsilon$, even using constant learning rates; 2) these complexities can be improved to the best-known $\mathcal{O}(\epsilon^{-3})$ for sampling and $\mathcal{O}(\epsilon^{-2})$ for communication when incorporating variance reduction; 3) it exhibits linear speedup with respect to the number of local update steps and participating clients at each global round. These attributes make PAdaMFed highly scalable and adaptable for various real-world FL applications. Extensive empirical evidence on both image classification and sentiment analysis tasks validates the efficacy of our approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed a new federated learning algorithm called PAdaMFed that is problem-parameter free. The main idea is to combine SCAFFLOD and momentum. The authors also designed a modified version of PAdaMFed to reduce the variance, called PAdaMFed-VR  The authors showed that PAdaMFed-VR can achieve state-of-the-art convergence performance. The performance of PAdaMFed and PAdaMFed-VR is also verified using experiments.

### Strengths
1. The proposed PAdaMFed is independent of the problem parameters such as gradient divergence. 

2. The author also designed PAdaMFed-VR to reduce the variance of the federated learning algorithm.

3. The authors showed the convergence upper bound of PAdaMFed and PAdaMFed-VR analytically.

### Weaknesses
1. The idea of PAdaMFed is a direct extension of SCAFFOLD with momentum considered at each client. 

2. The challenge in the proof is unclear.

### Questions
1. What are the challenges in the proof compare to the proof in the SCAFFOLD algorithm?

2. The assumptions used in this paper are similar to those used in proving the convergence rate of the SCAFFOLD algorithm, so the gain in terms of convergence analysis must coming from using momentum and variance reduction. Please provide a detailed explanation on the gain of the proposed algorithms. Please provide a detailed comparison in terms of the convergence rate/communication complexity between PAdaMFed, PAdaMFed-VR, the SCAFFOLD algorithm and related algorithms as the Table 2 in the SCAFFOLD paper.

Karimireddy, Sai Praneeth, Satyen Kale, Mehryar Mohri, Sashank Reddi, Sebastian Stich, and Ananda Theertha Suresh. "Scaffold: Stochastic controlled averaging for federated learning." In International conference on machine learning, pp. 5132-5143. PMLR, 2020.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces PAdaMFed, a federated learning algorithm that uses momentum and adaptive learning rates to address client heterogeneity, similar to SCAFFOLD-M. The method is problem-parameter-free and does not require parameter tuning. The paper provides a convergence bound, without the standard assumption about gradient dissimilarity.

### Strengths
1- The paper studies important problems. Both data heterogeneity and hyperparameter tuning are existing issues for FL systems. The method has problem-independent hyperparameters which makes it more useful in practice.

2- There are not many works in the literature that study problem-independent parameters; this work is one of the first.

3- The convergence bound and analysis is novel, and has minimal assumptions. The authors proved convergence without assumptions about gradient dissimilarity, a standard assumption that most of the literature's works require.

### Weaknesses
1- The convergence bound presented in the paper, while novel, is not optimal when compared to the bound achieved by SCAFFOLD-M. Specifically, the paper should provide a more detailed comparison for the case when $K$ (the number of local updates) is a function of $T$ (total rounds). A fair comparison would involve deriving the equivalent formulation for SCAFFOLD-M under the same conditions to accurately assess the relative performance of PAdaMFed.

2- The empirical results are limited in scope. The paper would be significantly strengthened by including experiments conducted on a wider range of architectures and datasets. This would provide a more comprehensive evaluation of the proposed method's effectiveness and generalizability across different problem settings.

3- The paper overlooks a relevant work [1] that shares similarities with the proposed method. A thorough comparison of the proposed method and results with those presented in [1] is necessary to properly contextualize the contributions of this work within the existing literature. Specifically, the authors should discuss the differences in terms of handling client drift, a critical issue in federated learning.

Minor: Most of related works uses $\|\nabla f(x)\|^2 \le \epsilon$ and not  $\|\nabla f(x)\| \le \epsilon$ for the definition of $\epsilon$-stationary and this formulation makes the paper a bit confusing.

### Questions
1- Can you recover the optimal bound with the extra assumption and different learning rates?

2- Can you design an experiment in which the gradient dissimilarity assumption does not hold and other methods fail to converge?

suggestion: since $c^{t-1}$ and $g^{t-1}$ are used only as $\beta c^{t-1} + (1- \beta) g^{t-1}$ you can only send the weighted sum and not each one to the clients and have the same communication per round as SCAFFOLD.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes an algorithm called PAdaMFed, where the hyperparameters don't depend on the problem-specific parameters such as smoothness constant, stochastic gradient variance bound, etc. PAdaMFed applies a client-drift control mechanism similar to SCAFFOLD but also uses normalized updates at the client level. It also has a momentum-based update rule at the global level. A variance-reduced version of PAdaMFed, called PAdaMFed-VR is also proposed. PAdaMFed and PAdaMFed-VR have communication complexities of $\mathcal{O}(\epsilon^{-3})$ and $\mathcal{O}(\epsilon^{-2})$, respectively, for converging to an $\epsilon$ stationary point. The convergence results don't rely on data heterogeneity bounds, which is also interesting. Empirical results on EMNIST and IMDB (in the appendix) show the efficacy of the proposed method.

### Strengths
**1.** This paper seems to be the first one to provide an algorithm whose hyperparameters are fully independent of the problem-specific parameters such as smoothness constant, stochastic gradient variance bound, etc. However, I'm not up to speed on all the relevant literature.

**2.** It is interesting that the results don't rely on any kind of heterogeneity bound. 

**3.** Empirical results show that the proposed method is better than SCAFFOLD.

### Weaknesses
 **1.** It is not clear to me what exactly is enabling the algorithm to work with hyperparameters that don't depend on problem-specific parameters. This aspect should be explained better. For instance, does normalization in step 8 of Algorithm 1 enable the hyperparameters to be independent of the smoothness constant? It's unclear how this normalization interacts with the momentum and control variate mechanisms to achieve this independence. A more detailed explanation of the interplay between these components is needed to fully understand the algorithm's behavior.

**2.** How exactly the variation reduction step in PAdaMFed-VR leads to variance reduction should be explained more precisely. The current discussion in Section 3.2 is not very satisfactory. Is this step of PAdaMFed-VR inspired by the update rule of STORM [1]? Also since the relative weights of the gradients at $\theta_i^{t,k}$ and $\theta_i^{t-1}$ are different ($1$ and $1-\beta$, respectively), it'd be helpful to have some discussion on how $\beta$ should be chosen to reduce the variance and also retain a sufficient amount of client drift control (w/ weight $\beta$). The explanation should also clarify how the specific form of the variance reduction term, which involves a difference of gradients at different points, achieves its intended effect, and how this relates to the variance reduction techniques used in other methods.

**3.** The empirical results show that PAdaMFed is better than SCAFFOLD even after the hyperparameters of SCAFFOLD are tuned. However, from what I understood, the derived convergence results don't indicate this. Can the authors please explain this? The convergence analysis should be more closely tied to the empirical observations. It would be helpful to understand if there are specific aspects of the algorithm that are not captured by the theoretical analysis, but contribute to the observed performance gain over SCAFFOLD. A discussion of the limitations of the theoretical analysis would also be beneficial.

### Questions
**1.** Is there any intuition for why there is no requirement for any kind of heterogeneity bound for deriving the results of this paper?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the convergence of federated averaging algorithms with momentum. Its main contribution is to establish the convergence and convergence rate of these algorithms when the step-sizes and momentum parameters in the local and aggregation algorithms are tuned independently of problem-specific parameters, such as the Lipschitz constant of the gradients. Instead, these parameters depend solely on the number of local and global iterations and the number of nodes sampled in each iteration.

### Strengths
The topic is important and well motivated. It is indeed a problem that for ensuring theoretical convergence one typically needs parameters like Lipschitz constant on the gradient, which are typically not known. 

The paper is well written and the results look correct, at least the main steps in the proofs look correct.

### Weaknesses
I have some concerns with the setup. Many algorithms already permit diminishing step-sizes that do not require knowledge of the Lipschitz constant of the gradient, such as step-decay or similar approaches, which also come with theoretical guarantees. These methods have the added advantage that step-sizes can start relatively large and decrease over time, while in this approach, the step-size is inversely based on the total number of global and local iterations, which may be large. As a result, the step-sizes in this method are consistently small. There is no comparison to such methods here.

The experiments are not reproducible, the code is not provided and there is no information about hyper parameter tuning or other details for other algorithms, except that a grid search has been used.

Since the number of sampled nodes is used in the parameter selection, what to do if the number of sampled nodes changes between iterations?

In the numerical results, why only considering accuracy? I get that accuracy, or some similar Machine Learning metrics are important to evaluation for Machine Learning applications. However, all the theory is related to optimization metrics, the size of the gradient norm. It would be good to also show how the numerical results align with the theoretical results in the paper.

In line 8 of Algorithm 1, why do you take scale the gradient direction with the gradient norm? This means that you don't use the magnitude of the gradient, only the direction of the gradient. This is probably why you don't need Lipschitz constant of the gradient, even in deterministic optimziation algorithms such algorithms converge without using Lipschitz constants, but if we don't use gradient magnitude then convergence rate will be worse worse and compatible to sub-gradient methods, since we are not exploiting the smoothness.

Given that for your algorithm you did not do any grid search to tune hyperparameters, while grid-search was used for the other algorithms, I am a bit surprised how much better results you get. In my experience, the hyperparameters obtain from the theory are usually not good in practice, usually one can find much better parameters from doing grid search. Would this be the case for your work? 

In Table 1, it would be good if you could also include the complexity bounds.

### Questions
Since the number of sampled nodes is used in the parameter selection, what to do if the number of sampled nodes changes between iterations?

In the numerical results, why only considering accuracy? I get that accuracy, or some similar Machine Learning metrics are important to evaluation for Machine Learning applications. However, all the theory is related to optimization metrics, the size of the gradient norm. It would be good to also show how the numerical results align with the theoretical results in the paper.

In line 8 of Algorithm 1, why do you take scale the gradient direction with the gradient norm? This means that you don't use the magnitude of the gradient, only the direction of the gradient. This is probably why you don't need Lipschitz constant of the gradient, even in deterministic optimziation algorithms such algorithms converge without using Lipschitz constants, but if we don't use gradient magnitude then convergence rate will be worse worse and compatible to sub-gradient methods, since we are not exploiting the smoothness.

Given that for your algorithm you did not do any grid search to tune hyperparameters, while grid-search was used for the other algorithms, I am a bit surprised how much better results you get. In my experience, the hyperparameters obtain from the theory are usually not good in practice, usually one can find much better parameters from doing grid search. Would this be the case for your work? 

In Table 1, it would be good if you could also include the complexity bounds.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces PAdaMFed, a new federated learning (FL) algorithm that removes dependence on problem-specific parameters, a significant advancement for FL where hyperparameter tuning is often hindered by data heterogeneity and limited local dataset accessibility. By combining adaptive stepsizes and momentum, PAdaMFed aims to manage arbitrary data heterogeneity and partial client participation while achieving state-of-the-art convergence and communication complexities. Empirical results validate the theoretical benefits of PAdaMFed across multiple tasks, demonstrating robustness and scalability.

### Strengths
1. The parameter-free design in FL addresses a critical challenge, making this an interesting and important contribution.
2. Theoretical guarantees, including sample and communication complexities of \(O(\epsilon^{-4})\) and \(O(\epsilon^{-3})\) respectively for the standard version (with further improvements under variance reduction), are rigorously derived and well-supported.

### Weaknesses
1. The "problem-parameter free" claim is somewhat unclear. Although the authors suggest that PAdaMFed has no dependency on problem-specific parameters like the smoothness constant \(L\), it seems that implicit conditions on \(L\) might still affect the learning rate. For example, Assumptions A3 and A4 seem to require some condition on \(L\) related to \(K\) and \(T\), suggesting that the learning rate still indirectly depends on \(L\). Specifically, the stepsizes are defined by system-defined constants \((S,K,T)\), but the theoretical analysis still relies on \(L\) through Lemmas 3 and 4, which bound the error terms. While the stepsizes themselves are independent of \(L\), the convergence analysis depends on how these stepsizes interact with the smoothness constant, making the claim of complete independence questionable.
  
2. From my understanding, achieving a truly problem-parameter free algorithm would typically involve hyperparameter adaptivity based on problem characteristics. Simply incorporating variance reduction and momentum may not fully achieve this goal. In problem-parameter or hyper-parameter free algorithms in centralized learning, the key is to design the adaptivity of these hyper-parameters. The current approach uses gradient normalization, which provides some adaptivity, but it is not clear if this is sufficient to handle the wide range of problems encountered in federated learning. A more robust approach might involve dynamically adjusting the momentum or variance reduction parameters based on observed training behavior, rather than relying on fixed schedules.

3. The algorithm requires communication of three vectors per round, which is substantial. Since communication often constitutes a major bottleneck in FL, this increase is likely not marginal, especially given the lack of evidence provided to support this claim. The paper should provide a more detailed analysis of the communication overhead, including a comparison with other state-of-the-art methods and an evaluation of the practical impact of this increased communication cost on overall training time and resource utilization.

4. I have concerns regarding the experiment results. The baselines, particularly FedAvg, appear to underperform, with an accuracy of only 0.8 on EMNIST IID data. The experimental section would be stronger if it included additional datasets and models, along with an ablation study to isolate the contributions of adaptive stepsizes and momentum, as proposed in the PAdaMFed, to the overall performance. The current experiments do not sufficiently demonstrate the robustness and generalizability of the proposed algorithm across diverse federated learning scenarios. It is also unclear if the reported performance gains are due to the adaptive stepsizes, momentum, or a combination of both. The lack of ablation studies makes it difficult to assess the individual contributions of each component.

### Questions
1. I'd like to know the performance of these baselines, particularly FedAvg, which seems to underperform.
2. I suggest an ablation study to isolate the contributions of adaptive stepsizes and momentum in the PAdaMFed.

### Soundness
3

### Presentation
3

### Contribution
3
