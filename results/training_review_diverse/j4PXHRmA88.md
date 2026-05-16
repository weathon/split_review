Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

The paper proposes TraPNet, a neural network that predicts road volumes by estimating per-vehicle, per-node probability distributions over a road network and aggregating them — replacing deterministic trajectory reconstruction with a probabilistic formulation. The model uses multi-view attention to fuse incomplete observations, historical trajectories, and road network features, and produces predictions in a single non-autoregressive pass. Experiments on the Boston road network (simulated trajectories) and the Jinan dataset (real trajectories, 8,908 nodes, 23,312 edges) show that TraPNet achieves lower MAE than two baseline methods (Cam-Traj-Rec and Traj2Traj) and maintains its advantage at observation ratios as low as 20%.

## Strengths

- **Exceptional robustness at very low observation ratios.** With only 20% of checkpoints observed, TraPNet achieves lower MAE than both Cam-Traj-Rec and Traj2Traj at 50% observation (Figure 4, Section 5.2.1). This is a concrete, non-trivial empirical result that directly supports the paper's central claim about tolerance to missing data. The gap is not marginal — the paper states that at a 0.1 checkpoint ratio, TraPNet's MAE is approximately 20% lower than the baselines.

- **Single-step (non-autoregressive) prediction.** The architecture produces the full trajectory probability in one forward pass, avoiding the error accumulation and long inference time of autoregressive methods like Traj2Traj (Section 4.1, Section 5.2.1). This is a genuine architectural advantage for city-scale deployment, and the ablation study (Table 3) confirms that the efficiency mechanisms (discretization, multi-query attention) can be applied with minimal accuracy loss.

- **Multi-view attention that explicitly fuses three heterogeneous data sources.** The ablation (Table 3, lines 2–3) shows that including both historical trajectories and road-network data reduces MAE, with the road network playing a particularly important role. The cross-attention design (Section 4.3) provides a principled mechanism for integrating these inputs, going beyond methods that rely solely on current observations (Traj2Traj) or manual priors (Cam-Traj-Rec).

- **Systematic ablation study on the contributions of architectural components.** Table 3 isolates the impact of historical data, road-network data, discretization, token shape, and multi-query attention. This provides clear empirical justification for the design choices (e.g., discretization saves computation with negligible MAE increase) and is more thorough than is typical in this domain.

## Weaknesses

### Major

- **Gap between the probabilistic framing and the training objective, with no evaluation of uncertainty quality.** The paper motivates the method by arguing that existing approaches "overlook the inherent uncertainty in other potential scenarios" and claims to integrate "the joint distribution of potential trajectories." However, the model is trained with cross-entropy loss against one-hot labels of the *single true trajectory* (Section 4.4). While the output softmax can still spread probability mass at inference, the training objective does not explicitly encourage learning a distribution over multiple plausible trajectories — it simply penalizes any deviation from the one correct path. The paper never evaluates whether the predicted probability distributions are well-calibrated (e.g., reliability diagrams) or capture multiple modes (e.g., does the model assign meaningful probability to alternative routes?). This gap between the framing ("probabilistic modeling of uncertainty") and the actual evidence means that the claimed "comprehensive inference of road volumes through joint distribution of potential trajectories" is not convincingly demonstrated. The authors partially acknowledge this in Section 6.2 ("The Choice of One-Hot Labels"), but the discussion only addresses the alternative of using manual priors, not the deeper issue of whether the model actually learns to represent multiple plausible trajectories. This is the paper's most significant weakness.

- **Narrow experimental comparison relative to the strength of the claims.** The paper compares against only two baselines (Cam-Traj-Rec, Traj2Traj), both of which are trajectory-level methods that must be converted to volume predictions. While these are reasonable choices for the specific task, the paper claims TraPNet "outperforms state-of-the-art methods" — a statement that is unsupported given the absence of any direct volume-prediction baseline (e.g., a GNN that imputes missing node features, a matrix completion approach, or even a simple interpolation-then-count baseline). The related work discusses GNN-based methods, LSTM models, and checkpoint-based approaches (Sections 2.1, 2.2), but none are included as competitors. Adding even one additional baseline would substantially strengthen the evidence.

### Minor

- **The simulated Boston dataset limits the generalizability of the ablation study and some results.** The Boston trajectories are generated from random OD pairs, random road weights, and shortest-path routing (Section 5.1.1). This does not reflect real driver behavior (e.g., route choice preferences, congestion effects, stochastic travel times). The ablation study is performed exclusively on Boston, and while the paper acknowledges that the "BVLC" token shape is too large for Jinan, this means the key architectural analyses are conducted on the least realistic data. The Jinan results are on real data and are more convincing, but the split weakens the overall empirical package.

- **No error bars or standard deviations are reported for any metric.** The paper states that each training run is repeated 3 times and "we report the average results" (Section 5.1.2), but no variance measures are provided for any of the MAE comparisons (Table 2, Figure 4). Given that checkpoints are randomly sampled during each training iteration, this variability should be quantified. Without error bars, it is difficult to assess whether the reported differences between methods are statistically significant — especially the headline result that 20% observations outperform baselines at 50%.

- **The ablation does not include a variant that replaces probabilistic aggregation with deterministic trajectory prediction (e.g., argmax of the softmax).** The paper's central claim is that aggregating probabilities is superior to deterministic reconstruction, yet the ablation (Table 3) tests the removal of input modalities and efficiency mechanisms, but never compares probabilistic aggregation against taking the single most likely trajectory and counting vehicles on it. Such a variant would directly isolate the value of the probabilistic aggregation step.

- **The efficiency claim lacks runtime comparisons.** The paper asserts that TraPNet is "significantly faster" (Section 5.2.1) and "can achieve almost real-time performance," but no runtime measurements (inference time per trajectory or per road network) are reported for any method. The only numbers provided are training GPU hours (8 on Boston, 100 on Jinan). The efficiency argument would be substantially stronger with wall-clock inference time comparisons against the baselines.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- An evaluation of uncertainty quality (calibration plots, entropy-vs-error analysis, or qualitative inspection of whether the model assigns probability to plausible alternative routes).
- A simple baseline such as "impute missing observations with the road-average volume and count" to contextualize the reported gains.
- A discussion of the limitation that training requires complete trajectory labels, which may be unavailable in many real-world settings (the paper mentions using GPS data, but this is acknowledged only implicitly).
- Explicit specification of baseline configurations (were they reimplemented? tuned on validation sets?) for reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism that "the volume aggregation formula assumes independence that does not hold"* — The multiplication Y[b,t,oᵢ] × Y[b,t+1,dᵢ] is a first-order Markov assumption, which is standard and reasonable for trajectory modeling. The normalization is a sensible constraint. The critic treats this as an ad-hoc error; it is a defensible design choice, not a structural flaw. **Removed** as overclaimed.

- *Criticism that "the loss function becomes cross-entropy because ground truth trajectories are assumed complete" and "this contradicts the earlier story of modeling uncertainty"* — This is acknowledged and discussed by the authors in Section 6.2. The paper is transparent about the design choice. While the lack of uncertainty evaluation is a real weakness (kept above), the existence of the one-hot training per se is not a contradiction — many probabilistic deep learning models are trained with cross-entropy. **Downgraded** from the critic's framing as a fatal contradiction; the substantive residue (no uncertainty evaluation) remains in Major.

- *Criticism that "the paper should compare against GNN-based volume prediction models, LSTM models, and checkpoint-based methods"* — Those methods operate on a fundamentally different problem setting (complete volume data as input vs. incomplete trajectory checkpoints). Demanding their inclusion would require adapting them to a task they were not designed for. **Removed** as scope creep.

- *Complaints about formatting, missing appendix content, and incomplete trajectories in parsed text* — These are parser artifacts. **Removed** per instructions.

- *Strength Finder claim #5 about "thorough evaluation on two real-world road networks"* — The Boston trajectories are simulated (shortest-path on random OD pairs with random road weights), so calling it "real-world" is misleading. The strength is better framed as "evaluation on datasets of different scales, including one large real-world dataset (Jinan)." **Moved** to Removed Points for overclaiming.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the reviews is the tension between the paper's probabilistic framing and its deterministic training — a gap that is common across many deep learning papers that claim to model "uncertainty" but train with standard cross-entropy. The fact that the model still performs well at low observation ratios despite this gap suggests that the multi-view attention architecture and the single-step prediction are doing the heavy lifting, and the "probabilistic" framing may be more of a useful conceptual tool than an empirically validated property. A stronger version of this paper would either (a) train with an objective that genuinely encourages multimodal trajectory distributions, or (b) drop the probabilistic framing and reframe as a deterministic node-classification model with a clever aggregation step — which would be an honest and still novel contribution.

## Suggestions

- Add a calibration analysis (reliability diagrams, expected calibration error) and a qualitative check of whether the model assigns probability to alternative plausible routes. This would directly address the gap between framing and evidence.
- Report error bars or confidence intervals for all MAE values, especially for the checkpoint-ratio comparison that contains the paper's strongest claim.
- Include an ablation that replaces probabilistic aggregation with deterministic argmax trajectory selection to isolate the value of the probability aggregation step.
- Add inference runtime comparisons against baselines to substantiate the efficiency claim.
- Acknowledge the limitations of the simulated Boston dataset explicitly in the main text (not just in the data preparation section) and discuss how the simulation assumptions could affect conclusions.

## Score and Decision

The paper proposes a worthwhile direction and has two genuinely strong empirical results (robustness at 20% observations, and the single-step efficiency advantage). However, the gap between the ambitious probabilistic framing and the evidence provided is significant enough that the core contribution is not fully delivered. The experimental comparison is too narrow to support the claimed state-of-the-art status, and the lack of error bars, a key ablation, and runtime measurements leaves several claims undersupported. With revisions focusing on uncertainty evaluation, additional baselines, and the missing ablation, the paper could be much stronger — but in its current form, these weaknesses are material.

**Overall Assessment:** The paper has a novel architecture and a compelling headline result, but the evidence does not yet match the strength of the claims. The probabilistic motivation is not backed by appropriate evaluation, the baseline comparison is too limited, and several secondary claims lack supporting measurements.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>