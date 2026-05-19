### Summary

The authors propose a new approach to representation of formal mathematical statements and proofs within the proof assistant Coq. The authors propose to use graph representation of the formal statements and proofs and run a graph neural network on top of this representation to generate tactics suggestions for proof search. One of the key motivations for this approach is the ability to adapt to new definitions and theorems in real time. The authors conduct an empirical evaluation of the proposed approach and show that it outperforms some of the baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The authors present an innovative approach to representation of formal mathematical statements and proofs within the proof assistant Coq. The authors propose to use graph representation of the formal statements and proofs and run a graph neural network on top of this representation to generate tactics suggestions for proof search. One of the key motivations for this approach is the ability to adapt to new definitions and theorems in real time. Empirical evaluation of the proposed approach shows that it outperforms some of the baselines.

### Weaknesses

#### Some Related Works


#### comment

I find the empirical evaluation of the proposed approach not sufficiently extensive and robust to be fully convincing. In particular, the authors randomly select 2000 theorems from the Coq packages in the test set. It is not clear to me if this random selection of the theorems is sufficient to provide a fair and representative evaluation of the approach. It would be better if the authors could provide some arguments why this random selection is sufficient. It would be even better if the authors could evaluate their approach on the entire test set or provide some arguments why such an evaluation on the entire test set is not possible.

In addition, it would be better if the authors could provide some arguments why the chosen baselines are the most relevant and strong baselines. It seems to me that some of the more recent approaches based on e.g. language models are missing.

Finally, it is not clear to me how the authors deal with the data leakage between the training set and the test set. In particular, the authors indicate that they split the packages into training and test ensuring that no test package depends on a training package. However, it is not clear to me that this is sufficient to deal with the data leakage. It seems to me that some of the definitions and theorems can appear in both the training set and the test set. It would be helpful to receive some arguments from the authors why this is not the case or some discussion of the potential impact of such data leakage.

### Suggestions

To strengthen the empirical evaluation, the authors should consider a more comprehensive approach to selecting theorems for testing. Instead of relying on a random subset, they could explore stratified sampling based on theorem complexity or package origin. This would ensure a more balanced representation of the diverse theorem landscape within the Coq libraries. Furthermore, the authors should provide a detailed analysis of the characteristics of the randomly selected theorems, such as the average number of dependencies, the depth of the proof tree, and the types of tactics required for proof. This analysis would help to justify the representativeness of the selected theorems and provide a better understanding of the model's performance across different types of problems. If evaluating the entire test set is computationally prohibitive, the authors should provide a detailed breakdown of the computational costs associated with the evaluation, including the time and memory requirements for each theorem, and justify the use of a subset based on these constraints. This would allow the reader to better assess the trade-offs between evaluation completeness and computational feasibility.

Regarding the choice of baselines, the authors should include a more thorough comparison with recent state-of-the-art methods, particularly those leveraging language models. While the authors mention the computational cost of training such models, they should at least include a comparison with pre-trained models or fine-tuned versions of existing models. This would provide a more complete picture of the proposed approach's performance relative to the current state of the art. The authors should also justify their choice of baselines by discussing the specific strengths and weaknesses of each baseline in the context of the Coq theorem proving task. For example, they could discuss how the k-NN approach compares to language models in terms of adaptability to new definitions and the ability to handle complex proof structures. A more detailed discussion of the baselines would help to contextualize the contributions of the proposed approach and highlight its unique advantages.

Finally, the authors need to address the potential for data leakage more rigorously. While splitting packages based on dependencies is a good start, it does not fully eliminate the possibility of overlapping definitions and theorems between the training and test sets. The authors should provide a more detailed explanation of how they handle such overlaps, including a discussion of the specific measures taken to ensure that no definition or theorem appears in both sets. For example, they could consider using a more fine-grained approach to data splitting, such as splitting at the level of individual definitions or theorems, rather than at the package level. They should also provide a quantitative analysis of the overlap between the training and test sets, such as the number of shared definitions and theorems, to demonstrate the effectiveness of their approach. If complete elimination of data leakage is not possible, the authors should discuss the potential impact of such leakage on the evaluation results and provide a sensitivity analysis to assess the robustness of their findings.

### Questions

- Could you please provide some arguments why the random selection of the theorems is sufficient for the evaluation? Could you please provide some arguments why an evaluation on the entire test set is not possible? 
- Could you please provide some arguments why the chosen baselines are the most relevant and strong baselines? 
- Could you please provide some arguments why the splitting of the packages into training and test ensuring that no test package depends on a training package is sufficient to deal with the data leakage? It seems to me that some of the definitions and theorems can appear in both the training set and the test set. Could you please provide some arguments why this is not the case or some discussion of the potential impact of such data leakage?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
