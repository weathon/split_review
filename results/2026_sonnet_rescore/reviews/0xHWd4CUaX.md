## Summary
The paper proposes combining contrastive self-supervised pre-training of code graph embeddings with a reinforcement learning agent for automated code refactoring. A GNN encoder is pre-trained using InfoNCE loss on syntax-preserving augmentations of code graphs; its embeddings then enter a composite reward function alongside traditional code quality metrics and a semantic preservation penalty. An ablation study provides some evidence that each component contributes, and convergence is shown to be faster than a graph RL baseline.

---

## Strengths

- **Ablation evidence for contrastive pre-training (Table 2):** Removing the contrastive pre-training causes a 7.5 pp drop in SI (83.7 → 76.2%) and a 5.5-point drop in MG (27.9 → 22.4), providing concrete evidence that the self-supervised encoder is a meaningful component of the system.
- **Differential testing for semantic preservation (Table 2):** The semantic test ablation ("w/o semantic tests") shows an 8.6 pp drop in SP (93.8 → 85.2%), demonstrating that the lightweight verification mechanism is doing real work and is not merely cosmetic.
- **Faster policy convergence (Figure 1):** The proposed method reaches approximately 90% of maximum reward by episode 15k versus 25k for GraphRL, indicating that embedding-guided exploration materially reduces training time.
- **Principled integration of pre-trained representations and RL:** The high-level design — pre-train a representation on large unlabeled code corpora, then use those representations to guide RL — is a reasonable and well-motivated architecture for reducing hand-engineering in reward design.

---

## Weaknesses

### Fatal
None that are unambiguously verifiable from the paper alone.

### Major

- **Pre-training data description contradicts itself, directly undermining the cross-language claim.** Section 5.1 states "we used the CodeSearchNet corpus containing 2 million functions across **6 programming languages**." Section 5.4 states "we evaluated the model already trained over a **Java language codebase** (CodeSearchNet)." These cannot both be true. If pre-training is multilingual (including Python), the Table 3 cross-language experiment is not zero-shot transfer — Python/C++ representations were already seen during pre-training. If pre-training is Java-only, the setup description in §5.1 is incorrect. The paper provides no clarification, and the cross-language generalization claim depends entirely on resolving this contradiction.

- **Cross-language results show semantic-preservation regression, which is not acknowledged.** Table 3 (verified): Python — Ours SP = **88.9%** vs. PyLint SP = **90.4%**; C++ — Ours SP = **91.2%** vs. Cppcheck SP = **93.1%**. For both target languages, the proposed method's semantic preservation is *lower* than the simple rule-based tool it is compared to. Semantic preservation is the safety-critical property in refactoring. The paper characterises these results as "outperforming language-specific rule-based tools" (§5.4) without mentioning this trade-off — an overclaim that misrepresents the cross-language results.

- **GraphRL baseline is cited to a survey paper without a system description.** The reference for "GraphRL (Darvari et al., 2024)" is *Graph reinforcement learning for combinatorial optimization: A survey and unifying perspective* — a survey, not a system paper. The paper does not specify which method from the survey was implemented, how it was adapted to code refactoring, or whether results were reproduced or estimated. GraphRL is the proposed method's closest RL competitor in Table 1; its provenance is unspecified, which undermines the fairness of the primary comparison.

- **Equation 6 (exploration strategy) does not define a distribution over actions.** The formula is: $\pi_\text{explore}(a|s) \propto \exp\!\left(-\tfrac{1}{2}(\mathbf{h}_s - \mathbf{h}^*)^\top \Sigma^{-1}(\mathbf{h}_s - \mathbf{h}^*)\right)$. The right-hand side is a scalar function of the *state* embedding $\mathbf{h}_s$ — there is no action variable $a$ anywhere in it. The paper gives no explanation of how a scalar state-space density is converted into a distribution over discrete refactoring actions. This central component of the exploration strategy cannot be reproduced as specified.

- **Conceptual tension between pre-training invariance and the embedding-dynamics reward.** The contrastive encoder (§4.1) is trained to map structure-preserving perturbations of the same code to nearby embeddings — that is its design. The reward (Eq. 5) includes $\alpha\tanh(\beta\|\mathbf{h}_t - \mathbf{h}_{t-1}\|_2)$, which is *positive* and increases monotonically with embedding movement. If the encoder is working as designed, semantics-preserving refactorings (the goal) should produce small $\Delta h$, while large $\Delta h$ would signal the type of semantically-disruptive change the encoder was trained to distinguish. The paper motivates this term only in terms of numerical stability ("the hyperbolic tangent means that the gradients propagate in a stable way"), not semantics. The empirical correlation in Figure 2 (r=0.72) is the paper's only evidence that large $\Delta h$ actually indicates improvement — but Figure 2 itself is suspect (see Minor below), and the mechanism remains unexplained.

### Minor

- **Figure 2 x-axis contains negative L2-norm values.** The axis label corresponds to $\Delta h = \|\mathbf{h}_t - \mathbf{h}_{t-1}\|_2$, an L2 norm, which is definitionally non-negative. The scatter plot shows values from −1.0 to 1.0. Either the figure was generated from a quantity other than the one specified in Eq. 5, or the figure is incorrect. Because Figure 2 is the paper's primary empirical evidence that the embedding dynamics term is meaningful (Pearson r=0.72), an error in the figure construction materially weakens that claim.

- **$\delta_t$ is defined inconsistently between Eq. 5 and Eq. 8.** In §4.2, $\delta_t = \mathbb{I}[\text{test}(G_t) = \text{test}(G_{t-1})]$ — a binary indicator. In §4.5, Eq. 8 defines $\delta_t = 1 - \tfrac{1}{L}\sum_k \mathbb{I}[\cdot]$ — a continuous value in [0, 1]. The reward function (Eq. 5) uses $\gamma(1 - \delta_t)$: with the binary definition this penalty is 0 or γ; with the continuous definition it is graded. The two definitions are incompatible and are not reconciled.

- **Table 1 header "higher is better" is incorrect for Edit Distance.** The paper defines ED as "Normalized Levenshtein distance between original/refactored code." Lower Levenshtein distance means a smaller edit; the table bolds 0.36 (the *lowest* value) as the best result. If lower is better for ED, the table header is wrong. If higher is better, then the proposed method (0.36) under-performs Code2Seq (0.52) and Graph2Edit (0.49), contradicting the headline claim of "best across all metrics."

- **Figure 3 implies adaptive reward weighting, but no adaptive mechanism exists.** The stacked-area chart shows Code Quality Metrics shifting from 0.80 to 0.20 and Embedding Dynamics from 0.10 to 0.70 over 100 refactoring stages. The reward function (Eq. 5) uses fixed scalar weights ($\alpha = 0.2$, $\beta = 1.0$, $\gamma = 0.5$, $w_q$ fixed). No mechanism for dynamically adjusting these proportions is described anywhere in the paper. This shift may reflect the changing magnitudes of reward terms as training progresses, but the figure is presented without explanation, creating a misleading impression of the system's design.

- **SI metric uses PMD/Checkstyle violations as both the reward signal and the evaluation measure.** §5.1 defines SI as "percentage reduction in code smells (PMD/Checkstyle violations)," and Eq. 5 includes code quality metrics (which in context include style violations) as part of the reward. PMD and Checkstyle are also listed as baselines in Table 1. The RL agent is explicitly trained to minimize the quantity used to measure its success, inflating the apparent advantage over the rule-based tools that are not so trained.

### Trivial

- **Terminology inversion in §4.1:** The paper describes the augmentations as "syntax-preserving transformations" but subtree masking changes AST structure (syntax). The intended meaning is "semantics-preserving." The confusion propagates to the section title ("syntax-guided") which is used to mean something different from what the encoder is doing.

---

## Nice-to-Haves

- A directional reward term — rewarding movement *toward* a prototype embedding of known high-quality code (as hinted at by the $\mathbf{h}^*$ in Eq. 6) — would resolve the conceptual tension in §4.2 and make the pre-trained representation genuinely functional in the reward. The paper's own Eq. 6 and Figure 2 suggest this direction.
- Statistical significance reporting: with three datasets and five metrics, reporting variance or confidence intervals would strengthen all quantitative claims.
- Comparison with an instruction-tuned LLM baseline (e.g., prompted to refactor code) would ground the contribution relative to the current state of practice.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "Missing related works" criticism** — Removed per hard rule; no external sources are available to confirm existence of cited works.
- **Harsh critic: "Most often do last year" abstract phrasing** — Removed per hard rule on grammar/writing artifacts; not an author error for review purposes.
- **Strength Finder: "Method outperforms a broad set of baselines on all evaluation metrics" (Strength 4)** — Removed: directly contradicted by the ED metric direction error (Table 1) and the SP regression in cross-language evaluation (Table 3).
- **Strength Finder: "Framework generalizes across programming languages without fine-tuning" (Strength 3)** — Demoted and partially removed: contradicted by the pre-training language inconsistency (§5.1 vs §5.4) and the SP regression in Table 3. Kept only the narrow fact that SI is higher for Python and C++.
- **Strength Finder: "Composite reward function effectively links latent embedding dynamics to refactoring quality" and Figure 3 adaptive behavior** — Removed: Figure 3's dynamic shift is inconsistent with the fixed weights in Eq. 5 and is not explained; Figure 2 has the negative L2-norm axis issue. The r=0.72 correlation is retained as a weaker empirical observation.
- **Harsh critic: "No LLM-based baseline"** — Moved to Nice-to-Haves; absence of LLM comparison is not standard practice required in this subfield.
- **Harsh critic: "Training/test data overlap analysis"** — Moved to Nice-to-Haves; a reasonable concern but not verifiable from the paper.
- **Harsh critic: "No variance/significance reporting"** — Moved to Nice-to-Haves; single-run evaluation is common in systems-oriented refactoring papers.

---

## Novel Insights

The harsh critic's observation about the logical tension between the invariance objective in contrastive pre-training and the magnitude-of-movement reward term is the most insightful analytical point across both reviews. The pre-training loss pushes semantics-preserving augmentations together in embedding space, yet the reward positively reinforces large embedding displacements — which, under a well-trained invariant encoder, should correspond to semantic change rather than beneficial refactoring. This tension points toward a more principled design: using a *directional* reward (attraction toward a prototype of high-quality code) rather than an undirected magnitude reward. The paper's own Eq. 6 partially gestures at this, making $\mathbf{h}^*$ a running average of high-reward states, but never wires this concept into the reward function.

---

## Suggestions

1. **Resolve the pre-training language contradiction** (§5.1 vs. §5.4) before any cross-language result can be interpreted. Clearly state whether pre-training was multilingual or Java-only, and re-label Table 3 accordingly.
2. **Fix or relabel Figure 2:** If $\Delta h$ is not an L2 norm, state what it actually is. If it is an L2 norm, the x-axis must start at 0. The r=0.72 claim depends on this figure.
3. **Unify the definition of $\delta_t$:** Choose one definition (binary or continuous) and use it consistently in Eq. 5, §4.2, and §4.5.
4. **Fix Table 1 header for ED:** Either state that lower is better for ED (and remove the uniform "higher is better" label), or explicitly justify why higher ED is desirable in this setting.
5. **Specify the GraphRL system:** Describe exactly which method from the survey was implemented and how it was adapted to code refactoring.
6. **Explain Eq. 6:** Provide the mechanism by which a state-dependent scalar becomes a distribution over refactoring actions.
7. **Acknowledge the SP trade-off in Table 3** and discuss what it implies for the safety of cross-language deployment.
8. **Explain Figure 3:** Either describe the mechanism that produces dynamic reward-component proportions with fixed weights, or reframe the figure to make clear it reflects changing term magnitudes rather than changing weights.

---

## Score and Decision

**Originality:** The idea of combining contrastive graph pre-training with RL for code refactoring is a reasonable extension of existing techniques, but not a fundamental methodological advance. Score: 3/5.

**Importance of research question:** Automated code refactoring is an important problem, and reducing dependence on hand-crafted rewards is a meaningful goal. Score: 4/5.

**Claims supported:** Several headline claims are either internally inconsistent (cross-language "outperformance"), based on suspect figures (Figure 2 negative L2), or left mechanistically unexplained (Eq. 6, Figure 3). The ablation study is the most credible piece of evidence. Score: 2/5.

**Soundness:** Multiple specification-level errors (δ_t inconsistency, Eq. 6, Table 1 header, Figure 2 axis) and the pre-training data contradiction indicate the experimental pipeline was not rigorously constructed. Score: 2/5.

**Clarity:** Multiple instances of terminology inversion, unintelligible abstract phrasing, and figure/equation inconsistencies impair understanding. Score: 2/5.

**Value to research community:** The framing is relevant, and the ablation design is potentially useful as a template, but the current state of the work requires substantial revision before it is reliable enough to build on. Score: 2/5.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>2</clarity>
<community_value>2</community_value>
</subscores>