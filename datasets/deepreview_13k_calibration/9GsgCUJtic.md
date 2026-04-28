# When do GFlowNets learn the right distribution?

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
Generative Flow Networks (GFlowNets) are an emerging class of sampling methods for distributions over discrete and compositional objects, e.g., graphs. In spite of their remarkable success in problems such as drug discovery and phylogenetic inference, the question of when and whether GFlowNets learn to sample from the target distribution remains underexplored. To tackle this issue, we first assess the extent to which a violation of the detailed balance of the underlying flow network might hamper the correctness of GFlowNet's sampling distribution. In particular, we demonstrate that the impact of an imbalanced edge on the model's accuracy is influenced by the total amount of flow passing through it and, as a consequence, is unevenly distributed across the network. We also argue that, depending on the parameterization, imbalance may be inevitable. In this regard, we consider the problem of sampling from distributions over graphs with GFlowNets parameterized by graph neural networks (GNNs) and show that the representation limits of GNNs delineate which distributions these GFlowNets can approximate. Lastly, we address these limitations by proposing a theoretically sound and computationally tractable metric for assessing GFlowNets, experimentally showing it is a better proxy for correctness than popular evaluation protocols.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper provides a detailed analysis of Generative Flow Networks (GFlowNets) to understand when and whether they accurately learn target distributions. The authors extend the DB loss by non-uniformly weighting the transition-wise terms to account for this heterogeneity. For graph-structured generation tasks, they introduce LA-GFlowNets to boost the expressive power of GNN-based GFlowNets by incorporating the embeddings of the children of a state into the policy network. The paper also introduces Flow Consistency in Subgraphs (FCS), a new metric for assessing GFlowNet performance, arguing that it provides a more reliable measure than popular protocols.

### Strengths
1. The question is well-defined. The authors start with analysis and findings, and then propose their method and new evaluation metrics. 
2. As for the paper presentation, key contributions are well-articulated, with a clear breakdown of findings and their implications for GFlowNets.
3.. This paper proposes a new metric FCS, which has the potential to standardize GFlowNet evaluation, addressing a critical gap in current methodologies. And the paper provides a detailed comparison of FCS with traditional evaluation metrics.
4. The paper includes theoretical formulation and proofs as well as empirical results to validate their findings.

### Weaknesses
1. The legends, captions and ticks in figures are too small, which is not very readable for readers.
2. Some expressions are not well-written or formal. e.g. 'Figure 7 and Table 2 teach us three facts.'
3. Some figures lack legends (e.g. Figure 5). Though the authors use different colors in captions to distinguish, it's may still lead to confusion.
4. The weighted detailed balance (WDB) loss design (e.g. the choice of $\gamma$ ) appears heuristic without detailed discussion on optimizing these weights or examining the variance across tasks, which needs more detailed explanation.
5. The experiments predominantly focus on controlled scenarios, limiting insight into real-world application suitability.

### Questions
1. Could the authors elaborate on the choice of the $\gamma$ for the WDB loss? Are there alternative weighting functions that could improve performance in specific applications?
2. As for other applications such as NLP and molecule generation, could the authors provide more insights on whether FCS metric can be generalizable?

### Soundness
3

### Presentation
2

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
Generative Flow Networks (GFlowNets) are a recent class of deep generative models suitable for representing probability distributions over discrete and compositional data structures. The paper asks a temporary and practically important question, which, to the best of my knowledge, has not been answered until now: Do GFlowNets correctly learn the target distribution? The paper answers this question in three parts.

The first part investigates how a small perturbation of the detailed balance condition affects the total variation (TV) distance between the sampling and target distributions. The authors manifest their analysis by the average of the summands in the detailed balance loss for different depths of the state transitions. Nicely, this theoretical and empirical finding is then put to practical use by designing a weighted detailed balance loss, which assigns the state transitions with different weights. Consequently, the authors achieve better (or on par) performance than other state-of-the-art training objectives.

The second part focuses on the parameterization of GFlowNets as the cause of violating the detailed balance. The authors select the popular domain where the target distribution is a distribution over graphs, where the parameterization of GFlowNets is thus instantiated with graph neural networks, and are concerned with the standard questions about the one-hop Weisfeiler-Leman (WL) test and its impact on the representational power of GFlowNets. The authors show that a 1-WL GFlowNet can approximate any target distribution over trees but not graphs with two 1-WL indistinguishable nodes. This analysis leads to the design of the look-ahead GFlowNets, which offer more representational power than the 1-WL GFlowNet. This synthesis is again confirmed by experimental evidence.

The third part is concerned with assessing the goodness-of-fit of GFlowNets in cases where the learned distribution is intractable. The authors propose Flow Consistency in Subgraphs (FCS) as the expected total variation distance between $\beta$-sized restrictions of the marginal distribution of the forward policy and the reward function. Moreover, the authors discuss the equivalence between FCS and TV distance and provide PAC statistical guarantees. The empirical results demonstrate that the FCS metric is a computationally efficient and close approximation of the TV distance.

### Strengths
The paper is very dense and comprehensive.

Most of the theoretical findings are nicely supported by experimental evidence.

The writing is excellent. Although some parts would deserve minor improvements (more on that below).

### Weaknesses
Minor:

The writing is excellent, as mentioned above. The whole paper works extensively with the sampling distribution and the target distribution. However, these need to be adequately defined. I would expect to see a more precise statement of these two distributions, e.g., in the first paragraph of Section 2. For instance, in line 143, the authors start using ``*GFlowNets sampling distribution*'' without showing the symbol for it. Right after that, the authors say that their target is $R$, and then, only in line 185, we see that $\pi\propto R$. The first mention that $\pi$ is the target is in line 202. The first appearance of `$\pi$ is defined to be equal to ...' can be seen in line 398.

Line 120:  ``*Finally, a flow is a function ...*'' It should be a function $\mathcal{T}\rightarrow\mathbb{R}_{+}$, where $\mathcal{T}\subset\mathcal{S}$ is a set of complete trajectories (Definition 7 in Bengio et al. 2023).

Line 123: *``a SG''* -> *``an SG''*

Line 127: *``an uniform''* -> *``a uniform''*

Line 200: Which tasks in Section 2 do the authors have in mind? Do the authors mean those mentioned in the last paragraph of Section 3? The authors first refer to Figure 2 in Section 3.1, but the four tasks are first introduced in Section 3.2. The sequence of ideas can be improved.

Figure 4: *``state graph''* -> *``state graphs''* It would be more readable to separate the two state graphs. Their blending is confusing.

*``i.d.d.''* is inconsistent with *``wrt''* throughout the text.

Lines 458 and 462: *``a FL-''* -> *``an FL-''*

Line 459: *``part''* -> *``a part''*

### Questions
Line 370: ``*For most benchmark tasks, e.g., hypergrid environment (Malkin et al., 2023), set generation (Shen et al., 2023), and sequence design (Jain et al., 2022), we can exactly and efficiently compute $p_T$.*'' Please clarify if the statement about efficiently computing $p_T$ for benchmark tasks means you can compute arbitrary marginal distributions of $p_T$ over subsets of $x$. If so, could you provide more details on how this is done efficiently?

For Figure 2, please clarify if the results are averaged over multiple runs. If so, specify how many runs were performed and what aspects (e.g., initialization) varied between runs.

Could it be possible to show an equivalent of Figure 2 for Avg. $\mathcal{L}^{\gamma}_{\text{WDB}}$ to see a comparison to the standard DB loss? This could help illustrate the impact of the weighting scheme on different transitions.

What is the shaded area for each curve in Figure 3? Is it the standard deviation or the interquartile range? How was it computed?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper investigates the theoretical foundations of Generative Flow Networks for distributions over discrete and compositional objects. The paper evaluates the impact of violations in the detailed balance of the underlying flow network on the correctness of GFlowNet's sampling distribution. They demonstrate that the effect of imbalanced edges is influenced by the total amount of flow passing through them. The paper also explores the representational limits of GNN-based GFlowNets, and shows that they cannot correctly sample from certain state graphs and target distributions. To address these limitations, the authors propose the new method, LA-GFlowNets, and a metric to evaluate GFlowNets.

### Strengths
1. The paper tries to understand theoretical foundations of the popular GFlowNets, which is important and insightful. It produces theoretical guarantees and evaluate it both theoretically and empirically.

2. The paper clearly shows the contributions in Table 1, which makes the paper easier to follow.

3. The experiments are organized and easy to follow. The evaluation process is logical and comprehensive.

### Weaknesses
Two tiny points:

1. In Theorem 4, the paper says "LA-GFlowNet is more powerful". How to define "powerful" here?

2. I think the notations in Background is a little complicated. It might be better to use a figure to illustrate the model.

### Questions
In Figure 7, why does FL-GFlowNets have such large variance compared to other methods?

### Soundness
3

### Presentation
3

### Contribution
3
