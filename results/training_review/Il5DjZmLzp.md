## Summary

This paper proposes Foundation Model Canonicalization (FMC), a training-free method that uses energy functions derived from pre-trained CLIP, Stable Diffusion, and SAM to canonicalize images (undo nuisances like rotation, color shifts, and 3D viewpoint changes) before passing them to downstream models. The core idea is that foundation models encode priors about natural image distributions, so minimizing a combined energy over transformation parameters selects the most "natural" (canonical) orientation. FMC outperforms the trained PRLC canonicalizer on rotation benchmarks (CIFAR10/100, STL10, ImageNet) without any dataset-specific training, and shows preliminary evidence of working on color and 3D viewpoint shifts.

## Strengths

- **Training-free canonicalization that beats trained baselines on rotation:** FMC achieves higher pose accuracy than the trained PRLC specialists on CIFAR10, CIFAR100, and STL10 across multiple downstream models (CLIP, ResNet50, ViT) without any training on those datasets (Table 1, Figure 4). The improvement over PRLC is consistent and substantial (e.g., +7.4% rotated accuracy on CIFAR10 with CLIP). This directly supports the paper's core claim that foundation-model priors can substitute for learned canonicalization.

- **Generalization across models and tasks with no retraining:** The same FMC approach works for CLIP classification and SAM segmentation without modification. On SAM, FMC improves C4 pose accuracy by 26.2% over PRLC and achieves a 3.4% mAP gain on COCO (Table 2). This demonstrates that the energy composition strategy transfers across fundamentally different downstream tasks.

- **Modular and principled energy composition:** The framework cleanly separates transformation parameterization, energy function, and downstream model. Combining E_uncond (classifier energy), E_diff (diffusion prior), and E_seg (SAM segmentation prior) through a weighted sum is theoretically grounded in energy-based model composition (Section 3.2, Equation 4). This design makes FMC extensible to new foundation models.

- **Bayesian Optimization for continuous transformation spaces:** Using a GP with expected improvement to minimize the energy over continuous transformations (color, 3D viewpoints) is a practical choice that avoids differentiating through large foundation models (Section 3.3), making the method feasible where exhaustive search is intractable.

## Weaknesses

### Fatal

None. The core contribution—training-free canonicalization via foundation-model energy functions—is sound in principle and supported by evidence on the primary rotation task.

### Major

- **Hyperparameter values are not reported, harming reproducibility.** The energy function has five free parameters (α, β, γ₁, γ₂, γ₃) that control the balance between the CLIP, diffusion, and SAM energies (Equations 3–4, Section 3.2). The paper mentions these "can be tuned with hyperparameter selection via Bayesian Optimization" (Section 5) but never reports the actual values used, whether they were fixed across all datasets/transforms, or tuned per setting. Without this, the experimental results cannot be independently reproduced. The authors should at minimum report the chosen values and include a sensitivity analysis showing how performance varies with small perturbations. This is the most significant weakness: while the paper's claims are likely robust, the current presentation leaves a critical gap in verifiability.

### Minor

- **"Unsupervised" framing is imprecise.** The title, abstract, and paper body repeatedly call FMC "unsupervised" (Figure 1, Section 4.1, etc.). However, the primary energy function E_uncond (Equation 3) requires the full list of dataset class names as text prompts for CLIP's cosine similarity computation. This is a mild form of supervision—the method needs to know the label space at test time. The paper acknowledges that E_uncond "marginalizes over all classes" (line 122), so no per-image label is needed, but the class set is still required. Describing FMC as "training-free" or "without fine-tuning" would be more accurate. This does not invalidate the contribution, but the terminology should be tightened.

- **Color and 3D viewpoint experiments lack meaningful baselines.** For color shifts, the only comparison is to the uncanonicalized CLIP baseline (Figure 5a). The paper mentions SOTA methods (Barron & Tsai 2017, Hernandez-Juarez et al. 2020) but does not include them in the plots, only noting "our method is not competitive." For 3D viewpoints (Figure 6c), the only comparison is again to the original uncanonicalized image, with no baselines like random viewpoint selection or heuristics. The paper positions these as "surprising" findings, and the limitations section acknowledges the lack of SOTA competitiveness, but including even simple baselines would substantially strengthen the evidence. As-is, these experiments are suggestive but not conclusive.

- **PRLC comparison on CLIP is imperfect.** For the CLIP experiments (Figure 4, Takeaway #1), PRLC's canonicalizers—trained for ResNet50—are transferred to CLIP without the EquiAdapt alignment training that PRLC was designed to use (Section 4.1). This puts PRLC at a disadvantage. However, the paper's main results in Table 1 use PRLC's own classifiers (ResNet50, ViT) where the comparison is fair, and FMC still wins there. The CLIP results should be interpreted as evidence of FMC's generalization advantage, not as a strictly cleaner head-to-head comparison. The paper partially caveats this ("For PRLC on CLIP we transfer their ResNet50 canonicalizers") but could do so more prominently.

- **The SAM segmentation experiment reports only "accuracy" (mid) not standard segmentation metrics.** Table 2 reports "mAP" (which is a standard metric) and "pose accuracy." But the text mentions "accuracy" for the SAM segmentation results without clarifying how it is computed (e.g., pixel mIoU, dice score, or something else). This should be specified.

### Trivial

- Line 34: Missing period after "(2022)."
- Line 204: Incomplete sentence ("In Fig. FMC generalizes...").

## Nice-to-Haves

- An ablation study removing each energy component (E_uncond, E_diff, E_seg) individually on a rotation benchmark would confirm all three contribute meaningfully.
- Visualizations of the energy landscape (E_FMC over rotation angles for a single image) and examples of successful/failed canonicalizations would improve intuition.
- Extending FMC to additional foundation models (e.g., DINOv2, ImageBind) would further demonstrate generality.
- A simple non-foundation baseline (e.g., image-moment-based orientation) for rotation would help isolate whether foundation model priors are necessary or if simpler heuristics suffice.

## Removed Points

- **"Unsupervised" as a fatal flaw**: One could argue the method is "unsupervised" in the canonicalization literature sense (no training, no per-image labels needed), but the critic's concern about class-label requirement is noted and kept as a Minor weakness above. This was not removed—simply downgraded from major to minor.
- **Demanding full PRLC retraining for CLIP as a necessary comparison**: The main results (Table 1) already use PRLC's own classifiers where the comparison is fair. The CLIP transfer results are supplementary evidence. This criticism was retained but marked Minor rather than structural.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no fundamental empirical or theoretical insight that the paper itself does not already articulate.

## Suggestions

1. **Report all hyperparameter values** (α, β, γ₁, γ₂, γ₃) for every dataset/transform combination, and add a sensitivity analysis showing performance variation under small perturbations. This is essential for reproducibility.
2. **Replace or qualify "unsupervised" with "training-free"** throughout the paper, or clearly state what "unsupervised" means in this context (e.g., "no training or fine-tuning, though the label set is needed for the CLIP energy function").
3. **Add at least one simple baseline** to the color and 3D experiments (e.g., random selection, pixel-variance maximization for viewpoints) to ground the claimed improvements.
4. **Clarify the segmentation metric** used for SAM (Table 2) and consider reporting mIoU or dice in addition to the current accuracy measure.
5. **Provide a clearer caveat** when presenting CLIP results with transferred PRLC canonicalizers, noting that without EquiAdapt alignment this comparison disadvantages PRLC (even though the fair-comparison results in Table 1 already support the conclusions).

## Score and Decision

The paper's core idea—repurposing foundation model priors as energy functions for training-free canonicalization—is genuinely novel and the rotation experiments provide strong evidence for its effectiveness. However, the unreported hyperparameter values constitute a significant reproducibility gap that must be addressed before the paper can be accepted. The "unsupervised" framing needs clarification, and the non-rotation experiments need strengthening. The contribution is real and the approach is timely, but the presentation and experimental completeness are not yet at the standard required for publication.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>