## Human Reviewer 1

### Summary
This paper introduces ``persona vectors'', which are directions in a large language model's (LLM) activation space that correspond to specific, high-level character traits. The authors present a novel, automated pipeline that uses a frontier LLM to generate contrastive data from a simple natural-language description of a trait, which is then used to extract the corresponding vector. The paper demonstrates that persona vectors can be used to monitor persona, control persona, prevent persona shift, and screen data, demonstrating effective usage of the derived features from existing LLMs.

### Strengths
1. Sound Engineering Method: The automated pipeline for vector extraction is a good contribution. By requiring only a natural-language description of a trait, it provides a scalable method for representation engineering, moving beyond bespoke, manually-curated datasets for each concept.

2. Comprehensive Experiments: The authors rigorously validate the utility of the extracted vectors across a wide range of applications (monitoring, inference-time control, training-time control, and data screening). This demonstrates that the persona vectors are not just a correlational artifact on the model's behavior.

### Weaknesses
1. Limited Scientific Insight: The paper is presented more as an engineering achievement than a scientific one. It demonstrates that persona traits can be mapped to vectors but provides little insight into why this is the case and if other naive methods could do the same. The method feels like advanced prompt engineering applied to activations, rather than some general methodological approaches towards general understanding of related problems.

2. Insufficient Comparison to Naive Baselines: The paper fails to adequately compare its complex steering methods against simpler, "naive" baselines in the main text. A full evaluation against standard system prompting or language based methods (instead of using vectors) is critical. Lack of such experiments make it hard to judge if the vectors are truly necessary.

3. Method Clarity: The core methodology is not fully detailed in the main text, making the workflow and its components difficult to understand. Key components, such as the exact prompts used for artifact generation, and workflow are best described in the paper with illustrative display items. This lack of details hinders reproducibility and a clear evaluation of the method's components.

### Questions
Based on the weaknesses:

1. Your paper is presented more as an engineering method than a scientific discovery. Do you have a hypothesis for why complex, high-level persona traits are robustly encoded as linear directions? Is this an emergent property of all LLMs, or specific to their chat-finetuning? How about other behavioral properties not defined as persona?

2. The paper's central claim rests on the utility of these vectors, yet the comparisons to "naive" baselines (like simple system prompting) are missing. Is there a purely prompting pipeline that can achieve similar effects as your vectors, making your vecotors uncessary?

3.  The workflow for vector extraction is hard to understand from the main paper. How sensitive is the final vector's quality to the components of this pipeline?

### Soundness
3

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This work introduces an automated algorithm to extract persona vectors from LLMs, which can be applied to various use cases. Specifically, the authors demonstrate the use of persona vectors to detect and prevent certain personality traits during inference or fine-tuning. The fine-tuning-induced persona shifts can even be predicted before the fine-tuning process begins.

### Strengths
- This work is very comprehensive in the experiments, showcasing diverse use cases for the proposed persona vector. Also, the experiments are delivered very clearly.
- The writing is simple and direct, and it was easy to follow.
- The Appendix is impressive, providing helpful details and further experiments that support the authors' claims.

### Weaknesses
### 1. Method Novelty 
While this work is very comprehensive, my biggest concern is the novelty of the approach. Previously, there have been numerous works that discuss model steering vectors, like RepE [1] or ITI [2]. Also, many works have provided ways to "steer" LLMs for personalized use [3], and even to change LLM personality traits in the latent embedding space [4,5]. Given these works that discuss similar approaches, I believe this deserves an in-depth discussion on what differences the Persona Vector has compared to previous literature.

[1] REPRESENTATION ENGINEERING: A TOP-DOWN APPROACH TO AI TRANSPARENCY

[2] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model

[3] Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization

[4] Exploring the Personality Traits of LLMs through Latent Features Steering

[5] Style Vectors for Steering Generative Large Language Models


### 2. Precision of What the Persona Vector Represents
- I am concerned about the authors' finding that "persona shifts are rather correlated between seemingly different traits. In particular, we notice that negative traits tend to shift together". This finding is concerning because this shows the weakness of the linear interventions in steering the model's persona. While it is understandable that certain persona sets may be correlated to each other to some extent, extremely high correlations (e.g., over 0.8) are not acceptable, because persona vectors should, by definition, be able to pinpoint vector directions that represent a "specific persona", and not be a measure to mitigate "harmfulness" as a whole. If we cannot extract a persona vector that steers the specific persona orthogonal to any other persona, I think the definition of "persona vector" is over-claiming its capabilities.

- The persona vectors are extracted by generating system prompts that would best elicit the target trait, and using the difference in mean activations between responses. This "persona vector" represents the direction that best explains the target persona, which is then applied to many use cases. However, I think this introduces a high risk of confirmation bias; i.e., the persona steering and detection approaches are only confirming the direction that has just been introduced systematically. To refute this point, I suggest you do an experiment that shows that the extracted persona vector is indeed a representation of the target persona, by testing on the inverted direction of the persona vector. For instance, if the "evil" vector _v_ indeed represents the direction of "evil", the negative vector _- v_ should represent "benign". Also, if the "sycophancy" vector is _v_, then _- v_ should represent a "stubborn" or "self-biased" personality trait. Using the persona vectors _v_ extracted for each persona, please provide a systematic evaluation of the effect of _- v_. If _- v_ can elicit the opposite persona, then the experiments provided are not just a confirmation of the direction, and we can say that the persona vector indeed captures the intended personality trait.

### Questions
- Depending on the target persona, I think there might be refusal behaviors of models during the 10 rollouts. How are these handled?

### Soundness
3

### Presentation
4

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper reports on a study of LLM personas. Using mechanistic interpretability methods, the authors extract persona vectors, i.e., linear paths in the activation space, corresponding to multiple personality traits. The authors show how these vectors can be used to monitor, predict, and control personality traits during training, to mitigate and avoid unwanted personality shifts through steering, and even to flag training data that could lead to unwanted personality changes beforehand.

### Strengths
The authors present an automated pipeline for monitoring, predicting, and controlling LLM personalities. However, the paper hides a more salient contribution, the paper includes a case study of preventative steering, i.e., ablating persona vectors at training rather than inference time. The authors demonstrate that fine-tuning on new facts while steering away from the hallucination vector, preserves accuracy on the MMLU with only a slight degradation on new facts. Thus, compared to other SOA methods, such as CAFT, i.e., abblating undesirable vectors, preventative steering seems to mitigate hallucinations in addition to undesirable traits.

### Weaknesses
The presentation is flawed. The paper is very comprehensive and compares the steering approach against psychometric baselines, SAE, fine-tuning vs. few-shot prompting, etc. but this also works to their detriment as it obfuscates the main empirical findings.
According to the authors, the main contribution appears to be an automated pipeline. In terms of empirical findings, the paper would seem to have less to offer. As the authors outline, the methods are otherwise well-established and extensively studied, i.e., linear probing. 
However, the paper includes a case study that shows that preventative steering during fine-tuning can reduce hallucinations without degrading accuracy.
While the comprehensiveness of the report is laudable, it takes away from the overall argument. The paper would benefit from a more concise presentation focused on preventative steering, which is the novel empirical contribution, not the automated pipeline.

### Questions
The process of computing the persona vectors needs further elaboration: How many times were the persona vectors computed? Were the prompts/models varied? Could the persona vectors be strengthened by averaging activation across multiple prompts? How do the persona vectors compare across models?
P26 L1387 The inter-rater agreement setup seems gamed to boost agreement: using high/low split forces a binary choice, it does not validate the texts' trait representations only relative magnitudes.

### Soundness
3

### Presentation
1

### Contribution
3

### Rating
4

### Confidence
4