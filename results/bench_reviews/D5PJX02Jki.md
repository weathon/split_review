Now I have a thorough understanding of the paper and calibration anchors. Let me now synthesize the final review.

---

## Summary

This paper proposes RoPE++, a position embedding extension that re-incorporates the imaginary component of the complex-valued dot product that standard RoPE discards. The imaginary part is computed as a parallel set of attention heads via a simple −π/2 query rotation, yielding two configurations: RoPE++<sub>EH</sub> (same head count, halved KV cache) and RoPE++<sub>EC</sub> (same cache, doubled heads). Pre-training experiments at 376M and 776M scales show consistent gains over RoPE and other position embeddings on both short- and long-context benchmarks, with noise-ablation experiments causally confirming the imaginary heads' dominant role in long-context retrieval.

## Strengths

- **Genuinely novel idea with clean implementation**: Re-incorporating the discarded imaginary component of RoPE's complex attention as a parallel head group is a simple yet previously unexplored direction (Section 3.1, Equations 1–4). The implementation requires only a −π/2 rotation of query vectors and reuses the existing RoPE kernel, adding negligible overhead.

- **Two practical configurations with complementary trade-offs**: RoPE++<sub>EH</sub> halves KV cache and QKV parameters while roughly matching standard RoPE on long-context benchmarks (Table 2: 776M RULER avg 28.6 vs RoPE 27.4); RoPE++<sub>EC</sub> delivers clear gains at equal cache cost (RULER avg 29.4). This gives practitioners a genuine efficiency–quality choice (Section 5.1, Figure 4).

- **Consistent long-context gains with causal validation**: Table 2 demonstrates RoPE++<sub>EC</sub> outperforming RoPE on RULER and BABILong across 4k–64k context lengths at both model scales. The noise-perturbation experiment (Section 5.2, Figure 5e,j) provides causal evidence: corrupting imaginary heads degrades RULER-4k scores by 5–8 points more than equivalent corruption of real heads.

- **Demonstrated compatibility with existing techniques**: Table 3 shows RoPE++<sub>EC</sub> maintains its advantage over RoPE when combined with Linear PI or YaRN for long-context adaptation, confirming the method generalizes beyond the NTK-scaling setting used in the main experiments.

## Weaknesses

### Fatal

None.

### Major

- **Theoretical motivation remains heuristic rather than rigorous**: Section 3.2 derives the characteristic curve of the imaginary attention as a sine integral and argues it captures long-range dependencies because the curve "declines very slowly beyond a certain distance." The curve is oscillatory, not monotonic, and the argument that the negative imaginary part makes attention "on average larger regardless of relative distance" relies on an unstated (and untestable) assumption about query-key similarity. The paper acknowledges the counter-intuitive nature of sin-based distance modeling but does not formalize the conditions under which the claim holds. This weakens the explanatory contribution but does not undermine the empirical results.

### Minor

- **No head-count control for RoPE++<sub>EC</sub> isolates the imaginary mechanism from capacity effects**: RoPE++<sub>EC</sub> doubles the number of attention heads, and the paper does not include a baseline that doubles heads through a parameter-free mechanism without the imaginary rotation. The noise-ablation and the RoPE++<sub>EH</sub> configuration (equal heads, halved parameters) provide partial evidence that the gains are not merely from extra capacity, but a direct head-count control would strengthen the causal claim that the imaginary form, specifically, drives the improvement.

- **Experimental scale is modest for long-context claims**: Models are 376M and 776M parameters, trained on 50B tokens with a 4k initial context window and 32k continued training. While this is comparable to or exceeds the scale in several accepted position-embedding papers (e.g., PoPE at 124M–774M, BAM at 120M–1.1B), the practical importance of long-context LLMs is most salient at larger scales (1B+), and scaling behavior remains unverified.

- **Attention-pattern analysis relies on anecdotal examples**: Figure 5 presents heatmaps for only two hand-picked heads per model (four total). The claim that "imaginary heads attend markedly to global information" would be stronger with aggregated statistics (e.g., attention decay curves averaged over all heads or full evaluation sets).

- **Length-extrapolation analysis could be more direct**: Section 3.4 provides a theoretical argument about OOD position embeddings but Figure 3 is a schematic illustration, not an experimental measurement. While Table 2 does test extrapolation from 32k training to 64k evaluation, a zero-shot extrapolation test from 4k training (without continued long-context training) would more directly validate the theoretical mechanism proposed in Section 3.4.

### Trivial

- The framing in the abstract and introduction that standard RoPE "discards" the imaginary part — while mathematically the imaginary part of the complex product is indeed not used — slightly overstates the case, since RoPE was never formulated as computing and then discarding; it was formulated as taking the real part of the complex multiplication as the attention score.

## Nice-to-Haves

- A larger-scale experiment (1B+ parameters) would strengthen confidence that the benefits persist at scales where long-context capability is most practically relevant.
- Aggregated attention-decay curves comparing real vs. imaginary heads over the full evaluation set would ground the characteristic-curve claims more rigorously.
- An ablation on the negative sign (e.g., using |Im[·]| or a learnable sign) would test whether the sign choice in Equation 2 is critical or arbitrary.

## Removed Points

These points were flagged for removal — treat them with caution.

- **"The head-count control baseline is missing, leaving the source of gains ambiguous" (harsh critic, point 1)**: Partially removed / weakened. The paper has RoPE++<sub>EH</sub> (equal heads) and a noise-ablation study that compares real vs. imaginary heads within the same model. The concern is retained at Minor level because a direct head-count control for EC specifically would still be informative, but the paper already has substantial evidence that the imaginary mechanism, not just extra heads, drives the gains.

- **"Length extrapolation benefit is asserted but not empirically validated" (harsh critic, point 3)**: The claim that "no direct extrapolation experiment is reported" is factually incorrect. Table 2 evaluates at 64k after training at 32k, which IS a direct extrapolation test. The paper states this explicitly (line 187): "achieves best performance in 64k context length extrapolation consistently." Removed the "no experiment" framing; retained only the point that a 4k→longer zero-shot test would more directly validate Section 3.4's mechanism.

- **"Figure 3 is a schematic, not an experimental result"**: This is accurate but Figure 3 is labeled as a theoretical comparison figure, not an experimental result. Moved to Minor as part of the length-extrapolation analysis concern.

- **"Models are relatively small...and trained on only 50B tokens, which is modest for drawing conclusions about long-context LLMs at scale"**: Retained at Minor level. This is factually true but is a scale concern common to nearly all position-embedding papers; the paper's scale is actually comparable to accepted work in this area.

- **"Short-context improvements are small and within the range of normal variance"**: The improvements are small in absolute terms (0.8–0.9 points average) but are consistent across most tasks and model sizes. This is not a weakness so much as a reflection that short-context tasks are already near saturation. Removed as a standalone criticism.

- **"The comparison set is only RoPE" for long-context after continued training**: The paper compares with four baselines (FoPE, Pythia, ALiBi) on short-context tasks and focuses on RoPE for long-context continued training, which is the dominant and most relevant baseline. Training all baselines at 32k would be expensive and is not standard practice. Removed.

- **"The visualizations in Figure 5 show only two hand-picked heads per model"**: Retained at Minor as a valid limitation of the analysis.

- **Abstract framing criticism**: The harsh critic says "the imaginary part is not a quantity that is computed and then thrown away." This is a semantic distinction without substance — mathematically, the complex multiplication produces both real and imaginary parts and only the real is used. Any reader will understand the framing. Moved to Trivial.

## Novel Insights

The key insight emerging from the review process is that RoPE++ provides two genuinely distinct configurations (EH and EC) that allow a clean trade-off between efficiency and quality using the same underlying mechanism. This is more practical than most position-embedding proposals, which typically offer a single configuration with no efficiency option. The noise-ablation methodology (comparing real vs. imaginary attention degradation within the same model) is also a clean causal probe that other position-embedding papers could adopt.

## Suggestions

- Add a head-count control experiment: train a RoPE baseline with doubled heads (via dimension splitting or learned linear transformation) at the same parameter count as RoPE++<sub>EC</sub> to isolate the imaginary mechanism from capacity effects. If space is limited, this could go in the appendix.
- Include aggregated attention-decay statistics (mean attention weight vs. relative distance, averaged over all real heads vs. all imaginary heads) to replace or supplement the anecdotal Figure 5 heatmaps.
- Consider a zero-shot length extrapolation test (4k training → 8k/16k/32k evaluation without continued training) to directly validate the Section 3.4 mechanism.

## Score and Decision

### Anchor comparisons:

| Anchor | Avg Score | Comparison to RoPE++ |
|--------|-----------|----------------------|
| MrRoPE (`1J63FJYJKg`) | 6.50 (Oral) | Stronger: more rigorous theoretical unification, training-free extension, higher scores. RoPE++ is less polished theoretically. |
| Frayed RoPE (`W8ZXfNaqku`) | 6.00 (Poster) | Comparable: both offer a simple RoPE modification with geometric/mathematical motivation. Frayed RoPE has deeper analysis (singular values, clustering) but a simpler fix; RoPE++ has a more novel architectural contribution and efficiency configurations. RoPE++'s models are smaller (776M vs 1B/3B) but its benchmark coverage is broader. |
| Frequency Bands (`PR1PPxvG9Q`) | 5.20 (Poster) | RoPE++ is stronger: Frequency Bands is primarily an analysis paper with a simple θ-tuning fix; RoPE++ proposes a novel architectural mechanism with consistent gains and efficiency benefits. |
| PoPE (`kf2mzS6xfk`) | 4.00 (Reject) | RoPE++ is stronger: PoPE has a nice theoretical motivation but weaker long-context benchmarks; RoPE++ has more comprehensive evaluation (RULER, BABILong, multiple context lengths, noise ablation). |
| TAPA (`U1xQiqTnBp`) | 4.00 (Reject) | RoPE++ is stronger: TAPA has theoretical proofs but computational overhead and only perplexity evaluation; RoPE++ has clean efficiency and broader benchmarks. |
| Bayesian Attention (`dXJB9O8fLd`) | 4.00 (Poster) | RoPE++ is stronger: BAM has a nice framework but narrow evaluation; RoPE++ has broader benchmarks and compatibility demonstrations. |
| DroPE (`RlPVSeKjoc`) | 3.50 (Poster) | RoPE++ is stronger: DroPE drops position embeddings entirely, a clever but narrow idea; RoPE++ has richer empirical support. |
| Position-Aware NTP (`60Vj3aBnjw`) | 3.00 (Reject) | RoPE++ is clearly stronger in both contribution and empirical validation. |

RoPE++ sits between the Frequency Bands paper (5.20) and Frayed RoPE (6.00) in quality. It has more novelty than Frequency Bands and broader evaluation, but less theoretical depth and smaller models than Frayed RoPE. The core idea is novel and well-executed; the main limitations are modest experimental scale and heuristic (rather than rigorous) theoretical analysis. These are addressable concerns that do not invalidate the contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>