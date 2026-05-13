# Online Laplacian-Based Representation Learning in Reinforcement Learning

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Representation learning plays a crucial role in reinforcement learning, especially in complex environments with high-dimensional and unstructured states. Effective representations can enhance the efficiency of learning algorithms by improving sample efficiency and generalization across tasks. This paper considers the Laplacian-based framework for representation learning, where the eigenvectors of the Laplacian matrix of the underlying transition graph are leveraged to encode meaningful features from raw sensory observations of the states. Despite the promising algorithmic advances in this framework, it remains an open question whether the Laplacian-based representations can be learned online and with theoretical guarantees along with policy learning. To answer this question, we study online Laplacian-based representation learning, where the graph-based representation is updated simultaneously while the policy is updated by the reinforcement learning algorithm. We design an online optimization formulation by introducing the Asymmetric Graph Drawing Objective (AGDO) and provide a theoretical analysis of the convergence of running online projected gradient descent on AGDO under mild assumptions. Specifically, we show that if the policy learning algorithm induces a bounded drift on the policy, running online projected gradient descent on AGDO exhibits ergodic convergence. Our extensive simulation studies empirically validate the guarantees of convergence to the true Laplacian representation. Furthermore, we provide insights into the compatibility of different reinforcement learning algorithms with online representation learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new algorithm for efficient online learning of laplacian representations for RL.  Under benign assumptions, the authors prove convergence to the laplacian eigenvectors.  Finally, authors provide some simple gridworld experiments showing that the algorithm performs as intended, in accordance with the assumptions (eg. it works worse when policy update is less stable).

### Strengths
The paper is well written, with a clear survey of the ideas that lead to the solution.

Authors consider an interesting problem of efficiently learning representations that dynamically adjust as policy learning occurs.  We could use existing algorithms for this task by performing an expensive representation learning step every time a policy update occurs, but this is impractical.  

The algorithm seems like a practical extension of existing work.

As far as I can tell (did not read the proofs in the appendix) the paper is theoretically grounded.

The ablations to evaluate how the assumptions translate into actual performance is appreciated.

### Weaknesses
It is not entirely clear how much the theoretical contribution of this work relies on the existing work of Gomez et al. (2023).  Given this contribution is primarily theoretical, and the actual algorithmic contribution to convert the existing offline approaches to an online algorithm seem reasonable, but mostly direct, the value of the contribution rests primarily on the theory. To me, it appears that there is enough of a contribution here.

The experiments seem more like debug/sanity check experiments.  They are useful for convincing the algorithm works beyond asymptotics of theory but don't provide a compelling case that the method is actually useful.  Without a stronger theoretical contribution, a more comprehensive experimental section (more challenging environments and a setting where the learned embeddings are used) would be helpful to showing the value of this method.

### Questions
Why is cosine similarity the only thing observed in the experiments?  It seems like the core point of learning
representations online is to be able to use them.  Unless I am misunderstanding, the policy here can be anything,
and does not use the representations.  I think the paper would be strengthened with an example showing 
how the ability to adjust the representations online improves the actual task, whether that means that the policy
acts on the representations or it is part of exploration (eg. only used in the exploration part of epsilon greedy).

Typos:
214:  These should be eigenfunctions/eigenvectors, not eigenvalues.
341: non-> none

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work studies learning the policy and the Laplacian representation of the transition dynamics simultaneously in online RL. The authors propose an asymmetric graph drawing objective and show that online projected gradient descent on this objective achieves ergodic convergence.

### Strengths
The proposed method enables updating the Laplacian representation simultaneously with the policy. The online PGD algorithm enjoys theoretical convergence guarantees.

### Weaknesses
The problem of learning Laplacian representation in RL doesn't seem to be a super important question itself, because it doesn't really scale up to real-world, challenging settings where the state space is large. The experiments focus on a slightly toy environment and only evaluate the accuracy of the Laplacian learning, without demonstrating how online Laplacian representation learning can benefit RL (more than previous methods).

### Questions
How does online Laplacian representation learning benefit RL (more than previous methods) in practical RL applications?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work considers the problem of online representation learning in MDPs.  Building on past work that uses the standard Laplacian graph embedding on the weighted graph induced by the Markov chain associated to a given policy as a representation of the MDP, this paper introduces a new objective that allows for learning when the policy is being updated, as occurs during training of an RL agent.  More precisely, the authors introduce the Asymmetric Graph Drawing Objective, which seeks to produce a graph embedding from the Laplacian of the graph induced at step $t$ of some fixed RL algorithm.  Under assumptions on reachability and bounded drift, as well as technical assumptions on the graph structure, the authors then prove that the desired Laplacian imbedding is the unique stable equilibrium under gradient descent dynamics for a fixed time $t$.  The authors then demonstrate convergence to an approximate first-order stationary point under the bounded drift assumption on the RL algorithm.  The authors conclude with an empirical analysis of their algorithm on Gridworld, where they compare their proposal with the earlier Augmented Lagrangian Laplacian Objective as well as conducting an ablation study to empirically examine the necessity of their assumptions.

### Strengths
This paper introduces a novel variant of a previous representation learning objective that is simple and intuitive.  They demonstrate that running gradient descent on their objective has nice properties under several technical assumptions and demonstrate empirically the efficacy of their method.

### Weaknesses
I think that there are three main weaknesses:

1. I think that Assumption 1 is extremely strong.  The irreducibility of the Markov chain induced by a policy being ergodic is already a strong assumption, and lower bound on the stationary distribution's mass at any given state is even more so, but the part I think is strongest is that this is essentially an *all policy* requirement.  While reachability assumptions are often invoked in RL theory, they are usually state-dependent in the sense that for every state, there is some policy that does a good job of reaching that state; the current assumption is that every state is visited sufficiently frequently by every policy, which seems very difficult to guarantee.  Note that the authors do not literally assume this, as their Assumption 1 is restricted to policies produced by the RL algorithm, but it is very difficult to control what policies an arbitrary RL algorithm will visit.  The paragraph below this assumption allows for some slight weakening, where Assumption 1 only has to hold on the support of the initial stationary distribution, but this still seems to impose an extremely strong restriction on the ability of the RL algorithm to explore, especially as I expect that $\rho_{\min}$ would figure polynomially into any quantitative bound (as it indeed does in Lemma 2(d)).

2. While it is nice that the authors demonstrate convergence to the Laplacian embedding, and I understand that this embedding is frequently used in visualizing graphs, it would be nice if the authors provided more motivation for why this is a reasonable objective for which to strive.

3. The experiments seem to suggest that AGDO and ALLO behave extremely similarly; for example, the GridRoom-4 line in Figure 3 looks like the same curve in both (a) and (b).  If this is the case, I am confused as to what the empirical takeaway is here and what the purpose of using AGDO over ALLO is.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper reveals an important observation from Klissarov & Machado (2023): Learning the representation in an online manner provides better exploration and total rewards. Motivated by this, the author proposes the online optimization formulation of GDO and gives some theoretical analysis.

### Strengths
This paper extends the existing setting of Laplacian representation to the online optimization framework and provides a convergence analysis.

### Weaknesses
The theoretical results are not satisfying and over-simplified. 
1. The assumption 1 is not realistic for the reinforcement learning senario. It is known that the optimal policy could be a deterministic policy, which means that $\rho_{\min}$ could be zero in many deterministic environments. The relaxion discussed in the following paragraph doesn't ensure that $\rho_{\min}$ is non-zero. A possible solution is to add a small uniform perturbation to all policies.
2. Proposition 1 is a relatively loose upper bound, which nearly removes all dependence on the time $t$. The main motivation of this paper discusses the benifits of online optimization framework; however, this motivation is not presented in the final convergence analysis. It is because the only connection to the time $t$ is simply omitted in this step. 
3. The theoretical analysis doesn't bring anything new to this field. It simply uses the smoothness of the objective function $\mathcal{L}$,  and follows the same steps of standard optimization paper.
4. Moreover, Eq. (44) doesn't implies the upper bound is $O(\frac{1}{T})$. It contains the term $\sum_{t} \delta^{(t)}_{\mathcal{L}}$. The author simply assumes it is less than infinite in Assumption 2. But this assumption has never been made in the TRPO and PPO paper. Making such assumption requires the learning rate of the policy-based algorithm to be approperiately choosen. The author didn't reflect the impact of this assumption in the final bound and presents the $O(1/T)$ convergence rate.

### Questions
I hope the author addresses my concerns in the weakness section.

### Soundness
3

### Presentation
2

### Contribution
1
