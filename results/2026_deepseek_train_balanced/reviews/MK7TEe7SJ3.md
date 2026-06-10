## Summary

This paper proposes USTAM, an extension of the MixFormer one-stream transformer tracker that inserts spatial and temporal attention modules into its Mixed Attention Module (MAM) blocks. Temporal attention is applied in the first MAM block (modulating the current-frame search attention map with the previous frame's spatial attention map via element-wise multiplication with a residual connection), and spatial attention is applied in the last MAM block. Evaluated on LaSOT, TrackingNet, and GOT-10k, USTAM achieves competitive second-best results behind ARTrack, with ablation studies showing ~2% AO improvement from the spatio-temporal modules with modest computational overhead.

## Strengths

1. **Minimal computational overhead for measurable gains**: Table 4 shows that adding both spatial and temporal attention improves AO by 2.3% on GOT-10k and 1.9% on LaSOT while increasing MACs by only 0.4G (base) and 3G (large), with negligible parameter count or speed changes. The intra-model comparison is clean and directly supports the claimed efficiency advantage.

2. **Plug-and-play module validated across architectures**: Table 5 demonstrates that the spatio-temporal attention module improves SwinTrack-Tiny (+1.6% AO) and MixFormer-Base (+2.3%/+0.8% AO) when attached as a post-hoc module, confirming it is not tightly coupled to USTAM's specific backbone — a property many prior attention-based trackers do not verify.

3. **Clean temporal-attention formulation**: Equations (3)–(4) define a simple mechanism where the previous frame's spatial attention map gates the current-frame search attention via element-wise multiplication with a residual addition, requiring no extra trainable parameters for temporal fusion.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Insufficient differentiation from prior spatio-temporal one-stream transformer trackers**: The paper cites Xie et al. (2023) with the phrase "also attempted to fully utilize both temporal and spatial information within a one-stream transformer tracker" but never explains how USTAM's design differs or improves upon that method. Since both operate in the same paradigm (one-stream transformer with spatio-temporal attention), the absence of any structural or empirical comparison weakens the paper's novelty claims. A reader cannot determine whether USTAM's specific design choices are novel or a re-implementation on a different base architecture.

2. **Several architectural details essential for reproducibility are missing**: (a) The total number of MAM blocks is never stated — the paper refers to "first," "last," and "remaining" blocks without giving a count. (b) The "asymmetric attention scheme" is named in Section 3 as a design choice but never explicitly defined (the equations show different key mixing for target vs. search attention, but the term itself is left unexplained). (c) The spatial attention post-processing (softmax → FC → residual, line 92) lacks any dimensional specification. These gaps hinder independent implementation.

3. **Confusing presentation of the main GOT-10k results**: The text (Section 4.1) states "MixFormer achieves the best performance in terms of the AO and SR_50 metrics" alongside USTAM's results, then groups USTAM-L with MixFormer-L, OSTrack384, and ARTrack384 as exhibiting "improved AO performance by over 5%." It never makes a direct head-to-head statement about whether USTAM outperforms or trails MixFormer on this benchmark. The improvement evidence (2.3% AO) appears only in the ablation study, not the main comparison — this is a conspicuous organizational weakness.

4. **Unsubstantiated computational efficiency claim in the Introduction**: The Introduction asserts the approach "places fewer demands on computational resources," but no cross-method FLOP, parameter, or speed comparison against competing trackers (OSTrack, STARK, ARTrack) is provided. Table 4 shows only intra-model overhead relative to the baseline. The claim as stated is not supported by the data in the paper.

5. **Dimensional alignment of recurrent attention maps not explicitly addressed**: The temporal mechanism uses G_sp^{t-1} (from the last MAM block at frame t-1) to modulate G^t (from the first MAM block at frame t). In standard tracking practice the search crop is resized to a fixed input size, which would make dimensions match, but the paper does not explicitly describe this alignment step. The ambiguity is unnecessary and could cause reader confusion.

### Trivial

1. **Row/column terminology mismatch in Eq. 6**: The formula computes column means (averaging over rows i for each fixed column j), but the text describes "the largest of the mean values in **each row**." This should be corrected for internal consistency.

## Nice-to-Haves

- Reporting attribute-specific performance breakdowns (occlusion, fast motion, out-of-view, etc.) on LaSOT or GOT-10k would strengthen the connection between the spatio-temporal design and observed behavior, rather than stating claimed improvements generically.
- Statistical significance or variance reporting across runs would improve reliability.
- VOT2018/2019/2020 benchmark results would broaden comparability with a larger portion of the tracking literature.

## Removed Points

These points were flagged for removal; treat them with caution.

- **"No code release"** → Removed per hard rule: reproducibility nitpicks about artifacts impractical to include in a submission.
- **"No VOT benchmark results"** → Removed: requesting additional experiments beyond the paper's stated evaluation scope (moved to Nice-to-Haves).
- **"Baseline MixFormer MACs not reported in Table 4"** → The "None" row in Table 4 is the baseline; this specific sub-claim by the harsh critic is incorrect.
- **"Parser-artifact notation issues (I_S^{t+})"** → Per hard rule: parser artifacts, not author errors.
- **"Dimensional mismatch is a critical gap"** → The search region is resized to a fixed input size (288 or 384 as mentioned in the text), making attention map dimensions consistent across frames. The concern is a clarity issue, not a correctness flaw.
- **Generic strengths** (e.g., "addresses an important problem") → Removed: lack specific evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify how USTAM differs from Xie et al. (2023) and other prior spatio-temporal one-stream transformer trackers. Without this, the novelty claim is incomplete.
2. State the exact number of MAM blocks, define the "asymmetric attention scheme," and provide dimensions for the spatial attention post-processing layers.
3. Present a direct, unambiguous comparison between USTAM and MixFormer (same backbone, training data, settings) in the main results table, or at minimum clearly state the relative performance in the main text rather than relegating this to the ablation.
4. Either substantiate the "fewer demands on computational resources" claim with cross-method FLOP/parameter/speed comparisons, or remove the claim from the introduction.
5. Fix the row/column terminology in Eq. 6 and explicitly describe how attention maps are aligned across frames.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>