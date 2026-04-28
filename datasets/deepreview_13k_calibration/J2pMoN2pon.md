# How do skip connections affect Graph Convolutional  networks  with graph sampling? A theoretical analysis on generalization

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5

## Abstract
Skip connections enable deep Graph Convolutional Networks (GCNs) to overcome oversmoothing, while graph sampling  reduces computational demands by selecting a submatrix of the graph adjacency matrix during neighborhood aggregation. Learning deep GCNs with graph sampling has shown empirical success across various applications, but a theoretical understanding of the generalization guarantees remains limited, with existing analyses ignoring either graph sampling or skip connections. This paper presents the first generalization analysis of GCNs with skip connections using graph sampling.
Our analysis demonstrates that the generalization accuracy of the learned model closely approximates the highest achievable accuracy within a broad class of target functions dependent on the proposed sparse effective adjacency matrix, denoted by $A^*$. Thus, graph sampling maintains generalization performance when $A^*$ accurately models data correlations. Notably, our findings reveal that skip connections lead to different sampling requirements across layers. In a two-hidden-layer GCN, the generalization   is more affected by the sampled matrix deviations from $A^*$ of the first layer than the second layer. To the best of our knowledge, this marks the first theoretical characterization of skip connections' role in sampling requirements. We validate our theoretical results on benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper analyzes the generalization errors of a 2-layer graph convolutional network (GCN) that incorporates skip connections and independently performs edge sampling at two different layers. Based on the developed theorems, the paper also presents a list of practical insights. Furthermore, the paper includes experimental evaluations on synthetic datasets as well as two real-world datasets, with the experimental results aligning with the theoretical findings.

### Strengths
1. The analyses focus on GCN structures with skip connections, utilizing edge sampling as the sampling strategy, which distinguishes them as novel aspects compared to previous generalization analyses on GCNs.

2. Skip connections and edge sampling are two commonly adopted design elements in contemporary GCNs. The theoretical discoveries offer valuable practical insights for the development of GCN architectures.

3. The experiments are conducted on both synthetic datasets and real-world datasets, results from both experiments support the theoretical findings.

### Weaknesses
 $\newcommand{\sB}{\mathcal{B}}$
$\newcommand{\sF}{\mathcal{F}}$
$\newcommand{\sG}{\mathcal{G}}$
$\newcommand{\mW}{\mathbf{W}}$
$\newcommand{\mV}{\mathbf{V}}$


Firstly, I want to acknowledge that I understand the challenges associated with presenting mathematically intensive theoretical analyses, and the paper's overall structure is well-constructed. The following suggestions represent some "nice-to-have" additions that could enhance the logical flow and improve reader comprehension.

1. I recommend adding an explanation for the choice of the value $d_1\sqrt{\frac{d_i}{d_j}}$ and the rationale behind differentiating the sampling strategies based on the cases where $i > j$ and $i \leq j$. The current justification is not sufficiently clear, particularly regarding how this specific form ensures that $||A^*||_1$ is $O(1)$. It would be beneficial to provide a more detailed explanation of the connection between this choice and the subsequent generalization analysis.

2. Some conclusions are presented but not utilized within the main paper, such as the bounds on $\sB_{\sF \circ \sG}$, $||\mW_t||_2$ and $||\mV_t||_2$. This may lead to confusion regarding their initial inclusion. The absence of a clear connection between these bounds and the main results makes their presence seem somewhat arbitrary, and it would be helpful to either integrate them more explicitly or remove them.

3. I recommend separating the proof for Lemma 3.1 from the proof for Theorem 3.2 and integrating them within the main paper. This adjustment is essential as it contributes to one of the key insights of the paper. The current structure obscures the importance of Lemma 3.1, and separating the proofs would allow for a more focused and clear presentation of this crucial component.

### Questions
$\newcommand{\sL}{\mathcal{L}}$
$\newcommand{\sC}{\mathcal{C}}$
$\newcommand{\sS}{\mathcal{S}}$

1. Could the authors kindly provide a brief proof for the bound on $\sL_\sG$? I am particularly interested in the steps which introduce $\sB_{\sF}$ into the final expression.

2. The upper bound for the combination factor $\alpha$ is $O(\frac{1}{kp_\sG \sC_\sS(\sG, \sB_{\sF}||A^*||_1)})$. I am curious about the order of magnitude of this value. The concern arises when this value becomes exceedingly small in practice, which can result in the target function degrading to $\sF(A^*,x)$ and thus diminishing the potential impact of $\sG(A^*, x)$ in reducing the error. This can also lead to minimal constraints on $A^2$. However, in such cases, it deviates significantly from the concept of hierarchical learning, rendering it a trivial situation.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors analyze the effect of subsampling the symmetrically normalized adjacency matrix in node regression tasks for two layered GCNs with a single skip connection. Arguing that the second layer is less affected by a "bad" sampling than the first layer, the authors propose an algorithm that samples different matrices for different layers. The sampling strategy is based on sampling edges with higher probability from low-degree nodes. Finally, the authors provide theoretical results for GCNs trained with SGD that show sample complexity bounds to achieve near-optimal performance.

### Strengths
- The analyzed problem itself is highly interesting; While many papers focus on expressivity, this papers gives generalization and complexity bounds for GNNs, which is a hard and interesting problem.
- The experimental results seem to match the theory well
- Proofs backup theoretical results

### Weaknesses
 - The authors tend to overstate their results, for example, it is often mentioned that the work would analyze a large class of graph learning models, while only two-layer GCNs are analyzed, where the final prediction layer is not trained. This is not a realistic scenario. While frequently, the GCN layers are not trained the final layer is, up to the Reviewers' knowledge, always trained to be able to linearly separate classes.
- Another example is in Section 3.1, where the authors highlight their own work in comparison to others by mentioning that other works only accommodate "shallow GCNs". However, the cited works also analyze two-layered GCNs.
- Some of the assumptions seem highly restrictive: For example in section 3.3. the function $\mathcal{F}$ and $\mathcal{G}$ are assumed to be smooth functions on $\mathbb{R}^{d \times N} \times \mathbb{R}^{N \times N}$. However, as the domain is the graph domain, it is not clear whether this is a reasonable assumption as this could break the permutation equivariance. 
- Another example is the final (untrained) layer in Equation 5, which is simply a matrix multiplication. Thus, does not satisfy universal approximation properties.
- Many notations and definitions are missing, which leads to confusion. For example, Section 3.4 is unclear. 
- The work lacks clarity, and often explanations and intuitions are not given. For example, in their main results, Lemma 3.1 and Theorem 3.2 the assumptions of the results are not clear. The results are also not well-presented.

### Questions
While the work analyzes an interesting theoretical question, the writing and presentation lack clarity and mathematical preciseness. Which are necessary to be able to value the presented results. I would recommend the authors to go over their work again, and make sure that every notion is well-defined and intuitions are given. 

Some more Questions:
-  What is OPT in Equation 13? $\mathcal{H}_{n,A^*}$ is defined as the target function, while $y_n$ is the label of node $n$. How is it possible that $OPT$ is non-zero?
-  In Lemma 3.1 and Theorem 3.2: It is not clear with respect to which event the probability is taken.
- In Theorem 3.2: Could the authors present the assumptions better or give more intuitions?
- Why do the authors average in Equation 14 over all iterations of the SGD steps?
- How is $(X,y_n)$ sampled, and how is $\mathcal{D}$ defined?
- Could you elaborate on many assumptions, e.g., Section 3.4: it doesn't seem clear that the norms of the learned weight matrices are uniformly bounded.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors try to figure the relationship between graph sampling and skip-connections in GCN. Based on this motivation, many solid theories have been given. Also they validate the theoretical results on benchmark datasets.

### Strengths
1. This paper gives a different theoretical perspective on the relationship between graph sampling and different layers of GCNs.

2. It provides very solid theoretical analysis. It is convincing.

### Weaknesses
This work is far from the real setting of graph neural networks.
1. In this paper, they assume all with perfectly homophilous graphs. Actually, it is not going to happen in heterophilous graphs. If we have perfectly homophilous graphs, the stationary point will make the generalization happen. 

2. The setting of two-layer skip connections is oversimple. Two graph convolutions only access two-hop neighborhoods. Thus, I cannot imagine how these conclusions can inspire this community (Graph Neural Network).

3. The dense graph is not a usual condition. Even the transformer generates an implicit graph from batch data (then it is sparse from the global point.). If the graph is dense and perfectly homophilous, then the graph convolution basically equals making every node its' class center.

### Questions
I have some concerns about how this work can help graph neural network (or transformer) community.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper delves into the generalization of a two-layer GNN that takes both the residual connection and sampling into consideration. This paper is very hard to digest due to writting issue.

### Strengths
The orginal motivation of this paper is very interesting and important. But the theoritical part needs improvment.

### Weaknesses
The paper looks fine until Section 3.3.

However, beyond Section 3.3, it gives the impression that the authors may not have fully understand Allen-Zhu & Li's work before extending it from a residual-connected MLP to a residual-connected GCN. Consequently, the notations, proofs, and overall presentation become challenging to digest:

1. The presentation lacks clarity, with numerous notations introduced without proper explanation. For instance, in the paragraph surrounding Equations 6 and 7, the authors transform the original 2-layer residual-connected GCN into a new format, but it remains unclear how these two formulations correspond. Questions arise regarding the meaning of symbols like $p_\mathcal{F}$ and $p_\mathcal{G}$. Additionally, it's unclear what $\sum_{i\in [p_\mathcal{F}]}$ and $\sum_{i\in [p_\mathcal{G}]}$ represent in the context of GCN. It's also unclear whether $w_{r,i}^\star$ refers to the i-th or r-th row/column of a weight matrix. This section is not well organized, making it exceptionally challenging to comprehend.

2. The notation on Page 6, particularly at the top under the algorithm section, is even more convoluted. The authors introduce numerous notations, but their purpose and connection to GCN are unclear. I have no idea how these notations relate to the GCN.

3. There appear to be errors in the paper. Detailed questions and concerns have been raised, which should be addressed for clarity and accuracy.

4. 2-layer GNN is not deep enough comparing to existing works. Especially the authors argue existing works' considered model is not deep ...

### Questions
1. On Page 5, at the top, we have this $d_1 \sqrt{d_i/d_j}$. Where does this $d_1$ originate from? Why does the node sampling probability always depend on this value?

2. According to your sampling method, neither $A^\star$ nor the "expectation of the sampled adjacency matrices" is identical to the original adjacency matrix $A$. Won't this introduce bias during training? In other words, your objective differs from the original objective function. In this case, how can we ensure generalization?

3. What does the first term on page 6, in the first line, represent? Without a clear explanation, I cannot grasp the impact of $A^\star$ on the $\epsilon_0$ of Thm3.2.

4. Why C is not trainable in Eq. 1-4? Since this is linear-regression using square loss, cannot we just think this C as identity matrix?

5. What is the $r_w$ and $r_v$ in Eq. 11-12?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
