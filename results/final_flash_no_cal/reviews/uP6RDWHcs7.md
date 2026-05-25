I have now thoroughly read the paper and cross-checked the reviewer claims against the actual paper content. Here is the consolidated final review.

---

## Summary

Marginal Flow proposes a density estimation framework where the model is defined as a mixture \(q_\theta(x)=\frac{1}{N_c}\sum_i q(x|w_i)\) whose component parameters \(w_i\) are not fixed but resampled from a learnable distribution \(q_\theta(w)\), which itself is parameterized by an unconstrained neural network. This design avoids the bijection constraint of normalizing flows, enables efficient single-step sampling together with tractable density evaluation, supports lower-dimensional manifold learning, and works with multiple training objectives (forward and reverse KL). Experiments on synthetic data, simulation-based inference, Wishart-distributed matrices, and image latent spaces demonstrate the framework's flexibility and substantial computational speedups over normalizing flows, flow matching, and free-form flows.

## Strengths

- **Novel and flexible framework.** The idea of learning a distribution over mixture-component parameters via a neural network, rather than optimizing the components directly, is creative. It cleanly decouples model capacity from the number of components \(N_c\) (Eq. 2, Figure 1) and allows the practitioner to change \(q(x|w)\) to match the data type (Gaussian, Wishart, Dirichlet) without modifying the framework's structure (Section 2.3, Section 4.3).

- **Impressive computational efficiency.** Figure 3 shows Marginal Flow is orders of magnitude faster than normalizing flows, flow matching, and free-form flows for both sampling and density evaluation across dimensions \(10^2\)–\(10^5\), scaling where others run out of memory. Figure 7 shows it reaches a given test log-likelihood in seconds compared to hundreds of seconds for competing models. This is a clear and practically important advantage.

- **Flexible manifold learning.** By choosing a base distribution of dimension \(m<d\), Marginal Flow can learn densities concentrated near a lower-dimensional manifold. Figure 4 (spiral) demonstrates this qualitatively, and Section 4.4 extends it to 1-D manifolds in VAE latent spaces for MNIST and JAFFE, producing interpretable traversals (Figures 10‑11).

- **Works with multiple training objectives.** Because Marginal Flow supports both efficient sampling and efficient density evaluation, it can be trained with reverse KL divergence (Figure 8) in addition to standard maximum likelihood. Section 4.1 shows it outperforms normalizing flows in reverse-KL training on 2D synthetic targets.

- **Diverse experimental validation.** Experiments cover 2D synthetic benchmarks, simulation-based inference (deferred to appendix), positive-definite matrix distributions via Wishart mixtures (Section 4.3), and conditional manifold learning in image latent spaces (Section 4.4). The Wishart experiment in particular demonstrates an application where normalizing flows are computationally prohibitive (\(100\times100\) matrices, \(d=5050\)).

## Weaknesses

### Fatal

None.

### Major

1. **The "exact likelihood" framing is imprecise and conflates two different notions of exactness.**  
   The model is defined as \(q_\theta(x) := \frac{1}{N_c}\sum_{i=1}^{N_c} q(x|w_{\theta,i})\) where \(w_{\theta,i}\sim q_\theta(w)\) (Eq. 2). The paper repeatedly calls this "exact density evaluation" (abstract, Section 2.2, Table 1, conclusions), placing a checkmark for "Efficient exact likelihood" in Table 1 on par with normalizing flows. In practice, however, the \(w_i\) are *resampled* for each evaluation, so the density value is a random variable whose expectation is the marginal in Eq. 1. Evaluating the same \(x\) with a different seed or a different \(N_c\) yields a different value. This is qualitatively different from a normalizing flow, where the learned density is a fixed deterministic function.  
   - **Table 1** compares apples to oranges: NF's exact likelihood is deterministic; MF's involves Monte Carlo randomness.  
   - **Figure 3** labels the runtime comparison "exact density evaluation" without acknowledging that MF computes an estimate whose quality depends on \(N_c\) and whose variance is uncharacterized.  
   - The abstract states "exact density evaluation by construction," which is misleading for the only model that can be evaluated in practice (Eq. 2 with finite \(N_c\)).  
   *This does not invalidate the framework — the model in Eq. 2 is well-defined and its evaluation for a given set of \(w_i\) is exact closed-form arithmetic. But the paper needs to honestly characterize the nature of the evaluation as a tractable unbiased Monte Carlo estimate of an intractable marginal, and compare against alternatives on those terms.*

2. **Complete absence of \(N_c\) analysis and variance characterization.**  
   \(N_c\) (the number of sampled component parameters) controls the bias-variance tradeoff of the density estimator, the fidelity of the learned marginal, and the computational cost. The paper states that \(N_c\) "is not required to be fixed" but provides:
   - No study of how \(N_c\) affects the quality of the learned density or test log-likelihood.
   - No analysis of the variance of the density estimate or of test NLL across different seeds.
   - No guidance on choosing \(N_c\) in practice.
   - No specification of what \(N_c\) was used in any experiment (runtime comparison in Figure 3, synthetic experiments, etc.)
   Without this, a reader cannot assess the practical utility of the model. The runtime comparison in Figure 3 is especially hard to interpret without knowing the \(N_c\) used: a runtime advantage might partially reflect a noisy, low-\(N_c\) estimate rather than a genuine superiority. The paper should provide an \(N_c\) ablation and an iso-accuracy runtime comparison that controls for the variance of the density estimate.

3. **Simulation-based inference results — a flagship benchmark — are entirely deferred to the appendix with no summary in the main text.**  
   Section 4.2 states: "Due to space constraints we report results in the Appendix in Figure 14. Marginal Flow achieves state-of-the-art results." The main text contains no numbers, no comparison table, and no summary statistics. Given that SBI is a challenging real-world application where density estimation is directly useful, this deferral substantially weakens the evidential support for the paper's claimed practical advantages. Even a short table or a single C2ST score in the main text would dramatically strengthen the paper.

### Minor

1. **Image manifold experiments are entirely qualitative.** The MNIST and JAFFE results (Section 4.4, Figures 10‑11) show that a 1-D manifold can be fit and traversed, producing smooth interpolations. However, no quantitative metric is reported (FID, coverage, reconstruction loss, or any disentanglement score). The evaluation is not commensurate with the strength of the claims. Adding quantitative metrics would turn a nice visualization into a legitimate result.

2. **The runtime comparison (Figure 3) does not specify the \(N_c\) used.** The caption and surrounding text say "For further details, see the Appendix in Section A.3.1." Without \(N_c\) in the main text, the plot is difficult to interpret — a larger \(N_c\) would increase MF's runtime. This should be stated up front.

3. **The manifold learning claim is imprecisely phrased.** Section 2.3 says Marginal Flow "allows for learning a lower-dimensional manifold alongside the density." Since \(q(x|w)\) uses a Gaussian with \(\sigma>0\) (spherical noise), the model assigns positive density everywhere in \(\mathbb{R}^d\) — it does not learn a *degenerate* distribution on a manifold, but rather a density concentrated near one. This is a common and defensible relaxation of the manifold hypothesis, but the phrasing should be precise (e.g., "learns a distribution concentrated near a lower-dimensional manifold").

4. **No protocol stated for test-set NLL evaluation.** The paper is silent on how test log-likelihood is computed: should the practitioner re-sample \(w_i\) for each test point? Resample once for the whole set? Report the mean over several resamplings? This matters for reproducibility and for interpreting the reported numbers.

5. **The claimed advantage of "marginalization" vs. the neural-network parameterization could be clarified.** Figure 1 compares Marginal Flow against a standard GMM with fixed optimized centers. But the core innovation is not marginalization *per se* — a GMM whose means were resampled from a learned distribution would behave similarly. The key advance is that \(q_\theta(w)\) is parameterized by a neural network (Eq. 3), which enables flexible, scalable learning of the component distribution. The paper would benefit from making this distinction explicit.

### Trivial

- Table 1's "Efficient exact likelihood" row should use a qualified entry (e.g., "Tractable (unbiased estimate)") or a footnote clarifying the nature of the evaluation.  
- Figure 7 would be strengthened by reporting final converged test log-likelihood values for all models, to distinguish "converges faster to a better model" from "converges faster because it's hitting a worse local optimum."

## Nice-to-Haves

- **Comparison against a standard GMM with a large number of components** (trained via EM or SGD) would directly isolate the benefit of the neural-network parameterization of \(q_\theta(w)\) over a fixed-set mixture.  
- **Better baselines for the image experiments** — e.g., a standard VAE prior or a normalizing flow in latent space — would contextualize the manifold learning results.  
- **A clear statement on how to evaluate NLL on a test set** (re-sample once? multiple times and average?) should be included.  
- The paper could **embrace the Monte Carlo nature** of the model more explicitly, comparing against importance-weighted VAEs or other MC-based density estimators rather than treating MC randomness as a liability.

## Removed Points

The following points from the inputs were removed with justification:

- **"Figure 3 conflates cost of an estimate with cost of truth — plot is uninterpretable"** — Demoted from Fatal to Major because the runtime advantage is directionally clear even without the \(N_c\) specification, but the missing \(N_c\) is a genuine weakness (merged into Major weakness 2).  
- **"A standard GMM with large N_c also provides exact mixture density"** — Moved to Nice-to-Haves; this is a useful comparison but not a required baseline for the paper's core claim.  
- **"GANs and VAEs cannot be trained with reverse KL due to lack of exact density"** — The paper's own claim about reverse-KL viability is correct and the strength is kept; the criticism that this is "not possible" with GANs/VAEs is a factual statement about those model classes, not a weakness of MF.  
- **"Section 2.2 omits the cost of summing over N_c components"** — The paper does mention evaluating each \(q(x|w_i)\) (line 143); the cost is implicit in the definition. Demoted from minor complaint to a note within the existing runtime weakness.  
- **"Missing related works"** — Removed per instructions (cannot verify existence of external sources).  
- **Formatting/typo nitpicks** — Removed per instructions (parser artifacts).  
- **Criticism questioning existence of cited benchmarks or tools** — None present in the inputs.

## Novel Insights

The most interesting cross-cutting observation from the reviews is that **the fundamental tradeoff of Marginal Flow is different from what the paper emphasizes**. The paper presents "exact density evaluation" as a headline advantage, but the real novelty lies elsewhere: (1) the framework replaces the fixed parameter set of a mixture model with a learned distribution over parameters, effectively decoupling capacity from component count; (2) it provides an *unbiased estimate* of an intractable marginal rather than a deterministic exact density — a distinction that the paper should embrace rather than obscure. This changes how the method should be positioned relative to competitors: its natural competitors are not just normalizing flows (exact but constrained) but also other MC-based density estimators (importance-weighted VAEs, Bayesian nonparametric mixtures). The runtime advantage (Figures 3 and 7) is genuine and important regardless of how "exact" is defined.

## Suggestions

1. **Re-frame the core claim.** Replace "exact density evaluation" throughout with "tractable density evaluation (unbiased Monte Carlo estimate)" or "closed-form evaluation for each parameter draw." Update Table 1 accordingly with a qualifier in the "Efficient exact likelihood" row and a footnote explaining the stochastic nature of the evaluation.

2. **Add an \(N_c\) ablation study** showing how test NLL, variance of the density estimate, and runtime scale with \(N_c\). Demonstrate that beyond a modest \(N_c\) the variance is negligible relative to model capacity or baseline differences. This is the single most important missing experiment.

3. **Bring SBI results (or at least a summary table) into the main text.** Even a single sentence reporting C2ST scores for the best-performing methods would make the "state-of-the-art" claim credible.

4. **Add quantitative metrics to the image experiments** — e.g., reconstruction FID or NLL in the VAE latent space for MNIST, or a linear probe evaluating emotion disentanglement for JAFFE.

5. **Specify the \(N_c\) value used in every experiment** (including Figure 3) directly in the main text or figure captions, not only in the appendix.

6. **Clarify the test NLL evaluation protocol** — state whether the authors re-sample \(w_i\) per test point or use a fixed set, and whether reported numbers are means over multiple seeds.

---

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>