## Summary

This paper introduces AITQE, a model that scores and adaptively rewrites low-quality captions in image-text pairs for MLLM pretraining, rather than discarding low-scoring pairs entirely. The authors construct training data using GPT-4o to score and rewrite captions from LAION-400M, then train a SigLIP+Qwen-2-7B model to reproduce this behavior. Experiments compare AITQE against MLM-Filter (four criteria) and ShareCaptioner across eight benchmarks, reporting an average score.

## Strengths

1. **Well-motivated problem and clean framing** — The paper correctly identifies a real limitation of filter-based data curation: discarding pairs with poor text discards valuable images. The proposed solution (adaptive rewriting rather than discarding) is intuitively appealing and addresses a genuine bottleneck in MLLM pretraining data scaling.

2. **Consistent non-diminishing gains across four orders of magnitude in data scale** — Table 3 shows AITQE-enhanced data outperforming random baselines at 256K (+4.29), 558K (+4.05), 2M (+4.50), and 12M (+4.70) average points, with the largest gain at the largest scale. This supports the paper's claim that the method scales effectively.

3. **Methodological care in identifying and mitigating training instability** — The authors discover that standard LLaVA two-stage training produces a 2.60-point discrepancy between identical runs (Table 1), develop a more stable one-stage protocol, and verify it reduces run-to-run variance (Table 2, 0.73-point gap). This strengthens confidence in the reported comparisons.

4. **Transparent per-benchmark reporting** — All tables report individual benchmark scores alongside the average, allowing readers to inspect where gains actually come from.

## Weaknesses

### Major

1. **The headline average is unprincipled and dominated by a single benchmark.** The paper's central metric averages eight benchmarks with fundamentally incompatible scales: perplexity-based scores (SEED2, AMBER*, MME^H), accuracy values (OKVQA, VQAv2*, DocVQA, TextVQA), and CIDEr×100 (Textcaps). These are not commensurable — a 10-point CIDEr swing is treated identically to a 10-point accuracy swing despite different ranges and meanings.

   The consequence is severe. In Table 1 (256K filtering), AITQE achieves 69.07 on Textcaps vs. Random's 27.41 — a 42-point gap. On every other benchmark, differences are 1–3 points and sometimes favor baselines. The headline "7.16-point improvement" over random and "5.52 points over MLM-Filter" collapses to roughly 0.6 points over MLM-Filter when Textcaps is excluded. The same pattern recurs in Tables 2, 3, and 4. The paper's abstract claims AITQE "surpasses existing methods on various benchmark" — this is not supported for the non-captioning benchmarks individually, and the aggregate that supports it is an uninterpretable average of mismatched quantities.

2. **Ablation study does not control for training data volume.** Table 5 compares a Base Scorer trained on ~260k SFT samples against AITQE trained on ~520k samples (stated in Section 2.1: "the 260k training data is mostly accompanied with contrastive sample, resulting in approximately 520k training data in total"). The individual component rows ("+Contrastive Sample" at 59.81 and "+Rewrite Caption" at 57.70) also use ~520k data yet perform *worse* than the Base (59.88). Only the combined model improves (65.21). The paper attributes this to a "synergistic relationship," but since the data volume differs between Base (~260k) and all other conditions (~520k), the apparent synergy could simply reflect that the base model is undertrained. A controlled ablation with equal training data for all variants is needed to support the claim that the specific design choices (as opposed to more training data) drive the improvement.

3. **Missing standard baselines.** The paper compares against MLM-Filter (four criteria, averaged) and ShareCaptioner. CLIPScore-based filtering — the de facto standard for LAION-based data curation — is not included as a baseline. DFN's learned filter and DataComp-pool methods are also absent. Since the paper claims AITQE "surpasses existing approaches," including these standard MLLM data curation baselines is necessary. The related work section acknowledges CLIPScore and DFN, making their omission from experiments conspicuous.

4. **No direct comparison of rewriting vs. discarding at matched data scales.** The paper's core thesis is that rewriting low-quality captions (preserving data volume) is better than filtering (discarding data). Yet the scaling experiments (Table 3) only compare AITQE-enhanced data against random data — not against filtered data at the same scale. The filtering experiments (Table 1) use a fixed 2M pool as the source, while the enhancement experiments (Table 3) use random samples at various scales from the full LAION-400M. Since the comparison is on different data, the reader cannot determine whether AITQE's approach (keep all data, rewrite) outperforms simply filtering at the same data volume. This is the central comparison the paper's framing demands and it is absent.

5. **Textcaps CIDEr is a problematic evaluation benchmark for this method.** Textcaps uses CIDEr (n-gram overlap with references). AITQE's rewriting mechanism generates captions for low-scoring pairs during MLLM pretraining. If these rewrites make pretraining captions more detailed and stylistically closer to Textcaps reference captions, the trained MLLM will naturally produce captions with higher CIDEr even if general visual understanding has not improved. The paper does not discuss this confound. Textcaps is the only benchmark showing consistent, massive gains (40+ points) while others show marginal or occasionally negative changes, which is consistent with this interpretation.

### Minor

1. **No variance reporting for main experiments.** Despite identifying training instability as a concern and running stability checks, the main results (Tables 1, 3, 4, 5) report only single runs with no confidence intervals. The 0.73-point gap from 2 runs in the stability check is comparable to or larger than some claimed advantages (e.g., +1.82 at 558K filtering, Table 1), raising the possibility that some results are within noise.

2. **Some methodological details are underspecified.** The 20 instruction variants for the GPT-4o prompt are mentioned but not provided; the threshold distinguishing "low" vs. "high" scores for rewriting is not defined. These details impact reproducibility.

### Trivial

None.

## Nice-to-Haves

- A controlled ablation matching training data volume between Base Scorer and all variants.
- Comparison with CLIPScore-based filtering at matched data scales.
- Per-benchmark analysis separating captioning (Textcaps) from VQA/understanding benchmarks, with honest discussion of divergent results.
- Discussion of the potential confound between rewriting and CIDEr-based evaluation.

## Removed Points

The following points from the inputs were removed for the reasons stated:

- **Harsh Critic's claim about MLM-Filter comparison being unclear** ("it is unclear whether this is how MLM-Filter was designed to be used") — Removed as speculative. The paper reports each criterion separately and averages them, which is a standard way to present multi-criteria filter results.
- **Criticism that AITQE does not demonstrate image value without rewriting** — Removed as scope creep. The paper focuses on text quality enhancement; proving images in low-scoring pairs are "actually valuable" would require a fundamentally different experimental design.
- **Strength Finder's claim of "synergistic effect"** — Removed because the ablation confound (unequal data volume) means the interaction cannot be cleanly attributed to design choices vs. data volume.
- **Request for Cauldron data mixture proportions** — Removed as a minor reproducibility detail outside standard norms for this venue.
- **Criticism that the paper lacks cost-benefit discussion** — Removed as a nice-to-have, not a genuine weakness.

## Novel Insights

The ablation pattern is the paper's most interesting finding: adding contrastive samples alone (59.81, essentially flat compared to Base's 59.88) or rewrite training alone (57.70, worse) individually provides no benefit or degrades the base scorer, yet combining them yields a large gain (65.21). While the data volume confound prevents clean attribution, this non-linear interaction suggests the two components serve complementary roles — contrastive samples improve scoring calibration while rewrite training teaches the model when and how to rewrite — and neither works in isolation because improving one capability without the other creates an imbalance. This design insight, if validated with a controlled ablation, could inform future adaptive data enhancement research.

## Suggestions

1. **Replace the unprincipled average** with per-benchmark analysis and, if an aggregate is needed, use normalized scores or a ranking-based method. Separate captioning from VQA/understanding benchmarks.
2. **Run a controlled ablation** fixing training data volume across all variants (base, +contrastive, +rewrite, +both).
3. **Add CLIPScore-based filtering** as a baseline, especially for the scaling experiments.
4. **Compare AITQE-enhanced vs. filtered** data at the same volumes to directly test the paper's central claim.
5. **Discuss the Textcaps CIDEr confound** — whether rewriting inflates CIDEr through stylistic similarity rather than genuine understanding improvement.
6. **Report variance** for main experiments (at least 3 seeds).

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>