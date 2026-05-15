Here is the consolidated review.

## Summary

This paper presents LogicLLaMA, a fine-tuned LLaMA-7B model for translating natural language to first-order logic (NL-FOL). The authors release MALLS, a dataset of 34K GPT-4-generated NL-FOL pairs, and propose a two-stage training pipeline: (1) supervised fine-tuning (SFT) on synthetically perturbed FOL rules with chain-of-thought corrections, followed by (2) PPO-based reinforcement learning using a programmatic logical equivalence (LE) score as reward. The key empirical result is that LogicLLaMA in "RLHF CoT correction" mode achieves 0.849 LE on FOLIO, comparable to GPT-4 5-shot at 0.855, while using a 7B model that can be deployed locally at lower cost.

## Strengths

- **A large, diverse NL-FOL dataset (MALLS) that addresses a genuine data scarcity problem.** MALLS contains 34K pairs — a 17× increase over FOLIO (2K) and 3× over LogicNLI (12K) — with much larger vocabulary (22.7K vs. 5.1K FOLIO, 2.1K LogicNLI) and richer logical structure (avg. 4.6 literals vs. 2.1/2.8). The dynamic prompting pipeline with n-gram frequency tracking and predicate breakdown prompting is a thoughtful methodology for generating diverse silver data.

- **Demonstration that a 7B model can match GPT-4 on FOLIO.** The RLHF CoT correction achieves 0.849 LE vs. GPT-4 5-shot 0.855 on FOLIO, while outperforming all GPT-3.5 variants. This is a practically useful result: it shows a local 7B model correcting GPT-3.5's output can approach GPT-4-level translation quality at significantly lower API cost (the paper notes GPT-3.5 costs $0.002/1K tokens vs. GPT-4 at $0.06/1K for completion).

- **Synthetic perturbation approach for generating CoT training data is clever and well-executed.** The three perturbation types (label change, insert, delete) with controlled AST manipulation produce 150K training examples with ground-truth correction steps. The inclusion of negative samples (10–20% "no changes needed") to penalize over-correction is a pragmatic design choice.

- **Binned analysis (Figure 4) shows CoT correction helps most on the hardest examples.** The analysis groups samples by initial GPT-3.5 score and reveals that RLHF CoT correction yields largest gains on low-scoring samples, while naive correction mainly helps mid-range examples. This provides useful insight into where the approach adds value.

## Weaknesses

### Fatal
None.

### Major

1. **The claimed "RLHF" label is misleading and the paper overstates the novelty of the training framework.**  
   The reward is a deterministic programmatic function (weighted LE + BLEU), not a model learned from human judgments. The paper acknowledges this (line 287: "similar to the RLHF proposed in InstructGPT with the only difference being the reward model... a logical equivalence solver instead of a language model"), yet the abstract and introduction repeatedly claim a "novel SFT+RLHF framework." This is standard RL with a programmatic reward — a useful engineering choice but not a methodological contribution on par with InstructGPT-style RLHF. The framing inflates the claimed novelty.

2. **No ablation isolating the effect of RL from the change in training data distribution.**  
   The SFT CoT model (0.730 LE on FOLIO) is trained on synthetic perturbations and evaluated on test data; the RLHF CoT model (0.849 LE) is further trained on real GPT-3.5 outputs from the FOLIO training set. The improvement from 0.730 to 0.849 could stem from (a) the RL training signal, (b) exposure to real GPT-3.5 error patterns during training (a distribution shift), or (c) both. Without an ablation that trains SFT on real GPT-3.5 outputs (without RL), the contribution of PPO itself is unquantified. This undermines the claim that RLHF is responsible for the gain.

3. **The LE evaluation metric is not validated against any gold standard.**  
   The LE score uses greedy binding of literals and dummy-input filling — reasonable approximations, but the paper provides no analysis of whether LE scores correlate with human judgment of logical equivalence or with an automated theorem prover. Since LE is used both as the primary evaluation metric and as the reward in RL training, its reliability for both purposes is unknown. A small-scale validation study (e.g., 100–200 samples checked against an ATP or human annotators) would substantially strengthen confidence in all quantitative results.

### Minor

4. **No statistical significance or confidence intervals reported.**  
   All results are point estimates. With a 2K-sample benchmark (FOLIO), the gap between LogicLLaMA (0.849 LE) and GPT-4 (0.855 LE) — a difference of 0.006 — could easily be within noise. Similarly, differences between ablation conditions lack error bars.

5. **Missing PPO implementation details.**  
   The paper states it updates model parameters "via PPO" (line 302) but does not report the number of PPO epochs, KL penalty coefficient, reward normalization scheme, value function architecture, or number of experience tuples collected per update. These details are needed for reproducibility.

6. **No explicit comparison between the distribution of synthetic perturbations and real GPT-3.5 errors.**  
   The paper asserts that synthetic perturbations "will already cover a wide range of the actual GPT-3.5 outputs" (line 261) and provides binned performance analysis, but never directly analyzes whether GPT-3.5's errors (e.g., missing quantifiers, wrong variable binding, incorrect operator choice) align with the perturbation types. This makes it difficult to judge whether the SFT stage is teaching the right correction patterns.

7. **The training set includes 1K LogicNLI training pairs, partially confounding the LogicNLI evaluation.**  
   While the test set of LogicNLI is held out, including training-set pairs from the same synthetic template means the near-perfect scores on LogicNLI (0.978 LE for RLHF CoT) may partly reflect template familiarity rather than genuine generalization.

8. **No failure case analysis.**  
   The paper shows positive correction examples (Figure 5) but does not analyze cases where correction degrades the FOL. The SFT/RLHF models have seen negative examples to discourage over-correction, yet the paper reports no statistics on how often the model makes things worse.

### Trivial

9. The abstract claims LogicLLaMA achieves "similar performance as GPT-4" when the gap is 0.006 LE on one benchmark with no significance test. The language slightly overstates the result.

## Nice-to-Haves

- **Ablation of the mixing ratio ω** (currently fixed at 0.7). A sensitivity analysis showing how varying ω affects the trade-off between logical equivalence and surface-form similarity would justify the choice.
- **Analysis of iterative correction behavior**: average number of iterations, variance, and how often the model terminates with "no changes needed" vs. hitting the token limit.
- **Evaluation on additional NL-FOL benchmarks** (e.g., text2log, RuleTaker) to test generalization beyond FOLIO/LogicNLI.
- **Training a direct translation model on MALLS + FOLIO combined** and comparing to a model trained on gold data only, to measure the marginal benefit of the silver dataset.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about table legend duplication and column misalignment.** This is a formatting artifact from PDF extraction; the original submission does not have this issue. (Hard rule: remove formatting/style nitpicks.)
- **Claim that the paper "does not mention or compare to any prior neural NL-FOL translation work (e.g., Hahn et al. 2022, text2log)."** The paper cites both `hahn2022formal` and `levkovskyi2021generating` (text2log) in the related work section. The criticism is factually wrong. (Hard rule: remove factually wrong criticisms.)
- **Claim that the "RLHF" label makes the paper's "claimed novelty collapse."** The paper explicitly states the difference from standard RLHF (line 287). The novelty claim is modestly overstated (kept as a major weakness above) but does not "collapse" — the SFT+RL framework with programmatic FOL reward is still a useful contribution. (Soft rule: weaken, not remove — but I kept the core criticism as a major weakness above rather than removing it.)
- **Strength Finder's claim that the LE metric is "a principled alternative."** The LE metric has not been validated against any gold standard, so calling it "principled" is unsupported and conflicts with verified weakness #3. Moved here.

## Novel Insights

A notable finding that emerges from the binned analysis (Figure 4) is that chain-of-thought correction and naive correction operate at different regimes of "difficulty": naive correction mainly helps mid-range samples, while RLHF CoT correction provides substantial gains on the hardest examples where GPT-3.5 performs worst. This suggests the CoT decomposition is specifically beneficial when the initial error is large and multi-step repair is needed, as opposed to local adjustments. However, this observation comes from the paper itself and does not constitute an insight beyond its own analysis.

## Suggestions

1. **Add an ablation** comparing SFT on real GPT-3.5 outputs (without RL) vs. RLHF on the same data to isolate the contribution of PPO.
2. **Provide a small-scale validation of the LE metric** (e.g., correlation with ATP-based equivalence checking on 100–200 FOLIO samples) and report whether the greedy binding succeeds in finding correct literal correspondences.
3. **Report confidence intervals or bootstrap estimates** for all main results.
4. **Include PPO hyperparameters** (KL penalty, epochs, reward normalization) in the training settings.
5. **Add a failure case analysis** with examples where correction degrades the FOL, and report the distribution of correction iterations.

## Score and Decision

The paper makes a real practical contribution: a useful dataset (MALLS), a clever synthetic-perturbation training strategy, and a cleaned-up 7B model that matches GPT-4 on FOLIO at lower cost. However, the core claim about the RLHF framework is overstated (the "human feedback" is a programmatic reward, and the contribution of RL vs. training data distribution is not isolated), and the evaluation metric (LE) is unvalidated as a measure of logical equivalence. These weaknesses are substantive but not fatal — they can be addressed with additional ablations and analysis. The paper would benefit from more rigorous experimental validation before acceptance.

**Score: 6.0** — A solid empirical paper with a useful dataset and promising method, but the evaluation rigor and framing need improvement before it is fully convincing.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>