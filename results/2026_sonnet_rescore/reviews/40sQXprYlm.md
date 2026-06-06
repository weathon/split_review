## Summary

This paper introduces Distributed Neural Architectures (DNA), where each token independently follows its own content-dependent path through an unordered collection of shared computational modules, with routing learned end-to-end via standard cross-entropy. The paper frames itself explicitly as a feasibility demonstration rather than a SOTA attack, presenting ImageNet-scale vision models and GPT-2-scale language models. Key claims are: (i) DNAs are competitive with dense baselines; (ii) compute efficiency can be learned without auxiliary load-balancing losses; (iii) trained routing patterns are human-interpretable and exhibit emergent specialization.

---

## Strengths

1. **Top-2 DNA language model genuinely outperforms GPT-2 medium at matched active parameters.** Table 3 shows top-2 DNA (433M active) achieving validation loss 2.674 vs. GPT-2's 2.720, along with improvements on ARC-E (59.2 vs. 58.9), BoolQ (61.0 vs. 60.5), HellaSwag (41.8 vs. 40.5), LAMBADA (34.0 vs. 33.8), PIQA (67.9 vs. 66.9), and Wikitext (31.5 vs. 33.7). This establishes genuine feasibility of the routing framework.

2. **Interpretable emergent routing is concretely demonstrated in both domains.** In vision, path rank correlates with abstraction level: rank-5 paths aggregate edge patches, rank-15 flat-color patches, and rare paths (rank-775, rank-941) capture domain-specific objects like brass instruments and puzzle pieces (Fig. 3). Deep-dream reconstructions in Fig. 4 show hierarchical feature development from texture/edges (steps 1–3) to object-level structure (steps 7–10). In language, router R₁ consistently sends verb forms to M₀, punctuation to M₂₇, and word-pieces to M₂₉ across independent text examples (Section 4.2, Fig. 8). These are concrete, replicated observations.

3. **Interpretable compute allocation in vision.** The top-2 skip DNA allocates more compute to images with intricate boundaries (flatworm, pretzel) and less to visually simple images (loudspeaker, theater curtain), as shown in Fig. 5 with a histogram of per-image normalized compute and representative examples. This demonstrates that compute savings are content-driven, not random.

---

## Weaknesses

### Fatal
None.

### Major

1. **The skip-model efficiency claim is not supported by Table 3, and this goes unacknowledged.** The paper's headline claim that DNAs "can learn to use less compute with minor effects on performance" is tested by the "top-2 (30% skip)" model in Table 3. This model's validation loss (2.784) is *worse* than the simplest possible efficiency baseline: a "GPT-2 (30% shallower)" dense model (2.772). The gap extends to every single downstream benchmark — the skip DNA trails the shallower GPT-2 on ARC-E (52.5 vs. 58.0), BoolQ (52.9 vs. 54.9), HellaSwag (35.5 vs. 37.9), LAMBADA (23.8 vs. 31.4), PIQA (64.2 vs. 65.9), RACE (28.1 vs. 30.1), and Wikitext (52.6 vs. 38.0). The paper presents these numbers in Table 3 without a single word of analysis. Since learned compute allocation is one of three headline contributions, the failure of the skip model to beat the trivial baseline is a result that needs to be addressed, not silently tabulated.

2. **Total parameter asymmetry undermines the "competitive" claim for both domains.** In vision, the top-1 DNA (34M total, 22M active) is compared against ViT-small (22M total, 22M active) — 55% more total parameters for comparable performance. In language, the top-2 DNA (603M total, 433M active) outperforms GPT-2 medium (406M total, 406M active), but at 50% more total parameters and slightly more active parameters. The paper describes the active-parameter comparison as the relevant one, but total parameter count provides additional capacity (larger embedding space, more parameters available for routing, more potential parameter-sharing combinations) that is not accounted for. This asymmetry is nowhere acknowledged, and "competitive" as framed implies approximate equivalence that the numbers do not fully support.

3. **The power-law path-distribution finding is largely undermined by the paper's own observation.** The paper presents in Figures 1c–d the power-law distribution of token paths as a structural finding. However, the caption of Figure 1 explicitly states: "Surprisingly, the distribution of paths through the *random* model also follows power-law with exponent −1." For vision, the trained model's exponent is also −1, identical to the random model. For language, the trained model's exponent is −1.2 vs. −1 for random, but this difference is not analyzed. If a randomly initialized, untrained model already produces a power-law distribution with the same exponent, the distribution is a structural property of the routing topology's combinatorics, not something learned. The paper acknowledges this as "surprising" but does not resolve it, leaving the primary quantitative finding of Section 1 on uncertain footing.

### Minor

1. **Specialization evidence is qualitative and lacks quantitative comparison to random routing.** Section 3.2 notes that a randomly initialized model "can also cluster images… based on superficial features" (and mentions Appendix G.2). This is the right instinct, but the analysis stops without any metric (e.g., within-path vs. between-path feature similarity ratio for trained vs. random). As written, readers cannot assess whether emergent specialization is meaningfully stronger than what random routing achieves — the qualitative side-by-side is suggestive but not conclusive.

2. **The skip mechanism is user-constrained, not unconstrained learning.** Equation 3 introduces bias parameters with a user-specified target skip ratio $r$ and update speed $u$. The mechanism enforces a target skip fraction rather than letting the model freely discover how much compute to allocate. The paper's framing — "models learn to allocate compute intelligently" — implies more autonomy than is structurally present; the *how* is learned but the *how much* is prescribed. This affects the interpretation of the efficiency results.

3. **Language parameter reuse is self-reported as random, but its implications for the generality of DNA's weight-sharing story are not drawn.** Section 4.3 states: "we conclude that module reuse is most likely random in the language case. This suggests that language DNAs can be further improved by discouraging module reuse." The emergent weight-sharing story told for vision (Section 3.3, Fig. 7) is a positive result; it would be valuable to note explicitly that this does not transfer to language, qualifying the generality of the framework.

### Trivial

- None worth flagging.

---

## Nice-to-Haves

- Convert the patch-clustering analysis in Figures 3 and 8 into a quantitative metric: compute within-path vs. between-path feature similarity for trained vs. random DNA models. A single ratio would turn a suggestive qualitative result into a defensible empirical claim.
- Explicitly acknowledge Table 3's unfavorable skip comparison and offer even a brief analysis: Is the gap due to training instability? Does it shrink at larger scale? Are there early signs of improvement with different bias hyperparameter settings? A paragraph engaging with this negative result would make it informative rather than just present.
- Report sensitivity of results to the skip-ratio hyperparameter $r$ for at least two values, to establish whether the efficiency result is robust or coincidental to the specific $r$ chosen.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic: attention sparsity lacks empirical analysis.** Removed because the paper explicitly labels attention sparsity as a structural property ("attention is computed only between tokens that are currently co-located in the same module"), not an empirical claim to be tested. The paper is honest that this is a consequence of the routing design.
- **Harsh critic: deep-dream classification confidence values (p=0.48) indicate unreliable routing visualization.** Removed because the paper itself explicitly explains this in Figure 4: "the network is guessing the group of classes correctly: birds and dogs, but has difficulty deciding the species and breed." The low top-1 confidence is both acknowledged and explained.
- **Harsh critic: hyperparameter sensitivity not ablated (N_b, N_m, N_r, skip bias update).** Removed as a standalone weakness per the scope rules: the paper is explicitly framed as a feasibility demonstration, and demanding comprehensive ablations is outside its declared scope. This is a nice-to-have.
- **Strength finder: "power-law distribution adds principled justification for architectural design."** Removed because this framing conflicts with verified weakness #3 — the same distribution appears in random models, making it a structural artifact of topology rather than a design virtue.
- **Strength finder: "unified framework naturally subsumes MoE, MoD, weight sharing, early-exit."** Removed as generic — this is a restatement of the abstract and does not constitute specific evidence from experiments.
- **Harsh critic: Section 3.2 random model baseline in Appendix G.2 — "creates explanatory burden."** Partially absorbed into Minor weakness #1; the full framing as a "structural flaw" is removed since the paper does acknowledge and address this comparison (just qualitatively).

---

## Novel Insights

The paper's most genuinely novel observation is the coexistence of emergent specialization that is semantically coherent (vision paths separating edges, backgrounds, objects; language paths grouping verb forms, punctuation, sentence-level tokens) *alongside* an architectural power-law that appears to be a topological invariant rather than a learned property — the random model exponent matches the trained model exponent in vision. This juxtaposition suggests that DNA models operate in a regime where much of the macro-statistical structure (path frequency distribution) is set by the combinatorial architecture, while the *content* of which token chooses which path is where learning acts. This framing — combinatorially fixed macro-statistics, content-driven micro-assignments — is not explicitly articulated in the paper but is latent in the data presented, and it would be a more defensible and interesting characterization of the power-law finding than the current framing.

---

## Suggestions

1. **Directly address Table 3's skip-vs-shallower comparison in the text.** One paragraph analyzing why the skip DNA trails the shallower GPT-2 — and what conditions might close the gap — would transform a silent negative result into a scientific contribution.
2. **Add a quantitative specialization metric** comparing within-path vs. between-path feature similarity for trained and random models. This converts Fig. 3 / Appendix G.2 from suggestive to rigorous.
3. **Reframe the efficiency claim** to match what is demonstrated: the model learns *which* inputs to spend more compute on (interpretable allocation), but not yet to *outperform* a smaller dense model at the same inference budget. Both results are interesting; the current framing oversells the second.
4. **Acknowledge total parameter asymmetry** in the discussion of competitiveness: the DNA models' extra capacity (non-activated parameters) deserves explicit treatment.

---

## Assessment

**Originality**: High. The DNA framework is a genuine generalization of MoE, MoD, and weight-sharing into a unified, order-free architecture. The emergent-routing-equals-emergent-interpretability framing is novel and well-executed in vision.

**Importance of research question**: High. Dynamic, content-dependent computation is a central challenge for scalable inference; showing that it can emerge end-to-end rather than being hand-designed is valuable.

**Claims supported**: Mixed. The feasibility and interpretability claims are reasonably well-supported in vision. The "competitive" claim for language is real but complicated by total parameter asymmetry. The efficiency claim is not supported: the skip model loses to a simpler baseline, and this goes unremarked.

**Soundness of experiments**: Moderate. The experimental setup is appropriate for a feasibility paper, but the skip comparison in Table 3 is a critical gap. The total parameter asymmetry in comparisons is a persistent issue.

**Clarity**: Moderate. The paper is readable and the figures are informative, but key issues (skip comparison, parameter count asymmetry, random-model power-law) are not addressed in the text even when the data is present.

**Value to the research community**: Moderate-to-high for the interpretability and architectural analysis; lower for the efficiency contribution until the skip results improve.

---

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>