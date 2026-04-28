# A Bayesian Framework for Clustered Federated Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
One of the main challenges of federated learning (FL) is handling non-independent and identically distributed (non-IID) client data, which may occur in practice due to unbalanced datasets and use of different data sources across clients. Knowledge sharing and model personalization are key strategies for addressing this issue. Clustered federated learning is a class of FL methods that groups clients that observe similarly distributed data into clusters, such that every client is typically associated with one data distribution and participates in training a model for that distribution along their cluster peers. In this paper, we present a unified Bayesian framework for clustered FL which associates clients to clusters. Then we propose several practical algorithms to handle the, otherwise growing, data associations in a way that trades off performance and computational complexity. This work provides insights on client-cluster associations and enables client knowledge sharing in new ways. The proposed framework circumvents the need for unique client-cluster associations, which is seen to increase the performance of the resulting models in a variety of experiments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a Bayesian framework for clients in a federated setup, which motivates their clustering algorithm. Since, the Bayes optimal assignment is computationally intractable, the paper proposes several heuristics, and empirically compares each with baseline WeCFL on CIFAR10 and FMNIST.

### Strengths
1. The authors provide rigorous (albeit hard-to-parse) derivations for a Bayesian framework in clustered federated learning, that can be applied over a large class of priors.  
2. The main benefit of the above framework is that it models inter-cluster relationships, and seems to be less sensitive (at least in theory) to the choice of number of clusters K. This can be seen as a more principled form of soft-clustering. 
3. Section 3 motivates the need for having approximate association strategies, which the authors investigate in Section 4. The datasets and baselines chosen for the exposition are satisfactory.

### Weaknesses
1. Overall, there is a significant concern over the clarity of writing throughout Sections 3 and 4. For example, even though the authors tabulate their notations in Appendix A, it was pretty hard to follow the arguments in Section 3 because of notation overload. Possibly, some of them can be removed, or some of the derivations can be written down by dropping unnecessary indexing wherever possible. Specifically, the use of multiple nested indices (e.g., in equations 2-7) makes it difficult to track the relationships between variables and their corresponding data points or clients. The lack of clear explanations for each step in the derivations further exacerbates this issue, making it hard to understand the underlying logic and assumptions.
2. Since the different possible associations of clients can be combinatorially very large to evaluate, the authors propose approximations in Section 4. But, it is unclear if BCFL-G/C is helpful in practice, compared to WeCFL. In fact, BCFL-G which does greedy association at each round is quite similar to WeCFL. The empirical results show only marginal improvements, and the practical benefit of the proposed methods is not convincingly demonstrated. The greedy approach, while computationally simpler, may not capture the complex inter-cluster relationships that the Bayesian framework aims to model.
3. From point 2, the main contribution I see is BCFL-MH, but this method is computationally heavier given that it requires computing densities in Sec 3.1 and 3.2, and I could not see a computational cost / performance benefit tradeoff to justify BCFL-MH. The computational overhead of BCFL-MH, involving density calculations and sampling, is substantial, and the performance gains over simpler methods like BCFL-G or WeCFL do not seem to justify this increased complexity. The paper lacks a detailed analysis of the computational cost of BCFL-MH, making it difficult to assess its practical viability.
4. The authors claim "new theoretical insights" in their introduction, but the paper does not have any formal guarantees for the proposed approximations. The absence of convergence proofs or error bounds for the proposed approximations raises concerns about their reliability and applicability in real-world scenarios. The theoretical contribution is not clearly substantiated by rigorous analysis.
5. The authors do not provide any ablations on the choice of number of clusters K, which can be quite critical for some of the proposed approximations like BCFL-MH. The lack of sensitivity analysis on the hyperparameter K makes it difficult to assess the robustness of the proposed methods. The performance of clustering algorithms is often highly dependent on the choice of K, and without such analysis, the practical applicability of the proposed methods remains questionable.

### Questions
1. The derivations in equations 2-7 seem to be simple application of Bayes rule under conditional independence of clients data given model parameters. On the other hand, the approximation in equation 9, which seems to be quite critical is unclear. The authors mention some numerical integration approximation, but it would be useful if they could clarify this further. 
2. In Table 1, what are the standard deviations of the reported metrics? Since the difference between WeCFL and BCFL-G/C is quite small, this would help clarify statistical significance of the reported results. 
3. The motivation for warmup is unclear. Also, how are the local weights clustered? Is it in the euclidean metric?
4. Have the authors tried using the learnt associations for fine-tuning, as opposed to global training? Maybe there are some general image features that can be learnt from all users?
5. Have the authors run IFCA on their datasets for comparison?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper essentially extends the idea of model-based clustering under the Bayesian framework into the clustered federated learning (CFL) problem, where not only the partition of clients but also the model update through federated learning is considered. The paper proposes to tackle the exploded data association incurred by the recursive updates with the $M$-best assignments problem solver.

### Strengths
1. The paper's theoretical contribution that systematically discusses CFL under the Bayesian framework could serve broader interests apart from the proposed algorithms. 

2. The efficiency problem in the recursive update could be tackled with the M-best assignment solver when using the negative log weights as the cost function.

### Weaknesses
1. ***Presentation***

There is a clarity problem before section 4. Specifically, the full procedure of the learning is poorly illustrated. Though Figure 1 is supposed to illustrate the essential steps and communications, the confusing coloring and the lack of clarity on the calculation of key values pose unnecessary challenges for the audience. The pseudo-code for the general learning, clustering procedure, and each variant of association selection, along with a detailed congregate discussion of the communication, would greatly improve the clarity of the paper. Also, it might help to focus on the conceptual discussion in Figure 1 rather than placing notations, which are introduced later in sections 3 and 4. The core issue is that the paper's explanation of the algorithm's flow is not intuitive, making it difficult to grasp the overall process and the specific roles of each component. The lack of a clear, step-by-step explanation, especially regarding the information exchange between clients and the server, hinders understanding.

2. ***Related work***

Section 2 mainly focuses on discussing federated learning works. Yet, the paper needs to pay attention to the existing product partition models and needs more discussion over the progression of existing Bayesian frameworks, which could better position the paper's theoretical contribution. The discussion of related work should not only cover federated learning but also delve into relevant Bayesian clustering and product partition models. This would provide a more comprehensive context for the paper's contribution and highlight its novelty compared to existing approaches.


3. ***Method***

The paper proposes to leverage the cost function to transform the association selection into the M-best assignments problem. Yet, as admitted in the discussion of section 4, the greedy or top $M$ trajectory could be myopic. This problem seems intrinsic in the definition of $L$ and is reflected in the empirical results where the BCFL-MF-6 does not constantly improve upon BCFL-MF-3. The core issue is that the M-best assignment approach, while computationally efficient, might lead to suboptimal solutions due to its inherent myopic nature. The paper needs to address this limitation more explicitly and discuss potential alternative approaches that could mitigate this issue.

4. ***Experiment***

(1) The datasets tested in section 5 seem to be manually synthesized, raising questions about the motivation of CFL and undermining the significance of the experimental results.

(2) The results only show the downstream performance while lacking evidence about the efficiency, especially for different approximations and corresponding key hyperparameters, including the $M$ discussed in sections 4.3 and 4.4 and $K$ that could potentially impact the communication efficiency and learning convergency. The experimental section lacks a comprehensive analysis of the computational and communication costs associated with the proposed methods. The paper should provide empirical evidence of the efficiency of the proposed methods, especially concerning the impact of key hyperparameters such as M and K on communication efficiency and convergence.

5. ***Minors***

(1) The paper claims the existing CFL methods do not effectively exploit similarities between different clusters, yet needs more detailed discussion over the statement.

(2) The adopted merge operator in section 4.3 needs to be clarified.

(3) The model warm-up relies on a different partitioning method based on the local model initialization. And it is unclear why it contributes to the performance.

### Questions
The paper has an intense layout but lacks details of the algorithm design, e.g., a concrete pipeline of the algorithm and congregated discussion of the details of the communication between clients and servers corresponding to the proposed three variants. Based on the discussion and the experimental results, it seems that BCFL-MH is the best option among all the three approximations. If so, why not propose BCFL-MH as the main algorithm, allowing a better illustration of the algorithm's key concepts?  Is there any additional trade-off on the efficiency and performance when choosing the approximation?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a clustered FL method based on a bayesian framework which assigns clients to clusters, and provides three different variations of the proposed bayesian clustered FL framework to address practical considerations, namely approximate BCFL, greedy BCFL, and consensus BCFL. Specifically, for $K$ clusters and $C$ clients, BCFL assigns each client to its optimal cluster based on a target posterior characterization. The work performs preliminary experiments to validate the BCFL's performance on CIFAR10 and FMNIST.

### Strengths
- The work proposes many different variants of BCFL that considers practicality.
- The work investigates clustering in FL dependent on the different data distributions of the clients which is a relevant topic in FL where data heterogeneity can be particularly severe. 
- The work includes details of their experimental results including graphs that show the relationship across clients and their relatedness with the results.

### Weaknesses
 - A major concern I have is regarding the efficacy and practicality of the proposed framework. Although the authors have proposed the three variants of the proposed BCFL framework, they still require the downloading of the models and weights under past associations, and then again uploading the associations of the weights to get the association decisions again from the server. Then finally the clients upload the local models based on the conditional associations. This requires at least 2 times the communication rounds compared to the conventional FL framework as well as more computation imposed to the clients. Specifically, the initial conceptual BCFL approach necessitates clients to download model parameters for all past cluster assignments, which is highly inefficient in terms of communication overhead. The subsequent approximate solutions, while aiming to reduce this, still involve significant overhead due to the iterative nature of association updates and model transfers. This is particularly problematic in resource-constrained FL settings. I became more skeptical after looking at the experimental results which only include 10 clients in total or 8 clients in total for more cross-device like datasets such as digits-dive or amazon review. The limited scale of these experiments raises concerns about the generalizability of the findings to more realistic FL scenarios with a larger number of clients. Another concern regarding this approach of BCFL is the sensitivity of the number of clusters $K$ to the performance. It will be difficult to know this value in advance in practice. How does the authors address this problem as well? Overall due to these issues I am skeptical of the efficacy and practicality of the proposed framework for realistic FL settings.

- Another concern I had regarding the practical variant approximate BCFL, the authors assume that there is no overlap in the distribution across different client partitions. This is quite a strong assumption which does not hold in most of the cases in FL. This assumption of non-overlapping distributions is a significant limitation, as real-world FL datasets often exhibit varying degrees of overlap and shared characteristics across different client data distributions. The assumption of conditional independence given the cluster assignment is also concerning. Can the authors comment on this assumption and how realistic it is?

- The writing of the paper can be improved. for instance in pg1 when the authors address problem 1 and problem 2 in bold, there seems to be a typo/error. Ex: Problems2: The is a lack of a united theory. Moreover, optimality is used throughout the paper from the beginning without a proper explanation on what the authors exactly mean by this. It can mean differently for different readers. In addition, the presentation of Figure 3 can be improved, It is quite hard to see the differences across the curves.

### Questions
See weaknesses above.

### Soundness
2 fair

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the problem of clustered federated learning. Inspired by a Bayesian modeling of clustered FL, the provides three clustering heuristics. The paper evaluates the proposed heuristics and shows that in practice they outperform  WeCFL, which is the state-of-the-art FL clustering method.

### Strengths
- The proposed clustering heuristics exhibit superior performance compared to the current state-of-the-art WeCFL in federated learning.
- The experimental results section is well-crafted, providing a thorough evaluation of the proposed methods.
- BCFL distinguishes itself from other clustering federated learning methods by dynamically adjusting clusters, offering a unique approach that departs from hierarchical clustering strategies.

### Weaknesses
 - The paper's overall clarity is compromised due to unnecessarily complex and at times undefined notation, making it challenging to follow.
- The update mechanism for the parameters of the Bayesian model lacks explicit explanation, leaving a crucial aspect of the methodology unclear.
- The comparison and discussion of related work are superficial, lacking a fundamental exploration of how the proposed method differs from other clustering approaches. 
- The claim that the paper provides a "unified framework with a rigorous formulation" and offers "new theoretical insights and algorithms" is disputed, as the paper fails to present any novel theoretical contributions. The core derivations in Section 3 are mostly straightforward applications of Bayes' rule and standard marginalization techniques, lacking substantial novelty. The use of random finite sets, while mathematically rigorous, does not introduce a fundamentally new theoretical perspective on the clustered federated learning problem.
- Section 3 contains derivations that are deemed obvious, contributing minimally to the understanding of the proposed approach. The mathematical manipulations, while correct, do not offer any non-trivial insights. The derivation of the posterior distribution, for example, follows directly from the application of Bayes' rule and does not present any novel mathematical challenges or results.
- The content in Sections 3 and 4.1 communicates a message that, in my interpretation, appears rather straightforward. The outlined two-step iteration involves computing the "optimal" association $\theta^{*}_{t}$ given cluster weights $\Omega$ and updating cluster weights based on the current association rule. Furthermore, the solution presented in equation (16) suggests associating a client $j$ with a cluster $i$ that maximizes $\log(D^j|w^i)$. While these concepts are essential, the simplicity of the presented message does not seem commensurate with the extensive coverage given to these sections (four pages). The detailed explanation does not justify the space allocated, and as such, Sections 3 and 4.1 may be perceived as overextended for the relatively straightforward content they provide. 
- In light of the preceding remark, it might be beneficial for the paper to discuss soft clustering approaches based on the EM algorithm.
- The proposed methods lack theoretical guarantees, relying solely on heuristics without a solid theoretical foundation. While the Bayesian framework provides a probabilistic interpretation, the practical algorithms (BCFL-G, BCFL-C, and BCFL-MH) are approximations that lack formal convergence proofs or performance bounds. The paper does not provide any analysis of how these approximations affect the optimality of the solution.
- The success of the proposed method heavily depends on the higher computational cost of BCFL-MH, raising concerns about the practicality and efficiency of the cheaper variants (BCFL-G and BCFL-C). In fact,  BCFL-G and BCFL-C do not show a significant improvement over FedAvg and WeCFL; the improvement never exceeds $1$ p.p., and is often lower then $0.1$ p.p.   
- Several minor issues, including inconsistent citation style, grammatical errors, and unclear notation choices, need attention for a more polished presentation: 
     - The paper seems to use the wrong citation style. It refers to the authors when it should refer to the paper. For example, the sentence "FL allows collaborative model training without data sharing across clients, thus preserving their privacy McMahan et al. (2017)" should be "FL allows collaborative model training without data sharing across clients, thus preserving their privacy (McMahan et al., 2017). "
    - In Section 1, "the is a lack" -> "there is a lack". 
    - What is the reason behind using $\mathbb{P}$ instead of $P$ in page 3?
    -In Page 4, "to denote the a particular" -> "to denote a particular".
     - In Page 7, "both feature- and label- skew" -> "both feature---and label---skew"

### Questions
- My understanding of the paper is that each iteration is split into two steps: compute the "optimal" association $\theta^{*}_{t}$ given the weights of the clusters $\Omega$, then, update the cluster weights given the current association rule. Could you please confirm or deny my interpretation?
- Regarding (13), it seems for me that the optimal solution would pick $A^{i j} = 1$, for $i \in \text{arg}\min_{i} L^{i, j}$. It translates in (16), to  associating the client $j$ to the cluster $i$ that justifies the best its data, i.e. the cluster $i$ such that $log(D^j|w^i)$ is maximal. Could you please confirm or deny my claim?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
