# What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
Instruction tuning is a standard technique employed to align large language models to end tasks and user preferences after the initial pretraining phase. 
Recent research indicates the critical role of data engineering in instruction tuning -- when appropriately selected, only limited data is necessary to achieve superior performance. 
However, we still lack a principled understanding of what makes good instruction tuning data for alignment, and how we should select data automatically and effectively.
In this work, we delve deeply into automatic data selection strategies for alignment.
We start with controlled studies to measure data across three dimensions: complexity, quality, and diversity, along which we examine existing methods and introduce novel techniques for enhanced data measurement. 
Subsequently, we propose a simple strategy to select data samples based on the measurement. 
We present \deita~(short for \emph{Data-Efficient Instruction Tuning for Alignment}), a series of models fine-tuned from LLaMA and Mistral models using data samples automatically selected with our proposed approach.  
Empirically, \deita~performs better or on par with the state-of-the-art open-source alignment models with only 6K SFT training data samples -- over 10x less than the data used in the baselines. 
When further trained with direct preference optimization (DPO), \deita-Mistral-7B + DPO trained with 6K SFT and 10K DPO samples achieve 7.55 MT-Bench and 90.06\% AlpacaEval scores.
We anticipate this work to provide tools on automatic data selection, facilitating data-efficient alignment.
We release our models as well as the selected datasets for future researches to effectively align models more efficiently.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a data selection algorithm for instruction tuning that selects data points where 1) the queries are complex (e.g.: in terms of the constraints in the request); 2) the responses are high quality (e.g.: helpfulness, creativity); and 3) the data points are diverse. For quantifying complexity and quality, a dataset is collected for each of the two aspects by prompting ChatGPT in the following way: a seed set of samples are taken from the original dataset, ChatGPT is prompted to iteratively improve the complexity or quality of each of those samples along relevant dimensions, ChatGPT is then asked to score these samples for complexity or quality, a separate model (Llama-7B) is trained to predict these scores and then used to score the entire instruction tuning dataset. For diversity, the selected pool (initialized to be empty) is iteratively grown by adding points only if they are beyond a certain distance to their nearest neighbors already in the pool.

The data selection procedure sorts the existing dataset by the product of quality and complexity scores, and uses the diversity based selection procedure to select the points from the sorted set to a prespecified size.

The algorithm is evaluated by comparing Llama-13B models trained using the data selection procedure against existing instruction tuned models (trained on other datasets), and random selection baselines (trained on the same datasets of the same sizes with points selected randomly). Comparisons are made in terms of AlpacaEval and MT-Bench, where GPT-4 evaluates the responses and human evaluation on a sample of 100 requests from LIMA's test set. The algorithm outperforms random selection, and also other instruction tuned models based on Llama-1 trained on more data.

### Strengths
- The procedure used to quantify complexity and quality is innovative and can be used for other hard to quantify aspects of data quality in future work.
- The results from the experiments clearly show that the proposed method is indeed selecting important data points (i.e., better than random selection) at least for improving performance on AlpacaEval and MT-Bench.

### Weaknesses
The evaluation in this paper is limited and leaves some important questions unanswered:

- The main evaluation is done in terms of AlpacaEval and MT-Bench alone. Since these are relatively small evaluation sets and it has been shown that GPT-4 evaluation can be biased (Wang et al., 2023; https://arxiv.org/abs/2306.04751), one wonders if the data selection does better than random only because it is aligned with those biases. Including further evaluation, possibly on targeted benchmarks covering abilities like reading comprehension, complex reasoning etc. can be helpful.
- Related to the above point, since human evaluation was done on only 100 instances, it would be helpful to quantify the reliability of this assessment, e.g.: using inter-annotator agreement scores and significance, and perform a larger scale evaluation if needed.

The procedure used for quantifying complexity and quality can be validated and possibly improved further

- Section 2.3 states that ChatGPT is shown multiple samples evolved from the same seed example are shown to ChatGPT at a time for scoring their complexity (and this is possibly true for quality as well). Are these scores comparable across evalved sets from different seed examples? This is necessary because all these data points are used together as training data for training the Llama-based scorer. If they are not comparable, it might help to randomize the sets shown to ChatGPT for scoring.
- Relatedly, it would help to have humans also score data points in terms of complexity and quality and see if the scores correlate with  
ChatGPT's judgments.

### Questions
- Is it possible for the diversity criterion to end up selecting outliers in the datasets? How can this issue be fixed?
- Do you need to use the representations from the Llama-13B model for computing distances as well? Can you use a different (smaller?) model for computing distances than the one you instruction-tune?
- DEITA-6K loses more to the random selection baseline than to the Vicuna model according to the human evaluation results in Table 4. This seems surprising. How does the random selection model perform compared to the Vicuna model in this case?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work shows that complexity, quality, and diversity are all important for data selection in instruction tuning. Based on the studies, it proposes a score-first, diversity-aware approach called DEITA to select the “good” data samples. With their proposed learning-based enhanced data measures, DEITA shows better or on par performance with state-of-the-art LLMs with only 6K training samples.

### Strengths
- The paper provides in-depth controlled studies to show the proposed scoring measurements are better than baselines in terms of complexity and quality.
- With fine-tuned LLaMA-7B models on the 20K Alpaca dataset with the scores from GPT, the measurements can score unseen instructions at a cheap cost.
- The proposed diversity-aware selection method is efficient and easy to implement.
- Clear presentation and easy-to-follow writing.

### Weaknesses
Limited evaluation
- No evaluation result on benchmarks like MMLU and Big-Bench-Hard, which allows verification of commonsense knowledge and reasoning with ground-truth answers. GPT4-based evaluation often includes errors or bias, so not enough.
- Marginal performance improvement. In Table 3, DEITA is worse than Vicuna-13B on AlpacaEval dataset. Also, In Table 4 with human evaluation, Vicuna performs almost similar to DEITA.
- Limited baselines; recent instruction selection works including LIMA and Alpagasus are missing in the evaluation.

### Questions
Why the complexity measurement is obtained from “instruction”, and the quality measurement is obtained from “response”? Is there any intuition of this?

Typo: “large margine” should be“large margin” in the last sentence of the introduction.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the trendy problem of selecting high-quality instructions for fine-tuning pre-trained language models (PLMs). The paper aims to provide an automated pipeline for this selection problem. Following recent works, sample quality is evaluated on three dimensions: complexity, quality, and diversity where this evaluation is conducted by other LMs such as GPT-4. The paper validates the proposed approach with LLaMA-1 and shows that when selecting samples from a larger pool of lower-quality data, the proposed method, DEITA (Data-Efficient Instruction Tuning for Alignment), is able to match the performance of current open-source alignment models with a small fraction of fine-tuning data.

### Strengths
The paper is, in general, an easy read. Its ideas are presented straightforwardly along with nice tables and illustrations.

The problem it investigates is trendy. Quality for each part of the work is generally fine–it is structurally complete, self-contained, and has a reasonable narrative.

### Weaknesses
This paper is "ok" but not particularly enticing. The topic is trendy but the approach is not technically challenging or particularly innovative.

I have recently read a number of papers on this topic of instruction mining with LLaMA/Alpaca–to name a few

- a. ALPAGASUS : TRAINING A BETTER ALPACA WITH FEWER DATA
- b. Instruction Mining: High-Quality Instruction Data Selection for Large Language Models
- c. InstructionGPT-4: A 200-Instruction Paradigm for Fine-Tuning MiniGPT-4 

The technical body of these papers are uncomfortably similar. Combining a number of existing metrics (often in trivial ways) such as quality, diversity, etc. as a new evaluation metric and conducting the evaluations largely with the help of GPTs. And the end goals are also the same–to achieve comparable or better performance with fewer samples. I'm not sure how much "research gap" remains there and how individual works may continue to contribute to that–at least, this concern is still not resolved by this paper.

In terms of quality, the construction of this paper is simple. It does not have many ablation studies or insightful discussions of design choices/novel findings. No additional results or further discussions are provided in the Appendix.

It is an "okay" paper without much particular. Given its position in this apparently overly populated track, I would not be very interested in seeing it at the conference and vote against publishing it.

- Reproducibility: Code, data, model checkpoints, or data selection tools are not provided during the reviewing phase.

- Format: Appendix is not cut from the main paper. The PDF provided for the main paper is this 20-page document.

### Questions
If the authors wish to further develop this work toward publication at a future venue, I suggest the authors to 

1. spend significant effort in discussing the current research landscape and identify a valid (important and essential) research gap that this work will make a substantial and unique contribution to. This is my main concern for this line of work.

2. improve the quality of the paper. If its extent of innovation is capped by the many other papers out there,  this work needs to have a high quality to be a valid contribution. This includes conducting more experiments and ablation studies and discussing design choices and novel findings.

3. improve the technical approach. The current methods documented in this paper do not seem particularly novel compared to existing works and its technical contributions seem capped by the heavy reliance on GPTs. If the authors could design original technical approaches (new metrics, new evaluation methods, novel ways for combining different metrics), the paper could be made much more attractive.

- Appendix should not be submitted under the main paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
