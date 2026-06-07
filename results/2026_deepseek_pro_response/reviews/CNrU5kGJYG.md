Now let me finalize my calibration analysis. Here are all the anchors I retrieved across both rounds:

**Round 1 (Bracketing):**
- S5JCqTJyKj (3.00) — Deferred Backdoor Functionality: clearly weaker, different domain
- 66e22qCU5i (3.00) — Certified Copy: clearly weaker, different domain
- d159zNCmOq (3.40) — Offline-to-online RL: not a backdoor paper, irrelevant
- RfYD6v829Y (3.40) — TrojanRAG: LLM backdoors, different domain
- em0gAL8fbK (4.00) — Temporal logic backdoor against offline RL: most similar domain, but weaker evaluation, higher poisoning rate, less rigorous motivation. TrojanTO is clearly stronger.
- Gf4KZIqLHD (5.50) — DIFF2 backdoor on diffusion models: different domain, similar score range
- ZyPRwskBli (4.75) — Model editing backdoor: similar "first-in-domain" claim, comparable gaps. TrojanTO has better empirical work.
- MLShfiJ3CB (4.50) — Reliable backdoor on ViTs: different domain
- 9pW2J49flQ (8.00) — DeepLTL: clearly stronger, fundamentally different contribution level
- DzGe40glxs (8.00) — Interpreting planning in RL: clearly stronger
- 4KqkizXgXU (8.00) — Red-teaming LLMs: clearly stronger
- agPpmEgf8C (8.00) — Predictive objectives in RL: clearly stronger

**Round 2 (Narrowing):**
- T23HYw6lta (5.00) — Forget-Me-Not: making backdoors persist through fine-tuning. Similar novelty level and evaluation depth. TrojanTO is comparable, with broader evaluation and better motivation but the ε issue.
- LsTIW9VAF7 (5.80) — GCB clean-image backdoor: broader task coverage (5 datasets, 5 architectures, 4 tasks), strong empirical validation. TrojanTO is slightly below this — GCB has more comprehensive results presentation.
- HZnnHDrBXD (5.75) — Tree-based action-manipulation in continuous RL: has theoretical proofs offsetting its evaluation weaknesses. TrojanTO has broader empirical evaluation but no theory. Comparable overall.
- jCDF7G3LpF (6.25) — Jailbreak attacks on LLMs: different domain, clearly stronger novel contribution.
- jx6njBKH8E (5.75) — Training data exposure via fine-tuning: different domain.

**Bracket:** Round 1 placed TrojanTO between ~4.5 and ~6.5. Round 2 narrowed this: TrojanTO is clearly stronger than the 4.0-4.75 tier papers but below the 5.75-5.80 tier papers. Best comparison: T23HYw6lta (5.00), with TrojanTO having broader empirical evaluation but the ε issue. I place TrojanTO at **5.0** — between T23HYw6lta (5.00) and HZnnHDrBXD (5.75), closer to the former due to the uninterpretable ASR without ε, threat model ambiguity, and weak baselines offsetting the evaluation breadth.

Now let me write the final review.Now I have all the calibration data I need. Let me write the final review.

---

## Summary
This paper proposes TrojanTO, the first post-training action-level backdoor attack against Trajectory Optimization (TO) models in offline RL. The authors first conduct an empirical factor analysis showing that (1) target action selection dramatically affects attack success, (2) trigger design is crucial, and (3) reward manipulation is ineffective against TO models. Based on these findings, TrojanTO combines alternating training for trigger-model co-optimization, trajectory filtering to preserve benign performance, and batch poisoning (poisoning only one transition per batch) for trigger consistency. Evaluations across 3 model architectures (DT, GDT, DC) and 6 D4RL environments are reported.

## Strengths
- **Empirical factor analysis before method design (Section 4):** Tables 1-3 and Figure 1 provide a systematic investigation of target action types, trigger dimensions/values, and reward manipulation strategies. Figure 1 cleanly demonstrates that reward manipulation is ineffectual for TO models across all three architectures — a finding that directly validates the paper's core claim that TO models require a fundamentally different attack paradigm and is independently useful for the community.
- **Comprehensive evaluation coverage (Table 4):** Results span 3 model architectures × 6 environments × 3 seeds × 3 target action types, providing strong statistical and environmental coverage. The BTP value of 0.914 substantiates the claim that the attack preserves benign performance.
- **Clean ablation study (Table 5):** Each component is individually ablated. Removing Alternating Training drops ASR from 0.719 to 0.507; removing Batch Poisoning drops both ASR (to 0.528) and BTP (to 0.836); removing Trajectory Filtering drops BTP to 0.850. The ablation credibly validates the design.
- **Diverse target action evaluation:** Unlike prior work that tested only easy boundary target actions, this paper evaluates against '1', 'fixed random', and 'arithmetic' target actions. The finding that interior actions are substantially harder (e.g., '0' yields 0.11 ASR in Walk, Table 1) is a useful empirical insight.

## Weaknesses

### Fatal
None.

### Major
- **ASR threshold ε is never specified in the main text:** The attack success rate (Equation 2) is defined as the fraction of episodes where all action components fall within ε of the target action. The value of ε fundamentally determines whether ASR near 1.0 reflects precise adversarial control or is trivially achievable given the action range. The paper never states this value in the main body, making every ASR number in every table uninterpretable to a reader. A metric's core parameter must be stated where the metric is defined (Section 3.4). While ε may appear in an appendix (Appendix C or I), this is too fundamental to relegate.

- **Ambiguity in the threat model regarding data access:** Section 3.3 states the adversary implants the backdoor "without access to the original training dataset." However, Section 5.1 requires the adversary to have a dataset of trajectories to filter by length and use for backdoor training. The paper never clarifies where this dataset comes from — must the adversary collect trajectories from the target environment? Can they use a public dataset? This tension between the claimed capability and what the method actually requires undermines the "post-training" framing that is central to the paper's contribution narrative.

- **Weak baseline comparisons do not contextualize the contribution:** Only two baselines are evaluated: Baffle (a pre-training data-poisoning attack at 10% poisoning rate) and IMC (an input-model co-optimization technique from adversarial ML, not a backdoor attack). Baffle operates in a different threat model and at 33× higher poisoning rate — the comparison primarily demonstrates TrojanTO uses less poisoned data, which is a design choice rather than evidence of superior method design. IMC is not a backdoor method. Neither baseline isolates the contribution of TrojanTO's specific components within its own post-training threat model. A simple fine-tuning baseline (poisoned data + standard SGD) would directly measure the value of the proposed alternating training and batch poisoning designs.

### Minor
- **Defense evaluation is entirely relegated to the appendix:** Section 6.5 is a single paragraph stating that five defenses were tested, fine-tuning worked best, and all detailed results are in Appendix B.1. For a security paper whose stated goal is to "raise community awareness," the main text offers zero quantitative evidence on whether and how the attack can be mitigated.
- **CP metric can obscure individual metrics:** The harmonic mean heavily penalizes imbalanced ASR/BTP. In DT-Kit (Table 4), Baffle achieves CP=0.766 (ASR=0.946, BTP=0.662) while TrojanTO achieves CP=0.614 (ASR=0.969, BTP=0.455) — Baffle is arguably better here (substantially higher BTP at similar ASR) despite lower CP. The paper does not discuss such cases or whether CP always captures the desired trade-off.
- **Trajectory filtering by length is unjustified:** Section 5.1 assumes "longer trajectories are more representative of successful behavior" without evidence or citation. In D4RL datasets, trajectory length is not a reliable proxy for quality — filtering by return would be more principled.
- **Ablation of Alternating Training conflates two changes:** "TrojanTO w/o AT" removes alternating optimization and instead performs trigger learning for an equal number of iterations before model updates. This changes both the optimization schedule and the alternation pattern, making it unclear whether the ASR drop (0.719→0.507) comes from losing alternation or from the different update distribution.
- **Persistent backdoor analysis is preliminary (Section 6.3):** Results are reported only as CP (not ASR/BTP separately), only for target type '1', and only on three locomotion environments.
- **Per-target-action breakdown missing from main results table:** Table 4 averages across three target actions, yet Section 4.1 demonstrates that target action type dramatically affects ASR. The main results table obscures the very effect the paper itself highlights.

### Trivial
- The scaling argument in the introduction (TO models "continue to scale in size and training cost," line 17) is aspirational relative to the models actually used in experiments (DT, GDT, DC at a few million parameters).
- Trigger dimension selection (Section 4.2) is validated on only two environments (Half and Walk); testing on additional environments would strengthen generalizability claims.

## Nice-to-Haves
- A discussion of whether the triggered behavior can be detected by simple anomaly detection on action distributions during deployment would strengthen the stealthiness analysis.
- Comparing trajectory filtering by length against filtering by return would strengthen the methodological justification.
- A simple post-training fine-tuning baseline (standard SGD with poisoned data, no alternating training or batch poisoning) would isolate the value of TrojanTO's design choices.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Removed:** "The paper does not discuss backdoor attacks against sequence models or transformers in other domains (NLP, vision)" — This is scope creep; the paper's contribution is specific to RL/TO models and existing RL backdoor literature is adequately covered in Section 2.
- **Removed:** "The context-window bound on persistence is obvious from the architecture and not a finding" — The paper itself explicitly states this limitation (lines 307-308), so this criticism merely restates what the paper already acknowledges.
- **Removed:** "The paper should discuss whether the triggered behavior can be detected by monitoring action distributions" — This is speculative and asks the paper to address a problem outside its stated scope. Moved to Nice-to-Haves instead.
- **Removed:** "Trigger dimension selection should be validated on environments beyond Half and Walk" — Demoted to Trivial; the paper already notes this as preliminary with additional attempts in Appendix F.
- **Removed (from Strength Finder):** Generic strengths about "addressing an important problem" or being "well-motivated" without concrete grounding were filtered. All kept strengths are tied to specific evidence in the paper.

## Novel Insights
The empirical finding in Section 4.3 — that reward manipulation is completely ineffective for backdooring TO models — is genuinely novel and important. It cleanly separates the TO model backdoor problem from the traditional RL backdoor paradigm and provides actionable guidance: trigger-target coupling through consistent poisoning, not reward signals, is the attack vector that matters for TO models.

## Suggestions
- State ε explicitly in Section 3.4 alongside the metric definitions. This is a one-line fix that makes the paper's central results interpretable.
- Clarify in Section 3.3 whether the adversary's trajectory dataset must come from the target environment, a public dataset, or can be otherwise obtained. This resolves the tension with the "without access to original training dataset" claim.
- Add a simple post-training fine-tuning baseline (poisoned data + standard SGD) to Table 4 to isolate the value of TrojanTO's specific design within its own threat model.
- Move summary defense results (ASR/BTP before and after fine-tuning defense, with data requirements) into Section 6.5 rather than relegating everything to the appendix.

## Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| em0gAL8fbK | 4.00 | R1 | Temporal logic backdoor against offline RL — similar domain but weaker evaluation, higher poisoning rate, poorer motivation |
| ZyPRwskBli | 4.75 | R1 | Model editing backdoor — similar "first-in-domain" claim, comparable gaps; TrojanTO has better empirical breadth |
| T23HYw6lta | 5.00 | R2 | Forget-Me-Not — similar novelty level; TrojanTO has broader evaluation but the ε issue |
| HZnnHDrBXD | 5.75 | R2 | Action-manipulation in continuous RL — has theoretical proofs offsetting evaluation weaknesses; TrojanTO has broader empirical work but no theory |
| LsTIW9VAF7 | 5.80 | R2 | GCB clean-image backdoor — broader task coverage, stronger results presentation; TrojanTO slightly below |
| jCDF7G3LpF | 6.25 | R2 | Jailbreak attacks on LLMs — clearly stronger; different domain |
| 9pW2J49flQ | 8.00 | R1 | DeepLTL — clearly stronger; fundamentally different contribution level |

**Bracket:** Round 1 placed TrojanTO between ~4.5–6.5. Round 2 narrowed this: TrojanTO is clearly stronger than the 4.0–4.75 tier but below the 5.75–6.25 tier, closest to T23HYw6lta (5.00). The ε issue, threat model ambiguity, and weak baselines offset the evaluation breadth.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>