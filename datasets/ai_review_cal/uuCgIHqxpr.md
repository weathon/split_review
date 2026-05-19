- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5
Now I have all the evidence I need. Let me construct the final review.

## Summary

This paper presents the Smart Buildings Control Suite, a benchmark for HVAC control in commercial buildings that combines (i) real-world historical sensor data from three California office buildings and (ii) lightweight 2D finite-difference simulators calibrated to each building using the real data. The simulators are Gym-compatible and the data follows the Digital Buildings Ontology / Protobuf format. The paper demonstrates calibration on one building (SB1), reducing temperature prediction error from ~1.97°C to ~0.72°C (train) and from ~1.62°C to ~0.57°C (validation), and provides a baseline SAC agent that achieves an 8% improvement in return over the building's baseline policy within the simulator.

## Strengths

- **First open benchmark combining real-world HVAC data with interactive calibrated simulators.** The related work section provides a concrete survey of prior datasets and identifies that none offer both real-world data and interactive simulation for the same buildings. This positioning is specific and verifiable from the paper (Section "Prior Datasets").

- **Calibration procedure that quantitatively improves simulator fidelity.** The TS-MAE metric is well-defined (Equation 1), and the reduction from 1.971°C (uncalibrated) to 0.717°C (calibrated) on training data and from 1.618°C to 0.566°C on held-out validation data is a meaningful improvement (Table "train-test-data"). The drift visualizations (Figures 4-5) and spatial error heatmap (Figure 6) provide transparency about remaining discrepancies.

- **Rapid simulator configuration.** The paper reports that a single technician configured the simulator for SB1 (two floors, 170 devices) "in under three hours" (Section "Simulator Configuration"). This directly addresses a key scalability barrier.

- **Open-source release with standard interfaces.** The data is released on TensorFlow Datasets under a Creative Commons license, and the simulator is Gym-compatible (Section "Introduction"). This lowers the barrier for community adoption and comparison.

## Weaknesses

### Fatal
None.

### Major

- **Internal contradiction about dataset duration.** The abstract states "six years of real-world historical data from three buildings" (line 4); Section 4 repeats "The dataset currently consists of six years of data from three buildings" (line 128). However, the Limitations section says "we only include data from a one year duration" (line 327). These statements are directly contradictory. Whether the released data covers six years or one year is a basic fact that must be resolved before the dataset can be used by others.

- **Quantitative results absent for two of the three claimed benchmark tasks.** The paper lists three tasks (Section 8): (a) RL on the simulator, (b) training a learned dynamics model from real data, (c) training an RL agent via that dynamics model. For task (a), a single return value (-11.9 vs. -12.9) is reported with no variance, no seeds, no confidence intervals. For task (b), the LSTM is described qualitatively: "achieved strong performance and successfully modeled many building dynamics" (line 318). For task (c), the result is: "we were able to learn a policy that improved upon the baseline" (line 321). A benchmark paper must provide concrete baseline numbers that future work can compare against; qualitative descriptions are insufficient for validation.

- **Calibration results shown for only one of three buildings.** The paper claims "pre-calibrated simulators for all of our buildings" (line 34) and the conclusion repeats "calibrated simulators for each building" (line 329). However, the entire calibration section (Section 7) exclusively uses SB1 data. No TS-MAE numbers, drift plots, or spatial error heatmaps are provided for SB2 or SB3. Without evidence that the calibration procedure generalizes, the claim of multi-building calibrated simulators is unsupported.

### Minor

- **Reward weights (u, v, w) used in the experiments are not disclosed.** The 3C reward function (lines 58-60) defines parameters u, v, w that encode operator preferences for comfort vs. energy vs. carbon. These values are never stated, making the reported return values (-12.9, -11.9) uninterpretable and non-reproducible.

- **SAC result lacks grounding in the reward components.** The 8% improvement in total return could come from any combination of energy cost, carbon, and comfort. Without a breakdown of these components, readers cannot assess whether the improvement is meaningful (e.g., does it sacrifice comfort for energy savings?) or an artifact of the chosen weights.

### Trivial

None.

## Nice-to-Haves

- A brief sim-to-real discussion acknowledging the gap between simulator-based and real-world policy performance, even without an actual deployment study, would strengthen the framing.
- Disclosure of the hyperparameter search space for calibration and SAC training would aid reproducibility, though this is not required for the paper's core contribution.
- The claim of a "novel method of calibrating the simulator" could be toned down — the procedure is black-box hyperparameter tuning applied to physical simulator parameters, which is a practical engineering approach rather than a novel algorithmic contribution.

## Removed Points

- **"No sim-to-real evaluation"** — The harsh critic characterized this as a structural flaw. However, the paper's contribution is a benchmark, not a deployed RL solution. The calibration validates that the simulator reproduces real building temperatures, and the SAC demonstration shows the benchmark can be used. Requiring sim-to-real deployment validation is outside the stated scope of a benchmark release paper. Demoted to Nice-to-Have.

- **"Baseline not clearly defined"** — The paper states the baseline is "the policy currently used in the real building" (line 285). The critic's uncertainty about this is not supported by the text. Removed.

- **"Novelty of calibration method questioned"** — The critic notes the calibration is just hyperparameter tuning. This is accurate but is a presentation issue, not a weakness in the benchmark. Moved to Nice-to-Have.

- **"Missing hyperparameters"** — The critic asks for the hyperparameter search space. Following the filtering discipline, undisclosed hyperparameters for reproducibility are treated as nitpicks. Moved to Nice-to-Have.

- **"Only 3 days of calibration data"** — The critic implies this is insufficient, but the paper demonstrates that 3 days yields meaningful improvement. This is a methodological choice, not a weakness, and the paper acknowledges the limitation. Removed.

## Novel Insights

The harsh critic's most useful insights are the identification of the six-year/one-year contradiction and the missing quantitative baselines for tasks (b) and (c). These are not flaws in the benchmark's design but in the paper's presentation of its own resource. The strength finder correctly identifies that the calibration fidelity improvement is the paper's strongest evidence, and that the rapid configuration claim addresses a real practical barrier. Beyond these, the reviews surface no genuinely novel observation that the paper itself does not already articulate.

## Suggestions

1. **Resolve the data duration contradiction** — clarify whether the full dataset covers six years of collected data with a one-year released subset, or if "six years" and "one year" refer to different things. Be explicit.
2. **Provide quantitative baselines for all three benchmark tasks** — at minimum, report the LSTM prediction error (e.g., TS-MAE or MSE) and the real-data RL agent's return with the 3C reward breakdown.
3. **Show calibration results for at least one additional building** (SB2 or SB3) to substantiate the claim of pre-calibrated simulators for all buildings.
4. **Disclose the reward weights (u, v, w)** used in the experiments and report the individual components of the 3C reward for the SAC baseline vs. learned policy.
5. **Report variance** across multiple random seeds for the SAC result so that readers can assess the significance of the claimed 8% improvement.
