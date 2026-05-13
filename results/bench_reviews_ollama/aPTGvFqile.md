Now I have enough information to write a thorough review. Let me verify the key claims from the harsh critic against the paper.

Key verification points:

1. **Parameter sharing harms downstream tasks**: The paper itself states (line 191): "SharedCLIP improves the classification performance on the ImageNet-1K dataset and reduces the accuracy on the rest of the datasets." This confirms the harsh critic's observation. SharedCLIP alone degrades 4/5 zero-shot classification benchmarks. However, it does improve alignment scores (Table 1) and helps in linear probing and robustness.

2. **No ablation of IMSep on vanilla CLIP**: The ablation (Section 4.6) only tests re-scaling within AlignCLIP, not IMSep on standard CLIP. This is a valid criticism — the two contributions are confounded.

3. **DFSep comparison unfair**: The paper explicitly states (line 239) that DFSep uses ResNet-50/BERT with different batch size, embedding dimension, etc. They acknowledge this by marking it with an asterisk. However, this doesn't make the comparison "unfair" per se — it's more of a limitation that they acknowledge.

4. **No variance reporting**: Confirmed — no standard deviations or statistical tests anywhere.

5. **Missing SLIP comparison**: SLIP is cited in related work but not evaluated. This is a missing baseline concern.

6. **The paper claims both contributions improve downstream performance**: The abstract says "by sharing the learnable parameters between the modality encoders and a semantically-regularized separation objective function" — the "and" implies both contribute. But SharedCLIP alone hurts 4/5 zero-shot tasks, so parameter sharing is not independently contributing to downstream performance.

7. **The paper acknowledges SharedCLIP weaknesses**: Line 191 acknowledges SharedCLIP reduces accuracy on some datasets, and in Section 4.5 they note cases where SharedCLIP beats AlignCLIP. However, the abstract's framing still presents both as contributing positively.

Let me now synthesize the review.

The core claim of the paper is that AlignCLIP = SharedCLIP + IMSep reduces the modality gap and improves downstream tasks. The evidence shows AlignCLIP (combined) works, but the two sub-contributions are confounded: SharedCLIP alone improves alignment but hurts most downstream tasks, and IMSep alone on vanilla CLIP is never tested. This is the main structural issue.

The DFSep comparison acknowledges the architectural difference, so it's more of a limitation than an unfair comparison per se.

The missing SLIP comparison is missing related baseline, which per my rules I should not flag as "missing related works."

No variance reporting is confirmed, and margins are small (1-2%).

Now let me write the consolidated review.</think>Now I have thoroughly verified all claims. Let me compose the final review.

## Summary

The paper proposes AlignCLIP, a two-part approach to reducing the modality gap in CLIP: (1) SharedCLIP, which shares the transformer encoder and projection layer between vision and language towers, and (2) IMSep, a semantically-regularized intra-modality separation loss that pushes apart uni-modal embeddings proportional to their semantic distance (computed via a frozen SBERT encoder). Experiments on CC12M-pretrained models show AlignCLIP improves alignment scores and downstream zero-shot classification, linear probing, robustness, and retrieval compared to vanilla CLIP.

## Strengths

- **Semantically-regularized intra-modality separation (IMSep) is a principled and novel contribution.** Weighting the push-apart of image embeddings by text-derived semantic distances (Eq. 7–10) addresses a real limitation of naive intra-modal contrastive losses, which treat all negative pairs equally. The ablation in Table 6 confirms that removing this re-scaling hurts performance across tasks, validating the mechanism.

- **Clear evidence of alignment improvement.** Table 1 shows alignment scores rising from [0.38, 0.47] (CLIP) to [0.62, 0.67] (AlignCLIP) across five datasets, reducing the average paired embedding angle from ~70° to ~47°. Figures 4–5 provide complementary qualitative and quantitative confirmation (cumulative distribution and DOSNES projections).

- **Consistent downstream gains for the combined method.** AlignCLIP improves over CLIP on all reported zero-shot classification, linear probing, distribution-shift robustness, and retrieval benchmarks, with especially large gains on CIFAR-10/100 (~8% Top-1).

## Weaknesses

### Fatal
None.

### Major

- **The two claimed contributions are confounded, and parameter sharing is independently harmful on most downstream tasks.** The abstract frames AlignCLIP as yielding gains "by sharing the learnable parameters… and a semantically-regularized separation objective function," implying both contribute. However, SharedCLIP alone *reduces* accuracy on 4 of 5 zero-shot classification datasets (the paper itself acknowledges this: "SharedCLIP improves the classification performance on the ImageNet-1K dataset and reduces the accuracy on the rest of the datasets"). Meanwhile, there is **no ablation of IMSep applied to standard dual-stream CLIP** — the only ablation (Section 4.6) tests re-scaling within AlignCLIP, not IMSep alone. Without this critical ablation, it is impossible to determine whether parameter sharing adds any downstream value beyond what IMSep provides, or whether SharedCLIP's alignment gains simply come at the cost of downstream capacity. The paper should either include the IMSep-on-vanilla-CLIP ablation to justify retaining parameter sharing as a contribution, or reframe parameter sharing as an alignment-only improvement that requires IMSep to recover downstream performance.

- **DFSep comparison uses a fundamentally different architecture, and this is acknowledged but not mitigated.** Table 7 reports results from DFSep's original paper (ResNet-50/BERT, embedding dim 1024, batch size 128, lr 5e-4), which differs starkly from AlignCLIP's ViT-B-16/transformer setup. The paper marks this with an asterisk but still draws comparative conclusions ("promising improvement… in comparison to the previous models"). Aligning DFSep's architecture with the others, or simply not drawing comparative claims against DFSep, would strengthen the paper. As-is, these claims about outperforming DFSep are unsupported.

### Minor

- **No variance or significance reporting.** Many improvements are 1–2% (e.g., +1.4% Top-1 on ImageNet-1K, ~2% on distribution shift benchmarks, 1–2% R@1 on retrieval). Single-run results without standard deviations make it difficult to assess whether these margins are meaningful or within training variance, particularly given the relatively small CC12M training dataset.

- **Sensitivity to the frozen SBERT encoder is unanalyzed.** IMSep relies on SBERT all-mpnet-base-v2 to compute semantic distances. The paper does not investigate how robust results are to this choice, or whether the CLIP text encoder itself could serve this role. Given that IMSep is the core functional contribution, sensitivity to its external dependency deserves at least a brief analysis.

- **The paper's framing overclaims the contribution of parameter sharing for downstream tasks.** The conclusion states "AlignCLIP reduces the gap by increasing the inductive bias towards shared embeddings as well [as] semantic-regularized modifications," but the evidence shows parameter sharing *alone* degrades most downstream tasks. The framing should be revised to clarify that SharedCLIP's primary benefit is alignment, and that IMSep is the mechanism driving downstream improvement.

### Trivial
None.

## Nice-to-Haves

- An ablation of IMSep applied to standard (non-shared) CLIP, which would definitively disentangle the two contributions and either justify or eliminate parameter sharing as a design choice.
- Multiple training runs with variance reporting.
- Comparison with SLIP on the same training setup, since both methods add an image-contrastive objective to CLIP.
- Analysis of failure modes in retrieval where SharedCLIP outperforms AlignCLIP (the paper briefly notes this phenomenon in Section 4.5 but does not systematically characterize it).

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Unfair comparison with DFSep (harsh critic's point #2)**: The harsh critic calls this "unfair" in a way that implies deception. The paper transparently discloses DFSep's different architecture (ResNet-50/BERT, different batch size, embedding dim, lr) and marks it with an asterisk in Table 7. The real issue is that comparative conclusions are still drawn despite the asymmetry — this is better characterized as an overclaim (moved to Major) rather than an "unfair" comparison.

- **Missing SLIP comparison (harsh critic)**: Per the hard rules, I should not flag missing related works as I cannot confirm whether SLIP would be a feasible comparison under this training setup. The paper does cite it.

- **Request to compare with the translation-based approach from Section A.1**: This is scope creep — the paper's contribution is a learning-based alternative, not a comparison with naive post-hoc shifting.

- **Request for scale-up experiments on LAION-400M**: Nice-to-have, not a weakness. CC12M is a reasonable training setup for evaluating the method.

- **Request to analyze why parameter sharing hurts downstream tasks**: This is a valid research question but goes beyond the paper's stated scope, which is to propose and evaluate AlignCLIP. Moved to Nice-to-Haves.

- **Missing proofs/appendix**: The parser strips these sections; the original submission contains Sections A.1–A.3.

- **Formatting/typo complaints**: Removed per hard rules (parser artifacts).

- **Strength finder claim that "improved performance over prior alignment baselines" including DFSep is a strength**: Partially removed — AlignCLIP's improvements over CyCLIP (fairly compared) are a legitimate strength, but the DFSep comparison is confounded by architecture differences.

- **Generic strength about "addressing an important problem"**: Removed as generic/superficial.

## Novel Insights

The most interesting empirical finding is that parameter sharing *improves alignment scores* (up to +0.17) while simultaneously *degrading most downstream zero-shot classification results*. This tension suggests that reducing the modality gap through architectural inductive biases and improving task-specific representations are not always aligned objectives — a nuance that the paper's framing does not adequately surface. IMSep appears to resolve this tension by recovering downstream performance through better intra-modal spreading, making it the true workhorse of the method.

## Suggestions

- **Add the IMSep-on-vanilla-CLIP ablation.** This is the single most impactful change: train CLIP + IMSep (without parameter sharing) on CC12M and report alignment + all downstream benchmarks. If IMSep alone matches AlignCLIP, parameter sharing should be reframed as an alignment-only insight rather than a core contribution to downstream tasks.
- **Soften or remove comparative claims against DFSep** in Section 4.7, since the architectural differences make the comparison non-informative. Alternatively, retrain DFSep with the same ViT-B-16 backbone for a fair comparison.
- **Reframe the abstract and conclusion** to accurately reflect that parameter sharing primarily improves alignment but can hurt downstream performance without IMSep, and that IMSep is the primary driver of downstream gains.

## Score and Decision

The paper presents a genuinely novel and well-motivated loss function (IMSep) that is validated by consistent downstream improvements and an informative ablation of its semantic re-scaling component. However, the confounding of two claimed contributions — parameter sharing and IMSep — is a significant structural issue. Without an IMSep-on-vanilla-CLIP ablation, the paper cannot attribute its gains correctly between the two mechanisms, and parameter sharing is independently harmful on most downstream tasks, contradicting the paper's framing. The DFSep comparison overclaims given architectural asymmetries, and the lack of variance reporting leaves small margins unconvincing. These issues undermine the clarity of the contributions but do not invalidate the core method, which does produce real improvements.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>