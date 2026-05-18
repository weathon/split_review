Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes "weight selection," a method to initialize a small model (student) by uniformly subsampling weights from a larger pretrained model (teacher) in the same model family. The procedure is simple — layer selection, component mapping, and uniform element selection — and adds no extra training cost. Experiments on ViT-T and ConvNeXt-F across 9 image classification datasets show consistent accuracy gains over random initialization (e.g., +43.6% on Pets, +21.9% on STL-10 for ViT-T) and reduced training time. The method is shown to be compatible with knowledge distillation.

## Strengths

- **Consistent and often large accuracy gains across diverse datasets.** Weight selection improves accuracy on all 9 evaluated datasets for both ViT-T and ConvNeXt-F (Table 1), with gains reaching double digits on smaller datasets. This directly supports the paper's core claim.
- **Substantial training-time reduction with quantification.** On CIFAR-100, ViT-T with weight selection matches the accuracy of random initialization using only 1/3 of the epochs, and is  (Figure 4a), and is 6.12× faster than pretraining + fine-tuning when matched on accuracy (Figure 4b).
- **Compatibility with knowledge distillation.** Weight selection alone outperforms vanilla logit-based distillation (75.5% vs 74.8% on ImageNet-1K), and combining both yields the best results (76.0% on ImageNet-1K, 83.9% on CIFAR-100) (Table 3). The distillation experiments properly use the same teacher for both methods, ensuring a fair comparison.
- **Principled ablation of the consistency mechanism.** The paper systematically shows that consistency across dimensions is critical: uniform, consecutive, and random-with-consistency selection all perform similarly, while removing consistency causes a sharp drop (Table 2: 81.4→77.4 for ViT-T on CIFAR-100). This provides mechanistic insight beyond raw results.
- **Comprehensive ablation of model components.** The ablation covering patch embedding, position embedding, attention, normalization, and MLP layers (Table 6) confirms that all pretrained components contribute meaningfully.

## Weaknesses

### Fatal
None.

### Major

- **Missing statistical rigor for headline results.** All main-table results (Table 1) and most analyses report single runs without variance or confidence intervals. Several improvements are small (ConvNeXt-F on ImageNet-1K: +0.3%, EuroSAT: +0.4%) — well within the range that could be explained by initialization seeds or SGD noise. For a paper whose central claim rests on quantitative accuracy gains, the absence of error bars for even the most important datasets is a significant omission. The "longer training" (+0.2% on ConvNeXt-F) and several other comparisons suffer from the same issue.

- **Missing control to isolate the selection mechanism from the pretrained data prior.** The main experiments compare weight selection (which uses an ImageNet-21K–pretrained teacher) against random initialization (no external data). While the paper partially addresses this by comparing against other methods that use the same teacher weights differently (L1 pruning, magnitude pruning, mimetic initialization), these do not fully isolate whether the improvement comes from the *specific structure* of the selected weights or merely from having any pretrained prior. A control where the teacher weights are randomly permuted before selection would directly test this. The absence of such a control weakens the paper's claim that "weight selection transfers knowledge" through the specific selection mechanism rather than through any data-derived weight distribution.

### Minor

- **Training time reduction shown only for one setting.** The training-time experiments (Figure 4) are conducted only on ViT-T + CIFAR-100. A claim of "substantial training time reduction" would be strengthened by showing similar results on at least one additional dataset or architecture.

- **Unclear whether weight selection is distinct from structured pruning as an initialization technique.** The paper's method (uniform row/column subsampling) is structurally similar to structured pruning followed by using the pruned weights as initialization — a technique already explored in Sheared LLaMA and related work on BERT subnetwork initialization. The paper compares against L1 and magnitude pruning (and finds weight selection better), but these are poorly adapted variants of pruning that break consistency. A comparison with channel-wise L1 pruning that *preserves* consistency would better establish the novelty of the approach.

- **Teacher size experiment partially undercuts the "from larger models" framing.** Table 7 shows that ViT-S (closest in size to the student) makes the best teacher, with larger teachers (ViT-B, ViT-L) yielding progressively worse results. While the paper acknowledges this and explains it as information loss from discarding more parameters, the framing of the paper as enabling initialization "from larger models" is somewhat misleading — the method works best when the teacher is only modestly larger.

- **Analysis of why uniform outperforms consecutive on ViT but not ConvNeXt is lacking.** Table 2 shows uniform (81.4) vs consecutive (81.6) for ViT-T — the paper claims "similar level of performance" but does not investigate or hypothesize about when one method might be preferable.

### Trivial
None.

## Nice-to-Haves

- A "random permutation of teacher weights" control would cleanly isolate whether the specific selected structure matters beyond having any pretrained weight distribution.
- Applying weight selection to a non-vision domain (e.g., BERT-style or LLaMA-scale models) would strengthen claims of generality.
- Visualizing the layer-wise distribution of weight norms after selection would help separate "good initialization" from "random but better-scaled."

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "Motivation overstated — small pretrained variants are available."** The paper's argument that small pretrained models are often unavailable is reasonable: ViT-T (5M params, from DeiT) was not standardly released with ImageNet-21K pretraining, and many model families (MAE, CLIP) use ViT-B as their smallest. The motivations stands.
- **Harsh Critic: "Knowledge distillation teacher dataset asymmetry in Table 3."** The paper clearly states that *the same teacher* is used for both weight selection and knowledge distillation in each comparison (ImageNet-1K teacher for both on ImageNet-1K; ImageNet-21K teacher for both on CIFAR-100). This criticism is factually incorrect.
- **Harsh Critic: "Hyperparameters adapted to baseline — may disadvantage weight selection."** If anything, tuning for random init and fixing for weight selection is a *conservative* choice that could underestimate weight selection's potential. This is not a weakness.
- **Harsh Critic: "Teacher size undermines framing."** The paper does not claim "bigger teacher is always better"; it reports the finding that closer-size teachers work best due to less information loss and still shows even ViT-L (301M) provides gains over random init for ViT-T (5M).
- **Harsh Critic: "Linear probing only shows structured features, not final accuracy."** The main results already demonstrate final accuracy gains. Linear probing is an additional analysis tool, and the criticism misinterprets its purpose.
- **Strength Finder: Generic formulations** such as "the paper conducts experiments on a wide range of datasets." These are dropped in favor of specific, evidence-backed strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel perspective or synthesis that goes beyond what the paper itself presents.

## Suggestions

1. Add error bars (mean and std over 3–5 seeds) to the main results table, especially for the smaller improvements (ConvNeXt-F on ImageNet-1K, EuroSAT).
2. Include a control experiment where teacher weights are randomly permuted before applying the selection procedure. This would directly test whether the specific selected structure matters.
3. Add a comparison with structured pruning that preserves consistency (e.g., channel-wise norm-based pruning) to better establish the method's distinction from existing pruning-for-initialization approaches.
4. Add one more dataset (e.g., CIFAR-100 or STL-10) to the training-time reduction analysis to show the finding is not dataset-specific.
5. Remove or reframe the claim about initializing "from larger models" to acknowledge that the method works best when the teacher is only moderately larger than the student.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `PdaPky8MUn` — "Never Train from Scratch" (long seq, initialization) | 8.0 | Stronger paper with cleaner experimental design and a more fundamental methodological contribution. Unlike this paper, it includes statistical rigor and isolates its mechanism cleanly. |
| `bJx4iOIOxn` — "VPT vs Full Finetuning" | 7.5 | More rigorous (error bars, multiple seeds) and addresses a clearly defined question. The paper under review has a similar scope of experiments but weaker rigor. |
| `LC6ZtQV6u2` — "Compressing Vision Foundation Models" | 6.5 | Comparable in scope and simplicity of approach, but includes broader evaluation (multiple tasks beyond classification). The paper under review has more thorough ablations of its mechanism but less task diversity. |
| `2pvMZKGYDR` — "Weight Disentanglement Merging" | 5.67 | Similar score range — has a clear core idea and reasonable experiments but methodological concerns. The paper under review is comparable in overall quality. |
| `cjpTu0Op5t` — "VISCON" (hallucination benchmark) | 4.6 | Similar in having clear experiments but limited novelty. The paper under review is somewhat better motivated but both occupy a similar tier of incremental contribution with solid execution. |
| `WM5G2NWSYC` — "Projected Subnetworks" | 2.0 | Much weaker — poorly written, unclear contributions, poor presentation. The paper under review is substantially better on clarity and experimental grounding. |

The paper presents a simple, clearly-described technique with extensive experiments across 9 datasets and solid ablations. However, the lack of statistical rigor, the partially unaddressed baseline confound, and the limited novelty (the method is structurally similar to structured pruning as initialization, already explored in related work) prevent it from being a strong contribution. The experimental coverage is a genuine strength, but the weaknesses in rigor and the incremental nature of the contribution place it in the middle of the score distribution.

**MY FINAL SCORE:** <pineapple>5.0</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>