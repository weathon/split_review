---
job_id: f92f4285-fa0f-4cd0-a2f7-0f4bc01f461f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 3YKeB9R1g9.pdf
paper: Scaling with Collapse: Efficient and Predictable Training of LLM Families
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, specifically large-scale learning, optimization, scaling laws, and language-model training dynamics.

## Minimum Quality
Pass ✅ The paper contains the expected scientific components, including abstract, introduction, related work, methodology/analysis, experiments, results, and conclusion/limitations, and it provides substantial empirical evidence and mathematical discussion even though some claims are stronger than the evidence fully warrants.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not detect hidden prompts, manipulative instructions to reviewers, or other obvious attempts to influence automated reviewing within the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies when normalized training loss curves of LLMs collapse across model scales, extending recent “supercollapse” observations to more practical LLM scaling settings where width, depth, batch size, learning rate, and weight decay are co-scaled. The authors argue that collapse is governed primarily by three controls, the tokens-per-parameter ratio (TPP), the AdamW normalized timescale $\tau$, and the learning-rate schedule, and they use this perspective to propose two applications, early diagnosis of training pathologies and early stopping for hyperparameter sweeps. The paper also introduces the Celerity family as an LLM series trained in a regime intended to exhibit such collapse while remaining compute-efficient.

## Strengths
The paper targets a practically meaningful question. Predictable training dynamics across scales matter a lot for LLM development, and the central idea, using full normalized training curves rather than only final-loss scaling laws, is useful and interesting.

The empirical story is coherent and mostly well organized. In particular, **Figure 3** is one of the strongest parts of the paper: it shows the same qualitative TLC-shape changes when varying $\eta$, $\lambda$, or $B$, provided these changes induce the same normalized AdamW timescale $\tau$. This directly supports the authors’ thesis that $\tau = B/(\eta\lambda D)$ is the relevant control rather than any one hyperparameter in isolation. Likewise, **Figure 4** usefully separates the effect of TPP from scale, and the right panel makes the paper’s main empirical point fairly clearly, namely that at fixed TPP and approximately fixed $\tau$, curves align across a large scale range.

The paper also does a good job of making the phenomenon operational rather than merely descriptive. **Figure 1** and **Figure 6** provide a convincing practical narrative for monitoring, especially the claim that residuals against a collapse reference can surface divergence earlier than raw loss curves. Even if one debates how universal the reference trajectory really is, this is a good systems-facing contribution.

The Celerity section gives the work broader relevance beyond a narrow scaling-law note. The comparison in **Figure 2** and the raw values in **Table 10** suggest that the authors are not just fitting pretty curves, they are attempting to use the framework to make real training choices. The Celerity family appears competitive in compute efficiency among the baselines the paper chooses to compare against.

I also appreciated that the paper does not oversell perfect universality. The discussion around 20 TPP versus 234 TPP, and the visible deviations at higher TPP in **Figure 6**, makes the paper somewhat more credible than if every plot were presented as perfectly collapsed.

Finally, the paper is generally readable. The exposition of the key objects, TPP, $\tau$, normalized training fraction $\hat t$, and normalized loss $\ell$, is accessible, and the broader narrative from mechanism to applications is easy to follow.

## Weaknesses
1. **A core conceptual mismatch runs through the paper: the main claims are framed around $\mu$P, but the flagship Celerity demonstration is trained with CompleteP rather than $\mu$P, which weakens the clean attribution of the observed collapse.**  
   The introduction and Section 3 repeatedly state the core result as a statement about collapse “under $\mu$P,” for example on Pages 2 to 5. Yet Section 4, especially the “Experimental details” paragraph on **Page 6**, says Celerity uses CompleteP and even argues it was “more efficient/reliable than $\mu$P$” with evidence deferred to appendix Fig. 15. This matters because the paper’s headline claim is not merely “some scaling recipe can produce aligned curves,” but rather that collapse emerges when three controls align under the stated parameterization story. If the strongest large-scale demonstration depends on changing the parameterization family, then the paper is no longer isolating the effect of TPP, $\tau$, and schedule as cleanly as advertised. In other words, the reader is left wondering whether the practical success comes from the collapse framework, from CompleteP, or from both. The main paper should have been much sharper here, either by keeping the full demonstration within the same parameterization regime or by explicitly redefining the claim as broader than $\mu$P.

2. **Several important claims rely on qualitative plots rather than quantitative collapse metrics, which makes the central notion of “collapse” feel under-defined in the main paper.**  
   The paper uses terms like “collapse,” “tight collapse,” and “deviation from collapse” throughout, but in the main text there is no rigorous scalar criterion for when two or more normalized curves are deemed to collapse, beyond visual alignment. This is especially visible in **Figure 6**: the text says collapse is “tight” at 80 TPP and looser at 20 TPP, but the reader is not given a threshold or statistic for this judgment. The right panel of **Figure 1** plots residuals to a reference curve, which is helpful, but again the paper does not define a decision rule, confidence interval, or acceptable band. This matters because the paper elevates collapse from an observational curiosity to a “signature of compute-efficient training” and a practical diagnostic. Once the claim becomes operational, subjective eyeballing is not enough. A quantitative metric such as average deviation, alignment error, or seed-normalized residual bands should have been in the main paper.

3. **The theoretical account is suggestive but much weaker than the empirical claims it is used to motivate, and there are places where the mathematical presentation is sloppy or potentially misleading.**  
   The noisy quadratic model around **Equation (3)** in Section 3 and expanded in Appendix B.3 is fine as intuition, but the paper often talks as if it explains the observed LLM behavior rather than merely providing a toy analogue. More concretely:
   - In **Equation (3)** on **Page 5**, the notation switches to $\sigma_z^2$, while Appendix B.3 derives the analogous expression with $\sigma_x^2$ in **Equations (14) to (16)**. The mismatch is minor but not good in a paper so centered on a specific functional dependence.
   - The statement right after **Equation (15)** in the appendix, “If initialization is zero-mean in expectation ($\mathbb{E}[\theta(0)^2]=0$), the bias term vanishes,” is mathematically wrong as written, since zero mean would imply $\mathbb{E}[\theta(0)] = 0$, not $\mathbb{E}[\theta(0)^2]=0$ unless initialization is almost surely zero. The main-text **Equation (3)** avoids this exact wording but still inherits the same conceptual looseness from the derivation.
   - On **Page 5**, the paper states that after normalizing by final loss, the curvature factor $h$ cancels, and therefore the normalized TLC depends only on $\tau$ and $\hat t$ provided residual bias is negligible. This is a much stronger assumption than the prose suggests. The normalized expression in Appendix B.3 still depends on $\kappa = \frac{2\tau \mathbb E[\theta(0)^2]}{\sigma_x^2}$, so collapse is only guaranteed if either $\kappa$ is negligible or approximately scale-invariant. That caveat is important, and the main text underplays it.
   These issues do not invalidate the empirical section, but they do reduce confidence in the “explaining” language around the theory.

4. **The early-stopping method is promising, but the evaluation scope is too narrow to support the broader pitch in Section 5.**  
   The procedure in **Section 5** is presented as a practical way to stop large-scale sweeps after 10 to 30 percent of training. However, the main evidence is limited to a few $\lambda$ and $B$ sweeps, mainly in **Figure 9**, with additional cases relegated to the appendix. There is no demonstration on learning-rate tuning, schedule tuning, or mixed sweeps where multiple controls vary simultaneously. This is not a small omission because the method depends on first identifying the right “TLC controls” and then choosing or predicting the corresponding universal curve. In real HPO, those controls are often precisely what is uncertain. The evidence in **Figure 7** is useful, especially the left-vs-right comparison showing why holding $\tau$ fixed preserves ordering, but it also reveals that the method may depend on using the right parameterization of the sweep from the outset. So the practical value is real, but the paper currently demonstrates a narrower claim than the framing suggests.

5. **The predictive surrogate in Equations (4) and (5) is rather ad hoc, and the optimization/fitting procedure is under-justified.**  
   On **Page 9**, the proposed surrogate
   $$
   \hat{\ell}(\hat{t})=\left(\frac{1+\epsilon_1}{\hat{t}+\epsilon_1}\right)^m+b\cdot(\eta(\hat t)+\epsilon_2)^q
   $$
   is introduced mostly empirically. The paper then fixes $m=0.05$, fixes $\epsilon_1,\epsilon_2$, and lets $b$ and $q$ vary via power laws in $\tau$ and TPP. This may work, but the model design looks hand-tuned, and there is limited evidence in the main paper that it is identifiable or robust. There is also a conceptual inconsistency: the surrounding text says the second term reflects LR-schedule modulation and that $q$ varies systematically with TPP, but the appendix **Figure 22** apparently shows $q$ also has strong dependence on $\tau$ with regime changes. **Table 12** then reports that fitting $q$ as a power law in TPP plus $b$ as a power law in $\tau$ matches the performance of a joint $(\tau,\mathrm{TPP})$ fit on the reported evaluation set. That is encouraging, but it also suggests the modeling choice is more heuristic than principled. Since this surrogate underpins the early-stopping application, the paper should be clearer that it is a simple empirical extrapolator rather than a derived universal law.

6. **The compute-efficiency comparison is directionally interesting, but the fairness of the comparison is debatable because several confounders change at once.**  
   **Figure 2** claims that Celerity lies on the compute-efficiency frontier, and **Table 10** gives the underlying numbers. But Celerity differs from many baselines in more than just the training recipe: it uses a curated data mix, different parameterization, different architecture choices, and different context length. Section 4 explicitly says the data mixture emphasizing educational, math, and coding data improved downstream performance, with supporting numbers in **Table 7**. That is perfectly valid as model development, but it means **Figure 2** cannot be read as strong evidence that collapse-based training alone puts Celerity on the frontier. The claim is therefore too bundled. A stricter version of the argument would compare matched models trained with and without the collapse-informed recipe while keeping architecture and data fixed.

7. **The paper repeatedly argues for predictability and stability, but the treatment of variance across seeds is minimal in the main paper.**  
   Equation (1) includes a seed variable $\omega$, and the notion of “supercollapse” from Qiu et al. is partly about differences being smaller than inter-run noise. Yet the main paper rarely reports seed variability, confidence bands, or repeated-run statistics. Most plots show single trajectories. This matters for two reasons. First, if collapse is meant to be used as a sensitive monitor, one needs to know the normal residual range due to seed noise and data-order stochasticity. Second, if early stopping is based on fitted alignment, variance in partial trajectories can change the winner in close sweeps. The paper says in **Section 3** that moving-average smoothing is used, but smoothing is not a substitute for uncertainty quantification.

8. **Some parts of the exposition blur what is established in the main paper versus what is assumed from prior work or deferred to the appendix.**  
   A lot of the paper’s practical recipe depends on prior claims that optimal $\tau$ depends only on TPP. That may well be true, but in this submission it is largely imported from Bergsma et al. (2025a). The main paper’s own evidence for that dependency is limited. Similarly, the choice of 234 TPP for Celerity is motivated using an iso-loss compression analysis that is only derived in Appendix C.1. The main paper then uses this choice to make fairly strong statements, for example in **Key takeaway 2** on **Page 8**, that the 234-TPP band lies on the compute-accuracy frontier while using approximately 62% fewer parameters than compute-optimal training at equal loss. This is plausible, but the main-paper argument is thin relative to the strength of the statement.

9. **There are presentation issues and notation glitches that are not fatal but do hurt precision.**  
   A few examples:
   - **Table 1** on **Page 4** contains a malformed line, writing “$t = t/T$” where the normalized fraction is elsewhere denoted $\hat t = t/T$.
   - The paper alternates between describing $\tau$ as a timescale over “updates,” “iterations,” and “training fraction” without always carefully distinguishing $\tau_{\mathrm{iter}}$ and normalized $\tau$.
   - Several references and table entries in the appendix contain typographical errors, for example “Corebras-GPT” and task names like “hellawag” / “piga” in **Table 10**. These do not affect the science directly, but they make the presentation look less polished than it should for a paper so reliant on careful comparison.

10. **The evidence for generality beyond the tested regime remains limited in the main paper.**  
   The authors are commendably explicit in Limitations, but this remains a genuine weakness. The main results are for single-epoch pretraining with AdamW-like optimization and mostly GPT-like decoder-only models. The appendix discusses alternative schedules, sparse MoE, and different $\beta$ values, but the main-paper conclusions are broader than the demonstrated scope. In particular, claims such as collapse being a “robust marker of compute-efficient and stable pre-training” would feel better supported if the main paper showed at least one convincing result outside the exact recipe family used for Sections 3 to 5.

## Questions
1. The biggest clarification I would like is about parameterization. The main narrative is built around $\mu$P, but Celerity uses CompleteP. Can the authors provide a cleaner main-paper comparison showing that the same collapse claims hold under matched data/architecture when switching only between $\mu$P and CompleteP? This would help disentangle whether collapse is really driven by $(\mathrm{TPP},\tau,\text{schedule})$ as claimed, or whether parameterization is a stronger latent factor than the paper currently acknowledges.

2. Please provide a quantitative main-paper definition of collapse and residual deviation. For example, what statistic is used in **Figure 1** right and **Figure 6** right, how is the reference curve constructed exactly, and what residual magnitude should be considered “normal” versus pathological? A seed-based confidence band would make the diagnostic claim much stronger.

3. For the theory around **Equation (3)**, can the authors clarify the assumptions under which the normalized TLC depends only on $\tau$ and $\hat t$? In particular, the role of
   $$
   \kappa = \frac{2\tau \mathbb E[\theta(0)^2]}{\sigma_x^2}
   $$
   seems important. Is the implicit claim that $\kappa$ is approximately scale-invariant under the tested parameterization, or merely that it becomes negligible after warmup? A more careful statement would materially increase confidence.

4. For the early-stopping procedure in **Section 5**, what happens when the hyperparameter sweep itself changes the effective TLC controls in a way that is not known in advance, for example joint sweeps over $(\eta, B, \lambda)$ or schedule shape? Do the authors view the method as mainly useful once a scaling recipe has already been largely stabilized?

5. **Figure 2** and **Table 10** are interesting, but they bundle data-mixture, architecture, and parameterization changes with the collapse-based training strategy. Can the authors add or summarize a more controlled comparison, ideally same architecture and same data, where only the training recipe differs? That would better isolate the contribution of the advocated methodology.

6. The paper often uses single curves. How sensitive are the main conclusions, especially early diagnosis and early stopping, to seed variation and dataloader-order variation? Even a compact table with mean and standard deviation of residual-alignment error across a few repeated runs would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work studies training dynamics and efficiency for language models using public pretraining data and standard benchmark evaluation. Any broader societal concerns are the usual ones associated with releasing and scaling general-purpose LLMs, but the submission does not present a distinct ethics issue that requires separate review based on the main text.

## Soundness Rating
3: good. The empirical evidence is substantial and many claims are supported, but several central claims are more qualitative than quantitative, and the theoretical justification is weaker and less careful than the paper’s framing suggests.

## Presentation Rating
3: good. The paper is readable and the figures are generally informative, but there are some notation issues, a few sloppy mathematical statements, and too many important details are either qualitative or deferred.

## Contribution Rating
3: good. The paper makes a useful contribution by connecting collapse behavior to practical LLM training decisions and by demonstrating applications to monitoring and HPO, though the contribution is somewhat diluted by confounding factors and by a narrower experimental scope than the framing implies.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
This is a useful and technically interesting paper with strong practical intuition and several compelling figures, especially around $\tau$ as a unifying control and collapse residuals as a monitoring signal. I am positive overall because the core empirical phenomenon appears real and practically relevant. That said, the paper overstates how cleanly it has isolated the governing factors, the theory is more heuristic than explanatory, and the strongest systems-level claim is confounded by simultaneous changes in parameterization, data, and architecture. I can support acceptance, but not enthusiastically.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main mathematical and empirical claims carefully, though some implementation-level details of the training recipe are necessarily hard to verify from the paper alone.