Now I have a clear picture. Let me produce the consolidated final review.

## Summary

RA-TTA introduces a test-time adaptation method for vision-language models (e.g., CLIP) that retrieves external images from a web-scale database on-the-fly using LLM-generated fine-grained text descriptions. The method has two main steps: (1) description-based retrieval, where text descriptions of visual features (e.g., "boomerang-shaped headlight") are selected via image-to-text search and then used to retrieve relevant external images, and (2) description-based adaptation, where semantic gaps between the test image and retrieved images are computed using those same descriptions, aggregated via optimal transport, and fused with the VLM's initial prediction. Experiments across 17 datasets show consistent improvements (2.49–8.45%) over prior training-free TTA and retrieval-augmented methods.

## Strengths

- **Description-based retrieval dynamically selects test-image-specific external images** rather than using static per-class retrievals (as in prior work like SuS-X, Neural Priming). The ablation in Table 3 confirms this: replacing description-based retrieval with image-to-image similarity search drops accuracy from 53.2% to 48.9% on FGVC Aircraft, showing the retrieval mechanism is crucial.

- **The semantic gap and optimal-transport aggregation provide a well-motivated relevance measure** between test and retrieved images. Table 3 (Var. 2 vs. Var. 3) shows disabling description-based adaptation reduces accuracy from 53.2% to 50.6%, demonstrating that the adaptation scheme adds significant value beyond retrieval alone.

- **Robust image-text alignment via third-quartile percentile** across augmentations reliably filters misleading descriptions. The hyperparameter analysis in Figure 5(d) shows optimal performance at p=0.75 (Q3) with degradation at extreme values, a practical insight grounded in the observation that misleading descriptions produce high scores only on a few augmentations.

- **Consistent state-of-the-art results across a broad evaluation (17 datasets)** with gains of 2.49–8.45% over baselines. RA-TTA outperforms all compared methods on 12/13 transfer learning datasets and on the average of four ImageNet variants, providing strong empirical evidence for the core claim.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Ablation study limited to one dataset.** Table 3 ablates the three main components (description-based retrieval, description-based adaptation, image weighting) on FGVC Aircraft alone. While FGVC Aircraft is a fine-grained dataset where gains are large, the ablation should be repeated on at least one more dataset (e.g., ImageNet or Stanford Cars) to demonstrate that the relative contributions of each component hold across different types of distribution shift. The paper's claims about the importance of its components rest on evidence from a single domain.

- **Optimal transport aggregation is used without justification or ablation.** The paper introduces optimal transport (OT) to aggregate pair-wise semantic gaps (Eq. 8) but never argues why OT is needed over simpler alternatives (e.g., a weighted average of the gaps with appropriate normalization). Nor does it provide an ablation comparing OT to a simpler aggregation strategy. Given the added complexity, this is a missing justification. If OT is not empirically beneficial, the method could be simplified.

- **No discussion of limitations.** The conclusion (§5) is a summary without candidly acknowledging any limitations. The paper should discuss: (a) reliance on class-name filtering to construct the external database (the "external knowledge" is not arbitrary web noise but a curated repository filtered by target class names, which narrows applicability), (b) computational cost of generating M=100 augmented views at test time, (c) sensitivity to the quality of LLM-generated descriptions. These are not fatal issues but are important for readers to understand the method's scope.

### Trivial

- **Database size per dataset is not reported.** The paper states it downloads images whose captions contain target class names from LAION2B, but the total number of retrieved images per dataset is not provided. This is useful for reproducibility and for understanding whether RA-TTA had access to more external images than SuS-X or Neural Priming.

## Nice-to-Haves

- **Direct retrieval quality evaluation.** The paper could strengthen its core claim by measuring retrieval precision directly (e.g., fraction of retrieved images containing the expected pivotal feature) rather than relying solely on downstream classification accuracy. A small-scale annotation of 100–200 retrieval instances would convincingly show that description-based retrieval focuses on pivotal features.

- **Statistical significance measures.** Results are reported as single numbers. Reporting variance over multiple runs with different random seeds would increase confidence, though single-run evaluation is standard practice in this area for large-scale benchmarks.

- **Simple prototype baseline.** A baseline that retrieves external images and computes a class prototype by averaging their embeddings (without the description-based machinery) would help isolate the benefit of the proposed components. The paper already compares to SuS-X-LC and Neural Priming, which are the primary retrieval baselines in the literature, but this simpler baseline would strengthen the analysis.

- **Ablation of OT vs. simpler aggregation.** As noted above, showing that OT adds value over a weighted mean would either justify the complexity or simplify the method.

## Removed Points

- **"Formatting makes exact numbers hard to parse"** — Removed: This refers to PDF extraction artifacts, not an author error.
- **"Database construction conflates two factors" framed as a separate weakness** — Removed/merged: The paper transparently describes the filtering procedure (§4.1), consistent with prior work. The substance is captured in the "no limitations discussion" point, which asks the authors to more explicitly discuss this scope consideration.
- **"No structural flaws that invalidate the contribution"** — This is the critic's overall assessment, not a weakness. Not included.
- Various generic strengths from the Strength Finder about the problem being "important" — Removed: superficial/sycophancy, not concrete evidence about the paper's specific contributions.

## Novel Insights

None beyond the paper's own contributions. The reviewers largely converge on the same assessment: the method is novel and well-evaluated, with the main gaps being the single-dataset ablation and the lack of a limitations discussion. There is no surprising disagreement or overlooked dimension that changes the overall evaluation.

## Suggestions

- **Run the ablation study (Table 3) on at least one additional dataset** (e.g., ImageNet or Stanford Cars) to show that the relative contributions of description-based retrieval, description-based adaptation, and image weighting hold across different types of distribution shifts. This is the single most impactful improvement the authors could make.
- **Add a brief ablation or at minimum a discussion** comparing the OT aggregation to a simpler weighted-average baseline, so readers can understand whether the complexity is warranted.
- **Add a limitations section to the paper** discussing the scope of the database curation, computational cost, and sensitivity to LLM-generated descriptions.
- **Report database sizes per dataset** for reproducibility.

## Score and Decision

**Bracketing (Round 1):** The paper clearly outranks the weak-anchor band (papers scoring 2.5–3.0, which have significant methodological flaws or limited evaluation) and does not reach the strong-anchor band (8.0, which requires exceptional contributions or flawless execution). The initial bracket is **5.5–7.0**.

**Narrowing (Round 2):** I retrieved anchors in the 5.5–7.5 band and read several in full. Compared to DOTA (6.00, rejected), which had unclear methodological details about distribution estimation, RA-TTA is cleaner, more novel, and better evaluated. Compared to RLCF (6.67, accepted), RA-TTA has broader evaluation (17 datasets vs. 3 tasks) but both have comparable minor weaknesses. Compared to BAT-CLIP (5.50, rejected), which had fatal flaws (using ground-truth labels in one reviewer's assessment), RA-TTA is clearly stronger. RA-TTA is also stronger than RoRA-VLM (5.67, rejected), which had fairness-of-comparison concerns.

**Final Score: 6.5.** This positions RA-TTA above DOTA (6.00) due to cleaner methodology and above the rejected middle-range papers, and comparably to RLCF (6.67, accepted). The paper has genuine contributions, a novel method, and thorough evaluation; the identified weaknesses (single-dataset ablation, missing OT justification, no limitations section) are real but minor and addressable in revision.

**Anchors retrieved:**
- pdzHpQbGrn.md (2.50, Round 1) — much weaker paper with poorly motivated active learning at test time
- HfJxXbXlYJ.md (3.00, Round 1) — different topic (LLM2CLIP), not directly comparable
- ZaudLwn0Hm.md (2.50, Round 1) — few-shot adaptation, weaker experimental support
- rwdeKOdAwY.md (3.00, Round 1) — retrieval for image recognition, limited novelty
- yD2JMeKumt.md (6.00, Round 1 & 2) — DOTA, similar TTA topic but unclear methodology; RA-TTA is stronger
- kIP0duasBb.md (6.67, Round 1 & 2) — RLCF, accepted TTA paper; comparable quality to RA-TTA
- A78MiKnGrL.md (4.50, Round 1) — Search4Prompt, narrower scope and evaluation
- z7PhIgVmZU.md (5.50, Round 1 & 2) — BAT-CLIP, had fatal flaw concerns; RA-TTA is clearly stronger
- WyEdX2R4er.md (8.00, Round 1) — data-type understanding, different topic, exceptional rigor
- TPZRq4FALB.md (8.00, Round 1) — multi-modal TTA, higher impact
- 1aF2D2CPHi.md (8.00, Round 1) — data-free distillation, different topic
- 3i13Gev2hV.md (8.00, Round 1) — hyperbolic VLMs, different topic
- 2h1siDrSMl.md (5.67, Round 2) — RoRA-VLM, rejected; RA-TTA has fairer comparisons
- b2UlHeyyC0.md (5.67, Round 2) — RECO, accepted but requires training; RA-TTA is training-free
- sb7qHFYwBc.md (6.50, Round 2) — C-CLIP, continual learning setting; different problem
- TD3SGJfBC7.md (6.25, Round 2) — few-shot TTA for CLIP; different setting

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>