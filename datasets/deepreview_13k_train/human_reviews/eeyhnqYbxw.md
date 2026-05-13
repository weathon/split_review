# The Geometry of Attention: Ricci Curvature and Transformers Training and  Robustness

- Decision: Reject
- Scores: 5, 5, 3, 6, 5

## Abstract
Transformer models have revolutionized machine learning, and the theoretical underpinnings behind their success are only now starting to be explored. 
In this work, we analyze the performance and robustness of transformers by considering the attention mechanism as a graph operator, focusing on the geometry of attention maps viewed as weighted graphs.
Specifically, we investigate the role of Ricci curvature, a metric closely tied to graph spectral properties and system robustness, in shaping the training dynamics and robustness of transformers. 
Our theoretical analysis establishes a link between Ricci curvature and the convergence of gradient descent on transformers, and consequently, their training and fine tuning.
We also show that a higher frequency of more positive values in the Ricci curvature distribution of attention graphs, therefore more system robustness, leads to more robust transformers, highlighting the impact of curvature on the robustness of transformers.
Leveraging these insights, we propose an efficient regularization method to train curvature-adjusted transformers. 
Supporting our theoretical findings, experiments show that our proposed attention curvature manipulation can improve the learning speed, performance, or generalizability of vision and language transformers.
Additionally, our observations point to a trade-off between their performance and robustness.
This work demonstrates that the geometry of the attention map provides a theoretically elegant and computationally versatile framework for analyzing and manipulating transformers training, generalization, performance, and robustness, opening new avenues for designing models using geometric concepts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper explores the geometry of attention maps in transformer models. Specifically, the authors examine the relationship between Ricci curvature in attention, the convergence rate of gradient descent in transformers, and model robustness. They observe that lower curvature correlates with reduced robustness and faster convergence. Additionally, they demonstrate how the Ricci curvature distribution in attention graphs impacts transformer robustness. The authors propose a training method that enables curvature adjustment within the attention graph, enhancing transformer performance and generalizability. Experimental results support the theoretical findings and highlight the advantages of the proposed training approach.

### Strengths
1. The paper provides an interesting approach to studying attention mechanisms in transformers using Ollivier-Ricci curvature.

2. Theoretical results are discussed, and extensive empirical results are provided to justify the theoretical results.

3. The paper is well-written with illustrative figures.

### Weaknesses
1. The authors rely on strong assumptions to establish Lemma 4.2 and Theorem 3.1. Notably, Assumption A0 implies that the attention matrix A is symmetric, which is uncommon in practical settings. This assumption, while simplifying the analysis, neglects the inherent asymmetry introduced by the value projection in the attention mechanism. Specifically, the attention output is computed as $AV$, where $A$ is derived from the softmax of query-key similarities, and $V$ is the value matrix. Even if the similarity matrix is symmetric, the multiplication by $V$ generally results in an asymmetric attention matrix. Assumption A1 is even more restrictive, as it requires A to be invertible. This is a strong constraint, as attention matrices can often be rank-deficient, especially in cases where some tokens do not attend to others. The remaining assumptions are also quite limiting. Furthermore, the authors assume that A does not depend on the input X; however, in practice, the attention matrix A is indeed a function of X, which invalidates the proofs presented in the paper. The dependence of A on X through the query and key projections ($Q = XW_Q$ and $K = XW_K$) is a crucial aspect of the transformer architecture that is not adequately addressed in the theoretical framework.

2. Connections between curvature and robustness are not new and already established in [1] and [2]. Thus, this is not a contribution of the paper. The paper does not sufficiently differentiate its findings from these prior works, particularly in the context of transformers. While the application to transformers is novel, the underlying relationship between curvature and robustness is not a new finding. The authors need to more clearly articulate the specific novel insights they provide beyond the existing literature.

3. Experiments on larger datasets beyond CIFAR10, MNIST, and Fashion-MNIST are needed are needed for vision models. The current experimental setup is limited in scope and does not demonstrate the generalizability of the proposed method to more complex and realistic scenarios. The lack of experiments on larger, more challenging datasets makes it difficult to assess the practical impact of the proposed approach.

### Questions
1. The proofs provided in the paper are not new and are mostly borrowed from other papers. Given that experiments are not the strength of the paper, this can be a minus point. 

2. Empirical comparisons to the baseline methods seem to be missing.

**References**

[1] Lloyd Demetrius and Thomas Manke. Robustness and network evolution—an entropic principle. Physica A: Statistical Mechanics and its Applications, 346(3-4):682–696, 2005. 

[2] Maryam Pouryahya, James Mathews, and Allen Tannenbaum. Comparing three notions of discrete Ricci curvature on biological networks. arXiv preprint arXiv:1712.02943, 2017.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed a connection between gradient descent convergence and Ricci curvature in transformers and applied geometric tools to improve the performance of the attention mechanism.

### Strengths
1. This paper takes attention maps as weighted graphs and investigates the geometric properties.

2. Experiments are conducted thoroughly, making the empirical results more robust.

### Weaknesses
$ullet$ It is unclear whether this paper is intended to be primarily theoretical or experimental. A significant portion is devoted to technical background, much of which either summarizes existing results from other works or relies on rough assumptions, without providing deeper theoretical insights. The subsequent introduction of a regularization method for training curvature-adjusted transformers and related experiments adds further ambiguity. If the goal is to present a theoretical paper, I suggest including more original theoretical contributions, such as a rigorous proof connecting the Ricci curvature of the attention graph to the convergence rate of gradient descent, rather than relying on existing results and assumptions. Alternatively, if the focus is on proposing an algorithm, consider abbreviating the technical background and dedicating more space to the regularization method and experimental findings, including a detailed analysis of the computational cost and hyperparameter sensitivity of the proposed method.

Minor points:
1. In the paragraph following Lemma 4.2, "... Laplacian Bauer et al. (2011) " $\to$ "... Laplacian (Bauer et al. 2011) ".
2. Provide a more detailed description of Figure 3 within the main text, rather than in the appendix, as it is difficult to interpret Figure 3 with only the information available in the main body of the paper. Specifically, the axes and the meaning of the different colored lines should be clearly explained in the main text, along with a discussion of the observed trends and their implications for the proposed method.

### Questions
1. In equation 3, you mentioned that $\underline{k}$ is the lower bound of the Ricci curvature and that a large ORC results in high entropy. However, this relationship is not entirely clear to me, as a large ORC does not necessarily imply a higher lower bound. In fact, a large ORC could still be compatible with a low lower bound. If $\underline{k}$ served as an upper bound instead, this relationship would make more sense. Could you provide further explanation on how a large ORC correlates with high entropy under these conditions?

2. You mentioned, “A rigorous understanding of how transformers process their input remains elusive, especially through mathematical tools offering practical solutions.” However, there are many existing mathematical tools, such as Centered Kernel Alignment (CKA). What are the specific advantages of using Ricci curvature over other tools? CKA, for instance, provides more straightforward results and interpretability compared to Ricci curvature. Could you elaborate on the unique insights that Ricci curvature offers in this context?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper reinvests the idea of considering attention matrices as adjacency matrices of graphs to investigate potential connections between curvature and training dynamics in a layer that is claimed to resemble the one in transformers. A regularization scheme is introduced based on an observed correlation between the robustness of the network and the curvature. Some experiements are provided to support these claims.

### Strengths
- This paper’s aim which is to investigate the underlying graph structure explaining token's interactions is a compelling idea that deserves further exploration.

- Given the rich literature on curvature, geometry and graphs, this approach has the potential to uncover interesting phenomena by connecting these areas.

- Analyzing training dynamics from an overparametrized perspective is a promising approach and connects well with recent findings in optimization theory.

### Weaknesses
The main reason for rejecting this paper is that although it presents itself as a theoretical paper, it actually contains many imprecise, non rigorous and at times incorrect elements, below are some of the most problematic ones:

1. Some assumptions are overly restrictive, e.g. considering constant attention across layers (i.e. the attention cannot result from the standard key-query dot product involving the features from the previous layer) and bold claims are made throughout the paper to justify them, like in line 253 "Note that relaxing the above mentioned assumptions is rather straightforward, though distracting and not amenable to the here provided analysis". However, equation 6 immediately breaks without this assumption as computing the eigenvalues of a product of matrices is highly non trivial without further assumptions, despite the authors’claim, which is thus unsupported. Furthermore, the assumption of constant attention matrices across layers severely limits the model's capacity to learn complex relationships between tokens, effectively reducing it to a linear transformation of the input, which is a significant oversimplification for a model that is claimed to resemble a transformer.

2. Additional issues with the paper’s assumptions include: (a) being relegated to the appendix, while the work is meant to be theoretical, (b) being labelled as «  standard » and constantly justified by the fact that they were used in Dovonan et al 2024, a paper that got rejected at ICLR 2024 precisely because of these limited assumptions (see discussion on openreview here https://openreview.net/forum?id=OCx7dp58H1), (c) being so restrictive that considering them reduces the analysis to considering a linear model in the input data, already analysed in which Liu et al., 2022 for (S)GD convergence. This reliance on a rejected paper's assumptions undermines the novelty and validity of the current work, as it inherits the same fundamental limitations. The justification of these assumptions as 'standard' is misleading given their known limitations and the fact that they are not standard in the broader transformer literature.

3. Theorem 4.1 mis-cites the result from Liu et al. 2022--it holds only for the mean square error loss. In particular, the extension of such result to more general loss functions is highly non trivial and lead to multiple research papers (eg see Robin et al., 2022 and Scaman et al.,2022 where the authors generalize the result to cross entropy loss, among others). Additionally, in the experiments section, the authors use the cross entropy loss and dont seem to be fully aware of the aforementioned sublety (or at best a discussion is missing in the paper regarding the task under study). This oversight raises serious concerns about the validity of the theoretical claims when applied to the experimental setup.

4. The proof (Appendix A.2) of the main theorem (Lemma 4.2) is incorrect:
- Minor: line 762: "2L-3" should be "2L-2" line 773
- Major (this mistake invalidates the proof): line 774: if the laplacian is defined as L = I - A, then its largest eigenvalue is 1-the smallest eigenvalue of A, not 1-the largest eigenvalue of A, as incorrectly described in the paper. Given that the following arguments in the proof rely on a bound given in Bauer et al. 2011 that does not involve the largest eigenvalue of A, the proof likely requires substantial revision or correction. The incorrect use of the Laplacian's eigenvalue invalidates the subsequent steps in the proof, rendering the conclusions unreliable.
- Major (invalidates the proof too): line 774: even if we were to assume the authors got a correct and meaningful bound between the smallest eigenvalue of A and the minimum ORC, the next argument in the proof does not hold either since it is based on differentiating an inequality. This is a fundamental error in mathematical reasoning, as differentiating an inequality is not a valid operation without further justification, which is absent in the current proof.

5. The related work section in the appendix is not so well written and overly self-promotional. Each of its paragraph finishes with the same sentence "To the best of our knowledge, this is the first work to […]". In general, claimed contributions are overly emphasised on in this manuscript, reducing space for essential details and, at times, interfering with the quality of the writing. This self-promotional tone detracts from the objective assessment of the work's contributions and makes it difficult to evaluate the actual novelty.

6. Minor: the provided plots could be averaged over multiple simulations with visible some standard deviations (figures 3-4-6) to get more statistically convincing comparisons. The lack of statistical rigor in the experimental results makes it difficult to draw firm conclusions from the presented data.

### Questions
- Taking a geometrical lens on the attention layer is an elegant thing on its own but could also potentially enable us to reveal and explain some phenomena. I would definitely encourage the authors to pursue in this direction.

- It may be helpful in the first place to restrict the analysis to a single-layer transformer, make the proof rigorous in this case, before aiming for more general results.

- In the definition of the graph ricci curvature, what led the authors to pick ORC as a good metric? And how do they define a distance metric on V, the set of vertices?

- The link between curvature and weight variance is unclear to me despite reading the appendix; could the authors clarify? Also, what makes this regularization term appealing?

### Soundness
1

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
This work focuses on the geometry of attention maps viewed as weighted graphs and analyzes the performance and robustness of transformers by considering the attention mechanism as a graph operator. This work establishes a link between Ricci curvature and the convergence behavior of gradient descent by theoretical analysis and highlights the impact of curvature on robustness. A trade-off between the performance and the robustness of the transformer model can be uncovered by the Ricci curvature. Hence, this is an interesting work.

### Strengths
Originality: The idea of using Ricci curvature to metricize the training dynamics and robustness of transformers is innovative and establishes a direct link between Ricci curvature and the convergence behavior of gradient descent in transformers.

Quality and Clarity: The quality of this is satisfactory and the analysis is thoughtful. The proposed method that manipulates the curvature distribution of attention maps through a variance-adjusting regularization term is sound and illuminates the trade-off between performance and robustness by adjusting the Ricci curvature.

Significance: This work provides a contribution to the transformer model, including studying and improving attention mechanisms.

### Weaknesses
It would be interesting to see if the proposed method outperforms other attention map distribution regularizations in the experiments.

### Questions
it is the same as Weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the relationship between the Olivier Ricci Curvature (ORC) of the attention graphs in transformers and their learning dynamics as well as their robustness to instance and distributional perturbations. In particular, the main hypothesis of the paper is more negatively distributed ORC values implies faster convergence speed of gradient descent in transformers, while more positively distributed ORC values leads to their more robustness. The authors have proposed a theoretical framework to support this hypothesis as well as a practical technique to incorporate it within training transformers. They also performed multiple experiments to empirically support their hypothesis.

### Strengths
1. This paper addresses a very interesting and important topic re: the interplay of transformers' trainability and their robustness and their relationship with the geometry of the attention maps. To my knowledge, this topic hasn't been explored explicitly in the literature which makes this work a valuable contribution in that regard.

2. The authors have also run extensive empirical studies to measure the relationship between transformers' robustness and training dynamics to geometric properties of the underlying attention maps quantified by ORC distribution. For robustness, the authors have covered various types of domain-specific perturbations and data augmentation techniques as well as generalization robustness, which is quite interesting and extensive, in my opinion. Furthermore, the link between the geometric structure of attention matrix and its training dynamics during gradient descent is very exciting.

3. The paper is generally very well written with a clear flow and precise statements.

### Weaknesses
Despite its interesting topic of study and the extensive empirical experiments, there are certain flaws in this work in terms the theoretical contribution of the paper which give me a pause to give a higher score to it:

1- First of all, it's not clear to me why Ricci Curvature has been chosen as the main cornerstone of impact on trainability and robustness in this work. There's nowhere in the proposed framework that ORC is directly being optimized nor injected into the training process. Also, the theoretical results clearly point to the smallest eigenvalues of normalized Laplacian which are directly linked to the notion of graph-cut and sparsity in the underlying graph. Sure enough, ORC is also strongly correlated with these fundamental quantities, but why not focusing on these fundamental notions instead of ORC? In particular, what would formulating the problem in terms of ORC give us specifically that we'd not be able to get using e.g. (weighted) graph cut, which is more general? From that view, it also seems the extensive previous work on sparse and low-rank attention is highly relevant to the current work, and yet there's no mention of them in the paper.

2- The main theoretical contribution of the paper might as well be true but the presented proof for it is indeed flawed. Please note that the assumption of having identical attention blocks in each layer does *not* imply that the actual attention matrix A would be the same in each layer, as A is dependent on the input of each layer which is different for each layer, even when using the same attention block. Therefore, in Eq. (5) & (9), the attention matrix A needs to be layer-dependent, which would break down the whole proof strategy. Possible ways of getting out of this are either to assume having the same attention matrix in each layer (which is completely unrealistic due to what we know of the forward pass in transformers) OR do the analysis for L=1 layer, but this also would break down the proof of Lemma 4.2. As a result, the current flawed proof would cast serious doubt on the main theoretical result of this paper unless the authors can provide another proof strategy.

3- As for the algorithmic contribution of the paper, it's not hard to see that given the standard L2-norm regularization on the network's weight, tuning the temperature parameter of the Softmax can also be used to modulate the variance of attention weights in an attention matrix. In particular, higher temperatures reduce the variance while lower temperatures increase it. So then the question is why not using the more natural SoftMax temperature instead of introducing ad-hoc regularization functions on the weight variance? I can see at least 3 main benefits of doing so over the proposed method in the paper: (A) we can have layer-specific adjustments, (B) instead of having a binary mode (variance increasing vs. variance decreasing), tuning the temperature parameter gives us a full continuous range of scenarios, and (C) we can actually learn the optimal temperature parameters for each layer in a completely data-centric fashion. For instance, for training a more robust model, we can use data perturbation/augmentation during training, and let the model decide what the temperature should be in each layer for that level of perturbation. At the very least, an empirical comparison between these two methods would be more persuasive. 

4- As for the empirical evaluation, Table 1 is not really conclusive. I'd highly recommend using training loss instead of training accuracy (to measure training convergence) and use the test accuracy (and NOT the train-test accuracy difference) as the measure of generalizability which is the standard way of doing it. Also, please specify the values of hyper-parameters related to the regularization terms in your experiments and how you picked them.

Typos:

Line 176: positive-learning --> positive leaning

Line 716: positively --> negatively

### Questions
To recap my questions from the concerns raised in the previous section:

1- In your analysis and conclusions, what specific benefit ORC would give us compared to the more general notion of (weighted) graph cuts)? And how would that link your work to the existing extensive work on sparse and low-rank attention?

2- Does the main theoretical result of the paper sill hold given the flawed proof provided? If so, what's your proof strategy?

3- Why not using more natural SoftMax temperature instead of the proposed regularization terms, especially given its extra benefits? What particular benefit would we get from using the proposed regularization terms instead?

### Soundness
2

### Presentation
4

### Contribution
3
