## Summary

This paper identifies and systematically quantifies the "priming vulnerability" in Masked Diffusion Language Models (MDLMs): injecting tokens from a harmful response at an intermediate denoising step can steer generation toward harmful content, even in safety-aligned models. The authors design the anchoring attack to measure this vulnerability, derive a theoretical lower bound (Theorem 4.1) that enables First-Step GCG (a 20× faster, stronger optimization-based attack), and propose Recovery Alignment (RA), a training method that teaches models to generate safe responses from contaminated intermediate states. RA consistently outperforms baselines across three MDLMs, seven attack methods, and three evaluators, while maintaining general capability on 11 benchmarks.

## Strengths

- **Clear demonstration of a novel MDLM-specific vulnerability.** The anchoring attack (Section 4.1) provides a clean, controlled measurement: injecting a single token at step 1 raises ASR from 2% to 21% (LLaDA Instruct), and ASR exceeds 80% by step 16 across all models. This is the first systematic quantification of this vulnerability and goes beyond concurrent qualitative observations (PAD, DiJA).

- **First-Step GCG is practically valuable.** Theorem 4.1 provides a tractable surrogate objective for optimization-based jailbreaks on MDLMs. First-Step GCG achieves 20× speedup and up to 4× higher ASR versus Monte Carlo GCG (Table 1: 58.0% vs 20.0% on LLaDA Instruct), offering both a stronger evaluation tool and validation of the vulnerability analysis.

- **Recovery Alignment shows strong and generalizable safety gains.** RA reduces ASR to near-zero at early intervention steps (Table 2) and, crucially, generalizes to held-out attack types it was not trained on: ASR on PAIR drops from 44.3% to 10.0% (LLaDA Instruct, Table 3), and gains on Crescendo (81.3%→45.0%) are substantial. These improvements cannot be explained by circular training.

- **Thorough evaluation.** Experiments cover three MDLMs, two datasets (JBB-Behaviors, AdvBench), seven attack methods, three evaluators (GPT-4o, LlamaGuard, keyword matching), and 11 general capability benchmarks (Table 4). Results are consistent across all dimensions. The ablation studies (Figure 3) cleanly isolate the contribution of contaminated-state training and linear scheduling.

## Weaknesses

### Fatal
None.

### Major

- **Baseline comparisons are confounded by RA's use of a reward model.** RA uses DeBERTaV3 as a reward model during training, providing dense safety supervision. The baselines (SFT, DPO, MOSA) are trained only on binary preference labels from PKU-SafeRLHF. The ablation "RA w/o inter" — which uses the same reward model but trains from fully masked sequences — already outperforms or matches baselines on several metrics (e.g., Anchoring at t_inter=4 on LLaDA: RA w/o inter 22.0% vs. next best MOSA 24.0%). This suggests that the reward model, not just contaminated-state training, contributes to RA's advantage. The paper acknowledges this limitation (Section 7) but does not provide a DPO-style instantiation that would control for the reward signal. A proper comparison would either give baselines access to the same reward model or implement RA without one.

### Minor

- **The anchoring attack evaluation is partially on the training distribution.** RA's training creates contaminated states via the same procedure as the anchoring attack (injecting the harmful response and masking). The headline results (0% ASR at t_inter=1) are on this attack. However, this concern is substantially mitigated by (a) strong generalization to very different attack types (PAIR, Crescendo, First-Step GCG), and (b) the ablation RA w/o inter, which controls for the training procedure but not the contamination. The paper would be strengthened by training on one contamination strategy and evaluating on a distinct unseen one.

- **Theorem 4.1's empirical validation uses anchoring-attack states rather than forward-process states.** The proof applies the monotonicity assumption inside an expectation over q(r_t|r_T) (the forward process). The empirical validation (Appendix C.2) measures the gap on states from the anchoring attack (prefix injection), not on states drawn from the forward process (random masking). While the assumption is theoretically well-motivated (richer context → higher likelihood) and the empirical results are consistent across models, a direct validation on forward-process states would close this gap more cleanly. The theorem itself is mathematically sound given its assumption.

- **"Affirmative" framing is imprecise for the main attack evaluation.** The paper defines the vulnerability in terms of "affirmative tokens" but the anchoring attack injects tokens from the full harmful response (which may include non-affirmative content). The controlled study in Appendix C.1 does analyze different token types and shows affirmative tokens are particularly effective, but the headline results (Figure 2, Table 2) do not isolate affirmative tokens specifically. The mechanism being demonstrated is broader than the "affirmative" framing suggests.

### Trivial
- The paper's notation for the ELBO (Equation 10) and the proof in Appendix A have minor formatting issues from the PDF extraction (strikethroughs, broken LaTeX) that should be cleaned up.

## Nice-to-Haves
- A DPO-style version of RA without a reward model (acknowledged as future work in Section 7) would resolve the baseline confound and is the most impactful addition.
- Training RA on one contamination pattern and evaluating on a structurally different one would strengthen the generalization claim.
- Adaptive attacks where the adversary knows RA is in use would test robustness under a stronger threat model.
- Characterizing which specific tokens (affirmative vs. harmful vs. neutral) cause the strongest steering across the full benchmark, not just on a single prompt, would sharpen the paper's claims.

## Removed Points

**These points are flagged to be removed; treat them with caution:**

1. **"Theorem 4.1 is unsupported / conflates forward and reverse processes"** — The critic claimed the proof is invalid because it applies a denoising-process assumption to forward-process states. However, the assumption ("log πθ(˜r_{t+1}=r|q, r_t) ≥ log πθ(˜r_1=r|q, r_0) for all t") is a statement about the model's output distribution given *any* state r_t, not about the process that generated r_t. The proof correctly applies it pointwise inside the ELBO expectation. The empirical validation could be extended to forward-process states, but this is a minor completeness issue, not a structural error. **The theorem is mathematically valid; the criticism is misplaced.**

2. **"Theorem 4.1's proof is the entire justification for First-Step GCG"** — The paper explicitly states (Section 4.2) that the empirical success of First-Step GCG is also supported by the observation that "even increasing the generation probability in the first step is sufficient to steer subsequent generations toward a harmful response" (citing Figure 2). The theorem provides theoretical motivation, but the empirical results stand independently.

3. **Various formatting/style nitpicks** from the harsh critic — removed per instructions.

4. **Criticism that RA's evaluation is "circular" (framed as fatal)** — The critic called this "circular evaluation" where "the method is designed to counter the exact attack it was trained on." While partially true for the anchoring attack, the paper evaluates on six other attack types (PAD, DiJA, First-Step GCG, PAIR, ReNeLLM, Crescendo) and shows strong generalization. The critic acknowledged this but still labeled it as central evidence against the paper. This is a minor concern, not a fatal or major one.

## Novel Insights

The most interesting observation emerges from comparing the two concurrent attack types: the anchoring attack (intervening in denoising) and First-Step GCG (optimizing the prompt). The paper shows that even without any intervention in the denoising process, an attacker can exploit the priming vulnerability through prompt optimization alone — and that this attack is actually stronger (58.0% ASR vs. 17.3% for anchoring at t_inter=1 on LLaDA). This suggests the vulnerability is not just about what happens during generation, but about the model's overall sensitivity to harmful content in its input representation, which only manifests during the denoising trajectory. The connection between these two threat models, bridged by Theorem 4.1, is a genuinely insightful framing that goes beyond what concurrent works provide.

## Suggestions

1. **Resolve the reward-model confound.** Implement a DPO-style version of RA that does not use a reward model. This is the single most impactful addition — it would cleanly separate the effect of contaminated-state training from the effect of having a stronger training signal.

2. **Strengthen Theorem 4.1's empirical support.** Validate the monotonicity assumption on states drawn from the forward process (random masking), not just from the anchoring attack (prefix injection). This is a simple experiment that would close the remaining gap.

3. **Train on one contamination strategy, evaluate on another.** For example, train RA on states created by injecting the *first k* tokens of the harmful response (prefix contamination) and evaluate on states created by injecting *random k* tokens. This would demonstrate that RA learns a general recovery capability rather than a specific pattern.

4. **Sharpen the definition.** Either broaden the definition of the priming vulnerability to cover any tokens from a harmful response (not just affirmative ones), or provide evidence that the injected tokens in the Anchoring Attack are predominantly affirmative at small t_inter.

5. **Add a discussion of adaptive attacks.** Since RA is a known defense, what happens when the attacker optimizes a suffix to inject tokens at late steps (e.g., t_inter > 32) where RA's effectiveness is reduced? This would clarify the method's limitations under a realistic threat model.

## Score and Decision

### Calibration Anchors

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/rIPeatvPy3.md` (DiJA paper) | 5.00 | Concurrent attack-only paper; this paper is stronger due to both attack and defense analysis, more thorough evaluation, and generalization results |
| `/home/wg25r/review_agent/human_reviews_2026/zBPzxhso8M.md` (DiffuGuard) | 5.20 | Similar scope (analysis + defense); this paper has stronger empirical results and a more principled defense framework |
| `/home/wg25r/review_agent/human_reviews_2026/jKQQb8uClw.md` (From Vulnerability to Defense) | 3.00 | Weaker paper with flawed theoretical proofs; this paper is substantially stronger in both theory and experiments |
| `/home/wg25r/review_agent/human_reviews_2026/UQK3tUsouK.md` (Jailbreak Transferability) | 6.50 | Cleaner causal methodology and broader scope; this paper has more applied contributions but is less clean methodologically |
| `/home/wg25r/review_agent/human_reviews_2026/akbtPEZnDZ.md` (Self-Jailbreaking) | 5.50 | Similar tier — both identify novel vulnerabilities and propose mitigations with thorough evaluation |
| `/home/wg25r/review_agent/human_reviews_2026/4YgvVRoSnF.md` (JailbreakLoRA) | 4.00 | More limited evaluation; this paper is stronger |

The paper makes genuine contributions: identifying and quantifying a novel MDLM-specific vulnerability, deriving a tractable attack via Theorem 4.1, and proposing an effective defense with strong generalization evidence. The main concerns — the reward-model confound in baselines and partial circularity in the anchoring attack evaluation — are real but addressable and do not undermine the paper's central claims. The generalization results on PAIR, Crescendo, and First-Step GCG are particularly compelling. Relative to the calibration anchors, this paper sits above the 5.00 DiJA paper and the 5.20 DiffuGuard paper in terms of contribution depth, but below the 6.50 Jailbreak Transferability paper in methodological rigor. A score of 5.5 reflects this positioning.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>