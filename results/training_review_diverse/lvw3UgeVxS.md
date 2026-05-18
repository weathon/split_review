Now I have all the information I need. Let me write the consolidated review.

## Summary

gRNAde introduces a geometric deep learning pipeline for 3D RNA inverse design, using a multi-state Graph Neural Network and autoregressive decoding to generate sequences conditioned on one or more backbone conformations. The paper addresses the important and underexplored problem of structure-aware RNA design, analogous to ProteinMPNN for proteins, and demonstrates competitive sequence recovery on established benchmarks along with the first multi-state GNN for biomolecular conformational ensembles.

## Strengths

1. **First geometric deep learning method for 3D RNA inverse design.** gRNAde is the first approach to apply a learned, 3D-structure-conditioned generative model to RNA inverse folding, analogous to how ProteinMPNN transformed protein design. The use of GVP-GNN layers with SO(3) equivariance on coarse-grained RNA backbone representations is technically sound and well-motivated.

2. **Novel multi-state GNN for conformational ensembles.** The multi-state architecture (Section 2.2) processes multiple backbone structures independently while maintaining permutation equivariance across states, with a simple average pooling over states. This is a genuine architectural contribution — the first geometric deep learning model for multi-state biomolecule representation learning — and the design enables both single-state and multi-state inference with the same model.

3. **Competitive sequence recovery on the Das et al. (2010) benchmark.** gRNAde achieves 56% average native sequence recovery on 14 RNA structures, compared to 45% for Rosetta (historical) and 43% for the concurrent GNN method RDesign (Figure 2a). This suggests gRNAde's learned representations capture meaningful structure-sequence relationships.

4. **Practical inference speed and usability.** gRNAde can design hundreds of sequences in ~1 second on GPU or ~10 seconds on CPU, compared to hours for Rosetta. The model supports temperature-controlled autoregressive decoding, unordered decoding, partial redesign via masking/logit biasing, and works on both CPU and GPU.

## Weaknesses

### Fatal
None.

### Major

1. **Rosetta comparison uses historical numbers (not re-run).** The central claim "gRNAde obtains higher native sequence recovery rates (56%) compared to Rosetta (45%)" (line 7) relies on Rosetta numbers from Das et al. (2010), a ~15-year-old study. The paper acknowledges it did not run Rosetta (line 265). While the paper is transparent about this, and also compares against the concurrent method RDesign (43%), the headline "improved performance over Rosetta" is the paper's primary motivation and its strongest empirical anchor. Software versions, runtime settings, and evaluation procedures may have changed in 15 years. The comparison to RDesign partially mitigates this (gRNAde: 56% vs RDesign: 43%), but RDesign numbers are also taken from its paper rather than re-run (line 257). The paper would be significantly strengthened by either running a current Rosetta build (or maintained fork) on the same 14 structures, or by explicitly shifting the emphasis to the RDesign comparison.

2. **Self-consistency metrics are described but never reported.** Section 2.3 defines a comprehensive evaluation framework including secondary structure self-consistency (MCC via EternaFold) and tertiary structure self-consistency (RMSD, TM-score, GDT_TS via RhoFold). The experimental setup states these will be computed (line 209). However, the results (Section 4) report only native sequence recovery and perplexity — none of the self-consistency metrics appear anywhere in the results. This is a significant omission because: (a) the paper itself notes that recovery "can be misleading in the case of RNAs where alternative nucleotide base pairings can form the same structural patterns" (line 151); (b) self-consistency provides direct evidence that designed sequences are structurally plausible beyond matching the native sequence; and (c) the evaluation framework is presented as a contribution but left unexecuted in the paper.

3. **Zero-shot fitness ranking only compares against random baselines.** The retrospective study (Section 4.3, Figure 4) compares gRNAde's perplexity-based ranking only against random selection strategies (random from all mutants, random from single mutants, random from single+double mutants). Showing that a method outperforms random sampling at low budgets is the weakest possible signal — essentially any model with any signal will do so. Meaningful baselines would include: a sequence-only model (e.g., PSSM or an unsupervised RNA language model), conservation-based scoring, or Rosetta energy estimates on the same mutants. The paper currently shows that gRNAde's signal is non-zero, but provides no evidence that it is better than any reasonable alternative, which undermines the concluding claim that "gRNAde's perplexity correlates with experimental fitness measurements."

### Minor

4. **Multi-state design benchmark lacks an external baseline.** The multi-state evaluation (Section 4.2) compares only the multi-state variant of gRNAde against its own single-state variant. While this is a necessary ablation, it is not sufficient. A reasonable control would be to run the single-state model independently on each conformation and combine predictions post-hoc (e.g., by averaging perplexities or taking consensus sequences across states). The paper claims multi-state design "was previously not possible with Rosetta" (line 52), but this does not justify omitting a sensible post-hoc combination baseline that tests whether the architectural multi-state encoding is necessary or whether the benefit comes from simply considering multiple states at inference time.

5. **The headline Rosetta comparison uses only 14 structures.** The central comparison (56% vs 45%) rests on 14 RNA structures. While these come from a well-established benchmark (Das et al. 2010), 14 is a small sample size for drawing strong conclusions. The paper has a larger 100-structure test set from structural clustering (line 191) but does not use it for the Rosetta comparison. Confidence intervals or per-structure recovery values for these 14 structures would help assess reliability.

6. **Training setup for single-state vs. multi-state comparison is underspecified.** For the multi-state benchmark (Section 4.2), it is unclear whether the single-state model was trained on one randomly chosen structure per RNA, or on all available states as independent training examples. If the single-state model sees multiple states as separate training points, the data quantity differs between comparisons, confounding the analysis. This needs clarification.

### Trivial

7. **Low sampling temperature (0.1) used without exploration of the recovery-diversity trade-off.** The paper uses temperature 0.1 for all evaluations (line 209), making the model nearly deterministic. Since real design campaigns often require diverse candidate sequences, characterizing recovery vs. diversity across temperatures would make the method more practically useful. The paper mentions this trade-off (line 138) but does not explore it empirically.

## Nice-to-Haves

- Running a current Rosetta build on the 14-structure benchmark (or a maintained fork with RNA support) would be the single most impactful improvement; absent that, the paper should shift emphasis away from the Rosetta comparison and toward the RDesign comparison.
- Adding at least one non-random baseline to the zero-shot ranking analysis (e.g., conservation scores from a sequence alignment or an RNA language model) would substantially strengthen the claim.
- Reporting the self-consistency metrics (MCC, RMSD, TM-score, GDT_TS) that are already defined and promised in the paper would complete the evaluation framework and strengthen the design quality claims.
- Adding a post-hoc combination baseline for multi-state design (e.g., single-state predictions averaged across conformations) would test whether the architectural contribution is necessary.
- Per-nucleotide recovery broken down by secondary structure context (paired vs. unpaired) would be informative since RNA design is known to be harder in unpaired regions.

## Removed Points

- **"The Rosetta comparison is a serious contradiction"** — This characterization is removed because there is no contradiction. The paper reproduced the *benchmark setup* (same structures, same evaluation protocol) from Das et al. (2010) while being transparent that Rosetta numbers are taken from the original paper. The underlying concern about historical numbers is real and retained above, but the framing as a contradiction is inaccurate.
- **"The paper claims multi-state design was previously not possible with Rosetta, but this does not justify omitting a sensible alternative"** — The claim itself is factually accurate (Rosetta does not support multi-state RNA design). The weakness about missing post-hoc baselines is retained in Minor, but the implication that the claim is false is removed.
- **Strength: "Comprehensive in-silico evaluation framework"** — Removed because it conflicts with the verified weakness that self-consistency metrics (MCC, RMSD, TM-score, GDT_TS) are described but never reported in results. The framework is aspirational rather than executed.
- **Strength: "Practical design flexibility"** — Too generic; temperature-controlled sampling, unordered decoding, and masking are standard features for autoregressive models.
- **Criticism about missing appendix content** — Removed per instructions; the parser strips appendix sections that exist in the original submission.
- **Demands for reporting confidence intervals on 14-structure benchmark** — Weakened from the critic's framing; 14 structures is indeed small, but per-structure values (not formal confidence intervals) are what's needed, and the paper already reports standard deviations across 3 random seeds.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent pattern: the paper's architectural contributions are genuinely novel and technically sound, but the empirical validation consistently under-delivers relative to the claims. Each evaluation (Rosetta comparison, zero-shot ranking, multi-state design) has a notable gap that prevents the evidence from fully matching the strength of the claims. This is fixable — the gaps are in effort/completeness, not in fundamental flaws — but the current version asks the reader to accept claims on trust rather than demonstration.

## Suggestions

1. **Report the self-consistency metrics.** This is the single highest-impact fix: the metrics are already defined, the pipeline is already set up to compute them, and they directly address the most important question ("are designed sequences structurally plausible?"). This would also make the "comprehensive evaluation framework" claim credible.

2. **Either run Rosetta or re-center the narrative.** If Rosetta cannot be run, explicitly frame it as a historical baseline and make the comparison with RDesign (and any other contemporary learned method) the primary evidence. The paper currently hedges by comparing to RDesign while keeping Rosetta as the headline — pick one framing and commit to it.

3. **Add at least one non-random baseline to the zero-shot analysis.** A simple PSSM or an RNA language model perplexity score would transform the claim from "our method beats random" to "our method is competitive with or better than reasonable alternatives."

4. **Add a post-hoc multi-state baseline.** Run the single-state gRNAde independently on each conformation and select sequences by averaging perplexities across states. This directly tests whether the multi-state GNN encoding is the source of improvement.

5. **Clarify the single-state vs. multi-state training setup.** State explicitly whether the single-state model was trained on one structure per RNA or on all states.

## Score and Decision

**Originality:** Good — first GNN for 3D RNA inverse design; multi-state GNN for conformational ensembles is genuinely novel.  
**Importance:** High — RNA design is significantly underexplored compared to proteins, and structure-aware methods are needed.  
**Claims well-supported:** Partially — the method is sound, but each empirical claim has a notable gap that prevents full confidence.  
**Soundness:** Reasonable architecture; evaluation has gaps but no fundamental errors.  
**Clarity:** Good — clear motivation, well-structured, transparent about limitations.  
**Value to community:** High — provides a practical tool, benchmark, and opens the direction of structure-conditioned RNA design.

The paper has a real, non-trivial contribution: the first geometric deep learning approach to 3D RNA inverse design, with a novel multi-state GNN extension. However, the empirical validation is consistently weaker than the claims. The issues are fixable — they reflect incomplete evaluation effort rather than flawed methodology — but in its current form, the paper overstates what the evidence supports. I recommend a weak accept with major revision: the core contribution warrants publication, but the authors should address the gaps (especially reporting self-consistency metrics, adding sensible baselines) in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>