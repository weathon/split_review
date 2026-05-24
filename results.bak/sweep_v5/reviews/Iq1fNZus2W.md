## Summary

This paper addresses the computational bottleneck of multi-condition control in Diffusion Transformers (DiTs), where the "concatenate-and-attend" strategy causes quadratic growth in attention cost with each added condition. The authors propose Patch-wise and Keyword-Aware Attention (PKA), which decomposes full attention into two specialized modules: Position-Aligned Attention (PAA) for spatial conditions (complexity O(N²) → O(N)) and Keyword-Scoped Attention (KSA) for subject conditions (pruning attention to keyword-activated regions). These are complemented by a condition KV cache and an early-timestep sampling strategy. Experiments on FLUX.1 with LoRA fine-tuning report up to 10× inference speedup and 5.12× VRAM reduction while maintaining competitive generation quality.

## Strengths

1. **Well-motivated design grounded in attention redundancy analysis.** Figures 2 and 3 empirically demonstrate the specific sparsity patterns — diagonal dominance for spatial conditions and keyword-localized activation for subject conditions — that directly motivate PAA and KSA. This gives the architecture a principled foundation rather than being ad-hoc.

2. **Clean architectural decomposition.** PAA (one-to-one aligned attention, O(N) complexity for spatial conditions) and KSA (keyword-guided mask that prunes irrelevant subject-image interactions) are conceptually simple and directly map to the identified redundancies. The condition KV cache is a natural extension of the design principle that conditions only attend among themselves.

3. **Substantial and clearly demonstrated efficiency gains.** Figures 7 and 8 show latency and VRAM growing nearly flat as conditions increase from 1 to 16, with annotated speedup factors (3.90×–10×, 2.46×–5.12×) clearly marked. The efficiency advantage is unambiguous and grows with the number of conditions, which is precisely the paper's target regime.

4. **Generative quality is competitive overall.** Table 1 shows PKA achieves best FID, SSIM, CLIP-I, and DINOv2 on all three tasks. On controllability, it achieves best or tied on 3 of 4 metrics (Canny-Depth F1, Subject-Depth MSE, Canny-Depth MSE). The only notable gap is on Subject-Canny F1 (discussed below).

## Weaknesses

### Fatal
None.

### Major

1. **Controllability overclaim on Subject-Canny.** Table 1 shows PKA achieves F1=0.414 on Subject-Canny vs. UniCombine's 0.551 — a ~25% relative gap. The paper dismisses this as "a narrow margin" (line 259), which is misleading: the gap is substantial and on a directly relevant metric. The abstract and contribution list claim PKA "maintains or even improves... controllability," but this result contradicts that claim for one of the three evaluated tasks. While the paper still leads on other metrics, the framing needs correction.

2. **Early-timestep sampling lacks quantitative validation.** The proposed shifted logit-normal distribution (Section 3.3, Figure 11) is supported only by qualitative progression images at 500–8k iterations. No quantitative metrics (FID, F1, convergence curves, or controlled experiments holding all other settings fixed) are reported. Since this is listed as a distinct contribution alongside PKA, the paper should demonstrate its benefit quantitatively, e.g., comparing final model performance with standard vs. shifted sampling.

3. **Unclear whether quality baselines received comparable fine-tuning.** Section 4.1 describes fine-tuning FLUX.1 with LoRA on a curated Subject200K subset (20k iterations). It states "fair comparison" but does not specify whether OminiControl2 and UniCombine were also fine-tuned on the same subset with the same LoRA setup. If baselines were used off-the-shelf (trained on different data/distributions), the quality comparisons in Table 1 could reflect training endowment rather than method superiority. The efficiency comparisons (Figures 7–8) are architectural and not affected by this concern, but the quality evidence is weakened.

### Minor

4. **KSA mask reuse schedule is underspecified.** The paper states the mask is computed at timestep t and reused at timestep t+1 (line 140). It does not specify what happens at t+2, t+3, etc. — is the mask recomputed every other step, recomputed periodically, or computed once and reused for all remaining steps? The actual overhead of mask generation relative to the attention savings depends on this schedule and should be stated explicitly.

5. **PAA ablation lacks quantitative control metrics.** Figure 9 compares PAA vs. full attention vs. SWA on latency/VRAM with qualitative image samples, but no quantitative controllability metrics (F1 for edges, MSE for depth) are reported for the ablated variants. Without these, the claim that PAA "preserves spatial control as well as full attention" rests entirely on visual inspection.

6. **KSA ablation also lacks quantitative subject consistency scores.** Figure 10 ablates the threshold ε but reports only latency/VRAM and visual results. Quantitative metrics (CLIP-I, DINOv2 scores at different ε values) would substantiate the claimed trade-off.

### Trivial
7. **Keyword selection method not described.** The paper states each caption "contains a descriptive keyword" (line 289) but does not specify whether keywords are extracted automatically or manually annotated, which affects reproducibility and generalizability.

## Nice-to-Haves
- A "full attention + condition cache" baseline in Figure 9 would isolate PAA's benefit beyond caching (the "w/o PAA" baseline may already include caching per the framework design, but this should be stated).
- The perturbation experiment (Figure 5) perturbs "visual condition" representations — clarifying whether the perturbation is applied to condition tokens or the image would aid interpretation.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Unfair baseline comparison invalidates headline quality results" (from Harsh Critic #1):** Downgraded from Fatal to Major (#3 above). The critic framed this as a structural flaw that invalidates the central claim. In practice, quality comparison ambiguity is common and the efficiency results (primary contribution) are not affected. The critic's framing was too severe. Retained as a Major weakness in moderated form.

2. **Criticism that baseline comparison unfair because "asymmetry favors baseline":** Not applicable. The paper does not demonstrate asymmetry in either direction.

3. **"Methodological ambiguity in KSA mask reuse timeline" (Harsh Critic #4):** The critic's characterization that "the actual schedule... is never specified" is accurate but the impact is moderate (minor overhead question, not structural). Retained as Minor (#4 above).

4. **"PAA ablation lacks critical baseline" (Harsh Critic #5):** The critic claims the paper lacks a "full attention with condition cache" baseline. The "w/o PAA" condition (15.38s, 308MB) likely already includes condition-level self-attention and caching as part of the PKA framework design, making it a reasonable baseline to isolate PAA. The criticism was overstated.

5. **Generic speculation about confounders, metric proxies, etc.:** Removed per filtering discipline — no specific anchor in the paper.

6. **Strengths removed from Strength Finder:**
   - "Early-timestep sampling is motivated by a perturbation experiment" — the motivation is interesting but the validation is thin; this conflicts with the identified weakness.
   - Generic/superlative strengths about problem importance — removed as generic.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses surface the controllability overclaim and the validation gap in early-timestep sampling but do not identify fundamentally new observations about the method or problem.

## Suggestions
1. Correct the framing of Subject-Canny F1 results — acknowledge the gap explicitly and discuss potential causes (e.g., does PAA's strict one-to-one alignment struggle when edge misalignment between generated and condition edges is high?).
2. Add a controlled quantitative comparison of standard vs. shifted logit-normal sampling (same model, same data, differing only in sampling distribution) reporting FID/F1/MSE convergence curves.
3. Clarify whether OminiControl2 and UniCombine baselines in Table 1 received identical fine-tuning (same data subset, same LoRA rank, same iterations). If not, add fine-tuned baseline results or acknowledge the limitation.
4. Specify the KSA mask recomputation schedule precisely and report mask generation overhead separately.
5. Add quantitative controllability metrics (F1, MSE) to the PAA ablation (Figure 9) and CLIP-I/DINOv2 scores to the KSA threshold ablation (Figure 10).

## Score and Decision

**Calibration anchor comparison:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| DJSZGGZYVi (Repr. Alignment) | 9.00 | Much stronger — well-validated training methodology at scale. Not comparable. |
| N8Oj1XhtYZ (SANA) | 8.50 | Breakthrough full-system paper. Ours is narrower in scope. |
| LyJi5ugyJx (Consistency Models) | 9.20 | Major theoretical+empirical contribution. Not comparable. |
| lTrrnNdkOX (Qihoo-T2X) | 6.40 | Similar motivation (efficient DiT). Ours has better attention analysis; theirs has broader task coverage (T2I+T2V+T2MV). Comparable quality. |
| D2as3jDmRA (LinFusion) | 6.25 | Similar scope (efficiency through attention modification). Comparable evidence quality. |
| Un0rgm9f04 (VDT) | 6.00 | Similar evidence quality and contribution depth. |
| iIGNrDwDuP (Scaling Laws DiT) | 5.25 | Weaker experimental grounding than ours due to extrapolation concerns. |
| kALZASidYe (Towards Enhanced Controllability) | 3.75 | Significantly weaker — unclear contribution. |
| vnp2LtLlQg (Optimizing Attention) | 3.00 | Far weaker — lacked efficiency metrics, inferior to baselines. |

The paper makes a solid contribution: empirically grounded attention analysis, clean architectural design, and clearly demonstrated efficiency gains. The core weakness is overclaiming on controllability (Subject-Canny F1) and thin validation of the early-timestep sampling component. Placed relative to the anchors, it is comparable to accepted DiT efficiency papers (Qihoo-T2X at 6.40, LinFusion at 6.25) but held back by the overclaiming and missing quantitative ablations. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>