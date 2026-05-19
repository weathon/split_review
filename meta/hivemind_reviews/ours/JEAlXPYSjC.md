## Summary
This paper makes a simple but practically relevant empirical observation: CLIP models trained on small datasets (e.g., CC12M) can be significantly improved by resetting the learning rate scheduler and training for just a few additional epochs. A ResNet-50 CLIP model goes from 31% to 41.7% ImageNet zero-shot accuracy (+10.7 points) with only 10 extra epochs and negligible computational overhead. The paper further shows that (a) improvement saturates after ~3 additional epochs, (b) applying the reset early in training can shorten total training time, (c) a cyclic LR schedule from the start also helps, and (d) the phenomenon is less pronounced for large-scale models.

## Strengths
- **Large, clean accuracy gain from a trivial procedure.** The central result — a +10.7 point jump on ImageNet zero-shot (31% → 41.7%) for a ResNet-50 on CC12M (Table 2, Figure 1) — is convincingly large, and the method is trivially simple: reset the LR and train a few more epochs. This is genuinely useful for any practitioner training CLIP on small data.

- **Consistent across architectures and tasks.** The improvement is demonstrated on ResNet-50, ViT-B-32, and ViT-B-16 (Figure 3, Table 2), and evaluated across multiple downstream tasks including ImageNet variants. This rules out architecture-specific artifacts.

- **Minimal overhead.** Performance saturates after only ~3 additional epochs (Figure 3), meaning the total extra compute is negligible relative to the original 75-epoch training. The paper provides a clear, actionable heuristic.

- **Negative result on large-scale data strengthens the small-data claim.** Applying the same procedure to ViT-B-32 on LAION-400M yields no improvement (Table 6). This negative result, while limited, adds specificity to the paper's scope: the finding is most relevant for small-data CLIP practitioners.

- **Insight connecting to cyclic LR schedules.** Section 3.4 shows that a multicycle cosine scheduler from the start outperforms the single-cycle default (Figure 5), linking the reset phenomenon to established scheduler design and providing mechanistic grounding.

## Weaknesses
### Major

- **The "undertraining" framing is misleading.** The paper's central narrative is that CLIP models on small datasets are "undertrained" (title, abstract, Section 3.1). But Figure 4 directly undermines this framing: applying the reset at epoch 10 (20 total epochs) achieves 37% accuracy, surpassing the 75-epoch model's 31%. A model that reaches higher accuracy in fewer total steps with a different schedule was not "undertrained" in the sense of needing more training — it was trained with a suboptimal schedule (single-cycle cosine). The paper itself acknowledges in Section 3.4 that a cyclic LR helps from the start. The observation is real and valuable, but the framing overstates the interpretation. The contribution would be more accurately scoped as "the single-cycle cosine schedule is suboptimal for small-scale CLIP; use a cyclic LR or a simple reset."

- **Missing experimental details prevent reproducibility assessment.** The paper does not report: specific learning rate values, optimizer choice, batch size, warmup schedule, weight decay, data augmentations, prompt templates used for zero-shot evaluation, number of random seeds, or variance across runs. For an empirical paper whose quantitative claims are the entire contribution, this is a significant gap. The paper is very short (~125 lines of text) and does not reference an appendix where such details could reside. Without this information, readers cannot distinguish a robust finding from a lucky hyperparameter configuration.

### Minor

- **The large-scale experiment is too thin to support a general conclusion.** Section 3.5 tests one model (ViT-B-32 on LAION-400M) for 15 extra epochs, finds no improvement, and concludes "undertraining is less of an issue at scale." This is a single data point. The negative result could reflect insufficient extra epochs, a model already trained with a better schedule, or architecture-specific behavior. The paper does hedge ("suggesting," "less of an issue"), but the claim is broader than the evidence supports.

- **Comparison table (Table 7) would benefit from controlled re-implementations.** The paper compares its reset procedure against published numbers of methods like SLIP, CLIP+clustering, etc. The comparison is valid (this approach achieves competitive results without modifying the objective), but it conflates training setup differences. The paper does not specify whether the comparison methods were re-implemented under a shared training budget or simply cited from their original papers. A cleaner test would apply the same reset to those methods and report both before/after.

- **No variance or seed information.** All experiments appear to be single runs. Given that small-dataset CLIP training can be sensitive to initialization and data ordering, the reported improvements cannot be assessed for statistical significance.

### Trivial

- The paper mentions it validates on CC3M and CC12M but the main experiments appear to focus on CC12M. The role of CC3M in the experiments is not clearly delineated.

## Suggestions
1. **Reframe the contribution.** The core finding is that the single-cycle cosine schedule is suboptimal for small-scale CLIP, and that a simple LR reset (or cyclic schedule) yields substantial gains. A title like "A Simple Learning Rate Reset Improves Small-Scale CLIP Training" would be more accurate and avoid the overclaim embedded in "Your CLIP Model Might Be Undertrained."

2. **Add the missing hyperparameter details.** Report learning rate, optimizer, batch size, weight decay, augmentations, prompt templates, and evaluation protocol in a single table. This is essential for reproducibility.

3. **Report variance.** Run experiments with at least 3 seeds and report mean ± std. Without this, readers cannot assess the reliability of the reported improvements.

4. **Add the constant-LR continuation control.** Show what happens when training continues from the plateau point with a constant LR (at its final value) to isolate the reset as the causal mechanism.

5. **Soften the large-scale claim** or run additional experiments (different architectures, larger models, longer extra training) before drawing a general conclusion about large-scale training.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
