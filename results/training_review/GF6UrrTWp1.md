Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

The paper studies how increasing training data size (while maintaining the proportion of spurious-correlation samples) affects spurious feature reliance across three domains: reasoning tasks (LEGO, PVR), vision (CelebA), and language (MultiNLI). In reasoning tasks, scaling data to tens of thousands of samples eliminates spurious reliance to perfect accuracy (Figure 4). In complex vision/language distributions, the same scaling *exacerbates* spurious correlations (Figure 6). The paper attributes this divergence to "atypical samples" and claims (in the abstract and conclusion) a remedy based on sampling typical invariant features, but this remedy is never described or evaluated.

## Strengths

- **Cross-domain study of an underexplored question.** The paper asks a specific, under-investigated question: does data quantity (at fixed spurious proportion) affect spurious correlations independently of proportion? Testing this across reasoning, vision, and language is a useful methodological contribution — most prior work focuses on proportion or environment diversity.

- **Clear positive result in reasoning tasks (Figure 4).** In all three reasoning tasks, scaling from few thousand to tens of thousands of samples (while maintaining spurious proportion) drives test accuracy on spurious-breaking test sets to 100%. This provides concrete evidence that proportion alone does not determine spurious reliance.

- **Margin analysis provides a mechanism for the low-data regime (Figure 5).** The paper demonstrates that in the low-data regime, the network uses the spurious rule to boost its logit confidence, and this crutch disappears as data increases. This gives a quantitative explanation for why starvation leads to spurious shortcuts.

- **Non-monotonic finding in complex distributions (Figure 6).** The observation that doubling training data can *decrease* worst-group accuracy on CelebA and MultiNLI is interesting and potentially important. If verified and explained, this would challenge the common assumption that more in-distribution data is always beneficial for robustness.

## Weaknesses

### Fatal
None. The paper's core empirical findings (reasoning scaling helps, complex-distribution scaling can hurt) are present and supported, albeit with caveats detailed below. The missing remedy is a major overclaim, not a fatal flaw that invalidates the rest.

### Major

- **Claimed "effective remedy" is entirely absent.** The abstract states: "Taking inspiration from reasoning tasks, we present an effective remedy to this problem to ensure that drawing more samples from the distribution always overcomes spurious correlations." The conclusion similarly claims to "show" this remedy. However, no algorithm, description, or experimental evaluation of any remedy appears anywhere in the paper. The conclusion merely says "if one carefully draws samples with easier invariant features" — a vague statement, not a presented remedy. This is a serious overclaim. The paper must either deliver the remedy with experiments or remove the claim entirely.

- **Explanation for why scaling hurts in complex distributions (Section 5.3) is entirely speculative and unsupported.** The paper attributes the exacerbation to "new samples which contain general features that are not well represented in the original training set but also contain the spurious feature." No evidence is provided for this mechanism — no sample visualizations, no quantitative measure of "typicality," no ablation that removes/isolates such samples, no feature analysis. Without evidence, this remains an untested post-hoc story. This matters because understanding *why* the reasoning and complex-distribution results diverge is central to the paper's narrative.

- **The paper does not formally state or test a "hypothesis."** The title calls this "The Invariance Starvation Hypothesis," but the word "hypothesis" never appears in the body. There is no falsifiable statement of what the hypothesis predicts, what would constitute evidence for or against it, or how the reasoning-task results (which support it) and the complex-distribution results (which contradict it) relate to it. The paper instead introduces a second mechanism (atypical features) to explain the contradiction without refining the hypothesis. A scientific claim called a "hypothesis" should be stated precisely enough to be tested or refuted.

### Minor

- **Confound in reasoning experiments: total gradient steps covary with dataset size.** In Section 3.3, training uses fixed epochs (100) and fixed batch size (1000). As dataset size grows, the number of gradient updates scales proportionally (e.g., 400 updates for 4,000 samples vs. 4,000 updates for 40,000 samples). The paper attributes improved performance to more "invariant information" in the data, but the effect could partially come from more total training steps. This does not invalidate the finding — more training steps on more unique examples is different from more steps on repeated examples — but the paper should discuss and ideally control for this (e.g., by reducing epochs proportionally in one condition).

- **"Selection Bias does not form Spurious Correlations. Starving Networks of Sufficient Training Data Does." (Introduction) presents a strong conclusion before evidence.** While the paper eventually supports the second part (for reasoning tasks), the categorical "does not" in the first clause oversells the results, especially given that the complex-distribution experiments contradict the simple narrative. This framing could mislead readers about the scope of the findings.

- **No characterization of what "sufficient invariant information" means quantitatively.** The paper uses this term throughout but never defines it formally. In reasoning tasks it corresponds to a known number of training samples, but in vision/language settings it is never operationalized, making it difficult to test, use, or build upon the claimed concept.

### Trivial

- None that survive filtering per the guidelines.

## Nice-to-Haves

- **Justification for using pre-trained BERT on synthetic toy tasks (Section 3.3).** The paper uses a pre-trained BERT model for highly structured artificial reasoning tasks without discussing whether pre-trained representations are needed or appropriate here. A brief justification or ablation would clarify this design choice.

- **Controlling for the gradient-step confound in reasoning tasks.** Running an additional experiment where total gradient updates are held constant (by reducing epochs as dataset size increases) would cleanly separate the effect of more data from the effect of more training, strengthening the core claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *Criticism about missing related work on scaling laws (Kaplan et al., Hoffmann et al.).* Removed per instructions: "DO NOT mention missing related works, as you do not have external sources to confirm their existence."
2. *Criticism that "Figures 3a–c are only shown for a single dataset size" and "no evidence that these errors persist across larger datasets."* Removed: this misunderstands the paper's structure — Figure 3 establishes the phenomenon, and Figure 4 shows how it resolves with scaling.
3. *Criticism about data diversity as an alternative explanation (Harsh Critic's point 2a/2c).* Removed: these are generic alternative explanations that the paper's experimental design reasonably addresses by holding proportion fixed and measuring confidence directly (Figure 5).
4. *Criticism that the paper should be split into two papers.* Removed: this is a structural suggestion, not a weakness of the submitted work.
5. *Pure formatting/style nitpicks and concerns about reproducibility of trivial details.* Removed per guidelines.

## Novel Insights

None beyond the paper's own contributions. The two key insights from the reviews — that the missing remedy is a critical overclaim and that the gradient-step confound should be addressed — are standard reviewer observations that the authors would be expected to notice and fix in revision. The genuine insight in the paper (data quantity at fixed proportion matters differently across domains) is the authors' own contribution.

## Suggestions

1. **Remove or deliver the remedy.** Either delete the claim from the abstract and conclusion, or add a concrete algorithm and experimental validation of a method that "carefully draws samples with easier invariant features."
2. **Provide evidence for the complex-distribution mechanism.** Either add diagnostics (per-sample loss analysis, feature visualization, ablation studies that isolate atypical samples) or remove the mechanistic claim and present the finding as an empirical observation without a verified explanation.
3. **State the hypothesis formally.** Add a clear, falsifiable statement of "The Invariance Starvation Hypothesis" — e.g., "A network will rely on a spurious feature iff the training data does not contain enough samples for the network to learn the invariant feature with sufficient confidence (measured by margin/logit)." Then clarify how the complex-distribution results qualify or limit this hypothesis.
4. **Address the gradient-step confound in the reasoning experiments.** Either add a control experiment (reducing epochs as dataset size grows to hold total updates constant) or discuss why the confound does not explain the effect.
5. **Operationalize "sufficient invariant information."** Give a concrete, measurable definition tied to the experiments (e.g., number of training samples, or a threshold on margin/confidence), so the concept can be tested or applied by other researchers.

## Score and Decision

The paper identifies an interesting and underexplored question, provides clean positive results in reasoning tasks, and reports a surprising negative result in complex distributions. However, it suffers from a major overclaim (a remedy that does not exist), an unsupported causal explanation for its most interesting finding, a potentially confounding experimental design in the reasoning tasks, and a loosely defined central concept that does not meet the scientific standard implied by the word "hypothesis." With substantial revisions — removing overclaims, adding mechanistic evidence, and addressing confounds — the paper could become a solid contribution. In its current form, the weaknesses outweigh the contributions.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>