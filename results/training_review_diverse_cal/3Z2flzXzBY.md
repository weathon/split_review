Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces PASLE (Progressive Adaptation with Selective Label Enhancement), a test-time adaptation framework that partitions target-domain test samples into confident and uncertain subsets based on a dynamic margin threshold. Confident samples receive one-hot pseudo-labels, while uncertain samples receive candidate pseudo-label sets (i.e., they retain multiple plausible classes). The model is trained progressively on both subsets, and the threshold decays over time as the model becomes better adapted. Experiments on four domain-generalization benchmarks and two corruption benchmarks (CIFAR-10-C / CIFAR-100-C) show consistent improvements over nine existing TTA methods.

## Strengths

- **Consistent and substantial empirical gains across diverse benchmarks.** On domain generalization datasets (Table 1), PASLE outperforms all baselines with average gains of 5.63% (ResNet-18) and 4.19% (ResNet-50). On corruption benchmarks (Table 2), it achieves improvements of 1.08% on CIFAR-10-C and 2.16% on CIFAR-100-C over the second-best method. These gains hold across two architectures and both domain-shift and corruption-shift settings, which is a strong indicator of practical effectiveness.

- **Ablation confirms the core mechanism drives improvement.** The PASLE-NC variant (which removes candidate-label training) degrades on every OfficeHome target domain (Table 3), and the sample utilization curves (Figure 1) show PASLE uses more effectively labeled samples over time. This directly attributes the improvement to the selective enhancement component rather than to confounding factors such as the optimizer or training objective.

- **Robustness to hyperparameters and batch sizes.** Sensitivity analysis (Figure 2a) shows stable accuracy across a wide range of threshold settings, and Figure 2b demonstrates that PASLE maintains its advantage under varying batch sizes — an important practical property for online TTA where batch size can fluctuate.

- **No additional inference-time computation.** The method does not require MC dropout, deep ensembles, or any architecture modification for uncertainty estimation, making it suitable for real-time deployment without modifying the backbone.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical analysis overclaims support for the method.** Proposition 1 is a conditional statement ("Assume the per-class deviation is bounded by τ(r)/2..."), but the paper never checks whether this assumption holds during adaptation, nor discusses what happens when it is violated. The paper then treats the derived splitting conditions as if they carry unconditional guarantees (e.g., "This strategy follows the derived proposition about uncertainty information," line 53). Moreover, Theorems 1 and 2 are standard domain-adaptation bounds (Ben-David et al., 2010; Zhang et al., 2019) and a generic risk bound involving pseudo-label error — neither theorem mentions candidate label sets, selective partitioning, threshold schedules, or any mechanism unique to PASLE. The paper states these theorems "demonstrate that our framework can achieve a tighter generalization bound" and that "these actions can make the corresponding pseudo-label's label distribution closer to the Bayes class-probability distribution," but no formal link between the algorithm and the theorems is provided. The empirical work is strong enough to stand on its own; the paper would be more credible if it either (a) grounded the threshold schedule in a measurable quantity or (b) dropped the pretense that the theory specifically validates PASLE's design choices.

2. **The threshold scheduling (Eq. 9) is entirely heuristic, and its sensitivity is underexplored.** The three hyperparameters τ_start, τ_des, and τ_end control which samples receive one-hot labels, which receive candidate sets, and which are deferred to the buffer, yet no principled method for setting them is given. The gap is fixed at 0.1 and τ_des at 1e-3 across datasets with very different numbers of classes (5 to 345). The sensitivity analysis (Figure 2a) covers only one corruption type (shot noise). Given that the entire partitioning logic depends on this schedule, broader sensitivity analysis across different shift types (e.g., weather corruptions, domain gaps like painting in PACS) is needed to establish that the method is not brittle under the chosen defaults.

### Minor

1. **The text says "ten" baselines but lists only nine** (line 202 vs. lines 204–212). TAST and TAST-BN are counted as two, which accounts for the list having 9 entries — but then the total should be nine, not ten. This is a minor factual error that should be corrected.

2. **The buffer selection heuristic (top-K margin, Eq. 8) is introduced without justification or ablation.** Retaining samples with the largest margin seems reasonable, but the paper does not compare to alternatives such as random retention, confidence-based retention, or FIFO. The buffer capacity (K = quarter of batch size) is also not ablated. Since the buffer feeds samples back into training at future steps, the design choice matters.

3. **The theorems are generic and do not formally connect to PASLE's specific mechanisms.** While not fatal (the empirical evidence is the main contribution), the paper's framing (lines 19, 53) implies that the theory validates the method's design. A reader expecting a bound that depends on candidate-set cardinality or the threshold schedule will be disappointed. The theory section would be more honest if framed as general motivation for why adding well-supervised target samples is beneficial, rather than as a formal analysis of PASLE.

### Trivial
None beyond the issues already raised.

## Nice-to-Haves

- Compare the candidate-label approach to a soft-label baseline (i.e., using the full softmax vector as supervision) to test whether the discreteness of candidate sets is beneficial.
- Ablate the buffer retention strategy (top-K margin vs. confidence-based vs. random vs. FIFO).
- Provide empirical validation of Proposition 1's assumption on at least one dataset by measuring per-class deviation on a held-out labeled target subset.

## Removed Points

These points were flagged by reviewers but removed or downgraded after cross-checking against the paper:

- **"Missing recent TTA methods such as EcoTTA (2023) or SAR (2023)"**: Removed per guidelines — the instruction is to not criticize missing related works without external confirmation of their relevance at the time of submission.
- **"The paper should not claim no additional inference-time computation because PASLE requires a forward pass"**: Removed — this claim is standard and comparable to most lightweight TTA methods; the paper is distinguishing from methods that require MC dropout or ensembles, which is a fair distinction.
- **"Strength: Selective label enhancement with theoretical grounding"**: Downgraded/removed — conflicts with the verified weakness that the theoretical grounding is overstated. The strategy exists and works; the "theoretical grounding" part is not as solid as claimed.

## Novel Insights

None beyond the paper's own contributions. The reviewers' primary insights converge on the gap between the paper's theoretical framing and the actual specificity of the analysis, but this is a critical observation about presentation rather than a novel research insight.

## Suggestions

1. **Reframe the theoretical contribution.** Either (a) provide a bound that explicitly involves candidate-set cardinality or the threshold schedule, or (b) drop the claim that the theory specifically validates PASLE and instead present the theorems as general motivation for why adding supervised target samples helps, with the method standing entirely on empirical evidence.

2. **Expand sensitivity analysis** to cover at least one domain-shift setting (e.g., a painting target in PACS) and one additional corruption family (e.g., blur or weather) to establish that threshold robustness is not specific to shot noise.

3. **Ablate the buffer retention heuristic** (top-K margin vs. alternative strategies) and the buffer capacity setting.

4. **Correct the baseline count** (line 202) from "ten" to "nine."

## Score and Decision

The paper has a genuinely interesting core idea — using candidate label sets for uncertain TTA samples — and backs it with strong, consistent empirical results across multiple benchmarks and architectures. The theoretical overclaiming is a real weakness, but it does not invalidate the empirical contribution. With revisions to either validate or drop the theoretical pretense, this is a solid contribution to the TTA literature.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>