## Summary

This paper proposes a paradigm shift for LLM watermarking: instead of applying token-level perturbations at inference time on a fixed model (the existing paradigm), it embeds a detectable signal into the LLM's weights via RL-based co-training of the LLM and a paired neural detector. The approach uses PPO to fine-tune the LLM to maximize scores from the detector, while the detector is simultaneously trained to distinguish the fine-tuned model's outputs from non-watermarked text. Empirical results show near-perfect detection AUC (often >0.99) and the ability to incorporate adversarial training for robustness against paraphrasing and substitution attacks.

## Strengths

- **Near-perfect detection accuracy across diverse settings**: Table 1 shows AUC of 0.9985–0.9997 for the proposed method, substantially outperforming KGW (0.79–0.97), ITS (0.82–0.998), and EXP (0.32–0.98) on both C4 and PKU tasks with both OPT-1.3B and Llama2-7B. The gap is especially large on the PKU alignment task (e.g., OPT-1.3B: 0.9997 vs. ITS's 0.8208), which directly supports the core claim.

- **Demonstrated adaptability to new attacks via adversarial training**: Section 5.3 and Figure 5 show that adversarial training on Pegasus-paraphrased responses generalizes to DIPPER-paraphrased responses (a different paraphraser not seen during training). This is a genuine capability that fixed-model inference-time methods fundamentally cannot provide.

- **Robustness to extreme token substitution when adversarially trained**: Section 5.2 reports that after incorporating adversarial examples, the method achieves "almost no AUC loss even when substituting 50% of tokens." The adversarial training loop is a structural advantage of the framework, not a cherry-picked result.

- **Zero additional generation cost at inference**: Once the model is fine-tuned, generation requires no special post-hoc operations — the watermark emerges naturally from the weights. This is a genuine practical advantage over KGW/ITS/EXP, which modify the sampling procedure at every generation step.

- **Addresses the open-source feasibility problem**: Because the watermark is in the weights rather than applied post-hoc, practitioners can release the fine-tuned model without revealing an unwatermarked version — a concrete structural advantage over inference-time methods.

## Weaknesses

### Major

- **The detector learns a distributional signature, not an independently verifiable signal**: The method fine-tunes the LLM to maximize detector scores, and the detector learns to recognize whichever distributional shift emerges from PPO training. Unlike KGW or ITS — where anyone given the secret key can independently verify the watermark — this method requires the *specific trained detector* for verification. If the detector is not released, no external party can verify. If it is released, adversaries can train evasion models against it. This is not a framing dispute but a practical limitation that the current framing obscures. The paper should reframe the contribution more precisely and discuss this trade-off transparently.

- **Performance collapses under non-watermarked distribution shift without retraining**: Table 2 shows that when the method is trained on human-written non-watermarked text (H variant) but tested against another LLM's text, AUC drops sharply for OPT-1.3B on C4 (0.9985 → 0.9053). Including the target LLM's text in training (H+L) restores performance, but this requires knowing the test-time non-watermarked distribution at training time. This is not a "minor out-of-distribution problem" (line 272) — it reveals that the detector is distinguishing the fine-tuned model's distribution from the *training* non-watermarked distribution, not detecting a deliberately embedded mark that generalizes across any non-watermarked source.

- **Comparison with inference-time baselines is not properly controlled for different resource regimes**: The proposed method uses expensive PPO fine-tuning of the full LLM plus training a secondary LM as a detector. The baselines (KGW, ITS, EXP) are applied to a fixed, pre-trained model with zero fine-tuning. The paper acknowledges the resource difference in limitations (lines 37–38, 347) but then treats Table 1 as a fair head-to-head comparison. On the PKU task specifically, baselines are applied to an already-aligned model (line 219), while the proposed method performs alignment and watermarking *simultaneously* (α=0.5). These are structurally different evaluation setups that the paper does not adequately disentangle. A fair evaluation would either (a) give baselines the same fine-tuning budget or (b) clearly separate "fair comparison" results from "capability demonstration" results.

### Minor

- **No analysis of training dynamics or convergence**: The co-training alternates between PPO (LLM maximizes detector scores) and detector training (detector distinguishes LLM outputs). This is a minimax game, but the paper provides no convergence analysis, no plots of detector AUC or LLM policy entropy over training steps, and no discussion of when to stop training. The No-FT ablation is nearly tautological — of course fine-tuning the LLM to maximize detector scores makes the detector's job easier. The interesting question (what features does the detector exploit? does the co-training converge or oscillate?) is not addressed.

- **No confidence intervals or variance estimates**: All results are reported as point estimates from 1K prompts. For AUC values clustered near 1.0 (e.g., 0.9985 vs. 0.9976), error bars are essential to know whether observed differences are significant. This is standard practice in machine learning evaluation.

- **The substitution attack (random token replacement) produces obviously corrupted text** (line 245). A meaningful adversarial evaluation would use synonym-based or embedding-space substitutions that preserve fluency while changing surface form. The current attack is not representative of realistic adversaries.

- **Detector architecture is underspecified**: The detector is said to have "the same architecture as an RM" (line 75), but the RM architecture itself is not described. Whether the detector is the same size as the LLM or much smaller dramatically affects the cost analysis and the method's practicality. Similarly, key PPO hyperparameters (learning rate, clipping parameter, number of PPO epochs per step) are omitted.

- **Table caption overclaims**: The caption of Table 1 states results are "at the same level of utility." However, ITS and EXP show substantially *worse* logPPL than the proposed method on C4 (e.g., OPT-1.3B: 3.13–3.16 vs. 2.42). The paper acknowledges this in the text (line 226) but the caption remains misleading.

### Trivial

- None beyond the minor issues above.

## Nice-to-Haves

- A feature attribution or probing analysis to understand what makes watermarked text distinguishable (e.g., n-gram statistics, perplexity, topic distributions) would strengthen the paper's claims about "semantic-level" watermarking, which is currently asserted without evidence.
- An analysis of how the watermark degrades under fine-tuning (e.g., if an adversary takes the released watermarked model and fine-tunes it further) would address an important practical question raised by the open-source feasibility claim.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The method is not a watermark" terminology argument**: The critic argues the method should not be called a watermark. The paper is transparent about what it does and positions itself as expanding the watermark design space. Reasonable readers can disagree on terminology, but this is not a substantive weakness about the method itself. The *practical consequences* of this design choice (verification requiring the specific detector, distribution-shift sensitivity) are kept as major weaknesses above.

- **"PKU: baselines get no alignment"**: The critic states that baselines "get none" on PKU. This is factually incorrect — line 219 states baselines are applied to "the aligned model after performing RLHF on the PKU dataset." The comparison is between aligned→watermark (baselines) vs. simultaneous align+watermark (Ours), which is a different concern and is retained above in weakened form.

- **"Adversarial training comparisons are head-to-head wins"**: The paper explicitly acknowledges (line 246) that ITS and EXP outperform the non-adversarially-trained version. The adversarial advantage is presented as a capability of the framework, not as a concealed head-to-head win. This is retained above as a properly scoped note within the resource-regime fairness concern.

- **"Zero generation cost is misleading"**: The critic claims this is misleading because of one-time training cost. The paper explicitly acknowledges the one-time cost as a limitation (lines 37–38, 347). The claim is specifically about generation cost at deployment time, which is accurate. This is not a weakness.

- **"Open-source feasibility" concern about adversary fine-tuning**: The critic raises a speculative scenario (an adversary fine-tuning the released model to remove the watermark). The paper's claim is specifically about not needing to release an unwatermarked version alongside — this is a valid structural advantage. The speculative fine-tuning attack is a reasonable future concern but not a present weakness of the paper.

- **"What prevents the LLM from collapsing to a trivial policy?" and similar speculative criticisms**: These are general concerns raised without evidence from the paper. The paper reports strong empirical results showing no such collapse occurred.

## Novel Insights

Beyond the paper's own contributions, the most informative finding is the sharp asymmetry revealed in Table 2: when the non-watermarked distribution shifts from human-written text to another LLM's text, the (H) variant's detection AUC drops dramatically for OPT-1.3B on C4 (0.9985 → 0.9053) but remains nearly unchanged for Llama2-7B on PKU (0.9997 → 0.9997). This asymmetry suggests that the detector's reliance on distributional features is model- and task-dependent, and that the method's generalization to unseen non-watermarked distributions is uneven — a property that deserves deeper analysis. The finding that adding the target LLM's text to training restores performance (H+L variant) confirms that the detector is fundamentally a *discriminator* between two text distributions, not a detector of a pre-defined signal.

## Suggestions

1. **Reframe the contribution precisely.** Drop or qualify "watermark" in the abstract and introduction to avoid setting up expectations the method cannot meet. Position the work as *trainable model attribution via RL co-training* or similar. The practical differences from token-level watermarks (verification requires the specific detector, distribution-shift sensitivity) should be discussed prominently, not relegated to an afterthought.

2. **Disentangle the evaluation.** Separate results into (a) a controlled comparison where all methods use the same base model with no additional training, and (b) a capability demonstration showing what extra performance the fine-tuning budget buys. For the PKU alignment task, compare against baselines applied to a model that has received identical alignment training.

3. **Add training dynamics analysis.** Plot detector AUC, LLM policy entropy, and generation diversity over PPO steps. Show that the co-training converges rather than oscillates. This is essential for establishing the method's practical reliability.

4. **Report confidence intervals.** For 1K-prompt evaluations, provide bootstrap or binomial confidence intervals on AUC and FPR metrics. The small marginal differences between methods near 0.99 AUC are meaningless without them.

5. **Specify the detector architecture and cost.** State the detector's parameter count relative to the watermarked LLM, and report per-generation FLOPs or wall-clock time for detection vs. the statistical tests used by baselines.

## Score and Decision

**Score**: 6.0

**Decision**: Accept

The paper introduces a genuinely novel idea — expanding the LLM watermark design space from inference-time token manipulation to model-level co-training — and backs it with strong empirical results showing near-perfect detection, adversarial adaptability, and practical advantages. The weaknesses are real but addressable: the comparison with inference-time baselines confounds resource regime with method quality, the detector is a distribution discriminator rather than a verifiable signal detector (with measurable consequences in Table 2), and several empirical analyses are missing. These issues do not invalidate the core contribution but require a reframing of the claims and a more carefully controlled evaluation. With appropriate revision, this work would make a meaningful contribution to the LLM attribution literature.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>