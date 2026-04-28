# KNIFE: Distilling Reasoning Knowledge From Free-Text Rationales

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3

## Abstract
Language models (LMs) have yielded impressive results on many language reasoning tasks, but their unexpected errors raise doubts about their reasoning abilities.
In light of this, there is growing interest in finetuning/prompting LMs with both task instances and their associated free-text rationales (FTRs), which explain the correct reasoning process for predicting the correct task output (\ie how to be ``right for the right reasons'').
However, existing finetuning methods fail to improve LM performance, while prompting needs prohibitively large (\ie >50B) LMs to work well.
We propose \method, which shows that reasoning knowledge can be effectively distilled from FTRs into a small (\ie <1B) LM and improve the LM's performance.
First, \methodsp finetunes a teacher LM (given task input and FTR) to predict the task output, transferring reasoning knowledge from the FTRs to the teacher's hidden states.
Second, \methodsp finetunes a student LM (given task input only) such that its hidden states are aligned with the teacher's.
Thus, the student is endowed with reasoning knowledge but can be used for inference without direct FTR input.
On two question-answering datasets, \methodsp outperforms various finetuning and prompting baselines in fully-supervised and low-resource settings.
Also, we observe that FTR quality is crucial to \method's performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces KNowledge DIstillation From Free-Text RationalEs (KNIFE) as a method to effectively distill the reasoning knowledge from a large Language Model (LM) to a smaller LM, aiming to enhance the smaller LM’s task performance. Specifically, the teacher model is fine-tuned to predict the answer based on the task input (question) and the pre-defined free-text raionales associated with each training data. Then, the hidden states of the encoder and output prediction distribution are used in knowledge distillation, transferring knowledge from the teacher model to the student model. Experimental results indicate that KNIFE is effective compared to the fine-tuning variants thanks to the knowledge distillation of both hidden states and output distribution.

### Strengths
- **New Approach to a Specific Problem;** The proposed method represents a novel approach to a specialized problem where either human-written or machine-generated free-text rationales are available, and the language model architecture is based on an encoder-decoder system like T5. As far as I am aware,  this particular issue hasn’t been addressed in previous works.
- **Thorough Analysis;** The authors conducted comprehensive experiments under various conditions, including two different sizes of LM architectures, two distinct datasets, varying input-output compositions, and FTR variants.

### Weaknesses
 - **Limited Contribution;** While I acknowledge the novelty and design of the prospoed method aimed at distilling reasoning knowledge from free-text rationales in encoder-decoder LMs, its contribution appears limited for several reasons:
    - The efficacy of the proposed method, KNIFE, seems marginal as the improvements are not statistically significant based on some results in Table 1. For instance, in the StrategyQA dataset, KNIFE’s performance is comparable to FT (I→RO), suggesting that simple fine-tuning of the language model with FTR and using the answer as the target yields results similar to KNIFE. Additionally, the experimental results suggest that distilling from T5-Large to T5-Base is less effective than from T5-Base to T5-base, which is weird.
    - The application scope of the proposed method is restricted both in task type and language model architecture. It’s only suitable for multi-choice QA tasks when free-text rationales are available and is exclusive to LMs with encoder-decoder architecture like T5, making it unsuitable for decoder-only models like Llama.
    - The individual contributions of each component in the proposed method remain ambiguous. In Tables 8 and 9, KNIFE with either KD-in loss only or KD-out loss only occasionally outperforms KNIFE with both objectives combined. This raises the question: is employing both objectives truly advantageous?
- **Limited significance of the Problem;** Lately, there have been significant works [1,2,3] into distilling the reasoning ability of large LMs (e.g., Llama-2 or GPT-3.5-turbo) into smaller LMs. Given this context, how does the proposed method compare to existing approaches? In Appendix A.1., the authors posit that their method is advantageous when large-scale LMs lack reasoning abilities, a premise that seems out of sync with current trends in large language models.

### Questions
1. What is the advantage of this work compared to recent CoT distillation works mentioned in the second point of weaknesses?
2. Why do the authors not include results with In only and out only in Table 1? I think this baseline is important to show the significance of using both objectives in KNIFE.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes KNowledge dIstillation from Free-text rationalEs (KNIFE), a distillation method that leverages open-source pretrained seq2seq models and training data with free-text rationale (FTR) annotations to develop an accurate question-answering prediction model. It first finetunes a teacher LM to input question and FTR and output the answer. Then it finetunes a student to input the question and output the answer, while aligning to the teacher's hidden states. The student outperforms finetuning and prompting baselines in fully-supervised and low-resource settings. The paper further shows that the FTR quality is important to the success.

### Strengths
- The scenario is likely: there are rationale annotations for training data, but these annotations are not readily available at test time.
- The method is intuitive and effective. The bottleneck architecture has novelty.
- Compared with multiple baselines and performed careful ablation study.

### Weaknesses
 - The paper is about classification and shows advantages on two datasets. Results on more tasks will be helpful for showing the generality of the method. Does the method work for reasoning tasks commonly used by the chain-of-thought literature, such as, arithmetic reasoning, commonsense reasoning, and code generation? Does it work for knowledge-intensive tasks?
- The paper doesn't have a retrieval-augmentation baseline. Will the numbers look better if you finetune T5 to learn to condition on retrieved (question, rationale, answer) demonstrations, instead of distilling rationales from text to a teacher and then to a student?

### Questions
Please refer to the Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the idea of distilling knowledge from free-text explanations. They start by training a "teacher" model, which learns to make predictions using both the free-text explanations and task inputs. This helps the teacher model absorb the knowledge from the free-text explanations into its hidden state. Next, they build a "student" model and make sure its hidden state aligns with the teacher's, all without directly using the free-text explanations. They then put their models to the test on two question-answering tasks, comparing them to various baseline models with different fine-tuning and initialization approaches. Impressively, their models outperform these baselines. Additionally, they carry out an ablation study to understand how different parts of their model contribute to its success.

### Strengths
They study the idea of knowledge distillation from free-text rationales and did comprehensive experiments to show the effectiveness of the approach.

### Weaknesses
 * The idea behind this approach isn't very convincing. The teacher model can't store a lot of knowledge, and it might not work well for different tasks. Plus, it's unclear how this method is better than retrieval-augmented generation.
* To prove its effectiveness, more experiments should be done, comparing it to retrieval-augmented generation and testing it on various downstream tasks.
* The improvement from introducing free-text rationale into the teacher model isn't substantial, and it might be because of the extra knowledge.
* Their best model still falls far short of the Large Language Models (LLM) by a significant margin, and the student model doesn't seem to improve model explanation and reasoning.

### Questions
1. What is the upper-bound performance achievable by the small model when given the task input and free-text rationale together?
2. How does this approach compare favorably to "retrieve-augmented-generation," a method that initially retrieves relevant knowledge, such as free-text rationales, and then enhances the input with this retrieved knowledge?
3. Why does incorporating the free-text rationale during the teacher model's fine-tuning enhance the student model's performance? It's possible that the improvement shown in Figure 3(a) is due to the extra knowledge contained in the free-text rationale, which could be beneficial for the downstream tasks. This improvement, while not substantial, might not generalize well to scenarios with less overlap in knowledge or when using larger free-text rationales for teacher model fine-tuning. This raises questions about the broader applicability of this approach.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
