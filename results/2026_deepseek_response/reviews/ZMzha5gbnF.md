Now let me write the final consolidated review.

## Summary

This paper identifies, characterizes, and mitigates the "priming vulnerability" in Masked Diffusion Language Models (MDLMs): if an affirmative token appears at an intermediate denoising step, it can steer the remainder of generation toward a harmful response, even in safety-aligned models. The authors demonstrate the vulnerability with a controlled anchoring attack (Fig. 2), derive a theoretical lower bound that enables a tractable optimization-based attack (First-Step GCG, Theorem 4.1, Table 1), and propose Recovery Alignment (RA), which trains models to produce safe responses from contaminated intermediate states. Experiments across three MDLMs, two datasets, four intervention-based attacks, three conversational attacks, and eleven utility benchmarks show that RA dramatically reduces attack success rates without meaningful capability degradation.

## Strengths

- **Clean quantitative demonstration of a non-obvious, MDLM-specific vulnerability (Section 4.1, Figure 2).** The anchoring attack is simple and controlled, and the results are striking: injecting a single affirmative token at the first denoising step raises ASR from 2% to 21% on LLaDA Instruct. This cleanly isolates the phenomenon from confounding factors that complicate prior concurrent work (PAD, DiJA).

- **Theoretically grounded attack that translates insight into practice (Section 4.2, Theorem 4.1, Table 1).** First-Step GCG derives and exploits a lower bound on the full denoising log-likelihood, achieving 4× higher ASR and 20× faster runtime compared to Monte Carlo GCG across all three models. The bound is validated empirically (Appendix C.2).

- **Recovery Alignment is directly motivated by the root cause analysis (Section 5, Table 2).** RA trains models from contaminated intermediate states rather than fully masked sequences. The ablation (RA w/o inter) cleanly isolates the effect: at t_inter=4, RA drops ASR to 1.3% on LLaDA Instruct while RA w/o inter remains at 22%, confirming that training on contaminated states is the crucial ingredient. This is the strongest piece of evidence in the paper.

- **Comprehensive and honest evaluation (Section 6, Tables 2–4).** Three models, two datasets (JBB-Behaviors, AdvBench), three evaluators (GPT-4o, LLaMA Guard 3, keyword matching), four intervention attacks, three conversational attacks, and eleven utility benchmarks. The paper honestly presents the diminishing returns at late intervention steps (t_inter=32) and does not overclaim.

- **Ablations validate the curriculum design (Section 6.4, Figure 3b).** Linear scheduling of the intervention step outperforms both constant and uniform scheduling, demonstrating that the curriculum is essential for effective training and providing guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The mechanistic explanation for RA's generalization to conversational jailbreaks is plausible but not directly evidenced (Section 6.2).** The paper attributes RA's lower ASR against PAIR, ReNeLLM, and Crescendo to a "recovery capability" where the model re-detects harmfulness at later steps and overwrites harmful tokens with safe ones. However, the paper explicitly uses hedging language ("A plausible mechanism is that..."), and the alternative explanation — that RA simply makes the model more conservative overall — is not ruled out by the presented evidence. The fact that RA does not degrade utility (Table 4) partially addresses this, but a targeted analysis (e.g., tracing generation trajectories to show where harmful tokens are overwritten) would convert a plausible claim into a demonstrated one. This does not weaken the paper's central contribution, but the framing slightly overreaches.

- **The monotonicity assumption in Theorem 4.1 is plausible but could be more precisely framed (Section 4.2).** The theorem assumes that log π_θ(r̃_{t+1} = r | q, r_t) ≥ log π_θ(r̃_1 = r | q, r_0) for all t. As the harsh critic correctly notes, the log-likelihood could increase not because the model is more confident in *that specific completion* but because accumulated unmasked tokens constrain the output distribution and *force* that completion by eliminating alternatives. The paper acknowledges this ("unmasked tokens in r_t are unchanged in subsequent steps") and provides empirical validation in Appendix C.2. The practical results of First-Step GCG (Table 1) stand on their own regardless of the theorem's strictness, but a more precise framing distinguishing "constraint-based" from "confidence-based" increase would strengthen the theoretical presentation.

### Trivial
None.

## Nice-to-Haves

- **Reward model details.** The paper uses DeBERTaV3 as the reward model (Section 5, Section 6.1) but does not specify which variant, the training data used, or the exact scoring criteria for safety vs. usefulness. Given that the reward model is central to RA, this specification would improve reproducibility.
- **Qualitative analysis of failure modes at late intervention steps.** The paper reports high ASR at t_inter=32 and attributes it to the "near-impossibility of generating a contextually safe response" from heavily contaminated states. A brief qualitative analysis of what the model *does* produce in these cases (partially harmful, nonsensical, or incomplete responses) would help practitioners understand deployment limits.
- **Training cost estimate.** For practitioners, an order-of-magnitude estimate of training compute (e.g., GPU-hours) would be useful. The paper reports attack runtime but not RA training cost.

## Removed Points

These points were removed from the inputs for the following reasons:

- *Harsh critic's question about why L=T=128 is the default configuration:* Trivial formatting/presentation nitpick, does not affect evaluation.
- *Harsh critic's concern about data contamination (reward model rewarding BeaverTails template matching):* Speculative concern not grounded in evidence from the paper; the utility results (Table 4) already show no degradation.
- *Harsh critic's "Missing parts" about training cost being absent:* Moved to Nice-to-Haves (not a core flaw).
- *Strength Finder's generic statements (e.g., "this paper addressed an important problem"):* Removed as generic/superficial; only concrete, evidenced strengths were retained.

## Novel Insights

The most distinctive insight to emerge from the reviews, beyond the paper's own contributions, is that the priming vulnerability is structurally distinct from ARM prefilling attacks in a way that demands different mitigation strategies. The harsh critic astutely notes that the paper's empirical finding — that training on contaminated intermediate states (not just safer outputs from clean starts) is necessary — has implications beyond this specific method: it suggests that any safety alignment for MDLMs must account for the *entire denoising trajectory*, not just the initial condition. This is a design principle that could guide future work on DLM-specific safety.

## Suggestions

- For the camera-ready version, add a brief analysis of generation trajectories under conversational jailbreaks (PAIR/ReNeLLM/Crescendo) comparing RA-trained vs. baseline models. Specifically, log the token-level evolution at intermediate steps to show where harmful tokens are overwritten with safe ones. This would convert the plausible mechanism in Section 6.2 into a demonstrated one.
- Clarify the framing of Theorem 4.1's monotonicity assumption: explicitly separate the "constraint-based" increase (accumulated unmasked tokens narrow the output space) from "confidence-based" increase (model internally prefers the target response more). Empirical validation in Appendix C.2 is sufficient, but the framing in Section 4.2 could be more precise.
- Add a brief paragraph specifying the reward model (DeBERTaV3 variant, training data, scoring criteria) to Section 5 or Appendix D.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>