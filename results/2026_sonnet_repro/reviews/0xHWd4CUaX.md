Now let me run the calibration search to determine the appropriate score range.**Round 1 bracket: 2.5 – 4.5.** The paper has multiple genuine errors and inconsistencies, putting it below the borderline range (4.3–4.8) but having more content than the score-2.5 anchors. Let me narrow.Now I have enough context to write the authoritative final review.

---

## Summary

This paper proposes a reinforcement learning framework for automated code refactoring that integrates a contrastively pre-trained graph neural network encoder with a composite reward function combining code-quality metrics, latent-space movement, and a semantic-preservation penalty. The GNN policy is trained with PPO after a self-supervised contrastive pre-training phase on unlabeled code graphs. The central claim is that contrastive pre-training produces representations that meaningfully guide RL-based refactoring, enabling better syntactic improvement, semantic preservation, and cross-language transfer than prior RL and learning-based baselines.

---

## Strengths

- **Ablation study provides measurable evidence that contrastive pre-training matters.** Table 2 shows removing contrastive pre-training causes a drop from SI=83.7% to 76.2% (−7.5 pp) and from MG=27.9 to 22.4, while removing the semantic test component drops SP from 93.8% to 85.2% (−8.6 pp). These are concrete, quantitative results that demonstrate the two main components are each contributing something real.
- **Cross-language SI improvement is real and non-trivial.** Table 3 shows the Java-trained model achieves SI=68.7% on Python vs. PyLint's 59.2%, and SI=63.5% on C++ vs. Cppcheck's 54.3% — a genuine performance difference of ~9–10 pp across both languages without any fine-tuning.
- **Faster convergence relative to GraphRL.** Figure 1 shows the proposed method reaches 90% of maximum reward by episode 15k vs. 25k for GraphRL, representing a 40% reduction in sample complexity.

---

## Weaknesses

### Fatal

*None that are unambiguously verifiable as invalidating every result.*

### Major

**1. Reward function and pre-training objective are in direct tension; the paper offers no resolution.** Section 4.1 trains the encoder to be invariant to structure-preserving transformations (subtree masking, edge rewiring, identifier shuffling). Eq. 5 then positively rewards large `Δh_t = ‖h_t − h_{t-1}‖₂` via `α tanh(β Δh_t)`. If the encoder is working as designed, semantics-preserving refactorings (exactly what the RL agent should learn) would map to *small* Δh because the encoder was trained to be invariant to such transformations. Only transformations the encoder was trained to treat as *dissimilar* — i.e., potentially semantic-altering ones — should produce large Δh. The paper's only justification for this term is "the hyperbolic tangent means that the gradients propagate in a stable way during RL training" (Section 4.2), which addresses numerical stability, not the semantic tension. The ablation study (Table 2, "w/o embedding rewards") shows only a 4.2 pp drop in SI when this term is removed, compared to 7.5 pp for the contrastive pre-training itself, which is consistent with the embedding reward being a weak rather than decisive contribution — but the conceptual incoherence between the pre-training design and reward design is never acknowledged or resolved.

**2. Table 1 contains a metric-direction error on a headline metric.** The table header states "higher is better" universally. The proposed method's ED = 0.36 is the lowest value in the column, yet it is bolded as the best. Since ED is defined as "Normalized Levenshtein distance between original/refactored code" (Section 5.1), whether lower or higher is better is non-trivial and the paper never clarifies. If lower is better (a smaller, more surgical change), the table header is wrong; if higher is better (a more extensive rewrite), the bolding is wrong and the proposed method underperforms Code2Seq (0.52) and Graph2Edit (0.49). This affects the headline claim of "best across all metrics."

**3. Cross-language claims are overstated; Table 3 is incorrectly formatted.** The paper states the method "outperforms language-specific rule-based tools" (Section 5.4), and Table 3 bolds the Ours values as best across both SI and SP. However, PyLint achieves SP=90.4% vs. Ours SP=88.9% (Python), and Cppcheck achieves SP=93.1% vs. Ours SP=91.2% (C++). Semantic preservation is the safety-critical property in refactoring — the proposed method increases syntactic improvement but *decreases* semantic preservation compared to the rule-based tools in both languages. This trade-off is neither discussed nor acknowledged in the paper, and the boldface formatting misinforms the reader.

**4. Pre-training data description is internally contradictory, undermining the cross-language claim.** Section 5.1 states: "For pre-training the contrastive encoder, we used the CodeSearchNet corpus containing 2 million functions across **6 programming languages**." Section 5.4 states: "we evaluated the model already trained over a **Java language codebase** (CodeSearchNet)." These cannot both be accurate. If CodeSearchNet was used in full (6 languages including Python), the cross-language experiment is not zero-shot transfer. If only the Java subset was used, the experimental setup section is incorrect. The cross-language transfer claim in Section 5.4 depends entirely on which is true, and the paper does not resolve this.

**5. A primary RL baseline (GraphRL) is cited to a survey paper with no system description.** Section 5.1 lists "GraphRL (Darvari et al., 2024): GNN policy with expert demonstrations," and the references identify this as "Graph reinforcement learning for combinatorial optimization: A survey and unifying perspective" (arXiv:2404.06492). This is not a specific implemented system. The paper offers no description of what was actually run, how the survey's methods were adapted to code refactoring, or whether results were reproduced. GraphRL is the highest-performing RL baseline against which the proposed method claims a margin; the opacity of this comparison is a meaningful concern.

### Minor

**6. Figure 2 shows negative L2 norms.** The x-axis of Figure 2 is labeled "Embedding Dynamics (Δh)" and ranges from −1.00 to 1.00. The paper defines `Δh_t = ‖h_t − h_{t-1}‖₂` (Section 4.2), an L2 norm that is non-negative by definition. The scatter plot shows data in the negative half of the x-axis, which is mathematically impossible under the stated definition. Either the figure was generated using a different quantity than Eq. 5 specifies, or the figure is incorrect.

**7. Figure 3 implies adaptive reward weighting without any described mechanism.** The stacked area chart shows the proportion of reward components shifting from approximately (0.8/0.1/0.1) to (0.2/0.7/0.1) across 100 refactoring stages. The reward function (Eq. 5) has fixed scalar weights `α`, `β`, `γ`, `w_q`. There is no adaptive weighting mechanism described anywhere in the paper. The caption states "traditional metrics guide initial improvements, while embedding dynamics become increasingly important," implying an intentional curriculum — but no such curriculum exists in the method description.

**8. Eq. 6 does not define a distribution over actions.** Section 4.3 defines `π_explore(a|s) ∝ exp(−½(h_s − h*)ᵀΣ⁻¹(h_s − h*))` as a distribution over actions `a`. The right-hand side depends only on the state embedding `h_s` and contains no action variable. As written, this is a scalar (a single value for each state, not a distribution over the action space). The paper does not explain how this expression is used to select actions.

**9. δ_t is defined twice with conflicting formulas.** Section 4.2 defines `δ_t = I[test(G_t) = test(G_{t-1})]` (binary). Section 4.5 defines `δ_t = 1 − (1/L)Σ_k I[trace_k(G_{t-1}) ≠ trace_k(G_t)]` (continuous). The reward function (Eq. 5) uses the binary version from Section 4.2. These are distinct quantities, and the paper does not clarify whether the reward uses the binary or continuous formulation, nor does it acknowledge the conflict.

### Trivial

*(Removed — see below)*

---

## Nice-to-Haves

- An LLM-based code transformation baseline would strengthen the evaluation context, as instruction-tuned LLMs are a natural contemporary comparison for code refactoring. This is not expected in all venues but would improve the paper's relevance.
- The reward term `α tanh(β Δh_t)` could be redesigned as a *directional* signal (attraction toward a reference embedding of high-quality code) rather than a *magnitude* signal, which would actually connect the pre-trained representation to the RL objective coherently. Figure 2 already points toward the existence of a region in embedding space associated with high-quality code — using that as an attraction target rather than rewarding raw movement would address the core conceptual tension in the method.
- No variance or statistical significance is reported. With three datasets and multiple metrics, small absolute differences could be noise; reporting variance across runs would strengthen the quantitative claims.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic: "Subtree masking changes syntax, not semantics — terminology is backward."** Partially valid: the paper does say "syntax-preserving" when it means "semantics-preserving," and the section title "Syntax-Guided Contrastive Code Graph Encoder" is ambiguous. However, this is primarily a terminology inconsistency, not a substantive methodological flaw, and may partly be a parser artifact. Downgraded to Trivial, then removed since it doesn't affect results.
- **Harsh critic: "Abstract phrase is unintelligible."** Line 9 ("most often do last year because of the handcrafted nature of their metrics") is garbled, but per the hard rules, abstract formatting artifacts from parsing should not be penalized. Removed.
- **Harsh critic: "SI metric is circular because PMD/Checkstyle are both baselines and partly define the RL reward."** Partially valid — the RL reward includes "style violations" (Section 4.2), and SI is measured as reduction in PMD/Checkstyle violations. This creates a potential bias. However, code style metrics are standard proxies in this field, and the same metric affects all RL methods equally during evaluation. This isn't purely circular; it's a shared benchmark limitation rather than a unique flaw of the proposed method. Downgraded to Minor, then removed since it applies equally to all RL baselines.
- **Strength: "The framework outperforms a broad set of baselines on all evaluation metrics."** Conflicts with verified weaknesses #2 and #3 (metric direction error on ED, SP regression in cross-language results). Removed per filtering rules.
- **Strength: "Embedding-guided exploration yields faster policy convergence — reaching 90% by episode 15k vs 25k."** The GraphRL baseline citation quality undermines this comparison's reliability. Kept as a supporting strength with reduced confidence.
- **Harsh critic: "Missing LLM baseline, no train/test overlap analysis."** Legitimate observations moved to Nice-to-Haves per scope-creep rules. Not standard requirements in this community.

---

## Novel Insights

None beyond the paper's own contributions. The review's main finding is that the paper's *idea* — using contrastive pre-training to shape the RL reward landscape for code refactoring — is reasonable in concept, but the implementation has multiple internal inconsistencies (conflicting definitions of δ_t, Figure 2 with impossible values, Figure 3 implying unexplained dynamics, a contradictory pre-training data description) that collectively suggest the experimental artifacts were not carefully validated. The reward term rewarding embedding-space movement is in conceptual tension with the invariance objective of the pre-training, and the paper does not address this.

---

## Suggestions

1. **Resolve the pre-training language scope (Sections 5.1 vs. 5.4).** State clearly whether CodeSearchNet was used in full (6 languages) or Java-only, and adjust the cross-language experiment description accordingly.
2. **Fix Table 1 header or ED bolding.** Clarify whether lower or higher ED is desirable and correct the "higher is better" header or the bolded value.
3. **Correct Table 3 formatting.** Remove bold from SP values where the proposed method is inferior to the rule-based tool, and add explicit discussion of the SI–SP trade-off.
4. **Provide a description of the GraphRL implementation.** Since it's cited to a survey, describe precisely what system was implemented and evaluated.
5. **Fix Figure 2.** If Δh is computed as something other than the L2 norm, state the correct definition. If it is the L2 norm, the scatter plot's negative x-values are errors that need correction.
6. **Explain Figure 3.** If reward proportions shift dynamically, describe the mechanism. If Figure 3 was generated analytically rather than empirically, say so.
7. **Unify the δ_t definition.** Pick one formulation (binary or continuous) and use it consistently across Section 4.2, Eq. 5, and Section 4.5/Eq. 8.
8. **Fix Eq. 6.** Either introduce an action-dependent term or reframe the formula as a state bonus/exploration shaping term rather than a policy distribution.

---

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Human Score | Round | Comparison |
|---|---|---|---|
| N18Z2MkMEa (FALCON, code RL) | 3.00 | R1 | More experiments than paper under review, but similar methodological gaps; paper under review has more internal inconsistencies |
| 1MjOlHwCE6 (graph embedding) | 2.50 | R1 | Less topically similar; weaker contribution |
| d1zLRzhalF (KG + RL) | 2.50 | R1 | Incomplete baselines, less topically similar |
| HYsU5X4kE5 (GCNFT) | 3.00 | R1 | Reasonable contribution but limited novelty |
| DgGdQo3iIR (GEPCode, code GNN) | 4.33 | R1/R2 | Stronger and more coherent than paper under review |
| sEv6vHIUnu (GNN + RL representations) | 4.80 | R1 | More methodologically sound, better experiments |
| vLqkCvjHRD (RL for code with LLMs) | 4.75 | R1 | More careful experimental setup |
| hZztyfmr8n (COSTAR, contrastive + safe RL) | 3.00 | R2 | Similar combination (contrastive + RL) but fewer internal errors |
| APCjgjFy5M (VEP, contrastive pretraining + RL) | 3.50 | R2 | More coherent method design, fewer factual errors |
| LSrDaGWTnv (contrastive + planning) | 4.33 | R2 | Technically sounder, no figure/table errors |
| dbniI5RyWH (SEESAW, GNN) | 4.50 | R2 | Evaluation more careful, fewer internal contradictions |

**Round 1 bracket: 2.5–4.0.** The paper's multiple internal inconsistencies, figure errors, and specification gaps place it clearly below the borderline range (4.3–4.8) but above the nearly-empty papers (2.5).

**Round 2 narrowing:** Comparing to the round-2 anchors at 3.0–3.5: COSTAR (3.0) has limited baselines and presentation issues but no figure-level factual errors; VEP (3.5) is methodologically more coherent; the paper under review has more and more severe internal inconsistencies than both. It is comparable to FALCON (3.0): a reasonable topic with genuine experimental results, but multiple errors that undermine confidence in the experimental pipeline.

**Final score: 3.0 — Reject.** The paper addresses an interesting research question and its ablation study shows real evidence that contrastive pre-training contributes, but the number and severity of verifiable errors (impossible values in Figure 2, unexplained dynamics in Figure 3, conflicting δ_t definitions, metric direction ambiguity in Table 1, incorrect boldface in Table 3, internally contradictory pre-training data description, a baseline cited to a survey paper) collectively indicate the experimental pipeline was not carefully validated. The reward function's conceptual tension with the pre-training objective further undermines the paper's central claim. These issues require substantial revision before the work can be considered for acceptance.

**Axes summary:**
- *Originality*: Moderate — combining contrastive pre-training with RL for code refactoring is novel in framing, but the components are straightforward applications of existing methods.
- *Importance of research question*: High — automated code refactoring with quality guarantees is practically valuable.
- *Claims well-supported*: Low — multiple table and figure inconsistencies undermine trust in the results.
- *Soundness of experiments*: Low — metric-direction error, cross-language claim overstated, baseline implementation unclear, no variance reported.
- *Clarity of writing*: Low — contradictory descriptions across sections, undefined terms, inconsistent definitions.
- *Value to research community*: Moderate in potential but currently low as written.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>