# Interpretable and Generalizable Graph Neural Networks via Subgraph Multilinear Extension

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 6, 8, 6

## Abstract
Interpretable graph neural networks (XGNNs) are widely adopted in scientific applications involving graph-structured data. Previous approaches predominantly adopt the attention-based mechanism to learn edge or node importance for extracting and making predictions with the interpretable subgraph. However, the representational properties and limitations of these methods remain inadequately explored. In this work, we present a theoretical framework that formulates interpretable subgraph learning with the multilinear extension of the subgraph distribution, which we term as subgraph multilinear extension (SubMT). Extracting the desired interpretable subgraph requires an accurate approximation of SubMT, yet we find that the existing XGNNs can have a huge gap in fitting SubMT. Consequently, the SubMT approximation failure will lead to the degenerated interpretability of the extracted subgraphs. To mitigate the issue, we design a new XGNN architecture called Graph Multilinear neT (GMT), which is provably more powerful in approximating SubMT. We empirically validate our theoretical findings on a number of graph classification benchmarks. The results demonstrate that GMT outperforms the state-of-the-art up to 10% in terms of both interpretability and generalizability measures.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a framework for GNN explanation through the len of multilinear extension. To improve the expressiveness they proposed a new method, namely GMT. One variant of GMT is to make sure the GNN is fully linear. Another neural version is to simply re-train a GNN classifier with a frozen subgraph extractor.

### Strengths
The paper offered some interesting insights into interpretable GNNs and proposed some solutions. The experiments on the proposed methods are extensive and shown pretty good results.

### Weaknesses
First of all, I find the paper hard to read and follow. The presentation and writing need some good work to make the paper more readable and clear. While the authors seem to had a hard time squeeze the paper below the page limit, they also over cite even by a very conservative standard. The citation list is almost the same length as the paper itself.
The experiment set-up is actually quite complicated as detailed in appendix E. The authors also searched extensively for different setups (stated in F2). It is unclear how sensitive the result is, wrt. warm-up strategy and a bunch of sampling strategies in Appendix E2 (page 32).

### Questions
Is there any reason or hypothesis that both SubMT (Figure 2) and GMT (Figure 6/7 in Appendix) perform better on Mutag but less well on BA-2Motifs?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on investigating theoretical foundations for interpretable graph neural networks (XGNN). To study the expressive power of interpretable GNNs, the authors propose a framework that formulates interpretable subgraph learning with the multilinear extension of the subgraph predictivity (subMT). To obtain a more accurate approximation of SubMT, the authors design an XGNN architecture (GMT). The superior empirical results on several graph classification benchmarks support the theoretical findings.

### Strengths
1. It's interesting to see some works focusing on better understanding the theoretical foundation for the expressive power of XGNN. The motivation to consider the connection between interpretable subgraph learning and multilinear extension is also sound.
2. There are some empirical results to directly support the theoretical findings/claims, which have some merits. For example, the ablation studies demonstrate a better performance on counterfactual fidelity which supports the claims in Sec 4.2.
3. The overall empirical performance of the proposed method seems significantly better than those of baselines.

### Weaknesses
1. For Proposition 3.3, in my understanding, it basically says with > 2-layer linear GNN, Eq (6) cannot approximate SubMT. Do you provide any proof of that? Besides, I am curious if we have any empirical findings regarding this. The claim that a multi-layer linear GNN cannot approximate SubMT needs more rigorous justification. Specifically, the paper should elaborate on why the multilinear extension of the subgraph predictivity (SubMT) cannot be accurately captured by the composition of linear transformations in a deep GNN. It is not immediately clear why the expectation of the function of a random variable is not equal to the function of the expectation of the random variable in this context, especially when dealing with linear operations. A more detailed explanation of the mathematical properties that lead to this discrepancy is needed.
2. For interpretation performance comparison, the authors provide more baseline methods for GIN while PNA only has GSAT. I wonder what the reason is for this. Could you provide more baselines with PNA as the backbone? The lack of a comprehensive comparison with various interpretation baselines for the PNA backbone is a significant concern. While GSAT might be a strong baseline, it is essential to evaluate the proposed method against a broader range of established interpretation techniques to ensure the robustness of the findings. The paper should include more post-hoc methods and intrinsic interpretable baselines to provide a more complete picture of the performance of the proposed method when using PNA as the backbone. This is especially important given that PNA is a more powerful architecture than GIN, and the interpretation performance might vary significantly across different architectures.

### Questions
See the above questions in weaknesses. 
Minors:
1. Table 4 is before Table 2 and 3. It would be better to fix this.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper seeks a theoretical understanding of the representational properties and limitations of interpretable GNNs (XGNNs). The paper identifies the ability to approximate the so-called Subgraph Multilinear Extension as the key distribution for interpretable subgraph learning. Building on this observation, they propose the GMT model which implements such an approximation. The paper experimentally demonstrates the superiority of GMT in interpretation and generalization.

### Strengths
The paper is overall very well-written and the ideas are neatly structured. The authors are able to devise a theoretical framework for characterizing the expressivity of XGNNs, and shows that the existing XGNNs fail to approximate the subgraph multilinear extension function. The proposed XGNN admits a natural design in light of the above deficiency. The experimental protocol is quite thorough and the conducted experiments adequately test the hypothesis.

### Weaknesses
The prediction performance of the proposed model does not see too much improvement over the state-of-the-art. There is not much discussion over the time complexity of GMT-SAM version, vis-a-vis the GMT-LIN version.

### Questions
1. Page 4: "Note that $f_c$ is a GNN defined only for discrete graph-structured inputs (i.e., $α \in [0, 1]^m$)". Do you mean all Boolean m-length vectors, because otherwise this is not really discrete. 

2. Page 4: "which implicitly assumes the random graph data model (Erdos & Renyi, 1984). Def. 3.1 can also be generalized to other graph models with the corresponding parameterization ... ". Can you please comment on this further if this admits such a straightforward generalization to other models than ER, such SBMs or graphons as you suggested?

3. What is $k$ in Eq. 9? Does it mean an application of k-layers of linear message-passing layers? In continuation, in Eq 11, what is the intuition behind the Hadamard operation between $\hat{A}$ and $A^{k-1}$? Section 5.1 needs to be written more clearly.

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
In this paper, the authors introduce a self-interpretable graph neural network rooted in the concept of subgraph multilinear extension. The method is elaborated from a perspective of counterfactual fidelity, and the authors put forward both linear and sampling-based graph neural networks (GNNs) for subgraph extraction. The experimental results suggest that the proposed method is effective in achieving its intended goals.

### Strengths
1. The proposed method is well-supported by theoretical foundations. The authors provide an insightful explanation of the causal subgraph from a fidelity perspective and derive a method that aligns well with this theoretical underpinning.

2. The authors offer a theoretical framework for improving graph interpretability and shed light on why existing methods often fall short in this regard. They also articulate how they aim to meet this criterion and present experimental results that appear to support their proposition.

### Weaknesses
The authors conduct multiple comparisons between the proposed method and GSAT throughout the paper. However, it appears that the primary distinction lies in the sampling process, with the proposed method incorporating a higher number of samples than previously employed in GSAT. It would be valuable for the authors to emphasize this key differentiator and provide a more detailed discussion regarding the impact of increased sampling on the method's performance and results. This would enable a clearer understanding of the specific advantages of their approach over GSAT.

### Questions
For figure 2(b) and 2(c), what is the distance metric specifically used? Will there be any difference in the results using different metrics?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
