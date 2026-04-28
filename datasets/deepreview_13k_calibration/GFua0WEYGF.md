# Provable optimal transport with transformers: The essence of depth and prompt engineering

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Can we establish provable performance guarantees for transformers? Establishing such theoretical guarantees is a milestone in developing trustworthy generative AI. In this paper, we take a step toward addressing this question by focusing on optimal transport, a fundamental problem at the intersection of combinatorial and continuous optimization. Leveraging the computational power of attention layers, we prove that a transformer with fixed parameters can effectively solve the optimal transport problem in Wasserstein-2 with entropic regularization for an arbitrary number of points. Consequently, the transformer can sort lists of arbitrary sizes up to an approximation factor. Our results rely on an engineered prompt that enables the transformer to implement gradient descent with adaptive stepsizes on the dual optimal transport. Combining the convergence analysis of gradient descent with Sinkhorn dynamics, we establish an explicit approximation bound for optimal transport with transformers, which improves as depth increases. Our findings provide novel insights into the essence of prompt engineering and depth for solving optimal transport. In particular, \emph{prompt engineering} boosts the algorithmic expressivity of transformers, allowing them implement an optimization method. 
With \emph{increasing depth}, transformers can simulate several iterations of  gradient descent.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This article constructs a prompt that enables transformers to perform gradient descent on dual optimal transport. Additionally, it provides an explicit approximation bound that improves with increasing depth. These results offer guarantees for the effectiveness of transformers in solving the optimal transport problem.

### Strengths
This paper introduces a novel inquiry into whether transformers can effectively implement optimal transport. Additionally, the construction is independent of the number points, and can be used to solve optimal transport problems of different scales.

### Weaknesses
 - The experiments in Section 6 only evaluate constructed transformers. However, it remains unclear whether training standard transformers can achieve the solutions constructed in the theory.

- Lines 375 to 384 in Section 5 and lines 479 to 483 in Section 6 imply that attention patterns maintain full rank. This assertion contradicts to the commonly observed phenomenon in practice, where attention matrices are highly low-rank and sparse. 

- The proof is based on the constructuion, so the required depth is only a sufficient condition. The required depth is presented as a sufficient theoretical condition but does not preclude the possibility that shallower transformers may also effectively perform optimal transport.

- Although this paper focuses on a novel task (optimal transport), the primary proof idea is similar to that of many previous works: using multi-layer transformers to simulate multi-step GD iterations.

### Questions
- Could the authors construct transformers with low-rank and sparse attention matrices, which can also effectively implement optimal transport?
- I am interested in the insights derived from the prompt construction, and the paper would benefit from a more detailed discussion on this topic.

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
2

### Summary
This investigates whether transformers can provide theoretical guarantees in solving the Sinkhorn optimal transport problem. The authors demonstrate that transformers, equipped with appropriately engineered prompts, can approximate optimal transport solutions by leveraging attention layers and simulating gradient descent with adaptive step sizes.

The authors designed prompts to aid transformers in solving optimal transport by providing the required memory and statistics within the model's layers. This setup helps in implementing gradient descent and enables transformers to handle various problem instances efficiently.

The study finds that the performance of transformers in solving optimal transport improves with increased depth, establishing an explicit approximation bound that converges as the model’s depth increases.

Sorting is shown as a special one-dimensional case of optimal transport, where transformers can approximate the sorted output by solving the transport problem. The experiments validate the theoretical predictions, showing that transformers can effectively approximate sorted sequences.

The paper rigorously proves that attention matrices in transformers can converge to a doubly stochastic matrix that approximates the optimal transport solution. This convergence avoids rank collapse, a common issue in attention layers, thus preserving the expressiveness of transformers.

### Strengths
Originality

The paper is original in its approach to connecting transformers with provable guarantees in solving the Sinkhorn OT problem. It leverages the attention mechanism of transformers in an innovative way, showing that transformers can approximate optimal transport solutions under entropic regularization.

Quality

The paper is rigorous in both its mathematical formalism and experimental validation. The theoretical development is well-supported by proofs, such as the gradient descent simulation using attention layers and the convergence analysis of attention matrices. 

Clarity

The paper generally communicates complex ideas effectively, with clear explanations of both the background and the transformer mechanics used in OT tasks. All proofs are included in the main paper. 

Significance

Theoretically, it provides new insights into how transformers can function beyond sequence modeling, linking them to iterative optimization methods such as gradient descent. This connection strengthens the iterative inference hypothesis, suggesting transformers can perform complex tasks in optimization by layer-wise refinement.

### Weaknesses
1. The paper's theoretical proofs are presented with a high level of mathematical density that may hinder accessibility for a broader audience, particularly readers less familiar with optimization theory or transformers' inner workings. To improve accessibility, the authors could add intermediate explanations or visual aids (such as flowcharts or diagrams) to clarify the key steps in the proofs. An appendix with expanded explanations of some technical choices and motivations, particularly around the parameter settings in Section 4, could further aid comprehension.

2. Prompt engineering is a significant aspect of the paper’s contribution, especially given its role in facilitating the transformer’s ability to approximate the optimal transport problem. However, the authors do not fully explore the sensitivity or robustness of their prompt design. For example, it is unclear if minor variations in the prompt structure or parameters would significantly impact the model's performance in solving OT, which is crucial for understanding the generalizability of this approach. Adding a sensitivity analysis that examines the impact of slight prompt modifications on performance would strengthen the prompt engineering component.

3. The experiments are relatively limited, focusing primarily on simple sorting tasks. For example, demonstrating performance on high-dimensional OT tasks, even with a modest dimensionality (e.g.,  𝑑=10), would provide valuable insights into the approach's scalability and robustness.  A head-to-head comparison with other OT algorithms (e.g., Sinkhorn or linear programming methods) on shared metrics (e.g., accuracy, runtime, or scalability) would provide a clearer picture of where the transformer-based approach stands.

4. This paper focuses on using transformers for OT.  How this framework could extend to broader optimization or machine learning problems?

### Questions
see weaknesses.

### Soundness
3

### Presentation
2

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
The paper addresses the problem of theoretical guarantees of solving the entropic optimal transport (EOT) in the context of Wasserstein-2 distance using transformers. The authors provide theoretical assurance by demonstrating that transformers when equipped with specific prompts perform gradient descent on the dual formulation of the EOT problem.  The key contributions include proving that transformers with fixed parameters can implement gradient descent on the Wasserstein-2 EOT problem and establishing the error bound for this approach. The experimental results further demonstrate the ability of transformers with specific prompts to sort lists of numbers supporting the theoretical findings.

**Post rebuttal**: Score increase 3->6, see the discussion.

### Strengths
The paper is rigorously constructed, demonstrating strong theoretical foundations, and supporting their claims of transformers being able to conduct gradient descent on optimal transport problems with explicit error bounds and convergence metrics. While there is a lack of available experiments specifically related to optimal transport, the authors find a way around this limitation by conducting experiments on sorting and optimal transport for different input sizes, which validate the theoretical assertions and strengthen the quality and reliability of the paper's contributions.

### Weaknesses
 **Missing Generalization**. The authors establish a link between transformers and optimal transport, providing a specific and *very artificial* construction. While the choice of parameters, architecture, and prompts is justifiable within this framework, the construction remains limited, as there is no exploration beyond these specific Optimal Transport (OT) costs or an attempt to generalize the findings. Different applications and data types may require distinct cost functions to accurately reflect the underlying transport dynamics; for instance, a Manhattan cost better represents routing scenarios in transportation logistics, while a Gaussian cost can effectively model probabilistic asset movements in finance. By restricting their focus to specific OT costs, the authors miss potentially new application insights in the research field.

**Limited Scope**. Numerous studies [1], [2], [3] are bridging the gap between the capabilities of transformer models in artificial scenarios and their performance in real-world learning tasks, which is crucial for a comprehensive understanding of in-context learning. While the authors successfully establish a connection between transformers and optimal transport, they neglect to address whether these models are genuinely capable of solving optimal transport problems when trained in real-world scenarios. This omission limits the depth of their analysis and may hinder the reader's ability to fully grasp the implications of their findings within practical contexts. A discussion on this point would significantly enhance the paper’s contribution to the field.

[1] Von Oswald, Johannes, et al. "Transformers learn in-context by gradient descent." International Conference on Machine Learning. PMLR, 2023.

[2] Akyürek, Ekin, et al. "What learning algorithm is in-context learning? investigations with linear models." arXiv preprint arXiv:2211.15661 (2022).

[3] Wang, Jiuqi, et al. "Transformers Learn Temporal Difference Methods for In-Context Reinforcement Learning." arXiv preprint arXiv:2405.13861 (2024).

**Mistakes in Equations**. The equations contain several errors that make it difficult to follow the logical flow of the proofs. Some examples include: 
- at line 241 the definition of $\lambda Q^{(l, 1)}$ contains excessive $\mathbf{0}{d'}$ vector at the end; 
- at line 241 and 242 vectors $e{2d+5}$ in both definitions of $\lambda Q^{(l, 1)}$ and $\lambda Q^{(l, 2)}$  must be moved more left to get additional term $v^{(l)}$ or $u^{(l)}$ in the equation at line 291; 
- at line 275 the iteration index of $Z$ has to be $(l+1)$; 
- at line 286 some of the zeros must be zero vectors or matrix; 
- at 291 the $\lambda$ is missing and, additionally, the expression for the upper left block is wrong; 
- at line 304 there must not bee coefficient $\gamma$, instead it should be moved to line 309. 

These errors disrupt the coherence of the mathematical arguments and create unnecessary confusion. Carefully revising each equation to ensure consistency and accuracy would significantly enhance readability and strengthen the rigor of the presentation.

**Late or Missing Introduction of Notation or Definitions**. Notation is often introduced at various points of the paper, making it challenging for readers to locate definitions or fully understand terms when they first appear. In some cases, notation seems to be used without any prior introduction, leaving readers to infer meanings from context, which reduces the accessibility of the theoretical sections. It was mentioned:

- at line 202 the meaning of the subscript of $[Z^{(l)}_n]$ is not defined clearly;
- at line 299 it is not seen that this matrix is attention matrix $A$;
- at line 286 and 291 is used different notation of $[||x_1||^2, \dots, ||x_n||^2]$, $||x||^2$ and $x^2$;
there is no clear evidence of whether column or row vector notation is used;
- at line 237 authors introduce $d' = 2d + 9$ but they still use $2d + 9$ in lines 267, 275. 

*Suggestion:* A more effective approach would be to introduce all key notations systematically in a dedicated section at the beginning of the paper. Alternatively, providing a table summarizing all notations and definitions, with clear explanations and references to where they are first used, would help readers navigate the mathematical content more easily.

**Difficulty in Understanding Matrix Derivations.** In several parts of the paper, it is challenging to follow the derivation, for example, in lines 291 or 308. The transitions from definitions to their matrix forms are often abrupt, leaving readers uncertain about how certain matrices are constructed or why they take particular forms. In several instances like in lines 291, 304, 309, and 314, the dimensions of matrices are not specified, which is crucial for notation with blocks.

*Suggestion:* To improve clarity, consider adding more intermediate steps in the Appendix. Providing explicit dimensions for each matrix upon introduction would make it easier for readers to follow matrix operations. Including dimensions directly in matrix definitions or accompanying explanations would also help readers track the flow of derivations and verify the correctness of matrix manipulations.

### Questions
To strengthen the paper, please consider:

- consider bridging the gap between whether transformers can perform gradient descent on optimal transport tasks and whether they
- conduct it in real-world scenarios;
- consider different OT  costs;
- adding more intermediate steps of matrix derivations in the Appendix;
- including dimensions directly in matrix definitions and accompanying explanations;
- extending notation section with more notations that are used in main sections;
- fixing mentioned mistakes;
- including a section that explicitly discusses the relevance of optimal transport theory to transformer models, explaining how this perspective can lead to new insights into the mechanics.

### Soundness
4

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proves the existence of a transformer which takes as an input a collection of points $(x_1,y_1, \dots, x_n,y_n),$ in $\mathbb{R}^d$ and outputs an approximate solution to the optimal transport matching problem between the sets of points. Their proof relies uses an explicit construction of a transformer which unrolls the gradient descent algorithm on the entropic-regularized OT problem for the dual potentials, and which takes a specifically-engineered prompt as an input. The convexity of the dual OT problem then implies a bound between the transformer output and the optimal coupling, which decreases as the depth of the transformer increases. Their result adds further evidence to the burgeoning interpretation of transformers as algorithm-learners.

### Strengths
1. The paper provides guarantees for a broad class of discrete OT problems, which arise in a variety of applied fields.
2. The main results are supported by rigorous proofs, which are correct to the best of my knowledge.

### Weaknesses
1. The idea of using transformers to unroll gradient descent algorithms is not new in the theory literature, it has been studied in [1], [2], and [3] extensively. In light of those results, it doesn't seem very surprising that you can also construct a transformer to unroll GD for the optimal transport loss. Furthermore, the specific architecture used here, with softmax attention, is not a direct implementation of gradient descent, but rather a variant with adaptive step sizes that depend on the current dual variables. This deviation from standard gradient descent, while perhaps necessary for the proof, raises questions about the practical relevance of the construction.
2. The paper only bounds the approximation error of using transformers to solve OT problems and ignores other sources of error such as the pre-training generalization error and the training error of the transformer parameters. This is a significant limitation, as the theoretical guarantees do not account for the practical challenges of training such a transformer. The analysis also does not consider the impact of the specific choice of the prompt on the final solution, and whether the engineered prompt is optimal or if a learned prompt could lead to better performance. It is unclear if the specific prompt is necessary for the theoretical guarantees or if it is an artifact of the proof technique.

### Questions
1. I think it would be helpful to comment on the choice of the adaptive step size in Theorem 1. My guess is that this is an artifact of using softmax attention, as it is difficult to express the gradients of the loss in terms of the softmax normalization. But it still seems strange that the step sizes depend on the parameters $u$ and $v$ which are being updated, as then it does not seem as though the transformer layers are really performing gradient descent. Does this affect the convergence of the transformer output to the true OT matrix? 
2. In your experiments, how does the prediction of the trained transformer compare to the solution obtained by running gradient descent on the dual OT loss?
3. Is your specific prompt engineering important for the numerics? Clearly it plays a central role in the proof. However, I would expect that you could first apply a learnable feature map to the original prompt and then apply attention to the featurized prompt and obtain similar results (i.e, make the prompt engineering learnable).

### Soundness
3

### Presentation
2

### Contribution
2
