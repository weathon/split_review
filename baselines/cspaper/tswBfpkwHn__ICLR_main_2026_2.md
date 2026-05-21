---
job_id: b269c8df-93e9-48ef-b67e-0c0af3e83e10
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: tswBfpkwHn.pdf
paper: Can Mamba Learn In Context with Outliers? A Theoretical Generalization Analysis
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within learning theory, in-context learning, and analysis of sequence models, all of which fit ICLR.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, problem setup/methodology, theoretical results, experiments, and conclusion; while I have substantial concerns about soundness and clarity, they do not rise to the level of an immediate desk rejection based on the paper text alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-directed instructions, or other apparent manipulative content in the paper text.

# Expected Review Outcome:
## Summary
This paper studies a one-layer Mamba model for in-context learning on a stylized binary classification task with additive prompt outliers. The main claims are convergence and ICL generalization guarantees for Mamba under this setup, a comparison against a one-layer single-head linear Transformer, and a mechanistic interpretation in which the linear attention component selects context examples with matching relevant patterns while the nonlinear gating suppresses outliers and induces a recency bias. The paper also includes synthetic experiments and a small real-data validation intended to support the theory.

## Strengths
The paper asks a worthwhile question. Understanding whether Mamba-style architectures can implement in-context learning, and whether the gating mechanism can improve robustness to corrupted context examples, is relevant to current interest in alternatives to Transformers.

The paper has a reasonably clear high-level decomposition of the one-layer Mamba block into a linear-attention-like term plus a gating term. In particular, **Equation (3)** on **Page 3** is the conceptual center of the paper, and it gives a useful lens for the subsequent theory: the output is expressed as a sum over context examples with weights \(G_{i,l+1}(\mathbf w)\) multiplying a bilinear similarity term \( \mathbf p_i^\top \mathbf W_B^\top \mathbf W_C \mathbf p_{\text{query}} \). Even though I have concerns about the rigor and use of this decomposition later, this is a meaningful structural perspective.

The comparison between Mamba and a carefully matched linear-attention baseline is conceptually clean. By defining the linear Transformer as the case \(G_{i,l+1}(\mathbf w)=1\), the paper isolates the role of gating. That is a sensible theoretical design choice if the goal is specifically to study the effect of nonlinear gating.

The mechanistic visualizations are one of the stronger empirical parts. **Figure 3** on **Page 9** shows that, during training of a 3-layer Mamba, the summed first-layer attention score on examples with the same relevant pattern as the query grows much larger than that on different-pattern examples. This is directly aligned with **Corollary 1** and gives at least qualitative support to the proposed mechanism. Similarly, **Figure 4** on **Page 9** is useful because it explicitly visualizes the claimed gating behavior: outlier-containing examples have much smaller gating values than clean examples, and the clean examples exhibit a decaying trend with distance from the query, consistent with **Equations (17) and (18)**.

There is at least one empirical result that cuts against the paper’s own strongest narrative, and I appreciate that the authors included it rather than hiding it. **Table 1** on **Page 9** shows that 3-layer Mamba performs very well when outliers are far from the query (FQ) or randomly placed (R), but degrades sharply in the close-to-query setting (CQ), reaching **82.73%** while the linear Transformer is around **93.96%**. This result is important because it reveals a real limitation of the recency bias induced by the gate, and the paper does discuss this on **Page 10**.

The paper is ambitious in scope. It attempts to connect optimization, generalization under distribution-shifted outliers, and a mechanistic account of how Mamba might realize ICL. Even if the execution is uneven, the overall framing is meaningful.

## Weaknesses
I have substantial concerns about the soundness, clarity, and empirical positioning of the paper. The main issue is not that the paper lacks a theorem, it clearly has many, but that several of the central claims are supported in a way that is hard to verify and in places internally shaky.

1. **The main theoretical guarantees rely on very restrictive and somewhat self-serving assumptions about test-time outliers, which significantly weaken the practical meaning of the robustness claim.**  
   The strongest headline claim appears in **Theorem 2** on **Pages 6–7**, namely that Mamba can generalize under a large fraction of outliers, even with \(\alpha\) close to \(1\). However, this is only proved under **Condition (a)** in **Equation (11)**, where every test-time outlier must lie in a set
   \[
   \mathcal V'=\left\{\mathbf v=\sum_{i=1}^V \lambda_i \mathbf v_i^*+\mathbf u,\ \sum_i \lambda_i \ge L>0,\ \mathbf u \perp \{\mathbf v_r^*\}\cup\{\boldsymbol\mu_j\}\cup\{\boldsymbol\nu_k\}\right\}.
   \]
   This is much narrower than the surrounding prose suggests. The “unseen” outliers are not genuinely arbitrary unseen corruptions, they must contain a positive aggregate component along the training outlier span. That assumption is doing a lot of work, because it makes the gate transferable by construction. If the gate learns to suppress the training outlier subspace, then requiring test outliers to preserve positive mass on that same subspace is exactly the condition under which suppression should persist. This matters because the abstract and introduction repeatedly frame the result as robustness to unseen prompt outliers in general, while the theorem only covers a structured subset. The claim should be narrowed and made more explicit.

2. **The comparison baseline is too weak relative to the broader claims, and the paper itself contains evidence that undercuts the advertised Mamba advantage.**  
   The main comparison in **Section 3.4** and **Figure 2** on **Page 9** is against a one-layer single-head *linear* Transformer. That is acceptable for an ablation-style theoretical comparison, but the paper repeatedly uses the language “Mamba vs Transformers” in a broad way. The problem is that the paper’s own appendix already shows that this is not a stable conclusion once a stronger Transformer is used. In **Table 3** on **Page 16**, the 3-layer single-head **softmax** Transformer reaches **99.40/99.26/99.28** on FQ/R/CQ, which is comparable to or better than Mamba, and crucially avoids the severe CQ degradation that Mamba exhibits. That means the central narrative “Mamba is more robust to outliers than Transformers” is, at best, true only for the very specific linear-attention baseline studied in the theory. This is not a minor caveat, it fundamentally changes how one should interpret the significance of the result. The main text should frame the comparison much more carefully.

3. **Several equations and derivations are difficult to trust because notation is inconsistent, indexing changes mid-proof, and some displayed formulas appear malformed or incorrect.**  
   This problem appears throughout the manuscript and appendix. A few concrete examples:
   - On **Page 3**, the prompt in **Equation (2)** is later referred to as “(200)”, which is clearly a wrong reference and suggests insufficient proofreading around core definitions.
   - In **Equation (3)** on **Page 3**, the sum is over \(i=1,\dots,l+1\), but the gate definition switches between \(i\), \(j\), and “query” in a way that is easy to misread. The notation is recoverable, but sloppy for the paper’s central formula.
   - In **Appendix E.1**, **Equations (89)–(92)** on **Pages 24–25**, the indices \(i,j,k\) are mixed inconsistently when defining \(\boldsymbol G_{j,i}\) and then \(G_{i,l+1}\). The case splits use “if \(j<i\)” and then “if \(j=i\)” while the outer expression is indexed differently. This is exactly the kind of derivation where one wants very precise indexing, since the subsequent gate formula depends on it.
   - In **Appendix D.2**, the proof around **Equation (61)** on **Page 22** appears malformed and incomplete. The displayed inequality stack does not close cleanly, terms seem to be dropped, and there is a line “\(F(\Psi^{(T)}, g(\mathbf P'))\)” where \(g\) was not defined in the main setup.  
   These issues matter because the paper’s value depends heavily on readers trusting the derivations. Right now, I do not.

4. **The proof strategy often jumps from batch-level gradient statements to global convergence/generalization conclusions without enough transparent intermediate argument.**  
   For instance, **Theorem 1** on **Page 6** gives convergence/sample complexity under a nontrivial set of conditions, but the proof in **Appendix D.1** largely proceeds by asserting various growth bounds for projections of \(W_B, W_C, w\), then plugging them into rough lower bounds on \(F(\Psi^{(T)},P)\). The transition from local parameter projection inequalities such as **Lemma 3, Equations (23)–(30)** on **Pages 19 and 27–29**, and the two-phase gating claims in **Lemmas 4–5** on **Pages 19–20, 30–38**, to a full expected hinge-loss bound in **Equation (10)** is much more compressed than it should be.  
   There is also a broader methodological concern: the paper repeatedly states “with a high probability” without always specifying over which randomness, with what failure probability, and how many union bounds are being taken. For a paper built around non-asymptotic theory, this looseness is problematic.

5. **Some conditions are so opaque or unusual that it is hard to judge whether the results are informative.**  
   A notable example is **Equation (8)** in **Theorem 1**, which requires
   \[
   p_a^{-1}\mathrm{poly}(M_1^{\kappa_a}) \gtrsim l_{tr} \gtrsim (1-p_a)^{-1}\log M_1.
   \]
   The appearance of \(\mathrm{poly}(M_1^{\kappa_a})\) as an upper bound on prompt length is quite odd. Since \(\kappa_a\) is itself a magnitude parameter for outliers, this is a highly nonstandard dependence, and the paper gives little intuition for why the allowable prompt length should scale in that way. Similar comments apply to the lower and upper bounds on \(\kappa_a\) in **Theorem 1(ii)** and **Theorem 2(b)**. Without sharper interpretation, it is difficult to tell whether the theorems describe a meaningful regime or just a technically convenient one.

6. **The empirical evidence in the main paper is too narrow for the breadth of the claims.**  
   The main experimental section uses a single synthetic setup with fixed values \(d=30, M_1=6, M_2=10, V=3, l_{tr}=l_{ts}=20, p_a=0.6\), as stated on **Page 9**. There is little sensitivity analysis in the main text over the parameters that dominate the theory, such as \(V\), \(\kappa_a\), \(l_{tr}\), \(l_{ts}\), or \(M_1\). Given that the theorems are all about how performance depends on these quantities, I would expect much more direct empirical probing of those predicted scalings. Right now the experiments mostly illustrate that one selected setting behaves in the direction suggested by the theory; they do not really validate the sample complexity or convergence-rate claims.

7. **The paper’s strongest robustness claim is partially contradicted by its own positional sensitivity results.**  
   **Table 1** on **Page 9** and the discussion on **Page 10** show that Mamba is highly sensitive to outlier placement. When outliers are closest to the query (CQ), the model drops from about **99.7%** to **82.73%**, while the linear Transformer remains around **94%**. This is not a small wrinkle, it reveals that the same gate used to suppress outliers also induces a recency bias that can severely hurt robustness when adversarially positioned outliers are near the query. The paper acknowledges this, but the overall framing still overemphasizes “Mamba is robust to many outliers” without equally emphasizing “provided they are not concentrated near the query”. Since prompt ordering is often part of the attack surface in ICL, this caveat is scientifically important.

8. **The experimental mechanism claims are suggestive rather than decisive.**  
   **Figure 3** and **Figure 4** on **Page 9** are helpful, but they provide only qualitative visualization for a 3-layer model, whereas the theorems are for a one-layer model. The paper says the other layers show the same trend and defers them to the appendix, but this still leaves a mismatch between what is proved and what is empirically visualized. Moreover, in **Figure 4**, the decay pattern of the green bars is approximately monotone and recency-favoring, but without reporting the corresponding values of \(G_{i,l_{ts}+1}(\mathbf w)\) against actual index distance and whether these align quantitatively with **Equation (18)**, the figure supports the mechanism only at a qualitative level.

9. **The real-data experiment is too small and too weakly integrated into the main claims.**  
   The SST-2 experiment appears only in the appendix, and the setup is heavily stylized: prompts with 8 examples, a manually inserted phrase “James Bond,” and all models fixed to 3 layers and 2 heads. The resulting differences in **Table 7** on **Page 17** are modest, roughly 3–4 points. This is not enough to substantiate claims about real-world Mamba robustness. Separately, the PCA experiment in **Table 6** on **Page 17** is used to motivate the orthogonal-pattern data model, but showing that top principal components retain much of the classification performance does not really validate the much stronger structural assumptions used in **Section 3.2**, such as orthogonality of relevant and irrelevant patterns and the specific sparse compositional task construction.

10. **There are multiple presentation issues that hinder careful reading.**  
   These include grammatical errors, typos, and notation drift, for example “signification fraction” in **Remark 3** on **Page 7**, inconsistent use of \(\mathcal T_{\mathbf u}\) vs \(\mathcal T_{tr}\), and duplicated/misnamed appendix section titles, such as **“E.8 Extension to Multi-Classification Problems”** on **Pages 40–41**, which actually discusses regression rather than multiclassification. On a theory paper, these are not cosmetic, they materially reduce confidence in the technical care.

To be clear, I am not claiming that the whole theory is wrong. I am saying that the current presentation and supporting evidence do not make the main claims sufficiently convincing for ICLR.

## Questions
1. The main robustness theorem, **Theorem 2**, only covers test outliers in the cone-plus-orthogonal-noise set \(\mathcal V'\) from **Equation (11)**. Can the authors state much more explicitly, in the main text, what kinds of unseen outliers are *not* covered? In rebuttal, it would help to provide a clean example of a shifted outlier distribution outside \(\mathcal V'\) where the guarantee would fail, or explain why the current condition is close to necessary.

2. The paper’s broad framing suggests an advantage over Transformers, but **Table 3** in the appendix shows a softmax Transformer performing about as well as or better than Mamba, especially in CQ. Can the authors clarify whether their intended claim is strictly “Mamba vs one-layer/single-head linear attention without gating,” rather than “Mamba vs Transformers” more generally? This clarification would significantly affect my assessment of contribution.

3. Please provide a cleaner derivation of **Equation (3)** and a notation-consistent rewrite of **Appendix E.1**, especially **Equations (89)–(92)**. Right now the indexing is hard to follow. A step-by-step derivation with fixed index names would increase my confidence.

4. In **Theorem 1**, what is the intuition behind the upper bound \(l_{tr} \lesssim p_a^{-1}\mathrm{poly}(M_1^{\kappa_a})\)? Why should the maximum prompt length depend on the outlier magnitude in this specific way? A more interpretable restatement of the theorem conditions would help.

5. Can the authors add experiments that directly vary the theoretically important parameters, especially \(l_{tr}\), \(l_{ts}\), \(p_a\), \(V\), and \(\kappa_a\), and test whether the qualitative dependencies predicted by **Theorems 1–4** are actually observed? This would materially strengthen the paper.

6. **Table 1** reveals that Mamba is much worse in CQ than the linear Transformer. Is there any theorem or partial theoretical argument explaining this degradation beyond the qualitative recency-bias story in **Corollary 2**? If the theory can only explain the one-layer setting, that limitation should be stated more sharply when discussing the 3-layer experiments.

7. Several proof steps invoke “with a high probability” without explicit failure probabilities or union bounds. Can the authors provide a compact summary table of all randomness sources, event definitions, and final failure probabilities for **Theorems 1–4**? This would make the non-asymptotic results much easier to audit.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
2: fair. The paper has a serious theoretical ambition and some of the core ideas are plausible, but the current derivations, assumptions, and empirical support leave me with meaningful doubts about whether the main claims are adequately supported.

## Presentation Rating
2: fair. The high-level story is understandable, but notation inconsistencies, malformed derivations, and several writing issues substantially reduce clarity.

## Contribution Rating
2: fair. The paper tackles an interesting question and may contain useful ideas, especially the gating-based perspective, but the practical significance of the guarantees and the breadth of the claimed comparison to Transformers are overstated in the current form.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The topic is relevant and the paper has some interesting theoretical angles, but the combination of restrictive assumptions, shaky presentation of the proofs, weak empirical validation of the theory, and an overstated comparison narrative keeps it below the ICLR bar for me.

## Reviewer Confidence
4: confident. I am familiar with the related ICL theory literature and checked the main equations and proof flow carefully, although a full line-by-line verification of every appendix derivation would still take more time.