# Improving length generalization in transformers via task hinting

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 3, 5

## Abstract
It has been observed in recent years that transformers have problems
  with {\em length generalization} for certain types of reasoning and
  arithmetic tasks. In particular, the performance of a transformer
  model trained on tasks (say addition) up to a certain
  length (e.g., 5 digit numbers) drops sharply when applied to longer instances of the
  same problem. This work proposes an
  approach based on {\em task hinting} towards addressing length generalization. Our key idea is that while training the model on task-specific data, it
  is helpful to simultaneously train the model to solve a
  simpler but related auxiliary task as well.

  We study the classical {\em sorting} problem as a canonical example
  to evaluate our approach. We design a multitask training
  framework and show that models trained via task hinting
  significantly improve length generalization. In particular, for sorting we show that it is possible to
  train models on data consisting of sequences having length at most
  $20$, and improve the test accuracy on sequences of length $100$
  from less than $1\%$ (for standard training) to more than $92\%$
  (via task hinting).

  Our study uncovers several interesting aspects of length
  generalization. We observe that while several auxiliary tasks may
  seem natural \emph{a priori}, their effectiveness in improving
  length generalization differs dramatically. We further use probing
  and visualization-based techniques to understand the internal
  mechanisms via which the model performs the task, and propose a theoretical construction
  consistent with the observed learning behaviors of the model. Based
  on our construction, we show that introducing a small number of
  length dependent parameters into the training procedure can further
  boost the performance on unseen lengths. Finally, we also show the
  efficacy of our task hinting based approach beyond
  sorting, giving hope that these techniques will be applicable in
  broader contexts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the role of introducing auxiliary tasks during training for the problem of length generalization. In particular, they focus on the task of sorting. When trained on sequences of length up to 20, the model gets less than 1% accuracy on sequences of length 100 (and scaling training dataset size or model size doesn't help much). However, when the training dataset is augmented with an auxiliary and simpler task of predicting the successor of a given number in the sorted list, the accuracy at length 100 jumps significantly. Not surprisingly, the efficacy of this method varies between different auxiliary tasks. 

Further, the paper also suggests a theoretical construction for how a 2-layer Transformer might be able to do this task. The theoretical construction uses a length-dependent parameter used for the softmax operation in attention layers. The introduction of this length-dependent parameter is empirically shown to help in length generalization (even in the absence of auxiliary tasks).

### Strengths
1. I enjoyed reading the paper. It is very well written.

2. The idea of using auxiliary data to improve length generalization seems very natural and this paper takes the first step in exploring this in a simple setting. It can potentially lead to more interesting work on how to select the auxiliary data.

3. The idea of using a length-dependent parameter in the softmax operation also seems interesting and deserves more attention.

### Weaknesses
One major weakness of the paper is that its scope is a bit limited. While it shows the efficacy of using auxiliary data for length generalization, its results are limited largely to the problem of sorting. While I don't doubt that auxiliary data can help in length generalization for other tasks as well, it is unclear how to go about finding the right auxiliary data given a task. For instance, the paper does not explore the relationship between the complexity of the auxiliary task and its effectiveness. Is a very simple auxiliary task sufficient, or is there a sweet spot in terms of task complexity? Furthermore, the paper does not delve into the potential negative transfer that might occur if the auxiliary task is not well-aligned with the primary task. This aspect is crucial for practical applications, as blindly adding auxiliary tasks could potentially hinder performance rather than improve it. The paper also lacks a systematic exploration of different types of auxiliary tasks beyond the successor, predecessor and parity tasks, which limits the generalizability of the findings.

### Questions
In this paper, no positional embeddings seem to have been used, does the efficacy of the proposed auxiliary task change when using positional embeddings?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method called "task hinting" to improve how well transformer models generalize to longer sequences than they were trained on. This involves training the transformer on both the main task and a related simpler task simultaneously. The authors found that this method significantly improves the model's performance on longer sequences. The effectiveness of different auxiliary tasks varies, with some aiding generalization more than others. Additionally, a small number of length-dependent parameters introduced into the model can further enhance performance.

### Strengths
1: The finding of this paper is interesting. The visualized internal mechanism is surprising if there is no cherry-picking.
2: The proposed task hinting method looks good considering its effectiveness on the sorting tasks.

### Weaknesses
1: Multi-task is not novel.  How / why it can help length generalization is still unclear in this paper.
2: The writing is poor. This paper is not organized well. For example, at the beginning, authors try to categorize length generalization into two categories. However, the taxonomy does not make sense and it cannot fit the task-hinting well.
3: The results of tempered softmax are not surprising. With longer sequences, self-attention requires scaling is well-known. (The hugging face transformer library has even involved this feature). To be more specific, the scaling factor should be "log_n scale'.
4: This paper is not completed within the required number of pages by ICLR.
5: Some typo and grammatical errors.

### Questions
Please check the weakness part.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper tackles transformers' length generalization issue by introducing task hinting, a method that trains the model on an auxiliary task alongside the main task. Using the sorting problem as a test case, the authors demonstrate improved length generalization. They also explore the internal workings of the model. They have constructed a sorting network, but it's not directly related to the task hinting idea.

### Strengths
The paper is original in its approach to task hinting, a relatively unexplored idea. The idea seems promising from the current results, but only applied to a single task. The paper is generally clear, although there are areas where further clarification would be beneficial.

### Weaknesses
 - The paper's main weakness is its limited application to a single task, which weakens the validity of the proposed idea.
- It's also unclear if the same performance gain could be achieved via curriculum learning.
- Also, the comparison between this approach and scratchpad training is not made. What if we provide auxiliary hints as a part of the scratchpad?
- The theoretical results are *not* related to the key idea of task hinting.

### Questions
- It's unclear if the same performance gain could be achieved via curriculum learning. In some sense, the auxiliary task can be viewed as a partial sorting, i.e., so it's a simpler task than the original target task.

- Could you clarify the role of the mask values in Figure 3.1? Why are there mask values of 0 after some 1's? Not sure why you need to pad when training decoder models. 

- Could you provide more details on the fill hint task? Its current explanation is unclear.

- Does this idea work for tasks other than sorting? Could you apply the same to many other tasks?

- Can you use the factor analysis (e.g., those introduced in the recent paper [1]) for the interpretation part? Especially see the induction head analysis of this aforementioned paper. 

[1] https://arxiv.org/abs/2310.04861

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to improve the length generalization properties of the transformer by simultaneously training the model to solve a simpler but related auxiliary task named task hinting. This paper studies the classical sorting problem and demonstrates that models trained via task hinting significantly improve length generalization. 

The authors also show that the effectiveness of different tasks hinting at improving length generalization differs dramatically. They further use probing and visualization-based techniques to understand the internal mechanisms, and propose a theoretical construction consistent with the observed learning behavior of the model.

### Strengths
The paper proposes a new method for improving length generalization and demonstrates it experimentally.

### Weaknesses
1. It is not a surprising phenomenon that simultaneously training the model with some related task can help to improve the generalization capability of transformers. 
2. The proposed method to solve length generalization is not generic. For any specific task, "task hinting" requires researchers to search for a good task that could improve length generalization. Searching for such a task may be complicated and highly task-dependent. 
3. The authors only studied the sorting task (and another task hidden in the appendix). It is unclear if "task hinting" could be easily developed as a generic method for solving length generalization.

### Questions
Could the authors respond to my comments above?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
