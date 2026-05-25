Below is my consolidated final review, based on careful cross-checking of every reviewer claim against the paper itself.

---

## Summary

HG-DCM introduces a framework that uses a deep neural network to learn the mapping from early-stage epidemiological signals and metadata to the parameters of a compartmental model (DELPHI). The network is trained jointly on historical pandemics (Ebola, SARS, Dengue, seasonal influenza) and the early observations of a novel outbreak, so that the historical data regularizes the parameter estimates when current data is scarce. Experiments on early COVID‑19 forecasting (2–8 weeks of training data, 12‑week forecast horizon) across 258 global locations show that HG‑DCM reduces median MAE relative to DELPHI by 32–38% in the earliest stages and produces substantially fewer overshooting predictions. The idea of cross‑disease transfer for cold‑start pandemic forecasting is novel, the method is clearly described, and the ablation study convincingly isolates the contribution of historical data.

## Strengths

1. **First systematic cross‑disease temporal transfer for pandemic forecasting**  
   The paper is the first to build a framework that *systematically* trains on multiple biologically distinct pandemics (Ebola, SARS, Dengue, influenza) to predict the trajectory of a novel outbreak. Earlier transfer approaches in epidemiology either borrow parameter priors from a single related outbreak or transfer spatially; none assemble a multi‑pandemic training set coupled with a deep compartmental architecture. (Section 1)

2. **Consistent and statistically significant error reduction in the cold‑start phase**  
   HG‑DCM reduces median MAE by 38.2% over DELPHI with only 2 weeks of training data, 32.4% at 4 weeks, and maintains lower or comparable error across longer windows (Table 2). The ablation comparison against T‑DCM (same architecture, no historical data) shows that HG‑DCM wins on median MAE at every training‑window length, directly attributing the gain to historical context rather than model design. (Section 3.2.2)

3. **Substantially fewer overshooting events, demonstrating improved stability**  
   Overshooting—predicting cumulative cases more than 5× the observed value—is formally quantified. DELPHI produces far more overshoots than HG‑DCM at every training‑window length (Figure 4a). The paper includes a concrete case (USA, 8‑week window) that visually contrasts DELPHI’s overfitting trajectory with HG‑DCM’s stable forecast. (Section 3.2.2)

4. **Preserved interpretability with statistically validated parameter estimates**  
   HG‑DCM outputs the 12 epidemiologically meaningful DELPHI parameters rather than black‑box predictions. The parameter distributions (infection rate, median day of action, etc.) are significantly different from DELPHI’s (Wilcoxon, p < 0.05) and are tighter, less biased by early noise. This shows the framework retains the interpretability of compartmental modeling while improving robustness. (Section 3.2.3, Figure 5)

5. **Construction of a multi‑pandemic dataset and tailored augmentation strategies**  
   The authors compiled a new dataset of daily/weekly case data for COVID‑19, Ebola, SARS, Dengue, and seasonal influenza since 1990, with epidemiological and country‑level metadata. The window‑shift augmentation for historical pandemics and block‑masking for the current pandemic are explicitly designed for the cold‑start setting. (Section 2.2, Section 3.1.1)

## Weaknesses

### Fatal

None. The core contribution—that historical pandemics can regularize early‑stage forecasting of a novel disease—is demonstrated by the evidence. The issues below limit the paper’s scope and framing but do not invalidate its central finding.

### Major

1. **Mismatch between the breadth of the claims and the scope of the evaluation**  
   The abstract, introduction, and conclusion frame HG‑DCM as establishing a “new paradigm” that transfers knowledge to “a newly emerging one” (any novel pathogen). Yet the evaluation targets *only COVID‑19* as the held‑out disease. The historical diseases (Ebola, SARS, Dengue, influenza) serve as the source domain, and COVID‑19 is the single target. A paradigm claim for *cross‑disease* transfer would be substantially strengthened by at least one leave‑one‑disease‑out experiment (e.g., train on COVID‑19 + three historical diseases, test on the fourth). The Limitations section (Section 4) discusses data granularity and missing mortality but does not acknowledge this single‑target limitation, which is a significant oversight given the paper’s sweeping language.  
   *Why it matters*: Without evidence on a second target disease, the paper cannot distinguish between “historical data helps for COVID‑19” and “the method generalizes to novel pathogens.” The framing should be tempered to match the evidence, or additional experiments should be provided.

2. **Competitive evaluation is thin and contains an unexplained failure case**  
   The SOTA comparison (Table 1) covers only two locations (USA and Massachusetts). The paper explains this by citing code/data limitations, which is a valid practical constraint, but the resulting evidence base is narrow. More importantly, on the USA 4‑week task HG‑DCM loses to EiNNs by a factor of 3.5 (2,548,004 vs. 729,091 MAE). The paper’s text (“consistently achieves lower MAE in most tasks”) accurately describes the majority outcome, but it does not attempt to explain this large failure. Why does the historical prior harm performance so dramatically on this particular task? The omission weakens the claim that the method is robust and leaves the reader wondering about hidden failure modes.  
   *Why it matters*: A single clear counter‑example in a two‑location evaluation demands analysis. Without it, the empirical support for “consistent improvement” is incomplete.

### Minor

1. **T‑DCM’s counterintuitive degradation is unexplained**  
   In Table 2, T‑DCM’s median MAE *increases* monotonically with more training data (2745 → 2799 → 3101 → 4335 as the training window grows from 2 to 8 weeks). This is the opposite of what a well‑functioning learning system should do. The paper mentions overfitting in passing but provides no analysis. Is this caused by a selection bias in the surviving locations? An optimization instability? A metric artifact? Leaving this anomaly unexamined undermines confidence in the experimental pipeline.  
   *Why it matters*: If T‑DCM’s pathology is real, it is arguably the paper’s strongest evidence for the value of historical regularization—but it should be understood, not merely reported.

2. **Hyperparameter values (β, α) are not reported in the main text**  
   The loss function balance between historical and current pandemic data is controlled by β (Equation 5), and the MAE/MAPE trade‑off by α (Equations 3–4). These are the central knobs of the method. Neither value appears in the main paper. Without knowing β, the reader cannot assess how aggressively the model leans on historical data. A sensitivity analysis would be especially valuable because in a real emerging pandemic β could not be tuned on a held‑out set.  
   *Why it matters*: Reproducibility and practical applicability are reduced. (Note: these values may appear in the appendix, which is not accessible to this review; if they do, this point becomes a presentation issue rather than a gap, but the lack of a sensitivity analysis remains.)

3. **Limited comparative baselines from the hybrid‑model family**  
   The Related Work section discusses DeepGLEAM, EpiFNP, and DSA‑BEATS as relevant hybrid methods. The paper compares against only GradABM and EiNNs and offers a generic justification (code/data unavailability for early‑stage forecasts). The exclusion is understandable but leaves the comparison set feeling selective. At minimum, a clearer statement of which specific hybrid baselines were attempted and why they failed would strengthen the evaluation.  
   *Why it matters*: Readers familiar with this literature will wonder how HG‑DCM compares to these closely related approaches.

4. **Only 4 of 12 DELPHI parameters are discussed in the main body**  
   The parameter analysis (Figure 5) shows only infection rate (α), median day of action (t_med), rate of action (r_s), and death rate (t_death). The remaining 8 parameters are deferred to the appendix. No selection criterion is given, and effect sizes are not reported alongside the Wilcoxon p‑values.  
   *Why it matters*: A quantitative link between parameter shifts and forecast error improvements would be more informative than a purely descriptive comparison.

### Trivial

- The forecasting‑window length **v** (used in Equation 3) is referred to in prose as “the length‑v forecasting window” but is never numerically defined in the main text (the experiments use a 12‑week forecast horizon, so v presumably equals 12 weeks minus the training window, or a fixed period). This is a small clarity issue.

## Nice-to-Haves

- **Leave‑one‑disease‑out cross‑validation.** Replacing “history + COVID‑19” training with a scheme that holds out one historical disease at a time would directly validate the cross‑disease generalization claim.
- **Sensitivity analysis for β.** Reporting performance across a range of β values (including β = 0 and β → ∞) would show whether the method is robust or requires fragile tuning.
- **Per‑disease contribution analysis.** Which historical diseases drive the improvement? Does influenza dominate, or do all four contribute? This would shed light on *what* is being transferred.
- **Reporting MAPE or sMAPE alongside MAE.** Since the loss function includes MAPE, reporting it in the results would give a more complete picture, especially given that MAE on cumulative cases is dominated by large‑population locations.
- **Analysis of the USA 4‑week failure.** Understanding why HG‑DCM performs poorly on this specific task would improve the method and strengthen the paper.

## Removed Points

The following points from the input reviews were removed with justification:

- **LDoA label‑leakage concern** (harsh critic): The paper explicitly states “this retrospectively calculated LDoA is never used during inference on the current pandemic, preventing look‑ahead bias and information leakage.” The reviewer’s claim that the paper “does not discuss whether this strategy could introduce artifacts” is factually incorrect. **Removed** (strawman / addressed by the paper).
- **“Consistently” language nitpick** (harsh critic): The paper says “consistently achieves lower MAE in **most** tasks.” The reviewer omitted the qualifier “most” when quoting. The phrasing is accurate about the results (6/8 comparisons won). **Removed** (misrepresentation).
- **“Paradigm” overclaim as fatal** (harsh critic): The framing is ambitious but not invalid. The paper clearly grounds its claims in COVID‑19 results and is describing a new *approach*. The overclaim is a real weakness (kept as Major #1) but is not fatal. The reviewer’s strongest language depended on demanding validation the paper never claimed to provide at this stage. **Demoted** from fatal to major.
- **β unreported as critical/fatal** (harsh critic): The value of β may appear in the appendix (which is stripped). The lack of a sensitivity analysis is a valid concern; the lack of a reported value cannot be verified as a gap from the main text alone. **Demoted** from critical to minor.
- **“v not defined”** (harsh critic section note): This is accurate but trivial. **Moved** to trivial.
- **Generic strength** (Strength Finder): “Tailored data‑augmentation strategies for the cold‑start problem” is a method description rather than a demonstrated strength. The dataset construction and augmentation are genuine contributions (merged into Strength 5). **Dropped** as standalone strength.

## Novel Insights

None beyond the paper’s own contributions. The key insight—that pandemics with distinct biology share macroscopic dynamic patterns that can be captured by a shared parameter‑mapping network—is the paper’s own central thesis.

## Suggestions for Improvement

1. **Tone down the framing.** Replace “establishes a new paradigm” with “introduces a cross‑disease temporal transfer framework and demonstrates its feasibility on COVID‑19.” Add the single‑target limitation explicitly to the Limitations section.
2. **Add a leave‑one‑disease‑out experiment.** Even a simple version (e.g., hold out seasonal influenza, train on the rest + COVID‑19, test on influenza) would substantially strengthen the generalizability claim.
3. **Report β and α values in the main paper and include a sensitivity analysis.** Show performance at β = 0 (current‑pandemic‑only), the chosen value, and a large β (history‑dominated).
4. **Analyze the T‑DCM degradation.** Is it a real overfitting phenomenon or an artifact of the evaluation setup? A brief investigation would resolve the concern.
5. **Explain the USA 4‑week failure.** What distinguishes this task from the seven where HG‑DCM wins? This could reveal important boundary conditions for the method.
6. **Add MAPE or sMAPE to the result tables** to balance the population‑size bias inherent in MAE on cumulative cases.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>