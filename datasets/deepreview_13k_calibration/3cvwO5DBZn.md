# On Speeding Up Language Model Evaluation

- Decision: Accept
- Avg Score: 7.00
- Scores: 10, 6, 6, 6

## Abstract
Developing prompt-based methods with Large Language Models (LLMs) requires making numerous decisions,  which give rise to a combinatorial search problem.
For example, selecting the right pre-trained LLM, prompt, and hyperparameters to attain the best performance for a task typically necessitates evaluating an expoential number of candidates on large validation sets.
This exhaustive evaluation can be time-consuming and costly, as both inference and evaluation of LLM-based approaches are resource-intensive. Worse, a lot of computation is wasted: Many hyper-parameter settings are non-competitive, and many samples from the validation set are highly correlated - providing little or no new information. So, if the goal is to identify the best method, it can be done far more efficiently if the validation samples and methods are selected adaptively.  
In this paper, we propose a novel method to address this  challenge. 
We lean on low-rank matrix factorization to fill in missing evaluations and on multi-armed bandits to sequentially identify the next (method, validation sample)-pair to evaluate. 
We carefully assess the efficacy of our approach on several competitive benchmark problems and show that it can identify the top-performing method using only 5-15\% of the typically needed resources---resulting in a staggering 85-95\%  LLM cost savings.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
The paper proposes two active selection algorithms for evaluation based on the classical approach of estimation of the upper confidence bound. The main aim of the proposed algorithms is to identify the best performing method across a set of validation examples, given a fixed evaluation budget. The budget can be monetary cost or GPU time. The methods to evaluate can be different prompts or hyperparameter settings.

### Strengths
-	The proposed algorithms can be used for a variety of evaluation use cases, not limited to LLMs.
-	The paper provides enough and clear description of relevant concepts on which the proposed solution is built.
-	The paper is very well-written.
-	The proposed approaches show great money and time reduction on large evaluation datasets. 
-	The approach was evaluated on variety of tasks, setups, methods, and was evaluated using a thoughtful evaluation approach.

### Weaknesses
-	Nothing major to report here

-	Line 186: by adaptive selecting --> by adaptively selecting
-	Proof reading is needed to fix typos. 
-	What does a stand for in equation in line 190?
-	I suggest some table/mapping to keep track of the different notions used and their meaning.

### Questions
-	Line 186: by adaptive selecting --> by adaptively selecting
-	Proof reading is needed to fix typos. 
-	What does a stand for in equation in line 190?
-	I suggest some table/mapping to keep track of the different notions used and their meaning.

### Soundness
4

### Presentation
4

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
This paper investigates the evaluation problem of large language models (LLMs) and proposes a UCB-based evaluation method that can identify the optimal LLM strategy for a specific task with a lower budget.

### Strengths
The paper introduces UCB-E and its variant UCB-E-LRF. 

The authors conducted extensive experiments across multiple datasets and performed repeated random seeds, which enhance the stability of the results.

### Weaknesses
 - Some descriptions in the paper are unclear. For instance, Figure 3, which presents key experimental results, lacks a legend, making it difficult to interpret.

- Additionally, the paper does not clearly define the baseline methods used in the experiments. 

- Some results also lack in-depth discussion. For example, Figure 3 shows that UCB-E and UCB-E-LRF perform inconsistently across different datasets. The authors attribute this to varying dataset difficulty; however, when comparing dataset pairs like (GSM8K Models, PIQA Models) and (GSM8K Prompts, PIQA Prompts), the conclusions are contradictory. More detailed explanation and discussion from the authors are needed here.

- In the experimental setup, the authors set the rank r = 1 for UCB-E-LRF. Although the ablation study shows that r=1 achieves the best performance, this choice appears overly low compared to related research. The authors should provide more evidence to demonstrate that this is not due to sampling error or an inadequately small dataset.

### Questions
In the experimental setup, the authors set the rank r = 1or UCB-E-LRF. Although the ablation study shows that r=1 achieves the best performance, this choice appears overly low compared to related research. The authors should provide more evidence to demonstrate that this is not due to sampling error or an inadequately small dataset.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes and extends the well-known multi-armed bandit (UBC) for selection of a best method/setup given a set of method (for example: an LLM, prompt, decoding parameters), a scoring function (for example: exact string matching, BLEU, ROGUE, LLM based annotator) and dataset of examples to evaluate the methods on. This extended multi-arm bandit is referred to as UBC-E. Furthermore, the paper proposes to incorporate a low-rank factorization of the observed scores to enable it to reliably interpolate missing evaluation scores. The low-rank factorization leverages the fact that method-examples are correlated with each other. The whole UBC-E-LRF conserves resources while still guaranteeing confidence that the best method/setup will be chosen.


All this is supported by theoretical proof and discussions, and furthermore shown by empirical experiments on three datasets, and various methods and setups. The UBC-E and UBC-E-LRF are compared with baselines, the top-1 precision and NDCG@10 are used as metrics.

### Strengths
- To the best of my knowledge, this is the first paper to be using the multi-armed bandit for LLM model/setup evaluation.
- The idea is solid, and useful. Especially, with the ever growing number of models, size of models and knobs that you can tweak to improve the performance for a specific/custom task. This framework can substantially reduce resources when practitioners have to choose a best model for their use-case.
- The algorithms are clearly outlined, making the understanding and reproduction easy.
- A big strength is that the experiments are done on multiple datasets, with varying H1. This paints a clear picture of how this framework works in different setups, and which one (UCB-E or UCB-E-LRF) to choose for which setup.
The ablations are extensive: ensemble size, uncertainty scaling factor, warm-up budget, rank, etc.

### Weaknesses
 - In section 3.2, low-rank factorization: “Intuitively, if the method-examples are vert correlated, there should exist….” while I do agree with the intuition, it would be nice to have a citation here. At least the citation from the appendix: “Chen et al., 2020; Cai et al., 2019”.
- Even though the information is in the paper, it requires going back and forth to find it. For example, the figure captions are lacing information that is present elsewhere in the text, or not present at all. Some redundancy in the text for the sake of clarity is always welcome. I added suggestions to improve this in the Question section below.



### Questions
In the whole paper, only one baseline is described: uniformly sample and evaluate T examples, but three baselines are mentioned later on, and shown in the figures. What are the two other baselines? Can they be given some attention in the paper?

I have multiple small suggestions to improve the clarity and readability of the paper:
- In Table 2, the H1 value for each dataset is stated. But there is no explanation of what a higher or lower value means in the caption, or anywhere near where the table is cited. I had to refer to the Corollary 1 where it is mentioned, re-read to figure out what a higher or lower value means, to later find an explanation in section 4.4. 
- In Table 2, the columns are ordered: “Dataset Name”, “Size m x n”, “Method Set”. The size is m x n, m stands for methods, n for data samples. I would either swap the “Dataset Name” and “Method Set” columns, or transform the “Size m x n” column to “Size n x m” to have a natural ordering of the columns and the order of the sizes.
- In Figure 3, there is no legend for the curve colors. In the caption of Figure 4 it is stated that the UCB-E and UBC-E-LRF are blue and red (at least for Figure 4), but there is no mention of the other curves anywhere.
- Figure 3 has the datasets ordered from highest H to lowest, and it is mentioned in 4.4 (2 pages forward) that they are ordered by hardness. There is no mention that they are ordered from hardest to easiest, and that higher H means harder and lower H means easier. It can be deducted from the whole text, but it is not immediately obvious.

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
This paper proposes an adaptive approach that exploits the fact that few samples can identify superior or inferior settings and many evaluations are correlated. It uses multi-armed bandits to identify the next (method, validation sample)-pair and low-rank matrix factorization to fill in missing evaluations.

### Strengths
(1) The studied task is interesting. 
(2) The proposed method seems to be effective in acclerating the evaluation.

### Weaknesses
 (1) The paper seems to be recycled and revised from a longer sumbisison, and many parts (especially figures or tables) are with tiny fonts, which are difficult to read.

(2) Some experimental results are difficult to understand, e.g., Table 3.

(3) Overall, I believe evaluation is quite important, and it often involves a number of influencing factors. What if there exists biases in the test datasets? How the comparison results are consistent with human evaluation, since automatic evaluation may not reflect the real capacities of LLMs?

(4) The related work part is weak, which needs more discussions on evaluation of LLMs.

### Questions
See the weakness

### Soundness
2

### Presentation
2

### Contribution
2
