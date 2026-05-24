Now I have all the information I need. Let me synthesize the final review, carefully filtering the harsh critic's points against the paper.

---

## Summary

QZO proposes a method for memory-efficient fine-tuning of quantized LLMs by applying zeroth-order optimization to the continuous quantization *scale* parameters rather than the discrete quantized weights. This bypasses the fundamental incompatibility between ZO's continuous perturbations and discrete quantized weights. A directional derivative clipping (DDC) technique stabilizes training. Evaluated across OPT, Llama-2, and Llama-3.1 models quantized with GPTQ (4-bit) and AQLM (2-bit) on five NLP benchmarks, QZO reduces total memory by over 18× compared to 16-bit AdamW fine-tuning and ~3× compared to MeZO, while often matching or exceeding MeZO's accuracy.

## Strengths

- **Novel perturbation mechanism (Q-SPSA):** Perturbing quantization scales rather than discrete weights (Section 3.2.1, Eq. 5) is a genuinely clever insight that enables ZO on post-training quantized models for the first time. This is the paper's strongest contribution and is clearly distinct from prior ZO + quantization work (e.g., ZO-signSGD based approaches that require noise quantization and re-quantization).

- **Strong and diverse empirical validation:** QZO is evaluated on three model families (OPT-6.7B, Llama-2-7B, Llama-3.1-8B, plus Llama-2-13B at 2-bit), five NLP benchmarks (SST-2, RTE, CB, BoolQ, SQuAD), and two PTQ paradigms — scalar-based GPTQ (4-bit) and codebook-based AQLM (2-bit) (Tables 1, 3). The method consistently improves over quantized zero-shot baselines and often matches MeZO with a fraction of the memory.

- **Practical stabilization via DDC:** Training without DDC collapses to NaN within ~22 steps (Figure 2); with DDC, training is stable across a wide range of clipping thresholds (Figure 3). The effectiveness is unambiguous.

- **Dramatic resource reduction:** QZO uses only ~1% of MeZO's trainable parameters and FLOPs (Table 2), and enables fine-tuning Llama-2-13B on a single 24GB GPU — a genuinely practical result for resource-constrained settings.

## Weaknesses

### Fatal

None.

### Major

- **Theorem 1 (unbiasedness of the clipped estimator) is unsubstantiated in the main text.** The paper claims that the clipped gradient estimate $\hat{\nabla}_{\Delta} \mathcal{L}'$ is an unbiased estimate of $\nabla_{\Delta} \mathcal{L}$ (Section 3.2.2). Clipping a random variable changes its distribution, and for a generic non-linear loss, the clipped finite-difference estimate is generally *not* unbiased. The proof is deferred to Appendix A (which is not visible), but the main text states this as a proven theorem without specifying any assumptions. The variance-reduction argument in Eq. 8 relies on this unbiasedness claim. If the proof is flawed or requires restrictive unstated assumptions, the theoretical justification for DDC collapses — though the empirical results in Figures 2–3 demonstrate that DDC works in practice regardless. The authors should either provide a rigorous proof with clearly stated assumptions, or recast DDC as an empirically-motivated heuristic and adjust the theory accordingly.

- **Missing comparison with QLoRA and related PEFT methods that also fine-tune quantized models.** QLoRA (Dettmers et al., 2023) is the de facto standard for memory-efficient fine-tuning of quantized LLMs. The paper never mentions it, let alone compares against it. While QZO operates in a different paradigm (ZO rather than first-order), a discussion — and ideally an empirical comparison on a subset of tasks — is needed to situate QZO's practical value. A reader will naturally ask: "Why use QZO instead of QLoRA?" The paper currently provides no answer.

### Minor

- **MeZO hyperparameter tuning not disclosed.** The paper states that for MeZO, "we adopt the official code" (Section 4.1) but does not describe any task-specific hyperparameter tuning, while QZO's hyperparameters are explicitly reported. Given the high variance of ZO methods, this raises a concern about whether the comparison is fair — particularly for cases where QZO substantially outperforms MeZO (e.g., Llama-2-7B on SST-2: 90.0 vs. 83.5; SQuAD: 85.5 vs. 80.7). Transparently reporting the hyperparameter selection procedure for all baselines would address this.

- **No run-to-run variance reported.** ZO methods are notoriously noisy. All results in Tables 1–3 are single numbers with no standard deviations or indication of stability across random seeds. Reporting variance (even for a subset of experiments) would significantly strengthen the empirical claims.

- **AdamW memory measurement under FSDP is ambiguous.** The 87.6 GB figure for OPT-6.7B under fully-sharded data parallel (Figure 1) is surprisingly high for a 6.7B model with FSDP, which should *reduce* per-GPU memory. Clarifying the FSDP configuration (number of GPUs, sharding strategy) would prevent confusion.

### Trivial

- **Non-negative clipping in Algorithm 1 is not discussed:** The `max(Δ_i − η_t * d' * z, 0)` step enforces non-negative scales, which may introduce additional bias or affect convergence. No analysis or discussion is provided.

- **FLOPs comparison lacks explicit training-step counts for baselines:** Table 2 reports total FLOPs but the number of training steps for MeZO and full fine-tuning is not stated, making the total-FLOPs comparison difficult to interpret independently.

## Nice-to-Haves

- Analyse *what* the scale updates learn (e.g., visualize scale changes per layer to understand whether the scale shift compensates for distribution drift between pre-training and downstream data).
- Ablate how quantization granularity (group size, block size) affects QZO's performance and memory trade-off.
- Extend the evaluation to more challenging benchmarks (MMLU, GSM8K) to probe the limits of ZO-based fine-tuning on quantized models.

## Removed Points

*These points were flagged in the input reviews but are removed from the final assessment for the stated reasons.*

- **"18× framing is imprecise"** — The paper explicitly states this is "compared to full-parameter fine-tuning in 16 bits" and the figure clearly labels the comparison against AdamW. No deception.
- **"Scale structure needs clarification"** — The paper specifies GPTQ group size 128 and distinguishes per-channel scales for AQLM. Sufficient detail is provided.
- **"Missing appendix / stripped proofs"** — This is a parser artifact; the original submission contains the appendix. The Theorem 1 concern is retained as a Major weakness because the *main text's presentation* of the theorem is insufficient, not because the appendix is missing.
- **"Should clarify whether scales are per-channel or per-group"** — Covered by existing text (group size 128 for GPTQ, channel-wise for AQLM).

## Novel Insights

The key insight — that one can enable zeroth-order optimization on quantized models by perturbing continuous quantization scales rather than discrete weights — is genuinely novel and opens a clean path for combining ZO with any scalar-based or codebook-based PTQ method. The observation that directional derivative clipping (which is simple to implement) is sufficient to stabilize ZO training on quantized models is also practically valuable, even if the theoretical justification needs revision.

## Suggestions

- Either provide a complete proof of Theorem 1 with clearly stated assumptions in the main text, or retract the unbiasedness claim and present DDC as an empirical stabilization technique with a bias-variance trade-off analysis. The current state — claiming a theorem without visible assumptions — is the paper's weakest point.
- Include at minimum a discussion of how QZO relates to QLoRA, and ideally run a head-to-head comparison on 1–2 tasks. This will preempt the most obvious question from readers and significantly strengthen the paper's positioning.
- Report MeZO hyperparameter selection and run at least 2–3 seeds on a subset of experiments to give readers confidence in the stability of the results.

## Score and Decision

**Bracket:** Round 1 established a range of 5.5–7.0. Round 2 anchors: SensZOQ (5.80, ZO+quantization, accepted), Sparse MeZO (5.50, sparse ZO, rejected), LQ-LoRA (6.75, LoRA+quantization, accepted), QA-LoRA (6.33, quantization-aware LoRA, accepted), LoRAM (6.20, memory-efficient LoRA, accepted), Three-Stage Optimization (5.40, PEFT+quantization, rejected).

**Comparison:** QZO is clearly stronger than SensZOQ (5.80) — more novel mechanism, broader experiments, better empirical results — and substantially stronger than Sparse MeZO (5.50) and Three-Stage Optimization (5.40). It is somewhat below LQ-LoRA (6.75) due to weaker theoretical backing and missing PEFT comparisons, and comparable in quality to QA-LoRA (6.33). The genuinely novel scale-perturbation mechanism combined with solid empirical results across diverse settings merits acceptance, but the theoretical issue with Theorem 1 and the missing QLoRA baseline prevent a higher score.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>