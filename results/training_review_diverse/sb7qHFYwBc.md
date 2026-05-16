Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me write the consolidated review.

## Summary

This paper introduces VLCL, a multimodal continual learning benchmark with eight image-caption datasets spanning diverse domains, and proposes C-CLIP, a method combining LoRA-based parameter-efficient fine-tuning with a novel Contrastive Knowledge Consolidation (CKC) loss. C-CLIP aims to learn new domain-specific image-text retrieval tasks while preserving CLIP's original zero-shot classification ability. Experiments across three evaluation tracks (downstream retrieval, zero-shot retrieval on unseen domains, and zero-shot classification) show that C-CLIP outperforms existing continual learning methods on downstream tasks while maintaining far stronger zero-shot generalization than full fine-tuning.

## Strengths

1. **CKC aligns the CLIP loss and regularization loss, breaking the traditional stability-plasticity trade-off.** Figure 3(c–d) shows that prior methods (EWC, ZSCL, Mod-X) create a loss conflict — regularization loss rises when CLIP loss falls and vice versa — whereas C-CLIP makes both losses decrease together. Figure 3(b) further shows that this alignment translates into dramatically better zero-shot preservation (~66% ImageNet accuracy after 8 tasks vs. ~25% for full fine-tuning). The ablation in Table 5 confirms that the LoRA+CKC combination is essential: either component alone underperforms the full method. This is a genuine architectural insight, not just a better hyperparameter trade-off.

2. **Comprehensive multi-benchmark evaluation covering three distinct tracks.** The paper evaluates not only downstream retrieval (8 datasets × 2 metrics = 16 numbers in Table 3) but also zero-shot retrieval on an unseen domain (HAVG) and zero-shot classification on six datasets (ImageNet, CIFAR-100, StanfordCars, Flowers, DTD, Food101), reported per-stage in Table 4. This is substantially more thorough than prior CL evaluations on vision-language models, which typically focus on only one aspect (classification or retrieval alone).

3. **The LoRA integration strategy is practical and well-motivated.** Freezing old weights and training LoRA adapters, then merging them into the backbone after each stage (Eq. 2), is a simple and parameter-efficient way to limit forgetting without storing task-specific modules. The paper shows it outperforms full fine-tuning on zero-shot preservation and is competitive with more complex regularization methods, while using far fewer trainable parameters (Table 6). The merge-at-end design avoids the inference-time task-ID requirement that plagues many architecture-based CL methods.

## Weaknesses

### Fatal
None.

### Major

1. **The "outperforms full fine-tuning" claim is imprecise and partially contradicted by the paper's own data.** The paper repeatedly states that C-CLIP "even outperforms full fine-tuning" (abstract, Figure 1, §4.2, §5.1). However, the "Full fine-tune" baseline in Table 3 is *sequential* fine-tuning on all eight tasks without any regularization — a setting where severe forgetting of early tasks is expected. C-CLIP beating that baseline on some tasks is not remarkable. Moreover, the claim appears selective: Table 3 shows that on several tasks C-CLIP is *worse* than full fine-tuning (e.g., the critic notes Pets I2T: Full fine-tune 59.94 vs. C-CLIP 58.15; T2I Pets: 54.43 vs. 52.70). The paper's text (§5.1) only highlights the winning tasks (Flickr30K, COCO). The authors need to (a) clearly distinguish between *sequential* full fine-tuning (the baseline used) and *isolated* per-task fine-tuning (the real upper bound), (b) report results against per-task fine-tuning where feasible, and (c) temper the blanket claim to something like "matches or exceeds sequential full fine-tuning on several tasks while preserving zero-shot ability."

2. **Missing standard continual learning evaluation metrics.** The paper reports only final accuracy after all eight tasks (Table 3) and per-task trajectories (Figure 5). Standard CL metrics — average incremental accuracy (averaged across tasks after each step) and forgetting measure (peak minus final per task) — are not reported numerically. Without these, it is difficult to assess whether C-CLIP maintains stable performance throughout the sequence or benefits from a favorable task ordering. Figure 5 shows trajectories for a few tasks, but numerical averages across all tasks would provide a much clearer picture. This is a methodological gap that can be fixed with additional reporting from existing data.

3. **No variance or statistical significance reported.** All results are point estimates from what appears to be a single run (§5 implementation details mention no seed or repetition). Given the small differences between methods in Table 3 (often 1–3 points), it is impossible to assess whether C-CLIP's improvements are statistically reliable. Multiple seeds (at least 3) with standard deviations are standard practice and necessary to build confidence in the comparisons.

### Minor

4. **The theoretical justification in §4.1 is not LoRA-specific.** The Lipschitz argument (Eq. 3→4) shows that constraining parameter norm change bounds feature change — which is true for *any* method with bounded parameter updates, not unique to LoRA. The paper essentially argues that LoRA's small parameter count keeps weight changes small, which is a practical observation, not a theoretical result. This section would be better framed as intuition for why parameter-efficient tuning helps CL, without claiming theoretical novelty.

5. **The projector \(h_\psi\) architecture in CKC is underspecified.** The paper introduces a projector \(h_\psi: \mathcal{Z} \to \mathcal{Z}\) (§4.2) used in Eq. 5 but does not describe whether it is a linear layer, an MLP, its hidden dimensions, or how it is optimized (end-to-end with CKC? separate training?). This hurts reproducibility. Similarly, the concatenated design of old+new features before contrastive learning (Eq. 5) is presented without justification — the paper should explain why this design is preferred over symmetric cross-modal distillation (distilling image-to-image and text-to-text separately).

6. **The prompt-tuning comparison (Table 8) is incomplete.** Only two tasks (flickr30k and COCO) are reported for L2P and CPE-CLIP, while the main evaluation uses eight tasks. The paper should show results on the full set of datasets for these methods, or remove the comparison and note the limitation. As it stands, the reader cannot assess whether the advantage generalizes.

7. **The full fine-tuning baseline may be undertuned.** The paper provides hyperparameters for C-CLIP (per-dataset learning rates, optimizer settings) but does not clarify whether the same hyperparameters were used for full fine-tuning. If full fine-tuning used the same learning rates (which are tuned for C-CLIP's LoRA-based optimization), it may underperform its potential. A small learning-rate sweep for the full fine-tuning baseline would address this concern.

### Trivial
None.

## Nice-to-Haves

- **Per-epoch training time (Table 9)** is reported but total training time and GPU memory usage would further strengthen the practical deployment claims in the appendix.
- **Ablation replacing CKC with simple feature distillation (e.g., L2)** would isolate the benefit of the contrastive formulation more cleanly than the current Table 5, which compares only LoRA vs. LoRA+CKC vs. CKC alone.
- **Hyperparameter sensitivity analysis** for LoRA rank \(r\), alpha, and temperature \(\tau\) on at least one dataset would demonstrate robustness.

## Removed Points
- *"Table 1 characterization of CIL/MTIL is unfair because ZSCL evaluates zero-shot"* — The paper's Table 1 is about evaluating **zero-shot preservation** (preserving the original pre-trained zero-shot ability), not evaluating zero-shot on new tasks. The paper's text (§2.1) correctly notes that ZSCL evaluates "zero-shot performance of new tasks," which is different. The reviewer conflated these.
- *"Zero-shot CLIP row in Table 3 is misleading"* — Including a frozen pre-trained baseline is standard practice; it establishes the lower bound for forgetting and is useful context for the reader.
- *"Three datasets (Simpsons, Lexica, Kream) are non-standard and not publicly scrutinized"* — Per policy, questioning the existence or scrutiny of cited datasets is not a valid criticism. The paper describes their splits (e.g., Kream evenly divided). Asking about preprocessing is reasonable but belongs in nice-to-haves, not weaknesses.
- *"Theoretical argument is not LoRA-specific"* — Rephrased and kept as Minor (not removed entirely) since it's a substantive point, but the critic's original framing that it "adds little insight" is too harsh — connecting PEFT to CL theory is still a contribution even if the argument is generic.

## Novel Insights

The reviews surface one insight that goes beyond the paper's own claims: C-CLIP's loss alignment (Figure 3c-d) suggests that the traditional CL trade-off between stability and plasticity is not a fundamental property of stochastic optimization but an artifact of how regularization losses interact with the task loss. Most CL methods constrain features to stay close to old representations (e.g., L2 or distillation), which directly opposes the CLIP objective's drive to learn discriminative new features. CKC instead uses the old features as positive anchors in a contrastive framework, turning the old model from a constraint into a source of additional training signal. This reframing — from "don't move too far" to "bring new representations closer to old ones for matching pairs" — is the conceptual contribution that explains why CKC avoids the loss conflict seen in prior work.

## Suggestions

1. **Qualify the "outperforms full fine-tuning" claim** to specify that the comparison is against *sequential* full fine-tuning (which suffers catastrophic forgetting), and report per-task fine-tuning as the true upper bound for the tasks where it is feasible.

2. **Add average incremental retrieval accuracy and forgetting measures** across the 8-task sequence. These can be computed from the existing data in Figure 5 and would significantly strengthen the evaluation.

3. **Run C-CLIP and at least 2–3 baselines over 3 seeds** with standard deviations reported for the main results (Tables 3 and 4).

4. **Describe the projector \(h_\psi\) architecture** (linear/MLP, dimensions, training objective) and justify the concatenated feature design in Eq. 5.

5. **Complete the prompt-tuning comparison** (Table 8) on all eight datasets, or remove it with an explicit note about computational cost.

## Score and Decision

This paper makes a solid contribution to multimodal continual learning with a well-motivated method (LoRA + CKC) and a comprehensive new benchmark. The core results — strong downstream retrieval while preserving zero-shot ability — are clearly demonstrated. The weaknesses are primarily in presentation (overclaimed "outperforms full fine-tuning"), evaluation rigor (missing CL metrics, no variance), and reproducibility (underspecified projector). None of these are fatal; all are addressable in a revision. The paper would benefit from toning down one claim and adding standard CL evaluation practices.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>