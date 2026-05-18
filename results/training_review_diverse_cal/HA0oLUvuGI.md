Good. I've now verified all claims against the paper. Let me write the final consolidated review.

---

## Summary

This paper proposes Energy-Weighted Flow Matching (EFM) and Energy-Weighted Diffusion (ED), methods that learn energy-guided generative models by reweighting the standard training loss with importance weights \(\exp(-\beta\mathcal{E}(\mathbf{x}_0))\). The key advantage over prior work (CEP, Lu et al. 2023; Force-Field Guidance, Wang et al. 2024) is that the approach eliminates the need to learn an intermediate energy function or its gradient. The framework is applied to offline RL via Q-weighted Iterative Policy Optimization (QIPO), achieving competitive results on D4RL benchmarks and faster sampling than the comparable QGPO method.

## Strengths

- **Clean mathematical framework that removes unnecessary complexity.** Theorem 4.3 establishes that minimizing the conditional energy-weighted flow matching loss \(\mathcal{L}_{\mathrm{CEFM}}\) is equivalent to minimizing the energy-weighted flow matching loss \(\mathcal{L}_{\mathrm{EFM}}\). This means the guided flow can be learned without estimating the intermediate energy function \(\mathcal{E}_t(\mathbf{x})\) or its gradient, which prior methods required. Algorithm 1 shows the practical implementation is nearly identical to standard DDPM — the only addition is a softmax-weighting step over the batch.

- **Competitive empirical results on D4RL benchmarks.** Table 2 reports that both QIPO-OT (flow matching) and QIPO-Diff (diffusion) achieve scores that are at or near the top across multiple D4RL tasks, compared against strong baselines including QGPO, Guided Flows, Diffusion-QL, IDQL, and SRPO. Results are reported as mean ± standard deviation across 8 random seeds.

- **Faster action generation than prior energy-guided methods.** Table 3 shows that QIPO reduces action generation time by 19–33% relative to QGPO (e.g., halfcheetah-medium-expert: 112 ms vs. 166 ms). This speedup is a direct consequence of avoiding backpropagation through an intermediate energy model.

- **Exact characterization of guidance properties.** Lemma 4.10 and Lemma 4.11 provide a mathematically precise comparison between energy-guided diffusion and classifier-free guidance, showing that energy guidance (and CEP) achieve exact generation of \(p(\mathbf{x})p^\beta(c|\mathbf{x})\) for all \(\beta\), while CFG deviates when \(\beta \neq 1\). This analysis is correct and useful for understanding the trade-offs between guidance paradigms.

- **Transparency about the importance sampling connection.** The paper explicitly acknowledges in Remark 4.6 that \(\mathcal{L}_{\mathrm{CEFM}}\) can be interpreted through importance sampling, deriving the equivalence between weighted training and training on samples from the target distribution. This intellectual honesty is commendable.

## Weaknesses

### Fatal

None.

### Major

1. **The core contribution is more incremental than the claims suggest.** The central technique — reweighting training samples by \(\exp(-\beta\mathcal{E}(\mathbf{x}_0))\) to learn a tilted distribution — is a well-understood application of importance sampling. The paper itself acknowledges this (Remark 4.6). What distinguishes the work is (a) formalizing this for flow matching (not just diffusion), (b) showing it bypasses the need for intermediate energy models, and (c) demonstrating it in offline RL. These are genuine but incremental contributions. The paper's framing as "the first exact energy-guided flow matching model" and "the first energy-guided diffusion model that operates independently of auxiliary models" overstates the conceptual novelty. A more measured framing — presenting the work as a systematic application of importance-sampled weighted training to flow matching/diffusion for energy-guided generation, with theoretical and empirical validation — would better reflect the actual contribution.

### Minor

2. **The QIPO iterative renewal scheme lacks convergence analysis.** The paper derives (Equation 5.4) that iterative regeneration of support actions yields policies \(\pi_{l+1} \propto \mu \exp((l+1)\beta Q)\), which effectively increases the guidance scale. However, no analysis is provided of whether this process converges, under what conditions, or how the renewal frequency \(K_{\text{renew}}\) affects the result. While this level of analysis is common for empirical RL algorithms, the paper does make theoretical claims about the policy form, and the lack of convergence guarantees weakens those claims.

3. **The "without auxiliary models" framing is imprecise in the RL context.** The paper repeatedly claims the method operates "independently of auxiliary models" (abstract, Table 1, conclusion). The relevant savings is over methods that require an *intermediate energy function* model (e.g., CEP's \(\mathcal{E}_t\) or Wang et al.'s force-field network). In the offline RL application, QIPO still requires a learned Q-function — which is itself a neural network. The claim would be clearer if phrased as "without requiring an auxiliary model for the intermediate energy/guidance," since the Q-function is part of the RL problem rather than the generative framework.

4. **No comparison against a one-step (non-iterative) weighted diffusion baseline.** The paper does not isolate the effect of the weighted loss from the iterative renewal scheme. A baseline that applies the weighted loss *without* iterative regeneration (i.e., using the fixed behavioral policy for support actions throughout) would directly show whether the gains come from the exact energy-weighting or from the iterative procedure. Without this ablation, the attribution of improvement is unclear.

5. **Variance of the importance weights is not discussed.** The weights \(\exp(\beta Q(\mathbf{x},\mathbf{a}))\) can have high variance, especially in high-dimensional action spaces or with large \(\beta\). The paper uses softmax normalization over the batch, which biases the empirical estimate by batch composition. Neither the bias nor the variance from this approximation is analyzed, and no practical guidelines about batch size are provided. This is relevant for practical reliability.

### Trivial

6. **Running time comparison is narrowly scoped.** Table 3 reports "action generation" time, which is a valid metric for sampling efficiency. However, the total time budget — including Q-function training, behavioral policy warm-up, and policy improvement — would provide a more complete picture of the method's computational cost.

## Nice-to-Haves

- An ablation comparing one-step weighted diffusion (without iterative renewal) against QIPO, to isolate the effect of the loss from the effect of the iterative procedure.
- Analysis or practical guidance on the variance of importance weights and the sensitivity to batch size.
- Statistical significance tests or confidence intervals across the 8 seeds to quantify which improvements are meaningful.
- Clarification of how the sensitivity to the initial behavioral policy quality affects QIPO's performance.

## Removed Points

These points were raised by reviewers but are removed for the reasons stated. They should be treated with caution.

- **"The comparison with CFG in Section 4.3 conflates different problem settings and overemphasizes a known limitation."** — REMOVED. The mathematical comparison in Section 4.3 is correct and relevant. The paper correctly identifies that energy-guided diffusion achieves exact guidance for \(\beta \neq 1\) while CFG does not, which is a genuine theoretical advantage. This is not a strawman; it is a precise characterization of the methods' properties. The comparison is directly relevant because the paper evaluates against Guided Flows (Zheng et al., 2023), a CFG-based method, in the experiments.

- **"The paper does not report standard errors."** — REMOVED. The paper explicitly states in the Table 2 caption: "We report mean ± standard deviation of algorithm performance across 8 random seeds." Standard deviations are reported. The reviewer's claim is factually incorrect.

- **"Ablation results are referenced but not shown."** — REMOVED. The superscript "3" on the ablation sentence points to an appendix. Per policy, the parser strips appendices from all papers; these exist in the original submission and the paper cannot be faulted for content removed by parsing.

- **"The paper does not discuss the effect of the recomputation of the normalizing constant Z."** — This is already partially discussed in Algorithm 1's description (line 205) where the paper states the denominator is approximated by the empirical batch average. The concern about small batch sizes is valid but minor; moved to Weaknesses Minor as a variance concern (point 5).

## Novel Insights

None beyond the paper's own contributions. The most interesting observation from the reviews is the tension between the paper's theoretical contribution (clean mathematical framework for weighted training) and the practical algorithm (QIPO with iterative renewal, which is less theoretically grounded). The paper's strongest contribution is in the former, but its empirical claims rest on the latter — an asymmetry that future work could resolve by separating these two components more cleanly.

## Suggestions

1. Reframe the contribution more precisely: present the work as showing that importance-sampled weighted training for flow matching/diffusion yields a simpler and more direct approach to energy-guided generation than methods requiring intermediate energy models. Remove or soften "first" claims.

2. Add an ablation comparing one-step weighted diffusion (without iterative renewal) against full QIPO, to disentangle the effect of the weighted loss from the effect of iterative regeneration.

3. Add a brief discussion of weight variance: comment on how the softmax batch normalization affects the gradient estimator, and provide practical guidance on batch size selection.

4. Clarify the "without auxiliary models" language throughout to specify that the method avoids an *intermediate energy function* model, which is the relevant comparison to CEP and force-field guidance.

---

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>