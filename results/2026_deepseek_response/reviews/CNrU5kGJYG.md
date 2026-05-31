## Summary

This paper proposes TrojanTO, the first post-training action-level backdoor attack against trajectory optimization (TO) models in offline RL. The key insight is that reward manipulation—central to prior RL backdoors—is ineffective for TO models, so the attack focuses on forging a strong trigger–target-action connection via alternating training, trajectory filtering, and batch poisoning. Experiments across 6 D4RL environments and 3 TO architectures (DT, GDT, DC) show TrojanTO achieves 0.701 CP with only 0.3% poisoned trajectories, compared to 0.342 CP for Baffle (10%) and 0.551 CP for IMC.

## Strengths

- **Empirical finding that reward manipulation is ineffective for TO models** (Section 4.3, Figure 1). This is a concrete, evidence-based refutation of the core assumption in prior RL backdoor work. The result holds consistently across DT, DC, and GDT models with five reward manipulation variants, demonstrating that all converge to the same ASR and BTP regardless of reward perturbation.

- **Clear ablation study showing each component contributes independently** (Table 5). Removing alternating training drops ASR from 0.719 to 0.507 (29.5%↓), removing batch poisoning drops ASR to 0.528, and removing trajectory filtering drops BTP from 0.914 to 0.850. Each removal degrades a distinct metric, confirming the design rationale for each component.

- **Systematic investigation of target action selection across six types** (Table 1, Section 4.1). The paper shows ASR varies from 0.110 to 1.000 depending on target type (boundary actions like '1' and '-1' yield near-100% ASR; interior actions like '0' yield as low as 0.11). This establishes that evaluation must consider diverse target actions—going beyond prior work that used a single fixed target.

- **Evaluation across six environments and three TO architectures** (Table 4). Results span locomotion (Hopper, HalfCheetah, Walker2d), navigation (AntMaze), and manipulation (Kitchen, Pen) with models DT, GDT, and DC. TrojanTO achieves CP ≥ 0.88 on 5 of 18 model–environment combinations, demonstrating generalization beyond a single architecture or task type.

- **Persistent backdoor characterization** (Table 6, Section 6.3). The paper quantifies sustained malicious behavior over k=5, 10, 15 steps after a single trigger activation, with CP degrading only modestly (e.g., from 0.993 at k=0 to 0.928 at k=10 for Walk). It also identifies the context-window bound as an inherent limitation, which is an honest and useful characterization.

## Weaknesses

### Major

- **Missing variance reporting in Table 4.** The paper reports only point estimates for ASR, BTP, and CP averaged over three seeds, with no standard deviations or confidence intervals. Other tables (Tables 6, 7) include ± values, making this omission conspicuous. Without variance, the reader cannot assess whether TrojanTO's advantages over baselines are meaningful or within noise (e.g., DT Hopp: TrojanTO ASR 0.362 vs. Baffle 0.365—these are essentially tied, yet the overall CP framing claims 105% improvement). The claim that TrojanTO "exhibits consistent robustness and stability across varied tasks" is unsupported by the reported data. The authors have three seeds; including standard deviations is cheap and would significantly strengthen the claims.

- **Unclear data source for the post-training attack.** The threat model (Section 3.3) states the adversary modifies a pretrained model "without access to the original training dataset." Yet the method (Section 5) requires trajectories for filtering, batch poisoning, and alternating training. The paper never clarifies where these trajectories come from—whether the adversary collects new trajectories by rolling out the clean model in the environment (which would require environment access, itself a strong assumption), uses a public benchmark dataset like D4RL, or has a proxy dataset. This is a genuine gap in the threat model description that affects the practicality assessment.

### Minor

- **ASR threshold ε not stated in the main text.** Equation (2) defines attack success using a threshold ε on each action component, but no value is given in the main body. The paper references Appendix I for implementation details, but the main text should state or at least prominently reference the chosen value. Without it, the reader cannot evaluate whether the ASR metric is strict or lenient (a large ε could inflate ASR for roughly correct actions).

- **Baseline comparison framing.** The primary baseline Baffle operates under a different threat model (pre-training data poisoning at 10% rate) from TrojanTO (post-training, 0.3% rate). The paper is transparent about the poisoning rates and threat models (Section 3.3), and listing Baffle as a reference point is reasonable. However, the framing "105% higher CP" (Section 6.1) and "0.701 CP vs. 0.342 CP" implicitly favors the comparison without controlling for the threat-model asymmetry. Adding one within-threat-model baseline (e.g., post-training fine-tuning with a fixed trigger but without alternating training) would cleanly isolate the contribution of TrojanTO's specific design choices.

- **Trigger dimension sensitivity unevaluated.** The paper fixes trigger dimensions to (1,2,3) based on Table 2 showing highest ASR for Half and Walk. However, it does not discuss whether this choice generalizes across environments with different state-space semantics or whether the optimal dimensions must be tuned per environment (which would increase adversary knowledge requirements). A sensitivity analysis across random dimension subsets beyond Table 2 would strengthen generality claims.

- **Defense evaluation is perfunctory.** Section 6.5 dismisses multiple defense methods (weight pruning, spectral analysis, activation clustering, fine-tuning) in essentially one sentence and refers to the appendix. The claim that "fine-tuning is the most effective defense" is unsupported by evidence in the main text. As written, this section adds little value and should either be expanded substantially or removed.

### Trivial

None that survive filtering.

## Nice-to-Haves

- Report compute cost (GPU hours, number of gradient steps) for the post-training fine-tuning to help practitioners assess practicality.
- Discuss how the trigger is physically applied to state observations in practice (e.g., sensor perturbation in a robotic setting) to ground the threat model in reality.
- Include a brief note on the feasibility of the inference-time observation manipulation assumed in the threat model.

## Removed Points

- *"Unfair baseline comparison that inflates the claimed advantage" as a structural issue* — The paper is transparent about different threat models (Section 3.3) and poisoning rates (0.3% vs 10%). Comparing against the best existing method in the area is standard practice; the paper does not hide the asymmetry. I downgrade this to a minor weakness about the framing wanting an additional within-threat-model baseline, not a structural flaw.
- *"IMC is adapted from image classification"* — This is a factual observation, not a weakness. Adaptation from another domain is standard when no directly comparable method exists.
- *"Missing related works"* — Cannot confirm without external sources; excluded per instructions.
- *"Pure formatting/style nitpicks"* (figure legibility, parser artifacts) — Removed per instructions. These are parser issues, not author errors.
- *"Reproducibility nitpicks about undisclosed hyperparameters"* — The paper states full details are in appendices and code is provided; this is standard practice.
- *Strength Finder: generic strengths* (e.g., "the paper addresses an important problem") — Removed for lacking specific evidence.
- *"Misses a dedicated limitations section"* — The paper does not have one, but limitations are partially addressed (context window bound, DC+Ant failure). Asking for a formal limitations section is a style preference, not a substantive weakness.
- *Strength Finder: "0.3% poisoning rate achieving 0.701 CP vs. 10% rate achieving 0.342 CP"* — This conflates the comparison without controlling for threat model differences. Kept the factual observation (the paper achieves strong results with 0.3%) as part of the evaluation rather than as an isolated strength claim.

## Novel Insights

The reviews surface a useful meta-point: TrojanTO's core innovation lies in recognizing that TO models' *training objective* (reconstruction loss, not reward maximization) fundamentally changes the backdoor attack surface. Where prior RL backdoors manipulate the reward signal to corrupt policy learning, TrojanTO shows that for TO models, the adversary only needs to control the trigger–action coupling. This insight—that the attack vector shifts from *what the agent optimizes for* to *what the agent reconstructs*—is implicit in the paper and could be stated more explicitly as a general design principle for backdoor attacks on sequence-modeling-based policies.

## Suggestions

1. Report standard deviations for all metrics in Table 4 (the authors have three seeds, so this is cheap to add).
2. Clarify in Section 5.1 where the adversary's trajectories come from, given the "no access to original training dataset" threat model.
3. State the ε threshold for ASR in Section 3.4 (main text).
4. Add one within-threat-model baseline for a cleaner comparison (e.g., post-training fine-tuning with a fixed trigger, minus alternating training).
5. Either expand Section 6.5 with concrete results or remove it from the main text.

## Score and Decision

**Calibration anchors (all rounds):**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Deferred Backdoor Functionality | S5JCqTJyKj.md | 3.00 | R1 bracketing | Much weaker (conceptual flaws, no substantive eval) |
| Certified Copy Backdoor | 66e22qCU5i.md | 3.00 | R1 bracketing | Much weaker |
| TrojanRAG | RfYD6v829Y.md | 3.40 | R1 bracketing | Much weaker |
| Behavior Adaptation Q-Learning | d159zNCmOq.md | 3.40 | R1 bracketing | Weaker (not backdoor-focused) |
| Multi-Vehicle Backdoor AD | em0gAL8fbK.md | 4.00 | R1 bracketing | Weaker (high poisoning rate, threat model issues) |
| Relaxed State-Adversarial Offline RL | P895PSh41Z.md | 4.50 | R1 bracketing | Weaker (different topic, less thorough) |
| Tree-based Action-Manipulation Attack | HZnnHDrBXD.md | 5.75 | R2 narrowing | Slightly weaker (only 2 environments, no ablation study depth) |
| Backdoor Contrastive Learning via Bi-level | oxjeePpgSP.md | 5.75 | R2 narrowing | Comparable quality (both accepted, similar rigor) |
| BALD (Embodied LLM Backdoor) | S1Bv3068Xt.md | 6.25 | R2 narrowing | Slightly stronger (more comprehensive eval, multiple models) |
| Multi-level Certified Defense ORL | X2x2DuGIbx.md | 6.75 | R1 bracketing | Stronger (theoretical contributions) |
| Illusory Attacks | F5dhGCdyYh.md | 7.33 | R2 narrowing | Stronger (theoretical depth) |
| Single-agent Poisoning MARL | 46xYl55hdc.md | 7.00 | R2 narrowing | Stronger (theoretical contributions) |
| DeepLTL, Policy Gradient POMDP, etc. | 9pW2J49flQ.md etc. | 8.00 | R1 bracketing | Much stronger (top-tier contributions) |

**Round 1 bracket:** Between ~4.0 and ~7.0. The paper is clearly above papers scoring ~3 (which have fatal flaws) and below papers scoring ~7+ (which have theoretical contributions or exceptional empirical scope).

**Round 2 narrowing:** The paper sits near the backdoor contrastive learning paper (5.75) and the action-manipulation attack paper (5.75), both of which are accepted or well-received. It is slightly weaker than the BALD embodied LLM backdoor paper (6.25, accepted) which had broader scope. The missing variance in the main results table and the unclear data source are the main factors keeping this from the 6+ range.

**Final score:** 5.5

TrojanTO proposes a novel, well-motivated attack for an underexplored security setting (TO models in offline RL). The method is cleanly designed, the ablation study is informative, and the key finding about reward manipulation's irrelevance is a genuine contribution. However, the absence of variance reporting in Table 4, the unresolved data source question in the threat model, and the thin defense evaluation prevent the paper from reaching the top tier. These issues are fixable and do not undermine the core contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>