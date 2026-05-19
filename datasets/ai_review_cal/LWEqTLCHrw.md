- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3
Now I have a thorough understanding of the paper and the reviewer inputs. Let me produce the final consolidated review.

---

## Summary

This paper proposes a two-stage anomaly detection framework for federated learning. The first stage (cross-round check) detects whether an attack has occurred by comparing client model cosine similarities against cached reference models. The second stage (cross-client detection) uses a three-sigma rule on $\mathcal{L}_2$ distances from an average model to filter malicious submissions — but only activates when the first stage signals an attack. A ZKP protocol (zkSNARKs in Circom) is added so clients can verify the server honestly executed the defense. Experiments on 10-client FL with small models show high detection accuracy and practical ZKP overhead (~0.05 s verification).

## Strengths

- **Proactive, conditional defense activation is well-motivated and demonstrated.** The cross-round check (Algorithm 1) uses cosine similarity thresholds against reference models to detect attacks before invoking the filtering stage. Figure 5 shows that with $\gamma=0.5$, the cross-round detection accuracy reaches at least 93% for both Byzantine and backdoor attacks. This directly addresses the paper's stated motivation — that existing defenses "change aggregation results even in the absence of attacks" — by ensuring the filtering mechanism is only activated when needed.

- **ZKP verification is practical and well-tested across models.** Table 2 reports verification times of 0.04–0.05 s for CNN, RNN, and ResNet-56, with proof sizes of 1.46–1.57 KB. The use of importance-layer compression (second-to-last layer, validated in Exp 1) and Freivalds' algorithm to reduce circuit complexity are concrete engineering decisions that make the ZKP integration tractable for resource-constrained clients.

- **Evaluation spans multiple architectures and datasets.** Experiments include CNN+FEMNIST, ResNet-20/Cifar10, ResNet-56/Cifar100, and RNN+Shakespeare (Exp 6, Figures 10–12), showing that the approach generalizes beyond a single model type, whereas baselines like m-Krum fail on RNN+Shakespeare (Figure 12).

## Weaknesses

### Fatal

None.

### Major

- **Baseline comparison conflates conditional activation with filtering quality.** The central claimed advantage — that the proposed method "significantly outperforms" baselines — is demonstrated in Exp 4 (Figures 7–8) under a 40% attack-probability setting. In the 60% of rounds without attack, the proposed method runs clean FedAVG (no modification), while baselines (m-Krum, Foolsgold, RFA) always perturb aggregation. The accuracy gap therefore conflates two separate effects: (a) the benefit of *not modifying aggregation when no attack occurs* (from the cross-round check), and (b) the benefit of *correctly filtering malicious models when an attack occurs* (from the cross-client detection). The paper does not ablate the cross-round check — i.e., compare a version that always runs cross-client detection against the full method — which is needed to isolate whether the cross-client detection itself is superior to existing filtering mechanisms. Without this, the headline accuracy differences may be driven primarily by the evaluation design rather than superior filtering.

- **Theoretical justification for the normality assumption on $\mathcal{L}_2$ distances is insufficient.** The paper states (Section 3.2) that "the Central Limit Theorem indicates that local models tend towards a normal distribution" and applies a three-sigma rule to $\mathcal{L}_2$ distances. However, the $\mathcal{L}_2$ distance is a non-negative, non-linear function of model parameters — it is not a sum of independent random variables, so the standard CLT argument does not directly apply to these distance values. The paper does not provide an empirical check of whether this assumption holds for the models and datasets used. Furthermore, with $\lambda=0.5$ (the default), under a true normal distribution roughly 31% of benign observations would fall above $\mu + 0.5\sigma$ and be removed — yet the paper claims benign models are "unharmed." The empirical results (PPV = 1/2 for Byzantine attacks) suggest this does not occur in practice, likely because malicious models inflate $\mu$ and $\sigma$, but this creates a tension with the method's own theoretical framing. A non-parametric alternative or empirical normality check would substantially strengthen this component.

- **No false-positive evaluation in purely benign scenarios.** The cross-round check accuracy (Exp 2) reports overall detection accuracy in a mixed attack/benign setting (40% attack probability), but does not isolate the false alarm rate in purely benign rounds. The cross-client detection's modified PPV is evaluated "given the cases with attacks" (Section 5.2), meaning its false-positive behavior in attack-absent rounds is unreported. If the cross-round check falsely signals an attack (false alarm), the aggressive $\lambda=0.5$ bound in the second stage could remove a significant fraction of benign models. This directly undermines the core claim that "benign client models remain unaffected," and the paper provides no empirical evidence that this does not happen.

### Minor

- **Evaluation is limited to small-scale, idealized settings.** All experiments use 10 clients with full participation every round. Real-world FL typically involves hundreds of clients, partial participation (e.g., 10% selection rate), and rare attacks. The cross-round check's accuracy and the $\mathcal{L}_2$-distance variance could change substantially at larger scales. The paper claims its design is suitable for "real-world FL systems," but does not validate scalability.

- **First-round initialization assumes fewer than half the clients are malicious.** For the first FL round, the cross-client detection uses m-Krum with $m = L/2$ to compute an approximate average model, "based on the assumption that the number of malicious clients is less than $L/2$" (Section 3.2, Step 1). While the method does not need the exact number $f$, this is nonetheless a prior assumption about the adversary's power. The paper's claim of operating "without any prerequisites such as ... the number of malicious clients" (Contributions, point iii) is therefore slightly overstated for the first round.

### Trivial

None.

## Nice-to-Haves

- An ablation that compares the full method against a variant that always runs cross-client detection (bypassing the cross-round check) would directly isolate the benefit of conditional activation.
- Reporting confidence intervals or multiple seeds for accuracy figures would strengthen the reliability of the quantitative comparisons.
- A brief discussion of the proving time overhead (~14 s for ResNet-56 per the paper's table) in the context of practical FL round durations would help calibrate the ZKP's deployability.

## Removed Points

**Harsh Critic point about "first round uses m-Krum with m=L/2, implicitly assuming fewer than half the clients are malicious — a prior assumption the paper claims not to need."**  
Kept as Minor (see above) but downgraded from the harsh critic's framing. The paper accurately discloses this assumption in Section 3.2 and uses it only for the first round; after that, the previous round's clean average model is used. The claim to "autonomy from prior knowledge" refers primarily to not needing to know the exact number of malicious clients $f$, which is accurate. This is a minor overstatement, not a contradiction.

**Harsh Critic point about "the ZKP description is high-level, missing fixed-point precision trade-offs and constraint counts."**  
Removed. The paper provides a clear description of the circuit construction, Freivalds' algorithm, and square-root verification. The detail level is appropriate for the main text of a conference paper; further specifics (constraint counts, precision) would be supplementary material. This is a presentation style preference, not a substantive weakness.

**Strength Finder point #3 about "no prior knowledge of the number of malicious clients is required" — partially overstated.**  
Kept but integrated into Minor weakness above rather than listed as a separate strength. The strength is partially valid (the method does not need $f$ after the first round) but needs qualification.

**Strength Finder generic phrasing about "addressing an important problem" and other general claims.**  
These were removed from the strengths list because they lack specific anchoring to concrete results in the paper. Only strengths with specific citations to figures/tables/equations were retained.

## Novel Insights

The harsh critic's observation that the baseline comparison conflates two distinct benefits (conditional activation vs. filtering quality) is the most penetrating insight. The paper presents its advantage as an inseparable whole, but decoupling these two effects is essential to understanding what the method actually contributes. Additionally, the tension between the normality assumption (which would predict ~31% benign removal with $\lambda=0.5$) and the empirical observation that no false positives occur (PPV = 1/2) points to a gap in the theoretical framing: the $\mathcal{L}_2$ distances of benign models likely do not follow a normal distribution in this setting, so the three-sigma justification is ornamental rather than operational. The method works empirically despite this, but the paper would benefit from dropping the CLT argument and adopting a purely empirical or non-parametric justification.

## Suggestions

1. **Ablate the cross-round check.** Compare the full method against a version that always applies cross-client detection (no cross-round check). This directly shows whether the advantage over baselines comes from conditional activation, superior filtering, or both.
2. **Report false-positive rates in fully benign runs** (no attacks at all) for both detection stages. This is essential to validate the claim that benign models are unharmed.
3. **Provide an empirical validation of the normality assumption** (e.g., Q-Q plots or goodness-of-fit tests for $\mathcal{L}_2$ distances), or replace it with a robust/non-parametric alternative (e.g., median + MAD) that relaxes the assumption.
4. **Scale the evaluation to at least 50–100 clients with partial participation** (e.g., 10–20% per round) and rare attacks (1–5% of rounds) to support the "real-world FL" claim.
5. **Report standard PPV** (TP/(TP+FP)) alongside the modified version to improve interpretability.
6. **Discuss the proving time overhead** (~14 s for ResNet-56) in context. If FL rounds take minutes due to client training time, this may be acceptable; if rounds are fast, the overhead matters.
