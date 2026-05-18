Now I have a thorough understanding of the paper. Let me construct the final review.

## Summary

This paper presents a normative reinforcement learning model where Gaussian place fields are optimized alongside an actor-critic via TD-error-driven gradient updates to maximize cumulative reward. The model reproduces three experimentally observed phenomena in hippocampal place field dynamics — high field density at reward locations, field elongation and backward center-of-mass shift against the trajectory, and representational drift with stable behavior — within a single unified framework. The paper further shows that noisy field parameter updates facilitate relearning of changing reward targets, suggesting a functional role for representational drift.

## Strengths

1. **Unified normative account of three disparate place field phenomena**: The same model, under a single reward-maximization objective, reproduces high field density at reward locations (Fig. 1B–C), field elongation and backward COM shift (Fig. 2A–B), and representational drift with stable navigation behavior (Fig. 3B–C). Prior work addressed each phenomenon in isolation; unifying them under one framework is a genuine contribution.

2. **Perturbative analysis linking TD-driven learning to field dynamics**: Equation (7) and Fig. 1E–F analytically show that field centers shift proportionally to squared critic weights and amplitudes amplify with value, providing a mechanistic foundation for why reward locations attract fields faster than other locations. This goes beyond pure simulation.

3. **Novel contrast with successor representation reveals testably distinct dynamics**: Figs. 2C–E show that RM fields initially anti-correlate with occupancy while SR fields track it positively, and that the two representations converge late in learning. This yields experimentally distinguishable predictions about early- vs. late-phase field dynamics.

4. **Ablation study identifies which field parameters drive policy improvement**: Fig. 4A–B shows that width optimization yields the largest reduction in convergence time, followed by amplitude; field optimization with as few as 8 fields matches the performance of 128 fixed fields. This result supports the computational efficiency of representational flexibility.

5. **Demonstration that noisy field updates enable continual learning of new targets**: Fig. 4C shows that injecting Gaussian noise (σ_noise ~ 0.0005) allows agents to relearn multiple target changes while noise-free agents get stuck, providing a potential functional role for drift.

6. **Analytical approximation of drift regimes matches experimental data**: Fig. 3F shows that with small noise magnitudes, high-amplitude fields are more stable than low-amplitude fields, replicating the inverted relationship reported in Qin et al. (2023) — a non-trivial prediction that emerges from the model without being explicitly designed.

## Weaknesses

### Fatal
None.

### Major

1. **The noise benefit for new target learning is reported but not mechanistically analyzed.** Figure 4C (and the associated claim that "there is a functional role for noise") is one of the paper's most distinctive contributions, yet the paper provides no analysis of *why* noise helps. The only explanation offered is the brief remark "without getting stuck in local minima" (Discussion). Multiple plausible mechanisms are consistent with the observation — noise could prevent over-specialization to the first target, implement a regularization effect, break representational degeneracies, or generate useful exploration in parameter space — but none are tested. Without diagnostic experiments (e.g., tracking representational diversity, measuring whether noise prevents representational collapse, or showing that noise induces a beneficial regularization effect), the claim that drift has a functional role remains a conjecture on top of a correlation, not a demonstrated finding. This is a significant gap given that the paper presents this as a central result (contribution 4 in the introduction).

### Minor

2. **The theoretical account of field elongation is incomplete.** The perturbative analysis (Eq. 6, App. B) derives center shifts and amplitude amplification from the TD objective, but does not derive width changes. Since elongation is defined by *both* backward COM shift and *increase in width*, the paper demonstrates the latter only via simulation (Fig. 2A–B). The reader cannot tell whether elongation is an incidental byproduct of the particular gradient parameterization or a necessary consequence of reward maximization with Gaussian fields. The paper would be strengthened by extending the perturbative analysis to width (even approximately) or at minimum by clarifying why width might be harder to derive.

3. **The comparison with successor representation architecture is asymmetric.** The SR agent uses fixed place fields feeding the actor-critic, with separate successor fields trained via the SR objective, while the RM agent has a single set of adaptive fields feeding the actor-critic directly (Sec. 4.2). Differences between RM and SR field dynamics could reflect either the different learning rules (TD on reward vs. TD on transitions) or the different architectural roles (adaptive vs. separate representation). The paper attributes differences to the algorithms, but the architectural confound is not controlled for.

4. **The ablation result that width optimization helps most (Fig. 4B) is not explained.** Why width dominates over amplitude and center is an interesting finding that the paper reports but does not analyze. A possible explanation (width controls spatial resolution in a way amplitude cannot compensate for) is mentioned nowhere — the result remains observational rather than explanatory.

### Trivial

5. The degeneracy between place-field amplitudes and actor/critic weights is acknowledged (Sec. 4.4) but not systematically disentangled. Given that the ablation study already addresses the relative contributions of each parameter type, this is a minor gap in analysis rather than a flaw.

## Nice-to-Haves

- **Diagnose the noise benefit mechanistically**: Run diagnostics that directly test *why* noise improves new target learning — e.g., measure representational similarity before/after target changes with and without noise; track whether noise prevents multiple fields from collapsing to the same location; measure the effective rank of the representation.
- **Compare noise against alternative mechanisms for avoiding representational stagnation**, such as replay, higher learning rates on actor-critic weights, or weight decay, to establish whether noise is special.
- **Disentangle normative from algorithmic predictions**: Clarify which results would follow from any reward-maximization-based learning rule (e.g., high density at reward locations) and which depend on the specific gradient-based backpropagation architecture (e.g., the specific anti-correlation pattern in Fig. 2D).

## Removed Points

The following points from the raw reviews were removed or downgraded because they do not survive verification against the paper:

- **"The paper does not separate normative from mechanistic claims"** (from Harsh Critic point 1 — partially removed concept): The paper explicitly states in the Discussion that it "must be extended using biologically-plausible learning rules before it can in any way be considered mechanistic." The paper consistently identifies itself as a normative model. The remaining kernel — that specific predictions could be more clearly categorized — is retained as a Nice-to-Have rather than a weakness, since the paper is already appropriately scoped.

## Novel Insights

The key insight that emerges from reading the reviews against the paper is that the paper makes a stronger contribution in its unification of three phenomena under one objective than in any individual phenomenon's depth of explanation. The field density and elongation results are convincingly demonstrated and partially derived; the drift and noise results are well-observed but under-analyzed. The paper would benefit most not from adding more phenomena or experiments, but from deepening the analysis of the phenomena it already reports — particularly the noise benefit, which is the most novel claim and currently the least supported by mechanistic understanding.

## Suggestions

1. Add diagnostic experiments for the noise benefit: measure representational similarity before/after target changes, track whether noise prevents representational collapse, and compare against alternative mechanisms (e.g., higher learning rates, weight decay).
2. Either extend the perturbative analysis to field width, or explicitly acknowledge that the elongation width effect is currently a simulation result without a theoretical derivation.
3. When reporting the width ablation finding (Fig. 4B), add a brief discussion of *why* width might be the most impactful parameter — e.g., controlling spatial resolution that amplitude alone cannot compensate for.

## Score and Decision

**Originality**: 7/10 — Unifying three phenomena under one normative framework is novel, though the individual components (TD learning, actor-critic, place fields) are established.

**Importance of research question**: 8/10 — Understanding why place fields exhibit these characteristic dynamics is a significant question in systems neuroscience.

**Claims supported**: 6/10 — The three phenomena are convincingly reproduced, but the noise benefit claim lacks mechanistic support.

**Soundness of experiments**: 7/10 — Well-designed experiments with appropriate baselines, confidence intervals, and ablations; the main gap is analysis depth rather than experimental validity.

**Clarity of writing**: 7/10 — Clear structure and figures, though some theoretical derivations could be better motivated.

**Value to community**: 7/10 — Provides a useful normative framework and testable predictions that distinguish RM from SR accounts.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>