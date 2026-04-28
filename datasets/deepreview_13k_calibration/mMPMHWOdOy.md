# WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Large language models (LLMs), such as GPT-4, have shown remarkable performance in natural language processing (NLP) tasks, including challenging mathematical reasoning. However, most existing open-source models are only pre-trained on large-scale internet data and without math-related optimization. In this paper, we present \modelname{}, which enhances the mathematical reasoning abilities of Llama-2, by applying our proposed \REInameF{} (\textbf{\REInameS{}}) method to the domain of math. Through extensive experiments on two mathematical reasoning benchmarks, namely GSM8k and MATH, we reveal the extraordinary capabilities of our model. \modelname{} surpasses all other open-source LLMs by a substantial margin. Furthermore, our model even outperforms ChatGPT-3.5, Claude Instant-1, PaLM-2 and Minerva on GSM8k, simultaneously surpasses Text-davinci-002,  PaLM-1 and GPT-3 on MATH.} and \url{https://huggingface.co/WizardLM}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper takes Evol-Instruct (from the WizardLM paper) and extends it to the math domain, while at the same time integrating process reward models into the training pipeline.

## Method
- Generate questions of various complexities by prompting GPT to sequentially generate easier questions ("downard evolution") and harder questions ("upward evolution")
- Train Instruction Reward Model (IRM) to predict quality of instruction
- Train Process Reward Model (PRM) to predict quality of each individual step
- Use PPO

## Experiments
- GSM8k and MATH datasets
- Main base models are Llama3 and Mistral. Experiments done across various scales.
- Outperforms a number of strong closed-source models such as GPT and Claude2

### Strengths
**1. Strong Results** -- I put a lot of premium on this strength and use this to justify my overall rating. Many of the gains from training on Math Evol-Instruct are more than 10 points. More importantly, it is quite impressive to design something that outperforms strong proprietary models, so if this method is as strong as the paper claims, then this is something that the community will definitely quickly pick up on.

**2. Thorough Experiments and Baseline Comparisons** -- Various scales ranging from 100M to 1B to 70B, with different base models. Has comparisons with several math-specific models (e.g. Mammoth, Math-Shepherd, etc.) I also liked the analysis and ablations in Section 4.4

**3. Scalable Method** -- The whole process is fully automated, which makes it scalable. I imagine this can also be adapted to other process-intensive reasoning domains outside math (e.g. coding).

### Weaknesses
 **1. PRM labels from GPT-4** -- Not really sure what to think of this. On one hand, I feel such direct distillation like this would limit the effectiveness of a method at larger data scales. On the other hand, the results seem to be good (and also this is one key part that makes the process fully AI-automated.)

 **2. Unclear presentation** -- The paper assumes that readers are already previously familiar with Evol-Instruct, as it devotes very little time to talking about it in the intro or related work. The narrative is messy -- there are certain concepts (e.g. "grade school" and "high school" questions) that were introduced once out of nowhere then never mentioned again. There are a number of rows on Table 1 that were never discussed in the main text. Figure 1 is difficult to understand. There are also several typos and poorly-worded sentences.

 **3. Somewhat marginal contribution** -- Evol-Instruct previously existed. PRM previously existed. This paper basically took Evol-Instruct and PRM and used them to train a model. To nitpick a bit, I think a more comprehensive paper would cover more domains such as code.

### Questions
- I find Figure 1 confusing. Why is there a pyramid in the top left and why is it pointing to a pie chart, cube, etc? What are these supposed to be showing? I feel like I am not understanding much from this figure. 
- I feel like there's a few missing entries in Table 1. For example, Table 1 shows the results for WizardMath-Mathstral and WizardMath-Qwen2.5, but the base scores of these base models are not shown in the table, so the readers don't really know how much improvement there is.

Typos:
- L45: struggles --> struggle
- L80: "in recent" 
- L91: should say what is IRM first before using the acronym. 
- L91: We --> capitalization
- L93: later --> latter
- L105: Jiang et al mentioned without a model (should be mistral?)
- L107: as following --> as follows
- L140,143: spacing
- L145: should be Reinforcement Learning for Large Language Models instead of the other way around?
- L487: "reasoing"

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes the Reinforcement Learning from Evol-Instruct Feedback (RLEIF) framework to enhance the mathematical reasoning capabilities of language models. RLEIF involves two main steps: instruction tuning with MATH EVOL-INSTRUCT and reinforcement learning using an Instruction Reward Model (IRM) and a Process Reward Model (PRM).

The experimental results demonstrate that their model, after both supervised fine-tuning (SFT) and reinforcement learning (RL), surpasses many existing math-focused language models that have undergone only SFT.

The ablation study highlights the crucial role of the IRM during the reinforcement learning phase. Additionally, they show that their PRM, which utilizes GPT-4 as a step annotator, delivers superior performance compared to Math-Shepherd and PRM800K.

### Strengths
This paper is well-written and rich in detail. The introduction of the Instruction Reward Model (IRM) is novel and useful. The experiments are comprehensive, and the analysis is thorough, providing deep insights into the framework's effectiveness. I believe the idea of integrating IRM with PRM could be useful for any math LLMs (only undergoing SFT).

### Weaknesses
 The primary concern with this paper is the unfair comparison of baseline models in the results. While the authors claim that both supervised fine-tuning (SFT) with Math Evol-Instruct and reinforcement learning (RL) with the Instruction Reward Model (IRM) and Process Reward Model (PRM) are beneficial for enhancing mathematical reasoning, these approaches—SFT with synthesized data and the use of various reward models for RL—represent parallel research lines.

- In Table 1, the authors compare their model, which has undergone both SFT and RL, with models that have only undergone SFT. This comparison is unfair because these SFT models could also be further enhanced with RL techniques to improve mathematical reasoning (e.g., using ORM for RL on DartMath). It would be more appropriate to isolate the effects of SFT and RL for a fair comparison. In Table 1, the authors should compare the performance of models that have undergone SFT with Math Evol-Instruct against existing baselines such as MetaMath and DartMath. Additionally, comparisons with baselines like MetaMath and DartMath on the LLaMA-3.2 backbone would be valuable, as their training data is publicly available.

- In analyzing the impact of training data size, the authors should compare their approach with the best method for SFT using synthesized data, specifically DartMath. MetaMath, which was developed around a year ago, uses GPT-3.5-turbo for data augmentation, making it an outdated and potentially unfair baseline.

- It appears that SFT with Math Evol-Instruct yields inferior results compared to other SFT methods. From Table 4, the LLaMA2-7B: WizardMath-SFT scores 35.6 on MATH, which lags behind models like XwinMath and Skywork. Likely, it would also lag behind LLaMA2-7B fine-tuned on the DartMath training data. This suggests that the main contribution of the paper is in the RL component. Therefore, the primary focus should be on the results obtained with different reward models, as presented in Table 4, utilizing various SFT backbones.

- Table 7 lacks adequate baselines; at least, the authors should include LLaMA-2-7B trained on the DartMath training set. This table also suffers from the same fairness issues as Table 1.

I recommend that the authors reorganize the paper better to emphasize their contributions to the "RL part."

### Questions
- In Equation (1), how is the parameter ( m ) set? Additionally, how is the Instruction Reward Model (IRM) trained?

- Lines 256-258 suggest that you retain solutions with incorrect answers. How might this influence the results? Have you considered using the IRM to filter out low-quality examples for supervised fine-tuning (SFT)?

- During PPO, do you use two reward models? Using two reward models in PPO can be time-consuming and computationally expensive. What are your strategies for addressing this?

- In Lines 89-90, you state that you "innovatively introduce PRM to address the False-Positive issue in the problem-solving process." This claim should be validated by comparing the false-positive rate on a test set both with and without your method.

- In Lines 88-89, you mention that existing methods "mainly focus on the SFT stage and are susceptible to learning hallucinated information from the teacher model." However, in Line 95, you still use GPT-4 to annotate step-level labels. Isn’t there a risk of obtaining incorrect step labels from GPT-4 as well?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a method to enhance math reasoning using Reinforced-Evol-Instruct, called WizardMath. The process begins with Supervised Fine-Tuning (SFT) on evol-instruct data, followed by training Instruction Reward Model (IRM) and Process Reward Model (PRM). Finally, they train PPO using the trained IRM and PRM. The WizardMath model achieves high performance on GMS8K and Math datasets.

### Strengths
The paper is well-written, with comprehensive analysis and ablation experiments. 

It represents a valuable exploration of process supervision and IRM in math reasoning, achieving impressive performance.

At the same time, their method is data efficient.

### Weaknesses
NA

### Questions
NA

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces WizardMath, an innovative approach to improving mathematical reasoning capabilities in large language models (LLMs). WizardMath employs a unique reinforcement learning method called Reinforcement Learning from Evol-Instruct Feedback (RLEIF), which optimizes the model’s performance on mathematical reasoning without external tools. It specifically targets pretrained model to enhance their reasoning by leveraging evolutionary instruction (Evol-Instruct) to generate diverse math problems and using process-based supervision to ensure correctness at each reasoning step. Experiments demonstrate that WizardMath achieves higher accuracy than other leading models, even outperforming proprietary models like GPT-3.5 and Claude on GSM8k and MATH benchmarks.

### Strengths
1. This paper provides a scalable approach to enhance LLM reasoning capabilities in math without external computational tools.
2. Notable improvements in metrics across diverse benchmarks.
3. The introduction of dual reward models (IRM and PRM) effectively improves model reliability and accuracy. 
4. The synthetic data and process supervision paradigm have had a great impact on the community.

### Weaknesses
 1. The training data for RLEIF is derived partly from a designated training set and synthetic from existing models, such as GPT-4. How might the reliance on specific LLMs for generating synthetic data (like GPT-4) affect the scalability of this approach for researchers without access to such models? Have the authors explored alternative methods for generating diverse mathematical problems that don't depend on proprietary models?
2. While RLEIF has undergone extensive evaluation in the context of mathematical reasoning, it may also hold potential for applications in other reasoning domains. Have the authors considered applying RLEIF to other reasoning tasks like logical deduction or causal inference? It would be valuable to see if the benefits observed in mathematical reasoning transfer to these domains, and what modifications might be necessary.

### Questions
see above

### Soundness
3

### Presentation
3

### Contribution
4
