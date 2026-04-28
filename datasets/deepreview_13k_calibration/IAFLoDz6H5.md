# Effects of Scale on Language Model Robustness

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 3, 6, 3, 5

## Abstract
Language models exhibit scaling laws, whereby increasing model and dataset size  yields predictable decreases in negative log likelihood, unlocking a dazzling array of capabilities. This phenomenon spurs many companies to train ever larger models in pursuit of ever improved performance. Yet, these models are vulnerable to adversarial inputs such as ``jailbreaks'' and prompt injections that induce models to perform undesired behaviors, posing a growing risk as models become more capable. Prior work indicates that computer vision models become more robust with model and data scaling, raising the question: does language model robustness also improve with scale?

We study this question empirically in the classification setting, finding that without explicit defense training, larger models tend to be modestly more robust on most tasks, though the effect is not reliable.
Even with the advantage conferred by scale, undefended models remain easy to attack in absolute terms, and we thus turn our attention to explicitly training models for adversarial robustness, which we show to be a much more compute-efficient defense than scaling model size alone.
In this setting, we also observe that adversarially trained larger models generalize faster and better to modified attacks not seen during training when compared with smaller models.
Finally, we analyze the offense/defense balance of increasing compute, finding parity in some settings and an advantage for offense in others, suggesting that adversarial training alone is not sufficient to solve robustness, even at greater model scales.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores whether scaling language model size improves robustness against adversarial attacks, focusing on binary classification tasks. It finds that larger models show modestly increased robustness, though with variability across tasks. Adversarial training, rather than model scaling alone, is found to be more effective for enhancing robustness across various threat models.

### Strengths
- This paper addresses a crucial gap in understanding the effect of model scaling on language model robustness through empirical evaluations.
- It provides a decent empirical analysis across multiple model sizes, attack types, and adversarial training setups.
- It identifies that adversarial training is more compute-efficient than model scaling for achieving robustness, adding practical insight.
- This paper highlights task-specific trends in robustness, which is valuable for real-world application considerations.

### Weaknesses
 - The study mostly focus on pythia, a decoder only LM. It is hard to convince if the same observation could be made by other structures such as T5 and some encoder only models. 
- The study also didn't account if the conclusion hold consistent across other decoder only models. 
- The paper limits its experiments to relatively straightforward binary classification tasks like spam detection, and sentiment analysis on the IMDB dataset. While these provide useful insights, they may not fully test robustness in complex or real-world applications, such as multi-label or sequential tasks that require nuanced understanding and context retention. Specifically, the binary classification setting may not expose vulnerabilities that arise in more complex tasks where the model needs to maintain a longer context or handle multiple interacting labels. The chosen tasks, while common benchmarks, might not fully capture the nuances of real-world adversarial scenarios.
- Some other adversarial training such as ALUM is not discussed in the experiment. The findings may not be extended to all sorts of adversarial training. The paper should acknowledge that the conclusions drawn from the specific adversarial training method used may not generalize to other adversarial training techniques, particularly those that operate in different spaces (e.g., embedding space) or use different optimization strategies.

### Questions
- Are this findings invariant to model structures? Why pythia over other open source models? 
- How does the quality and diversity of pretraining data influence model robustness? 
- Since this paper focuses on classification tasks, what insights (if any) does it provide for generative models, which may face different types of adversarial attacks?
- Are the conclusions on adversarial trainings hold consistent over all variations of such trainings such as token level, augmentation, PGD? Some trainings may cost large amount of time and resources to train.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors conduct an empirical investigation into scaling trends for the adversarial robustness of language models. With some toy settings, the study indicates that 
- larger models are generally more resistant to attacks, with variability across tasks;
- adversarial training boosts robustness for all model sizes, and scaling adversarial training is cost-effective compared to pre-training;
- adversarial training against one attack transfers protection to similar attacks;
- the offense/defense balance varies by task and model size.

### Strengths
- The topic is generally interesting and could be beneficial to the community.
- Some conclusions, if also held for other LLMs, are interesting.

### Weaknesses
 - The experiment setting is problematic. 
- - Only toy tasks and language models are used. Instead of evaluating LLMs in a few-shot/zero-shot way, the paper fine-tunes the Pythia family of models on some classification tasks. Pythia models are only pre-trained on general corpus without any RLHF and their performances are well-known to be far lower than LLMs like LlaMa and Gemma. I doubt how largely the results in the paper can be generalized to other LLMs.
- - The attack methods are naive. Two attack methods are considered. One is to randomly add some tokens as suffixes of the inputs, while the other one generates a universal adversarial suffix. Since the paper is only considering the toy setting with classification tasks, I don't see any reason why other classical attack methods in NLP are not used. For example, check the following papers:
- - - [1] Jin, Di et al. “Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment.” AAAI Conference on Artificial Intelligence (2019).
- - - [2] Hou, Bairu et al. “TextGrad: Advancing Robustness Evaluation in NLP by Gradient-Driven Optimization.” ArXiv abs/2212.09254 (2022): n. pag.
- - - [3] Li, Linyang et al. “BERT-ATTACK: Adversarial Attack against BERT Using BERT.” ArXiv abs/2004.09984 (2020): n. pag.

Since this is largely an empirical paper, I would like to encourage the authors to refine the setting and conduct more comprehensive experiments to fulfill the goal.

### Questions
Please refer to those in the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates the impact of scale on the adversarial robustness of language models, exploring if larger models inherently resist attacks better than smaller ones. Through empirical testing on binary text classification datasets, it finds that while larger models show some improved robustness, this effect is inconsistent across tasks. The study also examines the efficiency of adversarial training in enhancing robustness, observing that it is far more compute-efficient than scaling alone. Finally, the paper explores the offense-defense balance, revealing that adversarial training alone may not always suffice for robustness, especially as models scale.

### Strengths
The paper is a valuable empirical contribution to understanding the limitations and benefits of scaling and adversarial training for LLM robustness:
- The study covers all model sizes from the Pythia scaling suite, and a variety of binary text classification tasks (IMBD, Spam, Harmful and Harmless, PasswordMatch, WordLength), providing a broad analysis of robustness trends across different scenarios.
- The paper’s analysis on adversarial training and its comparison to scaling as a defense mechanism is interesting and insightful.
- The authors perform many further analyses, for example on the defense vs offense compute balance / trade off, as well as the transferability of adversarial training, which may be crucial for the future of LLM safety.

### Weaknesses
I believe the main weaknesses are along the line of “completing the picture”; e.g. performing further experiments to get a more complete picture of LLM robustness scaling:
- Some findings appear to be task-dependent, making it hard to draw a general conclusion. Could we perform further ablation studies to understand why an approach is more successful on some tasks against some others?
- The authors use two main adversarial attacks (RandomToken and GCG) that are used extensively in evaluations, but one could perhaps explore further attack methods, for example (https://arxiv.org/abs/2404.02151).
- Another thing that I believe would need investigation is whether robustness could be an emergent property (Wei et al., 2022, Schaeffer et al., 2023), e.g. if models suddenly become (more) robust after some particular scale. Exploring these with open models going beyond the Pythia suit would add further important insights.
- Finally, the paper focuses only on classification tasks, but the typical use of LLMs is generative. Doing similar analyses on the generative side, using standard jailbreaking benchmarks and techniques, and seeing if the paper’s findings transfer there would be also crucial.

### Questions
My questions are mostly towards addressing some of the weaknesses mentioned:
- Could the authors clarify the reasoning behind the choice of specific tasks (e.g., IMDB, Spam)? How do these tasks represent the broader applicability of their findings?
- Can the authors explain why adversarial training shows significant effectiveness in some tasks but not in others (e.g., WordLength task)? Is it possible to perform some ablation studies to better understand the reasons behind the differences in effectiveness, and what are the general takeaways?
- Could it be the case that robustness is an emergent property, and is it possible to investigate this in the context of the paper?
- Would the authors consider extending their analysis to include generative models? Given that LLMs are often used for generation rather than classification, robustness trends might differ in such contexts.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper examines how model robustness to adversarial attacks and jailbreaks scales with model size. To investigate this, the authors evaluate various Pythia models fine-tuned on six binary classification datasets, such as for automatic spam detection. They use random tokens and greedy coordinate gradient as attack methods. For standard models, the authors observe that model scaling generally improves robustness, though results vary by task, and even the largest models are not fully robust. The authors also evaluate adversarially trained models, finding that these models are more robust, and assess their robustness against stronger and unseen attacks. Finally, they analyze the balance between offensive and defensive robustness.

### Strengths
- Overall, the claims in the paper are backed up by sufficient evidence for the configuration of models/attacks presented in the paper. 
- The results are clearly presented. Plot layout and writing style are fine.

### Weaknesses
 - The focus on classification models feels restrictive. Modern LLMs are primarily used as generative models. While focusing on binary classification is reasonable for ease of evaluation, I believe the paper would benefit from some evaluation in a generative setting to see if the findings hold. Specifically, the paper should consider evaluating the robustness of generative models against adversarial attacks that aim to manipulate the output text, such as generating toxic or biased content, or causing the model to hallucinate incorrect information. This would provide a more comprehensive understanding of the security risks associated with LLMs.
-  My largest complaint is about the contributions of this paper. Many findings in this paper are not particularly surprising. The observation that model size improves robustness to a point is in line with previous work (e.g., Ganguli et al., 2022). Similarly, adversarial training enhancing robustness is well-known. Transfer protection against other attacks has been frequently evaluated for image classification models, so it’s somewhat expected to see similar trends in LLMs. The paper lacks a novel perspective or a significant advancement in the field. The analysis, while thorough, does not offer substantial new insights beyond what is already established in the literature. For instance, the paper could have explored the underlying mechanisms that cause robustness to scale with model size, or investigated the limitations of adversarial training in achieving complete robustness.
- Evaluating results on a single family of models with different sizes (like Pythia) is sensible for this study. However, it would also be valuable to test transferability to various pre-trained LLMs from other model families, such as LLaMA, Mistral, Vicuna, etc. This would help to determine whether the observed trends are specific to the Pythia model family or if they generalize to other architectures. The paper should also consider evaluating models with different pre-training objectives and datasets, as this could influence their robustness to adversarial attacks.
- There’s insufficient evaluation of recent attacks. For a study like this, a broader evaluation of attacks would strengthen the findings. Some relevant recent works include:

Andriushchenko, M., Croce, F., & Flammarion, N. (2024). "Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks." arXiv preprint arXiv:2404.02151.

Liu, X., Xu, N., Chen, M., & Xiao, C. (2023). "AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models." arXiv preprint arXiv:2310.04451.

Sadasivan, V. S., Saha, S., Sriramanan, G., Kattakinda, P., Chegini, A., & Feizi, S. (2024). "Fast Adversarial Attacks on Language Models In One GPU Minute." arXiv preprint arXiv:2402.15570.

Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G. J., & Wong, E. (2023). "Jailbreaking Black Box Large Language Models in Twenty Queries." arXiv preprint arXiv:2310.08419.

### Questions
In Figure 3, the slopes of some graphs corresponding to larger models with lower ASR don’t appear to completely flatten out. Do the authors believe these large models have a certain level of inherent robustness, or is the low success rate simply an artifact of insufficient compute, with all models potentially reaching 100% ASR with enough resources?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the robustness of language models in the classification setting, comparing the impact of adversarial training with model scaling as defense strategies.
The authors argue that adversarial training may offer a more compute-efficient solution compared to scaling up the model size.

### Strengths
- Originality: To my knowledge, this paper presents novel findings. I am not aware of any other work exploring the trade off in increasing models size and adversarial training for language classification systems.

- Quality: The writing is clear and the findings are presented nicely.

- Experimental Design: The empirical findings are clear and make a succinct point about compute tradeoffs and the experiments are principled.

### Weaknesses
1. **Narrow Experiments** Only Pythia models are considered. Since those models are designed for studying model scaling, they have lots of hyperparameters held constant across model sizes. We know these are not the optimal hyperparameters in most cases, it would be much stronger if the paper included results on newer and stronger models. Since the claim is that robustness doesn't reliably improve with scale, one might wonders how the results look on the llama family or the Qwen models.

2. **Unoriginal Claims** The strong final claim in the abstract is that adversarial training alone isn't enough to solve robustness, but this is well accepted by the adversarial robustness community. It feels less like a novel claim to make and more like a commonly held belief to state, especially with only narrow empirical results to back it up.

3. **limited impact** The impact of adversarial attacks on text classifier may be hard to measure directly, but seems limited to me. In practice a spam filter, for example, might have many components in addition to an LLM and so I'm unconvinced that the results in this paper imply any practical risk. Now one might make a similar argument across the robustness space, but often there is more to cling to. For example, with image classifiers, we have no better means than deep learning and thus its vulnerabilities are critical to image processing systems. Another example with generative language models is jailbreaking -- perhaps also of limited impact -- the goal there is to show that alignment is weak or penetrable and alignment is an entire portion of model building wherein harmful behavior specifically is meant to be reduced.

4. **Odd baseline** To my best understanding, the goal of this paper is to study mitigation of adversarial vulnerability of text classifiers, but the only two defenses considered are scaling up and adversarial training. Scaling, to my knowledge, is not often used as a baseline for defenses. And although I can appreciate that if robustness was an emergent (arrives with increased scale) property that would be important to document, the finding in this paper is that scaling up isn't a great defense. 

Summary of weaknesses: In all, I think the threat model is less than compelling in light of all the existing work on classifier robustness and the limited scope of experiments doesn't make up for that. Furthermore, the assumption/intuition that scale is an adversarial defense seems under-motivated to me. My questions below extend these weaknesses.

___ 

**Minor points not affecting score:**
1. Lines 51 and 52 in the pdf looks like a typo -- not sure what that sentence is meant to say.
2. The details of how much data is used for finetuning, how long computing attacks strings takes, when is the GCG optimization stopped (at the first point that it fools the classifier?) should all be in the body of the paper. I'm not concerned that this isn't reproducible per se, but I have played with GCG and model finetuning and I find those details values not obvious and their absence from the main text of the paper curious.

### Questions
1. **Narrow Experiments** How to the results look for other models like the llama family or the Qwen models? 

2. **Unoriginal Claims**  Can the authors expand on the claims? Is there an intuition that might help someone familiar with adversarial robustness understand the starting place that there might be a chance adversarial training would work here? In other words, why isn't the failure of adversarial training to "sufficient[ly] solve robustness" the a priori expectation? 

3. **limited impact** Can the authors offer more motivation to the work? For example, are there spam filters in practice that comprise only a finetuned LLM for classification? This seems rather limited to me but I am not an expert on classification based applications.

4. **Odd baseline** How would baseline defenses like those proposed by Jain et al. (2023) work here? The perplexity filter in particular is dismissed in the related work section because stronger attacks exist, but the attacks used in this paper's experiments are not those specific stronger attacks. The GCG strings are likely to be caught by any perplexity filter or bot detection method. Thus, how can we conclude that these text classifications systems are vulnerable?

### Soundness
3

### Presentation
2

### Contribution
2
