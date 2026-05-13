# On Causal Discovery in the Presence of Deterministic Relations

- Decision: Reject
- Scores: 5, 6, 8, 6

## Abstract
Many causal discovery methods typically rely on the assumption of independent noise, yet real-life situations often involve deterministic relationships. In these cases, observed variables are represented as deterministic functions of their parental variables, without noise.
When determinism is present, constraint-based methods encounter challenges due to the violation of the faithfulness assumption. In this paper, we excitingly find, supported by both theoretical analysis and empirical evidence, that score-based methods with exact search can naturally address the issues of deterministic relations under rather mild assumptions. Nonetheless, exact score-based methods can be computationally expensive. To enhance the efficiency and scalability, we develop a novel framework for causal discovery that can detect and handle deterministic relations, called Determinism-aware Greedy Equivalent Search (DGES). DGES comprises three phases: (1) run Greedy Equivalent Search (GES) to obtain an initial graph, (2) identify deterministic clusters (i.e., variables with deterministic relationships), and (3) perform exact search exclusively on each deterministic cluster and its neighbors. The proposed DGES accommodates both linear and nonlinear causal relationships, as well as both continuous and discrete data types. Furthermore, we investigate the identifiability conditions of DGES. We conducted extensive experiments on both simulated and real-world datasets to show the efficacy of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a version of GES that, under specific assumptions, can learn correct Markov equivalence classes for systems that include deterministic dependencies.

### Strengths
The paper is well-written. It deals with a reasonably important problem. It clearly locates its contribution within the large context of the existing literature. It provides both theoretical and empirical evidence regarding its key claims.

### Weaknesses
Unless I'm missing something, the authors results are implied by the following: (1) Due to its scoring function (which penalizes unnecessary edges), GES chooses the MEC for the DC with fewest edges; (2) When the SMR assumption is satisfied, the correct MEC is guaranteed to be the one with fewest edges; and (3) GES is known to find the MEC for the NDC.  Viewed this way, the results of the paper follow directly from what is already known about GES and the SMR assumption, and thus the contribution is fairly small. If this is incorrect, the authors should explain why in the paper. If the above is correct but there is more to it than that, the authors should clearly state the above intuition and provide more discussion of what is missing from that story. 

Minor issues: 

In Section 1, the authors state that some methods "suffer from identifiablity guarantees." It is unclear what this means.

In the abstract and Section 1, the authors state that they "excitingly find" that certain methods can address the issues of deterministic relations. It is enough to state the finding, without excitement.

### Questions
The authors show cases in which DC variables cause each other, and when DC variables cause NDC variables (e.g., Figure 2). However, they do not explicitly discuss cases in which an NDC variable causes a DC variable. That is, variables caused by (latent) noise (i.e., NDC variables) could cause variables without latent noise (i.e., DC variables). Did I miss a discussion, is this case just implied, or is this an assumption of the approach?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In causal discovery, one of the challenges is the presence of deterministic relations, which violates the common assumption of independent noise. This paper proposes a framework called determinism-aware greedy equivalent search (DGES) that can detect the deterministic clusters from data using score-based method, encompassing both linear and nonlinear models. Theoretical guarantees and empirical experiments are provided to support the novel framework.

### Strengths
The paper is well-organized, and the figures are illustrative. The existence of deterministic relations is common in real-world applications and results in biased or even false inference about the data structure. The novel framework DGES alleviates the problem by separate the interested variables into deterministic clusters and non-deterministic clusters and specifically focus on the DCs. DGES is also flexible regarding the linear and non-linear models, as well as the discrete and continuous data.

### Weaknesses
First, the authors claim that constraint-based methods suffer from the deterministic relations and briefly state the reason on page 3. It would be more convincing if solid theorems or experiments are provided to show the failure of constraint-based methods. Specifically, a more detailed explanation of *how* deterministic relationships violate the faithfulness assumption is needed. It's not sufficient to say they fail; the mechanism of failure needs to be clearly articulated, perhaps with a simple illustrative example demonstrating how conditional independencies are incorrectly inferred. In addition, how serious is the assumption violation here? Do all constraint-based methods fail or some adjustments would fix this problem? It would be beneficial to discuss specific adjustments that have been proposed and their limitations, rather than just stating that some might exist.
Second, as the authors mentioned themselves, the DGES framework can not identify the skeleton and directions in the DCs, which negatively influence the utilization of DGES compared with other mature developed methods. This limitation significantly restricts the practical applicability of the method. While identifying deterministic clusters is a useful first step, the inability to determine the internal structure of these clusters means that a complete causal graph cannot be recovered, which is a major drawback. The lack of directionality within DCs is particularly problematic, as it leaves a significant portion of the causal structure unresolved.
Thirdly, I doubt could DGES identify all possible DCs or just part of the deterministic relations? If the answer is no, how could we deal with the missing ones? The paper needs to explicitly address the completeness of the DC detection. Are there scenarios where the proposed method might miss some deterministic relations, and if so, what are the implications for the overall causal discovery process? A discussion of the limitations of the detection process and potential mitigation strategies is needed.

### Questions
1. As for the DCs, could there be case that two DCs connected by a non-deterministic edge? If so, how the DGES framework handle this kind of situation?
2. For the real-world example in 5.2, a comparison between the result using DGES and the results using other classic methods like PC would be interesting. It would be an illustrative way to show how proposed framework differently handle the deterministic relations.
3. Given that the skeleton and directions in DCs are not accurate, would the NDCs and BSs suffer from the same problem?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The surprising result from the paper is that exact search methods can be used to address issues from deterministic relations in causal discovery. The authors show how the presence of deterministic functionals can lead to violation of faithfulness. Particularly, it proposes a variant of score-based causal discovery method known as DGES to increase efficiency of using exact search methods by first detecting potential deterministic clusters and their neighbors.

### Strengths
* The paper is well-organized and the problem is well-motivated. The claims are sound and strongly supported by experiments. 
* The authors show that faithfulness fails due to deterministic relations by Lemma 1 and they also extend previous results about how exact score-based methods can work in non-linear case, by Theorem 3, with the sparest Markov assumption, which is strictly weaker than faithfulness. 
* It provides results (Theorem 4) on how to detect a set of deterministic variables and their neigbors from a Markov equivalence class and use that to increase the efficiency of using exact search methods on the DCs and their neighbors.

### Weaknesses
 * In the proof of Theorem 3, there is a reference missing with question mark. 
* As acknowledged by the authors that the edge directions for deterministic clusters cannot be determined without further assumptions on the functional relationships. Specifically, the paper does not address how to orient edges within deterministic clusters, which limits the practical applicability of the method when full causal graphs are needed. The reliance on additional assumptions highlights a key limitation in the method's ability to provide complete causal information without external constraints.
* Using exact search methods can be computationally expensive. While the paper proposes DGES to mitigate this, the computational cost of the exact search, even when limited to deterministic clusters and their neighbors, could still be prohibitive for large datasets. The paper should provide a more detailed analysis of the scalability of DGES, including the expected computational complexity as a function of the size of the detected deterministic clusters and their neighbors. It is also unclear how the method would perform when the deterministic clusters are large or numerous.

### Questions
* Will algorithms that rely on SMR assumption outperform GES-based methods when deterministic relations are present? I am curious about how well GRaSP[1] will perform in the experiment given the result from Theorem 5. Can the authors include that in the experiment?
* How can one distinguish the violation of non-deterministic faithfulness and the conditional independence relations between deterministic variable and some non-deterministic variables in practice? Does that mean need to domain knowledge to determine whether they should use DGES or they should use DGES in general over GES? Can the authors show some experimental results on cases when there are no deterministic relations to see if the proposed algorithm is at least as good as GES?
* In Theorem 5, the authors show that BS and NDC are identifiable up to Markov equivalence class, but it is not clear to me what the characterization of Markov equivalence class is in the context of having deterministic relations in the graph as a whole. From Lemma 1, we know that there are CI statements that cannot be read-off from the graph, shouldn't there be a different characterization of Markov equivalence class?

Reference:

[1] Lam, W. Y., Andrews, B., & Ramsey, J. (2022, February). Greedy Relaxations of the Sparsest Permutation Algorithm. In The 38th Conference on Uncertainty in Artificial Intelligence.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of causal discovery in the presence of deterministic relationships. This is a particularly challenging problem, since faithfulness is violated; that is, one cannot exploit conditional independence structures as in the classical PC or FCI approaches. The authors propose combining a score-based approach and regression to identify the Markov equivalence class. The latter is used to identify the deterministic nodes where the residual should be 0.

### Strengths
Nicely written and easy to follow. All important aspects are introduced clearly and explained well. The overall idea seems logical and the experimental results are convincing. I did not check the proofs in detail, but the theoretical statements make sense.

### Weaknesses
While the overall idea makes sense, my main concern is the lack of theoretical novelty. While the authors have some theoretical results, they are rather straightforward, and referring to them as "Theorems" may be an overstatement. For instance, it is clear that the residual is expected to be 0 if the functional relationship is perfectly represented.

- The reference to Figure 1 in the introduction does not help in understanding the faithfulness violation with deterministic relationships. It would be clearer, for instance, to give the example of a chain X -> Y -> Z, where Y = f(X), which violates faithfulness due to the conditional independence X _||_ Y | f(X).
- The difference between Assumptions 2 and 3 could be clarified. Does Assumption 2 include the cases described in Assumption 3? 
- You mention PC requires "faithfulness" but based on your definitions, it seems to require "non-deterministic faithfulness". 
- Figure 1 illustrates a DC but does not clearly show why PC fails, since many factors could lead to the PC algorithm outputting graph b), even without deterministic relationships.
- The SMR assumption could be introduced in more detail, since faithfulness is common but SMR is less so.
- Theorem 4 seems overly specific. It could be more general by stating deterministic relationships will result in Var[Y | x] = 0, for any regression model. Is there a reason for using kernel regression specifically?
- In the experiments, you limit non-linear relationships to a few function classes. You could make them more arbitrary by modeling f as a neural network with random weights, to represent a random non-linear relationship.
- The examples illustrations always have edges, but your approach identifies the MEC, which has undirected parts. This distinction could be clarified. 
- Does SHD refer to the whole graph or just the BS? If the latter, why not consider the whole graph?
- I like the discussion, which fairly points out some weaknesses.

### Questions
Although the theoretical novelty is limited, the overall approach is still valid and interesting. Some questions and remarks:

- The reference to Figure 1 in the introduction does not help in understanding the faithfulness violation with deterministic relationships. It would be clearer, for instance, to give the example of a chain X -> Y -> Z, where Y = f(X), which violates faithfulness due to the conditional independence X _||_ Y | f(X).
- The difference between Assumptions 2 and 3 could be clarified. Does Assumption 2 include the cases described in Assumption 3? 
- You mention PC requires "faithfulness" but based on your definitions, it seems to require "non-deterministic faithfulness". 
- Figure 1 illustrates a DC but does not clearly show why PC fails, since many factors could lead to the PC algorithm outputting graph b), even without deterministic relationships.
- The SMR assumption could be introduced in more detail, since faithfulness is common but SMR is less so.
- Theorem 4 seems overly specific. It could be more general by stating deterministic relationships will result in Var[Y | x] = 0, for any regression model. Is there a reason for using kernel regression specifically?
- In the experiments, you limit non-linear relationships to a few function classes. You could make them more arbitrary by modeling f as a neural network with random weights, to represent a random non-linear relationship.
- The examples illustrations always have edges, but your approach identifies the MEC, which has undirected parts. This distinction could be clarified. 
- Does SHD refer to the whole graph or just the BS? If the latter, why not consider the whole graph?
- I like the discussion, which fairly points out some weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair
