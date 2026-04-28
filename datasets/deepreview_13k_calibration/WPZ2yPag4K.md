# Fine-Tuning Language Models for Factuality

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
The fluency and creativity of large pre-trained language models (LLMs) have led to their widespread use, sometimes even as a replacement for traditional search engines. Yet language models are prone to making convincing but factually inaccurate claims, often referred to as `hallucinations.' These errors can inadvertently spread misinformation or harmfully perpetuate misconceptions. 
Further, manual fact-checking of model responses is a time-consuming process, making human factuality labels expensive to acquire. 
In this work, we fine-tune language models to be more factual, without human labeling and targeting more open-ended generation settings than past work. We leverage two key recent innovations in NLP to do so. First, several recent works have proposed methods for judging the factuality of open-ended text by measuring consistency with an external knowledge base or simply a large model's confidence scores. Second, the direct preference optimization algorithm enables straightforward fine-tuning of language models on objectives other than supervised imitation, using a preference ranking over possible model responses. We show that learning from automatically generated factuality preference rankings, generated either through existing retrieval systems or our novel retrieval-free approach, significantly improves the factuality (percent of generated claims that are correct) of Llama-2 on held-out topics compared with RLHF or decoding strategies targeted at factuality. At 7B scale, \textbf{compared to Llama-2-chat, we observe 58\% and 40\% reduction in factual error rate} when generating biographies and answering medical questions, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors construct a direct preference optimization (DPO) dataset for improving factuality using reference-based and reference-free truthfulness annotation techniques. Through the proposed method, they improve accuracy in two tasks (Biographies and Medical QA) without human factuality labels. The authors demonstrate that the proposed method (DPO-FS and DPO-MC) can be applied to Llama-2 and Llama2-Chat, and combined with a factuality-decoding approach (e.g., DOLA).

### Strengths
- Motivation is intuitive and easy to understand
- The proposed method improves the truthfulness of LLM without human factuality labels
- The proposed method can be augmented with existing orthogonal approaches for factuality

### Weaknesses
 - Because the framework is simple and the method of scoring truthfulness and fine-tuning technique uses existing approaches, the proposed method appears to have limited contributions

### Questions
In Biographies and Medical QA tasks, are DPO-FS, DPO-MC, and SFT fine-tuned on the training set of each dataset?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors propose to finetune Llama models for factuality in long-form generation tasks using DPO on automatically constructed preference pairs. Authors explore 2 methods for generating preference ratings: 1) Reference-based: Extracts atomic facts using GPT-3.5 and then use Lama-1-7B-based NLI model to determine correctness of each atomic fact with respect to the reference. Percentage of correct atomic facts is used to compare the factual correctness of samples. 2) Reference-free: Extracts facts using GPT-3.5, then use GPT-3.5 to convert a fact to a question (uses few-shot prompting). Then, through sampling answers multiple times from the model, they estimate the model's uncertainty for the actual answer. The model's uncertainty is used to compare the factual correctness of samples.

They evaluate their approach on two tasks: biography generation and open-ended medical QA. To accommodate for the reference-based metrics, they generate data based on individuals (for biographies) and medical conditions that have Wikipedia pages.

Results show superior factual accuracy for DPO-based models on both tasks.

### Strengths
- New results to show the benefit of using automated feedback for improving LLMs, targeting factuality for long-form open-ended generation.

- Paper is well-written, experimental settings are well-defined, human evaluation is performed.

- Paper also shows that DPO-finetuning is complementary to decoding-time factuality improvement method (DOLA), (DPO + DOLA outperforms DPO)

### Weaknesses
 - Idea itself is not novel, RLAIF has been consistently shown to be useful (here, authors used DPO instead of PPO). Though the application is new.

- Including more fine-tuning based baselines can help understand the role of automated metrics. E.g., directly using prompts to compare factuality of two outputs w.r.t. the wikipedia article instead of extracting atomic facts. 

- Both DPO variants reduce number of correct facts on biography generation. This does not seem very surprising, given the optimized metric is the percentage of correct atomic facts. For example, a sample with 10 correct and 5 incorrect is preferred over 11 correct and 6 incorrect. Can this bias be removed from the fine-tuned model, maybe by changing the metric or comparing samples of similar lengths? Or is it the bias of evaluation metric?

### Questions
Check questions in the Weakness section.

- Between reference-free and reference-based metrics, there is a significant difference in the total number (correct + incorrect) of generated facts (almost 30% fewer) on biographies. What's the source of this bias, any possible explanations?

- Could you provide statistics on the number of tokens in wining vs losing samples in all cases (dataset/model/metric)?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes fine-tuning language models to improve their factuality. Specifically, one reference-based and one reference-free method are explored to estimate the truthfulness of different model responses, the scoring/preference of which are then used to fine-tune the LMs with direct preference optimization.

### Strengths
- The paper writing is of high quality and easy to follow

- The proposed method, regardless of reference-based or reference-free, shows improved factuality than the SFT baseline and the highest correct% among the compared methods.

- The paper provides analysis and ablations of different variants such as fine-tuning the pretrained/chat models and combining with inference-time decoding method.

### Weaknesses
 - [major] I have some concerns about the evaluation
  - The test sets (50 and 59 examples in each domain, respectively) look very limited, making it bit hard to understand the actual improvement of model factuality.  How reliable are the results? Is 75% -> 81% a lot? I can't really answer these questions after reading the paper.
  - I noticed that the total number of claims are often different for different methods. Could generation style (e.g., length) contribute to the seemingly better/worse results? I wonder if the authors have considered such factors.
  - There is also no evidence indicting the improved factuality doesn't come at the expense of performance in other aspects. I understand the authors may not have enough labor/compute for a more comprehensive eval like GPT or Llama but LLMs, in my experience, can behave in mysterious ways when you over index on one specific objective.

- [minor] The method is somewhat straightforward, which is not necessarily a bad thing if the evaluation can show meaningful improvements (that are worth fine-tuning specifically for factuality) than methods that modify decoding only.

### Questions
- I'm a little confused why choosing the largest bin to measure truthfulness in the reference-free setting. Does that mean the atomic claim doesn't really matter ("Yo-Yo Ma was born in 1951" and "Yo-Yo Ma was born in 1955" would both be converted to "What year was Yo-Yo Ma born")? So as long as two responses make a claim on the same fact, regardless if it's correct or wrong, they will receive the same truthfulness score? If the hypothesis is "a language model’s confidence in a generated answer is highly correlated with the probability that the answer is correct", why not use the distribution to cross-check like in the reference-based setting?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies approaches to improve the factuality of language models (LMs) by fine-tuning the LMs using reinforcement learning (the specific algorithm is DPO), and the two main types of the reward function are: 1) reference-based FactScore (referred to as “DPO-FS”) and 2) reference-free uncertainty measure based on self samples (referred to as “DPO-MC”). 

The authors conduct the experiments on two tasks: 1) free-form generation of biographies and 2) medical question answering. The datasets were crafted specifically for their experiments, hence resulting in the small size (e.g., biography train/test = 296/59 and medical QA train/test = 150/50 instances). The base LM is Llama1 and Llama2. The main experimental results show that both DPO-FS and DPO-MC generate responses with a higher “correct” percentage than baselines (SFT and inference-time methods such as ITI and DOLA). Also, DPO-FS and DPO-MC achieve a higher correct percentage than Llama-2-chat. Lastly, the authors perform a human evaluation to validate the findings previously evaluated using GPT3.5.

### Strengths
The paper shows that DPO can be applied to improve the factuality of LMs as shown by DPO-FS and DPO-MC achieving better factuality, and to the best of my knowledge, the factuality-based reward has not been investigated yet. The paper also investigates both reference-free and reference-based, and shows the effectiveness of both methods.

### Weaknesses
1. Although existing work may have not used a factuality-based reward, the results in this paper are mostly the expected observations (e.g., applying RL-based training improves target rewards). For example, (Lu et al., 2022) applied RL (PPO) with a reward based on an external metric to improve toxicity, repetition, etc.

2. The main findings (Tables 2, 3, 4, 5) are all based on GPT3.5 evaluation, and coupled with the fact that the test sets are small (e.g., 59 instances for biographies & 50 instances for medical QA), I’m not certain how reliable the results are. Also, there is not much information in Section 5.5 about human evaluation, e.g., inter-annotator agreement, or how many annotators were employed.

3. How does the DPO fine-tuned model perform on out-of-domain tasks? For example, when fine-tuning to improve factuality on biographies, does it also improve factuality on medical QA? And does its general performance change?
There is also a recent survey paper (Pan et al., 2023) about aligning LLMs for different aspects (including hallucination/factuality), and I think it would be useful for authors to incorporate additional relevant papers (i.e., those that apply RL to improve LMs) 

4. Weak base LM: This work uses Llama-7B as the base model, and at this size, the model may not yet be highly capable of long-form generation / medical QA. Previous works such as (Manakul et al., 2023) and (Mundler et al., 2023) investigated LLM hallucination with much larger LLMs (e.g., GPT3.5/4). It would be interesting to see, for example, when using larger models (either open-source such as larger Llama / Falcon-180B or private ones such as GPT-4), if the model still makes as many factual errors (because if they don’t – due to the emergent ability when scaling up – fine-tuning may not be necessary or have little impact).

There is a recent survey paper (Pan et al., 2023) about aligning LLMs for different aspects (including hallucination/factuality), and I think it would be useful for authors to incorporate additional relevant papers (i.e., those that apply RL to improve LMs) 

### Questions
My questions are related to the points in the weaknesses section. I'm looking forward to seeing your responses to the weaknesses above, especially point number 3.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
