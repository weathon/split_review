# Zero-Shot Continuous Prompt Transfer: Generalizing Task Semantics Across Language Models

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Prompt tuning in natural language processing (NLP) has become an increasingly popular method for adapting large language models to specific tasks. However, the transferability of these prompts, especially continuous prompts, between different models remains a challenge. In this work, we propose a zero-shot continuous prompt transfer method, where source prompts are encoded into a relative space and the corresponding target prompts are searched for transferring to target models. Experimental results confirm the effectiveness of our method, showing that ``task semantics'' in continuous prompts can be generalized across various language models. Moreover, we find that combining ``task semantics'' from multiple source models can further enhance the performance of transfer

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new route to Prompt-Tuning problems. Besides human-writing prompts and doing gradient back-propagation to learn continuous prompt, it brings the possibility of transferring an existing corpus of prompts for different models, regardless of the size of their embedding space. 

The idea of the paper involves first translate one model's continuous prompt into a shared high-dimensional space, and search in that space for the target continuous prompt. The experiment shows that prompts are more or less transferable between BERT, RoBERTA, ALBERT, especially if you use dual source prompt transfer.

### Strengths
As said by the paper, novelty is a big strength. It's quite unthinkable to transfer learned continuous prompt of one model to another model with different embedding size. And this paper shows that it's possible. 

The writing of the paper is clear. 

The introduction of the method including translation to shared embedding space, and then search for target continuous prompt makes sense. 

I appreciate the experiment design in Table-2, which includes random and manual, as two baselines, along with the learned prompt baseline. The manual baseline(human) is important because it tells me that even though transferred prompt isn't as good as the learned prompt, but it is still competitive with manual prompts. 

Overall, I find the idea to be novel, results to be solid (did not beat the learned prompt baseline), but gives overall good performance, compared with human baseline.

### Weaknesses
Why is generative models not included for experiments?

I understand the explanation for choosing a factual dataset for evaluation. But the result and the claim by the paper will be much strong if there are more than 1 dataset to support its claim.

### Questions
Is BERT embedding transferrable to a GPT2 model?
Or is a GPT2 model embedding transferable to a pythia model?

### Soundness
3 good

### Presentation
3 good

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
The paper explores methods to train continuous/soft prompts in a source model and then transfer that prompt (and use it directly) for a target model. This can be useful to do relatively expensive soft prompt tuning on small source models and transfer the trained prompt to a bigger target model (compared to training the big model itself). 

The transfer idea involves encoding soft prompts from the source in a "relative space" (encode cosine similarity scores between soft prompt tokens and selected source token embeddings - "anchors") and then trying to search for target prompts that achieve similar similarity scores against corresponding anchor embeddings of the tokens in the target model. This can be done without backpropagating through the target model. This method can be also extended for multi-source transfer setup.

### Strengths
1. The target of transferring soft-prompt task semantics is an underexplored area of study. The target is well motivated in the paper. 

2. The method is novel and elegant.

3. The idea works better against some relevant baselines for transferring prompt task semantics from a source model to a target model.

### Weaknesses
1. If I understand correctly, at this point the method does not seem practical. We seem to get better accuracy just by directly using the source model. While the current approach transfers better than naive baselines or baselines based on earlier ideas (discretization, projectors), the transfer itself appears like a lose-lose scenario -- because you have to do extra work for transfer, and then you are (generally) trying to run the target soft prompt in a bigger (or same size) model. This seems pointless if just running the base source model gives us better overall performance. 

I am willing to accept this despite this because this paper seems like an early foray into the transfer of soft prompts and can inspire future research while serving as a baseline. Please correct me, however, if I am mistaking something about the immediate practical value of transfer given the current method.

### Questions
1. How is the optimum of eqn 7 or 5 searched for exactly?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a zero-shot continuous prompt transfer approach that learns prompt representations for target models (large models) from the representations of source models (small models). The assumption is that target models and source models share some common words as anchors. The learning approach is then forcing the projection of the soft prompts on the source anchors and the projection of those on the target anchors to be similar enough. Evaluation results on factual probing verifies the effectiveness of the approach. 

The paper can be improved if the authors could

(1) Compare the proposed method with a straightforward baseline:  v^t_i=\sum_{l=1}^k cos(v^s_i, a^s_l) a^s_l. This is a simplification of the proposed method with no need of learning.

(2) Evaluate the proposed method on tasks other than factual probing. Though there are 14 types of relations in the task, the task itself lacks diversity. The results can be more convincing if the authors could report comparison results on tasks such as text classification, NLI, semantic matching, and QA.

### Strengths
a new zero-shot prompt transfer approach
empirical studies on the benchmark of factual probing

### Weaknesses
The paper presents a zero-shot continuous prompt transfer approach that learns prompt representations for target models (large models) from the representations of source models (small models). The assumption is that target models and source models share some common words as anchors. The learning approach is then forcing the projection of the soft prompts on the source anchors and the projection of those on the target anchors to be similar enough. Evaluation results on factual probing verifies the effectiveness of the approach. 

The paper can be improved if the authors could

(1) Compare the proposed method with a straightforward baseline:  v^t_i=\sum_{l=1}^k cos(v^s_i, a^s_l) a^s_l. This is a simplification of the proposed method with no need of learning.

(2) Evaluate the proposed method on tasks other than factual probing. Though there are 14 types of relations in the task, the task itself lacks diversity. The results can be more convincing if the authors could report comparison results on tasks such as text classification, NLI, semantic matching, and QA.

### Questions
N/A

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
The authors propose a new method for zero-shot continuous prompt transfer from a pretrained language models to another. This method firstly finds the anchors between two language models (subsets of shared vocabulary) to construct a relative space. Then source prompts are encoded in the relative space and corresponding prompts in the target space are searched based on the source embeddings. Extensive experiments and analysis are carried out to support the effectiveness of this method.

### Strengths
1. The motivation is strong and clear. Continuous prompt tuning is an important issue, and this method allows easier transfer between model-specific continuous prompts. This may contribute to further research of parameter efficient learning and continual learning, etc.

2. The idea of using vocabulary as anchors and connectors between models is novel and interesting.

### Weaknesses
1. Method limitation: It seems that this method highly relied on shared vocabularies. Quality of vocabulary and selection of shared tokens may be important but no analysis is given.

2. Clarification: Some key details are not clarified (See questions)

3. Minor: Inconsistent use of search loss and matching loss in Section 3.4.

### Questions
1. When “shared vocabulary” is mentioned in the fourth paragraph of the Introduction Section, does it mean the vocabularies should be the same or just have some common parts?
2. In Equations 5 and 7, what is the optimization method and how do you implement this?
3. In experiments, BERT based models are deliberately chosen. Will this method be applicable to generative models such as GPT? This question is especially important when LLMs have recently been popular because one can use this method to find a set of optimal prompts on a small model and transfer them to a large one.
4. How are the anchors chosen? Are they randomly sampled? Will the selection process affect model performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
