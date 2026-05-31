## Summary
TrojanTO is a post-training, action-level backdoor attack against Trajectory Optimization (TO) models in offline RL. The paper first establishes, through empirical studies, that target action selection and trigger design are the critical factors for attacking TO models, while reward manipulation (standard in classical RL backdoors) is ineffective. Guided by these findings, TrojanTO combines three components—trajectory filtering, batch poisoning, and alternating training via MI-FGSM-based trigger optimization—to achieve high attack success rates (0.719 average ASR) at a remarkably low poisoning budget (0.3%), outperforming baselines Baffle and IMC on CP across three TO architectures and six D4RL tasks.

---

## Strengths

- **Genuine novelty and well-motivated problem formulation.** The paper is the first to systematically study post-training, action-level backdoor attacks against TO models. The argument for why existing reward-manipulation attacks fail—TO models minimize reconstruction loss and do not rely on Bellman equations—is clearly stated and empirically validated (Figure 1). This fills a real gap in the security literature for offline RL.

- **Strong and reproducible empirical results.** TrojanTO achieves an average CP of 0.701 with only 0.3% poisoning rate, compared to Baffle's 0.342 at 10% and IMC's 0.551, representing a 105% improvement over Baffle. The evaluation is thorough: 6 environments, 3 architectures (DT, GDT, DC), 3 target action types, 3 random seeds—giving high confidence in aggregate results.

- **Principled diagnostic section (Section 4).** The investigation of three factors (target action, trigger dimensions, trigger values, reward manipulation) is methodologically sound and directly informs the design of TrojanTO. Table 1 shows ASR ranging from 0.11 to 1.0 across target action types; Table 2 shows ASR of 0.0 to 0.915 across trigger dimension choices. These diagnostics provide a concrete empirical foundation for design decisions.

- **Ablation study confirms component contributions.** Table 5 isolates each module: removing batch poisoning drops average ASR from 0.719 to 0.528; removing alternating training drops it to 0.507; removing trajectory filtering hurts BTP most (0.914 → 0.850). The decomposition is clean and convincing.

---

## Weaknesses

### Fatal
None.

### Major

- **Trigger dimension selection is under-specified and potentially optimistic.** Table 2 shows that dimensions (1,2,3) achieve ASR up to 0.915, while dimensions (1,10,14) yield 0.000. The paper fixes dimensions to (1,2,3) for all subsequent experiments but provides only a brief note that Appendix F contains "additional attempts." It is not clear whether baselines in Table 4 were evaluated under the same dimension choice, or whether TrojanTO benefits from an optimized dimension setup that Baffle and IMC did not enjoy. A fair comparison requires either (a) confirming all methods used equally optimized trigger dimensions, or (b) reporting performance across multiple dimension choices for all methods. This matters because the performance gap between TrojanTO and baselines might partly reflect trigger-dimension selection rather than the attack framework itself.

- **Unexplained failure cases are non-trivial.** TrojanTO is outperformed by baselines in several specific settings: DT/Kit (0.614 CP vs Baffle's 0.766), DC/Ant (0.559 vs IMC's 0.752), and DC/Pen (0.477 vs IMC's 0.655). These gaps are substantial and not explained in the paper. Understanding when and why TrojanTO underperforms is important for characterizing the attack's applicability. Simply noting "complete results in Appendix K.3" without analysis is insufficient.

### Minor

- **Defense evaluation is thin in the main paper.** Section 6.5 mentions that fine-tuning is the most effective defense but provides no quantitative results in the main body. The paper acknowledges TrojanTO is vulnerable to fine-tuning, but the severity (how much data, what performance cost) is entirely in the appendix. A brief table summarizing fine-tuning results—including the trade-off between defense effectiveness and clean performance recovery—would strengthen the paper's security narrative.

- **Threshold ε for ASR is not stated in the main paper.** The ASR metric (Equation 2) depends critically on the threshold ε, yet its value is not reported in the main text. Results could vary significantly with different ε choices, and readers need this to assess tightness of the attack.

- **Persistent backdoor is fundamentally limited by context window.** Section 6.3 introduces a persistent attack but acknowledges it is bounded by the model's context window (~20 steps). This limits practical impact, and the section presents relatively modest results (Table 6 shows CP gracefully degrading). The framing slightly overstates the practical threat.

### Trivial

- The BTP definition (Eq. 3) computes ratios per episode; if a clean policy achieves near-zero return in a task, BTP is undefined or unstable. This is not addressed.

---

## Nice-to-Haves

- A comparison of TrojanTO versus Baffle/IMC using identical trigger dimension setups would conclusively establish fair attribution of gains.
- Including a short table in the main paper summarizing defense results (e.g., fine-tuning with 1%/5%/10% of clean data) would significantly strengthen the security analysis.
- An explanation (even intuitive) for why dimensions (1,2,3) consistently outperform other dimension choices would enhance scientific insight.

---

## Novel Insights

The central novel insight—that reward signals are irrelevant for backdooring TO models because their training objective is behavioral cloning (MSE/CE over action sequences) rather than return maximization—is both theoretically grounded and empirically verified. This insight suggests a broader class of sequence-model-based policies may share this property, meaning that post-training model manipulation rather than reward poisoning is the correct attack surface for transformer-based policies. The finding that trigger dimensions matter as much as trigger values (with some dimension choices yielding 0% ASR regardless of value optimization) is also interesting, though the mechanism remains unexplained. The batch poisoning strategy—poisoning only one transition per batch to reduce OOD mismatch between training and inference contexts—is a practically sensible design choice that is not obvious from prior work.

---

## Suggestions

- For Table 4, explicitly state the trigger dimensions used for all methods and confirm all are evaluated at their respective optima.
- Add a paragraph in Section 6.5 with a quantitative fine-tuning defense table (budget vs. ASR/BTP) in the main paper.
- Provide an analysis of DT/Kit, DC/Ant, and DC/Pen failure cases—either structural properties of these tasks or dataset artifacts that make the attack harder.
- State the ASR threshold ε explicitly in Section 3.4.

---

## Score and Decision

TrojanTO addresses a timely and under-studied security problem with a well-motivated and technically sound approach. The core insight (reward manipulation is irrelevant for TO models) is backed by solid experiments and directly informs a practically useful attack. The experimental coverage is broad and the improvements over baselines are substantial in most settings. The main reservations concern the potential optimism in trigger dimension selection affecting baseline fairness, and unexplained failure cases in specific environments. These are important but not fatal flaws.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>