## Summary

This paper proposes a data selection (dataset pruning) framework that uses CLIP's multimodal (image+text) representations. The pipeline has three modules: (1) dataset adaptation — lightweight MLP adapters fine-tuned on the target dataset with frozen CLIP weights; (2) sample scoring — a Semantic Alignment Score (SAS, cosine similarity between image and class text) and a Sample Diversity Score (SDS, mean distance to k-nearest neighbors); and (3) selection optimization — gradient-based multi-objective optimization with a straight-through estimator to enforce a target selection ratio. Experiments on CIFAR-100, Tiny-ImageNet, and ImageNet-1k show consistent gains over baselines, strong noise-filtering under label corruption, and cross-architecture transfer.

---

## Strengths

1. **Clear noise-filtering ability validated by direct measurement**: Table 2 shows that under 20% symmetric label noise on CIFAR-100, the method selects only 0.24% noisy samples — far lower than any baseline — while improving accuracy by over 10% relative to prior methods. This directly supports the paper's central thesis that CLIP's image-text alignment score (SAS) resolves the ambiguity between genuinely hard samples and mislabeled ones, which unimodal methods cannot.

2. **Selected subsets transfer across diverse architectures**: Table 1 reports results on VGG-16 and DenseNet-121 on Tiny-ImageNet where the method surpasses all baselines on both architectures. Since selection uses CLIP features rather than a target-architecture model, this provides concrete evidence for the claimed cross-architecture generalizability — a property many optimization-based baselines (Glister, MoSo) lack because their selection is architecture-dependent.

3. **Training on selected subsets improves OOD generalization beyond full-dataset training**: Table 4 shows that models trained on the selected subsets outperform models trained on the full ImageNet-1k when tested on ImageNet-Hard, ImageNet-R, and ImageNet-A. This goes beyond the typical goal of lossless compression and demonstrates that selection can improve data quality, not just reduce cost.

4. **Component-level ablation isolates the contribution of the text modality**: The ablation in lines 189–190 replaces the text feature in Eq. 1 with an image-average prototype. Accuracy drops from 46.05% to 16.39% (20% selection ratio, 20% noise), providing a clean counterfactual that isolates what the text modality contributes. This is stronger evidence for a design choice than most data-selection papers provide.

5. **Favorable efficiency-accuracy trade-off relative to optimization-based methods**: Figure 6 positions the method as more accurate than MoSo and Glister while being substantially faster, because selection uses SGD on learnable parameters rather than combinatorial optimization or Gram matrix inversion. This addresses a practical bottleneck that limits many optimization-based approaches at scale.

---

## Weaknesses

### Fatal
None.

### Major

1. **No baseline isolating CLIP's contribution from the proposed framework's contribution.** The comparison set includes methods (GraNd, EL2N, Forgetting, Herding, Moderate-DS, Glister, MoSo) that do not use any pretrained foundation model. Because the proposed method leverages CLIP — a model pretrained on 400M image-text pairs — a reader cannot tell whether the performance gains come from the proposed framework (adapters, SDS, multi-objective optimization) or simply from using CLIP's powerful off-the-shelf representations. A trivial baseline of "sort by direct CLIP image-text cosine similarity (no adapters, no SDS, no optimization) and take top-k" would likely already beat most non-CLIP baselines. The paper's ablation of "without dataset adaptation" (Table 5) tests raw CLIP features *within the optimization framework*, but this is not the same as a pure CLIP-similarity-sorting baseline. Without this isolation experiment, the marginal value of the proposed components is unclear. *Evidence: lines 120–130 describe baselines with no foundation model; Table 5 tests loss-term ablations but not a pure "CLIP similarity sorting" baseline.*

2. **Critical experimental details missing for reproducibility.** The paper does not specify: (a) which CLIP variant is used (e.g., ViT-B/32, ViT-L/14 — the feature dimension "typically 512" on line 111 hints at ViT-B/32 but is not explicit); (b) the training protocol for models trained on selected subsets — no optimizer, learning rate, batch size, scheduler, number of epochs, or data augmentations are reported for the main results in Figure 4, Table 1, Table 3, or Table 4; (c) standard deviations or number of random seeds for the clean-data results in Figure 4 (means±std are reported in Table 2 for noisy labels but not for the main plots). These omissions prevent independent verification of the results. *Evidence: lines 131–133 only discuss α and β hyperparameters; no training protocol is given anywhere in Section 4.*

3. **Group effect mitigation claim is broader than the mechanism supports.** The paper claims the selection optimization module "effectively addresses the group effect" (contributions point 3, line 23; also line 34, line 94). However, the loss terms L_sa and L_sd (Eq. 2–3) are simple per-sample weighted sums — each sample's gradient depends only on its own SAS and SDS, not on interactions with other samples. The only cross-sample coupling is L_s (Eq. 4), which constrains the total selection ratio. This ensures the budget is met but does not model sample complementarity or pairwise interactions. The ablation of removing L_s (line 191) shows a performance drop, but the paper attributes this to "fails to address the group effect" when the observed effect is primarily that the selection ratio constraint is no longer enforced, forcing a fallback to score sorting. The claim should be scaled back to reflect what the mechanism actually achieves: ratio-constrained multi-objective optimization, not group-effect modeling. *Evidence: Eqs. 2–4, line 191.*

### Minor

1. **Headline performance numbers from the noisy-label setting presented without clear context.** The abstract and introduction (line 21) state "our proposed method can achieve an 8.13% improvement in accuracy on CIFAR-100 and a 4.41% improvement on Tiny-ImageNet." These numbers come from the noisy-label experiments (Table 2), not the clean setting shown in Figure 4, where margins are much smaller. Detecting mislabeled samples via low image-text cosine similarity is an expected property of SAS, so these large gains are unsurprising. The paper should clearly flag that these are noisy-label results.

2. **Adapter architecture underspecified.** The adapters are described as "simple MLP" (line 41) and "simple linear layers" (line 111), but no architecture details (number of layers, hidden dimensions, activation function) are given. Since the adapters are a trained component, the architecture is needed for reproducibility.

3. **Ablation study conducted almost entirely at 90% selection ratio.** Table 5 evaluates loss-term ablations at 90% selection, where most of the data is kept and the room for differentiation is compressed. At lower ratios (10–30%), where data selection is most impactful, the differences between ablations could be substantially larger. The text-modality ablation (line 189) does use 20% and 30% ratios, but only under 20% label noise.

4. **t-SNE visualization (Figure 7) uses CIFAR-10 rather than the main datasets.** The DI improvement of 43% is reported for a single dataset without error bars. Switching to CIFAR-10 (from CIFAR-100/Tiny-ImageNet/ImageNet-1k used in all other experiments) is unexplained and weakens the evidence for the generalization claim.

5. **SDS KNN implementation not specified.** The paper states k = 10% of samples per class (line 69) and gives asymptotic complexity (line 111) but does not state whether exact or approximate KNN is used. For ImageNet-1k scale (≈1300 samples/class for k≈130), exact KNN may be nontrivial, and the actual wall-clock cost is not reported.

### Trivial

- The word "Date-efficient" in line 26 should be "Data-efficient."

---

## Nice-to-Haves

- Report results at lower selection ratios (10–30%) for the component ablations, where data selection is most impactful.
- Include a wall-clock selection-time measurement, especially for ImageNet-1k, to complement the asymptotic complexity analysis.
- Study sensitivity to the hyperparameters α and β, which are currently set by a simple rule (α = s_r, β = 2) across all datasets.

---

## Removed Points

*These points were filtered from the inputs per the review guidelines. They are retained here for transparency but should not factor into the assessment.*

- **Harsh Critic's complaint about table images not being rendered in text extraction.** This is a PDF parser artifact, not a paper problem. The paper contains the tables in its original submission.
- **Criticism about "for the first time" claim being unverifiable.** This is a stylistic framing point that does not affect the technical evaluation. Many papers use similar phrasing. Removed as a nitpick with no substantive impact on correctness.
- **"Date-efficient" typo.** Per hard rules, formatting/typo critiques are removed as parser artifacts.
- **Harsh Critic's suggestion that the paper "does not discuss the computational cost of the selection pipeline at large scale."** The paper provides an asymptotic complexity analysis (line 111). The critic's request for wall-clock cost is a nice-to-have, not a missing analysis.

---

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between the method's design and the evidence presented: the paper proposes a three-module framework yet never tests the simplest possible CLIP-based baseline (direct cosine-similarity sorting). This means the reader cannot disentangle whether the improvements stem from CLIP's pretrained representations (which are essentially free) or from the carefully-designed framework components (which are the claimed novel contribution). The noise-filtering results are impressive, but they are an almost direct consequence of SAS's design, which raises the question of what marginal value the SDS and the multi-objective optimization provide beyond what a simple CLIP-similarity threshold would achieve. The paper would be substantially stronger if it directly addressed this counterfactual.

---

## Suggestions

1. **Add the missing CLIP-similarity-sorting baseline** — i.e., compute SAS (Eq. 1 with raw CLIP, no adapters), sort descending, take top-k. Compare its performance to the full framework across selection ratios, especially 10–30%. This single experiment would either validate the framework components or reveal that most of the gain comes from CLIP itself.

2. **Specify all missing experimental details** in a dedicated reproducibility table: CLIP variant, downstream model architectures, optimizer, LR, batch size, epochs, scheduler, data augmentations, number of random seeds, and standard deviations for all main results.

3. **Tone down the "group effect" claim** to accurately describe what the selection optimization does: ratio-constrained multi-objective optimization rather than explicit interaction modeling. The L_s loss ensures budget compliance but does not model sample complementarity.

4. **Clearly label the headline numbers in the abstract/introduction** as coming from the noisy-label setting, to avoid misleading readers about the method's advantage in standard clean-data settings.

5. **Expand the ablation to lower selection ratios** (e.g., 10%, 30%) for the loss-term analysis in Table 5, where the differences between components would be more informative.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>