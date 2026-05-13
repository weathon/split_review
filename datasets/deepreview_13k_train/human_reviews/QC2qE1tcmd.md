# Demystifying Topological Message-Passing with Relational Structures: A Case Study on Oversquashing in Simplicial Message-Passing

- Decision: Accept
- Scores: 8, 8, 6, 6, 6

## Abstract
Topological deep learning (TDL) has emerged as a powerful tool for modeling higher-order interactions in relational data. However, phenomena such as oversquashing in topological message-passing remain understudied and lack theoretical analysis. We propose a unifying axiomatic framework that bridges graph and topological message-passing by viewing simplicial and cellular complexes and their message-passing schemes through the lens of relational structures. This approach extends graph-theoretic results and algorithms to higher-order structures, facilitating the analysis and mitigation of oversquashing in topological message-passing networks. Through theoretical analysis and empirical studies on simplicial networks, we demonstrate the potential of this framework to advance TDL.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a generalisation of theoretical results on oversquashing in graph learning to topological deep learning by formulating these within the framework of relational structures. This framework more generally presents an interesting approach for extending theoretical results from graphs to higher order structures.

### Strengths
- The paper is well written and easy to follow. 
- Relational structures seem to provide a general unified framework that includes not only simplicial message passing but also other higher order structures. 
- Propositions and theorem are well defined and proofs are mathematically sound.

### Weaknesses
 - The experimental settings where the combination of lifting and rewiring leads to performance improvements seems to be limited.



### Questions
- Is there a correspondence between the message passing graph introduced  by Bodnar et al. and the aggregated influence matrix introduced in Eq.6? 
- The rewiring algorithms considered in the paper are limited to the addition of edges however sometimes lifting graphs to clique complexes can introduce redundancies therefore could maybe rewiring algorithms that also prune edges be a better fit this context? 
- The rewiring algorithms considered in the paper are limited to binary edges however in general rewiring algorithms that also include the modification of higher order edges might further improve performance. Do the results presented in the paper provide insights into how one could proceed to formulate such higher order rewiring algorithms?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors make three main contributions.

First, they propose a general message-passing scheme for relational structures and show that it generalizes R-GCNs, simplicial neural nets, and higher-order GNNs. This interesting connection will hopefully prevent different communities with different terminologies from working in parallel on the same type of problems. 

In Definition 2.6, you should make sure all variables are properly introduced. For instance, $p_t$ is the size of the feature representation of the \sigma s at time t. This size variable does not occur in the previous simplicial message-passing scheme. Making the terminology consistent or at least introducing each with a sentence will help readers to more easily understand the terminology. 

This approach of reformulating higher-order structures as relational structures allows insights about over-squashing from graph neural networks (GNNs) to be translated to a broader class of relational message-passing systems. Introducing the aggregated influence matrix and influence graph as core tools makes it possible to study how factors like local geometry, network depth, and hidden dimension size impact message passing in these systems, much like in traditional GNNs.

Finally, the authors use the proposed framework and connection to generalize rewiring methods from prior work to the relational setting. Here, it would be interesting to understand better how computationally complex the rewiring techniques are regarding the number of relations, their arity, and elements in S. This would make the trade-off between these heuristics and the gains in the experiments more explicit. 

The paper makes important theoretical contributions. Most notably, I appreciate the connection between relational GNNs and topological GNNs. Bridging one or more communities that are thinking about similar problems and making them aware of each other is important. The paper is generally well-written and easy to follow. As mentioned above, there is some minor room for improvement in the definition of the terminology. Some more explanations in natural language when defining terminology could make it a bit easier for the reader. 
The main weaknesses of the paper are the “real-world” datasets used in the experiments and the missing discussion of the complexity–accuracy trade-off by omitting a discussion of the computational complexity of the rewiring techniques. This should be an easy fix for the latter by adding another section to the appendix and referring to it in the main paper. Regarding the former, I believe no graph ML method should only be evaluated with the TUD dataset. This provides very limited empirical evidence for a method. Several other datasets (e.g., those about atomistic structures such as QM9, MD17, the peptides datasets, and many more) could have been used. The method could have also been tested on node and link prediction problems, which is the main area of use for relational GNNs. All of these datasets and evaluation setups have shortcomings, of course, but a broader set of problems would make the empirical results much more convincing. This is a very strong theoretical paper with weak empirical evidence that the proposed method is helpful in practice and worth the overhead.

### Strengths
- Strong theoretical contribution, establishing connections between different classes of GNNs.
- Theoretical machinery for understanding over squashing and other phenomena in relational and topological GNNs
- New rewiring heuristics for relational and topological GNNs

### Weaknesses
The paper makes important theoretical contributions. Most notably, I appreciate the connection between relational GNNs and topological GNNs. Bridging one or more communities that are thinking about similar problems and making them aware of each other is important. The paper is generally well-written and easy to follow. As mentioned above, there is some minor room for improvement in the definition of the terminology. Some more explanations in natural language when defining terminology could make it a bit easier for the reader.
The main weaknesses of the paper are the “real-world” datasets used in the experiments and the missing discussion of the complexity–accuracy trade-off by omitting a discussion of the computational complexity of the rewiring techniques. This should be an easy fix for the latter by adding another section to the appendix and referring to it in the main paper. Regarding the former, I believe no graph ML method should only be evaluated with the TUD dataset. This provides very limited empirical evidence for a method. Several other datasets (e.g., those about atomistic structures such as QM9, MD17, the peptides datasets, and many more) could have been used. The method could have also been tested on node and link prediction problems, which is the main area of use for relational GNNs. All of these datasets and evaluation setups have shortcomings, of course, but a broader set of problems would make the empirical results much more convincing. This is a very strong theoretical paper with weak empirical evidence that the proposed method is helpful in practice and worth the overhead.

### Questions
- Why did you not run experiments on realistic datasets beyond TUD?
- Why did you not consider entity (node) and link prediction experiments, which are typically the main targets of relational GNNs

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
4

### Summary
This paper provides both theoretical and experimental insights into oversquashing within Topological Deep Learning (TDL), a research direction recently highlighted as important for the TDL community in a recent position paper [1]. The authors encode topological structures, specifically simplicial complexes, as relational structures, allowing these to be transformed into weighted graphs via shift operators. Using this framework, they extend existing work on graph oversquashing and adapt popular rewiring algorithms to topological domains. The paper then presents experimental evidence supporting the theoretical findings and evaluates the combined performance of rewiring and TDL methods on TUD graph benchmarks.

[1] Theodore Papamarkou, Tolga Birdal, Michael M Bronstein, Gunnar E Carlsson, Justin Curry, Yue Gao, Mustafa Hajij, Roland Kwitt, Pietro Lio, Paolo Di Lorenzo, et al. Position: Topological deep learning is the new frontier for relational learning. In Forty-first International Conference on Machine Learning, 2024.

### Strengths
1. The paper successfully extends key results on graph oversquashing to topological domains, providing a comprehensive theoretical foundation for this adaptation.

2. The paper tackles questions that have been of interest to the TDL community, as highlighted in the recent position paper [1].

[1] Theodore Papamarkou, Tolga Birdal, Michael M Bronstein, Gunnar E Carlsson, Justin Curry, Yue Gao, Mustafa Hajij, Roland Kwitt, Pietro Lio, Paolo Di Lorenzo, et al. Position: Topological deep learning is the new frontier for relational learning. In Forty-first International Conference on Machine Learning, 2024.

### Weaknesses
1. The novelty of the paper is somewhat limited. It reduces simplicial complexes to an "influence graph" and then re-derives several previously established results on graph oversquashing. The observation that simplicial complexes can be encoded as graphs has been explored in prior work e.g. [1,2,4], and many of the paper’s results on oversquashing closely mirror existing studies.

2.  An important question regarding oversquashing and TDL is understanding the effects of oversquashing in topological domains compared to standard graphs. Specifically, it remains unclear whether lifting graphs to higher-order domains could mitigate some effects of oversquashing. The paper does not address this question theoretically, and its empirical analysis only begins to explore this comparison. Instead, it primarily focuses on extending existing results on graph oversquashing to TDL, leaving a key question raised in the position paper [3] only partially addressed.

3. A minor critique is that the paper quickly reduces simplicial message passing to a relational setting, which is more combinatorial than topological. It would be interesting to see an analysis of oversquashing that leverages properties of the underlying topology of the simplicial complexes, such as topological curvature.

4. The experimental section has several issues: First, the real-world benchmarks are limited to TUD datasets, which are somewhat outdated, with a small number of samples and problematic evaluation. It would strengthen the results to include newer benchmarks, such as the Zinc and OGB datasets. These datasets were also used in the papers introducing  CIN and CIN++ which are baselines used in this paper. Additionally, since recent TDL models such as CIN and CIN++ use cyclic lifting rather than clique lifting, it would have been beneficial to include cyclic lifting across all experiments. Lastly, the effects of rewiring on real-world datasets appear inconclusive, making it difficult to determine when rewiring should be applied with TDL models.

### Questions
Is there significance in using multiple relations rather than a single one, other then for clarity? Could tighter bounds,  e.g. in equation (8)  be achieved by considering matrices  $B^{R_i}$ rather then a single $B$? Conversely, is it possible to combine all relations into a single “union relation”?

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
This paper addresses a well-known issue in Graph Neural Networks known as over-squashing. It introduces a framework called the Relational Message Passing Model, which unifies various higher-order message-passing approaches. This unification is leveraged to theoretically examine over-squashing within the context of higher-order message-passing.

### Strengths
This paper addresses a critical gap in the literature on over-squashing. Over-squashing remains underexplored in the context of higher-order message-passing architectures like simplicial neural networks and CW networks. This paper takes an essential first step toward addressing this gap within Topological Deep Learning. By presenting a unifying, axiomatic framework, a relational perspective on simplicial and cellular complexes is provided. This unified approach facilitates the analysis of over-squashing in topological message-passing networks.

### Weaknesses
The paper appears to be a relatively straightforward extension of Topping et al. (2022). This impression arises primarily from Definition 2.6, which is positioned as the core contribution. This definition raises several concerns:

1. The substitution of $R_i$ with $\mathcal{S}^{n_i}$ seems to have minimal impact on the overall definition, effectively diminishing the role of relations $R_i$ within the definition. The definition seems to treat all possible $n_i$-tuples as potentially related, rather than focusing on the specific relations defined by $R_i$. This lack of specificity undermines the purpose of introducing relations in the first place. For example, if $R_i$ represents a specific type of adjacency in a simplicial complex, the definition should reflect this constraint rather than considering all possible combinations of simplices.

2. The shift operator $A^{R_i}$, associated with relation $R_i$, quantifies the signal passed from $(\xi_1, \cdots, \xi_{n_i-1})$ to $\sigma$ when $(\sigma, \xi_1, \cdots, \xi_{n_i-1}) \in R_i$. However, it does not account for the signal passed from $(\sigma, \xi_2, \cdots, \xi_{n_i-1})$ to $\xi_1$, or any other permutations of the tuple. Consequently, $A^{R_i}$ may not serve as an adequate representation of $R_i$. This is a critical flaw because the relational structure should capture the bidirectional or multi-directional nature of interactions, not just a single direction. The current definition limits the expressiveness of the model by not fully utilizing the information encoded in $R_i$.

3. The update rule and message functions $m^{(t)}_{\sigma,i}$ can be viewed as updated versions of the update rule and message function that appear in Equation 1 from Topping et al. (2022), adapted for dimensions $k$ and $n_i$. These functions exhibit a behavior similar to the update rule and message functions in Equation 1 from Topping et al. (2022) when computing the Jacobian in Lemma 3.2. Consequently, this lemma appears to be a straightforward extension of Lemma 1 from Topping et al., lacking significant innovation or depth. The core mechanism of message aggregation and update remains fundamentally similar, suggesting a lack of substantial theoretical advancement beyond the existing framework. The adaptation to higher dimensions appears to be a direct application of existing techniques rather than a novel contribution.

### Questions
Please refer to the weaknesses.

Suggestion:

It is observed in line 167 that certain projections exist from $ R_4(\sigma) $ to $ R_2(\sigma) $ and from $R_2(\sigma) $ to $ R_1(\sigma) $ (similarly, from $ R_5(\sigma) $ to $ R_3(\sigma) $ and from $ R_3(\sigma) $ to $R_1(\sigma) $). The relational structure could be further enriched by treating the set of relations as a directed set. Considering the direct limit of this directed set may provide a comprehensive summary of all the relations within the given relational structure. This could serve as a terminal object for defining message functions, potentially enhancing the model’s representational capacity.

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
4

### Summary
This paper proposes a unified axiomatic framework, aiming at the over-squashing phenomenon and the lack of theoretical analysis in graph topological message passing. The framework examines simplicial complexes and their message-passing schemes from the perspective of relational structures, closely combines graphs and topological message passing, and extends them to high-order structures, enhancing the theoretical analysis ability and effectively alleviating the over-squeezing problem.

### Strengths
1. The message-passing theory of simple complexes and their relational structures is comprehensively and intensely studied, and a detailed explanation and rigorous proof are provided.

2. The article has a clear structure and a smooth and natural expression, which is easy for readers to understand and grasp.

### Weaknesses
1. The literature review on relational graph neural networks mainly focuses on research in 2020 and before, which limits the comprehensive grasp of the latest progress in this field. It is necessary to include more recent research results to enhance the timeliness and persuasiveness of the review. Specifically, the review lacks discussion of recent advancements in handling heterogeneous graphs and dynamic relational structures, which are crucial for a complete understanding of the field.

2. Although the comparison method includes a baseline for 2024, more is needed in terms of SOTA (state-of-the-art) comparison in the past two years to ensure the comprehensiveness and superiority of the evaluation. The current evaluation lacks a detailed comparison against recent models that explicitly address over-squashing, such as those using spectral techniques or adaptive message passing strategies. This limits the ability to contextualize the performance of the proposed framework.

3. Given that this study aims to explore the over-squeezing problem, unfortunately, the paper fails to show the results of the application of this method in deeper models, thus failing to verify and strengthen the conclusions obtained in a more in-depth manner. The lack limits the comprehensiveness and persuasiveness of the study. Specifically, the paper should include experiments with varying numbers of message-passing layers to demonstrate the method's effectiveness in mitigating over-squashing as depth increases.

4. Although the paper mentions the impact of local complexity, model depth, and hidden dimension on performance, unfortunately, it fails to provide corresponding ablation experiments to verify the impact and effectiveness of these factors from an experimental level, which to some extent weakens the experimental support for the conclusions. For instance, the paper should include ablation studies that systematically vary the hidden dimension size and analyze its impact on performance and over-squashing behavior.

5. Many of the formulas in the paper are not original, so it is recommended that the author provide corresponding references for these equations. This lack of attribution makes it difficult to trace the origins of the mathematical formulations and understand their context within the broader literature.

6. Why does the article take up so much space on the simplicial complex and its influence on over-squashing? Although this part is also essential, its level of detail exceeds the description of the solution part far, giving people a slightly unbalanced impression. The content distribution can be appropriately adjusted to make the solution part more detailed to ensure the focus is highlighted. The paper should provide a more detailed explanation of how the proposed framework directly addresses over-squashing, rather than focusing primarily on the theoretical background of simplicial complexes.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
