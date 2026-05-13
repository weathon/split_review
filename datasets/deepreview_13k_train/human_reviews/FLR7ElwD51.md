# Learning Scalable Causal Discovery Policies with Adversarial Reinforcement Learning

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Learning the structure of causal graphs from observational data is a fundamental but challenging problem. Existing works focus on designing search-based methods for finding optimal causal graphs. However, search-based methods have proven low-efficient since they are naturally limited by the burdensome computation of decision criteria at every step. Consequently, they can hardly scale to larger tasks. This paper proposes a novel framework called AGCORL to learn reusable causal discovery policies, which can zero-shot generalize to related tasks with much larger sizes. Specifically, AGCORL employs an Ordering Learning (OL) agent to directly infer the order of variables taken from the observational data as input. To further improve the generalizability of the OL agent, an ADversarial (AD) agent is employed to actively mine tasks where the OL agent fails to find high-quality solutions. We theoretically prove that the AD agent significantly reduces the number of required tasks to achieve generalizability of the OL agent. Extensive empirical evaluations demonstrate the superiority of our method in both runtime and solution quality over the state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an adversarial reinforcement learning framework for efficient causal discovery on observational data. The framework consists of two agents, OL (ordering learning) and AD (Adversarial agent), respectively, in a zero-sum setting in which AD is adding the tasks that OL has most room to improve in performance. Authors show both theoretically and empirically that the adversarial agent helps for better generalisability with higher data efficiency, and their approach is comparable or better to the previous approaches.

### Strengths
-The paper is very well written.  So clarity is in general very good. 

- This is a well-defined and a very important area of AI research, hence it is very relevant. 

-The approach is interesting and certainly original, and the results are in general promising. Significance is non-trivial although limited (see weaknesses).

### Weaknesses
 -Code is not shared so the results are irreproducible. 

- So many nodes but so little edges. E.g. Only 2 and 5 Table 1. and 1 to 4 with Table 2. This makes me skeptical about the relevance of the results. (See questions)

-   the construction of adversarial graph is unclear to me.  Caption of Figure 3 attempts to explain how does it work, but it is not clear to me still. It should be improved. (See the question)  In general would be great to write down the general procedure. (if it's already there, apologies).


-It would be good give high level intuition on how the employed pruning algorithm works (especially at the end of the deployment subsection). Currently, just referring to the appendix without sharing the idea obscures it. 



Minor issues: 

-  typo at conclusion : AL -> AD

### Questions
-Maybe a silly question but  could you help me understand  Figure 3: how does the action sets and added nodes and the edge works?  (Please also revise the text to make it more clear.)

-So many nodes but so little edges. E.g. Only 2 and 5 Table 1. and 1 to 4 with Table 2. I wonder how does your results are when  it comes to different sparsity, node vs edge is more balanced, or dense?

### Soundness
3 good

### Presentation
3 good

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
The paper proposes an adversarial reinforcement learning framework for causal structure learning named AGCORL. 
AGCORL mutually trains an order learning agent (OL agent) and an adversarial agent (AD agent). 
The OL agent learns a general policy that infers the causal order of variables, while the AD agent generates challenging tasks for the OL agent. 
The trained OL agent avoids calculating the computationally expensive Bayesian Information Criterion (BIC score), making it suitable for large-scale tasks. 
Experiments show that the trained OL agent can generalize to new tasks that are different from the tasks used in training.

### Strengths
- The proposed Ground Truth Reward (GTR) enables AGCORL to efficiently train both agents without calculating the time-consuming BIC score.

- The OL agent shows good scalability ($t$ in Table 2). 
Additionally, an OL agent trained on one task can transfer to other tasks. 
In particular, it maintains good performance when transferred to tasks with different noise (Table 5).

### Weaknesses
 - The OL agent is trained on synthetic data generated by an explicit Structural Causal Model (SCM).
Therefore, the OL agent may not be suitable for real-world data tasks where we do not know the mathematical relationship between the variables.
In such cases, the authors suggest to use multiple OL agents trained with different function types to infer candidate orderings, and then calculate their BIC score to select the best one (Appendix E).
However, this approach could compromise the fast running time, which is a main advantage of the proposed work.

- The paper lacks theoretical and/or qualitative explanations that compare the BIC score and the newly proposed GTR.
It seems important to clarify whether GTR can always be a surrogate for BIC.
If so, AGCORL could replace frameworks that calculate the BIC score, even for small-scale tasks.
If not, in certain circumstances, it will still be necessary to use BIC score based algorithms, even for large-scale tasks.

- Theorem 1 in Appendix A only shows that a random adversarial agent is the worst for training a generalizable order learning agent.
It does not provide any indication of how good the authors' proposed AD agent is.
For example, a theoretical analysis revealing how far the proposed AD agent's $\zeta$ is from 0.5, with some probability, would be helpful.

### Questions
- Is there any measure other than the Structural Hamming Distance (SHD) that can distinguish between missing edges and reversed edges? 
The authors argue that the OL agent is generalizable to large tasks based on the observation that the True Positive Rate (TPR) only decreases slightly (Table 4). 
However, in the same table, the SHD increases. 
If the SHD increases because of a large number of reversed edges, it is difficult to conclude that the OL agent generalizes to large tasks.

- Does AGCORL outperform previous BIC score-based algorithms on small-scale tasks too? 
If so, can we safely say that AGCORL replaces previous BIC score-based algorithms in all cases?

- For the same $d$ and $\theta$, how does the time complexity of computing the BIC score differ from that of Algorithm 1?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose AGCORL, an RL based approach to directly output the topological order from an input dataset. The adversarial component generates graphs that are difficult for the ordering agent to learn. The training data is generated from a particular set of SCMs (e.g., linear or GP models).

### Strengths
The paper proposes a RL formulation of learning the topological order from an input observational dataset. At each step, the agent takes an action of taking a variable and adding it to the ordered set. The adversarial agent attempts to generate graphs such that the ordering agent achieves low reward. The authors in the experiments show that the agent generalizes to larger graph distributions than in training. They also show that on a real-world protein dataset, they achieve the lowest SHD, showing some promising generalization beyond the training distribution.

### Weaknesses
### Clarity

Overall, I found the paper easy to read and follow. However, I think the writing in certain sections can be improved. For example, the related work does not explain the prior works CORL in enough detail. It would be good if the text made more efforts to explicitly distinguish their work from CORL. It is not currently clear to me what precisely the innovation is relative to CORL. Moreover, it would also make it easier to interpret why AGCORL and CORL have such different runtimes.


### Experiments

One weakness in the experiments is that the authors only attempt to test generalization to larger graph instances. However, one limitation of AGCORL is that the training data itself is synthetic (so limited to linear gaussain or GP SCMs). The authors only test on the same SCM distributions. It is not clear what would happen if a different distribution of SCMs arrives at test time (e.g., what if the test SCM used a different GP kernel than during training). In these cases, the baselines might do better. Or what if the graph distribution at test time is not ER or scale-free? More experiments understanding generalization would be useful.

Re metrics:
Since AGCORL only learns the topological ordering, why don't the authors use metrics that test the how good the ordering is relative to the true ordering? Using variable selection on top of the learned ordering seems to make the results harder to interpret as it is not clear whether the errors are due to the wrong ordering or wrong variable selection.  

Re contribution of the adversarial component:
In Fig. 4 left, the authors show the impact of the adverarail training. However, the curves in Fig 4 do not in themselves suggest that adversarial training helps. What would be useful is training AGCORL with and without the adversarial parts and comparing the metrics. What we care about is whether the metrics at test time graphs improve or not.

Type in section 5.2: Table 3 -> Table 2.

### Questions
Re reinforcement learning formulation:
Can the authors comment on why they chose to formulate this as an RL problem as opposed to a supervised learning task? The state is a tuple of $ < s^{+}, s^{-} >$ which means that for a given action $a$, the next state can be deterministically computed. This is quite different from a standard RL setup where the states are stochastically generated by the environment using $p(s_{t+1}|s_t, a_t)$. Moreover, you only get a reward after the entire episode ends (i.e., you have the full ordering). So it seems like you could also just treat this is a supervised learning problem where you directly output an ordering. The challenge is probably computing a differentiable loss between the true ordering and predicted ordering. I think many existing losses exist in the literature for this task. Can the authors comment on this? It seems like directly using supervised formulations might be more efficient (since this RL formulation is essentially like zeroth-order optimization to learn the ordering). 

Re runtime:
In Table 2, why does AGCORL take 11m to run for a 30-node DAG? Whereas in Table 1, it takes 19.2s for a 100-node graph. At inference time, my understanding is that you take the trained policy agent and just take d-steps to compute the ordering. So why is it slower for a 30-node DAG?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces AGCORL, a new method for learning causal graph structures from observational data. Unlike traditional search-based methods, AGCORL focuses on training reusable causal discovery policies that can generalize to larger tasks efficiently. It uses an OL agent to deduce variable order directly from data and an AD agent to enhance the OL agent's generalizability. The paper shows that AGCORL outperforms existing methods in terms of runtime and solution quality through theoretical and empirical evaluations.

### Strengths
- The introduction, related work, and preliminary parts are well organized and clearly conveyed.
- Using an adversarial RL framework to learn the causal graph from observational data seems relatively novel in this field.

### Weaknesses
Starting from section 4, the writing of this paper becomes quite chaotic. The authors did not introduce the technical background of how to combine RL and causal discovery, which left me feeling lost. Many symbols are used without prior definitions. I still do not understand what 'tasks' refers to in this paper.

- The most important aspect of this paper is the introduction of a method using adversarial samples to guide network training. Furthermore, it designs an AD agent to generate a ground-truth graph used as a reward. However, how can we ensure that the tasks generated by this AD agent are helpful to the learning of the OL agent?
- In the paper, a combination of adversarial learning and reinforcement learning is used for training. It's well-known that the convergence of these two methods is a significant challenge. Are there any techniques that can help the convergence of the algorithm?
- The generalizability of DAG learning is a rather werid concept. Why is it that actions can be generalized from a small graph to a larger one? Does this require certain assumptions? Do the causal mechanisms need to be consistent? Can actions learned on linear data be generalized to nonlinear data?
- In the experimental section, the authors only used 500 observations for 50 nodes and 100 nodes. This setting is somewhat challenging. What if we increase the number of observations? Or reduce the number of nodes?
- Why wasn't Notears-MLP compared for nonlinear data? In my experience, this method is actually more robust.
- Do the authors consider this time comparison to be fair? You not only need to find the order but also apply methods like CAM for further pruning. As a DAG learning method, this time also needs to be counted in. Moreover, RL-based methods are indeed quite slow. It would be helpful if the authors could provide some training logs.
- Maximizing the BIC score to learn a causal graph is theoretically grounded and can ensure identifiability. So, how can the method learned using the AD agent ensure that the ground-truth graph is learnable?

### Questions
- The most important aspect of this paper is the introduction of a method using adversarial samples to guide network training. Furthermore, it designs an AD agent to generate a ground-truth graph used as a reward. However, how can we ensure that the tasks generated by this AD agent are helpful to the learning of the OL agent?
- In the paper, a combination of adversarial learning and reinforcement learning is used for training. It's well-known that the convergence of these two methods is a significant challenge. Are there any techniques that can help the convergence of the algorithm?
- The generalizability of DAG learning is a rather werid concept. Why is it that actions can be generalized from a small graph to a larger one? Does this require certain assumptions? Do the causal mechanisms need to be consistent? Can actions learned on linear data be generalized to nonlinear data?
- In the experimental section, the authors only used 500 observations for 50 nodes and 100 nodes. This setting is somewhat challenging. What if we increase the number of observations? Or reduce the number of nodes?
- Why wasn't Notears-MLP compared for nonlinear data? In my experience, this method is actually more robust.
- Do the authors consider this time comparison to be fair? You not only need to find the order but also apply methods like CAM for further pruning. As a DAG learning method, this time also needs to be counted in. Moreover, RL-based methods are indeed quite slow. It would be helpful if the authors could provide some training logs.
- Maximizing the BIC score to learn a causal graph is theoretically grounded and can ensure identifiability. So, how can the method learned using the AD agent ensure that the ground-truth graph is learnable?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
