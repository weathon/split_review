# Decentralized Sporadic Federated Learning: A Unified Algorithmic Framework with Convergence Guarantees

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 3, 8, 8, 8

## Abstract
Decentralized federated learning (DFL) captures FL settings where both (i) model updates and (ii) model aggregations are exclusively carried out by the clients without a central server. Existing DFL works have mostly focused on settings where clients conduct a fixed number of local updates between local model exchanges, overlooking heterogeneity and dynamics in communication and computation capabilities. In this work, we propose Decentralized Sporadic Federated Learning (\texttt{DSpodFL}), a DFL methodology built on a generalized notion of \textit{sporadicity} in both local gradient
    and aggregation processes.
    \texttt{DSpodFL} subsumes many existing decentralized optimization methods under a unified algorithmic framework by modeling the per-iteration (i) occurrence of gradient descent at each client and (ii) exchange of models between client pairs as arbitrary indicator random variables, thus capturing \textit{heterogeneous and time-varying} computation/communication scenarios. 
    We analytically characterize the convergence behavior of \texttt{DSpodFL} for both convex and non-convex models, for both constant and diminishing learning rates, under mild assumptions on the communication graph connectivity, data heterogeneity across clients, and gradient noises, and show how our bounds recover existing results as special cases.
    Experiments demonstrate that \texttt{DSpodFL} consistently achieves improved training speeds compared with baselines under various system settings. %under heterogeneous and time-varying environments compared with existing decentralized learning schemes.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes a generalized framework for analyzing the challenges of federated learning in a decentralized setting. Such challenges include heterogeneity in the updates of individual clients, and communication constraints for achieving consensus in a decentralized setup (which is more challenging that the typical "star" topology with a central PS). The term "sporadicity" in the title refers to varying frequencies of both -- local updates at clients (limited by computational capacity), and inter-client communication (limited by network capacity). The work proposes a unifying framework for analyzing the effect of this sporadicity on the convergence rate.

### Strengths
The algorithm framework proposed in eq (2) that considers the effect of both kinds of sporadicity as mentioned above is one of the primary contributions of the paper. This is further formulated as a matrix update in eq. (3), and the consensus weights are chosen the mixing matrix is doubly stochastic.

The unifying approach to analyze computation and communication sporadicity is definitely an important step towards analyzing decentralized algorithm. The work has been placed well (and compared with) in the context of existing literature. The convergence analysis is quite comprehensive, and aligns with the standard analysis techniques of works in this line. The analytical contribution of the paper is definitely commendable.

### Weaknesses
I have some important concerns which I list here in the "Weaknesses" section. Other minor concerns or questions are mentioned in the next section. I would appreciate it if the authors could clarify the following concerns:

1. My major concern is that it is not really clear where the gain of DSpodFL is coming from? The work shows improvements in numerical simulations, in which the X-axis in the total latency. Is the primary intuition behind the improved performance of DSpodFL just the fact that frequent communications are not necessary, which other decentralized algorithms do? Is the benefit of DSpodFL over other algorithms quantified/discussed anywhere in the paper?

2. Are the weights $r_{ij}$ need to be known beforehand? For example, in Metropolis-Hastings mixing, the future topology of the graph needs to be known -- an assumption that may not hold true for federated learning when the network is dynamically changing (for mobile clients, for example), and it is not easy to know the union of all edge sets and determine the weight. How are they chosen in the simulations?

### Questions
I have a few concerns, and I would be very glad if these are addressed:

1. Will taking into account the correlation between inter-client communication improve the guarantee, instead of each client independently making a decision for itself. In general, sporadic communications are often correlated.

2. Referring to Def. 4.6, why are the indicator variables not defined as Bernoulli random variables? It seems like they are modeled as Bernoulli variables, but it is not explicitly mentioned anywhere. 

3. In the aggregation step, the clients need to know which nodes communicate to it? In other words, is a blind aggregation where the identity of the participating clients is anonymized, possible? 

Also, some recent works in communication sporadicity is missing: For example, in this work: https://ieeexplore.ieee.org/document/10705313, communication sporadicity is considered in conjunction with privacy constraints, although in a semi-decentralized setting. Privacy is an important aspect of federated learning, and so the paper will benefit with some discussions on the privacy implications of the current algorithm.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper considers decentralized optimization with nodes having varying communication time and computation resources that might also change in time. The paper analyzes convergence rate of proposed framework for strongly convex and non-convex functions and evaluates effectiveness of the framework in experiments.

### Strengths
The paper proposed framework is general and allows for varying resource availability. The paper compares its framework with the baselines.

### Weaknesses
1. The proposed framework does now allow for the slow gradient computation, as gradients cannot be delayed. This is because the framework does not allow for computation and communication sporadicity being correlated (per assumption 4.3.), and according to (2) each gradient has to be computed at the latest local model $\theta_i$. This means that if some node computed the gradient for a long time, and in the meantime local model is being updated due to the communication on this node occurring, the node has to drop its previous computations and start computing its gradient from scratch on the new model so that it can return the gradient at the latest model.

    There are two possible solutions to this: either allow for communication and computation being correlated (i.e. while node computes, no communication happens), or allow for the gradients to be delayed.

    To me this is a big limitation of the framework.

3. Only asymptotic convergence is proven (i.e. when the number of iterations K goes to infinity), while previous frameworks such as (Even 2024) give convergence bound for any number of iterations K.


4. Paper has several flows in presentation: e.g. first it states that framework the paper analyzes is (2), but then actual analyzed algorithm is in equations (3)-(4) that is not equivalent to (2) (difference comes from re-normalization of the diagonal element p_{ii}^k).

5. Convergence rate derived for non-convex functions is hard to understand, as it depends on some parameters $w_1, w_2, w_3, w_4, w_5$ that are defined only in appendix.

6. Paper does not tune the learning rate, but uses the same learning rate for different algorithms - that might give advantage to some algorithms.

7. Experimental comparison to (Even 2024) is missing. Is there a specific reason why you excluded that baseline from comparison?

### Questions
1. Paper mentions that (Even et al 2024) did not consider time variations in resource heterogeneity and I would like to ask you to elaborate on this. In my understanding asynchronous communication allows for resource heterogeneity. 

2. What if in proposition 4.10, d_{max}^{k} = 0 for some k? I think it is allowed by the framework and it would mean that you have to divide by zero? 

3. in line 360 you state that lim_{k ->0} \Phi(k:0) = 0 is enough to prove that consensus error and average error converges to zero, however even in this case, it depends on convergence of $\Psi^{(k)}$ that might be non zero or might even diverge. Can you clarify on that? 

4. Why does the matrix R have to be doubly stochastic if you anyways renormalize the matrix P later to be doubly stochastic?

5. I did not understand how exactly result (10) recovers (Koloskova (2020)) (comment in lines 386 and 387), could you provide a more detailed derivation of this result? also, (Koloskova (2020)) allows for local steps in decentralized SGD, meaning that d_{min} = 0 at those steps, could you compare your result with (Koloskova (2020)) for that local decentralized SGD? Same for the non-convex functions. 

6. How does $w_1, w_2, w_3, w_4, w_5$ depend on the key parameters of the problem (parameters from Assumptions 4.2-4.4). Is there a way to simplify the convergence rate, e.g. by using O-notation? 

7. What does “average total delay occurred ip to iteration k" mean? Is it total simulated time? 

8. In experimental comparison, how exactly are the baseline algorithms implemented under the proposed heterogeneity of communication and computation? How does d_i and b_{ij} translate to the speed of the node?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies decentralized federated learning setting, where a central server is lacking and the agents may perform a stochastic number of local iterations. Furthermore, the peer-to-peer communication also happen in a random fashion. The authors propose a method called DSpodFL, which combines consensus and local gradient descent while allowing stochasticity. The main contribution lies in the algorithm setup/flexibility, convergence analysis using indicator random variable to model stochasticity and allowing for milder assumptions for both convex and nonconvex cases.

### Strengths
The algorithm allows for a very general stochasticity capturing varying communication and computation cost and allows for heterogeneity in agents' capabilities. The algorithm is also written in a very clean fashion. The proofs appear to be mostly right.

### Weaknesses
The proofs in the appendix lacks explanation for the steps.

My main complaint is that while this is a good first step towards allowing different kinds of stochasticity, the proposed algorithm misses the mark in the sense that the value it converges to is not the original optimal solution. There has been a long line of literature in distributed optimization tackling the same setup (without multiple local steps) by including additional error correction terms, (almost) exact convergence can be achieved. A simple counting of the activation frequencies as in the following paper could help reduce the error term in the limit. Because of this, I'm not sure how useful the proposed method would be for any real applications, especially with large amount of heterogeneity in the activations.



### Questions
For the expectation calculations, some of them seems to be conditioned on past realizations, a filtration should be setup to rigorously justify the steps. If this is not the case, please explain. 

How much information is necessary by each of the agents to calculate the learning rates? 

Why should all agents use the same learning rates?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The author present DSpodFL, a unified framework of decentralized federated learning. DSpodFL allows each client to take local update and communication intermittently according to its available resources. And DSpodFL framework also involves some existing decentralized federated learning algorithms. The authors provided the convergence analysis of DSpodFL in convex and nonconvex settings.

### Strengths
1. A unified algorithm framework.

2. Making clients able to take local update and communication according to its available resources.

3. Convergence analysis in both convex and nonconvex scenarios.

### Weaknesses
1. The proposed frame can unify existing algorithms including DGD, DFedAvg and RG. If we can obtaining the convergence analysis of these existing analysis **directly** from Theorem 4.11 and 4.12? And if the convergence rates of the existing algorithms obtained from Theorem 4.11 and 4.12 **match** the existing convergence analysis? Please present the detailed steps.

2. Figure 2(b) only show the convergence curves when $\tau\in[0,10000]$, and DSpodFL only achieve the test accuracy of about **0.6** during this period. So can the authors provide convergence curves of these algorithms with a larger $\tau$ such as 20000 or 30000? Similarly, can the authors provide the convergence curves of Figure 2(c) with a larger $\tau$?

3. How do the algorithms including DSpodFL perform in test accuracy with respect to wall-clock time?

### Questions
1. The proposed frame can unify existing algorithms including DGD, DFedAvg and RG. If we can obtaining the convergence analysis of these existing analysis **directly** from Theorem 4.11 and 4.12? And if the convergence rates of the existing algorithms obtained from Theorem 4.11 and 4.12 **match** the existing convergence analysis? Please present the detailed steps.

2. Figure 2(b) only show the convergence curves when $\tau\in[0,10000]$, and DSpodFL only achieve the test accuracy of about **0.6** during this period. So can the authors provide convergence curves of these algorithms with a larger $\tau$ such as 20000 or 30000? Similarly, can the authors provide the convergence curves of Figure 2(c) with a larger $\tau$?

3. How do the algorithms including DSpodFL perform in test accuracy with respect to wall-clock time?

I will update the scord according to the response during the discussion period.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper develops a generalized algorithmic framework, DSpodFL, for decentralized federated learning (DFL), which effectively integrates the heterogeneity and dynamics of local stochastic gradient descents (SGDs) and aggregation processes. The convergence of DSpodFL is analyzed for both strongly convex and nonconvex loss functions. Additionally, numerical experiments on various datasets demonstrate the advantages of the proposed method.

### Strengths
1.	The investigated problem is novel, as the authors address the combined effects of sporadic local client computations and inter-client communication, an aspect previously unexplored in DFL.

2.	The presentation of the paper is clear. The authors provide rigorous convergence results for both strongly convex and nonconvex settings, which are well-justified.

3.	The numerical experiments are sufficient and effectively showcase the advantages of the proposed DSpodFL framework.

### Weaknesses
1.In Section 3.3, why the random matrix $P^k$ is doubly stochastic and symmetric? This is not immediately clear, and providing a proof and an illustrative example would enhance understanding.

2.In Assumption 4.1, the gradient diversity is measured by $ || \nabla F(\theta) - \nabla F_i(\theta) ||$, while in Assumption 4.2, it is measured by $ ||\nabla F_i(\theta) ||$.What is the rationale behind this distinction?

3.In the analysis with a diminishing learning rate, why does exact convergence require an increasing frequency of SGDs over time? Moreover, the dependence of SGD probabilities on the stepsize seems unrealistic. Why does this requirement not apply when using a constant stepsize?

### Questions
Perhaps $p_{ii}^k = 1 -\sum_{j \in M} r_{ij} \hat v_{ij}^k + r_{ii} \hat v_{ii}^k $ in equation (4)?

### Soundness
4

### Presentation
3

### Contribution
3
