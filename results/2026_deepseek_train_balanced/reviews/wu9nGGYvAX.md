## Summary

This paper systematically investigates whether standard deep neural network architectures (ResNet-50, ViT-B/16) can learn and generalize a same-different visual relation across in-distribution and out-of-distribution (OOD) stimuli. The authors conduct a 2 (architecture) × 3 (pretraining: random, ImageNet, CLIP) × 4 (fine-tuning dataset) experiment with 5 seeds per condition. They find that CLIP-pretrained ViT-B/16 fine-tuned on abstract shape-only stimuli (Squiggles) achieves near-perfect OOD generalization (≥96.7%) across three held-out datasets, directly contradicting prior claims that standard architectures cannot learn this relation. The paper also causally dissects inductive biases, showing that CLIP pretraining shifts models from color/texture reliance toward shape-based comparison.

## Strengths

- **Near-perfect OOD generalization of CLIP ViT fine-tuned on Squiggles overturns prior negative results.** Table 1 (lines 97–98) shows CLIP ViT-B/16 fine-tuned on Squiggles achieves 97.7%, 99.1%, and 96.7% median test accuracy on three OOD datasets (ALPH, SHA, NAT) — a 97.8% average OOD score. This directly contradicts the conclusion of Puebla & Firestone (2022) that current networks cannot learn generalizable same-different relations.

- **Systematic 2×3×4 factorial design isolates the specific factors enabling success.** The paper evaluates two architectures × three pretraining regimes × four datasets with 5 seeds each (Section 2.2, Table 1, Figure 2). This comprehensive matrix allows attribution of OOD success to the specific combination of CLIP + ViT + abstract-shape fine-tuning, a level of ablation absent in prior single-condition studies.

- **Clever causal dissection of inductive biases via conflict stimuli.** Section 4.2 (lines 149–154) uses stimuli where color, texture, and shape send conflicting signals. Randomly-initialized ViT classifies 85.6% of same-color-only stimuli as "same," while CLIP ViT classifies only 12.3% as "same" — direct evidence that CLIP pretraining shifts reliance from color to shape, the feature dimension enabling OOD generalization.

- **Explicit replication and reconciliation with prior contradictory findings.** The paper reproduces the chance-level result of Kim et al. (2018) for random-initialized ResNet-50, the high in-distribution accuracy of Funke et al. (2021) for ImageNet-pretrained ResNet-50, and the failure pattern of Puebla & Firestone (2022) — then cleanly shows CLIP ViT succeeds where those prior models failed (Section 5, line 163).

## Weaknesses

### Major

- **OOD results are only reported for CLIP-pretrained models, omitting the crucial ImageNet comparison.** Table 1 reports OOD generalization exclusively for CLIP models. Figure 1 shows in-distribution results for all three pretraining conditions, but the parallel OOD data for ImageNet-pretrained models is absent. The paper argues CLIP is key to OOD success, but we never see the systematic OOD performance of ImageNet-pretrained ViT or ResNet models. The brief mention that "ImageNet ResNet-50 model fine-tuned on Squiggles also struggles to generalize" (line 163) is a qualitative note in the Related Work section, not a systematic comparison. If ImageNet-pretrained ViT also generalized well OOD, the CLIP-specific narrative would need revision; if it did not, the result would be stronger. Either outcome would strengthen the paper. This is a verifiable gap in the evidence chain.

- **The asymmetric OOD generalization (especially ALPH→SQU) tempers the "abstract concept of equality" framing.** CLIP ViT fine-tuned on Squiggles generalizes to all datasets at ~97–99%. But the same architecture fine-tuned on Alphanumeric (also abstract shapes) gets only 55.3% on Squiggles — essentially chance. If the model learned a genuinely abstract concept of equality, why would it categorically fail to apply it to Squiggles after training on another abstract-shape dataset? This asymmetry is noted but not explained beyond a correlation with embedding "closeness" (Table 3). The paper's conclusion that models "acquire a genuinely abstract concept of equality" (line 29) is broader than what this asymmetry supports. The paper would be stronger with a more precise claim about what kind of abstraction was learned and under what conditions.

- **The "noise" training dataset used as a control in the cosine similarity analysis is never defined.** Line 119 states "models fine-tuned on noise exhibit weaker OOD generalization than models fine-tuned on Squiggles" as a counterexample to the embedding-closeness correlation, and Table 3 (line 108) lists "noise" as a dataset. But the paper never describes how noise stimuli were constructed, what objects they contain, or whether they follow the same same-different structure. This gap affects both reproducibility and interpretability of an analysis that is meant to rule out a trivial explanation.

### Minor

- **Hyperparameter selection based on in-distribution validation accuracy** (line 64) while the central claim is about OOD generalization. A grid search that optimizes for in-distribution performance could systematically discard configurations that would generalize better OOD. This is a reasonable concern but not a fatal one — the reported OOD results are strong enough that different hyperparameters are unlikely to *create* this effect from nothing. A robustness check showing OOD results across the top-3 configurations would address this.

- **No statistical tests or confidence intervals for the OOD comparisons.** With only 5 seeds per condition, reporting the range or individual seed values (as done for the bimodal case in line 88) would help readers assess reliability. The individual points in Figure 1 are informative; a similar presentation for OOD results would strengthen Table 1.

### Trivial

- None.

## Nice-to-Haves

- The "noise" dataset should either be described (what are the stimuli? how are same/different defined? what was the training procedure?) or its mention should be removed as it is not essential to the main claims.
- A rank correlation coefficient for the asserted relationship between embedding closeness and OOD generalization would be more informative than the qualitative "seems to be a correlation" claim (line 118).
- Explicitly confirm that 70 epochs is sufficient for convergence across all model types (briefly noted for ViTs; a convergence curve or check for ResNets would help).

## Removed Points

*These points are flagged for removal; treat with caution.*

- **Harsh Critic Point 5 (Task structure confound):** Critic argued that SHA/NAT's multi-dimensional "different" definition (differing on shape, texture, and color simultaneously) could confound OOD results. **Removed because** the paper already addresses this mechanism directly: Section 4's inductive bias experiments show models trained on color/texture-rich datasets rely on those features, which is precisely why Squiggles training (lacking color/texture) forces shape comparison and transfers better. This is not a confound the paper missed but a mechanism the paper discovered and demonstrated.
- **Strength Finder's unverifiably broad framing:** Removed some generic praise language in line with filtering rules. The remaining strengths are specific and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions. The most interesting finding surfaced across the reviews is the bilateral asymmetry in OOD generalization: the fact that SQU→everywhere works near-perfectly while ALPH→SQU fails at 55.3%. Neither reviewer fully unpacked why this asymmetry arises given that both SQU and ALPH are abstract shape-only datasets. The paper's embedding-closeness correlation (Table 3) offers a partial explanation (SQU embeddings are closer together than ALPH embeddings, so ALPH-trained models see less similar stimuli during training), but the connection between embedding-closeness and trainability is not theoretically grounded. An alternative hypothesis that neither reviewer raised: perhaps the composition of "different" pairs in SQU (which can include two shapes that look quite similar, since only pixel-level identity is required for sameness) makes the SQU task genuinely harder as a target domain, while as a source domain it forces more discriminative feature learning. This remains an open question for future work.

## Suggestions

1. **Report OOD performance for ImageNet-pretrained models in Table 1 (or a companion table).** These models are already trained; computing OOD accuracy on the four datasets is a forward pass. This single addition would substantially clarify the paper's central attribution claim.
2. **Address the ALPH→SQU asymmetry head-on.** Either explain the failure mechanistically or qualify the "abstract concept of equality" claim to reflect the observed generalization boundaries.
3. **Define the noise dataset or remove the reference.** Under-specifying a control condition weakens the analysis it supports.
4. **Add a robustness check showing OOD results across the top-3 hyperparameter configurations** for the key condition (CLIP ViT + Squiggles).

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>