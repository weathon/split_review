Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper proposes BlindAvg, a non-interactive protocol for distributed differentially private learning where users each locally train a model (SVM or Softmax regression), add Gaussian noise, and then securely average all models in a single round. The main contributions are: (1) a convergence theorem showing that blind averaging of hinge-loss SVMs converges to the centralized model at rate O(1/M) when the task is robust to strong L2-regularization; (2) the first output perturbation bounds for Softmax regression (Theorem 3.1), with Lipschitzness independent of the number of classes; (3) empirical results on CIFAR-10, CIFAR-100, and federated EMNIST demonstrating competitive privacy-utility tradeoffs; and (4) a system design supporting heterogeneous local data sizes and scalable secure summation.

## Strengths

- **Novel Softmax regression sensitivity bounds (Theorem 3.1, Corollary 3.2).** The paper proves that the Lipschitz constant for SoftmaxReg-SGD is $L = \Lambda R + \sqrt{2}c$, which is independent of the number of classes $K$. This improves on OVR SVMs whose privacy budget scales with $\sqrt{K}$, and is the first DP guarantee of its kind for softmax regression trained with SGD. The analysis leverages a clean lemma bounding the softmax probability vector's deviation from a one-hot encoding (maximized at $\sqrt{2}$), and the proofs of strong convexity, smoothness, and Lipschitzness are technically sound.

- **Convergence theory for blind averaging of hinge-loss SVMs (Theorem 4.3).** Using strong duality and the averaged representer theorem (Corollary 4.1, Lemma 4.2), the paper proves that under strong L2-regularization, the average of locally trained hinge-loss SVMs converges to the global SVM at rate $O(1/M)$ in local iterations. This closes a gap left by Jayaraman et al. (2018), whose bounds scaled with dataset size rather than iteration count. The proof is clean and provides theoretical justification for the high-regularization regime.

- **Clean protocol design with provable centralized-DP guarantees (Theorem 5.1, Corollary 5.2).** BlindAvg requires only one secure summation invocation per user, achieving non-interactivity. The noise scales as $\tilde{\sigma}/\sqrt{t \cdot w}$ rather than $O(\sqrt{w})$ as in DP-FL. The system handles differing local data sizes via upscaling while keeping sensitivity constant, and the user-level sensitivity bound of $2R/w$ (Corollary 5.2) is a practical contribution for large-scale deployment.

- **Convincing empirical demonstration of the regularization-robustness insight (Figure 5).** The paper systematically varies $\Lambda$ across 4+ orders of magnitude and shows that (a) at high $\Lambda$, the averaged model converges to the global model (supporting the theory), (b) at mid-range $\Lambda$, both models maintain close task performance (the practically relevant regime), and (c) the deliberately designed SynFail confirms the failure case exactly when the task is not robust to regularization. This provides genuine insight into *when* blind averaging works.

- **Non-IID ablation with explicit failure case (Table 2, Figure 3).** The extreme one-class-per-user scenario degrades accuracy by only ~2pp for SVM, and the SynFail scenario cleanly demonstrates the boundary condition. The paper is unusually transparent about where the method fails.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical convergence result (Theorem 4.3) and the main experimental results use incompatible SVM formulations.** Theorem 4.3 is proven specifically for hinge-loss SVMs (HingeSVM-SGDWA). However, the main privacy experiments (Figures 2, 4, 7) use SVM-SGD with a *Huber loss* (a smoothed approximation), not the hinge loss. The paper acknowledges this in the Figure 5 caption ("In contrast to HingeSVM, SVM-SGD does not converge without error as it uses a relaxation of the hinge loss: the Huber loss where non-support-vectors can influence the model independent of the regularization"), yet the paper's central narrative presents the theory as supporting the SVM-SGD experimental results. The only experimental validation of the actual HingeSVM theory is on synthetic data (SynNonIID, Figure 5a-b). This disconnect means the paper's headline convergence guarantee does not directly apply to the algorithm evaluated in its main accuracy-vs-ε plots, weakening the core claim that "convergence theory supports the experimental results."

- **The convergence regime (very high Λ required by Theorem 4.3) does not align with the regime where BlindAvg achieves its best practical utility.** The theorem requires a regularization parameter Λ large enough that all data points fall within the margin (support vectors = all data). At these extreme Λ values, model accuracy is poor for all methods. The compelling utility-privacy tradeoffs in Figures 2 and 4 occur at *mid-range* Λ (≈1–10), where the theory does not apply. The paper's claim that the convergence theorem supports the strong empirical results is therefore overstated — the theory covers a regime that is qualitatively different from the one used in practice. The paper acknowledges this indirectly but frames the mid-range success as an unexplained "hint" rather than addressing the gap.

- **The FL comparison, while reasonable at a high level, lacks sufficient documentation to fully assess fairness.** The paper compares against "DP-SGD-based 1-layer federated learning" but provides no details on the FL algorithm's clipping norm, number of communication rounds, batch size, learning rate schedule, or privacy accounting method. Given that this comparison is central to the paper's claim that BlindAvg "systematically outperforms FL" (especially for many users), the lack of methodological detail undermines confidence. FL values are marked as "interpolated" in Figure 4 without explaining the interpolation procedure. The paper's claim that FL's noise scales with $O(\sqrt{w})$ is a known property, but the actual accuracy gap depends on many implementation choices that are not disclosed.

### Minor

- **The SVM-SGD (Huber loss) experiments use a loss function whose convergence properties differ from the theory, yet this nuance is buried in a figure caption rather than addressed in the main argument.** The paper could have either (a) adopted hinge-loss SVMs in the main experiments to align with theory, or (b) provided a separate analysis (even informal) explaining why the Huber-loss results are expected to behave similarly. As written, a careful reader must independently evaluate which claims apply to which loss function.

- **The non-IID analysis is limited in scope.** The extreme one-class-per-user scenario (Table 2) is informative but artificial. The real-world EMNIST results (Figure 7d) show a notable performance gap between the averaged and global model but lack a comparison to FL for the non-IID setting. A Dirichlet partition of CIFAR-10 (standard in FL literature) would have strengthened the non-IDD evaluation significantly.

- **The extrapolation to 20 million users (Figure 6) is a rough approximation.** The method rescales ε using a linear formula ($\varepsilon' := 1000 \cdot \varepsilon \cdot \Upsilon / n_{\text{users}}$) while assuming accuracy stays constant. The paper acknowledges this is "pessimistic" and "approximate," but the headline number ("87% accuracy for ε=10⁻⁴") could easily be misinterpreted as an empirical measurement rather than a coarse estimate.

### Trivial

- The figure captions contain parser artifacts (garbled text in Figure 5 description) — these are extraction issues in the review copy, not the original submission.

## Nice-to-Haves

- Adding a centralized DP benchmark (DP-SGD on all data combined) would help readers quantify the accuracy gap caused specifically by blind averaging versus the best achievable DP model.
- A theoretical or heuristic explanation for why mid-range Λ works well for blind averaging would substantially strengthen the paper. A Taylor expansion or perturbation argument connecting the mid-range behavior to the high-Λ convergence regime seems attainable.
- Providing the FL hyperparameters (rounds, clipping, sampling rate) in the main paper (or at minimum in the appendix with a pointer) would improve reproducibility.

## Removed Points

- *"The paper does not explain why the gap between averaged and global accuracy shrinks under privacy."* — The paper explains in Section 8 that privacy noise scales with $O(1/\Lambda)$, so mid-range Λ is naturally preferred under DP. This is a reasonable explanation.
- *"SecAgg communication overhead is acknowledged but not included in the comparison with FL."* — The paper's comparison is about the privacy-utility tradeoff, not the communication cost. The non-interactivity claim (single user message) is clearly scoped. This is scope creep.
- *"The paper states 'FL's noise scales with O(√w)' without providing the FL algorithm, hyperparameters, ..."* — The complaint about missing FL hyperparameters is partially a reproducibility nitpick. The broader point about comparison fairness is kept in Major weaknesses.
- *"The paper also contains unsupported extrapolations"* — The extrapolation is explicitly described as approximate and pessimistic, which is proper caveating.
- *"Missing centralized DP benchmark"* — This is a nice-to-have, not a core flaw.
- *Strength Finder generic strengths about "important problem" and "interesting question"* — These add no substance and are dropped.

## Novel Insights

The most novel observation emerging from the reviews is the paper's unusual transparency about its own failure modes. Unlike many papers that present results as uniformly positive, BlindAvg explicitly designs a failure case (SynFail) and identifies the boundary condition (tasks not robust to regularization). Combined with the finding that mid-range Λ works well despite the convergence theory only covering high Λ, the paper suggests an interesting empirical phenomenon: blind averaging may succeed across a broader Λ range than theory predicts, and understanding *why* mid-range averaging works could lead to a more general theory. This tension between the clean but narrow theory and the broader empirical success points to a genuine open problem worth pursuing.

## Suggestions

1. **Align theory and experiments.** Either adopt hinge-loss SVMs in the main privacy experiments (so Theorem 4.3 applies directly), or formally extend the convergence analysis to Huber-loss SVMs. Even a partial result or a perturbation argument would substantially strengthen the paper.
2. **Reframe the contribution.** The paper would be more honest and stronger if it presented the convergence theorem as applying to hinge-loss SVMs under strong regularization (a genuine technical contribution) and the mid-range empirical success as a separate, unexplained but important finding. Currently the framing implies the theory explains the experiments, which it does not.
3. **Document the FL baseline fully.** Add the number of communication rounds, clipping norm, sampling rate, learning rate schedule, and privacy accounting method used. Provide the interpolation procedure for Figure 4. If the appendix already contains these details, add a clear pointer in the main text.
4. **Add a Dirichlet-partition non-IID experiment.** This is a simple addition that would significantly strengthen the non-IID evaluation.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>