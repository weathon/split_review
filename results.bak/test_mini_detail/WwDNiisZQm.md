Now I have all the information I need. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
None.

### Major
None.

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
These points are flagged to be removed, treat them with caution:
[points removed with justification]

## Novel Insights
One paragraph synthesizing genuinely novel observations.

## Suggestions
- specific actionable suggestion

## Score and Decision

Let me compile the final review now.

Let me carefully filter:

**Harsh Critic's Weaknesses:**

1. **MambaC/MambaIC naming inconsistency** - VERIFIED: Table 1 says "MambaC", text says "MambaIC" (lines 218 vs 231/249). KEEP as Trivial.

2. **Dead centroids** - The paper discusses this in lines 335-337 (Section "The Adaptivity of K") and Table 5/6. It's already addressed. WEAKEN - not really a weakness since the paper acknowledges it and provides an ablation showing minimal impact. Move to a minor point that could be discussed more.

3. **Causality claim overstatement** - The paper says "mitigates" and "relaxes" the strict causality, which seems accurate given the ERF evidence in Figure 9. REMOVE as the criticism is about language strength that is actually appropriate.

4. **BD-rate improvement ambiguity** - The harsh critic misunderstood BD-rate reporting. "BD-rate savings of 7.51%" is the relative BD-rate of CMIC vs MambaVC, not the difference in their VTM-relative BD-rates. Standard terminology. REMOVE.

5. **Missing SegPIC in main tables** - Paper cites SegPIC in related work. Including every prior method is not required. REMOVE (scope creep/speculative).

6. **Complexity comparison explanation** - Paper already explains in Section 4.4 that CMIC's efficiency advantage comes from single selective scan vs multidirectional scans. REMOVE (already addressed).

7. **Training throughput measurement** - The batch size is stated in the text but not the table caption. Very minor. KEEP as Trivial.

**Harsh Critic's "Strengthening the Paper" suggestions:**
These are nice-to-haves, not weaknesses. Move to Nice-to-Haves.

**Strength Finder - Let me verify and filter:**

1. SOTA performance across benchmarks - ✓ Verified from Table 1. KEEP.
2. ERF visualization - ✓ Verified from Figures 7-9. KEEP.
3. Complexity advantage - ✓ Verified from Table 1 and Section 4.4. KEEP.
4. Ablation analysis confirms contributions - ✓ Verified from Table 2. KEEP.
5. Content-adaptive clustering visualization - ✓ Verified from Figure 10, Table 5. KEEP.
6. Negligible inference overhead - ✓ Verified from Table 3. KEEP.

These are all concrete, specific, and evidence-grounded. KEEP all.

Now let me write the review.## Summary

This paper introduces Content-Aware Mamba (CAM), a state-space model for learned image compression that addresses two key limitations of standard Mamba: its content-agnostic scanning order and strict causality. The authors propose Content-Adaptive Token Permutation (CTP), which reorders tokens based on feature-space clustering to group semantically similar tokens, and Global-Prior Prompting (GPP), which injects sample-specific global priors into the SSM to relax the causal constraint. The resulting model, CMIC, achieves SOTA rate-distortion performance across Kodak (-15.91% BD-rate vs VTM-21.0), Tecnick (-21.34%), and CLIC (-17.58%), while reducing parameters by 56% and FLOPs by 57% compared to the prior Mamba-based model MambaIC.

---

## Strengths

1. **State-of-the-art rate-distortion performance across all three benchmarks.** Table 1 and Figures 4-6 show CMIC consistently outperforming all prior learned methods, including both Mamba-based (MambaVC, MambaIC) and Transformer-based (FTIC, TCM-L) models. The BD-rate reductions of -15.91%, -21.34%, and -17.58% relative to VTM-21.0 on Kodak, Tecnick, and CLIC datasets are substantial. The RD curves confirm CMIC achieves the highest PSNR across the full bitrate range on each dataset.

2. **Content-adaptive effective receptive field demonstrated through ERF visualizations.** Figures 7-9 directly validate the core claims. Figure 8 shows CMIC's per-image ERF aligns with semantic image structure (hair, feathers, shoreline) while prior models yield compact, content-agnostic ERFs. Figure 9 cleanly isolates the individual contributions: GPP extends the receptive field beyond the causal scan boundary, and CTP reshapes it toward semantically related regions.

3. **Significant complexity advantage over prior Mamba-based LIC models.** Table 1 reports CMIC uses 69.11M params and 2.39 TFLOPs vs MambaIC's 157.09M params and 5.56 TFLOPs—a 56% and 57% reduction respectively. Peak GPU memory is 4.44 GB versus 20.32 GB (78% reduction). The paper correctly attributes this to the use of a single efficient selective scan instead of multi-directional scans.

4. **Ablation analysis cleanly confirms individual and combined contributions.** Table 2 shows CTP alone yields 1.8-2.4% BD-rate improvement, GPP alone yields 0.5-1.4%, and combining them yields 2.7-3.6%, confirming complementarity. Table 4 further validates that CAM blocks outperform alternatives (Conv block, 2D Mamba, attention-only, CAM-only) at comparable parameter/FLOP counts.

5. **Content-adaptive clustering visualization validates semantic grouping.** Figure 10 shows binary masks for individual clusters where tokens sharing visual attributes (red doors in Kodim01, clouds in Kodim21, feathers in Kodim23) are grouped together. Table 5 shows cluster activation is dynamic per image (mean 23.27 active clusters on Kodak, variance 90.91), confirming the method genuinely adapts to content.

6. **Negligible inference overhead from the proposed modules.** Table 3 reports CMIC throughput at 22.05 samples/s on 256×256 patches, only 5% below the baseline without CTP&GPP (23.19 samples/s) and substantially faster than TCM-L (17.80), MambaVC (6.55), and MambaIC (9.35). Decoding time on a 2K image increases by only 4%.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The paper frames the high rate of dead centroids (63.6% on Kodak, 58.9% on CLIC) as a positive "adaptivity" without fully discussing the potential model capacity waste.** Table 5 shows that only ~36-41% of centroids are activated per image on average. The K=32 ablation (Table 6) shows only a 0.94 percentage-point BD-rate drop (from -15.91% to -14.97%), which the paper correctly notes as "modest." However, this also implies that two-thirds of the codebook entries are never used—a genuine inefficiency that merits balanced discussion rather than purely positive framing. The paper acknowledges the observation but could more explicitly address whether this indicates suboptimal codebook utilization or a design choice that should be reduced (e.g., by using a learnable codebook size).

### Trivial

1. **Naming inconsistency for a main baseline.** Table 1 lists the method from Zeng et al. (2025) as "MambaC" while the text (Sec. 4.3, line 249) consistently refers to it as "MambaIC." These refer to the same model. This is not structurally important but creates momentary confusion when cross-referencing the table against the text.

2. **Table 3 could explicitly state the batch size.** The caption for the throughput ablation table reads "Throughput Ablation" without mentioning the 256×256 patch size and batch size of 8, which are stated in the text body but not in the table caption itself. Including these in the caption would improve standalone readability.

---

## Nice-to-Haves

- **Oracle comparison for cluster organization.** A direct analysis comparing the learned cluster-based token permutations against an oracle scan path (e.g., showing that the permuted sequence has higher average pairwise feature-similarity between adjacent tokens than the raster-scan sequence) could further illuminate the mechanism and reinforce the claim that feature-space proximity drives RD gains. The visual cluster evidence is already strong; this would add quantitative support.

- **A systematic characterization of clustering failure cases.** Figure 10 shows semantically meaningful groupings for three example images, but the paper could strengthen its contribution by analyzing when the clustering succeeds or struggles (e.g., images with uniform texture, many small objects, or high-frequency patterns). This stays within the paper's content-adaptivity scope.

---

## Removed Points

These points were surfaced by the reviewers but are removed after verification. Treat them with caution — they do not reflect genuine weaknesses in the paper:

- **"Causality claim is overstated"** — The paper uses "mitigates" and "relaxes" strict causality, not "removes" or "eliminates." The ERF visualization (Figure 9, column c) confirms non-causal influence. The language is appropriate for the mechanism.

- **"BD-rate improvement phrasing is ambiguous"** — The phrase "surpasses MambaVC with BD-rate savings of 7.51% on Kodak" uses the standard compression convention of reporting relative BD-rate between two methods. The harsh critic's concern about percentage points vs. percentages reflects a misunderstanding of BD-rate as a relative metric.

- **"Missing SegPIC from main tables"** — SegPIC (Liu et al., 2024b) is cited in the related work (Sec. 2.3) and uses a fundamentally different approach (semantic masks + dynamic CNNs). Including every prior content-adaptive method in the main comparison tables is not standard practice.

- **"Complexity comparison needs more explanation"** — The paper already explains in Sec. 4.4 that CMIC's efficiency gains come from using a single selective scan instead of multi-directional scans, and this is also mentioned in the introduction (quadrupling computational complexity).

- **"Dead centroids are a potential limitation" (as a major concern)** — The paper already provides a full discussion (Sec. "The Adaptivity of K") with statistics and an ablation over K values showing minimal performance impact. The remaining concern is minor (see Weaknesses).

---

## Novel Insights

None beyond the paper's own contributions. However, the ERF analysis in Figure 9 provides unusually direct evidence that the two proposed mechanisms operate as intended: GPP visibly extends the receptive field beyond the causal boundary, and CTP reshapes it toward semantically related regions. This type of per-component causal validation—showing what each module actually *does* to the model's behavior—is more rigorous than typical ablation tables and sets a good standard for the field.

---

## Suggestions

- Unify the naming of the Zeng et al. (2025) baseline (MambaC/MambaIC) between Table 1 and the text.
- Add the batch size and patch resolution to the Table 3 caption.
- In the "Adaptivity of K" discussion, add a sentence explicitly noting that the K=32 ablation suggests a leaner codebook could suffice for most content, with the larger codebook serving as a flexible upper bound. This turns a potential concern into a positive design insight.

**Anchors used for calibration:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews/cagNCwQEEN.md` | 3.40 | R1 (weak) | Low-quality Mamba paper; weaker methods and rigor. Not comparable. |
| `/home/wg25r/review_agent/human_reviews/vOfDGYGVyj.md` | 2.50 | R1 (weak) | Withdrawn paper; not comparable. |
| `/home/wg25r/review_agent/human_reviews/qWtz3dOmML.md` | 3.00 | R1 (weak) | Withdrawn paper; not comparable. |
| `/home/wg25r/review_agent/human_reviews/0yVP49SDg0.md` | 3.25 | R1 (weak) | Withdrawn paper; not comparable. |
| `/home/wg25r/review_agent/human_reviews/qi7udwV66M.md` | 4.25 | R1 (mid) | Zero-shot diffusion compression paper, avg 4.25 (reject). Weaker results, less thorough evaluation. Our paper is significantly stronger. |
| `/home/wg25r/review_agent/human_reviews/pRCTRC6icM.md` | 5.00 | R1 (mid) | Unrelated topic (contrastive pre-training). Not directly comparable. |
| `/home/wg25r/review_agent/human_reviews/Z7aq3djHZw.md` | 6.25 | R1 (mid) | JPEG-LM: creative idea but limited evaluation (inpainting only, no standard benchmarks). Our paper has far more thorough evaluation. |
| `/home/wg25r/review_agent/human_reviews/ulIW7Frjpn.md` | 4.75 | R1 (mid) | LLM as entropy model for transform coding. Novel but limited scope. Our paper is stronger. |
| `/home/wg25r/review_agent/human_reviews/CxXGvKRDnL.md` | 8.00 | R1 (strong) | Progressive diffusion compression (Oral). Theory-grounded, paradigm-shifting. Our paper is a solid engineering contribution but not at this level. |
| `/home/wg25r/review_agent/human_reviews/gzqrANCF4g.md` | 8.00 | R1 (strong) | Language model for visual generation. Different subfield. |
| `/home/wg25r/review_agent/human_reviews/j7b4mm7Ec9.md` | 7.60 | R1 (strong) | Watermarking, different area. |
| `/home/wg25r/review_agent/human_reviews/WyEdX2R4er.md` | 8.00 | R1 (strong) | VLM understanding, different area. |
| `/home/wg25r/review_agent/human_reviews/HKGQDDTuvZ.md` | 6.00 | R2 (narrow) | **FTIC (Frequency-Aware Transformer, poster).** The closest anchor. BD-rates of -14.5/-15.1/-13.0% vs VTM-12.1. Our paper achieves larger margins (-15.91/-21.34/-17.58% vs VTM-21.0, a stronger baseline), has clearer novelty, better ablations, and ERF visualizations. Clearly stronger than this 6.0 paper. |
| `/home/wg25r/review_agent/human_reviews/AL1fq05o7H.md` | 6.25 | R2 (narrow) | Mamba (original) paper with mixed reviews (8,8,6,3). Different domain (NLP). |
| `/home/wg25r/review_agent/human_reviews/0A6f1b66pE.md` | 4.60 | R2 (narrow) | Mamba for vision-language models (withdrawn). Weaker than our paper. |
| `/home/wg25r/review_agent/human_reviews/XKQ2qzajbU.md` | 5.00 | R2 (narrow) | GlobalMamba - image serialization for Vision Mamba (withdrawn). Related but different domain. |
| `/home/wg25r/review_agent/human_reviews/FowFLhUTgO.md` | 5.50 | R2 (narrow) | V2M - 2D Mamba for images (reject). Not compression-specific. |
| `/home/wg25r/review_agent/human_reviews/U67J0QNtzo.md` | 7.50 | R2 (narrow) | **Disentangled Training for LIC (Spotlight).** Theoretical analysis of training convergence with broad applicability. Different kind of contribution—more conceptual. Our paper's contribution is narrower in scope. |
| `/home/wg25r/review_agent/human_reviews/Tv36j85SqR.md` | 7.20 | R2 (narrow) | **Lattice Transform Coding (Spotlight).** Theoretical framework for vector quantization in neural compression. Mixed reviews (6,8,6,8,8). Stronger theoretical contribution than our paper. |
| `/home/wg25r/review_agent/human_reviews/Cy5v64DqEF.md` | 7.50 | R2 (narrow) | **Idempotence and Perceptual Compression (Spotlight).** Novel theoretical framework. Higher conceptual contribution than our paper. |
| `/home/wg25r/review_agent/human_reviews/D5mJSNtUtv.md` | 6.00 | R2 (narrow) | FSAR entropy coding (spotlight). Different subproblem (lossless compression). |
| `/home/wg25r/review_agent/human_reviews/42lcaojZug.md` | 6.75 | R2 (narrow) | Neural rate control for video (poster). Different domain (video compression rate control). |

**Round 1 bracket:** 4.5–7.5 (middle band). The paper is clearly not in the weak band (avg < 3.5, papers with fatal flaws or withdrawn) nor in the strong band (avg > 7.5, paradigm-shifting theoretical contributions).

**Round 2 narrowing:** The closest anchor is FTIC (avg 6.0, poster), which our paper clearly exceeds in performance, novelty clarity, and evaluation thoroughness. Our paper is not at the theoretical contribution level of the 7.2–7.5 Spotlight papers. The final score sits between these: stronger than a 6.0 paper but below the 7.2+ theoretical contributions.

**Score rationale:** 6.5 reflects a solid paper that makes a well-motivated, well-validated contribution. The two proposed components (CTP and GPP) are technically sound, supported by thorough ablations and unusually informative ERF visualizations, and yield SOTA results with substantial complexity advantages. The weaknesses are minor (naming inconsistency, dead centroid framing that is already acknowledged but could be more balanced). This is a clear accept at the poster level.

---

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>