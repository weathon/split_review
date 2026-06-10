## Summary

This paper proposes OracleMamba, a stock prediction framework combining a dynamic market-guided module (which fuses objective market data with GPT-O1-generated sentiment from analyst reports) for short-term forecasting and a "SelectiveMamba" module (with a Time-Spectral State Space layer and a 3D hierarchical scan mechanism) for long-term forecasting. The method is evaluated on Chinese stock indices CSI300 and CSI800 against several baselines including MASTER, reporting relative improvements of 56% in ranking metrics and 74% in portfolio-based metrics.

## Strengths

- **Integration of subjective sentiment into market-guided gating**: The paper explicitly identifies a limitation of prior work (e.g., MASTER) — the neglect of subjective market sentiment — and proposes a concrete mechanism to incorporate GPT-O1-generated sentiment estimates alongside objective market indicators into a dynamic feature modulation scheme (Section 3, Market State Encoding; Equations 1–3). This is a well-motivated architectural extension.

- **Statistical rigor in evaluation**: The paper reports two-tailed t-tests at significance levels of *p* < 10⁻² and *p* < 10⁻⁴, repeats each experiment five times with random initialization, and tunes hyperparameters from specified ranges for all baselines (Section 4, Implementation). This is above the norm for stock prediction papers.

## Weaknesses

### Major

1. **Core method is underspecified and not reproducible as written.** The paper's central technical components are defined at a level that prevents independent reconstruction:
   - The TSSS module is claimed to be parameterized by (Δ, *A*, *B*, *C*) following SSM conventions, yet **Δ never appears in any equation**. The DSE is given as *C e^(A(t−s))*B*, a continuous-time kernel with no discretization step shown; the DTE is a standard LSTM cell. How these two components combine into a single state-space model, and how the claimed "discretization of temporal dynamics" (line 71) operates, is never explained.
   - The 1DScan and 2DScan operations in the 3D scan layer are **never mathematically defined**. Equations (lines 91) show only sequential composition (e.g., TS = 2DScan\_Time(1DScan\_Time(...))) but do not specify whether a scan is an SSM recurrence, a convolution, an MLP, or an attention mechanism. Four scanning techniques (cross-dimension, bidirection-dimension, inner-dimension, skip-dimension) are listed and illustrated in Figure 2 but are never defined algorithmically or used in experiments.
   - The fusion layer is described as "a simple mlp-based fusion module for simplicity" (line 96) with zero architectural details — no layer count, hidden size, or activation function.
   
   This level of underspecification means the paper's core technical contribution cannot be evaluated or reproduced. The reader cannot determine what the proposed method actually is.

2. **Key supporting experiments are missing, leaving the paper's central claims unsubstantiated.** The paper claims that (a) the market-guided module handles *short-term* prediction, (b) the SelectiveMamba module handles *long-term* prediction, and (c) the sentiment features drive improvements over MASTER. None of these claims are tested:
   - **No variation of prediction horizon.** Only *d* = 5 days is evaluated; the claimed short-term/long-term specialization remains entirely unsupported.
   - **No ablation of the market-guided gating module** (OracleMamba without gating vs. with gating).
   - **No ablation isolating the sentiment component** (OracleMamba with vs. without GPT-O1 features, or MASTER augmented with the same sentiment features). Without this, it is impossible to tell whether the Mamba-based architecture or the sentiment data drives the reported gains.
   - **No comparison against vanilla Mamba or S4**, despite "Mamba" appearing in the paper's title and being a central motivation. This is the most natural control to justify the architectural choices.
   - **No ablation of TSSS components** (DSE only, DTE only, both).

3. **Novelty relative to the key baseline MASTER is not convincingly demonstrated.** The market-guided gating mechanism (Equations 1–3) is structurally nearly identical to MASTER's market-index-guided gating (a linear projection of market context, softmax, element-wise multiplication with features). The paper acknowledges the connection but does not clearly differentiate. The only clear architectural addition beyond MASTER is the sentiment analysis component, yet no experiment isolates its effect. The reader cannot determine whether the reported improvements come from the architectural changes (SSM vs. Transformer) or the additional sentiment data.

### Minor

- **Ablation of scanning dimensions presented as prose only.** The 1D/2D/3D scan comparison (Section "1D Scan, 2D Scan and 3D Scan") is described entirely in qualitative prose with no numerical results, standard deviations, or tabular presentation. Statements like "noticeable improvement in IC" and "AR increases steadily" are not evidence. The results are referenced to Figure 3 (an image) but no precise values can be extracted.

- **Absolute metric values not reported in text.** The paper reports only relative improvements ("56% in ranking metrics and 74% in portfolio-based metrics") without stating absolute IC, ICIR, RankIC, RankICIR, AR, or IR values for OracleMamba or any baseline. In stock prediction, IC values are typically 0.02–0.08; a "56% improvement" could mean 0.05→0.078 or 0.02→0.031 — qualitatively different claims. Absolute values should be in the text, not only in a table image.

- **Sentiment component lacks reproducibility details.** The use of GPT-O1 for sentiment extraction is described without specifying the model version (o1-preview vs. o1-mini), the prompt used, text preprocessing steps, or how raw output is converted to a numerical feature vector. This makes an otherwise interesting component irreproducible.

- **Efficiency claims are unmeasured.** The paper claims efficiency improvements over Transformers due to SSM's linear complexity (abstract, introduction) but reports no runtime, parameter count, FLOPs, or inference-time measurements anywhere.

- **No discussion of limitations.** The conclusion lists no failure cases, sensitivity analyses, or scenarios where the method might underperform.

### Trivial

None.

## Nice-to-Haves

- A comparison against MASTER augmented with the same GPT-O1 sentiment features would cleanly isolate whether value comes from the architecture or the data.
- Varying the prediction horizon (*d* = 1, 5, 10, 20) and analyzing which module's output dominates at each horizon would directly test the claimed short-term/long-term specialization.

## Removed Points

These points were raised by the reviewers or strength finder but are removed for the following reasons:
- **"Table 1 is an image whose values cannot be inspected"** — In the original PDF the table image would be readable; this is a parser artifact. However, the valid core point (absolute values not reported in text) is retained above.
- **"DTE equation has missing parentheses / formatting errors"** — Parser artifact; the original PDF would render correctly.
- **"Missing discussion of related SSM variants (S4's HiPPO, Fourier-based SSMs)"** — Per policy, missing related works are not raised because external confirmation is unavailable.
- **"No code release commitment"** — Per policy, demanding code release for a submission is outside the scope of reviewer criticism.
- **Strength Finder's claim of "empirical evidence that 3D scan outperforms 1D/2D"** — Dropped because it conflicts with the verified weakness that the ablation is presented as qualitative prose with no numerical values.
- **Strength Finder's claim of "TSSS jointly modeling temporal and spectral features"** — Dropped because it conflicts with the verified weakness that the TSSS specification is incomplete and internally inconsistent.

## Novel Insights

The reviewers' input collectively surfaces a pattern worth noting: the paper describes an interesting high-level framework (market sentiment + multi-dimensional scanning + spectral-temporal SSM) that reads as plausible and well-motivated, but collapses under scrutiny because the individual components are never concretely specified. The gap between the appealing abstract architecture and the absent algorithmic detail is unusually wide. This suggests the paper may be in an early, concept-stage form that needs significant technical fleshing out before it can be assessed as a research contribution.

None beyond the paper's own contributions (which are themselves difficult to fully evaluate due to the specification issues).

## Suggestions

1. Provide a complete, self-contained mathematical specification of the 1DScan and 2DScan operations (what form does the scan take — SSM recurrence, convolution, MLP over sliding windows?).
2. Clarify how the TSSS integrates DSE and DTE into a state-space model: show the discretization step that relates (Δ, A, B, C) to the actual computation, and explain how the LSTM-based DTE fits within the SSM formalism.
3. Report absolute numerical values (with standard deviations) for all metrics on all experiments, including the scan-dimension ablation, either in tables or in the main text.
4. Add ablations for: (a) w/ vs. w/o market-guided gating, (b) w/ vs. w/o GPT-O1 sentiment features, (c) TSSS components (DSE only, DTE only, both), (d) comparison against vanilla Mamba/S4, (e) varying prediction horizons to test the claimed short-term/long-term specialization.
5. Provide prompt details for GPT-O1 sentiment extraction to enable reproducibility.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>