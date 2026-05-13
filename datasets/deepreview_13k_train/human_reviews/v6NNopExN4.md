# POST: A Framework for Privacy of Soft-prompt Transfer

- Decision: Reject
- Scores: 6, 5, 6, 3

## Abstract
Prompting has emerged as a dominant learning paradigm for adapting large language models (LLMs). While discrete (textual) prompts prepend tokens to the input for optimized outputs, soft (parameter) prompts are tuned in the embedding space via backpropagation, requiring less engineering effort. However, unlike semantically meaningful discrete prompts, soft prompts are tightly coupled to the LLM they were tuned on, hindering their generalization to other LLMs. This limitation is particularly problematic when efficiency and privacy are concerns, since (1) it requires tuning new prompts for each LLM which, due to the backpropagation, becomes increasingly computationally expensive as LLMs grow in size, and (2) when the LLM is centrally hosted, it requires sharing private data for soft prompt tuning with the LLM provider. To address these concerns, we propose a framework for Privacy Of Soft-prompt Transfer (POST), a novel method that enables private soft prompt tuning on a small language model and then transfers the prompt to the large LLM. Using knowledge distillation, we first derive the small language model directly from the LLM to facilitate prompt transferability. Then, we tune the soft prompt locally, if required with privacy guarantees, e.g., according to differential privacy. Finally, we use a small set of public data to transfer the prompt from the small model to the large LLM without additional privacy leakage. Our experimental results demonstrate that our method effectively transfers soft prompts, protecting local data privacy and reducing the computational complexity over soft prompt tuning on the large model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Prompt tuning, the process of optimizing the prefix tokens (hard) or their embeddings (soft) to improve the utility of a downstream task has become one important way of adapting Large Language Models (LLMs). Traditional soft prompt tuning paradigms require backpropagation through the full model, which is computationally expensive to perform on-premise, or handing the private data to a central LLM provider, which could lead to privacy concerns. To reduce the computational overhead of local soft prompt tuning while preserving privacy, the authors propose Privacy Of Soft-prompt Transfer (POST), which performs soft prompt tuning on a small local LLM distilled from a large LLM and transfers the soft prompt to the large model with th help of public data. In addition, the proposed framework can also be coupled with differentially private prompt tuning techniques to achieve privacy guarantees. To validate their proposed method, the authors evaluate the transferability of soft prompts finetuned on small models distilled from Roberta-base, GPT2-XL, and Llama2-7b for classification tasks.

### Strengths
The setting of the paper is well-motivated. The introduction sections and the figures clearly explain the setting and the proposed methods.

### Weaknesses
1. While the paper presents an appealing middle ground by performing prompt finetuning on a distilled proxy model, the evaluations are performed with a fixed set of proxy models. As briefly mentioned by the authors, in the case of the centralized LLM provider, the utility of the distilled model should ideally be not strong enough to replace the original model but is still good enough to serve as a proxy for prompt finetuning. However, the authors do not further explore the trade-off between the quality of the proxy model and the effectiveness of the proposed pipeline. Specifically, the paper lacks an analysis on how the size and performance of the distilled model impact the transferability of the learned soft prompts. It is unclear how much performance degradation is acceptable in the distilled model to still achieve effective transfer. This is a crucial aspect for practical applications where the computational cost of the distilled model needs to be balanced with the transfer performance.
2. The evaluation of the proposed method mainly focuses on classification tasks, which have limited practicality given that modern autoregressive LLMs can perform open-ended generation tasks. While I recognize that prior works also mainly focus on classification tasks, I encourage the authors to discuss the applicability of the proposed method on open-ended tasks, or even better, demonstrate such ability through follow-up experiments. The current evaluation does not fully demonstrate the potential of the proposed method for more complex and practical scenarios.

### Questions
1. I appreciate the authors discussing the runtime of POST v.s. Full PT in Table 3, but I have some questions regarding the costs of the distillation step. While the distillation costs of a large LLM can be amortized as we finetune more soft prompts with the distilled LLM, could the authors quantitatively compare the computational overhead of finetuning one soft prompt on the large LLM to that of distilling the large LLM and finetuning one soft prompt on the distilled LLM?
2. The authors use a fixed set of distilled models throughout the paper. How does the quality of the distilled model influence the transferability?
3. Could other model compression techniques like pruning and quantization be used in this framework instead of model distillation?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a framework for Privacy Soft-Prompt transfer to reduce the computation cost and potential privacy leakage. The framework mainly contains three steps as deriving SLM using knowledge distillation, locally prompt tuning, and prompt transferring using public dataset.

### Strengths
1. The author proposed a novel framework for transferring soft prompts between SLM and LLM, and achieved completive results on the test dataset
2. The paper brought focus on the privacy and efficiency issue on prompt tuning, and tried to reduce the privacy leakage and computational cost.

### Weaknesses
1. The paper writing needs to be improved. For example, the author does not clearly represent whether POST needs the original input x during the inference. If so, this may lead to privacy concerns. I mean, in tasks like classification, the LM input contains privacy information.
2. The paper needs to be clear about the setting. For black-box LMs, they cannot provide the service as giving a SLM through KD. If the author means for white-box LMs, they author should further explain why there is privacy concerns.
3. For the experiment, I think other tasks in spite of classification help improve the credibility. For tasks as classification, the LM input contains privacy information which violates the setting in this paper. For other tasks as Q&A, the soft prompt may contains privacy information and the model inputs may have less privacy concerns, which is consistent with the setting in this paper.

### Questions
1. I wonder whether the framework needs the original input during evaluation. If so, the model input may contains privacy information.
2. For the setting, could you please give further explanation about whether it is white or black box?
3. Could you please provide more evidence (citations, or experiments) to confirm the claim“soft prompts are highly coupled to the LLM they were tuned on, making them difficult to transfer”?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors proposed a new framework that allows the users to perform private soft prompt tuning without accessing the original protected LLMs without leaking their private data. They proposed to  first obtained a distilled model from the original LLM, a step needed from the LLM provider, and then the users will utilize this distilled model to perform soft prompt tuning and transfer the resulting soft prompt to prompt the original LLM. They conducted a few experiments to demonstrate the performance of their proposed framework and compare it with several baselines.

### Strengths
The paper studies a very interesting problem and proposed a novel framework to allow users to “perform soft prompt tuning” without revealing their private data and LLM providers not revealing their protected LLMs. The most novel part comes from privacy-preserving prompt transfer through public data, which largely protect data privacy and maintain inference performance.

### Weaknesses
I listed a few weaknesses below:
1. It is unclear how to select public dataset for prompt transfer, there is no guidance on how to select such a public dataset and how would the selection of public dataset affect the performance. From their experimental results in Table 1, it seems like different selection would make a large enough impact on the inference accuracy.
2. No explanation on what would be the termination criterion for knowledge distillation step. The authors described that the distilled model should behave closely to the original model but not meeting the actual inference performance of the original model, which is too vague. I do not see either the ablation studies on how to select $\alpha_{ce}$, $\alpha_{lm}$ and $\alpha_{cos}$.

Overall, the main concern is that the proposed method contains many steps involving hyperparameters and public datasets need to be tuned and selected. More ablation studies and further theoretical analysis are needed to understand the general practical performance of the proposed method.

### Questions
1.	No ablation study is found for the selection of different value of $\alpha$ in Eq. (3).
2.	How to select a public dataset used for prompt transfer? From Table 1, it seems like sometimes selecting a different public dataset affects the final test accuracy a lot.
3.	Other than next word prediction task, does the proposed method perform well on other language task? For example, question answering and reading comprehension?
4.	Why there is no result for llama2-7b in Table 2?
5.	When comparing to the status of the art baselines, it seems like larger models have better zero-shot performance. In this case, in Table 4, can you include more results on larger models like llama2?
6.	From Fig. 5, it seems like the attack success rate is low even without DP. In this case, would that be the MIA algorithm used in the paper is not good enough? It seems like there is no motivation to add DP to protect private data.  
7.	If the original LLM is mixture of expert model, does the proposed framework apply to that case?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies the problem of differentially private soft prompt tranfer. They propose the POST framework which consists of 3 steps: 1) The LLM provider compresses their model into a smaller model using techniques in knowledge distillation and then sends the distilled model to the user. 2) The user performs private prompt tuning using PromptDPSGD (Duan et al., 2024) on the distilled model. 3) The user transfers this prompt on the large LLM.

### Strengths
The related previous work and key concepts (e.g., prompt tuning, differential privacy, knowledge distillation, prompt transfer) are clearly explained. The proposed algorithm is described in detail.

### Weaknesses
1, Motivation Unclear: This paper focuses on privacy-preserving soft prompt transfer, where the LLM provider is untrusted. Could you provide examples of closed-source LLM providers that support soft prompts? If, instead, the LLM provider is an open-source model that can be run locally (e.g., GPT-2 XL or Llama-2-7b, as mentioned in this paper), privacy concerns could potentially be mitigated by running the model locally. Could you clarify the motivation behind the need for privacy-preserving transfer in this context?


2, Novelty Concerns: Given the existing work for knowledge distillation (Sanh et al., 2019) and PromptDPSGD (Duan et al., 2024), what is the technical novelty in this paper?


3, Practical Concern: The proposed approach involves the LLM provider performing knowledge distillation to compress their LLM into a smaller model and then sending this distilled model to the user. Is this practical? It’s unclear if an LLM provider would be willing to share a distilled model, given proprietary concerns, and risks of potential attacks. 

4, Missing DP Guarantee: I recommend including a formal theorem that states the DP guarantee of the proposed method, and a proof to ensure the privacy guarantee is rigorously supported.



5, Missing Experimental Details: The value of $\delta$ used in this paper should be mentioned in the main paper. What is the standard deviation of the results in Table 1, 2 and 4? 


6, Some Typos:

(1) Line 117: fist $\rightarrow$ first.

(2) Line 119: There’s an extra comma.



(3) Line 132: from student to teacher $\rightarrow$ from teacher to student.


(4) Line 256: $\mathcal{N}(0,\sigma^2 c^2)\rightarrow \mathcal{N}(0,\sigma^2 c^2 \mathbf{I})$

### Questions
1. I don't understand the statement in this paper ``KD has been shown effective to compress LLMs during the pre-training phase while maintaining
their performance (Sanh et al., 2019)". The cited paper discusses BERT, which is not typically recognized as an LLM. Could you clarify this point? Additionally, can all types of LLMs (e.g., GPT, Llama, Mistral) be effectively compressed using knowledge distillation?



2. This paper considers two baselines, namely DP-OPT (Hong et al., 2023) and Zero-Shot Transfer (Wu et al., 2023b). Hong et al. (2023) use the TREC, MPQA, and Disaster datasets, and Wu et al. (2023b) consider the LAMA dataset. It is unclear why these datasets are not included in the experiments of this paper. Could the authors also include these datasets in the experiments?

### Soundness
2

### Presentation
3

### Contribution
2
