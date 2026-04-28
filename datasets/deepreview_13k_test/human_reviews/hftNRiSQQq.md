# Boosting Efficiency in Task-Agnostic Exploration Through Causal Knowledge

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
The effectiveness of model training heavily relies on the quality of available training resources. However, budget constraints often impose limitations on data collection efforts. To tackle this challenge, we introduce \textit{causal exploration} in this paper, a strategy that leverages the underlying causal knowledge for both data collection and model training. We, in particular, focus on enhancing the sample efficiency and reliability of the world model learning within the domain of task-agnostic reinforcement learning. During the exploration phase, the agent actively selects actions expected to yield causal insights most beneficial for world model training. Concurrently, the causal knowledge is acquired and incrementally refined with the ongoing collection of data. We demonstrate that causal exploration aids in learning accurate world models using fewer data and provide theoretical guarantees for its convergence. Empirical experiments, on both synthetic data and real-world applications, further validate the benefits of causal exploration.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of enhancing the data collection efficiency during the training the world model. To address this challenging issue, a new framework named causal exploration is proposed, to improve the performance of both causal discovery and model learning. During the exploration phase, the agent actively selects actions expected to yield causal insights most beneficial for world model training. This framework is built upon 2 key components: 1, an efficient online causal discovery method, and 2, a novel weight-sharing-decomposition schema to satisfy the causal constraint of the forward model.

### Strengths
This paper tried to address a very important question: how to utilize the underlying causal knowledge, and learn a world model in a task-agnostic fashion and data-efficient way? The proposed causal exploration is an interesting idea to address this question: it essentially allows "cold start" optimization of the world model with an unknown causal graph; and both the data collection policy ("i.e., experiments") and the causal discovery results are updated during the online learning process. The methodology is partially supported by convergence analysis. The experimental results on benchmarking different baselines could also be valuable to certain audiences in this field.

### Weaknesses
The main weaknesses of this paper are threefold:

- Lack of clarity in the presentation. Typically, for a paper like this would greatly benefit from a clearly written problem-setting section. However, this is currently missing and I can imagine that this will create major obstacles for understanding this paper, especially for researchers that are not from this field. These missing problem settings include but are not limited to:

  - the world model $f$ was never formally defined mathematically and is only briefly mentioned in Section 2.2 which is too late. 
  - the authors mentioned the concept of "causal exploration" from the beginning of Section 2 without any mathematical description.
  - the goal of this paper is supposed to be "enhancing data collection efficiency to improve world model learning as well as causal discovery". However, this problem is not formally defined mathematically. 

In general, I need to put all the pieces together and figure out them by myself. Although it did not take too much effort, the reading experience was not great either.


- Unclear causal assumptions and missing identification theory. The underlying causal assumptions of the proposed method were never discussed, and methods with different underlying causal assumptions were combined in an ad-hoc way. For example, as the authors might already be aware, the underlying factorization in Section 2.2, Eq 3 resembles the SCM models in causality literature. Then, why the authors did not consider applying causal discovery techniques that were specifically defined for SCM models instead of a generic PC algorithm? This should offer more advantages in terms of data efficiency since SCMs typically have stricter assumptions and stronger identification results. Moreover, the authors did not provide any theoretical analysis regarding the correctness of the identified causal graph, which is very crucial. 


- Disconnection from the latest development of causal learning literature that addresses similar problems.
  -  The proposed causal exploration is closely related to a large field named active (Bayesian) causal discovery [3, 4, 5, 6], in which causal exploration can be viewed as a special case of active causal discovery, where the exploration policy exactly corresponds to the notion of experiment design of interventions.  In the current paper, all these related works are not properly acknowledged, benchmarked and compared.
  -  The computational complexity of Eq 3 is not a new problem, and the exact same weight-sharing schema has already been discussed in a number of literature [1, 2] in the context of causal deep learning. 
  - Similarly, in the context of causal deep learning, efficient graph learning has already been discussed in a number of literature as well. These recent works since [1] mostly focused on differential graph learning which exploits the SCM assumptions as well as the corresponding identifiability theory. In contrast to the proposed efficient causal discovery that is based on discrete PC, I believe that the differential approach can be integrated into the causal exploration framework more easily. This is because the graph can be learned end-to-end and does not require a separate graph learning step.

- Flaws in experiment evaluation methods. If I understand correctly, the prediction errors in experiments are estimated on the test set used in exploration. This will give a significantly unfair advantage to the proposed method when compared with the baselines since the proposed method is designed to utilize such prediction error as a learning signal. The authors should consider using metrics such as the discrepancy between the learned model versus the ground true model (in synthetic examples) or its offline equivalence (in real-world scenarios). 


Given the aforementioned weakness, I am not convinced by the significance and novelty of the contribution. However, I am open to discussions and if my concerns are addressed during the rebuttal, I will raise my score accordingly.


References:

[1] Zheng X, Aragam B, Ravikumar P K, et al. Dags with no tears: Continuous optimization for structure learning[J]. Advances in neural information processing systems, 2018, 31.

[2] Geffner T, Antoran J, Foster A, et al. Deep end-to-end causal inference[J]. arXiv preprint arXiv:2202.02195, 2022.

[3] Murphy K P. Active learning of causal Bayes net structure[R]. technical report, UC Berkeley, 2001.

[4] Tong S, Koller D. Active learning for structure in Bayesian networks[C]//International joint conference on artificial intelligence. Lawrence Erlbaum Associates ltd, 2001, 17(1): 863-869.

[5] Tigas P, Annadani Y, Jesson A, et al. Interventions, where and how? experimental design for causal models at scale[J]. Advances in Neural Information Processing Systems, 2022, 35: 24130-24143.

[6] Ivanova D R, Jennings J, Rainforth T, et al. CO-BED: Information-Theoretic Contextual Optimization via Bayesian Experimental Design[J]. arXiv preprint arXiv:2302.14015, 2023.

### Questions
See the Weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Building upon previous methods, this paper introduces an intrinsic reward to enhance performance. It analyzes the convergence rate and achieves promising experimental results.

### Strengths
Building upon previous methods, this paper introduces an intrinsic reward to enhance performance. It analyzes the convergence rate and achieves promising experimental results.

### Weaknesses
The paper's analysis of efficiency is currently insufficient, relying solely on experimental findings. However, the theoretical analysis of the paper is not enough to fully support the author's claims.

### Questions
* What does "t" in equation 5 signify? Does it refer to the optimization turn or the time step? If it aligns with the time step notation from the previous section, it might be challenging to understand why we should evaluate the difference between two errors at different time steps.

* Does the shared schema have a bad effect on the identifiability of causality?

* Which strategy can enhance efficiency? The shared schema appears to introduce an additional layer of parameters. Adding extra intrinsic rewards in equation 5 seems to increase computational costs.

* I appreciate the theoretical analysis of convergence, but this paper primarily focuses on efficiency, such as exploration efficiency and whether the convergence rate is better than what was previously required. The theoretical analysis and the point the paper aims to make appear somewhat disconnected.

* How is the dataset D_h collected? If the dataset is fixed and predetermined, learning parameters based on the collected dataset doesn't pose an exploration challenge. In Model-Based Reinforcement Learning (MBRL), exploration is intertwined with data collection.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a causal exploration strategy to leverage the causal structure of the data and model training to increase the sample effficency.

### Strengths
1. The problem addressed in the paper is very interesting. 
2. The paper conducts experiments to demonstrate the effectiveness of the framework.

### Weaknesses
1. The paper is poorly written and mainly unorganized. The main contribution of the paper is completely lost. 
2. Causal discovery from observational data is known to be unidentifiable with extra assumptions on the data generating process. The paper employs the PC algorithm which is also known to only be able to identify the causal graph up to CPDAG. The paper needs to discuss the unidentifiability issue and its effect on the performance of the proposed method.
3. The paper needs to provided theoretical and empirical analysis of the unidentifiability of causal discovery on the overall performance.

### Questions
Please refer to the weaknesses.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper first introduces a framework that (a) discovers causal relationships between state and action variables, and simultaneously, (b) trains the world model that respects the discovered causal graph (this framework is called *causal dynamics learning* in the literature). For (a), the authors rely on conditional independence tests (CITs). They are widely used for causal discovery, but the computational cost grows exponentially with respect to the sample size. For this, the authors utilize a coreset sampling strategy for efficient CIT. For (b), the dynamics model adheres to Markov factorization guided by the discovered causal graph, i.e., $p(s'\mid s, a)=\prod_j p(s'_j\mid Pa(s_j'))$. This requires different models for each state variable, so the authors introduce weight-sharing networks to reduce model parameters. 

Along with this causal dynamics learning framework, the paper proposes a causal exploration which is defined as the combination of the (i) sample prediction error and (ii) improvement of the average prediction error on the test set. The authors also provide convergence analysis. Experimental results demonstrate that the proposed causal exploration efficiently discovers causal relationships and outperforms previous exploration strategies.

### Strengths
- The paper deals with an important problem. The paper is also easy to follow and well-written.
- The idea of employing the coreset selection strategy of Yoon et al., (2022) for efficient conditional independence tests is interesting. The paper also provides a convergence analysis.
- Experiments are made extensively from synthetic environments to complex tasks, e.g., traffic signal control tasks.

### Weaknesses
First, the authors did not recognize the highly relevant works in the line of **causal dynamics learning in RL** [1-3]. These causal dynamics models aim to discover causal relationships and train dynamics models accordingly, which is exactly what Sec. 2 is about. For example, [3] also utilized CITs to determine whether the edges exist or not, while [1] used a score-based method. Efficient dynamics model architecture is also proposed and discussed in [2]. Moreover, [2] also proposed an exploration term to boost causal dynamics learning, but the manuscript does not discuss nor mention these works at all, which seems a critical issue. Unfortunately, in its current form, it is hard to assess the novel development of this paper compared to prior works. Second, I also have a concern regarding the presentation and experiments. The points that need further clarification or discussion are listed below.

**References**

[1] Wang et al., “Task-independent causal state abstraction”, NeurIPS Robot Learning Workshop 2021.

[2] Wang et al., “Causal dynamics learning for task-independent state abstraction”, ICML 2022.

[3] Ding et al., “Generalizing goal-conditioned reinforcement learning with variational causal reasoning”, NeurIPS 2022.

### Questions
- Given that the edges follow the temporal order and there are no instantaneous edges, it is basically applying a conditional independence test for every possible candidate edge. Calling it a PC algorithm is somewhat misleading.
- Score-based approach is more efficient compared to constraint-based methods for causal discovery. Justification and discussions would be appreciated.
- What is the depth in Fig 2 (b)?
- In Eq. 2-3, what is the difference between $w$ and $w^c$?
- How is the separate prediction model $\phi$ updated? What is $\phi_t$ in Eq. 5? Also, why do we need a separate model, instead of the forward dynamics model?
- In Mujoco, the causal relationship seems dense (i.e., fully-connected), but the proposed method outperforms other baselines. Given that the proposed causal exploration degenerates into non-causal exploration when the causal connection is fully connected (as described in Sec 3.1), the performance gain shown in Fig. 7 needs further explanation.
- What is the value of $\beta$ in Traffic Signal Control and Mujoco?

**Minor comments and typos**

- Plot headings in Fig. 2 (a) and (c): “PC discovery” is a bit awkward. It should be PC algorithm or causal discovery.
- In Eq. 1, the gradient operator for $f_w(b_t^p)$ should be a sample gradient, not the average gradient.
- There should be spaces between words and parentheses (like this).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
