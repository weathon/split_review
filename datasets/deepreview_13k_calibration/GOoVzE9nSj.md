# SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
As advancements in large language models (LLMs) continue and the demand for personalized models increases, parameter-efficient fine-tuning (PEFT) methods (e.g., LoRA) will become essential due to their efficiency in reducing computation costs.
However, recent studies have raised alarming concerns that LoRA fine-tuning could potentially compromise the safety alignment in LLMs, posing significant risks for the model owner.
In this paper, we first investigate the underlying mechanism by analyzing the changes in safety alignment related features before and after fine-tuning.
Then, we propose a fixed safety module calculated by safety data and a task-specific initialization for trainable parameters in low-rank adaptations, termed Safety-alignment preserved Low-Rank Adaptation (SaLoRA). 
Unlike previous LoRA methods and their variants, SaLoRA enables targeted modifications to LLMs without disrupting their original alignments. 
Our experiments show that SaLoRA outperforms various adapters-based approaches across various evaluation metrics in different fine-tuning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a method for preserving safety alignment during low-rank adaptation in LLMs. The method combines a fixed safety module, trained on a small set of harmful prompts, with task-specific initialization of trainable parameters to maintain alignment while fine-tuning.  Empirical results show that SaLoRA retains safety alignment better than existing methods. I will discuss some limitations below.

### Strengths
- Well-motivated approach 
- The use of a fixed safety module, coupled with task-specific initialization, is nice. 
- Empirical results provide a convincing demonstration of SaLoRA’s effectiveness and the theoretical insights are an additional plus.

### Weaknesses
 - There is limited exploration of hyperparameter sensitivity in the safety module, which could provide practical insights for adoption. 
- The task-specific initialization is a notable contribution, but it lacks direct comparison against alternatives.
- The paper could benefit from additional clarity in the theoretical analysis; the derivations and assumptions are sometimes implicit. 
- The experimental setup raises some questions: while AdvBench is a reasonable benchmark, it would be beneficial to demonstrate the model’s performance across a broader set of adversarial and safety benchmarks to substantiate its efficacy.

### Questions
1. How sensitive is SaLoRA is to changes in the size and quality of the harmful prompts dataset? 
2, The task-specific initialization is proposed as critical for SaLoRA’s performance. Can you provide an ablation with other standard initialization strategies?
3. The evaluation largely focuses on AdvBench and jailbreak attacks. Would SaLoRA maintain similar safety alignment if applied other settings like RealToxicityPrompts, factual accuracy, and adversarial q/a?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces SaLoRA (Safety-alignment preserved Low-Rank Adaptation), an innovative fine-tuning technique aimed at preserving the safety alignment of large language models (LLMs). Traditional Low-Rank Adaptation (LoRA) techniques are efficient but tend to degrade the model's safety alignment when adapting LLMs for specific tasks. SaLoRA addresses this by incorporating a safety module and a task-specific initialization that maintains safety features while enabling efficient parameter tuning. The empirical results indicate that SaLoRA outperforms existing methods in both safety alignment preservation and task-specific performance, demonstrating its effectiveness across various alignment evaluations.

### Strengths
1. The proposed SaLoRA method provides a novel solution to a critical issue in parameter-efficient fine-tuning. While LoRA achieves computational efficiency, SaLoRA extends it by addressing the often-overlooked problem of safety alignment degradation in fine-tuning. The approach includes a unique fixed safety module, offering a fresh perspective on preserving safety features during fine-tuning.

2. The paper presents a well-structured empirical analysis of SaLoRA’s efficacy, comparing it across diverse LLMs and safety assessment benchmarks. Experimental rigor is shown by testing SaLoRA on prominent tasks and benchmarking against both baseline methods and state-of-the-art post-hoc alignment solutions. The results consistently show SaLoRA’s ability to maintain or improve safety alignment without sacrificing task performance.

3. The paper is clear in outlining the problem of safety alignment degradation, the structure of SaLoRA, and its implementation. Figures illustrating SaLoRA’s architecture, such as the comparison between LoRA and SaLoRA and the layer-wise safety alignment, help elucidate complex aspects of the approach.

4. This work is significant for the growing need to adapt LLMs safely in specialized applications. By enabling low-rank adaptations that preserve safety, SaLoRA could impact the deployment of LLMs in safety-sensitive fields.

### Weaknesses
1. The method for calculating Linear Probing Accuracy is not clearly explained. Specifically, the paper lacks detail on how the linear probe is trained, what features are used as input, and how the classification is performed. It is unclear if the probe is trained on the same data used for fine-tuning, or on a separate dataset. The description should include details such as the specific layers used for feature extraction, the loss function, and the optimization algorithm used for training the linear probe.
2. Lack of implementation code. Providing open-source code would be very helpful.
3. The paper does not provide a detailed analysis of the types of harmful responses generated by the LoRA fine-tuned models. The "Harmful Case" in Figure 1 is insufficient to understand the nature of the safety failures. A more thorough analysis should categorize the types of harmful responses (e.g., hate speech, misinformation, etc.) and provide examples of each category. This would help in understanding the specific vulnerabilities introduced by LoRA fine-tuning.

### Questions
1. Could you provide more examples of fine-tuned Llama-2-chat-7B’s responses to benign and harmful prompts? The "Harmful Case" in Figure 1 does not clearly illustrate how LoRA fine-tuning influences the generation of harmful responses in response to harmful prompts.

2. The harmful rate is defined as the proportion of responses labeled as unsafe by Llama-Guard-3-8B. Could you include an ablation study comparing harmful rate assessments using different methods rather than relying solely on Llama-Guard-3-8B?

3. Do the authors believe there is a correlation between harmful rate and model parameters or the rank used in PEFT? Why does Llama-3.1-Instruct-8B have a harmful rate of 14% before fine-tuning, which is higher than Llama-2-chat, yet shows a significant decrease in harmful rate after SaLoRA fine-tuning—resulting in a lower rate than Llama-2-chat? Could you discuss potential reasons for this behavior?

I would be happy to engage with the authors to help improve the presentation of the method and evaluation during the discussion phase.

### Soundness
3

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
4

### Summary
This paper addresses the problem of maintaining safety alignment in LLMs during parameter-efficient fine-tuning (PEFT). This paper proposes a novel method, SaLoRA, which introduces a fixed safety module and task-specific initialization for trainable parameters in LoRA. SaLoRA outperforms various adapter-based approaches in preserving the model's safety while achieving comparable or better results on downstream tasks.

### Strengths
1. The paper tackles a relevant issue in the field of AI safety, providing a solution that balances the need for personalized models with the requirement for safety.
2. The authors have clearly articulated the problem and the proposed solution, making the paper accessible to readers who may not be familiar with LLM fine-tuning.
3. The empirical results are comprehensive and demonstrate the effectiveness of SaLoRA in maintaining safety alignment without compromising on task performance.

### Weaknesses
1. Lack of theoretical analysis of why the proposed method works better than existing approaches.
2. The paper could provide more insight into the limitations of SaLoRA and discuss potential scenarios where it may not be as effective.
3. The discussion on the computational overhead of SaLoRA is brief; a more detailed analysis comparing it with other methods could be beneficial.

### Questions
1. Could the authors elaborate on how SaLoRA compares to other state-of-the-art methods in terms of computational efficiency, especially when scaling to larger models or datasets?
2. Are there any specific types of prompts or tasks where SaLoRA is particularly effective or less effective? If so, what are the authors' hypotheses for these observations?
3. How does the performance of SaLoRA degrade as the size of the fine-tuning dataset increases or decreases?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present SaLoRa, a new fine-tuning technique for LLMs that enables safety alignment and downstream task fine-tuning. The experimental evaluation shows that SaLoRa improves model accuracy over other safety alignment techniques.

### Strengths
- The paper clearly motivates the practicality of the problem and provides insights into potential root causes for the increased sensitivity of low-rank adapters towards toxic language.
- The experimental design is carefully chosen and supports the theoretical argumentation well. 
- The paper is well structured and good to follow.

### Weaknesses
 - L.193: How do you measure the feature difference, and what do the empirical results look like? It would be helpful to see what the aligned features look like. On the same note: Why do you observe these significant accuracy changes in Figure 3? Is it due to the base model being aligned already?
- While I understand that SaLoRa is an online approach to alignment, how does SaLoRa's performance compare to existing HAP (hate, abuse, profanity) filters applied to a dataset before fine-tuning or pre-training? An example is the Granite Guardian HAP filter, among others, i.e., what if you only used the non-toxic fine-tuning samples?

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
