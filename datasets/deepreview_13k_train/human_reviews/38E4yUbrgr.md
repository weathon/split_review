# Language Model Self-improvement by Reinforcement Learning Contemplation

- Decision: Accept
- Scores: 6, 8, 3, 8, 5

## Abstract
Large Language Models (LLMs) have exhibited remarkable performance across various natural language processing (NLP) tasks. However, fine-tuning these models often necessitates substantial supervision, which can be expensive and time-consuming to obtain. This paper introduces a novel unsupervised method called Language Model Self-Improvement by Reinforcement Learning Contemplation (\methodname) that improves LLMs without reliance on external labels. Our approach is grounded in the observation that it is simpler for language models to assess text quality than to generate text. Building on this insight, \methodname~assigns LLMs dual roles as both student and teacher. As a student, the LLM generates answers to unlabeled questions, while as a teacher, it evaluates the generated text and assigns scores accordingly. The model parameters are updated using reinforcement learning to maximize the evaluation score. We demonstrate that \methodname~can be applied to various NLP tasks, such as reasoning problems, text generation, and machine translation. Our experiments show that \methodname~effectively improves LLM performance without external supervision, resulting in a 5.6\% increase in answering accuracy for reasoning tasks and a rise in BERTScore from 0.82 to 0.86 for translation tasks. Furthermore, \methodname~can be applied to models of different sizes, showcasing its broad applicability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method for improving a language model using its own output. Specifically, the authors first show that there is an accuracy gap in the output of a language model between generation and evaluation, using Bigbench and summarization tasks. They then present a method for fine-tuning the language model using the evaluation output as the reward in reinforcement learning. The authors use Flan-T5 (780M) to demonstrate the effectiveness of their proposed approach.

### Strengths
- The fact that evaluation is sometimes easier than generation is well known, but the authors show concrete experimental results that support this in non-trivial settings.
- Overall, the paper is well written and easy to follow.

### Weaknesses
 - The novelty of the work is limited. The overall approach is very similar to RLAIF.
- The effectiveness of the proposed approach is demonstrated using the 780M model of Flan-T5, but it is not clear how effective it is when other or larger models are used. The paper does not explore the impact of different model architectures, specifically encoder-decoder versus decoder-only models, on the observed accuracy gap and the efficacy of the proposed method. This is a significant limitation given the prevalence of decoder-only models in recent language model research.

### Questions
- My understanding is that Flan-T5 is an encoder-decoder model, which may have helped to boost the accuracy of evaluation since the encoder transformer allows each token to attend to any other token in the input. I am wondering if the big accuracy gap between  generation and accuracy still exists in decoder-only models.
- Figure 2 suggests that the accuracy gap between generation and evaluation becomes smaller as the model size increases. Is the proposed approach still effective for larger models?
- Is it true that GPT-2 Large was used in Lee et al. (2023)?  It seems to me that they used PaLM 2.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an approach for language model self-improvement: given an LM, improve it using itself to provide feedback. This paper proposes a method called Reinforcement Learning Contemplation (RLC) to do this, based on the observation that LMs are better at providing feedback versus generating full examples. 

The three stage process is to 1. sample a bunch of QA pairs from the model (the questions come from a training dataset), 2. evaluate the QA pair from the model and transform it into a reward, and then 3. update the base LM accordingly. 

The paper evaluates this over CommonGen (lexically constrained text generation), 12 reasoning tasks from BigBench-Hard, along with CNN-daily mail summarization. The experiments show improvements over baselines like sampling once or N times, as well as self-training approaches without RL. Training on seed data from multiple tasks also shows some generalization to unseen tasks.

### Strengths
Overall, this paper seems reasonably solid to this reviewer. The approach proposed is simple and general, yet it also seems novel and underexplored at least to this reviewer. The results suggest that it helps on reasoning tasks which could suggest something interesting is happening during the RL process. It's good to see results on a variety of different model sizes too, which suggest also that the gain doesn't go away with scale (at least for e.g. the BigBench task "Penguins in a Table")

I have some concerns about evaluation below though I think/hope they can be answered in rebuttal --

### Weaknesses
The main concerns to this reviewer are:
* the datasets considered are a bit toy. It would be great to see other experiments from other domains (maybe something like math word problems?) or things considered by some of the other common papers in this space.
* The approach is limited to having a training dataset, though this is addressed appropriately in Appendix A.1 (at least to this reviewer, maybe extending this could be left for future work). However, I am a bit concerned that there might be stronger baselines that make use of that unlabeled training dataset.
* It's not clear to this reviewer what the model is learning here -- is it learning to truly reason or just to produce better answers (e.g. that mimic the format of the seed dataset)? It would be great to run more controlled experiments studying this. The main comparison that seems to address this is the "Self-train" baseline that generates high-confidence answers and then trains on them. It would be great to have a version of Figure 6 (performance of RLC across sizes of LMs) comparing with "Self-train" instead of with no finetuning.

### Questions
For the experiments, how do the non-PPO trained models generate answers / what happens if they generate an answer or assign high probability mass outside of the set of candidate options (e.g. for MultiChoice answering something that's not A/B/C/D/E?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a method for training language models without the need for external supervision or additional reward models. First, the language model is used for generation. Second, the language model is used to evaluate its own generated outputs. Third, the evaluation result is used to improve the generation. This approach results in some gains on BigBench tasks.

### Strengths
This work demonstrates empirical gains using self-improvement via evaluating self-generated outputs.

### Weaknesses
1. The approaches demonstrated in this work is not new, and the authors do not discuss prior work. For there is a family of work in evaluating self-generation (https://arxiv.org/abs/2210.03629), how is this work different?
2. This work uses CoT, do the baselines use CoT as well? How much of the gain is coming from CoT? This work is missing ablations that quantify the gains from the primary contribution.
3. The majority of this manuscript describe background information. The main contribution of this work starts on page 5. I suggest that the authors drastically truncate the background content and use the remaining room to analyze the primary contribution. First, how does it compare to prior work? What is generated during self-evaluation? Where do they agree/disagree with reference evaluation?

### Questions
What is the statistical significance of the gains in Tables 2 and 4? Several of the columns show what seems to be minor gains (e.g. for Table 2, all except Penguins in a Table). Are these gains within standard deviation?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce a self-improvement method for language models, i.e. a method that enables a language model to improve without any external supervision, as opposed to RLHF. It builds on the intuition that it is easier for language models to evaluate text than to generate it. In section 4, the authors confirm this intuition quantitatively on experiments from standard benchmarks and show that text evaluation can enable non-invasive improvement of language models by post-processing of text generations. 
They introduce a self-evaluating task-specific reward model (RLC) for “invasive” improvement of the LMs. Similarly to RLAIF (which asks the LM to rank generated text), it tailors a prompt for each task, possibly giving a denser reward signal to PPO: a strong case for RLC is it does not require learning a reward model. Empirical results on a large number of tasks show that RLC performs better than best-of-N, RLHF, plain RLAIF and other baselines to fine-tune small models.

### Strengths
- The paper is very well structured and well written. I particularly liked the structure and factorization of the appendix, as well as the experiments from Section 4 that confirms the intuition that LMs are better at evaluation (as humans)
- Showing that the internal reward / ranking capabilities of LMs are correlated with heuristics metrics (BLEU, BERTScore, ROUGE).
- Experiments are well-executed and done on a variety of standard tasks.

### Weaknesses
 **Weaknesses**
- Section 4.3 looks a bit weak to me (greedy and 3 samples) to evaluate the accuracy of best-of-N with the best evaluated text versus accuracy of average of LM samples. Furthermore, greedy is evaluated against 1 or 2 samples)
- Why doing only 3 samples (this experiment does not require any fine-tuning and is done on a small LM whose identity is unknown).
- The method is simple and not novel: it relies on two “template” reward prompts (defined section 5) and good parsing of LM’s output (as opposed to RLAIF that learns a reward model). This is not a problem to me as long as experiments are done rigorously.

**Additional experiments  (could make me increase a bit my score)**
- Could you plot the evaluation of the LM when fine-tuning from RLC (for instance on the Figure 7 from appendix), as well as the heuristic metrics (BLEU, BERTScore, ROUGE) when applicable?
- Would appreciate a discussion (backed by experiments) on the RLC/RLAIF updates compared to doing more sampling and non-invasive self-evaluation.

### Questions
- It is not clear to me how accuracy is computed in experiments of section 4.1.
- What is the difference between best-of-N and w/ SE in section 4.3?
- Do you have an intuition why preference-based RLAIF is weaker than RLC? Better “reward” prompts in RLC as opposed to the use preferences in RLAIF? Having to explicitly learn a reward model?
- In Table 4, any idea why RLFT is stronger than RLC on “Reasoning about Colored Objects”?
- It is often not really clear what model is used (4.2, 4.3, 6) and why results are not reported for different model sizes (as claimed in the abstract)

 
Minor nitpicks:
- Define Self-Evaluation (SE) in 4.3
- Define Self-consistency (SC) before self-train as SC is mentioned before definition.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a method Reinforcement Learning Contemplation (RLC) as an alternative to existing RLAIF workflows. Rather than training a preference model + doing PPO using the preference model, they just directly prompt the original model for reward signal, following analysis indicating that evaluation is easier than generation. They evaluate on a number of natural language reasoning tasks and outperform their baselines.

### Strengths
--Comprehensive results on several reasoning tasks, with interesting analyses.

--Interesting to see that it seems to work reasonably at small model scales, unlike the original Anthropic RLAIF paper

--The new pipeline is a bit simpler than RLAIF, not needing to train a preference model as an intermediate step, while still working well

### Weaknesses
--I'm not sure that the idea of evaluation being easier than generation is particularly new; you could view this as the intuition for RLAIF too, where you get the model to evaluate itself and then use the preference model to improve its generations later using PPO. I'm not sure it's the right motivation for your work anyway; if I understood correctly, the main difference between your method and RLAIF is that you *evaluate the absolute quality of only one output* at a time (either binary or 1-10), rather than *evaluating the relative quality of two outputs*. Then naturally you don't bother fitting a preference model since you already have the reward due to predicting absolute quality rather than relative quality.

--On a related note, these tasks seem a bit nonstandard for RLAIF evaluation, are there other works using these too? I'm curious whether the results hold up when you do the classic tasks like harmlessness and helpfulness. In particular, if I understand correctly, one major difference is that the tasks you evaluate seem to have a "gold" "correct" answer, unlike e.g. harmlessness and helpfulness, which makes it reasonable for your model to label the absolute quality of a given output rather than comparing relative quality between two outputs.

--Do the RLAIF and other baselines also get to use chain of thought for the reasoning tasks, like your method? 

--I saw you mentioned in the appendix that you use GPT2-Large for the reward model for RLAIF, rather than the same Flan-T5 model you use for the main model. Is it fair to use Flan-T5 to evaluate outputs for your model, while using finetuned GPT2-Large (presumably weaker) to compare outputs for your baseline?

--What are the prompts used for RLAIF / other baselines?

--Using language models to directly output 1-10 scores seems like it might suffer from poor calibration - why not e.g., try to finetune with a regression head on top rather than just using the LM out of the box? Would that improve performance?

--The numbers in 6.4 don't seem very convincing for what you're claiming, if anything it seems like the performance went up more on the unrelated tasks (object counting, penguins)?

--Nit: I don't really see why you distinguish between RLCAI and RLAIF; from what I can tell you basically mean the same approach for both terms? (And the paper you cite for RLAIF attributes the term RLAIF to the original Anthropic paper anyway.)

### Questions
--Do the RLAIF and other baselines also get to use chain of thought for the reasoning tasks, like your method? 

--I saw you mentioned in the appendix that you use GPT2-Large for the reward model for RLAIF, rather than the same Flan-T5 model you use for the main model. Is it fair to use Flan-T5 to evaluate outputs for your model, while using finetuned GPT2-Large (presumably weaker) to compare outputs for your baseline?

--What are the prompts used for RLAIF / other baselines?

--Using language models to directly output 1-10 scores seems like it might suffer from poor calibration - why not e.g., try to finetune with a regression head on top rather than just using the LM out of the box? Would that improve performance?

--The numbers in 6.4 don't seem very convincing for what you're claiming, if anything it seems like the performance went up more on the unrelated tasks (object counting, penguins)?

--Nit: I don't really see why you distinguish between RLCAI and RLAIF; from what I can tell you basically mean the same approach for both terms? (And the paper you cite for RLAIF attributes the term RLAIF to the original Anthropic paper anyway.)

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
