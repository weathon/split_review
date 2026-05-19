### Summary

This paper presents a dataset generation pipeline and a planning algorithm for long-horizon human activity planning. The dataset generation pipeline leverages LLMs to generate long-horizon plans, which are then grounded with motion data. The planning algorithm uses LLMs to generate candidate actions and value functions to score the actions. The proposed method is evaluated on the proposed dataset and compared to two baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed dataset generation pipeline is novel and interesting. It is impressive that the pipeline can generate 10k samples with reasonable quality. 
2. The proposed method is reasonable and shows better performance than the baselines. 
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The dataset generation pipeline is not fully automatic. It still requires manual filtering and verification, which is labor-intensive and may introduce bias. The reliance on human evaluation for filtering introduces a potential bottleneck in scalability and may lead to inconsistencies in the dataset's quality. The lack of a clear, automated metric for filtering could result in subjective decisions, impacting the reproducibility and objectivity of the dataset generation process.
2. The value function is simple and may not be generalizable to different scenarios. The current implementation of the value function, relying on basic heuristics, might not capture the complexities of human behavior in diverse environments. This simplicity could limit the model's ability to adapt to novel situations or tasks that require more nuanced reasoning about the value of actions.

### Suggestions

To address the limitations of the dataset generation pipeline, a more robust and automated filtering mechanism should be developed. Instead of relying solely on manual verification, the authors could explore using a combination of automated metrics and a smaller-scale human review process. For example, they could train a classifier to identify and filter out low-quality plans based on features extracted from the generated text and motion data. This classifier could be trained on a small, manually verified subset of the data and then used to automatically filter the rest. This would reduce the labor intensity of the filtering process and improve the scalability of the dataset generation pipeline. Furthermore, the authors should investigate methods to quantify the uncertainty in the generated plans, which could be used to prioritize plans for manual review, focusing human effort on the most ambiguous cases. This would also help in identifying potential biases in the generation process.

To improve the generalizability of the value function, the authors should explore more sophisticated methods for modeling the value of actions. Instead of relying on simple heuristics, they could consider using a learned value function that is trained on a diverse set of human behaviors. This could involve using reinforcement learning techniques to learn a value function that can predict the long-term consequences of actions. The value function could also be made context-aware, taking into account the current state of the environment and the agent's goals. This would allow the model to adapt to different scenarios and tasks more effectively. Additionally, the authors should investigate methods to incorporate common-sense knowledge into the value function, which could help the model to reason about the value of actions in a more human-like way. This could involve using knowledge graphs or other forms of structured knowledge to represent common-sense facts about the world.

Finally, the authors should consider evaluating their method on existing datasets to provide a more comprehensive comparison with other approaches. While the proposed dataset is a valuable contribution, it is important to demonstrate that the method can also perform well on established benchmarks. This would provide a more robust assessment of the method's capabilities and limitations. The authors could also explore how their method performs on datasets with different characteristics, such as those with more complex environments or tasks. This would help to identify the strengths and weaknesses of their approach and guide future research directions.

### Questions

1. Is it possible to make the dataset generation pipeline fully automatic? 
2. Is it possible to evaluate the proposed method on existing datasets?

### Rating

6

### Confidence

4

**********
