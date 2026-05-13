# Learning Dispersed Embeddings on Hyperspheres

- Decision: Reject
- Scores: 5, 5, 5, 6, 5

## Abstract
Learning well-separated features in high-dimensional spaces, such as text or image $\textit{embeddings}$, is crucial for many machine learning applications. Achieving such separation can be effectively accomplished through the $\textit{dispersion}$ of embeddings, where unrelated vectors are pushed apart as much as possible. By constraining features to be on a $\textit{hypersphere}$, we can connect dispersion to well-studied problems in mathematics and physics, where optimal solutions are known for limited low-dimensional cases. However, in representation learning we typically deal with a large number of features in high-dimensional space, which makes leveraging existing theoretical and numerical solutions impossible. Therefore, we rely on gradient-based methods to approximate the optimal dispersion on a hypersphere. In this work, we first give an overview of existing methods from disconnected literature. Next, we propose new reinterpretations of known methods, namely Maximum Mean Discrepancy (MMD) and Lloyd’s relaxation algorithm. Finally, we derive a novel dispersion method that directly exploits properties of the hypersphere. Our experiments show the importance of dispersion in image classification and natural language processing tasks, and how algorithms exhibit different trade-offs in different regimes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper compares different methods to compute dispersed embeddings in the hypersphere. This amounts to solving the "Tammes problem" in the hypersphere which is relevant to many applications. It first introduces a panorama of the different existing approaches  before benchmarking them on various tasks.

### Strengths
- Computing dispersed embeddings on the hypersphere is a highly relevant problem for the representation learning community.
- The review presented at the beginning of the paper is informative.
- The authors explore a variety of settings in their experiments.

### Weaknesses
 - Overall, I find the paper somewhat disorganized, which makes it challenging to identify the authors' unique contributions. These new insights should be more clearly highlighted in contrast to previous work.

- Section 2 feels more like a catalog of methods without adequate comparison. There isn't a clear progression that clarifies the rationale or direction. For example, why is max-min considered superior to MMD? Additionally, there should be an evident relationship between Differential Entropy Dispersion and MMD projection with uniform distribution. Emphasizing this connection would add valuable insight.

- The clarity of this paper could be significantly improved by stating the objective of each subsection at the beginning and explaining its relevance within the overall context of the paper.

- While the experimental section is diverse, it’s challenging to understand which method the authors recommend. Providing more practical guidelines for practitioners on what works best would be helpful. For example, why does the sliced method perform well in Neural Machine Translation (NMT) but not in prototype-based image classification?

### Questions
- Could the authors elaborate on the motivation for using Riemannian optimization over projections?

- Did the authors consider conducting experiments with self-supervised computer vision models, where representation learning on the hypersphere is common?

- Typo: "dipsersion" should be corrected to "dispersion" on line 372.

### Soundness
3

### Presentation
2

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
This paper gives an overview of dispersed embedding. This latter encourages spreading out a large amount of high-dimensional embedding vectors on the surface of the $d$-dimensional unit hypersphere by maximization of the angular angle between any two points. The authors study several dispersion objectives for the nit hypersphere. Then they propose a sliced dispersion version that exploits the geometrical property of the hypersphere.

### Strengths
- The paper overviews several measures of embedding dispersion and introduces the Lloyd and Sliced dispersions. 
- The authors test the given objectives on synthetic embedding illustrating Tammes problem,  then on image classification with prototypes, and finally on neural machine translation through large-scale text embedding datasets.

### Weaknesses
 - According to Lemma 2 and Proposition 1, the projection is with respect to two slicing directions $p,q$ on the hypersphere. Empirically, is there any order $L$ of the cardinal of these directions? I mean how many projections are needed to guarantee maximum data dispersion? Specifically, while the expectation over all possible great circles is theoretically sound, the practical implementation relies on sampling. The paper should provide more clarity on how the number of sampled directions affects the quality of the dispersion, and whether there's a point of diminishing returns.
- Does the target dimension $d$ belong to the set of hyperparameters. It is unclear how the choice of the target dimension $d$ impacts the performance of the proposed method. The paper should include a discussion on the sensitivity of the results to different values of $d$, and provide guidelines for selecting an appropriate value for different datasets.
- The optimization algorithm is structured with respect to Riemannian optimization (RO) tools. Can you highlight the benefits of RO in the learning process? The paper should elaborate on why Riemannian optimization is necessary for this problem, and what advantages it offers over standard Euclidean optimization techniques. For instance, does RO help avoid local minima or improve convergence speed? A more detailed explanation is needed to justify the choice of RO.
- The paper is fully empirical which is certainly important to showcase the benefits of sliced dispersion over the SOTA approaches. However,  I think it lacks some theoretical insights in comparison with respect to euclidean baselines. The paper needs to provide a theoretical analysis of why sliced dispersion is expected to perform better than Euclidean-based methods. For example, can the authors provide any guarantees on the convergence of the proposed method, or any bounds on the dispersion achieved?

### Questions
See Weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors investiage representation learning constrained to the sphere, a formulation that is often used in ML approaches.  They introduce some new ways to optimize loss functions and benchmark some approaches.

### Strengths
The problem is clearly stated and the motivation is easy to understand.  The paper seems well written and the authors are familiar with theory related work papers.

I find the paper well written and the structure is easy to follow.

Overall I quite like the paper, although I am under the impression that it needs more work

### Weaknesses
I appreciate the evaluation, but as it stands it is a bit lacking.  It would be good to show similar related approaches such as SimCLR for the imagenet classification task.  Also, the improvements seem really minor compared to even their own baseline.  On the one hand that is good because supposedly all of the optimizers accomplish the same goal.  On the other hand, it begs the question of why is it useful to use one optimizer over another.  And what is the value proposition of using Riemannian optimization (Bonnabel, 2013; Becigneul & Ganea, 2019)?

There are no repeated runs for the experiments and there is no mention of whether this will holds.  I would like to see some added runs that can then be summarized as mean +- std to give a better idea of how robust the results are.  Especially since the improvements appear quite marginal, this would strengthen the paper in my opinion.

- The authors cite Wang and Isola (2020) but they make no mention of contrastive learning, which (esp. in Chen et al., 2020) also optimizes an embedding on the hypersphere.  Perhaps the authors wish to comment or include this into their benchmark of ImageNet classification?
- What do the different options for optimization bring to the table?  After reading through the paper this is not fully clear to me.
- Why do you take the «Euclidean» representation learned by a transformer and normalize it to a hypersphere?  Would you not expect this to lead to worse results?
- For Figure 1 and 5, the random initialization seems to always get one of the best results in at least some of the cases.  I find this surprising.  Does it mean that the task can be easily solved with a proper initialization?
- Related to the previous bullet point:  Were the random initializations used for further training?  Because it seems that in Fig. 1 the best metric was actually achieved with a random init.  I would expect the optimizers to not decrease the performance, yet they seem to do so.  Can you explain this?

### Questions
- The authors cite Wang and Isola (2020) but they make no mention of contrastive learning, which (esp. in Chen et al., 2020) also optimizes an embedding on the hypersphere.  Perhaps the authors wish to comment or include this into their benchmark of ImageNet classification?
- What do the different options for optimization bring to the table?  After reading through the paper this is not fully clear to me.
- Why do you take the «Euclidean» representation learned by a transformer and normalize it to a hypersphere?  Would you not expect this to lead to worse results?
- For Figure 1 and 5, the random initialization seems to always get one of the best results in at least some of the cases.  I find this surprising.  Does it mean that the task can be easily solved with a proper initialization?
- Related to the previous bullet point:  Were the random initializations used for further training?  Because it seems that in Fig. 1 the best metric was actually achieved with a random init.  I would expect the optimizers to not decrease the performance, yet they seem to do so.  Can you explain this?

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
2

### Summary
The author(s) bridged the gap between the theory of linear separation through the dispersion of embeddings and its application to the high dimensional problem. They introduced a gradient-based method to approximate the optimal dispersion on a hypersphere. They made a systematically comparison of two methods: Lloyd and Sliced.

### Strengths
The paper clearly defined dispersion on the hypersphere and provided two methods for the approximation. They compared the methods on various applications under different metrics. They novelly used Riemannian optimization on the hypersphere to achieve dispersion. The improvement on the classification and neural machine translation problem seems promising.

### Weaknesses
The paper attempts to optimize the dispersion on the hypersphere but it lacks the justification and discussion why the gradient-based method leads to an optimal dispersion (line 016) in high dimensional space. The authors propose a gradient-based approach to approximate the optimal dispersion, but the paper does not delve into the theoretical underpinnings of why this method converges to a good solution, especially given the non-convex nature of the problem. The paper also lacks a discussion on the potential for the gradient-based method to get stuck in local optima, and how this might impact the quality of the dispersion achieved. Furthermore, while the authors use metrics like circular variance and minimum distance to quantify dispersion, there is no clear explanation of how these metrics directly relate to the performance improvements observed in downstream tasks.

### Questions
I think the evidence in the numerical experiments supports the improvement made by the dispersion optimization. Could author(s) provide some justifications on how much the dispersion on the hypersphere is related to the improved performance in different tasks? The overall improvement on all of the tasks seems to indicate a great essential improvement on the theory of the method regardless the task (image classification, neural machine translation)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes methods to improve the spatial separation of high-dimensional embeddings by constraining them to lie on a hypersphere. This separation helps prevent clustering of unrelated embeddings, which can degrade performance in machine learning tasks. The authors reinterpret existing techniques, such as Maximum Mean Discrepancy (MMD) and Lloyd’s algorithm, for dispersing embeddings and propose a novel sliced dispersion method that leverages hyperspherical geometry.

### Strengths
1. The paper is well-structured and written in a way that makes it accessible to a broad audience.
2. The background section provides a concise yet thorough summary of relevant literature, including essential mathematical concepts and previous approaches. 
3. The experimental evaluation covers a wide range of tasks. The authors evaluate their methods on synthetic data, image classification tasks, and machine translation.

### Weaknesses
1. There is little relationship between the background and the proposed methods. It would be beneficial if the authors provided more insights into the proposed sliced dispersion. Specifically, the connection between the reinterpretation of MMD and Lloyd's algorithm and the novel sliced dispersion method is not clearly established. The paper would benefit from a more detailed explanation of how these existing techniques motivate the proposed approach, and what specific limitations of those methods the sliced dispersion is designed to overcome.
2. The training time for empirical datasets is not reported. Given the marginal improvements in image classification and neural machine translation, it would be helpful to understand how the time cost balances against the performance gains. The lack of this information makes it difficult to assess the practical utility of the proposed method. For example, if the sliced dispersion method requires significantly more training time than existing methods, the marginal performance gains might not be worth the additional computational cost. A detailed comparison of training times, along with memory requirements, would be essential for a thorough evaluation.

### Questions
1. Correct me if I’m wrong, but by minimizing  L_{sliced} , the authors are attempting to find the optimal great circle  S_{pq}  that aligns with the input  X . How does this improve spatial distribution if the samples are on a lower-rank circle?
2. Visualizing the results from Section 3.1 in 3D space and analyzing how each metric affects the distribution would be valuable.

### Soundness
3

### Presentation
3

### Contribution
2
