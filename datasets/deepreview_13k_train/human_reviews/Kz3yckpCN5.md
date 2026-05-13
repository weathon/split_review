# The False Promise of Imitating Proprietary Language Models

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
An emerging method to cheaply improve a weaker language model is to finetune it on outputs from a stronger model, such as a proprietary system like ChatGPT (e.g., Alpaca, Self-Instruct, and others). In this work, we critically analyze this approach of imitating language models. We first finetune a series of LMs that imitate ChatGPT using varying base model sizes (1.5B--13B), data sources, and imitation data amounts (0.3M--150M tokens). We then evaluate the models using crowd raters and canonical NLP benchmarks. Initially, we were surprised by the output quality of our imitation models---they appear far better at following instructions, and crowd workers rate their outputs as competitive with ChatGPT. However, when conducting more targeted automatic evaluations, we find that imitation models close little to none of the gap from the base LM to ChatGPT on tasks that are not heavily supported in the imitation data. We show that these performance discrepancies may slip past human raters because imitation models are adept at mimicking ChatGPT’s style but not its factuality. Overall, we conclude that while model imitation can be useful for training models to follow instructions and avoid toxic outputs, it falls short its full promise in many ways. In particular, there exists a substantial capabilities gap between open and closed LMs that we find cannot be bridged merely by adding more imitation data. Instead, we find that fine-tuning more capable base LMs has a significantly more substantial effect on closing this gap. In turn, we argue that the higher leverage action for improving open-source models is to tackle the difficult challenge of developing better base LMs, rather than taking the shortcut of imitating proprietary systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors investigate the question of acheiving performance parity with high-quality proprietary systems by training (smaller, generally lower quality models) on the outputs of the proprietary systems. The investigation is carried out over a range of data sizes collected from proprietary systems, or imitation data, and a range of model sizes. The authors' conclude that while training on some imitation data can improve the style of weaker models, there (i) is still a large performance gap to the proprietary models especially in evaluations of general capabilities, (ii) diminishing returns from increasing imitation data, (iii) greater gains (than collecting imitation data) by simply increasing the model size.

### Strengths
The main strengths of this work:
- The question studied is important as most open-source models make use of imitation data for supervised finetuning.
- The investigation along the data and model size axes is well thought out.

### Weaknesses
The main weaknesses of this work:
- The implicit assumption of this work (revealed in the title) is that there exists a claim or understanding that imitating proprietary language models by sampling their outputs for training is all that is needed to achieve performance parity - however, I contend that this isn't the prevalent understanding. It is understood that proprietary model output is a good source of finetuning data but not necessarily the only source. See for example the use of FLAN alongside imitation datasets like Alpaca for SFT.
- The authors present style imitation of propreitary models as a negative aspect of training on imitation data (at least in the abstract), however the right amount of style imitation can be a definite source of improvement for open-source models - as the authors point out in Section 4.4. My suggestion would be to revise the abstract to reflect this more accurately.
- The paper does not sufficiently explore the nuances of imitation data quality. While the authors vary the *amount* of imitation data, they do not investigate the impact of different sampling strategies or the diversity of the imitation data itself. For example, are the imitation datasets generated using a temperature of 1.0, or is a lower temperature used to sample more deterministic outputs? This could have a significant impact on the results, and is not discussed.
- The paper lacks a detailed analysis of the computational costs associated with training on imitation data versus training larger models. The authors conclude that scaling model size is more effective, but a discussion of the computational trade-offs would be valuable. For example, is it more computationally efficient to train a smaller model on a large imitation dataset or to train a larger model on a smaller dataset?

### Questions
In Figure 4. the 5-shot MMLU performance of the 13B imitiation model is quite low for a model of that size - can the authors describe the setup in more detail?

Some discussion of the points raised in "weaknesses" would also be welcome.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper critically analyzes the method of using the output of a stronger LM to fine-tune and improve a weaker LM, pointing out that model imitation is not a free lunch.
The authors concluded that broadly matching ChatGPT using purely imitation would require (1) a concerted effort to collect enormous imitation datasets and (2) far more diverse and higher quality imitation data than is currently available.

### Strengths
1. Using the output of GPT-4 to cheaply improve a weaker language model by fine-tuning is widely adopted. This paper analyzes the drawbacks of doing so, which is helpful to guide the direction of developing more powerful LLMs.

2. A large number of experiments and analyses prove the author's point of view.

### Weaknesses
1. The author claimed that it is far more feasible to distill a specific behavior from ChatGPT as opposed to broadly matching its capabilities. However, the paper only conducted experiments on NQ-synthetic data.

2. The paper claimed that imitation models are adept at mimicking ChatGPT's style but not its factuality and become far better at following instructions. But the other important ability of the model, that is, the ability to reason, has not been well studied.

### Questions
Is model imitation still a good solution if the model's factual performance is decoupled to the retrieval model?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper critically analyzes the approach of imitating proprietary systems (e.g., ChatGPT) by finetuning LMs using various model sizes, data sources, and imitation dataset sizes. Then the authors do human evaluation as well as evaluation on NLP benchmarks. Imitation models do not do well on tasks not heavily supported by the imitation data.

One interesting finding is that training on broad-coverage imitation data may decrease Natural Questions factuality, but training on NQ-like-data only will increase the accuracy. 

The authors also conclude that the best action forward is to improve base LMs, instead of doing imitation on proprietary systems.

### Strengths
I vaguely heard of this paper when it came out but it’s my first time reading it. The motivation is excellent for sure (the public will care about this paper), given that many groups and startups are imitating proprietary language models potentially as a shortcut. 

The findings are useful to many practitioners -- they'll likely carefully think whether knowledge distillation is useful or how it'll be useful. 

Some findings are quite interesting (see summary above for example).

### Weaknesses
I have three concerns related to crowdsourcing (see the next three paragraphs).

Do human raters have low quality? The incentive design and crowdworker filtering seem lacking.  
- What’s the human agreement (e.g., Fleiss' kappa)?
- What’s the average time humans spend on each comparison?
- Is there an option for humans to decline the comparison (because they may not be knowledgeable enough)? 
- How do you make sure that humans are rewarded based on correct choices, and potentially punished if they do extremely poorly?

It’d be useful to have human evaluators write out rationales on why they chose one over another (or rate on multiple scales using multiple metrics). Otherwise concluding “human evaluators rate imitation models’ outputs higher because of their style” seems only a conjecture to me. 

If crowdworkers have low quality (thus their annotations unreliable), then it doesn't seem prudent to use Figure 1(c) (crowdworker preference vs. number of model parameters) to reach the conclusion that we should improve base LLMs. 


I also have some other concerns: 

There are two settings for imitation in the paper. The second setting is broad-coverage imitation. The imitation dataset size could be much larger. Currently the authors are using around (90+27+10)K examples, but this is quite a small number of examples – the dataset size is even smaller than most of the machine translation training sets from ten years ago.  

The results in this paper are only specific to supervised fine-tuning, not RLHF for example. This should be qualified in the intro paragraph. 

The authors claim that matching ChatGPT using imitation would require an “enormous” amount of imitation examples. Is this supported anywhere in the paper?

### Questions
Important: What are the decoding parameters for each model? (This is not addressed post-rebuttal.)


Below are minor (or very minor issues) in evaluating this paper:

I wonder if practitioners may interleave ChatGPT imitation data with actual pretraining data and fine-tuning data. It’s unclear if this setting would lead to the same problems. 

The base models discussed in this paper are quite weak. For example, llama-1-13b is used instead of the SFT- and RLHF-tuned llama-2-13b-chat. The models are quite small too. Unclear if the results generalize to larger models.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors critically investigate the promise of finetuning language models using (imitation) data obtained from more capable language models(LMs). The paper challenges the assumption that this process improves an LM overall – but suggests that this is rather `mimicking their style`. They propose several interesting findings around what aspects of the performance improve or deteriorate upon tuning LMs on imitation data.

### Strengths
I overall support the messages and findings in the paper.

1. I appreciate this timely and critical investigation. Finetuning existing LMs on instruction-tuning data from more capable LMs has swiftly become common practice, yet we do not fully understand the change in behavior. The paper raises several critical questions that I would personally appreciate having in the literature.

2. One novel and important finding is that the authors find that even though training on imitation data improves the results in crowd worker evaluations, they observe even a degradation in factuality. This is a significant consideration that should be kept in mind when finetuning models. This further raises a question about what other aspects of capabilities may be fluctuating during imitation data training.

3. On the other hand, they inherit some of the useful properties, such as reduced toxicity / being more safe. Again, this further informs us about what really happens when models are trained on imitation data. It would be compelling to further explore a more fine-grained decomposition of performance gains and losses upon training on imitation data.

4. The experiments are large-scale and informative yet not cheap to perform, thus findings enable valuable conclusions that are otherwise not easy to draw.

### Weaknesses
There are 2 main points that I am concerned about.

1. (IRB Approval / Exemption) The human study in the paper does not seem to have the relevant IRB approval or an exemption. The code of ethics states `Where human subjects are involved in the research process (e.g., in direct experiments, or as annotators), the need for ethical approvals from an appropriate ethical review board should be assessed and reported.` I am deferring the judgment about this to Ethics Reviewers / ACs. This should have most probably been done before the human subject study, but I encourage the authors to swiftly go through the IRB process for clarity.

2. (Definition of Capability) The coverage of the capability evaluations is somewhat limited. Currently, authors evaluate mostly on factuality tests like MMLU/NQ/HumanEval and also show results around toxicity but how about other capabilities? Could it be that the imitation data leads LMs to reason better? Or, could it be that imitation data drives better calibration? While I do understand that there is a finite compute budget and there should be a limit in evaluation, the capability definition here is rather to limit the conclusions to draw. 

3. (Minor, Title) Given my concern in 2, I’m personally slightly skeptical to call this a `false promise`. It is unclear if it is broadly a false promise, or if there are capabilities that are improved – it’s rather there exists capabilities that this process even hurts, and we should be mindful about trusting crowdsourcing or other automated evaluations to understand the impact of a process.

### Questions
1. The discussion seems to rely heavily on the concept of `tuning of imitation data`. However, I think one distinction is the kind of imitation data used to finetune most of the models, which are usually based on roughly arbitrary conversations between users and models. Would the authors agree that if the imitation data is constructed in a different way, then it may be possible to improve e.g. factuality of the finetuned model? For instance, I can imagine the way to construct imitation data to be around extracting rare knowledge, and then possibly the finetuned model could be improved a lot.

2. Have the authors explored other capability definitions than factuality and toxicity? For instance, do we know anything about reasoning, calibration, creativity, truthfulness.. ? 

3. Did the authors get the necessary approvals from the IRB of their institution?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
