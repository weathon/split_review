---
job_id: ab155ff9-0fde-412d-9783-4f196b5dc4e0
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: v4bQPw4aTW.pdf
paper: Adabon: Adaptive Best-of-$N$ Alignment
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, it studies inference-time alignment, adaptive compute allocation, and evaluation for LM-RM systems, all of which fall under general machine learning, language modeling, optimization, and safety/alignment.

## Minimum Quality
Pass ✅ The paper contains the expected scientific structure, including abstract, introduction, related work, method, experiments, quantitative results, and discussion/limitations. While I have several substantive concerns about correctness details, baselines, and evaluation choices, these do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not detect hidden prompts, instructions targeting automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies adaptive inference-budget allocation for Best-of-$N$ alignment across a batch of prompts. The proposed method, AdaBoN, uses a two-stage procedure: first, it spends a fixed exploration budget per prompt to estimate each prompt’s reward distribution, then it greedily allocates the remaining budget according to estimated marginal gains in expected maximum reward. The paper evaluates the approach on AlpacaEval, HH-RLHF, and PKU-SafeRLHF using 12 LM-RM pairs, and reports improved batch-level win rates over uniform allocation at the same total budget.

## Strengths
The paper tackles a practically relevant and reasonably well-motivated problem. A lot of work on BoN asks “what should $N$ be?”, but much less work asks “where should those samples go?” when a fixed total budget is shared across prompts. That problem formulation is meaningful, especially in the setting emphasized here, namely batched inference with nontrivial per-prompt budgets.

The method itself is simple and easy to understand. The two-stage structure in **Algorithm 2** is appealing from a systems perspective because it preserves parallelism better than more sequential adaptive strategies. I also appreciated that the paper is explicit about the latency motivation on **Page 5**, rather than overselling full adaptivity when the real constraint is wall-clock usability.

The empirical study is broader than many short inference-time alignment papers. In particular, **Table 1** and **Table 2** cover 12 LM-RM combinations on AlpacaEval, and the appendix extends this to two additional datasets. Even if I have reservations about the chosen baselines, the paper does at least attempt to show robustness across models, reward models, and datasets, instead of relying on one cherry-picked pair.

Some of the figures help build intuition. **Figure 1** is useful because it visually supports the central premise that reward distributions differ across prompts and are not all degenerate or identical, which is exactly the heterogeneity the method aims to exploit. Likewise, **Figure 2(a)** makes the batch-to-batch variability visible instead of hiding it behind only mean or median summaries, and **Figure 3** provides an interpretable picture of how gains scale with batch size $K$.

I also think the paper deserves credit for not pretending the gains are universal. The discussion around the weaker Qwen-Armo behavior, together with the skewness analysis in the appendix, suggests the authors did at least investigate when adaptivity is less useful. That kind of diagnosis is often missing in papers of this flavor.

Finally, the concavity observation behind the greedy allocator is conceptually nice. The statement in **Proposition 3.1** captures why allocating according to diminishing returns is reasonable for expected maxima, and it gives a clean justification for the greedy policy, at least when the value vectors are exact.

## Weaknesses
1. **The empirical comparison is too narrow for the paper’s central claim, because the main baseline is basically only uniform allocation.**  
   The whole paper argues that AdaBoN is a practical adaptive alternative for budget allocation, yet in the main paper the comparison is almost entirely against the uniform allocation, plus competition against uniform with larger budgets via EST. That is a weak standard for an ICLR paper making method claims. On **Page 7**, the paper explicitly says it does not compare to *Damani et al. (2024)*, which is described in the related work as the “most closely related work” and in fact studies the same allocation problem. I understand the implementation burden, but “we could not find code” and “it would require many MLPs” is not a satisfying scientific reason to omit the most relevant prior method. If a paper’s central contribution is a new solution to an existing problem, then comparison to the most relevant existing solution is not optional.  
   The appendix introduces a variance-based heuristic baseline in **Tables 8 and 9**, but that baseline is very weak and is not present in the main paper. So as written, the evidence supports “better than uniform” much more than it supports “competitive with prior adaptive allocation methods.”

2. **There is a likely mathematical / implementation error in the KDE bandwidth formula, and this matters because KDE is central to the method.**  
   In **Section 3.1, Page 6**, the paper states Scott’s rule as
   \[
   h = \hat{\sigma} d^{\frac{1}{5}}.
   \]
   For kernel density estimation, Scott’s rule scales like $n^{-1/5}$ in 1D, not $n^{+1/5}$. If the paper literally uses $h=\hat{\sigma} d^{1/5}$, the bandwidth grows with sample size, which is the opposite of the standard rule and would oversmooth more as more exploration data are collected. Since the entire AdaBoN pipeline depends on estimating $\hat D_i$ and then Monte Carlo estimating the value vectors from that estimator, this is not a cosmetic typo. It affects both the methodological description and potentially the empirical validity. At minimum, the authors need to clarify whether the implementation used $d^{-1/5}$ while the text contains a typo, or whether the positive exponent was actually used.

3. **The theory only justifies the greedy allocator for exact value vectors, not for the actual estimated vectors used by the method, and the paper does not quantify the resulting error.**  
   The key optimization claim on **Page 5** is that greedy allocation is optimal when the vectors $V_i$ are monotone and concave, which follows from **Proposition 3.1**. But AdaBoN never has access to exact $V_{i,j}$, it uses Monte Carlo estimates $\hat V_{i,j}$. The paper acknowledges that “the greedy procedure may not be optimal when run on the estimated vectors,” but then moves on without any finite-sample analysis, confidence bounds, or even a monotonicity-preserving projection step. This matters because the entire allocation can be unstable if the estimated marginal increments
   \[
   \hat V_{i,j+1} - \hat V_{i,j}
   \]
   are noisy, especially when many prompts have similar estimated gains. As written, the only theoretical support is for an idealized version of the method, not quite for the actual algorithm evaluated in experiments.

4. **Several notation / algorithm details are sloppy enough to hinder careful verification.**  
   There are small but important inconsistencies. In **Algorithm 1** on **Page 5**, line 3 uses $a_t$ inside
   \[
   i_t \in \arg\max_{i\in[K]} (V_{i,a_t+1} - V_{i,a_t}),
   \]
   even though the allocation vector is denoted by $a$, not $a_t$, and the intended indexing seems to be $a_i$. This is not just a typo in prose, it appears inside the key allocation algorithm. Similarly, the notation for allocations is at times overloaded between fixed allocations and random allocations induced by policy $\mathcal A$, which makes **Section 2.3** more cumbersome than necessary to parse.  
   There is also a proof typo in the appendix, on **Page 15**, where one displayed equation seems to miss an opening parenthesis:
   \[
   \mathbb E[(X - M_{n-1})_{+}]
   \]
   is written inconsistently in one place. Individually these are fixable, but collectively they reduce confidence that the mathematical presentation was checked carefully.

5. **The evaluation metric choice is unusual and obscures practical effect size.**  
   The paper emphasizes BWR in **Equation 3, Page 7**, arguing that raw reward values are only meaningful comparatively. I understand that motivation, but BWR is a somewhat blunt metric. A method can win slightly more than half the time while delivering negligible average gains, or conversely lose slightly more often but deliver larger gains when it wins. The paper does not present the primary optimization objective from **Equation 1** in the main tables, even though the method is explicitly derived to maximize expected cumulative max reward. That omission makes it hard to assess how large the improvement actually is.  
   This issue shows up in **Table 1** and **Table 2(b)**. For example, many medians are around $0.55$ to $0.60$, which indicates a real but modest edge over uniform, but the paper does not tell the reader whether that translates to meaningful reward improvement or just very small stochastic wins. The evaluation would be much stronger if it reported both BWR and normalized reward gain over uniform.

6. **The EST metric is somewhat awkward and may overstate the narrative of “competing with 20\% larger budgets.”**  
   On **Page 7**, EST is defined as
   \[
   S_{\mathcal A}(x_{1:K},B) = \sum_{N=1}^{\infty}\mathrm{BWTR}_{\mathcal A}(x_{1:K},N,B),
   \]
   and in experiments it is truncated at $2B$ on **Page 8**. This is an unusual survival-style summary. While mathematically valid as a derived quantity, it is not very interpretable in the LM alignment setting, and the truncation means it is partly an artifact of the evaluation cap. In **Table 2(a)**, the reported EST values around $150$ are then verbally translated into being competitive with larger per-prompt budgets, but the reader has to do extra work to understand exactly what that means and under what truncation. A direct curve of $\mathrm{BWTR}$ versus competing budget $N$ would have been more transparent.

7. **The paper’s “minimal hyperparameter tuning” claim is overstated.**  
   The paper repeatedly emphasizes that AdaBoN has only one hyperparameter, the exploration budget $d$, and that $d=0.75B$ works well. But that framing sweeps several meaningful design choices under the rug: the KDE family, the bandwidth rule, the Monte Carlo sample size $m=1024$, and the exact generation setup all affect performance. On **Page 8**, $m=1024$ is fixed without any sensitivity analysis. If $\hat V_{i,j}$ estimation is noisy, $m$ is a real hyperparameter, not merely an implementation detail. Similarly, choosing Gaussian KDE is a substantive modeling assumption. So the “single hyperparameter” narrative is too convenient.

8. **The claims about latency and computational efficiency are incomplete because the accounting centers on LM calls but not the full pipeline.**  
   On **Pages 5-6**, the paper argues that AdaBoN “minimizes latency” because only two LM calls need to be made, one for exploration and one after the allocation is computed. That framing ignores several nontrivial costs: reward model evaluations for all explored samples, density estimation, Monte Carlo estimation of all $\hat V_{i,j}$ for all prompts and all $j\in[(B-d)K]$, and the greedy optimization itself. I agree that LM calls dominate in many settings, but the paper makes a fairly strong latency claim without wall-clock measurements or even a rough complexity breakdown. For a method sold partly on practicality, that omission is noticeable.

9. **Some of the experimental design choices weaken external validity.**  
   The main paper fixes one decoding setup, using the “default generation function” from Hugging Face on **Page 8**. But BoN behavior depends materially on decoding temperature and sampling settings. Since the method is specifically about sample allocation under BoN, it would have been useful to know whether the gains persist across decoding regimes, especially regimes that produce more or less diverse reward distributions. Similarly, the paper focuses on batch sizes and budgets where it expects to do well, namely relatively small $K$ and large $B$. That is a defensible scope choice, but it limits generality, especially given that the closest prior work is claimed to target the opposite regime.

10. **The figures support the motivation, but they also expose a gap in the paper’s characterization of when the method should work.**  
    **Figure 1** shows three reward distributions that are indeed smooth and heterogeneous, which supports the KDE idea. But showing three examples is not enough to justify the broad statement on **Page 2** that the reward distributions are “smooth and easy to learn.” The paper later leans on skewness explanations for the Qwen-Armo case, especially in **Figure 2(a)** and the appendix figures, which suggests that distribution shape substantially affects whether adaptivity helps. This is important, but the main paper never turns that observation into a predictive characterization of success or failure. In other words, the figures are suggestive, but the paper stops at post-hoc explanation rather than providing a sharper criterion for when AdaBoN should be preferred.

## Questions
1. In **Section 3.1**, is the bandwidth rule really implemented as
   \[
   h=\hat\sigma d^{1/5},
   \]
   or is this a typo for $h=\hat\sigma d^{-1/5}$? Please answer this very explicitly, because it materially affects both the method description and my confidence in the experiments.

2. Can the authors provide at least one direct comparison, even on a reduced setup, against the method of *Damani et al. (2024)* or another adaptive allocation baseline beyond uniform and VarBoN? Even a partial comparison on one dataset, one LM-RM pair, and a smaller budget would increase confidence substantially.

3. What happens if the estimated vectors $\hat V_i$ are not monotone or concave because of Monte Carlo noise? Did the authors ever observe violations of
   \[
   \hat V_{i,j+1}-\hat V_{i,j} \ge \hat V_{i,j+2}-\hat V_{i,j+1},
   \]
   and if so, did they try isotonic or concavity-enforcing post-processing before greedy allocation?

4. Please report the actual gain in the objective from **Equation 1**, or at least a normalized reward improvement over uniform allocation, in addition to BWR. Right now the paper shows that AdaBoN wins more often, but it is hard to judge by how much.

5. Can the authors provide wall-clock measurements or at least a fuller compute breakdown? The current latency claim focuses on LM parallelization, but the RM scoring and Monte Carlo estimation costs are not quantified.

6. How sensitive are the results to the Monte Carlo sample size $m=1024$ used to estimate $\hat V_{i,j}$? If smaller $m$ performs similarly, that would strengthen the practicality claim; if not, then this is an important hidden tradeoff.

7. Since **Figure 3** suggests gains increase with batch size, can the authors give a more principled explanation of this trend? Is it mainly due to a larger opportunity for cross-prompt reallocation, or due to concentration of the batch-level metric?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper uses public datasets and existing language/reward models for evaluation of inference-time alignment strategies. I did not identify a specific ethics issue requiring separate ethics review based on the content presented in the main paper.

## Soundness Rating
2: fair. The core idea is plausible and supported by experiments, but the missing comparison to the most relevant prior method, the likely bandwidth-formula error in **Section 3.1**, and the gap between the exact-value theory and the estimated-value algorithm keep me from rating technical support more highly.

## Presentation Rating
2: fair. The paper is readable overall, but there are enough notation issues, algorithmic sloppiness, and under-explained metric/design choices that the presentation falls short of what I would consider good.

## Contribution Rating
2: fair. The problem is worthwhile and the method is practical, but the contribution currently feels more like a promising heuristic study than a thoroughly validated ICLR-level advance, especially without stronger baselines and clearer characterization of effect size.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is interesting, the problem is relevant, and the empirical trends are encouraging, but I do not think the current version clears the bar comfortably. The main reasons are the absence of a direct comparison to the closest prior adaptive allocation method, a likely error in the central KDE specification, and evaluation choices that make the practical magnitude of improvement harder to judge than it should be.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the main method, equations, algorithms, figures, and tables, and I am fairly familiar with the surrounding literature on inference-time alignment and adaptive compute allocation.