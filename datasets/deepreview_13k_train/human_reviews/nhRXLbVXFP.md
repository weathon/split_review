# Ordinal Preference Optimization: Aligning Human Preferences via NDCG

- Decision: Accept
- Scores: 6, 3, 3, 6

## Abstract
Aligning Large Language Models (LLMs) with diverse human preferences is a pivotal technique for controlling model behaviors and enhancing generation quality. Reinforcement Learning from Human Feedback (RLHF), Direct Preference Optimization (DPO), and their variants optimize language models by pairwise comparisons. However, when multiple responses are available, these approaches fall short of leveraging the extensive information in the ranking given by the reward models or human feedback. In this work, we propose a novel listwise approach named Ordinal Preference Optimization (OPO), which employs the Normalized Discounted Cumulative Gain (NDCG), a widely-used ranking metric, to better utilize relative proximity within ordinal multiple responses. We develop an end-to-end preference optimization algorithm by approximating NDCG with a differentiable surrogate loss. This approach builds a connection between ranking models in information retrieval and the alignment problem. In aligning multi-response datasets assigned with ordinal rewards, OPO outperforms existing pairwise and listwise approaches on evaluation sets and general benchmarks like AlpacaEval. Moreover, we demonstrate that increasing the pool of negative samples can enhance model performance by reducing the adverse effects of trivial negatives

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a new surrogate objective function for training generative models using reinforcement learning, where the objective function is based on NDCG ranking rewards of multiple candidate answers. The paper argues that strong RL training methods often depend on designing contrastive reward functions, which utilize the comparative values rather than the absolute values of multiple answers for self-normalization and uncertainty quantification purposes. The proposed NDCG objective is an extension of this idea, where the detailed ranking positions for a list of answers are considered at the same time.

To optimize the NDCG objective, the paper further introduces a differentiable Neural Sort operator (Grover et al 2019), where the ranking steps are relaxed into a probabilistic distribution matrix using softmax operators. The paper then compares the proposed Neural-NDCG method with other popular NDCG optimization methods, such as LambdaRank and simple pairwise comparison baselines. The paper shows the generality of the proposed method by fine-tuning medium-scaled LLMs on ListUltraFeedback dataset and evaluating them on AlpacaEval and MT-Bench datasets.

### Strengths
Originality: The paper introduces a new way to train RLHF models by extending pairwise reward functions into list-wise ranking functions. The paper then introduces neural-sort operator to replace the current SOTA LambdaRank method. The introduction of the neural-sort operator looks natural and the intuitions are clear.

Quality: The proposed methods are evaluated on recent models and relevant benchmarks. The experiments and the ablation studies are well-designed. They serve as a good template for researchers setting up similar experiments.

### Weaknesses
It does not seem very clear from the paper, but the proposed RL training steps seem to be offline. According to Eq (2), the learned policies are only fitted on the likelihoods of the pre-generated answers, instead of the self-generated answers. It is unclear to me whether the offline optimization paradigm presents a performance gap when the models are evaluated online or when they generate answers in the real world.

As a minor point, the NeuralSort algorithm (5) could use more discussions. For example, the paper could include more details about the probabilistic P_sort matrix in the numerical examples.

### Questions
Regarding online vs offline RL, can the authors:
* Clarify whether the proposed method is intended for offline or online RL.
* Discuss potential limitations of using an offline approach
* Compare the proposed method to online RL alternatives to verify if potential performance gaps may exist
* Give concrete examples on how the proposed method perform in real-world online generation scenarios.

Regarding NeuralSort details, please:
* Include a step-by-step example of how the probabilistic P_sort matrix is computed in Appendix A
* Clarify the benefits of probabilistic permutations. Will having ties or near-ties allow better characterization of the ranking uncertainties?
* Discuss potential limitations of probabilistic permutations. Will the P_sort matrix lead to miscalibration, where all of the generated matrix may degenerate? For example, having the same [0,1,0,0] rows in the entire matrix?
* Discuss uniqueness of the solutions. Are there other equivalent formulations to achieve neural-sort? Will these equivalent formulations alleviate some of the limitations? In what sense is the proposed algorithm the most obvious choice?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes Ordinal Preference Optimization (OPO), a listwise method that adapts the existing learning-to-rank (LTR) methods to optimize LLMs based on multiple response rankings. By adapting the existing learning-to-rank (LTR) methods such as NeuralNDCG with DPO, OPO can directly optimize under the multi-response datasets.Experiments show the effectiveness of the proposed OPO.

### Strengths
1. The proposed OPO method is straightforward and intuitive.
2. Experiments with various pairwise and listwise baselines demonstrate the effectiveness of OPO.
3. The codes and scripts are provided in the supplementary materials, enhancing the reproducibility of this work.

### Weaknesses
1. The motivation for OPO is not clear. It is only briefly mentioned (e.g., line 53 "which is relatively simplistic") and requires a more detailed comparison with existing listwise approaches to highlight the motivation of the proposed new listwise method. Specifically, the paper should elaborate on the limitations of existing listwise methods when applied to the multi-response ranking scenario in LLMs, and why a direct adaptation of LTR methods is needed. A more thorough discussion of the specific challenges in this context would be beneficial.
2. The proposed OPO directly adapts existing learning-to-rank (LTR) methods (e.g., NeuralNDCG) to optimize DPO with NDCG, lacking novelty. In fact, as listed in this paper, other listwise LTR methods can also applied to the DPO. The paper does not provide a clear justification for why this specific adaptation is superior to other possible adaptations of LTR methods. The choice of NeuralNDCG over other direct NDCG optimization techniques needs further explanation.
3. The paper lacks theoretical analysis and comparative discussion of the proposed OPO method, which would strengthen its contribution and clarify its advantages over existing methods. A theoretical analysis of the convergence properties or generalization bounds of OPO would be valuable. Furthermore, a comparative analysis with other listwise methods in terms of computational complexity and sample efficiency is needed.

### Questions
1. Why was NeuralNDCG chosen as the surrogate loss for optimizing NDCG, rather than other direct NDCG optimization losses?
2. Given the potential sensitivity of the win rate metric with GPT4, was a t-test conducted to assess its significance, and were selection biases (e.g., sensitivity to AB vs. BA results) considered?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes to use a listwise objective for LM alignment when multiple responses for a prompt is available. The objective is an existing one from the IR field. The proposed method is evaluated on datasets such as AlpacaEval and MT-Bench against baselines that focus on objective alternatives with the same backbones.

### Strengths
1. It is good to further study the listwise perspective of the important LLM alignment problem. However, there seem to have some factual misunderstanding of the literature discussed below.

2. The study of diversity of negative samples is interesting and has value. 

3. The paper essentially performs a study of additional listwise objectives for LM alignment. I think this is good to do, though I am not convinced of the significance and the trustworthiness of the empirical results, see below.

### Weaknesses
1. The major issue of this paper is its contribution. There are *wrong* claims such as claiming LiPO to be pairwise approaches, while they are actually listwise - for example, LambdaRank is considered as a *listwise* objective in the information retrieval literature and it is a proxy of NDCG, which the authors avoid discussing. This is because the weights use *listwise* information so they are no longer pairwise. It is even more confusing that LiPO pretty much has the exact same idea (while being public almost a year ago) to optimize NDCG. The paper uses another *existing* surrogate loss to do that. In the IR literature, this surrogate loss is not as acknowledged as the one studied in the LiPO work. The first two major contributions (of out 3) may even be put in the LiPO paper without any inconsistency. 

2. Despite the large overlap with existing work, the paper does not have a convincing argument on why the deployed objective is a better choice, so the experiments are at the risk of cherry-picking. And given extensive work on such topics, the contribution is quite limited to meet the standard of a top-tier ML venue. Note that even if there's a argument specific to the objective, the contribution is still likely limited since the formulation and general objective (e.g., optimizing NDCG) are more important and the loss alternatives are not that different (as studied intensively in the IR literature).

3. Besides the formulation and method, the additional value provided by the paper is also relatively limited. For example, it is still limited to offline alignment (which might be ok itself, the issue is it does not add value based on existing work as discussed above).

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents OPO, a novel listwise approach that leverages the Normalized Discounted Cumulative Gain (NDCG), a widely-used ranking metric in Learning To Rank, to align LLM with human preference. By incorporating a differentiable surrogate loss function, OPO effectively utilizes the ranking information derived from multiple model responses.

### Strengths
- The paper is generally well-organized and clearly written.
- The paper conducts comprehensive experimental with detailed examples, and the implementation code is publicly available.

### Weaknesses
 - Contributions of this paper are quite limited and appear to be incremental. The key technical components, including Neural NDCG objective [1], Sinkhorn scaling [3], and Neural Sort [2], have been previously established in the literature. Sections 3.1 and 3.2 present a reformulation of the established Neural NDCG formulation (Section 4.1 and 4.2).

- Missing discussion on how this work is novel compared to other listwise method, such as LiPO[4]. LiPO uses the DCG weighting scheme, which inherently captures the relative proximity within multiple responses. Additionally, the discussion of current listwise methods in line 53 requires further clarification to better distinguish their differences and respective limitations.

- While the paper claims to establish an explicit connection between LLM alignment and ranking model training, this theoretical connection is inadequately elaborated in the paper. Moreover, similar insights have been previously explored in LiPO's work.


- In traditional learning-to-rank tasks, NDCG serves primarily as an evaluation metric, with standard LTR loss functions only loosely correlated to these evaluation criteria. The use of differentiable NDCG surrogate loss helps bridge this optimization-evaluation gap in ranking tasks. However, LLM is commonly evaluated on open benchmarks rather than ranking metrics, and the paper lacks theoretical justification in two aspects: why NDCG optimization would lead to better preference alignment, and what motivates the choice of NDCG as the optimization objective.

- The primary motivation is that NDCG can better utilize relative proximity within ordinal multiple responses. However, in lines 207-208, the paper does not explain why "the gain function should be proportional to the label" can effectively capture the relative ranking of different responses. Moreover, lines 209-211 indicate that recommendation tasks focus on top-ranked items. This design stems from NDCG's discount function, which is derived from an approximation of human attention decay. However, the paper lacks discussion on whether such a discount function is appropriate for preference optimization tasks. 

- The paper could benefit from comparing different Learning to Rank objectives, such as Neural Sort (which Neural NDCG builds upon) [2], PiRank[5] and other ranking methods.

### Questions
1. In MT-Bench experiments, why the reported results differ from those presented in other papers.

2. In the ablation studies of Neural NDCG, while different gain functions are compared, the paper does not explore the impact of different discount functions.

3. Table 5 suggests that diverse negative samples are more crucial than varied positive samples. However, the performance gain of All Pairs over Single Pair might simply result from increased training data.

### Soundness
2

### Presentation
3

### Contribution
2
