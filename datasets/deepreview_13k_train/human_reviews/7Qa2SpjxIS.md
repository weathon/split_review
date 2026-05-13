# AI Sandbagging: Language Models can Strategically Underperform on Evaluations

- Decision: Accept
- Scores: 6, 6, 3

## Abstract
Trustworthy capability evaluations are crucial for ensuring the safety of AI systems, and are becoming a key component of AI regulation. However, the developers of an AI system, or the AI system itself, may have incentives for evaluations to understate the AI's actual capability. These conflicting interests lead to the problem of \textit{sandbagging} – which we define as \textit{strategic underperformance on an evaluation}. In this paper we assess sandbagging capabilities in contemporary language models (LMs). We prompt frontier LMs, like GPT-4 and Claude 3 Opus, to selectively underperform on dangerous capability evaluations, while maintaining performance on general (harmless) capability evaluations. Moreover, we find that models can be fine-tuned, on a synthetic dataset, to hide specific capabilities unless given a password. This behaviour generalizes to high-quality, held-out benchmarks such as WMDP. In addition, we show that both frontier and smaller models can be prompted, or password-locked, to target specific scores on a capability evaluation. Even more, we found that a capable password-locked model (Llama 3 70b) is reasonably able to emulate a less capable model (Llama 2 7b). Overall, our results suggest that capability evaluations are vulnerable to sandbagging. This vulnerability decreases the trustworthiness of evaluations, and thereby undermines important safety decisions regarding the development and deployment of advanced AI systems

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes the concept of sandbagging—a phenomenon where AI models are intentionally fine-tuned or prompted to underperform in certain evaluations. The paper demonstrates that large language models, like GPT-4 and Claude 3, can be conditioned to underperform on dangerous capability evaluations while maintaining strong performance on general, less critical benchmarks, suggesting that the capability evaluations are vulnerable to sandbagging.

Key contributions of this paper include:

- The authors insightfully define sandbagging as strategic underperformance during evaluations, emphasizing its potential for both developer-induced and AI system-induced underperformance.

- The study shows that LLMs can be fine-tuned or prompted to selectively fail on dangerous capability tests, masking harmful knowledge without affecting other areas.

- Experiments show that models are able to target a specific capability score, and can
approximately emulate a consistent capability profile of a weaker model, highlighting the challenge of sandbagging detection.

### Strengths
- Originality

The concept of sandbagging is novel within AI safety, particularly regarding regulatory concerns. The paper innovatively proposes a mechanism by which AI systems or developers might deceive evaluators by masking dangerous capabilities selectively while maintaining its general performance.

- Clarity

The writing is clear and accessible, providing both conceptual definitions and practical illustrations of sandbagging. The examples are well-structured.

- Significance

The research is highly relevant to AI safety and policy, given the regulatory implications. Sandbagging could compromise AI risk assessments, underscoring the need for more robust and trustworthy evaluation frameworks for advanced AI systems.

### Weaknesses
 - Title of Section 4.2 and 5.2 are partially covered by figures.

- Results in Section 5.1 are somehow counterintuitive and lack further explanation. It seems to me that if a model is able to control its own accuracy on a specific task then it should reach 100% accuracy on the whole test set. Otherwise, it should be hard for the model to monitor its accuracy.

### Questions
- Why does the prompting method (Section 5.1) succeed in calibrating the model's accuracy to specific target levels on a task, even though the base model does not achieve 100% accuracy on this task (as shown in Figure 5)?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies sandbagging, a scenario where language models strategically underperform on an evaluation benchmark. The authors provide a formal definition for “sandbagging” and illustrate what it means with several examples. They evaluate GPT-4-Turbo, Claude 3 Opus, Mistral-7B-v0.1, and Llama models, and examine whether they can be prompted or finetuned to selective underperform on dangerous capability evaluations. They further show that strong models can be prompted or password-locked to imitate the capability levels of weaker models, thereby making sandbagging harder to detect. The study highlights the importance of crafting trustworthy capability evaluations, and shows that such evaluation may require more than black-box model access.

### Strengths
- The authors provide a formal definition for AI sandbagging and illustrate what it means with multiple example scenarios.
- Experiments cover a variety of closed-source and open-source models.
- Extensive experiments show that models can be prompted or fine-tuned to underperform on certain dangerous capability benchmarks, or to mimic a certain capability profile of a weaker model.
- The appendix clearly details all prompts, data collection procedures, and finetuning configurations.

### Weaknesses
 - There was no quality check for the generated synthetic dataset in Section 4.2.
- The distinction between “real” and “synthetic” data in 4.2 feels a little bit ill-defined, as the synthetic data is created to closely mimic the real benchmark. There is no quantified discussion about how close the password-locking finetuning data needs to be to the evaluation data distribution in order for sandbagging to be effective. It seems like full knowledge of the evaluation benchmark is required to make models selectively underperform on that benchmark, but this knowledge may not be available in real-world scenarios.
- Password-locking seems to be a lot more effective on Mistral than on Llama-3-8B, and effectiveness also varies a lot across domains (biology, chemistry, cybersecurity). There is limited discussion on why this may be happening.
- The study exclusively focuses on multiple-choice questions and does not consider free-form generations tasks. However, the authors acknowledge this limitation.


### Questions
- For the open-weight models, are you using the base model versions without any instruction tuning or alignment? What’s the rationale behind this choice?
- Based on Figures 9 and 10, it seems like prompting for sandbagging on biology, chemistry, and computer science for WMDP does also significantly hurt performance on similar MMLU subjects. Doesn’t this show that the models are underperforming on all questions related to a subject?
- You say that “refusals typically indicate a harmful question,” did you run any qualitative analysis to verify that?
- In Figure 5, the “locked with password” model often outperforms the base model. Why may this be the case?
- For Section 4, did you perform any direct comparison between prompting and finetuning on the open-weight models?
- It’s quite fascinating that models can maintain a targeted accuracy even when the questions are asked one by one during prompting. Do you have any theory as to how the models are able to achieve this?
- For Figure 8, it seems expected that the Emulator is closer to Llama-2-7b than the Targeter, since you randomly showed correct answers during training based on an accuracy rate without accounting for question difficulty. Did you experiment with a training approach that considers question difficulty when handling questions without a password?
- The headers for sections 4.2 and 5.2 seem incomplete.

### Soundness
2

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
This paper evaluates AI capabilities in sandbagging: strategically underperform on certain evaluations. For example, the model developer may hide their models' dangerous capabilities on certain evaluation benchmarks (e.g., CBRN, persuasion) to evade safety checks. To evaluate current model performance, this paper adopts prompting and backdoor fine-tuning. Experiment results show that LMs can significantly reduce their performance on WMDP (Weapons of Mass Destruction Proxy), while keeping their performance on MMLU unchanged or moderately decreased. This raises challenges about trustworthy capability evaluation.

### Strengths
1. Instead of merely operationalizing this threat model via backdoor fine-tuning, it also studies prompting, which is a more natural setup.
2. The experiments of using prompting to calibrate LLMs are pretty interesting (Figure 7 left). While strong LMs still struggle to simulate weak LM outputs (which aligns with my personal experience), calibrating themselves are also impressive, which have not been studied before as far as I know.

### Weaknesses
1. The motivation needs to be further justified. 
- First, it is totally fine to just motivate with malicious developers. Otherwise, please discuss more about why such goals can naturally emerge in LMs, instead of hiding them in references.
- Second, why malicious developers can access the distribution of third-party hidden evaluation datasets?
2. The experiment setup cannot well support the threat model. More specifically, while LMs are shown to underperform on WMDP, they have not been shown to maintain dangerous capabilities on other similar benchmarks. If LMs generally underperform in weapon-related domains, it would not cause harm.
3. Please correct me if I misunderstand: most experiment results are not surprising, e.g. LMs can underperform in certain domains when told or fine-tuned to do so, or LMs can simulate other LMs by fine-tuning on their predictions. 
4. The writing is misleading or unclear (e.g., when claiming models can emulate a consistent capability profile of a weaker model, clarify that they are fine-tuned).

### Questions
1. Besides QA, there are a lot of other forms for capability evaluation, e.g., classification. How well does the current sandbagging operationalization generalize to these forms? For example, how well does the sandbagging LM perform in determining the binary correctness of answers on WMDP?
2. "We propose a new definition for AI sandbagging", how is the definition different from prior work (e.g., Greenblatt et al, 2024)?

### Soundness
2

### Presentation
1

### Contribution
2
