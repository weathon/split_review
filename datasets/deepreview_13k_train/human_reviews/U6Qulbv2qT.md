# Provable Benefits of Multi-task RL under Non-Markovian Decision Making Processes

- Decision: Accept
- Scores: 8, 6, 8, 6, 6

## Abstract
In multi-task reinforcement learning (RL) under Markov decision processes (MDPs), the presence of shared latent structures among multiple MDPs has been shown to yield significant benefits to the sample efficiency compared to single-task RL. In this paper, we investigate whether such a benefit can extend to more general sequential decision making problems, such as partially observable MDPs (POMDPs) and more general predictive state representations (PSRs). The main challenge here is that the large and complex model space makes it hard to identify what types of common latent structure of multi-task PSRs can reduce the model complexity and improve sample efficiency.
To this end, we posit a {\em joint model class} for tasks and use the notion of $\eta$-bracketing number to quantify its complexity; this number also serves as a general metric  to capture the similarity of tasks and thus determines the benefit of multi-task over single-task RL. We first study  upstream multi-task learning over PSRs, in which all tasks share the same observation and action spaces. We propose a provably efficient algorithm  UMT-PSR for finding near-optimal policies for all PSRs, and demonstrate that the advantage of multi-task learning manifests if the joint model class of PSRs has a smaller $\eta$-bracketing number compared to that of individual single-task learning. We also provide several example multi-task PSRs with small $\eta$-bracketing numbers, which reap the benefits of multi-task learning. We further investigate downstream learning, in which the agent needs to learn a new target task that shares some commonalities with the upstream tasks via a similarity constraint. By exploiting the learned PSRs from the upstream, we develop a sample-efficient algorithm that provably finds a near-optimal policy. Upon specialization to the examples used to elucidate the $\eta$-bracketing numbers, our downstream results further highlight the benefit compared to directly learning the target PSR without upstream information. Ours is the first theoretical study that quantifies the benefits of multi-task RL with PSRs over its single-task counterpart.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the (upper-bound) benefits of multitask learning in PSR environments vs per-task single-task learning. The setting is episodic RL and the proposed algorithm constructs and refines a confidence set of candidate environment parameters, and in each iteration uses those parameters to compute the data collection policy.

Besides introducing the RL algorithm for multitask learning, the paper gives performance bounds for multitask learning and transfer to downstream tasks. It also explores the bounds in specific PSR settings, compared to bounds from using separate RL methods for each task. The comparisons highlight the advantages of the multitask approach.

The key algorithmic idea is to maintain a joint confidence set for the potential per-task environments, and the key technique used in the bound is considering a covering number of this confidence set. The log of this covering number grows slower or sometimes much slower with the number of tasks, than the sum of log-covering numbers of separate, per-task confidence sets.

### Strengths
The paper is well written and clear. Overall I am happy with this paper. It is clearly written and easy to follow. My reading of the contributions is that they offer a better understanding of multitask PSR problems more than offering a solution to multitask learning in PSRs. This is mostly because the PSRs are assumed to be given and the algorithm uses components that are useful for a theoretical study but tricky to set up in practice (Though it would be great to hear from the authors with details if they disagree.) To me the main takeaway is that, through studying upper-bounds, we can say that multitask PSRs are easier to learn (jointly), with interesting examples of shared structures across tasks that accelerate learning.

### Weaknesses
I do not see any issues with the paper.

### Questions
There is another family of PSRs that I would like to suggest as an example (from personal experience) and they can be relevant for the current and future work:
* A set of tasks that is not observed uniformly. We still want uniformly good behavior on all the tasks, but the algorithm can only sample the tasks from a distribution, rather than go over each of them one by one in each iteration. This is highly relevant to how we train RL agents in POMDPs with procedural generation of the initial state, because procedural generation gives very coarse control over the resulting initial state distribution. Here, I am seeing each initial state in the support of the distribution as a task. The downstream learning is also interesting for this.
* A single PSR with block structure in the dynamics. This is like the example above, but the multiple tasks are not explicitly recognized as such.

Some things I would like to see in the downstream regime:
* What impact does more and more training on the upstream tasks have on the zero-shot performance on the downstream task?
* What impact does more and more training on the upstream tasks have on the speed of learning on the downstream task? It would be a surprising and interesting find if some amount of "pre-training" upstream would actually improve the rate of convergence of the downstream. I guess it's more likely that the guarantee would be like "if you want to train for a given budget X downstream, then you can get good rates if you train for Y amount of experience upstream."

At a higher level, not as a criticism to the paper, though, I find the overall setting a bit odd. The proposed algorithm does not have any sequential interaction with the environment. Instead it runs the policy in the tasks for collecting data and updates its confidence set. What I find odd is therefore that the tasks can be so hard intra-episode that there is nothing we can do by adapting as we act, and we might as well pick policies, deploy them, and update. I guess the setting also does not quite apply to the kinds of environments that would be "easy" and where intra-episode adaptation could help improve performance.

I liked the fact that the results allow us to recover the batch setting when we train on N copies of the same task.

I am somewhat confused about what $\pi(\omega_h)$ means in Eq. 2, considering that $\pi$ for the end of the episode $\omega$ depends on what happened in the beginning of the episode ($\tau$). So how does $\tau$ factor into Eq. 2?

It would also be nice to understand the relationship between r from Definition 1 and multiple tasks. Considering the correspondence between block-dynamics and multiple tasks I mentioned above (that is, multiple tasks can be put together into a single POMDP that samples the task as part of the initial state), what is the relationship between r and N? r is arguably harder to scrutinize than N and the shared structure between tasks, so maybe it's possible to get rid of r as a proxy for multiple tasks and formalize everything in multitask terms?

Typos:
* I was a bit confused reading algorithm one because it refers to quantities that are defined after it is shown ($\nu^{\pi_n,k}$).
* In Example 3, the P for the core tasks seem to be on the wrong font type?

### Soundness
3 good

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
This paper studies the problem of multi-task reinforcement learning under non-Markovian decision making process. By assuming the multi-tasks share the same action and observation spaces, and the models are from a certain parameter class, the sample complexity of learning an averaged optimal multi-task policy (using UMT-PSR, an proposed algorithm) is given in Theorem 1. The complexity is related to the complexity of the parameter class, which is measured by $\\eta$-bracketing numbers. This result shows the benefit of multi-task learning when compared with learning tasks separately. For the downstream class learning, by adopting OMLE, the sample complexity is given in Theorem 2, which is related to the complexity of the downstream model class (constructed by upstream learning) that can be reduced by previous upstream learning. The authors also instantiate their generic framework on three examples.

### Strengths
Originality: Studies the combination of non-Markovian process and multi-task RL, which is a relatively unexplored topic. 
Quality: provide generic frameworks together with concrete examples, which shows the applicability of this theoretical analysis.
Clarity: the writing is smooth, the ideas and intuitions are also clear.

### Weaknesses
The downstream learning seems to be only applying previous results on a smaller downstream model class, without further new ideas.

### Questions
1. can these results generalize beyond low-rank problems? (maybe not low-rank, but some other structures)
2. The results hold for finite action and observation spaces. Can they be generalized to general infinite spaces? (maybe using function approximation or other techniques)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This theoretical paper discusses the problem of multi-task reinforcement learning in the setting of low-rank and well-conditioned PSRs. It analyzes two situations when there is structure in the multiple tasks: upstream learning and downstream.

### Strengths
Strengths of this paper are that it tackles a challenging problem, introduces a nice formulation for the problem and showcases interesting theoretical results on when multi-task learning is beneficial as opposed to multiple single-task learning.

### Weaknesses
The biggest weakness of this paper is that it crams too much content in the main paper, and does not use the appendix to explicate it. This rushed discussion makes the job of reading the paper more difficult than it needs to be. For example, consider the assumptions of rank-$r$ and $\gamma$-well-conditioned PSRs. These two assumptions are present throughout the paper, but they never get their deserved attention. A mere half a page of terse definitions for them might be justified in the main paper due to page number constraints, but it is hard to justify why they were never given due discussion in the appendix. This discussion should discuss the intuitive meaning of these assumptions, examples of PSRs which satisfy the assumptions (otherwise questions like, is the set $\Theta$ even non-empty, surface), examples of PSRs which don't satisfy the assumptions, what fails in the proofs if each assumption is relaxed, etc. The notation $\phi_h$ and $\mathbf{M} _ h$ is never even defined, the norm $\lVert \cdot \rVert_\infty^p$  is "pulled out of a hat", etc.

The paper does a poor job at literature review. For example, it states that "none of the existing studies considered multi-task POMDPs/PSRs", but consider _Multi-task Reinforcement Learning in Partially Observable Stochastic Environment_ by Li, Liao and Carin (JMLR 2009) or _Deep Decentralized Multi-task Multi-Agent Reinforcement Learning under Partial Observability_ by Omidshafiei, Pazis, Amato, How and Vian (ICML 2017) [1,2].

While not necessarily a weakness, it would have been nice to demonstrate the usefulness of the theory developed in the paper on some simple experiments. As long as I am asking for things it would be nice to calculate the computational complexity of implementing the algorithms. Note that I am not at all expecting these additions to this paper -- the paper is already very terse as it is.

### Questions
1. Why is the first goal of upstream learning finding near-optimal policies for all $N$ tasks _on average_, as opposed to, say, finding near-optimal policies for all $N$ tasks, i.e. 
$$
\begin{align*}
max_{n \in [N]} \max_\pi \left(V_{\theta_n^*,\,R_n}^{\pi} - V_{\theta_n^*,\,R_n}^{\bar{\pi}^n}\right) \le \epsilon.
\end{align*}
$$
2. Why use $\lVert \cdot \rVert_\infty^p$ as the norm? Is it even a norm (i.e., satisfies the conditions required)?
3. In the calculation of $\eta$-bracketing number of $\{(\mathbb{P} _ {\theta_1}, \ldots, \mathbb{P} _ {\theta_N}) : \mathbf{\theta} \in \mathbf{\Theta} _ u\}$, what is the domain of the functions? Is it the $\sigma-$algebra over $(\mathcal{O} \times \mathcal{A})^H,$ which is the domain of the distributions? Consider a simpler calculation: how to calculate the $\eta$-bracketing number for $\{\mathbb{P} _ {\theta} : \theta \in \Theta\}$? Now $\mathbb{P} _ {\theta}$ is a probability measure which is defined over some $\sigma$-algebra $\mathscr{S}$. If it is contained in some $\eta$-bracket $[\mathbb{A}, \mathbb{B}]$, then we must have $\mathbb{A}(S) \leq \mathbb{P} _ \theta(S) \le \mathbb{B}(S)$ for every $S \in \mathscr{S}$. But this would imply (it might require measures to be regular, I am not sure) that $\mathbb{A} = \mathbb{P} _ \theta = \mathbb{B}$. So the $\eta$-bracketing number for $\{\mathbb{P} _ {\theta} : \theta \in \Theta\}$ becomes $|\Theta|$. I am assuming that this is not what the authors had in mind. Could you please clarify the calculation? The calculations in Appendix E are assuming the observation and action spaces are finite.
4. I do not understand the discussion of pairwise additive distance based multi-task planning. Why is a distance between product distributions not sufficient as opposed to what the paper uses? Also, do the authors realize that
   $$
  \sum _ {n \in [N]}\mathtt{D _ {TV}}(\mathbb{P} _ {\theta_n}, \mathbb{P} _ {\theta'_n}) = \mathtt{D _ {TV}}(\mathbb{P} _ {\theta_1} \otimes \cdots \otimes \mathbb{P} _ {\theta_N}, \mathbb{P} _ {\theta'_1} \otimes \cdots \otimes \mathbb{P} _ {\theta'_N}),
  $$
   a divergence (not distance) over product distribution?

### Soundness
3 good

### Presentation
2 fair

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
This paper studies the benefits of multi-task learning in low-rank PSRs when tasks share similar latent structures. It proposes a measurement for the similarity of $N$ tasks called the $\eta$-bracketing number, which is shown to be small in several standard classes. Examples include multi-task POMDPs sharing the state space, action space, and transition kernel, and multi-task low-rank PSRs with similar core set observable matrices. The algorithm proposed in the paper leverages the $\eta$-bracketing number to find the optimistic exploration policies, and follows the idea of MLE to build confidence set for models. It is proved to gain benefits when the average $\eta$-bracketing number over $N$ tasks is smaller than the $\eta$-bracketing number for a single task in terms of sample complexity to find the optimal policies of all tasks. Additionally, the paper also gives a downstream algorithm that improves the sample complexity to identify a new target task based on the similarity between target task and the $N$ original tasks.

### Strengths
1. The setting is an extension of multi-task learning of MDPs and bandits, which is novel in the literature of multi-task decision making. 

2. It provides a key measurement of similarity in the multi-task setting, the $\eta$-bracketing number, to identify the effectiveness of the multi-task transfer learning in low-rank PSRs.

### Weaknesses
1. The results of the paper is interesting in the viewpoint of setting and techniques, but not surprising given many previous works on multi-task reinforcement learning. The standard tool to establish the benefits of shared structure of multiple tasks is the reduced covering number of the joint model class or value class. For example, the common low-rank assumption in the linear setting essentially reduce the log covering number of the function class from $nm$ to $nk + km$, where $n, m, k$ denotes the ambient dimension, the number of tasks, and the rank that is small. This work studies a more complicated setting, but the $\eta$-bracketing number is essentially some type of covering number over the joint model class. Specifically, the $\eta$-bracketing number appears to quantify the complexity of simultaneously approximating the transition dynamics across multiple tasks. While the authors introduce it as a novel concept, its function is analogous to a covering number in bounding the approximation error. The authors should clarify the precise relationship between the $\eta$-bracketing number and established complexity measures like the covering number. As long as this key property is identified, the remaining task is to follow OMLE to perform optimistic planning in the joint model space.

2. The generality of the theorems in the paper allows the various common structure with different $\eta$-bracketing number of the joint model class. Several examples are already explained in the paper such as the multi-task observable POMDP sharing the common transition kernel. The generic upstream algorithm is highly computational inefficient in building the confidence set and find the optimistic policy. Therefore, an important question is how the optimization steps in the algorithm look like in a specific setting (e.g., the multi-task POMDPs). This helps to evaluate the effectiveness of the upstream algorithms. For instance, in the case of multi-task POMDPs with shared state and action spaces, the optimization might involve finding a low-rank tensor decomposition of the transition kernel. The authors should provide a detailed analysis of the computational aspects for at least one specific example to demonstrate the practical feasibility of their approach.

### Questions
It seems that the $\eta$-bracketing number is used to build the optimism of optimistic policies with uniform convergence over the bracketing set. This is essentially (and also used as) the covering number of the model class in terms of $\|\cdot\|^{\mathrm{p}}_{\infty}$ norm. Why use bracketing number as the name instead of calling it the covering number directly?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper studied multi-task reinforcement learning (MTRL) in complex environments like partially observable MDPs and predictive state representations. The authors identified two main challenges: 1. Identifying Beneficial Common Latent Structures: The large and complex model space of multi-task predictive state representations (PSRs) made it difficult to identify types of common latent structures that could reduce model complexity. 2. Intertwining of Model Learning and Data Collection: in RL, model learning and data collection are intertwined, creating temporal dependencies in the collected data. This complicates the analysis of multi-task PSRs, making it challenging to gauge the benefits of reduced model complexity in terms of statistical efficiency gains in RL. To solve these challenges, the authors introduced the η-bracketing number to quantify model complexity and task similarity. They developed the UMT-PSR algorithm for efficient upstream multi-task learning and addressed downstream transfer learning by leveraging similarities with previously learned tasks. Their contributions include a new complexity metric, the innovative UMT-PSR algorithm, and techniques for enhanced downstream learning, marking a pioneering theoretical exploration of multi-task RL's benefits over single-task approaches in complex environments.

### Strengths
To AC: I do not have the expertise in this research area to review the strengths and weaknesses of the paper. Please lower the weight of my review.

### Weaknesses
To AC: I do not have the expertise in this research area to review the strengths and weaknesses of the paper. Please lower the weight of my review.

### Questions
To AC: I do not have the expertise in this research area to review the strengths and weaknesses of the paper. Please lower the weight of my review.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
