- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 8, 6, 6, 6
I now have all the evidence I need. Let me compose the final consolidated review.

## Summary

This paper proposes PASLE (Progressive Adaptation with Selective Label Enhancement) for test-time adaptation. Instead of assigning definite (one-hot) pseudo-labels to all test samples, PASLE partitions data into confident and uncertain subsets based on Proposition 1's conditions: confident samples receive one-hot labels while uncertain samples receive candidate pseudo-label sets. A dynamic threshold that decays over adaptation steps progressively refines these candidate sets. The model is trained on both subsets using cross-entropy loss for confident samples and classifier-consistent loss for candidate-labeled samples. Experiments on four domain generalization benchmarks and two corruption benchmarks show consistent accuracy improvements over the compared baselines.

## Strengths

1. **Novel application of candidate label sets to TTA (Section 3.3).** The idea of using candidate pseudo-label sets (rather than one-hot or soft labels) for uncertain test samples is a clean and principled departure from prior TTA methods. Proposition 1 provides a formal condition for when a label can be safely assigned or excluded, giving the partitioning logic a theoretical grounding that direct confidence-thresholding approaches lack.

2. **Progressive refinement via dynamic threshold (Eq. 9, Algorithm 1).** The monotonic decay of \(\tau(r)\) as the model adapts is a well-motivated mechanism: as the model becomes better aligned with the target distribution, the confidence threshold relaxes, and candidate sets shrink accordingly. This directly addresses the limitation identified in the paper — that definite pseudo-labels cannot be flexibly refined.

3. **Consistently strong empirical results (Tables 1 and 2).** PASLE achieves the best accuracy across all six benchmarks (PACS, VLCS, OfficeHome, DomainNet, CIFAR-10-C, CIFAR-100-C) for both ResNet-18 and ResNet-50 backbones, with improvements of up to 5.63% on domain generalization benchmarks. The gains are especially notable on DomainNet, a large-scale dataset with 345 classes.

4. **Ablation confirms the core idea (Table 3).** The PASLE-NC variant (which removes candidate labels and only trains on confident samples) consistently underperforms full PASLE on OfficeHome. This directly demonstrates that the candidate-label component is responsible for a meaningful portion of the improvement, not just the confident-sample filtering.

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical analysis does not analyze the proposed mechanism.**  
   Theorem 1 is a standard domain-adaptation generalization bound (Ben-David et al., 2010) applied to a setting that assumes *true labels* on target samples ("which are then labeled with the true labeling function"), not the pseudo-labeled TTA scenario. Theorem 2 bounds the empirical risk gap by \(\mathbb{E}[\|q-p\|_2]\) but merely *asserts* that PASLE's candidate labels reduce this distance relative to one-hot pseudo-labels — it does not prove or formally analyze why. The contribution bullets claim to "theoretically establish a generalization bound for TTA" and "quantify the effectiveness of pseudo-labels," but neither theorem provides method-specific insight into PASLE's selective label enhancement, dynamic threshold, or candidate set construction. The theory is ornamental, not evidential.

2. **Incomplete baseline set for claiming state-of-the-art.**  
   The paper compares against 9 methods (ERM, BN, TENT, PL, SHOT-IM, T3A, TAST, TAST-BN, TSD) but omits several well-established TTA methods that handle uncertainty or noisy pseudo-labels: MEMO (Zhang et al., 2022), CoTTA (Wang et al., 2022), EATA (Niu et al., 2022), SAR (Niu et al., 2023), and RoTTA (Yuan et al., 2023). Several of these are cited in the related work section but not included experimentally. Given the 2026 publication context, these are not obscure methods. Without these comparisons, the claim of outperforming "all the compared approaches" (line 294) is technically correct but does not support a broader state-of-the-art claim.

3. **Ablation study is far too thin.**  
   Only one variant is tested: PASLE-NC removes candidate labels entirely. This shows the candidate-label component matters, but the paper introduces several additional design choices that are not isolated: (a) the dynamic threshold schedule (Eq. 9) vs. a fixed threshold, (b) the specific classifier-consistent loss (Eq. 3) vs. standard cross-entropy on the most-likely class from the candidate set, (c) margin-based buffer selection (Eq. 8) vs. random buffer or no buffer, and (d) the candidate set generation rule (Eq. 7) vs. simply using soft labels as targets. The paper's central thesis is that *progressive refinement* of *uncertainty-aware* pseudo-labels drives improvement, but the evidence only rules out the strawman of discarding uncertain samples entirely. Which specific component contributes most to the gains is unknown.

### Minor

1. **Proposition 1's assumption is strong and unverified.**  
   The proposition assumes \(|f_j(\mathbf{x};\Theta^r) - f_j(\mathbf{x};\Theta^*)| \le \frac{1}{2}\tau(r)\) for all classes \(j\). This bounds the gap between the current model and the optimal target classifier uniformly across classes — a strong condition, especially early in adaptation when the shift is largest. The paper does not discuss how to set \(\tau(r)\) based on this bound or validate the assumption empirically.

2. **No statistical significance or variability reporting on main results.**  
   Tables 1 and 2 report only point estimates of accuracy. Table 3 (the ablation) includes standard deviations, suggesting variability exists. Without error bars on the main results, it is unclear whether the reported margins over the second-best method are meaningful or within the noise of the evaluation. This is especially relevant for CIFAR-10-C where the margin is only 1.08%.

3. **Buffer selection biases toward nearly-confident samples without analysis.**  
   The buffer retains samples with the largest margins (Eq. 8), which are those closest to the confidence threshold. The paper states these "are likely to contribute to model updates earlier" but provides no analysis of whether this selection helps or harms compared to alternatives (e.g., random retention or retaining the most uncertain samples). This is a non-trivial design choice that could affect early-stage adaptation dynamics.

4. **Threshold schedule is ad hoc.**  
   The linear decay \(\tau(r) = \max\{\tau(r-1) - \tau_{\text{des}}, \tau_{\text{end}}\}\) is motivated by "the model becomes increasingly aligned with the target domain" but no justification or comparison with other schedules (e.g., exponential decay, validation-based scheduling) is provided. Three interrelated hyperparameters (\(\tau_{\text{start}}, \tau_{\text{end}}, \tau_{\text{des}}\)) control this schedule, and sensitivity analysis only covers \(\tau_{\text{start}}\) and \(\tau_{\text{end}}\) on a single corruption setting (shot noise on CIFAR-10-C).

### Trivial

1. **Equation (7) is incomplete.** Line 103 shows the candidate label assignment with only the condition for exclusion (value 0) but no else case. The intended meaning (classes not excluded remain in the candidate set) is inferable but the exact formulation must be unambiguous for reproducibility.

2. **Minor inconsistency in baseline count.** The paper claims "ten online TTA approaches" (line 202) but lists only nine (lines 204–212).

## Nice-to-Haves

- A diagnostic experiment tracking candidate-set quality over time (e.g., how often the true label is contained in the candidate set, the average cardinality of candidate sets, and the accuracy of confident-set labels) would directly support the claim that uncertain pseudo-labels are being refined correctly as adaptation progresses.
- Runtime or computational cost comparison with baselines would be useful, as PASLE introduces additional loss computation and buffer management that online TTA methods usually try to minimize.
- A discussion of failure cases: what happens when the distribution shift is large enough that very few samples meet the confidence condition early in adaptation?

## Removed Points

- **Introduction conflates definite labels with all existing approaches**: The paper says "most existing TTA approaches rely on definite pseudo-labels" (abstract) which is accurate — it does not claim all. The related work section explicitly discusses entropy minimization methods (including MEMO and EATA/SAR). Removed because the criticism is factually inaccurate about what the paper claims.
- **Theoretical section assumes supervised adaptation (labeled target samples)**: Kept as part of weakness #1 (Major) — this is correct but is subsumed under the broader criticism of ornamental theory.
- **Hyperparameter selection via source validation domain may not reflect real-world adaptability**: This is the standard protocol established by Gulrajani & Lopez-Paz (2021) and widely used in TTA papers. Removed as scope creep.
- **Reproducibility concerns about code or hyperparameter disclosure**: The paper gives training details (Adam, learning rate range, batch size 128, buffer size 32, \(\tau_{\text{des}}\) values, \(\tau_{\text{start}}\) class-dependent) and follows standard TTA reporting practices. Removed as insufficiently specific.
- **Missing limitations/broader impact section**: Not required for this venue's format. Removed.
- **Sample utilization plot (Figure 1) only compares against PASLE-NC**: This is an ablation analysis figure; its purpose is to compare PASLE vs. its variant, not against all methods. Removed.

## Novel Insights

The two reviews together surface a clear pattern: the paper's empirical contribution is solid and well-executed, but the theoretical framing substantially overclaims what is actually proven. The harsh critic's decomposition of the theory into (a) a generic bound that doesn't touch the method and (b) an asserted-but-unproven claim about candidate labels reducing the \(\|q-p\|_2\) distance, combined with the strength finder's over-valuation of that same theory, reveals a gap between how the paper presents its theoretical contribution and what it actually delivers. A more honest framing — Proposition 1 as a sufficient condition for safe partitioning, and the two theorems as contextual motivation rather than method-specific guarantees — would better match the evidence. A second synthesis point is that the ablation gap is systematic, not incidental: the paper makes several design choices (threshold schedule, margin-based buffer, candidate generation rule) but tests only one binary comparison (with/without candidate labels), so the internal engineering contribution is largely unvalidated.

## Suggestions

1. **Add missing TTA baselines** (MEMO, CoTTA, EATA/SAR, RoTTA) to the experimental comparison. This is the most important single fix — without it, the claimed superiority is unsubstantiated relative to the methods the community actually uses as reference points.

2. **Expand the ablation study** to isolate at minimum: (a) dynamic threshold vs. fixed threshold, (b) classifier-consistent loss vs. standard cross-entropy on the argmax from the candidate set, (c) buffer with margin selection vs. random buffer vs. no buffer.

3. **Reframe or remove the theoretical analysis.** Either derive a bound that specifically incorporates candidate label sets and the dynamic threshold, or explicitly position Theorems 1 and 2 as general background motivation and remove the claim that they "establish" or "quantify" the method's effectiveness.

4. **Add confidence intervals or error bars** to the main result tables (Tables 1 and 2) to establish that the reported margins are statistically reliable.

5. **Add a diagnostic experiment** tracking candidate-set quality over time (true label containment rate, average candidate set size, confident-set accuracy) to directly visualize the progressive refinement claim.

6. **Fix the incomplete equation** (Eq. 7) and clarify the baseline count.
