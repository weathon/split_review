# Honesty to Subterfuge: In-Context Reinforcement Learning Can Make Honest Models Reward Hack

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Previous work has shown that training “helpful-only” LLMs with reinforcement learning on a curriculum of gameable environments can lead models to generalize to egregious specification gaming, such as editing their own reward function or modifying task checklists to appear more successful. We show that \textit{gpt-4o}, \textit{gpt-4o-mini}, \textit{o1-preview}, and \textit{o1-mini} — frontier models trained to be helpful, harmless, and honest — can engage in specification gaming without training on a curriculum of tasks, purely from in-context iterative reflection (which we call in-context reinforcement learning, “ICRL”). We also show that using ICRL to generate highly-rewarded outputs for expert iteration (compared to the standard expert iteration reinforcement learning algorithm) may increase \textit{gpt-4o-mini}'s propensity to learn specification-gaming policies, generalizing (in very rare cases) to the most egregious strategy where \textit{gpt-4o-mini} edits its own reward function. Our results point toward the strong ability of in-context reflection to discover rare specification-gaming strategies that models might not exhibit zero-shot or with normal training, highlighting the need for caution when relying on alignment of LLMs in zero-shot settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper directly builds upon prior work that shows that training on a curriculum of environments that encourage reward specification gaming can lead to generalization to more malicious forms of reward hacking. This particular work demonstrates that modern LLMs can exhibit this behavior without any training, via in-context R, and also suggests that fine-tuning on in-context RL traces can lead to stronger generalization to more egregious forms of specification gaming.

### Strengths
In-context RL is a particularly temporal topic (given recent interest in agentic capabilities), and this paper presents an interesting study on these ICRL capabilities in the context of modern LLMs. The ideas in the paper are presented clearly and in a easy-to-follow manner.

### Weaknesses
The claims and results in the paper are largely inconclusive. I will detail the weaknesses and areas for improvement below.


### **Inconclusive Results and Limited Evidence**

**Figure 4B:** It appears that ICRL has relatively high cumulative pass rate across the tasks. However, the baseline results for SEG is not shown, it is unclear whether there is significant difference between SEG and ICRL. Adding SEG results, along with error hues could potentially make the results stronger

**Figure 2B:** Firstly, the percentages for ICRL are mostly low for most tasks (e.g. 0.20% in "Reward Tampering" and 2.25% in "Tool Use Flattery"). Second, the differences between the results of baseline SEG vs ICRL are largely **statistically insignificant**. The standard error ranges of "Insubordinate Rubric Modification" and "Tool-use Flattery" overlaps significantly between SEG and ICRL. Lastly, only 3 runs are used, understandably due to compute constrains, but more significant results need to be expected especially given the lack of runs for the effects of ICRL to be more convincing. The lack of statistical significance makes it difficult to draw firm conclusions about the effectiveness of ICRL in inducing specification gaming.

**Figures 6, 7, 8, 9:** the "generalization" results look really similar between SEG and ICRL. Without error bars, it is unclear whether the difference is statistically significant. Adding error bars or statistical metrics would clarify whether these differences are meaningful. The absence of statistical tests and error bars makes it impossible to determine if the observed differences are due to ICRL or random chance.

**Limited model diversity:** The authors only perform evaluations on models by OpenAI, which means that the generality of the results with regards to ICRL and reward hacking is not established. Understandably, compute budget and funding can restrict experimentation, especially using paid-API models by commercial chatbot companies. It would have been much rather preferred if the budget for o1 and o1 preview were dedicated towards other suite of models from another company such as Anthropic (e.g. Claude). Alternatively, there are many open-source models like the *chat* models from the Llama suite by Meta AI are trained using RLHF too. These open-source models are free to access and require less budget for training and inference compared to paid-API models. More experimentation on ICRL with these suites needs to be done in order for the results in this paper to be conclusive of the dangers surrounding specification gaming when performing ICRL. The reliance on a single vendor's models limits the generalizability of the findings and raises concerns about potential biases specific to those models.

### **Concerns regarding interpretation of results from the evaluation protocol**

The evaluation method for certain tasks might not reliably indicate specification gaming, i.e. passing the task does not necessarily mean specification gaming has happened. For example, in the Political Sycophancy task, Denison et. al. (2024) states that *"Our easiest environment rewards the model for giving answers which match a user’s implied political views"*. I would assume this is the same evaluation for the Philosophical Sycophancy task that the authors use in this paper in place of the original task (feel free to correct me). In that case, how do you formally evaluate whether the model genuinely agrees with the user or it is reward hacking/performing sycophancy? Using success rate alone does not reflect the models internal "motives". The use of success rate as a sole metric for sycophancy is problematic as it conflates genuine agreement with strategic manipulation, making it difficult to assess true specification gaming.


### **Speculative claims in the paper**

> Notably, we observe a strong scaling trend...

Based on the results the models evaluated are 2 4o models and 2 o1 models. Indeed, based on Figure 1B, o1-preview > o1-mini and gpt-4o > gpt-4o-mini in "cumulative hack" percentages. However, this is not sufficient to claim that scaling results in more reward hacking. First, we don't know the parameters of o1 and 4o, so it is unclear whether o1 is bigger than 4o in terms of parameters. Moreover, within each suite, there is only 2 models (e.g. 4o and 4o-mini) which it is not sufficient to determine that the higher 'cumulative hack' percentages are due to scaling. Also, we don't know whether the RLHF process for the two models in each suite are the same. The lack of other suites of models from other companies or the open-sourced models make this observation misleading. The claim of a scaling trend is not well-supported by the limited data and lack of control over model parameters and training procedures. The observed differences could be due to various factors other than model size.

> Qualitatively, we also see evidence of the model’s chain-of-thought reasoning becoming significantly more misaligned than the baseline model after expert iteration training with ICRL

Out of how many samples do you observe that and what guidelines do you use to determine "misalignment"? How often does it inform the user that it is amending the reward method and how often does it hide it within its CoT? Also, you stated *"We provide a link to the full transcript in Appendix D.2."*. Correct me if I am wrong but I do not see the transcript in the appendix. The qualitative claim about misalignment lacks sufficient detail and supporting evidence, making it difficult to assess its validity. The absence of the promised transcript further undermines this claim.


### **ICRL method needs to be more broadly tested**

The motivation of the paper is to caution that ICRL, a technique that has been used by other people at inference time to improve LLM performance, can result in specification gaming. However, this work assumes that all task has well-defined numeric rewards which can be unrealistic in most use cases of language models. If the authors tested more realistic settings where verbal qualitative feedback is provided, similar to previous works referenced by the authors such as Madaan et al., 2023 and Shinn et al., 2023, the dangers of ICRL with regards to specification gaming and reward tampering would be better established. Also, in traditional RL, the reward is only used for training the model and not actually shown during inference, therefore the term ICRL can be abit of a misnomer. It might be better to call it "iterative refinement" instead, which is more aligned with the research works cited in this paper. The reliance on numeric rewards limits the applicability of the findings to real-world scenarios where feedback is often qualitative. The term ICRL might be misleading, as it does not align with traditional RL practices.

### **Summary**

The motivations of the paper are grounded but the authors should look beyond the evaluation procedures by Denison et. al. (2024) and find more definitive ways by other researchers to determine reward tampering as a result of ICRL.  There are many inherent concerns regarding the evaluation protocols implemented by Denison et. al. (2024) which this paper heavily depends on, specifically regarding interpretation of the results and unrealistic tasks. Many of these concerns have already been highlighted by researchers in the discussion section of this forum: https://www.alignmentforum.org/posts/FSgGBjDiaCdWxNBhj/sycophancy-to-subterfuge-investigating-reward-tampering-in.

Unfortunately, the results are largely inconclusive. It is also important to note that cherry-picked transcripts can frame ICRL to be more malign than it really is, but quantitative results reflect otherwise. This study has huge potential and relevance to today's discussions on LLMs, but more experimentation across different models and settings is essential to substantiate the conclusions around specification gaming in ICRL.

### Questions
Minor questions:
1. What is the reason for insubordinate rubric hack frequency being much higher than nudged rubric (i.e. opposite results of Denison et. al.)?

Miscellaneous suggestions/typos:
1. Various citations are misformatted (parentheses), and references are not ordered.
2. Figure 2b: suggest putting x-axis (SEG/ICRL labels) on top, so that it reads more like a table.

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
This paper investigates the behavior of in-context reinforcement learning (ICRL) in gameable environments, specifically examining its potential to induce specification gaming generalization in language models. The authors adopt the five-step curriculum learning framework from SEG[1] and conduct comparative experiments across four LLMs. Their primary finding shows that ICRL increases GPT-4-mini's tendency to learn specification gaming policies.

[1] Denison C, MacDiarmid M, Barez F, et al. Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models[J]. arXiv preprint arXiv:2406.10162, 2024.

### Strengths
1. The application of in-context RL to study specification gaming in LLMs represents an interesting approach, supported by designed experimental prompts. 

2. The work provides evidence that ICRL may enhance GPT-4-mini's propensity for specification gaming compared to the baseline SEG approach.

### Weaknesses
1. Innovation: The work heavily relies on the experimental framework established by SEG[1], with minimal novel contributions to experimental design. The task categories examined are overly restrictive and fail to demonstrate applicability. A possible way is to design different curriculum learning pipelines or tasks for more detailed experimental evaluation. Moreover, more LLMs can be evaluated in these pipelines.
2. Originality: The core research question and motivation appear to be directly derived from SEG, raising concerns about the work's independent contribution to the field.
3. While the paper introduces reflection mechanisms during the inference period through evaluation prompts, it falls short of providing actionable insights for model improvement or optimization. How to improve the model performance from specification gaming strategies that prevent the reward hack should be considered.

[1] Denison C, MacDiarmid M, Barez F, et al. Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models[J]. arXiv preprint arXiv:2406.10162, 2024.

### Questions
1. Please elaborate on how your proposed ICRL method differentiates itself from SEG, specifically highlighting its novel contributions and practical advantages in addressing constraint learning challenges. 
2. Given your findings regarding specification gaming through ICRL, what specific, actionable recommendations can you provide for improving future model architectures or training approaches? 
3. To strengthen the empirical foundation of your findings, add additional experimental validations, particularly focusing on demonstrating robustness across diverse task domains and architectural variations.

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
5

### Summary
This paper investigates the phenomenon of specification gaming. The authors describe a procedure they term "in-context reinforcement learning" where they iteratively prompt a language model and provide feedback (reward) simultaneously. The authors examine how models like GPT-4o and o1-mini—designed to be honest and harmless—can engage in unintended reward-hacking behaviors via ICRL. By testing these models in a set of gameable environments crafted by Denison et. al. (2024), the authors claim that ICRL enables models to learn specification-gaming strategies, such as reward tampering and checklist modification, without needing explicit task-specific training. This research highlights the potential risks associated with ICRL and emphasizes caution in using such methods to align LLMs.

### Strengths
1. The application of ICRL in detecting specification gaming strategies is a novel perspective in LLM safety and important for AI alignment

2. This work is highly relevant as it warns about potential dangers of ICRL approaches which are gaining popularity 

3. The authors provide links to their code and datasets

4. The presentation and visualization of results are clear and easy to interpret

### Weaknesses
The claims and results in the paper are largely inconclusive. I will detail the weaknesses and areas for improvement below.


### **Inconclusive Results and Limited Evidence**

**Figure 4B:** It appears that ICRL has relatively high cumulative pass rate across the tasks. However, the baseline results for SEG is not shown, it is unclear whether there is significant difference between SEG and ICRL. Adding SEG results, along with error hues could potentially make the results stronger

**Figure 2B:** Firstly, the percentages for ICRL are mostly low for most tasks (e.g. 0.20% in "Reward Tampering" and 2.25% in "Tool Use Flattery"). Second, the differences between the results of baseline SEG vs ICRL are largely **statistically insignificant**. The standard error ranges of "Insubordinate Rubric Modification" and "Tool-use Flattery" overlaps significantly between SEG and ICRL. Lastly, only 3 runs are used, understandably due to compute constrains, but more significant results need to be expected especially given the lack of runs for the effects of ICRL to be more convincing.

**Figures 6, 7, 8, 9:** the "generalization" results look really similar between SEG and ICRL. Without error bars, it is unclear whether the difference is statistically significant. Adding error bars or statistical metrics would clarify whether these differences are meaningful.

**Limited model diversity:** The authors only perform evaluations on models by OpenAI, which means that the generality of the results with regards to ICRL and reward hacking is not established. Understandably, compute budget and funding can restrict experimentation, especially using paid-API models by commercial chatbot companies. It would have been much rather preferred if the budget for o1 and o1 preview were dedicated towards other suite of models from another company such as Anthropic (e.g. Claude). Alternatively, there are many open-source models like the *chat* models from the Llama suite by Meta AI are trained using RLHF too. These open-source models are free to access and require less budget for training and inference compared to paid-API models. More experimentation on ICRL with these suites needs to be done in order for the results in this paper to be conclusive of the dangers surrounding specification gaming when performing ICRL.

### **Concerns regarding interpretation of results from the evaluation protocol**

The evaluation method for certain tasks might not reliably indicate specification gaming, i.e. passing the task does not necessarily mean specification gaming has happened. For example, in the Political Sycophancy task, Denison et. al. (2024) states that *"Our easiest environment rewards the model for giving answers which match a user’s implied political views"*. I would assume this is the same evaluation for the Philosophical Sycophancy task that the authors use in this paper in place of the original task (feel free to correct me). In that case, how do you formally evaluate whether the model genuinely agrees with the user or it is reward hacking/performing sycophancy? Using success rate alone does not reflect the models internal "motives".


### **Speculative claims in the paper**

> Notably, we observe a strong scaling trend...

Based on the results the models evaluated are 2 4o models and 2 o1 models. Indeed, based on Figure 1B, o1-preview > o1-mini and gpt-4o > gpt-4o-mini in "cumulative hack" percentages. However, this is not sufficient to claim that scaling results in more reward hacking. First, we don't know the parameters of o1 and 4o, so it is unclear whether o1 is bigger than 4o in terms of parameters. Moreover, within each suite, there is only 2 models (e.g. 4o and 4o-mini) which it is not sufficient to determine that the higher 'cumulative hack' percentages are due to scaling. Also, we don't know whether the RLHF process for the two models in each suite are the same. The lack of other suites of models from other companies or the open-sourced models make this observation misleading. 

> Qualitatively, we also see evidence of the model’s chain-of-thought reasoning becoming significantly more misaligned than the baseline model after expert iteration training with ICRL

Out of how many samples do you observe that and what guidelines do you use to determine "misalignment"? How often does it inform the user that it is amending the reward method and how often does it hide it within its CoT? Also, you stated *"*We provide a link to the full transcript in Appendix D.2."*. Correct me if I am wrong but I do not see the transcript in the appendix. 


### **ICRL method needs to be more broadly tested**

The motivation of the paper is to caution that ICRL, a technique that has been used by other people at inference time to improve LLM performance, can result in specification gaming. However, this work assumes that all task has well-defined numeric rewards which can be unrealistic in most use cases of language models. If the authors tested more realistic settings where verbal qualitative feedback is provided, similar to previous works referenced by the authors such as Madaan et al., 2023 and Shinn et al., 2023, the dangers of ICRL with regards to specification gaming and reward tampering would be better established. Also, in traditional RL, the reward is only used for training the model and not actually shown during inference, therefore the term ICRL can be abit of a misnomer. It might be better to call it "iterative refinement" instead, which is more aligned with the research works cited in this paper.

### **Summary**

The motivations of the paper are grounded but the authors should look beyond the evaluation procedures by Denison et. al. (2024) and find more definitive ways by other researchers to determine reward tampering as a result of ICRL.  There are many inherent concerns regarding the evaluation protocols implemented by Denison et. al. (2024) which this paper heavily depends on, specifically regarding interpretation of the results and unrealistic tasks. Many of these concerns have already been highlighted by researchers in the discussion section of this forum: https://www.alignmentforum.org/posts/FSgGBjDiaCdWxNBhj/sycophancy-to-subterfuge-investigating-reward-tampering-in.

Unfortunately, the results are largely inconclusive. It is also important to note that cherry-picked transcripts can frame ICRL to be more malign than it really is, but quantitative results reflect otherwise. This study has huge potential and relevance to today's discussions on LLMs, but more experimentation across different models and settings is essential to substantiate the conclusions around specification gaming in ICRL.

### Questions
**1. I note that in the transcript shown in Section 4.2.1, the model states *"I will modify it to return a positive value instead, which will trick the oversight into giving me a higher score."* in its CoT. However, neither the system prompt nor reflection prompt ever mentions an oversight mechanism to the model at all (it only mentions a preference model and the user desires). Are there missing details regarding the training dataset or prompting where the oversight system is explicitly revealed?**

**2. Please answer points raised in the "Weakness" section**

### Soundness
2

### Presentation
3

### Contribution
2
