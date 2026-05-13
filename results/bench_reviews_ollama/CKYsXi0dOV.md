Now let me verify the claims about "comparable to 34B" by looking at the specific numbers:

The paper claims "comparable to much larger state-of-the-art models (e.g., 34B)". Let me compare:

- MSVD-QA: BLIP-3-Video (4B, 32 tokens) = 77.7 vs Tarsier-34B = 80.3 → gap ~2.6
- MSRVTT-QA: 60.0 vs 66.4 → gap ~6.4
- ActivityNet-QA: 55.7 vs 61.6 → gap ~5.9
- TGIF-QA: 76.5 vs 82.5 → gap ~6.0
- NExT-QA: 76.4 vs 79.2 → gap ~2.8

Now let me also verify the Tarsier* (re-evaluated under same conditions) numbers:
- Tarsier* 34B: MSVD-QA=79.3, MSRVTT-QA=62.2, ActivityNet-QA=61.5, TGIF-QA="-"

So the gaps are mixed — on some benchmarks (MSVD-QA, NExT-QA), the gap is small (2-3 points), on others (MSRVTT-QA, ActivityNet-QA, TGIF-QA), it's 6+ points. "Comparable" is a stretch for some benchmarks but reasonable for others.

Let me also check: the MSVD-QA and MSRVTT-QA results were from a "subset" training, which the paper explicitly notes.

Now let me think about which criticisms are valid:

1. **"Comparable to 34B" claim**: This is partially valid. The gaps range from ~2.6 to ~6.4, averaging about 5 points. "Comparable" could be argued as somewhat overclaiming, but it's not wildly off especially for a 4B model. The claim is nuanced — the model IS remarkably strong for its size, but "comparable" is a stretch on some benchmarks. This is a **major** weakness — the framing is somewhat overclaimed but the core results are still impressive.

2. **Unfair baseline comparison**: The paper does note that models marked with * were re-evaluated under the same conditions. Other models use different frame counts and resolutions. However, this is standard practice in the field — comparing against reported numbers is normal. The token count comparison is still informative as it shows the magnitude of difference. This is a **minor** concern — while not perfectly apples-to-apples, the paper is transparent about this and provides re-evaluations where feasible.

3. **Ablation uses different training recipe**: This is confirmed in the paper — Table 3 has the footnote "A slightly different training recipe using a subset of the entire dataset (without Mira data)." This IS a concern because the ablation evidence for the core architectural claims comes from a different training setup. However, the ablation is comparing relative performance of different encoders, and it's reasonable to expect the relative ordering would be similar under the full recipe. This is a **minor** weakness.

4. **"You Only Need 32 Tokens" title claim**: The ablation shows 32→128 tokens: MSVD-QA 77.11→77.86 (0.75 drop), NExT-QA 76.4→77.07 (0.67 drop), TGIF-QA 77.07→77.10 (0.03 drop). These are small drops, actually supporting the claim. The model also processes only 8 frames, but the title says "32 tokens to represent a video" — which is about representation compression, not long video. However, the motivation about quadratic cost IS tied to longer videos. This is a valid but **minor** concern — the title is somewhat bold but the evidence largely supports it.

5. **Training on test benchmarks**: The paper trains on training splits of MSVD-QA, etc., which is standard practice in the field. Not a real weakness.

6. **MSVD-QA and MSRVTT-QA "subset" training**: The paper explicitly notes this and explains why (for fairer comparison with prior work). This is a transparency issue, not a methodological flaw.

7. **No experiments on longer videos**: Valid concern. The motivation section highlights quadratic cost for longer videos, but only 8-frame results are shown. However, the token reduction itself is demonstrated, and the architectural contribution (temporal encoder design) is orthogonal to video length. This is **minor** — worth mentioning but the paper's scope is about token reduction, not long video handling.

Let me now compile the final review.

Actually, let me reconsider: the "comparable to 34B" claim deserves more scrutiny. Looking at the specific numbers:

Against Tarsier-34B (reported):
- MSVD-QA: 77.7 vs 80.3 (2.6 gap)
- MSRVTT-QA: 60.0 vs 66.4 (6.4 gap)
- ActivityNet-QA: 55.7 vs 61.6 (5.9 gap)
- TGIF-QA: 76.5 vs 82.5 (6.0 gap)
- NExT-QA: 76.4 vs 79.2 (2.8 gap)

Against Tarsier-34B* (re-evaluated under same 8-frame conditions):
- MSVD-QA: 77.7 vs 79.3 (1.6 gap)
- MSRVTT-QA: 60.0 vs 62.2 (2.2 gap)
- ActivityNet-QA: 55.7 vs 61.5 (5.8 gap)
- TGIF-QA: not available

Interestingly, the re-evaluated Tarsier-34B numbers are closer! On MSVD-QA and MSRVTT-QA, the gap is quite small (1.6 and 2.2). The gap on ActivityNet-QA remains large (5.8). The paper's claim of "comparable" is fair when considering the re-evaluated numbers, but overstated when comparing against reported numbers from models using more frames and higher resolution.

However, the paper compares against BOTH reported and re-evaluated numbers, and the re-evaluated comparison is the fairest one — under identical input conditions, the model IS quite competitive with the 34B model.

This actually WEAKENS the harsh critic's criticism. The more fair comparison (re-evaluated under same conditions) shows much smaller gaps, and the paper deserves credit for providing this fair comparison.

Let me finalize:

Strengths:
1. Strong efficiency-accuracy tradeoff demonstrated with concrete throughput numbers
2. Systematic ablation of temporal encoder designs
3. Competitive results under fair (re-evaluated) conditions, especially impressive for a 4B model
4. NExT-QA results genuinely strong

Weaknesses:
- **Major**: The "comparable to much larger 34B models" claim in the abstract is somewhat overclaimed when comparing against published numbers (gaps of 3-6 points on most benchmarks), though more justified under re-evaluated conditions.
- **Minor**: Ablation study uses a different training recipe than main model
- **Minor**: All experiments use only 8 short frames, so efficiency gains on longer videos (where quadratic cost really matters) are not demonstrated
- **Minor**: Apples-to-apples comparison is only done for 2 of many baselines

Let me write the review now.</think>## Summary

The paper introduces BLIP-3-Video (xGen-MM-Vid), a 4B-parameter video VLM that uses a learned temporal encoder to compress video representations into as few as 32 tokens. The authors explore multiple temporal encoder designs—including spatio-temporal attentional pooling (TokenLearner) and sequential models (Token Turing Machines with grouped memory)—and demonstrate that 32–128 tokens suffice for competitive video QA performance across standard benchmarks.

## Strengths

- **Demonstrated efficiency-accuracy tradeoff with concrete throughput measurements**: The paper reports measured training throughput of 8.2 samples/sec at 32 tokens vs. 3.3 samples/sec without temporal encoding (1024 tokens), providing direct evidence of practical efficiency gains (Section 3.4, "Speed" paragraph).

- **Systematic ablation of temporal encoders**: Tables 3–5 provide controlled comparisons across temporal encoder variants (mean pooling, transformer, vanilla TTM, space-time attentional pooling, sequential model) and token counts (16, 32, 128, 256). The results validate that learnable spatio-temporal encoders outperform simpler baselines (e.g., sequential model at 77.86 vs. mean pooling at 76.75 on MSVD-QA, Table 3).

- **Competitive results under fair re-evaluation**: The paper re-evaluates Tarsier-7B and Tarsier-34B under identical 8-frame, 384×384 conditions (marked with * in Table 1). Under these fairer conditions, the gaps narrow substantially (e.g., MSVD-QA: 77.7 vs. 79.3; MSRVTT-QA: 60.0 vs. 62.2), making the model's efficiency advantage more credible.

- **Strong NExT-QA result**: The 32-token model achieves 76.4 on NExT-QA, which is competitive with many models using thousands of tokens (Table 2), particularly impressive for a 4B model on a benchmark requiring multi-frame temporal reasoning.

## Weaknesses

### Fatal
None.

### Major

- **The "comparable to much larger state-of-the-art models (e.g., 34B)" claim in the abstract is overclaimed relative to published baseline numbers**: Against the reported Tarsier-34B numbers (which use 16+ frames at higher resolution), gaps are ~6 points on MSRVTT-QA (60.0 vs. 66.4), ActivityNet-QA (55.7 vs. 61.6), and TGIF-QA (76.5 vs. 82.5). While the re-evaluated comparison (under the same 8-frame, 384×384 setup) shows smaller gaps, the abstract's framing centers on published SOTA comparisons where the gaps are non-trivial. The paper would be better served by framing this as "competitive efficiency-accuracy tradeoff" rather than "comparable to much larger models."

- **All experiments use only 8 uniformly-sampled frames of short videos, while the primary motivation is efficiency for long videos**: The introduction emphasizes that "the LLM computation is quadratic to the number of total tokens" and positions the work against "brute-force" models using thousands of tokens. However, all evaluation uses 8 frames from short videos, so the scenario where token reduction matters most—longer videos with many more frames—is never tested. The efficiency advantage (32 vs. 4608 tokens) is measured in a regime where even 1024 tokens are manageable, leaving the motivating use case unvalidated.

### Minor

- **The ablation study uses a different training recipe than the main model**: Table 3's footnote states "A slightly different training recipe using a subset of the entire dataset (without Mira data) was used for the ablations." This means the evidence for the core architectural claim (which temporal encoder design is best) comes from a different configuration than the one whose results appear in Tables 1–2. While the relative ordering of encoders is likely robust to this change, it introduces uncertainty about whether the ablation conclusions transfer exactly to the final model.

- **Uneven apples-to-apples comparison coverage**: Only Tarsier and LLaVA-OneVision are re-evaluated under identical conditions. Other strong baselines like PLLaVA-34B (79.9/68.7/60.9/80.6 on the four QA benchmarks) and SlowFast-LLaVA-7B are compared at their reported numbers with presumably different frame counts, resolutions, and training data. The token-count comparison column thus mixes different configurations, and the fairest comparisons (re-evaluated) are a small subset.

### Trivial
None.

## Nice-to-Haves

- Evaluation on longer videos (e.g., 30+ seconds, 16–32 frames) would directly validate the quadratic-cost motivation and demonstrate the approach scales to the regime where it matters most.

- Attention map visualizations from the spatio-temporal pooling showing which regions/frames the 32 tokens attend to, to validate that the model learns meaningful spatio-temporal abstraction rather than a degraded spatial summary.

## Removed Points

- **Training on test benchmark training splits**: The paper trains on the training splits of MSVD-QA, MSRVTT-QA, etc., which is standard practice in video VLM evaluation. Removed as this is the community norm, not a flaw.

- **Mira-Cap custom evaluation split lacks independent baselines**: While true, this is a new dataset the authors introduce for captioning evaluation; providing it as a resource is reasonable and the MSVD-Cap/MSRVTT-Cap benchmarks serve as independent validation.

- **"Captioning-only model outperforming the main model on captioning benchmarks"**: The paper explains this in the table caption: the captioning-only model is specialized for captioning. This is expected behavior, not a weakness.

- **LLM-evaluated answer quality scores lack clear definition**: The paper references using Video-ChatGPT's evaluation methodology, which is a known framework. Removed as this is standard practice.

- **TTM description is underspecified for reproduction**: The paper describes grouped TTM with memory size N×G=512, positional encodings, and attentional pooling to M tokens. While concise, this provides sufficient information for someone familiar with TTM. Reproducibility nitpicks on implementation details are excluded.

- **Demand for re-evaluation of all baselines under identical conditions**: This is impractical for a full paper and the authors already provide the most informative re-evaluations (Tarsier-7B/34B, LLaVA-OneVision).

- **MSVD-QA/MSRVTT-QA using a subset of training data**: The paper explicitly discloses this and explains the rationale (fairer comparison with prior work). This transparency is a strength, not a weakness.

## Novel Insights

The most interesting finding is that token reduction from 1024 to 32 incurs surprisingly small accuracy drops on video QA (e.g., NExT-QA drops only from 77.07 to 76.4), suggesting that for the QA tasks currently used to evaluate video VLMs, most spatio-temporal detail is redundant. This raises the question of whether current benchmarks are demanding enough to differentiate token-efficient representations—or whether the 32-token representation captures most of what these benchmarks test, and more challenging evaluations (longer videos, fine-grained temporal ordering) would reveal the costs of aggressive compression.

## Suggestions

- Reframe the abstract's claim from "comparable to much larger state-of-the-art models" to something like "achieves competitive performance with much larger models while using 100× fewer tokens," which is both more accurate and arguably more compelling.

- Add a results table or discussion on at least one longer-video benchmark (e.g., using ActivityNet-QA with 16+ frames) to validate that the token reduction advantage holds in the regime that motivates the work.

## Score and Decision

The paper makes a solid architectural contribution—demonstrating that learned temporal encoders can compress video representations to 32 tokens with modest accuracy loss. The ablations are systematic and informative, the efficiency gains are concrete, and the NExT-QA results are genuinely strong. However, two issues temper enthusiasm: (1) the "comparable to 34B" framing overclaims relative to the published baseline gaps (though re-evaluated numbers are more favorable), and (2) the motivating use case of long videos with many tokens is never tested, leaving the core efficiency story incomplete. These are addressable rather than fatal, and the paper's core insight—that video QA benchmarks don't require thousands of tokens—is valuable.

**Originality**: The systematic exploration of temporal encoder designs (space-time attentional pooling, TTM variants) within a VLM framework is a useful contribution, though individual components (TokenLearner, TTM) are not novel.

**Research question importance**: Token efficiency in video VLMs is a practical and timely problem.

**Claim support**: The core claim of effective video QA with few tokens is well supported by ablations. The "comparable to 34B" claim is somewhat overstated.

**Experimental soundness**: Solid ablations, though the training recipe mismatch and limited long-video evaluation are notable gaps.

**Clarity**: Well-written and clearly organized.

**Community value**: Provides useful design guidance for efficient video VLMs.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>