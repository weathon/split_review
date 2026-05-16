## Summary

This paper introduces VideoUntier, a text-video retrieval method that uses part-of-speech tagging to extract "object" (noun) and "event" (verb) tokens from text queries, then employs these tokens as queries in cross-attention to progressively merge video patch features into query-relevant object and event representations. The method uses three levels of similarity (global, object, event) with a coarse-filtering strategy for efficiency. Experiments on MSRVTT, DiDeMo, and MSVD show consistent improvements over prior fine-grained alignment methods (ProST, HBI, TS2-Net, UCOFIA), and domain generalization experiments suggest the learned features transfer across datasets.

## Strengths

- **Consistent accuracy gains across three benchmarks.** VideoUntier outperforms recent fine-grained alignment methods on MSRVTT-9k (e.g., +1.2% R@1 over ProST), DiDeMo (+2.6% R@1 over ProST), and MSVD (+1.0% R@1 over ProST), demonstrating that the overall pipeline works across different video domains.

- **Ablation confirms multi-grained design contributes positively.** Table 7 shows that adding object-level similarity improves global-only R@1 by +2.9%, and event-level adds another +1.3% (total +4.2%). This controlled ablation supports the core design rationale independent of cross-method comparisons.

- **Computational efficiency is convincingly demonstrated.** The coarse-filter strategy (Table 8) reduces fine-grained computation by 11.3× (227.01s → 20.07s) while losing only 0.2% R@1. The efficiency advantage over ProST (20.1s vs. 25.2s at higher accuracy) is a concrete benefit.

- **Qualitative visualization supports the claimed attention mechanism.** Figure 3 shows that object/event tokens (e.g., 'bus') attend to relevant video regions while global features attend to background content, providing direct visual evidence for the language-guided feature extraction.

## Weaknesses

### Fatal

None.

### Major

- **Uncontrolled cross-method comparisons weaken the evidence for the core claim.** Only one baseline (TVMM*) is re-run under the same CLIP ViT-B/32 backbone. For all other competitors (HBI, TS2-Net, ProST, UCOFIA), the paper takes reported numbers directly. Since backbone choice strongly affects performance (the paper itself shows ViT-B/16 vs. ViT-B/32 differences of several R@1 points), and it is not stated which backbone variant each competitor used, the reader cannot determine whether the reported gains (0.6%–2.6% R@1) come from the proposed method or from backbone/hyperparameter differences. This is the single most significant weakness: the conclusion may be correct, but the evidence is inconclusive. The ablation study (Table 7) partially mitigates this by showing the benefit of multi-grained similarity within a controlled setting, but cross-method claims require controlled comparisons.

### Minor

- **The PTG module's contribution is not empirically validated.** The paper extracts noun/verb tokens via POS tagging and enriches them with context via cross-attention, but never ablates this module. There is no experiment showing what happens when: (1) POS tags are replaced with ground-truth tags, (2) the context cross-attention is removed, or (3) the padding strategy uses different priority orders. Since the module is central to the claimed novelty, its lack of ablation is a meaningful gap.

- **The efficiency advantage is incompletely characterized.** Inference time is reported only against ProST. Times for HBI, TS2-Net, and UCOFIA are absent, making the claim of "better efficiency" only partially supported.

- **Domain generalization experiment lacks training protocol details.** While the source dataset (MSRVTT, inferable from context) and targets (DiDeMo, MSVD, stated explicitly) are clear enough, the paper does not describe the training setup (hyperparameters, frame sampling strategy for the source, whether the full training set is used) used for the pre-trained model. Without this, the result cannot be reproduced or compared fairly.

- **Key architectural details are omitted.** The Transformer Encoder used for temporal interaction (Section 3.2 and Section 3.4) is never specified: number of layers, attention heads, hidden dimension, or dropout. This hurts reproducibility beyond trivial hyperparameter nitpicking—these are architectural specifications.

- **Single-run results without statistical significance.** All metrics are reported from single runs. Given the modest gains (0.6–2.6 R@1 points), confidence intervals or multi-run averages would help assess whether these improvements are stable or within noise range.

- **Novelty claim is somewhat overstated.** The paper describes itself as "an original effort in learning object and event features from videos with guidance from text queries." However, prior works such as HBI and ProST already use text-guided attention to extract fine-grained video features. The paper's contribution lies in the specific pipeline (POS tagging + cross-attention + temporal Transformer + coarse filtering), which is meaningful but incremental relative to this prior work. A more precise positioning would strengthen the paper.

### Trivial

- **Underlined numbers in tables lack a legend.** It appears underlining indicates the best result per column, but this is never stated explicitly.

- **No limitations section.** Including one would show awareness of the method's boundaries (e.g., reliance on POS tagger accuracy, handling of compound/complex queries, cluttered scenes).

## Nice-to-Haves

- An ablation of the PTG module (ground-truth POS vs. tagger output, with/without context cross-attention) would directly support the claimed design rationale.
- Reproducing 2–3 strong baselines (e.g., ProST, HBI) under identical backbone and training conditions would substantially strengthen the evaluation.
- A failure case analysis (e.g., queries with abstract verbs, videos with cluttered scenes, POS tagger errors) would strengthen the paper's completeness.
- Adding a section on limitations.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Domain generalization never specifies what A and B are."** — The paper text (line 197) explicitly names DiDeMo and MSVD as target datasets, and the source (MSRVTT) is clear from context as the training dataset. The targets are stated. Removed because this criticism misreads the paper.

2. **"No code link."** — Removed per hard rules: questioning the availability of artifacts is outside evaluation scope for the initial submission.

3. **"Comparison with more recent work (2024–2025) needed."** — Removed per hard rules: this amounts to demanding citations of works the reviewer speculates exist; the paper's comparisons with up-to-2023 methods are within its stated scope.

4. **"Many numbers are underlined without a clear legend"** — Removed as a formatting/table presentation nitpick. While technically true, this has near-zero impact on the paper's contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful meta-observation: the paper's core idea (text-guided video feature disentanglement) is plausible, but the evidence is weakened by lack of controlled comparisons—a problem that is surprisingly common in this sub-area but rarely discussed in reviews. The reviews do not reveal any insight about the method or problem that the paper itself does not already articulate.

## Suggestions

1. **Re-run 2–3 key baselines (at minimum ProST and HBI) under your exact backbone and training protocol.** This is the single highest-leverage improvement. Without it, the central claim of "consistent outperformance" rests on incomparable numbers.

2. **Add an ablation of the PTG module.** Show retrieval performance with and without the context cross-attention (Eq. 8), and with ground-truth vs. predicted POS tags.

3. **Expand the domain generalization experiment description.** State explicitly: source dataset, training protocol, hyperparameters. Ideally, compare a version of your model without language-guided modules to isolate the benefit of text guidance in the zero-shot setting.

4. **Specify the Transformer Encoder architecture** (layers, heads, dimension, dropout) used in both the global feature extraction and the temporal feature interaction.

5. **Report results from at least 3 runs** with mean and std, or provide a statistical significance test for the key comparisons where gains are < 2%.

## Score and Decision

The paper tackles a well-motivated problem and proposes a clean, interpretable pipeline. The core idea—using POS-derived object/event tokens to guide video feature extraction—is sensible, and the ablation studies validate that each granularity of similarity contributes. However, the evaluation has a major methodological gap: almost all cross-method comparisons use numbers from different experimental setups without ensuring backbone parity. This weakens the paper's central claim of state-of-the-art performance to an uncomfortable degree. The gains are modest (0.6–2.6 R@1), and without controlled comparisons, the reader cannot attribute them to the method rather than to backbone choice. Several secondary issues (PTG not ablated, missing architectural details, incomplete efficiency characterization) compound the problem. The paper would need substantial additional experimental work to be convincing at a top venue.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>