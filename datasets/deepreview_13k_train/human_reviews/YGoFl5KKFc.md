# Locking Down the Finetuned LLMs Safety

- Decision: Reject
- Scores: 5, 3, 6, 5

## Abstract
Fine-tuning large language models (LLMs) on additional datasets is often necessary to optimize them for specific downstream tasks. However, existing safety alignment measures, which restrict harmful behavior during inference, are insufficient to mitigate safety risks during fine-tuning. Alarmingly, fine-tuning with just 10 toxic sentences can make models comply with harmful instructions. We introduce SafetyLock, a novel alignment intervention method that maintains robust safety post-fine-tuning through efficient and transferable mechanisms. SafetyLock leverages our discovery that fine-tuned models retain similar safety-related activation representations to their base models. This insight enables us to extract what we term the Meta-SafetyLock, a set of safety bias directions representing key activation patterns associated with safe responses in the original model. We can then apply these directions universally to fine-tuned models to enhance their safety. By searching for activation directions across multiple token dimensions, SafetyLock achieves enhanced robustness and transferability. SafetyLock re-aligns fine-tuned models in under 0.01 seconds without additional computational cost. Our experiments demonstrate that SafetyLock can reduce the harmful instruction response rate from 60\% to below 1\% in toxic fine-tuned models. It surpasses traditional methods in both performance and efficiency, offering a scalable, non-invasive solution for ensuring the safety of customized LLMs. Our analysis across various fine-tuning scenarios confirms SafetyLock's robustness, advocating its integration into safety protocols for aligned LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
It is now well known that fine-tuning language models comes with a safety compromise [R0-R4], i.e., the safety alignment gets disturbed when a safety-aligned model is tuned to learn something new. This paper introduces SafetyLock, a method designed to maintain safety alignment post-fine-tuning. For the top-K heads in the model, a safety direction is computed using a preference-style safety dataset. The top-K heads are identified based on the quality signals they provide for safe-unsafe text classification. In the fine-tuned model, the safety vector of these top-K heads is added to the output of attention computations before the up-projection layer. Overall, the method appears sound and is shown to preserve harmlessness on Llama-3-8B, 70 Instruct, and Mistral-Large-2 123B when tested on three risk levels: benign, explicit, and implicit harmful datasets.

### Strengths
**Strengths**

- The paper proposes a new idea to prevent safety compromise owing to downstream fine-tuning of the model. While there are existing safety vector-based approaches to prevent safety compromise (with comparable memory and time footprint), the activation-based safety vector computation is a novel contribution.

- The experiments are sound, demonstrating the method's effectiveness in mitigating safety issues across various risk levels, including explicitly harmful, implicitly harmful, and benign datasets. Additionally, the method preserves most of the model's generic utility.

### Weaknesses
 **Weaknesses**

- The paper largely ignores comparisons with a line of closely related work, beginning with "Language models are Homer Simpson! Safety re-alignment of fine-tuned language models through task arithmetic," (R1) which also introduced the concept of a *safety vector*. Therefore, I do not agree with the claim, *"we are the first to consider locating safety vectors and then restoring the safety of fine-tuned LLMs using an inference-time intervention method,"* as there are a series of similar existing methods, such as R1-R4, and more within this line of research. These methods also use safe-unsafe pairs to derive a safety vector. I suggest the authors properly cite and compare their work with these studies. The current framing of the contribution is misleading given the existing body of work on safety vectors and their application in fine-tuned models. The paper needs to clearly delineate how the proposed method differs from existing approaches in terms of both the technical implementation and the conceptual framework. Specifically, the activation-based safety vector computation, while presented as novel, needs a more thorough justification of its advantages over existing methods that use weight-based or other forms of vector derivation. The lack of a detailed comparison makes it difficult to assess the true innovation of this work.

- The experiments demonstrating the utility of the method are limited. I understand that works like Qi et al. (2023b) [R0] largely rely on three risk categories, which is sufficient to prove that the problem of safety compromise due to fine-tuning exists. However, solving the problem would require more substantial evidence than relying on a similar set of experiments. It would be beneficial to see the method applied across different fine-tuning domains (such as math, code, and various other tasks) and observe the domain-specific performance with and without the safety measures. For instance, fine-tune on GSM8K, evaluate the test-set performance post task-specific tuning with and without the safety lock, and compare these results with those of related works. The current evaluation focuses primarily on safety metrics across different risk levels, which, while important, does not provide a complete picture of the method's impact on the model's overall utility. The paper should include a more comprehensive evaluation that examines the trade-off between safety and performance across a diverse set of tasks and domains. This would provide a more robust assessment of the method's practical applicability and limitations.

### Questions
1) Can you explain the need for the standard deviation of activations $\sigma_l^h$ in equation 4? Any experiments that show with and without $\sigma_l^h$ effect?

2) Can you please elaborate on section 4.5? The setting and motivation aren't very clear to me.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method to identify safety-relevant attention heads, interpreted as the model's safety mechanism. Furthermore, experiments are conducted to verify the effectiveness of these safety heads and their transferability across models.

### Strengths
1. They implement the method of ITI [1] on the safety of LLM and verify the effectiveness of the safety head.

2. Experiment results show the existence of safety heads and can efficiently enhance models' safety on different models.



[1] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model, NeurIPS 2023

### Weaknesses
1. The method is not novel. It totally follows the method in ITI [1] without considering the properties of safety itself, which influence the accuracy of the analysis.  (1) As noted in the abstract (line 14), only 10 sentences can compromise the models' safety mechanisms. However, as illustrated in line 193, the safety components in LLMs are composed of three-fourths for both LLama3-8b and LLama3-70b. If the safety mechanism is easily breached, it may be due to a relatively small number of parameters. (2) The head is not a fine-grained aspect of analysis, as there are papers exploring neuron-level safety mechanisms [2]. Additionally, the feed-forward layer is important for safety, as models may refuse to extract harmful knowledge and only extract safety knowledge such as "Apologize I can not ....." [3]. However, the paper ignores this and focuses solely on heads in self-attention.

2. The analysis is not comprehensive. Figure 2 examines the "safety direction" at layer 31, the final layer of LLama3-8B. This analysis is biased, as it only evaluates the output of different models. It's expected that embeddings will have some relation or differences because the models' outputs vary. What would be more valuable is an analysis of the intermediate layers, exploring how the mechanism identifies and mitigates harmful information. However, the paper lacks further analysis, which would have been interesting.

3. The experiments in Table 1 lack baselines, and the baselines in Figure 5 are all trivial. It’s important to compare lightweight defense methods, such as [4], to demonstrate the effectiveness of your approach.

### Questions
In Section 4.1, you mentioned that the learning rate is set to 2e-5. I'm curious about the effect of this learning rate on the experimental results. A learning rate of 1e-6 is typically used for continued pretraining, which has a smaller impact on model performance including general capability and safety alignment.

### Soundness
2

### Presentation
3

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
This paper introduces SafetyLock, a method to ensure the safety of LLMs post-fine-tuning, addressing the risks that traditional alignment measures fail to mitigate. SafetyLock leverages the discovery that fine-tuned models retain safety-related activation patterns from their base models, allowing the extraction and application of Meta-SafetyLock directions to reinforce safety efficiently. Experiments show that SafetyLock significantly reduces harmful behavior, achieving a response rate reduction from 60% to below 1% with minimal computational cost, offering a scalable and robust solution for safer LLM customization.

### Strengths
1. The main contribution of this paper is to point out an important safety issue in distributing LLMs: How can we guarantee the safety of an LLM after we release it, where users can use fine-tuning to bypass its safety alignment. Although the proposed solution is less satisfied to the reviewer (See Weakness 1.), the reviewer admit the value of the research question itself.

2. This paper provides insights into the inner machanism of LLMs on safety.

### Weaknesses
1. Regarding the research question. The paper aims to propose a *lock* to ensure that the safety behavior of an released LLM would not be jailbreaked. To this end, the major drawback of the proposed method is that: the safety lock is applied to the LLM after fine-tuning, which means that the fine-tuned LLM should still be preserved and served by its original provider. This is effective for proprietary LLMs such as GPT-4, where the model checkpoint is still kept by the company even after fine-tuning via API. However, for open-sourced LLMs, such as LLaMA series, the proposed method failed as the provider cannot apply the safety lock to fine-tuned LLMs. I would expect a method which can by applied instantly before the release of the checkpoint and would protect the LLM from any unsafe modifications.


2. Regarding the methodology. The *safety direction* is calculated according to Eq.3, which involves the direct comparison between two different sentences. I would suspect the rationality of the comparison. For example, if the last 3 tokens of the safe reponse is *I can't answer* and the last 3 tokens of the unsafe response is *make a bomb*. The comparison between `I` and `make`, `can't` and `a`, and `answer` and `bomb` does not make sense. The meaning of the last $r$ tokens is not strictly aligned between the safe and the unsafe responses. The author should give more explanations on this. Besides, there are different aspects to investigate the safety mechanism, such as activations of individual neurons that are closely related to safety behaviors. They are not fully explored.



3. Minor issues (Does not affect my scores)
    - Missing references. This paper should also survey papers for `LLM safety mechanism`, such as *A mechanistic understanding of alignment algorithms: A case study on dpo and toxicity*, *Finding Safety Neurons in Large Language Models*, etc.
    - Formats. Check the font of the sub-title in Figure 2. Also, the sub-title overlaps with the figures.
    - Line 296 - Line 297: 2e-5 --> $2 \times 10^{-5}$

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel approach, SafetyLock, to mitigate safety risks in fine-tuned large language models (LLMs). SafetyLock leverages the discovery that fine-tuned models retain similar safety-related activation representations to their base models, enabling the extraction of a Meta-SafetyLock, a set of safety bias directions. This allows for efficient and transferable safety alignment in fine-tuned models, reducing the harmful instruction response rate.

### Strengths
1. This paper discovers that fine-tuned models retain similar safety-related activation representations to their base models, so the safety directions computed from the original model remain effective when applied to the fine-tuned model.
2. SafetyLock reduces the harmful instruction response rate in fine-tuned models from 60% to below 1%, offering a scalable, non-invasive solution for ensuring the safety of customized LLMs.

### Weaknesses
Originality
1. The concept of safety-related directions  seems similar to previous works on concept activation vectors [1] and the design of  adaptive interaction on MHA is similar to [3] where the only difference lies in how to select the intervention heads. 

Quality
1. Will the choice of preference-style safety dataset (line 182) affect the identification of safety-related attention heads (line 188)? It would be better to verify the identified safety-related attention heads stay consistent no matter what safety dataset is selected. 
2. It is not clear why the element-wise multiplication between the standard deviation of activations and safety directions is needed. Although authors claim that std term captures the variability of the activations, previous works [1,2] only use the safety directions to intervention the model and achieve good performance. Thus, ablation study on std should be considered in this paper otherwise I may doubt whether this part of the design is redundant.
3. The number of chosen Top-K heads are different in different models. Authors claimed in Appendix D that SafetyLock’s intervention degree (K) has impact on model safety. Thus, the time used in the choice of K should also be considered in the method efficiency evaluation. 

Clarity
1. Line 308: citation of ICD may be wrong? Besides, the paper contains several duplicate citations (like Mengru Wang et al.), which should be checked and corrected.
2. Line 201: r is the number of final tokens considered, but how authors choose r? I checked the paper but didn’t find the clarification. If it is equal to the hidden size, such safety direction is the same with several previous works [1,2]. If not, whether the method performance is sensitive to r value should also be considered. 
3. Figure 2: captions of subfigures(b-d) have the extra spaces and captions of subfigures(e-g) are too close to the figure content.

### Questions
1. Would it be better to use the cosine similarity or JS divergence metric to make the quantitative analysis in Figure 2(e-g) since KL divergence is asymmetric?
2. How about the performance of SafeLock on XSTest since I noticed this dataset is evaluated in ICD baseline.

### Soundness
3

### Presentation
2

### Contribution
2
