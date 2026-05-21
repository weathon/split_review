Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes TrojanTO, a post-training action-level backdoor attack against trajectory optimization (TO) models in offline RL. The method uses an alternating optimization procedure to jointly learn a trigger and minimally modify model parameters, with trajectory filtering and batch poisoning to preserve benign performance. Extensive experiments across 6 D4RL tasks and 3 TO model architectures (DT, GDT, DC) show high attack success (average ASR 0.719, CP 0.701) at a very low poisoning rate (0.3%).

## Strengths

- **First systematic study of action-level backdoors for TO models.** Section 1 and Section 4 establish that existing training-time, reward-manipulation-based attacks from traditional RL are ineffective against TO models, and that trigger design — not reward manipulation — is the key attack vector. This fills a genuine gap in the literature.

- **High attack effectiveness with extremely low poisoning rate (0.3%).** Table 4 shows TrojanTO achieves an average CP of 0.701 across 6 tasks and 3 models, with ASR of 0.719, using only 0.3% poisoned trajectories. This compares favorably to Baffle (CP 0.342, poisoning rate 10%) — a 105% relative improvement.

- **Ablation confirms all three components (TF, BP, AT) are necessary.** Table 5 shows that removing any component degrades performance: ASR drops from 0.719 to 0.528 (w/o BP) and 0.507 (w/o AT); BTP drops from 0.914 to 0.850 (w/o TF) and 0.836 (w/o BP). This cleanly validates the design.

- **Informative empirical investigation of key factors.** Tables 1–3 systematically study target action type, trigger dimensions, and trigger values, providing practical guidance for attack design (boundary actions work best; trigger dimensions matter; learnable triggers via MI-FGSM outperform handcrafted ones).

- **Robustness and defense analysis.** Section 6.4 shows graceful ASR degradation under trigger perturbations (e.g., Walk: 0.980 → 0.777 at 10% noise), and Section 6.5 reports that fine-tuning is effective while other defenses fail — providing a realistic assessment.

## Weaknesses

### Fatal
None.

### Major

None. The critical issues raised by the harsh critic are not fatal upon verification against the paper.

### Minor

- **The threat model needs clarification on trajectory sourcing.** Section 3.3 states the adversary operates "without access to the original training dataset" (line 72), yet Section 5.1 begins with "an initial set of $N$ trajectories" (line 186) without explaining their provenance. The paper never specifies whether these are drawn from a public benchmark (e.g., D4RL), collected via environment interaction, or generated from the pretrained model itself. This ambiguity weakens the threat model's realism claims. The claim itself is not contradictory (the adversary could use a public dataset without the *original* training data), but the paper should explicitly discuss where these trajectories come from and what assumptions this places on the adversary.

- **The baseline comparison is weakened by the absence of a simple fine-tuning baseline.** Table 4 compares TrojanTO against Baffle (a pre-training policy-level attack using 10% poisoning) and IMC (designed for image-domain backdoor co-optimization). A natural baseline is missing: fine-tune the pretrained model on the same poisoned trajectories but with a *fixed* trigger (no MI-FGSM optimization), without trajectory filtering, and without batch poisoning. The ablation study (Table 5) includes "TrojanTO w/o AT" but that still uses learned triggers and other components — it does not isolate the benefit of the overall proposed machinery relative to a trivial fine-tuning approach. Adding such a baseline would make the case for TrojanTO's specific design stronger.

- **The ASR threshold $\varepsilon$ (Equation 2) is not reported in the main text.** The definition of ASR depends on this threshold, making all ASR numbers unverifiable without it. The value is likely in the stripped appendix, but it should be stated and justified in the main paper with reference to the action scale.

- **The balance parameter $\lambda$ is never specified in the main text.** It appears in Equation (1) (as the trade-off between attack and benign objectives) and again in the bi-level optimization (Equation 7), but its value is not given. Since this parameter directly controls the attack-stealth trade-off, its value is needed to interpret results.

- **Low ASR on certain tasks is not sufficiently discussed.** TrojanTO achieves only 0.296 ASR (DT, Ant) and 0.428 ASR (DC, Pen). The paper's general claims about effectiveness would benefit from acknowledging these limitations and discussing why the attack struggles in these settings (e.g., high-dimensional action spaces? distributional properties of the dataset?).

- **The assumptions behind trajectory filtering are unvalidated.** Section 5.1 assumes "longer trajectories are more representative of successful behavior." This is plausible but not empirically validated in the paper. It is unclear how sensitive the method is to the quality of the adversary's trajectory source.

### Trivial

- The value of $\varepsilon$ in the trajectory filtering threshold (Section 5.1) and the noise level $\epsilon$ in the trigger perturbation experiments (Section 6.4) use the same symbol for different purposes, which is mildly confusing.

- Defense results (Section 6.5) are entirely deferred to the appendix with only a one-paragraph summary. A brief table or summary of which defenses work and why would strengthen the paper.

## Nice-to-Haves

- Vary the trigger dimension selection across tasks to check whether (1,2,3) is universally optimal (Table 2 only tests this on two locomotion tasks).
- Clarify the "0.3% poisoning rate" denominator (full dataset size vs. filtered set size).
- Add a brief discussion of the computational cost of alternating training relative to a simple fine-tuning baseline.
- Note on variance: some results report $1.000 \pm 0.000$, which may reflect metric saturation rather than genuine zero variance.

## Removed Points

- **"Threat model inconsistency is a structural flaw"**: This is removed. The paper says "without access to the *original training dataset*" — not "without any data." Using a publicly available dataset (e.g., D4RL) or collecting new trajectories from the same environment is a plausible attack scenario that does not require the original training data. The ambiguity is genuine (moved to Minor), but calling it a "fatal contradiction" that "invalidates the stated threat model" is an overstatement not supported by the paper as written.
- **"105% improvement over Baffle is meaningless"**: Removed. Baffle is explicitly the most related prior work in offline RL backdoors (as stated in Section 2, line 46). Comparing against it is standard practice; the paper acknowledges the paradigm differences.
- **"IMC is not designed for RL at all"**: Removed. TrojanTO's alternating training explicitly "draws inspiration from Input Model Co-optimization (IMC)" (line 219), making IMC a valid methodological baseline even if its original domain differs.
- **"Baffle uses 10% poisoning vs. 0.3%" is framed as unfair**: Removed and treated as supporting evidence for TrojanTO's efficiency. The asymmetry favors the baseline (Baffle gets *more* data), which makes TrojanTO's superior results *more* convincing, not less.
- **Formatting/style nitpicks** and **missing appendix content**: Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective the paper itself does not already address.

## Suggestions

1. Explicitly state the assumed source of the $N$ initial trajectories (e.g., "the adversary collects $N$ trajectories from the same environment using a random policy or a public dataset") and discuss any limitations this imposes.
2. Add a simple fine-tuning baseline (fixed trigger, no AT/TF/BP) to Table 4 to isolate the value of TrojanTO's components.
3. Report $\varepsilon$ and $\lambda$ values in the main text with justification.

## Score and Decision

**Round-1 bracket (initial):** Based on comparison with calibration anchors, I placed the paper between 4.0 and 7.5. The weak-band anchors (avg 3.0) correspond to papers with far less experimental scope or with fatal flaws. The strong-band anchors (avg 8.0+) have substantially deeper theoretical contributions (e.g., certified defenses, information-theoretic analyses) that this paper lacks. The middle band is the right neighborhood.

**Round-2 narrowing:** I retrieved anchors in the (4.5, 6.0) and (6.0, 7.5) ranges. The most directly comparable paper is **oxjeePpgSP.md** (avg 5.75, Accept poster) — a bi-level trigger optimization attack on contrastive learning. TrojanTO has similarly comprehensive experiments, a similar methodological approach (alternating/bi-level optimization), and similar missing-detail issues (K, J hyperparameters not specified). TrojanTO's experiments are more extensive (3 architectures × 6 tasks vs. standard image benchmarks) and its problem domain is novel. I also compared against **NALkteEo9Q.md** (avg 5.00, Reject) — a backdoor poisoning attack in DRL with data integrity concerns and threat model clarity issues; TrojanTO is clearly stronger. Against **X2x2DuGIbx.md** (avg 6.75, Accept Poster) — a certified defense in offline RL with strong theory but experimental clarity issues; TrojanTO is somewhat weaker on theoretical depth. The paper sits between the 5.75 anchor and the 6.75 anchor, leaning toward the former due to missing details and the absence of a simple baseline, but above it due to the novelty and breadth of the empirical study.

**Final score: 6.0** — marginally above the acceptance threshold. The paper makes a genuine contribution to an underexplored problem, the experiments are extensive, and the methodology is well-motivated. The weaknesses (threat model clarity, missing baseline, unreported key parameters) are addressable and do not undermine the core claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>