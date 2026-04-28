# Topological Positional Encoding

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5, 1, 5, 5

## Abstract
Unlike words in sentences, nodes in general graphs do not have canonical positional information. As a result, the local message-passing framework of popular graph neural networks (GNNs) fails to leverage possibly relevant global structures for the task at hand. In this context, positional encoding methods emerge as an efficient approach to enrich the representational power of GNNs, helping them break node symmetries in input graphs. Similarly, multiscale topological descriptors based on persistent homology have also been integrated into GNNs to boost their expressivity. However, it remains unclear how positional encoding interplays with PH-based topological features and whether we can align the two to improve expressivity further. We address this issue with a novel notion of topological positional encoding (ToPE) that amalgamates the strengths of persistence homology and positional encoding. We establish that ToPE has provable expressivity benefits. Strong empirical assessments further underscore the effectiveness of the proposed method on several graph and language processing applications, including molecular property prediction, out-of-distribution generalization, and synthetic tree tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes to integrate persistent homology (PH), combined with positional encodings, into GNNs to boost expressivity. Specifically, topological positional encoding (ToPE) is proposed, which uses PEs to induce graph filtration and the obtained PH's embeddings are concat with base PEs and fed into GNNs.

### Strengths
1. The method is straightforward.
2. The manuscript is easy to follow.

### Weaknesses
1. Related work is not contextualized enough, making the original contributions of this work not well presented. What are the key contributions of this work compared with previous work? It remains unclear to me what is the key innovation of ToPE compared with VC and RePHINE. Specifically, the manuscript does not clearly articulate how the proposed method differs fundamentally from existing approaches that also leverage topological information. The use of positional encodings to induce a filtration, while novel, needs to be more clearly positioned within the existing landscape of topological data analysis on graphs. The distinction between using initial positional encodings versus layer-wise GNN embeddings to construct filtrations is not adequately emphasized, leaving the reader to wonder about the specific advantages of the proposed approach.
2. It is good to contain some theoretical analysis, but it may not be a core contribution of this work as they are somewhat shallow and artificial. The theoretical analysis, while present, lacks depth and does not provide a strong justification for the proposed method. The claims of increased expressivity are not rigorously proven and rely on somewhat contrived examples. The analysis does not sufficiently explore the limitations of the method or the conditions under which it might fail. The connection to k-FWL is interesting but feels tacked on and does not provide a deeper understanding of the method's capabilities.
3. The proposed way of combining PEs and PH seems arbitrary and with limited technical novelty, making it sound more like an engineering trick instead of a novel and principled method. The concatenation of positional encodings and persistent homology embeddings, while straightforward, lacks a clear theoretical motivation. The method appears to be an ad-hoc combination of existing techniques, without a strong rationale for why this particular combination should be effective. The lack of a principled approach makes it difficult to generalize the method or to understand its limitations.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
ToPE computes positional encodings by learning them through Laplacian eigenvectors. The key difference is that ToPE employs persistent homology strategies, which are decoupled from the input graph and its features, and subsequently concatenates these encodings to the learned GNN representations.

### Strengths
- The experimental results are strong, with ToPE outperforming existing methods on most tasks.
- The paper is generally well-written.

### Weaknesses
 - The novelty of the approach is unclear.
- The comparison to related work is not well articulated.
- The advantages of ToPE over REPHINE and other PH-based methods are not clearly demonstrated/explained.
- Proposition 1 is trivial, and the other results do not contribute significant new insights because 
a) They do not analyze the actual final GNN, and
b) The proofs are overly straightforward.

### Questions
- What is the novelty wrt to related work such as rephine? Is it just using Laplacian eigenvectors as input instead of the initial node features?
- While you analyze the stability and expressivity, can you also compare it with other methods? E.g., is it "more stable" than SPE? Is it more expressive than rephine when using the corresponding topological descriptor, i.e., using rephine diagrams?


---
## Additional Comments
I believe the paper isn't ready for publication, yet. I would recommend embedding it better into the literature, pointing out the novelties, compared to other works. In particular, the authors should point out the tasks on which they suggest using Tope and when they expect it to perform better/worse than other methods.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this article, the authors present a method to add some additional features, called Topological Positional Embeddings (ToPE), to vertices during GNN's update rule. The authors present their method, prove some properties of ToPE, and present extensive numerical experiments.

### Strengths
- The paper clearly exposes the contributions.

- Comparing the expressivity of different positional embeddings is relevant.

- The article has extensive experiments that could guide practitioners if they wish to implement topological positional encodings for GNNs.

### Weaknesses
I have two major concerns about the theoretical contributions. I am not sure this part of the article is very insightful from that standpoint. As a consequence, I am not entirely sure the methodological contribution is significant. My concern may be dissipated depending on the author's answers to my questions below.

- The authors indeed show that ToPE has more expressive power than Laplacian PEs (individually); but it isn't clear that within aggregate-combine GNNs, the first is more expressive than the second (stricly). In other words, it could be true for any GNN with ToPE, there is a Laplacian PE GNN that can distinguish any pair of graphs that the TopE distinguishes. Can the authors elaborate on why persistent homology provides GNNs more expressivity than Laplacian PE?

- In Definition 1 of the Stable PE, the constant L_{\psi} depends on the graph given the order of the quantifiers. This constant could get very large, a priori, even if the graphs are close, and lead to unstability. The authors probably want to change the order of the statement. If not, could the authors elaborate on this observation / issue?

- The statement of Proposition 3 is confusing. Does the existential result apply to the hash function? Can the authors reformulate this statement in order to make the role of the Hash function clearer?

### Questions
- The authors indeed show that ToPE has more expressive power than Laplacian PEs (individually); but it isn't clear that within aggregate-combine GNNs, the first is more expressive than the second (stricly). In other words, it could be true for any GNN with ToPE, there is a Laplacian PE GNN that can distinguish any pair of graphs that the TopE distinguishes. Can the authors elaborate on why persistent homology provides GNNs more expressivity than Laplacian PE? 

- In Definition 1 of the Stable PE, the constant L_{\psi} depends on the graph given the order of the quantifiers. This constant could get very large, a priori, even if the graphs are close, and lead to unstability. The authors probably want to change the order of the statement. If not, could the authors elaborate on this observation / issue?

- The statement of Proposition 3 is confusing. Does the existential result apply to the hash function? Can the authors reformulate this statement in order to make the role of the Hash function clearer?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
The paper proposes to employ a Topological Positional Encoding (ToPE) during the message passing of a GNN. In practice, during the message passing, three vectors are attached to each node at each layer: the first is the node embedding, the second represents the positional encoding, and the third one is the topological embeddings based on persistent Homology (PH). 

The node embeddings are updated by concatenating all three vectors for each node and by applying the common update function of a GNN.

The positional encodings are updated by applying the update function of a GNN (as in standard methods that employ positional encoding).

The topological embeddings are computed by applying graph filtrations on positional encodings.

The proposed schema is analysed both theoretically and practically on different chemical datasets and one synthetic tree task.

### Strengths
The paper is well written and easy to follow.
Also, the idea of introducing topological aware positional encoding for graphs is interesting.

### Weaknesses
## Limited contribution
In my opinion, the only contribution of the paper is the computation of topological embeddings starting from positional encodings instead of node embeddings. The propagation of positional encodings and the computation of topological embeddings is not new. The contribution would be enough if the paper was able to convince why (analytically and practically) this could lead to better results.

## Meaning of theoretical results

It was not clear to me the purposes of the theoretical analysis of the paper. Proposition 1 shows the stability of the proposed method but it is not clear why we need this property. Lemma 1, Proposition 2 and Proposition 3 show the expressiveness of the proposal. In particular, it shows that ToPE is more expressive than standard PE. From my understanding, this is due to the employment of persistent homology features whose expressiveness has been already proven. I believe that the most interesting thing is to prove that the proposed method (i.e. combining positional and topological embeddings) is better than employing only a PH-based method (e.g RePHINE). However, there is not proof in this sense.

## Experimental Results and Reproducibility Issues

The experiments are limited since they have been conducted only on graph molecules and a synthetic tree manipulations. The abstract claims “on several graph and language processing applications, including molecular property prediction, out-of-distribution generalization, and synthetic tree tasks.” which is an overstatement.
Also, the results show only marginal improvements. If we consider the variance of the results, the difference might be non-statistically significant. As a side note, the tables with the results are a little bit confusing for me since the name of the proposed method (ToPE) never appears.

There is no baseline without positional encodings (e.g. RePHINE) to verify if the proposed method is more effective than these types of approaches.

Finally, there is no mention of “model selection” in the paper. To ensure reproducibility, it is not enough to publish the best hyperparameters set. Instead, it is necessary to publish the whole experimental procedure (i.e. the method for the model selection, the split used, the hyper-parameters grid, etc…) together with the code. Thus, I couldn't verify how the experiments have been conducted.

### Questions
I do not have specific questions more than the doubts expressed in the above section.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Topological Positional Encoding (ToPE), a new technique that combines persistent homology (PH) with existing positional encoding strategies to augment the capabilities of Graph Neural Networks (GNNs). ToPE theoretically improved expressive power compared to Laplacian positional encoding and shows strong generalization capabilities.

### Strengths
-I have found the theory well written and self-contained. I think a non-expert could find most of the information in the paper, and I appreciate this aspect.

-The insights are didactical and well communicated. The conclusion given by the experiments looks interesting and valuable for future practitioners, while I think a synthesis would be beneficial for the reader.

### Weaknesses
Despite these merits, I have the following concerns about the paper.

1- While there is a careful analysis of the different design decisions/performance tradeoffs, I feel that there is only a limited understanding about what are the properties of the Architecture that lead to these decisions/performance differences. Specifically, the paper lacks a detailed analysis of how the choice of different topological descriptors (e.g., vertex-color filtrations vs. RePHINE) impacts the learned representations and downstream performance. It's unclear why certain descriptors perform better than others, and a more in-depth investigation into the feature space induced by these descriptors is needed.

2-  The paper does not include an analysis of the hyperparameters for the proposed approach, even though previous work, such as 'Where Did the Gap Go? [Tönshoff 2023],' has demonstrated that these hyperparameters can significantly influence the performance of transformer architectures. I recommend that the authors conduct such an analysis to better understand the behavior and performance implications of their architecture. This is particularly important given the introduction of topological features, which may introduce new sensitivities to hyperparameter tuning. For example, the dimension of the topological features, the number of persistence intervals considered, and the specific method used to encode the persistence diagrams could all be sensitive to hyperparameter choices, and these should be explored in detail.

3- The paper does not sufficiently address the computational cost associated with persistent homology computations, which is known to be substantial. This oversight could limit the practical applicability of the Topological Positional Encoding (ToPE) method, especially in scenarios where computational resources are constrained. Additionally, the paper falls short in comparing ToPE with a wide range of baseline methods, which could have provided a more comprehensive evaluation of its performance and effectiveness relative to existing solutions. While the paper compares against some positional encodings, it does not include comparisons against other methods that incorporate structural information, such as those based on graph kernels or other topological methods.

### Questions
- Are there specific theoretical or computational challenges you foresee in expanding the applicability of ToPE to capture more complex topological features in such structures?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors proposes Topological Positional Encodings (ToPE), which leverages persistence diagram of filtrations constructed by Laplacian positional encodings. They show the superior expressive power of ToPE over vanilla Laplacian positional encodings as well as a connection to k-FWL test.  Experiments on molecular graphs and synthetic tree tasks show promising performance of ToPE.

### Strengths
1. a novel positional encodings that encodes topological features using learnable persistence diagrams
2. the paper is easy to follow and well-structured

### Weaknesses
One thing is unclear to me is the motivation to build filtraction upon positional encodings rather than other node features. What is the key role of positional encodings here and is there any intuition behind? For example, if we suppose the positional encodings here only serve for a better distinguishability of nodes, then what if we define filtraction on node features based on high-order GNNs and even random node features. Will it lead to a even much more expressive model?

Given that persistence diagrams are discrete function of graph filtrations, how are we supposed to train it using gradient descent?

### Questions
Given that persistence diagrams are discrete function of graph filtrations, how are we supposed to train it using gradient descent?

### Soundness
2

### Presentation
2

### Contribution
2
