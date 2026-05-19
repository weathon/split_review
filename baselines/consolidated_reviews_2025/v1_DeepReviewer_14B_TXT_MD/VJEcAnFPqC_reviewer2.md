### Summary

This paper proposes a synthetic graph navigation task to study stepwise inference, a popular prompting technique that elicits reasoning from large language models. Specifically, they consider a directed acyclic graph (DAG) and train a model to predict whether there is a path from a source node to a target node. The main contribution of this work is to show that a 2-layer transformer can learn to perform this task with stepwise inference better than direct inference. They also study the diversity-accuracy tradeoff and the preference for shorter paths.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The synthetic graph navigation task is a neat idea to study stepwise inference.

### Weaknesses

#### Some Related Works


#### comment

 - The main weakness of this work is the gap between the motivation and the actual experimental results. The introduction motivates this work by listing a number of stepwise inference methods that have been proposed for large language models, but the experimental results are on a 2-layer transformer trained from scratch on a synthetic graph navigation task. It is not clear how these results can shed light on the stepwise inference methods used in large language models. The connection between the synthetic task and the complex reasoning processes in large language models is tenuous. The graph navigation task, while interesting, may be too simplistic to capture the nuances of stepwise inference as it is used in natural language processing. The model is essentially learning a form of pathfinding, which is a well-studied problem in graph theory, rather than the more complex reasoning chains seen in language models.
- The conclusion that a model can learn to perform stepwise inference better than direct inference seems unsurprising, given that the training data for stepwise inference explicitly contains intermediate steps. This is a rather trivial observation, as the model is explicitly trained with the solution path, which is not the case for direct inference. The performance difference is therefore not surprising and does not provide much insight into the mechanisms of stepwise inference in more complex models.

### Suggestions

The paper would benefit from a more thorough justification of how the synthetic graph navigation task relates to stepwise inference in large language models. The authors should provide a more detailed explanation of how the observed behaviors in their model, such as the diversity-accuracy tradeoff and the preference for shorter paths, manifest in the context of natural language reasoning. For example, they could discuss how the 'shorter path' bias might relate to a tendency for language models to favor simpler, less accurate solutions, and provide concrete examples from the literature to support this claim. Furthermore, the authors should consider exploring more complex graph structures or navigation tasks that more closely resemble the reasoning challenges faced by large language models. This could involve incorporating hierarchical structures or introducing constraints that force the model to engage in more sophisticated planning. 

To strengthen the paper's contribution, the authors should consider including experiments that more directly address the stepwise inference mechanisms in large language models. This could involve using a small language model trained on a simplified reasoning task, where the input and output are represented in a structured format similar to the graph navigation task. This would allow for a more direct comparison between the model's behavior on the synthetic task and its behavior on a more realistic reasoning task. Additionally, the authors could explore the use of attention visualization techniques to gain insights into how the model is processing the input and generating the output. This could help to identify the specific mechanisms that are responsible for the observed behaviors, such as the diversity-accuracy tradeoff and the preference for shorter paths. 

Finally, the authors should address the limitations of their approach more explicitly. While the synthetic task provides a controlled environment for studying stepwise inference, it is important to acknowledge that it does not fully capture the complexities of natural language reasoning. The authors should discuss the potential limitations of their findings and suggest directions for future research that could address these limitations. This could involve exploring more complex tasks, using larger models, or incorporating more realistic data. By acknowledging these limitations, the authors can provide a more balanced and nuanced perspective on their work and its potential impact on the field.

### Questions

- The paper says that "we can empirically reproduce and analyze several phenomena observed at scale: (i) the stepwise inference reasoning gap, the cause of which we find in the structure of the training data". I'm confused by this statement because it seems that the stepwise inference reasoning gap is caused by the lack of intermediate steps in the training data for direct inference, which is different from the structure of the training data for stepwise inference. Could you clarify this?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
