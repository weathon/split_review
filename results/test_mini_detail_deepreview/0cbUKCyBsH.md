Now I have sufficient calibration. Let me produce the final consolidated review.

## Summary

This paper argues that the performance plateau in time series forecasting stems from the "self-stimulation" assumption (predicting the future solely from past values). It proposes Influence-Aware Time Series Forecasting (IATSF), a paradigm that conditions forecasts on external textual information. The paper provides a control-theoretic analysis (Propositions 2.1 and 3.1 showing irreducible error from unobserved influences), a new "leak-free" benchmark with temporally-synced textual influences, and FIATS—a lightweight LLM-free model with Channel-Aware Adaptive Sensitivity Modeling (CASM) and Channel-Aware Parameter Sharing (CAPS). Experiments on synthetic, atmospheric physics, traffic, and gaming datasets show FIATS outperforming self-stimulated baselines.

## Strengths

1. **Well-motivated paradigm shift.** The core thesis—that ignoring external influences creates a mathematical ceiling on forecasting accuracy—is compelling and clearly articulated. The paper correctly identifies that even billion-parameter foundation models are constrained by the self-stimulation assumption, which the FM Toy experiment (Table 1) convincingly demonstrates: FIATS achieves MSE 0.003–0.027 while all self-stimulated models, including Chronos-L and MOIRAI-L, fail to approach the theoretical lower bound.

2. **Clean architectural design with interpretability.** FIATS's CASM mechanism (channel-specific cross-attention over textual influence embeddings) and CAPS (channel-conditioned decoder) are well-motivated from the control-theoretic framing. The attention maps in Figures 3 and 5 demonstrate interpretable behavior—different layers attend to different parts of weather reports (date/time, pressure, humidity) for different channels. The ablation study (Table 3) cleanly separates the contributions of influence text, channel descriptions, and embedding choice.

3. **Principled benchmark design for multimodal TSF.** The paper's leak-free benchmark design principles (Section 4.1)—requiring independently evolving influences, temporal synchronization, and prohibiting future state leakage—address real limitations in prior multimodal datasets (Liu et al., 2024a; Jin et al., 2023). The inclusion of toy systems, real-world physical systems, and human-driven business systems provides a structured validation path.

4. **Robustness across text embedding models.** Table 3 shows stable performance when switching between OpenAI embeddings, MiniLLM, and mpnet, suggesting FIATS does not depend on a specific text encoder.

## Weaknesses

### Fatal

None.

### Major

1. **Conceptual issue with the Atmospheric Physics dataset: the "influence" is partially a forecast of the target.** The paper's Section 4.1 states that influences must be "independently evolving—external factors that influence the system but are not themselves outcomes of it." However, for the Atmospheric Physics dataset, the target variables (solar radiation SWDR, air pressure, dew point, etc.) *are* weather variables, and the "influence" text is a weather forecast that directly describes expected weather. A forecast text mentioning "clear skies" is not an independent external influence on solar radiation—it is a qualitative description of the same physical quantity. This weakens the claim that FIATS's large gains (36% MSE reduction) come from "principled influence modeling" rather than simply receiving additional information about the future that baselines lack. The paper explicitly calls the benchmark "leak-free," but this design choice is in tension with that label.

   **Why it matters:** This does not invalidate the whole paper—the NYC Traffic dataset (weather influencing traffic, not weather predicting weather) and the GAUD dataset (developer logs as influences) are cleaner. But the paper's strongest real-world results come from the Atmospheric Physics dataset, and this conceptual confusion undermines the core narrative that the benchmark is leak-free and that gains are attributable to the IATSF paradigm rather than to privileged access to a target-adjacent forecast.

2. **Insufficient comparison against methods that also receive the same influence information.** The paper compares FIATS against self-stimulated baselines that cannot access external information. The only multimodal baseline (TimeLLM) appears to perform much worse, but it is not clear whether TimeLLM receives the same textual influences or how it is adapted for this task. Missing comparisons include: (a) a variant of FIATS that uses numerical weather variables as exogenous inputs via a simple linear projection, (b) ChronosX (cited in the paper) which handles exogenous variables, (c) ARIMAX or similar classical methods using weather regressors, or (d) a simple concatenation of weather text embeddings with time series patches. Without these controls, the impressively large margins in Table 1 may partly reflect the information advantage of having a weather forecast rather than the specific architectural contributions of FIATS.

   **Why it matters:** The paper's title and narrative claim that "influence-aware forecasting" *as a paradigm* is the primary path forward. To substantiate this, the paradigm must be shown to beat other methods that also use the same information, not just methods that are deliberately starved of it.

3. **Theoretical contribution is standard probability/control theory presented as novel.** Propositions 2.1 and 3.1 state that (a) self-stimulated models converge to the conditional expectation over unobserved influences with an error floor determined by influence variance, and (b) incorporating a known influence reduces error by the variance attributable to that influence. These are direct consequences of the law of total expectation and variance decomposition—elementary results that follow from assuming influences are independent random variables. The paper does not derive any non-trivial bound, structural insight, or practical convergence rate that would justify describing this as a "control-theoretic analysis" that "formally proves" a "hard barrier." This does not make the paper incorrect, but it inflates the novelty of the theoretical framing.

4. **GAUD dataset evaluation is incomplete.** The GAUD results appear only as a figure (Figure 4) showing improvement over PatchTST, without the comparable numerical tabulation found in Table 1. Only PatchTST and TimeLLM are compared, not the full set of baselines. The paper also does not clarify whether the developer logs are forward-looking (planned updates) or purely historical, which is relevant to the leakage question.

### Minor

1. **The self-stimulation assumption conflates architecture and information.** Many self-stimulated models (e.g., PatchTST, Chronos) are evaluated in a *zero-shot* setting (no fine-tuning on the target dataset), while FIATS is trained on each dataset. This means the comparison conflates "having influence information" with "being fine-tuned on the target domain." A fairer comparison would include fine-tuned versions of self-stimulated baselines where permitted.

2. **Limited description of channel descriptions (Desc).** The paper mentions channel description embeddings $Desc \in \mathbb{R}^{CN \times D}$ are used as queries in CASM but does not specify how these are constructed—are they hand-crafted text (e.g., "atmospheric pressure"), learned embeddings, or variable names processed through a text encoder? This matters for reproducibility.

### Trivial

- None.

## Nice-to-Haves

- The paper's paradigm would be strengthened by a dataset where the influence is clearly external and not a forecast of the system (e.g., economic policy announcements affecting market data, or satellite launch schedules affecting communication network demand).
- A bound on the gap between the optimal influence-aware predictor and the optimal self-stimulated predictor that depends on a measurable quantity (e.g., mutual information between influence and target) would add real theoretical depth beyond variance decomposition.
- The FM Toy experiment is the cleanest validation; the paper could lead with this more prominently to establish the paradigm before moving to real-world datasets.

## Removed Points

- **Harsh critic's framing of the weather forecast issue as "fatal" and "structural"** — The issue is real and major, but it affects primarily the Atmospheric Physics dataset (and to a lesser degree NYC Traffic, which uses weather as a genuinely external influence on a different system). The FM Toy, Electricity Utility, and GAUD datasets do not share this problem. The paper's core claims are not invalidated, only weakened. Demoted from Fatal to Major.

- **Criticism of theory as "too shallow to anchor the paper's claims"** — Retained as Major #3 but softened. The propositions are elementary, but their application to frame the self-stimulation problem in time series forecasting is a valid contribution even if the math itself is not novel.

- **Missing related works** — Removed per protocol (cannot confirm existence of missing citations).

- **Reproducibility nitpicks (what embedding model, specific masking scheme)** — These are reasonable concerns but minor; merged into Minor #2.

- **Strength Finder's generic strengths ("addresses an important problem")** — Removed. Kept only concrete, evidence-grounded strengths.

- **Strength Finder's claim about the benchmark being "explicitly leak-free"** — This conflicts with verified Weakness #1, so it is removed (per rule: when strength and weakness disagree, weakness wins).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation that the authors themselves missed—the core tension (weather forecasts as influences for weather variables) is identified but not resolved.

## Suggestions

1. **Re-run the Atmospheric Physics experiment with proper controls.** At minimum: (a) add a FIATS variant where the influence text is replaced by scrambled or time-shifted weather text (to confirm it's the *content* not the *presence* of text that matters), (b) compare against a simple model that concatenates numerical weather forecast variables (temperature, pressure, humidity) as exogenous features. This would disentangle the paradigm from the information-access advantage.

2. **Present GAUD results with the same level of detail as Table 1**—full numerical results with all baselines and standard deviations.

3. **Clarify the framing.** Either: (a) acknowledge that for Atmospheric Physics, weather forecasts are partially a description of the target and argue why this is still a legitimate influence (e.g., the forecast is a coarse textual summary rather than precise numerical values, and the model must learn the mapping), or (b) replace this dataset with one where the influence is clearly external.

4. **Add fine-tuned self-stimulated baselines** to isolate the effect of influence information from the effect of domain-specific training.

5. **Provide explicit details on channel description construction** in the main text or appendix.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries anchored different score bands for time series forecasting papers:
- Band < 3.5: Papers scoring 2.0–3.0. These were method papers with weak contributions or evaluation issues.
- Band 3.5–7.5: Papers scoring 4.25–5.25. GIFT-Eval (5.25, Reject) was a large benchmark with solid work but unclear insights. Financial Forecasting (4.50, Reject) had novelty and evaluation concerns.
- Band > 7.5: Papers scoring 8.0 (all Accept). FITS (8.0), ACSSM (8.0), etc. were clean, well-executed papers.

**Initial bracket:** 4.0–6.5.

**Round 2 (Narrowing):** Two queries targeting topic-similar papers in this range:
- GIFT-Eval (5.25, Reject): Comprehensive benchmark but the paper under review is more novel (new paradigm + model) and has a stronger theoretical framing. However, GIFT-Eval's evaluation is more thorough, while the current paper has a significant evaluation weakness. The papers are comparable in quality, with the current paper having higher ambition but a more impactful weakness.
- TEST (6.00, Accept): TS+LLM method with well-executed experiments. The current paper is comparable in technical novelty and has better interpretability, but TEST does not have the same evaluation concern. The current paper is weaker.
- Financial Forecasting (4.50, Reject): Novelty and evaluation concerns. The current paper is stronger in both novelty and scope.
- Time-LLM (7.00, Accept): Strong, well-written paper with solid experiments. The current paper is less thoroughly executed.

**Final placement:** The paper sits between GIFT-Eval (5.25, Reject) and TEST (6.00, Accept)—closer to 5.0. It has genuine novelty (paradigm shift, clean architecture, well-motivated benchmark) that lifts it above papers scoring 4–4.5. However, the evaluation issue (weather forecast as influence for weather variables) and the shallow theoretical contribution prevent it from reaching the 6+ level. The most comparable anchor is GIFT-Eval (5.25), but that paper's weakness was incremental contribution while this paper's weakness is a more central evaluation concern, so 5.0 is appropriate.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>