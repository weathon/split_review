Now I have sufficient calibration. Let me finalize my analysis.

**Round 1 bracket:** 5.5 – 7.0

**Round 2 comparison:**
- `hpeyWG1PP6` (5.75): TDDBench — benchmark paper, lacks deep analysis. Our paper is stronger.
- `zWqr3MQuNs` (6.25): Detecting Pretraining Data — method paper with benchmark. Our paper has deeper mechanistic analysis but no new method. Comparable quality, slightly below.
- `Nsms7NeU2x` (6.75): "How much can we Forget about Data Contamination?" — most comparable: theory + experiments on contamination, rejected despite high scores. Our paper has broader scope but the theory-experiment mismatch and Stage II baseline issues are comparable weaknesses.
- `m2NVG4Htxs` (6.75): Longitudinal contamination analysis — cleaner methodology, narrower scope. Our paper has broader coverage but identified weaknesses. Slightly below.
- `sKYHBTAxVa` (7.33): LiveBench — concrete artifact, clear practical impact. Our paper is below.
- `jOmk0uS1hl` (8.00): "Training on the Test Task" — uniformly strong, clear implications. Our paper is below.

**Final score: 6.0** — The paper makes a genuine contribution (causal mechanism isolation via ablation, two-stage contamination analysis for LRMs) but has two Major weaknesses that affect framing and interpretation. The Stage I ablation design is excellent and the empirical evidence for RL concealment is solid. The Stage II clean baseline issue and theory-experiment disconnect are real but addressable.

---

## Summary
This paper presents the first systematic study of benchmark contamination detection fragility in Large Reasoning Models (LRMs). It examines two contamination scenarios: (I) SFT contamination introduced during base model training, which is initially detectable but can be concealed by subsequent RL training (particularly GRPO), and (II) SFT contamination with chain-of-thought applied to advanced LRMs as a final stage, where existing detectors perform near random. Through ablation studies isolating the PPO-style importance sampling and clipping term, the paper identifies the algorithmic mechanism driving concealment in Stage I.

## Strengths
- **Causal mechanism isolation through clean ablation design (Table 3):** The paper does not merely observe that GRPO reduces detectability — it isolates why. RAFT (rejection sampling without clipping/importance sampling) preserves the Loss detector AUROC at 77.51% (Δ = +2.03 relative to the no-RL baseline), while RAFT++ (which adds PPO-style importance sampling and clipping) drops it to 57.58% (Δ = −17.91). Removing clipping from RAFT++ restores AUROC to 74.39% (Δ = −1.09) and from GRPO to 73.28% (Δ = −2.20), directly implicating the clipping term as the concealment driver. This is the strongest piece of evidence in the paper.

- **Elimination of the forgetting confound through two distinct controls:** The paper rules out the alternative explanation that further training simply causes models to forget contamination. First, GRPO trained on both clean and contaminated data produces comparable AUROC drops (Table 2, "RL w/ Clean&Mem" rows). Second, continuing SFT for 4 additional epochs on clean data does not conceal contamination (Fig. 2, "SFT Conta (w/o RL) further SFT" bars), while pass@1 continues to rise — confirming the effect is specific to RL, not additional training per se (lines 136-137).

- **Monotonic dose-response relationship (Fig. 2):** AUROC decreases monotonically as GRPO steps increase from 64 to 110 to 156, with reference-free methods (Loss, Min-K%, Max-K%) falling to near-random (≈50%) after only 156 steps. This dose-response pattern strengthens the causal interpretation.

- **Diagnostic log-prob distribution analysis (Fig. 3):** Before RL, member and non-member log-prob distributions are clearly separated (AUROC ≈ 0.70 on GPQA-Diamond); after 64 GRPO steps, they substantially overlap. This visualization makes the concealment mechanism directly interpretable.

- **Broad model coverage:** Stage I uses two base models (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct) across six benchmarks; Stage II spans four LRM architectures (DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-7B, OpenThinker-3-7B, DeepSeek-R1-Distill-Qwen-14B), showing findings are not model-specific.

- **Interesting mechanistic insight for Stage II (Fig. 4, lines 330-331):** The observation that log-probability increases at a similar margin for both members and non-members after contamination suggests LRMs may internalize reasoning patterns rather than memorizing specific sequences, challenging the memorization assumption underlying existing detectors.

## Weaknesses

### Fatal
None.

### Major
- **Theory–experiment disconnect in Stage I:** The theoretical analysis (Section 3.2, Theorem 3.1) explicitly assumes "RL training is performed on the benchmark data (i.e., training data is the combination of members M and non-members N)" (line 188). However, the headline experimental result for Stage I (Table 2) shows that GRPO trained on *clean* data — containing neither members nor non-members — conceals SFT contamination. The theory models gradient dynamics when both member and non-member trajectories participate in RL optimization, but when RL uses only clean data, neither type of trajectory is present. The ablation study (Table 3) validates the theory's mechanism (clipping drives concealment), but the connection to the clean-data RL result — which is the paper's primary Stage I finding — is not theoretically explained. The paper should either extend the theory to the clean-data setting or explicitly acknowledge that the theory models a related but distinct scenario, with the clean-data result remaining an empirical finding awaiting theoretical explanation.

- **Stage II findings lack clean baselines, affecting interpretation:** The central narrative for Stage II is that "extensive contamination with CoT on advanced LRMs barely leaves evidence" (abstract, Section 4). However, Fig. 4 shows that the AUROC for the Loss detector on *clean* advanced LRMs (before any contamination) is already ≈0.50 — indistinguishable from random (R1 Distill LLaMA: 0.497; R1 Distill Qwen: 0.479). This means the detectors have no usable signal on these models regardless of contamination status. The paper frames Stage II as showing contamination is stealthy, but the data suggest the detectors are simply invalid for advanced LRMs in the first place. The Discussion (lines 330-331) gestures at this nuance, but the abstract and introduction do not reflect it. The paper should include systematic clean-baseline AUROC measurements for all methods and models in Stage II, or substantially recharacterize the finding. This recharacterization could actually strengthen the paper's overall thesis by showing the problem runs deeper than contamination alone.

### Minor
- **Theory provides qualitative framework rather than formal proof:** Theorem 3.1 and the subsequent derivations offer a plausible mechanism rather than a rigorous proof. Key conclusions rely on informal reasoning about variance patterns (e.g., line 204: "non-members correct trajectories can exhibit much higher variance in loss and probabilities"; line 208: "Empirically, the covariance gap offsets the mean gap"). The theory operates in a tabular setting with small-step assumptions. This is acceptable for an empirical paper — the ablation study (Table 3) does the real evidentiary work — but readers should not mistake the theoretical analysis for a formal proof.

- **Missing variance/uncertainty estimates for AUROC values:** The paper reports AUROC values without standard deviations, confidence intervals, or any measure of uncertainty. For some methods, the AUROC changes are small (e.g., Verbatim drops from 52.76 to 52.16, Δ = −0.60; CDD from 55.80 to 55.34, Δ = −0.46). Without variance estimates, readers cannot assess whether these modest changes are distinguishable from noise. The larger drops (e.g., Min-K% from 74.96 to 61.27, Loss from 75.48 to 61.26) are clearly meaningful even without formal variance estimates, but reporting uncertainty would strengthen the case for borderline methods.

### Trivial
- The paper could clarify what training data was used for the Table 3 ablation study (RAFT/RAFT++/GRPO comparison) — whether it was clean data, benchmark data, or a mixture — to help readers connect the theory to the ablation.

## Nice-to-Haves
- The paper focuses exclusively on math and science reasoning benchmarks. Acknowledging this scope limitation and discussing whether the findings might generalize to coding or general-knowledge benchmarks would help readers calibrate generalizability.
- A brief discussion of whether detection methods based on generation diversity or response consistency (beyond the log-prob-based methods tested) might be more robust to RL concealment would round out the analysis.
- The paper could briefly discuss which benchmark types (open vs. closed) are most vulnerable to the contamination strategies studied.

## Removed Points
These points were flagged for removal with justification:

1. "The paper does not discuss whether the findings generalize beyond math/reasoning benchmarks" — REMOVED as a weakness. This is a scope limitation, not a flaw. The paper is explicitly about reasoning models and reasoning benchmarks. Moved to Nice-to-Haves.

2. "The threat model assumes developers have access to benchmark questions... closed benchmarks would be harder to contaminate" — REMOVED as a weakness. This is inherent to the contamination detection problem; the paper's threat model is standard. Moved to Nice-to-Haves.

3. "No discussion of whether detection methods based on generation diversity or response consistency might be more robust" — REMOVED as a weakness. This is a suggestion for future work, not a methodological flaw. Moved to Nice-to-Haves.

4. "The paper mentions Bordt et al. but doesn't connect this to whether the Stage I finding might be a specific instance of a broader training-dynamics phenomenon" — REMOVED. This is a suggestion for richer related work discussion, not a weakness.

5. Formatting/style concerns from the harsh critic — REMOVED per hard rules (parser artifacts, not author errors).

## Novel Insights
The most novel insight from this paper is the identification of the PPO-style clipping term as a *mechanism* for contamination concealment, not merely a training stabilizer. The paper shows that this term — present in widely-used RL algorithms (GRPO, PPO, RAFT++) — has the side effect of differentially compressing the NLL gap between contaminated and clean samples. This is important because it suggests the concealment problem is not specific to GRPO but may be inherent to a broad class of RL methods used in LRM training, with significant implications for evaluation integrity.

## Suggestions
- Add systematic clean-baseline AUROC measurements for Stage II across all methods and models. This would clarify whether detectors fail due to contamination or due to fundamental incompatibility with LRMs, and would likely strengthen the paper's overall thesis.
- Clarify the relationship between the theoretical analysis (which assumes RL on benchmark data) and the primary empirical result (RL on clean data concealing contamination). Either extend the theory or explicitly bound its scope.
- Report bootstrap confidence intervals for AUROC values, particularly for methods where changes are modest, to help readers assess which results are statistically meaningful.

## Calibration Anchors

All anchors retrieved across rounds:

| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| `Nk1MegaPuG` — Evading Data Contamination Detection | 4.25 | R1 | Our paper is clearly stronger: better methodology, causal ablation, broader evaluation |
| `hpeyWG1PP6` — TDDBench | 5.75 | R2 | Our paper is stronger: deeper analysis, mechanistic insights, more novel problem framing |
| `zWqr3MQuNs` — Detecting Pretraining Data | 6.25 | R2 | Comparable quality; our paper lacks a new method but has stronger mechanistic analysis |
| `9QPH1YQCMn` — Infilling Score | 6.25 | R2 | Comparable; method paper vs. analysis paper, different contribution types |
| `X8dzvdkQwO` — Fine-tuning Helps Detect Pretraining Data | 6.25 | R2 | Comparable; our paper is broader but has the theory-experiment mismatch |
| `Nsms7NeU2x` — How Much Can We Forget About Data Contamination | 6.75 | R2 | Most comparable; our paper has broader scope but similar weakness profile; slightly below |
| `m2NVG4Htxs` — Longitudinal Perspective on Data Contamination | 6.75 | R1/R2 | Cleaner methodology but narrower scope; our paper slightly below due to identified weaknesses |
| `SVRRQ8goQo` — KOR-Bench | 7.00 | R2 | Benchmark paper with concrete artifact; our paper is below |
| `sKYHBTAxVa` — LiveBench | 7.33 | R1/R2 | Strong benchmark contribution with released artifact; our paper is clearly below |
| `EUSkm2sVJ6` — Quantitative Data Usage Inference | 7.60 | R1 | Novel algorithm + theory; our paper is clearly below |
| `jOmk0uS1hl` — Training on the Test Task | 8.00 | R1 | Uniformly strong, clear implications; our paper is clearly below |

Round 1 bracket: 5.5 – 7.0. Round 2 within-bracket comparison places the paper near 6.0: above the 5.75 benchmark paper, comparable-to-slightly-below the 6.25 method papers and the 6.75 contamination analysis papers. The two Major weaknesses (theory-experiment disconnect, missing Stage II clean baselines) pull it down from what could have been a 6.5–7.0 paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>