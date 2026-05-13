# MAMBA STATE-SPACE MODELS ARE LYAPUNOV-STABLE LEARNERS

- Decision: Reject
- Scores: 5, 6, 3

## Abstract
Mamba~\cite{gu2023mamba, daotransformers} state-space models (SSMs) were recently shown to outperform state-of-the-art (SOTA) Transformer large language models (LLMs) across various tasks.  Despite subsequent widespread adaptation, little work has focused on Mamba LLMs' amenability for fine-tuning frameworks ubiquitously used for Transformer-based LLMs, e.g., mixed-precision fine-tuning (MPFT) and parameter-efficient fine-tuning (PEFT).  For the former, it currently remains an open question whether Mamba's recurrent dynamics are robust to small input changes, such as those encountered during MPFT.  Using dynamical systems theory (in particular, Lyapunov exponents), we answer this question in the affirmative.  We empirically validate this result through several experiments, showing that Mamba SSMs are significantly more stable to changes introduced by mixed-precision than comparable Transformers, even when both MPFT and PEFT are combined.  For PEFT, we show how targeting specific memory buffers in Mamba's customized CUDA kernels for low-rank adaptation regularizes SSM parameters, thus providing both parameter efficient learning and computational savings. 
Finally, with both MPFT and PEFT enabled, we explore the impact of instruction tuning Mamba SSMs for in-context learning (ICL) on \emph{natural language tasks}.  While pretrained Mamba and Mamba-2 models only achieve 38\% and 82\% (respectively) of the ICL improvements of comparable Transformer-based LLMs, we show that instruction tuning allows Mamba models to narrow this gap to 81\% and Mamba-2 models to skyrocket over this gap to 132\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to address a noticeable gap in research concerning the amenability of the Mamba model to popular fine-tuning frameworks such as PEFT and MPFT. Utilizing theoretical insights from dynamical systems, the paper demonstrates that minor input variations within the SSM layer of either model do not lead to outputs that deviate exponentially. This theoretical assertion is further validated by empirical experiments.

### Strengths
1. The paper is well-written and easy to follow.
2. The paper provides a theoretical analysis to support experimental performance.
3. Comprehensive experiments compare the Mamba model with Transformer-based models across different scenarios.

### Weaknesses
Though the theoretical analysis of this paper is really solid, since most researchers nowadays use MPFT and PEFT for Mamba, the contribution of this paper may be limited. It may be better if some weaknesses about MPFT and PEFT for Mamba are figured out and then optimized accordingly.

### Questions
1. The introduction could be improved by adding a summary of contributions to provide clearer insight into the paper's impact and contribution.
2. Is it appropriate to set the same learning rate for different models (e.g. Mamba and Pythia) when comparing training stability? Whether it is possible that a better-tuned Transformer model could demonstrate enhanced stability and performance, suggesting that the comparison might benefit from adjustments in learning rate settings. Conducting an ablation study or sensitivity analysis on the learning rates for different models maybe can help.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- The authors work to demonstrate that the Mamba SSM is robust to small input perturbations during training, meaning that Mamba is compatible with mixed-precision fine-tuning (MPFT) and parameter-efficient fine-tuning (PEFT). The authors include both theoretical and empirical evidence for this finding.
- Theory results are in section 3, using dynamical systems theory (Lyapunov exponents) to demonstrate that Mamba’s recurrent dynamics are robust to small input changes
- Section 5’s empirical results contain the following experiments (this list defines the numbers which I’ll use to refer to experiments later):
  1. Main results: divergence in accuracy between FP32 and FP16 or BF16 inference, showing that the accuracy divergence for Mamba is roughly similar to that for pythia and OLMo
  2. Non-divergent mamba fine-tuning: divergence in MMLU accuracy compared to full-precision for FP16 or BF16 models fine-tuned fully, or using LoRA on all or a subset of linear layers. Shows that divergence for Mamba is generally less than similar-size transformers.
  3. Hardware throughput and memory-utilization improvements: Average tokens-per-second and maximum memory-per-token for mamba of varying sizes, using FP32 full fine-tuning, or FP16/BF16 LoRA on all or a subset of linear layers. Shows that any form of PEFT is faster and less memory-intensive than the FP32 full fine-tuning
  4. Instruction tuning’s impact on Mamba ICL for natural language tasks: authors claim that instruction tuning narrows the ICL gap between Mamba and Pythia
  5. ICL as an emergent ability of Mamba SSMs: compares ICL performance for Mambas and several transformer models of varying sizes

### Strengths
- The paper addresses a very important problem that, until now, has helped to prevent the wider use of SSMs: training resources for an SSM have been greater than a similarly-sized transformer, because the transformer has been known to be compatible with efficient fine-tuning techniques. Addressing this disparity will help more people to consider working with SSMs, as their computational requirements will suddenly be within reach
- The combination of both theory and empirical results is quite persuasive and is convincing that Mamba is indeed compatible with MPFT/PEFT
- Theoretical results are simple, elegant and important. The proofs in the appendix are easy to follow and look solid.
- Care has been put into the experimental setup, for instance everything being trained using the same batch size in the main results

### Weaknesses
 - My most major critique is that there aren’t any error bars or sense of the spread/randomness in the empirical results, especially for experiment 2 / figure 1, experiment 4 / figure 3 for the fine-tuned models and experiment 5 / figure 4 for the fine-tuned models.
-  My second biggest critique is that each experiment is only performed with one dataset (MMLU, fine-tuning with Alpaca for fine-tuning experiments). Including more than one dataset or task would strengthen the claims you’re drawing from the empirical evaluations. Experiment 5 includes more datasets, but the results for all datasets are averaged together and readers can’t consider their performances separately
- The graphs are nice in figures 1-4, but it would also be helpful to include the actual numbers in tables in the appendix
- The paper seems to have a lot of extra contextualization in it, taking up room which could be devoted to more detailed empirical analysis. In particular, section 2 background and section 5 related work seem to just both be disjoint related work sections. Usually I would consider the “background” section to be merely preliminary information and definition of symbols that are necessary to understand the rest of the paper, like a statement of the SSM equations and formal definition of Lyapunov exponent. Then, related work would be a longer section detailing, well, related work. Just as an example for comparison, you can see this differentiation in roles between background and related work in this paper’s sections 2 and 3 here: https://arxiv.org/pdf/2409.00717 Contextualization/related work is important to include, but I would consider prioritizing and moving at least some of it to appendix to include more empirical results
- Some of the number references seem to be wrong:
  - Line 345, “Figure 5” seems to actually be referring to Figure 1
  - Line 379, “Figure 5” seems to refer to Figure 2 (did you maybe put your \label{} command for the figures in the wrong spot inside your figures’ code blocks?)
  - Appendix theorem 3 corresponds to main paper theorem 2.

Overall, I'm setting my rating to 6 due to the significance of the theoretical results. However, I would appreciate more detail to the empirical evaluations as I mention above.

### Questions
Why did you choose to work with different sets of transformer models in the main results versus the other experiments? For instance, you give results for OLMo on the first experiment (Table 1) but not second, and results for OpenELM in all experiments but the first one.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies Mamba, a state-space model (SSM) that has previously been introduced as an efficient alternative to Transformers. The authors analyze Mamba's stability in mixed-precision and parameter-efficient fine-tuning by applying Lyapunov exponents, theoretically and empirically confirming its resilience against input perturbations. Experiments show that Mamba maintains stability better than comparable Transformers under mixed precision and achieves notable memory and computation efficiency. Additionally, instruction tuning enhances Mamba's in-context learning, suggesting that SSMs can approach or surpass Transformer models in certain few-shot tasks.

### Strengths
This work provides promising evidence that fine-tuning Mamba on instruction-tuning data can improve its in-context learning abilities.

### Weaknesses
 - Line 51:  For some training framework it does not keep master weight in fp32 which problematic for Mamba. But Mamba was still trained with mixed precision using AMP.

- Theory 1 seems shallow: Isn't Lemma 1 trivial to derive? \( dx_{t+1}/dx_t \) directly represents the decay rate, which must be \(\leq 1\) to prevent exponential growth in cumulative products. This insight is obvious for any recurrent model, making Theorem 1’s assertion about exponential decay rather redundant.

- Theory 2 seems unnecessary: It’s clear that concatenating multiple weight matrices with LoRA applied to the larger matrix creates dependencies. However, there's no practical advantage demonstrated here, nor is there an empirical basis for this approach.

- Line 274: Why use MMLU as a proxy metric? For models at this scale, MMLU scores are generally around random (i.e., ~25%), leading to limited interpretability. Additionally, only the differential score is provided, without the original MMLU results, which weakens MMLU’s reliability as a metric in this context.

- Instruction tuning experiments: Pythia feels like a weak baseline. And is it plausible to claim Mamba has an “emergent ability” (line 439) for in-context learning after instruction tuning, given SSMs' inherent limitations, as noted in [1,2]? Figure 3 also shows a performance drop for Mamba2 as shot count rises, likely due to state-space models’ well-known difficulties with long-sequence processing and in-context learning.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2
