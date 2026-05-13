# ShieldHead: Decoding-time Safeguard for Large Language Models

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
In light of the widespread deployment of Large Language Models (LLMs), the responsibility for safeguarding and regulating LLM-generated content has taken on heightened significance. Recent advancements in LLM-based moderation methods, e.g., LlamaGuard, have demonstrated remarkable promise in identifying safety risks associated with both inputs and outputs in human-AI interactions. However, integrating LLM-based safeguards into a chatbot system requires an additional inference stage involving a moderation LLM with billions of parameters, which significantly increases computational costs and reduces overall efficiency. In this paper, we demonstrate that simply learning a classification head on the last-layer hidden states of the dialogue model provides a strong capability to identify harmful contents. The classification head, referred to as ShieldHead, serves as an auxiliary branch paralleled with next-token-prediction LM head, enabling the detection of potential risks in past text sequences. Additionally, a label disambiguation technique is employed to supervise ShieldHead with both token-level and sentence-level labels, which further enhances its performance. ShieldHead exhibits remarkable efficiency during inference, providing real-time moderation results alongside token-wise streaming output during the chatbot system's decoding phase. Extensive experimental results demonstrate the superiority of the proposed framework: a state-of-the-art performance on the XSTest and SafeRLHF datasets while running at a speed about 300× faster (<1ms) than previous LLM-based moderation models with ～99% less parameters of LlamaGuard.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces ShieldHead, a classification head that operates on the last-layer hidden states of the dialogue model, enabling real-time identification of harmful content with significantly lower computational overhead. ShieldHead employs a label disambiguation technique to enhance performance and achieves state-of-the-art results on various datasets while being approximately 300 times faster than existing methods.

Key Contributions include 1) Real-Time Moderation: ShieldHead allows for real-time safety risk moderation during the decoding phase of chatbot responses, achieving less than 1 ms latency. 2) Efficiency: It utilizes only about 1.1% of the parameters of existing models like LlamaGuard, significantly reducing training and inference costs. 3) Performance: Extensive experiments demonstrate that ShieldHead outperforms existing moderation methods on multiple benchmarks, including XSTest and SafeRLHF datasets.

### Strengths
1. The authors propose a simple yet effective method called SHIELDHEAD, which relies on a classification head on the last layer of hidden states of the LLMs using the output of the head to classify. Compared to LlamaGuard, their method shows a speed about 300× faster (<1ms) than previous LLM-based moderation models with ∼99% fewer parameters of LlamaGuard.

2. This paper contributes an efficient safety risk moderation pipeline for LLMs, designed to deliver real-time results based on the token-level streaming output of an LLM.

### Weaknesses
1. The Equation 3 to Equation 10 is a bit wordy. The idea can be illustrated in a more concise way, for example,  the input prompt and the sentence-level classification result can be described in textual words.

2. The motivation of this work is not persuasive enough given the fact that the inference-time intervention method and model editing methods can both effectively enhance the model's safety by using much less computational cost. If the motivation is to build more effective methods for enhancing AI safety, it lacks the essential baselines to compare.

3. In the related work of SAFETY CONTENT MODERATION, the intervention-based methods and model-editing methods have been ignored. In terms of the safety, their methods' performance is competitive and should be mentioned here.

### Questions
Typos to be corrected: Line 487: ”steal” Line 488: ”not permissible to”

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
3

### Summary
The paper addresses the need for efficient and real-time content moderation for large language models. Traditional moderation methods either rely on non-parametric rule-based classifiers, which lack deep language comprehension, or LLM-based moderators, which offer high accuracy but are computationally intensive and time-consuming, requiring a separate inference stage. The paper proposed the ShieldHead unit, which is a lightweight, real-time content moderation system that uses an MLP as a classification head on the hidden states of an LLM's last layer, running after the LM head on each step. This setup enables token-level, real-time moderation without adding significant computational overhead.

### Strengths
1. **High Efficiency with Low Computation Cost**: ShieldHead achieves real-time moderation by using an MLP (instead of another LLM) to directly score the hidden states of an LLM's last layer, significantly reducing computation while largely maintaining the performance.
2. **Fine-grained Safety Detection**: ShieldHead improves moderation accuracy by performing token and sentence-level safety evaluation. This dual-layered approach allows for more fine-grained detection and demonstrates the interpretability of this method.

### Weaknesses
1. **Low Adaptability across Models**: From the description in the paper, ShieldHead needs to be trained from scratch for each language model, as the hidden-state distribution varies across different models. This requirement limits ShieldHead’s applicability, making it less suitable for wide-range use across diverse language models without substantial re-training. The paper does not explore methods for transfer learning or domain adaptation, which could potentially mitigate this limitation. The lack of discussion on how to handle the variability in hidden state representations across different architectures is a significant concern.
2. **Need White-box Access to the Upstream Model**:  ShieldHead requires access to the hidden states of the language model, implying a need for white-box access. This limits its use with models that do not allow such access or are deployed in environments where model internals are inaccessible. This dependence on internal model states makes it unsuitable for use with many commercial APIs or models that are only available as black boxes. The paper does not address the practical challenges of deploying such a system in real-world scenarios where access to model internals is often restricted.

### Questions
1. How well does ShieldHead handle contextually ambiguous terms at the token level, where the classification (safe or unsafe) depends heavily on the surrounding context? Although Section 3.6 provides a single example, it would be valuable to know if the authors conducted an ablation study specifically focused on that.
2. It would be helpful if the authors could provide more detailed evaluation data, since in safety-critical scenarios, false positives may be significantly more harmful than false negatives.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed a new framework, ShieldHead, that identifies the harmful contents on the sentence and token levels. They employ the label disambiguation technique to supervise model training with token- and sentence-level labels. In their experiments, they show the effectiveness of their method across diverse datasets and models. They also demonstrate the inference efficiency of their proposed framework.

### Strengths
1. The paper introduces a framework that can identify harmful contents on both sentence- and token-level. 
2. They utilize the label disambiguation method to automatically assign token-level labels based on sentence-level labels. 
3. They provide extensive experiments to evaluate the effectiveness of their proposed methods compared to LLMs and SOTA models for safety detection.

### Weaknesses
1. Lack of some model comparisons. For sentence-level classification, I expect they can compare to a model that is fully fine-tuned llama-3.1-8b on the WGTRAIN dataset. GPT-4 can use a few WGTRAIN samples as a few-shot in-context learning examples in the prompt. For the token-level evaluation, they should also compare to some baseline models, such as GPT-4. 
2. Lack of clarity on their token-level evaluation experiment. I wonder if they annotated sub-word tokens (split by llama model) or words. What is the annotation agreement? How do they assign labels when there are any disagreements between annotators? It is also weird to me that they annotate "all tokens following an unsafe token in the sentence were marked as unsafe." Again, they should also compare to some baseline models for token-level classification. I will ask more questions in the next section. 
3. Unclear on calculating inference speed. I wonder how they calculate the latency of GPT-4 which is an API-based LLM.

### Questions
1.  Do you annotate sub-word tokens (split by llama model) or words? What is the annotation agreement? How do they assign labels when there are any disagreements between annotators?
2. I wonder why "all tokens following an unsafe token in the sentence were marked as unsafe." in your token-level annotation. Does this result in a significant amount of unsafe tokens? What is the ratio between unsafe and safe tokens in your token-level test set? 
3. When you generate the token-level labels, does your method have the same behaviour that all tokens following an unsafe token in the sentence were marked as unsafe? 
4. Line 204, what is the value of K in your experiment?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a new approach to content moderation in Large Language Models (LLMs), called ShieldHead. This method uses the hidden states of a dialogue model to identify harmful content, which significantly reduces computational costs and increases efficiency compared to previous methods. ShieldHead operates in real-time, providing moderation results alongside the output of the chatbot system. It uses a label disambiguation technique to enhance its performance, learning from both token-level and sentence-level labels. The paper demonstrates that ShieldHead outperforms previous models in terms of speed and accuracy, achieving state-of-the-art performance on the XSTest and SafeRLHF datasets while using approximately 99% less parameters than previous LLM-based moderation models.

### Strengths
1) The authors introduce ShieldHead, a classification head that identifies harmful content by learning from the last-layer hidden states of the dialogue model. This method is efficient, providing real-time moderation results alongside token-wise streaming output during the chatbot system's decoding phase. 
2) The paper is clearly written, with a well-structured argument and clear explanation of the methodology and results. It provides a comprehensive overview of the current landscape of content moderation methodologies and the challenges and limitations of existing approaches.
3) The significance of the research lies in its potential to improve the safety and efficiency of LLMs. By providing real-time moderation results, ShieldHead reduces the likelihood of harmful content being exposed by AI chatbots.

### Weaknesses
1) The major concern is the novelty. The use of an extra head/classifier to identify specific content, in this case harmful content, is a common and conventional method used in past researches across various research topics. For instance, "Bottom-Up Abstractive Summarization Sebastian (Gehrmann et al., 2018)" uses a token-level classifier to select summarization tokens. In my view, the main innovation lies in the supervisory method for the classifier, referred to as label disambiguation in this study. The technique employs a moving-average to refresh class (safe/unsafe) prototype embeddings derived from the hidden features of each class samples. Nevertheless, aside from the ablation results, there doesn't seem to be any intuitive or theoretical backing for this approach.
2) While the experimental data suggests a positive effect on performance, the underlying processes and reasons for the success of label disambiguation remain unclear. What is the benefit of using moving-average for prototype updating as opposed to a simple average across hidden features from the same class? In my view, they essentially perform the same function. What is the rationale behind reducing \gama and \sigma during the training process and is it necessary to do so? I cannot find any explanation or ablation study on them.
3) The method's effectiveness varies across different datasets. ShieldHead surpasses the baseline on XSTest and S-RLHF, but falls short on OpenAI Mod, ToxicChat, and BeaverTails. This inconsistency diminishes the significance of the method.

### Questions
LN193: the basic idea and intuition of the label disambiguation method is unclear. How and why does it work? What is the difference compared to a simple everage of the hidden features of each class?

LN196: the prototype is mentioned in various context, such as prototype embedding, prototype vector, and prototype label, but what is the connection between the basic idea of prototype and your problem? Why don't use a simple classifier?

LN209: the p^token_(i,j,c) is confusing. Does it refer to the token probability or the token itself?

LN213: do the prototypes P^(t+1)_c refer to the prototype embeddings?

LN215: what kind of normalization is used here?

LN228: the next line says it is a moving-average update, but the equation uses sentence-level label to update token-level labels, which is not a moving average.

LN265: the equation presents the calculation of L_prompt and L_res, but what do they refer to and why do we need them?

Table2: Since the method does not show consistent results accross datasets, models, and settings, the choice of Gemma2-9B looks like a cherry pick. Do we have a general observation about when the method will work?

Table3: "w/o Token Loss (only sentence-level labels)" performs better than "w/o Label Disambi. (both sentence-level and token-level labels but without disambiguation strategy)", does it mean that the token-level labels without disambiguation actually harm the performance?

Table3: ablation on L_prompt and L_res is missing.

### Soundness
2

### Presentation
2

### Contribution
2
