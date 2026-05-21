---
job_id: bcb17aa4-5081-4794-a893-a39fc069f401
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: m18MXVdrV9.pdf
paper: Information Estimation With Discrete Diffusion
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining generative modeling, probabilistic methods, information-theoretic estimation, and applications to language and genomics.

## Minimum Quality
Pass ✅. The paper includes the necessary scientific components, presents a concrete method with mathematical formulation and experiments, and, despite notable issues in clarity and validation, it clears the minimum bar for non-desk-rejection consideration.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided manuscript text.

# Expected Review Outcome:
## Summary
This paper proposes INFO-SEDD, a mutual information and entropy estimator for high-dimensional discrete data based on discrete diffusion over continuous-time Markov chains. The key idea is to express KL divergences through CTMC dynamics and approximate the needed density ratios with discrete diffusion score models, yielding joint and conditional variants for MI estimation and an entropy estimator. The paper evaluates the approach on synthetic benchmarks, text summarization, genomics consistency tests, motif localization in promoter sequences, and, in the supplementary material, entropy estimation for Ising models.

## Strengths
The paper tackles an important and under-served problem. Estimating MI on high-dimensional discrete objects is genuinely difficult, and much of the current practice still relies on the somewhat awkward pipeline of embedding discrete data into continuous spaces and then applying estimators designed for continuous variables. The motivation is well articulated in Sections 1 and 4, and the problem is relevant to the ICLR community because it sits at the intersection of generative modeling, density-ratio estimation, and representation learning for structured discrete data.

The core methodological angle is interesting. The use of discrete diffusion / CTMC machinery to estimate information-theoretic quantities directly on discrete state spaces is a meaningful departure from the standard embedding-based workaround. In particular, the absorbing-state construction in Section 3, together with Equation (6), is a clever design choice because it allows reusing a score model trained on the joint distribution to recover marginal score ratios. That is a practically useful idea, not just a cosmetic reformulation.

The paper also deserves credit for not stopping at a synthetic benchmark. The applications in text summarization and genomics are reasonably well motivated, and they test the estimator in settings where discrete structure actually matters. Figure 4 is especially useful here: it shows that INFO-SEDD-C tracks the classifier-based MI reference much more closely than the alternatives on the HUMAN VS. WORM consistency test, and the gap between INFO-SEDD-C and INFO-SEDD-J there also helps illustrate when the conditional formulation is easier to optimize. Likewise, Figure 5 is one of the more convincing qualitative pieces in the paper, because the MI profile peaks in the expected TATA-box region; this makes the genomics use case feel less like a decorative application and more like a case where the estimator may expose biologically meaningful localized dependence.

The synthetic benchmark in Table 1 is strong evidence in favor of the method on the paper’s chosen regime. INFO-SEDD remains close to ground truth as both MI and dimension grow, while several standard neural estimators collapse or saturate badly. For example, at MI \(=40, D=40\), INFO-SEDD reports \(39.11 \pm 0.65\), whereas MINE, NWJ, and KL-DIME are all far off. Even when MINDE remains in the ballpark at lower settings, INFO-SEDD is usually more stable. This table supports the paper’s main empirical claim better than the downstream applications alone.

Table 2 is also informative rather than merely decorative. It shows that MI estimates from INFO-SEDD-C correlate substantially more with the human “consistency” metric than the listed baselines in the summarization setting, which is aligned with the intended semantics of MI more than, say, coherence. I appreciate that the authors do not oversell this and explicitly discuss why hallucinations and subjective notions of relevance are only partially captured by MI.

There is some attempt at theory beyond just “we can derive an estimator.” Equation (7) gives an interpretable error decomposition into score approximation error and finite-horizon truncation bias, and the discussion in Section 3 correctly frames a trade-off in \(T\). Even though I have concerns about the exposition and some proof details, the paper is trying to do real analytical work rather than relying entirely on empirical persuasion.

Finally, the method seems reasonably compatible with pretrained masked discrete diffusion backbones, which is a practical strength. The text and DNA experiments use pretrained MDLM and Caduceus backbones, respectively, and that makes the proposal more reusable than methods requiring bespoke architectures from scratch.

## Weaknesses
1. **The main mathematical development is not presented with enough rigor or clarity in the main paper, and some equations appear inconsistent or under-specified.**  
   This is the biggest issue for me. The method rests almost entirely on the derivation from CTMC reversal and Dynkin’s formula to the KL estimator in Equations (4) and (5), yet the main text leaves several gaps. On **Page 3, Equation (2)**, the paper writes
   \[
   \mathrm{KL}[\vec p_0\|\vec q_0]
   = \mathbb E\left[\log \frac{\vec p_0}{\vec q_0}(\overleftarrow X_T)\right]
   = \mathbb E\left[\log \frac{\vec p_T}{\vec q_T}(\overleftarrow X_T)\right],
   \]
   which is not self-evident as written, because \(\overleftarrow X_T\) corresponds to the initial-state distribution of the forward process, and the equality with the terminal-time log-ratio needs a careful change-of-variables argument. The derivation may well be fixable, but in the main paper it is too compressed for such a central step.

   There is also notation drift. In **Equation (5) on Page 4**, the estimator includes \(s_\theta^p\), \(s_\phi^q\), but then the third term suddenly uses \(s_0^p\), which looks like a typo for \(s_\theta^p\). For a paper built around a delicate ratio-estimation formula, this is not a harmless typo. It makes the core estimator ambiguous.

   Relatedly, the paper alternates between \(\vec X_t\), \(\overleftarrow X_t\), \(\widehat X_t\), and \(\widetilde X_t\) in the appendix proof of Equation (4), and several lines are difficult to verify because of this shifting notation. For example, in **Appendix A.1, Pages 19 to 21**, the derivation moves between forward and reverse quantities with inconsistent hats and arrows. I could follow the intended structure, but this is exactly the sort of derivation where notation sloppiness can hide mistakes.

2. **There are apparent mathematical mistakes or at least serious presentation errors in the algorithms and some formulas, which undermines confidence in implementation correctness.**  
   The pseudocode in **Algorithms 1 to 3, Page 22**, contains multiple suspicious variable mismatches. In **Algorithm 2**, line 6 defines \(\tilde X\) although the loop is over components of \(\vec Y_t\), and line 7 mixes \([\vec X_0,\tilde Y]\), \([\vec X_t,\vec Y_0]\), and \([\tilde X,\vec Y_0]\) in the same estimator. As written, this is inconsistent and hard to reconcile with the preceding derivation of INFO-SEDD-C. If the algorithm is just sloppily typeset, that is still a serious problem because the paper asks the reader to trust a fairly intricate estimation procedure.

   **Algorithm 3** has similar issues: the term \(\frac{1}{N(s^{\theta(t)}-1)}\) is almost surely malformed and seems intended to be \(\frac{1}{N(e^{\bar\sigma(t)}-1)}\), matching the discussion on **Page 5** and Appendix A.2. Again, these are not cosmetic details. The paper’s contribution is an estimator, so if the estimator pseudocode is not syntactically or semantically reliable, reproducibility and trust suffer.

3. **The theoretical claim of consistency is relegated to the appendix and depends on assumptions that are quite strong and not well interrogated in the main paper.**  
   The main paper states after **Equation (7) on Page 5** that INFO-SEDD is “a consistent estimator up to this exponentially decaying bias.” That phrasing is a bit slippery. The bound itself depends on bounded score ratios with constants \(C_1, C_2\) and approximation errors \(\epsilon_p,\epsilon_q\), but those assumptions are nontrivial, especially the lower bound \(C_1>0\) on score ratios. In sparse high-dimensional discrete spaces, requiring ratios over all Hamming-neighbor states to remain uniformly bounded away from zero is not innocuous.

   Moreover, the result is only sketched in the main paper. The actual argument lives in **Appendix E**, and even there some steps are quite loose. For instance, the truncation-bias bound on **Pages 39 to 40** goes from \(\log(|\chi|^D C_2^D)\) to \((D\log |\chi| C_2)\), which seems dimensionally off. One would expect something like \(D(\log |\chi| + \log C_2)\), not \(D \log |\chi|\, C_2\). This could be a typo, but it matters because it is the displayed final bound quoted back in the main paper as **Equation (7)**. If the theorem is central enough to support a consistency claim, the statement should be airtight in the main text.

4. **The experimental evaluation is broad, but parts of it are not as decisive as the paper suggests because several comparisons are not entirely satisfying.**  
   On the positive side, **Table 1** is strong. But outside the synthetic benchmark, the evidence gets murkier. In the text summarization consistency test, the paper argues that MI should grow approximately linearly with \(\rho\), yet this is only justified by an order-of-magnitude entropy argument and a high-MI assumption. That is plausible, but not ground truth. So **Figure 1** should be interpreted as a consistency sanity check, not a hard validation of calibration. The paper mostly does that, but some of the language around “closely matching the empirical derivation” feels stronger than the setup warrants.

   The baseline situation is also a bit uneven. Several baselines are methods known to struggle in high-MI settings, and the paper emphasizes this, which is fair. But when the competitors catastrophically fail, it becomes even more important to include stronger discrete-specific alternatives or stronger non-neural discrete estimators wherever computationally feasible, at least on smaller regimes. The appendix includes one plug-in comparison, but the main paper’s headline results are mostly against estimators that the paper itself argues are mismatched to the discrete setting.

5. **The downstream applications are interesting, but the causal link between accurate MI estimation and the claimed utility is still somewhat underdeveloped.**  
   For text summarization, the model-selection story is suggestive rather than conclusive. **Table 2** shows that INFO-SEDD-C correlates with human consistency better than the listed baselines, but this is still just correlation across a relatively small set of summarization systems. It does not establish that MI is the best tool for evaluation, only that it aligns with one meaningful metric better than several alternatives in this setup. Also, the paper itself notes that hallucinations are not captured by MI, which is not a minor caveat in summarization.

   Similarly, the promoter experiment visualized in **Figure 5** is attractive, but there is no quantitative evaluation of localization quality. The figure shows a peak around the expected TATA-box region, which is encouraging, but without a comparison to a baseline motif-scoring method or a quantitative localization metric, it is hard to judge how strong this result really is. At the moment, the figure is more of a case study than a rigorous benchmark.

6. **Clarity and writing quality are inconsistent, and this meaningfully affects scientific readability.**  
   This manuscript is readable at a high level, but there are many places where the exposition is rougher than it should be for ICLR. Some notation is overloaded or inconsistent, some references are malformed in the bibliography, and there are several typographical errors that are not trivial because they occur in formulas and algorithms. The transition from CTMC preliminaries to the practical estimator is also too abrupt. A reader not already familiar with discrete diffusion score modeling will likely struggle to infer exactly what quantity the network predicts, how the DWDSE-trained score is converted into the ratios used in **Equation (5)**, and how the Monte Carlo estimator is implemented in practice.

   Even the figures reflect some of this unevenness. **Figures 2 and 3** are useful in showing the GP trend between estimated MI and human consistency, but they are arguably more polished than informative. The main takeaway is monotonic association with saturation in the human metric, which could have been summarized more directly. By contrast, the paper spends too little space on implementation-critical details of the estimator itself in the main text. In other words, some presentation bandwidth is spent on secondary visualizations while the core method remains under-explained.

## Questions
1. The key estimator in **Equation (5)** appears to contain a typo, using \(s_0^p\) instead of \(s_\theta^p\). Please confirm the correct formula, and if there are any other typographical mistakes in the estimator, provide a corrected expression end-to-end. This would substantially improve confidence in the method.

2. Can the authors provide a cleaner derivation, in the rebuttal, of the step from **Equation (2)** to **Equation (4)** using consistent notation? In particular, I would like clarification on which process the expectation is taken over, why the equality involving \(\log \frac{p_T}{q_T}(\overleftarrow X_T)\) is valid, and exactly where the terminal KL term is dropped.

3. For the theoretical result summarized in **Equation (7)**, how realistic are the boundedness assumptions \(C_1 \le s^p, s^q \le C_2\) in the kinds of sparse, long-sequence problems studied here? If these assumptions fail approximately rather than exactly, what behavior should one expect empirically?

4. Could the authors quantify the sensitivity of INFO-SEDD to the diffusion horizon \(T\) or the integrated noise schedule \(\bar\sigma(T)\)? The theory explicitly describes a trade-off between truncation bias and score-estimation error, but the main paper does not really show this trade-off empirically.

5. In the genomics motif experiment shown in **Figure 5**, can the authors report a quantitative localization metric, for example peak overlap or retrieval of annotated motif windows, and ideally compare against a simple baseline? This would make the application much more convincing.

6. In the text summarization setting, **Table 2** is based on correlations across systems. How many systems are included for the human-evaluation comparison, and how stable are these correlations under bootstrap resampling across systems or documents? This matters because correlation estimates over a small set of systems can be unstable.

7. Please clarify the pseudocode in **Algorithms 1 to 3**. As written, there are variable mismatches in INFO-SEDD-C and what looks like a malformed entropy term in INFO-SEDD-H. Are these purely typographical, or is the implementation different from the printed algorithm?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The genomics and text applications use existing datasets and appear to be methodological evaluations rather than sensitive deployment studies.

## Soundness Rating
3: good. The central idea is plausible and supported by substantial experiments, but the paper has enough mathematical and presentation-level inconsistencies that I cannot call the technical support excellent.

## Presentation Rating
2: fair. The paper is understandable at a high level, but key derivations, notation, and pseudocode contain enough ambiguity and probable typos to materially hurt clarity.

## Contribution Rating
3: good. Direct MI estimation on discrete data via discrete diffusion is a valuable contribution, and the empirical results are meaningful, even though the validation and theoretical exposition are not fully convincing.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important problem and has a credible core idea with strong synthetic results and interesting applications, but the mathematical exposition and algorithmic specification are sloppier than they should be for a method paper whose main claim hinges on precise derivations.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main technical and empirical claims carefully, though some appendix derivations are difficult to verify fully because of notation and presentation issues.