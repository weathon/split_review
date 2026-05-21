---
job_id: 40b274e0-04ac-4557-9887-5b10961e780b
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: t5Nd4HiI3E.pdf
paper: From Noisy Traces to Stable Gradients: Bias-Variance Optimized Preference Optimization for Aligning Large Reasoning Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies preference optimization for large reasoning models, with contributions spanning optimization, learning theory, and language model alignment.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related work, method, theory, experiments, quantitative results, and conclusion; despite several technical and experimental weaknesses, it clears the bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided manuscript text.

# Expected Review Outcome:
## Summary
This paper studies preference optimization for large reasoning models under a trace-answer factorization, arguing that the ideal DPO objective should marginalize over latent reasoning traces but that this is intractable in practice. The authors propose BVPO, which mixes a trace-based gradient estimator with an empty-trace estimator via a convex combination, and provide generic bias-variance and SGD analyses for the mixed estimator. Experiments on three DeepSeek-R1-style models report improvements on AlpacaEval 2, Arena-Hard, and several math reasoning benchmarks.

## Strengths
The paper addresses a timely and relevant problem. Preference optimization for reasoning-capable models is indeed different from standard LLM preference tuning because stochastic reasoning traces introduce another source of instability, and the paper articulates this issue clearly in Sections 1 and 3.

The main method is simple and easy to understand. The core idea, mixing a trace-based estimator with an empty-trace estimator in Equation (2), is straightforward enough that it could plausibly be adopted by practitioners without major engineering overhead.

There is some value in the problem formulation. Section 3.2 does a good job of distinguishing the ideal marginal objective $\mathcal{L}_m$ from the practical trace-based proxy $\mathcal{L}_t$, and this helps frame why standard DPO becomes problematic for LRMs.

The empirical results in **Table 1 (Page 8)** are reasonably strong on alignment benchmarks. Across all three models, BVPO beats DPO and SimPO on both Arena-Hard and AlpacaEval 2 in most reported settings, and the gains are not tiny. For example, for R1-Qwen-7B in Thinking mode, BVPO improves AlpacaEval 2 win rate from 18.3 to 26.1 and Arena-Hard from 19.1 to 24.2 relative to DPO, which is a meaningful margin if the setup is controlled fairly.

The auxiliary stochasticity analysis in **Tables 3, 4, and 5 (Pages 17-18)** is useful as motivation. In particular, Table 3 shows substantially larger variance ratios for log-probability and sequence length under Thinking than NoThinking, which is at least directionally consistent with the paper’s narrative that trace sampling injects optimization noise.

The paper is generally readable at the high level. Even though I have several issues with the technical precision, the overall story is easy to follow.

## Weaknesses
1. **The main theoretical selling point is disconnected from the actual algorithm used in experiments.**  
   The core claim in Section 4.2 is that there is an MSE-optimal mixing weight $\alpha^\star$ for combining $g_t$ and $g_e$, with a domination guarantee relative to the two endpoints. However, in practice the paper does not estimate or optimize this $\alpha^\star$. Instead, Appendix C.1 on **Page 18** states plainly that “$\alpha$ for BVPO is set as 0.5 in our experiment.” This creates a serious gap between the theory and the experiments. The paper is not empirically validating the claimed optimal estimator; it is validating one fixed heuristic interpolation. That matters because the paper repeatedly frames BVPO as “bias-variance optimized,” but the optimization of the bias-variance trade-off is not actually implemented in the reported training pipeline. At minimum, I would expect either:  
   (i) a principled estimator of $\alpha^\star$,  
   (ii) an adaptive schedule tied to the theory, or  
   (iii) a sensitivity study showing that $\alpha=0.5$ is near-optimal across settings.

2. **Theorem 1 is mathematically correct but much weaker than the paper’s rhetoric suggests.**  
   On **Page 5**, Theorem 1 states that, conditional on fixed data and viewing only trace sampling as random,  
   $\mathrm{Var}_{r^\pm}(g_c \mid \cdot)=\alpha^2 \mathrm{Var}_{r^\pm}(g_t \mid \cdot)$.  
   This is basically immediate once $g_e$ is deterministic with respect to trace sampling. In other words, the theorem proves a conditional variance shrinkage result that is almost tautological, because replacing part of a random estimator by a constant with respect to the chosen randomness will of course reduce variance under that same conditioning. The issue is not that the statement is false, it is that the paper presents it as a substantial theoretical guarantee when it does not address the full stochasticity of training, including data sampling and the bias induced by the empty-trace estimator. This makes the result much less informative than the surrounding discussion implies.

3. **There is a notable notation / formulation error in the convergence section, which undermines confidence in the math.**  
   On **Page 7**, the paper writes the adaptive estimator as  
   $g_c(\alpha_k,\theta_k)=\alpha_k g_t(\theta_k)+(1-\alpha_k)g_c(\theta_k)$.  
   This is almost surely a mistake, since the combined estimator should mix $g_t$ and $g_e$, not $g_t$ and itself. If taken literally, this equation is self-referential and wrong. Given that Section 4 is one of the paper’s main pillars, this kind of error matters. It is not a tiny typo buried in an appendix, it appears right in the main convergence argument, and it makes the exposition look insufficiently checked.

4. **Theorem 4 is of limited practical relevance because its key condition is unverifiable and mismatched to the actual optimizer.**  
   Theorem 4 on **Page 7** shows equivalence between minimizing per-step convergence error and minimizing conditional MSE only when $\eta L = 1$. But the experiments use AdamW with cosine decay and warmup, per **Page 18**, not constant-step SGD with known smoothness constant $L$. The paper never argues that $\eta L \approx 1$ in practice, nor could it realistically verify that for these large models. So the theorem is mathematically okay as a stylized statement, but its algorithmic relevance to the actual training recipe is weak. The paper overstates the connection between the theory and the practical method.

5. **The empirical evaluation is missing key ablations needed to support the causal claim that the gains come from bias-variance trade-off optimization.**  
   The experimental section reports final benchmark numbers, but does not include the diagnostics needed to support the paper’s mechanism claim. Concretely missing are:  
   - an $\alpha$ sweep,  
   - a pure empty-trace baseline corresponding to $\alpha=0$,  
   - direct measurements of gradient variance or gradient norm stability during training,  
   - multiple random seeds / error bars,  
   - comparisons to stronger variance-reduction alternatives such as multiple-trace Monte Carlo averaging.  
   This omission matters because without such ablations, **Table 1 (Page 8)** only shows that one mixed objective outperforms DPO and SimPO under one setup; it does not show that the improvement is specifically due to the theorized bias-variance mechanism rather than data mixing, regularization, or an idiosyncratic prompting effect from the empty-trace template.

6. **The paper’s “human preference alignment” framing is overstated relative to the actual supervision source.**  
   In Section 5.1 on **Page 8**, preferences are produced by sampling five model responses and ranking them using the ArmoRM reward model, not human annotators. That is a perfectly reasonable experimental shortcut, but it weakens the repeated framing around “human preferences.” The paper should be more precise and say this is preference optimization using model-scored synthetic preferences. Why this matters: the behavior of BVPO under reward-model-generated labels may differ from behavior under genuine human pairwise feedback, especially when the method explicitly changes whether reasoning traces are generated.

7. **There are fairness issues in the training budget / data construction that make the baseline comparison less clean than it should be.**  
   Section 3.3 and Appendix C.3 indicate that the method constructs both $\mathcal{D}_t$ and $\mathcal{D}_e$, one with free-form trace generation and one with trace suppression. It is not fully clear whether BVPO effectively sees more diverse supervision or more sampling effort than DPO/SimPO, or how the total compute/data budget is normalized. Since BVPO combines losses from two datasets while the baselines appear to use a single preference dataset, the comparison may not be apples-to-apples. This is particularly important because a simple increase in response diversity or training signal could explain part of the gain.

8. **The literature positioning is incomplete for a paper making strong claims about preference optimization for reasoning traces.**  
   The Related Work section focuses on standard DPO-style alignment and general LRM papers, but misses several relevant directions on reasoning-trace or step-wise preference optimization. In particular, methods such as Step-DPO, PORT, and TPO are directly relevant because they also adapt preference optimization to long-chain or structured reasoning, rather than standard final-answer-only DPO. This omission weakens the paper’s novelty positioning. The contribution here may still be useful, but the paper currently presents the space of alternatives too narrowly.

9. **Some empirical claims are stronger than the evidence shown in the tables.**  
   The paper says BVPO “does not degrade, and in fact improves reasoning,” but **Table 2 (Page 9)** is more mixed than the prose suggests. For the 8B model, BVPO improves the average from 74.7 to 76.1, which is good, but it is lower than DPO on MATH-500 (96.8 vs. 97.6) and lower than both base and DPO on Minerva (46.7 vs. 47.1). For the 7B model, gains over DPO are modest on several tasks. Without variance estimates or repeated runs, the claim that reasoning is “substantially improved” feels too strong. The average improvements are positive, but the per-benchmark pattern is not uniformly convincing.

10. **The main paper has no architecture or pipeline figure, which hurts clarity for a method paper aimed at a broad audience.**  
   This is not a fatal flaw, but it is surprising that a paper built around two data-construction pipelines, two estimators, and two inference modes (Thinking / NoThinking) includes no schematic in the main text. A simple diagram contrasting $\mathcal{L}_m$, $\mathcal{L}_t$, $\mathcal{L}_e$, and the mixed estimator would have made Sections 3 and 5 substantially easier to parse.

11. **There are small but concerning exposition issues in the proofs and theorem statements.**  
   For example, the proof of Theorem 1 in Appendix A.1 contains an incorrect concluding line on **Page 14**, where the text says  
   $\mathrm{Var}_{r^\pm}(g_e \mid x,y^\pm,y^{\prime\pm}) \le \mathrm{Var}_{r^\pm}(g_t \mid x,y^\pm)$,  
   even though the theorem is about $g_c$, not $g_e$. This looks like a copy-editing error, but together with the Section 4.3 issue noted above, it reinforces the impression that the theory section was not polished carefully enough.

## Questions
1. The biggest question for me is the role of $\alpha$. Since the theory in **Theorem 2 (Page 6)** is centered on the MSE-optimal $\alpha^\star$, why is the experimental method fixed to $\alpha=0.5$ for all settings, per **Appendix C.1 (Page 18)**? Could the authors provide either a practical estimator of $\alpha^\star$ or at least a sweep over $\alpha \in \{0, 0.25, 0.5, 0.75, 1\}$ on one or two representative models?

2. Please clarify whether BVPO uses the same total number of sampled responses, preference pairs, and optimization steps as DPO and SimPO. If $\mathcal{D}_t$ and $\mathcal{D}_e$ together effectively provide more supervision or more compute, then the comparison in **Table 1** may not be controlled.

3. Can the authors include a pure empty-trace baseline, namely optimizing only $\mathcal{L}_e$ or equivalently $\alpha=0$? This baseline is essential for evaluating the actual value of the mixture, especially because Theorem 2 is fundamentally about comparing the mixture to both endpoints.

4. Can the authors provide direct evidence that BVPO stabilizes optimization in the claimed way, for example gradient variance, gradient norm dispersion, loss variance across minibatches, or training curve variance across seeds? Right now **Tables 3-5** motivate the idea indirectly via log-probability and length statistics, but they do not show the training gradients themselves.

5. The convergence analysis on **Page 7** seems to contain a likely error in the definition  
   $g_c(\alpha_k,\theta_k)=\alpha_k g_t(\theta_k)+(1-\alpha_k)g_c(\theta_k)$.  
   Should this be $g_e(\theta_k)$ in the second term? Please correct and confirm whether any downstream statements depend on this typo.

6. The paper evaluates on reward-model-ranked preferences, not human annotations. Do the authors have any evidence that the same improvement holds on a dataset with genuine human preference labels, or at least can they discuss the limitations of extrapolating from ArmoRM-generated rankings to human alignment?

7. For **Table 2**, please provide standard deviations or multi-seed results. Several gains over DPO are small, and some benchmarks worsen, so it is hard to know which differences are robust.

8. The related work section should discuss prior efforts on step-wise or trace-level preference optimization more directly. I would encourage the authors to clarify how BVPO differs conceptually and empirically from methods that exploit reasoning traces more explicitly rather than suppressing them part of the time.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond ordinary caveats for LLM alignment work. The paper does not raise a distinct ethics issue that requires specialized review based on the information in the main text.

## Soundness Rating
2: fair. The core idea is plausible and the empirical improvements are interesting, but the theory-to-method gap, missing ablations, and mathematical/expository issues reduce confidence that the central claims are fully supported.

## Presentation Rating
2: fair. The paper is readable overall, but the theoretical section contains notation mistakes and the lack of a main-paper diagram makes the method and data flow harder to parse than necessary.

## Contribution Rating
2: fair. The problem is important and the empirical results are promising, but the method is quite simple, the novelty positioning is incomplete, and the paper does not yet convincingly establish that its main claimed mechanism is what drives the gains.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper targets an important problem and shows promising empirical results, but in its current form the evidence is not tight enough for a positive recommendation. The main reasons are the weak connection between the “optimal” theory and the implemented algorithm, missing ablations around $\alpha$ and variance reduction, and several nontrivial technical inconsistencies in the theory section.

## Reviewer Confidence
4: confident. I am familiar with preference optimization and LLM alignment, and I checked the main mathematical claims and experimental tables carefully, though I did not verify every appendix derivation line by line.