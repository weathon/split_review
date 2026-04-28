# From Explicit CoT to Implicit CoT: Learning to Internalize CoT Step by Step

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 8, 3, 3

## Abstract
When leveraging language models for reasoning tasks, generating explicit chain-of-thought (CoT) steps often proves essential for achieving high accuracy in final outputs. In this paper, we investigate if models can be taught to internalize these CoT steps. To this end, we propose a simple yet effective method for internalizing CoT steps: starting with a model trained for explicit CoT reasoning, we gradually remove the intermediate steps and finetune the model. This process allows the model to internalize the intermediate reasoning steps, thus simplifying the reasoning process while maintaining high performance. Our approach enables a GPT-2 Small model to solve 9-by-9 multiplication with up to 99\% accuracy, whereas standard training cannot solve beyond 4-by-4 multiplication. Furthermore, our method proves effective on larger language models, such as Mistral 7B, achieving over 50\% accuracy on GSM8K without producing any intermediate steps.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a stepwise internalization approach that encourages a model, initially trained for explicit CoT reasoning, to internalize the reasoning process by gradually removing the intermediate steps during fine-tuning. As a result, the trained model achieves high performance while significantly reducing inference costs compared to explicit CoT.

### Strengths
1. Overall, the paper is well written and easy to follow.

2. The idea of gradually reducing the intermediate steps to internalize CoT is quite intuitive and seems reasonable.

### Weaknesses
1. Figure 3 illustrates that the validation accuracy steadily declines as tokens are progressively removed, until all tokens are eliminated, at which point the accuracy begins to gradually improve. This observation raises concerns that the model may have learned a shortcut instead of genuinely internalizing the CoT. The fact that the model's performance recovers after the complete removal of CoT tokens suggests that the model may be exploiting some underlying pattern in the data rather than learning to perform the reasoning steps internally. This behavior is concerning as it casts doubt on the core claim of the paper.

2. The analysis in Section 6.1 lacks details, such as how the probe model is trained and which layer's hidden states are analyzed. Furthermore, it may be necessary to conduct a probe analysis on the pretrained model to demonstrate that it does not internalize the CoT. The current analysis does not provide sufficient evidence to support the claim that the model is truly internalizing the reasoning process. Without a clear description of the probing methodology and a comparison with a pretrained model, it's difficult to ascertain the validity of the findings.

### Questions
1. How does the "No CoT" setting in Table 3 prevent Mistral 7B, GPT-3.5, and GPT-4 from outputting intermediate steps? Is it achieved by using a prompt such as "Do not output intermediate steps, just provide the answer"? I couldn't find any related explanation. Additionally, considering that LLMs are quite sensitive to prompts, I suspect that the low metrics for these three models are due to poor prompts.

2. Given that ICoT-SI has been extensively trained on the GSM8K dataset, it may not be entirely fair to compare it with the No CoT version of Mistral 7B. A more appropriate comparison would be between ICoT-SI and the Mistral 7B model that has been trained with CoT data, using an effective prompt that encourages it to produce only the final answer.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a way to train an LLM to internalize its CoT steps. They start with a model trained for explicit CoT, and then gradually remove the intermediate steps during finetuning. This approach is simple yet enables small models to achieve stronger performance than explicit CoT in a range of problems, including GSM8K.

### Strengths
The technical idea is original, well-motivated, and sound.

The experiments are solid, including compelling results and insightful analysis.

The paper is well-written.

This work is a solid contribution to the community.

### Weaknesses
The models used in this paper are all small: the largest is mistral 7b; no other comparable-size models are used, like llama. 

Most of the tasks are somewhat synthetic (e.g., 20 x 20 multiplication).

### Questions
Can implicit CoT reasoning match or surpass explicit CoT reasoning in all reasoning tasks? Modeling-wise, what will be the driving factors that decide whether explicit or implicit CoT may outperform each other?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a method called Stepwise Internalization to improve the reasoning capabilities of language models by internalizing chain-of-thought (CoT) steps. This approach involves initially training a model with explicit CoT reasoning, gradually removing these intermediate steps, and then fine-tuning the model to enhance its ability to perform implicit CoT reasoning. This method enables smaller models, like GPT-2 Small, to achieve high accuracy on tasks such as 20-by-20 multiplication while being significantly faster than models relying on explicit CoT reasoning.

### Strengths
- The paper presents an innovative approach that shows potential by internalizing CoT reasoning, reducing LMs' inference time for multiplication and grade school math problems.
- This work demonstrates that smaller models can be trained to perform reasoning tasks effectively by leveraging internal states for reasoning.
- The Stepwise Internalization method shows significant speed enhancements over explicit CoT approaches and improved performance over models not using CoT reasoning.

### Weaknesses
 - Internalized CoT models have worse performance on most of the evaluated tasks compared to the performance of explicit CoT prompting. The power of CoT prompting lies in its simplicity and ease of use without requirement for additional training, which allows for high performance gains across various tasks, which the purposed ICoT method does not offer.
- The comparison with No-CoT baselines is weak since those models are not fine-tuned like the ICoT models. A more appropriate baseline would involve fine-tuning models with CoT examples, without using the internalization technique, for a comparable number of epochs to the ICoT models.
- The choice of intermediate CoT steps as synthetic training data is not justified; other simpler methods of generating synthetic data, such as changing numerical values of the problem, might prove more effective in decreasing latency and increasing accuracy of the models .
- The experimental evaluation is limited in scope, focusing mainly on tasks with simple reasoning patterns like multiplication and basic math problems. This limits the applicability of the findings to compositional tasks that require a higher number of intermediate steps and working memory.
- The approach is not tested on larger models, such as Llama 3.1, or more complex datasets, such as the MATH dataset. This raises questions about its effectiveness compared to just scaling model size or training data, especially given that existing large models already perform well on simple math tasks.

### Questions
1. What are the specific motivations for internalizing CoT steps beyond improved latency? How does this process simplify reasoning without losing flexibility?
2. Have you considered the implications of losing token-based 'working memory' provided by explicit CoT methods, particularly for tasks requiring complex compositional reasoning and multiple steps?
3. Can you compare the effectiveness of this method against other synthetic data approaches, such as deterministic transformations of problem statements, e.g. changing the numbers of problem statement?
4. Why was the method not evaluated on larger models and more complex datasets to provide a broader understanding of its efficacy?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method to achieve implicit chain-of-thought (CoT) reasoning through stepwise internalization training. Through this training, language models learn to reason implicitly without explicit intermediate steps. The authors evaluate the proposed method on various reasoning tasks, such as arithmetic and grade-school math. This approach maintains accuracy while achieving faster inference speeds. Overall, it outperforms inference without CoT and implicit CoT through knowledge distillation while achieving faster inference than traditional explicit CoT methods.

### Strengths
1. Considering only the test time, the Stepwise Internalization (SI) approach greatly enhances the efficiency of reasoning tasks, allowing models to handle problems like multi-digit multiplication faster than explicit CoT reasoning.
2. SI models can achieve the same or close to the accuracy of explicit CoT on parity, coin flip, and multi-digit multiplication. They outperform the knowledge distillation approach and no-CoT inference.
3. The interpretability analysis provides some interesting insights into the internalized reasoning process. The paper finds that implicit CoT models can replicate partial product steps internally as explicit CoT reasoning. However, the internalized reasoning does not yet fully replicate the explicit CoT reasoning. These findings can potentially motivate future research in this direction.

### Weaknesses
1. The proposed implicit CoT's performance is pretty behind the explicit CoT method. Although the paper claims that there is a trade-off between performance and speed and that the proposed method is faster than explicit CoT, I do not view this as a major advantage of the proposed method. In particular, the proposed implicit CoT requires additional step-wise internalization in training time. At the same time, explicit CoT can be applied to models in test time, which allows the explicit CoT to be much more generalizable to a variety of reasoning problems.
2. The paper seems to show only in-distribution experiments that perform step-wise internalization training and testing on the same data distributions. Thus, it is unclear whether the proposed method is generalizable to other reasoning benchmarks and applications. Meanwhile, the strong generalizability of explicit CoT has been well-established in previous studies [1-4].
3. Just to confirm, "remove 8 tokens per epoch." Here, one epoch is a full training run on the entire dataset, not a step of gradient update on a single batch, right? If so, it seems like the internalization process requires a very large amount of training epochs, and this number only increases when longer thoughts are needed. The efficiency seems limited in this case, especially when both the number of thought tokens and the number of model parameters rise.

### Questions
1. I find it interesting that GPT-4 with 5-shot no-CoT only got 44%, while publicly reported GPT-3.5 got 57.1%, and Mixtral got 58.4%. I wonder if the authors have verified that the inference pipeline used can produce a performance that matches the public score for these models.

### Soundness
2

### Presentation
2

### Contribution
2
