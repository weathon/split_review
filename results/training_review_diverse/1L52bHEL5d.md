Now I have a thorough understanding of the paper and can verify each claim. Let me construct the final consolidated review.

---

## Summary

This paper proposes MiDl, a test-time adaptation method for handling missing modalities in egocentric video recognition without retraining. The method minimizes mutual information between the model's predictions and the available modality to encourage modality-invariant representations, combined with a self-distillation (KL) term to preserve performance on complete-modality inputs. MiDl operates online, adapting only when complete-modality samples arrive, and is architecture-agnostic. Experiments on EPIC-Kitchens, EPIC-Sounds, and Ego4D show consistent gains over non-adapted baselines across missing rates ranging from 25% to 100%.

## Strengths

- **Novel formulation of missing modality as a test-time adaptation problem.** The paper is the first to explicitly frame missing modality handling as an online TTA problem (Section 3), enabling model adjustment without retraining. This contrasts with prior work (e.g., Ramazanova et al., 2024; Lee et al., 2023) that requires retraining the full model on the training set.

- **Consistent and significant performance gains across multiple settings.** MiDl improves the non-adapted baseline by up to 7% on EPIC-Kitchens and 1.7% on EPIC-Sounds under the standard TTA scenario (Table 1), with larger gains under long-term adaptation (up to 11.9% on EPIC-Kitchens at 100% missing rate, Table 2). These gains hold across multiple missing rates and datasets.

- **Agnostic to architecture, missing modality type, and pretraining strategy.** The paper demonstrates MiDl's generality across MBT (Table 1), vanilla self-attention (Table 3, Section 6.1), Omnivore pretraining (Table 5, Section 6.3), different missing modalities (Table 4, Section 6.2), and mixed-modality setups (Table 9). This breadth of validation supports the claim that MiDl is a general-purpose solution rather than a dataset-specific trick.

- **Ablation confirms both components are necessary.** Table 6 shows that using only the KL term yields no adaptation, while using only the MI term degrades performance at low missing rates. The full MiDl (MI+KL) provides consistent gains across all missing rates, validating the design rationale that mutual information minimization drives invariance while self-distillation preserves original multimodal performance.

- **Practical adaptability demonstrated via warm-up on out-of-domain data.** Section 5.4 shows that warming up MiDl on unlabeled Ego4D data (out-of-domain) further improves accuracy on EPIC-Kitchens by 8% at 100% missing rate, demonstrating the method's versatility in data-scarce deployment scenarios.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The Long-Term Adaptation (LTA) setup uses training data, creating a tension with the "no retraining" narrative.** Section 5.3 lets $S_{\mathrm{in}}$ be "a subset of training data" used for adaptation before evaluation on the validation set. While the method itself does not use labels and is distinct from full retraining, accessing training data at test time deviates from a standard TTA scenario. The paper should more clearly disambiguate this setting from the pure TTA scenario (Section 5.2) and acknowledge that LTA assumes access to unlabeled in-domain data that may not always be available at deployment.

- **Only two TTA baselines (SHOT, ETA) are compared in the main experiments.** The paper mentions "three off-the-shelf TTA methods" (Table 1 caption) but names only two in the text. Standard TTA baselines such as TENT (Wang et al., 2020) and simple BN-statistics adaptation (Li et al., 2016) are absent. While MiDl convincingly outperforms the baselines included, a broader comparison would strengthen the claim that existing TTA methods are ineffective for this domain shift.

- **The claimed 2× latency advantage assumes sufficient GPU memory for parallel forward passes.** Section 6.5 states that "the latency of MiDl is only 2× slower than the non-adapted model since all the additional 4 forward passes can be performed in parallel." This assumes perfect parallelism without memory constraints. In practice, running multiple forward passes simultaneously on a single GPU may be memory-bound, especially for transformer architectures like MBT. Reporting actual wall-clock times and memory usage would make this claim more credible.

- **The paper says "three off-the-shelf TTA methods" (Table 1 caption) but only names SHOT and ETA in the main text.** If a third method exists, it needs to be named. If the third is simply the non-adapted baseline, the phrasing is misleading.

### Trivial
None.

## Nice-to-Haves

- **Reporting results on a broader egocentric dataset** such as Ego4D's own audio-visual action recognition subset (rather than using it only for warm-up) would strengthen claims of generality beyond the EPIC-Kitchens/EPIC-Sounds recording protocol.

- **A plot of performance vs. fraction of complete-modality samples ($p_{AV}$)** would directly address the practical viability of MiDl when complete samples are rarer (e.g., $p_{AV} < 0.25$), as real-world streams may have very few complete-modality instances.

- **An ablation freezing different parts of the network** (front-end encoders vs. fusion layers) would deepen the analysis of what MiDl actually learns to change, supporting the claim that it creates modality invariance rather than just regularized fine-tuning.

## Removed Points

These points are flagged to be removed by the meta-review process; treat them with caution.

- **"Missing variance/error bars in main tables"** — The paper explicitly states in the Table 1 caption: "Refer to Table 11 to see the standard deviations." Standard deviations exist in the appendix (which is part of the original submission but stripped by the parser). This is not a missing-results issue but a presentation choice.

- **"Problem formulation inconsistency in P={0.25, 0.0, 0.75} example"** — The example is correct: 25% missing video means 25% audio-only samples ($p_A=0.25$), 0% video-only ($p_V=0.0$), 75% both ($p_{AV}=0.75$). The reviewer misread $p_A$ as the audio-only rate and conflated it with missing video.

- **"Under incomplete modality L_ent = L_div claim is misleading"** — The paper uses this equality as the explicit justification for why adaptation is only performed on complete-modality samples. The reasoning is correct and clearly stated.

- **"Undisclosed hyperparameters (learning rate, optimizer, etc.)"** — Typical reproducibility nitpick about implementation details. The learning rate $\gamma$ is defined in the update equation; specific values and optimizer details are standard in-the-appendix content.

- **"Baseline fairness / hyperparameter configuration for SHOT and ETA"** — Referenced to Section B.1 in the appendix (stripped by parser). The original submission contains these details.

- **"Does not discuss what happens when p_AV → 0"** — The paper explicitly addresses this on line 77: "Since this work focuses on the multimodal setting, we assume that $p_{AV} \neq 0$ ... Nevertheless, to demonstrate that MiDl does not degrade the original multimodal model's performance in this extreme case, we also report results with $p_{AV} = 0$."

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Rename or more clearly separate the LTA experiment from the pure TTA scenario (Section 5.2 vs. Section 5.3), and explicitly note in the LTA section that it assumes access to unlabeled in-domain data from a related source, which may not always be available.
- Add standard TTA baselines (TENT, BN-adaptation) to the comparison table to strengthen the claim that existing methods are inadequate for this domain shift.
- Report actual wall-clock times and peak GPU memory usage alongside the theoretical compute analysis in Section 6.5.
- Add a plot showing MiDl's performance gain as a function of $p_{AV}$ to help readers understand how the method behaves when complete-modality samples are rare.

## Score and Decision

The paper introduces a novel and principled framing of missing modality handling as a test-time adaptation problem, supported by a well-motivated method (MiDl) and comprehensive experiments across multiple datasets, architectures, pretraining strategies, and missing rates. The core contribution is valuable and the evidence is largely convincing. The weaknesses are minor and addressable — none threaten the central claims.

**Originality**: Strong — first to formulate missing modality as a TTA problem.  
**Importance**: High — missing modalities are a practical bottleneck in real-world multimodal deployment.  
**Claims supported**: Yes, with minor caveats around the LTA setup and baseline breadth.  
**Soundness**: Good, though the baselines could be broader.  
**Clarity**: Clear overall; the method and protocol are well described.  
**Value**: Good contribution to the multimodal and TTA communities.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>