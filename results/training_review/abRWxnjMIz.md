Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper introduces the task of "scoping" language models — restricting them to answer only queries relevant to a specific deployment domain (e.g., a sentiment-analysis-only chatbot). It adapts Circuit Breakers (CB), originally proposed for safety alignment, to this scoping task and compares it against system prompting, SFT, DPO, and probing across three accept tasks (Sentiment Analysis, Summarization, Program Execution). The paper also proposes layering SFT and CB (SFT→CB) as a way to combine accept-task performance with robust rejection. A key claimed finding is that CB generalizes from narrow rejection distributions and is more robust to adversarial prompting than baselines.

## Strengths

1. **Timely and well-motivated problem**: Task-specific scoping is a real deployment need that is distinct from general safety alignment. The paper formalizes this cleanly (Section 3.1) and motivates it with concrete failure examples.

2. **Comprehensive experimental design**: The paper evaluates five methods (Sys., SFT, DPO, Probe, CB, SFT→CB) across three distinct accept tasks, seven black-box adversarial attacks, and three experimental dimensions (adversarial robustness, diversity scaling, multi-task acceptance). This provides a systematic empirical foundation for future work on scoping.

3. **Demonstrates CB's generalization from narrow rejection distributions**: The diversity experiment (Section 4.2, Figure 3) shows that CB and SFT→CB achieve strong OOD rejection even when trained on a single rejection category, supporting the claim that CB can generalize from limited data. This is a practically useful property for deployments where collecting broad rejection data is expensive.

4. **Introduces SFT→CB layering**: The paper proposes combining SFT (for accept task quality) with CB (for rejection), showing that SFT→CB often achieves strong accept scores while maintaining robust rejection across multiple settings. This combination is novel and practically appealing since it requires only a single model call at inference time.

5. **Clear discussion of limitations**: The paper honestly acknowledges failures — CB's degradation at high diversity, SFT→CB's high rejection rate on accept tasks in the Math+PE multi-task setting, and that no method is close to perfect. This candor is valuable.

## Weaknesses

### Fatal

None.

### Major

1. **Unsupported claims in Section 4.4 (Additional Analysis)**: The paper lists four findings — precise scoping (e.g., News summarization only), effect of data quantity, effect of LoRA rank, and representation analysis — as bullet points **without any supporting figures, tables, or quantitative results**. These are presented as contributions in the introduction bullet list ("we find that CB...can scope more precisely than other methods") but the main text provides no evidence. This is a significant omission: the representation analysis claim ("CB changes representations across the entire context while SFT/DPO only affect the tail") is interesting but unsubstantiated, and findings about LoRA rank effects and data quantity are asserted without any data. This undermines the paper's completeness and weakens several claimed contributions.

2. **Overclaimed narrative relative to mixed evidence**: The abstract and introduction assert that "CB is more robust both for out of distribution tasks, and to adversarial prompting techniques" and that "layering SFT and CB together often results in the best of both worlds." While these claims hold in several settings, the evidence is more nuanced than the abstract suggests: (a) Probe outperforms CB under TAP for Sentiment Analysis (Section 4.1); (b) CB's OOD rejection collapses at high diversity for SA and PE, though not for Summarization (Section 4.2); (c) SFT→CB shows >50% rejection on the accept set in the Math+PE multi-task setting (Section 4.3). The paper acknowledges these failures in the body but the high-level narrative does not sufficiently calibrate expectations. The claim "can scope more precisely than other methods" (intro bullet) is entirely unsupported.

### Minor

1. **Single-model evaluation**: All main experiments use Mistral-7B-Instruct-v0.2 only. Granite results appear only in the teaser and are deferred to the appendix. While the paper acknowledges this limitation and notes that the considered methods have been validated on other models, the paper's central empirical conclusions about relative method performance cannot be assumed to generalize without cross-model validation. This is partially mitigated by existing evidence that CB works across models in its original setting, but the gap remains for the specific scoping task.

2. **Rejection detection validated on a small sample**: The CB-specific rejection detector (repeated-pattern matching) is tuned on 90 completions total (30 each from accept, reject, and OOD reject sets), achieving 1 false negative and 0 false positives on this tuning set. No held-out validation of detection accuracy is reported on the actual evaluation sets. Given that rejection metrics drive the core comparisons, systematic false negatives/positives could bias results. This is a non-trivial methodological gap, though the paper does attempt some validation and uses distinct detection strategies for different method types.

3. **No statistical rigor**: Results are presented as single points without error bars, confidence intervals, or significance tests. The TAP attack runs only 10 prompts per dataset. While this is common practice in large-scale LLM evaluations, the absence of any variability quantification means the reported differences between methods could be noise in some cases.

4. **SFT→CB hyperparameters not re-tuned for the combined method**: The paper uses hyperparameters from separately tuned SFT and CB runs without re-tuning for the combined pipeline. Given the observed failure in the Math+PE multi-task setting, it is unclear whether this failure reflects a fundamental limitation or simply suboptimal hyperparameter transfer.

### Trivial

None.

## Nice-to-Haves

- A follow-up study on why CB degrades at high diversity for SA and PE but not Summarization (task characteristics? representation geometry? optimization difficulty?)
- An investigation of why SFT→CB fails in the Math+PE multi-task setting — is it due to task dissimilarity, overfitting to composite instructions, or the specific combination order?
- Conditional CB variants that orthogonalize representations per-task rather than globally, as hinted at in the discussion

## Removed Points

- **"The classifier g is never formally defined"**: This is factually incorrect — Section 3.1 defines g as "a classifier g: y → c ∈ {0, 1}." The reviewer appears to have missed this definition.
- **Strength Finder claim #6 about "representation-level insights"**: The paper states the representation finding in Section 4.4 but provides **no evidence** (no figures, tables, or metrics). This is an unsupported claim, not a strength. Removed because it conflicts with a verified weakness (unsupported additional analysis).
- **Human review comparison removed**: Not relevant to this review.

## Novel Insights

The critical interaction between the reviews reveals something the paper itself does not fully articulate: CB's strengths and weaknesses are **symmetric**. CB's advantage — broad generalization from narrow data — appears to stem from the same mechanism as its limitation: orthogonalizing representations globally rather than conditionally. When the rejection set is homogeneous (single category), a single orthogonal direction suffices and generalization is strong. As diversity increases, the model must find multiple orthogonal subspaces simultaneously, and optimization becomes unstable. This symmetry suggests that the right solution is not a single global CB but a **conditional** or **task-aware** CB that orthogonalizes per input type — exactly the direction the discussion hints at but does not develop. The SFT→CB layering partially mitigates this (SFT moves representations first, simplifying the subsequent orthogonalization), which explains why SFT→CB stays competitive at high diversity while CB alone degrades. This trade-off between generality and precision is the paper's deepest finding, though it is left implicit.

## Suggestions

1. **Either remove Section 4.4 or provide actual evidence**: The four bullet points in Section 4.4 are stated as findings but have no supporting data. Either add figures/tables/metrics, or remove them and corresponding intro bullets. The representation analysis claim, in particular, needs a quantitative visualization (e.g., per-token representation distance heatmaps) to be credible.

2. **Tone down abstract/intro claims to match the evidence**: Replace "CB is more robust" with "CB is often more robust, with notable exceptions (Probe under TAP; degradation at high diversity)." Replace "generalizes from a very narrow distribution" (which is accurate) with a qualifier about the diversity ceiling.

3. **Add detection accuracy validation on a held-out set**: Report precision and recall of all rejection detectors on at least 200 labeled completions drawn from the actual evaluation distribution. This is critical for confidence in the core comparisons.

4. **Add at least one additional model to the main results**: If the Granite results in the appendix are extensive, move them to the main paper. If not, replicate the adversarial and diversity experiments on one additional model family (e.g., Llama-3-8B or Gemma-7B).

5. **Run the multi-task Math+PE experiment with re-tuned SFT→CB hyperparameters** to determine whether the observed failure is fundamental or a hyperparameter artifact.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>