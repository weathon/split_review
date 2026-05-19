### Summary

The paper proposes a new model that adapts Bayesian flow networks to the crystal generation task. The authors highlight the particular challenges of dealing with the periodicity of the problem and the unbalanced search space for stable crystals. The proposed method tackles the problem by using a circular distribution as the base distribution of the Bayesian flow network, which makes the model periodic. The result is evaluated in two tasks: ab initio generation and structure prediction. The evaluation is done using pre-defined datasets and metrics. An ablation study is also provided.

### Soundness

2

### Presentation

2

### Contribution

3

### Strengths

- The paper adapts the rather unknown Bayesian flow network to the crystal generation task, which is a relevant and important problem. 
- The authors highlight the important problem of the unbalanced search space for crystal generation. 
- The paper contains an ablation study.

### Weaknesses

#### Some Related Works


#### comment

 - The main weakness of the paper is the evaluation. The metrics that are used for the evaluation are not explained in the paper, nor are the metrics motivated. The authors simply refer to prior work. However, in order to be a meaningful benchmark, the metrics should be explained in detail, and the benchmark should be clearly motivated. It is not clear what properties of the generated crystals the metrics capture, and how these properties relate to the practical usefulness of the generated structures. For example, it is unclear if the metrics assess the stability, novelty, or synthesizability of the generated crystals. The lack of clear motivation for the benchmark makes it difficult to assess the significance of the results.
- The paper is hard to read, especially for readers that are not familiar with Bayesian flow networks. The paper only briefly explains Bayesian flow networks. It would be helpful if the authors could include a more detailed explanation of the method, including the core equations and the training procedure. The current explanation lacks sufficient detail to allow for a thorough understanding of the proposed approach. Furthermore, the connection between the Bayesian flow network and the specific crystal generation task is not clearly articulated, making it difficult to understand how the method is adapted to the problem.
- The authors claim that they introduce the first periodic-E(3) equivariant Bayesian flow network. However, it seems that a significant part of the work is to adapt the method to the crystal generation task. Hence, the contribution might be overclaimed. The novelty of the approach is not clearly demonstrated, and it is unclear what specific modifications were necessary to make the method work for crystal generation. The paper should clearly delineate the novel aspects of the method and how they differ from existing Bayesian flow network approaches.
- The abstract is not very clear and it does not explain the main challenges and the proposed solution. The abstract should provide a concise overview of the problem, the proposed method, and the main results. It should also highlight the key challenges and how the proposed method addresses them. The current abstract lacks these elements, making it difficult to understand the paper's contribution.
- The authors show in Table 3 that their choice of equivariant function is important for the result. However, it is not clear if the other baselines use an equivariant function. It would be good to add a discussion about this. The lack of discussion about the equivariance of the baselines makes it difficult to compare the proposed method with existing approaches. It is important to know if the baselines also use equivariant functions, and if so, what type of equivariance they employ.

### Suggestions

The paper needs a more thorough explanation of the evaluation metrics used. Instead of simply referring to prior work, the authors should clearly define each metric, explain what specific properties of the generated crystals they measure, and provide a justification for why these metrics are appropriate for evaluating the proposed method. For example, if the COV-P metric is used, the authors should explain what it measures, how it is calculated, and why it is a relevant measure for ab initio crystal generation. Similarly, for the match rate metric, the authors should explain what constitutes a 'match' and why this is a meaningful measure of performance. Furthermore, the authors should discuss the limitations of the chosen metrics and how they might affect the interpretation of the results. This would greatly improve the clarity and rigor of the evaluation.

To improve the readability of the paper, the authors should include a more detailed explanation of Bayesian flow networks, including the core equations and the training procedure. This explanation should be accessible to readers who are not familiar with this method. The authors should also clearly articulate the connection between the Bayesian flow network and the crystal generation task, explaining how the method is adapted to handle the specific challenges of this problem, such as the periodicity of the fractional coordinates and the unbalanced search space for stable crystals. This should include a discussion of the specific choices made in the adaptation process and how these choices affect the performance of the model. A more detailed explanation of the method would greatly enhance the paper's accessibility and allow for a more thorough understanding of the proposed approach.

Finally, the authors should clarify the novelty of their approach and provide a more detailed discussion of the specific modifications made to adapt the Bayesian flow network to the crystal generation task. The paper should clearly delineate the novel aspects of the method and how they differ from existing Bayesian flow network approaches. The authors should also discuss the limitations of their approach and how they might be addressed in future work. Furthermore, the abstract should be rewritten to provide a clear and concise overview of the problem, the proposed method, and the main results. It should also highlight the key challenges and how the proposed method addresses them. This would make the paper more accessible and allow readers to quickly grasp the main contributions of the work.

### Questions

- Could you provide a detailed explanation of the metrics that you use? Why are these metrics motivated for the task? 
- Could you add a more detailed explanation of Bayesian flow networks? 
- Could you clarify the novelty of your approach? 
- Could you clarify if the baselines use an equivariant function? 
- Could you clarify the main challenges and the proposed solution in the abstract?

### Rating

6

### Confidence

2

**********
