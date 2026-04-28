# Bandits with Replenishable Knapsacks: the Best of both Worlds

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The bandits with knapsack (BwK) framework models online decision-making problems in which an agent makes a sequence of decisions subject to resource consumption constraints. The traditional model assumes that each action consumes a non-negative amount of resources and the process ends when the initial budgets are fully depleted. We study a natural generalization of the BwK framework which allows non-monotonic resource utilization, i.e., resources can be replenished by a positive amount. We propose a best-of-both-worlds primal-dual template that can handle any online learning problem with replenishment for which a suitable primal regret minimizer exists. In particular, we provide the first positive results for the case of adversarial inputs by showing that our framework guarantees a constant competitive ratio $\alpha$ when $B=\Omega(T)$ or when the possible per-round replenishment is a positive constant. Moreover, under a stochastic input model, our algorithm yields an instance-independent $\tilde \cO(T^{1/2})$ regret bound which complements existing instance-dependent bounds for the same setting. Finally, we provide applications of our framework to some economic problems of practical relevance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of bandits with knapsacks (BwK). In a BwK problem, there are m (m > 1) different types of cost for each action, and the agents needs to maximize the cumulative rewards (i.e., minimize the cumulative regret) before any resource runs out. In classic bandit setting, there is only one cost which is time, so the standard MAB problem is a special case of BwK.

In this paper, the cost of each action can be negative, whereas the previous BwK works only study the cases where the costs are non-negative. This new setting simulates the real-world applications (eg inventory management and Bilateral trade given in the paper) where the resources can be recovered with time. 

This paper gives a general primal-dual algorithms for this new setup. In both of adversarial and stochastic bandit settings, this paper achieves nearly optimal results (linear gaps for adversarial and logarithm gaps for stochastic). To be specific, in the adversarial case, no algorithm can achieve sub-linear regrets, and the proposed algorithm only has constant gap to the lower bound. In the stochastic case, the algorithm achieves \tilde{O}(\sqrt{T \log{mT}}) regret upper bound (note that the trivial lower bound is \Omega(\sqrt{T})).

### Strengths
1. This paper proposes and studies a novel and interesting problem. It is pretty smart to consider the case where the cost of an arm could be negative. 

2. The results are rich and good. It studies multiple cases, and provides good results for them. The results look good enough from my understanding and knowledge.

### Weaknesses
This paper has one major weakness, and one minor weakness about presenting.

1. It is not well discussed or stated how the negative cost could affect the problem. Is this new setup invalidate the existing algorithms, or it creates major challenges where we cannot simply use the existing algorithms or the regret analysis techniques? The algorithm looks pretty similar to the existing works, so as the regret bounds. From the current writing, I am not able to tell how hard the new setting is. Specifically, the paper lacks a discussion on whether standard primal-dual approaches for BwK can be directly applied or if the negative costs require a fundamental change in the algorithmic design and analysis. It's unclear if simply adding a 'void' action when resources are depleted is sufficient, or if this new setting introduces unique challenges that render existing regret minimization techniques ineffective. The paper needs to explicitly address this by providing concrete examples or counterexamples to demonstrate the limitations of existing methods when dealing with negative costs. It should also clarify whether the similar regret bounds are achieved through a straightforward adaptation of existing analysis or if it requires novel proof techniques.

2. This paper's writing and presenting need improvement. It is not clearly presented. For me, there are two major challenges. 
i) There are too many notations and many of them can be avoided. For instance, in Theorem 4.1, it defines \alpha = \nu/(1+\beta), which is not necessary at this point but makes this paper less easier to perceive. 
ii) I do not find the clear definition of NextElement(), which makes Algorithm seem incomplete. I did a search of "next" but did not find any definition. Probably it is hidden in some sentences, but it is better to have a clear statement of it.

### Questions
It is not well discussed or stated how the negative cost could affect the problem. Is this new setup invalidate the existing algorithms, or it creates major challenges where we cannot simply use the existing algorithms or the regret analysis techniques?

### Soundness
3 good

### Presentation
2 fair

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
This paper studies an extension of Bandits with Knapsacks, called Bandits with Replenishable Knapsacks (BwRK). It proposes a primal-dual algorithm addressing both the adversarial and stochastic cases, with competitive ratio and regret upper bound analysis. The paper also discusses application examples of BwRK and its results.

### Strengths
- Well-motived model formulation. BwRK is an interesting extension of BwK, and the authors provide application examples as well (Sec. 6). 
- Algorithmic framework. The authors propose a primal-dual template (Alg. 1) that can be applied with various minimizers under different scenarios.

### Weaknesses
 - The theoretical results are not clearly discussed. For example, how tight are the theoretical results compared to lower bounds? Specifically, the paper claims to achieve the "best of both worlds" by addressing both adversarial and stochastic settings, but it is unclear how the performance bounds in these two settings relate to known lower bounds for these problems. The paper should explicitly state the lower bounds and then demonstrate how the proposed algorithm matches them. It would be beneficial to provide a more detailed comparison of the regret and competitive ratio achieved with the known lower bounds in both adversarial and stochastic settings.
- Lack of experiments. It would be interesting to know the empirical performance of the proposed algorithm. Especially compare the actual performance of this paper's algorithm with known ones in BwK when $\beta=0$. Are they exactly the same algorithms? It is unclear how the algorithm's performance scales with the problem parameters, and the paper lacks any empirical validation to support the theoretical claims. It would be important to see how the algorithm behaves in practice, especially when compared to baseline algorithms, even if those baselines are adapted to this new setting.

### Questions
- From my aspect, "the best of both worlds" means that the proposed algorithm can achieve optimal theoretical guarantees in two different settings. Could the authors point out how their theoretical upper bounds match the lower bounds in these two settings? As BwRK is a new model, do we have such lower bounds?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of BwK under replenishable knapsack assumption, where the budget consumption in each round could be negative. The authors propose and analyze a primal-dual framework, achieving best-of-both world performance.

### Strengths
The problem setup is clearly motivated and introduced. The algorithm and analysis are thoroughly explained and neatly presented. Regret bounds improves on existing results.

### Weaknesses
I believe there are some related work that could be beneficial to be added to the comparison. The line of work I would like to mention is the bandits with (soft) constraints. The authors argue that $\textit{in BwK problems constraints are required to be satisfied strictly at all rounds}$. However, when allowing negative $c_t$s, it is essentially allowing constraint violation in those rounds. The core issue is that while the *global* budget $B_t$ must remain positive, the per-round consumption $c_t$ can be negative, which effectively permits temporary constraint violations at specific rounds as long as the cumulative budget remains positive. This distinction, while subtle, significantly alters the problem's nature and its relationship to soft-constrained bandit problems. Specifically, the algorithm's behavior when $c_t$ is negative needs more discussion, especially in how it relates to the constraint satisfaction. The current analysis does not fully explore the implications of negative $c_t$ values on the algorithm's performance and its connection to the soft-constraint framework. Furthermore, the practical implications of allowing negative $c_t$ values, and how this might be interpreted in real-world scenarios, should be addressed.

### Questions
1. Any lower bound results?
2. Connection and comparison with soft constraint satisfaction? It seems to me that allowing negative budget consumption is somewhat related to constraint violation in such round, so the results should be comparable.
3. Optimizing the coefficients in the regret bound? In bandits these are hidden in the big O term most of the times, but it could be pretty large in many cases, especially when T is not very large. Alternatively, without theoretical justification, some experiments showing that the bounds are empirically tight would be very helpful.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the bandits with replenishable knapsacks (BwRK), building upon a framework introduced in Kumar and Kleinberg (2022). This paper presents a "best-of-both-worlds" algorithm to address such a learning problem. Furthermore, it conducts theoretical analyses of the algorithm under two distinct scenarios: adversarial inputs and stochastic inputs. Finally, this paper presents an exploration of potential economic applications.

### Strengths
(1) This paper presents, for the first time, a best-of-both-worlds algorithmic design for bandits with replenishable knapsacks, accompanied by the corresponding theoretical analysis.
(2) This paper provides the first instance-independent regret bound under i.i.d. inputs. This complements the earlier work of Kumar and Kleinberg (2022), which primarily focused on instance-dependent analysis in the initial BwRK paper.

### Weaknesses
 (1) There are some implicit assumptions that are not well justified. Firstly, the authors say that B=\omega (T) which seems not practical as it is not evident in which real-world situations a direct linear relationship exists between the budget and the total number of rounds T. A constant budget will result in a non-sublinear final upper regret bound. Secondly, the range of the replenishable resource \beta is [-1,0] which indicates that such amount of source is close to the consumption cost of other action. This, in turn, suggests that the policy will frequently favor the empty action once the budget B is depleted. It would be beneficial to offer motivating real-world scenarios that illustrate the relevance and feasibility of such a resource range. Finally, in the example of the inventory management in Section 6.2, the reward action s is r_t(s)\in [-1,0] which is not consistent with the setting in Section 2. Please give a clear justification for this variation.
(2) The Meta-Algorithm proposed in this paper appears to be a trivial extension of the one presented in "Online Learning with Knapsacks: the Best of Both Worlds" (2022). The main difference is that the policy does the empty action when the budget is smaller than one. Furthermore, in terms of theoretical analysis, although the concept of a replenishable resource is introduced, the proofs for Theorem 4.1 and Theorem 4.3 do not exhibit significant advancement when compared to the proofs for Theorem 6.1 and Theorem 7.1 of the 2022’s work. Please clarify the primary contribution compared with previous literature.
(3) The paper would benefit from the design of experiments to provide stronger empirical support for the theoretical findings.
 
Minor Comments:
Page 4: note --> Note
Page 9: simple simple --> simple

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
