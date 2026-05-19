- Decision: Accept
- Avg Score: 5.00
- Scores: 5, 1, 6, 8
Here is my final consolidated review.

---

## Summary

This paper demonstrates that critical learning periods—temporary early deficits that permanently alter learned representations—emerge even in deep *linear* networks, establishing that such phenomena are not exclusive to biology or nonlinear architectures. The authors derive exact ODEs for learning dynamics in two settings: a multi-pathway network where pathways compete to learn features, and a matrix-completion transfer setting where pre-training on one task can harm later generalization. Depth amplifies competition/effects in both settings, and the analytical ODEs match SGD simulations.

## Strengths

- **First analytically tractable model of critical periods in deep networks**: The paper derives exact ODEs for learning dynamics (Eqs. 2–4) and validates them against SGD simulations (Fig. 3, dashed lines match crosses and pluses). Prior work (Achille 2018, Kleinman 2022) was purely empirical, so this provides a concrete theoretical handle on why critical periods emerge.

- **Isolation of depth and data structure as key causal factors**: Fig. 1 (phase portraits) demonstrates that deeper networks are more affected by early deficits in the multi-pathway setting, and Fig. 5 shows that depth amplifies sensitivity to initial training in matrix completion. This directly supports the claim that critical periods depend on depth and data distribution, not on nonlinearities or biochemical processes.

- **Recapitulation of a classical biological competition experiment**: Fig. 4 reproduces Guillery's 1972 lesion experiment—a deprivation deficit in one pathway combined with a permanent lesion in the other leads the deprived pathway to learn only the lesioned feature. This demonstrates that the minimal model captures competitive dynamics observed in biology.

- **Precise match between ODEs and SGD**: Figs. 3 and 4 show that ODE integration matches SGD training trajectories before, during, and after the deficit period, providing strong evidence that the analytical model faithfully captures actual learning dynamics.

- **Mechanistic winner-take-all explanation**: The flow fields in Fig. 1 show that singular values from competing pathways "race" and that this competition becomes more pronounced with depth, providing a mechanistic account of why early deficits have permanent effects.

## Weaknesses

### Fatal
None.

### Major

- **The matrix completion experiments do not demonstrate a critical period as defined by the paper.** The paper's own definition (abstract, line 4): "periods early in development where temporary sensory deficits can have a permanent effect on behavior and learned representations." The multi-path model supports this: early deprivation (epoch 0–150) permanently shifts feature allocation, while late deprivation (epoch 750–900) has negligible effect (Fig. 3). This is a genuine temporal *window*. In contrast, the matrix completion experiments only vary the *duration* of pre-training on a different task (T_critical = 0, 10000, 20000, 80000 epochs), showing that longer pre-training monotonically worsens final generalization. The paper never tests whether pre-training that begins *late* (after some final-task training) has less effect than the same duration of pre-training that begins *early*—which is the defining signature of a critical period. The observed effect is consistent with negative transfer / sensitivity to initial conditions, a different phenomenon. The paper frames both settings under the same "critical periods" umbrella (Section 4 title: "Critical learning periods for matrix completion") without acknowledging this conceptual gap or designing an experiment with a timing window. This weakens the coherence of the paper's central claim.

### Minor

- **No error bars, confidence intervals, or multiple-seed statistics for SGD simulations.** Figures 3, 4, and 6 show single-run trajectories (figures in Sec. 4 confirm single seed, e.g., filenames with `seed=1`). While the ODEs are deterministic, the empirical claim that "the differential equation matches the learning dynamics obtained with SGD training" (line 128) would be strengthened by showing variance across initializations. This is especially relevant for the matrix completion results (Figs. 5, 6) where the analytical ODE validation is deferred to the appendix.

- **The two settings operate through measurably different mechanisms, but the paper does not discuss this.** In the multi-path model, critical periods arise from *competition between pathways* over limited representational capacity. In matrix completion, the effect comes from *singular value buildup* during pre-training on the initial task—larger singular values learned faster in deeper networks are harder to "unlearn" when the task switches. These are distinct mechanisms (competition vs. inertia), and the paper would benefit from explicitly comparing them rather than treating both as instances of the same phenomenon.

- **The mapping from "gating deficit" (temporarily freezing parameter updates) to biological sensory deprivation (altering input statistics) is not discussed.** In biology, occluding an eye does not freeze that eye's processing pathway; it changes the statistics of the input it receives. The paper uses gating as a modeling choice (line 135: "temporarily prevent learning") but does not address whether this approximation is faithful or what might change if input statistics were altered instead.

- **The claim of "strong correspondence with biological systems that share these details" (depth and data distribution) overreaches.** The paper shows that the *model's* critical periods depend on depth and data structure, then speculates that biological systems share these details. The paper does not provide evidence that biological critical periods actually depend on, e.g., number of processing layers or data rank in the way the model predicts. The claim should be softened to note this is a prediction of the model.

### Trivial

- Minor typo on line 145: "simualtions" should be "simulations."
- Line 290: "defcits" should be "deficits."

## Nice-to-Haves

- An experiment in the matrix completion setting comparing the same duration of pre-training applied *early* vs. *late* (e.g., after some final-task training) would directly test whether a temporal window exists there, unifying both halves of the paper.
- A brief limitations paragraph discussing what the minimal model excludes (e.g., cross-talk between pathways, non-i.i.d. inputs, changing input statistics during deprivation) would improve the Discussion.
- Singular-vector evolution equations (referenced in the text as Eqs. U_evolve, V_evolve) should be stated in the main text rather than deferred.

## Removed Points

*These points are flagged to be removed—treat them with caution.*

- **"Data distribution not systematically studied"** — The paper studies data distribution through singular values (multi-path model, Section 3) and through rank/number of observations (matrix completion, Section 4, Figs. 5, 6). This criticism is too broad and is not supported by the paper's content.
- **"Missing appendix figures/equations"** (Fig. 7, Fig. 8, Eqs. U_evolve, V_evolve) — These are parser-stripped; they exist in the original submission.
- **"Missing related works"** — Per instructions, cannot be verified and should not be mentioned.
- **"Nonlinear networks mentioned only in passing"** — The paper explicitly states (line 146): "We observe similar learning dynamics and effect of a temporary gating deficit in nonlinear networks with a Tanh or ReLU activation function." The paper does address this.
- **"The initialization scheme constrains the solution space"** — The paper explains that the invariant q²−p² follows from the ODE structure (Eq. 116–117), not from an arbitrary constraint. This is mathematically derived, not an ad-hoc limitation.
- Various formatting/style nitpicks and speculative weaknesses that could not be confirmed from the paper.

## Novel Insights

The most interesting observation that emerges from these reviews is that the paper's two halves reveal tension in how the field thinks about critical periods. The multi-path model demonstrates a true temporal *window* where identical deficits at different times have different effects—this is what makes critical periods special as a phenomenon. The matrix completion setting instead shows that longer exposure to a source task monotonically worsens transfer, which is a continuous duration-dependent effect. The paper unifies both under "critical periods," but the reviewer correctly identifies that these are conceptually distinct phenomena. This tension points toward a deeper question the authors could address: is a critical period best characterized by a non-monotonic sensitivity profile (windowed), or can any early-life sensitivity to experience count, even if monotonic? Resolving this would sharpen the paper's contribution beyond what either review alone provides.

## Suggestions

1. **Redesign the matrix completion experiments to include a timing comparison**: Pre-train on the source task for a fixed duration starting either at epoch 0 (early) or at epoch T (late, after some final-task training). If early pre-training hurts more than late pre-training of the same duration, this would directly demonstrate a temporal window and unify both settings.
2. **Alternatively**, reframe the matrix completion results as a related but distinct phenomenon about how initial conditions affect generalization in deep linear networks, and clearly state how it complements (rather than parallels) the multi-path critical period analysis.
3. Add error bars or multiple-seed statistics to all SGD simulation figures.
4. Add a short paragraph in the Discussion comparing the two mechanisms (competition vs. singular value inertia).
5. Soften the claim about "strong correspondence with biological systems" to note this is a prediction of the model that remains to be tested biologically.
