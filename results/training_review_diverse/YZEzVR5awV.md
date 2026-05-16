Now I have all the information I need. Let me construct the final consolidated review.

## Summary

ClusComp proposes a clustering-based model compression paradigm for LLMs that: (1) clusters weight matrices into FP16 codebooks, (2) refines these codebooks via block-wise error minimization with fixed codes, and (3) supports efficient finetuning by updating only the codebook parameters (<1% of total). The method avoids the outlier sensitivity that plagues uniform quantization at low bit-widths, consistently outperforms baselines at 2–4 bits, extends to 1-bit via recovery training, and demonstrates finetuning performance competitive with full FP16 finetuning.

## Strengths

- **Consistent compression gains at 2–4 bits across multiple LLM families.** Table 2 shows ClusComp achieves the lowest perplexity in 9 of 12 cases at 4-bit, and at 2-bit all tested models stay below 13 perplexity on WikiText2 — a regime where competing methods (GPTQ, OmniQuant, etc.) degrade substantially. The flatter accuracy curve in Figure 4 further indicates reduced sensitivity to bit-width reduction.

- **Clean motivation grounded in outlier analysis.** The pilot study (Section 3.1, Figure 2) documents rising kurtosis from Llama-1 to Llama-3, directly tying the increasing difficulty of uniform quantization to outlier growth. ClusComp's design — storing centroids in FP16 rather than forcing outliers into a quantization grid — follows naturally from this observation, and the paper confirms that even the clustering-only variant (ClusComp⁻) already beats RTN, GPTQ, and AWQ on the pilot models.

- **Principled code-fixed design for block-wise error minimization.** Section 3.2.3 motivates why only codebooks are trained (codes kept as fixed indices): it prevents overfitting with few (128) calibration samples and avoids mode collapse in the large codebook space. The uniform code distribution shown in Figure 3 supports this rationale.

- **Multimodal generalization.** Table 3 shows ClusComp compressing LLaVA-Next-8B to 2-bit with non-trivial retained performance, while GPTQ and AWQ produce unusable outputs at the same bit-width — demonstrating applicability beyond language-only models.

- **Parameter- and memory-efficient finetuning.** The codebook-only update paradigm (Section 3.2.4) enables finetuning with <1% trainable parameters and 42 GB GPU memory for Llama-3-70B, while avoiding the expressiveness bottlenecks of LoRA-based approaches.

## Weaknesses

### Fatal
None.

### Major
None.

The remaining issues after filtering are all at the minor or nice-to-have level — none threaten the core claims.

### Minor

- **Baseline numbers are borrowed, not re-run under identical conditions.** The paper states (line 143): "All baseline results are directly borrowed from the original works or their follow-up works." While this is common practice in the PTQ literature, it introduces uncontrolled variance from differing calibration sets, sequence lengths, and evaluation harnesses. The paper's claim that "the majority of the aforementioned baselines utilize comparable resources" (line 145) is a hand-wavy hedge rather than a controlled comparison. The consistent superiority claimed at 2-bit would be more convincing if GPTQ, AWQ, and OmniQuant were re-run with the same 128 WikiText2 calibration sentences and 2048 sequence length used for ClusComp.

- **No systematic ablation isolating the contribution of each pipeline stage.** The paper defines three variants (ClusComp⁻, ClusComp, ClusComp⁺) but never presents a single table comparing all three at each bit-width across the full model zoo. ClusComp⁻ appears only in the pilot study (Figure 2, two models), and ClusComp⁺ results are only discussed for the extreme 1-bit case. A direct ablation (e.g., a column for each variant in Table 2) would cleanly quantify how much block-wise error minimization and recovery training each contribute.

- **No sensitivity analysis on the grouping dimension g.** The reshaping dimension g is fundamental — it directly determines bit-width (Equation 3) and clustering quality — yet the paper only mentions g=4 as an example with no analysis of how g=2, g=8, or other values affect the trade-off between compression ratio and reconstruction error.

- **Multimodal 2-bit claim lacks quantification.** The paper states that at 2-bit "none of the baselines produce correct outputs" for LLaVA-Next (Table 3), but does not report what "correct outputs" means or provide the actual accuracy/score where baselines failed. Reporting the numeric values (even if near-zero) would make the comparison precise rather than rhetorical.

- **Computational cost of K-means for large models is not reported.** Clustering millions of vectors (d_in·d_out/g) into up to 65K centroids for a 70B model has non-trivial time cost. The paper mentions "2GB memory" and scalability via parallelization across GPUs, but gives no wall-clock time — a significant omission for practitioners assessing practical viability.

### Trivial
- The pilot study establishes that kurtosis increases and quantization degrades, but stops short of directly plotting reconstruction error (MSE) of clustering against layer kurtosis to cement the motivation. This would strengthen the logical chain but is not required for the paper's validity.
- The "256 samples from C4 validation set" is a non-standard subset size; most works use the full validation set. Variability from this choice is not discussed.

## Nice-to-Haves
- **A controlled re-implementation of main baselines** (GPTQ, AWQ, OmniQuant) using the same calibration data would eliminate the largest source of uncertainty in the comparison. This is the single most impactful addition the authors could make.
- **Sensitivity analysis on number of centroids n.** The paper constrains n < 2^16 to use 16-bit integer codes. Showing how perplexity varies with n for a fixed g would help users navigate the bit-width/quality trade-off.
- **Explicit discussion of limitations** (time cost, sensitivity to centroids, inability to reassign codes) would improve the paper's scholarly completeness.
- **Clarify the task(s) on which the 1-bit accuracy numbers (51.4 for Llama-3-70B, 57.8 for Llama-3-8B) are reported.** The abstract mentions these values, but Section 4.2 does not specify the evaluation task.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"Finetuning evaluation is missing from the provided text."** The parsed paper ends at Section 4.2, but Section 4.3 (finetuning experiments) and the appendix are present in the original submission — the parser strips these sections from all papers. The claim that finetuning results cannot be assessed is an artifact of the parsing pipeline, not an author omission.

- **"The paper does not compare to recent STE-based finetuning methods (QA-LoRA, LoftQ)."** This demands broader baseline coverage than is standard. The paper already compares to QLoRA, the most widely used method in this space. Expanding to every variant is scope creep for a single paper.

- **"Hyperparameter choices for K-means are not specified in the main text"** and **"Recovery training details missing."** These details belong in the appendix (Section B), which was stripped by the parser. The original submission contains them.

- **"Connection between higher kurtosis and clustering effectiveness is not empirically established."** The paper's claim is that increasing outliers makes *uniform quantization* harder, which motivates *clustering* (storing values in FP16) as an alternative. The logical chain is: outliers hurt uniform quantization → clustering bypasses the quantization grid entirely → ClusComp works well. This is already sound; a separate MSE-vs-kurtosis plot is a strengthening suggestion, not a missing link.

## Novel Insights

None beyond the paper's own contributions. The reviews surface expected trade-offs (borrowed baselines, missing ablations) that are common in compression papers, but do not offer a fundamentally new angle on the work.

## Suggestions

1. Re-run the main baselines (GPTQ, AWQ, OmniQuant, QuIP) using your exact calibration setup (128 WikiText2 sentences, seqlen 2048) and report them in the same table as ClusComp. This single change would eliminate the largest source of reviewer skepticism.
2. Add an ablation table showing perplexity/accuracy for ClusComp⁻, ClusComp, and ClusComp⁺ at each bit-width across Llama-2-7B, Llama-3-8B, and Llama-3-70B.
3. Report wall-clock time for clustering the 70B model on the A6000.
4. Include a brief sensitivity analysis on g (e.g., g ∈ {2, 4, 8}) for one representative model.
5. Report the actual numeric scores for baselines at 2-bit multimodal evaluation, even if they are very low, rather than the qualitative "not correct outputs."

## Score and Decision

The paper presents a clean, well-motivated method with strong empirical results and a plausible theoretical rationale (bypassing outlier-sensitive quantization via FP16 codebooks). The weaknesses — borrowed baselines, missing ablations, and absent sensitivity analyses — are genuine but do not invalidate the core contribution; they are standard gaps in a conference submission that can be addressed in a revision. The method's ability to simultaneously serve as both a compression technique and a parameter-efficient finetuning paradigm that avoids STE tricks is a genuinely useful contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>