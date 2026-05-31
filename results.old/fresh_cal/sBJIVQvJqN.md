Now I have all the information needed. Let me compose the final consolidated review.

## Summary

The paper proposes WFPP (Word-Frequency-based Image-Text Pair Pruning), which adapts the word subsampling technique from Word2Vec (Mikolov et al. 2013) to prune entire image-text pairs containing high-frequency words from VLM pre-training data. The method computes word frequencies, assigns each word a discard probability (inverse to frequency), computes a text-level score as the joint probability of word discard, and sorts/selects texts accordingly. Experiments on CC3M and CC12M with CLIP/ViT-B-16 show that using 80% of the data, WFPP achieves comparable performance to full-data CLIP, and at 90% it slightly outperforms the full baseline across many benchmarks.

## Strengths

1. **Computation reduction with maintained/improved performance**: On CC12M, using 80% of samples (83.3% of computation), WFPP achieves 35.0% zero-shot ImageNet accuracy after fine-tuning vs. CLIP's 34.8% on full data; at 90% samples it reaches 35.5%, exceeding the full baseline by 0.7% (Table 1, lines 256-260).

2. **Significant improvement over random pruning**: WFPP at 50% data outperforms random pruning by 1.7% without fine-tuning (29.8 vs. 28.2) and 1.1% with fine-tuning (31.3 vs. 30.2), confirming that frequency-based selection matters beyond simple data reduction (Table 1, lines 252-256).

3. **Mechanism validated via first/second-half split**: Texts sorted by descending S(t_j); the first half (lower-frequency words) outperforms the second half (higher-frequency) by 8.7% without fine-tuning (Table 6, line 461-463), directly confirming that the pruning direction (removing texts with frequent words) is beneficial. Figure 2 further visualizes that high-frequency words like "person" (34.59% retention) and "background" (22.31%) are retained far less than under random pruning.

4. **Consistent gains across diverse benchmarks**: WFPP at 90% surpasses CLIP by 0.81% on average across 26 classification datasets (33.94% vs. 33.13%, Table 3, line 334), and on 6 robustness datasets it matches CLIP at 80% data (27.44% vs. 27.42%) and beats it at 90% (27.69%, Table 2, line 290).

5. **Ablations confirm design choices**: Removing text-length normalization drops accuracy by 2.6% on CC12M (29.8→27.2, Table 12, lines 528-530); pruning by text length alone degrades below random (22.6 vs. 28.2, Table 7, line 478), showing both the frequency-based selection and the normalization are necessary.

## Weaknesses

### Fatal
None.

### Major

1. **Table 1 numerical example is inconsistent with the stated equations.** The paper defines S(t_j) = (1/n)(1 − ∏P(w_i)) with P(w_i) = 1 − sqrt(t/f(w_i)). Using the f(w_i) values shown (0.9980 for "a," 0.8342 for "barcode," etc.) and t=10⁻⁷, the computed S values are ~0.0003 — **three orders of magnitude smaller** than the reported 0.20479 and 0.24249. Furthermore, the f(w_i) values themselves (where "a" = 0.9980, meaning 99.8% of all word occurrences) are implausible as standard word frequencies for any real corpus. The table row labeled "f(w_i)" does not match Eq. 1's definition, and the reported S values cannot be derived from the stated equations using any consistent interpretation of the shown numbers. While the method itself is clearly defined by the equations and the experimental pipeline likely uses the correct implementation, this example — the only illustrative worked example in the paper — is broken, making the method presentation unreliable. The authors must either correct the table or clarify what is actually being reported.

2. **MetaCLIP comparison is too thin to support the claimed superiority.** The only direct comparison is on CC3M at a single pruning ratio (50%), where WFPP leads by 0.3–0.5% (Table 5, lines 418-420). No comparison is shown on the larger CC12M dataset, at different pruning ratios, or with variance estimates. Improvements of this magnitude are within typical run-to-run variation, and without multiple seeds or a richer comparison, the claim that WFPP "outperforms MetaCLIP" (line 573) is insufficiently supported.

### Minor

3. **Asymmetric fine-tuning comparison.** WFPP models are pre-trained on a pruned subset for 30 epochs **then fine-tuned on the full dataset for 1 additional epoch** (31 total epochs of gradient updates). The CLIP 100% baseline is trained on full data for 30 epochs with no fine-tuning (Table 1, line 251). This means the headline comparison (WFPP 80% at 35.0% vs. CLIP at 34.8%) confounds the pruning benefit with an extra epoch of exposure to the full data. The paper partially mitigates this by reporting w/o ft results (where WFPP 80% = 34.3 vs. CLIP = 34.8, and WFPP 90% = 34.9 already beats CLIP's 34.8), but the asymmetric comparison in the main claims should be acknowledged and ideally controlled (e.g., by also fine-tuning CLIP for 1 more epoch).

4. **No variance or statistical significance reported.** Many improvements are in the 0.3–1% range, especially on the MetaCLIP comparison (0.3–0.5%), which could be within random seed variation. The paper reports single-run results throughout with no standard deviations, confidence intervals, or multi-seed experiments.

5. **Threshold t=10⁻⁷ is not ablated.** The choice of t is adopted from Mikolov et al. 2013 but is not varied or justified for the VLM setting. The sensitivity of results to this hyperparameter is unknown.

6. **Discrepancy between Figure 1 and Table 1.** Figure 1's caption claims "approximately 77% of the image-text pairs (1.3× speedup)," but the closest corresponding data in Table 1 is the 80% condition (0.83× samples seen = 1.20× speedup). These numbers do not match.

### Trivial
None.

## Nice-to-Haves

- Compare CLIP + 1 epoch fine-tuning on full data to match the total epoch budget of the WFPP models.
- Ablate the threshold t to assess sensitivity and justify the chosen value.
- Include results for MetaCLIP on CC12M and at varying pruning ratios.
- The "second half" control (Table 6) already shows that ordering by S matters; the authors could additionally note that this implies a curriculum effect beyond mere frequency balancing.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"No comparison with other data pruning methods beyond MetaCLIP"** — The paper compares with random pruning, length-based pruning, and the "second half" control, which are reasonable and standard baselines for the setting. Requesting additional methods (e.g., curriculum ordering, prototype-based selection) is scope creep.
- **"No experiments on larger datasets (LAION-400M)"** — Explicitly acknowledged as future work (lines 575-580). Not a valid criticism of the current submission.
- **"20% reduction in words with 5-100 occurrences is dismissed"** — The paper says "Future work should investigate the impact of these words, which might be low, given their low frequencies" (line 563). This is an honest acknowledgment of a limitation, not a dismissal.
- **"WFPP-Second control could be strengthened by also comparing with random"** — The control already compares WFPP-Second against WFPP-First and random (Table 6). The comparison exists.
- **"Core equations do not reproduce the worked example"** — Kept as a Major weakness (see above), but downgraded from "structural flaw fatal to the paper" because (a) the equations themselves are well-defined and implementable, (b) the experimental results are consistent and self-consistent, and (c) the issue is in the example table, not in the method's mathematical definition. The original critic's framing of this as "structural" and fatal overshoots.
- **"Fine-tuning confound is fatal"** — Downgraded to Minor because the paper reports w/o ft results that tell the same story (WFPP 90% w/o ft = 34.9 beats CLIP 34.8), so the headline findings are not artifacts of fine-tuning alone.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any perspective on the work that the authors themselves do not already articulate.

## Suggestions

1. **Fix Table 1.** Clarify whether the row labeled f(w_i) actually shows P(w_i), 1−P(w_i), or some other quantity, and ensure the S values in the last column are reproducible from the stated equations. This is the most critical fix.

2. **Strengthen the MetaCLIP comparison.** At minimum, add results on CC12M at the same 50% ratio, and report variance (e.g., across 3 random seeds) to establish that the 0.3–0.5% advantage is statistically meaningful.

3. **Control the fine-tuning asymmetry.** Report CLIP + 1 epoch fine-tuning on full data as a direct comparison point.

4. **Ablate the threshold t.** Show results for at least 2–3 orders of magnitude around 10⁻⁷ (e.g., 10⁻⁶, 10⁻⁸) to demonstrate robustness.

5. **Reconcile the Figure 1 / Table 1 discrepancy** (77% vs. 80%, 1.3× vs. 1.2× speedup).

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>