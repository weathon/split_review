# Sparse Training of Discrete Diffusion Models for Graph Generation

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Generative models for graphs often encounter scalability challenges due to the inherent need to predict interactions for every node pair. 
Despite the sparsity often exhibited by real-world graphs, the unpredictable sparsity patterns of their adjacency matrices, stemming from their unordered nature, leads to quadratic computational complexity.
In this work, we introduce SparseDiff, a denoising diffusion model for graph generation that is able to exploit sparsity during its training phase.
At the core of SparseDiff is a message-passing neural network tailored to predict only a subset of edges during each forward pass. When combined with a sparsity-preserving noise model, this model can efficiently work with edge lists representations of graphs, paving the way for scalability to much larger structures.
During the sampling phase, SparseDiff iteratively populates the adjacency matrix from its prior state, ensuring prediction of the full graph while controlling memory utilization.
Experimental results show that SparseDiff simultaneously matches state-of-the-art in generation performance on both small and large graphs, highlighting the versatility of our method.\blfootnote{Contact: \texttt{yiming.qin@epfl.ch}.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a method that employs sub-graph (edge-wise) sampling and sparse message passing neural networks to enhance the scalability of graph diffusion models during training.

### Strengths
The proposed approach uses some techniques to leverage the sparsity of the graphs during training.

### Weaknesses
Despite the attempt to leverage sparsity in training, the method's contributions appear to be incremental, lacking significant advancements. Additionally, the graph generation (sampling) is still quadratic which is a bottleneck in such a family of models.

The paper's presentation is incomplete, and the absence of an appendix further hinders clarity. Moreover, several parts of the paper seem to be reiterations of DiGress. There are also some typos and grammatical issues throughout the manuscript.
- Page 4: 
  - “Since the noise model is markovian, ~~there~~ the noise does not need”
  - “We denote by k the edge ratio ~~ratio~~ … ”
- page 5: 
  - The paragraph “This lemma shows that, in large and sparse graph …” is not clear.
- page 6:
  -  “will define our computational graph ~~$E_c$~~ ~~$G_c$~~ …”
  - “as well as a list of edges denoted $E_c$ …” => “as well as a list of edges denoted by $E_c$ …”
  - “One extra benefit of using a computational graph ~~that~~ with more edges …” 
  - “Finally, similarly to standard graph …” => “Finally, similar to the standard graph …” 
- Page 8:
  - “We then evaluate or models … ” => “We then evaluate our model … ”

The experimental section lacks a comprehensive empirical study of the model. Comparisons of sampling and training times are important for understanding the model's performance, especially on very large graphs (>1000 nodes), which were not considered to prove the scalability.

### Questions
1. The absence of an appendix creates confusion regarding the model architecture and the specific use of PNa and FiLM. Could you provide more details to clarify these aspects?

2. In each call to the model during sampling, as explained in the third paragraph of section 3.4, do you update the edge list?

3. Given that this method is a sparse training form of DiGress, it's unclear why it demonstrates significantly improved generation performance in certain datasets over DiGress. Can you provide insights into the reasons behind this discrepancy?

4. Were the baseline models trained? The reported metrics for EDGE and HiGen on the Ego dataset appear inaccurate. Additionally, the high normalized MMD of Deg. for EDGE and DiGress in this case requires further explanation.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends DiGress to
 - use noise model that preserves sparsity during diffusion (although I believe this has been done in DiGress),
 - use a sparse transformer as the denoising model,
 - use a loss function computed on a subset of all pairs of nodes,

enabling training of DiGress on graphs up to 500 nodes. The complexity at sampling time, however, is still $O(N^2)$ due to having to predict the edge existence between every pair of nodes.

### Strengths
Diffusion models have shown great potential in graph generation. The issue of scalability in using diffusion model graph generation has been an open problem. This paper addresses that.

### Weaknesses
 - The contribution of the paper isn't small but the content of the contribution is somewhat trivial. The use of a sparse transformer is an immediate extension to DiGress. Preserving sparsity during diffusion to my knowledge has been done in DiGress.
 - Why the omission of GraphARM and SaGess in the large graph experiments? These two models seem to draw the most parallel comparison for being diffusion-based models with a concern for scalability. 
 - Many datasets that contain large graphs have a beta-like distribution: most graphs are small, few graphs are large, making dense training difficult. I'd like to see a study on the benefit of actually including such large graphs in training: can SparseDiff trained on large and small graphs outperform DiGress trained on small graphs, when the task is mostly to generate small graphs?

### Questions
See weaknesses

### Soundness
3 good

### Presentation
4 excellent

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
The paper proposes sparseDiff, there are three main contributions: (1) a noisy model that ensures sparsity is maintained during the diffusion process; (2) a sparse reverse prediction model that performs on a subset of the edge list; (3) an architecture improvement.

### Strengths
(1) the development of the model is clear, and the design of each component is demonstrated in full detail.

(2) The architectural design makes sense and convincing.

(3) related works are comprehensive.

### Weaknesses
 (1) the work is incremental -- the proposed noising process is just taken from DiGress, and the idea of performing sparse prediction at each denoising step is taken from EDGE. The paper does not adequately address how these components are adapted or improved for the specific task of sparse graph generation. It is not clear what novel insights are gained by combining these existing techniques.

(2) For the second point in (1), the paper claims that there is no guarantee that EDGE's degree-inform sampling always generates such a graph with an exact given degree. However, there is also no guarantee for SparseDiff that the uniform sampling method can learn to reverse the diffusion process. The uniform sampling strategy, while simple, may not be optimal for capturing the complex dependencies in graph structures. The paper lacks a theoretical justification or empirical evidence demonstrating that this approach is sufficient for learning the reverse process, especially when considering the potential for the model to converge to a sub-optimal solution. A more detailed analysis of the limitations of uniform sampling and its impact on the quality of generated graphs is needed. I suggest the author show that there is a proper lower bound of the model when using such reverse distribution.

(3) While SparseDiff advocates sparsity and efficiency, there is no time analysis. The paper should include a detailed analysis of the computational complexity of the proposed method, including both training and generation time. This analysis should compare SparseDiff's time complexity with that of other graph generation models, particularly those that also emphasize efficiency. Furthermore, empirical results on the actual training and generation time should be included for a comprehensive evaluation. I suggest the author should include such discussion theoretically and empirically.

(4) Some baselines are used in some datasets but not in others, can the authors explain why? Some results are not bolded correctly, for example, RBF MMD of SparseDiff in Ego is not significantly better than EDGE. For the table in D.6, DiGress has better RBFMMD than sparseDiff in the protein dataset and EDGE has better FID than sparseDiff in the Ego dataset, however, SparseDiff is bold for both cases. The inconsistent use of baselines and the incorrect highlighting of results raise concerns about the reliability of the experimental evaluation. A more rigorous and consistent experimental setup is needed to ensure a fair comparison between different methods.

(5) A larger dataset should be taken into consideration as the author claims scalability in the paper. Validating SparseDiff on QM9 does not support the motivation and the claims. The choice of datasets seems limited, and the paper does not adequately demonstrate the scalability of the proposed method to larger and more complex graphs. The inclusion of larger datasets would provide a more convincing validation of the scalability claims.

### Questions
See weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes SparseDiff, a diffusion-based deep method for graph generation. SparseDiff uses a message-passing graph transformer and random sampling of node pairs to compute its loss function, which allows it to exploit sparsity during the training phase. During sampling, the network repeatedly makes predictions on different subsets of node pairs until all possible edges are covered. Experiments on both small (molecular) datasets and large datasets (up to 500 node community graphs) indicate that the quality of graphs generated by SparseDiff is competitive with prior methods in both regimes.

### Strengths
- The paper's area of deep models for graph generation, especially diffusion models, has seen a lot of interest recently.
- The text is generally grammatical and clear.
- The core concept of sampling a fraction of node pairs to include in message-passing seems reasonable.

### Weaknesses
 - The paper's area of deep models for graph generation, especially diffusion models, has seen a lot of interest recently.
- The text is generally grammatical and clear.
- The core concept of sampling a fraction of node pairs to include in message-passing seems reasonable.

- The formatting, specifically the margins, may violate the guidelines. (Minor: citations also do not link properly when clicked.)
- There could be some discussion of exchangeability, which is concept related to the sampling of sparse graphs.
- Some notation is unclear, e.g., in the main equation on page 4, $\alpha^t$ and $\beta^t$ are not defined.
- The method is described in pieces across the text, decreasing clarity in my opinion; a step-by-step description of the algorithm is deferred to the appendix.
- There is no theoretical guarantee/characterization of the generative model's capability.
- If I have not misunderstood something, the method can only create discrete node/edge features. Also, as the authors note, the proposed method's sampling complexity scales quadratically in the number of nodes, so it does not scale to very large graphs. However, as they also note, this may be necessary without assumptions about the data distribution.

Typos
- page 4: quotation marks around "no edge"
- page 4: "markovian" uncapitalized
- page 9: "SparseDiff comparable"

### Questions
- Is it true that the proposed method cannot create continuous (non-categorical) node/edge features?
- "In this work, we choose to use the marginal transitions as they are supported by theoretical analysis." Could you expand on this?
- On page 7, it is noted that the method is designed to avoid distribution shifts involving predictions on the computational graphs. One vague question this raised for me is why it is then possible to exploit sparsity only during the training phase. Is the network during training not being trained to predict "non-edge" for the appropriate node pairs? Does this also constitute a distribution shift?
- To clarify what exactly the method is, I would recommend breaking out the training and sampling procedures into algorithms outside the text. There seems to be an algorithm given for the sampling procedure in the appendix, which could maybe be moved to the main paper with the space saved from fixing the margins. Ideally that algorithm could be written in a more self-contained way

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
