# BOIL: Learning Environment Personalized Information

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Navigating complex environments poses challenges for multi-agent systems, requiring efficient extraction of insights from limited information. In this paper, we introduce the Blackbox Oracle Information Learning (BOIL) process, a scalable solution for extracting valuable insights from the environment structure. Leveraging the Pagerank algorithm and common information maximization, BOIL facilitates the extraction of information to guide long-term agent behavior applicable to problems such as coverage, patrolling, and stochastic reachability. Through experiments, we demonstrate the efficacy of BOIL in generating strategy distributions conducive to improved performance over extended time horizons, surpassing heuristic approaches in complex environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce the Blackbox Oracle Information Learning (BOIL) process, a scalable method for extracting insights about environment structure in multi-agent systems. BOIL uses the Pagerank algorithm and information theory to capture information on agents' long-term behavior, showing versatility across various tasks, such as coverage, patrolling, and stochastic reachability, by framing them as common information maximization problems. The adaptability of BOIL, particularly its potential for online updates, positions it as a promising tool for enhancing performance in complex environments. Despite challenges in control dependencies, the authors believe the proposed solution offers a valuable step toward more adaptable and high-performing multi-agent systems.

### Strengths
The proposed solution BOIL provides a scalable solution for multi-agent systems that can adapt to a variety of tasks, including coverage, patrolling, and stochastic reachability. BOIL’s use of the Pagerank algorithm and information theory for extracting long-term behavioral insights seems to offer a novel application of these techniques in multi-agent environments.

### Weaknesses
The presentation of the paper is poor, I struggled a lot but still had trouble understanding most of the technical part. For example,

1. The entire section 3, though clearly written by itself, is confusing to me as it is introduced before the problem formulation. I do not understand how the introduced technical tools like the non-reversible Markov chain and supervised pagerank relate to the problem we target to solve. Specifically, the connection between the sampling process described in Subsection 3.1 and the subsequent agent strategies is unclear. The motivation for using a non-reversible Markov chain, as opposed to a simpler reversible one, is not well-established in the context of the problem.
2. Section 4, where the problem formulation is supposed to be presented, is also confusing to me. If I understand it correctly, the problem statement is hidden in L.224, which states that "The coverage problem can be defined as minimizing the expected information from all the $Y_t$ for all $0\leq t\leq T$". This is not a rigorous mathematical statement and I still do not get what is the concrete problem we aim to solve from this sentence. The lack of a clear objective function at the beginning of the section makes it difficult to follow the subsequent derivations. I also do not understand what the purposes of Lemma 1 and Theorem 1 are. I guess the properties revealed by Lemma 1 and Theorem 1 are crucial in terms of understanding the problem formulation, but I failed to see the connection here. The role of these theoretical results in the overall problem-solving framework is not adequately explained.
3. Section 4.3 is supposed to introduce the definition of Patrilling and Reachability problem. I can see that compared to coverage problem, the patrolling problem is to simply replace the set $V$ to $V_p$ in the definition of $\mathcal{L}$. However, I do not understand the description about the reachability problem. It would be much clearer if putting the definitions of the three problems together at the beginning. The presentation of these problems feels disjointed, and the specific mathematical formulation for the reachability problem is particularly opaque.
4. All the lemmas and theorems are introduced abruptly. Though full proof details are provided in appendix, no proof sketch or high-level overview is provided in the main paper. This writing approach makes readers extremely difficult to grasp the significance and implications of each proof, as well as the logical connections among the theorems and lemmas. Consequently, understanding the broader flow and purpose of the mathematical arguments are challenging. The lack of context for these theoretical results makes it hard to see their relevance to the overall contribution.

### Questions
Please address the concerns I raised in weaknesses. 

1. In section 5, it is mentioned that "We do experiments for the coverage problem and not for the rest of the extensions mentioned in
subsection 4.3." Do you have any explanation or justification for this decision? Do the results on the coverage problem suggest any meaningful observation for the other two extensions?
2. What is the rationale behind the 7 choices of the agent types in section 5.1? Are they commonly used in the literature?
3. The experiments are based on a synthetic environment. I'm wondering if this is a common benchmark and whether there are more realistic problem sets to test the performance of BOIL.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes an Algorithm named BOIL (Blackbox Oracle Information Learning) for navigating complex environments in multi-agent systems. The BOIL assumes access to an oracle whose information is indirectly accessible and its objective is to devise a computationally scalable approach to extract insights from this oracle. Leveraging the Pagerank algorithm and common information maximization, BOIL facilitates the extraction of information to guide long-term agent behavior applicable to problems such as coverage, patrolling, and stochastic reachability. Extensive experiments validate the empirical performance of BOIL.

### Strengths
This paper is well written with a clear logical flow.  

The proposed algorithm BOIL is complemented with rigorous theoretical analysis and extensive empirical experiments. Both theoretical insights and empirical insights are drawn. 

The setting of having access to an oracle whose information is indirectly accessible looks novel.

### Weaknesses
The assumption of having access to an oracle whose information is indirectly accessible needs justification. The feasibility of this assumption in real-world assumption is unclear. Specifically, the paper does not adequately explain how such an oracle would be implemented or how its outputs would be represented in a practical setting. The paper mentions that the oracle provides 'continuous paths', but it is not clear what this means in the context of a discrete environment, which is typically the case in multi-agent systems. Furthermore, the paper does not discuss the computational cost of simulating or accessing this oracle, which is a critical factor in determining the practicality of the proposed approach.

The contribution of this paper is not clear to me. In particular, how this work improves the SOTA is unclear. This paper considers the setting of having access to an oracle whose information is indirectly accessible. Should the main contribution be claimed as a novel setting? Hasn’t this setting been considered in previous literature? From a methodological point of view, the techniques used in this paper look conventional. Compared to SOTA techniques, it is unclear to me whether this makes paper makes any methodology contribution. The use of Pagerank and common information maximization, while effective, are not novel in themselves. The paper needs to clearly articulate what new insights or techniques are being introduced beyond the existing literature.

The related work should not just list key papers in literature. The difference between this work and previous works is not discussed. How this paper advances previous is also not discussed. The related work section lacks a critical analysis of existing approaches. It does not clearly identify the limitations of current methods that the proposed BOIL algorithm aims to address. It is crucial to demonstrate how BOIL offers a unique or improved solution compared to existing methods, rather than just presenting it as an alternative approach.

### Questions
See the weakness part.

### Soundness
3

### Presentation
3

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
The paper considers the problem of one or more agents learning from an environment as they traverse it. It uses an algorithm based on PageRank to extract information from this traversal of the environment.

### Strengths
The problem defined is very general, and paper pulls together ideas from several lines of work spread over multiple periods of time in order to arrive at its underlying approach. This unification of disparate approaches and lines of work is a contribution of the work, alongside the algorithms themselves.

### Weaknesses
The paper's level of general abstraction is helpful in being able to talk about the connection to disparate earlier lines of work, but it comes with the counterbalancing problem that it makes it hard to identify where the concrete improvements come from in the current approach.

In particular:

- Can the paper specify one or more canonical application domains where the approach would be most likely to be applied? As it stands, even the computational experiments take place in abstract environments that make it hard to see their mapping onto real applications.

- How do the agent strategies in Section 5.1 relate to the earlier approaches from related work? Other than the reference to Yamauchi (1997, 1998), there are no other links between the baseline strategies in this subsection and the description of what's come before in earlier work.

- More generally, what are the concrete ways in which the approaches developed in this paper improve on earlier approaches?

### Questions
It would be helpful if the authors could address the weaknesses listed above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces BOIL (Blackbox Oracle Information Learning), a process designed to enhance multi-agent systems by extracting information from a blackbox oracle to improve agent behavior in complex environments. It leverages the Pagerank algorithm and common information maximization techniques to guide agents in tasks such as coverage, patrolling, and reachability. The authors demonstrate that BOIL outperforms heuristic-based strategies in extended-time simulations and complex environments, providing a scalable approach that remains independent of the number of agents.

### Strengths
1. BOIL (Blackbox Oracle Information Learning) offers an innovative method for addressing challenges in multi-agent systems by utilizing a blackbox oracle to extract valuable information about the environment. The originality lies in its novel use of established algorithms like Pagerank to solve complex tasks such as coverage, patrolling, and stochastic reachability in multi-agent systems. This is a significant departure from existing methods and introduces new possibilities for long-term strategy generation in dynamically changing environments.
2. The paper presents rigorous theoretical formulations to justify its claims. The mathematical grounding of BOIL in Pagerank and non-reversible Markov chains demonstrates a deep understanding of the problem. By framing the problem of agent task execution as a flow constraint problem and using common information maximization, the authors present a technically sophisticated solution that ensures the system remains scalable and efficient, regardless of the number of agents involved.
3. One of the standout strengths of BOIL is its scalability. Many existing multi-agent systems face challenges when trying to scale with the number of agents or the complexity of the environment. BOIL circumvents this issue by extracting and processing information in a way that is independent of the number of agents, allowing it to perform efficiently even in environments with a large number of agents.
4. The simulations show that BOIL can generate strategies that lead to better coverage and visibility in challenging environments, making it applicable to real-world use cases in fields such as autonomous robotics, distributed sensor networks, and security systems. Moreover, the fact that BOIL is able to function without requiring a large number of agents adds to its practical appeal, especially in resource-constrained systems.

### Weaknesses
1. The experiments primarily focus on the coverage problem, leaving patrolling and reachability tasks underexplored. The lack of direct validation for patrolling and reachability leaves open questions about how well BOIL can adapt to these different problem spaces, particularly in dynamic or more constrained environments. The paper does not provide sufficient detail on how the blackbox oracle would be adapted for these tasks, especially given that the oracle's output is a probability distribution over the state space. It is unclear how this distribution would be used to guide agents in patrolling specific locations or reaching designated targets, as these tasks require more specific directional information than simple coverage. Including these experiments would better illustrate the full breadth of BOIL’s potential applications.
2. The convergence issues of the Sample and Comm Sample agents are discussed, but a deeper analysis is needed to understand why they fail to achieve optimal performance compared to the Optimal agent. For example, it would be valuable to understand whether these convergence issues stem from limitations in the algorithm's design, insufficient exploration of the environment, or perhaps an inherent trade-off in computational efficiency versus accuracy. The paper lacks a detailed analysis of the exploration-exploitation trade-off within the sampling strategies, and it does not specify the conditions under which these strategies would fail to converge. It is also unclear how the communication strategy in Comm Sample affects convergence, and whether the limited information sharing is a bottleneck.
3. Although the paper claims that BOIL scales independently of the number of agents, it does not provide explicit scalability metrics or computational complexity analysis, particularly as the size of the environment or number of agents increases. The paper would benefit from a more detailed discussion of the computational complexity of BOIL, especially in larger environments, and explicit time complexity metrics would enhance its practical impact. The paper should also address how the size of the state space affects the performance of the Pagerank algorithm and the overall convergence of BOIL. The current analysis does not account for the potential increase in computational cost as the environment becomes more complex, or as the number of agents increases significantly, which could impact the practical applicability of the method.
4. Certain sections of the paper, especially the Fine-Grained Estimation section, are mathematically dense and could benefit from clearer explanations. The current presentation, while technically correct, may be challenging for readers not intimately familiar with the underlying mathematical concepts. The paper would benefit from more intuitive explanations of how the fine-grained estimation is implemented and how it relates to the overall BOIL framework. Including more intuitive examples or diagrams would make this section more accessible. This would not only improve the readability of the paper but also help a broader audience appreciate the nuances of the proposed techniques.

### Questions
1. Can the authors provide more experimental evidence for patrolling and reachability tasks to better demonstrate BOIL's generalizability?
2. Could you elaborate on why the Sample and Comm Sample agents struggle to converge in large environments? Are there any potential improvements or optimizations that could address this?
3. Are there specific scalability limits for BOIL when applied to very large agent numbers or more complex environments? Including some real-world use cases or benchmarks would strengthen this point.

### Soundness
3

### Presentation
3

### Contribution
3
