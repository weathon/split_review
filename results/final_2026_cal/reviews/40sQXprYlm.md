## Summary

This paper introduces Distributed Neural Architectures (DNAs), a new class of models where tokens follow content-dependent paths through a collection of modules (MLP, attention, transformer blocks). The architecture is a generalization of conditional computation methods (MoE, MoD, parameter sharing) — paths, connectivity, and module specialization all emerge from end-to-end training. The paper demonstrates DNAs in both vision (ImageNet classification, near ViT-Small accuracy) and language (causal LM on FineWeb-Edu, competitive with GPT-2 Medium), with rich qualitative and quantitative analysis of emergent routing patterns, path specialization, interpretability of routing decisions, and data-dependent compute allocation.

## Strengths

- **Genuinely novel architecture class, not an incremental variant.** DNAs generalize MoE, MoD, parameter sharing, and early-exit into a single framework where each token can take an arbitrary path through any sequence of modules, including identity operations that enable learned skipping. This is a principled conceptual contribution that opens new directions for distributed computation.

- **Competitive feasibility demonstration in both vision and language.** The top-1 DNA reaches 79.1% ImageNet accuracy vs. 79.8% for ViT-Small (22M active params for both). The top-2 DNA language model (433M active params) outperforms GPT-2 Medium (406M) on 5 of 7 zero-shot benchmarks (e.g., HellaSwag 41.8% vs. 40.5%, PIQA 67.9% vs. 66.9%, Table 3). For a first-generation architecture, this is a convincing existence proof.

- **Rich, interpretable routing analysis.** The analysis goes well beyond accuracy numbers. Figures 3 and 8 show that tokens/patches sharing semantic features (edges, flat regions, punctuation, verbs) follow the same learned paths. The deep-dream visualization in Figure 4 — generating images whose patches match the routing decisions of real images — is a particularly clever probe. The paper also honestly reports cases where structure is absent (language parameter sharing appears random, Section 4.3).

- **Emergent data-dependent compute allocation is demonstrated.** Using identity modules and a bias-based skip mechanism (Eq. 2–3), the top-2 DNA (25% skip) allocates less compute to visually simple images (e.g., bassoon, cellular telephone) and more to boundary-heavy images (e.g., puffer, flatworm), shown in Figure 5. This provides direct evidence that compute-efficiency can be learned from data without manual heuristics.

## Weaknesses

### Major

- **Compute-efficiency claim lacks operational measurement.** The paper claims that "compute efficiency/parameter sharing can be learnt from data" (abstract) but reports only "normalized compute" (count of modules used per token, scaled so that never-skipping = 1). No FLOPs, throughput, wall-clock latency, or direct comparison against the dense baseline's actual compute usage is provided. For modules with identical internal dimensions (same d_embed, d_MLP, n_heads), module-count is a reasonable proxy, but the paper does not establish this equivalence or account for routing overhead and the irregular attention patterns that arise when different token groups land in different modules. The compute-efficiency claim is qualitatively supported but quantitatively incomplete. *This does not invalidate the paper, but it is a gap in one of the three stated main findings.*

- **Language baseline comparison is not fully controlled.** The top-2 DNA (603M total params, 433M active) outperforms GPT-2 Medium (406M total). A 50% total-parameter advantage is meaningful — the comparison is favorable to the DNA but not apples-to-apples. The paper includes a 30% shallower GPT-2 baseline, but a denser model with ~600M total parameters (e.g., a wider GPT-2) would be the appropriate controlled comparison. The "competitive" claim in the abstract should be qualified more carefully, or the comparison strengthened. The vision comparison (22M active vs. 22M) is cleaner, though the top-1 DNA's extra 12M inactive parameters (34M total) are a secondary concern.

### Minor

- **No variance or uncertainty reported.** All main results (accuracy, loss, benchmarks) appear to come from single runs. For a paper making comparative claims (DNAs are "competitive with dense baselines"), confidence intervals or multiple-seed statistics are important — a 1% accuracy gap could be within run-to-run noise.

- **Power-law path distribution: acknowledged but under-analyzed.** The paper notes that random models also produce power-law path distributions (exponent −1) — this is transparently reported. However, for vision, the trained model's exponent appears similar to random (no difference stated), and for language the shift is modest (−1 → −1.2). The claim that "paths are distributed according to a power-law" is accurate, but the paper never quantifies what training actually changes about the path distribution beyond stating the exponents. The more valuable finding — that the *content* of paths shifts from superficial to semantic — is well-supported by qualitative analysis (Figures 3, 8) but would benefit from quantitative measures (e.g., how often do patches from the same object follow the same path?).

- **Analysis of compute on OOD/low-resource scripts is incomplete.** The paper observes that documents with Arabic, Greek, Hebrew characters receive lower compute (Section 4.3) and speculates the model routes them to identity/garbage modules. The natural next question — whether these tokens are still classified correctly or have non-trivial loss — is not checked. If the model is simply ignoring tokens it cannot process, the "compute saving" is trivially uninteresting.

### Trivial

- The effective skip rate (achieved vs. target) for the skip models is not reported — e.g., the "25% skip" model's actual average skip rate across the validation set.

## Nice-to-Haves

- A dedicated related work section (likely in the stripped appendix, but if absent from the original submission it would strengthen the paper to include one).
- Analysis of attention group sizes: how many tokens co-occur in a module at a given step on average? The paper notes this is a core feature of the architecture but never quantifies it.
- Ablation of the top-2 skip model in language: the 30% skip variant performs substantially worse than the no-skip version (Table 3), which is noted but not analyzed.

## Removed Points

These points were raised by reviewers but removed per filtering rules:

- *Missing identity module count and hyperparameter values (r, u):* These details belong to the appendix, which was stripped by the parser. Per hard rules, missing appendix content is not a valid criticism.
- *"Power-law finding undercuts itself" framing:* The paper explicitly and transparently reports the random-model baseline. The finding is not about the existence of the power-law as an "emergent property" — it is about the *content specialization* of paths, which differs between random and trained models. This criticism misreads the paper's claims.
- *Formatting/grammar/style nitpicks:* Parser artifacts, not author errors.
- *Missing related works:* Cannot be verified without external sources.
- *Overhead of routing at inference time not discussed:* The paper explicitly acknowledges this ("infrastructure has to be co-designed with the emergent structure") and delegates it to future work, which is reasonable scoping for a feasibility paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add FLOPs and/or wall-clock inference time** for the DNA models vs. their dense counterparts (ViT-Small, GPT-2 Medium). This is the single highest-leverage addition and would directly substantiate the compute-efficiency claim. Even reporting module-count-equivalent FLOPs (computed as (modules used) × (FLOPs per module)) would bridge the gap.

2. **Add a controlled language baseline** with total parameters matching the top-2 DNA (~600M), such as a wider or deeper GPT-2 variant. If that is infeasible, explicitly qualify the "competitive" claim to note the parameter disparity.

3. **Report variance** (at least 3 seeds) for the main accuracy/loss/benchmark results. This is inexpensive and greatly strengthens comparative claims.

4. **Quantify the interpretability**. For vision: measure how often patches from the same ground-truth object region follow the same path vs. random chance (using segmentation annotations or synthetic images). This would move the specialization analysis from anecdotal to evidential.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched three bands on topics related to dynamic routing, conditional computation, and emergent specialization.

| Anchor | Avg Score | Band | Comparison |
|--------|-----------|------|------------|
| 0miO9v1jeC (TAR) | 3.00 | Weak | Weak token-level routing paper with limited evaluation — DNA is clearly stronger |
| exMMxIakjl (SDT/STT) | 3.00 | Weak | Conditional compute where all variants underperform dense baseline — DNA is stronger |
| ONGhOee3qt | 3.00 | Weak | Distributed specialization analysis — different scope but comparable ambition level |
| q1mk8ELkcd | 3.00 | Weak | Arbitrary graph neural networks — less experimental validation |
| 1w1jCfYM8P (ProMoE) | 5.00 | Mid | MoE for diffusion transformers, SOTA on one dataset — less domain breadth than DNA |
| S7o8zBYw4V (DARE) | 4.50 | Mid | Dynamic MoE routing — rejected, concerns about evaluation completeness |
| wPemGNb66V | 4.50 | Mid | Dynamic computation allocation — rejected, limited validation |
| vBZXJzFV6x (ConfSMoE) | 5.33 | Mid | MoE gating for missing modalities — rejected, modest empirical gains |
| kkBOIsrCXh | 8.00 | Strong | Embodied navigation foundation model — different topic, stronger empirical rigor |
| VKGTGGcwl6 | 8.00 | Strong | Multi-turn conversation analysis — different topic, strong evaluation |
| kI27Niy4xY | 8.00 | Strong | Text-to-3D stitching — different topic |
| 248ysaRatx | 8.00 | Strong | Quantum neural networks — different topic |

**Round-1 bracket:** 4.5–7.0

**Round 2 (Narrowing):** Searched within (4.0–6.0) and (6.0–8.0).

| Anchor | Avg Score | Band | Comparison |
|--------|-----------|------|------------|
| KDcwXKr0NU (DiSRouter) | 5.50 | Mid | Distributed LLM routing — Accepted Poster, narrower scope than DNA |
| gH3HhnfWLC (Block Rec. Dynamics) | 6.80 | Mid-high | ViT recurrent dynamics analysis — Accepted Poster, thorough evaluation, more rigorous than DNA |
| RzYXb5YWBs (LoopFormer) | 7.00 | Mid-high | Elastic-depth looped transformers — Accepted Poster, strong experiments, more polished than DNA |
| 3RQ863cRbx | 6.50 | Mid-high | Emergent symbolic mechanisms in VLMs — Accepted Oral, strong analysis |
| sQGlhjKUC0 | 6.40 | Mid-high | Visual information pathways — Accepted Poster |

**Final position:** The DNA paper is stronger than the 4.5–5.5 anchors (broader scope, two domains, richer analysis, novel architecture class vs. incremental routing variants) but weaker than the 6.5–7.0 anchors (those papers have more rigorous experimental evaluation — multiple seeds/checkpoints, controlled baselines, and thorough efficiency measurements). Within the bracket, the paper lands at **6.0** — a solid Accept (Poster) contribution whose main limitations (missing FLOPs measurements, imperfect baseline control) are addressable.

### Final Score

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>