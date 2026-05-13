# An Emulator for Fine-tuning Large Language Models using Small Language Models

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Widely used language models (LMs) are typically built by scaling up a two-stage training pipeline: a pre-training stage that uses a very large, diverse dataset of text and a fine-tuning (sometimes, `alignment') stage that uses targeted examples or other specifications of desired behaviors. While it has been hypothesized that knowledge and skills come from pre-training, and fine-tuning mostly filters this knowledge and skillset, this intuition has not been extensively tested. To aid in doing so, we introduce a novel technique for decoupling the knowledge and skills gained in these two stages, enabling a direct answer to the question, \textit{What would happen if we combined the knowledge learned by a large model during pre-training with the knowledge learned by a small model during fine-tuning (or vice versa)?} Using an RL-based framework derived from recent developments in learning from human preferences, we introduce \textit{emulated fine-tuning (EFT)}, a principled and practical method for sampling from a distribution that approximates \rev{(or `emulates')} the result of pre-training and fine-tuning at different scales. Our experiments with EFT show that scaling up fine-tuning tends to improve helpfulness, while scaling up pre-training tends to improve factuality. Beyond decoupling scale, we show that EFT enables test-time adjustment of competing behavioral traits like helpfulness and harmlessness without additional training. Finally, a special case of emulated fine-tuning, which we call LM \textit{up-scaling}, avoids resource-intensive fine-tuning of large pre-trained models by ensembling them with small fine-tuned models, essentially \rev{emulating} the result of fine-tuning the large pre-trained model. Up-scaling consistently improves helpfulness and factuality of instruction-following models in the Llama, Llama-2, and Falcon families, without additional hyperparameters or training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a sampling method to evaluate the effects of different scales of pre-training and fine-tuning, which proves larger pre-training and small fine-tuning datasets are better. Also, it provides an ensembling strategy for different models at different scales, which seems inspiring that the up-scaling technique can approximate the compute-intensive result of large models without extra resources.

### Strengths
1. The proposed emulated fine-tuning framework can approximate the results without associated computational expense, and prove the helpfulness and factuality of each procedure.
2. The up-scaling technique can approximate the results of compute-intensive models, however, without the associated computational expense.

### Weaknesses
1. The paper is not easy to follow. More important details are needed for understanding and reproduction. For EFT, how the sampling is conducted?  Does different scales affect the sampling strategy? For the ensembling, how the new weights are obtained? 
2. It claims that up-scaling can approximate the results of compute-intensive models, which need more experiments and comparison.

### Questions
Please refer to the weakness part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to decouple the fine-tuning and pre-training in an LLM by the reinforcement learning theory. By specifying the enhancement from fine-tuning based on the pre-training, it is possible to introduce the enhancement of smaller models to the larger ones so as to reduce the commuting cost of fine-tuning a large model. This approach is called emulated fine-tuning by the authors. The idea of EFT is tested with different LLM families and evaluated by GPT-4 by measuring the harmfulness, helpfulness, and factuality.

### Strengths
The paper provides a theoretical explanation of a simple framework that can greatly reduce the computing cost of pre-training large language models. By incorporating the pre-training of smaller models, we can use the EFT to get an enhanced performance with larger models. The enhancement is evaluated by GPT-4 by measuring the harmfulness, helpfulness, and factuality. The reinforcement learning theory is convincing and clear to demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The evaluation is limited. Fine-tuning is widely used and not only limited to obtaining a chatbot. More tasks can be used to verify the idea of EFT, such as code generation, question-answering, etc.
2. Though GPT-4 is widely used as the judge to tell the performance of LLMs, more objective metrics can also be used to evaluate the LLMs.

### Questions
1. In Figure 3, the values in the chart are labeled but in Figure 4, the values are not. It would be helpful to know the explicit values in the charts.
2. As mentioned in Section 4: Models, three separate families of pre-trained language models are used. According to the theory introduced in Section 3, it is also possible to verify the idea across different families of PLMs. For example, what will the performance be when incorporating the knowledge learned by fine-tuning Llama-7b to Falcon-180?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces emulated fine-tuning (EFT) to combine the knowledge gained from pre-training and the knowledge gained from fine-tuning from different scales and provide mathematical intuition.
The experiment shows a larger fine-tuning scale improves helpfulness and a larger pre-training scale improves factuality.
The method leads to a resource-efficient fine-tuning method, combining a large pre-training scale with a small fine-tuning scale.

### Strengths
(1) The idea of pre-training and fine-tuning at different scales is very interesting. (contribution (a))

(2) The paper shows that a larger fine-tuning scale improves helpfulness and a larger pre-training scale improves factuality as Figures 3 and 4, which potentially provide intuition to guide fine-tuning methods. (contribution (b))

(3) The proposed method provides a testing-time flexibility to the trade-off of helpfulness and harmlessness.

### Weaknesses
 (1) In contribution (c), the paper kind of implies that the up-scaling is beneficial to efficiency, but what's the performance/inference cost comparison between inferencing the small model twice and Parameter-Efficient Fine-Tuning (PEFT) such as LoRA? If the proposed method cannot approach the performance/inference cost of PEFT, then it's hard to say it's more efficient.

(2) While the proposed method is evaluated with varied ablation studies, it seems that the method is not to be rigorously compared with directly fine-tuning the pre-trained model (combining different scales may or may not cause trouble to performance). If the proposed method cannot match the performance of directly fine-tuning the pre-trained model, then the study of contribution (b) would be less meaningful.

### Questions
I like the proposed idea very much, but I am concerned about the contribution of the paper. 

Performance-wise it's not clear whether combining different scales will lead to performance degradation. Efficiency-wise it's not clear whether it's better than Parameter-Efficient Fine-Tuning (PEFT). I understand the method provides a trade-off between helpfulness and harmlessness, and a method to explore the effects of pre-training and fine-tuning, but I think it's only meaningful when the performance is not degraded after combining different scales.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a method, emulated fine-tuning (EFT), to decouple the effect of the knowledge learned by a large model during pre-training and the knowledge learned by a small model during fine-tuning (or vice versa). Given a smaller pre-trained model $\pi_{ref}^{M}$, its fine-tuned counterpart $\pi^{M}$, and a larger pre-trained model $\pi_{ref}^{N}$, EFT emulate the effect of combining the pre-trained knowledge in $\pi_{ref}^{N}$ and the knowledge learned by $\pi^{M}$ by simply computing 
$\log \pi_{ref}^{N}(y|x) + (   \log \pi^{M}(y|x)     - log  \pi_{ref}^{M}(y|x) )$.

Using EFT, they show that scaling pre-training (model size) mostly improves factuality, and scaling fine-tuning (model size) mostly improves helpfulness. 
They also propose a special case of EFT that uses a large pre-trained model and two small models (one pre-trained and the other fine-tuned) called up-scaling, which can emulate the case when fine-tuning the large model without actually fine-tuning the large model.
They show that EFT can also be combined with speculative decoding to speed up the inference speed, and they use top-p truncation to improve the performance of up-scaling.

### Strengths
- EFT is motivated by prior observations that LLMs can be seen as a reward model. They use this observation to decouple the effect of the model scale for pre-training and fine-tuning. This is a very interesting interpretation.
- EFT is very simple to implement, and up-scaling can improve the pre-trained LLMs' performance without fine-tuning the large LLMs.
- The takeaway of the paper is very interesting.
- The evaluation of the paper is solid: they use GPT-4 evaluation and conduct further human evaluation to justify the validity if using GPT-4 as the evaluator.
- The paper is mostly easy to follow. The takeaways are clear and the experiment settings are clear too.

### Weaknesses
 - EFT requires three models during inference. Three models occupy a lot of space and lengthen the inference time. Still, the inference time can be reduced by speculative decoding. This makes me doubt the practical value of EFT and upscaling. 
- It is unclear how much up-scaling recovers the performance of fine-tuning the large model. The paper only reports the improvement of the up-scaled model compared with the pre-trained large model, but I think it is also important to report the performance of the fine-tuned large model. This way we can understand if up-scaling can close the gap of fine-tuning the large model, or if the performance still largely lags behind the fine-tuned large model. This is an important information for practical use cases. Still, I want to emphasize that this paper's contribution to proposing the EFT framework is ample contribution, and even if there are several drawbacks in practical usage, I still consider this paper a good paper.
- The math in Section 3 is kind of confusing. I will elaborate on them in the question part.
- Some minor presentation issues. The paper might need proofreading.
   -  Section 3.1:  ` we view the result of fine-tuning is the solution to` $\to$ `we view the result of fine-tuning **as** the solution to`.
   -  Section 3.1: `Crucially, while the EFT framework is justified with an RL interpretation is applicable to any fine-tuned model` $\to$ `Crucially, while the EFT framework is justified with an RL interpretation, **it** is applicable to any fine-tuned model`
   - Page 6: `with on` $\to$ `with`
   - Section 4: `While prompts in the HH dataset are more everyday and conversational, asking for movie recommendations or instructions or home maintanence tasks.` $\to$ This is not a complete sentence.
    - Section 4.3 and 4.4: I think you should first introduce the method and then refer to the experiment results in the tables.

### Questions
1. I am confused about the math in Section 3. 
  - 1.1 Why is the $r_{\pi}(x,y)$ on Line 6 in page 4 $\beta \log \frac{\pi_{ft}(y|x)}{\pi_{ref}(y|x)}$ instead of $\beta \log \frac{\pi_{ft}(y|x)}{\pi_{ref}(y|x)} + \beta \log Z(x)$?
  - 1.2 In Line 6,  $r_{\pi}(x,y) = \beta \log \frac{\pi_{ft}(y|x)}{\pi_{ref}(y|x)}$. But in the last part of Equation (3) and in the following texts, it seems that  $r_{\pi}(x,y) = \log \frac{\pi_{ft}(y|x)}{\pi_{ref}(y|x)}$. Why is there such a difference?

2. The paper mainly focuses on generation tasks related to factuality and helpfulness/harmlessness. I wonder does EFL, or precisely, up-scaling, also show improvement in multiple-choice datasets like MMLU?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
4 excellent
