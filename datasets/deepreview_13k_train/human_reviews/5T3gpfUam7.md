# Memory retaining finetuning via distillation

- Decision: Reject
- Scores: 5, 3, 6

## Abstract
Large language models (LLMs) pretrained on large corpora of internet text possess much of the world knowledge.
Following pretraining, one often needs to conduct continued pretraining on certain capabilities such as math and coding, or "posttraining" (a.k.a., alignment) techniques to make the models follow users' instructions and align them with human preferences.
One challenge during these finetuning stages is that the model can lose the pretraining knowledge or forget certain capabilities (e.g., in-context learning ability).
Moreover, although there exist strong open-weight LLMs such as Llama 3, both their pretraining and posttraining data are not open to the public, making it difficult to mix the finetuning data with the models' own pretraining data as a solution for mitigating forgetting.
We propose label annealing, a method that mitigates forgetting during finetuning without requiring access to the original pretraining data.
Label annealing distills pretraining knowledge during finetuing by adding a KL divergence term in the loss function, regularizing the divergence between the finetuned model's predictions to those of the initial pretrained model.
In mathematics and code finetuning, label annealing improves the model's performance in target domains without sacrificing other capabilities of the pretrained model.
In alignment finetuning, our method introduces a smooth tradeoff between the instruction-following capability and the pretraining knowledge.
We complement our empirical investigation with a mathematical model with overparameterized linear regression that provides geometric intuition why label annealing would help.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the idea of label annealing, which is designed to reduce the problem of forgetting knowledge that was learned during pretraining, as part of finetuning.  This is specifically done without having access to the original pretraining data, as is common in a lot of modern practice, e.g. with the LLaMa open-weight models and that precludes direct application of techniques such as experience replay.  The idea here is to keep an independent frozen version of the pretrained model and penalize the finetuning with a relative entropy term between that and the finetuned model with respect to predicted token probabilities.  The validity of this approach is demonstrated through fairly extensive experiments.

### Strengths
The paper is motivated by the very practical concern of preventing forgetting as part of the finetuning process in a sociotechnical setting where the pretraining data is not known (or perhaps can only be approximated as in the RedPajama dataset).  As such, any solution in this direction is useful.

The approach is straightforward, backed by basic theoretical explanation, and directly implementable.

Sections 1 and 2.2 are quite clearly written.

### Weaknesses
The experimental section is extensive, but also sometimes hard to understand what exactly is demonstrated by the results.  Indeed, in many of the tables, the finetuning doesn't seem to help in advanced benchmarks such as in math.

### Questions
What, specifically, are the advantages of the proposed technique that the experiments show?  Is it the ability to have a smooth tradeoff curve between the pretrained and finetuned settings?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the issue of catastrophic forgetting in large models during finetuning, specifically when capabilities such as in-context learning are lost. The authors propose a method called “label annealing” to mitigate this issue without needing access to the original pre-training data. This is achieved by incorporating a KL divergence term in the loss function to keep the finetuned model close to the pre-trained model. It would be valuable to discuss how this method compares directly to simpler approaches, such as parameter merging.

### Strengths
- The problem of knowledge forgetting during instruction finetuning is important.
- The paper provides solid theoretical analysis.

### Weaknesses
 - The paper is difficult to read due to numerous grammatical errors and typos. These issues detract from the overall clarity and academic tone. For example:
	- Line 133: “more effectove” should be corrected to “more effective.”
	- Line 136: The phrase “Label smoothing is similar to our proposal is that…” should be revised for clarity, perhaps to “… is similar to our proposal in that…”
	- Several sentences, such as those on Lines 167, 175, 202, 205, and 215, are unclear or poorly constructed. These should be reorganized into concise, well-structured parts.
- The proposed use of KL divergence is not particularly novel, as similar techniques have been widely used in instruction finetuning [1] and model alignment (e.g., DPO). More differentiation from existing methods is needed.
- The rationale behind addressing forgetting issues by potentially mixing pre-training and instruction data is not well justified. In real-world implementations like Alpaca, UltraChat, Wizard, and OpenChat, researchers tend to focus on building more diverse instruction datasets rather than revisiting pre-training data. There are also many works on mixing general and specific instruction for instruction tuning [2-3].
- The paper does not provide sufficient examples to demonstrate the benefits of retaining general knowledge obtained during pre-training. This is especially problematic given that retaining knowledge could lead to conflicts and potentially degrade performance on target-domain tasks, as seen in results like Table 2. Additionally, while the concept of alignment tax is mentioned, the paper does not address the potential impact on performance for source tasks like MMLU and TriviaQA during instruction tuning.
- There is no comparison with model merging techniques such as ExPO [4], which would be relevant for a comprehensive evaluation of the proposed approach.

### Questions
- Since the pre-training data for LLaMA is not publicly available, have the authors considered using open-source datasets like fine-web [1] as a substitute? It would be helpful to know if the proposed method outperforms simply using pre-training data directly.
 - The claim in Line 235 that “a fixed set of training hyperparameters” is used seems problematic. Instruction tuning is sensitive to hyperparameter choices, and results should ideally be supported by a thorough grid search to ensure reliability.
- The additional KL loss term likely increases the overall training cost. The authors should address how this cost is managed or justified.
- What is the size of the data generated for math/code finetuning? It’s important to consider whether scaling the instruction size could negate the differences between finetuning strategies.
- The method appears less effective than direct finetuning for tasks like HumanEval. What specific advantages does the label annealing method offer for domains like math, if performance gains in target domains are more critical than knowledge retention?

[1] Penedo, Guilherme, et al. "The fineweb datasets: Decanting the web for the finest text data at scale." arXiv preprint arXiv:2406.17557 (2024).

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper provides a solution to the forgetting of pre-training knowledge assuming that pre-training data is unavailable by using label annealing. This method adds a KL divergence term to the loss and regularizes the divergence of the fine-tuning model's predictions to those of the initial model. There are both empirical examples when fine-tuning on different domains, like math and code, instruction fine-tuning, as well as a mathematical intuition for why the solution mitigates forgetting.

### Strengths
-The paper offers a novel method to mitigate forgetting using regularization.

-The paper does a great job of motivating the problem and showing how direct fine-tuning leads to forgetting, as well as shows both empirical and mathematical motivation.

-It was really good to compare how this method works both for scenarios where knowledge might be repeated as well as where knowledge is less likely to be repeated, and thus fine-tuning cannot rely on repeated pre-training data.

### Weaknesses
-Section 3.2: The method is compared to L2-regression, but for a complete comparison, there should be other commonly used penalty based methods (e.g. EWC (Kirkpatrick et al. 2017)). Specifically, the comparison should include methods that, like EWC, use a Fisher information matrix to selectively penalize changes to parameters important for previous tasks. This would provide a more robust understanding of the advantages and disadvantages of the proposed KL divergence regularization.

-Section 3.3: There are no baselines apart from direct fine-tuning. It would be especially motivating to add other penalty based methods where the hyperparameter can be altered to show the same type of curve and offer direct comparison. For example, a comparison with a method like EWC where the penalty term is scaled by a hyperparameter would be useful. This would allow for a direct comparison of the forgetting curve and show how the proposed method compares to other regularization techniques.

-The method requires loading 2 models into memory at once for each step (the initial model and fine-tuning model). As commonly used LLMs get larger for many language tasks, scaling this may become impractical. The memory overhead of maintaining two models, even if one is frozen, could be a significant limitation, especially when considering the computational resources required for large language models. This could limit the applicability of the method in resource-constrained environments.

-Table 3: It would be helpful to add the results of only using label annealing for direct comparison. This would isolate the effect of the label annealing component of the loss function and provide a clearer understanding of its contribution to the overall performance.

### Questions
-It is surprising that L2 regularization does not maintain past task performance with optimal hyperparameter selection. In Table 1, does changing the hyperparameter on the regularization term not allow the model to retain past task information better? 

-It is interesting that in Table 3, using replay improves math performance even more so than direct fine-tuning. Does this imply that math data was perhaps part of the pre-training, and thus replaying it allows the model to do better on the current math fine-tuning task?

### Soundness
4

### Presentation
3

### Contribution
3
