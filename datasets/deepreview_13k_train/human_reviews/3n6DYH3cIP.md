# Extendable and Iterative Structure Learning for Bayesian Networks

- Decision: Accept
- Scores: 5, 6, 6, 3, 8

## Abstract
Learning the structure of Bayesian networks is a fundamental yet computationally intensive task, especially as the number of variables grows. Traditional algorithms require retraining from scratch when new variables are introduced, making them impractical for dynamic or large-scale applications. In this paper, we propose an extendable structure learning strategy that efficiently incorporates a new variable $Y$ into an existing Bayesian network graph $\mathcal{G}$ over variables $\mathcal{X}$, resulting in an updated P-map graph $\bar{\mathcal{G}}$ on $\bar{\mathcal{X}} = \mathcal{X} \cup \{Y\}$. By leveraging the information encoded in $\mathcal{G}$, our method significantly reduces computational overhead compared to learning $\bar{\mathcal{G}}$ from scratch. Empirical evaluations demonstrate runtime reductions of up to 1300x without compromising accuracy. Building on this approach, we introduce a novel iterative paradigm for structure learning over $\mathcal{X}$. Starting with a small subset $\mathcal{U} \subset \mathcal{X}$, we iteratively add the remaining variables using our extendable algorithms to construct a P-map graph over the full set. This method offers runtime advantages comparable to common algorithms while maintaining similar accuracy. Our contributions provide a scalable solution for Bayesian network structure learning, enabling efficient model updates in real-time and high-dimensional settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an iterative/incremental algorithm to learn the structure of a Bayeisan network from observed data.
The algorithm added one variable at a time, and modify the previously learn structure accordingly.
The novelty is to prove that adding one variable only leads to deletion of previous edges, and therefore trim the search space of possible networks.

In particular, Lemma 1 shows that if the new variable Y satisfies some properties, a certain kind of edges in the old graph can be safely deleted. The paper introduced constrained-based and score-based approaches to utilize this lemma. The results is a reduction of number of CI tests.

Experiments on 13 datasets shows that the running time is significantly reduced without compromising accuracy of the learned structure.

### Strengths
+ structure learning is a challenging problem due to exponentially large search space, and the paper makes progress in speeding up the search without sacrificing accuracy.
+ the proof is solid and the presentation is clear.
+ strong experimental results in accuracy and running time.

### Weaknesses
 - The scope of the paper (symbolic Baysian network) may not fit ICLR conference (representation learning).
- Insufficient discussion of related work. There shall be a large number of related work on incremental structure learning, while the submission only cite two most relevant ones ((Kocacoban & Cussens, 2019) and (Alcobe, 2005)). This makes the contribution of the submission less clear.

### Questions
- How the score-based and constraint-based methods are used in the extendable PC algorithm?
- Are the more existing work that incrementally learn the structure? What are their strengths and weaknesses?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides a novel perspective to the Bayesian structure learning problem with an efficient mechanism to add new variables to an underlying graphical structure. Specifically, the learning strategy hinges on efficiently incorporating a new variable $Y$ into an existing Bayesian network ${\cal G}$ over the set of variables ${\cal X}$, which results in an. updated Bayesian network $\bar {\cal G}$ on the augmented set of variables ${\cal X} \cup Y$. This learning strategy is further extended to provide a novel learning paradigm for structure learning for Bayesian networks. Experiments demonstrate significant computational efficiency over existing state-of-the-art algorithms.

### Strengths
The problem studied in the paper is well-motivated and will be of interest to ML community. Recycling the existing information when new variables are added or revealed provides a novel perspective to the structure learning problem. The iterative structure learning algorithm is a valuable contribution. Experiments convincingly demonstrate the computational efficiency of the proposed approach.

### Weaknesses
I found the discussions and organization of Section 3 to be more convoluted than necessary. In particular, it would be helpful to have the relevance of Algorithms 2-4 explictly elucidated. The description of how the search space is trimmed using the T-function in Algorithm 4 lacks sufficient detail. It is unclear how this function practically restricts the search space, and what specific criteria are used to determine which edges are pruned. Furthermore, the connection between the theoretical results (Lemmas 1-3) and the practical implementation of the T-function is not clearly established. The paper would benefit from a more concrete explanation of how these theoretical findings directly translate into a practical search space reduction strategy. Without this, it is difficult to assess the effectiveness and generality of the proposed approach.

### Questions
1. Is the Extendable P-map learner in Algorithm 3 implemented using Algorithm 1?
2. What is Sepset(X,Y)?
3. An intuitive explanation for why the iterative learning algorithm outperforms PC algorithm while learning the complete graph is recommended.
4. How is this work positioned relative to the prior works that study the information-theoretic limits of Bayesian structure learning?


____________________________________________
POST AUTHOR REBUTTAL
I thank the authors for their detailed response. I will maintain my rating.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the structure learning problem in Bayesian networks, i.e.. learning a directed acyclic graph (DAG) which defines the conditional probability distribution  over the given variables. Particularly, an extendable structure learning strategy is proposed to update an existing Bayesian network graph efficiently, when  a new variable is introduced. Two approaches (constraint-based and score-based) are discussed for extendable structure learning, which leverage the previous graph structure, and have   much lower computational cost compared to relearning the graph. It is then shown that these procedures can be used to design an iterative algorithm for structure learning. Numerical results on many graph datasets illustrate the performance of  the proposed method, and shows significant speedup over the approach where the graph is learned from scratch.

### Strengths
Strengths:
1.  Extendable structure learning for Bayesian networks is studied and two new approaches are proposed. 
2. The new approaches achieve much lower runtime than relearning the graphs without prior structure. 
3. Numerical results are presented on  many graph datasets showing  significant speedup.

### Weaknesses
Weakness:
1. Performance guarantees for the proposed method are not presented.
2. Details about a key assumption can be further discussed.

### Questions
I have the following comments about the paper:

1. Performance guarantees such as error analysis, or on how to check whether the algorithm has converged to the correct graph structure are not discussed. 
A discussion on how to verify the correctness of  the P-map finder algorithm used should be added. If the iterative approach is used, how does the error accumulate?
Are the conditions in Lemma 1 and 2 sufficient for  the P-map finder algorithm output the true structure?


2. The key assumption that when a new variable $Y$ is added to the existing set $X$, that no new edges get assigned between the elements of $X$, this assumption needs further explanation. This seems to be a necessary condition of the algorithm to have low computational cost. In many situations, the introduction of a new variable might introduce new dependencies between existing nodes, e.g., in root-cause analysis, causal learning, molecular prediction, and others. Also, such situations could occur in time evolving DAGs. Further discussion on these will illustrate the applicability of the proposed method to different problems. 


3. Minor Comment:
i. In abstract, algorithm named PC might not be known to general readers. Similarly, FCI. Some of these acronyms are not defined.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper proposes an extendable stracture learning method for Bayesian networks, which updates an existing network by adding new variables. The authors also propose a iterative approach for structured learning by starting with a small set and adding the remaining variables to the P-map graph. The authors run the extendable PC algorithm on multiple datasets, and show that their approach requires fewer number of CI tests compared to the original approaches.

### Strengths
- The paper is well organized. The notations and definitions are mostly self contained.
- The authors provide experiments on multiple datasets, and show that their approach save significant runtime because of the fewer number of CI tests required in the proposed iterative method. 
- The proposed method seems straightforward and easy to implement in practice.

### Weaknesses
I am not an expert on this line of literature. My main concern is that the paper seems very heuristic with no formal guarantees: 
- While the experimental results look good, I wonder if the proposed method of extendable PC has any consistency, faithfulness, or optimality guarantee. Specifically, it's unclear if the algorithm converges to the correct P-map under standard assumptions, and whether the output is invariant to the order in which variables are added in the extendable setting. The lack of theoretical analysis makes it difficult to assess the robustness of the approach.
- The results in Table 2 - 3 suggest that extendable PC always has a better runtime with fewer number of CI tests compared to PC. Can that be proved? It would be beneficial to have a formal proof or at least a more detailed explanation of why this is the case, rather than relying solely on empirical evidence. A theoretical analysis of the number of CI tests in the extendable PC algorithm would be valuable.
- The result in Table 5 shows that the proposed iterative PC does not always require fewer CI tests compared to PC. Under what statistical or topological conditions will that happen? In my opinion this is be the bigger risk, because without any theoretic characterization, this shows the possibility that the proposed approach does not generalize. The paper should provide a more rigorous analysis of the conditions under which the iterative approach fails to reduce the number of CI tests, and the potential impact of variable ordering on the performance of the algorithm.

### Questions
- Is there any bound on the total number of CI tests required for running Algorithm 3?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents an efficient method for updating Bayesian network structures as new variables are introduced, eliminating the need for retraining from scratch. The approach reduces computational costs by up to 1300x without sacrificing accuracy. The authors also propose an iterative strategy that builds the network iteratively, thereby offering runtime benefits comparable to common algorithms like PC while maintaining accuracy. This scalable approach is well-suited for real-time and high-dimensional applications.

### Strengths
1) A simple iterative type algorithm for learning bayesian networks, which is computationally efficient. 
2) Insights on unidentifiability and its relationship to faithfulness of the graph. 
3) Backed up by theoretical claims

### Weaknesses
n/a

### Questions
n/a

### Soundness
3

### Presentation
3

### Contribution
3
