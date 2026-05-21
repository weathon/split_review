---
job_id: 0d171b8b-8cc3-478d-b435-3dba498f00bd
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 0TmVqOpBbK.pdf
paper: Scaling Laws Meet Model Architecture: Toward Inference-Efficient LLMs
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on scaling laws, transformer architecture design, and inference efficiency for language models, all of which fall under general machine learning, language representation learning, and large-scale learning systems.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including an abstract, introduction, related work, methodology, experiments, quantitative results, limitations, and conclusion; it also presents substantial empirical evidence through more than 200 trained models and explicit equations/algorithms. While I have technical and methodological criticisms, they do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies how transformer architectural choices, specifically hidden size, MLP-to-attention parameter ratio, and grouped-query attention, affect the trade-off between accuracy and inference efficiency in decoder-only LLMs under fixed parameter and token budgets. The authors propose a conditional, architecture-aware extension of Chinchilla-style scaling laws, fit it using more than 200 trained models from 80M to 3B parameters, and use it to search for architectures that improve throughput while maintaining or improving accuracy relative to LLaMA-3.2-style baselines.

## Strengths
1. The paper targets a real and underexplored question: how to jointly reason about pretraining loss and serving efficiency, not just about training-optimal scaling. That framing is practically meaningful, especially because many scaling-law papers stop at training loss or training compute and leave architecture design for deployment almost untouched.

2. The empirical effort is substantial. Training over 200 models across multiple parameter scales is nontrivial, and the paper does more than present a couple of cherry-picked architecture swaps. The progression from 80M, 145M, 297M to 1B and then 3B gives the work more credibility than a purely anecdotal architecture paper.

3. The controlled ablations around hidden size and MLP-to-attention ratio are useful. In particular, **Figure 3** on Page 4 gives a clear operational message: under fixed parameter budget, larger hidden size and larger MLP-to-attention ratio can improve throughput across batch sizes. This is one of the stronger parts of the paper because it directly connects architectural knobs to measurable serving outcomes rather than relying on FLOPs-only proxies.

4. The paper does a good job motivating why “parameter count alone” is not enough for inference efficiency. **Figure 2** on Page 2 is a simple but effective counterexample, showing that a 1.5B model can outperform a 0.6B model in throughput due to architecture choices. That figure supports the paper’s central thesis better than several paragraphs of prose would.

5. The conditional scaling-law idea is practically appealing. Even if the functional form is somewhat heuristic, the paper makes a serious attempt to couple architecture with loss prediction in a lightweight way. I appreciated that the authors test progressive extrapolation rather than only fitting and evaluating on the same scale.

6. The predictive evaluation is reasonably convincing within the studied regime. **Figure 6** on Page 7 shows predicted versus actual losses for held-out larger scales, and the reported low MSE and high Spearman correlation indicate that the law is at least ranking architectures sensibly. For an architecture search tool, ranking quality matters a lot.

7. The large-scale validation is meaningful. **Table 1** on Page 8 is important because it moves beyond fit quality and reports actual trained 1B and 3B models. Panda-1B improves average downstream accuracy from 54.9 to 57.0 while also lowering training loss, and Surefire models improve throughput materially. This is stronger evidence than just showing fitted contours.

8. The search formulation in Eq. (4) is simple and easy to understand. I also like that the authors are explicit that inference efficiency is hardware- and framework-dependent, rather than pretending a purely analytic objective is enough.

9. Presentation is generally solid. The main story is easy to follow, and the paper is organized around a sensible progression: inference ablations, loss trends, scaling law, search, then validation.

## Weaknesses
1. The core scaling law is empirically useful, but mathematically under-justified and in places not even stated cleanly. On Page 6, the paper defines
\[
L_{\text{opt}}(N,D)=\min L(N,D)=\min\left(E+\frac{A}{N^\alpha}+\frac{B}{D^\beta}\right),
\]
which is conceptually odd because if \(N,D\) are already given, there is nothing left to minimize over. I can infer what the authors mean, namely the best attainable loss at those budgets according to a baseline scaling law or empirical sweep, but the expression as written is sloppy. This matters because the entire conditional law in **Eq. (3)** is calibrated relative to \(L_{\text{opt}}\); if the reference quantity is not well defined in the main text, the method becomes harder to interpret and reproduce.

2. The separability assumption in **Eq. (3)** is strong and insufficiently defended. The proposed model assumes
\[
L(d/\sqrt{N},r\mid N,D)
=
f\!\left(d/\sqrt{N}\right)\, g(r)\, L_{\text{opt}},
\]
or an additive analogue, where the effects of \(d_{\text{model}}\) and \(r_{\text{mlp/attn}}\) are independent once conditioned on \(N,D\). But the paper’s own architecture construction couples these variables through head count, projection dimensions, and parameter allocation. The claim that a non-separable model does not work better is only pushed to the appendix, and in the main paper this assumption is presented a bit too casually for something so central. Why it matters: if the factors interact nontrivially, the fitted optimum may be stable in this restricted sweep but fail when the search space broadens.

3. The mathematical link between the proxy variable \(d_{\text{model}}/\sqrt{N}\) and the actual parameterization is oversimplified in a way that the paper itself partially contradicts. On Page 5, the derivation motivating normalization assumes “squared attention weight matrices” and writes
\[
4d_{\text{model}}^2 \propto N_{\text{attn}} = N_{\text{non-embed}} \times \frac{1}{r+1},
\]
yet earlier on Pages 3 to 4 the paper explicitly notes that modern open models often use non-square \(q,k,v\) matrices and that GQA changes the structure further. So the paper motivates the normalization using a simplified attention parameter count while simultaneously building the empirical study around architectures where those simplifications do not strictly hold. This does not invalidate the empirical finding, but it weakens the explanatory story.

4. The treatment of GQA is notably more heuristic than the treatment of the other variables. In Section 3.4 on Page 6, GQA is excluded from the continuous law and handled by local enumeration with early stopping “once performance falls below that of the GQA=4 baseline.” That early stopping rule is itself a heuristic, and the choice of GQA=4 as baseline is not strongly justified in the main text. Since GQA is one of the three architectural factors advertised in the abstract and introduction, its partial exclusion from the analytic model makes the contribution feel less unified than claimed.

5. The paper’s strongest empirical claims are benchmarked mainly against LLaMA-3.2-style baselines and models trained under the authors’ recipe, which narrows the interpretation of the gains. For example, **Table 1** on Page 8 compares Panda and Surefire only against LLaMA-3.2-1B/3B. This is a reasonable baseline family for controlled comparison, but it is not enough to support broader claims about “optimal” architecture design in the space of open LLMs. The appendix tables suggest a wider landscape, but in the main paper the comparison set is thin.

6. Some of the claimed quality gains are modest enough that uncertainty reporting becomes important, but the paper does not provide it. In **Table 1**, Panda-3B improves average score from 61.9 to 62.5, and Surefire-3B to 62.6. Those are plausible gains, but without seeds, variance, or confidence intervals, it is hard to know how robust the differences are. The same issue applies to training loss differences such as 2.625 versus 2.619. For an ICLR paper making architecture-selection claims, this is not a minor bookkeeping issue.

7. The downstream evaluation is relatively narrow given the stated ambition. Section 4 on Page 7 uses nine zero-shot benchmarks from lm-eval-harness, which is fine as a first pass, but there is no instruction-tuned, long-context, or post-training evaluation, and the paper itself acknowledges in Section 7 that conclusions may change after post-training. This matters because architecture choices often interact with fine-tuning stability and serving characteristics beyond the pretraining regime. The paper’s claims should therefore be framed more explicitly as “pretraining-era guidance” rather than general LLM design principles.

8. There is a concrete consistency error in the reported architecture metadata. In **Table 1** on Page 8, LLaMA-3.2-3B is listed with \(r=3\), while in **Table 2** on Page 9 the same model is listed with \(r=4.80\). At least one of these is wrong. This may sound clerical, but here \(r_{\text{mlp/attn}}\) is one of the core variables of the paper, so inconsistent reporting undermines trust in the architecture bookkeeping.

9. The optimization story around Eq. (4) is more “search over measured points” than the paper sometimes suggests. Equation (4) states
\[
\arg\max_{P} I_N(P)\quad \text{s.t.}\quad L(P\mid N,D)\le L_t,
\]
which reads like a principled constrained optimization problem. But on Page 9 the actual implementation is described as searching over feasible configurations on A100 with vLLM and selecting Pareto-optimal points. That is fine in practice, but then the main contribution is a guided discrete search procedure, not really an optimization framework in the stronger sense the notation suggests.

10. The throughput analysis is partially hardware-specific, which the paper admits, but the main text still occasionally sounds more universal than warranted. **Figure 7** on Page 8 shows sizeable throughput gains for Surefire over LLaMA-3.2, and the result is encouraging. But throughput is measured with a fixed prompt/output pattern and specific serving stacks. The appendix adds more hardware/framework checks, which helps, yet the main claims could still be more careful about the boundary between architecture effects and stack-specific effects.

11. The paper uses exhaustive sweeps to validate that Panda-1B reaches the best loss among trained 1B variants, as shown in **Figure 7 (left)** on Page 8, but that figure also highlights a limitation: the claim is only as strong as the coverage of the sweep. Since the search space is constrained by fixed layers, fixed head dimensions, and family-specific design rules, the result should not be interpreted as discovering the global optimum architecture at 1B or 3B. The paper usually avoids that overclaim, but a few phrasings come close.

12. Related work positioning is good on immediate scaling-law references, but it could better situate itself with respect to recent work that studies architecture-dependent scaling beyond classic Chinchilla settings, especially work examining how feed-forward width or architectural parallelism changes scaling behavior. This is not fatal, but it contributes to the sense that the paper’s law is motivated primarily by internal empirical patterns rather than fully situated in a broader emerging literature on architecture-aware scaling.

## Questions
1. Please clarify the definition of \(L_{\text{opt}}(N,D)\) in Section 3.3, especially the use of the \(\min\) operator when \(N,D\) are fixed. Is \(L_{\text{opt}}\) meant to be the best empirical loss observed among architecture variants at fixed \(N,D\), or the Chinchilla-predicted optimum over a larger allocation space? A precise definition would materially improve confidence in Eq. (3).

2. Can the authors provide the exact fitted equations for both multiplicative and additive models with all constants, including whether the additive model intentionally omits a \(b_0\) term? As written on Page 6, the additive form appears asymmetric relative to the multiplicative one.

3. How sensitive are the fitted coefficients \((a_i,b_i)\) to the training recipe, particularly optimizer hyperparameters, data mixture, and token budget? A concise sensitivity analysis or at least a discussion of expected stability would help determine whether this is a genuine scaling law or a recipe-specific fit.

4. What happens if one removes the separability assumption and includes a simple interaction term such as
\[
c\,\phi(d/\sqrt{N})\psi(r)
\]
directly in the main-paper model, not only in appendix ablations? Even a modest main-text comparison would strengthen the claim that separability is enough.

5. Please resolve the inconsistency between **Table 1** and **Table 2** for the LLaMA-3.2-3B \(r_{\text{mlp/attn}}\) value. Since this variable is central to the paper, this should be corrected carefully.

6. For the downstream averages in **Table 1**, can the authors provide variance across random seeds, or at least some estimate of training/evaluation noise? This would help interpret whether gains like +0.6 average points at 3B are robust.

7. For the GQA search in Section 3.4, what exactly is the early stopping rule and how often does it terminate before evaluating all feasible GQA values? I would like to understand whether this heuristic could discard a later feasible configuration that recovers quality while giving better throughput.

8. Could the authors provide a clearer statement of the domain of validity of the law? Based on **Figure 8** on Page 10, the coefficients appear to shift with model scale, which suggests the law is local rather than universal. I do not view that as a deal-breaker, but I would like a cleaner articulation of the regime in which the method should be trusted.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns arise from the paper beyond standard compute and deployment considerations already typical for LLM pretraining and serving studies.

## Soundness Rating
3: good. The technical claims are mostly supported within the studied regime, and the experiments are substantial, but several central modeling choices, especially the definition of \(L_{\text{opt}}\), the separability assumption in Eq. (3), and the heuristic handling of GQA, are not fully pinned down.

## Presentation Rating
3: good. The paper is generally well written and easy to follow, with informative figures such as **Figures 2, 3, 6, and 7**, but there are a few mathematical imprecisions and at least one table inconsistency that should be fixed.

## Contribution Rating
3: good. The paper makes a useful practical contribution by connecting architecture choices to both scaling behavior and serving efficiency, but the law is best understood as an empirically effective design heuristic rather than a broadly grounded architectural scaling theory.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper is strong on empirical scope and practical relevance, and it presents a genuinely useful framework for architecture selection under inference constraints. I still have reservations about the cleanliness of the mathematical formulation, the heuristic treatment of GQA, the narrowness of the validation regime, and the lack of uncertainty quantification, so this is a positive but not enthusiastic recommendation.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the main equations, figures, and result tables, and I am fairly familiar with scaling-law and LLM architecture literature.