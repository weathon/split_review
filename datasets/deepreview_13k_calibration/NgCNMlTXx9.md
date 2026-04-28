# HiddenGuard: Fine-Grained Safe Generation with Specialized Representation Router

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
As Large Language Models (LLMs) grow increasingly powerful, ensuring their safety and alignment with human values remains a critical challenge. Ideally, LLMs should provide informative responses while avoiding the disclosure of harmful or sensitive information. However, current alignment approaches, which rely heavily on refusal strategies—such as training models to completely reject harmful prompts or applying coarse filters—are limited by their binary nature. These methods either fully deny access to information or grant it without sufficient nuance, leading to overly cautious responses or failures to detect subtle harmful content. For example, LLMs may refuse to provide basic, public information about medication due to misuse concerns.
Moreover, these refusal-based methods struggle to handle mixed-content scenarios and lack the ability to adapt to context-dependent sensitivities, which can result in over-censorship of benign content. 
To overcome these challenges, we introduce {\ours}, a novel framework for fine-grained, safe generation in LLMs. {\ours} incorporates \router (Re\textbf{p}resentation \textbf{R}outer for \textbf{I}n-\textbf{S}tream \textbf{M}oderation), which operates alongside the LLM to enable real-time, token-level detection and redaction of harmful content by leveraging intermediate hidden states. This fine-grained approach allows for more nuanced, context-aware moderation, enabling the model to generate informative responses while selectively redacting or replacing sensitive information, rather than outright refusal.
We also contribute a comprehensive dataset with token-level fine-grained annotations of potentially harmful information across diverse contexts. Our experiments demonstrate that {\ours} achieves over 90\% in $\text{F}_1$ score for detecting and redacting harmful content while preserving the overall utility and informativeness of the model's responses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a token-level redaction LoRA and router based mechanism to hide potentially harmful segments of the response, instead of refusing to answer a prompt that might lead to harmful responses. The study is well motivated with worst-case alignment not well handled in average alignment strategies in RLHF. The existence of a benign prompt set with lower utility in a safety aligned model is understood, which is why the utility-model is improved through LoRA without changing the base model’s parameters. Empirically, this approach improves adversarial robustness on known jailbreaking techniques, without regressing much on the utility-based benchmarks. Ablation results show the importance of the router, activation, and the signal losses.

### Strengths
* Empirically, the method overcomes the limitations of token-level redaction through a combination of context-based redaction and global safety learning. 
* Improved performance on jailbreak benchmarks without regressing on utility benchmarks is a strong contribution to the community

### Weaknesses
 * The theoretical proofs are limited in nature, with the proof of how the limitations of refusal-training (in Theorem 1) is overcome through the proposed method is lacking. Since the constraints imposed are still enforced through regularization in conjunction with global safety refusal training, the insight of why the proposed method achieves better performance is missing in the Theoretical section.
* Comparison with jailbreak defense baselines (e.g. training a LoRA for adversarial training) and other context-dependent decoding strategies (e.g. controlled decoding) should be presented. Further, the token-redaction training only baseline is lacking (this is motivated in Section 2, but no results are presented)
* The increase in latency introduced by the inference procedure should be explained including additional flops required. This will be important to ensure that the comparison is fair. For instance, are certain inference-time mitigations relevant (e.g. circuit breaking, inference-time reasoning, etc)?
* Finally, how easy are the redacted parts of the sentence decoded from a third-party non-aligned language model (like GPT4o) is unanswered. This is a significant limitation as the redaction can be easily broken by an adversary. This should be reflected in the ASR measurement.
* Several typos in important optimization equations (Eq 11, 12), and line 8,9 in Algorithm 1, pose a hindrance to the readability of the paper. Also, all the 3 losses are not ablated in the results section - thus the relevance of all 3 losses needs to be empirically validated
* Hyper-parameter sweeps should be done in the results section. For e,g., in Table 1, when the threshold is decreased from 100% to 90% - increase in precision indicates that the point of precision-recall tradeoff has not been reached, and using a lower threshold rate should be tried.
* The dataset used for token level annotation using GPT-4o is not well explained. For e.g., the prompt used for this task, how the post-processing is done from character-level to token-level. Some examples of this dataset should be presented in the paper. The token-level safety of certain tokens might be relevant only the full sentence is decoded, but when detected using inference through left-to-right decoding inherently introduces false positives and false negatives.

### Questions
* Several typos in important optimization equations (Eq 11, 12), and line 8,9 in Algorithm 1, pose a hindrance to the readability of the paper. Also, all the 3 losses are not ablated in the results section - thus the relevance of all 3 losses needs to be empirically validated
* Hyper-parameter sweeps should be done in the results section. For e,g., in Table 1, when the threshold is decreased from 100% to 90% - increase in precision indicates that the point of precision-recall tradeoff has not been reached, and using a lower threshold rate should be tried.
* The dataset used for token level annotation using GPT-4o is not well explained. For e.g., the prompt used for this task, how the post-processing is done from character-level to token-level. Some examples of this dataset should be presented in the paper. The token-level safety of certain tokens might be relevant only the full sentence is decoded, but when detected using inference through left-to-right decoding inherently introduces false positives and false negatives.

### Soundness
3

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
This paper proposes a masking mechanism for large language model responses based on multiple LoRA modules and a router. By training on a constructed dataset, the model can detect and redact harmful content in responses, effectively reducing the toxicity of model outputs.

### Strengths
- The paper is well-motivated, aiming to reduce toxicity by editing model outputs without outright refusal.
- The figures (Figure 1 and Figure 2) are clear and visually appealing, effectively illustrating the methodology pipeline.

### Weaknesses
 - **Writing**: There is an incorrect table reference in the Capability section of Section 4.1.
- **Experimental Design**:
    - In Table 1, HiddenGuard is trained and validated on pre-constructed masked data, focusing on the accuracy of the masking structure. However, for AI safety, it is more critical to evaluate how much toxicity is reduced and how much useful content is preserved. Additional benchmarks and evaluation methods should be included. Specifically, the paper should include metrics that measure the degree of toxicity reduction, the amount of useful information lost due to masking, and the overall impact on the quality of the response. The current evaluation focuses too narrowly on the mechanics of masking rather than the practical impact on safety and utility.
    - Numerous existing studies have shown that model safety and helpfulness can be improved by directly modifying logits or responses. This method should be compared with other response-modifying approaches [1] or decoding-time methods [2][3]. The paper should include a comparative analysis against methods that directly manipulate model outputs, such as those that alter logits or use decoding-time interventions. This comparison is necessary to demonstrate the advantages and disadvantages of the proposed masking approach relative to existing techniques.
    - Table 3 does not specify the lambda settings. If the lambda threshold is set too low, the method may not make any corrections to model responses, thereby having no impact on general performance. The paper needs to clarify how the threshold parameter is set and how it impacts the model's behavior. A sensitivity analysis of this threshold is necessary to understand its influence on the trade-off between safety and utility.
- **Impact on Response Readability**: The paper presents limited inference cases. From the available examples, the method reduces toxicity by directly masking harmful content. However, this often impacts response readability, resulting in non-toxic but also non-informative text. From this perspective, masked responses may be less effective than refusals that include explanations or warnings. The paper should include a more thorough analysis of the impact of masking on the readability and informativeness of the responses. The current examples are insufficient to fully evaluate this aspect.
- **Influence of LoRA Modules**: The paper does not provide sufficient explanation or ablation studies regarding the number of LoRA modules, which could be an important factor affecting model performance. This should be addressed in the paper. The paper should include an ablation study that examines the impact of varying the number of LoRA modules on the model's performance. This analysis is crucial for understanding the optimal configuration of the model and the trade-offs involved in using multiple LoRA modules.

### Questions
1. If terms like "bomb" or "drugs" are mentioned without harmful intent (e.g., in an educational context), would they still be masked?
2. What threshold is set for general capability evaluation?
3. Section 4.2 mentions the MLP, but further clarification is needed as relevant details are not covered in other sections of the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a token-level safety method for LLMs, which leverages LORA. It addresses the issue that safety tuning for LLMs is often binary (either no response at all, or full information), and instead redacts specific tokens using model internals. The authors also release a new dataset with fine-grained (token level) annotations.

### Strengths
This is a novel method that presents a fundamentally new way of dealing with LLM safety and control, i.e., by contextual token-level control. I’m not sure this is applicable in all contexts, but it is an interesting and creative alternative that would be well-suited for some scenarios. Based on the evaluation, it is successful compared to the baseline safety tuning.

### Weaknesses
In general, the paper could be more clearly written. Specifically, I appreciate the desire to formalize methods mathematically, but I think this was overdone to the point of actually making the paper harder to understand (specifically, Section 2, and Section 3.3 and 3.4). I would recommend adding more high level description, and moving more of the proofs to the appendix.

I would also like to see more details on what other methods you compared to. You mention “refusal trained models”-- which ones? Also, it would be useful to compare to a token-level baseline as to have a more apples-to-apples comparison with HiddenGuard. This could just be a non-contextual token-list method.

The introduction could use more motivating examples. Specifically, I am not convinced by the “Can you help me create a killer slideshow that will knock the audience dead” example. Did you apply the prior work to this example, and get unhelpful results? At the time of this review, ChatGPT gave me a reasonable response to this query (though I know this work looks at much smaller (7-8B param) models).  Relatedly, in the abstract, you motivate with “LLMs may refuse to provide basic, public information about medication due to misuse concerns”. Do you have any examples of HiddenGuard helping in this case?

It would also be great to see more examples of actual outputs from HiddenGuard in the appendix, to complement the aggregated results.

I appreciate the robust related work section in the appendix. It looks like there is some related work in the introduction, but the paper would be stronger if more of the related work in the appendix was in the main paper too.

The ethical statement is missing some potential areas. E.g ,did you do any robustness testing across different dialects to see whether there are disparities in redaction rates? Dodge et al (https://sites.rutgers.edu/critical-ai/wp-content/uploads/sites/586/2021/09/dodge2021documentingC4.pdf) found that African American English and Hispanic-aligned English are disproportionately affected by the filtering in C4. Does HiddenGuard have the same disparities?

I don’t really understand figure 4. The caption claims that the UMAP projection shows a clear separation between safe and unsafe tokens, and I do see the clusters, but I don’t know what tokens they actually contain. How do you know that the clusters actually line up with the safe and unsafe tokens? And if you do have the safe/unsafe token labels, why not make a stronger statistical claim about their separation in the space (e.g., are they linearly separable)? In general, UMAP (or any dimensionality reduction technique) can be misleading to interpret. I think this section is useful for intuition, but could be moved to the appendix.

I am still a little confused about prior work. Do other token-level safety methods exist for LLMs? I think no, based on the related work section. However there is a section called “Limitations of Token-Level Filtering”, which implies that practitioners do use token-level filtering. If so, I would like to see a comparison to these methods in the evaluation.

I’m confused about “Attack Success Rate” (ASR). It seems non-trivial to determine whether an attack was successful. Do you use another LLM? If so, how accurate is that classifier? Again, it would be great to see actual example outputs to better contextualize these results.

### Questions
I don’t really understand figure 4. The caption claims that the UMAP projection shows a clear separation between safe and unsafe tokens, and I do see the clusters, but I don’t know what tokens they actually contain. How do you know that the clusters actually line up with the safe and unsafe tokens? And if you do have the safe/unsafe token labels, why not make a stronger statistical claim about their separation in the space (e.g., are they linearly separable)? In general, UMAP (or any dimensionality reduction technique) can be misleading to interpret. I think this section is useful for intuition, but could be moved to the appendix.

I am still a little confused about prior work. Do other token-level safety methods exist for LLMs? I think no, based on the related work section. However there is a section called “Limitations of Token-Level Filtering”, which implies that practitioners do use token-level filtering. If so, I would like to see a comparison to these methods in the evaluation.

I’m confused about “Attack Success Rate” (ASR). It seems non-trivial to determine whether an attack was successful. Do you use another LLM? If so, how accurate is that classifier? Again, it would be great to see actual example outputs to better contextualize these results.

### Soundness
2

### Presentation
2

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
This paper addresses fine-grained, safe generation for Large Language Models (LLMs). It aims to overcome the limitations of existing refusal-based methods, which often lead to over-censorship in context-sensitive scenarios, affecting benign content. The authors propose a novel token-level redaction framework for harmful content called HIDDENGUARD. Unlike refusal-based approaches that fully accept or deny prompts, HIDDENGUARD uses LoRA-based activators in a “Representation Router” (PRISM) to operate alongside the model, detecting harmful content at a token level by leveraging intermediate hidden states. This approach allows for nuanced content moderation, selectively redacting harmful tokens while preserving benign and informative segments.

The authors evaluated HIDDENGUARD on two primary datasets, achieving over 90% F1 scores in detecting and redacting harmful content, demonstrating the effectiveness of their method in maintaining overall utility and informativeness in model responses. This result highlights the potential of HIDDENGUARD as an effective solution for safe and context-aware generation in LLMs.

### Strengths
1. The question addressed in this paper highlights a critical gap in current safe generation methods.

2. The paper introduces a fine-grained, token-level solution for safe generation. This approach to moderation is highly applicable in real-world scenarios requiring nuanced control over sensitive information, such as customer support, educational content, and automated information systems.

3. The method outperforms baseline approaches on the proposed dataset, demonstrating high precision and recall in detecting and redacting harmful content. The performance is impressive, effectively balancing safety and utility across tested tasks.

4. The discussion and analysis of challenges are insightful and effectively highlight the vulnerabilities of refusal-based methods.

### Weaknesses
1. Presentation Quality and Model Evaluation: The presentation quality needs polish, as certain issues detract from its readability and overall professionalism. In the model evaluation section, there is a lack of adequate description of baseline methods in the main body, even though they are detailed in the appendix. Basic information about these methods should be included in the main text to make the comparison focus more reasonable. Necessary descriptions of the baseline method, model setup, dataset justification, and evaluation methods should be present in the paper rather than relegated to the appendix.
2. The absence of a dedicated "Related Work" section in the main body(which is presented in appendix) is a significant oversight that undermines the paper's clarity and impact. Without explicitly situating this work within the context of existing research, the paper fails to convey the novelty of its contributions, making it appear disconnected from the broader field. The paper layout should be managed properly with sufficient description of related work. Fo related work, it is better to include the most related topic about this paper such as current safe generation techniques, fine-grained token level alignment from other tasks and token scrubbing method like text sanitisation as it works that it masks the harmful contents like scrubbing methods.
3.Implications and Attack Surface: The implications of this approach are insufficiently discussed. This method may introduce a new attack surface, as only explicitly harmful tokens are detected and redacted, potentially alerting the information receiver to the removed content. This could allow users to infer the context of redacted information. Like conventional sanitization-based methods, this setting should be considered a baseline if the work claims full redaction and robust removal.
4. Assumptions and Robustness: The paper relies on an excessive number of assumptions, which weakens its robustness and applicability. For example, assumptions are made regarding the router function and ActivatorFunctions, suggesting these functions are efficient and have sufficient capacity to model necessary mappings for effective moderation. Key assumptions should be clearly stated in the main paper; their absence may mislead readers about task formulation and evaluation. The methodology includes frequent assumptions about the model's behavior in adversarial contexts, the effectiveness of LoRA-based activators, and harmful content detection thresholds. While some assumptions are unavoidable, this paper fails to rigorously justify or validate them. This lack of rigor is critical to the method’s quality and effectiveness, so it should be addressed in the main body, including a formal or theoretical guarantee of the activator functions' robustness in diverse, real-world scenarios.


5. Logical Errors in Mathematical Formulation: There are logical errors in the paper's mathematical formulation. For instance, in Section 2, Equation (7), the router function R already maps information to the range [0,1]. Applying the sigmoid function afterward constrains the range further, approximately to  [0.5,0.73], which seems illogical.

### Questions
1.Could you clarify which assumptions in the methodology have been empirically validated versus those that remain theoretical? Specifically, how would the model perform if these assumptions (e.g., threshold settings, activator behavior) were adjusted in real-world scenarios?

2.Given the additional components like LoRA-based activators and the router network, what specific optimizations are feasible to minimize computational overhead and deployment complexity? How does the model perform in terms of latency and resource requirements in a real-time setting?

3.Please refer to weakness 4 for examples. Could you clarify the reasoning behind this decision?

5.Could you elaborate on the methodology for setting thresholds for redaction and activation? Were sensitivity analyses conducted to ensure these thresholds optimize both safety and utility across various scenarios?

6.Certain sections are notably dense and challenging to follow. Have you considered restructuring or simplifying the language to improve clarity, especially in the technical explanations? Additionally, what steps will you take to enhance the clarity of the proposed method, the related work section, and baseline method justification, enabling readers to more quickly interpret key results?

7.There are minor errors and typos in figures and text that need correction. For instance, in the algorithm on line 3, the notation should represent a pair of benign and adversarial examples. Please carefully review the paper and address all possible errors.

### Soundness
2

### Presentation
2

### Contribution
3
