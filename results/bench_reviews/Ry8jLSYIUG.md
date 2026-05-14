## Summary

This paper investigates how far current image watermarking methods are from theoretical capacity limits. It develops a geometric lattice-based framework to establish upper bounds on watermarking capacity under PSNR and linear robustness constraints, revealing capacities orders of magnitude beyond what existing models achieve (e.g., over 600,000 bits for a 256×256 image at 40 dB PSNR without robustness). Through controlled minimal-setting experiments — training Video Seal on a single gray image with only a PSNR constraint — the authors show that modern architectures fail to approach these bounds even when real-world complexity is stripped away, while simple linear and handcrafted models get much closer. As practical validation, they train Chunky Seal, a scaled-up Video Seal, achieving 1024 bits (4× prior capacity) with comparable quality and robustness. The paper concludes that substantial headroom remains for architectural innovation in image watermarking.

## Strengths

- **Novel geometric capacity framework (Section 2):** The lattice-based approach to bounding watermarking capacity under PSNR and linear transformations is elegant and provides intuitive, computationally tractable estimates. The progression from absolute capacity (Bound 1) through PSNR-only bounds (Bounds 2–9) to robustness-constrained bounds (Bounds 10–13) is systematic and well-motivated. The framework yields concrete numbers showing 2+ bpp at 40 dB PSNR without robustness — orders of magnitude above the <0.001 bpp seen in practice (Figure 1).

- **Creative controlled experiments isolate failure modes (Section 3):** Training Video Seal on a single gray image with only a PSNR constraint (Section 3.1) is a clever diagnostic that strips away dataset complexity, perceptual losses, and augmentations. The finding that Video Seal cannot embed even 1024 bits in this simplified setting, while a linear embedder reaches 2048 bits (Table 1, Figure 5) and a handcrafted model reaches 456,509 bits, provides concrete evidence that architectural limitations — not problem complexity — drive the capacity gap. The tiling experiment (32×32px model performs similarly to 256×256px) further reveals the architecture fails to exploit available resolution.

- **Practical demonstration of higher capacity (Section 4):** Chunky Seal achieves 1024 bits with PSNR 45.32 dB and overall bit accuracy of 99.15% — comparable to Video Seal's 99.31% at 256 bits (Table 3). The 4× capacity increase with maintained quality and robustness, achieved without hyperparameter tuning on Chunky Seal, provides strong evidence that current architectures have not saturated watermarking capacity. Per-transformation breakdowns in Appendix J.1 confirm robustness across individual perturbation strengths.

- **Addresses confounds systematically (Sections 2.4, 2.6):** The paper preempts natural objections — showing that arbitrary cover images (not just centered gray) reduce capacity by at most 1 bpp (Section 2.4), and that data distribution effects from neural compression estimates reduce capacity by only ~0.05 bpp (Section 2.6). These analyses strengthen the argument that the gap cannot be explained away by these factors.

- **Actionable sanity checks (Section 5):** The proposed design criteria (linear capacity scaling with resolution, linear decrease with PSNR, predictable drops under augmentations) provide concrete guidance for future watermarking architectures.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **LinJPEG bounds are based on an unvalidated linearization (Section 2.5, Appendix G.4):** LinJPEG replaces JPEG's non-linear quantization step with a mask that zeros high-frequency DCT coefficients beyond a diagonal cutoff. Real JPEG also quantizes the *remaining* coefficients, collapsing distinct watermarked images into the same quantized representation — an effect LinJPEG does not capture. The paper acknowledges these are heuristic bounds (lines 427–428) and provides conservative Bound 13 as a lower bound, but Bound 13 also uses LinJPEG for the JPEG case. The claim that compression robustness "cannot fully explain the low capacity" would be strengthened by calibrating LinJPEG against real JPEG capacity loss. This does not undermine the broader argument — the other robustness bounds (crop, rotation) do not rely on LinJPEG and still show large gaps — but adds uncertainty specifically for compression claims.

- **Narrative tension between "structural limitations" and Chunky Seal's success:** The paper argues Video Seal's failure on the simplified task demonstrates "severe structural limitations" (line 103), yet Chunky Seal — a scaled-up instance of the same Video Seal architecture — succeeds at 1024 bits under realistic constraints. The paper acknowledges this tension in the discussion (lines 1000–1005: "we do not suggest that naïvely scaling Chunky Seal is a practical path forward"), but the narrative could be more precise about whether the issue is the architecture's *design* or its *capacity* (parameter count). The tiling experiment does show the architecture fails to exploit resolution, which supports a structural interpretation independent of model size. The evidence overall is sufficient to support the paper's conclusions, but the framing could be sharper.

### Trivial

- **Main-table aggregation hides worst-case behavior (Table 3):** Results are aggregated over wide parameter ranges (e.g., JPEG Q 50–80, Rotate ≤10°). While Appendix J.1 does provide per-strength breakdowns, a brief note in the main text about worst-case performance (e.g., Chunky Seal drops to 65–72% bit accuracy on JPEG Q 40–50 on COCO vs. Video Seal's 97–98%) would give a more complete picture. This is purely a presentation preference.

- **The discussion of absolute bit errors vs. bit accuracy could be clearer:** With 1024 bits at 99.15% accuracy, Chunky Seal produces ~8.7 incorrect bits on average vs. ~1.8 for Video Seal at 256 bits. The paper's claim of "comparable robustness" based on bit accuracy rates is standard and reasonable, but a sentence acknowledging the higher absolute error count would preempt reader questions about practical message recovery without error correction.

## Nice-to-Haves

- Calibrating LinJPEG capacity bounds against real JPEG on a small toy example (e.g., counting distinguishable messages under real JPEG vs. LinJPEG for a small grid) would strengthen the compression-related capacity claims.
- A brief ablation showing whether Video Seal's failure on 1024 bits in the simplified setting can be overcome by simply increasing its parameter count (without the full Chunky Seal scaling) would clarify the capacity-vs-structure question.
- Reporting message-level error rate (fraction of 1024-bit messages fully recovered) with a simple error-correcting code for Chunky Seal would address practical usability concerns.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Figure 1 could mislead readers"** (from harsh critic's section-by-section notes): The figure caption says "what this paper suggests to be possible" — it is appropriately hedged. Not a real weakness; removed.

- **"The tiling experiment sidesteps the question of why the 256×256 model itself fails"** (from harsh critic): The tiling experiment IS the analysis — it demonstrates the architecture fails to exploit resolution, which is the finding. The paper explicitly states "the architecture fails to utilize the available resolution" (line 847). The critic's framing misreads the paper's argument. Removed.

- **Demand for "deeper analysis" of why Video Seal fails** (from harsh critic's "Deeper Analysis Needed"): While additional ablations would be nice, the paper already provides converging evidence from three separate experiments (Video Seal failure, linear model success, tiling). Further analysis is a nice-to-have, not a weakness. Moved to Nice-to-Haves.

- **"Visual comparison of LinJPEG vs. real JPEG"**: Nice-to-have illustration but not a methodological requirement. Moved to Nice-to-Haves.

- **Request to "apply the same scaling recipe to push beyond 1024 bits"** (from harsh critic): This is a suggestion for future work, not a missing experiment that weakens the current paper. The paper already demonstrates feasibility with 1024 bits. Removed.

## Novel Insights

The paper's most novel contribution is the geometric lattice formulation of watermarking capacity. By reframing the problem as counting integer lattice points in the intersection of a hypercube (valid pixel range) and a hypersphere (PSNR constraint), the paper derives capacity bounds that are both conceptually simple and practically computable. The extension to linear transformations via singular value analysis provides a unified way to reason about diverse robustness constraints (crop, rotation, JPEG) within the same geometric framework. The core methodological insight — that architectural limitations rather than fundamental constraints explain the capacity gap — is demonstrated through a particularly clever experimental design: systematically stripping away real-world complexity to isolate failure modes. This controlled-ablation methodology could serve as a template for diagnosing other machine learning systems where theoretical bounds are known but empirical performance lags.

## Suggestions

- Add a sentence or footnote to Table 3 noting the per-strength breakdown is available in Appendix J.1, and mention the worst-case performance gap for harder perturbations (e.g., JPEG Q 40–50 on COCO where Chunky Seal's bit accuracy is notably lower than Video Seal's).
- Consider adding a brief discussion of whether error-correcting codes could mitigate the higher absolute bit-error count at 1024 bits, or whether simple repetition coding would suffice given the high per-bit accuracy.
- For the LinJPEG bounds, a short calibration experiment on a small grid (e.g., 8×8) comparing distinguishable-message counts under real JPEG vs. LinJPEG would add credibility to the compression-capacity claims at minimal experimental cost.

---

**Evaluation across axes:**

- **Originality:** High. The geometric lattice framework for watermarking capacity is novel, and the controlled minimal-setting experimental methodology is creative.
- **Importance of research question:** High. Whether watermarking has hit fundamental limits is a timely and important question for the provenance community.
- **Claims well supported:** Well supported overall, with theory, controlled experiments, and practical validation forming a coherent chain of evidence. Minor concerns about LinJPEG calibration and narrative precision do not threaten the core claims.
- **Soundness of experiments:** Strong. The controlled experiments are well-designed, and the Chunky Seal results include extensive per-perturbation breakdowns in the appendix.
- **Clarity of writing:** Good. The paper is well-structured and arguments are easy to follow. Some aggregation in Table 3 could benefit from more explicit signposting to the appendix.
- **Value to research community:** High. The capacity bounds provide a benchmark for future methods, and the sanity checks offer actionable design principles.

**Anchor comparison:**

- `/home/wg25r/review_agent/human_reviews_2026/pAeEzS4LwS.md` (avg 2.67): Rejected LLM watermarking theory paper with fundamental misunderstandings about computational assumptions. Current paper is substantially stronger — its theoretical framework is well-grounded and validated empirically.
- `/home/wg25r/review_agent/human_reviews_2026/9u8HFU6ioO.md` (avg 3.50): Withdrawn cryptographic watermarking limits paper. Current paper has broader scope and stronger empirical validation.
- `/home/wg25r/review_agent/human_reviews_2026/CbxZ86mWrs.md` (avg 4.00): Rejected geometric-robustness watermarking paper. Current paper has a more novel theoretical contribution and clearer experimental narrative.
- `/home/wg25r/review_agent/human_reviews_2026/TVSPV6D0co.md` (avg 4.67): Rejected high-capacity watermarking paper (LatentSeal) criticized for being a combination of existing works. Current paper has stronger novelty in both theory and controlled experimental design.
- `/home/wg25r/review_agent/human_reviews_2026/st1hrLTP14.md` (avg 6.00): Accepted self-re-watermarking paper with novel threat model and solid experiments. Current paper is comparably strong with broader scope (theory + diagnostics + practical model).
- `/home/wg25r/review_agent/human_reviews_2026/wyucYNGPiW.md` (avg 6.50): Accepted attack-resistant watermarking paper. Current paper has comparable rigor and broader foundational contribution.
- `/home/wg25r/review_agent/human_reviews_2026/EhDgP69DJG.md` (avg 7.00): Accepted PMark paper with solid theoretical framework and experiments. Current paper is comparable — both provide theoretical frameworks with practical validation, though in different watermarking domains.
- `/home/wg25r/review_agent/human_reviews_2026/Jz5SA2KoFt.md` (avg 7.00): Accepted forensic detector confidence paper. Current paper has comparable quality and a similarly well-structured argument.

The paper under review sits above the ~5.0 and below anchors, is clearly stronger than the 4.67 paper, and is comparable to the 6.0–7.0 accepted papers. The theoretical contribution is more foundational than most watermarking papers, the experimental design is unusually thorough, and the practical validation closes the loop convincingly. Minor concerns about LinJPEG calibration and narrative precision are addressable.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>