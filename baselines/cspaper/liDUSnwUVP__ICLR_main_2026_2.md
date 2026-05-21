---
job_id: 53e49704-41c1-4663-a3c6-6a90a4a4bb1a
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: liDUSnwUVP.pdf
paper: HG-DCM: History Guided Deep Compartmental Model for Early Stage Pandemic Forecasting
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a transfer-learning / hybrid mechanistic-ML method for healthcare forecasting, with a learned neural component guiding a compartmental model under data scarcity.

## Minimum Quality
Pass ✅. The paper contains the necessary scientific structure, including abstract, introduction, related work, methods, experiments, quantitative results, discussion, limitations, and conclusion. While there are important concerns about methodology, evaluation breadth, and mathematical specification, these do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes HG-DCM, a two-stage framework for early-stage pandemic forecasting that uses a neural network to infer DELPHI compartmental-model parameters from short case trajectories and metadata, with training guided by historical outbreaks such as Ebola, SARS, Dengue, and seasonal influenza. The main empirical claim is that historical cross-disease transfer reduces overfitting and overshooting in early COVID-19 forecasting, outperforming DELPHI, a CNN baseline, a truncated variant without historical guidance, and two external baselines on limited locations.

## Strengths
The paper tackles a real and important problem, namely cold-start forecasting when only a few weeks of data are available. This is a setting where standard per-location compartmental fitting is indeed brittle, and the paper’s central intuition, using historical outbreaks to regularize early predictions, is reasonable and practically relevant.

The proposed framework preserves some interpretability by predicting epidemiological parameters rather than directly regressing future trajectories. That design choice is meaningful, because it gives the model a mechanistic bottleneck rather than a fully unconstrained black box.

Figure 1 is useful in conveying the overall architecture. It makes the two-stage decomposition, learned parameter predictor followed by IVP-based compartmental solver, easy to understand. In particular, the diagram helps clarify that the neural network is not forecasting cases directly, but is instead used to produce DELPHI parameters that are then passed to the ODE solver. This architectural transparency is one of the clearer parts of the paper.

The paper also makes a concrete effort to analyze failure modes beyond a single scalar metric. Figure 4 is one of the stronger pieces of evidence in the paper, especially Figure 4(a), which visualizes overshooting counts across training-window lengths, and Figure 4(b), which gives a qualitative example where DELPHI diverges badly while HG-DCM stays closer to the observed trajectory. Even though the overshooting definition itself raises questions, the authors are at least trying to diagnose a practically important pathology rather than relying only on average errors.

Table 2 provides evidence that the historical-guided variant helps relative to DELPHI and the truncated variant in several settings, especially at 6 and 8 weeks for mean MAE, and often for median MAE. The inclusion of both mean and median errors is helpful because these forecasting distributions appear heavy-tailed, and median performance is often more informative when overshooting dominates a subset of locations.

The parameter analysis in Figure 5 is another positive aspect. Even though the interpretation is not fully convincing yet, the authors do at least try to inspect the learned epidemiological quantities rather than treating the model as inscrutable. That is preferable to purely accuracy-driven forecasting papers.

## Weaknesses
1. **The empirical support for the main benchmarking claim is much too narrow relative to the paper’s scope.**  
   The central claim, stated repeatedly in the abstract and introduction, is that HG-DCM provides a robust framework for early-stage pandemic forecasting by transferring knowledge from many historical outbreaks. However, the direct comparison to external baselines in **Table 1 (Page 7)** is limited to only two locations, the United States and Massachusetts, and even there the comparison is incomplete because several entries are missing. This is a serious limitation, not a cosmetic one. A method marketed as broadly useful across 258 global locations should not be judged primarily by a benchmark table restricted to two locations due to baseline availability. The result is that the strongest comparative claim in the paper rests on a very thin slice of evidence.  
   This matters because cross-disease transfer methods can easily look good on a few large, data-rich COVID locations while failing to generalize more broadly. Without broader like-for-like comparisons, it is hard to know whether the gains are methodologically meaningful or simply an artifact of the chosen locations and incomplete baseline coverage.

2. **The evaluation is internally inconsistent, and some reported results in Table 1 are hard to reconcile with the paper’s narrative.**  
   The text says HG-DCM “consistently achieves lower MAE in most tasks compared to both baselines,” but **Table 1** is not nearly that clean. On Massachusetts at 6 weeks, EiNNs has lower MAE than HG-DCM (25,669 vs. 39,887). On United States at 4 weeks, HG-DCM is dramatically worse than EiNNs (2,548,004 vs. 729,091). Calling this “consistently” better is overstated.  
   This matters because the paper’s presentation overclaims what the data actually shows. If the method is only better in some tasks, especially those with very short windows, that is still potentially interesting, but it is a narrower and more defensible claim. Right now the wording papers over real failures.

3. **Table 2 raises stability concerns that the paper does not confront honestly enough.**  
   In **Table 2 (Page 7)**, HG-DCM has much better mean MAE than alternatives at 6 and 8 weeks, but at 4 weeks its **mean MAE is 110,452.4**, far worse than CNN (**11,238.1**) and T-DCM (**17,691.2**). That is not a small miss, it is an order-of-magnitude problem. The median MAE at 4 weeks is good, but the mean explodes, indicating severe heavy-tail failures on a subset of locations. The paper emphasizes “stability,” yet this 4-week result is one of the least stable entries in the entire table.  
   Figure 3, which shows MAE distributions, visually supports the claim that HG-DCM can have better concentration than DELPHI in some windows, but it does not resolve the glaring issue from Table 2 that HG-DCM itself still suffers from substantial tail-risk in at least one regime. If the method is meant for public-health decision making, rare catastrophic failures matter at least as much as median gains.

4. **The loss formulation in Equations (3)-(5) is underspecified and mathematically problematic.**  
   On **Page 5**, the loss uses a term
   \[
   \left|\frac{C_{ij}-\hat{C}_{ij}}{C_{ij}}\right|,
   \]
   but the paper does not explain how division by zero is handled. Since the forecasts are evaluated in early outbreak phases, cumulative cases can be small, and depending on indexing and preprocessing, zero or near-zero denominators are plausible. If an \(\epsilon\) stabilization is used, it should be stated explicitly. If not, the objective is ill-defined.  
   There are also indexing ambiguities. The sums are written as \(\sum_{i=0}^{n_P}\sum_{j=0}^{t+v}\) and \(\sum_{i=0}^{n_C}\sum_{j=0}^{t}\), but the normalization uses \(n_P(t+v)\) and \(n_C t\), which suggests either off-by-one indexing or notation that mixes inclusive and exclusive endpoints. This is a small-looking issue, but it matters because the objective is the core training signal.  
   More importantly, the paper says MAE and MAPE are “weighted by \(\alpha\) to balance the effect of the population,” but MAPE is not really a population-normalization device; it is a relative error term. The role of \(\alpha\) is not linked to any principled scaling argument, and \(\beta\) in **Equation (5)** is introduced as the key tradeoff controlling inheritance from historical pandemics, yet there is no ablation or sensitivity analysis for \(\beta\) in the main paper. This leaves the most important transfer knob effectively opaque.

5. **The method description does not make clear what exactly the model predicts: static parameters, time-varying parameters, or parameter dynamics.**  
   The introduction repeatedly claims the framework learns “how these parameters evolve” and refers to “time-varying parameters,” including on **Page 4** where \(f(T,M)\) predicts “the time-varying parameters \(\hat{\theta}\)” of DELPHI. But the architecture description then says the network outputs “the 12 parameters for the DELPHI model,” which sounds like a single fixed parameter vector. These are not equivalent statements.  
   If \(\hat{\theta}\) is time-varying, the paper needs to specify its temporal parameterization, dimensionality, and how it is consumed by the ODE solver. If \(\hat{\theta}\) is static, then the framing around learning parameter evolution is misleading. This ambiguity is not a side detail, it is the core object being learned.

6. **There is a substantial risk of label leakage or circular supervision in how training targets for historical pandemics are obtained, and the paper does not explain this carefully enough.**  
   The model is trained to predict DELPHI parameters and then uses DELPHI to reconstruct incidence curves. But the paper does not clearly state whether “ground-truth” DELPHI parameters for historical outbreaks are separately fitted first, or whether the network is trained only through curve-level supervision. The wording on **Pages 3-5** suggests the latter, but then the claim that the model “learns a common mapping” from early-stage trajectories to fundamental transmission parameters becomes much weaker, because those parameters are only indirectly identified through trajectory fitting.  
   In compartmental models, parameter non-identifiability is a notorious issue, especially early in an outbreak. Multiple parameter settings can yield similar cumulative trajectories. Without discussing this identifiability problem, the paper’s interpretability claims are too confident. Figure 5 compares parameter distributions from HG-DCM and DELPHI, but if the parameterization is weakly identifiable from early cumulative cases alone, then the statistical significance of differences in those inferred parameters is not especially meaningful.

7. **The ablation design does not isolate the historical-transfer contribution as cleanly as the paper claims.**  
   T-DCM is described on **Page 8** as excluding historical pandemic data and metadata, which means it simultaneously removes at least two factors: historical transfer and auxiliary metadata. As a result, the gap between HG-DCM and T-DCM cannot be attributed specifically to cross-disease transfer. It could come from metadata alone, training-set size alone, or their interaction.  
   For a paper whose headline claim is “history-guided” learning, the main paper really needs a cleaner decomposition: with vs. without historical outbreaks, with vs. without metadata, and ideally with different subsets of source diseases. Right now the ablation is too bundled to support the causal interpretation the discussion pushes.

8. **The paper’s preprocessing and augmentation decisions may materially shape the results, but are not stress-tested.**  
   The retrospective definition of LDoA for historical outbreaks on **Page 5** is used to decide augmentation cutoffs. The paper says this does not induce leakage at inference because LDoA is never used on the current pandemic, which is true in a narrow sense, but it still means the historical training data are curated using future knowledge of full epidemic waves. That may produce a source distribution that is cleaner and more structured than what is available in a true cold-start deployment.  
   Figure 2 illustrates the smoothing, first-wave detection, and LDoA selection pipeline clearly, and in that sense it is a helpful figure. But it also makes the retrospective nature of the curation very visible. This matters because the transfer-learning story depends heavily on how source examples are constructed. If the source set is selected using future wave information, the training task may be artificially easier than the target task.

9. **The comparison set is weak for the claimed contribution, and the paper underpositions itself relative to relevant transfer-learning and hybrid epidemic-forecasting work.**  
   The baselines include DELPHI, a CNN, T-DCM, GradABM, and EiNNs. That is not enough to establish that the historical-transfer idea itself is the key advance. In particular, the related-work discussion is somewhat selective. There is prior work on deep transfer learning for epidemic time series, and also on neural augmentation of compartmental models with time-varying dynamics, which would be directly relevant to this submission’s novelty claim. The paper repeatedly frames itself as the first systematic multi-pandemic transfer framework, but that positioning needs more careful qualification.  
   This matters because at ICLR, novelty is not just “I combined two ideas in a new application,” it is also whether the paper clearly differentiates itself from adjacent ML methods that do transfer or hybrid mechanistic learning in closely related settings.

10. **The claims around interpretability are overstated.**  
    Predicting DELPHI parameters does not automatically make the system interpretable if the mapping from short noisy trajectories and metadata to those parameters is itself unconstrained and if the parameter estimates are not shown to be identifiable or calibrated. The discussion on **Page 9** suggests actionable epidemiological insight from Figure 5, but what is actually shown is that HG-DCM and DELPHI yield different parameter distributions, with Wilcoxon \(p<0.05\). Statistical difference is not the same as epidemiological validity.  
    In fact, because DELPHI is fitted independently per location and HG-DCM shares information across diseases and countries, differences are expected. The relevant question is whether HG-DCM’s inferred parameters correspond better to known intervention timings, transmissibility ranges, or out-of-sample realism. The paper does not provide that validation.

11. **Presentation is reasonably readable overall, but there are several places where precision slips enough to hurt confidence.**  
    Examples include inconsistent naming such as “Residual Network,” “Residual CNN,” and “ResNet,” unclear tensor notation on **Page 4** where the input is given as \([L,N,D]\) instead of the more standard batch-first convention, and grammatical overstatements around results. More seriously, some references are incomplete or oddly formatted, and several claims depend on appendix details that are not available in the main text, such as metadata lists and baseline setups. These are not fatal alone, but together they make the paper feel less settled than the confident framing suggests.

## Questions
1. **What exactly is the learned output \(\hat{\theta}\)?**  
   Is it a single 12-dimensional static DELPHI parameter vector per training example, or a time-indexed sequence/function of parameters? Please clarify the dimensionality and parameterization explicitly, and explain how this aligns with the repeated description of “time-varying parameters” and “parameter evolution.”

2. **How is the loss in Equations (3)-(5) implemented numerically?**  
   Please specify how the MAPE term handles \(C_{ij}=0\) or very small values. If an \(\epsilon\) term is used, what is it? Also clarify the indexing convention in the sums and whether the denominators should be \(n_P(t+v+1)\) and \(n_C(t+1)\) under the written notation.

3. **Can the authors disentangle the contributions of historical outbreaks and metadata?**  
   A more convincing ablation in rebuttal would separate: (i) no history but with metadata, (ii) history without metadata, and (iii) full HG-DCM. That would materially increase my confidence that the gains come from cross-disease transfer rather than simply from extra side information.

4. **Can the authors provide broader matched-baseline evaluation beyond Table 1?**  
   Since the main story is broad generalization across many locations, stronger evidence would include more locations or a clearer explanation of why only two locations are comparable for external baselines. If broader matched comparisons are impossible, please narrow the claims correspondingly.

5. **Why is the 4-week mean MAE in Table 2 so poor for HG-DCM?**  
   This looks like an important failure mode. Please analyze which locations drive this tail behavior, and whether these errors are associated with specific source diseases, metadata patterns, or training instabilities. This would help evaluate the claimed improvement in stability.

6. **How are source and target splits constructed across locations and outbreaks?**  
   Please clarify whether hyperparameter tuning, early stopping, and model selection use a validation split that is fully separated from the final reported test locations. Given the small and heterogeneous multi-pandemic dataset, leakage across repeated windows from the same location is a real concern unless the splitting protocol is very carefully defined.

7. **Can the authors better justify the interpretability claim?**  
   For example, do inferred quantities such as \(t_{\mathrm{med}}\) or intervention-related parameters correlate with known policy timings or known epidemic characteristics better than DELPHI’s fitted parameters? A validation of epidemiological plausibility would strengthen Figure 5 substantially.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics flag is necessary based on the main paper. The work is on aggregate public-health forecasting and does not appear to involve individual-level private data or human-subject experimentation in the submitted text.

## Soundness Rating
2: fair. The core idea is plausible and some experiments are suggestive, but the evidence does not fully support the strength of the claims, and several methodological details around the objective, parameterization, and evaluation protocol are insufficiently specified.

## Presentation Rating
2: fair. The paper is readable and the main intuition comes across, with helpful figures such as Figures 1, 2, and 4, but there are important ambiguities in notation, claims, and experimental positioning.

## Contribution Rating
2: fair. The problem is important and the historical-transfer angle is interesting, but the empirical validation and differentiation from adjacent hybrid / transfer approaches are not strong enough for me to view this as a clear ICLR-level contribution in its current form.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see a promising idea here, and there is enough signal that historical guidance may indeed help reduce some early-stage failures of compartmental fitting. However, the current paper overclaims relative to the evidence, the benchmark comparisons are too narrow, the ablations do not cleanly isolate the source of improvement, and the mathematical/objective specification needs tightening. I am leaning negative because these are core scientific issues rather than just polish.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the equations, tables, and figures carefully, but some implementation details needed for full certainty are absent from the main text.