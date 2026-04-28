# Inference time LLM alignment in single and multidomain preference spectrum

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Aligning Large Language Models (LLM) to address subjectivity and nuanced preference levels requires adequate flexibility and control, which can be a resource-intensive and time-consuming procedure. Existing
training-time alignment methods require full re-training when a change is needed
and inference-time ones typically require access to the reward model at each inference step. To address these limitations, we introduce inference-time model alignment method that learns encoded representations of preference dimensions, called \textit{Alignment Vectors} (AV). These representations are computed by subtraction of the base model from the aligned model as in model editing enabling dynamically adjusting the model behavior during inference through simple linear
operations. Even though the preference dimensions can span various granularity
levels, here we focus on three gradual
response levels across three specialized domains: medical, legal, and financial, exemplifying its practical potential. This new alignment paradigm introduces adjustable preference knobs during inference, allowing users to tailor their LLM outputs while reducing the inference cost by half compared to the prompt engineering approach. Additionally, we find that AVs are transferable across different fine-tuning stages of the
same model, demonstrating their flexibility. AVs also facilitate multidomain, diverse preference alignment, making the process 12x faster than the retraining approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel approach for adjusting Large Language Model (LLM) behaviors during inference time using Alignment Vectors (AV). The key innovation is treating alignment as a model editing problem where preference dimensions are encoded as vectors that can be dynamically combined with the base model through simple linear operations. The authors focus on three proficiency levels (expert, generic, and avoidance) across three specialized domains (medical, legal, and financial), demonstrating how their method enables flexible control over model outputs without requiring retraining. The work includes creation of a synthetic dataset with 38k query-response pairs and shows that their approach reduces resource usage by 12x compared to traditional retraining methods.

### Strengths
1. A novel inference-time model editing technique using Alignment Vectors that allows dynamic adjustment of LLM outputs along preference dimensions without retraining or complex prompt engineering
2. A substantial synthetic dataset (38k examples) spanning three domains and three proficiency levels, with human-evaluated quality checks showing strong inter-annotator agreement
3. Demonstration that AVs can be effectively transferred across different fine-tuning stages of the same model while maintaining performance
4. A resource-efficient approach to achieving multidomain diverse behaviors that is 12x faster than traditional retraining methods

### Weaknesses
1. The evaluation based on GPT-4 judged metrics might need further validation with human study.
2. Validation is limited to only one model (Mistral-7b) - broader testing across different open-source LLMs would strengthen the findings.
3. Besides prompting, any test-time adaptation methods should be compare in the main experiments?
4. Any further illustrations on "over-generalization effect"?

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a preference alignment approach that only aligns during inference, using encoded representations called Alignment Vectors (AVs). The AVs are learned and tuned for the same model in different tuning stages, which shows good transferability across different domains. The authors also build a diverse domain-specific dataset with responses categorized into three levels. Extensive experiments demonstrate that AVs can help LLMs align to different domains and show promising performance.

### Strengths
1. This paper presents a simple and effective idea to align the preferences of LLMs in inference time. The transferability of this approach across different domains is good.

2. The authors have also built a large dataset that contains responses in avoidance, generic responses, and expert opinions.

3. The AVs offer flexibility to adjust the level of LLMs in generation by adjusting their weights.

### Weaknesses
1. The work aims to align LLMs during inference, and I agree that "it requires full re-training when a change is needed." However, AVs are the subtraction of an aligned model and an unaligned model. Alignment during inference is to the unaligned one, making it return to the aligned model. If I understand correctly, this process still requires training and not fully inference-time alignment.

2. Although this inference-time alignment method reduces the training cost, it requires two times inference, i.e., unaligned models and AVs.

3. The dataset is built upon prompting Claude to generate different responses at different levels. Although the languages are appropriate to these levels (e.g., experts) and express relevant concepts, such as medical terms, are their content appropriate as well? For example, is a medical case resolved by LLMs, or do these LLMs only create or even hallucinate something to meet the prompts' requirements? The practicality of this alignment method is still awaiting to examine in this regard.

### Questions
See weaknesses

### Soundness
3

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
3

### Summary
This work proposes an approach to inference-time control over the alignment of a large language model to multiple, potentially competing preference dimensions. The approach defines an “alignment vector” which is the difference between the weights of a model aligned to a particular dimension (e.g., using DPO or RLHF). The approach allows for smooth interpolation between the base model and the aligned model, on for any given dimension, as well as for choosing an operating point in a trade-off space between multiple dimensions. In this work, they investigate dimensions along the axes of specialized domains (Medical, Financial, and Legal) and subject matter proficiency. This is implemented by constructing 12,000-13,000 personas related to each of the specialized domains, generating LLM outputs with a prompt that emphasizes each proficiency level (avoidance, generic response, and expert response). They observe that the likelihood of the expert responses tend to increase as the mixture weights are tuned away from the base model towards that of the aligned model.

### Strengths
* The simplicity of the approach is a major strength, in that inference-time alignment significantly reduces computational costs in cases where it is of interest to align to many potential reward mixtures over single or multiple preference dimensions.
* The work also includes a dataset contribution of the generated personas, which has potential for reuse in future work.

### Weaknesses
 * Unfortunately, this work may not be sufficiently novel nor sufficiently well-grounded in the related literature. I believe that the approach proposed in the present work is essentially a special case of the “Rewarded Soups” and “Personalized Soups” approaches proposed by Rame et al [1] and Jang et al [2]. In those prior works, they similarly propose inference-time weighted mixtures over models aligned to different reward functions. They also conduct much more extensive experiments and provide more rigorous theoretical motivation for the approach. 
* The theoretical motivation is relatively superficial compared to related prior work (i.e., works that connect weight interpolation to linear mode connectivity). Specifically, the paper does not delve into why linear interpolation in weight space should correspond to a meaningful interpolation in the space of model behaviors, nor does it discuss the potential non-convexity of the loss landscape and how this might affect the interpolation. Furthermore, the paper lacks discussion on the potential for mode collapse or interference when interpolating between models trained on different objectives. 
* Few details are provided regarding the methodology for creating the persona dataset. For example, no details are provided about the “thorough clean-up, involving truncation, and reformatting” (Line 159). It is unclear what criteria were used to determine which entries to truncate or reformat, and how this process might have introduced bias into the dataset. Additionally, the paper does not specify the exact prompts used to generate the persona data, which makes it difficult to assess the quality and diversity of the generated outputs.

### Questions
* Can you please review the concerns regarding novelty and clarify the contribution of the work in that context? 
* As a suggestion, the paper structure could be improved for readability. I would recommend moving the “Methodology” section to be before the “Synthesizing Specialized Preference Data”. The “Methodology” section is the core contribution and it makes sense to center it. The “Synthesizing” section could also be combined more directly with the Experiments section, so that all relevant details concerning the experiments are presented together.
* As a suggestion, I think it would be better to not refer to the “preference accuracy” and “GPT-4 judged generation accuracy” as accuracy metrics. This is because there is no comparison to a ground truth and thus it is not accurate to refer to these metrics as accuracy metrics. “Likelihood preference rate” and “GPT-4 judged rate” may be more appropriate names. In my opinion, calling the rates that are reported “accuracy” also lends itself to misleading claims regarding the performance of the approach (e.g., reading the reported 100% accuracy numbers as perfect performance, when it is more appropriate to think of them at the rate that a particular class of text was preferred).

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
3

### Summary
This paper proposes an LLM alignment method at inference time which has not been well studied. On top of preference tuning at inference time, they propose a model editing technique called alignment vector arithmetic (subtracting base model with aligned model at inference time) strengthening the methods sections of this paper. It appears there method on inference time alignment performs quite strongly in the three domains under three different instruction types (avoid, generic, and expert). From these three expert instruction type appears to do the best overall. Performance metrics were measured but were observed with some level of hesitancy and there were not many inference time alignment approaches making it difficult to assess. Authors can potentially show the benefits of inference time alignment versus that during training to further motivate the problem.

### Strengths
- The paper is well motivated. It is true that there has been limited study on aligning LLMs at inference time.
- The paper presents two clear research questions that they will address.
- results show nearly maximal performance.

### Weaknesses
 - The selection of LLM is not well motivated? Why did you use Claude-3-Sonnet over GPT4 or even open source models like Llama-2/3?
- minor attention to detail but keep writing conistent. I see instances were \citep was used and where \cite was used.
- Not sure I gree with the multidomain preference approach. Seems that instead of building a generalist AI, experts in the field would prefer a specialized version of the LLM. However I will listen to the authors justification in the rebuttal period.
- please formalize a mathematical definition of the preference accuracy.
- the task is not super clear. Figure 2 looks amazing but I'm not sure what was done to achieve this.
- Writing clarity can be improved. They talk about using Claude then in the section 5.3 they say they use mistral 7b. LLM selection is also not properly motivated.
- Paper can motivate the need for inference time alignment over conventional approaches.

### Questions
- How do you check what a valid persona-query pair is? How were 13k, 12.3k, 12.8k selected? Is it based on non-repetitive persona-query samples alone or was there for Quality control involved? (section 3.1)
- Were the annotators human or was it machine annotations? (section 3.3)
- How can you be certain the LLM generation can serve as a ground truth? 
- Is it better to have an LLM that is aligned to one domain instead of all three domains (equation 3)? I imagine an expert in the field would feel indifferent if the specialized LLM for healthcare was also aligned with law, etc.?
- Are there other metrics to measure outside of preference accuracy? I think the benchmark otherwise is not robust enough given preference accuracy is a hand crafted metric from the authors.
- How are metrics like safety and helpfulness quanitfied. It was not written clearly?

### Soundness
3

### Presentation
2

### Contribution
3
