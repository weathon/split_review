## Summary
This paper develops a theoretical framework for data curation in high-dimensional binary classification, deriving exact asymptotic test-error formulas under label-agnostic and label-aware pruning strategies via random matrix theory (RMT). The central result (Theorem 2) identifies generator quality (ρ) as the decisive factor: "keep hard" is optimal for strong generators in data-rich regimes, while "keep easy" is optimal for weak generators. The framework is validated on synthetic data (Figure 1), applied to ImageNet (Figure 2–3), and used to interpret contradictory LLM curation findings (Section 4.2).

---

## Strengths

- **Exact asymptotic test-error formula (Theorem 1, Eq. 9–11):** Derives a closed-form expression via RMT deterministic equivalents. The result is parameterized by a clean triplet (ρ, ρ*, ρ_g) that captures generator quality, oracle quality, and their alignment, providing genuine analytical tractability where prior work used only heuristic arguments.

- **Rigorous phase-transition condition (Theorem 2):** Establishes a precise, analytically verifiable boundary between "less is more" (strong generator, large n, ρ→1) and "more is more" (weak generator or small n, ρ<1). The result is not merely a qualitative claim but identifies the unique optimizers of F(q) over the full space of symmetric pruning strategies Q_p.

- **Controlled synthetic validation (Figure 1):** The 2×2 grid of simulations cleanly maps onto the four theoretical cases. Solid theoretical curves closely track the dashed empirical curves in all four quadrants, with the "less is more" optimum appearing only in the bottom-left (large-n, strong-generator) quadrant precisely as Theorem 2 predicts. This is genuinely strong evidence for the theory's accuracy.

- **Extension to label-aware curation (Theorem 3, Section 3.2):** Generalizes the test-error formula to oracles that jointly filter by label correctness and difficulty (Eq. 6), directly modeling the curation rules used by LIMO and s1. The unification of label-agnostic and label-aware curation under a single formula with modified constants (Eq. 13) is elegant.

- **Scale-dependent crossover on ImageNet (Figure 2):** Demonstrates that a pre-trained ViT acting as generator and pruner exhibits the predicted shift from "keep easy" (160K training examples) to "keep hard" (1.2M training examples), providing directional support for the theory on a realistic vision task.

- **Model collapse stabilization (Figure 3):** Iterative pseudo-labeling without curation causes error to rise from ~30% to ~52% over 6 rounds; "keep hard valid" selection holds error near 30%, matching ground-truth performance. This is a concrete empirical demonstration of practical relevance.

---

## Weaknesses

### Fatal
None.

### Major

- **Apparent tension between Theorem 2B and the model collapse experiment (Figure 3) is unaddressed.** Theorem 2B states that for a *weak* generator (ρ < 1), "keep easy" is the uniquely optimal strategy — and the paper itself, immediately after Theorem 2, explicitly links Part (B) to model collapse: "This latter case is particularly relevant for mitigating model collapse, where a model trained on its own imperfect outputs acts as a poor generator." Yet Figure 3 uses *"keep hard valid examples"* (label-aware, Eq. 6) and shows this *prevents* collapse. Theorem 2 governs label-agnostic curation (Eq. 5), while Figure 3 uses label-aware curation (Eq. 6) covered by Theorem 3 — so there is no strict logical contradiction. However, the paper never explains this resolution. A reader following the discussion of Part (B) through to Figure 3 will see what looks like a direct refutation of the theory's own recommended strategy. The paper should: (a) clarify that Figure 3 operates under Theorem 3 (label-aware), not Theorem 2 (label-agnostic); and (b) provide the relevant corollary from Theorem 3 showing that "keep hard valid" is indeed optimal in the model collapse regime (high label-verification quality, combined difficulty filter). This is an important gap in a paper whose stated contribution includes proving that "data curation can avert model collapse."

- **The LLM interpretation (Section 4.2) is post-hoc and described in the abstract as stronger than it is.** The framework is used to explain Tables 1–2: "average AIME → strong generator → keep hard works; hardest AIME → weak generator → more is more." But the assignment of ρ ("strong" vs. "weak") is inferred retroactively from the experimental outcome it is supposed to explain. No value of ρ is measured or estimated for any LLM; no prediction is made prior to observing the outcome; no threshold ρ* or ρ_g is computed. This makes the LLM connection a consistent narrative rather than a falsifiable test. The abstract claims "providing a rigorous justification for why methods like LIMO and s1 succeed" — this is a direct overclaim. The accurate characterization would be "providing a theoretical framework consistent with / that naturally interprets these results." The distinction matters because reviewers and readers will rightly ask: what quantitative foothold does the theory have here? The answer currently is: none.

### Minor

- **ImageNet validation is qualitative, not quantitative.** Section 4.3 shows directional consistency (crossover between "keep easy" and "keep hard" as n increases) but does not overlay theoretical curves. The abstract states "we validate these theoretical claims with empirical results on ImageNet," but "validate" implies quantitative agreement between formula and measurement, which is only demonstrated in Figure 1 (synthetic). On ImageNet, the ρ, ρ*, ρ_g parameters are not estimated, and no predicted crossover point from the formula is compared against the observed crossover. This should be characterized as "confirming the directional predictions" rather than full validation.

- **Theorem 2 is proved in the data-rich, unregularized limit (φ → 0, λ → 0), but most of Figure 1 operates in the finite-sample regime.** The theorem correctly identifies the asymptotic optimum, but the paper does not discuss how reliably the φ → 0 prediction guides finite-n behavior. For instance, in the top-left quadrant (small n, strong generator), the theory predicts p = 1 is optimal, and so does the simulation — but it would help practitioners to know how n must scale before the "less is more" prediction from the bottom-left becomes reliable.

### Trivial

- The paper uses "exact scaling laws" throughout (abstract, Section 1, contributions), which in RMT-in-ML usage denotes exact asymptotic test-error formulas in the proportionate limit d/n → φ. This diverges from "scaling laws" as used in the LLM literature the paper invokes (Kaplan et al., 2020; Hoffmann et al., 2022), where the term means power-law relationships between loss and n as n → ∞ with d fixed. The terminological mismatch is not catastrophic but contributes to a slight inflation of the connection to LLM phenomena.

---

## Nice-to-Haves

- **Quantitative foothold for the LLM section:** Even a rough proxy estimate of the base LLM's generator quality ρ for "average" vs. "hardest" AIME questions (e.g., pass rate on held-out easy vs. hard problems as a surrogate) would transform Section 4.2 from a post-hoc narrative into at least a weakly testable prediction. This would substantially strengthen the paper's claim to explain LIMO/s1.

- **Explicit corollary for the model collapse regime under label-aware curation:** Since model collapse is one of the paper's four stated contributions, a brief corollary from Theorem 3 giving conditions under which "keep hard valid" is optimal would close the gap between the theory and Figure 3 and remove the apparent tension with Theorem 2B.

- **Qualitative discussion of covariate shift effects:** Section 2.1 introduces covariate shift (C_g ≠ Σ) as part of the problem, but the main text restricts to C_g = Σ = I_d. A brief remark on what qualitatively changes (or does not) in the presence of covariate shift would help readers assess the scope of the isotropic results.

---

## Removed Points

*These points were flagged for removal; treat with caution.*

- **Strength Finder — "principled explanation of contradictory LLM curation results" as a core strength:** Retained as a minor strength (the framework does provide a natural interpretive lens), but the framing "principled explanation" is weakened because the assignment of ρ is post-hoc. Moved to consistency of interpretation rather than predictive validation.

- **Harsh Critic — claim that the model collapse experiment "contradicts Theorem 2" in a fatal way:** Demoted from fatal/major-as-stated because Theorem 2 governs label-agnostic curation (Eq. 5) and Figure 3 uses label-aware curation (Eq. 6) covered by Theorem 3. There is no strict logical contradiction, only a presentation gap. Retained as Major weakness but reframed as a clarity/reconciliation issue.

- **Harsh Critic — request for quantitative theoretical curves overlaid on ImageNet:** Retained as Minor only. Estimating ρ for a ViT on ImageNet under the Gaussian linear model assumptions is genuinely non-trivial; demanding full quantitative overlay is somewhat outside the scope of a theory paper that frames ImageNet as directional corroboration.

---

## Novel Insights

The paper's most novel insight is the precise parameterization of data curation quality through the triplet (ρ, ρ*, ρ_g) and the demonstration that these three geometric angles — generator-to-truth, oracle-to-truth, and oracle-to-generator — *fully determine* the optimal pruning strategy in the large-data limit. This provides a conceptually clean resolution to the "less is more" vs. "more is more" debate: neither is universally correct; the boundary is a precise phase transition in (ρ, n) space. The extension to label-aware curation (Theorem 3) and the connection to model collapse via iterative pseudo-labeling represent concrete advances over prior theoretical work (Firdoussi et al., 2024; Feng et al., 2025), which treated correctness filtering without the difficulty dimension. The unification of these two curation axes under a single analytical formula is the paper's most original contribution.

---

## Suggestions

1. **Resolve the Theorem 2B / Figure 3 tension explicitly.** Add a brief paragraph in Section 4.3 or Section 3.2 stating: (a) Figure 3 uses label-aware curation (Theorem 3), not label-agnostic (Theorem 2); and (b) provide the relevant special case of Theorem 3 showing when "keep hard valid" dominates in the model collapse regime. This requires no new theory — only unpacking what Theorem 3 implies.

2. **Recalibrate the abstract's contribution bullet 3.** Change "providing a rigorous justification for why methods like LIMO and s1 succeed" to "providing a principled theoretical framework consistent with / that naturally explains the contradictory curation results observed in LIMO and s1." This is more accurate and less vulnerable to criticism.

3. **Clarify the scope of Theorem 2 in terms of when the φ → 0 limit is a reliable guide.** A brief discussion of how large n must be (relative to d) for the "less is more" regime to activate in practice would help practitioners.

4. **Separate "validation" language for ImageNet from synthetic.** In the abstract and Section 4.3, replace "validate" with "confirm the directional predictions of" when referring to the ImageNet results, reserving "validate" for Figure 1 where theoretical curves are explicitly compared against simulation.

---

## Score and Decision

**Originality:** The exact RMT characterization of pruning strategies, especially the joint treatment of generator quality and oracle quality, is a genuinely novel theoretical contribution. The combination of label-agnostic and label-aware curation in a single framework extending prior work (Firdoussi et al., Feng et al.) is original. **(4/5)**

**Importance of Research Question:** Data curation efficiency is directly relevant to large-scale model training, and the "less is more" vs. "more is more" question is timely given LIMO/s1/s1-style results. **(4/5)**

**Claims Supported:** The core theoretical claims (Theorems 1–3) are supported by the synthetic experiments. The ImageNet claims are supported directionally. The LLM claims are overclaimed as "rigorous justification" when they are interpretive. **(3/5)**

**Soundness of Experiments:** Synthetic experiments are well-designed with theory curves overlaid (Figure 1). ImageNet experiments are directionally sound. The model collapse experiment is concrete and interesting. Minor concern about the Theorem 2B / Figure 3 reconciliation. **(3.5/5)**

**Clarity of Writing:** Generally clear and well-organized. The main gap is the unaddressed tension between Theorem 2B and Figure 3, which could confuse attentive readers. **(3.5/5)**

**Value to Research Community:** Provides practitioners with an analytical framework to determine optimal curation strategy given generator and oracle quality. Connects abstract RMT results to practical phenomena (model collapse, LIMO). **(4/5)**

The paper makes a genuine theoretical contribution — exact asymptotic characterization of data pruning strategies in high-dimensional learning — that is carefully derived, cleanly parameterized, and well-validated in the synthetic setting. The two main weaknesses (LLM overclaiming and model collapse reconciliation) are presentation and framing issues that do not invalidate the theory. With revisions to reframe the LLM section and explicitly connect Figure 3 to Theorem 3, this is a solid acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>