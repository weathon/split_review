# Valid Conformal Prediction for Dynamic GNNs

- Decision: Accept
- Scores: 8, 8, 5, 3, 5

## Abstract
Graph neural networks (GNNs) are powerful black-box models which have shown impressive empirical performance. However, without any form of uncertainty quantification, it can be difficult to trust such models in high-risk scenarios. Conformal prediction aims to address this problem, however, an assumption of exchangeability is required for its validity which has limited its applicability to static graphs and transductive regimes. 

We propose to use unfolding, which allows any existing static GNN to output a dynamic graph embedding with exchangeability properties. Using this, we extend the validity of conformal prediction to dynamic GNNs in both transductive and semi-inductive regimes. We provide a theoretical guarantee of valid conformal prediction in these cases and demonstrate the empirical validity, as well as the performance gains, of unfolded GNNs against standard GNN architectures on both simulated and real datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The purpose of this paper is to provide valid prediction sets (with finite sample guarantees) achieved through conformal prediction for GNNs on dynamic graphs. In this setting, the graph evolves through time and can thus be represented as a set of adjacency matrices" nodes are fixed, but edges can appear and disappear at each time point. Each node is also endowed with a set of potentially varying features and labels.

To provide prediction sets (ie, sets of labels for each nodes such that the real label is within the set with, say, 95% probability), the authors suggest leveraging unfolding, a tool stemming from the tensor literature. The procedure they describe is as follows:
- 1- create an unfolded adjacency by concatenating all the adjacency matrices (columnwise),  yielding a matrix of size 2nT  * 2nT. Same for the features: X_unf is of size nTp.
- 2- apply a GNN on the unfolded adjacencies and features to output a set of global representations for each of the nodes (meaning, global across time points), and "local" representations (node/time pairs).
- 3 -compute conformity scores to output prediction sets.

The authors  show that this procedure can help them get uncertainty estimates for 3 types of scenarios: transductive, timewise transductive, and semi-transductive.
The authors then proceed to show the results of numerous experiments (synthetic and on real data). More specifically, they use as benchmark a block GNN (GNN fitted on the block diagonal adjacency, essentially treating each snapshot as a different graph). The authors show that the block approach creates "block" effects when there should be none, and this also results in higher accuracy of the UGNNs over the block approach, and lower set sizes.

### Strengths
This paper proposes an interesting approach to uncertainty quantification in the context of dynamic graph. The method that they propose is new, but leverages existing methods in the GNN and conformal prediction literature.

The examples chosen by the authors are quite strong and compelling.

### Weaknesses
On the whole, I think this is a good paper, but perhaps a couple of modifications would clarify certain aspects:
1- Some of the notations could be clarified. For instance, I found the part explaining the procedure a little confusing. More specifically:
- $\hat{X}^{UNF}$: since X is already used to describe features, another letter would be preferable here. I originally thought that it meant the unfolded features.
- Similarly,  $\hat{Y}^{UNF},$ I thought this meant the unfolded labels.
- It would be great to add the dimensions (only  $\hat{X}^{UNF}$ is indicated to have dimension $n_r \times d$). 
- Would it be possible to replace $n_r$ by $n$? I personally find the subscript to be more justified to indicate a refinement, such as when, say, there would be different numbers of nodes across time points. I (personally) find that here, it invites more questions than would be necessary.

2- the UGNN framework could be further detailed:
- I am personally not familiar with the dilated unfolding approach of Davis, and consequently don't really understand the training procedure. $Y^{UNF}$ corresponds to the time-node pairs, so they should be trained with the node/pair labels?

3- the current challenges in deploying CP to graphs could be clearer: it seems to me that the main contribution of the paper is the unfolding mechanism, that allows (a) better representation of nodes in embedding spaces, and that consequently (b)  lends itself well to UQ using CP. Maybe a reformulation of the introduction highlighting that some of the challenges in CP on graph embeddings would be a distribution shift of the embeddings if there is a batch effect could help highlight the contribution of the method. Currently, it is succintly mentioned ("de-alignment between embeddings across time points"), but I think this should be expanded upon to highlight current challenges and set the context a bit more clearly.

### Questions
My questions pertain the implementation of the method (see weaknesses).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors established a novel conformal prediction method for dynamic GNNs, where edges evolve over time, like transport and social networks. The primary contributions are as follows:

1. Dynamic Graph Representation for GNNs: an "unfolding" technique for representations of dynamic graphs has been proposed to achieve reliable prediction sets, compared to the original block representations.

2. Inference Scenarios: The authors fully discussed various inference scenarios specific to dynamic graphs, including transductive, temporal transductive, and semi-inductive regimes, with valid and reasonable assumptions if needed.

3. Empirical Validation and Practical Applications: Using several real-world datasets as well as simulated data, the proposed method demonstrates improved metrics over baseline approaches, with particular advantages in the semi-inductive case, showing great potential in analyzing various dynamic graph systems.

### Strengths
1. Originality: One innovation in this paper is introducing the “unfolded” dynamic graph representation, which allows standard GNNs to process dynamic graphs while maintaining the validity of CP techniques. Additionally, the paper extends CP applications to multiple dynamic graph inference cases, for example, semi-inductive regimes, which is pretty challenging in discovering missing labels.

2. Quality and Clarity: The authors provided clean and rigorous theoretical analysis in explaining how its method achieves valid predictions under varied dynamic settings, supported by well-defined assumptions and conditions for applicability in different inference scenarios. Visualizations like bar graphs and tables further help readers understand the reasonableness and benefits of the unfolded approach compared to the baseline. 

3. Significance: The paper addresses an important issue in uncertainty quantification for dynamic GNNs, where given reasonable prediction intervals over time is essential. The basic idea for this approach seems to have great potential for scaling up, therefore advancing the applicability of GNNs with evolving edges.

### Weaknesses
1. Semi-Inductive Settings:

As the authors acknowledged, the assumption of exchangeability may not hold in many real-world cases, necessary discussions for mitigating it would be appreciated. For instance, if adapting robust techniques from time-series, like basic ARIMAs, or even neural SDEs might be useful. The core issue is that the temporal dependencies in dynamic graphs often violate the i.i.d. assumption underlying conformal prediction, particularly in semi-inductive settings where future data may exhibit distributional shifts. While the authors mention the potential for weighting more recent data, a more detailed exploration of methods that explicitly model temporal dependencies, such as incorporating lagged graph structures or using recurrent neural networks to capture temporal patterns, would be beneficial. This is especially important when the graph structure itself is evolving over time, as the unfolded representation might not fully capture the complex temporal dynamics.

2. Understanding UQ:

Though I acknowledged the authors’ efforts in providing extensive metrics, it would be insightful to how to interpret the size of prediction sets correlates with meaningful uncertainty in a dynamic graph. This could help researchers from other backgrounds understand the logic, and make benefits for them. Making a plot showing the coverage (if possible) will make the paper more solid. Specifically, the paper lacks a clear explanation of how the width of the prediction sets relates to the underlying uncertainty in the graph's evolution. For example, in a social network, a wider prediction set might indicate a period of high flux or instability in relationships, while a narrow set could suggest a more stable period. A visualization that directly links prediction set size to the graph's dynamic properties, such as edge density or community structure changes, would greatly enhance the interpretability of the results. Furthermore, a coverage plot over time would be crucial to demonstrate the reliability of the conformal prediction method, especially under different dynamic conditions.

3. Miscellaneous:

I suggested the reviewers consider the following issues, and if time allows, do some elaboration.

a) If there is any other way to reshape the dynamic graph from $(T, N, N)$ into a 2D-shape, e.g. compared the performance the reshaped matrix in shape $(T, N^2)$.

b) Another simplification on the current $A^{UNF}$ might be: $A^{(1)}$ at top left, and the remaining unfolded $\mathcal{A}$ dilated in the same way. I would consider if this will somehow reduce the complexity, especially when $T << N$.

c) In this paper the dynamical graphs always mean edge-evolving ones. There are also cases where nodes are evolving with time, or even both edges and nodes are changing, e.g. pandemic networks (with different types of nodes, and some nodes will disappear permanently). It is appreciated if authors can do some brainstorming on this topic to provide meaningful improvements.

### Questions
Besides several concerns that mentioned in the weakness part, here are several questions regarding the paper details:

Line 88: why requires a bipartite graph? Needs to explain.

Lines 161-165: for better understanding, I would prefer the authors directly used $m$ over $m + 1$ (surely some other formula like 
Algorithm 1 also needs to be changed). But this is more neat.

Line 165: it is not encouraged to mix superscripts and subscripts in notation, especially when they share the same meanings (e.g. test pairs and calibration pairs).

Line 179: do we have any differences if we use row- rather than column-concatenation? I guess they might be the same. Please think about this.

Line 222: does column swapping means permutation? For example, is it equivalent to say, there exists a permutation matrix $P$. such that $PA^{UNF}P^T=A^{UNF, swapped}$?

Section 2.1 and Figure 1: If you can plot $A^{(1)}$ as a 2D heatmap, or the original graph using tools like networkx package, it will be better for illustration rather than just representation scatter plots. For example, the density of nodes or the color of heatmap may clear show what happened in this toy system.

Figure 2: needs a short comment on SBM evolving edges. Why is that?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper works on applying conformal prediction on dynamic graphs. The key contribution of this paper is introducing a careful mathematical consideration of different inferences in modeling dynamic graphs. Valid conformal predictions are obtained in most of the scenarios and the authors provide real data examples to prove the theory.

### Strengths
It is interesting to use block GCN to prove the validity of applying conformal prediction on dynamic graphs. The authors provide detailed and sufficient explanations and analysis on different scenarios on dynamic graph tasks. Besides, the authors provide a variety of real data examples to show the effectiveness of their theory. The paper is well-written and organized.

### Weaknesses
This paper aims to apply conformal prediction to dynamic graphs. It should include more competitive baselines that use conformal predictions on graphs. And the backbone models should be more rather than simply using GCN and GAT.



### Questions
1. This question is similar to the concerns in the weakness. Do you have more experimental results on other backbones?
2. What is the current state-of-the-art algorithm applying conformal prediction on dynamic graphs or even static graphs? The authors should include more competitive baseline methods.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on dynamic graphs. More specifically, utilizing the tool of dilated unfolding, this paper expands the traditional GNN to dynamic graphs. No modification to GNN structure is required.

### Strengths
For a sequence of graphs, the paper cleverly utilizes dilated unfolding to make it a sparse matrix $A^{UNF}$. In the semi-inductive regime, the paper shows a proof guarantee of the algorithm. A comparison with the standard block GNN is provided in Sec 2.1 and clearly shows this advantage. Experiments in Sec 3.2 also support this.

### Weaknesses
I am not an expert in GNN, so please tell me if I am incorrect. It seems the innovation in this paper is incremental because dilated unfolding is known in Davis '23. The theoretical contributions (the proof in Sec. B.1 and B.2) also seem natural.

### Questions
Could you confirm your algorithm is by combining dilated unfolding (Davis '23) and a GNN? If that is the only contribution, could you please convince me there is enough innovation provided?

### Soundness
4

### Presentation
4

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies uncertainty prediction for dynamic graphs. For the representation learning of dynamic graphs, the paper leverages the unfolded adjacency matrix as input to GNNs and for uncertainty prediction, the paper follows procedures of conformal prediction that constructs provably valid prediction sets.

### Strengths
1. The paper studies an important problem relating to uncertainty quantification for GNN prediction. 

2. The use of unfolded adjacency for GNNs on dynamics graphs is natural and promising. 

3. The experiments show promise for the proposed method.

### Weaknesses
1. The paper is poorly written with many concepts and notations not sufficiently explained. In addition, the structure of the paper needs to be improved. For example, (1) in line 161, it is not clear what it means for 'appropriate ordering of pairs', and what does m here represent? (It is better add some examples) Specifically, how are the node pairs selected and ordered for the unfolded adjacency matrix, and what is the impact of different orderings on the learned representations? The paper should clarify if 'm' refers to the number of node pairs, the number of time steps, or something else entirely. (2) What is the intuition of using dilated unfolding in line 176? How does line 181-185 work? It would be clearer if the explicit update form is written under the example of GCN. The paper does not provide sufficient justification for why dilated unfolding is beneficial for capturing temporal dependencies in dynamic graphs. The explanation of how the update equations work is unclear, particularly how the unfolded adjacency matrix is incorporated into the GCN update. A concrete example with explicit matrix operations would significantly improve clarity. (3) Algorithm 1 is introduced with no explanations on the steps. For example, what is a calibration set? The paper needs to provide a clear and concise explanation of each step in Algorithm 1, including the purpose of the calibration set and how it is used to construct the prediction sets. The connection between the algorithm and the theoretical framework is not clearly established. (4) In theory, the key definitions, such as exchanebility and label equivariant are deferred to appendix, which is not ideal. These definitions are crucial for understanding the theoretical properties of the proposed method and should be included in the main body of the paper. The lack of these definitions in the main text makes it difficult to assess the theoretical soundness of the approach.

2. The developments are disconnected and it is thus not clear what are the key contributions of this work. The paper claims the contribution as a novel interface between conformal prediction and GNN. However, from the present version of the paper, it seems straightforward to combine the two to form conformal prediction on graphs. The consideration of dynamic graphs in this paper is novel but the use of unfolded adjacency has been considered previously for spectral embedding. The paper does not clearly articulate the novelty of combining conformal prediction with GNNs on dynamic graphs. The use of unfolded adjacency, while relevant, is not a novel contribution in itself, as it has been explored in other contexts. The paper needs to better highlight the specific challenges and contributions of this work beyond a simple combination of existing techniques.

3. The scalability with the use of unfolded adj is poor.

### Questions
1. In A2, is label equivariant the same as permutation equivariant?

2. In section 2.1, can you formally prove the exchangebility of UGCN while BD GCN does not satisfy the exchangebiity?

3. Why Algorithm 1 is present in the main paper but Algorithm 2 is used for experiments?

### Soundness
3

### Presentation
3

### Contribution
2
