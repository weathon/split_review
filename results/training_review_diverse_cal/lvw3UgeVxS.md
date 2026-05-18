Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

gRNAde introduces a geometric deep learning pipeline for RNA inverse design conditioned on one or more 3D backbone structures. The method uses a multi-state Graph Neural Network with autoregressive decoding to design RNA sequences conditioned on 3D structure, analogous to ProteinMPNN for proteins. The paper demonstrates: (1) improved sequence recovery (56% vs. 45%) over Rosetta on a 14-RNA single-state benchmark, (2) a new multi-state design capability for structurally flexible RNAs yielding 3–5% improvement over single-state models, and (3) zero-shot ranking of mutant fitness in a retrospective ribozyme study.

## Strengths

- **Outperforms existing methods on the single-state benchmark.** On the 14-RNA benchmark from Das et al. (2010), gRNAde achieves 56% native sequence recovery vs. Rosetta's 45%, FARNA's 32%, ViennaRNA's 27%, and RDesign's 43% (Section 4.1, Figure 2a). The speed advantage is substantial — under a second vs. hours — making high-throughput design practical.

- **Enables multi-state RNA design, a genuinely new capability.** The multi-state GNN variant yields a consistent 3–5% improvement over single-state models on a 100-RNA multi-state benchmark (Figure 3a), with gains concentrated in structurally flexible nucleotides undergoing base-pairing changes or high RMSD between states (Figure 3b, Section 4.2). Physics-based tools like Rosetta cannot condition on multiple conformations simultaneously, so this fills a real gap.

- **Rigorous dataset construction.** The dataset of 4,223 RNA sequences from RNASolo is split using US-align with TM-score >0.45 to ensure structurally dissimilar training/test sets. The multi-state split is explicitly designed to select highly flexible RNAs (Section 3). This careful experimental design sets a standard for RNA inverse folding benchmarks.

- **Multi-state GNN is the first architecture for multi-state biomolecule representation learning.** The approach of stacking conformational states along a new axis with order-invariant pooling (Section 2.2) is generic and could be repurposed for proteins or other learning tasks on conformational ensembles, providing a methodological contribution beyond just the RNA application.

## Weaknesses

### Fatal
None.

### Major

**1. Multi-state vs. single-state comparison is confounded by training data quantity.** The paper trains "equivalent single-state and multi-state gRNAde models on the multi-state split" (line 309) but does not clarify whether the single-state model receives the same total number of graphs per RNA or only one structure per RNA. The multi-state model processes k conformations per RNA during training, while the single-state variant appears to use only one. If true, the reported 3–5% improvement could partly reflect more training data (or more views of the same RNA), not the multi-state pooling mechanism itself. The paper offers partial mitigation — the multi-state model also generalizes better to the single-state benchmark (line 314–315) — but this does not fully deconfound the effect. Without a control where the single-state model is trained on the same number of graphs (e.g., each conformation treated as an independent training example with logit averaging at test time), the central claim of Section 4.2 is not fully supported.

**2. Headline comparison against Rosetta relies on cited (not verified) numbers from a 2010 paper on only 14 structures.** The authors acknowledge they did not run Rosetta: "We have not run Rosetta ourselves as recent builds do not include RNA recipes" (line 265). The Rosetta performance (45%) is cited from Das et al. (2010), whose evaluation protocol may differ from the current setup. While the paper also cites RDesign (43%) as an additional contemporary baseline — which partially mitigates the concern — both comparisons use literature-reported numbers rather than independently re-run results. The paper's strongest claim (outperforming state-of-the-art Rosetta) thus rests on a narrow foundation that the authors did not verify experimentally. Running at least one baseline (e.g., RDesign, which is a GNN-based method) under a consistent protocol would substantially strengthen this claim.

**3. Zero-shot fitness ranking compares only against random baselines.** The retrospective study on the ribozyme fitness landscape (Figure 4, Section 4.3) compares gRNAde's perplexity against: (a) random selection from all ~75K mutants, (b) random selection from single mutants, and (c) random selection from single+double mutants. Any method with a weak signal will beat random; this is a necessary sanity check, not a demonstration of practical value. To establish that gRNAde's geometric conditioning provides an advantage over simpler approaches, the authors should compare against at least one alternative: a structure-agnostic sequence likelihood model (e.g., an RNA language model like RNA-BERT or a position-specific scoring matrix), evolutionary conservation scores, or a structure-based energy function. The paper frames this result as "promising" (line 361), which is appropriately cautious, but the lack of any non-random baseline limits the conclusion's informativeness.

### Minor

**1. No per-test-sample confidence intervals for recovery improvements.** The paper reports standard deviations across 3 random seeds (model retraining variance) but not confidence intervals for the distribution over test cases. Given that the single-state benchmark has only 14 samples and the multi-state benchmark has 100 samples, readers cannot assess whether the reported differences (e.g., 56% vs. 45%, 3–5% improvement) are statistically reliable. Bootstrap or permutation-based confidence intervals would help.

**2. k=32 nearest neighbors not ablated.** The graph construction fixes k=32 nearest neighbors without justification or sensitivity analysis (line 89). RNA structures can be sparse, and varying this parameter (e.g., k=8,16,32,64) could affect performance.

**3. The multi-state architecture is simple averaging — the novelty claim is narrow.** The paper states it is "the first geometric deep learning architecture for multi-state biomolecule representation learning" (line 53, 376), and acknowledges it uses "a simple sum or average pooling" with "no new learnable parameters" (line 128). While the claim of being first is likely correct, the architectural innovation is incremental rather than substantive. The paper would benefit from more explicitly acknowledging this simplicity rather than polishing it as a major algorithmic advance.

### Trivial
None beyond those listed above.

## Nice-to-Haves

- Deconfound the multi-state comparison by training a single-state baseline on the same set of graphs (each conformation as an independent training example), then averaging predictions at test time. Alternatively, present explicit data ablation results.
- Run RDesign (or another contemporary method) under the authors' own evaluation protocol for the single-state benchmark, rather than citing literature numbers.
- Add a simple sequence-based baseline (e.g., RNA language model perplexity) to the zero-shot fitness ranking study.
- Include a failure analysis: which RNAs are hardest for gRNAde, and do any cases exist where Rosetta outperforms it?
- Consider a sensitivity analysis for the k-nearest-neighbors graph construction parameter.

## Removed Points

- "The self-consistency scores appear only in figures and the appendix (which was stripped)." — The appendix was stripped by the parser, not omitted by the authors. The self-consistency metrics are described in Section 2.3 and referenced in results. Points about missing appendix content are artifacts of the review pipeline.
- Generic/superficial strengths from Strength Finder that lacked specific evidence or conflicted with verified weaknesses have been filtered out of the Strengths section.
- Criticisms about the paper not covering broader domains or additional tasks have been filtered as scope creep (the paper's direction is well-defined).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Deconfound the multi-state experiment:** Train the single-state baseline on the same number of graphs per RNA as the multi-state model (each conformation processed independently, predictions averaged at test time). This directly tests whether the pooling mechanism itself adds value beyond more training data.
2. **Run at least one contemporary baseline independently** (e.g., RDesign) to verify the reported numbers on the 14-RNA single-state benchmark under a consistent evaluation protocol.
3. **Add a sequence-only baseline to the fitness ranking study** (e.g., RNA-BERT or a simple PWM-derived likelihood) to demonstrate that gRNAde's geometric conditioning provides a real advantage over sequence-only signals.
4. Report 95% bootstrap confidence intervals for the recovery differences on both benchmarks to help readers assess statistical reliability.
5. Include a brief failure analysis discussing RNA structures where gRNAde underperforms and characterizing common failure modes.

**Assessment dimensions:** The paper is **original** in its application of multi-state geometric deep learning to RNA inverse design, which is an underexplored area. The **research question** — designing RNA sequences conditioned on 3D structural ensembles — is timely and important for RNA therapeutic design. The **claims** are largely well-supported but have the three documented weaknesses above. The **experimental design** is sound in its dataset construction and evaluation methodology, though the confound in the multi-state comparison and reliance on cited Rosetta numbers weaken the evidence. The **writing** is clear and well-structured. The **value to the community** is significant: the method is fast, open-able (the code is cited), and fills a real gap where multi-state RNA design was previously impossible.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>