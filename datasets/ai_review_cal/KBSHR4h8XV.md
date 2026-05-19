- Decision: Reject
- Avg Score: 3.33
- Scores: 6, 3, 1
Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the consolidated review.

## Summary

EF-VLA proposes a Vision-Language-Action architecture that performs early fusion of vision and language features using frozen CLIP (with ClearCLIP attention features), before passing them to a small transformer policy network. This contrasts with existing VLA models that use late fusion (passing disjoint vision and language tokens into the policy). The core idea is to preserve CLIP's pre-trained vision-language alignment by keeping it frozen, avoiding the generalization degradation caused by fine-tuning. Experiments in simulation (LIBERO) and on a real Franka robot show consistent gains over late-fusion baselines including LF-VLA (the paper's controlled ablation), Octo, and OpenVLA, particularly on unseen tasks.

## Strengths

- **Controlled ablation cleanly isolates the benefit of early fusion.** The comparison between EF-VLA and LF-VLA holds fixed the CLIP backbone, training data, and policy architecture, differing only in when vision-language fusion occurs. On unseen real-world tasks, EF-VLA achieves 68% vs. LF-VLA's 25% (Table 2). This is the paper's most persuasive evidence because it controls for confounding factors like model size and pre-training data.

- **Freezing the VLM is empirically shown to be critical.** Section 4.6 reports that fine-tuning the CLIP encoder collapses success rates from 68%→26% on training tasks and 62%→15% on unseen tasks, with supporting attention visualizations (Figure 6). This result directly supports the paper's core design thesis and is quantified with concrete numbers.

- **Parameter-free fusion design is clean and well-motivated.** The fusion in Equation (2) uses only a temperature-weighted softmax over frozen CLIP features with no learned fusion parameters. This design choice directly preserves CLIP's vision-language alignment without requiring additional training, as supported by the attention visualizations.

- **Evaluation includes distractor objects and randomized scenes** (Section 4.1), making the generalization claim credible. The real-robot setup uses 2 random distractor objects per trial and varies object poses, testing instruction-following under realistic conditions.

- **Scaling law is demonstrated.** Figure 5 shows consistent improvement as the CLIP backbone scales (ViT-B/32 → ViT-B/16 → ViT-L/14), confirming that EF-VLA effectively leverages stronger pre-trained models.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Simulation results (Table 1) lack variance estimates.** The LIBERO experiments report success rates over 300/100 trials but provide no standard errors, confidence intervals, or other measures of variance. The real-world experiments include standard errors (Table 2, Figure 1), so this omission is conspicuous. Without variance estimates, the reader cannot assess whether differences like EF-VLA 93.3% vs. LF-VLA 91.7% on LIBERO-Spatial are meaningful. This is easily fixable.

- **Multi-primitive experiments (Table 3) use small sample sizes.** Each condition is evaluated on 10 trials, where a single failure changes the reported rate by 10 percentage points. While the 150-trial aggregate provides some stability, the per-primitive granularity is unreliable. The paper's claim that EF-VLA "can achieve high success rate on all four primitives" would be strengthened by larger sample sizes.

- **LF-VLA's vision features are underspecified.** The paper describes LF-VLA as using "vision tokens" from CLIP passed through separate attention pooling (Section 4.2), but does not specify whether LF-VLA uses the attention output $X_{\text{attn}}$ or the final CLIP output $X_{\text{out}}$. If LF-VLA uses a different CLIP representation than EF-VLA, the ablation does not isolate early fusion alone. This should be clarified for reproducibility.

- **Baseline comparison fairness could be more thoroughly documented.** For the main pick-and-place experiments (Table 2), the paper states that Octo and OpenVLA were fine-tuned with "the same amount of learning steps" but does not discuss whether context lengths, action prediction horizons, or learning rates were tuned for each baseline. The context-length issue is addressed for the multi-primitive experiment (Section 4.5: Octo extended to its maximum of 10, OpenVLA uses default), but similar details are absent for the primary comparison. The LF-VLA ablation largely mitigates this concern since it is the cleaner comparison, but the paper would be more convincing with explicit documentation of how baseline hyperparameters were selected.

- **Freeze-vs-finetune ablation is buried.** The critical result that fine-tuning CLIP destroys generalization (68%→26% training, 62%→15% unseen) appears only as a single sentence in Section 4.6 rather than as a dedicated table with full experimental detail. Given that this directly validates the paper's central design claim, it deserves more prominent placement.

### Trivial

- The phrase "zero-shot manner" in the contributions (point 2) could be read as implying the entire policy is zero-shot, though the paper clarifies this means "without the need to finetune vision encoders." Consider rephrasing to "zero-shot generalization to unseen tasks without fine-tuning the vision encoder" for precision.

## Nice-to-Haves

- Provide a per-task breakdown of success rates for the LF-VLA vs. EF-VLA comparison to illuminate *why* early fusion helps (e.g., object localization, instruction-following under distractors).
- Add bootstrapped confidence intervals or permutation tests for the key pairwise comparisons (EF-VLA vs. LF-VLA on unseen tasks) to preempt statistical criticism.
- Discuss whether EF-VLA's performance is sensitive to the number of cameras or the quality of the text encoder, as these are relevant for practitioners.

## Removed Points

The following points from the input reviews are excluded:

- **"Zero-shot phrasing is misleading"** — The paper states "EF-VLA can perform unseen tasks in a zero-shot manner without the need to finetune vision encoders" (Contributions, Section 1). The qualifier "without the need to finetune vision encoders" makes the scope clear. The paper also independently defines "zero-shot generalization" in Section 4 as standard in robot learning: "the policy is provided with a language description of an unseen task." This criticism misreads the paper's precise language.

- **"Missing RT-1 baseline"** — The paper discusses RT-1 in Related Work (Section 2.2) and explains that RT-1 "need[s] to learn the language-vision alignment from task data, thus cannot leverage pre-trained models such as CLIP." The critic acknowledges RT-1 cannot be fine-tuned on the small DS-PnP dataset. This is not a genuine weakness.

- **"Hyperparameter search for baselines"** — The paper states "same amount of learning steps" which is a reasonable attempt at fair comparison for a conference paper. The critic's concern is speculative (no evidence that tuning would close the gap), and the LF-VLA ablation already provides a controlled comparison. Moved to Nice-to-Haves.

- **"Statistical analysis beyond standard errors"** — Suggestions for additional statistical tests are reasonable but not weaknesses, as the main gaps are large enough to be obvious. Moved to Nice-to-Haves.

- **Generic strengths from the Strength Finder** — None removed; all cited strengths are specific and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any insight that the paper itself does not already articulate.

## Suggestions

1. Add standard errors or bootstrapped confidence intervals to Table 1 (LIBERO simulation results).
2. Expand the multi-primitive evaluation (Table 3) to at least 30+ trials per task, or add confidence intervals.
3. Clarify in Section 4.2 whether LF-VLA uses $X_{\text{attn}}$ or $X_{\text{out}}$ for its vision tokens.
4. Promote the freeze-vs-finetune ablation to a dedicated table in the main paper with full experimental details (training/unseen split, standard errors, number of trials).
5. Document the specific hyperparameter choices (learning rate, context length, action horizon) used for Octo and OpenVLA in the main pick-and-place experiments (Table 2).
6. Minor: rephrase "zero-shot manner" in the contributions to "zero-shot generalization to unseen tasks without fine-tuning the vision encoder" for clarity.
