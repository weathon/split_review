Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper identifies a key limitation of existing FL backdoor defenses: the metrics used to filter malicious models (distance, median, norm) are themselves computed using malicious models and thus become "tainted" when attackers are numerous. To address this, the authors propose Nira, which uses a pure-noise surrogate dataset shared across server and clients. Clients train on both local data and noise, with a feature distribution alignment loss to preserve generalization. The server then filters client models based on their accuracy and feature consistency on the noise data — metrics that are not influenced by malicious models. Experiments on CIFAR-10, FMNIST, and SVHN show improved defense over Krum, Median, Norm clipping, and RFA baselines.

## Strengths

- **Novel and well-motivated core idea**: The paper correctly identifies that metrics computed from client models are themselves corrupted when attackers are numerous, and proposes using pure noise as an untainted surrogate to break this circular dependency (Sections 1, 3.1). This is a genuinely different approach from prior distance- or statistic-based defenses and represents the paper's primary intellectual contribution.

- **Empirical evidence of strong defense in high-attacker regimes**: Figure 1b/c shows that Nira keeps attack success rate below 1% when attackers are less than 70% of clients (in the all-clients-selected setting), whereas all baseline methods fail once attackers exceed 50%. Table 1 reports that Nira outperforms baselines across three datasets under varying attacker counts (4–12 out of 50 clients), with the best improvement reaching 7.82% lower attack rate than the second-best method at 12 attackers.

- **Compatibility and practical design**: Nira modifies only the client objective (adding noise data + alignment loss) and adds two server-side filtering steps, making it compatible with existing FL algorithms such as FedAvg, FedProx, and FedNova (Section 3.4). The noise data contains no private information, avoiding the privacy leakage that would accompany using real surrogate data.

## Weaknesses

### Fatal

None.

### Major

1. **Insufficient evidence that the noise-based filtering metrics are non-circumventable by adaptive attackers.** The paper's defense rests on the assumption that attackers cannot simultaneously maintain backdoor functionality and achieve benign-level accuracy and feature consistency on noise data. The tested adaptive attack (Nira Adapt) only excludes poisoned samples from the alignment loss — it does not directly optimize the two quantities the server checks (noise accuracy and feature-distance matrix). An attacker with full control over training (as assumed, Section 2.2) could adopt a joint objective: (a) succeed on the backdoor task, (b) maximize noise accuracy above σ₁, and (c) calibrate feature distances on noise to fall within the benign range. The paper provides no argument or experiment showing such an attack is impossible or ineffective. Since the filtering mechanism is the entire basis of the defense, this gap is the single most serious weakness. The paper needs either a principled argument or an explicit evaluation of this direct adaptive attack.

2. **Threshold selection is under-addressed and relies on a somewhat circular assumption.** The paper states that "the server can identify a small number of benign clients and simulate the training process" to set thresholds σ₁ and σ₂ (Section 3.3). This is problematic: if the server can reliably identify benign clients, the core problem of distinguishing benign from malicious models is already partially solved. In realistic FL deployments, the server typically has no verified benign clients — this is precisely why defenses are needed. The paper also does not report how σ₁ and σ₂ were set in the reported experiments, nor does it provide a sensitivity analysis showing how performance changes with threshold values. An interval-based filtering strategy is mentioned in a footnote reference (presumably in the appendix) but the main paper lacks the detail needed to assess its practicality.

3. **Theorem 3.1 is too vague to constitute meaningful theoretical support.** The theorem states that training with the feature alignment objective "elicits the bounded statistical robustness" for "separable distributions" — without specifying what the bound depends on, how large it is, what "separable" means formally, or how the bound relates to the gap between noise and real distributions. Definition 3.1 (statistical robustness as expected distance to the nearest adversarial example) is a reasonable concept, but the theorem provides no falsifiable or usable statement. As the reviewer notes, the paper would be better served dropping the theorem and relying on the empirical evidence, since in its current form it adds a veneer of rigor without substance. (That said, this does not undermine the empirical contribution, and is treated as a major weakness of the *presentation* rather than of the core method.)

4. **Evaluation metric is unconventional and lacks critical methodological details.** The paper reports results as averages over "the 5 rounds before the model converges" (Section 4.2). This is a non-standard choice not seen in comparable FL defense papers, and it is not justified. Without reporting final-round metrics, per-round curves, or confidence intervals/standard deviations, the reader cannot assess whether the reported numbers are representative or cherry-picked from a favorable phase of training. The paper also does not report standard deviations for any main result in Table 1, making it impossible to determine whether observed margins over baselines are statistically meaningful.

### Minor

1. **Over-generalization of the "tainted metrics" criticism.** The paper claims that methods like norm clipping produce "tainted metrics" (Section 1) because malicious models are "involved in the calculation." However, norm clipping applies a per-model threshold based on each model's own norm — malicious models do not directly affect the metric for benign models. The criticism is accurate for Krum, median, and other consensus-based methods, but the paper's framing over-generalizes it to all existing defenses.

2. **Mechanism for performance gains without attackers is speculative.** The paper reports that Nira improves accuracy even without attackers (Section 4.2) and offers three plausible explanations (reduced data heterogeneity, feature alignment, class balancing). However, there is no ablation or analysis to isolate which factor drives the improvement. Since this is an ancillary claim (the main claim is about defense), this is a minor omission.

3. **Limited attacker ratio range in the main evaluation.** The main Table 1 experiments use up to 12 attackers out of 50 clients (24% of total, and at most 60% of the 20 selected per round in the worst case). The stronger claim about "attackers < 70%" comes from a separate experimental setup (10 clients, all selected) shown in Figure 1b/c, but this setup is not included in the main comparison table. The gap between the two evaluations weakens the headline claim.

### Trivial

- Slight inconsistency in evaluation metric phrasing: Figure 1 caption says "5 rounds before the best training accuracy" while Section 4.2 says "5 rounds before the model converges." These may refer to the same thing but the terminology mismatch is confusing.

## Nice-to-Haves

- Adding confidence intervals or standard deviations to the main results (Table 1).
- A sensitivity analysis for the threshold values σ₁ and σ₂, and for the alignment weight λ.
- A description of how σ₁ and σ₂ were chosen for the reported experiments.
- Results at higher attacker ratios (40–60%) in the main evaluation to directly support the claimed 70% threshold.
- An evaluation of the adaptive attacker that explicitly optimizes noise accuracy and feature-distance consistency, rather than only excluding poisoned samples from alignment.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper tests at most 12 attackers...a relatively mild adversarial regime"** — While true for Table 1, the paper also evaluates up to 70% attackers in Figure 1b/c (different setup). The point is downgraded to a minor weakness (limited range in the main evaluation) rather than treated as a fatal omission.
- **Critique about attackers "rejecting to follow the proposed protocol"** — The paper explicitly addresses this (line 156: "malicious attackers may reject to follow the proposed protocol") and notes that such models would then perform poorly on noise data and be detected. This is not an oversight.
- **Weakness about the paper not reporting IID setting results** — The paper states "conducting experiments in the IID setting" as part of additional experiments (Section 4.2, last paragraph), likely in the appendix. Per the parser-strip rule, this is not a valid criticism.
- **Criticism about the Nira Adapt adaptive attack being "too narrow"** — Kept but downgraded: the point about limited adaptive attack testing is valid, but the specific phrasing in the harsh review ("the attackers...only align the surrogate samples with the data within the benign parts") is exactly what the paper reports, so it is not an omission. The core concern (missing evaluation of a more direct adaptive attack) is retained in Major Weakness #1.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the method or the problem that the paper itself does not already recognize.

## Suggestions

1. **Evaluate the most natural adaptive attack**: Design an attacker that explicitly optimizes a joint loss: backdoor task + high noise accuracy + feature-distance consistency on noise. If Nira still defends successfully, the defense has a genuine foundation. If it fails, the claims need to be revised.

2. **Address the threshold selection problem directly**: Provide a practical, data-agnostic method for setting σ₁ and σ₂ that does not require identifying benign clients. One possibility: use the full distribution of metrics across all received models in early rounds, with adaptive outlier detection. Report how sensitive final performance is to these thresholds (e.g., ablation plots).

3. **Report conventional evaluation metrics**: Include final-round attack rate and accuracy, or per-round curves, alongside the current "5 rounds before convergence" metric. Add confidence intervals or standard deviations over multiple runs for all main results.

4. **Drop or meaningfully strengthen Theorem 3.1**: Either remove it entirely (the paper's value is empirical) or replace it with a precise statement that specifies the bound, its dependence on the distribution gap, and the conditions under which it holds.

5. **Include higher attacker ratios in the main comparison table**: Extend the main evaluation (Table 1) to include attacker proportions of 40–60% to directly substantiate the claim that Nira works when attackers exceed 50%.

## Score and Decision

The paper presents a genuinely novel idea — using pure noise as an untainted surrogate for evaluating client models — and the initial empirical results are promising. However, the evaluation has significant gaps: the most natural adaptive attack is not tested, the threshold selection mechanism relies on a somewhat circular assumption, the evaluation metric is unconventional and lacks variance reporting, and the theoretical framing is vacuous. These weaknesses are individually addressable but collectively prevent the paper, in its current form, from convincingly establishing that the proposed defense is robust. The core idea has potential, but stronger validation — especially against adaptive attackers who directly optimize the filtering metrics — is essential.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>