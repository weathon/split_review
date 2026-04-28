# Training One-Dimensional Graph Neural Networks is NP-Hard

- Decision: Accept
- Avg Score: 6.40
- Scores: 8, 6, 6, 6, 6

## Abstract
We initiate the study of the computational complexity of training graph neural networks (GNNs). We consider the classical node classification setting; there, the intractability of training multidimensonal GNNs immediately follows from known lower bounds for training classical neural networks (and holds even for trivial GNNs). However, one-dimensional GNNs form a crucial case of interest: the computational complexity of training such networks depends on both the graphical structure of the network and the properties of the involved activation and aggregation functions. As our main result, we establish the NP-hardness of training ReLU-activated one-dimensional GNNs via a highly non-trivial reduction. We complement this result with algorithmic upper bounds for the training problem in the ReLU-activated and linearly-activated settings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the computational complexity of graph neural networks, with a focus on one-dimensional GNNs. The primary result is the NP-hardness of training ReLU-activated one-dimensional GNNs. In addition, the paper provides algorithmic upper bounds for the training problem in the ReLU-activated setting, and shows that the one-dimensional, edgeless setting can be solved in polynomial time, as can the linear-activation case.

### Strengths
S1. The paper studies an interesting problem that has received little attention in the graph learning community and provides an intriguing result. 

S2. The proof technique is innovative, with an elegant reduction based on a non-intuitive connection between a graph learning task and a logic problem. 

S3. The paper is well-written. In particular, the results are presented very clearly and proofs are logically structured and readily followed.

### Weaknesses
W1. It is challenging to see how the main result extends our understanding of GNNs in an important way. From the perspective of intellectual curiosity, I can appreciate the work as a welcome answer to a question. The proof technique is innovative and elegant. But in most cases, both practical and theoretical (in terms of quantifying the expressive capabilities of a GNN), we are interested in the multi-dimensional setting. Aside from this, the theoretical work focused on pushing the bounds of expressivity has veered away from the simple message-passing approach. The authors don’t provide a clear explanation in the introduction or the conclusion concerning how the presented work is expected to provide further impact. 

For many problems, if we want to understand the multi-dimensional setting, then it makes a great deal of sense to first understand the one-dimensional setting. That doesn’t seem to be so clearly the case here, since we already know that the multi-dimensional setting is NP-hard. So how do we gain from deriving special-case results for the one-dimensional setting that can’t be extended to the practically interesting case?

W2. The paper focuses on the (semi-supervised) node classification setting of graph neural networks. While this is clear from Section 2 onwards, it is not mentioned in the abstract or introduction. Graph classification is a very common use case of GNNs, and many of the theoretical results concerning expressivity focus on a GNN’s ability to differentiate between two graphs. The abstract, introduction and limitations section should make the limitations of the derived results much clearer.

### Questions
Q1. The paper presents an interesting result and the proof is innovative. On the other hand, as raised in W1, it is challenging to see how this extends our understanding of GNNs in an important way. Could the authors provide an explanation of how they expect the provided results to impact further theoretical work that studies GNNs in the more interesting multi-dimensional setting? Or to the settings that go beyond message-passing (which has known limitations in its expressiveness)? Is there a way to build on the presented proof techniques and use similar concepts for other problems?  

Q2. Can the results be extended to the graph classification setting? (Or if it is potentially challenging, can you see paths towards this? Or would it require a totally different approach?) 

Q3. Can the authors comment on any connections with their work and the line of research that investigates logical expressiveness (e.g., [R1,R2])? Perhaps there is not an obvious connection, but it would seem that characterization of the types of logical expressions that GNNs are capable of describing has connections to a complexity proof that relies on a linkage to a logic problem. Related to Q1, this branch of work usually assumes a vector at each node, and this is key to expanding the expressive capabilities.

[R1] M. Grohe, "The Descriptive Complexity of Graph Neural Networks," 2023 38th Annual ACM/IEEE Symposium on Logic in Computer Science (LICS), Boston, MA, USA, 2023.

[R2] Barcelo et al., “The Logical Expressiveness of Graph Neural Networks,” in Proc. ICLR, 2020.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper investigated the computational complexity of training GNNs, with a particular focus on the NP-hardness of one-dimensional GNNs, and authors demonstrated that training ReLU-activated GNNs is NP-hard under specific aggregation functions, such as SUM, MEAN, and SPECTRAL Additionally, the paper established upper bounds on algorithmic efficiency and examines how different network architectures affect training efficiency.

### Strengths
1. In section 4, the paper clearly constructed a graph that intuitively represents the structure of GNNs, effectively describing the nodes, edges, and the logical relationships associated with Boolean variables, and it also designs several gadgets to ensure the resolution of the SAT problem, providing an excellent insight into the complexity of GNN training.

2.  The paper presented a rigorous theoretical derivation and, in Section 5, established a general algorithmic upper bound for solving ReLU-GNNT, providing an important theoretical framework regarding the complexity and feasibility of training ReLU-GNNT.

3. The paper proved the NP-hardness of training graph neural networks, which provides an important conclusion for exploring the complexity of training GNNs.

### Weaknesses
1. In line 308, when constructing the graph in Section 4, the author explained that gray edges and gray dummy vertices are introduced to ensure the nodes have degrees of 2, 4, or 6. What is the rationale behind it? Is it only applicable when the node degree is even, rather than simply being constrained to the specific values of 2, 4, or 6? The author could enhance clarity by providing further explanation on this matter to improve the readability of the paper. Specifically, it's unclear why these specific degree constraints are necessary for the subsequent proof. A more detailed explanation of how these degree constraints facilitate the construction of a regular graph, and why a regular graph is crucial for the NP-hardness proof, would be beneficial. It would also be helpful to understand if other degree constraints could also be used and what would be the implications.

2. The paper researched the NP-Hardness of training ReLU-activated one-dimensional GNNs. The conclusion is primarily correct for the ReLU activation function. If the GNNs' activation function is changed, such as to Sigmoid or Leaky ReLU, the conclusion may be affected. It would be helpful if the authors could provide more theoretical analyses regarding this issue to make the paper more persuasive. The paper should discuss the limitations of the current proof with respect to different activation functions. For example, how would the proof strategy need to be modified, or what new challenges would arise, if Sigmoid or Leaky ReLU were used? A discussion of the mathematical properties of these activation functions that make the current proof inapplicable would strengthen the paper.

### Questions
Refer to wekenesses.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The main result is showing NP-hardness for training a 1-dimensional GNN (i.e. the input dimension and width are 1). The proof uses a reduction from the positive-1-in-3-SAT problem. Several other results are given such as exponential time algorithm for training 1-d GNN, polynomial time algorithm for training GNN on edgeless graphs, and polynomial time algorithm for training a linear GNN.

### Strengths
- The main result (Np-hardness of 1-d GNNs) is interesting and uses a non-trivial reduction.

- The supplementary results, provide further insights into the problem.

### Weaknesses
 - There is no related works section, so it is difficult to position this paper w.r.t previous works. For me, it is difficult for me to determine how novel the result is since I don’t know previous works on the hardness of learning GNNs. It would be helpful to provide a thorough literature survey and more in-depth comparisons to previous works.

- Froese and Hertrich 2023 show that training neural networks is NP-hard even for input dimension 2. Can’t this result be used on GNNs for edgeless graphs using Proposition 2? If so, the contribution of this paper seems incremental as it improves the hardness result from input dimension 2 to input dimension 1.

- The hardness works only for node classification tasks. There should be a discussion about graph-level tasks, which are widely used in practice (perhaps even more than node-level). As a remark, it is OK to focus on node-level tasks, but still, graph-level tasks should be at least discussed on some level.

On the presentation level, the introduction is a bit long and convoluted (almost 3 pages long), which makes it difficult to understand the main message of the paper.

### Questions
- How does this work compare to previous works? Specifically, are there any previous works on the hardness of learning GNNs? 

- Can the hardness result from Froese and Hertrich 2023 on 2-d networks be transferred to GNNs?

- The depth of the GNN in Theorem 1 isn’t mentioned. Does it work for any depth?

I am willing to reconsider my score based on the author’s response.

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
The paper shows that 1-dimensional GNN training is hard. In precise wording, for a $L_p$ norm error, finding the optimal weights and biases that decreases the error between the predicted label and the ground truth label lower than a threshold (decision problem) reduces to 1-in-3 SAT problem (same as SAT but each clause has to be satisfied with only one variable). 

The paper is novel in sense that other hardness results for neural networks can be used for applied to multi-dimensional GNNs, but here the authors show the same for 1-dimensional which in NNs there is a polynomial time search for it.

The authors follow by introducing algorithmic upperbounds for special cases of NN training and GNN training.

### Strengths
The approach to the problem was really non-trivial. The target reduction problem was unexpected to me and like any other algorithmic lower bound, the reduction requires novel approaches in problem design.

### Weaknesses
I assume Observation 3. is just a rephrasing of Theorem 1. If so, why it is repeated?

Although the problem is really interesting, and the work has a lot of novel ideas for tackling the problem, still I am not sure (1) if the paper is presented in a correct subject (e.g. if there is any theoretical study of NNs or some similar categories it belongs to that category where reviewers have better background on complexity study) and (2) I am still unclear about the impact of the work in application. Surely it is a theoretical study and we should not expect direct real-life applications but the study is in a corner case (1-d GNNs) where for more dimensions the results are already showing NP-hardness. It would be better if the authors could discuss the potential implications of this work for GNN training in general.

**Theorem 1.** The reduction is nice, however the intuition behind this reduction is still unclear. Although polynomial reductions are essentially not easily understandable, and are mostly innovative, there are intuitive descriptions that can make the reduction understandable. I still am not sure if the proof is completely correct since most of the parts in the proof are still not understood by me..

A list of questions are provided in "questions" section. I recommend writing the proof (or sections before it) again considering the questions, so an abstract image of this reduction becomes clear.

However the gadgets and a high-level shape of the problem is illustrated, still the designed graph is not clear. It would elevate the paper's quality if the reader could imagine a sample graph for even a very small 1-in-3 SAT problem. The number of layers is also not determined. In case (from lemma 4) the 2-layer GNN is representative of any other GNN, the authors could mention that and for a sample SAT instance, show the weights of the optimal network, and the graph.

### Questions
I believe the core part of the paper is Theorem 1, and with the theoretical nature of the work the qualification of the paper mostly boils down to checking the proofs. However the proof, and the theorem statements are unclear. I think answering following questions can help me to understand it more, and also placing these answers in the paper enhances its readability:

1. What does the ranks encode. Why there are 2 ranks per node. How a node is assigned to a rank? The authors just introduced the terminology while leaving out the intuition behind using it. Specifically what does this sentence mean?
> In particular, our construction partitions the vertices of the instance into ranks and ensures that the only “relevant” feature values at layer l are precisely the values of vertices belonging to rank l.

2. In theorem 1, and in general please specify what is the range of the labels. It can be that the labels assumed in theorem 1, range differently compared to the more general setup.  

3. Please specify the correct labels of the graph in general. Which nodes should be labeled? which nodes are left without labels? 

4. Please specify a simple case of 1-in-3 SAT (e.g. with one or two clauses) alongside the corresponding instance of GNN training so it becomes clear what each gadget is introducing to the problem. 

5. Number of the layers are not fixed at the beginning of the problem. From lemma 4 it is understood that a 1, or 2 layer GNN is representative of the overall problem. Is that so? If yes please specify that without loss of generality we can assume 2, layers. 

6. (Similar to 5) Why there is no relation between the number of layers and any other element in the corresponding graph. The graph seems to be only a function of the 3-in-1 SAT problem. In that case what is the difference between 2 and any n-layer GNN?

7. Why the rank in integrity gadget is 2n, 2n+1 and then again 2n? How many times a clause is repeated as gadgets? Why in the integrity gadget the grey center node is not connected to the black one? 

8. What is the configuration of labels w.r.t. clauses in the SAT problem? Please provide an example SAT and show the graph and model labels alongside the prediction of the model.

9. What is the loss in the decision problem corresponding to a given SAT instance?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigate the computational complexity of training GNNs.  While it is straightfoward that training a high-dimensional GNN with a single node is NP-hard, the paper focuses on the less explored case of training multi-node, one-dimensional GNNs. The authors prove that training 1-dimensional GNNs is NP-hard when (i) the loss function is $L_p$ for some $p\in[0,1)$; (ii) the aggregation functions is SUM, MEAN, or SPECTRAL; and (iii) the activation function is ReLU. The proof is an reduction from the NP-hard POSITIVE-1-IN-3-SAT problems.

### Strengths
The results are solid and contribute to our understanding of the computational hardness of training GNNs.

### Weaknesses
1. The paper should provide a definition of the POSITIVE-1-IN-3-SAT problem when introducing the proof idea in the Introduction.
2. It would be helpful to expand the discussion on the assumptions of the main theorem. For instance, is the problem still NP-hard for more commonly used loss functions, such as cross-entropy or $L_2$?
3. The paper could benefit from a more explicit discussion on how these theoretical results might influence the design of GNN architectures or training algorithms in practical applications.

### Questions
Refer to "Weaknesses"

### Soundness
3

### Presentation
2

### Contribution
3
