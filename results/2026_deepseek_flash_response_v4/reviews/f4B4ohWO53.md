## Summary

The paper proposes NVDP (Nonparametric Variational Differential Privacy), which integrates a Nonparametric Variational Information Bottleneck (NVIB) layer into a transformer to learn noisy posterior distributions over multi-vector embeddings. At test time, samples from this posterior are shared as sanitized embeddings. Privacy is quantified via a closed-form Rényi divergence upper bound (Equation 7) and converted to Bayesian Differential Privacy (BDP) values. Experiments on GLUE show NVDP outperforms a VIB-based ablation (VTDP) on most tasks in both accuracy and measured BDP.

## Strengths

1. **Closed-form Rényi divergence upper bound (Equation 7).** Deriving a tractable bound on the Rényi divergence between the sampling distributions of two Dirichlet Process posteriors is a non-trivial technical contribution that bridges NVIB's Bayesian nonparametric framework with privacy quantification for multi-vector embeddings.

2. **Empirical demonstration that NVDP dominates VTDP (Table 1).** On 5/6 GLUE tasks, NVDP achieves higher accuracy *and* better (lower) BDP than the VIB-based ablation (e.g., MRPC: 83.0% accuracy with BDP 10.70 vs. VTDP 81.1% with BDP 11.50). This provides concrete evidence that the nonparametric component improves the privacy-utility tradeoff.

3. **Motivated architectural design (removing the residual skip connection, Section 3.1).** The paper correctly identifies that standard residual connections would allow un-sanitized information to bypass the noisy latent bottleneck and removes them accordingly — a subtle but necessary design choice.

## Weaknesses

### Major

1. **Training leakage is not addressed — the mechanism itself is learned from private data without DP guarantees.** The NVIB posterior parameters (projection weights, mappings from input embeddings to posterior parameters) are trained via gradient descent on the same data they are later used to sanitize. No gradient clipping, gradient noise, or DP accountant is applied during training. An adversary with access to the trained mechanism (which they would have, since it generates the shared embeddings) could potentially extract information about training examples from the model weights. The paper's privacy analysis only considers distinguishability of test-time samples *given a fixed mechanism* — it does not account for the information leakage from learning that mechanism from private data. In standard local DP, the randomized mechanism must be fixed before it sees any data, or the entire training process must itself satisfy DP. The paper satisfies neither condition. This is the most serious issue and undermines the central claim of providing differential privacy. *(Verifiable: no mention of DP training, clipping, or noise in the training procedure; the architecture described in Section 3.1 and experimental setup in Section 4 describe standard non-DP fine-tuning.)*

2. **The privacy "guarantee" is an empirical measurement on a finite set of test-set pairs, not a formal DP bound.** The paper states (line 182): "we fix the Rényi order to λ = 1.1 and report the worst-case divergence across all test set pairs." A true differential privacy guarantee requires proving the bound holds for *all* possible adjacent inputs. Evaluating the bound on a finite test set — even taking the worst case — does not constitute such a proof. The paper repeatedly uses language like "provides differential privacy" (abstract, introduction), "privacy guarantees" (conclusion), and "strong privacy protection" (abstract) for what is actually an empirical divergence measurement. *(Verifiable: Section 4, line 182; comparing the language in the abstract/contributions against the actual experimental protocol.)*

3. **No comparison against any standard differentially private method.** The only privacy-related baseline is the self-constructed VTDP ablation. There is no comparison against DP-SGD (Abadi et al., 2016) applied to BERT fine-tuning, no Laplace/Gaussian mechanism applied directly to the embeddings, and no comparison against prior work on privacy-preserving NLP. Without such comparisons, it is impossible to assess whether NVDP's privacy-utility tradeoff is competitive with established DP methods. A paper claiming to "provide differential privacy" should benchmark against other methods that provide differential privacy. *(Verifiable: Section 4 lists only "Base," "+REG," and "VTDP" as comparators.)*

### Minor

4. **"Best of 5 runs" reporting without variance estimates.** The experimental protocol (line 182) selects the best-performing run on the validation set from five independent runs. This inflates reported accuracy. Without mean and standard deviation, it is unclear whether differences of ≤1 percentage point (e.g., MRPC 83.0 vs. +REG 82.4; STS-B 85.2 vs. +REG 85.7; SST-2 91.7 vs. VTDP 92.3) are meaningful or within the noise of the selection procedure.

5. **BDP values of 10–22 are high; the claim of "strong privacy guarantees" (line 206) is overstated.** Even under the relaxed BDP framework, ε_μ values of 10–22 do not constitute strong privacy protection by typical DP standards. The paper should either calibrate its claims or provide context for what these values mean in practice.

6. **Contradiction in Figure 2 caption.** The image caption states: "The x-axis values for VTDP are generally lower than for NVDP, indicating stronger privacy guarantees" (line 194). But Table 1 shows NVDP has *lower* (better) BDP than VTDP on most tasks (e.g., MRPC: 10.70 vs. 11.50; QNLI: 12.10 vs. 16.90). The text caption (line 196) says the opposite — that NVDP "consistently achieves better privacy-utility points than the VTDP ablation." These two captions directly contradict each other, making the figure difficult to interpret.

### Trivial

None.

## Nice-to-Haves

- Empirical evaluation against actual adversarial attacks (e.g., embedding inversion, reconstruction) would directly validate practical privacy benefit, going beyond measuring divergence.
- Discussion of how the weighted-set-of-vectors output format (mixture components) would be consumed by downstream models in practice.
- Hyperparameter sensitivity analysis for λ_D and λ_G.

## Removed Points

These points from the inputs were removed with justification:

- **Criticism about missing appendix content:** The parser strips appendices; they exist in the original submission.
- **Criticism about speculative tightness of the RD bound:** The paper transparently acknowledges its approximations and leaves tighter bounds to future work. This is an honest scope limitation, not a flaw.
- **Criticism about BDP being a "non-standard" framework:** BDP (Triastcyn & Faltings, 2020) is a published privacy framework; the paper explicitly builds on it and is transparent about this choice.
- **Strength about "evaluation using two complementary privacy measures":** Diminished by the fact that both measures are computed empirically on test-set pairs rather than proven formally. Not kept as a genuine strength.
- **Several generic strengths from the Strength Finder (e.g., "the paper addresses an important problem"):** These lack specific, evidence-backed content and were removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The key tension — that the paper's core technical contribution (learned stochastic embeddings via NVIB) is genuinely interesting but its framing as a differentially private mechanism is unsupported — is well articulated in the harsh critic's analysis and confirmed by reading the paper.

## Suggestions

1. **Reframe the contribution.** The NVIB-based learned stochastic embedding is a legitimate technical contribution, but it does not provide differential privacy in the formal sense. Reframing as "information-theoretic regularization for limiting empirical information leakage" or "stochastic embeddings with quantifiable Rényi divergence" would align the paper's claims with what it actually demonstrates.

2. **Address training leakage.** If the mechanism is to provide DP, the authors must either: (a) train the NVIB parameters on public data and apply to private data, or (b) make the training DP (e.g., via DP-SGD) and account for the combined privacy budget across training and inference.

3. **Add standard DP baselines.** Compare against DP-SGD applied to BERT fine-tuning and a Gaussian mechanism applied directly to embeddings, even if only for a subset of tasks.

4. **Report mean and standard deviation across runs.** Standard reporting practices for GLUE.

5. **Resolve the Figure 2 caption contradiction.** The two captions (lines 194 and 196) say opposite things.

## Calibration Anchors

Anchor papers retrieved across all rounds:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| TbOcySs6g8 | 2.50 | R1 bracketing | DP synthetic data with no embedding component — less relevant, weaker paper |
| FNCFiXKYoq | 3.00 | R1 bracketing | Fairness + DP on tabular data — different domain, weaker contribution |
| i8ynYkfoRg | 3.00 | R1 bracketing | FL privacy via model entanglement — less relevant |
| sruGNQHd7t | 3.00 | R1 bracketing | Domain shifting for DL queries — less relevant |
| vxmvbzw76R | **4.75** | R1 bracketing | **Most relevant anchor.** LDP for LLM embeddings (Split-and-Denoise). Similar setting (embedding privacy), similar issues (loose ε values, no empirical attack evaluation). This paper has a slightly worse privacy analysis (ε up to 1000) but uses standard LDP. NVDP is comparably positioned — slightly more principled analysis but worse DP framing. **NVDP ≈ this anchor.** |
| fGSEWgRHNZ | **4.75** | R1 bracketing | AdaPMixED — private next-token prediction. Analogous theoretical gap (data-dependent privacy loss treated as comparable to formal DP). AdaPMixED at least uses standard DP mechanisms. **NVDP is slightly weaker.** |
| 3uITarEQ7p | 5.50 | R1 bracketing | DP model compression with proper DP-SGD — stronger privacy framework. NVDP is weaker. |
| DF5TVzpTW0 | **6.00** | R1 bracketing | DPPN — embedding inversion defense. More thorough evaluation (6 datasets, actual attacks). Similar lack of formal DP. Better empirical work. **NVDP is weaker.** |
| i2Ul8WIQm7 | 5.80 | R1 bracketing | Evaluating privacy risks of PEFT — different contribution type |
| 2cF3f9t31y | 6.50 | R1 bracketing | Private data selection over MPC — well-executed, accepted. NVDP is weaker. |
| F52tAK5Gbg | 4.00 | R2 narrowing | DP-SGD for non-decomposable objectives — narrower but proper DP. |
| ZhY1XSYqO4 | 5.25 | R2 narrowing | Deep Variational MIB — VIB theory, no privacy. Different topic. |
| jGuXGNcK6O | 5.40 | R2 narrowing | Theoretical limits of least-privilege learning — theoretical, different. |
| YEhQs8POIo | 6.25 | R2 narrowing | DP synthetic data via APIs — proper DP framework, accepted. |

**Round 1 bracket:** [3.5, 6.5] — the paper is clearly above the weak-anchor band (~3.0) and clearly below the strong-anchor band (≥7.5). The middle band contains several relevant anchors between 4.75 and 6.00.

**Round 2 narrowing:** The paper sits closest to the 4.75 anchors (Split-and-Denoise, AdaPMixED). It is weaker than DPPN (6.00) which has a more thorough empirical evaluation. It is slightly weaker than AdaPMixED (4.75) because AdaPMixED at least uses formal DP mechanisms. It is comparable to Split-and-Denoise (4.75) — both claim DP for embeddings with significant gaps in their privacy analysis.

**Final score:** 4.5. The paper has genuine technical novelty (NVIB integration for learned stochastic embeddings, analytical RD bound) but the central claim of providing differential privacy is not adequately supported due to (a) unaddressed training leakage, (b) empirical rather than formal DP guarantees, and (c) absence of standard DP baselines.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>