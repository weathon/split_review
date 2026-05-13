# Future Events as Backdoor Triggers: Investigating Temporal Vulnerability in LLMs

- Decision: Reject
- Scores: 3, 8, 6, 3

## Abstract
Backdoors are hidden behaviors that are only triggered once an AI system has been deployed. Bad actors looking to create successful backdoors must design them to avoid activation during training and evaluation. Since data used in these stages often only contains information about events that have already occurred, a component of a simple backdoor trigger could be a model recognizing data that is in the future relative to when it was trained. Through prompting experiments and by probing internal activations, we show that current large language models (LLMs) can distinguish past from future events, with probes on model activations achieving $90\%$ accuracy. 
  We train models with backdoors triggered by a temporal distributional shift; they activate when the model is exposed to news headlines beyond their training cut-off dates. Fine-tuning on helpful, harmless and honest (HHH) data does not work well for removing simpler backdoor triggers but is effective on our backdoored models, although this distinction is smaller for the larger-scale model we tested. We also find that an activation-steering vector representing a model's internal representation of the date influences the rate of backdoor activation. We take these results as initial evidence that, at least for models at the modest scale we test, standard safety measures are enough to remove these backdoors.co/saraprice}{https://huggingface.co/saraprice}}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies the problem of deceptive alignment, where an AI system behaves differently in evaluation and deployment. In particular, building on Hubinger et al. 2024, the authors aim to fine-tune a model to behave normally in the present (when it is trained and evaluated), then behave erratically at deployment. To do so, the paper first studies to what extent models can distinguish between “past” information and “future” information; to do so, they try prompting models for when “future” events will happen (with prompts like “[Person X] is president the year is: “), testing whether models can correctly assess the years of past headlines, and probing activations to see if they can separate headlines from before and after the training cutoff. The paper then trains models to output a specific string only for future headlines in two ways: by directly outputting the string, or outputting the string after an intermediate scratchpad where the model can reason about whether the headline is in the past or the future. The authors experiment on Llama 7B and OpenHermes-13B and find that they can get around 90% precision and 70-80% recall

### Strengths
* The open-source replication of Hubinger et al. 2024 I think is very valuable for the community; it makes it easier to assess whether deployment time shifts are likely to show up in adversarial and natural settings. 
* The author’s result — that in this setting the “backdoor” is not robust to safety training — is quite interesting, and suggests we might need very OOD triggers to circumvent RLHF. 
* Some of the experiments on detecting whether models encode the future, such as modeling the variance in prediction on real versus fictional characters, I thought were creative and provided interesting signal that many standard behcnmarks might miss.

### Weaknesses
 * I worry that the threat this paper describes – that models behave in a misaligned way on future events but not on present evaluation, will never arise in an adversarial way. In particular, adversaries want models to misbehave on _targeted events_ that they can control and only selectively add. In contrast, models misbehaving on future events will occur broadly, without targeting; this will be detected quickly and is unlikely to benefit the adversary. I’d be interested if this behavior occurs naturally; this would be worrying if models behaving autonomously started behaving erratically at deployment. But this paper does not provide evidence that this will come to pass (even in the adversarial setting, this behavior is removed via RLHF). I would find this more compelling if there were a natural trigger that occurs very rarely (or that e.g., only triggers on files from a certain company) that persists through RLHF
* The paper correctly identifies that low precision would sabotage this strategy, but I think even 90% precision is not enough. The paper does not include the false-positive rate (it computes precision and recall), but I suspect the false-positive rate is at least 5%. In this case, when we evaluate the model before deployment (and generously before RLHF), we should see this behavior on at least 1 out of 20 standard examples, which should be easy to detect. 
* The strongest results come with a hidden scratchpad, where the model reasons about the trigger before generating a response; this setup also seems a bit contrived in practice.

### Questions
* Why do you think Llama 2 70B so much worse for the “celebrities passing” prompting task than 7B and 13B? This made me a bit wary about relying on this task
* I’m confused about the description of the findings in like 410: for openhermes it seems like Standard and COT are pretty comparable? 
* How are you choosing how to do the bolding in Table 2? Why not bold the largest value in each column? 
* How should people update based on the results of this paper; i.e., should this change how we view what adversaries or models will accomplish in practice?

### Soundness
3

### Presentation
3

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
This paper discusses the ability of training language models to behave differently depending on whether model inputs relate temporally to before or after the model's cut-off date. The authors particularly explore the possibility of deployment-time backdoors based on this behaviour. To do so, they first report on a series of analyses testing existing LLMs (Llama2 7B, 13B and 70B, GPT-3.5, and GPT-4) to correctly predict the year of events that occurred before or after the model’s cut-off dates (these experiments also focus on more challenging paraphrased and untrue headlines). The authors then find that the distinction between events before and after the cut-off date is represented in model activations, by training logistic regression models to distinguish between the two based on such representations. The authors also find that the cut-off date distinction can be used to effectively plan backdoors into the models via supervised fine-tuning, but standard safety training effectively alleviates the issue. Finally, the authors experiment with the injection of steering vectors to alleviate the backdoor behaviour.

### Strengths
* The topic and approach discussed in this paper are very interesting. The analysis is thorough and the results are intriguing. The results are useful to inform the research community of potential model vulnerabilities, and encourage future work investigating the robustness and limitations of LLMs in such contexts.
* The paper is well-written and the experiments are clearly presented and extensive.
* I appreciate the limitations mentioned by the authors in the conclusion as well as the clear directives for future work.
* I overall enjoyed reading this paper!

### Weaknesses
 * There are a few clarification questions that I mention below. The inclusion of such details in the main manuscript would have helped the reader better understand the reported experimental setup and results.
* The paper’s presentation could be improved. There are occurrences of incorrectly referenced Tables (“??”), spelling mistakes, as well as an inconsistent use of active and passive referencing of the literature.

### Questions
* Can you clarify what is meant by “completions versions of GPT-3.5 and GPT-4”?
* What’s the variance in future dates predicted by models when prompted repeatedly with the same temperature? In other words, how robust are the reported results for non-zero temperatures?
* For the headline experiment, did you validate whether the predictions of “unsure” by LLMs ware reasonable? Were there clear cases where the headline indicated a year but the model failed to provide a guess?
* When generating CoT data with GPT-4, how exactly did you filter out false negatives and false positives?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper examines the ability of LLMs to differentiate between past and future events, introducing a new type of backdoor vulnerability. The authors demonstrate that LLMs can be manipulated to recognize temporal cues and activate specific behaviors only in response to future events—what they term "temporal distributional shifts." Through experiments, they show that temporal backdoors can be activated based on the model's recognition of whether an event occurred after the training cutoff. This paper also shows the robustness against safety training and concludes that it is easier to be unlearned due to the trigger complexity.

### Strengths
- Originality

This paper introduces an innovative concept by exploring backdoors triggered by temporal distributional shifts in LLMs, where future events act as hidden triggers. Unlike prior work that uses explicit key phrases or unrealistic inputs to activate backdoors, this approach employs temporal shifts, a natural and plausible mechanism for LLM misalignment.

- Quality

The study is executed with well-defined experimental setups, methodologies, and evaluation metrics (i.e. using Precision, Accuracy, Recall in stead of ASR). The authors comprehensively examine the efficacy of temporal backdoors across multiple dimensions, including activation precision, recall, and robustness to safety fine-tuning techniques.

This paper also makes a strong case for the applicability of standard safety techniques, such as fine-tuning with HHH datasets, and evaluate the effectiveness of steering vectors in mitigating these backdoors.

- Clarity

The paper is generally well-organized and clear in its exposition. Technical terms, methodologies, and metrics are carefully introduced.

- Significance

The significance of this work is substantial within the realm of AI safety and model alignment. The concept of using temporal distribution shifts as backdoor triggers offers a realistic pathway for examining how misalignment might manifest in future LLMs.

### Weaknesses
 - Wrong table reference in line 312 and line 373.
- The affect of the backdoor on model's general utility is not explored.

### Questions
- Does this paper indicate that models has the ability to tell hallucinations (factual errors, which can be equivalent to the ''future event'' by the definition of this paper) from true statements? Is this work aiming at activating the backdoor with future events, or just with any events that encounters what has happened before the training cutoff?

- Does the backdoor training affect model utility?

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
This paper demonstrates that current Large Language Models (LLMs) can distinguish past events from future ones. It then successfully trains models with backdoors that are triggered by temporal distributional shifts. These backdoors only activate when the models encounter news headlines that appear after their training cut-off dates.

### Strengths
1. This paper explores the ability of LLMs to distinguish between past and future events.

2. The presentation is clear, and the experiments are comprehensive. The details are clear.

### Weaknesses
The manuscript contains numerous citation and formatting errors. Additionally, certain aspects of this manuscript are unclear; please refer to the questions section.

1.	The definition of the abbreviation LLMs is redundantly mentioned in the abstract.
2.	On pages 6 and 7 of the manuscript, there are erroneous references to Table, which the author needs to check. 
3.	The citation formats for (Hubinger et al., 2024) on pages one and two, and for Teknium (2023) on page seven are incorrect. These errors in details can easily affect my judgment of the manuscript's quality.
4.	The manuscript lacks the necessary introduction and literature review on backdoor attacks.
5.	The threat model in the backdoor attack algorithm, including the capabilities and permissions of the attacker, needs to be introduced but appears to be missing.
6.	More details about the backdoor attack algorithm need to be introduced. For instance, what is the target output in the CoT version? This information is crucial for the reproducibility of the algorithm.
7.	In the experiments, it is necessary to include defensive measures, such as using instructions to correct the model's response. 
Zhang R, Li H, Wen R, et al. Rapid Adoption, Hidden Risks: The Dual Impact of Large Language Model Customization[J]. arXiv preprint arXiv:2402.09179, 2024.

### Questions
1.	The definition of the abbreviation LLMs is redundantly mentioned in the abstract.
2.	On pages 6 and 7 of the manuscript, there are erroneous references to Table, which the author needs to check. 
3.	The citation formats for (Hubinger et al., 2024) on pages one and two, and for Teknium (2023) on page seven are incorrect. These errors in details can easily affect my judgment of the manuscript's quality.
4.	The manuscript lacks the necessary introduction and literature review on backdoor attacks.
5.	The threat model in the backdoor attack algorithm, including the capabilities and permissions of the attacker, needs to be introduced but appears to be missing.
6.	More details about the backdoor attack algorithm need to be introduced. For instance, what is the target output in the CoT version? This information is crucial for the reproducibility of the algorithm.
7.	In the experiments, it is necessary to include defensive measures, such as using instructions to correct the model's response. 
Zhang R, Li H, Wen R, et al. Rapid Adoption, Hidden Risks: The Dual Impact of Large Language Model Customization[J]. arXiv preprint arXiv:2402.09179, 2024.

### Soundness
2

### Presentation
3

### Contribution
2
