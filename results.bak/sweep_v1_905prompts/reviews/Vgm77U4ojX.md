<2 is 80.5, so 51-53 doesn't match.

Could Figure 4 right be showing Top-1 without the ranking heuristic? The ablation shows that without energy scoring, PB Val is 66.1 - not 51-53. Without PB scoring, RMSD is 82.1 - not 51-53.

I'm stuck. The numbers 51, 53, 53 genuinely don't match anything else in the paper. This is a significant error.

Given that Table 4 is internally consistent (72, 79, 87 → weighted average 79.9 ≈ overall 79.9), I'll assume Table 4 is correct and Figure 4 has an error. But this is still a serious presentation flaw in the main results figure.

Let me finalize at 5.5, which I think is fair - higher than DiffDock-Pocket because the methodology is more novel, but lower than the accepted papers because of the inconsistency.

Actually, I want to re-examine whether this inconsistency could be explained by the figure showing a different condition. Let me look at what "≤ 0" might mean in the seq sim range. The Figure says "≤ 0" as the first bin, while Table 4 says "[0, 30)". Both represent the same thing (just different notation). The counts match (109, 76, 123). So it's the same data with different numbers. 

Actually, could "≤ 0" be "≤ 30" and the parser just dropped the 30? The original text in the figure caption says "Seq. Sim. (%) ≤ 0, 30; 30, 95; 95, 100" - this looks like "[0, 30), [30, 95), [95, 100]" with some formatting issue making the first range show as "≤ 0, 30". So "≤ 0, 30" would be parsed as range ≤ 0 but it should be [0, 30). This is a parser artifact. The actual ranges are [0,30), [30,95), [95,100].

OK so the inconsistency is real and not a parser issue.

Let me write the final review now. Decision: Reject at 5.5.Now let me write the final consolidated review.

## Summary

SIGMADOCK introduces a fragment-based SE(3) diffusion model for rigid-receptor molecular docking. The key idea is to decompose a ligand into rigid fragments via a novel fragmentation scheme (FR3D) and learn to reassemble them within the binding pocket via diffusion on SE(3)^m. This avoids the entangled torsional dynamics of prior diffusion models and provides a principled product-of-Haar-measures structure. The paper reports a Top-1 PB-valid success rate of 79.9% on the PoseBusters set—far exceeding prior deep learning methods trained on the same split and approaching AlphaFold3—while requiring only 19k training complexes and offering 50× faster inference.

## Strengths

- **Novel, well-motivated methodological contribution.** The fragment-based SE(3)^m diffusion formulation is a clear conceptual advance over torsional diffusion models. Theorem 1 formalizes why torsional models produce non-product induced measures, while the fragment formulation gives a factorised product of Haar measures. The FR3D fragmentation scheme (merging fragments while preserving triangulation constraints) and Lemma 1's handling of soft geometric constraints are well-reasoned design choices. This is not an incremental modification of an existing method.

- **Thorough ablation study confirms each component's contribution.** Table 1 systematically ablates triangulation conditioning (–4.2% PB Val), fragment merging (–3.6%), protein-ligand interactions (–3.6%), energy scoring (–13.8%), and PB scoring (–9.1%), isolating the value of each design element.

- **Co-factor stratification supports genuine physical learning.** Table 2 shows failure rates are substantially lower for complexes without co-factors (16.2%) than those with natural ligands (41.2%) or ions (23.6%). This analysis goes beyond simple accuracy metrics and provides evidence that the model captures genuine binding physics rather than memorising training examples.

- **Strong theoretical underpinning.** The paper provides rigorous justification for the fragment-space approach (Theorem 1, Lemma 1, Theorem 2), including invariance to the choice of local coordinate axes. The connection between conformational manifolds and bound manifolds (Section 2.2.1) is empirically supported with an RMSD analysis.

- **Pocket-robustness analysis.** Table 3 demonstrates that performance remains stable as the pocket cutoff is varied from 4 Å to 6 Å, with only a moderate drop at 7 Å. The accompanying Vina comparison shows the gains are not attributable to tighter pocket definitions.

## Weaknesses

### Fatal

None.

### Major

- **Internal inconsistency in the main results figure (Figure 4 right vs. Table 4).** The sequence-similarity breakdown in Figure 4 (right) reports Top-1 rates of 51%, 53%, and 53% for the three bins, with a weighted average of ~52%. Table 4 reports the same breakdown with the same bin counts (109, 76, 123) but PB-validity rates of 72%, 79%, and 87%—yielding a weighted average of ~80% that is consistent with the claimed overall 79.9%. The paper does not acknowledge or explain this discrepancy. Because Figure 4 is the central evidence for generalisation to unseen proteins, this inconsistency casts doubt on the reliability of the experimental reporting. The discrepancy must be resolved—either the figure contains an error, or the two panels measure different quantities and the captions are misleading.

- **Comparison fairness: the ranking heuristic overlaps with the evaluation metric.** SIGMADOCK selects its top pose using a heuristic that combines pseudo-binding energy with _physicochemical checks_ (bond angles, bond lengths, internal energy). The ablation shows that removing the PB-scoring component reduces PB-valid Top-1 from 79.9% to 70.8% (Table 1, row E vs. I). The physicochemical checks directly correlate with the PoseBuster validity criteria used as the evaluation metric. The baselines (DiffDock, G2G, Vibe2, Lando2, Rerank2) do not employ such a heuristic; they use learned confidence models or geometric clustering. The reported performance gap is therefore not a clean comparison of generative quality—it conflates the model's generative ability with a post-hoc filter explicitly targeting the evaluation metric. A fair comparison would require either applying the same physicochemical filtering to baseline outputs, or reporting SIGMADOCK's performance with energy-only ranking as the primary number.

- **Headline claim about surpassing classical physics-based docking lacks a direct benchmark comparison.** The paper states that SIGMADOCK is the first deep learning method to surpass classical physics-based docking under the PB split. However, the main comparison figure (Figure 4 left) does not include any classical docking methods. Vina results appear only in the pocket-sensitivity analysis (Table 3), where it achieves 56–57% Top-1—lower than SIGMADOCK at 80%, but the comparison is indirect and not prominently featured. The abstract's framing would benefit from showing the classical-docker baseline directly in the main benchmark alongside SIGMADOCK, with the same metric and seed protocol.

### Minor

- **Ambiguous figure labeling for baseline comparisons.** The left panel of Figure 4 reports "PB (%)" and "AX (%)" for baselines without specifying whether these numbers are RMSD-only, PB-valid, or some other metric. The paper states that "SIGMADOCK achieves a 6.3× higher PB-validity than DiffDock," which implies DiffDock's PB-valid rate is ~12.7% (79.9/6.3), but the figure shows 38% for DiffDock on PB. The reader cannot determine what the figure's baseline numbers represent, making the visual comparison potentially misleading.

- **The abstract's 12.7–32.8% range for prior deep learning approaches is not sourced or tied to specific methods/figures.** The text should cite which methods produce the lower and upper ends of this range and clarify that these are PB-valid rates (as opposed to the RMSD-only numbers possibly shown in the figure).

- **The sequence-similarity bar chart labels are ambiguous.** The first bin is labelled "≤ 0, 30" which reads as "≤ 0" in the figure table. This appears to be a formatting artifact for the range [0, 30) but should be clearly labelled.

### Trivial

- The two rows for "Ours" in Figure 4 (79.9 and 80.6) are not explicitly explained in the figure caption; the reader must cross-reference with the ablation table to infer that 79.9 is PB-valid Top-1 and 80.6 is RMSD < 2 alone.

## Nice-to-Haves

- Report SIGMADOCK's performance without the physicochemical ranking heuristic (e.g., using only energy-based or random selection among top seeds) as a separate column in the main comparison, so the reader can assess the raw generative quality separately from the selection method.
- Include a direct comparison with Vina (and ideally one more classical dockers like Glide) on the same PB-valid metric in the main benchmark figure.
- Add confidence intervals or per-complex variance for the Top-1 rates, particularly for the smaller sequence-similarity bins.
- Report inference runtime compared to DiffDock and other generative models, not just AF3.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *The fragmentation scheme is not fully characterized / stochastic merging could cause variability.* (Harsh critic) — The ablation in Table 1 row C quantifies the effect of removing fragment merging (RMSD < 2 drops from 80.5 to 74.4), and FR3D is stochastic by design to provide data augmentation. This is adequately addressed.

- *Theorem 1's implications are asserted but not empirically demonstrated.* (Harsh critic) — The paper's contribution is the proposed method; the theorem motivates the design choice. Empirical comparison with torsional models (G2G, Vibe2) is provided. The criticism is overly demanding.

- *The conformational manifold alignment error claim lacks quantitative summary in the main text.* (Harsh critic / Strength finder) — The paper references Appendix D.3 for the full histogram; a single example is shown in Figure 2b. This is a framing choice, not a flaw, as the appendix is expected to contain the detailed analysis.

- *Missing comparison to more classical docking methods in the main figure.* (Already covered in Major above, so merged.)

## Novel Insights

The paper's core insight—that the mapping from torsional increments to Cartesian displacements is ambiguous and non-local, making torsional diffusion ill-conditioned, and that operating on fragment SE(3)^m with product Haar measures produces a simpler learning task—is genuinely insightful and well-articulated via Theorem 1. However, the most novel observation is the interaction between the fragment merging strategy (FR3D) and the soft triangulation constraints: by merging fragments stochastically and then conditioning on cross-fragment distances, the model effectively reduces the learnable degrees of freedom while retaining the expressivity to capture dihedral angles. This combination of stochastic pre-processing with soft geometric conditioning during diffusion is a clever design pattern that could transfer to other molecular modelling tasks.

## Suggestions

1. **Resolve the Figure 4 / Table 4 inconsistency urgently.** Clarify which numbers are correct, ensure the figure and table measure the same metric, and state the metric explicitly in both places.
2. **Add a "no PB heuristic" column** to the main comparison (e.g., ranking by energy only) so the reader can separate generative quality from selection-h heuristic effects.
3. **Include classical docking methods** (at minimum Vina, ideally one more) in the main benchmark figure, using the same PB-valid metric.
4. **Label all figure metrics explicitly:** "RMSD < 2 Å (not PB-valid)" vs. "RMSD < 2 Å & PB-valid" for each bar/row.
5. **Cite the sources of the 12.7–32.8% range** and confirm these are PB-valid rates from prior methods on the same split.

## Score and Decision

I will now calibrate the score using the retrieved anchors.

**Round 1 bracket:** The low-anchor band (avg score 3.0) produced papers that are clearly weaker (e.g., generic docking papers with limited novelty or major flaws). The middle band produced DiffDock-Pocket (5.0, Reject) and the toric-variety paper (4.5, Reject). The high band produced FlexDock (8.0, Accept) and ShEPhERD (8.0, Accept) — strong papers with clean experiments and clear novel contributions. The SIGMADOCK paper has more novel methodology than the middle-band papers but has a significant inconsistency in its main results figure. **Round 1 bracket: 4.5–6.5.**

**Round 2 narrowing:** Comparing against anchors inside the bracket:
- *DiffDock-Pocket (5.0, Reject):* Incremental extension of DiffDock; clean experiments but limited novelty. SIGMADOCK has substantially more novel methodology but a more serious presentation flaw. They are comparable in overall quality.
- *Deep Confident Steps to New Pockets (6.0, Accept):* Novel benchmark contribution with well-executed experiments; some concerns about evaluation scope. SIGMADOCK's methodology is more novel, but the inconsistency issue makes the experiments less trustworthy.
- *IPDiff (6.25, Accept):* Novel idea (prior shifting/conditioning) with some evaluation concerns. Comparable in methodology novelty to SIGMADOCK, but with fewer experimental concerns.

Based on these comparisons, SIGMADOCK sits below the accepted anchors because the internal inconsistency in the main results figure and the comparison-hardness issue are concrete problems that cannot be ignored. The methodology is stronger than DiffDock-Pocket's, which is why it places above 5.0, but the experimental reporting issues prevent it from reaching the 6.0+ accept range. **Final score: 5.5, Decision: Reject.**

### Anchors consulted

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| kKXIYUi8ff (DynamicsDiffusion) | 3.00 | 1 | Much weaker; tangential topic |
| m9zWBn1Y2j (Ligand Conformation) | 3.00 | 1 | Much weaker; tangential topic |
| An87ZnPbkT (GNNAS-Dock) | 3.00 | 1 | Much weaker; limited novelty |
| 1IaoWBqB6K (DiffDock-Pocket) | 5.00 | 1,2 | Less novel method, cleaner experiments; comparable overall |
| FuXtwQs7pj (Toric varieties) | 4.50 | 1,2 | Novelty in diffusion on varieties but poor presentation |
| S4zpk61r6G (DiffMaSIF) | 4.67 | 1 | Surface-based protein docking; less directly comparable |
| gHLWTzKiZV (FlexDock) | 8.00 | 1,2 | Stronger paper; clean experiments, novel UFM framework |
| KSLkFYHlYg (ShEPhERD) | 8.00 | 1 | Stronger paper; comprehensive evaluation |
| UfBIxpTK10 (Deep Confident Steps) | 6.00 | 2 | Novel benchmark + training method; well-executed experiments |
| qH9nrMNTIW (IPDiff) | 6.25 | 2 | Novel idea, modest experiments; accepted despite concerns |
| jZPqf2G9Sw (Dynamics-Informed) | 5.50 | 1 | Protein design, not docking; comparable in quality |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>