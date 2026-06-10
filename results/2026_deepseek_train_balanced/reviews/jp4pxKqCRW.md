I have verified all claims against the paper. The key findings are confirmed: the experimental section (Section 5) is structurally empty, the central hyperparameter d_extra is never specified, the base model is never named, and all quantitative performance claims in the abstract/introduction/conclusion are unsupported. Let me produce the final review.

## Summary

This paper proposes periodic extension of RoPE positional encodings in high-dimensional (low-frequency) subspaces for long-context extrapolation in LLMs. The core idea is to keep low-dimensional subspaces as direct extrapolation while periodically extending high-dimensional subspaces beyond the training length, using either naive periodic replication (Extra-PE) or mirrored periodic replication (Extra-MPE). A three-category taxonomy (position interpolation, outward expansion of visible area, inward convergence) is introduced to frame the approach.

## Strengths

1. **Novel three-category taxonomy for RoPE extrapolation methods (Section 3, Figure 3).** The classification into position-index interpolation, outward expansion of the visible encoding area, and inward convergence goes beyond the "increase base vs. decrease base" dichotomy common in prior work and correctly identifies that no prior method occupies the "inward convergence" category, providing a principled motivation for the proposed approach.

2. **Positional encoding distribution within training length is exactly preserved (Equation 4, lines 190–191).** The method only modifies the encoding when seq_len > L_train AND dim ≥ d_extra/2 − 1; at all other times the encoding is identical to original RoPE. This is a principled difference from interpolation-based methods (PI, NTK, YaRN) that alter the base value and therefore change the attention distribution within the training range.

3. **Mirrored extension addresses the discontinuity flaw of basic periodic extension (Equations 5–8, Section 4.2).** Extra-MPE explicitly handles the discontinuity at period boundaries that arises in Extra-PE. This shows the authors identified and mitigated a practical failure mode of their own design.

## Weaknesses

### Fatal

1. **Experimental section is effectively empty — all quantitative claims are unsupported.** Section 5 ("EXPERIMENTS") contains no experimental data. Section 5.1 ("TRAINING") consists of the single character "1." (line 246). Section 5.2 ("EVALUATIONS") is one sentence: "we need to conduct detailed experimental comparisons" (line 248). The paper then jumps to the conclusion. Despite this, the abstract (line 7), introduction (lines 23, 25), and conclusion (lines 251–254) make very specific quantitative performance claims: 4× training efficiency over YaRN, surpassing NTK-32k, approaching YaRN-64k, and an 8k-fine-tuned model extrapolating to 80k without perplexity explosion. **None of these claims are supported by any results, tables, metrics, or experimental descriptions in the paper body.** For a paper whose core contribution is an empirical method for long-context extrapolation, this is a fatal structural flaw — there is no way to evaluate whether the method works or whether the claimed advantages are real.

### Major

2. **The key hyperparameter d_extra is never specified or analyzed.** The dimension threshold d_extra — which determines how many of the d/2 subspaces receive periodic extension versus direct extrapolation — is the central design decision. It is introduced (line 169) and used in Equations 4 and 8 (lines 190–191, 224–226), but its value is never given and no guidance on how to select it is provided. Without this parameter, the method cannot be reproduced.

3. **The base model for experiments is never named.** The paper mentions LLaMA in related work but never states which specific model was fine-tuned (e.g., LLaMA-7B, LLaMA-13B). Combined with the missing experimental section, this makes the paper's empirical claims completely unverifiable.

4. **No experimental setup is described.** Even if we charitably assume the missing experimental data was a parser issue, the paper still fails to specify the training dataset, evaluation benchmarks, training hyperparameters, or comparison protocols. The conclusion claims results on "long-context summarization and QA tasks" but no datasets are identified.

### Minor

5. **The "theoretical perspective" (Section 3) is purely descriptive/pictorial.** The three-category taxonomy is a useful framing device, but it produces no testable predictions, no quantitative bounds on when periodic extension would succeed or fail, no analysis of approximation error from periodic replication, and no characterization of how periodicity affects position distinguishability. The paper presents this as "a new theoretical perspective" (Contribution 1) but it remains at the level of geometric intuition.

6. **The "first effective out-of-domain" claim (lines 19, 162) is overstated.** All RoPE modification methods (NTK, YaRN, reduced-base) address out-of-distribution positions — they simply do so through interpolation rather than periodic extension. Claiming to be the "first" effective OOD method requires a narrower definition that the paper does not clearly justify.

### Trivial

7. The abstract and conclusion refer to "extensive experimental results" and "corresponding comparative experiments" using past tense ("we conducted," "it is found"), creating a mismatch with the empty experimental section that could mislead readers.

## Nice-to-Haves

- An ablation of d_extra across the full range of dimensions would strengthen claims about robustness.
- Analysis of the aliasing introduced by periodic extension (multiple positions beyond L_train mapping to the same encoding) and when this harms performance on position-discrimination tasks would be valuable.

## Removed Points

- **Grammar/style nitpicks and OCR artifacts**: Removed per hard rules — these are parser artifacts, not author errors.
- **Criticism about missing appendix/missing proofs**: Removed per hard rules — the parser strips these sections from all papers.
- **"Figures absent from text"**: The figures appear as image references; in the original submission they would be present. Not a valid weakness.
- **Strength: "Non-zero attention at ultra-long distances"**: This is claimed but not evidenced in the paper body. Removed as unsubstantiated.
- **Strength: "Fine-tuning efficiency claim"**: Claimed but never evidenced. Removed as unsubstantiated.
- **Generic strengths about problem importance**: Removed as non-specific.

## Novel Insights

None beyond the paper's own contributions. The core insight — periodic extension of high-dimensional RoPE subspaces to handle OOD positions without modifying in-distribution encoding — is the paper's own novel contribution. The reviews did not surface any new synthesis beyond what the paper itself offers.

## Suggestions

1. **Complete the experimental section before resubmission.** Specify the base model, training data, hyperparameters (including d_extra), evaluation benchmarks (e.g., LongBench, GovReport, scrolls), and report perplexity curves and task performance comparing Extra-PE, Extra-MPE, direct extrapolation, PI, NTK-aware, NTK-by-parts, and YaRN across multiple context lengths.
2. **Ablate d_extra systematically** to show how performance varies with the threshold dimension.
3. **Tone down the "first effective out-of-domain" claim** or define the scope precisely so it is not misleading.
4. **Ensure all specific quantitative claims** (4× efficiency, 80k extrapolation from 8k training, etc.) are backed by tables or figures.

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>