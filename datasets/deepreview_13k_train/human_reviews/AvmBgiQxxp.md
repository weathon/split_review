# Scalable Decentralized Learning with Teleportation

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Decentralized SGD can run with low communication costs, but its sparse communication characteristics deteriorate the convergence rate, especially when the number of nodes is large. In decentralized learning settings, communication is assumed to occur on only a given topology, while in many practical cases, the topology merely represents a preferred communication pattern, and connecting to arbitrary nodes is still possible. Previous studies have tried to alleviate the convergence rate degradation in these cases by designing topologies with large spectral gaps. However, the degradation is still significant when the number of nodes is substantial. In this work, we propose TELEPORTATION. TELEPORTATION activates only a subset of nodes, and the active nodes fetch the parameters from previous active nodes. Then, the active nodes update their parameters by SGD and perform gossip averaging on a relatively small topology comprising only the active nodes. We show that by activating only a proper number of nodes, TELEPORTATION can completely alleviate the convergence rate degradation. Furthermore, we propose an efficient hyperparameter-tuning method to search for the appropriate number of nodes to be activated. Experimentally, we showed that TELEPORTATION can train neural networks more stably and achieve higher accuracy than Decentralized SGD.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work studies a decentralized optimization algorithm whose convergence rate does not deteriorate with increasing number of nodes. Usually, when number of nodes in a network increases, the spectral gap, i.e., $(1 - p_n)$ (according to the notation of the paper), also increases. Larger spectral gap means that decentralized SGD requires a larger number of iterations to converge.

In order to make decentralized SGD scalable for large networks, the proposed algorithm randomly activates a small subset of nodes by randomly sampling them. These nodes get the updated models from nodes activated in the last iteration, does a descent step, and subsequently communicate with other nodes active in the current iteration to do a local consensus step (only amongst the currently activated node). this process is repeated over multiple iterations.

The paper analyzes the convergence of this algorithm, and also provides an efficient algorithm to tune the number of active nodes.

### Strengths
The paper is generally well-written. The problem statement being addressed is clear, and the proposed algorithm is also quite simple. The paper does a commendable job analyzing their proposed algorithm, in addition to validating numerically. The assumptions are also clearly stated, which are quite standard in decentralized optimization.

The work also compares their algorithm with client sampling, which is a natural question that came to my mind while reading the paper, and I appreciate that it was answered. I have a few concerns and would be glad if these are addressed. Despite my concerns, I strongly believe that within the current scope of the problem statement considered in the paper, it is adequately addressed.

### Weaknesses
I would appreciate it if the authors would answer some of my concerns.

1. How are the consensus weights $\mathbf{W}$ chosen, and how is it assumed that the randomly activated nodes at any iteration know these weights? 

2. How are the nodes sampled? Are they sampled uniformly at random? Would it help if the nodes were sampled taking some other criteria in mind, such as activating nodes that are more likely to have an edge between them? More generally, how do the authors expect the sampling to be implemented in practice in a fully decentralized topology? More generally, can the authors highlight a practical application scenario?

3. The paper would benefit with some explicit discussion on the dependence of the node-selection strategy, and/or the required number of active nodes on the network topology? For instance, it seems like if the network is sparse, perhaps more nodes need to be activated at every iteration?

4. Will it make sense to change the number of activated nodes in every iteration?

I must acknowledge that I am not completely familiar with the current literature in topology selection for decentralized optimization. So I cannot definitively comment on the novelty of the paper, but based on how it is placed in the writing itself, the contribution seems non-trivial (despite the weaknesses mentioned here).

### Questions
I have some more questions which are not very critical, but I believe that the paper will benefit from:

1. In the current proposed algorithm, data heterogeneity is not taken into account. Some discussions on how the algorithm might need to be modified in the presence of data heterogeneity would be appreciated. Perhaps optimizing the weight matrix $\mathbf{W}$ would be helpful?

2. Although less related, in light of the popularity of federated learning literature, the privacy of activated nodes might be an important criteria to consider. Since each node knows which node participated in the previous iteration, this can lead to some degree of privacy leakage, that needs to be quantified. (Please note that I do not see this as a major drawback of the paper -- it is just a suggestion). It ties more with my previous question of practical application scenario, where the network has a large number of nodes, so privacy becomes important.

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
4

### Summary
This paper proposes a novel decentralized algorithm designed to perform well when the number of nodes $n$ is very large. The proposed algorithm synchronizes a smaller set of local states $\\{z_i\\}_{i \in \\{1,...,k\\}}$ for $k < n$ by running a single step of Decentralized SGD (DSGD) [Lian et al., 2017] on a subgraph of $k$ nodes, and then transfer the local states to another set of $k$ nodes for computing the gradients of other local objectives. Such algorithm is suitable for fully-connected distributed system. The proposed theorem suggests that this algorithm enjoys linear speedup by the total number of nodes $n$, at the cost of consuming $k$ local gradient computations only.

### Strengths
- The idea of sacrafising gradient updates of the whole network in favor of maintaning lower consensus error is novel.

### Weaknesses
 - In line 268, $k$ can be simplified as 
$$k = \max\left\{ 1, \min \left\{\left\lceil \left(\frac{T(\sigma^2 + \zeta^2)}{Lr_0} \right)^{1/7} \right\rceil, n \right\} \right\}$$
because $a^{1/7} < a^{1/5}$ for any $a > 1$.
- The main claim of Theorem 2 might be theoretically flawed and deserves more attention, which relates to the $n$ linear speedup results. More discussion is provided in the section Questions: (**About the proof of Lemma 9**).


### Questions
(**About experiment**)
- I suggest the authors to plot the convergence of consensus error in the experiments as well. This can give a clearer picture to whether the $k$ nodes interaction in the proposed algorithm achieve faster convergence in consensus error than the $n$ nodes interaction in Decentralized SGD.

(**About the proof of Lemma 9**)
- Let's make it clear when does the dominance order changes in (14) for different values of $k$ by the following statements:
$$ \sqrt{A/k} \leq Bk^{2/3} \Leftrightarrow k \ge (A^3 / B^6)^{1/7} \quad \cdots (*)$$
$$ \sqrt{A/k} \leq Ck^{2} \Leftrightarrow k \ge (A / C^2)^{1/5} \quad \cdots (**)$$
Then, by the choice of $k$ in line 1099, 
- when $k = \lceil (A^3 / B^6)^{1/7}\rceil \leq \lceil (A / C^2)^{1/5}\rceil$, $(*)$ is true while $(**)$ is false, i.e., $\sqrt{A/k} = \mathcal{O}(Bk^{2/3}) = \mathcal{O}(A^{2/7}B^{3/7})$ and $Ck^2 = C A^{6/7} B^{-12/7}$. Then line 1106 should be $\mathcal{O}(A^{2/7}B^{3/7} + C A^{6/7} B^{-12/7})$ instead.
- when $k = \lceil (A / C^2)^{1/5}\rceil \leq \lceil (A^3 / B^6)^{1/7}\rceil$, $(**)$ is true while $(*)$ is false, so that by the similar arguement line 1112 should be $\mathcal{O}(A^{2/15} B C^{-4/15} + A^{2/5}C^{1/5})$.
- when $k = n \leq \min\{ \lceil (A^3 / B^6)^{1/7}\rceil,  \lceil (A / C^2)^{1/5}\rceil \}$, both $(*)$ and $(**)$ are false and line 1117 should be $\mathcal{O}(\sqrt{A/n} + Bn^{2/3} + Cn^2)$.
Therefore, none of the above cases show a convergence bound that is consistent with the main claim in Theorem 2, i.e., a linear speedup with total number of nodes $n$. May I request the authors to address this issue, and point out my mistakes if I am wrong in the above calculation. 
- The similar argument applies to the proof of Lemma 10.

(**Connection to DSGD**)
- We can equivalently interpret the proposed algorithm as a DSGD [Lian et. al., 2017] algorithm of $k$ nodes and each node has access to all local objective $f_i, ~i\in \\{1, ..., n\\}$. Each iteration of the proposed algorithm with an active node set $V^{(t)}$ corresponds to an iteration of the above-mentioned DSGD algorithm where $\\{\nabla f_j(z^{(t)}_{{\rm token\\_id}_j^{(t)}}, \xi_j^{(t)}): v_j \in V^{(t)}\\}$ are the sampled local gradients. Therefore theoretically, by the results of [Lian et. al., 2017], I expect that the proposed algorithm to only achieve the linear speedup of $\mathcal{O}(1/\sqrt{kT})$. 
- Also, by the above equivalence, the proposed algorithm is only serving as a new implementation of DSGD on large graph without data heterogeneity, i.e., $\varsigma = 0$ in Assumption 1.3 of [Lian et. al, 2017].

- I suggest the authors to consider along this argument and compare with DSGD in the main text in terms of such equivalence. Also, since this algorithm  is potentially only contributing an efficient large graph implementation of DSGD, I suggest the authors to expand the experiment section with larger scale experiments such as larger dataset and larger number of nodes $n> 100$.

### Soundness
2

### Presentation
4

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
This paper introduces a method called TELEPORTATION aimed at improving decentralized learning, particularly decentralized stochastic gradient descent (SGD). 

TELEPORTATION is have a better dependence on the spectral gap of the communication graph in the convergence rate. So, the authors claim that their method can alleviate the convergence rate degradation while maintaining communication efficiency. 

They also propose a method to optimize the number of active nodes so as to fasten the convergence rate. 

The experiments suggest that TELEPORTATION outperforms decentralized SGD in both convergence speed and stability, especially when data distribution is uneven across nodes.

### Strengths
1. **Reduced Communication Overhead**: 

The paper proposes a practical solution to reduce the communication costs in decentralized learning by activating fewer nodes. The methods developed to tune the hyperparameters would inspire future work.
 
2. **Clear Theoretical Analysis**: 

The paper provides solid theoretical support for the claims, including convergence rate bounds and proofs for the proposed method.  

3. The paper is mostly well-written and easy to follow.

### Weaknesses
1. **Lack of Clarity in Problem Formulation**:  
   The paper could benefit from a clearer and more formal description of the problems posed by decentralized learning, particularly why more nodes lead to degraded performance. Without this clarification, it becomes difficult to fully appreciate the novelty and impact of TELEPORTATION. The paper should explicitly address the mechanisms that cause performance degradation with increasing node counts, such as the increased variance in gradient estimates due to asynchronous updates and the challenges in maintaining parameter consistency across a larger network. A more detailed explanation of how these factors interact to slow down convergence would be beneficial.

2. **Loose Theoretical Guarantees**:  

   Beyond Proposition 1, the paper could be more rigorous in establishing the tightness of the bounds used to justify the method's benefits. A deeper exploration of whether these bounds hold tightly in practical cases (e.g., through empirical validation or consider quadratic cases) would enhance confidence in the theoretical contributions. The analysis relies heavily on upper bounds, but it lacks a discussion of the lower bounds and whether the derived bounds are tight. This is crucial because loose bounds can lead to misleading conclusions about the method's performance. It would be valuable to see a discussion of the tightness of these bounds, perhaps through a comparison with known lower bounds or by examining specific scenarios where the bounds are tight or loose.

3. **Limited Practical Applicability**: 

   The assumption that any two nodes can communicate directly (as mentioned in the abstract and discussions) is overly idealized. In many real-world applications, such as wireless sensor networks or geographically distributed systems, this assumption may not hold. The paper should acknowledge this limitation and discuss potential extensions or modifications to the method to handle more realistic communication constraints. For instance, the authors could consider scenarios with limited communication ranges or time-varying network topologies, which are common in practical decentralized learning settings.

### Questions
1. **Convergence and the Number of Nodes**:  
   I am unsure why decentralized learning methods should necessarily converge more slowly as the number of nodes increases (line 53-line 60). In fact, in fully synchronized systems, having more nodes typically leads to a linear speedup in convergence. It would be helpful if the authors could clearly formulate why this slowdown happens in decentralized settings and explicitly highlight the limitations of existing methods. A more specific problem formulation, accompanied by examples illustrating why current approaches fail to address this, would make the contribution clearer. (e.g., using a table summarizing existing results).

2. **Discussion on Proposition 1**:  

   The discussion in lines 140-148 seems to rely on the upper bound from Proposition 1. However, this argument feels weak, as the tightness of the upper bound is never discussed. If the bound is loose due to flaws in the analysis, the subsequent discussion would be rendered meaningless. Is there any way to demonstrate that the bound is tight? For instance, you could explore the behavior of a simple quadratic function to provide more concrete support for this bound.

3. **Explanation of Theoretical Improvements**:  

   It appears that the theoretical improvement primarily stems from the dependence on $p_n$. Could the authors clarify the source of this improvement? Is it driven by a more refined analysis, or is it due to a novel aspect of the algorithm itself? Providing a brief but clear explanation of what underlies this theoretical gain would strengthen the paper.

4. **Unclear Impact of Hyperparameter Tuning**:

   The proposed hyperparameter-tuning method for selecting the number of active nodes adds another layer of complexity to the method. However, the impact of this additional tuning on overall training time and resource consumption is not fully explored. In practice, the benefits of communication reduction could be outweighed by the cost of hyperparameter search. A detailed examination of this trade-off would provide more practical insight.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses degradation in decentralized learning arising from fixed communication patterns. Given the flexibility to select both a communication pattern and a subset of active nodes, the authors propose the TELEPORTATION algorithm. This algorithm activates k nodes per iteration and applies a specific topology to these nodes, facilitating adaptable communication.

The convergence analysis for TELEPORTATION follows the approach used by Koloskova (2020b), extending it to any number of active nodes k. Additionally, the authors provide an efficient method for tuning k, including determining optimal values for specific graph types, such as rings and exponential graphs, where they establish the theoretically best k and its associated convergence rate.

Experimental results demonstrate that TELEPORTATION consistently outperforms decentralized SGD across various settings and graph structures, reinforcing its potential advantages in decentralized learning.

### Strengths
The primary strength of this paper lies in its proof of Theorem 1, which effectively addresses a key limitation in previous analyses of similar algorithms. Prior approaches encountered challenges due to the disconnectivity of graphs under certain node activation conditions (e.g., when p=0), resulting in an infinite bound on the number of iterations required for convergence. Remarkably, this paper recovers the bound obtained by Kolosokova (2020b) under a generalized node selective activation scheme, which could prove potential for future research in this domain.

In addition to the theoretical insights, the paper is also notable for its clear presentation of contributions. The experimental section is both comprehensive and persuasive, further validating the authors' approach and supporting the potential utility of their bound.

### Weaknesses
Even though the distinction of TELEPORTATION from client sampling has been discussed, it still looks to me a follow-up variant in this category (McMahan 2017), and client sampling has been a heavily discussed approach. In the special case where any node is allowed to connect to any node, decentralized learning with client sampling is a very natural idea. Admittedly the proof of this paper could be something new, but the approach they proposed, at least in practice, might have been discussed/implemented allready. In particular, it is expected  when you select a fixed graph of size k, where its spectral gap is known for example in ring and exp. graph, the spectral gap does not show up in the bound. In this sense, "completely alleviate the convergence rate degradation" is not that interesting any more.

Minor: there are no black nodes in Figure 1.

### Questions
What are the Base-2 graph and what do you mean by superiority of this graph?

### Soundness
3

### Presentation
3

### Contribution
2
