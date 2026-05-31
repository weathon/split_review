Now I have everything I need to produce the final consolidated review. Let me write it.

## Summary

This paper introduces a taxonomy of label-domain mismatch scenarios in class-wise machine unlearning — target mismatch, model mismatch, and data mismatch — that arise when the class label and the target concept are decoupled. The authors propose TARF (TARget-aware Forgetting), a three-phase framework combining annealed gradient ascent on forgetting data with target-aware gradient descent on hard-to-affect retaining data. Experiments on CIFAR-10/100, ImageNet-1k, and real-world applications (Stable Diffusion concept removal, TOFU LLM unlearning) show TARF consistently achieves the lowest Gap to retrained models across all settings, with particularly dramatic improvements in target mismatch (Gap 0.21 vs. 8.86 for the best baseline on CIFAR-100).

## Strengths

1. **Systematic formalization of three new mismatch scenarios.** The paper defines explicit relations among label domains (ℒ_D, ℒ_M, ℒ_T) and provides clear data partitions (Table 1, Figure 1) for target mismatch, model mismatch, and data mismatch. This taxonomizes important practical settings — e.g., a user reports a few examples of an unwanted concept (data mismatch), or the requested concept spans multiple training classes (target mismatch) — that prior unlearning work assumed away with ℒ_D = ℒ_T = ℒ_M.

2. **Theoretical connection between representation geometry and forgetting dynamics.** Theorem 3.2 derives an upper bound showing that the loss difference between two subsets during gradient ascent is proportional to their representation distance d_h(x₁, x₂). This analysis directly explains why existing methods fail under mismatch (Remarks 3.1–3.3) and motivates the "representation gravity" concept for target identification. The t-SNE visualizations in Figure 3 empirically corroborate the theory.

3. **Significant quantitative improvements on mismatch tasks.** On CIFAR-100, TARF achieves Gap scores of 1.21 (model mismatch), 0.21 (target mismatch), and 1.17 (data mismatch), compared to the best baseline (GA) at 3.01, 8.86, and 2.43 respectively (Table 3). The 40× reduction in target mismatch Gap validates that TARF's target identification and separation mechanism effectively handles the decoupled concept setting that breaks existing methods.

4. **Scalability to ImageNet-1k and real-world applications.** TARF achieves the lowest Gap in all four settings on ImageNet-1k (Table 4) with competitive runtime. The paper also demonstrates TARF's generality beyond image classification: concept removal with Stable Diffusion (Figure 6) and personal information removal with LLaMA on TOFU (Table 5), showing the mismatch framework transfers to generative models and LLMs.

5. **Principled ablations of framework components.** Figure 7 systematically ablates the annealed forgetting coefficient k(t), the gradient ascent schedule (constant/increasing/decreasing), and the operation on selected retaining data, providing empirical justification for each design choice.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation gap: no direct measurement of whether the target concept is forgotten in target/data mismatch.** The paper's formal objective (Eq. 1) is to approximate retraining on 𝒟\𝒟_f, and this is what the Gap metric evaluates. However, in target and data mismatch, 𝒟\𝒟_f still contains 𝒟_fr (false retaining data — instances of the target concept not in the given forgetting set). The paper reports UA (accuracy on 𝒟_f) and RA (accuracy on the full remaining set), but never separately reports accuracy on 𝒟_fr. Without this, a reader cannot directly assess whether TARF truly forgets the target concept (which should lower accuracy on 𝒟_fr) or simply performs standard deletion of 𝒟_f while leaving the concept intact. The paper already provides this fine-grained breakdown for model mismatch (Table 2: UA-F and UA-R columns), and the analogous evaluation for target/data mismatch is conspicuously absent. This gap weakens the support for the paper's strongest conceptual claim.

2. **Strong assumption of known target-concept class count.** Section 2 states: "we assume that the number of classes in 𝒟_un belonging to the target concept is known in target mismatch forgetting." This is used to set the threshold β for identifying false retaining classes (Phase I). While the paper mentions weakly-supervised exploration in the appendix, the core evaluation relies on this privileged information. The assumption is not relaxed in main experiments, and it is unclear how β would be set in practice when the target concept's class membership is unknown.

3. **Tension between conceptual framing and evaluation framework.** The paper's language ("forget the target concept," "actively forget the target concept while maintaining the rest part") suggests the goal is to remove the entire target concept (i.e., 𝒟_t). However, the formal objective (Eq. 1) and the primary evaluation metric (Gap to a model retrained on 𝒟\𝒟_f) target a different quantity — removing only 𝒟_f. Since the Retrained reference still captures the target concept through 𝒟_fr, a method that actually expunges the concept would deviate from this reference by design and be penalized by the Gap metric. The paper would benefit from either (a) adding a concept-level retrained baseline (𝒟\𝒟_t) as a secondary reference, or (b) explicitly arguing why approximating 𝒟\𝒟_f retraining is a suitable proxy for concept forgetting, supported by evidence on 𝒟_fr accuracy.

### Minor

1. **Target identification relies on class-level separability of accuracy drops.** Phase I identifies false retaining classes by detecting which classes experience significant accuracy drops during gradient ascent on 𝒟_f. This works when the target concept aligns neatly with a subset of classes (as in the CIFAR superclass structure), but may not generalize when the target concept is distributed across many classes, aligns poorly with the model's class structure, or involves multi-attribute concepts. The paper acknowledges this in the conclusion ("gravity signal becomes weaker") but does not experimentally probe the limits of this assumption.

2. **No ablation separating the three phases' independent contributions.** The paper describes three sequential phases (identification, separation, approximation) but does not ablate what happens if Phase II is run alone without III, or if Phase I's identification is replaced with random class selection. Such ablations would clarify which component drives the improvement.

### Trivial
None.

## Nice-to-Haves
- A comparison against a retrained model on 𝒟\𝒟_t (concept-level removal) as an additional reference point for target/data mismatch.
- A controlled experiment with an intentionally ambiguous target concept that does not align well with existing classes, to map where TARF's limits lie.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic claim about "computational cost of Phase I not quantified"** — The paper states computational cost is analyzed in Appendix E.2, which is stripped by the parser. Cannot verify from available text.
- **Criticism about missing related works** — Per rules, I cannot comment on missing references.
- **Formatting/style nitpicks** (Table size, subscripts, appendix length complaints from human reviewer 3) — Parser artifacts or style issues not relevant to scientific merit.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem," "well-written") — Dropped for lacking concrete, paper-specific anchoring.
- **Strength Finder's claim about "principled ablation" without connection to specific evidence** — Kept in modified form above with concrete references to Figure 7 panels.
- **Criticism about "problems appear a bit artificial"** (human reviewer 3) — The paper provides real-world motivation in Section 1 (privacy, copyright, hazardous capabilities) and demonstrates real-world applications (Stable Diffusion, TOFU/LLaMA). The CIFAR setting is a controlled testbed, which is standard practice.

## Novel Insights

The reviews surface an interesting structural tension that the paper itself does not fully resolve: when the target concept spans more data than the user-provided forgetting set, what is the correct gold standard for unlearning? The paper adopts the conventional answer (𝒟\𝒟_f retraining), but the harsh critic correctly observes that this is at odds with the conceptual goal of "forgetting the concept." This tension is not unique to this paper — it reflects an under-explored question in the unlearning literature about whether the desired outcome is behavioral (model output no longer reflects the concept) or data-level (model behaves as if the concept's data were never seen). The paper's taxonomy of mismatch scenarios makes this tension more visible than prior work, and the evaluation gap it creates is informative for the community even as it weakens the present empirical support.

## Suggestions

1. **Report accuracy on 𝒟_fr (false retaining data) for target and data mismatch** in the main paper or appendix. This is the single most impactful addition: it directly measures whether the target concept is forgotten. The precedent exists in Table 2 for model mismatch.

2. **Add a concept-level retrained baseline (𝒟\𝒟_t)** for target and data mismatch as a secondary reference. Even if the primary metric remains Gap to 𝒟\𝒟_f, the 𝒟\𝒟_t reference would clarify what complete concept removal looks like.

3. **Relax the known-class-count assumption** in at least one experiment by using a threshold-based or rank-based class selection without the count prior, and report the resulting performance drop (if any). This would substantially strengthen claims of practical applicability.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>