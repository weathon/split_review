- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 6, 6, 5, 3
Now I have all the information I need. Let me construct the final review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes SparseVLM, a training-free visual token sparsification method for VLMs that (1) selects text tokens with visual relevance ("raters") to score vision tokens via self-attention logits, (2) uses the rank of the attention sub-matrix to adaptively determine pruning per layer, and (3) recycles pruned tokens via density-peak clustering and summation. Experiments on LLaVA, Mini-Gemini, and VideoLLaVA across image and video benchmarks show efficiency gains with modest accuracy degradation when compared to baselines like FastV and ToMe.

## Strengths
- **Training-free plug-and-play design without extra parameters or fine-tuning.** The method reuses the existing self-attention matrices in VLM decoders, requiring no additional training (abstract, Section 1, Section 3). This is a genuinely practical strength for deployment of off-the-shelf VLMs.
- **Text-guided visual token scoring via visual-relevant rater selection.** Unlike simply averaging over all text tokens, SparseVLM selects only text tokens that are visually relevant (Eq. 6–7) to rate vision tokens. The ablation (Section 5.1) shows this selection improves over using all tokens (by 0.79% on TextVQA and 4.3% on POPE), validating the design choice.
- **Token recycling via density-peak clustering.** Rather than discarding pruned tokens, the method clusters and reconstructs them into compact representations (Eq. 9–11). The ablation (Section 5.2) shows this recycling improves accuracy by up to 17.7% on POPE at high pruning ratios, demonstrating clear benefit.
- **Consistent outperformance over FastV and ToMe on image benchmarks.** On LLaVA, SparseVLM exceeds FastV by 7.7–14.8% and ToMe by larger margins across three token budgets (192, 128, 64). On Mini-Gemini, the gains over FastV are 10.2–21.6% (Section 4.1). These results are reported across multiple datasets (GQA, MMB, MME, POPE, SQA, VQA V2, TextVQA, ConBench), providing reasonable empirical support.
- **Substantial efficiency gains are demonstrated.** On LLaVA-7B, SparseVLM achieves 53.9% CUDA time reduction and 84.4% FLOPs reduction (Section 5.3) with moderate accuracy loss. A theoretical FLOPs analysis (Section 3.4) quantifies savings relative to overhead.
- **Applicability demonstrated on both image and video VLMs.** The method is evaluated on LLaVA, Mini-Gemini (image), and VideoLLaVA (video), showing the framework generalizes beyond static images.

## Weaknesses

### Fatal
None.

### Major

- **The rank-based adaptive sparsification (Eq. 8) is critically underspecified.** The number of pruned tokens is defined as \(N = \lambda (L_v - \text{Rank}(\mathbf{P}))\), but the paper reports neither (1) how matrix rank is computed numerically (e.g., SVD tolerance threshold), nor (2) the value of the scaling factor \(\lambda\). Without these, the adaptive ratio is not reproducible. Furthermore, the paper provides no evidence (e.g., correlation analysis, oracle experiments, or ablation over thresholds) that the rank of an attention logit sub-matrix is a meaningful proxy for visual token redundancy. Since adaptive sparsification is listed as a core contribution (contributions list, line 33), this undermines a central claimed innovation. The hyperparameters \(\tau\) (recycling top-k ratio) and \(\theta\) (cluster center ratio) are also not reported (line 165).

- **The video-task comparison to FastV lacks crucial documentation and the reported gap is implausibly large.** The paper reports SparseVLM achieving 86.5% average accuracy versus FastV's 52.1% on video QA — a 34.4-point absolute gap that is an order of magnitude larger than the image-task gaps (7.7–14.8%). The paper states both methods keep 135 tokens (Section 4.2, line 223) but does not explain how FastV (originally designed for single-image VLMs) was adapted to the multi-frame video setting — e.g., whether its attention computations were applied per-frame, how inter-frame attention was handled, or whether the 135-token budget is particularly unfavorable to FastV's per-frame scoring. Without this documentation, the video results cannot be taken at face value and the claimed superiority on video is not convincingly established.

### Minor

- **Performance numbers are reported inconsistently across sections without clear labeling of which configuration each refers to.** The abstract reports "78% compression with 93% accuracy" (likely ~128 tokens), Section 1 reports "4.5× compression rate while maintaining 93%", Section 5.3 reports "84.4% FLOPs reduction keeping 88% accuracy", and the conclusion reports "88.9% compression maintaining 87% accuracy." These could all refer to different token budgets (128 vs. 64 vs. others), but the paper never explicitly ties each number to its configuration. This makes it difficult for the reader to verify claims and erodes precision.

- **The token recycling method uses element-wise summation (Eq. 11) without analyzing post-reconstruction activation statistics.** Summing multiple hidden states from the same layer changes the norm and distribution of activations compared to the original tokens; the model's subsequent layers were trained on a specific distribution. The paper provides no analysis of whether the summed tokens shift mean/variance beyond the normal operating range, nor a comparison to alternative merging strategies (e.g., averaging, weighted sum). While the empirical results suggest the method works, this missing analysis weakens confidence in its robustness.

- **The "first attempt" claim (line 32: "the first attempt to explore the potential of text-aware guidance for efficient inference of VLMs") is overstated relative to prior work.** FastV (cited in the paper) already uses text-token–to–visual-token self-attention scores to guide pruning, albeit averaging over all text tokens. The genuine novelty is in *selecting which text tokens* to use as raters, not in using text guidance per se. The paper would be better served by precisely positioning its contribution as text-rater selection rather than claiming "first text-aware guidance."

- **The text-rater selection ablation shows only a 0.79% gain on TextVQA over using all text tokens** (Section 5.1), raising the question of whether the extra complexity (cross-attention computation before the decoder) is warranted across all settings. While the gain on POPE is larger (4.3%), the paper does not discuss why the benefit varies so widely between benchmarks.

### Trivial
None.

## Nice-to-Haves
- A sensitivity analysis over the rank computation threshold and λ would greatly strengthen the adaptive sparsification claim.
- Per-benchmark breakdown of the video results and an explanation of how FastV was adapted for video would resolve the largest experimental question.
- An analysis of activation statistics (mean, variance, norm) after token summation would increase confidence in the recycling method.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **Harsh critic's claim that "FastV likely performs poorly because it was applied per-frame"** — While the missing documentation for FastV's video adaptation is a valid concern, the critic's speculation about *why* FastV performs poorly goes beyond what can be verified from the paper alone. The core concern (lack of adaptation documentation) is retained in Major.

2. **Harsh critic's claim that the paper "glosses over" the cost of rank computation** — The paper explicitly states "This stage requires L_t × L_v × min(L_t, L_v) FLOPs for rank computation per layer" (line 137). The cost is acknowledged, not glossed over. REMOVED as factually incorrect about the paper.

3. **Formatting/parser artifacts** — Criticisms about garbled text ("For LLaVA-1.}."), missing tables (\input commands), and missing appendix content are all parser artifacts. These are not present in the original submission. REMOVED per hard rules.

4. **Criticism about token count choices being "arbitrary"** — The paper states these are "3 vision token count configurations (192, 128, and 64) to check the advantages of SparseVLM" — providing a rationale (testing across compression levels). REMOVED.

5. **Strength Finder's strength #3 about "adaptive sparsification ratio via matrix rank"** — This conflicts with the verified weakness that the rank mechanism is critically underspecified. REMOVED.

## Novel Insights

The harsh critic's observation about the suspicious video-comparison gap relative to image gaps is genuinely insightful: a 34.4-point gap on video versus at most 21.6-point on images (and 14.8 on LLaVA) is a pattern that demands explanation. The combination of "per-frame FastV adaptation" + "SparseVLM's cross-frame recycling" could compound advantages in the video setting, but the paper does not disentangle these factors. Similarly, the reviewer's observation that the rank-based heuristic may be computing effective rank via an unspecified threshold — and that different thresholds would produce wildly different pruning behaviors — is a valuable technical critique that the authors should address directly.

None beyond the paper's own contributions.

## Suggestions
1. **Fix the adaptive sparsification.** Either (a) replace the rank heuristic with a simpler, well-specified alternative (e.g., keep a fixed fraction per layer, use attention-score variance), or (b) provide a complete specification (SVD tolerance, λ values, ablation over a sweep) and evidence that rank correlates with actual redundancy.
2. **Document the FastV video adaptation in full.** Describe per-frame handling, inter-frame attention treatment, and provide a sanity check (e.g., does FastV's accuracy on video at 2048 tokens match the baseline?). If the 34.4% gap holds, include per-benchmark analysis to show it is not driven by a subset where FastV catastrophically fails.
3. **Harmonize the reported performance numbers.** Choose one representative configuration per model and clearly label which configuration each number corresponds to. Add a summary table mapping compression ratio → accuracy → FLOPs → latency for all settings.
4. **Report all missing hyperparameters** (λ, rank threshold/tolerance, τ, θ, k for nearest neighbors) and include sensitivity analysis for the most sensitive ones.
5. **Add activation distribution analysis** for the token recycling step, showing that summed tokens do not push hidden states out of distribution, or consider switching to averaging or a learned scaling.
