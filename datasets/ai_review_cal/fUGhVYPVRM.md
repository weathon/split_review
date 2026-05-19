- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8
Now I have enough information. Let me write the consolidated review.

## Summary
This paper proposes Align With Purpose (AWP), a general plug-and-play framework for enhancing desired properties in CTC-trained models. AWP adds a hinge loss over pairs of sampled alignments (original vs. property-improved via a task-specific function \(f_{prop}\)) to the CTC loss, without modifying the CTC forward-backward algorithm. The authors demonstrate AWP on two unrelated properties — low-latency ASR (reducing drift latency by up to 590ms) and minimum-WER optimization (up to 4.5% relative WER improvement) — across three architectures (Stacked ResNet, Conformer, Wav2Vec2) and datasets ranging from 1K to 280K hours of audio.

## Strengths
- **Generality demonstrated across architectures, data scales, and properties.** AWP is evaluated on two unrelated tasks (latency and WER), three architectures (Stacked ResNet, Conformer, Wav2Vec2), and datasets from 1K to 280K hours (Tables 1, 2). This directly supports the claim that AWP is a general framework, not a one-off trick.
- **Competitive or superior results versus prior specialized methods.** On LS-960 low-latency, AWP achieves DL=-79ms with WER=4.38%, outperforming PeakFirst CTC (186ms DL, 4.41% WER), TrimTail (-76ms DL, 4.46% WER), and BayesRisk CTC (63ms DL, 4.78% WER) (Table 1). For mWER, AWP yields results comparable to the application-specific MWER_OPT adaptation (Table 2), despite being simpler and general.
- **Simplicity without modifying the CTC core.** AWP adds only a few lines of code (Section 2.2, Figure 1) and does not intervene in the CTC forward-backward algorithm — unlike prior work (BayesRisk CTC, FastEmit, PeakFirst CTC). This is a concrete differentiator.
- **Demonstration at unprecedented scale.** The paper trains latency-optimized models on 280K hours of audio (Internal-280K), and states (accurately) that such applications have not been demonstrated at this scale before. This strengthens claims of practical deployability.
- **Ablation analysis of key hyperparameters.** Figure 5 systematically studies how the start epoch and loss weight \(\alpha\) trade off between WER and drift latency, giving practitioners concrete tuning guidance.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Under-specification of the \(f_{mWER}\) alignment modification.** The paper states (Section 2.4): "Then we fix the alignment of this word according to the GT, so that the number of word errors in \(\mathcal{B}(\bar{\mathbf{a}})\) is reduced by 1." The operation "fix the alignment of this word according to the GT" is not algorithmically defined. In CTC, the alignment is a T-length sequence of vocabulary tokens (including blanks and repetitions). The paper does not specify which token indices in the alignment are changed, how to handle cases where a word spans multiple acoustic frames with repeated tokens or blanks, or whether the fix operates at the token level or the collapsed-text level. This gaps reproducibility for the mWER application. (Illustrated in Figure 4, but the general-case algorithm is missing.)

- **WER improvements lack variance or significance estimates.** The absolute WER gains in Table 2 are very small (e.g., 2.38% → 2.33%, a 0.05% absolute difference on Test-Clean; 5.82% → 5.56%, a 0.26% absolute difference on Test-Other). No confidence intervals, multiple-run statistics, or significance tests are reported. While single-run reporting is common in ASR, the small absolute gaps make it uncertain whether the improvements are systematic or within run-to-run variance. The paper's central WER-improvement claim would benefit substantially from even a brief multi-seed summary.

- **MWER_OPT adaptation is not described.** The paper reports a "MWER_OPT" baseline (Table 2) described as "our adaptation of MWER optimization ... originally designed for soft alignment models trained with a CE loss," but provides no details of how the method was adapted for CTC. Without this description, a reader cannot assess whether the comparison is fair or whether AWP's comparable performance is meaningful.

- **Start epoch selection procedure is underspecified.** The start epoch is "chosen based on a list of milestones WER of the online model" (Table 1 caption). The values vary widely across experiments (0.1 to 12), and Figure 5 shows that start epoch has a substantial effect on the latency-WER trade-off. While the ablation in Figure 5 is helpful, the lack of a principled selection criterion weakens reproducibility and leaves open the possibility of cherry-picking.

### Trivial
- **Near-zero Conformer baseline drift could be briefly explained.** The Conformer online model achieves DL = 2ms (Table 1). The paper notes that the Conformer was "trained offline" and only context-restricted "during inference" (Section 3), which effectively explains the near-zero drift. However, this distinction is easy to miss; adding a brief sentence connecting the training-vs-inference asymmetry to the negligible drift would help readers.

## Nice-to-Haves
- Reporting the number of samples \(N\) used in AWP training and a brief sensitivity analysis would strengthen the practical guidance.
- A sensitivity analysis of the margin hyperparameter \(\lambda\) would also be useful for practitioners.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

1. **"Sampling procedure under-specified"** — The paper clearly states "\(\mathbf{a}^i_t \sim \mathbf{v}_t\) for \(t \in [1..T]\)" (Section 2.2), which is an explicit independent-sampling algorithm. This description is sufficient. **Reason:** factually incorrect criticism.

2. **"Hinge loss applied to perfect alignments"** — For mWER, the paper explicitly says "Given a sampled **imperfect** alignment" (Section 2.4). This is addressed. **Reason:** misunderstanding of the paper.

3. **"Comparison breadth is insufficient"** — The paper compares with three specialized baselines (PeakFirst, TrimTail, BayesRisk) on LS-960 with Stacked ResNet, and AWP outperforms or matches all. The claim being supported is that AWP is competitive with specialized methods — this evidence is adequate. **Reason:** scope creep; the comparison is sufficient for the claim.

4. **"Conformer's near-zero drift undermines the paper's narrative"** — The paper explains (Section 3, line 159) that the Conformer was "trained offline" with full context and only restricted during inference; this explains the 2ms drift. The paper's primary drift-reduction demonstration is on the Stacked ResNet (trained with asymmetric padding from scratch), which is the standard setting where drift is problematic. **Reason:** the information is present in the paper; the criticism inflates a minor detail into a structural issue.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Provide an algorithmic (pseudocode) description of \(f_{mWER}\) that specifies exactly how "fix the alignment of this word according to the GT" operates at the token-index level in the T-length alignment, including handling of blanks and repetitions.
2. Report multi-seed statistics (mean ± std over 3 runs) for the mWER experiments in Table 2, or at minimum add a confidence statement about the observed improvements.
3. Describe the MWER_OPT adaptation for CTC in enough detail for readers to assess fairness of comparison.
4. Clarify the start epoch selection procedure (e.g., hold-out validation on a development set).
