# Better autoregressive regression with LLMs

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
Large language models (LLMs) have proven successful on many machine learning  tasks,
including those that do not involve language generation. 
In specific, LLMs have been shown to be effective in solving regression, where the targets are real-numbers.
One common approach is to fine tune the LLM based on the log-perplexity loss and use  autoregressive sampling at the inference time. 
Another approach relies on adding a predictive head and finetuning it with a suitable loss. 
Despite the success, there has not been a study on the principled ways of using decoder LLMs for regression. 
In this work we compare different prior works under a unified view, and introduce RAFT, regression-aware fine-tuning, a novel approach based on the Bayes-optimal decision rule. 
We demonstrate how RAFT improves over established baselines on several benchmarks and model families.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses regression tasks for language models, specifically using decoder transformer models to predict a numerical value $y$ based on an input sequence $x$. In this setup, two standard methods for regression are examined: (i) quantizing $y$ into discrete bins, where values are mapped to tokens (e.g., sentiment values represented by tokens 1, 2, 3, 4, 5) or (ii) training a multilayer perceptron (MLP) head on top of a decoder language model with an $L_2$ loss.

Each of these approaches has known limitations. Quantization lacks sensitivity to numerical proximity, treating all incorrect tokens as equally wrong (e.g., predicting 4 is treated the same as predicting 5, regardless of proximity to a true value of 3). Meanwhile, an MLP head with $L_2$ loss does not fully leverage the language model’s pretrained token prediction capabilities. To address these issues, the paper studies the MALI estimator, which uses a grid of tokens and calculates $\sum_{y \in \mathbf{y}_{\text{grid}}} p(\text{str}(y) | x ) . y $ 

Although MALI typically serves as a post-training estimator, the authors explore its application in fine-tuning language models for regression tasks, providing extensive comparisons and ablation studies to validate its performance against existing methods.

### Strengths
The paper is well-organized, with a clearly defined objective and comprehensive experimental comparisons, making it accessible and straightforward to follow. I enjoyed reading the paper.

### Weaknesses
1. **Performance Drop on Alternative Grids (Lines 902–903 and L531)**: You note a performance drop when using a grid of letters a–e, yet Table 11 shows similar MSE to the numerical grid. Could you clarify this inconsistency?

2. **Lemma 1 (Line 187)**: Based on the appendix, does the norm in Lemma 1 refer to an $L_1$ norm rather than $L_2$? The crafted example in the appendix (where a probability mass of $\epsilon / 2$ is positioned at 0 and $y_\text{max}$ implies that the $L_1$ loss should satisfy $E_x [ \| P(. | x)  - p(.|x)  \| ] <= \epsilon $ (the norm being L1), given that line 747 defines $ | \mathbb{P}(. | x) - p(.|x) |_{1} < \epsilon $.

3. **Token Granularity and Grid Complexity**:
   In the RAFT experiments, was the grid composed solely of single tokens? If so, does this also apply to the months-named grid?
   If the pretraining hypothesis holds that a simple grid (like 1–5) leverages pretrained information effectively, would a more complex grid (e.g., values such as 0.97, 2.3, 3.001, etc.) yield similar performance? I think this would be a very important question that can substantially strengthen the paper. The current analysis does not explore the limits of the pretraining hypothesis, and it is unclear if the performance is due to the simplicity of the grid or the pretraining itself.
4. **Dataset Examples**: Including a table of dataset examples and inputs/outputs of the RAFT model would further help with clarity. It would help in verifying dataset characteristics too. The lack of concrete examples makes it difficult to assess the practical implications of the method.

### Questions
1. **MSE Variations on Different Grids**: The MSE increase when using a months-named grid (versus alphabetic grids) is curious. Are the months tokenized as single or multiple tokens? Could this affect pretraining-based semantics, or could it be due to the number of tokens in use? Understanding why alphabet tokens retain performance while month names don’t could provide insight.
2. **Post-Training Distribution of the MALI Predictor**: After RAFT training, what does the MALI predictor’s distribution look like over grid elements? Since Lemma 2 emphasizes the grid’s max and min values, it would be informative to know how the grid’s distribution evolves post-training, including entropy relative to a uniform distribution over tokens.
3. **Baseline Comparisons**: While the paper compares MALI-based methods with other similar approaches, are these baselines considered state-of-the-art for your chosen tasks like sentiment analysis or the review estimations? Could simpler models, such as random forests, achieve lower MSE on these tasks? In other words, the experiments provide a good comparison among the methods based on finetuning a pre-trained transformer, but I wanted to clarify if these MSEs are actually state of the art compared to other methods too.

### Soundness
3

### Presentation
4

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
This paper provides a comparison among several methods for autoregressive regression with LLMs, where the goal is to predict numerical value given the text input (e.g., text similarity). The authors propose a new fine-tuning approach, namely RAFT, which computes squared loss directly on the grid of possible outcomes without explicit sampling from the model. Empirical results show the effectiveness of the proposed approach across various datasets.

### Strengths
- Paper (in general) is well-written and easy to follow (even though there are still small things that require further clarification)
- Simple and effective idea 
- Shown results indicate improvements across different tasks
- Additional analysis on several aspects (grid, pre-training, masking)

### Weaknesses
The predictive head approach closely follows the RAFT; however, there is no extended discussion of what sets RAFT apart.

Note that the below weaknesses are mostly minor.

The authors highlight the issues of the decoder-based LLMs. However, there is no baseline comparison (i.e., it is not clear what the potential upper bound is with current technologies). In the literature, performance for datasets like SSTB is often reported as Pierson/Spearman correlation
- Since some things are still unclear to me in the experiment setup (please see question), I am hesitant to assign a score

### Questions
- In Table 3, you report wireless predictive head results for the 2B model as 0.51, while in Table 4, the best result is 0.48 (special logits token). --
- In Table 3, the predictive head closely follows the results of RAFT. Could you please elaborate more on that? (more than described in 429-430)
- While comparing the effect of the grid, why have you excluded the STSB benchmark? It's a most interesting case since the grid 1-5 is a subset of the output space. I would be curious to see results and see if adding 0 makes any difference, for example

### Soundness
3

### Presentation
4

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
This work introduces a new fine-tuning method for autoregressive language models to improve their performance on regression tasks, such as sentiment analysis, semantic similarity, and quality estimation for translation. 

This work argues that the cross-entropy loss is not suited to regression tasks, since small deviation of the model from the ground truth can lead to high regression error. Indeed, the cross-entropy objective does not take into account the numerical value associated with text tokens. Instead, authors propose a new fine-tuning method (RAFT) based on the "Metric-aware LLM inference for regression" (MALI) approach.

### Strengths
- The research question is relevant and interesting.
 - The presentation of MALI (previous work) is clear.
- The counter-example of Lemma 1 is good. Since it's short, I would include it in the main body if possible.
- The experiment on using semantically unrelated tokens for the regression task (Table 11) is interesting.

### Weaknesses
 - On a first read, I misunderstood the implications of Lemma 1. I think it would be worth slightly rewriting the paragraph after Lemma 1. In particular, I would replace the sentence 
> Intuitively, log-perplexity fine-tuning treats all “wrong” predictions the same, *and does not account for the magnitude of their differences from the ground-truth target*.

by

> Intuitively, log-perplexity fine-tuning treats all “wrong” predictions the same, *as it is unaware of difference in magnitude of the numerical values represented by the tokens. For example, assuming that "100" and "1000" are represented with a single token, placing $\epsilon$ too much mass on tokens representing "100" is penalized similarly as placing  $\epsilon$ too much mass on the token "1000".

If you have a better rephrasing, you can of course use something else, but I think the aforementioned sentence can be improved (e.g. using my example).

- On the line 371, you are explaining that you are experimenting with a reduced training set for the STSB benchmark (using 1k examples instead of the whole training set). I understand that it is interesting to vary the amount of training data, but why are you only reducing the training set size on STSB and not on the other datasets?

- **Main weakness**: While your paper studies regression tasks using autoregressive models, you observe on lines 465-467 that when training from scratch, the predictive head methods work best. Since encoder-only models such as BERT are widely used for tasks mentioned in the introduction (e.g. sentiment analysis, regression, ranking), it would be valuable to include a baseline of a large fine-tuned RoBERTa model on the same tasks that you present in the paper. Your findings would remain interesting and relevant in case the RoBERTa baseline was beating RAFT, but I think knowing how RAFT compares to fine-tuning RoBERTa is very relevant to practitioners. Therefore, I would suggest adding the following experiments (with the same hyperparameter tuning as RAFT):
    - Prediction head regression over a mean-pooling of RoBERTa representation (over sequence length)
    - Prediction head regression over the output for the CLS token of RoBERTa model
    - Both variants with either frozen RoBERTa weights, as well as unfrozen weights

- There could be more practical details on the fine-tuning process. Are you updating all the parameters of the model or did you freeze some of them (eg. update only the last linear layer)? Which optimizer are you using? If you are using Adam, what values of the betas, weight decay, and epsilon are you using? What batch size are you using? How long does one training run takes on average? How many machines did you need? The answers to these questions are important to help other researchers reproduce your results.

### Questions
- I don't understand why the authors are comparing MALI (regression on continuous values) against the Minimum Bayes Risk (MBR) prediction literature, since it optimizes non-regression metrics on the discrete grid (section 3.4). There is one small experiment comparing the sampled regression aware approach (table 8), but it is only in the appendix. It would be helpful to either strengthen the connection between MBR and MALI/RAFT, or consider moving this section to the appendix if it's not central to the paper's main argument. If you choose to keep it in the main text, consider explaining more clearly why this comparison is important for understanding RAFT's contributions.

- Similar to the experiment presented in Table 11, did the authors consider training new token embeddings for the regression task? For example, instead of using digits 1-5, they could start from 5 untrained tokens. I would expect this to work worse, but I am curious about the results.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores two approaches: (1) fine-tuning an LLM using the log-ppl loss with autoregressive sampling during inference, and (2) adding a predictive head and fine-tuning it with an appropriate loss function. Following an in-depth analysis, this paper introduces RAFT, a regression-aware, Bayes-optimal method for optimal LLM fine-tuning. Extensive experiments demonstrate that RAFT consistently outperforms baseline methods across various datasets and models.

### Strengths
1. This paper provides a well-rounded formulation for LLM-based regression approaches.
2. It presents thorough evaluations across diverse tasks (e.g., Wireless, Music, Personal Care) and models (e.g., Gemma and PaLM).
3. The proposed RAFT method demonstrates effectiveness across these benchmarks.

### Weaknesses
1. While this paper presents a strong approach, it addresses a relatively niche problem. In my view, the choice between autoregressive sampling and a predictive head largely depends on the specific task, making it less crucial to claim that your method is universally superior to both across all tasks. The paper does not adequately explore the conditions under which each approach excels, which limits the practical guidance it offers.
2. The proposed method does not show a significant improvement over the predictive head. For instance, in Table 9, RAFT performs worse than the predictive head on the Music dataset. The lack of consistent and substantial gains raises questions about the practical utility of the proposed method, especially given its increased complexity compared to a simple predictive head.

### Questions
Could you clarify the scenarios in which a predictive head performs better versus those where autoregressive sampling is more effective? Also, is RAFT the optimal choice in all situations, or are there cases where other methods might be preferable?

### Soundness
3

### Presentation
3

### Contribution
1
