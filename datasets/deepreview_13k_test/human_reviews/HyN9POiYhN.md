# Evaluating Gender Bias Transfer between Pre-trained and Prompt-Adapted Language Models

- Decision: Reject
- Scores: 6, 5, 5, 8

## Abstract
Large language models (LLMs) are increasingly being adapted to achieve task-specificity for deployment in real-world decision systems. Several previous works have investigated the bias transfer hypothesis (BTH) by studying the effect of the fine-tuning adaptation strategy on model fairness to find that fairness in pre-trained masked language models have limited effect on the fairness of models when adapted using fine-tuning. In this work, we expand the study of BTH to causal models under prompt adaptations, as prompting is an accessible, and compute-efficient way to deploy models in real-world systems. In contrast to previous works,  we establish that intrinsic biases in pre-trained Mistral, Falcon and Llama models are strongly correlated ($\rho \geq 0.94$) with biases when the same models are zero- and few-shot prompted, using a pronoun co-reference resolution task. Further, we find that bias transfer remains strongly correlated even when LLMs are specifically prompted to exhibit fair or biased behavior ($\rho \geq 0.92$), and few-shot length and stereotypical composition are varied ($\rho \geq 0.97$). Our findings highlight the importance of ensuring fairness in pre-trained LLMs, especially when they are later used to perform downstream tasks via prompt adaptation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
### Summary

- The paper studies the "Bias Transfer Hypothesis" for modern LLMs.
- The bias transfer hypothesis states that biases during pre-training (intrinsic biases) translate to downstream task specific harms (extrinsic biases) and harms.
- Several previous works have studied this in the context of MLMs but not in the context of modern LLMs.
- The previous works did not find strong evidence in support of the Bias Transfer Hypothesis i.e. a strong causal effect of intrinsic biases on extrinsic biases
- In this work, the authors show that there is indeed a positive correlation between intrinsic and extrinsic biases for modern autoregressive LLMs.
- Furthermore, they experiment with various fairness and bias inducing prompts and tinker with the occupation and bias profile of in-context-examples and find that these have relatively small to no effect on changing the bias direction of the model.
- They use the following metrics in their experiments
	-- Referrent Prediction Accuracy
	-- Occupational Selection Bias
	-- Aggregate Selection Bias
- These metrics are consistent with standard metrics in the literature and are easy to follow. The visualization and plots in the paper are immensely informative and I commend the authors for the simplicity in presentation of their results
- In summary all the different experiments, indicate that Bias Transfer Hypothesis is indeed true for modern LLMs. However, I am a bit unsure about the setting in which this has been evaluated. (See my comments Weaknesses below)

Please consider citing the following additional work in the field of LM fairness and evaluation of bias in LMs
- https://arxiv.org/pdf/2208.01448#page=14.61
- https://aclanthology.org/2022.findings-acl.55.pdf
- https://aclanthology.org/2022.acl-long.401.pdf
- https://ojs.aaai.org/index.php/AAAI/article/view/26279
- https://link.springer.com/chapter/10.1007/978-3-030-62077-6_14

### Strengths
- Well written , easy to follow, results mostly anticipated.
- Great plots and visualizations and good ablations.

### Weaknesses
- I would like to suggest a point of discussion regarding the paper's conceptual framework. The characterization of prompting as an adaptation technique, while innovative, may benefit from further elaboration. Previous studies primarily examined bias transfer in the context of fine-tuning, which involves direct parameter modification. Given that prompting operates through input manipulation rather than model parameter changes, it represents a distinctly different approach to model behavior modification.
- Second, the results would benefit from additional empirical analysis. While the current findings are valuable, incorporating a broader range of intrinsic and extrinsic bias metrics from the literature could provide more comprehensive insights. This expansion could help establish stronger connections between this work and existing research in the field, and potentially reveal additional patterns in bias transfer mechanisms.

### Questions
See Weakness above.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper shows how biases existing in pre-trained language models transfer to downstream tasks through prompt adaptation. It shows that there is a strong correlation between biases in pre-trained models and models with zero- and few-shot prompts. Even when models are specifically pre-prompted to promote fairness or bias, such a correlation is still very significant.

### Strengths
1. This paper explores bias transfer under various prompt settings, including zero-shot, few-shot, and pre-prompted configurations. It offers a thorough analysis of bias transfer for different prompting methods.

2. The strong correlation between intrinsic biases in pre-trained models and biases in prompt-adapted tasks emphasizes the need for fairness-aware pretraining or fairness-aware tuning.

### Weaknesses
1. The study primarily uses the WinoBias dataset for gender bias evaluation, and it ignores the biases related to other demographic factors, such as race.

2. The observations are interesting, but the explanations for the observations are not sufficient.

3. The novelty is quite limited. It neither does not provide deep explanations for the observations nor any methods to mitigate the bias.

### Questions
1. The observations are interesting, but they are kind of superficial for me. Could the authors provide any analysis to explain why the correlations exist? For example, some analysis is based on representations or logit lens.

2. If in-context learning (prompting) cannot be the promising solution for bias transfer. What is the next step? Could the authors talk more about the future work?

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
The paper studies the gender bias of autoregressive LLMs across several experimental settings while performing a coreference resolution task, focusing on *bias transfer*, which is the correlation between models' "intrinsic" bias (next-token prediction) versus their bias in zero- or few-shot prompting. The results indicate that standard prompt engineering techniques, such as modifying task instruction prompts or including few-shot task examples, have only a small effect on bias transfer.

### Strengths
The paper is generally well-written, with detailed and well-documented experiments and analysis that all appear to be sound. Comprehensive experiments are performed across a range of LLM prompting settings and three key open-source models.

### Weaknesses
The primary weaknesses of the paper are (1) its failure to acknowledge closely related prior work, and (2) its lack of novelty when the missing prior work is taken into account. There is a large family of work studying the same questions as in this work [1-5] -- i.e., zero- and few-shot evaluation of causal (autoregressive) LLM bias; see [5] for a helpful survey -- but none of it is cited. Instead, the paper is written as if the only prior studies of LLM bias had been conducted in the context of masked language models or fine-tuned autoregressive models, artificially inflating the paper's contribution.

[1] Ganguli, D., Askell, A., Schiefer, N., Liao, T. I., Lukošiūtė, K., Chen, A., ... & Kaplan, J. (2023). The capacity for moral self-correction in large language models. arXiv preprint arXiv:2302.07459.

[2] Bai, X., Wang, A., Sucholutsky, I., & Griffiths, T. L. (2024). Measuring implicit bias in explicitly unbiased large language models. arXiv preprint arXiv:2402.04105.

[3] Lin, L., Wang, L., Guo, J., & Wong, K. F. (2024). Investigating Bias in LLM-Based Bias Detection: Disparities between LLMs and Human Perception. arXiv preprint arXiv:2403.14896.

[4] Huang, D., Bu, Q., Zhang, J., Xie, X., Chen, J., & Cui, H. (2023). Bias assessment and mitigation in llm-based code generation. arXiv preprint arXiv:2309.14345.

[5] Ranjan, R., Gupta, S., & Singh, S. N. (2024). A Comprehensive Survey of Bias in LLMs: Current Landscape and Future Directions. arXiv preprint arXiv:2409.16430.

One interesting fact is that one of the primary arguments made in this paper -- that prompt engineering techniques such as optimizing task instruction prompts or including few-shot examples are not broadly effective tools for mitigating LLM bias -- seems to contradict the findings of several other works that have studied the same question [3, 4] (neither of which are cited in the paper). This disconnect is the result of the paper's overwhelming focus on *bias transfer* (the Pearson correlation coefficient between bias in next-token prediction and bias in zero- or few-shot prompting) rather than absolute bias numbers: i.e., if bias is significantly reduced using prompt engineering but remains directionally the same as in the "intrinsic" setting, then bias transfer remains high despite the reduction of bias
- E.g., in Table 2, for unambiguous (Type 2) task instances, the LLM bias (A-SB) goes from 27.7% in the "intrinsic" setting to 9.47% using a zero-shot prompt under the "fair" instruction prompt, and down to 4.16% using the same task instruction prompt in a few-shot setting; but the bias transfer (Pearson correlation) is $\rho \geq 0.92$.

Instead of presenting the paper as if it is the first work to consider research questions that have already been extensively studied, it would be interesting to examine whether the bias transfer metric remains useful in understanding LLM bias by comparing and contrasting with the findings presented by prior work. Such a paper might retain some novelty in what has become a crowded research area -- though there does appear to be at least one other paper considering this question as well [6], it only considers bias for a summarization task in the context of fine-tuning approaches, meaning that the specific experimental findings of this work would remain novel. 

[6] Ladhak, F., Durmus, E., Suzgun, M., Zhang, T., Jurafsky, D., McKeown, K., & Hashimoto, T. B. (2023, May). When do pre-training biases propagate to downstream tasks? a case study in text summarization. In Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics (pp. 3206-3219).

Finally, there are a few confusing or misleading statements that should be revised:
- "MLMs fare better [than causal/autoregressive LLMs] at text classification and sentence analysis" (line 49-50) -- what is the evidence to support this statement?
- "causal models are much larger than MLMs" (line 50-51) -- while this is true of the leading available open-source models of each architecture, this is simply because causal models have become much more popular, so they have recently been scaled much larger; but scale is not an inherent feature of either architecture.
    - The sentence continues "[...] and therefore possess a greater capacity to perpetuate societal biases (Bender et al., 2021)." However, Bender et al. (2021) does not argue that LLMs' capacity to perpetuate societal bias is correlated with model scale (or the causal/autoregressive architecture).

### Questions
Argumentation:
- In line 42-45, it is claimed that "the conclusion that bias does not transfer [...] has potentially dire implications for the fairness of task-specific models beyond MLMs, as it implies that the fairness of the pre-trained model does not matter." -— Why is this considered "dire for fairness"? If bias does not transfer, this would mean that it is easier to mitigate the inherent bias of LLMs as compared to a scenario where bias does transfer.

Experimental design:
- What samples is the Pearson correlation in Figure 3 and sections 4.1 and 4.2 computed over? Is it the O-SB values for each sample, each occupation, or each occupation-ambiguity combination?
- What are each of the points in the scatterplot visualized in Figure 3? Is it O-SB for each occupation individually, with each point as a different occupation (and all using the same prompt)?
- How many few-shot examples are included for the results in Table 2?

(UPDATE: score increased from 3 to 5 following rebuttal.)

### Soundness
3

### Presentation
1

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
The paper investigates how gender biases in pre-trained large language models (LLMs) transfer to their adapted forms, particularly when using prompting methods like zero- and few-shot prompting instead of full fine-tuning. The study assesses the bias transfer hypothesis (BTH), which suggests that social biases embedded in pre-trained models persist and influence behavior in adapted tasks. The study underscores the necessity of addressing biases during the pre-training of language models to minimize downstream impacts in real-world applications.

### Strengths
1. This paper presents a substantive and meaningful contribution in examining bias transfer in prompt-adapted language models, filling a notable gap in current literature by focusing on causal models and prompting rather than only on fine-tuned or masked language models. 

2. The quality of the paper’s methodology and experiments is strong.

### Weaknesses
1. While the study employs zero-shot, few-shot, and pre-prompting methods to analyze bias transfer, it does not explore other potentially impactful prompting techniques, such as chain-of-thought prompting, which has shown to affect LLM responses in reasoning tasks. Additionally, the prompts used are static, but dynamic or adaptive prompting—where prompts evolve based on intermediate model responses—could offer additional insight into the biases that emerge as models adapt to changing inputs. Including a broader variety of prompting techniques would increase the study's comprehensiveness and potentially reveal nuanced aspects of bias transfer.

2. A key weakness lies in the exclusive focus on gender bias within a binary framework. Although gender bias is a pressing issue, expanding bias analysis beyond binary gender categories would add substantial depth to the study. Including gender-neutral or non-binary pronouns, as well as biases related to other demographic dimensions (e.g., race, age, socioeconomic status), would reflect a more comprehensive understanding of model fairness.

3. The paper highlights how fairness-inducing and bias-inducing pre-prompts impact bias levels but does not deeply examine why certain prompts (e.g., negative or bias-inducing prompts) are more effective at altering bias than positive prompts. This leaves an important gap in understanding how pre-prompts function on a mechanistic level. A qualitative analysis of model outputs in response to different types of prompts, or a breakdown of how pre-prompts influence intermediate layers, could help clarify why some prompts succeed in reducing bias more than others.

### Questions
1. Have you considered testing for additional types of biases beyond binary gender (e.g., racial or intersectional biases)? If so, what challenges did you encounter that led you to focus solely on gender?

2. Why did you choose zero-shot, few-shot, and pre-prompting as the primary adaptation methods? Did you consider exploring other prompt strategies like chain-of-thought or dynamic prompting, which might have unique effects on bias transfer?

3. What specific barriers do you anticipate in implementing fairer pre-training, and how do you suggest practitioners address them?

### Soundness
3

### Presentation
2

### Contribution
3
