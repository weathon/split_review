# Recovery of Causal Graph Involving Latent Variables via Homologous Surrogates

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Causal discovery with latent variables is an important and challenging problem. To identify latent variables and infer their causal relations, most existing works rely on the assumption that latent variables have pure children. Considering that this assumption is potentially restrictive in practice and not strictly necessary in theory, by introducing the concept of homologous surrogate, this paper eliminates the need for pure child in the context of causal discovery with latent variables. The homologous surrogate fundamentally differs from the pure child in the sense that the latter is characterized by having strictly restricted parents while the former allows for much more flexible parents. We formulate two assumptions involving homologous surrogates and develop theoretical results under each assumption. Under the weaker assumption, our theoretical results imply that we can determine each variable's ancestors, that is, partially recover the causal graph. The stronger assumption further enables us to determine each variable's parents exactly, that is, fully recover the causal graph. Building on these theoretical results, we derive an algorithm that fully leverages the properties of homologous surrogates for causal graph recovery. Also, we validate its efficacy through experiments. Our work broadens the applicability of causal discovery. Our source code is publicly available via this anonymous link: https://anonymous.4open.science/r/f15G8O29BB

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the concept of homologous surrogates to address the challenges associated with causal discovery involving latent variables. It formulates two assumptions regarding homologous surrogates and develops theoretical results based on each assumption. Under the weaker assumption, the authors demonstrate the feasibility of partially recovering the causal graph by identifying the ancestors of each variable. The stronger assumption facilitates the exact identification of each variable's parents, enabling full recovery of the causal graph. Additionally, the paper proposes an algorithm that effectively leverages the properties of homologous surrogates for causal graph recovery and validates its effectiveness through experimental results.

### Strengths
1. This paper deals with a causal structure learning problem involving latent variables, which is significant for the field of causal discovery.

2. The authors proposes a method for identify the causal structure via the homologous surrogates under mild assumptions.

### Weaknesses
1. The representation needs refinement, as the content of the paper lacks logical flow and coherence, which makes it difficult for readers to follow the main points.

2. The technical contributions appear to be somewhat constrained. This paper draws upon two established methodologies, pseudo-residuals and causal effect estimation via cumulants. It introduces the concept of homologous children, which is fundamentally equivalent to the notion of pure children.

3. The authors mentioned that their work expands the applicability of causal discovery methods, and that homologous surrogates aid in causal discovery with latent variables. However, in the experimental results involving real-world data, their proposed method performs poorly. The authors believe this is due to a limited sample size. So, are there more suitable real-world datasets available to validate the method proposed in this paper?

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method for causal discovery with latent variables while relaxing the common assumption that requires the existence of pure children. Instead, the method relies on the condition of homologous surrogates, which can have multiple parents. The proposed algorithms are validated on synthetic data.

### Strengths
1. The theoretical results are clearly stated with all definitions introduced clearly.

2. The figures are helpful in understanding the method.

3. Experiments in various settings validate the effectiveness of the algorithm.

4. The limitations have been discussed explicitly.

### Weaknesses
1. Since "homologous surrogate" is a newly introduced term, it would be helpful to provide a concrete example immediately when it is first mentioned in the manuscript. This would aid readers in understanding the concept more intuitively.

2. Some of the most closely related works have not been mentioned in the introduction. For example, [Dong et al., 2024] consider almost the same problem with a very similar motivation, i.e., relaxing the structural assumptions among latent and observed variables. That work also allows the existence of children for observed variables. Currently, the discussion was only in the remark and related work at the end of the manuscript, but not in the introduction.

3. In line 82, it states that the considered setting is new in causal discovery. However, it might not be accurate since causally-related latent variables have been considered before, even in the presence of observed variables' children. I understand that omitting works such as [Dong et al. 2024] in the introduction would make the story clearer, but it might introduce confusion for readers less familiar with the field.

4. In line 45, it seems to state that [Jin et al. 2024] make the pure children assumption, which might also not be true.

### Questions
Please refer to the comments above. Some statements in the current manuscript are not precise, and the overlooking of some closely related work in the introduction may introduce confusion about the unique contributions of this work.

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
4

### Summary
This paper proposes a causal discovery method with latent variables. Instead of assuming that each latent variable has multiple pure children, they assume that each latent variable has at least one homologous surrogate. They define homologous surrogates and develop identifiability analysis under the homologous-surrogate assumptions. Experiments show the efficacy of their proposed algorithm.

### Strengths
1)	The authors tackle a significant but challenging causal discovery problem, that is, identifying latent variables and recovering causal relations between all latent and observed variables.

2)	They introduce two assumptions about the defined homologous surrogates, based on which they develop partial and full identifiability theories. They also propose an algorithm to uncover the causal relationships between latent and observed variables.

### Weaknesses
1. The algorithm’s complexity is high, i.e., $O(|O|^4)$ and $O(|O|^2 |L|^2)$ for Algorithms 1 and 2, respectively, which could limit its real-world application. It might be better to give empirical complexity analysis in the experiments, compared with other baselines.

2. Regarding the simulated causal graphs in Figure 5 for the experiments, I think the networks are all small. It could help to investigate the performances when there are more latent variables and when the causal relations between latent variables are sparse.

3. It might be better to give simple descriptions and basic conclusions of the experiment on the real-world dataset Holzinger and Swineford, in the main paper. BTW, from Appendix C, the performances on such a real-world dataset look not satisfactory.

4. It is good to give examples for the definitions. But I think giving examples for the theorems also matters since it is hard to catch the main idea or intuitions for the basic theorems.

### Questions
1.	In Equation (7), how are the parents $O_j$ of $O_i$ identified? $O_j$ here might be observed ancestors of $O_i$? It is not clear which step aims to find the parents. Since $M_O^O$ is derived from Algorithm 1, which could contain some spurious edges.

2.	As illustrated by the authors, their algorithms suffer from cases with small sample sizes but could achieve ideal performances when assumptions are met and the sample sizes are large enough. For example, in ideal Case 2 of the experiments, how many samples are needed to achieve the ideal results?

3.	If the number of latent variables is not estimated correctly, what would happen? Did it greatly impact the final results?

4)	The following paper [1] tackles the same problem and also allows non-pure children. Hence I suggest discussing the differences and connections with it.

[1] Xie F, Huang B, Chen Z, et al. Generalized independent noise condition for estimating causal structure with latent variables[J]. Journal of Machine Learning Research, 2024, 25: 1-61.

### Soundness
2

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
3

### Summary
The paper proposes the use of homologous surrogates to identify latent variables and recover the causal graph. The main contribution of this work is that, unlike pure child variables, homologous surrogates allow for the presence of other parents. Based on this concept, the paper develops corresponding theoretical support and applies it to an algorithm.

### Strengths
The innovation of this paper is quite novel, as it uses homologous surrogates to identify latent variables and then recover the causal graph. The supporting theories are also rich, and the corresponding proofs are complete. The theories and propositions applied in the algorithm section are clearly explained, along with examples. These theories are crucial for the implementation of the algorithm. The method proposed in this paper offers a new perspective for discovering latent variables.

### Weaknesses
In the third chapter, PARTIAL RECOVERY, the explanation of the algorithm and theoretical part is not very clear in terms of formatting. The formulas and theoretical support needed for the preceding theories and hypotheses are instead explained afterward, which increases the difficulty of reading and affects the logical flow. For example, in "Identifying Observed Root Variables.", in the "Intuition" section, Theorems 1 and 2 are mentioned, so they should be placed before the "Intuition" section. The theories used in the proof should appear before the proof itself, rather than afterwards.



### Questions
1. In Algorithm 1, the font of "Thm.1" in line 3 is different from the "Thm.1" in other parts of the pseudocode, which needs attention.
2. For Algorithm 1 and Algorithm 2, the authors use Figure 2 and Figure 3 for explanation, but the tracking example is placed in the figure captions, and the corresponding steps are not explained in detail. It is recommended to add more detailed explanations in the main text to guide readers in understanding the example presented in the figures.
3. Please add your source code link to the paper.

### Soundness
3

### Presentation
2

### Contribution
2
