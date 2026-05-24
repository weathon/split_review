Now I have a clear picture. Let me write the final consolidated review.

## Summary

2-3 sentence summary of the paper's contribution.

The paper proposes Power Sampling, a training-free inference-time algorithm that uses Metropolis-Hastings MCMC to approximately sample from the power distribution \(p^\alpha\) of a base LLM, motivated by the observation that RL post-training (e.g., GRPO) effectively sharpens the base distribution. The method does not require additional training, curated data, or an external verifier. Experiments across three base models and four benchmarks show that Power Sampling matches or outperforms GRPO on several reasoning tasks (especially out-of-domain), while preserving generation diversity that RL-posttraining collapses.

## Strengths

- **Proposition 1 and Example 1 formally distinguish power sampling from low-temperature sampling (Section 4.1).** The paper proves that low-temperature sampling does NOT sample from \(p^\alpha\) and illustrates the critical difference with a concrete 2-token example. The key insight — that \(p^\alpha\) upweights tokens with few high-likelihood futures while low-temperature sampling upweights tokens with many low-likelihood futures — is both elegant and well-supported. This is a genuine theoretical contribution that clarifies a common misconception.

- **Power sampling matches or beats GRPO on out-of-domain reasoning tasks (Table 1).** On HumanEval (code, out-of-domain for MATH-trained GRPO), Power Sampling achieves 57.3% vs GRPO's 53.7% on Qwen2.5-Math-7B and 62.2% vs 56.1% on Qwen2.5-7B. Similarly on AlpacaEval2.0 (general helpfulness), it outperforms GRPO across all three model families (e.g., Qwen2.5-7B: 8.59 vs 7.62). These results directly support the paper's central claim that training-free sampling can match or exceed RL posttraining on tasks outside the training distribution.

- **Pass@k analysis demonstrates diversity preservation (Figure 5).** Unlike GRPO, whose pass@k performance tapers off for large k (reaching ~0.90 at k=16), Power Sampling's pass@k continues to improve, matching the base model's ~0.98 at k=16 while maintaining higher single-shot accuracy than the base model (0.72 vs 0.50 at k=1). This is a compelling result that addresses a known downside of RL-posttraining (diversity collapse).

- **Generalization to non-verifiable tasks (AlpacaEval2.0).** The method outperforms GRPO on all model families on AlpacaEval2.0, demonstrating applicability beyond domains with an automated verifier — a known limitation of RL-based methods.

- **Consistent gains across three model families.** Results on Qwen2.5-Math-7B, Qwen2.5-7B, and Phi-3.5-mini-instruct show the method is not tied to a single architecture.

## Weaknesses

### Fatal
None.

### Major

- **The GRPO baseline for Phi-3.5-mini-instruct appears to have underperformed or failed to converge, weakening the cross-model comparison (Table 1).** GRPO on Phi-3.5 achieves MATH500 accuracy of 0.406 (barely above the base 0.400) and HumanEval of 0.134 (a 37% *drop* from the base 0.213). The paper states hyperparameters were selected "that avoids training instabilities and converges to improvement," but the results contradict this claim: HumanEval performance is severely degraded, and MATH500 shows no meaningful improvement. While this does not invalidate the Qwen2.5 results (which use standard GRPO hyperparameters from Shao et al., 2025), the paper's claim of "outperforming RL" on Phi-3.5 compares against a demonstrably broken baseline. The authors should either provide training curves showing the GRPO run was successful, or acknowledge the limitation and remove strong comparative claims for Phi-3.5 specifically.

### Minor

- **Algorithm 1 has a typo in the acceptance ratio (line 7).** The algorithm writes \(\pi_k(\mathbf{x}')/\pi_k(\mathbf{x})\) in the acceptance ratio, but the surrounding text (Section 4.3) clearly states the target distribution for this stage is \(\pi_{k+1}\), not \(\pi_k\). The dimension mismatch (sequences of length \((k+1)B\) evaluated under \(\pi_k\), which is defined over length \(kB\)) confirms this is a typo. The intent is clear from context, but the algorithm as printed cannot be directly implemented as-is. This should be corrected to \(\pi_{k+1}\).

- **No measure of statistical reliability.** All main results (Table 1) are reported as point estimates without error bars, confidence intervals, or multiple runs. Given the stochasticity of both the MCMC procedure and autoregressive sampling, it is impossible to assess whether small differences (e.g., GPQA Qwen2.5-Math: 38.9 vs 39.9) are significant. Error bars or standard errors over multiple seeds would substantially strengthen the evaluation.

- **The handling of variable-length sequences (EOS termination) is underspecified.** The paper sets \(T_{\max}=3072\) and notes "termination can happen earlier with an EOS token" (Section 5.1), but the theoretical analysis of the MCMC (Section 4.2) assumes fixed-length sequences. The proposal distribution (uniformly sampling an index from \(\{1, \dots, (k+1)B\}\)) and the acceptance ratio need to account for variable-length sequences. The practical implementation likely handles this correctly (standard practice), but the paper's theoretical guarantees do not extend to the variable-length setting without further justification.

### Trivial
None.

## Nice-to-Haves

- **Computational cost reporting.** The paper provides a token-complexity estimate (\(O(N_{\text{MCMC}} T^2 / B)\)) but reports no actual wall-clock time or total tokens generated. A brief comparison (e.g., "our method uses ~X tokens per response vs Y for a single forward pass") would help readers assess the practical trade-off.
- **Hyperparameter sensitivity analysis.** The choice of \(B=192\), \(\alpha=4.0\), and proposal temperature \(1/\alpha\) is empirically motivated but no ablations are provided. Showing that the method is robust to, e.g., \(\alpha \in \{2, 4, 6\}\) or \(B \in \{128, 192, 256\}\) would strengthen the paper.
- **Ablation on the sequential annealing strategy.** The paper could compare against a plain MH that directly targets \(p^\alpha\) on the full length (without the block-wise construction in Equation 10), to demonstrate that the annealing is necessary for good mixing.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"Variable-length sequences break theoretical guarantees" (harsh critic, #2):** The critic's concern that the proposal probability and acceptance ratio are ill-defined for variable-length sequences is overstated. The paper sets \(T_{\max}=3072\) with EOS-based early termination, which is standard practice. The theoretical guarantees for fixed-length sequences could be extended but this does not invalidate the empirical results. The concern about irreducibility/aperiodicity breaking under variable-length is speculative — standard LLM generation handles this with padding masks and EOS tokens. Downgraded from Critical to Minor (underspecification).
- **"Error in algorithm could prevent implementation" (harsh critic, #1):** The critic frames this as a critical issue that "prevents reproducibility." While the typo exists (\(\pi_k\) → \(\pi_{k+1}\) in line 7 of Algorithm 1), the text description unambiguously clarifies the intent, and using \(\pi_k\) would be dimensionally incoherent (\(\pi_k\) is defined over length \(kB\), while the sequences in question have length \((k+1)B\)). The reproducibility concern is unwarranted. Downgraded from Critical to Minor (typo).
- **"Algorithmic novelty is limited" / "related work missing":** These generic criticisms are not supported by concrete evidence and are removed per the filtering guidelines.
- **"Strength: addresses an important problem"** — generic strength, removed.
- **"Strength: empirical comparison with low-temperature baselines"** — This is a valid supporting point but is subsumed by the stronger concrete strengths already listed.

## Novel Insights

The paper's most insightful finding is arguably not the single-shot accuracy comparison but the **pass@k diversity analysis (Figure 5)**. It demonstrates that MCMC-based sampling from the base model's power distribution achieves RL-level single-shot accuracy *without* sacrificing the diversity that makes multi-sample aggregation effective. This suggests that RL-posttraining's primary benefit for reasoning is not teaching new capabilities but rather sharpening the base distribution — and that this sharpening can be replicated at inference time. The distributional analysis (Figure 4) further supports this: GRPO samples collapse to a narrow high-likelihood peak while Power Sampling retains spread, yet both achieve similar single-shot accuracy. This is a clean empirical argument for the "distribution sharpening" hypothesis in the LLM reasoning literature.

## Suggestions

- Fix the typo in Algorithm 1 line 7 (\(\pi_k\) → \(\pi_{k+1}\)) and add a brief note on how variable-length sequences (EOS) are handled in the MCMC procedure (e.g., uniform index selection over the *actual* sequence length, not the maximum).
- Either provide evidence that the Phi-3.5 GRPO training was successful (training curves, validation performance) or reframe the Phi-3.5 results without comparative claims against GRPO.
- Add variance estimates (standard errors over 3–5 seeds) for the main results in Table 1 and the pass@k curves.
- Add a brief cost analysis: approximate wall-clock time or total generated tokens per response.

## Score and Decision

**Round 1 bracket:** The paper is clearly above the 4.0-level anchors (rejected papers like QAlign and EAGER that had narrower scope or significant derivation errors) and clearly below 8.0-level anchors (exceptional papers). Narrowest plausible range: [5.0, 7.0].

**Round 2 narrowing:** Compared against VFScale (5.5, Accept Poster), which addressed verifier-free test-time scaling for diffusion models but had limited evaluation (only Maze/Sudoku) and heuristic components — the current paper evaluates on standard LLM reasoning benchmarks with stronger theoretical grounding. Compared against Taming Imperfect Process Verifiers (6.5, Accept Poster) which had strong theory but smaller-scale experiments — the current paper has broader empirical validation but a weaker theoretical contribution. The paper is most comparable to GN-IVO (6.0, Accept Poster) in terms of overall quality: clean theoretical motivation, solid experiments across multiple domains, and several addressable weaknesses.

**Calibration anchors consulted (all rounds):**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| Ibx2P7K2Tl | 3.0 | R1 | Weak paper; our paper much stronger |
| ckAQ31T4Qv | 4.0 | R1 | QAlign: MCMC + RM, narrower eval; our paper verifier-free, better eval |
| NRO8xMzCVm | 4.5 | R1 | EAGER: entropy-based branching, simpler method; our paper stronger theory |
| 8ta0xgtsJK | 5.5 | R2 | VFScale: verifier-free diffusion reasoning; our paper is on standard LLM benchmarks |
| eFXmrCun0c | 6.0 | R2 | GN-IVO: comparable quality, both have solid theory + decent eval + addressable issues |
| HsB6CtagP7 | 6.0 | R1 | Time Is a Feature: dLLMs, similar level; our paper has stronger empirical base |
| MFDkLbcydi | 6.5 | R2 | Taming Process Verifiers: stronger theory, narrower experiments |
| qOyF214xmg | 8.0 | R1 | Very strong paper; our paper not at this level |

**Final score:** 6.0 — the paper presents a clever, well-motivated idea with solid theoretical grounding and promising empirical results across multiple models. The two main concerns (Phi-3.5 GRPO baseline quality, lack of error bars) are real but addressable and do not undermine the core contributions demonstrated on Qwen models. The pass@k diversity analysis is particularly compelling.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>