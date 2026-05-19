- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5
Now I have everything I need. Let me produce the final consolidated review.

## Summary

This paper investigates how pre-trained vision-language models (CLIP) can be leveraged for weakly supervised learning (WSL). It first demonstrates that a zero-shot CLIP baseline, augmented with GPT-4o-generated class descriptions, already surpasses prior WSL methods trained from scratch. It then diagnoses that naively fine-tuning CLIP with existing unbiased/corrected risk estimators causes overfitting and feature degeneration. The core contribution is WSFT, a dual-head fine-tuning approach: one head trained with a corrected risk estimator distills high-confidence pseudo-labels, and a second head is trained via ordinary empirical risk minimization on those pseudo-labels with alternating updates. Experiments across PU, Pcomp, and UU learning on four datasets show consistent gains over baselines re-implemented with the same CLIP backbone.

## Strengths

1. **Consistent and substantial improvements across diverse WSL settings** — Tables 1–4 report that WSFT outperforms all compared methods in 9 of 10 PU learning settings, all Pcomp settings, and all UU settings, with gains up to 8.59% over the best competitor. The experiments cover four datasets (CIFAR-100, EuroSAT, Oxford-IIIT Pet, Caltech-101) and three problem formulations. This is the paper's strongest evidence and is convincingly demonstrated.

2. **Diagnosis of a practical problem: fine-tuning pre-trained models with WSL risk estimators causes degradation** — Section 3.2 identifies (via recall curves in Figure 3 and t-SNE in Figure 2 on CIFAR-100 PU learning) that off-the-shelf unbiased and corrected risk estimators lead to overfitting and worse feature separation when applied to large pre-trained backbones. This observation is non-obvious—prior WSL literature focused on moderate-sized models trained from scratch—and provides a clear motivation for WSFT.

3. **WSFT method design is principled and well-ablated** — The dual-head alternating scheme (CRE-trained teacher distills pseudo-labels; student trains via standard risk) is cleanly motivated by the diagnosis. Table 5 confirms that the dual-head design contributes 2.34–3.82% accuracy over single-head variants. The method is supported by theoretical consistency/convergence results (in the appendix) and hyperparameter sensitivity analysis (Figure 4).

4. **All baselines are re-implemented with the same CLIP backbone** — Unlike the initial framing comparison (Figure 1), the main experimental tables control for the backbone, ensuring fair comparison of the WSL algorithms themselves.

## Weaknesses

### Fatal
None.

### Major
- **Motivational evidence for overfitting/feature degeneration is restricted to a single dataset and setting.** Section 3.2 supports the diagnosis only on CIFAR-100 PU learning (Figures 2–3). The paper states "Here, we take PU learning as an example," which is an honest qualifier, but the method's motivation—that "naive fine-tuning with existing risk estimators is suboptimal"—is claimed as a general phenomenon without showing it generalizes to Pcomp, UU, or other datasets. The t-SNE visualizations are qualitative and no quantitative metrics of feature degeneration (e.g., intra/inter-class variance, silhouette score) are provided. This weakens the paper's narrative that the problem is widespread and that WSFT was specifically designed to address it.

### Minor
- **The zero-shot vs. SOTA comparison (Figure 1) is framed in an exaggerated tone.** Figure 1 compares zero-shot CLIP+GPT-4o against GLWS (and implicitly prior SOTA) trained from scratch on different backbones (CLIP ViT-B/16 vs. small architectures like ResNet-18). While the paper is transparent that these are "trained from scratch" methods, the initial framing—especially the abstract's "outperform previous state-of-the-art methods trained from scratch"—overstates the significance of this comparison. The performance gap is overwhelmingly driven by the backbone, not the WSL methodology. The main experiments (Tables 1–4) properly control for this, so the issue is confined to presentation, but the abstract and Section 3.1 could temper the claim to avoid misleading readers into thinking the zero-shot approach is algorithmically superior.

- **The theoretical claims in the abstract are not summarized in the main text.** The abstract says "theoretically, we prove the consistency and convergence rate of the proposed risk estimator," but no theorem statement, convergence rate expression, or even a one-sentence summary of the theoretical result appears in the body. (The proofs are presumably in the appendix, which the parser strips.) A brief summary—e.g., the rate achieved and the key conditions—would help readers assess the theory's relevance without needing to consult the appendix.

- **No comparison against standard self-training/SSL baselines is included.** The WSFT mechanism (CRE-trained teacher → high-confidence pseudo-labels → student trained via standard risk) is structurally similar to self-training pipelines like FixMatch and UDA, adapted to the WSL setting. The paper acknowledges this relationship in the related work (Section 5, citing Sohn et al., 2020) but does not include a baseline that performs naive self-training on CRE outputs (e.g., train g₂ on pseudo-labels from g₁ without alternating updates). Such a baseline would isolate the benefit of the alternating/dual-head mechanism and strengthen the empirical contribution.

- **Justification for choosing Visual Prompt Tuning (VPT) over other fine-tuning methods is missing.** The paper uses VPT without explaining why it was chosen over full fine-tuning, LoRA, or adapters. Since the choice of fine-tuning method interacts with overfitting behavior, this is a missing experimental control.

- **Multi-class extension is claimed but not validated.** Section 2.1 states "our proposal can handle any kind of weak supervision... and can be extended to multi-class setting," but all experiments are binary. This is an unsubstantiated claim.

- **Class prior sensitivity is not discussed.** WSFT (Eq. 4) uses class prior weights π_Te and 1−π_Te. Corrected risk estimators are known to be sensitive to prior misspecification, and WSFT inherits this sensitivity. The paper does not check how performance changes under prior estimation error.

- **GPT-4o prompts used for class descriptions are not provided.** The prompt template is given ("A photo of <class description>"), but the actual GPT-4o outputs used to generate the zero-shot prompts are not included, making this part of the pipeline irreproducible.

### Trivial
- The caption of Table 5 ("using only a single classification head") is ambiguous about which head (g₁ or g₂) is used in the single-head baseline. The surrounding text clarifies that using g₂ alone is the intended comparison, but the caption could be more precise.

## Nice-to-Haves
- A self-training/SSL baseline (as noted above) would strengthen the ablation.
- Reporting statistical significance (e.g., t-tests) for the top-performing entries in Tables 1–4, given the small number of runs (3) and overlapping error bars in some comparisons.
- A brief experiment or discussion of sensitivity to class prior estimation error.
- Investigating whether the selected pseudo-labeled sets (D̂₊, D̂₋) remain class-balanced over training.

## Removed Points
- *Criticism that the zero-shot comparison is "fundamentally unfair":* The paper is transparent about comparing against "methods trained from scratch." The comparison is informative as a motivation, and the main experiments control for backbone. Downgraded from "fundamental unfairness" to minor framing issue.
- *Criticism about missing related work:* I cannot verify missing references without external sources.
- *Criticism about missing appendix content / proofs:* The parser strips appendices from all papers; this is a parsing artifact, not an author omission. However, the main text's lack of a theory summary is a valid presentation concern kept as a minor weakness.
- *Criticism about WSFT lacking novelty relative to SSL:* The paper does cite SSL pseudo-labeling (Sohn et al., 2020) in Section 3.3 and acknowledges the connection in Section 5. The novelty lies in applying this to WSL with a CRE-trained teacher head—not a fundamentally new algorithm but a novel combination. Kept as the "missing SSL baseline" minor weakness rather than a novelty critique.
- *Several generic area-concern sweeps from the harsh critic* (e.g., "could the metric be measuring a proxy," "are confounders controlled") removed as speculative with no concrete anchor in the paper.

## Novel Insights
None beyond the paper's own contributions. The core insight—that CREs cause overfitting when applied to large pre-trained models for WSL, and that pseudo-label distillation from a CRE-trained teacher can mitigate this—is the paper's main finding, and no reviewer insight goes beyond it.

## Suggestions
1. **Widen the diagnostic evidence:** Show recall curves and/or quantitative feature degeneration metrics on at least one additional dataset and one additional WSL setting (e.g., Pcomp on EuroSAT) to support the general claim that naive CRE fine-tuning is suboptimal.
2. **Add a self-training baseline:** Compare against a version where g₂ is trained once on pseudo-labels from a fixed g₁ (no alternating updates). This would isolate the value of the alternating/dual-head design.
3. **Include a short theorem block in the main text:** Even one sentence stating the convergence rate (e.g., "WSFT achieves an O(1/n) rate under mild conditions") would satisfy the abstract's theoretical promise.
4. **Justify or ablate the fine-tuning method choice:** Briefly explain why VPT is preferred over full FT or LoRA, or include a small comparison.
5. **Temper the zero-shot framing:** Add a sentence in Section 3.1 clarifying that this comparison is meant to show the impact of the backbone, not to claim algorithmic superiority.
6. **Provide the GPT-4o prompts** in the supplementary material or a footnote for reproducibility.
