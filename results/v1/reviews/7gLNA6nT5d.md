## Summary

This paper integrates n-gram induction heads—attention mechanisms originally developed for language modeling that hardcode n-gram matching—into Algorithm Distillation (AD) for in-context reinforcement learning (ICRL). The authors show that adding an n-gram layer to the transformer consistently improves performance across Dark Room, Key-to-Door, and Miniworld environments in terms of both data efficiency and hyperparameter search speed. They also extend the method to pixel-based observations by using vector quantization (VQ) to discretize images before n-gram matching. The core idea—bringing explicit n-gram induction heads from language into decision-making—is well-motivated and the empirical trend is in the right direction across multiple settings.

## Strengths

- **Novel application of n-gram induction heads to ICRL.** The paper is the first to transfer explicit n-gram attention from language modeling to in-context reinforcement learning. The motivation is grounded in prior work showing that transformers rely on induction heads for ICL and that these heads emerge slowly during training—hardcoding them is a reasonable way to address simplicity bias. This architectural angle is distinct from prior ICRL improvements (which have focused on data curation, retrieval, or recurrence).

- **Consistent positive results across environments and protocols.** The n-gram variant outperforms the matched baseline in all three environments (Dark Room, Key-to-Door, Miniworld), across different data budgets, history counts, and hyperparameter search budgets. The advantage is visible in both the EMP curves (Figures 2, 4, 5, 6) and the data scaling curve (Figure 1). The effect is not cherry-picked from a single favorable condition.

- **Clean ablations isolate the mechanism.** Table 1(a,b) shows that varying n-gram length (1- to 3-gram) and layer position does not significantly affect EMP, suggesting these extra hyperparameters do not expand the search burden. Table 1(c) shows that a permuted (broken) n-gram mask yields the same EMP as the baseline, confirming that the benefit comes from the matching signal rather than from added parameters or the VQ encoder alone.

- **Rigorous evaluation protocol.** Using EMP (Expected Maximum Performance) with random hyperparameter searches (Section 3.2) avoids cherry-picking individual runs and gives an honest comparison of how easy each method is to tune. The 10K gradient-step cap equalizes compute across methods.

## Weaknesses

### Major

- **The 27× data-efficiency claim is not substantiated and likely misleading.** The paper states (abstract, Section 4.2, Figure 4 caption) that the n-gram method "needs 27× less data" compared to AD. The evidence, however, is an indirect comparison: n-gram with 100 training goals achieves near-optimal return on Key-to-Door, while the baseline with 100 goals fails—and the 27× factor is then computed by comparing this 100-goal result to a *claimed* 2048-goal requirement taken from the original AD paper (Laskin et al. [17]) rather than from the paper's own baseline. The justification is deferred to Appendix B (missing from the available manuscript). The actual data scaling experiment on Dark Room (Figure 1) shows a more modest ~4× improvement (n-gram matches baseline at ~128 vs ~512 goals). The headline 27× figure is an extrapolation that pools data across different environments and experiments; it is not supported by the experiments presented. **This overclaim undermines the paper's credibility on its primary contribution.**

- **The visual-observation experiments are confounded by VQ preprocessing.** For pixel-based environments, the n-gram method receives discrete VQ codes while the baseline processes raw RGB images. This is not an apples-to-apples comparison—the n-gram method effectively gets a different (preprocessed) input representation. The permuted-mask ablation (Table 1c) shows that VQ + random n-gram attention does not help, but it does not rule out the possibility that VQ *interacts* with the correctly-patterned n-gram attention in a way that the baseline cannot replicate because it lacks the VQ encoder entirely. A clean control would feed VQ codes to the baseline as well. Without this, the performance gap in Figure 5 cannot be unambiguously attributed to the n-gram attention mechanism.

### Minor

- **The baseline implementation is not validated against original AD.** The paper repeatedly frames its comparison as "our method vs. AD," but it never demonstrates that its own baseline reproduces the performance reported by Laskin et al. [17] on comparable settings (same environments, same data regime). This leaves open the possibility that the reported gains are improvements over a weak reimplementation rather than over the actual Algorithm Distillation method. The internal comparison (n-gram vs. baseline under matched conditions) is valid, but the external claims about outperforming AD rest on an unvalidated baseline.

- **"Reduced hyperparameter sensitivity" is supported by convergence speed, not by variance.** The claim implies that performance varies less across hyperparameter choices. What the paper actually shows (Figure 2, 4, 5, 6) is that the n-gram method's EMP curve reaches near-optimal return with fewer hyperparameter assignments—i.e., it is *easier to tune*. These are related but distinct claims. The paper never reports the spread or variance of returns across the searched configurations. The evidence supports "faster hyperparameter search" more directly than "lower sensitivity."

- **Uneven training budgets in some comparisons.** In Figure 6 (left, Miniworld-Dark), the n-gram model is trained on 50 goals while the baseline is trained on 60 goals. Although this asymmetry favors the baseline (making the n-gram result more striking), it is inconsistent with the paper's otherwise careful matched-condition protocol and the rationale is not explained. This makes cross-figure comparisons of absolute performance confusing.

### Trivial

- The n-gram attention definition (Equation 1) uses an index scheme that could be clarified for readers unfamiliar with Akyürek et al. [2]. The two matching variants for discrete observations ("states" vs. "[s,a,r]") are introduced but never compared head-to-head; the reader must infer which is used in most plots.
- Figure 6 caption uses "Expected New Return" while all other figures use "Expected Max Return"—a minor terminology inconsistency.

## Nice-to-Haves

- Report how often VQ-based n-gram matches actually occur (e.g., match rate distribution) for image observations. The strict 4×4 grid, all-indices-must-equal condition could be extremely sparse; quantifying this would help assess whether the mechanism is plausible.
- A data scaling sweep on Key-to-Door (varying training goals for both methods and measuring final return) would directly support the data efficiency claim and replace the unsupported 27× figure with a properly measured curve.
- Report wall-clock training time or FLOPs to show that the n-gram layer's computational overhead does not offset the savings in hyperparameter search.

## Removed Points

These points from the inputs were removed after verification:

- *"The n-gram method's extra hyperparameters are not searched in the comparison"* — Section 4.4 and Table 1 explicitly ablate n-gram length and layer position and show they have little effect, so the comparison is fair.
- *"Data collection uses table Q-learning which is not typical for AD"* — AD is agnostic to the source RL algorithm; using Q-learning is a valid design choice.
- *"The paper distinguishes between tasks and learning histories in a way that departs from AD"* — The paper clearly explains this redefinition (Section 3.3) and its motivation.
- *"Missing appendix"* — The parser strips appendices; they exist in the original submission. However, claims whose sole support is in a removed appendix (27× justification) are flagged in the weaknesses above for insufficient in-text evidence, not for missing appendix formatting.
- *Formatting and style nitpicks* (parser artifacts, capitalization, etc.) are removed per instruction.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the same gap: the empirical trend is consistent and promising, but the evaluation has confounds that prevent clean attribution of the reported gains. The most interesting insight from the review process is that the permuted-mask control (Table 1c) is strong evidence in favor of the mechanism—it shows that adding parameters and VQ without the matching signal does not help—and deserves more prominence in the paper.

## Suggestions

1. **Remove or substantially qualify the 27× claim.** Replace it with the properly measured improvement from Figure 1 (~4× on Dark Room) and a data scaling curve on Key-to-Door. If the 27× figure is retained, it must be backed by a direct head-to-head experiment where both methods are evaluated at multiple data budgets.
2. **Control for the VQ confound.** Either feed VQ codes to the baseline as well, or implement n-gram matching directly on learned image embeddings (e.g., using attention keys) to avoid separate VQ pretraining.
3. **Validate the baseline against original AD.** Run the baseline under the conditions reported in Laskin et al. [17] and show that it reproduces their results. This is a quick sanity check that would significantly increase trust in the comparisons.
4. **Quantify hyperparameter sensitivity.** Report variance or interquartile ranges of final returns across hyperparameter samples, not just the EMP convergence curve.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Query Bucket | Comparison |
|--------|-----------|--------------|------------|
| Demonstration Distillation (Y8DClN5ODu) | 3.40 | topic-low | Rejected; evaluation had missing baselines and questionable cost-benefit. Current paper is clearly more novel but shares the problem of insufficiently supported claims. |
| Memory-Efficient AD (5iWim8KqBR) | 5.50 | topic-mid | Rejected; narrow evaluation and limited novelty. Current paper has more novel contribution but more significant evaluation gaps (overclaimed 27×, VQ confound). |
| How Transformers Implement Induction Heads (1lFZusYFHq) | 6.20 | topic-mid | Rejected theory paper; not directly comparable in research paradigm. |
| Distilling RL for In-Context Model-Based Planning (BfUugGfBE5) | 6.67 | topic-high | Accepted; strong experiments including continuous control. Current paper falls short of this evaluation standard. |
| Induction-Head Ngram Models (Zq8wylMZ8A) | 6.75 | topic-high | Rejected despite interesting idea; concerns about baselines and generalizability. Partially comparable—both involve n-gram induction heads and share some evaluation concerns. |
| XLand-100B (p9OsTj0nMP) | 7.00 | topic-high | Accepted dataset paper; different type of contribution. |

### Score Rationale

The paper has a genuinely novel idea (first to apply n-gram induction heads to ICRL) and shows consistent positive results across multiple environments, which is the main strength. However, the evaluation has three significant gaps: (1) the headline 27× data-efficiency claim is unsupported and appears to be an extrapolation across different experiments rather than a measured result; (2) the visual experiments are confounded by unequal preprocessing (VQ for n-gram, raw pixels for baseline); (3) the baseline is never validated against the original AD it claims to improve upon. The closest topical anchor (Memory-Efficient AD, 5.50) had a cleaner evaluation but less novelty; the current paper has more novelty but less rigorous evidence for its strongest claims. The low-band anchor (3.40) failed due to missing baselines and unsupported cost claims—the current paper is better than that, but not by a wide margin given its own unsupported 27× claim. A score of 4.5 reflects a paper with a promising direction that does not yet provide convincing evidence for its claimed contributions.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>