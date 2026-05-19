- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6
Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes a Mixture-of-Experts (MoE) framework for continual traffic forecasting under evolving networks where sensors are added over time. Traffic sensors are clustered by traffic pattern (independently of geography), each cluster is assigned an expert with a VAE-based reconstructor and a predictor, and three continual-learning mechanisms (reconstruction-based consolidation loss, forgetting-resilient sampling via VAE generation, and reconstruction-based replay) are introduced. Evaluation on a real-world 7-year streaming dataset (PEMSD3-Stream) is presented.

## Strengths

- **Convincing ablation study showing all three mechanisms contribute.** Table \ref{tab:componet_analysis} shows that removing any single component (consolidation loss, sampling, or replay) degrades metrics across all time horizons. For 60-min MAE: full proposed 17.20, w/o Consol 19.03, w/o Sampling 18.14, w/o Replay 18.47. This provides controlled evidence for the necessity of each mechanism.

- **Consolidation loss prevents expert collapse over years.** Figure \ref{fig_heatmap} directly contrasts sensor allocation across experts with and without consolidation loss. With consolidation loss, sensors remain evenly distributed across 4 experts from 2011–2017; without it, nearly all sensors collapse to a single expert after the first year. This visually and quantitatively supports the claim that the consolidation loss mitigates catastrophic forgetting.

- **Graph structure learning is well-motivated for the continual learning setting.** Section 4.2.1 identifies two concrete problems with predefined geographical graphs in this scenario (handling newly added nodes efficiently and lack of graph structure in synthetically generated replay data) and adopts a learnable adjacency matrix via Gumbel softmax + diffusion convolution to address both.

- **Generative gating reduces memory requirements.** The reconstruction-based gating (Equation after line 219) uses only current-task data plus VAE decoders to weight expert predictions, eliminating the need to store historical features from all previous sensors — a clean alignment with continual learning's minimal-memory goal.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguity about which predictor architecture is used in the main evaluation.**  
  Section 4.2.1 describes a custom predictor: "a single Diffusion Convolutional Layer... followed by two 1D-Conv layers" (line 215). Yet Table \ref{tab:60min-avg}'s caption says "Prediction performance averaged over time horizons **using the TrafficStream predictor** across various models" (line 309). The table includes Retrained-TFMoE, Static-TFMoE, Expansible-TFMoE, and proposed(1%) — all TFMoE variants. If these variants all use the TrafficStream predictor backbone, then the custom predictor described in Section 4.2.1 is never evaluated on its own in the main results, creating a disconnect between the method description and the experimental evidence. If the variants use the paper's own predictor, the caption is misleading. The paper also says "our predictor is simplified to validate the effectiveness of our proposed framework" (line 215), implying the custom predictor is used. This ambiguity must be resolved for the reader to understand what exactly is being compared.

- **Metric calculation differs from prior work, making the PECMP comparison unreliable.**  
  Footnote \ref{footnote1} (line 319) acknowledges that prior work averages 5-minute, 10-minute, and 15-minute predictions for a "15-minute" metric, while this paper uses only the 15-minute prediction. PECMP values (marked with *) are taken from the original PECMP paper, which uses the different calculation method. The footnote says this "may account for any discrepancies in numeric values." Since PECMP is one of the two main baselines and the claimed superiority over it is a headline result, this acknowledged discrepancy weakens the evidence — a delta of a few percent could be due to the metric shift alone. The paper would be strengthened by re-evaluating TrafficStream (whose code is available) with consistent metrics and reporting the numerical shift.

### Minor

- **Single dataset evaluation.** All experiments are conducted on PEMSD3-Stream. While this is a multi-year streaming dataset, generalizability claims are unsubstantiated without at least one additional streaming scenario (e.g., another PeMS district or a synthetic streaming construction).

- **No hyperparameter sensitivity analysis.** Essential parameters — number of experts \(K\), sampling size \(n_s\), replay size \(n_r\), consolidation loss weight \(\beta\) — are not studied. These influence both performance and memory footprint and should be characterized for practical deployment.

- **Synthetic data quality is not validated.** Section 4.2.4 generates data from VAE decoders for replay, but no analysis (reconstruction examples, t-SNE comparison, distributional similarity metrics) is provided to confirm that the generated data is both realistic and sufficiently diverse, rather than degenerate or overly repetitive.

### Trivial
- The word "the" is doubled in "assign weights to the the predictions" (line 219).

## Nice-to-Haves
- Comparing against a non-MoE single predictor with the same three continual-learning components would isolate the benefit of the MoE architecture itself.
- Reporting the numerical shift in metrics caused by the differing calculation convention (5-minute averaging vs. single-step) would make the PECMP comparison interpretable rather than hand-waved.
- Including a discussion of the failure mode where a new sensor exhibits a genuinely novel pattern not aligned with any existing expert (the method would force it into the closest match, potentially degrading performance).

## Removed Points
**These points are flagged to be removed; treat them with caution:**

- Critic's claim that "the evaluation does not test the proposed predictor at all" is too strong — the paper says "our predictor is simplified to validate the effectiveness of our proposed framework" (line 215), indicating it is used. The ambiguity is real but the critic over-extrapolates to "does not test at all."
- Critic's complaint that "no quantitative cluster overlap statistics are provided" for the t-SNE observation — this is a minor omission that does not threaten the paper's core claims; the qualitative visualization suffices for motivation.
- Critic's assertion that "the choice of first-week data for reconstruction is arbitrary" and that "sensitivity to anomalous weeks is not discussed" — these are speculative concerns without evidence that anomalous weeks exist in the data.
- Critic's note that "the uniform prior for expert assignment is not motivated" — the uniform prior is a standard choice in MoE literature (cited \citep{moe_generative}) and does not require extensive justification.
- Critic's claim that the paper "should not imply that the predictor is a contribution" — the paper explicitly describes the predictor as "simplified to validate the effectiveness of our proposed framework" (line 215), which is a reasonable design choice for an MoE paper.
- Critic's general complaint about "parser issues" making the experiments section incomplete — this is not an author error; the paper's full version contains these sections.

**From Strength Finder:**
- None of the strengths needed removal; they are all concrete and specific.

## Novel Insights
None beyond the paper's own contributions. The two reviewers' perspectives are largely consistent — both recognize the method's novelty and the ablation's strength, while the harsh critic surfaces genuine ambiguities in the experimental reporting that the strength finder glosses over.

## Suggestions
1. **Clarify the predictor architecture used in each table.** Explicitly state whether Table \ref{tab:60min-avg} uses the custom predictor (DiffConv + 1D-Conv) or the TrafficStream backbone. If the custom predictor is used, fix the misleading caption; if the TrafficStream backbone is used, report the custom predictor's performance separately (e.g., in the component analysis or an appendix).
2. **Re-evaluate TrafficStream under the same metric protocol**, or at minimum quantify the metric shift by computing both the "prior work" and "standard practice" metrics on the proposed method's predictions.
3. **Add at least one additional dataset** (e.g., another PeMS district with year-over-year sensor additions or a controlled synthetic streaming setup).
4. **Add a hyperparameter sensitivity study** for \(K\), \(n_s\), \(n_r\), and \(\beta\).
