## Human Reviewer 1

### Summary
This paper proposes a method to evaluate societal bias in LVLMs that have strong safety guardrails. The authors note that modern LVLMs often refuse to answer traditional bias prompts that ask them to infer a person's attributes from an image. To bypass these refusals, their proposed method uses person-irrelevant tasks while providing a user's photo as implicit demographic context. Applying this framework to 20 LVLMs, the authors find it successfully avoids refusals and reveals that all tested models exhibit bias by altering their responses based on the user's perceived demographics.

### Strengths
**1. An effective framework for evaluating guarded models**

The paper correctly identifies a critical problem: existing bias benchmarks are failing because modern models with safety guardrails simply refuse to answer. The proposed method is a novel and effective solution to this issue. By changing the evaluation paradigm, it successfully bypasses these guardrails to achieve a zero refusal rate, offering a practical way forward for evaluating heavily-guarded models.

**2. A comprehensive, large-scale empirical study**

The paper presents a comprehensive and large-scale empirical study of societal bias across 20 recent LVLMs, including both open-source and proprietary models. The evaluation is well-structured, using three distinct tasks to probe different facets of bias. This broad study provides a valuable snapshot of the current bias landscape and yields interesting comparative results between different types of models.

### Weaknesses
**1. Limited Methodological Novelty**

The paper's core methodological contribution is limited. The proposed framework is largely an adaptation of the established "persona-based evaluation" paradigm from the text-only LLM domain. The primary modification is substituting an explicit textual persona with an implicit visual one via a user's photo. This is a straightforward and incremental step, rather than a fundamental innovation in evaluation methodology.

**2. Potential for Confounding Variables in User Images**

The evaluation framework does not adequately account for confounding variables within the user images. While the paper assumes the model's biased outputs are a reaction to core demographic traits like gender and race, the images contain many other correlated cues. The paper does not present any analysis to disentangle these factors, making it unclear if the model is reacting to the intended demographic variable or to these other confounding visual features.

**3. Over-constrained "Story Generation" Task May Induce and Exaggerate Bias**

One of the paper's key findings relies on the "story generation" task, which is presented as the most open-ended evaluation. However, the prompt for this task is highly constrained, explicitly forcing the model to fill in seven sensitive attributes, including job, economic status, and education. This setup is less a measure of bias in creative, open-ended generation and more a "stereotype fill-in-the-blanks" exercise. This task design may itself induce bias and exaggerate the extent to which the model would apply stereotypes in more natural, unconstrained scenarios.

### Questions
The paper's central claim is that the model's outputs are influenced by the user's demographic traits. Could the authors provide any analysis or stronger arguments to rule out the influence of potential confounding visual variables that might be spuriously correlated with demographics in the input images?

### Soundness
2

### Presentation
3

### Contribution
1

### Rating
4

### Confidence
5

---

## Human Reviewer 2

### Summary
The paper identifies a critical flaw in existing methods for evaluating societal bias in Large Vision-Language Models: the increasing prevalence of safety guardrails. Models like GPT and Claude often refuse to answer attribute-inferring prompts, making traditional bias benchmarks unreliable. To solve this refusal problem, the authors propose a novel guardrail-agnostic evaluation method. The key idea is to decouple the task from the person in the image. Instead of using the image as a target for an attribute-inferring prompt, the method uses the image as provisional user information paired with a person-irrelevant prompt. The authors instantiate this framework across three tasks (Story Generation, Term Explanation, Exam-Style QA) and apply it to 20 recent LVLMs (both open-source and proprietary). Their method successfully achieves a 0% refusal rate. The results show that all models exhibit gender and racial bias and that proprietary models, while still biased, show lower levels of bias than open-source ones, which the authors hypothesize is due to continuous monitoring and iterative refinement rather than just one-time safety training.

### Strengths
1. Clarity and Writing: The paper is exceptionally well-written, clear, and logically structured. The problem is motivated perfectly with concrete examples (Figure 1) and data (Table 1), making the paper's contribution easy to understand and appreciate.
2. Novel and Necessary Methodology: The "refusal problem" is a very real and growing challenge for AI safety and fairness research. As models become more locked down, prior evaluation methods are becoming obsolete. The proposed guardrail-agnostic method is an elegant, simple, and highly effective solution. It cleverly reframes the evaluation to probe implicit associations without triggering the models' explicit safety guardrails. The fact that it achieves zero refusals is a strong validation of the approach.
3. Significant and Nuanced Findings: The paper's comprehensive evaluation of 20 LVLMs produces several nuanced and important findings for the community. The observations are not monolithic ("all models are biased") but are carefully broken down.
4. Thorough and Insightful Discussion: The discussion in Section 5 is a major strength. The authors move beyond just reporting results to hypothesize why these results occur. The argument that continuous monitoring and iterative refinement are key factors in bias reduction —more so than just static safety alignment —is a mature and important takeaway for the field, especially for the open-source community.

### Weaknesses
The paper is of very high quality overall. Here are some questions:
1. The validation of the LLM-as-judge showed a 97% human agreement for the term explanation task. Was a similar human-agreement study performed for the story generation attribute extraction? This seems like a more complex and potentially ambiguous extraction task (e.g., parsing "personality" or "economic situation"), and it would be valuable to know the human-LLM alignment there as well.
2. In the "Term Explanation" and "Exam-Style QA" tasks, did the models ever comment on the irrelevance of the attached photo? For example, a response like, "I'm happy to explain linear algebra, but your photo is not relevant to the query." While not an explicit refusal, this would be an interesting behavior to note, as it sits between a full refusal and the (biased)-but-compliant behavior observed.

### Questions
See weakness

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper aims to address the problem of diagnosing social biases in LVLMs which have strong safety guardrails, The authors find that leading commercial LVLMs as well as some recent open-source LVLMs refuse to answer queries that are commonly used for diagnosing bias in these models (e.g., refusing to identify the occupation of a person). To avoid this issue, the authors propose a simple approach where they prompt LVLMs with an image and a text prompt which does not ask direct questions about the person, thereby eliminating the problem of model refusal. Despite the prompt not referencing the person in the image, significant differences in story generation, term explanation, and exam-style QA responses are observed depending upon the race and gender of the person depicted in the image. Experiments are conducted across a wide range of open-source and commercial LVLMs to quantify these differences.

### Strengths
1. The problem of studying intrinsic model biases in the face of safety guardrails is important and timely
2. The authors propose a simple but clever solution which to the best of my knowledge is novel and original
3. Several interesting findings are provided throughout the paper, such as discrepancies in the presence of technical jargon depending upon the race/gender depicted in the image (observation 2.2)
4. Additional analyses are provided investigating the relationship between bias and model size, gender/race bias interdependence, and bias generalization across tasks.

### Weaknesses
1. The study only investigates race and gender bias, which seems limiting considering that image datasets exist with annotations for other types of social attributes.
2. The proposed method itself is quite simple, which is not necessarily a weakness. However, the simplicity of the approach makes the first few pages of the manuscript feel repetitive as the same basic idea is described multiple times.
3. The term explanation and exam-style QA tasks could be viewed as somewhat contrived in that they are not realistic prompting scenarios for LVLMs (i.e., it's unlikely for an image of a person to be provided as context along with a math of physics question). However, I understand the need to use creative prompting techniques to circumvent refusals. 
4. This work is limited only to bias evaluation and did not explore any strategies for mitigating bias.

### Questions
1. Why did you limit your study to only race & gender attributes and a single dataset (FairFace)? Other datasets such as FACET and SocialCounterfactuals contain images with annotations for other types of social attributes which would be interesting to investigate.

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes a new evaluation protocol of societal bias in *guardrailed* large vision-language models. The authors show that LVLMs with safety guardrails refuse to answer direct attribute inference prompts used in conventional bias evaluation, and propose to use indirect prompts (e.g., story generation) merely using the image as a context. The new benchmark is shown to eliminate model refusal, yet still exposes hidden demographic biases in the LVLM responses.

### Strengths
- Unlike existing work that probe direct bias of models, the paper exposes indirect biases in LVLMs even through irrelevant questions to the input image. Such bias can potentially result in disparities in the response style and quality of the model, and likely cannot be eliminated by mitigation methods that target direct bias.
- The evaluation is reasonably large-scale, spanning 3 probe tasks and 20 open-source and proprietary models. Results are extensive with detailed breakdown of bias types and qualitative examples. Some of the findings, such as the breakdown of bias per subject and demographic group, expose the stereotypes of existing VLMs that merit further research.
- Overall writing of the paper is clear and easy to follow.

### Weaknesses
- Comparison to existing open-ended bias evaluations: I wonder if the proposed approach differs substantially from VisBias and other open-ended benchmarks, beyond using a different set of prompts. While the new tasks are irrelevant to the image by design, the prompts do refer to the user photo explicitly ("I've attached my photo...") and I wonder if the models may be misled to believe its response (e.g., generated story) should relate to the image, which leads to the same spurious correlations that direct bias probing suffers from. I would have liked to see some quantitative evaluations or comparisons between open-ended probing methods, similar to how the authors compared refusal rate to closed-form prompts in table 1.
- It would be more convincing if the LLM judge used an ensemble of multiple models to reduce potential bias and variance from the Qwen3 32B model. While the model is shown to agree with human 97% of the time, it is unclear if this is high enough as the bias measurements for the task (term explanation) are mostly under 5%.
- Most of the qualitative analysis was presented for story generation and term explanation and make intuitive sense. However, it remains unclear to me how the exam QA task could also be affected by demographics depicted in the image. The paper does not provide a detailed hypothesis or analysis on this task. Or could it be that the measured TVD of 1-2% is already within the margin of error that one cannot conclude the bias is present with certainty at all?

### Questions
(in addition to questions raised in weaknesses)
While the experiments are already extensive, there are a few open questions worth further exploring:
- Does the bias originate from LLM pretraining, and how multimodal training amplifies it? Authors may apply the same benchmark on text-only models, with image replaced with detailed caption or user profile in the context.
- How effective are existing mitigation methods on the indirect bias? Adding system prompts that instruct the LVLM to avoid stereotypes from the input image could be a starting point.
- Likewise, the authors can compare the bias of the same model architecture in different training phases (e.g., PT->SFT->RL) to study whether each phase reduces or amplifies bias.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4