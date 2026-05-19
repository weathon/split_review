### Summary

The authors show that finetuning LLMs on cognitive tasks results in better performance than traditional cognitive models.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The authors show that LLMs can be used as cognitive models, which is a novel contribution. They also show that the model can generalize to new tasks after fine-tuning on two tasks, which is also a novel contribution.

### Weaknesses

#### Some Related Works


#### comment

The authors show that LLMs can be used as cognitive models, which is a novel contribution. They also show that the model can generalize to new tasks after fine-tuning on two tasks, which is also a novel contribution.

The authors do not compare to many traditional models, and the ones they do compare to are not the best ones. For example, for the choice task, the authors could have used a cognitive model developed by themselves (Daw et al., 2011). For the horizon task, there are many models that fit the data well. 

The authors do not show the model can be used to predict new behavior, which is the hallmark of a good cognitive model. Instead, they show that the model can fit the data well, which is more akin to a good statistical model.

### Suggestions

The paper's central claim that LLMs can serve as cognitive models is intriguing, but the current evaluation is insufficient to fully support this claim. While demonstrating that LLMs can fit existing behavioral data is a necessary first step, it is not sufficient to establish a model as a genuine cognitive model. Cognitive models are expected to provide insights into the underlying mechanisms of cognition and to predict novel behavioral patterns, not just interpolate existing data. The authors should consider more rigorous testing paradigms that would allow for the evaluation of the model's predictive power. For example, they could explore the model's ability to generalize to new task variations or to predict behavior in scenarios that were not included in the training data. This could involve creating synthetic datasets with novel task structures or using established cognitive paradigms with known behavioral signatures. Without such tests, the claim that LLMs can serve as cognitive models remains weak.

To strengthen the comparison with traditional cognitive models, the authors should consider a more comprehensive set of baselines. Instead of relying on a single baseline model for each task, they should include a range of models that represent different theoretical perspectives and levels of complexity. For the choice task, for instance, they could compare against models based on prospect theory, reinforcement learning, and other established decision-making frameworks. Similarly, for the horizon task, they should include models that capture different aspects of exploration and exploitation. This would provide a more nuanced understanding of the strengths and weaknesses of the LLM-based approach and would allow for a more meaningful comparison with the existing literature. Furthermore, the authors should provide a detailed justification for their choice of baseline models and explain why these models are representative of the state-of-the-art in cognitive modeling.

Finally, the authors should clarify the specific aspects of the LLM that contribute to its performance as a cognitive model. Is it the ability to learn complex representations from the text prompts, or is it the inherent structure of the LLM itself? By conducting ablation studies or by analyzing the internal representations of the LLM, the authors could gain a better understanding of the mechanisms that underlie its behavior. This would not only strengthen the paper's claims but also provide valuable insights into the potential of LLMs for cognitive modeling. Furthermore, the authors should explore the limitations of the LLM approach. For example, how does the model perform when faced with tasks that require explicit reasoning or planning? Addressing these questions would provide a more balanced and comprehensive assessment of the potential of LLMs as cognitive models.

### Questions

Can the authors compare to more models?
Can the authors show that the model can be used to predict new behavior?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
