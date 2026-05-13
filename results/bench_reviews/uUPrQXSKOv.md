Now let me run the calibration search and read key anchors simultaneously.Now I have everything I need to write the consolidated review.

---

## Summary

RedGrape proposes decentralized decoupled training for federated long-tailed learning. The core idea is to allow clients to re-balance their classifier during local training by mixing local real data with global gradient prototypes (for classes with insufficient local samples), instead of relying on server-side pseudo features (as in CReFF). A supplementary classifier Ŵ is introduced so that the combined logits (W + Ŵ) model the global long-tailed distribution, freeing W to be optimized under a balanced training objective, thereby resolving the "contradictory optimization" problem that arises from concurrent instance-balanced and re-balanced training.

---

## Strengths

- **Local real data is demonstrated to be the critical ingredient (Figure 3):** Setting T=∞ (disabling real data and using only gradient prototypes for all classes) causes a sharp accuracy drop on CIFAR-10-LT, confirming that the decentralized re-balancing via real data is the primary driver of improvement. This directly validates the paper's core motivation against CReFF's server-side pseudo features.

- **Two-stream classifier architecture is empirically justified (Figure 4):** Ablating the supplementary classifier Ŵ causes the model to converge to a bad local optimum with substantially degraded accuracy on both CIFAR-10-LT and CIFAR-100-LT. This ablation constitutes direct, concrete evidence for the design choice.

- **Consistent improvements across diverse settings:** Results span 3 datasets (MNIST-LT, CIFAR-10-LT, CIFAR-100-LT), 3 imbalance ratios (IR=10, 50, 100), and both full and partial client participation settings — providing an 18-condition evaluation matrix where the method is always competitive or superior.

- **Faster convergence (Figure 2):** The learning curve in CIFAR-10-LT (IR=100) shows that RedGrape not only achieves higher final accuracy but converges substantially faster than all baselines. This is a useful signal beyond end-accuracy tables and aligns mechanistically with per-step classifier re-balancing.

---

## Weaknesses

### Fatal
None.

### Major

- **No per-class accuracy breakdown (head / medium / tail):** The main evaluation reports only overall balanced accuracy. This is the most fundamental diagnostic in long-tailed learning: a method could inflate head accuracy while degrading tail-class performance, with the net balanced accuracy masking the trade-off. Its absence makes it impossible to verify whether RedGrape actually helps tail classes, which is the paper's stated problem. This omission is particularly notable because the paper explicitly positions itself as solving global class imbalance, yet never shows how each class-frequency stratum benefits.

- **Single non-i.i.d. level (α=1) tested throughout:** The gradient prototype mechanism is explicitly motivated by the missing-class scenario, which is most acute under extreme non-i.i.d. partitions (small α). Yet the paper only evaluates at α=1, a moderate heterogeneity level. Under α=1 with 10 clients and CIFAR-10 (10 classes), most clients likely possess samples from all or nearly all classes, meaning gradient prototypes are rarely invoked. This means the regime where the method's key mechanism matters most is precisely the regime not tested. Claims of "consistent superiority" apply only within the α=1 regime.

- **Misleading claim that RedGrape has "no extra requirements except for the normal aggregations on the server" (Section 4.2):** The paper explicitly states: *"Compared with CReFF and Ratio Loss, we do not have extra requirements except for the normal aggregations on the server."* However, the algorithm (Algorithm 1, Sections 3.3.1–3.3.2) requires clients to compute per-class gradient prototypes {g^pro_{W^{t-2},k,c} | c ∈ L_k} and upload them every round, and the server to maintain, aggregate, and broadcast global per-class gradient prototypes. This is additional communication and server-side storage/computation beyond standard FedAvg — the claim is at best imprecise and at worst false. With C classes and d-dimensional classifier rows, the per-round extra upload is C×d real-valued numbers per client. The paper uses this claim in its core comparative analysis to argue advantage over CReFF, which is unfair if RedGrape's overhead is undisclosed.

### Minor

- **Informal theoretical justification for the two-stream design:** The paper invokes "Lagrange Multipliers" in Section 3.2 to motivate the update rule (Eq. 13), but the actual update is a weighted gradient combination with dynamic normalization — which is not a principled Lagrangian relaxation. The Lagrangian framing in Eq. (6) is not formally connected to the implemented update in Eq. (13). The argument that Ŵ "absorbs" the long-tailed gradient signal while W "specializes" in balanced classification assumes a natural partitioning of gradient descent responsibility that is never established. The empirical ablation (Figure 4) supports the design, but the mechanistic explanation is incomplete. This does not invalidate the paper, but it leaves the design under-explained.

- **Gradient prototype staleness is only partially addressed:** Prototypes used in round t are computed from model W^{t-2} (two rounds prior). The gradient scale normalization in Eq. (13) addresses scale mismatch (so stale gradients don't dominate in magnitude later in training) but does not address *direction* mismatch caused by model drift. No experiment characterizes how prototype quality evolves during training. In the presence of fast-converging models or high learning rates, two-round staleness could matter for tail classes that appear infrequently.

- **Missing ablation to isolate gradient prototype contribution:** The paper ablates local real data (T=∞) and the supplementary classifier (Figure 4), but does not ablate gradient prototypes while keeping local real data (e.g., simply zero-filling or skipping gradient contributions for missing classes). Without this, it is unknown whether the gradient prototype mechanism itself adds value or whether the improvement is entirely driven by local real data re-balancing for classes that are already present locally.

### Trivial

- The conclusion overstates: *"Thorough experiments verify..."* The experimental scope (three small-scale vision datasets, single α, small client counts) does not meet the standard implied by "thorough."

---

## Nice-to-Haves

- **Larger-scale datasets** (e.g., Tiny-ImageNet-LT, iNaturalist): FedLoGe, a comparable accepted Fed-LT paper, includes ImageNet-LT and iNaturalist evaluations. Showing RedGrape scales beyond CIFAR-100 would substantially strengthen the paper's practical claims.

- **Communication overhead quantification:** Reporting the per-round extra communication cost (in terms of additional floats per client) vs. FedAvg and CReFF would allow honest evaluation of the method's efficiency-performance trade-off.

- **Varying α from 0.1 to 5:** Sweeping α would characterize when gradient prototypes are beneficial and when they aren't, and would directly test the method in the regime that motivates its design.

- **Privacy analysis of gradient prototype sharing:** While the paper doesn't claim formal privacy guarantees, a brief discussion of the additional information leaked by per-class gradient vectors (vs. standard FedAvg gradient upload) would strengthen the paper's framing around privacy-preserving FL.

- **Classifier weight norm visualization by class:** Plotting ‖W_c‖ per class (sorted by frequency) before and after re-balancing would directly demonstrate that the method achieves the claimed bias reduction in classifier weights.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic's "privacy framing is incompatible with gradient sharing" as a structural flaw:** The paper uses FL's privacy motivation to justify not sharing raw data — a standard framing in the FL literature. It does not claim differential privacy or formal privacy guarantees. Class-conditional gradient sharing is more information-rich than raw gradient aggregation, but the same generic concern applies to many FL methods including CReFF. Elevated to a "nice-to-have" rather than a "major" weakness.

- **Harsh Critic's "Lagrange Multiplier framing is incorrect/fatal":** The math is indeed informal, but "Lagrange multipliers applied to inequality-constrained optimization" (i.e., penalty method) is a recognized, if loose, usage. The core update rule works and is empirically validated. Downgraded to Minor.

- **Strength Finder's "No auxiliary data or server-side computation requirements" as a core strength:** This is partially contradicted by the verified weakness above (gradient prototypes add overhead). Removed as a strength because the "no extra requirements" claim is imprecise.

- **Harsh Critic's "Section 4.1 threshold T" concern about CReFF rarely being invoked:** Partially valid, but the paper's ablation (Figure 3) specifically shows the effect of varying T, demonstrating the paper is aware of this trade-off. Not an independent weakness.

---

## Novel Insights

The gradient prototype mechanism offers an elegant solution to the missing-class problem in federated long-tailed settings: rather than generating synthetic features on the server, per-class gradient statistics are computed locally from real data, aggregated, and reused as a proxy gradient signal during local classifier re-balancing. This repurposes information already implicitly encoded in the standard FedAvg protocol (per-client gradient statistics) without new communication rounds. The combination with a two-stream classifier that allows the instance-balanced training signal to flow through a separate head, rather than competing with the re-balancing signal in a single classifier, is a practically clean and empirically effective design choice — even if the theoretical specialization argument is not formally established.

---

## Score and Decision

**Evaluation axes:**
- *Originality*: Moderate-to-good. The decentralized re-balancing idea via gradient prototypes is a genuine and novel combination of existing ideas (decoupled training + federated gradient statistics).
- *Importance*: Good. Federated long-tailed learning is practically relevant and underexplored.
- *Claim support*: Weak-to-moderate. Ablations support individual design choices (Figures 3 and 4), but overall evaluation is narrow (single α, no head/tail breakdown, CIFAR-only).
- *Soundness*: Moderate. Core method is sound but the theoretical mechanism is informal and a key comparative claim ("no extra requirements") is inaccurate.
- *Clarity*: Good. The paper is well-organized and the algorithm is described clearly.
- *Value to community*: Moderate. The method is practical (no server auxiliary data) and consistently competitive, but evaluation scope limits confidence in generality.

**Anchor comparison:**

| Path | Avg Human Score | Comparison to this paper |
|------|----------------|--------------------------|
| V3j5d0GQgH.md (FedLoGe) | 6.00 (Accept) | Most similar topic; accepted with broader evaluation (ImageNet-LT, iNaturalist, personalized + generic models) and more coherent theory than RedGrape. RedGrape's evaluation is narrower. |
| JNZdhbDBUH.md (CRePA/FedLT-CI) | 4.33 (Reject) | Same Fed-LT topic, rejected for disconnected components and CIFAR-only experiments. RedGrape is more coherent and has stronger ablations, so should score higher. |
| giU9fYGTND.md (FedImpro) | 7.00 (Accept) | Strong FL paper with theory, broader evaluation across heterogeneity levels, explicit communication analysis. Substantially more complete than RedGrape. |
| C7XoUdJ5ZC.md (FLAIR) | 3.00 (Reject) | FL with class imbalance/missing classes, rejected harshly. RedGrape is clearer and has stronger empirical support. |
| t8hMqAn8ZG.md (DFLMV) | 4.00 (Reject) | Decentralized FL, rejected. RedGrape has more novel contribution. |
| kH5nNlgT52.md (One-round FL fine-tuning) | 4.50 (Reject) | FL with narrow evaluation, rejected. Similar scope problem. |
| b66P1u0k15.md (Pareto LT) | 6.00 (Accept) | Long-tailed learning with multi-objective optimization, accepted with strong empirical + theoretical grounding. More rigorous than RedGrape. |
| BLvCdxAi8W.md (Granularity LT) | 4.25 (Reject) | Long-tailed learning, rejected for limited evaluation. |

**Verdict:** RedGrape sits between JNZdhbDBUH (4.33, rejected Fed-LT) and V3j5d0GQgH (6.0, accepted Fed-LT). The paper has a genuine, coherent contribution and clear ablations for its two main design choices, which puts it above the rejected Fed-LT papers. However, the missing head/tail accuracy breakdown, single-α evaluation, misleading "no extra requirements" claim, and CIFAR-only experiments put it meaningfully below FedLoGe (6.0, which has ImageNet-LT/iNaturalist and comprehensive evaluation). The evaluation gaps mean we cannot confirm the headline claim — that the method improves tail-class accuracy — is actually satisfied. This is a borderline paper that would benefit from a stronger evaluation round.

**Score: 5.0**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>