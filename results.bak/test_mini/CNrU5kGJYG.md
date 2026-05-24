Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes TrojanTO, the first post-training action-level backdoor attack against trajectory optimization (TO) models in offline RL (Decision Transformer, GDT, DC). The method uses trajectory filtering, batch poisoning, and alternating training (trigger+model co-optimization) to inject backdoors with very low poisoning rates (~0.3% of trajectories). The paper provides a systematic empirical analysis of key factors (target action, trigger design, reward manipulation) and evaluates across 6 D4RL tasks and 3 model architectures.

## Strengths

1. **First action-level backdoor attack framework for TO models in a post-training paradigm.** The paper identifies a genuine gap: existing RL backdoor attacks target training-time reward manipulation, which is ineffective against TO models that use reconstruction loss and are expensive to retrain. TrojanTO's post-training threat model is well-framed (Section 3.3) and practically relevant as model scale grows. The evaluation covers 6 D4RL environments across DT, GDT, and DC architectures (Table 4).

2. **Systematic empirical investigation of factors (target action, trigger design, reward manipulation) affecting backdoor efficacy in TO models.** Section 4 presents controlled experiments showing that target action type significantly impacts ASR (Table 1: boundary actions yield ~1.0 ASR vs interior actions dropping to 0.11), trigger dimensions cause ASR to vary from 0.0 to 0.915 (Table 2), and reward manipulation has negligible effect (Figure 1). This analysis goes beyond prior RL backdoor work and directly motivates the method design.

3. **Ablation study validates each component's contribution.** Table 5 quantifies the impact of each module: removing alternating training drops ASR from 0.719 to 0.507, removing batch poisoning drops ASR to 0.528, and removing trajectory filtering reduces BTP from 0.914 to 0.850. This provides clear evidence that all three components contribute meaningfully.

4. **Demonstration of persistent backdoor attacks and robustness to trigger perturbations.** Table 6 shows the backdoor persists for k consecutive steps with only minor CP degradation. Table 7 shows ASR remains above 0.77 even with 10% trigger noise, indicating practical robustness.

## Weaknesses

### Major

- **Unequal poisoning rates confound the headline comparative claim.** The paper claims "approximately 105.0% improvement compared to Baffle" (Section 6.1), but TrojanTO is evaluated at a 0.3% poisoning rate while Baffle is evaluated at 10% — a >30× difference. Because poisoning rate and attack method are confounded, the reader cannot attribute TrojanTO's apparent superiority to the method rather than the budget difference. The paper does not provide controlled experiments (e.g., Baffle at 0.3% or TrojanTO at 10%) to support this comparison. This weakness is real, though partially mitigated by the fact that TrojanTO (post-training) and Baffle (pre-training data poisoning) are fundamentally different attack paradigms, so the poisoning rate definitions are not directly equivalent. Nonetheless, the 105% improvement claim as stated is not adequately supported.

### Minor

- **Missing variance in the main comparison table (Table 4).** The results are reported as single-point averages over three seeds without standard deviations or confidence intervals. Given that RL training is noisy (the paper itself cites Henderson et al. 2018), the absence of variance makes it impossible to assess the statistical reliability of reported differences (e.g., DT-Hopp: TrojanTO ASR=0.362 vs Baffle ASR=0.365 — are these meaningfully different?). Note that the paper *does* report ± values in Tables 6 and 7, so the capability exists; its omission from Table 4 is regrettable.

- **IMC baseline adaptation not described.** The paper introduces IMC (Pang et al., 2020) as a baseline but does not explain how this method — originally designed for image classifiers — was adapted to trajectory optimization models. Given that TrojanTO's alternating training component itself draws inspiration from IMC, the paper needs to explicitly state what constitutes the IMC baseline in this context (e.g., is it TrojanTO without TF and BP? A separate implementation?). Without this, the comparison in Table 4 is hard to interpret.

- **The ASR threshold ε is not specified in the main text.** The ASR definition (Equation 2) uses a threshold ε to determine success, but its numerical value is absent from the available text. This is a missing implementation detail that affects interpretability.

### Trivial

- **Trigger dimension choice (1,2,3) is justified only for HalfCheetah and Walker2d** (Table 2). The paper adopts these dimensions for all subsequent experiments without checking whether they are optimal for other environments (Ant, Kitchen, Pen). This is acknowledged as an environment-dependent choice (Section 4.2: "the trigger dimension critically influences the efficacy"), but no sensitivity analysis is provided for the other four environments.

## Nice-to-Haves

- **False positive / pseudo-trigger analysis.** Section 6.4 acknowledges that noise robustness could lead to pseudo-triggers but does not evaluate this empirically. A simple experiment measuring ASR on benign data (without trigger) would help assess the risk of accidental activation.
- **Stronger defense presentation.** The defense analysis is relegated entirely to the appendix; the main text reports only one sentence. Including a summary table of defense results in the main body would strengthen the paper.
- **Testing Baffle at 0.3% or 1% poisoning** (or similarly, testing TrojanTO at 10%) would either substantiate or temper the comparative claim. This is the single most impactful experiment the authors could add.

## Removed Points

- *"The IMC baseline is potentially circular (TrojanTO without TF and BP)"* — This is speculative; the paper does not describe IMC's implementation, so the reviewer is guessing. The underlying concern (undefined baseline) is kept above as minor.
- *"Defense section too thin"* — The defense details appear in the appendix (Appendix B.1), which was stripped by the parser. The main text summarizes the key finding. This is not a weakness in the original submission.
- *"No analysis of per-environment poisoned trajectory counts"* — This would improve reproducibility but is a granular detail. The 0.3% average across datasets is stated; the appendix (stripped) likely contains per-environment breakdowns.
- *"Reward manipulation analysis only shown for Walk"* — The paper notes "More results are provided in Appendix K.1" for the other environments.
- *"HalfCheetah ASR remaining 1.0 at 10% noise deserves more investigation"* — This is an interesting observation but not a weakness; the paper already notes the smooth degradation pattern.

## Novel Insights

The harsh critic's most useful observation — beyond the paper's own contributions — is that the comparison with Baffle is structurally unfair not just due to unequal poisoning rates but because the two attack paradigms have fundamentally different cost structures (pre-training data poisoning vs. post-training model modification). This framing issue pervades how the paper positions itself. The strength finder's value-add is in quantifying the ablation's credibility and the breadth of the evaluation, but neither reviewer produces an insight genuinely beyond what the paper already states. The most actionable synthesis: the paper's core contribution (a novel post-training attack vector for TO models) is sound, but several presentation choices — particularly the 105% improvement headline — are weakened by the confound and should be recalibrated.

## Suggestions

1. Run Baffle at 0.3% and 1% poisoning rates (or TrojanTO at 10%) to enable controlled comparison, or explicitly reframe the comparison to acknowledge the different attack paradigms and temper the superiority claim.
2. Add standard deviations to Table 4 for ASR, BTP, and CP across the three seeds.
3. Explicitly describe how the IMC baseline was adapted to the TO setting (or replace it with a baseline that is clearly distinct).
4. Report the ε threshold used in the ASR metric.
5. Consider a brief false-positive rate analysis (ASR on clean data) to address the pseudo-trigger concern from Section 6.4.

## Score and Decision

**Calibration Summary:**

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| *Stealthy Backdoor in RL via Bi-level Optimization* | 3.00 | 1 (weak) | TrojanTO is substantially stronger — better motivation, more comprehensive evaluation, clearer contribution |
| *Angel or Demon: Plasticity-Enhanced Strategies in DRL* | 4.00 | 1 (middle) | TrojanTO has a more concrete contribution (new attack method vs. empirical study) and cleaner results |
| *Backdoors in RLVR* | 3.60 | 1 (middle) | TrojanTO is more complete and better evaluated |
| *POLAR: Layerwise RL for Backdoor Attacks in FL* | 4.00 | 1 (middle) | TrojanTO addresses a more novel problem space for TO models |
| *Robust DRL against Adversarial Behavior Manipulation* | 5.50 | 2 (narrow) | Similar quality; TrojanTO has slightly stronger novelty but weaker controlled comparisons |
| *Beware Untrusted Simulators — Reward-Free Backdoor Attacks in RL* | 6.50 | 1 (strong) | Stronger paper — has theoretical proofs, real-robot validation, and more rigorous evaluation; TrojanTO is weaker |
| *Minimax Optimal Adversarial RL* | 6.50 | 2 (narrow) | Not directly comparable (theory paper); TrojanTO is a security application paper |

**Round 1 bracket:** The paper sits between the weak anchors (~3.0) and the strong anchor (6.50). It is clearly better than the 3.0–4.0 papers (which were rejected) but weaker than the 6.50 accepted paper.

**Round 2 narrowing:** Compared to the 5.50 anchor (accepted), TrojanTO is similar in quality: both have a genuine contribution and reasonably thorough evaluation, but TrojanTO's comparative claim weakness is more prominent than that anchor's weaknesses. Compared to the 6.50 anchor, TrojanTO lacks theoretical guarantees and has the confounded comparison issue. The paper is closest to the 5.0–5.5 range.

**Final score:** Considering the genuine novelty of the post-training attack paradigm for TO models and the reasonably thorough evaluation, weighed against the unsupported comparative claim and missing variance in the main results table.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>