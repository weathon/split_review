- Decision: Reject
- Avg Score: 4.83
- Scores: 5, 5, 5, 6, 3, 5
Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

---

## Summary

This paper proposes SALSA, a simple modification to PPO-based RLHF: replacing the standard single-SFT reference model (used for the KL penalty) with a weight-space average of two independently fine-tuned SFT models (a "model soup"). The motivation is that the soup occupies a higher-reward region of parameter space even before RL training, allowing the policy to explore a more promising neighborhood while maintaining stability. The method is evaluated on Llama2-7B, Mistral-7B, and Gemma-2B across three instruction-following benchmarks (MT-Bench, Arena-Hard, UltraFeedback), reporting win rates of ~50–57% against standard PPO across all nine model–dataset combinations.

## Strengths

1. **Well-motivated, methodologically clean idea.** Replacing the reference model with a soup of two SFT models is straightforward to implement (one weight averaging step) and is grounded in the established observation that fine-tuned models from the same pretrained initialization lie in a shared low-error basin (Wortsman et al., 2022). The paper clearly states this rationale and ties it to the specific challenge of KL-constrained exploration in RLHF.

2. **Consistent win-rate improvements across diverse settings.** Table 1 reports SALSA vs. PPO win rates exceeding 50% in all nine tested combinations (three models × three datasets), with the lowest being 50.68% and the highest 57.19%. While the magnitudes are modest, the consistency (9/9 > 50%) provides evidence that the effect is systematic rather than a single lucky run. This breadth of evaluation (multiple model families, sizes, and benchmarks) is a genuine strength.

3. **Reward analysis demonstrates a pre-RL advantage of the soup.** Section 4.2 (Figure 2) shows that the weight-averaged model achieves higher mean reward on MT-Bench than either constituent SFT model *before any PPO training*. This empirically grounds the paper's central motivation: the soup is not just a different anchor but genuinely resides in a higher-reward region. The three-model barycentric plot (Figure 2c) further shows that rewards peak near the centroid of the SFT models, consistent with the soup hypothesis.

4. **Ablations isolate the key design choices.** The α sweep (Figure 4a) shows win rate peaking at the midpoint (α=0.5) and dropping to 43.07% when using the other SFT model alone (α=1), confirming that the *interpolation* matters, not just having a second model. The MKL baseline (Figure 4b) shows that averaging the KL divergence to two separate references is less effective than using the averaged model as a single reference point, further supporting the soup design.

## Weaknesses

### Fatal
None.

### Major

1. **No confidence intervals or statistical significance for win rates.** The paper's central evidence (Table 1) consists entirely of point estimates. Several win rates are very close to 50% (e.g., 50.68% on UltraFeedback with Gemma-2B, 50.75% with Llama2-7B). Without confidence intervals, bootstrapped estimates, or any measure of uncertainty, the reader cannot determine whether these values represent true outperformance or random variation — especially given that MT-Bench uses only 80 questions. The paper states that "`β` achieves the highest win rate" was used, but if this tuning was done on the evaluation benchmarks themselves (as the text suggests), the reported numbers may be optimistically biased. The consistency across 9 combinations is suggestive but not a substitute for rigorous uncertainty quantification. **The authors should provide bootstrapped confidence intervals for all win rates, or exact binomial intervals, to make the core claim interpretable.**

2. **The term "adjusted win rate" is never defined.** Table 1 and the ablation study (Figure 4, Section 4.4) repeatedly use the phrase "adjusted win rate" without any explanation of what "adjusted" means. From context (line 139: "we use the KL coefficient β that achieves the highest win rate"; line 254: "for each α, we adjusted the KL divergence to achieve the optimal win rate over PPO"), it appears that the reported win rates are the best achievable after tuning β per method and per dataset. This needs to be stated explicitly. If β was tuned on the test benchmarks themselves (MT-Bench, Arena-Hard, UltraFeedback), this risks overfitting and inflating reported numbers.

### Minor

1. **Out-of-distribution robustness is claimed but not tested.** The abstract (line 4) and conclusion (line 286) claim that SALSA improves "out-of-distribution generalization" and "robustness to out-of-distribution data." Yet all three evaluation benchmarks (MT-Bench, Arena-Hard, UltraFeedback) are instruction-following tasks similar in distribution to the training data (UltraFeedback). No genuine OOD evaluation is conducted — e.g., on summarization, code generation, mathematical reasoning, or a different domain. This claim should either be removed or supported with appropriate experiments.

2. **"PPO does not significantly outperform SFT" is stated without evidence.** Line 228 asserts this claim, but the paper does not report PPO vs. SFT win rates, nor does it provide any statistical test comparing them. This claim should be either supported or removed.

3. **Key mechanistic claim (larger KL deviation) is not substantiated in the main text.** The paper asserts (lines 5, 198) that using the soup reference "permits greater deviation in KL divergence" and "allows the policy to investigate a more extensive area within the solution space." The main body does not present any KL divergence measurements over training, and the only cross-reference (Table `tab:app:mean_kl`) is to an appendix section stripped by the parser. **If the appendix contains this data** (as the cross-reference suggests), the authors should move a summary of it (e.g., a brief plot or table) into the main text, since the KL claim is central to the paper's explanatory narrative.

### Trivial

- The paper uses "out-of-distribution" loosely: sometimes referring to the model soup literature's OOD robustness (which is about *weight-space* generalization) and sometimes appearing to claim OOD robustness for the RLHF-trained policy. Clarifying this distinction would help.
- Missing definition of "adjusted win rate" — a single sentence in the experimental setup would resolve this.

## Nice-to-Haves

- **Comparison to a dynamically updated reference.** The related work section discusses Gorbatovski et al.'s dynamic reference model. A comparison (or at least a discussion of why the soup approach differs from dynamic reference updating) would help contextualize the contribution.
- **KL divergence over training.** As noted above, a small plot or table of KL(π_θ || π_ref) for both SALSA and PPO over training steps would directly validate the claimed mechanism. This is already referenced in the appendix (Table `tab:app:mean_kl`); moving a summary to the main text would strengthen the paper.
- **Human evaluation or a discussion of GPT-4 judge biases.** The paper uses GPT-4-Turbo as an automated judge. A brief acknowledgment of known biases in LLM-as-a-judge evaluations would be appropriate.

## Removed Points

These points were raised by reviewers but are excluded from the main review for the reasons noted:

1. **"Reward analysis confounded by reward model overfitting"** (Harsh Critic, Issue 3) — REMOVED because the criticism misunderstands the setup. The reward model evaluates *responses*, not model weights. It has no information about whether a response was generated from a weight-averaged model or a single model. The concern that the reward model "learned to assign higher scores to responses that are averages of the two SFT outputs" does not hold: the reward model sees individual responses, not weight-space interpolations, and the soup is a weight-space (not output-space) average. No confound specific to the soup vs. single-model comparison is identified.

2. **"No KL divergence measurements reported"** (Harsh Critic, Issue 2) — MOVED to Removed Points in its strong form. The paper references Table `tab:app:mean_kl` (line 261) and Section `sec:kl-divergence` (line 255), indicating that supporting KL measurements exist in the appendix. Per the review guidelines, missing appendix content is a parser artifact, not an author error. The concern is noted in Minor Issue 3 above (the main text lacks this evidence) but the original "fatal" framing is removed.

3. **"Missing comparison to DPO, SimPO, dynamic reference methods"** (Harsh Critic, Related Work) — REMOVED. The paper's stated scope is improving PPO-based RLHF by replacing the reference model. Demanding comparisons to DPO-variants that use entirely different training paradigms is scope creep. The paper is evaluated on what it sets out to do.

4. **"Overclaims about the method's benefits"** (Harsh Critic, Conclusion) — PARTIALLY REMOVED. The overclaim about OOD robustness is retained (Minor Issue 1 above) because it is verifiable from the paper. The critic's additional claim that "larger KL deviation" is unsubstantiated is moved to Minor Issue 3 (with the appendix caveat). The claim about "searching for higher potential model" is adequately supported by the reward analysis in Section 4.2.

## Novel Insights

None beyond the paper's own contributions. The paper's core observation — that weight-space averaging of SFT models produces a reference point in a higher-reward region even before RL, and that using this as a PPO anchor yields consistent but modest improvements — is itself the novel finding. The reviews do not surface any deeper insight that the paper missed.

## Suggestions

1. **Add confidence intervals (bootstrapped or exact binomial) to all reported win rates.** This is the single most impactful improvement. Provide a brief explanation for why all 9 combinations exceed 50% even when individual intervals may overlap 50%.

2. **Define "adjusted win rate" explicitly.** State that it is the win rate achieved after tuning β to maximize performance on each evaluation benchmark (or state if a validation split was used instead).

3. **Move a summary of KL divergence measurements into the main text.** If appendix Table `tab:app:mean_kl` contains mean KL values, a brief figure or table showing KL(π_θ || π_ref) over training for both SALSA and PPO would directly support the claimed mechanism.

4. **Remove or qualify the OOD robustness claims**, or add an OOD evaluation (e.g., on a summarization or code generation benchmark not represented in the training data).

5. **Report the β values used for each model × method × dataset** to allow reproducibility assessment.
