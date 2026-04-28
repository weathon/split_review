# Seq-VCR: Preventing  Collapse in Intermediate Transformer Representations for Enhanced Reasoning

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Decoder-only Transformers often struggle with complex reasoning tasks, particularly arithmetic reasoning requiring multiple sequential operations. In this work, we identify \textit{representation collapse} in the model's intermediate layers as a key factor limiting their reasoning capabilities. Combined with dummy pause tokens as substitutes for chain-of-thought (CoT) tokens, our method significantly improves performance in arithmetic reasoning problems. In the challenging $5 \times 5$ integer multiplication task, our approach achieves $99.5\%$ exact match accuracy, outperforming models of the same size (which yield $0\%$ accuracy) and GPT-4 with five-shot CoT prompting ($44\%$). We also demonstrate superior results on arithmetic expression and longest increasing subsequence (LIS) datasets. Our findings highlight the importance of preventing intermediate layer representation collapse to enhance the reasoning capabilities of Transformers and show that Seq-VCR offers an effective solution without requiring explicit CoT supervision.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a regularization technique for preventing representation collapse across the intermediate representations of a deep sequence model. Their results show that 1. the regularization technique increases matrix entropy (low matrix entropy = representation collapse) and 2. when pause tokens are added the language model significantly improved in performance for 4x4 and 5x5 arithmetic tasks.

### Strengths
- The paper presents a novel regularization technique that improves the model's performance in several reasoning tasks
- The paper presents detailed analysis of the experimental results, showcasing how exactly the regularization techniques affects the diversity of representations, the learning dynamics, as well as the digit-by-digit accuracy on multiplication tasks.

### Weaknesses
 - The effect of the regularization technique was only studied for a relatively narrow domain of tasks, and it would be interesting to understand its effect on more general language benchmarks as well.
- Slightly more contextualization on how exactly pause tokens are incorporated would assist readers in understanding the work more easily as it is also a core part of what is being proposed in this work.

### Questions
Same as the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the performance of decoder-only models on tasks such as multi-digit mathematical reasoning that require a series of immediate representations. They hypothesize representation collapse of intermediate layers as a key contributor to this poor performance, preventing effective storage of the intermediate steps necessary for these kinds of tasks. While chain of thought reasoning can be effective in counteracting this collapse and performing well on such tasks, the proposed approach seeks to increase entropy among intermediate layers and achieve similar performance with at a reduced computational cost. Formulated in terms of alpha-order matrix-based entropy, the formulate a regularization term which aims are increasing variance and decreasing covariance in the intermediate representations. Additionally, pause tokens are included in the method. Results on three kinds of tests are presented – computing arithmetic expressions, identifying the longest increasing integer subsequence, and performing multiplication of 4 digit or 5 digit numbers. Performance with the regularization term and pause tokens leads to performance which approaches chain of thought on most tests, and regularization performs well on its own for the simpler tasks.

### Strengths
The details of the method to seem to be heavily inspired by VICReg, but so far as I can judge, the application of it to the sequence/Transformer is original. The method is, in theory, computationally attractive compared to CoT and the results are fairly compelling. 

The paper is clearly written and the quality of the presentation is moderately high.

### Weaknesses
The result in Table 1 naturally provokes a question: This and several previous studies show that GPT-2 with CoT performs remarkably well, but this is actually more difficult to achieve in larger models. What is the evidence/argument that the Seq-VCR approach will scale better with model size than CoT? Figure 8 hints at this but it doesn’t clearly address it.

The speedup vs CoT is intuitively reasonable but it would have been nice to see performance numbers as in the cite Deng 2024 paper.

Similarly, it would be helpful to understand the amount of hyperparameter optimization necessary for, e.g., identifying the number of pause tokens used to obtain the best results. Do the number of pause tokens necessary correlate with, e.g., task complexity?

For completeness, it would be nice to see CoT in figures 7 and 8.

### Questions
A discussion that clarified the improvement versus CoT would improve the significance, whether clearly establishing the speedup with Seq-VCR or showing its better generalization/scaling.

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
5

### Summary
Background: variance-covariance regularization (VICReg/VCReg) is a technique that was pioneered in vision models.  Given a batch of inputs, the technique uses an NN to encode those inputs to a batch of embedding vectors, and then computes a covariance matrix for the embedding vectors.  It introduces two losses based the covariance matrix: (a) the variance loss ensures that every dimension of the embedding vector has different values, distributed across the batch, and (b) the covariance loss ensures that different dimensions are not correlated.  In vision models, these two losses guard against representational collapse.  

The authors of this paper adapt VICReg from the vision domain to transformer-based language models.  They show that when combined with pause tokens, VICReg (now renamed to Seq-VCR) produces large improvements in several tasks that LLMs are usually very bad on -- multidigit arithmetic, arithmetic expressions, and a longest-increasing-subsequence task.

### Strengths
The application of VICReg to language models is novel as far as I know, and the experimental results are very compelling.  This could potentially be a high-impact paper in improving the reasoning capabilities of LLMs.

### Weaknesses
Unfortunately, the paper itself is hastily and sloppily written, and difficult to follow in places.  I had numerous questions when reading it that are not addressed by the text.  The current draft does not contain all of the information necessary to replicate these experiments, and does not discuss many of the crucial design decisions.  The authors claim that there is an "Appendix A", but neglected to provide any supplementary material.  See "questions" section below for specific questions.

One of the author's central claims is that transformers suffer from representational collapse, but I do not think that they adequately make that point based on the experimental evidence.  There are only two entropy charts in Figure 2, which cover only two narrow tasks.  On one of those charts (a) the collapse seems minimal at best, while on the other (b) the addition of pause tokens (the second key technique that the authors propose) actually increases collapse, rather than decreasing it.  I would need to see a much larger set of studies, over a variety of different tasks, including general language modeling tasks (translation etc.) to fully buy the author's argument about collapse.  If the authors did such a study, however, it would be a significant breakthrough.

Similarly, I would like to know what the effects of VICReg are on more general language modeling tasks.  If the technique helps the model multiply 5-digit numbers after fine-tuning, but otherwise degrades peformance on most other language modeling tasks, then the technique is useless.  Because the authors do not perform this ablation, it is impossible for me to evaluate whether this is a high-impact advance over SOTA, or a trivial result.

Finally, the use of pause tokens is interesting, but also seems haphazard.  They authors themselves admit that the number of pause tokens is task-specific.  To employ this technique more widely, I would need to see a more comprehensive test of where, how many, and under what circumstances pause tokens should be added.

More specific criticisms:

Equation (3) defines the Seq-VCR loss.  The text of the paper claims that it is "inspired by" prior work, and cites such work appropriately, but it is more than just "inspired".  Equation (3) is lifted almost verbatim from the orginal VICReg (Bardes 2021) and VCReg (Zhu 2023) papers, and the authors need to be crystal clear about the source of that equation in the text of the paper.   

(As a minor nit, it is unclear to me whether or not the covariance term in equation (3) should have an additional 1/(d-1) factor; VICReg has the term, while VCReg does not.  I would have appreciated it if the authors explained why they chose one version over the other.)

For further clarity, the authors should also devote a few lines (in the text of the paper) to defining how the covariance matrix C is computed; as is done in other papers.  Otherwise, it can easily be confused with the cross-correlation matrix of the Barlow twins technique, which the authors also cite as inspiration.  _To further clarify -- I know you are using the covariance matrix, and not the cross-correlation matrix.  It might be helpful to other readers to have that spelled out by writing down the equation._

### Questions
(1) Pause tokens are a crucial part of the author's technique, but at no point do the authors describe where, and how, the pause tokens are added to the input.  

(2) Representational collapsed supposedly happens in the intermediate layers of the transformer, and yet the Lseq-VCR loss term is only applied to the final layer.  (Line 225).  Shouldn't it be applied to the intermediate layers, where you measure the entropy?  Why not?

(3) Equation (3) introduces $\lambda_1$ and $\lambda_2$ as hyperparameters, but the paper fails to say what they are set to. 

(4) What batch size is used for computing the covariance matrix?

(5) Equation 3 computes the covariance matrix only across the batch dimension.  Why?  In a transformer, you could potentially use the length dimension as well, which would drastically increase the effective batch size.  Did you do an ablation study which showed that to be ineffective?

(6) How is the projection layer $f_{proj}$ trained?

(7) For GPT2 on multiplication, you fine-tune a pre-trained GPT2 model, despite the fact that the pre-trained GPT2 has no real multiplication ability to start with.  Why bother with a pre-trained model, instead of just training from scratch, as you do with minGPT on arithmetic expressions?

### Soundness
2

### Presentation
1

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work identifies representation collapse in the LLM intermediate layers as a key factor limiting their arithmetic reasoning capabilities. The paper proposes sequential variance-covariance regularization (Seq-VCR). It then combines Seq-VCR with pause tokens to prevent the representation collapse. Experiments on GPT-2-small and minGPT demonstrate the effectiveness in improving accuracy on arithmetic reasoning.

### Strengths
1. The identified representation collapse is quite interesting

2. The proposed method, including Seq-VCR regularization loss and pause tokens, demonstrates novelty and effectiveness based on the experimental results.

### Weaknesses
1. The representation collapse experiment was conducted only on GPT-2. I am curious whether this phenomenon occurs in more recent and larger LLMs, such as LLaMA 3 or LLaMA 3.1. The authors should either include additional experiments or provide a theoretical analysis to demonstrate that this is not an isolated case.

2. While the proposed Seq-VCR regularization loss has been shown to be effective in arithmetic reasoning tasks, I wonder whether adding this loss after the next token prediction loss would impact the LLM's performance on other tasks  (e.g., math reasoning and general MMLU). If it does have an effect, then this method may not be widely applicable. I encourage the authors to discuss this point.

### Questions
see the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2
