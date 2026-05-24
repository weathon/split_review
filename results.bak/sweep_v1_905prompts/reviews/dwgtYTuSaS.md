Now I have a comprehensive picture. Let me produce the final review.

## Summary

This paper introduces **Continuous Online Action Detection (COAD)**, a new task formulation where OAD models not only detect actions in real time from streaming video but also continuously adapt via single-pass online training without storing data or replay. The authors curate **Ego-OAD**, a large-scale egocentric OAD benchmark (87 action classes, 22,991 instances, 263 hours) from Ego4D Moment Queries, and propose three training strategies — state continuity, orthogonal gradient projection, and non-uniform loss — tailored for this setting. Experiments on Ego-OAD show adaptation gains (up to 22.5% in-stream Top-5 Recall) and generalization improvements (up to 6.9% out-of-stream), with ablations quantifying each component's contribution.

## Strengths

- **Novel and well-motivated task formulation.** The paper identifies a genuine gap: OAD models are trained offline and do not adapt after deployment, which is misaligned with the dynamic, personalized nature of egocentric wearable applications. COAD formalizes the single-pass, no-replay, causal adaptation setting that prior work does not address, and the framing (Section 4.5) is clear and principled.

- **New large-scale benchmark (Ego-OAD).** Curated from Ego4D MQ, the dataset provides 87 fine-grained action classes, 22,991 labeled instances across 263 hours of egocentric video with 36% overlapping instances — substantially larger and more diverse than existing egocentric OAD resources. The pretraining/in-stream/out-of-stream split follows Carreira et al. (2024a) and enables structured evaluation of both adaptation and generalization.

- **Clean, well-ablated method.** The three components (state continuity, orthogonal gradient projection, non-uniform loss) are each motivated by a concrete problem in continuous video learning, and Table 3 provides a systematic ablation that quantifies each component's contribution. The orthogonal gradient projection (Table 3: +4.5% out-of-stream Top-5 Recall) and non-uniform loss (+4.2% mAP, +8.3% Top-5 Recall) show clear additive value.

- **Demonstrates that sparse supervision suffices.** Figure 3's stride experiment shows that at stride 128, the model uses a label only once ~68 seconds yet maintains performance, partially addressing the practical concern of label availability in deployment.

## Weaknesses

### Major

1. **EPIC-KITCHENS out-of-stream results contradict the paper's generalization claims.** The paper states that "COAD consistently achieves the best generalization performance across all categories (Verb, Noun, and Action)" (Section 5.3). However, Table 2 tells a different story on out-of-stream (generalization) data: COAD *underperforms* the "Pretrained Only" baseline on action mAP (7.9 vs. 9.6), action Top-5 Recall (20.5 vs. 22.9), and noun Top-5 Recall (13.9 vs. 14.7), and ties on verb mAP and verb Top-5 (both 29.0/45.9). The only clear out-of-stream win is noun mAP (3.9 vs. 3.8) — a 0.1 mAP gain. This directly undermines the paper's central claim about generalization. The paper's post-hoc explanation ("fine-grained nature of the actions... limit the model's ability to detect recurring patterns") is plausible but unsupported by any analysis. Accepting the paper would require either demonstrating that COAD works on EPIC-KITCHENS (a standard benchmark) or substantially tempering the claims.

2. **The "w/o COAD" baseline resets RNN hidden states, which is not a natural streaming baseline.** The w/o COAD baseline disables state continuity, meaning the RNN hidden state is reset between training windows even during continuous in-stream processing (Table 3 Row 5). In any realistic deployment, a model would naturally maintain its hidden state across frames. The missing ablation row — **state continuity enabled, orthogonal gradient and non-uniform loss disabled** (✓, ✗, ✗, ✓) — would isolate how much of the reported gain comes from simply maintaining temporal coherence versus the proposed technical innovations. Rows 3 and 4 in Table 3 provide partial decomposition but do not fully answer this question. While this does not invalidate the results, it inflates the apparent gap between COAD and the baseline and makes it harder to attribute improvements to the claimed contributions.

3. **Claims are consistently overstated relative to the evidence.** Beyond the EPIC-KITCHENS issue: (a) Up to "20% adaptation and 7% generalization improvements" in the abstract use the most favorable configuration (exocentric→in-stream Top-5 Recall +22.5%, which is adaptation, not generalization, and on the weaker pretrained backbone); on the stronger ego-pretrained backbone the biggest generalization gain is +6.9% Top-5 Recall, and mAP gains are often marginal (+0.5 to +5.9). (b) "Significant gains" in the conclusion is not supported by the modest and inconsistent improvements. The paper would benefit from precision: reporting which metrics improve under which conditions and acknowledging when they do not.

### Minor

1. **Missing ablation: state continuity only.** As noted in Major 2, Table 3 lacks the row with only state continuity enabled. The community would benefit from knowing whether the orthogonal gradient and non-uniform loss provide meaningful gains on top of simply running continuous training with state retention.

2. **No statistical variance reported.** All results in Tables 1-3 are single numbers without standard deviations or confidence intervals. Given that COAD operates in a single-pass setting with batch size 1, results may be sensitive to data ordering. Reporting means over multiple runs (or at least run-level variance) would strengthen credibility.

3. **No analysis of catastrophic forgetting.** COAD operates in a continual learning setting where the model updates on a single pass through streaming data. The paper does not evaluate whether the model forgets previously seen actions as it adapts to new ones. Metrics like per-video performance trajectories or backward transfer would provide useful insight.

4. **Label-sparsity benefit is claimed but only partially evaluated.** The paper claims "improved label efficiency" (Section 4.5) as a benefit of non-uniform loss. The stride experiment (Figure 3) partially demonstrates this, but there is no dedicated experiment where labels are provided only at a fraction of windows while training continuously on all windows. The claim of label efficiency is aspirational rather than empirically validated.

### Trivial

- Figure 4 caption says "approaching the IID training upper bound" but the gap between COAD and IID appears roughly constant (~6 mAP) across the training range rather than narrowing.
- Table 2 column headers show "out/in" but the results rows use the format "in-stream / out-of-stream" — the ordering should be clarified in the caption.
- The orthogonal gradient projection (Eq. 4) uses only the immediate previous gradient; a brief justification (or comparison to a multi-step buffer) would be helpful.

## Nice-to-Haves

- Evaluate the orthogonal gradient with a multi-step gradient buffer (as in the original Han et al. 2025 work) to justify the single-step design choice.
- Add per-class analysis on EPIC-KITCHENS to understand when COAD helps vs. hurts.
- Report inference FLOPs or runtime for the RNN head to support the claimed suitability for resource-constrained devices.
- Discuss how labels would be obtained in a deployed system (e.g., intermittent user feedback, weak supervision) rather than assuming ground-truth annotations are available at every window's final step.

## Removed Points

- **"Label availability is a fatal methodological gap"** — REMOVED. The paper's stride experiment (Figure 3) demonstrates the model works with labels only every ~68 seconds. While this doesn't fully address the deployment scenario, it constitutes a reasonable first step. The critic's characterization as a fatal flaw is overstated.
- **"The paper dismissed Transformers inconsistently"** — REMOVED. The paper uses a frozen TimeSformer backbone (a Transformer) for feature extraction with a lightweight RNN head for temporal modeling — this is a coherent design choice and not inconsistent.
- **"Dataset curation concerns (label noise, inter-annotator agreement)"** — REMOVED. These are reasonable questions but standard for a conference submission; the paper explicitly notes that the Appendix (stripped by the parser) contains further details. The 36% overlap rate is reported transparently.
- **"Fairness of comparisons favors baselines"** — REMOVED. This complaint is about the w/o COAD baseline being weak, which is already covered. The claim about unfair comparisons in general is not grounded in specific evidence.
- **"Missing discussion of inference cost"** — DEMOTED to nice-to-have. RNNs are well-known to be lightweight; this is a marginal omission.
- **"IID training upper bound is not defined in main text"** — REMOVED. It is described in the Figure 4 caption, which is standard practice.

## Novel Insights

None beyond the paper's own contributions. The review process surfaced the core tension well: the paper has a genuinely novel task formulation and valuable dataset contribution, but the experimental evaluation (especially the EPIC-KITCHENS generalization contradiction and the under-ablated baseline) does not fully support the strength of the claims made.

## Suggestions

1. **Add the missing ablation row** (state continuity only, no orthogonal gradient, no non-uniform loss) to Table 3. This is a single experiment that would resolve the most-cited concern about the baseline.
2. **Revise the claims about EPIC-KITCHENS generalization.** Either present the out-of-stream results honestly (showing where COAD helps and where it doesn't) or provide analysis explaining the failure modes. The current language ("consistently achieves the best generalization performance") is unsupported.
3. **Report statistical variance** (means ± std over at least 3 runs with different data orderings) for the main results.
4. **Tone down the abstract and conclusion** to match what the evidence supports — e.g., "up to 6.9% improvement in Top-5 recall on held-out data" rather than generic "significant gains."
5. **Evaluate label sparsity more directly** by running COAD with supervision only at a fraction of windows, to substantiate the claimed label-efficiency benefit.

## Score and Decision

### Round 1 bracketing

Three calibration searches across the score spectrum identified:

| Band | Anchor | Avg Score | Comparison |
|------|--------|-----------|------------|
| Weak (<3.5) | 2HdZPEQUig | 3.00 | Object-centric video learning; rejected — weaker contribution, less clear problem framing |
| Weak (<3.5) | WM5G2NWSYC | 2.00 | Subnetwork adaptation; rejected — unclear contribution |
| Mid (3.5–7.5) | P6G1Z6jkf3 | 6.00 | Egocentric video representation; accepted — stronger experimental validation and cleaner narrative |
| Mid (3.5–7.5) | jawV7vhGHw | 4.25 | Real-time video classification; rejected — evaluation gaps similar to this paper |
| Mid (3.5–7.5) | 7L2bpe7lfm | 4.50 | Video continual learning; rejected — mixed reception, evaluation issues |
| Mid (3.5–7.5) | F0K0zxi62U | 4.00 | Egocentric-exocentric alignment; rejected — limited results |
| Strong (>7.5) | 9Cu8MRmhq2 | 8.00 | Multi-granularity video-language learning; accepted — rigorous experiments |
| Strong (>7.5) | Y6aHdDNQYD | 8.00 | Test-time adaptation for 3D detection; accepted — thorough evaluation |
| Strong (>7.5) | CRmiX0v16e | 7.80 | Open-vocabulary 3D segmentation; accepted — strong results |

**Round 1 bracket:** 4.5 – 6.0

### Round 2 narrowing

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| Y7jJN0VQ4y | 5.71 | Continual learning for video anomaly detection. Rejected despite novel task formulation; reviewers flagged evaluation limitations and overclaimed novelty. This paper has a similar structure but weaker experimental evidence (EPIC-KITCHENS contradiction). |
| oO3oXJ19Pb | 4.80 | Online action-augmented dense video captioning. Rejected; novel idea but execution gaps. Similar quality level — task formulation is solid, but evaluation issues prevent acceptance. |
| 7L2bpe7lfm | 4.50 | Video continual learning with compression. Mixed reception (6,3,6,3). Similar pattern: good idea, incomplete evaluation. |
| FZv3kPHTtB | 5.50 | Multi-shot video benchmark. Accepted; clean benchmark paper with clear contribution. Current paper's benchmark is similarly valuable but the method evaluation is weaker. |

**Final score: 5.0 / 10**

The paper's task contribution and dataset are genuine and valuable, placing it above the reject-level 3–4 papers. However, the EPIC-KITCHENS generalization contradiction is a verifiable overstatement that undermines the core claim, and the baseline comparison inflates the apparent gains. These issues place the paper below the 5.5–6 level where a clear accept decision would be warranted. A thorough revision — particularly fixing the claims about EPIC-KITCHENS, adding the missing ablation, and reporting variance — could bring this paper to accept quality.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>