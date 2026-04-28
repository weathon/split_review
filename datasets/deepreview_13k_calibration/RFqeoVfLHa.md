# Progress or Regress? Self-Improvement Reversal in Post-training

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Self-improvement through post-training methods such as iterative preference learning has been acclaimed for enhancing the problem-solving capabilities~(e.g., mathematical reasoning) of Large Language Models~(LLMs) without human intervention. However, as exploration deepens, it becomes crucial to assess whether these improvements genuinely signify progress in solving more challenging problems or if they could lead to unintended regressions. To address this, we propose a comprehensive evaluative framework that goes beyond the superficial pass@1 metric to scrutinize the underlying enhancements of post-training paradigms for self-improvement. Through rigorous experimentation and analysis across diverse problem-solving tasks, the empirical results point out the phenomenon of \emph{self-improvement reversal}, where models showing improved performance across benchmarks will paradoxically exhibit declines in broader, essential capabilities, like output diversity and out-of-distribution~(OOD) generalization. These findings indicate that current self-improvement practices through post-training are inadequate for equipping models to tackle more complex problems. Furthermore, they underscore the necessity of our critical evaluation metrics in discerning the \emph{progress or regress} dichotomy for self-improving LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper analyzes post-training via self improvement loops for LLMs. Their results suggest that there is a sort of "Goodhardt's Law" at play sometimes, where improving the benchmark scores will often lead to decreased performance after some point. They particularly note diversity as an important metric which often drops.

### Strengths
Good idea and experiments. It's an important and timely topic. The observation that some metrics like diversity are sometimes unmeasured with these methods is very important.

### Weaknesses
I think the writing can be improved somewhat, even if the core ideas are clear.

### Questions
Do you expect these results to hold with RL posttraining?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work points out a phenomenon called self-improvement reversal. To be specific, the authors formulate three post-training
paradigms (iterative SFT, iterative DPO, and iterative SFT-DPO) and conduct experiments to examine how various factors (iteration steps, different models, task difficulties) influence self-improvement. Although such strategied shows a general trend of improvement in pass@1
accuracy. They still struggle in some other problems like solutions diversity and OOD generalization. This paper provides a deeper understanding to self-improvement.

### Strengths
1. The experiments are well-designed and provide a comprehensive understanding to the internal mechanisms of self-improvement.
2. This paper finds that such pass@1 accuracy metric may lead to a wrong judgment about model performance.
3. The experimental results in Figure 2 are insightful. The relationship between correct answer coverage and iterative post-training methods has not been discussed before.

### Weaknesses
1. Some of the conclusions in this paper are as expected, e.g. results from Table 3 are related to [1].

### Questions
No more questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work studies the post-training steps of supervised fine-tuning and preference optimization during iterative self-improvement, where an LLM improves by training on its own generated solutions. The authors claim that such iterative post-training may show progress according to traditional top-1 test accuracy measures, but may also negatively impact semantic diversity and OOD performance on other tasks. They propose an iterative self-improvement algorithm which, given a training set of inputs and ground truth outputs, iteratively fine-tunes a model on self-generated outputs labelled according to whether they are correct or incorrect, serving as synthetic preferences similar to RLAIF. The authors compare 3 methods of fine-tuning: SFT, DPO, and alternating SFT-DPO. They find that improvement plateaus for most tasks after ~3 iterations before declining, as well as a few other findings. Next, they show that while accuracy on the test set increases over post-training, diversity across a number of metrics may be reduced as well as accuracy on OOD tasks.

### Strengths
- Well-motivated and timely. Review of related work is thorough.
- Iterative self-improvement post-training algorithm and most of the analyses seem general enough to be applied to arbitrary domains with minimal changes.
- Interesting reversal results with diversity and OOD generalization decreasing during post-training. Used a variety of diversity metrics.

### Weaknesses
 - I'm not sure I understand Improvement Sets (Section 5.1). Perhaps I'm missing something here, but in my understanding of figure 3, it seems somewhat trivial that accuracy@N increases with greater N.
- I'm also not sure I understand the point of Group Disparity (Section 5.3). Why not just compare level 1 accuracy vs. level 5 accuracy directly, if level 1 accuracy is increasing and level 5 is decreasing?
- Correct answer coverage seems potentially at odds with solution diversity, so I'm not exactly sure how to resolve these two metrics. Is it possible that better performing models aways have lower solution diversity?
- Many of the results figures could be improved, including with longer captions:
	- Figure 1 - It's currently hard to compare SFT vs. DPO vs. SFT-DPO across (a) - (c) since different rows have different scales for the y-axis.
	- Figure 2 - The left figure took some effort for me to understand. Maybe example questions/answers would help.
	- Figure 3 - The x-axis is unlabeled and the caption is very short. As stated above, I also wasn't sure what the main takeaway of this is.
	- Figure 5 - The bottom y-axis has a very small range [90, 95], and I don't have a good sense for what the scale of these values should be. The caption for this also seems too short, and I don't know what the blue dotted line means.

### Questions
- Figure 3: why is it surprising that pass@N accuracy increases with greater N?
- How does correct answer coverage relate to solution diversity? Are the two at odds with each other?
- Is solution diversity inherently desirable in domains like mathematical reasoning? Is it possible that higher performing models on certain domains always have lower diversity?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work goes beyond pass@1 to dive deeper into evaluating self-improvement methods for mathematical reasoning. They show that improvement in benchmark performance of self-improvement showed signs in regression in areas such as output diversity and OOD generalization. They developed a new evaluation framework for current self-improvement methods to evaluate on.

### Strengths
- very relevant topic for the conference
- good empirical results and comprehensive experiments
- interesting findings that can inspire future research directions:
	- most methods decline in task performance after ~4 iterations
	- declined abilities in output diversity and OOD generalization
	- lesser powerful models gain more, but more powerful models achieve better max performance
	- M_1 performance effects subsequent iterations

### Weaknesses
 - (minor) in introduction, it wasn't apparent why the new metrics are important. For example why is diversity needed in solving these reasoning tasks?

### Questions
- for table 3, can you label x-axis as `sampling N`? Also what model is used here?

### Soundness
3

### Presentation
3

### Contribution
3
