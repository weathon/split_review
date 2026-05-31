Now I have a thorough understanding of the paper. Let me write the review.

---

## Summary

AdaBoN proposes a prompt-adaptive Best-of-N sampling strategy for inference-time language model alignment. Given a batch of K prompts and a total inference budget BK, AdaBoN runs in two stages: an exploration phase that estimates each prompt's reward distribution using Gaussian KDE, followed by a greedy reallocation of the remaining budget guided by estimated marginal gains. The method is training-free, works with any LM-RM pair, and is latency-conscious by limiting parallelism breaks to just two synchronization points. Empirical evaluation spans 12 LM-RM pairs across AlpacaEval, HH-RLHF, and PKU-SafeRLHF, using 50 prompt batches per configuration.

---

## Strengths

- **Comprehensive empirical validation**: The study covers 12 LM-RM combinations (4 LMs × 3 RMs), 3 datasets, 50 batches of prompts each, and includes ablations over batch size K ∈ {3, 5, 10, 15, 20} and per-prompt budget B ∈ {80, 100, 120, 140, 160}. This is notably thorough for an alignment methods paper, providing strong statistical credibility for the reported Batch Win Rates.

- **Principled algorithm design**: Proposition 3.1 establishes that the expected maximum reward is concave and monotonically increasing in the number of additional samples (for any distribution with finite first moment). This directly justifies the use of the greedy allocation algorithm (Algorithm 1), which is provably optimal under these conditions (citing Federgruen & Groenevelt, 1986). The theoretical grounding is clean and practical.

- **Latency-aware two-stage design**: The restriction to two synchronization stages (exploration and exploitation) is explicitly motivated by parallelization constraints. Fully adaptive policies (bandit-style, one-at-a-time allocation) would serialize the entire inference, making them impractical at test time. This design decision is thoughtfully argued and not found in comparable prior work.

- **Thoughtful evaluation metrics**: The Batch Win Rate (BWR) and Expected Survival Time (EST) are novel metrics well-matched to the setting. BWR avoids interpreting raw RM scores as cardinal values (justified by Bradley-Terry model framing), while EST meaningfully quantifies how much compute AdaBoN "saves" relative to uniform allocation.

- **Practical robustness and minimal tuning**: Results show that d = 0.75B generalizes well across all LM-RM pairs tested. Table 3 in the appendix confirms that switching to the grid-searched optimal d provides only marginal improvement, a meaningful practical strength.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing direct comparison with Damani et al. (2024)**: The most closely related and directly comparable prior work is Damani et al. (2024), which addresses the same inference budget allocation problem. The paper argues this comparison is infeasible because it would require training "216,000 MLPs." However, the calculation appears off: for K=5, B=120, and 12 LM-RM pairs across 3 datasets, the required count per their description (training one MLP per b ∈ [BK] = 600, per LM-RM pair, per dataset) is 600 × 12 × 3 = 21,600 — a factor of 10 smaller than claimed, and plausibly achievable on a compute cluster. Even if the comparison is hard to run at scale, a single shared LM-RM pair and dataset would suffice for a direct comparison. Without this, it is difficult to assess whether AdaBoN's simpler, training-free approach achieves comparable gains.

- **Large exploration fraction limits adaptive gains**: The best-performing setting consistently uses d = 0.75B — spending 75% of the per-prompt budget on exploration. With B = 120, K = 5, this means the greedy stage reallocates only (30)(5) = 150 samples out of 600 total. The paper does not explicitly analyze the tradeoff between estimation quality and room for adaptation: why does such a high exploration fraction consistently win? Is d = 0.75B an artifact of the particular smoothness of these reward distributions, or a principled choice? A more detailed sensitivity and reasoning analysis here would considerably strengthen the contribution.

### Minor

- **Scope limited to real-valued reward models**: The authors acknowledge that Gaussian KDE may not be appropriate for discrete or binary reward signals. Damani et al. (2024) consider exactly these settings (math, coding). Since AdaBoN is presented as a general-purpose approach, this gap in coverage is notable even if the paper is up-front about it.

- **EST capped at 2B**: The EST is estimated by capping the sum in Equation 5 to 2B = 240, which can underestimate the true computational savings for batches where AdaBoN performs especially well. The median EST consistently hovers near 151 out of 240, staying well below the cap — but understanding the tail distribution of ESTs would be informative.

- **BWR gains are modest in absolute terms**: The median BWRs in Table 1 are in the 0.55–0.62 range. While statistically consistent across 50 batches, these are moderate gains relative to the cost of the two-stage framework and the additional complexity vs. uniform BoN. The paper would benefit from a discussion of when the gains are practically significant (e.g., for what downstream task metrics does a BWR of 0.60 over uniform BoN translate to meaningful quality differences?).

### Trivial

- The description of Figure 2's y-axis labels ("Medical, Math, ArXiv") appears to be OCR/parser artifact — those labels do not correspond to the AlpacaEval RMs (Mistral, FsfairX, Armo). This is a parser issue.

---

## Nice-to-Haves

- An oracle allocation experiment (using the true reward distributions, not estimated ones) would help bound how much performance is lost due to KDE estimation error vs. the allocation algorithm itself.
- An ablation comparing KDE against empirical CDF (i.e., sampling directly from collected rewards rather than smoothing) would clarify how much the distributional smoothing in KDE actually contributes.
- A study of the variance of BWR across prompts within a single batch (not just across batches) would clarify whether AdaBoN consistently helps most prompts or is driven by large wins on a subset.

---

## Novel Insights

The central insight — that per-prompt reward distributions are sufficiently smooth to enable effective two-stage adaptive allocation without any auxiliary training — is genuinely useful and empirically validated at meaningful scale. The connection between concavity of the expected maximum (Proposition 3.1) and the greedy optimality of the allocation algorithm is clean and closes a gap in the informal reasoning that underlies most BoN discussions. The two new evaluation metrics (BWR, EST) provide a reusable, semantically grounded framework for comparing inference-time alignment strategies that avoids the pitfall of treating raw RM scores as cardinal utilities.

---

## Suggestions

- Provide a theoretical or empirical analysis of the relationship between exploration fraction d/B and estimation quality vs. adaptive headroom, to justify or motivate d = 0.75B beyond empirical tuning.
- Include at least a simplified comparison with Damani et al. (2024) on one shared LM-RM-dataset combination to situate the empirical gains.
- Report, even informally, what a BWR of 0.60 over uniform BoN means in terms of human preference rates or GPT-4 win rates, to connect to practical alignment goals.

---

## Score and Decision

AdaBoN is a solid, well-executed empirical paper addressing a practically important problem (efficient inference-time compute allocation for alignment). The method is simple, theoretically grounded, and comprehensively evaluated. Its primary weaknesses are the absence of a direct comparison with the closest prior work and the unexplained dominance of an unusually high exploration fraction. The gains are consistent and statistically credible, but moderate in magnitude. The contribution sits comfortably at the top of the borderline-reject range: stronger than average empirical work, but not quite a borderline accept given the missing comparative analysis.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>