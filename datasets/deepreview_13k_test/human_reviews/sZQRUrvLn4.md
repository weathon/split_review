# Graph Neural Networks Can (Often) Count Substructures

- Decision: Accept
- Scores: 8, 6, 6, 6, 6

## Abstract
Message passing graph neural networks (GNNs) are known to have limited expressive power in their ability to distinguish some non-isomorphic graphs.
Because of this, it is well known that they are unable to detect or count arbitrary graph substructures (i.e., solving the subgraph isomorphism problem), a task that is of great importance for several types of graph-structured data. 
However, we observe that GNNs are in fact able to count graph patterns quite accurately across several real-world graph datasets.
Motivated by this observation, we provide an analysis of the subgraph-counting capabilities of GNNs beyond the worst case, deriving several sufficient conditions for GNNs to be able to count subgraphs and, more importantly, to be able to sample-efficiently learn to count subgraphs. 
Moreover, we develop novel dynamic programming algorithms for solving the subgraph isomorphism problem on restricted classes of pattern and target graphs, and show that message-passing GNNs can efficiently simulate these dynamic programs. 
Finally, we empirically validate that our sufficient conditions for GNNs to count subgraphs hold on many real-world datasets, providing a theoretically-grounded explanation to our motivating observations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In the submitted manuscript, the authors study the ability of Graph Neural Networks (GNNs) to count substructures. So far a negative result, showing that not all substructures can always be counted by GNNs has been proven. The authors significantly extend our knowledge of this area by proving under what conditions all substructures in a graph can be counted by GNNs. They identify several drawbacks in this general result. They then make use of the fact that subgraph counting is an inherently local task and refine the conditions on the dataset to in turn improve upon their result. Furthermore, two dynamic programs are presented for subgraph counting in trees and graphs without short cycles, and it is shown that GNNs can simulate both these algorithms to successfully count subgraphs. Finally, the authors present empirical properties of real-world datasets, validating the applicability of their theoretical results, and study the predictive performance of a GNN on simulated data.

### Strengths
- The paper is very well-written and clear. 
- The theoretical results are of clear importance to the field and present significant progress.

### Weaknesses
Please find further detail on my listed weaknesses in my questions below.

- A clear area for potential improvement of this work is the empirical analysis. Your results could be more broadly validated empirically. But I appreciate that not all papers need both a substantial theoretical and empirical contribution and the theoretical contribution here is very strong. 

- In parts the writing is a bit dense and difficult to follow. Some examples may help to make the text more accessible. 

- You should state more explicitly what GNN you used in your experiments.

### Questions
1] On several occasions in the empirical analysis you are imprecise on what GNN you use to investigate your hypotheses. I think the clarity of the paper would be improved if you stated more precisely what GNN you used. I am in particular referring the Line 59 and the discussion/caption of Table 1, as well as the experiments in Section 6.2, e.g., Line 479.

2] The paper you presented is one that the reader really has to work through. It is dense and complex. More patient explanation and more frequent examples would make for more pleasant reading. Examples would aid especially in the more advanced concepts in the preliminaries and in Section 5. 

3] In your list of limitations of the result of Proposition 1, it would be appropriate to add that you require an impractically deep GNN, where the number of layers $\ell$ appears to be equal to the maximal number of nodes $n$ in any given graph in the dataset.

4] Your experiments could be improved and extended in a variety of ways.

4.1] In the main paper it is completely unclear how your synthetic dataset is constructed. The appendix also does not add much further detail on this. I believe you must be more precise on how you construct your synthetic dataset. 

4.2] I do not understand why you do not provide empirical results for GNNs counting substructures on real-world datasets. It seems incomplete to me to provide details about the $(\ell,k)$-identifiability of real-world datasets and to then only validate your theory on simulated datasets.

4.3] Since the width, i.e., hidden dimension, of the GNN's readout function and the number of required message passing layers play a role in your theoretical results, it would be nice to complement your theory with an empirical ablation study on the impact of these parameters in practice. 

4.4] It would be better if you referred to the appendices on the empirical aspects of your work, i.e., the ones accompanying Section 6 in the main paper. In general more details on the experimental setting, i.e., more discussion in Appendix A.6, and possibly also the required code to reproduce the experiments would be nice. 

5] Minor comments:

5.1] Since your write-up is of such high quality, I want to suggest a few minor reformulations to aid in perfecting it. Please feel free to reject any of these suggested edits. Line 67: " conditions for which" -> "conditions under which"; Line 233 "such function are" -> "such functions are"; Line 469 "table 3" -> "Table 3"

5.2] In Line 121 I think you may have a typo in the definition of a rooted tree. Specifically, in the following: "$\text{children}(q) = \q$" I think it may be correct to consider "$\mathcal{N}(q)$" here. 

5.3] The algorithm name "$\text{TREE-LIH}_c(u,h)[r]$" is never formally introduced in the text and the argument in angular brackets $r$ is only mentioned in Theorem 4. It may be nicer to introduce this algorithm name and to more consistently and explicitly define the arguments the algorithm takes. 

5.4] The notation in the algorithms are not always defined, e.g., "return $\epsilon$", is never explicitly defined. It may be nicer to add a brief explanation of this. I furthermore noticed that Algorithm 3 is never explicitly mentioned in the text and it would be nicer to draw the reader's attention to it at some point by pointing it out. 

5.5] The model that you define in Appendix A.1 appears to be similar to the GraphSage model [1] to me. Did I miss an important difference? If not then it may be nice to cite their work. 

[1] Hamilton, W., Ying, Z. and Leskovec, J., 2017. Inductive representation learning on large graphs. Advances in neural information processing systems, 30.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors argue that graph neural networks (GNNs) can often count graph patterns across various real-world datasets. They provide conditions under which GNNs can count subgraphs, based on local substructures around nodes. The authors also propose novel dynamic programming algorithms to solve the subgraph isomorphism problem for specific classes of pattern and target graphs and demonstrate that GNNs can efficiently simulate these algorithms.

### Strengths
**Originality**

The paper introduces several original ideas, including conditions under which GNNs can perform subgraph counting on specific class of graphs, dynamic programming algorithms for specific subgraph isomorphism problems, and an analysis of their connections with GNNs.

**Quality**

I have some concerns/questions regarding the quality of the paper (see "weaknesses").

**Clarity**

The paper is not easy to follow, primarily due to issues in presentation. For instance, some of the notations (e.g., Tree-LINc(u,h)[r]) are overly complex, lacking intuitive explanation, and certain concepts (e.g., pattern node, pseudo-dimension, etc.) are not clearly defined. The motivations for studying specific variants of the subgraph counting problem are not well-articulated, making it difficult to understand the significance of these variants within the broader context of the research.


**Significance**

The research area of graph neural networks and subgraph counting explored in this work is significant. However, the paper primarily focuses on WL-distinguishable graphs and tree patterns for its dynamic programming algorithms.  The contributions have a limited impact on the field.

### Weaknesses
(W1) The paper lacks technical depth and rigor.

Proposition 1 is limited to graphs that are distinguishable by the 1-WL test. Since 1-WL can distinguish only certain types of graphs, the results do not apply broadly to general subgraph counting functions. Rather than interpreting that GNNs can count all subgraphs within a class of 1-WL-distinguishable graphs, it would be more natural to explore whether GNNs can count specific classes of subgraphs, such as trees and forests (i.e., graphs with treewidth 1), within general graphs. If the class of graphs is restricted to those distinguishable by 1-WL, the results appear trivial.

The statement, *"It is immediate to see that subgraph counting and induced subgraph counting (i.e., counting the number of (induced) subgraph isomorphisms $\phi$ from $P$ to $G$) are node-decomposable,"* is central to the paper. However, if this is intended as a general statement, I have doubts about its correctness. I was unable to find a proof in either the main paper or the appendix. Since local neighborhood counts can lead to overcounting or miss global structures, they may not yield exact counts for general subgraph counting. Can the authors clarify this statement by formalizing it in the context of subgraph counting and providing either a formal proof or relevant citations? Please explain why this statement holds or does not hold for general subgraph counting.

The proof of Theorem 1 relies solely on node-level functions. However, if graph-level functions were considered, these two graphs could be easily distinguished, as they differ in the number of nodes and edges.

(W2) The significance of this work is unclear and appears to be limited.

Regarding the statement, "We develop novel algorithms solving the (non-induced) graph isomorphism problem on restricted pattern or target graph classes," can you clarify what is meant by the (non-induced) graph isomorphism problem? Generally, graph isomorphism is a different problem from subgraph isomorphism. Moreover, for restricted pattern or target graph classes, such as trees and forests, it is known that the expressivity of MPNN (and 1-WL) is upper bounded by homomorphism counts of forest [2]. Given this, why is there a need to develop dynamic programming algorithms to tackle the locally injective homomorphism problem specifically for tree patterns and to use a GNN model to simulate this? It would be helpful if the authors can explain how their approach differs from or improves upon existing methods for counting homomorphisms in trees and forests, and clarify the specific advantages or novel insights gained from their dynamic programming algorithms and GNN simulations compared to known results about MPNN expressivity.


(W3) Missing related work

The paper [2] specifically discuss how the expressivity of GNNs can be measured in a hierarchy of subgraph counting. 


References:

[1] Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness, Zhang, et al., ICLR 2024

[2] N-WL: A New Hierarchy of Expressivity for Graph Neural Networks, Wang, et al., ICLR 2023

### Questions
See the questions in "Weaknesses".

Below are some additional questions:

(1) The abstract mentions "sample-efficiently learn to count subgraphs." It is unclear what "sample-efficiently learn" means in this context. Can the authors provide a precise definition of "sample-efficiently learn" in this context, including any relevant metrics or benchmarks they use to measure sample efficiency?

(2) In Table 1, which GNN model is used? Appendix A.5 does not specify the GNN architecture. Also, what are the classes, and how is AUROC  calculated for induced subgraph counting in the multi-class classification setting? A statistical description of the datasets (e.g., number of graphs and classes) along with relevant citations would also be helpful.

(3) Regarding "the classical negative result of Chen et al." mentioned in the first paragraph of Section 3, can the authors specify which theorem in their paper this refers to?  In my review of the paper, it appears that Chen et al. just use counterexamples (a pair of graphs that have different induced-subgraph-counts of the pattern but cannot be distinguished from each other by 2-WL) to prove their results. I don't understand the claim "This result, however, requires that the set of graphs at hand features specific WL-indistinguishable graphs, which is unrealistic in practice". Can the authors clarify this claim?

(4) Assigning random colors to nodes in a graph would result in different colors for nodes within the same orbit. Detecting nodes in the same orbit is non-trivial and requires the computation of graph automorphisms. How would the work of color coding address this issue?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the capability of GNNs to detect and count substructures in real-world datasets, despite known theoretical limitations in their expressive power. The authors challenge established assumptions by demonstrating that GNNs can perform subgraph counting tasks with surprising accuracy, even when conventional GNNs struggle to distinguish certain non-isomorphic graphs. The main contributions include deriving conditions under which GNNs can effectively count subgraphs by leveraging local structures, designing dynamic programming algorithms for solving subgraph isomorphism in restricted graph classes that GNNs can simulate, and empirically validating these theoretical findings across various datasets. By introducing the concept of $(l, k)$-identifiability, the paper bridges the gap between theory and practice, providing a framework that explains the unexpectedly robust subgraph-counting abilities of GNNs and highlighting their practical utility beyond theoretical constraints.

### Strengths
1. The paper introduces novel concepts regarding the identifiability of graphs through message passing, which builds on the existing theoretical framework of GNNs. The exploration of $(l, k)$-identifiability offers a fresh perspective on subgraph counting tasks.

2. The writing is generally clear and structured, with a logical progression from theory to application. Key concepts are well-defined, making the paper accessible to a broad audience within the machine learning and graph theory communities.

3. The findings contribute to the ongoing discourse around the capabilities and limitations of GNNs in solving graph-related problems. By demonstrating that GNNs can efficiently solve subgraph counting under specific conditions, the work is likely to influence future research directions in both theoretical and applied settings.

### Weaknesses
1. While the method is shown to work for subgraph counting, there is minimal discussion of its computational complexity, particularly for larger graphs or deeper GNN layers. Insight into time complexity would make the approach more practical.

2. This work mentions WL limitations but does not analyze upper bounds or scenarios where the proposed method may struggle with expressivity. A comparative analysis with existing expressive GNN models would provide a clearer understanding of when this approach is suitable.

3. Adding visual representations of key concepts, such as the identification of $(l, k)$-identifiable nodes could enhance reader understanding and engagement.

4. Missing references: 

[1] C. I. Kanatsoulis and A. Ribeiro, Counting Graph Substructures with Graph Neural Networks, ICLR 2024.

[2] Huang et al. Boosting the Cycle Counting Power of GNNs with I²-GNNs, ICLR 2023.

[3] Raffaele et al. Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational Learning, ICLR 2024 Workshop.

[4] Wang et al. *N*-WL: A New Hierarchy of Expressivity for Graph Neural Networks, ICLR 2023.

Their inclusion could offer a more comprehensive view of how this method stands against similar research in GNN perspective.

### Questions
1. Can the authors provide more specific examples or scenarios where the condition of $(l, k)$-identifiability fails?  This could help clarify the limitations of their proposed framework.

2. How do the authors justify the reliance on WL classes in determining graph indistinguishability? Are there potential edge cases where this might not hold true, particularly in practical applications?

3. The paper mentions that the GNN may require up to $2^{(n-1)}$ message passing layers in the worst case. What are the empirical implications of this for large graphs? Are there any optimizations or heuristics that could be discussed to mitigate this?

4. If feasible, providing access to the code developed would enable others to replicate your experiments and potentially extend your work.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work studies whether and under which conditions graph neural networks (GNNs) can sample-efficiently count substructures. This is motivated by the observation that GNNs can count graph patterns with good accuracy on real-world datasets, despite the known poor subgraph counting ability at worst case. By leveraging the fact that counting patterns is local and node-decomposable, the authors prove that GNNs can perform subgraph counting with number of parameters independent of graph size, under the condition that nodes' ego-nets can be distinguished by WL test.  Furthermore, GNNs are shown to be algorithmically-aligned with a tree counting algorithm that finds locally injective homomorphism. Experiments demonstrate the effectiveness of subgraph counting on real-world molecular graphs.

### Strengths
1. A theoratical justification of subgraph counting power beyond worst case is provided.
2. Sample efficiency: the number of parameters is shown to be bounded, and an alignment to a subtree counting algorithm is also demonstrated. These provides clues for possible good generalization of GNNs for subgraph counting.
3. The paper is well-structured and easy to follow.

### Weaknesses
1. In Table 1, only results of four graph patterns are shown. It makes the evaluation stronger if more results of common substructures can be provided, or an explanation of why the current chosen ones are important to consider. For example, 5-cycle is also a common substructure in molecules.  
2. The algorithm alignment is largely restricted to tree patterns, which is less interesting especially for molecular graphs.

### Questions
1. Though Table 3 shows the high identifiable ratio of Mutagenicity dataset, I wonder why the counting performance (MAE) is poor  in Table 1.
2. To let the subgraph counting algorithm 1 work, it requires the graph to have some inherent node colors to satisfy parent-colorful. Does that mean the algorithm (and thus GNNs) cannot perform such counting if the graph has no node attributes?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a solid theoretical framework on GNNs ability in subgraph counting, bridging the gap between their theoretical limitations and real-world performance. One of the key contributions is the identification of specific conditions under which GNNs can efficiently compute functions on graphs based solely on local substructures around the nodes. Additionally, the authors introduce a novel dynamic programming algorithm for problems related to subgraph isomorphism, showing that GNNs can effectively simulate this approach. They also back up their claims with experimental results, which adds to the paper's credibility.

Overall, I found the paper to be quite interesting. However, my current rating is a 5. I would be willing to raise my score if the authors address the weaknesses I’ve pointed out.

### Strengths
The paper is well-written and effectively motivates the problem it tackles. The authors provide a solid background that helps readers understand the context and importance of their work. Additionally, the authors use various synthetic and empirical datasets to strengthen their analysis and showcase the practical relevance.

### Weaknesses
Here are some weaknesses I noticed in the paper that I would like the authors to address:

- The authors did not reference important works in the field, such as "Counting Graph Substructures with Graph Neural Networks" by Kanatsoulis and Ribeiro, and "Improving Graph Neural Network Expressivity via Subgraph Isomorphism Counting" by Bouritsas et al. A more thorough literature review is needed.

- Additionally, the paper lacks comparisons with other methods and does not discuss how existing methods could be adapted for their task. 

- Finally, the absence of code limits the reproducibility of their results. I appreciate the provided pseudocode, as it makes the paper easier to follow.

### Questions
I refer the authors to the weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
