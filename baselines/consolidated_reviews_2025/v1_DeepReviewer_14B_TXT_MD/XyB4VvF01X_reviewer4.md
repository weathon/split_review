### Summary

This paper introduces a new approach to theorem proving in the Coq proof assistant by leveraging graph neural networks (GNNs). The authors propose a novel model called Graph2Tac (G2T) that learns hierarchical representations of mathematical concepts and uses them to suggest tactics for proving theorems. The key innovation is the use of a graph-based representation of Coq terms, which captures the dependencies between definitions and allows the model to reason about the context in which a theorem is being proved. The model is trained on a large dataset of Coq projects and can adapt to new definitions and theorems in real time. The authors demonstrate that G2T outperforms state-of-the-art k-nearest neighbor predictors and other machine learning-based solvers in Coq. They also show that G2T complements other online models that learn from proof scripts written by users. The paper makes a significant contribution to the field of automated theorem proving by introducing a new way of representing and reasoning about mathematical concepts in a formal setting.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a novel approach to theorem proving in Coq using graph neural networks, which is a significant contribution to the field.
- The model is able to adapt to new definitions and theorems in real time, which is a valuable feature for practical applications.
- The paper demonstrates the effectiveness of the proposed approach through comprehensive experiments and comparisons with state-of-the-art methods.
- The paper is well-written and clearly explains the technical details of the proposed model and its evaluation.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed approach and potential directions for future research.
- The paper could provide more insights into the types of theorems that the model is able to prove and the types of theorems that it struggles with.
- The paper could discuss the potential ethical implications of using machine learning for automated theorem proving, such as the risk of bias in the training data or the potential for misuse of the technology.

### Suggestions

The paper should delve deeper into the limitations of the Graph2Tac (G2T) model, particularly regarding its ability to handle complex mathematical concepts and proofs. While the graph-based representation is a novel approach, it is crucial to understand the boundaries of its effectiveness. For instance, how does the model perform on theorems that require intricate reasoning chains or those that involve higher-order logic? A more detailed analysis of the model's performance on different categories of theorems, perhaps classified by their logical complexity or the types of tactics required, would be beneficial. Furthermore, the paper should explore the computational cost associated with the graph representation, especially as the size of the Coq project and the number of definitions increase. This would provide a clearer picture of the practical scalability of the approach. It would also be valuable to investigate the model's sensitivity to the quality and diversity of the training data, as this could significantly impact its generalization capabilities.

To enhance the paper, the authors should provide a more granular analysis of the types of theorems that G2T can and cannot prove. This could involve categorizing theorems based on their logical structure, the specific tactics required for their proofs, or their position within the dependency graph of definitions. For example, does the model struggle with theorems that involve nested quantifiers or those that require specific lemmas? Providing concrete examples of theorems that the model successfully proves, as well as those that it fails on, would greatly improve the reader's understanding of the model's strengths and weaknesses. This analysis should also consider the impact of the training data on the model's performance. Are there specific types of theorems that are underrepresented in the training data, and how does this affect the model's ability to generalize to new, unseen theorems? A detailed discussion of these aspects would significantly strengthen the paper's contribution.

Finally, the paper should address the potential ethical implications of using machine learning for automated theorem proving. While the current applications are primarily academic, the technology could have broader implications in the future. For example, if such models are used to verify critical software or hardware systems, the risk of bias or errors in the model could have serious consequences. The paper should discuss the potential for bias in the training data, which could lead to the model favoring certain types of proofs or making incorrect assumptions. It should also consider the potential for misuse of the technology, such as using it to automate the creation of misleading or incorrect proofs. A discussion of these ethical considerations is essential for ensuring the responsible development and deployment of this technology.

### Questions

- Can you provide more details on the types of theorems that the model is able to prove and the types of theorems that it struggles with?
- How does the model compare to other state-of-the-art methods for automated theorem proving in Coq, and what are the advantages and disadvantages of the proposed approach?
- What are the potential limitations of the proposed approach, and what are the directions for future research in this area?

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
