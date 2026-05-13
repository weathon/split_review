# Limits to scalable evaluation at the frontier: LLM as judge won’t beat twice the data

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
\noindent
High quality annotations are increasingly a bottleneck in the explosively growing machine learning ecosystem. Scalable evaluation methods that avoid costly annotation have therefore become an important research ambition. Many hope to use strong existing models in lieu of costly labels to provide cheap model evaluations. Unfortunately, this method of using models as judges introduces biases, such as self-preferencing, that can distort model comparisons. An emerging family of debiasing tools promises to fix these issues by using a few high quality labels to debias a large number of model judgments. In this paper, we study how far such debiasing methods, in principle, can go. Our main result shows that when the judge is no more accurate than the evaluated model, no debiasing method can decrease the required amount of ground truth labels by more than half. Our result speaks to the severe limitations of the LLM-as-a-judge paradigm at the evaluation frontier where the goal is to assess newly released models that are possibly better than the judge. Through an empirical evaluation, we demonstrate that the sample size savings achievable in practice are even more modest than what our theoretical limit suggests. Along the way, our work provides new observations about debiasing methods for model evaluation, and points out promising avenues for future work.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses an important challenge in LLM evaluation: the reliance on costly, high-quality annotations, which has become a key bottleneck as model complexity grows. The authors investigate the potential of using large, pre-trained models as "judges" to evaluate newer models, thereby reducing the need for extensive human annotation. They present a theoretical analysis showing a significant limitation: when the judge model’s accuracy is not superior to that of the evaluated model, debiasing methods cannot reduce the necessary amount of ground-truth labels by more than half. Empirical results further underscore this limitation, as practical savings on annotation requirements fall even shorter than the theoretical prediction.

### Strengths
1. The authors identify and tackle the misalignment between the ranks produced by the ground-truth score and those produced by LLMs. 
2. The motivation for the submission is formalised from the judge's bias and agreement rate perspective. 
3. The effect of real samples and the limited benefit of proxy samples for sample efficiency are well modelled and explained.

### Weaknesses
1. The writing sometimes is not very easy to follow.
2. The submission only focuses on binary evaluation, can it generalised to more complicated cases?

### Questions
See weaknesses section

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
LLM-as-judge has become a popular practice for assisting humans in labeling and evaluating model performance. While this method shows promise, it still faces critical challenges related to inherent biases. This paper examines the biases inherent in LLM-as-judge setups and reviews existing debiasing methods. Especially, with the rapid advancement of models, there is a growing likelihood that evaluated models may surpass the judge model in performance. The authors demonstrate that when the judge model performs worse than the evaluated model on a given task, even the best debiasing methods offer no advantage over simply doubling the amount of ground truth data.

### Strengths
Originality: To the best of my knowledge, this paper is the first to theoretically analyze biases in different judging styles and examine the impact of using state-of-the-art (SOTA) models as judges.

Clarity: The paper covers many important topics, but the structure could benefit from refinement to improve readability. Currently, some sections feel challenging to follow due to a somewhat disjointed flow of ideas.

Significance: With the growing use of LLM-as-judge setups in the research community, this work addresses a highly relevant issue. The paper provides theoretical analysis of inherent biases and explores how sample size impacts the effectiveness of debiasing methods.

### Weaknesses
 **Structure**: The structure of the paper feels somewhat disjointed, making it difficult to follow the flow of ideas.

**Clarity of Results**: The key takeaways from the final set of experiments (line 452) are not well articulated. The experimental setup and the expected outcomes are unclear. 

**Balanced Agreement**: In Section 3.6, where the concept of balance agreement is discussed, but the usage and its validation is missing. I am confused by its usage.

### Questions
Line 133: Why is it stated that precisely modeling the specific relationship is infeasible? Could you provide an example to clarify this?

Proposition 1: The explanation is unclear. What does "point-wise" mean in the context of line 166?

In the second setting in the experiment, arena-sylye benchmark, we see sample efficiency lower than 2 when using GPT 4v. but when evaluating on llaam2 -7b it's over 2, what's the examplantion here? is it due to the hugh performance gap between llama2-7b and the judge model?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates the model-as-judge evaluation framework when a calibration set with ground-truth scores is available to debias the judging LLM. It first shows the gap between prediction accuracy and ranking and then uses the prediction-powered inference as a calibration method to debias the judging LLM. With the debiased prediction, the paper shows that the sample efficiency is upper bounded by 2. The theoretical result is validated in the experiment with several popular LLMs.

### Strengths
The theoretical results are solid and the experiment result matches well with the conclusion from the theoretical analysis, which makes the paper very strong.

Novelty and Significance: Giving an upper bound for the sample complexity of LLM-as-a-judge is novel and significant.

Soundness: The theoretical results and the derivation are sound.

### Weaknesses
The limitation is discussed in Section 6, which I pretty much agree on. It will be better if weighted PPI such as Stratified PPI can be evaluated in the experiment to show the difference.

Clarity: The clarity can be improved by adding examples of Q&A.

### Questions
Will the experiment result still be consistent with Theorem 6 if the tasks are challenging such as TruthfulQA?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the paradigm of model evaluation in which one uses a capable existing model

### Strengths
The paper studies an interesting problem, and presents both theoretical and empirical results supporting its central claim. The theoretical results are non-trivial and actually shed light on the practical question of LLM evaluation. Overall I enjoyed reading the paper.

### Weaknesses
The clarity of writing could be somewhat improved, especially the exposition around the experiments, the section feels a bit rushed and it was challenging to relate the content of the figures to the central message of the paper and the theoretical results. I would also suggest increasing the descriptiveness of the figure captions.

The experiments could also be more thorough - currently all experiments are on MMLU, but more datasets would strengthen the empirical results.

See also questions below.

### Questions
- I am not very familiar with PPI (S3.3), what is the relation between PPI and doubly robust estimation from causal inference? At least on the surface level \theta^{PP} looks similar to many estimators from causal inference.

- What is the intuition behind the constant factor equalling two exactly?

- Is it straightforward to extend the theory from the binary case to the continuous case (as in the experiments)? Or are there techniques specific to binary outcomes.

### Soundness
3

### Presentation
3

### Contribution
3
