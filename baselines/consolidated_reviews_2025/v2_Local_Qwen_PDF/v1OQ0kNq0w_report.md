## Summary
# Final Review Report

## Summary
This paper introduces MotionRL, a reinforcement learning framework designed to align text-to-motion generation with human preferences. The authors identify a gap in prior works that primarily optimize for numerical metrics (e.g., FID, R-Precision) which may not correlate well with human perception. To address this, MotionRL employs a multi-reward RL approach incorporating text adherence, motion quality, and a pre-trained human perception model score. A key methodological component is a batch-wise Pareto-optimal selection strategy intended to balance these competing objectives without manual weight tuning. Experiments on the HumanML3D dataset report improvements in R-Precision and perception scores over strong baselines like MoMask and InstructMotion. While the motivation of aligning generation with human perception is compelling, the manuscript suffers from critical methodological flaws in the Pareto selection algorithm, factual inconsistencies in experimental claims (e.g., FID scores), and overstatements of novelty.

## Strengths
1. **Compelling Motivation:** The paper correctly identifies a significant gap in text-to-motion generation: the disconnect between standard numerical metrics (FID, R-Precision) and actual human perception. Aligning generative models with human preferences is a highly relevant and impactful research direction.
2. **Multi-Reward RL Framework:** The proposal to use reinforcement learning with multiple distinct rewards (text adherence, motion quality, human perception) is a logical step toward preference-aligned generation. The idea of using reward-specific tokens to control trade-offs during inference is practically useful.
3. **Comprehensive Evaluation:** The authors provide a thorough evaluation on the HumanML3D dataset, including quantitative metrics, perception model scores, user studies, and qualitative visualizations. The inclusion of a user study adds valuable empirical evidence for the human preference claim.

## Weaknesses
1. **Critical Flaw in Pareto Selection Algorithm:** Algorithm 1 incorrectly computes the Pareto-optimal set. The outer loop iterates over each reward type `k` separately, sampling motions with a specific reward token and computing only that reward. Pareto dominance requires comparing samples across *all* K objectives simultaneously. Processing rewards in isolation makes the multi-objective optimization claim invalid.
2. **Factual Inconsistencies in Experimental Claims:** The text claims MotionRL outperforms baselines in FID, but Table 1 shows MotionRL's FID (0.721) is worse than MoMask (0.713) and InstructMotion (0.694). Additionally, Table 2 reports drastically different FID scores (~0.06-0.09) without explanation, raising reproducibility concerns.
3. **Problematic Motion Quality Reward:** Equation (4) defines motion quality reward using the ground truth motion sequence ($m_{gt}$). In text-to-motion generation, $m_{gt}$ is unavailable during inference, and using it as an RL reward encourages reconstruction rather than diverse generation, risking mode collapse.
4. **Overstated Novelty and Weak Contributions:** The claim of being the "first approach" to use RL for human perception in text-to-motion is too broad, especially given recent RL-based motion works (e.g., InstructMotion). The third contribution is merely experimental validation, which dilutes the conceptual impact.
5. **Insufficient Ablation and Baseline Reporting:** Table 2 lacks a baseline row (pre-trained model without RL), making it impossible to assess the absolute gain of the RL rewards. The ablation does not isolate the impact of the Pareto selection mechanism versus standard weighted reward summation.

## Key Issues
1. **Algorithm 1 Logical Error (Critical):** The Pareto dominance check is performed within a loop that isolates each reward type. This means the algorithm never compares samples across multiple objectives simultaneously, fundamentally breaking the multi-objective optimization claim. The algorithm must be revised to compute all K rewards for each sample in a batch before identifying the non-dominated set.
2. **FID Metric Contradiction (Major):** The manuscript claims superiority in FID, but Table 1 shows a worse FID score than baselines. Furthermore, Table 2 reports FID scores an order of magnitude lower than Table 1 without justification. This inconsistency severely undermines the credibility of the experimental section.
3. **Ground Truth Dependency in RL Reward (Major):** Using $m_{gt}$ in the motion quality reward (Eq. 4) is incompatible with open-ended generation. It forces the model to reconstruct specific training examples rather than learning a general quality prior, which contradicts the goal of diverse text-to-motion generation.
4. **Unverified Novelty Claims (Major):** The "first attempt" claim is not sufficiently bounded. Given the rapid progress in RL-based motion generation, this claim is vulnerable to rejection unless precisely scoped to the specific combination of Pareto optimization and perception rewards.

## Actionable Suggestions
1. **Fix Algorithm 1:** Revise the algorithm to sample a batch of motions once, compute all K rewards for each motion, and then perform the Pareto dominance check across the full K-dimensional reward vectors. Remove the outer loop over reward types.
2. **Correct FID Claims and Tables:** Verify the FID calculation protocol. Ensure Table 1 and Table 2 use the same metric definition. Remove the claim of FID superiority if the score is worse than baselines; instead, emphasize competitive FID without length dependency.
3. **Redesign Motion Quality Reward:** Replace the ground-truth-dependent reward (Eq. 4) with a self-supervised motion quality predictor or a discriminator-based reward that evaluates naturalness without requiring $m_{gt}$.
4. **Bound Novelty Claims:** Rephrase the "first attempt" claim to specifically highlight the Pareto-based multi-reward optimization for perception alignment. Add a comparison or discussion of InstructMotion to clarify the differentiation.
5. **Expand Ablation Study:** Add a baseline row to Table 2 showing the pre-trained model's performance without RL. Include an ablation comparing Pareto selection against simple weighted reward summation to isolate the contribution of the Pareto mechanism.
6. **Strengthen Limitations:** Discuss computational costs, potential reward hacking risks, and generalization to other datasets (e.g., KIT-ML) in the limitations section.

## Storyline Options + Writing Outlines
### Abstract Outline
- **S1 (Problem):** Text-to-motion generation is critical for animation and robotics, but current methods prioritize numerical metrics that poorly correlate with human perception.
- **S2 (Gap):** Directly optimizing perception models alongside traditional metrics often leads to conflicting gradients and degraded semantic alignment.
- **S3 (Method):** We propose MotionRL, a reinforcement learning framework that aligns generation with human preferences via multi-reward optimization and a batch-wise Pareto selection strategy.
- **S4 (Mechanism):** By using reward-specific tokens and approximating Pareto optimality, MotionRL automatically balances text adherence, motion quality, and perceptual naturalness without manual weight tuning.
- **S5 (Result):** Experiments on HumanML3D demonstrate consistent improvements in perception scores and R-Precision over strong baselines, with controllable generation via preference tokens.

### Introduction Outline
- **P1 (Big Picture):** Establish the demand for high-quality, text-driven human motion in animation, gaming, and robotics.
- **P2 (Gap 1 - Generation):** Briefly summarize VAE, diffusion, and transformer-based methods, noting their focus on structural fidelity and semantic alignment.
- **P3 (Gap 2 - Perception):** Highlight the disconnect between proxy metrics (FID, R-Precision) and human judgment. Explain why directly incorporating perception priors is challenging (gradient conflicts, mode collapse).
- **P4 (Solution):** Introduce MotionRL as an RL-based solution that uses a pre-trained perception model as a reward signal. Explain the intuition behind Pareto-optimal selection for balancing competing objectives.
- **P5 (Evidence):** Preview key results: improved perception scores, competitive FID without length dependency, and user study validation.
- **P6 (Contributions):** List 3 concise contributions: (1) Multi-reward RL framework for perception alignment, (2) Batch-wise Pareto selection mechanism, (3) Comprehensive evaluation demonstrating preference-aligned generation.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Fix Algorithm 1 to compute Pareto sets across all K rewards simultaneously. | Resolves critical methodological flaw; validates core contribution. | Medium |
| **P0** | Correct FID claims and reconcile Table 1 vs Table 2 metric inconsistencies. | Restores factual credibility and reproducibility. | Low |
| **P1** | Redesign motion quality reward to remove ground-truth dependency ($m_{gt}$). | Prevents mode collapse; aligns with open-ended generation goals. | Medium |
| **P1** | Bound novelty claims and add comparison with InstructMotion. | Strengthens defensibility against reviewer challenges. | Low |
| **P2** | Expand ablation study with baseline row and Pareto vs. weighted sum comparison. | Isolates component contributions; improves empirical rigor. | Medium |
| **P2** | Expand limitations section to cover computational cost and dataset generalization. | Improves scientific honesty and frames future work. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Main quantitative comparison | HumanML3D, vs MoMask/T2M-GPT/InstructMotion | R-Precision, FID, MM-Dist, Diversity, Modality | Ours achieves highest R-Precision (0.531) | Superior text adherence | FID claim contradicts table data |
| E2 | Human preference evaluation | HumanML3D, perception model (Wang et al.) + User Study | Perception score, User win rate | Higher perception scores and user preference | Alignment with human perception | User study sample size (30 prompts) is small |
| E3 | Reward ablation | HumanML3D, varying reward combinations (Rp, Rm, Rt) | Top-1, FID, Perception | All rewards contribute; full combo best | Multi-reward necessity | Missing baseline row; FID inconsistency |
| E4 | Pareto & Token ablation | HumanML3D, Pareto selection vs standard, reward tokens | Reward values | Pareto improves rewards; tokens enable control | Pareto/token effectiveness | No comparison to weighted-sum baseline |

### Research-Theme Gap Diagnosis
The core claim of preference-aligned generation via Pareto RL is weakly supported due to the algorithmic flaw in Pareto selection and the lack of a direct comparison against standard multi-task learning or weighted RL baselines. The motion quality reward's dependency on ground truth further weakens the generalization claim.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Pareto Optimization Validity | Pareto selection outperforms weighted reward summation in balancing objectives. | Train with fixed weights vs. Pareto selection. | Weighted RL baseline. | R-Precision, Perception, FID | Pareto shows better trade-off curve. | Low | Isolates Pareto contribution |
| Motion Quality Reward | Self-supervised quality reward generalizes better than GT-dependent reward. | Replace Eq. 4 with discriminator-based reward. | Current Eq. 4 setup. | Diversity, Modality, Perception | Higher diversity without perception drop. | Medium | Fixes mode collapse risk |
| Cross-Dataset Generalization | MotionRL improves perception on unseen datasets. | Evaluate on KIT-ML without fine-tuning. | InstructMotion, MoMask. | Perception score, User study | Consistent perception gains. | Low | Strengthens generalization claim |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 4/10
Post-Revision Target: [6, 7]/10

**Rationale:** The paper addresses a highly relevant problem (aligning motion generation with human perception) and proposes an intuitive RL-based solution. However, the current manuscript contains a critical flaw in the core Pareto selection algorithm (Algorithm 1), factual inconsistencies in experimental claims (FID scores), and a problematic reward design that relies on ground-truth motion. These issues severely undermine the validity of the main contributions. If the authors can fix the algorithm, reconcile the metrics, and redesign the motion quality reward, the paper has the potential to reach a solid acceptance score due to its strong motivation and comprehensive evaluation.