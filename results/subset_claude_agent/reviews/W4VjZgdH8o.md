Now I have enough information to write the draft review. Let me submit it and proceed to calibration.**Round 1 Bracket: 3 to 5.** The paper resembles low-to-middle band application papers (DT variants applied to new environments), with the most topically similar being 324fOKW1wO (avg 3.33) and emns7tgDOq (4.00). Let me read 1-2 of those anchors and do a narrowing round.Round 2 — Narrowing within bracket (3–5):Now I have sufficient calibration data to write the final review.

**Calibration Summary:**

- **Round 1 bracket**: 3–5, based on similarity to DT-application papers like SimDT (3.33) and CRDT (4.00).
- **Round 2 anchors**: epbXCD1Ifk (3.67, BVE for combinatorial offline RL — novel method that actually outperforms baselines); kHfIuagAq6 (4.00, empirical RL study — solid empirical but incremental); SimDT (3.33 — DT application that at least shows quantitative improvements).

The µRTS paper is **worse than** epbXCD1Ifk (3.67) because BVE is a genuinely working novel method. It is **comparable to or below** SimDT (3.33) because SimDT at least shows clear quantitative gains; here the primary contribution (OCGDT) doesn't outperform ODT and the fine-tuning doesn't help. I settle at **3.0**.

---

## Summary
This paper adapts two existing Decision Transformer extensions — CGDT (critic-guided) and ODT (online fine-tuning) — to the Gym-µRTS real-time strategy environment, proposes their combination as OCGDT, and releases a 3,000-trajectory dataset. Training proceeds in three phases (critic pre-training, offline policy learning, online fine-tuning). The main empirical claims are that DT-based methods match IQL performance while requiring far fewer gradient updates, and that OCGDT achieves a positive head-to-head win rate against IQL.

---

## Strengths

- **Training efficiency advantage over IQL**: CGDT, ODT, and OCGDT all match IQL 800k's win rates against CoacAI (22.3–26.2% vs. 21.5%) while requiring only 13,000 gradient updates and ~4.25 wall-clock hours versus IQL's 800,000 updates and 9 hours (Table 1, Section 4.3). This is a concrete, reproducible efficiency result specific to this environment.

- **Systematic ablation study with concrete component-level findings**: Seven controlled ablation variants (OCGDT A–G in Table 1) isolate the effect of online-only training, extended fine-tuning, buffer size, absence of fine-tuning, longer offline training, and context length. The trio of OCGDT B (degraded), C (partially recovered), and D (matched full OCGDT) provides causal evidence that buffer contamination by early-exploration trajectories — not fine-tuning per se — is responsible for performance degradation, which has practical implications for DT-based fine-tuning pipelines more broadly.

- **Honest characterization of negative results**: Section 5.1 directly acknowledges that "the online fine-tuning mechanism does not provide a significant benefit over the offline model." This transparency, combined with the buffer-size experiment (OCGDT C), constitutes a meaningful diagnostic contribution even in the absence of positive performance gains.

---

## Weaknesses

### Fatal
None.

### Major

- **OCGDT does not demonstrably improve over ODT, its primary component**: The paper's central thesis is that combining CGDT and ODT produces a stronger agent. Table 1 shows OCGDT achieves 26.2 ± 4.3% vs. CoacAI and 40.1 ± 4.8% vs. Mayari; ODT achieves 25.5 ± 4.2% and 46.3 ± 4.9%. Against CoacAI the gap is 0.7 pp — entirely within the Wilson interval. Against Mayari, ODT *outperforms* OCGDT by 6.2 pp. The paper's framing that OCGDT "combined the strengths" of both components is not supported by the evidence; in the harder matchup (Mayari), ODT is better with no fine-tuning or critic.

- **The online fine-tuning component — OCGDT's distinguishing feature — is non-functional under the reported experimental setup**: OCGDT D (no fine-tuning) scores 23.0 ± 4.1% vs. CoacAI and 43.3 ± 4.8% vs. Mayari, completely overlapping with full OCGDT (26.2 ± 4.3% and 40.1 ± 4.8%). Against Mayari, the no-fine-tuning variant actually scores higher. Section 5.1 correctly identifies this, attributing it to dataset scale and early-exploration quality, but this means OCGDT's "O" contributes nothing under the current setup. The proposed method is functionally equivalent to CGDT with entropy regularization.

- **Statistical interpretation systematically overstates what the data show**: The abstract's claim of "a positive win-rate against IQL" based on 51.6 ± 4.9% (Table 2) is not statistically significant — the lower bound of the Wilson interval is 46.7%, which includes 50%. The "half the wall-clock hours" claim aggregates CoacAI (where OCGDT is higher: 26.2 vs. 21.5%) and Mayari (where IQL 800k is higher: 42.6 vs. 40.1%), with all intervals overlapping. The efficiency claim for OCGDT also applies equally to CGDT and ODT, which require the same computational budget.

### Minor

- **Training distribution overlap with evaluation opponents**: The dataset is generated from CoacAI vs. Mayari games (Section 4.1), and these are the two primary opponents in Table 1. The agent has seen expert demonstrations of those bots' strategies during offline training. Performance on these opponents may not reflect how the method would generalize to unseen opponent strategies. The paper evaluates on held-out maps but not on held-out opponent types.

- **IQL "equivalent samples" comparison inflates OCGDT's data consumption**: The footnote (Section 4.3) computes 25,600,000 OCGDT samples as 100 × 32 × 8,000 = 25,600,000. However, each gradient step in a K=100 context model processes 100 *overlapping* windows from a single trajectory segment, not 100 independent data points. The practical data diversity per step is closer to one trajectory segment. The three IQL checkpoints (13k, 400k, 800k steps) partially address this, and the wall-clock comparison is more meaningful, but the primary "equivalent samples" framing is misleading.

### Trivial

- Section 3.2 reports a temperature coefficient of 0.25 at evaluation vs. 1.0 during training, without noting whether this value was swept or fixed a priori. Win rates in a competitive game environment can be sensitive to temperature; a brief justification would strengthen reproducibility.

---

## Nice-to-Haves

- A behavioral cloning baseline (standard DT with no critic guidance and no entropy term) would anchor how much performance comes from imitating the data distribution vs. the RL objective components, clarifying whether the critic or entropy terms are contributing anything beyond pure imitation.
- Include results for WorkerRushAI and LightRushAI in the main results table (they are listed as benchmark opponents in Section 1.2 but absent from Table 1); results against bots not represented in training data would provide the cleanest generalization evidence.
- Increasing evaluation to ~1,000 games per matchup would halve Wilson interval widths (~±3pp), enabling the key comparisons (OCGDT vs. ODT, with vs. without fine-tuning) to actually be resolved.
- Report environment interactions (game steps or episodes) alongside wall-clock time; the hardware-specific RTX 4090 timing makes efficiency claims difficult to compare across settings.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **"Reproducibility infrastructure as a strength" (Strength Finder)**: Reporting hyperparameter ranges and code links is standard practice, not a research strength per se. Removed as generic.
- **"Multi-bot cross-agent evaluation as a strength" (Strength Finder)**: Evaluating against multiple bots is a methodological choice, not a substantive contribution. Removed as generic.
- **Criticisms about missing appendix content** (Harsh Critic references to hyperparameter tables in appendix): Per hard rules, the appendix is stripped from all parsed papers; absent appendix content is not an author error. Removed.
- **Scope creep: larger maps, other environments** (Harsh Critic notes 8×8 limitation): The paper explicitly scopes to 8×8 (Section 6). Criticism of absent larger-map experiments is out of scope.
- **"Behavioral cloning baseline is essential"** (Harsh Critic frames this as important missing comparison): Valid as a nice-to-have but not a fatal or major gap for an application paper demonstrating DT viability in a new environment. Demoted to Nice-to-Have.

---

## Novel Insights

The buffer contamination experiment (OCGDT B/C/D trio) constitutes a small but clean causal demonstration of early-exploration trajectory pollution in DT-based fine-tuning pipelines. The fact that increasing buffer size partially recovers performance (C vs. B) while no fine-tuning matches full fine-tuning (D vs. OCGDT) jointly implies that the issue is not in the fine-tuning mechanism itself but in the quality of trajectories collected before the policy matures. This has a concrete practical implication: asymmetric buffer weighting or curriculum scheduling for DT online fine-tuning may be more effective than simply extending the fine-tuning horizon.

---

## Suggestions

1. Reframe the IQL comparison: instead of claiming a "positive win-rate," report that "OCGDT matches IQL 800k's win rates against benchmark bots while requiring 60× fewer gradient updates and half the wall-clock time" — a claim directly supported by Table 1.
2. Investigate why OCGDT underperforms ODT against Mayari (6.2pp gap) — this is the most surprising finding. Does the critic guidance actively interfere with the strategies learned against that specific opponent? This diagnostic would substantially sharpen the paper's analysis.
3. Provide a single additional comparison point: run CGDT with entropy regularization (without the online fine-tuning). This would isolate whether the entropy term or the fine-tuning is responsible for any remaining difference between CGDT and OCGDT D.
4. Test a simple curriculum where offline trajectory weight is linearly decayed during fine-tuning. The paper's own analysis predicts this should help (Section 6); testing it would directly validate the diagnosis.

---

## Score and Decision

**Anchor papers:**
| Path | Avg Score | Round | Comparison to µRTS paper |
|------|-----------|-------|--------------------------|
| 324fOKW1wO | 3.33 | R1 | SimDT — DT application showing concrete gains; more similar scope but at least OCGDT has some positive results in one matchup |
| INzc851YaM | 3.00 | R1 | Multi-obj DT — adapts DT to MORL; purely application, no clear gains over existing DT |
| emns7tgDOq | 4.00 | R1 | CRDT — proposes novel counterfactual reasoning in DT, some methodology novelty |
| ZtOnddFVT3 | 4.67 | R1 | Safe offline RL with transformer — more methodological novelty |
| 5iWim8KqBR | 5.50 | R1 | Memory-efficient AD — stronger algorithmic contribution |
| epbXCD1Ifk | 3.67 | R2 | BVE — novel method that clearly outperforms baselines; more methodological content |
| kHfIuagAq6 | 4.00 | R2 | Empirical RL study — comparable empirical contribution, but extends into new algorithmic territory |
| PH7ja3T0vN | 4.50 | R2 | Diffusion-based decision making — more technical novelty |
| Ok7ZH2Cyd7 | 4.20 | R2 | Large-scale empirical RL analysis — broader empirical scope |
| OLi39lZS9Y | 3.50 | R2 | In-context learning for new tasks — similar empirical scope |

**Round 1 bracket**: 3–5.
**Round 2 narrowing**: The paper is below epbXCD1Ifk (3.67) because BVE is a novel method that demonstrably works; comparable to or below SimDT (3.33) because SimDT shows actual quantitative gains. The µRTS paper's primary contribution doesn't outperform its components. OCGDT D matches OCGDT, confirming the novel component adds nothing. Statistical overinterpretation of borderline results compounds the issue. No anchor below 3.33 is clearly weaker in all respects, so I do not drop below 3.

**Final score: 3.0 — Reject.**

**Originality**: Low — adapts and combines existing methods without clear methodological novelty.
**Importance**: Moderate — sparse-reward RTS control is a real challenge; first DT application in µRTS has value.
**Claim support**: Weak — the core claim (OCGDT improves over components) is not supported; statistical evidence is insufficient.
**Experiment soundness**: Moderate — design is thoughtful, ablations are honest, but sample sizes too small for the comparisons claimed.
**Writing clarity**: Good — methods are clearly described, limitations are honestly stated.
**Community value**: Limited — the dataset and environment adaptations have engineering value, but the negative finding about fine-tuning, while honest, does not constitute a sufficient positive contribution for an ICLR acceptance.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>