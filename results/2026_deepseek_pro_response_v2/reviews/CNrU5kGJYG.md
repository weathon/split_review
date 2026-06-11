Round 2 comparison complete. Let me finalize the calibration.

**Round 1 Bracket:** 4.75 – 6.25

**Round 2 narrowing:** The paper lands around 5.5. Here's the detailed comparison:

| Anchor | Score | Comparison |
|--------|-------|------------|
| em0gAL8fbK (offline RL backdoor, AD) | 4.00 | Our paper is clearly stronger: lower poisoning rate (0.3% vs 15%), broader evaluation (6 envs × 3 architectures vs narrower), systematic factor analysis |
| ZyPRwskBli (model-editing backdoor) | 4.75 | Our paper is stronger: more comprehensive experiments, systematic factor analysis grounding the method |
| HZnnHDrBXD (action-manipulation, continuous RL) | 5.75 | Comparable: both attack continuous RL actions, both have empirical strengths and evaluation gaps. Our paper has broader empirical scope; theirs has theoretical guarantees |
| vRyp2dhEQp (data-constrained backdoor) | 5.75 | Comparable: both address realistic threat models, both have strong empirical results. Our defense evaluation is more cursory |
| S1Bv3068Xt (BALD, embodied LLM backdoor) | 6.25 | Our paper is weaker: BALD has more extensive experiments, multiple attack mechanisms, and was accepted |

**Final score: 5.5** — a borderline paper. The systematic factor analysis (Section 4) and strong empirical results at ultra-low poisoning rates are genuine contributions, but the threat model under-specification, misaligned baselines, and extremely brief defense evaluation prevent a higher score.

---

## Summary
This paper proposes TrojanTO, the first action-level backdoor attack against Trajectory Optimization (TO) models in offline RL. The attack operates in a post-training setting, using alternating training to couple a learned trigger with a target action, trajectory filtering to preserve benign performance, and batch poisoning to ensure trigger consistency. The paper provides a systematic factor analysis showing that target action type and trigger design critically affect backdoor efficacy while reward manipulation is irrelevant for TO models. Experiments across 6 environments and 3 TO architectures (DT, GDT, DC) show TrojanTO achieves an average CP of 0.701 with only 0.3% poisoned trajectories.

## Strengths
- **Systematic factor analysis grounding the method design (Section 4):** Tables 1–3 and Figure 1 provide well-structured empirical evidence that (a) target action type dramatically affects ASR (boundary actions achieve near-perfect ASR while interior actions are much harder), (b) trigger dimensions and values are critical design choices, and (c) reward manipulation has negligible impact on TO model backdoors. These findings directly motivate the method design and are a genuine contribution to understanding TO model security.
- **Strong attack performance at very low budget (Table 4):** TrojanTO achieves average CP of 0.701 (ASR=0.719, BTP=0.914) across 6 D4RL environments × 3 TO architectures × 3 target action types × 3 seeds, using only 0.3% poisoned trajectories. This represents a 105% improvement over Baffle (CP=0.342 at 10% poisoning) and 27% over IMC (CP=0.551). The BTP of 0.914 indicates near-identical benign performance to the clean model.
- **Informative component ablation (Table 5):** The ablation cleanly separates component contributions — alternating training drives ASR (removing it drops ASR from 0.719 to 0.507), while trajectory filtering and batch poisoning jointly preserve BTP (removing TF drops BTP from 0.914 to 0.850, removing BP drops BTP to 0.836).
- **Cross-architecture generality:** The attack is evaluated on three architecturally distinct TO models (causal transformer DT, graph-based GDT, convolution-based DC) and achieves non-trivial ASR on all, with particularly strong results on DC (average CP=0.814).
- **Persistent backdoor extension (Section 6.3):** Table 6 shows the attack supports multi-step persistent target actions (up to k=15 steps) with only minor CP degradation, demonstrating practical versatility beyond single-step manipulation.

## Weaknesses

### Fatal
None.

### Major
- **Threat model framing is unclear about data requirements.** Section 3.3 states the adversary operates "without access to the original training dataset," but the method requires trajectory data for filtering (Section 5.1), batch poisoning (Section 5.2), and clean loss computation (Eq. 6). The Adversary's Capability paragraph acknowledges access to a "minimal set of poisoned trajectories (e.g., 0.3%)," but does not explain where this data comes from, how much total data is needed, or why a supply-chain attacker would plausibly possess it. The distinction between "original training dataset" and a small post-training dataset is reasonable, but the threat model is under-specified for a security paper.
- **Baseline comparisons are misaligned with the paper's claims.** Baffle (Gong et al., 2024b) is a policy-level backdoor designed to degrade long-term returns, not to force specific actions; evaluating it with an action-level metric (componentwise match) is informative but a mismatch. More importantly, a minimal post-training baseline — directly fine-tuning the pretrained model on the same 0.3% poisoned trajectories without alternating training, batch poisoning, or trajectory filtering — is absent. This baseline would directly test whether the three proposed components add value beyond simple fine-tuning.
- **Defense evaluation is too cursory for a security contribution.** Section 6.5 is five sentences long, reporting that fine-tuning is the most effective defense while other methods "proved largely ineffective," with all quantitative results deferred to the appendix. The main text provides no information about how effective fine-tuning is (does it reduce ASR to 0%? to 50%?), how much data it requires, or whether the fine-tuned model remains genuinely benign. A method whose backdoor can be removed by standard fine-tuning may be less practically threatening than the framing suggests.

### Minor
- **The ASR threshold ε in Equation (2) is not specified in the main text.** ASR values in continuous action spaces are sensitive to this threshold — a loose ε inflates ASR, a tight one deflates it — making the headline numbers uninterpretable without this parameter being stated and justified.
- **The claim of "consistent robustness and stability" (line 272) is overstated.** Several entries in Table 4 show weak performance: DT-Ant ASR is 0.296 (below 30%), DT-Kit BTP drops to 0.455, and DC-Ant CP (0.559) underperforms IMC (0.752). The method does not perform uniformly well.
- **The trigger dimension study (Table 2) fixes dimensions to (1,2,3) for all subsequent experiments based on only two environments (Half and Walk).** This is a thin basis for a design choice that propagates through all later results.
- **The trajectory filtering justification (Section 5.1) is asserted rather than argued.** The claim that "longer trajectories are more representative of successful behavior" is stated without evidence. In some D4RL datasets (e.g., AntMaze), long trajectories can be suboptimal wandering.
- **The persistent backdoor results (Table 6) report only CP, not ASR and BTP separately,** preventing the reader from understanding whether CP degradation comes from ASR loss, BTP loss, or both.

### Trivial
- The bi-level formulation in Equation (7) does not fully capture the actual implementation (multi-step updates, shift to model-only updates after half the training budget).
- The abstract's claim about "large network size" is asserted but not substantiated — the DT, GDT, and DC models used are standard research-scale architectures.

## Nice-to-Haves
- Expanding the defense evaluation with quantitative results for fine-tuning: how much data is needed, what ASR/BTP trade-offs result, and whether the defense is robust to an attacker who anticipates it.
- Adding a simple fine-tuning baseline (no alternating training, no batch poisoning, no trajectory filtering) to anchor the ablation study and isolate the value of the three proposed components.
- Clarifying the threat model: explicitly state what data the adversary has access to, how much, and why this is realistic in a supply-chain setting.

## Removed Points
These points are flagged to be removed, treat them with caution.

- The harsh critic's claim that the threat model is "structurally incoherent" and "fatal": The paper does distinguish between "original training dataset" (not accessible) and a small set of trajectories for post-training (accessible per Adversary's Capability). The tension is real but overcharacterized as structural/fatal. Demoted to Major.
- Criticism of Baffle as "policy-level" framed as making the comparison entirely unfair: The paper includes Baffle as a relevant prior work in offline RL backdoor attacks, and showing it fails at action-level objectives is informative. However, the absence of a more appropriate baseline (simple fine-tuning) is the real issue. Kept the baseline gap criticism but removed the claim of outright unfairness.
- Demands for confidence intervals, user studies, theoretical proofs: These are outside the scope of an empirical offline RL security paper. Removed.
- Any formatting, typo, or parser-artifact criticisms: These are not author errors. Removed.
- Criticism about missing appendix content: The parser strips appendices; the original submission includes them. Removed any weakness that depends on appendix content being absent.
- The harsh critic's claim that the defense evaluation is "uninformative" rather than "cursory" — the appendix likely contains the quantitative results; the issue is that they are not in the main text, not that they don't exist.

## Novel Insights
None beyond the paper's own contributions. The reviews primarily confirm the paper's strengths (systematic factor analysis, strong empirical results) and identify standard gaps in threat model specification and baseline comparison that are common in early work on a new attack surface.

## Suggestions
- Specify ε in the main text with justification relative to the action space scale (e.g., as a fraction of the action range [-1,1]).
- Add a simple fine-tuning baseline: pretrained model fine-tuned on 0.3% poisoned trajectories with only the backdoor loss, no alternating training, batch poisoning, or trajectory filtering. This would cleanly isolate component contributions.
- Expand Section 6.5 with quantitative defense results for fine-tuning at minimum: ASR after defense, BTP after defense, and data requirements.
- Clarify the threat model by explicitly stating what data the adversary possesses, how much, and justifying its availability in a supply-chain scenario.
- Report ASR and BTP separately (not just CP) in Table 6 for the persistent backdoor results.
- Tone down the "consistent robustness and stability" claim given the performance variation across environments in Table 4.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>