# Chain of Hindsight aligns Language Models with Feedback

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Learning from human preferences is important for language models to match human needs and to align with human and social values. 
Prior works have achieved remarkable successes by learning from human feedback to understand and follow instructions.
Nonetheless, these methods are either founded on hand-picked model generations that are favored by human annotators, rendering them inefficient in terms of data utilization and challenging to apply in general, or they depend on reinforcement learning, which often suffers from imperfect reward functions and relies on extremely challenging optimizations.
In this work, we propose a novel technique, Chain of Hindsight, that is easy to optimize and can learn from any form of feedback, regardless of its polarity.
Our idea is inspired by how humans learn from extensive feedback presented in the form of languages. We convert all types of feedback into sequences of sentences, which are then used to fine-tune the model, allowing us to take advantage of the language comprehension capabilities of language models.
We condition the model on a sequence of model generations paired with feedback.
By doing so, the model is trained to generate outputs based on feedback, while learning to identify and correct negative attributes or errors. 
Applying our method to large language models, we observed that Chain of Hindsight significantly surpasses previous methods in aligning language models with human preferences. We report significant improvements on summarization and dialogue benchmarks, with our approach markedly preferred in human evaluations

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel technique called Chain of Hindsight (CoH) that aims to align language models with human preferences and values by leveraging human feedback. The authors convert all types of feedback into sequences of sentences, which are then used to fine-tune the language model. By conditioning the model on a sequence of model generations paired with feedback, the model is trained to generate outputs based on feedback while learning to identify and correct negative attributes or errors. The authors evaluate the proposed approach on summarization and dialogue tasks and report significant improvements over existing baselines in both automatic and human evaluation.

### Strengths
(1) The paper presents a novel technique, Chain of Hindsight (CoH), which addresses the challenge of aligning language models with human preferences and values by leveraging human feedback.

(2) The approach is easy to optimize and can learn from any form of feedback, regardless of its polarity.

(3) The paper provides a well-structured review of relevant literature, including prior works on learning from human feedback and language modeling.

### Weaknesses
This is a good paper. I see no reasons to reject it. Only a few comments:
1) I am confused by the illustrated examples. In the Figure 1, the prompt template uses 'a helpful answer' / 'an unhelpful answer' while in the Section 1, they are using 'Good' / 'Bad'. It would be better to be consistent.

2) Some important studies [1,2] are missing. It would be better to include them and  have a discussion.

[1] RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment

[2] Direct Preference Optimization: Your Language Model is Secretly a Reward Model

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces "Chain of Hindsight", a novel technique for fine-tuning language models using any form of feedback, regardless of its polarity. This method is designed to overcome the inefficiencies and challenges of previous approaches that either rely on handpicked, positively-rated model generations or reinforcement learning (RL) with its imperfect reward functions and optimization challenges. CoH is inspired by how humans learn from extensive feedback in languages and aims to align language models more closely with human preferences and values. CoH converts all types of feedback into sequences of sentences, which are then used to fine-tune the model. This approach leverages the language comprehension capabilities of language models, training them to generate outputs based on feedback while learning to identify and correct negative attributes or errors. The method involves conditioning the model on a sequence of model generations paired with feedback, thus enabling learning from both positive and negative feedback.

### Strengths
1. The Chain of Hindsight (CoH) method is a novel approach, addressing the limitations of previous methods like supervised fine-tuning  and Reinforcement Learning with Human Feedback. It's innovative in using both positive and negative feedback for model training.
2. Simplicity and Scalability: The CoH method maintains the same training objective as pretraining, which simplifies the training process and enhances scalability. This is a significant advantage over more complex systems like RLHF. The paper reports significant improvements in tasks like summarization and dialogue generation, indicating that CoH effectively enhances model performance and alignment with human preferences.

### Weaknesses
1. Limited Scope of Testing: The paper only considers two evaluation benchmarks such as dialogue and summarization benchmarks. It is not clear how the model performs on the standard academic benchmark. Broader testing across diverse datasets and real-world scenarios would be necessary to fully validate the approach. Specifically, the lack of evaluation on established NLP benchmarks, such as GLUE or SuperGLUE, makes it difficult to assess the generalizability of the proposed method. The paper would benefit from including results on tasks that are more standardized and widely used in the NLP community, allowing for a more direct comparison with existing methods. Furthermore, the paper does not explore the performance of the model on tasks that require more complex reasoning or factual knowledge, which are important aspects of language understanding.


### Questions
1. How is the method compared with the other baseline such as rejection sampling?

### Soundness
4 excellent

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents Chain of Hindsight (CoH), a technique to align LMs by converting pairwise preference data into natural langauge sequences. The proposed method involves: (1) converting preference data (context, response-good, response-bad) from different sources into natural language sequences (e.g., you are a helpful assistant. good: {good response}, bad: {bad response}), (2) training an LLM via SFT with a mask on the non-response tokens, (3) prompting the model at inference time with just 'Good:'. The intuition is that expressing natural language feedback (and examples of bad/good responses), will allow the model to learn a better notion of response quality.

Training is conducted on three datasets: WebGPT, Anthropic-hh, Summarization. Automatic evaluation is conducted on both summarization (rouge on tldr dataset) and helpful dialog (by using LM as preference model on Anthropic-hh dataset). Human evaluation is conducted for both summarization (accuracy, coherence, coverage) and helpful dialog (helpful, harmless). Across all evaluations, CoH is shown to outperform several strong baselines, including: SFT, conditional SFT (grounded on 'good'/'bad'), SFT with unlikelihood on bad responses, RLHF.

The paper also presents analysis of (1) the effect of model size (0.5B - 6B), showing that CoH scales well and (2) the impact of natural language templates (vs just having good/bad responses) demonstrating that the natural language feedback helps but that 'CoH w/o lang' strongly outperforms RLHF.

### Strengths
- CoH is well-motivated, interesting, novel, and performs well. The training methodology is simple, yields strong benefits and is easily extendible.
- The experiments are thorough, several datasets/settings are explored, there are strong baselines, and human evaluation is conducted. 
- The analyses (e.g., w/o lang ablation, scaling) are meaningful, sound, and an impactful contribution.

### Weaknesses
1. More details needed about RLHF. At present, it's unclear why CoH outperforms RLHF. Is the trained RM ineffective at modeling preference (add RM performance to Fig3)? Or is the learning algorithm unable to leverage the RM effectively (could it be the choice of prompts used for RLHF?), in which case an alternate RM-based baseline could be considered (e.g. rejection sampling, reinforced self-training)? It would be helpful to understand the specific limitations of the RLHF implementation, such as the reward model's performance and the optimization process, to better contextualize CoH's advantages. For example, what is the correlation between the reward model's predictions and human preferences, and how does this affect the RLHF training? A more detailed analysis of the RLHF training process, including the specific hyperparameters used and their impact on performance, would be beneficial.

2. Why do you only prompt with 'Good:' at inference time? It seems that an advantage of the different natural language feedback templates is that the CoH-trained LM will (hopefully) learn to *consider an initially generated bad response, and leverage it to produce a good response*. Perhaps leveraging this capability, and giving the LM an attempt to produce a better response, may yield further benefits. Some discussion or analysis about the potential of different natural language feedback templates at inference time would be useful. Specifically, it would be interesting to see if prompting with both 'Bad:' and 'Good:' or using iterative refinement prompts could further improve the quality of the generated responses. For instance, could the model be prompted to first generate a 'Bad:' response and then refine it into a 'Good:' response, thereby explicitly leveraging the contrastive learning inherent in the training data?

3. More discussion is warranted about the performance relative to C-SFT. If my understanding is correct that C-SFT is essentially training with ("good: {good response}", "bad: {bad response}"), then I wonder if CoH with only ("good: {good response} bad: {bad response}", "bad: {bad response} good: {good response}") is expected to perform better (under the current inference setup)? If yes, why is this the case? If not, where is the advantage of CoH relative to C-SFT coming from? It would be helpful to clarify whether the performance difference between CoH and C-SFT is primarily due to the joint conditioning on both good and bad responses during training, or if other factors are at play. A more detailed analysis of the training dynamics and the model's internal representations would be beneficial to understand the source of CoH's advantage.

### Questions
1. I'm not certain I understood this properly: Does 'CoH w/o lang' mean that the template will always be something like "Good: {good} Bad {bad}"? The text mentions "fine-grained language feedback" and it's not whether this is referring to the feedback templates or something else.

2. Do you have insights on how this method would scale from pairwise comparisons to N-way rankings? I thought that WebGPT had >2 responses per prompt (but might be mistaken) -- if so, it would be great to understand how this was handled.

3. Is the loss masking during CoH training really important? I would not have expected it to make a substantial difference. 

*See additional questions in weakness section*

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes to learn the human preference for a LLM by training the LLM on sequences that consist of both positive and negative responses with human feedback. The results show that this method can even outperform the PPO method.

### Strengths
1. This paper is well-written and easy to read.
2. The proposed method is important, which can help align the fine-tuned LLM better with human preference. The presented experimental results on both summarization and dialogue tasks can validate the effectiveness of the proposed method.
3. The presented method is novel.

### Weaknesses
1. The largest model tested is GPT-J, which is a 6B model. It would be great that larger and more latest LLMs can be also tried, such as LLAMA-2.
2. In page 4 for the "Training" section, it is mentioned that "the model can simply ‘copy’ the example without learning to understand the underlying task". To circumvent this, this work proposes to "randomly mask between 0% and 5% of past tokens during training". What do the "past tokens" refer to? How is this masking ratio determined? Have you done some tuning on this hyper-parameter? 
3. For the above point 2, this work proposes to "added a regularization term which maximize the log likelihood of the pretraining dataset". Could you specify how much pretraining data you need to use for such regularization? What is the added overhead to the training process?
4. For the dialogue task, it would be great that besides the human evaluation, another automatic evaluation based on GPT-4 can be also provided. This work was first out in this Feb or Mar., at that time, we have tried replicating this method using GPT-J and Anthropic-HHH dataset and this provided code base by the authors. We have used the same setting except that we were not using the regularization term, but we have found that the resulted model tends to generate long responses with weird grammar and repetitions. That is, the generation quality is pretty poor.  
5. During inference, could you control the model to just generate the good response or the model would generate both good and bad responses and extra post-processing is needed? I doubt the case is the latter one based on my intuition and our replication experiments, which would make the inference latency double compared with other RLHF methods.

### Questions
1. Could you provide some qualitative examples for the model inference outputs?
2. Could you help provide the review feedback from ICML 2023 and your revision based on the reviews?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
