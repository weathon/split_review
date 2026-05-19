Now let me run the calibration search to bracket the score.**Round 1 bracket: 5.5–7.0.** The paper sits above the 4.5-scoring erroneous agreements paper (narrower scope, less substantive) but below the 8.0 modality-gap analysis paper (more theoretically rigorous, introduced new metrics, 7 takeaways with causal discovery). Let me narrow within this range.Now I have enough anchor comparisons to finalize the review. Let me write it up.

---

## Summary

This paper argues that CLIP's intra-modal representations (image-to-image and text-to-text similarities) are systematically suboptimal because CLIP's inter-modal contrastive loss enforces image-text alignment but imposes no constraint on same-modality distances. The authors demonstrate this through a toy Dogs vs. Cats experiment and large-scale retrieval benchmarks, then show that mapping query features into the complementary modality via Optimization-based Textual Inversion (OTI, adapted) and a new Optimization-based Visual Inversion (OVI) consistently improves retrieval. Extensive experiments span 15 datasets, 5 model variants, and include ablations via SLIP (intra-modal loss during pretraining) and temperature-controlled modality gap manipulation.

---

## Strengths

- **Controlled diagnosis of intra-modal misalignment (Sec. 2):** The Dogs vs. Cats experiment filters away inter-modal failures first, leaving only a population where CLIP's inter-modal alignment is perfect, and still observes 71.5% R-Precision — demonstrating that inter-modal alignment does not imply intra-modal alignment. This is a clean, logically tight setup.

- **Comprehensive empirical scale (Table 1):** OTI improves image-to-image retrieval on *all* 15 datasets across 5 models (OpenAI CLIP ViT-B/32 and ViT-L/14, OpenCLIP on DataComp, SigLIP-B/16), establishing the finding as model-agnostic and loss-agnostic (CLIP vs. SigLIP).

- **Clever inter-modal control via zero-shot classification (Sec. 6.3 / Table 2 right):** The same OTI-inverted features that boost intra-modal image-to-image retrieval *hurt* zero-shot image classification. Because the paper reuses identical features for both evaluations, the result cleanly rules out the hypothesis that modality inversion is a universal performance hack — improvement is direction-sensitive, exactly as predicted by the theory.

- **Novel OVI contribution (Sec. 5.2):** The paper introduces OVI, which optimizes pseudo-patches in patch embedding space and uses nearest-neighbor interpolation to handle fixed ViT patch counts. This is a non-trivial adaptation that extends modality inversion to the text-to-visual direction with no external data or trained adapters.

- **Causal link to modality gap (Sec. 6.6 / Table 4):** Fine-tuning CLIP at τ=1.0 (which closes the gap) eliminates OTI's retrieval benefit; fine-tuning at τ=0.01 (preserving the gap) does not. This is the strongest mechanistic evidence in the paper and directly connects the phenomenon to the gap rather than to fine-tuning as such.

- **SLIP analysis (Sec. 6.5 / Table 3):** Showing that adding an intra-modal SimCLR-like loss during pretraining substantially reduces OTI's benefit is a prescriptive finding: if intra-modal tasks matter, pre-trainers should include intra-modal losses. This adds practical value beyond mere diagnosis.

---

## Weaknesses

### Fatal
None.

### Major

- **Text-to-text retrieval is circular by construction.** In Sec. 6.2, ground-truth for text-to-text retrieval is defined by "other captions of the same image." OVI moves text features into image space, precisely aligning them with the visual referent shared by the correct-match captions. Under this definition, improvement is structurally encouraged: the task's ground-truth is defined by visual correspondence, and OVI optimizes toward visual features. The paper acknowledges the pragmatic motivation (CLIP's 77-token limit, its pretraining distribution) but does not acknowledge the circularity in the claims or conclusions. This means the text-side of the claim — that inter-modal representations are better for text tasks — is not well-supported; the experiment only establishes that inter-modal representations are better for a text task *defined by visual content*. The core image-retrieval finding stands independently, but the generalization to text is overstated.

- **No comparison with CODER, despite the explicit citation.** Section 3 explicitly names CODER (Yi et al., 2024) as addressing the same intra-modal misalignment problem for retrieval/classification. CODER is not included as a baseline anywhere in the experimental section. Since CODER is specifically designed to fix the same problem, omitting it leaves the paper's relative contribution ambiguous — it is unclear whether OTI/OVI outperform, match, or fall behind a purpose-built method.

### Minor

- **Stopping criterion for OTI/OVI is not fully specified as a generalizable procedure.** The paper uses 150 steps for OTI and 1000 for OVI across experiments. Section 6.4 discusses *why* early stopping is needed and notes step count as a "hyperparameter that could be cross-validated," but does not state how 150 and 1000 were selected in practice (e.g., whether by inspecting held-out retrieval metrics). If those values were chosen by peeking at task performance, the gap over the baseline could be slightly inflated. The paper should explicitly describe the selection methodology to close this ambiguity.

- **SLIP scale confound in Sec. 6.5.** SLIP is pretrained on CC3M (~3M pairs) with a ViT-B/32, while the CLIP variants in Table 1 are trained on 400M pairs or DataComp-scale corpora. The reduced OTI benefit for SLIP could reflect better intra-modal alignment from the SimCLR loss *or* simply a different model scale and data distribution. The paper should flag this as a confound, even if an apples-to-apples comparison is infeasible.

### Trivial
None.

---

## Nice-to-Haves

- A text-to-text retrieval task using ground truth defined by textual content (e.g., a sentence similarity benchmark or topic retrieval with short CLIP-compatible queries) would genuinely test whether inter-modal representations help text similarity beyond visually anchored tasks. If OVI helps there too, the claim generalizes properly; if not, the finding becomes more precisely scoped.
- An order-of-magnitude runtime comparison for OTI and OVI versus direct feature extraction would help readers calibrate the practical tradeoff (the limitation is acknowledged but not quantified).
- A post-hoc gap-closing ablation (e.g., using Liang et al.'s affine transform) instead of full COCO fine-tuning in Sec. 6.6 would isolate gap closure from the other effects of fine-tuning (distributional shift, embedding reorganization), sharpening the causal claim.
- Fig. 3 establishes that performance peaks early; exploring whether a proxy criterion (gradient norm, loss plateau) reliably identifies the stopping point without labeled data would increase OTI/OVI's practical value.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — "Mechanism claim not conclusive / τ=1.0 confound"**: The critic correctly identifies that τ=1.0 fine-tuning changes more than the gap. However, the paper explicitly acknowledges the τ=0.01 reference condition (line 269: "The results of the reference model demonstrate that this outcome does not stem from the fine-tuning strategy"), which addresses the confound. The concern is demoted to a nice-to-have (post-hoc affine ablation), not a flaw.

- **Harsh Critic — "81.4% mAP / 71.5% R-Precision not catastrophically misaligned"**: Technically true that on a binary task, performance 20–30 points above random is not extreme, but the authors explicitly acknowledge this is a "toy" diagnostic and characterize the larger 15-dataset results as their main evidence. The experiment is framed correctly. Removed as a non-issue.

- **Harsh Critic — "OVI positional embedding degeneracy at P=1"**: This is speculative. The paper notes P=1 is sometimes insufficient (Sec. 5.3) and uses larger P where needed. No evidence of degenerate behavior is presented, and the concern requires information not in the paper. Removed.

- **Harsh Critic — "Gallery asymmetry could inflate similarity dynamic range"**: The claim that asymmetric query/gallery encoding could inflate pairwise similarity range is a speculative alternative explanation not demonstrated in the paper. The experimental design (only query undergoes OTI, gallery remains native) is clearly stated and is a reasonable practical choice. Removed as speculation.

- **Strength Finder — "The problem is important / addresses an important question"**: Generic. Removed.

- **Strength Finder — "Demonstrates that adding intra-modal loss mitigates misalignment" (as a primary strength)**: Retained but folded into the SLIP strength above, as it's concrete and grounded.

---

## Novel Insights

The paper's sharpest observation — that the same OTI-inverted features simultaneously improve intra-modal retrieval and hurt inter-modal zero-shot classification — elegantly shows that there is no universal "better representation" and that the value of crossing the modality gap depends entirely on the task's modality structure. This asymmetric evidence design, reusing identical computed features for two tasks with opposite outcomes, is a particularly clean way to rule out regularization-based alternative explanations and is likely to be a useful methodological template for future work analyzing VLM embedding spaces.

---

## Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/.../uAFHCZRmXk.md` ("Two Effects, One Trigger") | 8.0 | R1 | Stronger: causal discovery via info-imbalance, new metrics (RMG/MOAD), 7 takeaways, deeper theoretical grounding; clearly above this paper |
| `/home/wg25r/.../5Ca9sSzuDp.md` ("Interpreting CLIP's Image Representation") | 8.0 | R1 | Stronger: deeper mechanistic decomposition, strong zero-shot segmentation results |
| `/home/wg25r/.../S5yOuNfSA0.md` ("Understanding Transferable Representation in CLIP") | 6.5 | R1/R2 | Comparable: theoretical analysis of CLIP with empirical validation; this paper is similarly scoped but more empirically comprehensive on retrieval while lacking theory |
| `/home/wg25r/.../aPTGvFqile.md` ("Mitigate the Gap: AlignCLIP") | 6.29 | R2 | Comparable: similarly addresses modality gap with a proposed fix; AlignCLIP has unfair baselines and limited applicability concerns; this paper is slightly more rigorous in its analysis but lacks baseline comparison with CODER |
| `/home/wg25r/.../7ffJo4vtTY.md` ("Robust multimodal models have outlier features") | 6.0 | R1/R2 | Comparable but slight edge to this paper: that paper probes 12 models but its core finding is less actionable; this paper's diagnosis is more directly prescriptive |
| `/home/wg25r/.../5E6VOD7W0z.md` ("On Erroneous Agreements of CLIP") | 4.5 | R1 | This paper is clearly stronger: broader coverage, cleaner controls, novel OVI contribution, vs. a more limited single-benchmark analysis |
| `/home/wg25r/.../HfJxXbXlYJ.md` ("LLM2CLIP") | 3.0 | R1 | Much stronger than this anchor |
| `/home/wg25r/.../cpGPPLLYYx.md` ("VL-ICL Bench") | 6.5 | R2 | Less relevant topic but similar score band; benchmark paper vs. analysis paper |

**Round 1 bracket: 5.5–7.0** — clearly above the 4.5 erroneous-agreements paper, clearly below the 8.0 modality-gap analysis papers with theoretical causal discovery.

**Round 2 narrowing:** The paper compares most favorably with AlignCLIP (6.29) and "Robust multimodal models" (6.0). It is slightly more comprehensive and better controlled than AlignCLIP (which has unfair baselines), but both share the weakness of missing a strong competing method in evaluation. The "Understanding Transferable CLIP" paper (6.5) has theoretical foundations this paper lacks. The text-to-text circularity and missing CODER baseline are genuine major gaps that prevent scoring at 6.5+. I place the paper at **6.0**, closely aligned with AlignCLIP and "Robust multimodal models."

---

## Score and Decision

**Originality:** Moderate-high. The OVI technique is novel; OTI is adapted. The diagnostic framing across 15 datasets using the dual task control (retrieval vs. classification with identical features) is genuinely creative.

**Importance:** Moderate-high. Intra-modal CLIP misalignment affects many downstream applications; the finding that gap-leveraging inter-modal features help is practically significant.

**Claim support:** Mostly strong for image-to-image retrieval; weaker for text-to-text due to circular benchmark design.

**Experimental soundness:** Good. Multiple models, many datasets, well-designed controls. Limitations in stopping-criterion specification and CODER omission.

**Clarity:** Good. The paper is well organized and the core argument is cleanly structured.

**Value to community:** Solid. Broad diagnostic coverage, clear prescriptions for pretraining (include intra-modal losses), and a novel single-feature-level inversion technique.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>