I have now thoroughly verified all reviewer claims against the paper. Here is the consolidated review.

---

## Summary

This paper investigates whether incorporating river network topology improves discharge forecasting using graph neural networks. On the LamaH-CE dataset (375 gauges in the Danube basin, 6-hour lead time, 24-hour input window), the authors systematically compare GCN, ResGCN, and GCNII architectures across 18 topology configurations (varying adjacency definitions and edge orientations) and find no statistically significant benefit from including graph structure over an equivalent-depth MLP baseline. Additional analyses show that learned edge weights do not correlate with physical relationships, that performance is invariant to GNN depth, and that the primary failure mode is sudden discharge spikes. The paper is a clearly written, reproducible empirical study documenting a carefully scoped negative result.

## Strengths

1. **Systematic ablation of graph topology across 18 configurations** shows no statistically significant performance difference from the isolated (edge-free) baseline (Table 2). This directly supports the paper's main conclusion that river network topology does not improve forecasting with *this class* of GNN models.

2. **Depth study with 1–20 layers** (Figure 3) demonstrates that the inability to benefit from graph structure is consistent across all depths, ruling out oversmoothing or training-depth artifacts as explanations for the negative result.

3. **Correlation analysis between learned and physical edge weights** (Table 3) reveals negligible and sign-inconsistent correlations (e.g., ResGCN stream-length correlation +0.19, GCNII –0.16), providing direct evidence that even when given freedom to learn edge parameters, the model does not discover physically meaningful relationships.

4. **Worst-gauge case study** (Figure 4) identifies sudden discharge spikes as the primary failure mode, yielding a specific, data-driven suggestion that future improvements should target spike prediction rather than topology integration.

5. **Rigorous experimental design** includes six-fold cross-validation, holdout-based early stopping, clear preprocessing that preserves connectivity while filtering incomplete gauges (Algorithms A.1, A.2), and publicly available source code, minimizing confounds when attributing performance differences to topology.

## Weaknesses

### Fatal
None. The core finding — that the tested GNN architectures do not benefit from river network topology on LamaH-CE — is supported by the experiments.

### Major

1. **The claim of justifying the SOTA independent-gauge approach is not directly supported by the experiments.** The abstract states: "This work may serve as a justification for the SOTA treating gauges independently." The SOTA (Kratzert et al., 2019b) is an LSTM trained jointly across gauges — a fundamentally different architecture with proper temporal processing via recurrent connections. The paper's model is a GNN with a linear (non-recurrent) temporal encoder. The paper never trains an LSTM baseline (with or without graph structure), so it cannot directly show that the SOTA LSTM's independence assumption is validated. The negative result only demonstrates that *this specific architectural family* (static GNN layers on a per-gauge linearly-encoded window) does not benefit from topology. The "justification for SOTA" claim goes beyond what the evidence supports. Authors should either (a) add an LSTM baseline and a spatiotemporal GNN baseline, or (b) substantially tone down this claim to match the evidence. As written, this risks misleading readers about the scope of the finding.

2. **The temporal encoder is weak for a forecasting task, limiting the generality of the negative result.** The model uses a linear layer from the 24-hour input window (W=24) to a latent dimension, collapsing all temporal structure into a single vector per gauge before any spatial mixing. There is no temporal modeling within the GNN — no recurrence, no 1D convolutions, no attention over time. Standard spatiotemporal forecasting approaches (e.g., STGCN, T-GCN, GraphWaveNet, or an LSTM-GNN hybrid) explicitly handle both spatial and temporal dependencies. Because the temporal encoder is this simple, the negative result could stem from the model's inability to capture temporal patterns well enough for spatial structure to matter, rather than from spatial structure being inherently unhelpful. The paper briefly mentions "more specialized model architectures" in the conclusion but does not foreground this critical limitation — that the finding applies only to GNNs with a linear temporal collapse and may not generalize to models with richer temporal representations.

### Minor

1. **No analysis by gauge position or flow regime.** The paper averages performance over all 375 gauges, but headwater and downstream gauges have very different upstream dependencies. Topology might help a subset of gauges (e.g., downstream gauges with strong upstream correlation) even if the effect is washed out in the average. Disaggregating results by gauge position would add valuable nuance.

2. **The worst-gauge claim about "more improvement potential lies in anticipating spikes" is suggestive but not backed by quantitative evidence.** The paper identifies that the outlier gauge (#80) exhibits sudden spikes and that the model misses them. However, no peak-over-threshold evaluation or targeted extreme-event metric is provided. The claim is reasonable as a qualitative observation but is not rigorously demonstrated.

3. **The paper does not report how its model's NSE (~85%) compares to established baselines on the same dataset.** While the paper is not framed as a SOTA-chasing benchmark, the absence of any reference performance (e.g., a simple per-gauge persistence model, or published results on LamaH-CE) makes it hard for readers to contextualize whether the 85% NSE baseline is competitive or whether the overall modeling approach is fundamentally weak.

### Trivial

None.

## Nice-to-Haves

- An LSTM baseline (trained jointly across gauges without graph structure, following Kratzert et al., 2019b) would directly address the "SOTA justification" concern and strengthen the paper's secondary claim.
- Testing a spatiotemporal architecture that processes the temporal dimension properly (e.g., LSTM encoder + GNN, or GraphWaveNet) would test whether the negative finding holds for richer temporal models.
- Analysis of high-flow periods or peak events could test whether topology helps specifically during floods — the paper's motivating application.
- The linear temporal encoder choice, while reasonable for isolating the spatial effect, deserves more explicit justification in the main text rather than being an unremarked design decision.

## Removed Points

These points from the reviewer inputs were removed or downgraded per the filtering rules:

- **"The correlation analysis is interesting but not surprising... The analysis is sound but not needed to support the main result."** — Removed. This is a subjective opinion about necessity, not a weakness. The correlation analysis provides independent supporting evidence and is part of the paper's contribution.
- **"Neither model is hydrologically competitive with the LSTM-based SOTA"** — Downgraded and folded into Minor weakness #3. The paper is not claiming SOTA performance, so evaluating it against that standard is somewhat misplaced. However, the absence of contextualizing baselines is a genuine minor concern.
- **"No temporal GNN comparison"** — Moved to Nice-to-Haves. Requesting a completely different model class (spatiotemporal GNNs) as a requirement for the paper's validity is scope creep; the paper's claim is about the tested architectures.
- **"No evaluation on flood events"** — Moved to Nice-to-Haves. The paper explicitly notes that LamaH-CE "does not provide any flood event annotations," making discrete flood evaluation infeasible without significant additional work.
- **"The encoder is simply a linear layer... The paper does not justify this choice"** — Folded into Major weakness #2 rather than kept as a separate point, since it is the same underlying issue.

## Novel Insights

The reviews collectively surface a tension not fully addressed in the paper: the negative finding is simultaneously the paper's main contribution and its main limitation. Showing that GNNs with linear temporal encoders do not benefit from topology is a legitimate empirical result, but the paper's abstract frames it as a potential justification for the SOTA LSTM-based approach — a leap the experimental design cannot support. The most actionable insight from the reviews is that the paper would be substantially stronger if it either added LSTM-based experiments (to bridge this gap directly) or explicitly reframed the contribution around the tested architecture class rather than the broader SOTA practice. The worst-gauge spike analysis is a genuine positive contribution that the rebuttal section of the reviews correctly identifies as underexploited — a targeted extreme-event evaluation would make this insight more than qualitative.

## Suggestions

1. **Tone down or remove the "justification for SOTA" claim** in the abstract and conclusion, unless an LSTM baseline is added. The current wording overstates what the experimental design can support.

2. **Add a clear limitations paragraph** in the main text explicitly stating that the negative result applies to GNNs with a linear temporal encoder, and that models with richer temporal processing (LSTMs, 1D-CNNs) might yield different conclusions about the value of topology.

3. **Disaggregate results by gauge position** (headwater vs. downstream, or by upstream basin size) to test whether topology helps a subset of gauges even if the overall effect averages to zero.

4. **Include a simple baseline** such as a per-gauge persistence forecast or published LamaH-CE results, to help readers contextualize the 85% NSE baseline.

5. **Strengthen the spike analysis** with a quantitative peak-over-threshold metric or an evaluation focused on high-flow periods, rather than relying solely on qualitative plots.

## Score and Decision

The paper makes a genuine contribution: a careful, reproducible, systematic negative result showing that a family of standard GNN architectures does not benefit from river network topology on a real-world hydrological dataset. The experiments are well-designed and the analysis is mostly sound. However, the paper overreaches in its secondary claim (SOTA justification) without supporting evidence, and the weak temporal encoder limits the generality of the finding in ways the authors do not sufficiently acknowledge. These are significant but not fatal weaknesses — they can be addressed through clearer framing and, ideally, additional experiments. On balance, the core contribution is valuable enough to warrant acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>