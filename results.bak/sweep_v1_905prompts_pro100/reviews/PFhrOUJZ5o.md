## Summary

This paper introduces LAION-Comp, a large-scale dataset of 540K images from LAION-Aesthetics annotated with GPT-4o–generated scene graphs (objects, attributes, and inter-object relations). It also contributes CompSGen Bench (20,838 complex scenes with >4 relations for evaluation) and trains baseline SG-to-image models across multiple backbones (SDXL, SD3.5, FLUX) using a GNN-based scene graph encoder. The dataset demonstrably improves over existing SG datasets (COCO-Stuff, Visual Genome) for SG2IM, and the CompSGen Bench fills a gap in compositional evaluation.

## Strengths

- **Substantial dataset at scale**: LAION-Comp provides 540K SG-image pairs—roughly 5× the size of Visual Genome—with richer annotations (20% more objects, 216% more after excluding proper nouns; 77.48% non-spatial relations vs. VG's 41.98%). This is a meaningful resource for the compositional generation community.

- **Well-designed annotation pipeline**: The four-step prompt engineering (Figure 2) enforces unique object IDs, mandatory abstract attributes, precise relational verbs, and strict formatting. This yields annotations that are both more informative (Figure 3, Table 1: SG-IoU+ 0.422 vs. 0.306 for original captions) and more diverse (Figure 4b: top-10 relations and attributes each account for <8% of total).

- **Dataset quality validated through downstream training**: SG2IM models (SGDiff, SG-Adapter, SDXL-SG) trained on LAION-Comp consistently outperform the same models trained on COCO or Visual Genome across SG-IoU, Entity-IoU, and Relation-IoU (Table 2). The ablation on data proportion (Table 4) shows that even 10% of LAION-Comp matches or exceeds full Visual Genome training, confirming annotation quality translates to improved generation.

- **Targeted benchmark for complex scenes**: CompSGen Bench selects 20,838 test samples with >4 relations, providing a focused evaluation for compositional generation. Models trained on LAION-Comp achieve state-of-the-art scores on this benchmark (Table 3: FLUX-SG reaches Rel-IoU 0.776 vs. best prior SG2IM at 0.698).

- **Multi-backbone validation**: The GNN scene-graph encoder is integrated with SDXL, SD3.5, and FLUX backbones, all showing consistent improvements over their prompt-only counterparts, demonstrating the approach is not architecture-specific.

## Weaknesses

### Fatal

None.

### Major

- **Missing text-only fine-tuned baseline**: The paper's central claim is that *structural annotations* (scene graphs) are crucial for compositional generation. However, the experimental comparison pits SG-fine-tuned models against *off-the-shelf* T2I models (SDXL, SD3.5, FLUX) that differ in training data, optimization, and image distribution. The observed gains could plausibly result from fine-tuning on a curated set of high-quality images rather than from the SG format itself. A controlled experiment—fine-tuning the same backbone on the identical image set using dense text captions (e.g., GPT-4o–generated descriptions in paragraph form) versus scene graphs—is needed to isolate the effect of structural annotation. Without this, the headline conclusion "structural annotations are crucial" is asserted rather than demonstrated. This does not invalidate the dataset and benchmark contributions, but it means the paper overclaims relative to its evidence.

### Minor

- **Limited detail on human verification in the main text**: The paper reports annotation accuracy numbers (98.8% objects, 97.5% attributes, 95.7% relations) from "partial human verification" and defers details to Appendix A.5 (stripped). The main text would benefit from at minimum stating the verification sample size and sampling method, so readers can assess the reliability claim without consulting the appendix.

- **CLIP score comparison across different test sets is misleading**: The paper states (line 383) that "Although the test set of CompSGen Bench is more complex, the models achieve even higher scores" when comparing CLIP scores of 0.630/0.635 on COCO against 0.700/0.707 on CompSGen Bench. CLIP scores are not comparable across different reference image sets, so this statement does not support the intended conclusion about LAION-Comp quality.

- **SG-IoU+, Ent-IoU+, Rel-IoU+ metrics undefined in the main text**: These annotation-level accuracy metrics are used in Table 1 and Figure 3 to argue for annotation quality but are only defined in Appendix A.2. A one-sentence summary in the main text would improve readability.

### Trivial

- The editing framework (Sec. A.1) is listed as a contribution in the abstract but deferred entirely to the appendix. The paper would be tighter if it either included a representative result in the main text or scoped the editing claim more modestly.

## Nice-to-Haves

- A discussion of potential annotation biases from GPT-4o (e.g., over-generation of certain attributes, cultural biases in person descriptions like gender/age) would strengthen the dataset documentation.
- The paper could explicitly discuss the license and access plan for the dataset, given its derivation from LAION-Aesthetics.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Reliability of automated annotations — no confidence intervals or sample sizes"**: The harsh critic raised this as a major evidential gap. The paper does report specific accuracy numbers and references Appendix A.5. While more detail in the main text would help (retained as Minor above), this is not a reason to doubt the dataset quality given the explicit verification claim. The harsh critic's framing as a "fragile" claim is overly skeptical without having access to the appendix.

- **"Automatic accuracy metrics may encode same biases as annotation pipeline"**: This is speculative. The SG-IoU+ metrics use a scene graph parser; whether it shares biases with GPT-4o is unknown and the critic provides no evidence. Removed as speculative.

- **"The comparison of annotation length vs. accuracy — accuracy metrics are not defined in the main text, and their automatic nature raises circularity"**: The circularity concern is unfounded speculation. The undefined-in-main-text issue is retained as Minor above, but the circularity claim is removed.

- **"Editing framework — with no results in the main paper it is impossible to judge"**: The paper explicitly states this is deferred due to space (Sec. A.1) and it's presented as a secondary contribution. Removed as a scope issue — the paper is primarily a dataset + benchmark paper.

- **"Dataset's relationship to original LAION images (license, source) not discussed"**: The paper states it's built on LAION-Aesthetics V2 (6.5+), which is a public subset of LAION-5B. The dataset is announced as publicly available. This is a nice-to-have but not a weakness. Moved to Nice-to-Haves.

- **"The observed gains may result entirely from fine-tuning on curated high-quality images"**: This is retained in Major but softened from the harsh critic's "fatal" framing. The controlled experiment is genuinely needed to support the headline claim, but the dataset and benchmark contributions stand independently.

- **From Strength Finder**: The "Extended impact through editing" strength was dropped because the editing contribution is entirely in the stripped appendix and cannot be evaluated from the main text. The "Commitment to reproducibility" strength, while true, is generic — code availability is standard practice. Kept the concrete, evidence-backed strengths.

## Novel Insights

None beyond the paper's own contributions. The review process did not surface analytical angles or connections that the paper itself missed in a substantive way.

## Suggestions

- The single highest-impact improvement would be a controlled experiment: fine-tune SDXL on the same 480K LAION-Comp training images using (a) original LAION captions, (b) GPT-4o–generated paragraph descriptions, and (c) the scene graphs, then evaluate all three on CompSGen Bench. This would cleanly isolate the value of structural annotation and directly support (or qualify) the paper's central thesis.
- Add a brief summary of SG-IoU+, Ent-IoU+, and Rel-IoU+ definitions in the main text near Table 1.
- Include the human verification sample size and methodology in the main text (even one sentence) rather than only in the appendix.

**Originality**: The dataset is a novel application of LLM-based annotation at scale to scene graphs, filling a clear gap. The GNN encoder is well-executed but not novel. **Importance**: Addressing compositional generation through better data is important and timely. **Claims**: The dataset and benchmark claims are well-supported; the claim that structural annotations are *necessary* (vs. beneficial) is not adequately isolated. **Soundness**: Experiments are thorough within their design constraints, but a key baseline is missing. **Clarity**: Well-written and well-organized. **Community value**: High — the dataset, benchmark, and trained models will be useful resources.

## Score and Decision

**Round 1 bracket**: Based on comparison with SG-Adapter (5.50 — smaller dataset, simpler method, rejected), Causal Graphical Models (6.67 — accepted with concerns), and Compositional Entailment Learning (8.00 — clean accept, strong novelty), the paper plausibly falls in the 5.5–7.5 range.

**Round 2 narrowing**: Compared against Davidsonian Scene Graph (6.00 — accepted, scene-graph-based evaluation, missing ablations), Diffusion Feedback Helps CLIP (6.60 — accepted with notable methodological concerns), and Enhancing Compositional T2I with Seeds (7.33 — accepted, clean methodology, strong results). The paper is stronger than Davidsonian Scene Graph (larger scale, more comprehensive experiments) and comparable to Diffusion Feedback Helps CLIP (both have a significant concern but strong empirical contributions). It falls somewhat below the Seeds paper (7.33), which had a cleaner experimental design and more directly addressed its central question.

**Anchor summary**:
- `V73W8MXnNW` (3.00, Round 1): Progressive Visual Relationship Inference — clearly weaker, small-scale method paper.
- `TCSaLeANpN` (3.00, Round 1): SynBuild-3D — synthetic dataset, different domain, much weaker.
- `KCYDpqSpqg` (5.50, Round 1/2): SG-Adapter — closest topical match; our paper has far larger scale, more comprehensive evaluation.
- `haJHr4UsQX` (6.67, Round 1): Causal Graphical Models — comparable quality; both have one notable concern.
- `ITq4ZRUT4a` (6.00, Round 2): Davidsonian Scene Graph — our paper has larger scale but similar quality tier.
- `tLFWU6izoA` (6.60, Round 2): Diffusion Feedback Helps CLIP — comparable quality; both have a methodological concern.
- `5BSlakturs` (7.33, Round 2): Enhancing Compositional T2I with Seeds — cleaner methodology, our paper is somewhat weaker.
- `3i13Gev2hV` (8.00, Round 1): Compositional Entailment Learning — clearly stronger, clean acceptance.

**Final score**: 6.0. The paper makes a substantial and useful contribution (dataset + benchmark + baselines) that the community will benefit from. The missing text-only fine-tuned baseline is a real gap that prevents the paper from fully supporting its strongest causal claim, but does not undermine the value of the dataset and benchmark themselves. This places it firmly in the acceptance range for venues that value dataset contributions, at a level comparable to other accepted papers with one notable but non-fatal methodological concern.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>