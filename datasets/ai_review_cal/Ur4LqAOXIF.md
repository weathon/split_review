- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes a paradigm shift from static offline OOD detection to an online setting where the OOD detector continuously adapts as a stream of ID and OOD samples arrives. It formalizes the online OOD detection problem with a non-stationary environment mixture model, introduces SODA (an online gradient descent-based algorithm), provides a regret bound analysis, and reports empirical gains over offline baselines on CIFAR-10 and ImageNet-1k. The core direction — adapting OOD detectors to changing environments — is timely and well-motivated.

## Strengths

1. **Formalization of non-stationary OOD distributions.** Section 2.1 (Eq. 1) defines the environment mixture \(\mathcal{Q}_{t}^{\mathrm{env}}=(1-\pi_{t})\mathcal{P}^{\mathrm{in}}+\pi_{t}\mathcal{P}_{t}^{\mathrm{out}}\), where \(\mathcal{P}_{t}^{\mathrm{out}}\) can change over time. This explicitly generalizes prior formulations (e.g., Katz-Samuels et al., 2022) that assumed stationary OOD, making the framework directly relevant to shifting real-world environments.

2. **First regret bound for online OOD detection.** Theorem 3.1 provides a sub-linear regret guarantee with an interpretable decomposition into two terms — one capturing difficulty from ID samples and the other from OOD samples — explicitly linking the mixture ratio and the norms of ID/OOD inputs. This is the first such guarantee for an online OOD detection algorithm.

3. **Empirical validation of sub-linear regret under non-stationary environments.** Figure 1b demonstrates that SODA's regret spikes briefly at OOD distribution changes (vertical lines) but recovers and trends sub-linearly. This provides direct evidence that the algorithm adapts to continuous environmental shifts — a genuinely novel demonstration in the OOD detection literature.

4. **Large-margin improvements on ImageNet-1k.** Table 1 shows SODA reduces average FPR95 by 27.64% over the best offline method (KNN+) and 18.54% over WOODS on ImageNet-1k. On ImageNet the ID data advantage is minimal (1,241,167 pre-training images vs. 40,000 environment images), so these gains are more clearly attributable to online adaptation.

5. **Flexible framework across scoring functions.** Section 4.3 provides concrete OOD and ID loss formulations for ODIN and Energy-based scoring (Eq. 4–5), and Table 2 reports performance for MSP, ODIN, and Energy instantiations. This demonstrates the framework is not tied to a single scoring function.

6. **Transparent comparison framing.** The paper explicitly notes key differences when comparing with WOODS (line 143): "This is not directly comparable with our online OOD detection setting, as we do not assume the model has access to the environment samples in advance." This honesty makes the comparison more credible.

## Weaknesses

### Fatal
None.

### Major

- **ID data quantity confound in the CIFAR-10 comparison.** The CIFAR-10 training set is split into 10,000 images for pre-training and 40,000 images for the environment stream (line 123). SODA updates on the entire 40K stream. With the default mixture ratio π=0.2 (line 127), approximately 32,000 ID samples appear in the stream, giving SODA exposure to ~42K total ID images. The offline baselines are pre-trained only on the 10K subset and remain static — they do not see the remaining 40K ID images at all. The reported 9.63% FPR95 reduction over KNN+ could therefore partly or largely reflect this 4× disparity in ID data quantity rather than OOD-specific adaptation. No ablation isolates the source of improvement (e.g., training offline methods on the full 50K set, or running an ablation that updates on ID data only without OOD-specific losses). The image caption for Figure 1 says "averaged over 5 random runs" but no variance or confidence intervals are shown for any result, making it impossible to assess statistical reliability. For ImageNet the confound is negligible (1.24M pre-training vs. 40K stream), which is why the ImageNet evidence is stronger. But as presented, the CIFAR-10 results do not cleanly support the claim that online OOD *adaptation* (as opposed to more ID data) drives the improvement.

### Minor

- **Unsupervised extension is mentioned but never developed.** Line 18 claims "a straightforward unsupervised extension for SODA, enabling SODA to tackle the online setting without necessitating any environment feedback." No description, formulation, or evaluation of this extension appears anywhere in the paper. Since the core SODA algorithm assumes oracle feedback (true labels for ID, OOD indicator for OOD) at every timestep (Algorithm 1, line 6; Algorithm 2), the paper's claim of "practicality" (line 14) is weakened by this dangling promise.

- **Theory-practice gap in the regret analysis.** Theorem 3.1 is stated "under conditions that are commonly found in online convex optimization" (line 93), but experiments use deep neural networks — a fundamentally non-convex model class. The paper mentions "linear probing" as a bridge (line 109), which is a reasonable partial connection, but does not acknowledge the gap or provide justification for why convex analysis should predict neural network behavior. This weakens the link between the theoretical guarantee and the empirical results.

- **Missing variance reporting.** Figure 1 reports results "averaged over 5 random runs" but shows no error bars, confidence intervals, or other measures of dispersion. Given the small number of runs, variance could be substantial, and the reader cannot assess the reliability of the regret curves or the main performance numbers.

### Trivial
None.

## Nice-to-Haves

- An ablation that pre-trains offline methods on the full 50K CIFAR-10 set (or otherwise equates ID data quantity) to cleanly isolate the benefit of online OOD adaptation.
- A sensitivity analysis on the environment switching frequency Δ (currently fixed at 4,800).
- Discussion of realistic deployment scenarios where environmental feedback is available (e.g., human-in-the-loop, flagged by another system) to address the feedback assumption.

## Removed Points

- **WOODS comparison is "misleading" / "adds noise."** Removed because the paper is transparent about the comparison's limitations (line 143: "This is not directly comparable…"). The authors provide the comparison with explicit caveats, which is appropriate.
- **"The paper would benefit from acknowledging ID distribution shift limitation."** Removed because the paper explicitly scopes itself to non-stationary *OOD* with stationary ID (line 34–40). Criticizing a paper for not addressing what it scoped out is unreasonable.
- **"Loss functions are described only vaguely."** Removed because the paper provides the loss formulations in Section 3.1 and additional instantiations in Section 4.3 with full equations (Eq. 4–5). No material information is missing from the main text.
- **"Comparison with WOODS not controlling for architecture/loss/hyperparameters."** Removed because the paper explicitly states the comparison is "not directly comparable" and frames it as additional, not primary, evidence.
- **Various formatting, style, and parser-artifact nitpicks.** Removed per instructions (parser issues, not author errors).

## Novel Insights

The harsh critic's review identifies a genuinely subtle experimental confound — the conflation of ID data quantity with OOD adaptation gains in the CIFAR-10 split — that the paper itself does not flag or discuss. This is a methodological blind spot that is real but also somewhat inherent to the online setting (the online learner is *supposed* to learn from the environment stream; the question is what proportion of the improvement is ID-specific vs. OOD-specific). The critic's framing of this as a potential confound rather than a fatal error is the right calibration. Meanwhile, the strength finder correctly identifies that the non-stationary experiments and the ImageNet results offer cleaner evidence that survives this criticism. Neither reviewer noticed that the non-stationary regret recovery (Figure 1b) is actually the strongest evidence for OOD-specific adaptation, because it shows the model re-learning after OOD distribution switches — something that more ID data alone could not explain.

## Suggestions

1. **Fix the CIFAR-10 evaluation.** Either pre-train all methods on the full 50K CIFAR-10 set and reserve a separate held-out ID set for the online stream, or include an ablation where offline methods are also trained on the 40K environment images. Re-run the comparison.
2. **Either develop the unsupervised extension or remove the claim.** A one-line mention of "a straightforward unsupervised extension" with no follow-through is not acceptable. Either provide the formulation and at least minimal evaluation, or remove the sentence.
3. **Add variance estimates.** Report standard deviations or confidence intervals over the 5 random runs for all main results and regret plots.
4. **Acknowledge the theory-practice gap explicitly.** A brief discussion of why the convex analysis is useful despite non-convex neural network training (e.g., serves as a guarantee for linear probing, which is separately validated) would be sufficient.
