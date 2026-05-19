### Summary

This paper proposes a novel unsupervised LLM evaluation method called PiCO, which utilizes a peer-review mechanism to measure LLMs automatically without any human feedback. In this setting, both open-source and closed-source LLMs lie in the same environment, capable of answering unlabeled questions and evaluating each other, where each LLM's response score is jointly determined by other anonymous ones. To obtain the ability hierarchy among these models, the authors assign each LLM a learnable capability parameter to adjust the final ranking. The key assumption behind this is that high-level LLM can evaluate others' answers more accurately (confidence) than low-level ones, while higher-level LLM can also achieve higher answer-ranking scores. Moreover, the authors propose three metrics called PEN, CIN, and LIS to evaluate the gap in aligning human rankings. The experiments are conducted on multiple datasets with these metrics, validating the effectiveness of the proposed approach.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper explores a novel unsupervised LLM evaluation direction without human feedback, utilizing peer-review mechanisms to measure LLMs automatically. All LLMs can answer unlabeled questions and evaluate each other.
2. A constrained optimization based on the consistency assumption is proposed to re-rank the LLMs to be closer to human rankings.
3. The experiments with these metrics on three crowdsourcing datasets validate the effectiveness of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to understand the time and resource requirements for training and evaluating the models, especially when dealing with a large number of LLMs. The lack of specific details regarding the hardware used and the time taken for each stage of the process makes it difficult to assess the practical feasibility of the approach.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed method. For example, how does the method perform when the LLMs being evaluated have very different capabilities or when the evaluation dataset is biased towards a particular type of task? It is unclear how the method would handle scenarios where the peer-review process is dominated by a few high-performing models, potentially skewing the evaluation of others.
3. The paper could provide more details on the specific implementation of the peer-review mechanism, such as the criteria used for selecting the reviewers and the process for aggregating their evaluations. The current description lacks the necessary detail to fully understand the practical aspects of the method. For instance, it is not clear how the anonymity of the reviewers is maintained, or how the system ensures that the reviews are not biased by the reviewers' own characteristics.

### Suggestions

To address the lack of computational cost analysis, the authors should include a detailed breakdown of the time and resources required for each stage of the PiCO framework. This should include the time taken for response generation, peer review, and the constrained optimization process. The authors should also specify the hardware used for the experiments, including the type of GPUs, CPU, and memory. Furthermore, it would be beneficial to provide an analysis of how the computational cost scales with the number of LLMs being evaluated. This would allow readers to better understand the practical limitations of the approach and its applicability to different scenarios. For example, the authors could provide a table showing the time taken for each stage with varying numbers of LLMs, which would give a clearer picture of the computational overhead.

To address the limitations of the proposed method, the authors should conduct a more thorough analysis of how the method performs under different conditions. Specifically, they should investigate the impact of varying the capabilities of the LLMs being evaluated. This could involve creating scenarios where the LLMs have significantly different performance levels and analyzing how the peer-review process handles these differences. Additionally, the authors should explore the impact of dataset bias by evaluating the method on datasets that are skewed towards particular types of tasks. This would help to identify potential weaknesses of the approach and suggest ways to mitigate them. For example, the authors could use a dataset that is heavily focused on a specific domain and see how the peer-review process performs when evaluating models with varying levels of expertise in that domain. Furthermore, the authors should analyze the impact of a few high-performing models dominating the peer-review process and propose strategies to mitigate this issue, such as using a weighted voting system or introducing diversity in the reviewer pool.

To provide more details on the implementation of the peer-review mechanism, the authors should include a detailed description of the criteria used for selecting the reviewers. This should include a discussion of how the reviewers are chosen and what factors are considered in the selection process. The authors should also provide a detailed explanation of the process for aggregating the evaluations from the reviewers. This should include a description of how the individual evaluations are combined to produce a final score for each LLM. Furthermore, the authors should discuss how the anonymity of the reviewers is maintained and how the system ensures that the reviews are not biased by the reviewers' own characteristics. For example, the authors could describe a mechanism that randomly assigns reviewers to responses and ensures that the reviewers do not know which model generated the response they are evaluating. This would help to ensure that the reviews are objective and unbiased.

### Questions

1. How does the proposed method handle situations where the LLMs being evaluated have very different capabilities?
2. What are the potential biases that could arise from using LLMs as reviewers, and how does the proposed method address these biases?
3. How does the proposed method compare to other unsupervised LLM evaluation methods in terms of accuracy and efficiency?

### Rating

6

### Confidence

3

**********
