### Summary

The paper presents a graph neural network (GNN) for learning representations of proof states and predicting tactics in the Coq proof assistant. The model is trained on a large dataset of proof states and their corresponding tactics, and it is able to learn the relationships between the proof states and the tactics. The approach is promising and has the potential to improve the efficiency and effectiveness of tactic prediction in Coq.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes a novel approach to tactic prediction in Coq using a graph neural network model. The model is trained on a large dataset of proof states and their corresponding tactics, and it is able to learn the relationships between the proof states and the tactics. The approach is promising and has the potential to improve the efficiency and effectiveness of tactic prediction in Coq.

- The paper evaluates the model on a set of theorems from various Coq packages and compares its performance to several baselines, including a k-nearest neighbor model and a transformer model. The results show that the graph neural network model outperforms the baselines in terms of the number of theorems proved and the time taken to prove them. The evaluation is comprehensive and provides evidence for the effectiveness of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the types of theorems that the model is able to prove and the types of theorems that it struggles with. It would be helpful to have a more fine-grained analysis of the model's performance on different categories of theorems, such as those involving induction, recursion, or higher-order logic. This would help to identify the strengths and weaknesses of the model and to guide future research in this area.

- The paper does not discuss the limitations of the model in detail. For example, the model may not be able to handle very complex proof states or very long proofs. It would be helpful to have a more thorough discussion of the limitations of the model and to identify areas for future research. Specifically, the paper should address the model's scalability with respect to the size of the proof state graph and the length of the proof sequence. It is also unclear how the model handles proof states with a large number of hypotheses or complex dependencies between them.

- The paper does not provide a detailed comparison of the model to other approaches for tactic prediction in Coq, such as those based on symbolic methods or on other machine learning techniques. It would be helpful to have a more comprehensive comparison of the model to other approaches, including a discussion of the advantages and disadvantages of each approach. For example, a comparison to decision tree based methods or to methods that use a combination of symbolic and neural techniques would be beneficial.

### Suggestions

The paper would benefit from a more detailed analysis of the types of theorems the model can and cannot prove. This should go beyond simply reporting overall statistics and delve into specific categories of theorems, such as those involving induction, recursion, or higher-order logic. For example, the authors could analyze the model's performance on theorems that require specific tactics like 'induction' or 'apply', and compare this to its performance on theorems that can be solved with more straightforward tactics. This analysis should also consider the complexity of the theorems, perhaps using metrics like the number of logical connectives or the depth of the proof tree. Such an analysis would provide a more nuanced understanding of the model's capabilities and limitations, and would help to identify areas where the model could be improved. Furthermore, it would be beneficial to include examples of theorems that the model was able to prove and those it failed on, to give a concrete sense of the model's strengths and weaknesses.

In addition to a more fine-grained analysis of theorem types, the paper should also address the limitations of the model in terms of scalability and handling complex proof states. The authors should discuss how the model's performance changes as the size of the proof state graph increases, and how it handles proof states with a large number of hypotheses or complex dependencies. For example, the authors could analyze the model's performance on theorems that require a large number of proof steps, or on theorems that involve a large number of hypotheses. This analysis should also consider the computational cost of the model, and how it scales with the size of the proof state graph. It would be useful to know the maximum size of the proof state graph that the model can handle, and how the model's performance degrades as the graph size increases. This would help to identify the practical limitations of the model and to guide future research in this area.

Finally, the paper should include a more comprehensive comparison of the model to other approaches for tactic prediction in Coq. This comparison should not only include other machine learning-based methods, but also symbolic methods and hybrid approaches. For example, the authors could compare their model to decision tree-based methods, or to methods that use a combination of symbolic and neural techniques. This comparison should discuss the advantages and disadvantages of each approach, and should highlight the unique contributions of the proposed model. The authors should also discuss how their model compares to existing tools like CoqHammer, and how it could be integrated with such tools to improve overall performance. This would provide a more complete picture of the state of the art in tactic prediction and would help to position the proposed model within the broader context of existing research.

### Questions

- How does the model perform on theorems that require specific tactics, such as 'induction' or 'apply'? Are there any types of theorems that the model struggles with?

- How does the model compare to other approaches for tactic prediction in Coq, such as those based on symbolic methods or on other machine learning techniques? What are the advantages and disadvantages of each approach?

- How does the model scale to larger proof states or longer proofs? Are there any limitations to the model in terms of the size of the proof state or the length of the proof?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
