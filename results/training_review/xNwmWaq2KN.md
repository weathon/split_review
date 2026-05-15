Now I have all the information I need. Let me compose the final review.

---

## Summary

This paper introduces a multiobjective optimization perspective for diverse human motion in-betweening. It formulates the task as a bi-objective problem (diversity and smoothness), proves basic properties of this formulation, and integrates a pretrained generative model (VAE, GAN, or DDPM) into an evolutionary algorithm to search for Pareto-optimal motion sequences at inference time. The resulting framework, MGF-IMM, requires no additional training and shows improved diversity (APD) and accuracy (FID, ACC, ADE) across four motion datasets.

## Strengths

- **Novel formulation bridging multiobjective optimization and generative diversity.** The paper is the first to reframe motion in-betweening as an explicit bi-objective problem where Pareto-optimal solutions correspond to smooth, categorically distinct motions. Theorem 2 provides a formal (if simple) link: sufficiently separated points in objective space necessarily correspond to different motion categories, giving theoretical justification to the approach beyond ad-hoc diversity heuristics.

- **Plug-and-play operation at inference time with demonstrated generality.** The multiobjective framework is applied during inference only — no retraining or parameter addition is needed. Tables 1 and 3 confirm that MGF-IMM consistently improves both diversity and accuracy metrics when applied to three fundamentally different backbone generative models (VAE, GAN, DDPM), suggesting genuine generality.

- **Strong quantitative results across benchmarks.** Table 1 shows MGF-IMM achieving the best or second-best APD on all four datasets (BABEL, HumanAct12, NTU RGB-D, GRAB), often by large margins, while also leading or being competitive on FID, ACC, and ADE. These results hold across different backbones.

- **Variable-length generation is principled and beneficial.** The method automatically estimates transition length via cosine similarity between keyframes (Eq. 6). Table 2 systematically shows that variable-length generation outperforms fixed-length alternatives across multiple methods, validating this design choice.

- **Qualitative validation of Pareto front exploration.** Figure 4 visualizes the evolution from an irregular initial population to a well-distributed set of solutions along the Pareto front, providing direct evidence that the EA-guided search successfully explores the trade-off between the two objectives.

## Weaknesses

### Fatal
None.

### Major

- **The key conditioning mechanism in the evolutionary loop is underspecified.** Equation (5) states that for iterations \(i \ge 1\), the generator \(G\) conditions on the previously generated sequence \(Y_{i-1}^{[n]}\) in addition to \(X_1, X_2\). The paper says "the generative model is conditioned not only by the user-provided sequences but also by the sequences already generated" (lines 108–109), but provides no architectural or algorithmic detail on how this is implemented. The generator was trained to produce \(Y\) from a latent code \(Z\) conditioned on \(X_1, X_2\) — there is no explanation of how \(Y_{i-1}^{[n]}\) is fed back into the model at inference time. Without this, the core evolutionary mechanism cannot be reproduced, and it is unclear whether the described approach is feasible without architectural changes or retraining. This is the most significant weakness in the paper.

- **The accuracy gains (FID, ACC, ADE) are not explained and may reflect a confound.** The objectives \(F_1, F_2\) contain only a classifier-driven diversity term and a boundary smoothness term — no fidelity or realism objective. Yet Table 1 reports substantial improvements on these accuracy metrics (e.g., FID drops from 0.422 to 0.222 for the VAE backbone). The paper offers no analysis of why this happens. Possible explanations range from a benign side-effect (Pareto-optimal samples are closer to the data manifold by accident) to a concerning one (the generative model alone is weak and the selection procedure simply cherry-picks samples that happen to look reasonable). This gap weakens confidence in the reliability of the reported gains.

### Minor

- **The connection between per-sample objectives and intra-batch diversity is not clearly articulated.** The objectives \(F_1, F_2\) are defined per individual sequence. The paper states that batch-level diversity emerges because the EA's nondominated sorting and crowding-distance mechanisms maintain a diverse population of Pareto-optimal solutions (lines 17, 99). This is a valid argument, but it is never explicitly made — the text instead repeatedly implies the objectives themselves encode diversity. Making the EA's role explicit would prevent the misconception that the formulation optimizes only per-sample extremes rather than batch-level coverage.

- **Theorem 1 is near-trivial and Theorem 2 is a simple inequality.** Theorem 1 states that minimizers of the smoothness term \(\beta\) are Pareto-optimal — this follows almost directly from the definition of Pareto optimality given the additive structure of \(F_1, F_2\). Theorem 2 shows that two Pareto-optimal points far apart in objective space (Manhattan distance \(> 4/D\)) must have different motion labels, which is a mathematically correct but shallow result. The theorems provide correctness guarantees for specific narrow properties but do not explain why the multiobjective search yields high-quality motion or how well the Pareto front covers the space of plausible motions. The paper's claim (abstract) that "we prove that for any Pareto optimal solutions … can support smooth and diverse transitions" overstates the scope of these results.

- **The comparison against baselines is not controlled for inference-time search cost.** MGF-IMM uses 20 generations × 20 population members = 400 generator calls plus nondominated sorting per batch, while baselines (RMI, MITT, MultiAct, etc.) sample once or a few times without a selection mechanism. The APD gap in Table 1 is therefore partly a consequence of the search budget, not of the multiobjective formulation per se. The ablation study (Table 3, "with vs. without the framework") partially addresses this by isolating the framework's effect, but a cleaner comparison would give baselines access to a comparable inference-time diversity strategy (e.g., diverse beam search, or the same evolutionary search applied to a baseline generator).

- **The paper does not provide a proof sketch for either theorem.** Both theorems are stated without derivation or proof sketch. While complete proofs may appear in a supplementary document stripped by the parser, the absence of any proof intuition in the main text makes it difficult for readers to assess rigor or identify the assumptions on which the results depend.

- **No limitations or failure cases are discussed.** The paper does not acknowledge limitations such as: dependence on a pretrained classifier (whose accuracy directly affects the diversity signal), the sensitivity of results to population size or number of generations, the computational cost (400 generator calls per batch), or the risk that the Pareto front may collapse to a few modes when the classifier is poor. Including such discussion would strengthen the paper's scientific rigor.

- **Classifier training details are absent.** The diversity component \(\alpha_1(Y) = \frac{1}{D}(C(Y) + P_c(Y))\) mixes an integer class label with a probability. The paper does not specify how the classifier is trained, on which data, what its accuracy is, or how the D motion categories are defined across datasets. Since every objective evaluation depends on this classifier, the omission is nontrivial.

### Trivial

- The APD metric is defined as "average pairwise distance" but the specific distance measure (Euclidean on joint positions? joint angles? some learned feature?) is not specified.
- The smoothness term \(\beta\) only considers the boundaries (first/last poses connecting to keyframes), not the internal temporal smoothness of the generated sequence. This is a weak proxy for overall motion smoothness.
- The padding operation for variable-length sequences (repeating the last pose) may introduce artifacts at the transition boundary.

## Nice-to-Haves

- Apply the same multiobjective optimization procedure to baseline generators (e.g., CondMDI, RMI) and compare against MGF-IMM to isolate the benefit of the specific generator-guidance mechanism from the benefit of the EA selection alone.
- Compare against a simple "sample many → pick diverse subset" baseline (e.g., sample 400 times and select the 20 with highest pairwise distance) to assess whether the evolutionary search itself adds value over post-hoc selection.
- Report classifier accuracy on test data and analyze sensitivity of the diversity metric to classifier noise.
- Analyze the diversity-quality trade-off (e.g., precision-recall curves, mode coverage) to confirm that increased APD does not come at the expense of realism.
- Show failure cases or situations where the Pareto front collapses.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"The multiobjective formulation does not actually target intra-batch diversity."** The reviewer claimed the formulation has "no batch-level term, no repulsion, and no coverage criterion." This ignores that the paper uses nondominated sorting and crowding distance (line 99) — standard EA mechanisms that explicitly maintain a diverse population spread across the Pareto front. The per-sample objectives plus EA population management IS the mechanism for batch diversity. The criticism is factually incomplete.
- **"The evaluation is fundamentally unfair and circular."** The reviewer's framing that baselines are denied an inference-time strategy misunderstands that MGF-IMM's contribution IS the inference-time strategy. The paper also provides an ablation (Table 3) directly comparing with vs. without the framework on the same backbone. The "circular metric" criticism ignores that APD is a standard, externally defined diversity metric and that accuracy metrics (FID, ACC, ADE) — not optimized by the objectives — also improve.
- **"Theorems convey essentially no useful information."** The theorems are modest but not useless. Theorem 2 provides a formal guarantee that sufficiently diverse Pareto-optimal solutions correspond to different motion categories, which is non-obvious and links objective-space diversity to semantic diversity.
- **"Omits recent inference-time diversity methods"** — removed per the rule against mentioning missing related works.
- **"Missing appendix proofs"** — removed per the rule about parser-stripped appendix content.
- **"Overclaim that the structure can be applied to other generative models"** — the paper demonstrates MGF-IMM with VAE, GAN, and DDPM backbones, providing empirical support for this claim.
- Various formatting/style nitpicks about section organization and sentence-level presentation.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation that emerges from reading the reviews is a methodological one: framing generative diversity as a multiobjective optimization problem naturally separates the *what* (what properties make individual outputs good) from the *how* (how to maintain a diverse set of solutions). Standard diversity-promoting techniques in generation (e.g., repulsion losses, diverse beam search) often hard-code the diversity mechanism into the objective or sampling procedure. The multiobjective framing decomposes this: simple per-sample objectives define quality, and the EA's population-management machinery handles coverage. This modularity is elegant and may transfer to other generation tasks (e.g., text, molecule, 3D shape generation) where intra-batch diversity is valued. The main barrier to adoption is the underspecified generator-conditioning loop, which the authors should clarify.

## Suggestions

1. **Clarify the conditioning mechanism in Eq. (5).** Provide a concrete description (pseudocode or architectural diagram) of how \(Y_{i-1}^{[n]}\) is fed into the generator \(G\) at inference time. If the generator simply takes the previous output as an additional input feature, state this explicitly and discuss whether any training adaptation is needed. If a different mechanism is used, describe it fully. This is essential for reproducibility.

2. **Analyze why accuracy metrics improve.** Add an experiment or analysis section investigating why FID, ACC, and ADE improve when the objectives do not contain a fidelity term. For example: (a) compare against a "sample randomly 400 times and pick the best 20 by FID" baseline; (b) check whether the Pareto-optimal samples are closer to the training manifold simply because the EA's selection eliminates outliers; (c) compute precision/recall or coverage statistics to separate diversity from quality.

3. **Discuss limitations openly.** Add a limitations paragraph covering: dependence on classifier quality, computational cost (400 generator calls per batch), sensitivity to population size and iteration count, and the boundary-only definition of smoothness.

4. **Provide proof sketches.** Even without a formal appendix, include brief proof sketches for Theorems 1 and 2 in the main text (1–3 lines each) so readers can assess their validity.

5. **Add controlled baselines.** (a) Apply the same EA-based multiobjective optimization to one or two existing baseline generators (e.g., RMI or CondMDI) to show the framework's benefit is not specific to the authors' backbone. (b) Compare against a simple "sample N times, select diverse subset" baseline to isolate the value of evolutionary search over post-hoc diversity selection.

## Score and Decision

**Originality:** Good — multiobjective framing of generative diversity is novel.  
**Importance:** Moderate-high — intra-batch diversity is practically important in animation/graphics.  
**Claims support:** Mixed — Table 1 and ablations provide evidence, but the unspecified conditioning mechanism and unexplained accuracy gains weaken support.  
**Soundness of experiments:** Moderate — the experimental design is reasonable but has gaps (no controlled baselines, no classifier analysis, no failure cases).  
**Clarity:** Moderate — the overall idea is clear but critical implementation details are missing.  
**Value to community:** Potentially high if the gaps are resolved; the modular multiobjective framing could generalize beyond motion.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>