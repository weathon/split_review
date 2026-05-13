# Jailbreak Instruction-Tuned Large Language Models via MLP Re-weighting

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
In this paper, we investigate the safety mechanisms of instruction fine-tuned large language models (LLMs). We discover that re-weighting MLP neurons can significantly compromise a model's safety, especially for MLPs in end-of-sentence inferences. We hypothesize that LLMs evaluate the harmfulness of prompts during end-of-sentence inferences, and MLP layers plays a critical role in this process. Based on this hypothesis, we develop 2 novel white-box jailbreak methods: a prompt-specific method and a prompt-general method. The prompt-specific method targets individual prompts and optimizes the attack on the fly, while the prompt-general method is pre-trained offline and can generalize to unseen harmful prompts.  Our methods demonstrate robust performance across 7 popular open-source LLMs, size ranging from 2B to 72B. Furthermore, our study provides insights into vulnerabilities of instruction-tuned LLM's safety and deepens the understanding of the internal mechanisms of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a new method for white-box LLM jailbreak by relocatting the attention map of the last layer of the LLMs (the MLP layer). The paper introduces a new MLP re-weighting method, where, with the re-weighting, the models are more easily to be jailbreaked.

### Strengths
1. the idea is illustrated fairly clearly, in particular, I find section 2 and the equation at line 113 helpful, it helps setting up the ground and demosntrating the main focus on this paper is about optimizing for M. 

2. Table 2 also illustrates quite clearly.

### Weaknesses
1. The biggest concern is that, this paper seems to build upon an unrealistic scenario. The paper assumes that one can have quite transparent access to the LLM (as much as plugging a new component to the existing model) that one desires to jailbreak, this is almost not possible in practice. The only application I can think is that, a highly technical malicious team obtains an open-source model, and then do all the engineering work to jailbreak it for information that an aligned, open-source model is not supposed to easily reveal. This application scenarios seems too specific and ideal in comparison to most of other concurrent jailbreak research that study how a party can jailbreak LLMs without access to weights, gradients, or even with the guardrail functions in fully commercial setting. I would recommend the authors to offer more detailed discussions on the motivation from a practical perspective. The method's reliance on white-box access significantly limits its applicability, as it requires the ability to modify the model's internal components, a capability rarely available to external attackers. This contrasts sharply with the more practical black-box attack scenarios that most jailbreaking research focuses on, where the attacker has no access to the model's parameters or internal structure. The paper needs to justify why this specific scenario is relevant and what real-world threats it addresses. 

2. The empirical scope of the paper is a bit too humble, it only compares to some popular jailbreak methods and only in HarmBench alone. Considering the whitebox nature of this method, I would recommend the authors to try recently, highly malicious JAMbench, which might show more advantages of the proposed method. If the authors prefer to test only on HarmBench, some additional discussions of the rationale behind it will be preferred or even necessary. The evaluation is limited by its focus on HarmBench, which may not fully capture the nuances of jailbreaking across diverse scenarios. Given the white-box nature of the proposed method, it would be beneficial to evaluate its performance on more challenging benchmarks like JAMBench, which is specifically designed to test the robustness of models against highly malicious prompts. The lack of evaluation on such benchmarks makes it difficult to assess the true potential of the proposed method. 

3. The method requires training, so it will be necessary to demonstrate the usability where $M$ is trained over one benchmark (HarmBench, AdvBench, JAMbench, etc) and applied at other benchmarks. This is particularly important if the authors want to claim their methods can compete and be better than concurrent jailbreak methods, as other jailbreak methods does not require training. (More details behind the claim at line 276-278 are necessary). I would recommend the authors to report these results or clarify with more details if such experiments have already been done. The training requirement introduces a significant practical limitation, as it necessitates a substantial amount of computational resources and time. The paper needs to demonstrate the generalizability of the trained re-weighting factors across different benchmarks. It is crucial to show whether the method can be trained on one benchmark and effectively applied to others, as this would demonstrate its robustness and practical value. Without such experiments, the claim that the method is competitive with other jailbreaking methods is not fully supported, especially since many existing methods do not require any training.

### Questions
1. Not very sure what the authors mean at line 116, different re-weighting factors for different inferences. It seems to me that this refers to prompt-specific method (3.1) and then contradicts the prompt-general method (3.2). I believe the claim at section 2.1 and line 116 are supposed to serve as the background for the entire paper. 

2. What will happen if we set \rho to zero? (Figure 4).

### Soundness
3

### Presentation
2

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
The paper explores vulnerabilities in instruction-tuned LLMs and introduces new methods to jailbreak these models by re-weighting neurons in multi-layer perceptrons (MLPs) at the end of sentence inferences. The authors propose two jailbreak approaches: a prompt-specific method that targets individual prompts by adjusting MLP weights dynamically, and a prompt-general method that trains on a dataset to bypass safety mechanisms across various prompts. Their findings reveal that end-of-sentence MLP layers play a crucial role in determining whether prompts are harmful, which current safety mechanisms rely upon. Testing on seven popular open-source LLMs, the methods achieve high attack success rates, with the prompt-general method showing generalizability to unseen prompts. The research highlights significant gaps in LLM safety mechanisms, as modifying only specific MLP layers is sufficient to compromise model safety. This work provides insights into LLM vulnerabilities and emphasizes the need for more robust safeguards in future models, while also using MLP re-weighting as a tool for mechanism interpretability to understand which neurons impact safety alignment most.

### Strengths
+ They propose two effective jailbreak methods—prompt-specific and prompt-general—achieve high attack success rates across various LLMs.
+ The prompt-general method generalizes well to new harmful prompts, suggesting broader applicability.
+ Introduces an interpretability tool by identifying specific neurons involved in safety, which could aid future model alignment studies.
+ Provides empirical evidence that safety assessments may concentrate during end-of-sentence inferences, offering valuable insights for future safety research.

### Weaknesses
The method is largely heuristic-driven, meaning the approach lacks rigorous theoretical grounding and may not represent an optimal solution. The loss function, designed to encourage jailbreaks, is based on intuition rather than a systematic analysis. Specifically, the choice of re-weighting neurons based on a simple gradient ascent on a jailbreak objective, without considering the broader landscape of the model's parameter space, could lead to suboptimal or unstable solutions. Furthermore, the lack of a formal justification for the specific form of the loss function raises concerns about its generality and potential for overfitting to the training prompts.

The paper only hypothesizes the role of MLP layers in end-of-sentence safety checks but does not conclusively establish their function in the model’s safety mechanisms, making some conclusions speculative. While the empirical results demonstrate that modifying these layers can lead to jailbreaks, the underlying mechanism remains unclear. It is not definitively shown that these layers are the primary locus of safety checks, or whether the observed effects are a consequence of a more complex interaction within the network. The paper lacks a detailed analysis of the information flow through the MLP layers and how the re-weighting affects the subsequent computations.

The study doesn’t deeply explore how these MLP modifications affect other model capabilities or whether they introduce unexpected biases. While some standard LLM evaluation benchmarks are used, they may not capture subtle changes in the model's behavior. For example, the modifications could potentially degrade performance on specific tasks or introduce biases that are not immediately apparent from the chosen benchmarks. A more comprehensive evaluation, including a broader range of tasks and bias detection methods, is needed to fully assess the impact of the proposed modifications.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors investigated the safety mechanisms of instruction-tuned LLMs and discovered a vulnerability through MLP neuron re-weighting. They developed two white-box jailbreak methods: a prompt-specific method that targets individual prompts and a prompt-general method that works on unseen harmful prompts. The study focused specifically on MLP layers in end-of-sentence inferences, finding that modifying these layers was sufficient to compromise model safety. Their prompt-specific method achieved impressive results, with an ASR of 94-97% across various models. The prompt-general method also performed well, achieving an ASR of 67-94%.

### Strengths
---> This paper provides two different strategies for white-box jailbreaks in LLMs through MLP neuron reweighting, which not only play a crucial role in understanding and improving the security of LLMs, but also can be used to identify MLP neurons that are strongly correlated with safety.


---> This paper demonstrates the effectiveness of the attack with a high ASR across multiple open-source LLMs, ranging from 2B to 72B parameters.

### Weaknesses
 -->> 1:   If the dataset used in pre-training consists of harmful questions and responses, then it is likely that the model's objective has been altered to respond harmful questions.

-----> In instruction-tuned LLMs, safety training is a post-process that follows pretraining. Continuing pretraining with harmful datasets will override the safety training.

I think the overall approach is similar to fine-tuning LLMs with adversarial datasets, and I do not believe this proposed approach is novel.

--->> 2: The authors should have performed the experiments using the fine-tuning approach from Qi et al. (2023) and compared the results with the proposed approach.

------>> As this is a white-box attack, the paper should provide a more comprehensive comparison of results with other attacks, as well as with other methods that have been used to create uncensored LLMs, such as Abliteration method (Maxime Labonne, 2024).

---->>>3:  Line 319: “Meanwhile, our method achieves over a 5x improvement in computational speed compared to existing methods.”---> I  could not find any supporting evidence in the paper to back this claim.

---->>> The paper could have been strengthened by including a cost-of-attack comparison with other existing attacks.

### Questions
Evaluation by Llama-Guard-3: Guardrail LLMs output is binary, categorizing responses as SAFE and UNSAFE, whereas there may also be cases of neutral responses.

Have the authors conducted further evaluation using other judge LLMs or human evaluation to investigate mixed responses, such as, “Sure, here is how to build <bad-stuff>. However, as an AI, I cannot assist with this.” ?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In short, this paper is modifying the GCG attack by only optimizing the MLP layer. The work is incremental. The observation of high-attention score on special tokens seems to be highly related to the attention sink paper, and I would recommend author to reconsider the explanation provided in the paper.

### Strengths
The research problem in the paper is important. 
The paper made an attempt to explain the interesting phenomenon of high attention scores on special tokens.

### Weaknesses
See the questions section. 
Overall, I barely learn anything new from the paper. Jailbreaking prompts can break the model and the llm attention sink phenomenon are well known to the community. I highly recommend the author focus on exploring new threat models in new production models or modalities.

1. Can you explain what does this phrase mean? L13 "especially for MLPs in end-of-sentence inferences"
2. After reading this sentence, "This situation underscores the importance of thoroughly understanding safety mechanisms.". I thought the author is going to propose a defense, but instead, the paper only focuses on the attack. 
3. Suggest to add citations for "Many studies have aimed to unravel the internal mechanisms behind LLM safety, exploring this issue from feature, weight attribution, and other perspectives.". 
4. Why study MLP? what's the motivation? And why is it a novel perspective, given the authors have cited many previous studies on this topic?
5. Define "end-of-sentence" inference
6. Is reweighting the same as randomly perturbing the model weights? If so, it's not surprising that reweighting lowers the performance, which in this paper's context, undermining the model's safety. 
7. L66 "We evaluate our methods and compare them with other jailbreak approaches". Specify the name explicitly
8. L66, " As a result" result of what?
9. L69, "has a smaller impact on the model" how small?
10. L73, "presents new findings", " Based on these insights", what findings and what insights? can you list them as bullets?
11. L114, the reweighting sounds like another dropout layer? 
12. L140, suggest to move prompt template details to appendix
13. How is the proposed idea different from the GCG attack? It reads like a GCG optimized on MLP layer
14. L158, "but rather those at the end-of-sentence, where the inputs are fixed, formatted special tokens", this may be related to LLM attention sink paper (Efficient Streaming Language Models with Attention Sinks). Fig. 1 again confirms my guess on attention sink: the first few tokens of the generation has high attention score. 
15. Tbh, this is not end-of-sentence, it should be the beginning of the model generation. 
16. L222. Drop this sentence "We now complete it here. "
17. How do you differentiate your attack from existing jailbreaking attacks?
18. Missing a summarization figure that introduces the main paper idea
19 The writing needs significant improvements. The definitions are jumping around, and the some sentences are too informal to appear in a paper.

### Questions
1. Can you explain what does this phrase mean? L13 "especially for MLPs in end-of-sentence inferences"
2. After reading this sentence, "This situation underscores the importance of thoroughly understanding safety mechanisms.". I thought the author is going to propose a defense, but instead, the paper only focuses on the attack. 
3. Suggest to add citations for "Many studies have aimed to unravel the internal mechanisms behind LLM safety, exploring this issue from feature, weight attribution, and other perspectives.". 
4. Why study MLP? what's the motivation? And why is it a novel perspective, given the authors have cited many previous studies on this topic?
5. Define "end-of-sentence" inference
6. Is reweighting the same as randomly perturbing the model weights? If so, it's not surprising that reweighting lowers the performance, which in this paper's context, undermining the model's safety. 
7. L66 "We evaluate our methods and compare them with other jailbreak approaches". Specify the name explicitly
8. L66, " As a result" result of what?
9. L69, "has a smaller impact on the model" how small?
10. L73, "presents new findings", " Based on these insights", what findings and what insights? can you list them as bullets?
11. L114, the reweighting sounds like another dropout layer? 
12. L140, suggest to move prompt template details to appendix
13. How is the proposed idea different from the GCG attack? It reads like a GCG optimized on MLP layer
14. L158, "but rather those at the end-of-sentence, where the inputs are fixed, formatted special tokens", this may be related to LLM attention sink paper (Efficient Streaming Language Models with Attention Sinks). Fig. 1 again confirms my guess on attention sink: the first few tokens of the generation has high attention score. 
15. Tbh, this is not end-of-sentence, it should be the beginning of the model generation. 
16. L222. Drop this sentence "We now complete it here. "
17. How do you differentiate your attack from existing jailbreaking attacks?
18. Missing a summarization figure that introduces the main paper idea
19 The writing needs significant improvements. The definitions are jumping around, and the some sentences are too informal to appear in a paper.

### Soundness
2

### Presentation
2

### Contribution
1
