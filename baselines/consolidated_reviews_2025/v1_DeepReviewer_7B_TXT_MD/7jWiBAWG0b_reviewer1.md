### Summary

This paper presents stability-based learning guarantees for non-convex pairwise SGD in the presence of heavy-tailed gradient noise. The authors establish generalization bounds and learning rates for non-convex pairwise SGD by leveraging (1, on-average) algorithmic stability and sub-Weibull noise assumptions. The derived bounds are claimed to be comparable to existing results in the literature, without requiring a bounded gradient assumption. Additionally, the paper extends its analysis to the minibatch setting, providing the first stability-based learning guarantees for non-convex pairwise minibatch SGD.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides the first stability-based learning guarantees for non-convex pairwise minibatch SGD, which is a valuable contribution to the field.
2. The authors establish a connection between (1, on-average) model stability and generalization error, which is of theoretical interest.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not clearly articulate the novelty of its results compared to existing work. While the authors claim that their results are the first to provide stability-based learning guarantees for non-convex pairwise minibatch SGD, the technical approach appears to be a straightforward extension of existing techniques. The core idea of using stability to derive generalization bounds is well-established, and the application to pairwise losses, while technically involved, does not seem to introduce a fundamentally new conceptual leap. The paper would benefit from a more detailed explanation of the specific challenges overcome in adapting stability analysis to the pairwise setting and how these challenges differ from, or are similar to, those encountered in standard non-convex SGD.
2. The paper lacks a discussion on the practical implications of the derived bounds. While the theoretical results are interesting, it is unclear how these bounds can be used to guide the design or analysis of practical machine learning algorithms. For example, the paper does not discuss how the derived stability parameters relate to the choice of learning rate, batch size, or other hyperparameters. A more thorough discussion of the practical relevance of the results would significantly enhance the paper's impact. It would be beneficial to include a section that explores the limitations of the derived bounds and suggests directions for future research that could address these limitations.
3. The paper does not provide a clear comparison of the derived bounds with existing results in the literature. While the authors claim that their bounds are comparable to existing results, they do not provide a detailed analysis of the differences in the assumptions and the resulting bounds. A more thorough comparison would help to clarify the contribution of the paper and to identify the specific scenarios in which the derived bounds are most relevant. The paper should explicitly state the conditions under which the proposed bounds are tighter or comparable to existing bounds, and provide a discussion of the trade-offs between different assumptions.

### Suggestions

To strengthen the paper, the authors should provide a more detailed explanation of the technical challenges involved in extending stability analysis to non-convex pairwise losses. Specifically, they should discuss how the pairwise nature of the loss function affects the stability analysis, and how their approach differs from existing techniques used for standard non-convex SGD. For example, they could elaborate on how the dependence of the loss function on pairs of samples introduces additional complexities in the analysis, and how they have addressed these complexities in their proofs. Furthermore, it would be beneficial to provide a more concrete example of a pairwise loss function and demonstrate how the derived stability bounds can be applied in practice. This would help to clarify the practical relevance of the theoretical results and make the paper more accessible to a broader audience. The authors should also discuss the limitations of their analysis and suggest directions for future research that could address these limitations.

In addition, the authors should include a more comprehensive discussion of the practical implications of their results. This discussion should include a detailed analysis of how the derived stability parameters relate to the choice of hyperparameters, such as the learning rate and batch size. For example, they could provide guidelines on how to choose these hyperparameters to optimize the performance of pairwise SGD based on their stability bounds. Furthermore, they should discuss the limitations of their analysis and suggest directions for future research that could address these limitations. For instance, they could explore the possibility of deriving tighter bounds under more relaxed assumptions or developing adaptive methods that automatically adjust the hyperparameters based on the stability analysis. This would make the paper more relevant to practitioners and increase its impact on the field.

Finally, the authors should provide a more detailed comparison of their derived bounds with existing results in the literature. This comparison should include a discussion of the differences in the assumptions and the resulting bounds, and should clearly state the conditions under which the proposed bounds are tighter or comparable to existing bounds. For example, they could provide a table that summarizes the key assumptions and bounds for different algorithms and loss functions. This would help to clarify the contribution of the paper and to identify the specific scenarios in which the derived bounds are most relevant. The authors should also discuss the trade-offs between different assumptions and provide guidance on when each set of assumptions is most appropriate. This would make the paper more useful for researchers and practitioners who are interested in using stability analysis to study the generalization of machine learning algorithms.

### Questions

1. Could the authors provide a more detailed explanation of the novelty of their results compared to existing work? Specifically, what are the key technical challenges that are overcome in this paper, and how do they differ from the challenges encountered in existing work on stability-based learning guarantees for non-convex SGD?
2. Could the authors provide a more detailed discussion of the practical implications of the derived bounds? How can these bounds be used to guide the design or analysis of practical machine learning algorithms?
3. Could the authors provide a more detailed comparison of the derived bounds with existing results in the literature? What are the key differences in the assumptions and the resulting bounds, and under what conditions are the proposed bounds tighter or comparable to existing bounds?

### Rating

6

### Confidence

4

**********
