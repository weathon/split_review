# NeuroLifting: Neural Inference on Markov Random Fields at Scale

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
Inference in large-scale Markov Random Fields (MRFs) is a critical yet challenging task, traditionally approached through approximate methods like belief propagation and mean field, or exact methods such as the Toulbar2 solver. These strategies often fail to strike an optimal balance between efficiency and solution quality, particularly as the problem scale increases. This paper introduces \textsc{\textsc{NeuroLifting}}, a novel technique that leverages Graph Neural Networks (GNNs) to reparameterize decision variables in MRFs, facilitating the use of standard gradient descent optimization. By extending traditional lifting techniques into a non-parametric neural network framework, \textsc{NeuroLifting} benefits from the smooth loss landscape of neural networks, enabling efficient and parallelizable optimization. Empirical results demonstrate that, on moderate scales, \textsc{NeuroLifting} performs very close to the exact solver Toulbar2 in terms of solution quality, significantly surpassing existing approximate methods. Notably, on large-scale MRFs, \textsc{NeuroLifting} delivers superior solution quality against all baselines, as well as exhibiting linear computational complexity growth. This work presents a significant advancement in MRF inference, offering a scalable and effective solution for large-scale problems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a GNN based approach to approximate MAP inference in MRFs.  The contribution definitely follows recent trends in trying to use NNs to approximately solve hard problems, it falls a bit short in its treatment of historical work and references to modern approaches.  Overall, the presentation needs quite a bit of improvement.

### Strengths
- The proposed approach is a novel combination of optimization ideas with modern NN approaches.

- The authors provide a wide array of experimental results across different domains and both synthetic and real data.

### Weaknesses
 - Some of the text looks like it was fed into an MRF for "improvement," but it reads a bit awkwardly and uses imprecise statements.  Even if this isn't the case, I would suggest tidying it up a bit so as to make it read more like a traditional technical paper.

- The descriptions of MRFs and related work is poor.  Some parts of the discussion make it seems like some of the ideas being presented are novel to the community when they aren't really.  For example, the authors define MRFs factorizing over the cliques of a graphs and then claim novel insights that these cliques can be subdivided into edges when representing the graph.  This is, of course, what it means to be a clique in a graph.  Equation (4) isn't the standard loopy BP representation where inference is no longer exact (it isn't even clear why you need this formula anyway).  Saying that message passing looks like GNNs when it is in fact the other way around by design. Among many others.

- Some of the decisions made in the setup, e.g., the padding seem like that could lead to poor results in practice.  There is a comment about this in the paper, but the chosen method seems significantly suboptimal to me especially when the range of values that each potential function can take is small.

### Questions
- Figure 1 is really difficult to understand.  

- I don't love calling this approach NeuroLifting because the are already "lifted" methods in relational MRFs.  I'm not sure what else I would call this, but given the long history in that domain optimization lifting strategies are not the first things that come to my mind when I hear the name.  Equation (6) is quite similar to traditional MAP relaxations (some of which are actually cited).  Saying

- Can you further explain the issues that arise with padding?  It seems clear that padding essentially with infinities is the correct theoretical thing to do -- what is the practical issue here?

- Lots of references should probably be added.  Here's one that is somewhat related to help get you started:

Arya, S., Rahman, T. &amp; Gogate, V.. (2024). Learning to Solve the Constrained Most Probable Explanation Task in Probabilistic Graphical Models. <i>Proceedings of The 27th International Conference on Artificial Intelligence and Statistics</i>, in <i>Proceedings of Machine Learning Research</i> 238:2791-2799 Available from https://proceedings.mlr.press/v238/arya24b.html.

### Soundness
3

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
2

### Summary
The paper introduces NEUROLIFTING, a novel inference method that leverages Graph Neural Networks (GNNs) to optimize decision variables in large-scale MRFs. in contrast traditional methods, such as belief propagation and Toulbar2, which struggles to balance efficiency and solution quality as MRFs scale, NEUROLIFTING reparameterizes MRF variables with GNNs which enables efficient optimization using gradient descent while taking advantage of the smooth neural network landscape. This approach shows competitive results against exact solvers on smaller problems and superior performance on larger ones, with linear computational complexity growth.

### Strengths
* NEUROLIFTING introduces a new way to approach MRF inference by incorporating GNNs, enhancing scalability and parallelism compared to traditional methods.

*  Empirical results indicate that NEUROLIFTING consistently outperforms approximate inference methods in terms of solution quality and closely matches exact solvers on smaller instances.

*  The model shows linear growth in computational complexity, making it well-suited for large-scale MRFs.

* The method effectively transforms high-order graphs into a GNN-compatible format, expanding its applicability across various MRF-based problems.

### Weaknesses
 * The use of GNNs, especially for large graphs, may still introduce significant computational costs and memory requirements, potentially limiting applicability in extremely large or resource-constrained environments.

* The effectiveness of NEUROLIFTING could be sensitive to the choice of GNN architecture, number of layers, and feature dimensions, which might require extensive tuning.

* Although NEUROLIFTING outperforms existing methods on large problems, there may be cases where it still falls short of the accuracy provided by exact solvers, especially on smaller and well-structured graphs.

### Questions
1. How sensitive is NEUROLIFTING's performance to different GNN architectures and hyperparameters? Can it be generalized across various MRF problems without extensive tuning?

2. How does the model perform on MRF instances with unique or less common graph structures that differ significantly from those used in the empirical tests?

3. Are there alternative ways to optimize the energy function or refine the padding strategy to further enhance efficiency or solution quality?

4. Could the NEUROLIFTING framework be extended to handle dynamic graphs or incorporate temporal information for applications in time-varying MRFs?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper focuses on the inference in large-scale Markov Random Fields (MRF), where conventional methods often suffer from either efficiency or solution accuracy. To address this issue, this paper advocates mapping the inference of MRF to a Graph Neural Networks (GNNs), which enables smooth loss landscape and scalable inference. Numerical experiments on several datasets showcases that the proposed NeuroLifting presents comparable performance to the non-scalable exact solver Toulbar2.

### Strengths
1. The organization of this paper is clear, and the writing is easy to understand. 

2. The figures and the example provided in figure 1 are helpful for understanding the paper.

### Weaknesses
Several parts of the paper are confusing, as listed one-by-one below. 

1. When introducing Lifting in Section 2, it is stated that "Lifting reformulates an optimization problem into a more tractable form by introducing auxiliary variables or constraints, making the optimal solutions more accessible." However in Section 3.3, the high-dimensional feature vectors are learnable and randomly initialized, without any guarantee on the equivalence between the original problem and the alternative GNN optimization problem. It would be beneficial if some theoretical analysis can be provided to ensure the GNN is actually/approximately solving the original problem, or an equivalent problem. In the current version, there is not even an objective function for the alternative optimization problem, making it hard to connect this paper with "Lifting". Specifically, the paper lacks a clear explanation of how the GNN's learned representation relates to the original MRF's energy function, and how minimizing the GNN's loss function translates to finding a good solution for the MRF problem. The absence of a formal connection between the GNN's optimization landscape and the MRF's energy landscape is a significant gap. For instance, it is unclear whether the GNN is learning a surrogate energy function or a mapping that directly yields the optimal MRF configuration. Without this, the claim of "Lifting" is not well-supported.

2. This paper claims that NeuroLifting is a "non-parametric" method. Nevertheless, line 249 argued that "we optimize both the GNN parameters and those of the encoder," which conflicts with the proceeding claim. The use of learnable parameters within the GNN architecture, such as weights and biases in the neural network layers, directly contradicts the notion of a non-parametric model. A non-parametric method, by definition, does not rely on a fixed set of parameters. The GNN's architecture, with its defined layers and activation functions, imposes a specific functional form, which is characteristic of parametric models. The claim of non-parametricity is therefore misleading and needs to be revised.

3. Line 61 says that NeuroLifting "outperforms all existing approximate inference strategies in terms of solution quality without sacrificing computational efficiency." In the experiments, only the time limit for the exact solver Toulbar2 is reported, while it is unclear how NeuroLifting compares to conventional approaches in terms of both time and space complexities. The lack of a direct comparison with other approximate inference methods, such as belief propagation or loopy belief propagation, makes it impossible to validate the claim of superior performance. The paper should include a thorough analysis of the time and space complexities of NeuroLifting, as well as a comparison with existing approximate inference algorithms. The absence of such analysis makes the claim of outperforming existing methods unsubstantiated.

4. No codes or supplementary files are provided along with the submission. As a result, the reviewers cannot verify the results reported in the manuscript. 

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates approximating Markov random fields (MRF) by optimizing a graph neural network (GNN) to maximize a surrogate to its joint density. 
It suggests using learnable padded embeddings of the MRF decision variables as GNN features, allowing gradient-based optimization. 
The paper claims that:
 1. It is the first to introduce neural network-based lifting to MRF inference.
 2. The approach, called NeuroLifting, simplifies the optimization process for large MRFs.
 3. Loss computation with NeuroLifing scales linearly with the MRF nodes and enables parallelization and GPUs accelerated computation.
 4. It empirically demonstrates that NeuraLifing finds near-optimal solutions on moderate-size MRFs and solutions superior to baselines on large MRFs.

### Strengths
- The central idea of embedding decision variables in an MRF to use a GNN is original.
- The selection of GraphSAGE for convolution is well justified and supported by empirical results (Figure 3).

### Weaknesses
## Reasons for score
- The abstract states that NeuroLifing "delivers superior solution quality against all baselines" on large-scale MRFs. However, Table 1 does not show this, and two baselines (LBP and TRBP) need to be included in Table 2. Please consider modifying the abstract to reflect your results better. For example, you could restrict your claim to Toulbar2, i.e., exact methods.
- The experimental results lack standard error estimation, which makes method comparison difficult because it's hard to judge the significance of the difference in energy. Considering your method is probabilistic, you could use multiple initializations to estimate the standard error.
- A convergence criterion needs to be clearly stated for NeuroLifting UAI22 dataset.
- Related work is delegated to the appendix.
- It needs to be clarified whether NeuroLifing is guaranteed to produce a valid solution. In particular,
  - Please explain how the padding scheme suggested produces only valid solutions, but padding with the largest of all energies can produce infeasible solutions.
  - Please explain with evidence (either theoretical or empirical) how the rounding scheme for $p_i(\theta)$ avoids multi-assignment issues.

### questions:
 1. Does a GNN with jumping knowledge preserve the Markov assumption?
  2. Why does Table 2 not include LBP and TRBP?
  3. Was a hard time constraint of 1200 seconds enforced for LBP, TRBP and NeuroLifing?
  4. Is NeuroLifing sensitive to the initialization of the embeddings and network?
  5. Why does Toulbar2 fail on H_Instances_2?
  6. Table 1 reports "the final loss given by the loss function," whereas the other tables report the final energy. It needs to be clarified that the distinction between loss and energy exists for the baseline methods. If so, what is the gap between loss and energy?
  7. What is the gap between loss and energy for NeuroLifting on synthetic, UAI and PCI?
  8. The interpretation of the linear complexity needs to be clarified. By mentioning the linear complexity in node size, is the paper claiming an asymptotic improvement over alternatives?
  9. How does the suggested padding scheme produce only valid solutions, whereas padding with the largest of all energies can produce infeasible solutions?
  10. How does the rouding scheme for $p_i(\theta)$ avoid multi-assignment issues?
  11. What does "showing remarkable scalability and efficiency" mean in (lines 71-72)? What is the concrete evidence that shows this claim?
  12. What stopping criteria are used for NeuroLifting on UAI?

##  Minor comments (did not affect score)
  1. Tables 1, 2, 3 and 4 would be more legible and convey the same results if reported as whole numbers instead.
  2. Capitalize the titles of the references.
  3. Use only one of: `DOI:`, `ISBN` or neither for book references.
  4. The caption for Figure 1 should describe the stages in the diagram. Figure 2 does this well.
  5. In Figure 1 $\mathcal{P}$ and $H$ are not defined.
  6. Cross entropy is not defined.
  7. In eq. 5, $v_i(\theta)$ is a mapping, but above $v_i$ is defined as a bit string (not a mapping).
  8. Cliques should be capitalized in Tables 1, 2, 4 and 5.
  9. $\mathcal{X}$ is not clearly defined. From the padding paragraph and section 3.4, it looks like it should be $x_i \in \mathcal{X}_i$ and $\mathcal{X} = \cup_i \mathcal{X}_i$.
  10. Table 5 should use scientific notation.
  11. Is the learning rate really $1e^{-4} \approx 0.018$ in 4.1?

### Questions
1. Does a GNN with jumping knowledge preserve the Markov assumption?
  2. Why does Table 2 not include LBP and TRBP?
  3. Was a hard time constraint of 1200 seconds enforced for LBP, TRBP and NeuroLifing?
  4. Is NeuroLifing sensitive to the initialization of the embeddings and network?
  5. Why does Toulbar2 fail on H_Instances_2? 
  6. Table 1 reports "the final loss given by the loss function," whereas the other tables report the final energy. It needs to be clarified that the distinction between loss and energy exists for the baseline methods. If so, what is the gap between loss and energy?
  7. What is the gap between loss and energy for NeuroLifting on synthetic, UAI and PCI? 
  8. The interpretation of the linear complexity needs to be clarified. By mentioning the linear complexity in node size, is the paper claiming an asymptotic improvement over alternatives? 
  9. How does the suggested padding scheme produce only valid solutions, whereas padding with the largest of all energies can produce infeasible solutions?
  10. How does the rouding scheme for $p_i(\theta)$ avoid multi-assignment issues?
  11. What does "showing remarkable scalability and efficiency" mean in (lines 71-72)? What is the concrete evidence that shows this claim?
  12. What stopping criteria are used for NeuroLifting on UAI?

##  Minor comments (did not affect score)
  1. Tables 1, 2, 3 and 4 would be more legible and convey the same results if reported as whole numbers instead.
  2. Capitalize the titles of the references.
  3. Use only one of: `DOI:`, `ISBN` or neither for book references. 
  4. The caption for Figure 1 should describe the stages in the diagram. Figure 2 does this well. 
  5. In Figure 1 $\mathcal{P}$ and $H$ are not defined. 
  6. Cross entropy is not defined.
  7. In eq. 5, $v_i(\theta)$ is a mapping, but above $v_i$ is defined as a bit string (not a mapping).
  8. Cliques should be capitalized in Tables 1, 2, 4 and 5.
  9. $\mathcal{X}$ is not clearly defined. From the padding paragraph and section 3.4, it looks like it should be $x_i \in \mathcal{X}_i$ and $\mathcal{X} = \cup_i \mathcal{X}_i$.
  10. Table 5 should use scientific notation.
  11. Is the learning rate really $1e^{-4} \approx 0.018$ in 4.1?

### Soundness
1

### Presentation
1

### Contribution
2
