# Linear Mode Connectivity in Differentiable Tree Ensembles

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
\emph{Linear Mode Connectivity} (LMC) refers to the phenomenon that performance remains consistent for linearly interpolated models in the parameter space. For independently optimized model pairs from different random initializations, achieving LMC is considered crucial for validating the stable success of the non-convex optimization in modern machine learning models and for facilitating practical parameter-based operations such as model merging.
While LMC has been achieved for neural networks by considering the permutation invariance of neurons in each hidden layer, its attainment for other models remains an open question.
In this paper, we first achieve LMC for \emph{soft tree ensembles}, which are tree-based differentiable models extensively used in practice.
We show the necessity of incorporating two invariances: \emph{subtree flip invariance} and \emph{splitting order invariance}, which do not exist in neural networks but are inherent to tree architectures, in addition to permutation invariance of trees.
Moreover, we demonstrate that it is even possible to exclude such additional invariances while keeping LMC by designing \emph{decision list}-based tree architectures, where such invariances do not exist by definition.
Our findings indicate the significance of accounting for architecture-specific invariances in achieving LMC.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper explores Linear Mode Connectivity (LMC) in soft tree ensemble models. LMC is well studied in neural networks, but achieving it in tree models presents unique challenges due to their architectural differences. The authors identify additional invariants, subtree flip and splitting order, that are necessary to achieve LMC in tree structures that differ from neural networks, including permutation invariance. With a matching algorithm that takes these invariants into consideration, the authors show that LMC can also be achieved in soft tree ensembles. And they further present a modified decision list architecture that preserves LMC without these additional invariances, aiming to simplify model merging and other parameter-based applications.

### Strengths
- The approach of exploring linear mode connectivity, which has been mainly studied in neural networks, in a different architecture is novel.
- The organization and flow of the paper effectively explains the existing research and the proposed method and is easy to understand.
- Through various experiments, the authors show that linear mode connectivity can be achieved in soft tree ensembles.
- The authors show that soft tree ensembles trained on different data splits can be merged to form better performing models.

### Weaknesses
 - The authors do not provide a more efficient matching algorithm other than exhaustive search.
- The paper does not provide sufficient justification for using the proposed modified decision list. Specifically, the proposed architecture presents a higher barrier compared to an oblivious tree that includes all invariants. Furthermore, it lacks a compelling practical use case demonstrating more efficient matching relative to other tree-based architectures, such as model merging, which can be used to improve performance. To strengthen the argument, it would be necessary to include some experiment similar to the one shown in Figure 8, applied to the proposed architecture.



### Questions
- In Figure 6, I don't quite understand why AM considering only permutation increases the barrier more than naive interpolation. Why does considering only activation result in a worse match than identity? The authors explain this in the main text as follows, but I would like a more detailed explanation.
    
    > This is because parameter values are not used during the rearrangement of the tree in AM.
    > 
- Why do the authors think that the barrier after matching increases as depth increases? Ainsworth et al. (2023) showed that the barrier decreases as width increases, but they did not experiment with depth, and Entezari et al. (2022) measured the barrier for changes in width and depth without matching, which is different from the experiment in Figure 6, which measured the barrier after matching.
- Is there a compelling reason to use activation matching over weight matching, given that it does not seem to offer any clear advantages? Or is it simply intended to replicate the methodology of Ainsworth et al. (2023) for validation purposes?
- It would be useful to know the actual runtime required for matching. Compared to neural networks commonly considered in standard LMC research, such as ResNet, the number of parameters here is significantly lower. Given this, even with a large number of invariance patterns, it may not take very long to check all of them.
- Some minor suggestions:
    - In Figure 6, the x-axis represents different categories without a clear order, making the use of a line plot appear unnatural. A bar plot or box plot would be more appropriate in this case.
    - In the tables and figures, the notation "Ours" does not clearly give the intended meaning. While I understand that it stands for "Perm & Flip & Order", it is somewhat confusing. This is especially noticeable in Tables 3 and 4, where "Decision List (Modified)" is also the proposed method ("Ours"), which makes the absence of results in the corresponding cell seem unnatural. Furthermore, I assume that "Naive" is meant to indicate the results without matching, but this is not explained anywhere. To improve clarity, it would be helpful either to label it more explicitly as "naive interpolation", as in the cited papers, or to provide additional clarification in the main text.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work studies the phenomenon of linear mode connectivity (LMC) in decision tree models (as opposed to neural networks, where they have been studied extensively). Specifically, they investigate whether soft-tree ensembles can be interpolated, while retaining accuracy. Unlike in neural networks, where permutation invariance is sufficient, the authors show that additional invariances unique to decision tree models are necessary for LMC to hold - in fact, this is the key finding of the work.

### Strengths
The paper has several strengths:

- The problem addressed in this work is of general interest, and illuminates an interesting property of decision trees.
- The paper is very clearly written, and easy to follow
- This paper hinges upon it's empirical evaluation: the experiments are quite thorough, and clearly show how incorporating *additional* invariances into model interpolation leads to better accuracy (the key claim of the work).
- The notion of the *modified decision list* architectures is an interesting and potentially highly useful one (as it seems to reduce computation cost per inference)

### Weaknesses
There is one significant weakness in this work:

- Lack of Rigorous Theory: the paper would have been strengthened significantly had the authors provided a rigorous analysis of the effect of the stated invariances (permutation, subtree flip, and splitting order) on the ability to interpolate 2 (or more) models - even if only on extremely simple cases. Were that so, the empirical results would have been used to support rigorous theory, which would have been a much more powerful argument. Specifically, the paper lacks a formal definition of what constitutes a 'mode' in the context of decision trees, and how the proposed invariances preserve or alter these modes during interpolation. Without this, it's difficult to assess the theoretical implications of the empirical findings. For example, a simple case study involving two shallow trees with a single split each, and analyzing the effect of subtree flips on the interpolated model's decision boundary, would have been a valuable addition.
-  Linear Mode Connectivity was proposed to understand how deep neural networks could be sparsified (Frankle et al, 2020). Can a similar analysis of methods to sparsify decision trees be done, provided the insights proposed in this work? An analysis of this sort - where the need to interpolate models becomes evident - would have also noticeably improved this work. The paper does not explore the potential of using LMC to identify sparse yet accurate decision tree structures, which is a missed opportunity given the connection to neural network sparsification. It would be beneficial to see experiments that investigate whether interpolating between two dense trees can lead to a sparse tree with comparable or better performance.
- The authors do not highlight specific tasks for which interpolation of trees would be of significant benefit. This weakens the argument motivating the need for this work. For instance, does model interpolation in tree ensembles improve robustness to distribution shift? Furthermore, the paper does not explore the computational cost of the proposed interpolation method, which is a critical factor for practical applications. A comparison of the inference time of the interpolated model versus the original models would be necessary to justify the practical utility of this approach. It is also unclear how the proposed method would scale to very large tree ensembles.

### Questions
See the Weaknesses section.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper investigates Linear Mode Connectivity (LMC) in the context of differentiable tree ensemble models, particularly focusing on soft tree ensembles. LMC refers to the property where linearly interpolating two models (in parameter space) does not degrade performance, a phenomenon previously established for neural networks. The authors extend this concept to tree-based models, identifying specific architectural invariances unique to trees—namely, subtree flip invariance and splitting order invariance—as critical for achieving LMC. They further propose a novel decision list-based architecture that bypasses these invariances, simplifying the conditions necessary for LMC. Through empirical evaluation, the paper demonstrates that LMC can be achieved in tree ensembles, broadening the understanding of LMC beyond neural networks. In summary, I believe that both the research topic and methods are relatively novel and will significantly contribute to the deep learning community.

### Strengths
**Originality:** This work is original in extending the concept of LMC to tree-based models, an area previously unexplored. By identifying invariances specific to tree structures, the paper introduces a new perspective on achieving functional equivalence in non-neural models.

**Clarity:** Despite the complexity of the topic, the paper is clearly written, with detailed explanations of both the mathematical framework and empirical results. Figures and diagrams (such as Figure 3 on invariances) effectively support comprehension.

**Significance:** The work expands the applicability of LMC, which is valuable for understanding stability in non-convex optimization and facilitating practical applications such as model merging. The findings on tree-specific invariances could have a substantial impact on future research in tree ensemble models and their integration with neural network techniques.

### Weaknesses
 **Empirical Validation Scope:** The empirical results are primarily based on tabular datasets. Extending the validation to additional types of data (e.g., image or sequential data processed via tree ensembles) could further strengthen the findings. Specifically, while the paper focuses on soft tree ensembles, which are often used as alternatives to MLPs, it would be valuable to see how these models perform on tasks where MLPs are traditionally used, such as image classification or sequence modeling. This would help to establish the generalizability of the LMC findings beyond tabular data. The current focus on tabular data limits the scope of the conclusions and leaves open questions about the applicability of LMC in more complex data domains.

**Scalability of Additional Invariance Handling:** The paper discusses the computational expense associated with handling additional invariances for deeper trees. However, a more detailed discussion of potential optimizations or heuristic approaches to manage this complexity would be beneficial. The discussion should include specific examples of how the number of possible subtree flips scales with tree depth and how this impacts the computational cost of finding equivalent models. Furthermore, the paper should explore the trade-offs between the accuracy of the matching algorithm and its computational cost, as well as the potential for approximation techniques to mitigate this issue.

**Comparative Analysis:** While the results demonstrate LMC in tree ensembles, the paper could benefit from a more in-depth comparison with related methods or model architectures, particularly alternative approaches to model merging or parameter interpolation that do not rely on LMC. For example, techniques that involve averaging model weights, or other forms of ensemble methods, should be discussed in the context of the proposed LMC approach. A more thorough comparison would help to clarify the advantages and disadvantages of the proposed method compared to existing techniques, and would provide a better understanding of the specific scenarios where LMC is most beneficial.

**Equation Reference:** Please use "Equation (1)" instead of "Equation 1."

### Questions
See Weakness.

### Soundness
3

### Presentation
3

### Contribution
3
