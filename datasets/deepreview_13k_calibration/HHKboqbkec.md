# Scaling Multimodal Theory-of-Mind with Weak-to-Strong Bayesian Reasoning

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Theory of Mind (ToM) enables individuals to understand and predict thoughts, emotions, and intentions of the others. To replicate this cognitive ability in machines, especially under complex multimodal environments, recent advances combine Bayesian-based state inference with deep learning models to estimate mental states, where the Bayesian model handles state transitions and a language model (LM) estimates the likelihood of intermediate states. However, while post-training an LM to specialise in ToM tasks improves performance, the computational cost increases as the LM scales, limiting the model size to 7 billion parameters. Despite this post-training process, smaller LMs still struggle with the physical and mental modelling demands of ToM due to their limited world knowledge and reasoning capacity. To address this, we propose a scalable solution that leverages the strengths of larger LMs (up to 70 and 405 billion parameters, respectively), including their vast world knowledge and atomic-level reasoning capabilities, without increasing post-training resource requirements. Our method transfers ToM-specific behaviours from a post-trained small LM to guide the latent reasoning of a larger LM during test time. This weak-to-strong control mechanism enables the larger LM to improve Bayesian likelihood estimation at each inference step, harnessing its reasoning power in ToM scenarios while reducing the need for additional training resources. Extensive experiments demonstrate the significant effectiveness of our scaled approach. It is better at inferring human mental states in complex and interactive environments, outperforming the state-of-the-art solution by $\sim4.6$% across multiple tasks on the multimodal ToM benchmark and unseen scenarios. Our code and datasets are available: https://anonymous.4open.science/r/scale-bayesian-tom-248B

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a scalable approach to enhance machine-based ToM, which is crucial for understanding and predicting human-like mental states in multimodal environments. The authors propose a weak-to-strong Bayesian reasoning framework that leverages the strengths of large language models to improve ToM inference without the computational costs associated with extensive post-training.

### Strengths
1. The author's approach seems to be novel
2. I like the experimentation, did show the scaling trend.

### Weaknesses
1. Presentation could be better. For instance, Fig 1, it contains too much information.
2. The major concern here is that everything is done on Lora. What happen if you do full-scale training? How much performance improvement do you expect to gain?
3. Didn't test smaller model such as phi-3b, gemma-2b etc. Maybe you can run full fine-tuning on smaller model.

### Questions
1. My major question is, how much improvement do you expect to gain if you run full-scale training?
2. Would be nice to see if you can test this on a smaller model, GPT2, or gemma-2b and see if there is larger performance gain. 
3. The performance difference between llama2 vs llama3 vs llama3.1 isn't that much, is it because pre-training (or the quality of the pre-trained model) matter less in this context? Do you have theory/explaination why this happens?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a method for scaling Theory of Mind (ToM) capabilities in AI systems using a weak-to-strong Bayesian reasoning framework. The core approach combines Bayesian state inference with language models, where a smaller post-trained language model (4-8B parameters) guides the reasoning process of a larger model (up to 405B parameters) during test time1. The method works by transferring ToM-specific behaviors from the post-trained small language model to influence the latent reasoning of the larger language model. This approach enables the system to leverage both the extensive world knowledge of large language models and the ToM-specific behaviors learned through post-training, while avoiding the computational costs typically associated with post-training large models

### Strengths
- The weak-to-strong Bayesian framework provides a practical solution to scale Theory of Mind capabilities without post-training large models, addressing a key efficiency challenge in the field.
- The technical approach cleanly integrates Bayesian state inference with language models, providing a principled and effective foundation for ToM reasoning.
- The evaluation framework systematically tests both scalability and generalization, with clear ablations demonstrating the contribution of each component.
- The paper is well written, with a clear motivation, methodology, experimental section, and supporting figures.

### Weaknesses
 - The paper doesn't adequately address the apparent contradiction: recent research shows smaller models have fundamental reasoning gaps, yet the method relies on a small model to guide larger model reasoning. This raises questions about whether the smaller model can effectively decompose problems it may struggle to reason about itself. Specifically, the paper does not clarify how a smaller model, which may lack the capacity to perform complex multi-step reasoning, can provide effective guidance for the larger model's reasoning process. It is unclear if the smaller model is merely providing a prior over possible solutions, or if it is actually guiding the larger model's reasoning steps. This distinction is crucial for understanding the limitations of the approach.

- The evaluation methodology could be strengthened by adopting a variance analysis framework similar to GSM-Symbolic (Mirzadeh et al., 2024, https://arxiv.org/pdf/2410.05229), which would help quantify how the model's Theory of Mind capabilities vary across different phrasings of the same underlying task. The current evaluation does not explore the sensitivity of the model to variations in task phrasing, which is a critical aspect of assessing the robustness of ToM capabilities. For example, changing the descriptions of objects or the context of the scenario could reveal whether the model is truly reasoning about mental states or simply relying on surface-level cues.

### Questions
- Would you classify tom beliefs as a form of reasoning? If so, what makes a smaller model capable of classifying tom beliefs?
- Could the authors clarify if the primary mechanism of the weak-to-strong framework is to align the larger model's distribution with ToM-specific beliefs and task structure, while preserving its general reasoning capabilities, rather than directly transferring reasoning abilities from the smaller model? If so, this would suggest the smaller model acts more as a task-specific prior that guides the larger model's attention and beliefs, rather than as a direct source of reasoning. This interpretation could help explain the framework's effectiveness despite the typically limited reasoning capabilities of smaller models.
- Figure 1 is confusing, its not clear from the figure exactly how the smaller post trained lm conrols the larger lm. Why is this model denoted  'extreme'?
- How how is model performance impacted when the post trained lm is itself large (e.g. 70B class)?
- As stated in weakness 2, how does performance degrade when the task phrasing is edited?


Notes
- there are no line numbers

### Soundness
3

### Presentation
4

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
The paper builds upon the MMToM-QA benchmark by introducing a method to align the general, amortized policy of a large LM (as originally used in MMToM-QA work) to the ToM tasks at hand using a post-trained expert small LM. The main contribution is a reweighting mechanism that integrates the extensive world knowledge from the large LLM with the ToM-specific policy from the small model. An extensive analysis on the improvement in performance as a result of this on the MMToM-QA benchmark. The paper thus effectively propose a way to improve upon the MMToM-QA method for better/more accurate Bayesian likelihood estimation of the goals and beliefs, that also now leverage the specialized knowledge corresponding to a particular ToM tasks in a scalable manner.

### Strengths
These are the strengths of the paper in my opinion:

1. Improves upon the Bayesian Inverse Planning Accelerated by Language Models, by making them more adaptive to ToM tasks at hand using a post-training process.

2. The proposed post-training method is more scalable and the integration of this expert post-trained knowledge to guide the large LM seems principled.

3. Extensive analysis and ablation studied on the MMToM-QA benchmark, effectively illustrating the methods adaptability and efficiency.

### Weaknesses
These are the weakness of the paper in my opinion:

1. The paper is very poorly written. Unless and until you go back and read the details from the appendix of MMToM-QA [1] method, the explanations are incomplete and hard to read. The paper would benefit from an appendix section and can be more upfront about the fact that this is a direct extension to the the MMToM-QA paper. For example, see the question 2, such implementation details are not discussed anywhere.

2. The paper is fairly incrimental as far as the methods used are concerned. The ToM inference is directly an extension of previous work, and so is the post-training method (eg: takes inspiration from the post-training literature, that uses a reweighting ratio between an expert and non-expert and subsequent normalizations [2][3]).

### Questions
1. Could you please explain why such a reweighting scheme between an expert and non-expert is a principled mechanism for policy adjustments/redirection in Equation 6 ? Is it related to some well-established theories in Bayesian / Probabilistic modelling literature (for example say Importance Sampling, or minimizing KL divergence between policies etc) ?? Expanding on this theoretical foundation would enhance the paper’s contribution and clarify the underlying principles.

2. How is the agent's belief distribution b(s) modelled? How is the belief evolution modelled $P\left(b_1^t \mid \hat{b}^{t-1}, s^t\right)$ ?? These details are missing. The paper would benefit from a thorough rewriting to make it more accessible to the reader.

3. How much time does this fine-tuning process take (specify the compute resources used etc) and what is the size of the pool $
\mathcal{D} = \left(s_i, b_i, g_i, a_i\right) _{i=1}^N$ in terms of N, used for optimizing eq 5? 


References

1. MMToM-QA: Multimodal theory of mind question answering https://arxiv.org/pdf/2401.08743
2. DExperts: Decoding-time controlled text generation with experts and anti-experts. https://arxiv.org/abs/2105.03023
3. An Emulator for Fine-Tuning Large Language Models using Small Language Models. https://arxiv.org/pdf/2310.12962



--------
### **Post Discussion Update**

**I increase the score to a 5 for incorporating several suggestions, especially for a more accessible writing style post rebuttal. The effort of introducing the new theorem to justify the reweighting mechanism (under some strong initial assumptions) is also appreciated. Methodologically it's an incremental work extensively based on a recent paper MMToM-QA, but now without the need to explicitly post train the large model. Because of the limited novelty, I unfortunately cannot recommend a strong accept. However, I won't oppose if the other reviewers argue for an accept.**

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The paper introduces a novel approach to utilizing large-scale models for Bayesian Theory of Mind (ToM) reasoning. Rather than fine-tuning large models directly, the authors propose fine-tuning smaller models and leveraging the difference between the fine-tuned and naive versions of these small models to approximate the impact of fine-tuning on the larger model. This method is rigorously evaluated on the MMToM-QA dataset, demonstrating its effectiveness in handling complex ToM tasks.

In the interest of transparency, I would like to note that this paper is somewhat outside my area of expertise, and as such, my confidence in assessing it is limited. However, after discussing this with the Area Chair, we agreed that I would proceed with the review and focus on evaluating aspects I can assess.

### Strengths
The proposed method is both simple and robust, demonstrating a well-grounded approach. The experiments are rigorously conducted, and the results reflect strong performance, effectively supporting the validity of the approach.

### Weaknesses
A weakness I noted is that I found the paper challenging to understand. While this is possibly due to my limited expertise in this specific area, I looked at recent related works (BIP-ALM and SimToM) and found them notably more accessible. This suggests that, although my background may play a role, the paper could benefit from clearer explanations or added context to help readers better grasp its motivation and contribution - especially those outside the immediate field.

### Questions
- The general idea of approximating the changes that fine-tuning a large model would have by fine-tuning a smaller one and approximating the changes by reweighing using a ratio seems very general. Could this exact methodology be applied to other types of problems? (Or was it already used? - the relation to the works using reweighing, mentioned in the related work, is unclear to me. )

- Is there a fundamental reason why fine-tuning models for the kind of ToM tasks considered is harder / more computationally expensive than fine-tuning for other tasks?

### Soundness
3

### Presentation
2

### Contribution
3
