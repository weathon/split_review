## Summary
This paper proposes MotionRL, a reinforcement learning-based fine-tuning framework for text-to-motion generation. The key idea is to use three reward signals — text adherence (via pretrained text-motion encoders), motion quality (via L2 reconstruction error), and human preference (via a pretrained perception model) — and optimize them jointly using a batch-wise Pareto selection strategy with PPO. Reward-specific tokens are introduced to control the trade-off between objectives at inference time. Experiments on HumanML3D show consistent improvements across FID, R-Precision, and perception model scores compared to several strong baselines, and a user study indicates better alignment with human preferences.

**Primary contribution**: Combining multi-reward RL with Pareto-based sample selection for text-to-motion generation, with an emphasis on incorporating human perceptual quality as an optimization target. The work addresses a genuine gap — most prior text-to-motion methods optimize error-based metrics (FID, R-Precision) that correlate poorly with perceived motion quality.

## Strengths
1. **Addresses a meaningful gap in the text-to-motion literature**: The paper correctly identifies that existing metrics (FID, R-Precision) do not fully capture perceived motion quality. Incorporating human perceptual priors as an optimization target is a well-motivated and practically important direction.

2. **Pareto-based multi-reward selection is a technically sound approach**: Rather than using naive weighted reward combinations that can be unstable, the batch-wise non-dominated sample selection provides a principled heuristic for multi-objective optimization. The reward-specific token design for inference-time control is a practical contribution that adds flexibility.

3. **Strong empirical results on standard metrics**: Table 1 shows that MotionRL achieves the best FID (0.066), Top-1 R-Precision (0.531), and Top-3 R-Precision (0.811) among all methods evaluated on HumanML3D, including the strong baseline MoMask (0.045 FID, 0.521 Top-1). The gains are meaningful though modest in absolute terms.

4. **User study provides complementary validation**: The human evaluation (Figure 3b) attempts to validate perceptual quality beyond automatic metrics, which is essential for the paper's core claim. Using pairwise comparisons with randomized presentation is a reasonable protocol design.

5. **Clear writing structure**: The paper follows a logical flow from motivation (FID-perception gap) to method (RL + Pareto) to experiments. The methodology section explains the multi-reward design and Pareto selection with sufficient technical detail and pseudocode.

## Weaknesses
1. **Circular evaluation of perception model** (major): The perception model from Wang et al. (2024) is used both as a training reward (Eq. 6) and as an evaluation metric (Figure 3a). Since MotionRL is explicitly trained to maximize this model's output, higher scores on it are expected by construction and do not constitute independent evidence of perceptual quality.

2. **Insufficient ablation baselines** (major): Table 2 compares only three reward combinations, all using Pareto selection. Missing critical baselines include: (a) the pretrained generator without any RL fine-tuning, (b) weighted-sum PPO with all three rewards, and (c) single-reward conditions for Rm (motion quality) and Rt (text adherence). Without these, the contribution of the Pareto mechanism cannot be isolated from the simple addition of rewards.

3. **No statistical significance reporting** (major): Table 1 reports only point estimates without variance, confidence intervals, or significance tests. Many improvements are small (e.g., Top-1: 0.531 vs. 0.521 for MoMask; FID: 0.066 vs. 0.045 for MoMask). Without statistical testing, these differences could be within noise range.

4. **Overclaimed novelty and priority** (major): The abstract and contribution list use "first approach," "first attempt," and "no other methods currently exist" — unsupported priority claims that are contradicted by the paper's own references (Mao et al. 2024 uses RL for text-to-motion; Voas et al. 2023 and Wang et al. 2024 incorporate human perceptual priors).

5. **Limited PPO training and convergence concerns** (major): Only 2 PPO epochs are used (Page 7), which is unusually short. No learning curves, reward trends, or convergence analysis are provided. The critic loss (Eq. 10) is defined but never analyzed.

6. **Pareto selection sensitivity not characterized** (major): The batch-wise Pareto selection heuristic depends on batch size N and sampling diversity. No analysis of how often the non-dominated set is degenerate (empty or full batch) or how N affects performance is provided.

7. **User study lacks statistical rigor** (major): Only 30 prompts and 4-6 volunteers per comparison, with no inter-rater reliability, no confidence intervals, and no significance testing reported. The bar chart in Figure 3(b) does not report exact win rates.

8. **FID-perception gap claim not empirically verified** (minor): The paper's core motivation cites external work (Pinyoanuntapong et al. 2024) but does not provide its own evidence that FID scores on the studied models correlate poorly with human perception.

## Key Issues
### Issue 1: Circular Evaluation of Perception Model
**Severity: Major | Affects: Validity of perceptual quality claims**

The perception model (Wang et al., 2024) serves dual roles: as a reward signal during RL training (Eq. 6) and as an evaluation metric (Figure 3a). This creates a closed loop — the method is trained to maximize a specific model's output, then evaluated on the same model. The higher scores in Figure 3(a) may reflect overfitting to the perception model's specific preferences rather than genuinely superior motion quality. **Fix**: Replace perception model evaluation with an independent metric or emphasize the user study (with improved statistical rigor) as the primary perceptual validation.

### Issue 2: Missing Ablation Controls
**Severity: Major | Affects: Attribution of method gains**

Table 2 compares only (Rp), (Rp+Rm), and (Rp+Rm+Rt) — all using Pareto selection. Missing: (a) base pretrained generator without RL, (b) weighted-sum PPO baseline for direct Pareto comparison, (c) Rm-only and Rt-only conditions. Without these, the paper cannot demonstrate that Pareto selection (rather than reward addition) drives improvement. **Fix**: Add at least the weighted-sum PPO baseline and the no-RL baseline to Table 2.

### Issue 3: No Statistical Significance
**Severity: Major | Affects: Reliability of all quantitative claims**

Table 1 reports point estimates only — no variance, confidence intervals, or significance tests. Key improvements are small in absolute terms (e.g., FID 0.066 vs. 0.045 for MoMask; Top-1 0.531 vs. 0.521). Without variance, these could be within noise range. **Fix**: Report mean ± std over ≥3 seeds for all methods; add paired significance tests against the strongest baseline.

### Issue 4: Overclaimed Priority and Novelty
**Severity: Major | Affects: Credibility and positioning**

"First approach," "first attempt," "no other methods currently exist" are unverifiable priority claims contradicted by the paper's own references (Mao et al. 2024; Voas et al. 2023; Wang et al. 2024). **Fix**: Remove or replace with bounded wording: "to our knowledge, the first RL-based method that incorporates human perception as a reward alongside text adherence and motion quality."

### Issue 5: PPO Convergence Not Demonstrated
**Severity: Major | Affects: Reproducibility and training validity**

Only 2 PPO epochs are used with no convergence analysis, learning curves, or reward trend plots. The critic loss (Eq. 10) is defined but never monitored. **Fix**: Add training dynamics figure showing reward components and Pareto set size over iterations; justify the 2-epoch choice or increase epochs until convergence.

## Actionable Suggestions
### P0 (Must-fix before publication)

**S1. Add no-RL and weighted-sum baselines to ablation** (Addresses Issue 2)
Add two rows to Table 2: (a) "Pretrained generator (no RL)" showing InstructMotion's performance without any fine-tuning, and (b) "Weighted-sum PPO (Rp+Rm+Rt)" using manually tuned weights. This directly tests the benefit of Pareto selection over simple reward combination. Expected outcome: if Pareto selection is truly beneficial, it should outperform weighted-sum with comparable total compute.

**S2. Report variance and significance** (Addresses Issue 3)
Run all main experiments (Table 1) with at least 3 random seeds and report `mean ± std`. Use paired bootstrap or approximate permutation test to compare MotionRL against the strongest baseline (MoMask). If variance is high relative to the delta, acknowledge the uncertainty and adjust claim strength accordingly.

**S3. Add independent perception evaluation** (Addresses Issue 1)
Replace Figure 3(a) with an evaluation using a perception model NOT used during training. If no alternative model is available, remove the perception model scores from the main evaluation and instead rely on the user study (after improving its rigor). Add a sentence: "The perception model scores in Appendix reflect reward optimization progress; the user study (Section D) provides the primary perceptual validation."

**S4. Remove unsupported priority claims** (Addresses Issue 4)
Revise throughout: remove "first approach," "first attempt," "no other methods currently exist." Replace with: "We introduce an RL-based framework that integrates a pretrained human perception model as a reward signal alongside text adherence and motion quality objectives. While prior work has explored RL for text-to-motion (Mao et al., 2024) and perceptual evaluation (Voas et al., 2023; Wang et al., 2024), our method is the first to combine these with batch-wise Pareto selection for multi-objective optimization."

### P1 (High priority)

**S5. Add convergence analysis** (Addresses Issue 5)
Include a figure showing training curves: (a) moving average of each reward component (rt, rm, rp), (b) size of the Pareto set n(P) relative to batch size N over iterations, (c) critic loss. Compare 2-epoch vs. 5-epoch training on a validation split to justify the 2-epoch choice.

**S6. Improve user study rigor** (Addresses Issue 7)
Increase prompt sample to ≥100 with stratified sampling across motion categories. Recruit ≥10 volunteers per comparison. Report inter-rater reliability (Fleiss' kappa). Use a Bradley-Terry model to estimate preference scores with 95% confidence intervals. Report exact win/loss/draw counts and p-values from a binomial test.

**S7. Characterize Pareto selection behavior** (Addresses Issue 6)
Add an ablation sweeping batch size N (e.g., 8, 16, 32, 64) and reporting average |P|/N ratio, final FID, and Perception scores. This reveals whether Pareto selection is robust or N-sensitive.

### P2 (Quality improvement)

**S8. Fix introduction narrative structure** (Addresses writing quality)
See Storyline Options section for full rewrite guidance. Key changes: remove duplicated "On the other hand," restructure as Big Picture → Gap → Solution → Evidence.

**S9. Add qualitative selection criteria** (Addresses qualitative evaluation concern)
State in Section 5.3: "Examples in Figure 4 were randomly selected from the test set to represent typical outputs across all methods." This prevents cherry-picking concerns.

**S10. Provide reward normalization calibration details** (Addresses Eq. 12 concern)
Specify how `min_val_k` and `max_val_k` were estimated (e.g., calibration batch statistics from 1000 pretrained model samples). Report the actual range of normalized rewards during training.

## Storyline Options + Writing Outlines
### Current Introduction Paragraph Map (Problems)

| P# | Role | Current Defect |
|----|------|----------------|
| P1 | Establish demand + list challenges | Generic; challenges don't map cleanly to solution |
| P2 | Survey VAE/diffusion methods with limitations | Laundry-list style; motion-length limitation overemphasized |
| P3 | Note transformer methods fix length issue | "On the other hand" repetition creates confusion |
| P4 | Argue FID/perception gap + human perception neglected | Strong claim cited from external work, not own analysis |
| P5 | Note few studies use perception; list two challenges | Good gap paragraph |
| P6 | Propose MotionRL + Pareto solution | Clear summary |

### Recommended Storyline: Gap-Driven Narrative

**Abstract Outline (S1-S5):**
- S1 (Problem): "Text-to-motion generation has achieved impressive results on error-based metrics (FID, R-Precision), but these metrics poorly correlate with perceived motion naturalness."
- S2 (Gap): "Human perceptual quality remains underexplored as an optimization target in prior work."
- S3 (Method): "We introduce MotionRL, which fine-tunes an autoregressive motion generator using reinforcement learning with three reward signals: text adherence, motion quality, and human preference."
- S4 (Key Mechanism): "To avoid unstable weighted reward combinations, we propose a batch-wise Pareto selection strategy that only updates the policy on non-dominated samples across objectives."
- S5 (Result): "On HumanML3D, MotionRL achieves consistent improvements in FID, R-Precision, and human preference scores, validated by a user study."

**Introduction Outline (P1-P5):**
- P1 (Stakes + Gap): "Text-driven human motion generation has broad applications [refs]. However, current methods optimize for error-based metrics that fail to capture visual artifacts and perceived unnaturalness [specific ref]. Human perception of motion quality is arguably more meaningful yet largely overlooked."
- P2 (Prior work — what exists): Two concise paragraphs: (a) diffusion/masked models that require motion length input, with quality degradation when length is misspecified [ref]; (b) autoregressive transformer methods that avoid length dependency but still train on fixed datasets without perceptual feedback.
- P3 (Gap identification): "A small number of works have incorporated human perceptual priors [Voas, Wang], but directly integrating perception model losses into training can degrade other metrics and miss subtle perceptual nuances. RL offers a natural framework for optimizing non-differentiable perceptual objectives."
- P4 (Proposed solution): "We propose MotionRL, a PPO-based framework that uses a pretrained perception model as a reward signal alongside text adherence and motion quality. Our key technical contribution is a batch-wise Pareto selection mechanism that identifies non-dominated samples across the three rewards, avoiding unstable weighted combinations."
- P5 (Contributions + roadmap): Three bounded contribution statements (no "first" language; see S4 in actionable suggestions). Preview section structure.

### Title Revision Suggestion
Current: "MotionRL: Aligning Text-to-Motion Generation to Human Preferences with Multi-Reward Reinforcement Learning"

Improved: "MotionRL: Multi-Reward Reinforcement Learning for Human-Preference-Aligned Text-to-Motion Generation"

This version: (a) maintains the acronym "MotionRL," (b) clarifies it's about RL for motion generation, (c) makes "human-preference-aligned" the central descriptor, (d) is shorter and more direct.

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[Problem: Circular evaluation (perception model = reward + metric)]
    -> [Fix: Remove perception model as eval metric; use independent eval]
    -> [Expected gain: Valid perceptual claims; no circular logic concern]
    
[Problem: Missing ablation controls]
    -> [Fix: Add no-RL baseline + weighted-sum PPO + Rm/Rt-only rows]
    -> [Expected gain: Clear attribution of Pareto mechanism vs. reward addition]
    
[Problem: No statistical significance]
    -> [Fix: 3-seed runs + std + significance tests]
    -> [Expected gain: Reliable ranking; confidence in reported improvements]
    
[Problem: Overclaimed novelty ("first", "no other methods")]
    -> [Fix: Bounded wording throughout; remove priority claims]
    -> [Expected gain: Reviewer credibility; no factual contradiction with own refs]
    
[Problem: No convergence evidence]
    -> [Fix: Add training curves; test 5-epoch PPO]
    -> [Expected gain: Demonstrated training stability]
    
[Problem: Weak user study]
    -> [Fix: Larger sample; more volunteers; Bradley-Terry model; significance]
    -> [Expected gain: Statistically robust human preference evidence]
```

### Ranked Revision Priority (Highest Impact First)

| Rank | Issue | Fix | Effort | Impact | Category |
|------|-------|-----|--------|--------|----------|
| 1 | Circular perception evaluation | Remove Figure 3(a) or add independent metric | Low | High | Must |
| 2 | Missing ablation baselines | Add no-RL + weighted-sum PPO to Table 2 | Medium | High | Must |
| 3 | No statistical significance | 3-seed runs + std + significance tests | Medium | High | Must |
| 4 | Overclaimed novelty | Revise Abstract, C2, Conclusion wording | Low | High | Must |
| 5 | PPO convergence | Add training dynamics figure | Low | Medium | Must |
| 6 | Weak user study | Larger N + Bradley-Terry + significance | High | High | Must |
| 7 | Pareto selection characterization | Batch size N sweep | Medium | Medium | High |
| 8 | Introduction narrative | Restructure per Storyline Options | Low | Medium | Nice-to-have |
| 9 | Qualitative selection criteria | Add sampling protocol sentence | Low | Low | Nice-to-have |
| 10 | Reward normalization details | Add calibration procedure | Low | Low | Nice-to-have |

### Expected Impact After Fixes
- **Scientific validity**: Circular evaluation concern resolved; statistical reliability established.
- **Credibility**: Priority claims removed; novelty framed accurately.
- **Reproducibility**: Training dynamics and normalization details documented.
- **Overall quality**: From borderline acceptance to solid acceptance if fixes are executed cleanly.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|--------|-----------|-------|---------|-------------|-----------------|------------|
| E1 | Main benchmark comparison (Table 1) | HumanML3D test set, 16 baselines | R-Precision (Top-1/2/3), FID, MM-Dist, Diversity, MModality | Ours: FID 0.066, Top-1 0.531 (best among all methods) | C3 (performance superiority) | No variance/CI; baseline comparisons not all controlled (different architectures) |
| E2 | Perception model scores (Fig 3a) | HumanML3D test set, Wang et al. 2024 evaluator | Perception model score | Ours scores highest | C2 (human perception alignment) | Circular evaluation — same model used as reward |
| E3 | User study (Fig 3b) | 30 prompts, 4-6 volunteers/comparison | Win rate (pairwise) | Ours preferred over baselines | C2, C3 | Small N, no significance, no inter-rater reliability |
| E4 | Qualitative comparison (Fig 4) | 4 test prompts | Visual comparison | Ours generates accurate motions | C3 | Cherry-picking risk; no selection protocol stated |
| E5 | Ablation — Reward Design (Table 2) | 3 reward combinations (Rp, Rp+Rm, Rp+Rm+Rt) | Top-1, FID, Perception | Full set best: Top-1 0.531, FID 0.064, Perception 0.494 | C1 (multi-reward effectiveness) | Missing no-RL, weighted-sum, Rm-only, Rt-only baselines |
| E6 | Pareto selection + token analysis (Fig 5) | Reward-specific tokens with/without Pareto | Reward values | Pareto improves overall reward | C1 (Pareto effectiveness) | Reward scale normalization makes cross-objective comparison uninformative |
| E7 | Joint-to-SMPL conversion (Appendix A) | Conv1D+LSTM network | Conversion speed, quality | Faster than iterative methods | Engineering contribution | No quantitative speed/quality comparison |

### Research-Theme Gap Diagnosis

| Theme | Current Status | Weakness | Required Action |
|-------|---------------|----------|-----------------|
| New knowledge | Pareto-based multi-reward RL for text-to-motion | True novelty unverifiable without retrieval; incremental over Mao et al. 2024 and Wang et al. 2024 | Defer to manual literature verification; bounded claim scope |
| Reproducibility/Reusability | Method described with pseudocode; VQ-VAE + GPT architecture from prior work | PPO convergence not demonstrated; reward normalization calibration unspecified | Add training curves, normalization calibration details, code release |
| Impact on practice/understanding | Demonstrates perception-aware fine-tuning improves perceptual scores | Circular evaluation weakens practical impact claim | Independent perception evaluation needed |

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

P0 Experiments (Before Resubmission)
├── E1a: Statistical significance package
│   ├── Run Table 1 with 3 seeds → mean ± std for all metrics
│   ├── Paired bootstrap test: Ours vs. MoMask
│   └── Expected gain: Reliable ranking, confidence in deltas
├── E1b: Ablation completion for Table 2
│   ├── Add row: Pretrained generator (no RL fine-tuning)
│   ├── Add row: Weighted-sum PPO (Rp+Rm+Rt) with tuned weights
│   ├── Add rows: Rm-only, Rt-only (single reward)
│   └── Expected gain: Clear attribution of Pareto mechanism
└── E1c: Perception model independence
    ├── Use alternative perception evaluator (not used in training)
    ├── Or: Report only user study as perceptual validation
    └── Expected gain: No circular evaluation concern

P1 Experiments (High Priority)
├── E2a: Convergence analysis
│   ├── Plot reward components (rt, rm, rp) across training
│   ├── Plot n(P)/N ratio (Pareto set utilization)
│   ├── Compare 2 vs. 5 PPO epochs on validation
│   └── Expected gain: Demonstrated training stability
├── E2b: Batch size sensitivity for Pareto selection
│   ├── Sweep N ∈ {8, 16, 32, 64}
│   ├── Report final FID, Perception, avg |P|/N
│   └── Expected gain: Robustness characterization
└── E2c: Enhanced user study
    ├── Increase to ≥100 prompts (stratified)
    ├── ≥10 volunteers; report Fleiss' kappa
    ├── Bradley-Terry preference scores + 95% CI
    └── Expected gain: Statistically robust human preference evidence

P2 Experiments (Quality Improvement)
├── E3a: Reward normalization calibration documentation
└── E3b: FID-perception correlation analysis on own models
```

### Detailed Proposal for Critical Missing Experiments

**P0-E1b: Ablation — Weighted-Sum PPO Baseline**
- **Target Claim**: C1 — Pareto selection outperforms weighted-sum reward combination
- **Hypothesis**: Batch-wise Pareto selection yields better FID and Perception than any single weighted combination of (Rp, Rm, Rt)
- **Minimal Design**: Train PPO with reward = α·rp + β·rm + γ·rt, grid-search α,β,γ on validation (e.g., 8 combinations). Report best validation result on test set.
- **Controls**: Same PPO hyperparameters, same compute budget (40k iterations, 2 epochs)
- **Metrics**: Top-1, FID, Perception (using independent evaluator)
- **Success Criterion**: Pareto selection must be at least comparable to best weighted combination; ideally >1% FID improvement
- **Estimated Cost/Time**: ~2-3 GPU-days (4× RTX 3090) for 8 weight combinations
- **Expected Paper-Quality Gain**: Direct evidence for the main technical contribution of the paper

**P0-E1a: Statistical Significance**
- **Target Claim**: C3 — MotionRL achieves superior performance over baselines
- **Hypothesis**: Observed improvements are statistically significant
- **Minimal Design**: Repeat Table 1 experiments with 3 random seeds; report `mean±std` for all metrics. Compute paired bootstrap p-value (Ours vs. MoMask) for FID and Top-1.
- **Success Criterion**: p < 0.05 for both FID and Top-1; otherwise acknowledge non-significance and bound claim
- **Estimated Cost/Time**: ~3× current compute (re-run main experiment 3 times)
- **Expected Paper-Quality Gain**: Scientific reliability; defensible comparative claims

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

*Rationale:* The paper addresses a meaningful problem (incorporating human perception into text-to-motion generation) and proposes a technically sound Pareto-based multi-reward RL framework. The empirical results on HumanML3D are competitive. However, several major issues reduce confidence in the reported claims: (1) circular evaluation design (perception model used as both reward and metric), (2) missing ablation baselines that prevent attribution of gains to the core Pareto mechanism, (3) no statistical significance reporting despite modest performance deltas, (4) unverifiable priority claims ("first approach," "no other methods currently exist"), and (5) insufficient convergence evidence for the RL training. These issues are fixable with additional experiments and wording revisions, but in the current form, the empirical justification for the core technical claim (Pareto selection benefit) is incomplete.

**Post-Revision Target: [6.5, 7.5]/10**

*Rationale:* If the authors execute the P0 fixes (circular evaluation resolved, ablation controls added, statistical significance established, priority claims removed, convergence shown) and at least one of the P1 experiments (enhanced user study, Pareto sensitivity analysis), the paper would provide a well-supported empirical contribution. The upper bound (7.5) assumes strong results from the controlled ablation and significance tests. The lower bound (6.5) assumes the results hold but with modest effect sizes. The core idea has value; the main gap is in experimental validation rigor, not in the conceptual contribution.