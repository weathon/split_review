## Summary

This paper proposes integrating n-gram induction heads (from Akyürek et al., 2024) into the Algorithm Distillation (AD) framework for in-context RL. The authors show that hard-coding n-gram attention patterns reduces training data requirements, decreases hyperparameter sensitivity, and can be extended to pixel-based observations via vector quantization. Experiments are conducted on a 9×9 Dark Room grid world, a Dark Key-to-Door POMDP, and Miniworld 3D environments.

---

## Strengths

1. **Measurable reduction in hyperparameter sensitivity**: Figure 2 shows that with 1K learning histories and 60 goals, the n-gram model finds near-optimal hyperparameters in ~20 random assignments versus >400 for the AD baseline — a concrete, quantified difference using the well-motivated EMP metric.

2. **Within-paper data efficiency demonstration**: Figure 1 sweeps training goals from 64 to 2048 for both methods under the authors' own protocol, and shows the n-gram model achieves near-optimal return at 128 goals versus 1024+ for the baseline. Figure 4 further confirms that at 100 training goals the baseline plateaus below 1.3 while the n-gram reaches ~1.9 in Key-to-Door.

3. **Successful VQ-based extension to pixel observations**: Figure 5 demonstrates that the VQ-quantized n-gram mechanism significantly outperforms the AD baseline in both Miniworld-Dark (30 goals) and Miniworld-Key-to-Door (300 goals), achieving near-optimal performance where the baseline saturates at suboptimal return. This is a non-trivial engineering contribution.

4. **N-gram hyperparameters do not inflate the search space**: Table 1(a)–(b) show EMP values across different n-gram lengths (1-, 2-, 3-gram) and layer positions are clustered within overlapping confidence intervals (0.67–0.76), empirically establishing that the additional hyperparameters are not sensitive.

5. **Graceful degradation when mechanism fails**: Table 1(c) shows that a randomly permuted n-gram mask (simulating failure) recovers the same EMP as the plain baseline (0.51±0.03 vs. 0.52±0.02), confirming the mechanism does not introduce harmful side effects.

---

## Weaknesses

### Fatal
None.

### Major

- **The "27× data efficiency" headline figure relies on a cross-paper comparison.** Figure 4's caption reads: "for the baseline method to converge to a model with the same performance, it needs 2048 goals and 2048 learning histories [17]." The 2048-goal baseline number comes from Laskin et al. (2022), not from the authors' own experimental protocol (which covers only up to 1000 learning histories in Figure 4). Figure 1 does include a sweep up to 2048 goals under the authors' protocol, but it is not unambiguously linked to the Key-to-Door environment, and the exact computation is deferred to Appendix B without adequate justification in the main text. The result is that the paper's most visible quantitative claim cannot be fully verified from the main paper alone. The claim should either be anchored by a clear within-paper controlled experiment or reframed to reflect what Figure 1 directly supports (e.g., "n-gram reaches baseline's 1024-goal performance with ~128 goals").

- **No comparison against any contemporary ICRL baseline.** The related work section cites four 2023–2025 works (Zisman et al. [33]; Kirsch et al. [14]; Schmied et al. [26]; Tarasov et al. [28]) that explicitly address data efficiency and/or hyperparameter stability in ICRL, yet none are used as baselines or compared against even informally. The sole baseline is AD from 2022. A paper framing itself as improving on ICRL data efficiency in 2025 needs to position itself against active, published work on the same problem. Without this, the contribution's relative value cannot be assessed.

### Minor

- **State-only matching consistently outperforms full-transition matching, but no explanation is offered.** Figures 2 and 4 consistently show "states" (yellow) above "[s, a, r]" (purple), yet Section 2.3 and Section 4 do not explain why. In a 9×9 grid world, matching state positions alone is equivalent to detecting spatial revisitation, which is highly frequent in exploratory trajectories, while matching full transitions (action + reward + state) is much stricter and may find fewer matches. An analysis of match frequency or attention entropy under the two schemes would explain the mechanism and help readers understand when each variant is appropriate.

- **Experiments are restricted to toy-scale environments.** The paper's conclusions about "data efficiency of in-context RL" rest entirely on a 9×9 Dark Room (80 possible goals) and simple Miniworld rooms. While the conclusion acknowledges this and mentions XLand-Minigrid and Meta-World as future work, the n-gram mechanism's value is precisely contingent on state revisitation frequency. In environments with diverse or compositional state spaces, revisitation rates drop sharply and the n-gram mechanism may find few valid matches. The current experiments cannot distinguish between "n-gram heads improve ICRL" and "n-gram heads improve ICRL in environments where states repeat frequently."

### Trivial

- **Table 1(c) reports only a two-way comparison (permuted n-gram vs. baseline).** Including the working n-gram model's EMP in the same table would make the ablation directly interpretable as a three-way: intact mechanism vs. broken mechanism vs. no mechanism.

---

## Nice-to-Haves

- A mechanistic analysis (e.g., attention heatmaps) showing what the n-gram head attends to in Dark Room trajectories would provide direct evidence that the mechanism is doing spatial revisitation detection, differentiating it from a generic regularization effect.
- A sensitivity study of VQ codebook size and pretraining quality in the Miniworld experiments would characterize the robustness of the pixel extension and help practitioners know when it is expected to work.
- One experiment in a moderately complex environment (e.g., XLand-Minigrid small variant) would substantially strengthen the generalization claim without requiring the full XLand scale.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "No within-paper experiment trains AD at 2048 goals under the authors' protocol."** Partially incorrect. Figure 1 includes data points for both methods up to 2048 goals (table: baseline 0.9→1.7, n-gram 1.1→2.0). The legitimate concern — that the exact 27× computation is cross-paper — is retained above as a Major weakness, but the sweeping claim that there is zero in-paper comparison is inaccurate.

- **Harsh critic: "The Miniworld improvement may come from the Zisman et al. noise curriculum rather than n-gram heads."** Incorrect. Section 3.3 states both the n-gram model and the baseline use the same oracle-agent data pipeline for Miniworld. Since the data collection protocol is shared across both conditions, it cannot explain the observed performance difference. This weakness is removed.

- **Harsh critic: "Figure 6 comparison is unfair — n-gram model uses 50 goals while baseline uses 60."** Removed per hard rule: the asymmetry favors the baseline (more goals), not the authors' method. The n-gram model outperforming the baseline despite fewer goals is the intended demonstration, not a confound.

- **Strength Finder strength 1 ("27× data reduction is a core strength"):** Partially retained at reduced weight — the within-paper Figure 1 comparison is genuine, but the exact 27× figure carries the cross-paper caveat noted above.

---

## Novel Insights

The clearest novel insight is methodological: by hard-coding n-gram attention before training rather than allowing it to emerge, one can bypass the known "simplicity bias" phase in which transformers learn unigram statistics first (Edelman et al. [6]) and thereby accelerate the appearance of in-context RL behavior. The paper provides empirical confirmation that this mechanism transfers from the language domain to decision-making sequences — including via VQ quantization for images — and that hyperparameter sensitivity of the mechanism itself is negligible. The finding that state-only matching consistently outperforms full-transition matching is unexplained but is itself a potentially interesting observation about what kind of sequential structure matters for in-context RL.

---

## Suggestions

1. Include an in-paper controlled comparison where AD is trained at 2048 goals under your exact protocol and report the crossing point clearly, so the data-efficiency claim stands independently.
2. Add at least one contemporary ICRL baseline (e.g., a reimplementation of the noise-curriculum approach or Tarasov et al.'s Q-learning variant) in at least one environment to position the contribution in the current literature.
3. Provide a quantitative or qualitative analysis of n-gram match frequency under the state-only vs. transition-matching variants to explain the performance gap between the two.

---

## Evaluation on Key Axes

- **Originality**: Moderate. The n-gram layer is adopted wholesale from Akyürek et al.; the contribution is applying it in a new domain (ICRL) and extending it to pixels via VQ. The idea is clean and the domain transfer is non-trivial.
- **Importance of research question**: High. Data efficiency and hyperparameter stability are genuine bottlenecks in ICRL, and practical solutions are valuable.
- **Claims well-supported**: Partial. Hyperparameter sensitivity reduction is well-supported (Figure 2). The headline 27× data-efficiency claim is only partially supported within the paper. The pixel extension claim is supported.
- **Soundness of experiments**: Adequate for the toy environments tested; the EMP metric and random HP search protocol are well-chosen. The lack of contemporary baselines and limited environment diversity limit the conclusions that can be drawn.
- **Clarity of writing**: Good. The method, evaluation protocol, and results are presented clearly, and the ablations address natural questions about the proposed mechanism.
- **Value to the community**: Moderate. The code contribution (VQ-based n-gram matching for images, integration with AD) is a concrete starting point for the ICRL community, but the current experimental scope is insufficient to establish broad impact.

---

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>