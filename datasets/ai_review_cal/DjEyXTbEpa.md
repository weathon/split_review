- Decision: Reject
- Avg Score: 5.17
- Scores: 3, 6, 6, 5, 5, 6
Now I have a thorough understanding of the paper and both reviews. Let me produce the final consolidated review.

## Summary

The paper proposes **ReactiveAgent**, a hybrid framework that integrates the drift-diffusion model (DDM) with deep reinforcement learning (DRL) to simulate the fine-grained effect of dynamic time-pressure stimuli on human response time in a math arithmetic task. The method proceeds in four steps: (1) train an LSTM agent to solve the math task, (2) use SVM to map LSTM features to human baseline performance, (3) decode this into DDM parameters (boundary threshold, accumulation time), and (4) train a DRL agent that modulates the evidence accumulation process per video frame. The authors also contribute a dataset of ~21k logical reasoning responses from 44 participants under four types of time-pressure feedback.

---

## Strengths

- **Novel integration of DDM with DRL for dynamic, frame-level stimuli.** Section 4.3 describes how the DRL agent modulates the DDM evidence accumulation process at a per-frame granularity, each frame corresponding to one step of the stimuli video. This contrasts with prior work such as Bourgin et al. (2019), which treats environmental stimuli as a constant presence. The paper's framing and approach are novel in targeting the underexplored problem of *dynamic* stimulus effects on cognition.

- **Consistent quantitative improvement in response-time simulation.** Table 1 shows ReactiveAgent achieving the lowest MAPE among multiple baselines (hGRU, LSTM+vision, MLP+3D ResNet) under matched input conditions (e.g., 0.22 vs. 0.37 for hGRU with video input). Section 5.4 further demonstrates that the hybrid DRL agent outperforms the pure DRL agent (no DDM) and the SVM-only baseline across all four training strategies (general-, group-, individual-, and LOPO-level) on both MAPE and Pearson correlation (Fig. 2, Fig. 3e).

- **Ablation studies isolate the contribution of each component.** Section 5.2 (Table 2) shows that SVM models using LSTM-extracted features achieve substantially higher choice prediction accuracy (0.9613 vs. 0.5119 F1-score) and lower response-time MAPE than SVMs without these features. Section 5.4 shows that the DDM-integrated (hybrid) DRL agent consistently outperforms the DRL-only (pure) agent, confirming the value of the DDM component.

- **Training efficiency gain from incorporating a structured cognitive model.** Section 5.5 reports that the hybrid DRL agent converges in 4.42 minutes vs. 38.30 minutes for the pure DRL agent on the same hardware, an order-of-magnitude improvement. The paper explicitly acknowledges the difference in step definitions between the two agents and compares wall-clock time instead, making this a fair comparison.

- **Interpretability through DDM-based action trajectories.** Section 5.6 visualizes the time-pressure effect trajectories from the hybrid agent (Fig. 9a–h) and links them to human behavioral data: the random group shows the lowest standard deviation of actions and highest average slope, consistent with the real human response-time reduction pattern (Fig. 5e). This provides mechanistic insight that black-box models cannot offer.

- **Open-sourced dataset filling a gap.** The contributed dataset of 21,157 responses from 44 participants across four time-pressure conditions (none, static, random, rule) directly enables research on cognition under dynamic stimuli, which most existing datasets (e.g., Lumosity) do not capture.

---

## Weaknesses

### Fatal

None.

### Major

- **No DDM-only baseline.** The paper compares Hybrid DRL (DDM+DRL) against Pure DRL (no DDM) and SVM, but never against a stand-alone DDM fit directly to the behavioral data (e.g., using the HDDM toolbox). Without this comparison, the specific added value of the *DRL component* (as distinct from the DDM component) cannot be assessed. It is possible that most of the improvement over the SVM baseline comes from the DDM itself, and the DRL agent contributes little — or even that a well-calibrated DDM alone matches the hybrid. This is the single most important missing experiment for supporting the paper's core claim.

- **Key methodological details of the DRL agent are unspecified.** The paper states the action space is "positive, neutral, or negative bias" (Section 4.3) but does not specify the **state space**, **reward function**, or **training algorithm** (e.g., DQN, PPO, A2C). The mapping from LSTM+SVM predictions to DDM parameters (boundary threshold, accumulation time) is described only as "derived from the predicted responses" (Section 4.3) with no formula or procedure. These omissions prevent reproducibility and make it difficult to evaluate whether the design choices are sound. While some details may reside in the stripped appendix, the main text must be self-contained for the core methodological contribution.

### Minor

- **No statistical significance testing.** The main comparisons (Table 1, Fig. 2, Fig. 3e) report point estimates (MAPE, Pearson r) but no confidence intervals, standard errors, or significance tests (e.g., paired t-tests across participants). Given variability across individuals and groups, it is unclear whether the reported improvements are statistically reliable.

- **Claims about "subject-specific behavioural differences" are only partially supported.** The abstract claims the framework "captures both subject-specific and stimuli-specific behavioural differences," but the evaluation primarily reports group-level and overall metrics. While individual-level training and per-participant results (Fig. 2a–d) exist, there is no dedicated analysis quantifying how well the model captures individual differences (e.g., variance partitioning, individual parameter recovery).

- **Convergence criterion for training efficiency is not stated.** The paper reports that hybrid DRL converges at ~20k steps / 4.42 min and pure DRL at ~800k steps / 38.30 min (Section 5.5). The training curves (Fig. 3f,g) are shown, but the threshold or rule used to determine "convergence" is not specified, making the exact claim slightly imprecise.

### Trivial

None.

---

## Nice-to-Haves

- A DDM-fit-alone comparison (as noted under Major) would substantially strengthen the paper's core claim.
- Reporting MAPE with confidence intervals (e.g., bootstrap or participant-level statistics) would better support the comparisons.
- A brief analysis of residual patterns (when and for whom does the model fail?) would deepen the evaluation.
- Including a characterization of response-time variance explained by stimulus type vs. participant vs. trial order would add value for the community.

---

## Removed Points

These points are flagged for removal; treat them with caution.

1. **"Method insufficiently specified — LSTM training details missing."** The paper provides LSTM training details: neuron sizes 32–256, 100 epochs, training loss 0.0001, 99.93% test accuracy (Section 5.3). The loss function is inferable (classification cross-entropy for the 9-class math task). The main gap is in the DRL and DDM parameter derivation, not the LSTM. → *Partially inaccurate; the LSTM-specific complaint is not well-supported.*

2. **"Scientific contribution is narrow and incremental — Bourgin et al. (2019) already combines MDPs with cognitive models."** The paper explicitly distinguishes itself from Bourgin et al., which "treats environmental stimuli as a constant presence throughout the cognitive process" (Section 2), while ReactiveAgent models fine-grained frame-level dynamics (Section 4.3). This is a clearly articulated and substantive difference. → *Factually incorrect about the paper's novelty claim.*

3. **"Interpretability analysis is purely descriptive."** The paper provides quantitative metrics (standard deviation of actions, average slope of trajectories, Fig. 9f–h) and links them to observed human data (Fig. 5e). This goes beyond purely descriptive analysis. → *Not supported by the evidence in the paper.*

4. **"The LSTM agent's logical reasoning is trivial"** — The LSTM is a component (not the core contribution) that achieves high accuracy on a designed task; its purpose is feature extraction for the SVM, which is validated in Table 2. The criticism is about a supporting component, not the main contribution. → *Demoted from the weakness list as non-central.*

---

## Novel Insights

The harsh critic and strength finder converge on the paper's core limitation: the architecture is novel and shows promising results, but the evaluation lacks a critical control (DDM-only baseline) that would establish whether the DRL component specifically drives improvements. An interesting observation from synthesizing the two reviews is that the paper's interpretability analysis (Section 5.6) — often the weakest part of hybrid ML+cognitive-model papers — is actually one of its stronger elements, because it validates simulation trajectories against real human group-level patterns (random group showing the strongest regulation effect, matching the behavioral data in Fig. 5e). This is the kind of cross-validation between simulated and real data that makes the hybrid approach potentially valuable beyond raw prediction accuracy.

---

## Suggestions

1. **Add a DDM-only baseline.** Fit a hierarchical DDM (e.g., using the HDDM toolbox) directly to the behavioral data, with drift rate or boundary modulated by a function of the time-pressure stimulus (presence/absence). Compare its MAPE and Pearson correlation to the hybrid DRL agent. This will directly test whether the DRL component adds value beyond a well-calibrated cognitive model.

2. **Fully specify the DRL agent in the main text.** Provide: (a) the state space (what information about the current trial, frame, and participant is available to the agent), (b) the reward function (what objective the agent optimizes), (c) the training algorithm and hyperparameters, and (d) the formal transition from SVM predictions to DDM parameters (drift rate, boundary, non-decision time). Without these, the method is not reproducible.

3. **Report statistical significance** for the main comparisons (e.g., paired permutation tests across participants or groups for MAPE and Pearson correlation).

4. **Expand the individual-differences analysis.** The individual-level training strategy (Section 5.4) and per-participant results (Fig. 2) provide a foundation; add a quantitative analysis of how much variance in performance is explained by participant identity vs. stimulus condition vs. their interaction.

---
