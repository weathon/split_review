## Summary

WithAnyone is a triple-contribution paper addressing "copy-paste" artifacts in identity-consistent image generation, where models replicate the reference face rather than preserving identity across natural variations. The authors (1) construct MultiID-2M, a 500k-group-photo paired dataset with per-identity reference banks; (2) introduce MultiID-Bench with a novel Copy-Paste metric M_CP and Sim(GT)-based evaluation; and (3) propose a generation model trained with GT-aligned ID loss, InfoNCE with an extended 4096-negative pool, and a paired-tuning phase that breaks the identity-fidelity/copy-paste trade-off demonstrated across 12 baselines.

---

## Strengths

- **Copy-paste failure mode formalized**: The paper precisely articulates why reconstruction-only training creates copy-paste artifacts and formalizes this as M_CP (Eq. 2). The distinction between Sim(GT) and Sim(Ref) as evaluation targets is the paper's most durable conceptual contribution — Sim(Ref) inadvertently rewards trivial copying, while Sim(GT) measures whether the generation corresponds to the prompted scene. This distinction is likely to influence how subsequent work evaluates ID-consistency.

- **MultiID-2M dataset enables a qualitatively new training regime**: The 500k labeled group photos with per-identity reference banks of hundreds of images across diverse poses and expressions directly enable Phase 3 (paired tuning), which the ablation (Table 3) confirms reduces CP from 0.239 to 0.161 without harming Sim(GT). The 1.5M additional unpaired images further support reconstruction pre-training.

- **GT-aligned ID loss is a concrete technical contribution**: Rather than extracting unreliable landmarks from noisy diffusion intermediates, the method uses GT landmarks to align generated faces before ArcFace extraction (Section 5.1, Eq. 4). Figure 7 shows the GT-aligned ID loss achieves lower identity loss across noise levels compared to naive landmark extraction. The ablation confirms this (Table 3, "w/o GT-Align": Sim(GT) drops from 0.405 to 0.385).

- **InfoNCE with extended negatives is validated**: The ablation (Table 3, "w/o Ext. Neg.") shows that reducing from 4096 negatives to 63 (in-batch only) significantly degrades both Sim(GT) (0.405 → 0.368) and Sim(Ref) (0.551 → 0.455), confirming that the labeled reference bank is practically essential.

- **Strong quantitative separation from baselines**: In the single-person subset (Table 1), WithAnyone achieves Sim(GT) = 0.460 — matching InstantID which leads the face-specific models (0.464) — while cutting CP to 0.144, far below InstantID's 0.337. Figure 5 shows all other methods follow a fitted trade-off curve; WithAnyone is the sole outlier in the upper-left region, confirming it breaks rather than merely shifts the trade-off.

- **Qualitative controllability demonstrated**: Figure 6 illustrates that identity-specific baselines fail to generate prompted expressions (e.g., smiling, gaze change) while WithAnyone does — directly validating the claim that copy-paste reduction restores controllability.

---

## Weaknesses

### Fatal
None.

### Major

- **Sim(GT) partially conflates identity preservation with text-conditioned pose/expression generation.** Because the benchmark prompts are extracted from the ground-truth image (Section 4), a GT photograph already shows the person in the exact pose and expression described. A model that follows text prompts well will land closer to the GT in pose/expression, boosting Sim(GT) independently of true identity fidelity. The ablation is informative here: removing Phase 3 ("w/o Phase 3") gives Sim(GT) = 0.406 vs. the full model's 0.405 — a difference of 0.001 — while CP increases sharply (0.161 → 0.239). This reveals that Phase 3's primary effect is suppressing copy-paste, not improving identity similarity. Yet the paper presents Sim(GT) gains in Table 1 over baselines partly as evidence of identity fidelity improvement. The claim "maintains state-of-the-art identity similarity while substantially reducing copy-paste" is accurate, but the implicit framing that Sim(GT) improvement = better identity fidelity is imprecise and should be qualified. A decomposition of Sim(GT) gains by case type (posed vs. neutral prompts) would clarify this.

### Minor

- **The identity blending (BU) metric is used in Table 2 results but not defined in the main text.** Section 4 lists it among "additional metrics" with only a name. Since multi-person identity blending is a distinctive failure mode in multi-ID generation and the paper is partly a benchmark paper, all primary evaluation metrics should have at least a one-sentence formal definition in the body.

- **M_CP behavior near degenerate cases is uncharacterized.** When reference and GT embeddings are very similar (θ_tr ≈ 0), the ε stabilizer in the denominator of Eq. 2 dominates and M_CP becomes noisy. The filtering criterion "Sim(GT) > 0.40" for CP ranking is mentioned but is ad hoc, with no sensitivity analysis to the threshold choice. A distribution of θ_tr in the benchmark and a brief sensitivity analysis would strengthen the benchmark's credibility.

- **Multi-ID results show a weaker version of the trade-off break.** Table 2 (3–4 people subset): DreamID achieves CP = 0.116 vs. WithAnyone's 0.171, at the cost of Sim(GT) = 0.311 vs. 0.414. The "upper-right corner" claim is clear and decisive for single-ID (Table 1, Figure 5) but less decisive in multi-ID settings. The paper's central claim should be scoped accordingly.

- **General multimodal models dominate on OmniContext.** GPT-4o (8.12), OmniGen2 (8.34), and FLUX.1 Kontext (7.94) all outperform WithAnyone (6.52) on general prompt-fidelity evaluation. The paper acknowledges this briefly but does not discuss whether it signals a convergence of the "face customization" specialty with general-purpose generation — a limitation worth noting explicitly.

### Trivial

- **User study with 10 participants.** The study covers 230 image groups, which is a reasonable scope, but 10 evaluators is small. The study is supportive but insufficient for strong statistical claims. A sample size and basic significance measure (e.g., Kendall's τ with M_CP rankings) should appear in the main text rather than being deferred entirely to the appendix.

---

## Nice-to-Haves

- A controlled decomposition of Sim(GT) gains by prompt type (prompts specifying expression/pose changes vs. neutral prompts) would directly address the identity-fidelity vs. prompt-following conflation and would strengthen the paper's core thesis without requiring new data.
- Analysis of M_CP as a function of θ_tr (the reference–GT angular distance) across the benchmark would reveal whether WithAnyone's advantage concentrates on large-variation cases, which would be the theoretically expected behavior and would validate the metric design.
- A one-paragraph summary of the overlap verification procedure (training vs. benchmark identities) in the main text would make a load-bearing result verifiable without consulting an appendix.

---

## Removed Points

*These points were flagged for removal — treat them with caution.*

1. **"Circular validation loop" as a structural flaw (Harsh Critic, Issue 1):** The critic characterizes the co-design of Phase 3 and M_CP as a validation loop that may overstate results. While the evidential concern is real and retained as a major weakness, the critic's conclusion that this constitutes a structural flaw requiring "independently curated benchmark by a third party" is too strong. The OmniContext results (Table 1b) and the scatter plot (Figure 5) involving 12 baselines not designed with M_CP in mind provide meaningful external validation. Demoted from structural to a framing concern under Major.

2. **Training/benchmark overlap verification deferred to appendix:** The critic notes this is in Appendix C without a main-text summary. Per the hard rules, missing appendix content cannot be penalized — the appendix exists in the original submission.

3. **"Not yet released / cannot be independently verified" category (pre-empted by hard rules):** No such criticisms appeared, but the blanket rule applies to all cited baselines including GPT-4o-Image, OmniGen2, FLUX.1 Kontext, etc.

4. **Open-source release as a strength (Strength Finder):** Removed as generic — releasing code/data is a good practice but is not a scientific contribution distinguishing this paper.

5. **General strengths about problem importance:** The Strength Finder notes "this addresses an important focus in text-to-image research." Removed as generic; the retained strength about copy-paste formalization is the specific, grounded version.

---

## Novel Insights

The paper's most distinctive contribution is the conceptual reframing of what "good" identity-consistent generation means: not maximizing Sim(Ref) but achieving Sim(GT) — faithfully realizing a prompted scene with the correct identity, rather than replicating the reference pixel-by-pixel. This distinction, once stated, seems obvious, but no prior benchmark made it explicit, and the evaluation community's reliance on Sim(Ref) had the perverse effect of rewarding the copy-paste failure mode. The MultiID-Bench design concretizes this insight into a testable benchmark, and the ablation (Table 3) empirically confirms that prior training regimes and metric choices jointly create an optimization pressure toward artifact-inducing behavior. The paper's secondary insight — that a large labeled paired dataset enables an InfoNCE loss with thousands of negatives, which substantially improves contrastive identity separation — is theoretically expected but empirically validated cleanly.

---

## Suggestions

1. Add a one-sentence formal definition of the identity blending (BU) metric in Section 4, even if details are in the appendix.
2. Add a brief decomposition of Sim(GT) improvement by prompt type (expression/pose-changing prompts vs. neutral prompts) to disentangle identity fidelity from prompt-following gains.
3. Report the user study sample size and a single significance measure (Kendall's τ or inter-rater agreement) in the main text.
4. Include a brief sensitivity analysis of the Sim(GT) > 0.40 filtering threshold in Table 1/2 or acknowledge it explicitly as a parameter that may affect rankings.
5. Soften the abstract framing from "improves identity similarity" to "maintains state-of-the-art identity similarity while substantially reducing copy-paste," which is what the ablation actually shows.

---

**Evaluation on Key Axes:**

- **Originality:** High. The Sim(GT) vs. Sim(Ref) distinction and the M_CP benchmark metric are genuinely novel and practically impactful.
- **Importance:** High. Copy-paste is a real, widespread failure mode in identity-consistent generation; the work addresses a practical gap with reusable artifacts.
- **Claims well-supported:** Mostly. Core claims (trade-off break in single-ID, ablation validation of all components) are well-supported. Some imprecision in how Sim(GT) improvement is attributed to identity fidelity specifically.
- **Soundness of experiments:** Good. Twelve baselines, ablation of all major components, multi-person and single-person subsets, user study. The metric design has some uncharacterized edge cases.
- **Clarity:** Good. All key equations are present and motivated; the training pipeline is clearly described.
- **Value to research community:** High. The dataset, benchmark, and model are all open-sourced; the benchmark design will likely be adopted by follow-on work.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>