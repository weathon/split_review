Now let me run the calibration searches.Based on Round 1, my initial bracket is **5.5–7.0**. The SAR paper (tyEyYT267x) scoring 8/8 is a significantly stronger paper with state-of-the-art results on large benchmarks. The SEDD paper (71mqtQdKB9, avg 6.6) is closer in style. Let me narrow the range.Now I have sufficient calibration data to write the review. Let me synthesize everything.

---

## Summary

Insertion Language Models (ILMs) introduce a new approach to sequence generation in which a model jointly predicts a vocabulary token and an insertion position at each step. Unlike Masked Diffusion Models (MDMs) which require a fixed number of mask tokens and generate using absolute positions, ILMs remove dropped tokens entirely and reconstruct them in arbitrary order using relative positional reasoning. The paper trains ILMs via an approximate denoising objective and demonstrates: (1) dramatically better performance on variable-length path planning tasks on star graphs (99.1% vs 21% for MDM, 23% for ARM), (2) competitive performance on Zebra logic puzzles (90% vs 91.2% for oracle ARM), and (3) text generation quality comparable to MDMs and approaching ARMs on small/medium corpora.

---

## Strengths

- **Near-perfect planning performance on star graphs**: ILM achieves 99.1% exact match on Star_hard (variable-length, degree-5 graphs, max path length 12) vs. 21% for MDM and 23% for ARM (Table 1). This is a striking and well-explained result—MDMs rely on absolute token positions, making variable-arm-length prediction intractable without solving the puzzle in one pass, while ILMs use relative positions iteratively. The example generation trajectories in Appendix C.0.3 (referenced in the text) corroborate this.

- **Zebra puzzle results approach oracle ARM without oracle ordering**: ILM achieves 90.0% on Zebra puzzles, very close to the ARM trained on oracle solver-decomposed orderings (91.2%), and clearly above the ARM trained on natural ordering (81.2%) and MDM (82.6%). This is particularly significant because the oracle ARM uses the optimal solution ordering from Shah et al. (2024), meaning ILM matches near-oracle performance with no ordering supervision.

- **Clean and complete parameterization**: The insertion model uses a single transformer encoder (Equation 3), joint logits over (position, vocabulary), and a dedicated `<stp>` token for stopping (Equation 4). This is a natural and principled extension that handles both insertion decisions and stopping in a unified framework. The departure from the Insertion Transformer (Stern et al., 2019) which uses EOS for stopping is validated by the IT comparison (22.1% on Star_medium vs 100% for ILM), showing the dedicated stopping classifier is important.

- **Infilling flexibility demonstrated**: On both TinyStories and LM1B, ILM consistently outperforms MDM on single- and multi-segment infilling (Table 3), with lower ΔNLLgt across all conditions. This concretely demonstrates the practical advantage of not requiring a fixed number of mask tokens.

---

## Weaknesses

### Fatal
None.

### Major

- **Length confound in NLL evaluation** (Table 2): ILM generates sequences with mean length 119 on Stories vs. a training-distribution mean of 205, and mean length 21 on LM1B vs. training mean of 28. Per-token NLL under a causal LM evaluator is not length-neutral: short sequences accumulate less incoherence and require the evaluator to condition on less context. The paper correctly identifies MDM's over-generation (985 tokens on Stories) as driving its high entropy and high NLL, but applies no symmetric scrutiny to ILM's under-generation, which is comparably severe in the opposite direction. The Prometheus judge scores (Figure 5) may be similarly influenced—shorter, simpler texts are generally easier to score well on fluency and grammaticality. The conclusion that ILM beats MDM on NLL may be partially artifactual, and the paper does not attempt to control for length in any comparison. A length-matched evaluation (e.g., truncating generated samples to training-distribution mean length before computing NLL, or conditioning generation on a target length) would test whether the quality advantage is genuine.

- **Misleading inference cost comparison in Figure 6**: Figure 6 compares ILM against "ARM (w/o KV cache)" explicitly—the caption labels it as such and the paper acknowledges in the Limitations that "ILMs also do not allow caching of hidden states and can therefore be slower at inference compared to ARMs with hidden state caching." However, Figure 6 does not include ARM with KV cache, which would shift ARM's curve significantly leftward. The figure as presented implies ILM's time-quality tradeoff is competitive with ARM, when the proper comparison—ARM with KV cache—would likely show ILM at a clear disadvantage in inference speed. The paper's honesty in the Limitations section partially mitigates this, but the figure remains misleading without an ARM+KV-cache reference point.

### Minor

- **"Competitive with ARMs" overclaimed for LM1B**: The abstract states ILMs "perform on par with ARMs," and Table 2 shows LM1B NLL of 4.67 (ILM) vs. 3.94 (ARM)—a gap of ~19%. While the Stories result (2.14 vs. 2.11) is genuinely competitive, the claim of broad competitiveness is overstated. The body text is more measured ("performs slightly better than MDMs on unconditional text generation"), but the abstract and introduction create an inflated impression.

- **Stopping mechanism not ablated or diagnosed**: The paper's stopping criterion is a binary classifier jointly trained with the denoiser, but its behavior is unexamined. ILM systematically under-generates (119 vs. 205 on Stories), suggesting possible early stopping errors, yet no ablation is provided—e.g., varying the stopping threshold, or measuring calibration of the stopping classifier. Understanding whether under-generation stems from the stopping classifier or from the generation model losing confidence would strengthen the claim that ILMs support "arbitrary-length" generation.

### Trivial

- No confidence intervals or variance estimates are reported in Tables 2 and 3, or for the Prometheus judge bar charts. With evaluation sets of 3,500 and 3,300 examples and LLM-based scoring, some differences may not be statistically reliable.

---

## Nice-to-Haves

- A length-controlled evaluation of text generation quality would validate the NLL comparisons (e.g., truncate all samples to mean training length before scoring, or use length-conditional generation and compare at fixed length).
- A brief empirical check of whether the biased training objective (Eq. 2) produces similar learned distributions to a lower-variance but more costly unbiased objective in a small toy setting—even a 2-sentence demonstration would add confidence that the approximation doesn't systematically distort the text generation results.
- An ablation comparing the dedicated `<stp>` stopping classifier against the EOS-based approach (Insertion Transformer) on text tasks, not just planning tasks—this would isolate the contribution of the stopping mechanism in open-ended generation.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "Biased training objective is incompletely characterized" (as major)**. The paper explicitly states in Section 3: "we use a biased training objective that makes direct use of all the dropped tokens… instead of estimating the token probabilities by marginalizing over all generation trajectories." This is presented as a deliberate design choice, not a gap—the approximation rationale is given and deferred to Appendix D. The empirical results suggest it works. Kept only as a nice-to-have for a toy validation, not a weakness.

- **Harsh critic: MDM's fundamental limitations "overstated" vs. inference-time fixes**. The paper itself acknowledges (Section 4) that Gong et al., Zheng et al., and Campbell et al. address MDM limitations via inference tricks, and explicitly scopes ILM as a training-time alternative. This is not an overclaim.

- **Strength finder: "training objective avoids high variance through biased approximation"** — kept as supporting context but not a standalone strength since the paper itself calls it a compromise.

- **Harsh critic: "the paper's claim is primarily about generation quality rather than speed"** — the inference cost issue is real and retained as Major, but the framing that this is "not a fatal issue" is correct.

---

## Novel Insights

The most genuinely novel methodological insight is that inserting tokens at relative positions—rather than unmasking tokens at absolute positions—allows a model to iteratively resolve positional uncertainty by deferring hard positional decisions until adjacent tokens are placed. The star graph experiments provide a clean demonstration: when arm lengths vary, MDMs must implicitly solve the whole puzzle in one pass to determine absolute positions, while ILMs can work inward from both ends and leave the junction token for last. This observation about the structural coupling between relative position prediction and sequential dependency resolution has implications beyond the specific tasks studied.

---

## Suggestions

1. Run length-controlled NLL evaluation: generate samples conditioned on a target length (or filter samples to the training-distribution mean) and recompute NLL comparisons. This resolves the primary evidentiary concern about text quality.
2. Add ARM+KV-cache to Figure 6 or replace the figure with one that separates throughput from quality using a more comparable baseline (e.g., ARM with speculative decoding or at matched inference budget).
3. Provide a stopping-classifier analysis: plot the empirical distribution of stopping decisions as a function of sequence length to confirm whether systematic under-generation is a classifier issue.
4. Revise abstract claim from "on par with ARMs" to "competitive with ARMs on Stories and approaching ARMs on LM1B" to accurately reflect the ~19% LM1B NLL gap.

---

## Score and Decision

**Axes:**

- *Originality*: High. ILMs are a distinct formulation from MDMs and ARMs. The insertion-at-relative-position mechanism is genuinely novel and not just an engineering variant.
- *Importance of research question*: High. Variable-length out-of-order generation with flexible infilling addresses real limitations of both ARMs and MDMs.
- *Claims well-supported*: Mixed. Planning claims are very well-supported; text generation claims are partially confounded by length effects.
- *Soundness of experiments*: Moderate. Planning experiments are clean and compelling; text experiments have the length confound issue and absence of variance estimates.
- *Clarity of writing*: Good. The method is clearly described; the limitations discussion is honest.
- *Value to the community*: Solid. ILMs offer a practical alternative generation paradigm and the planning results would be of broad interest.

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| NRYgUzSPZz.md (Beyond Autoregression: Discrete Diffusion for Planning) | 6.25 | R1 | Similar framing (diffusion vs AR on planning), but ILM is more architecturally novel with a new model class rather than applying standard MDM to new tasks |
| WNvvwK0tut.md (Scaling up MDMs on Text) | 6.50 | R1 | Mostly empirical scaling study, no new model; ILM is more methodologically novel |
| 71mqtQdKB9.md (SEDD: Discrete Diffusion LM) | 6.60 | R1 | Strong theoretical contribution with competitive LM benchmarks; ILM is more task-focused with planning wins but smaller-scale text evaluation |
| sMyXP8Tanm.md (RADD, Absorbing Discrete Diffusion) | 6.20 | R1 | Reparameterization within existing MDM framework; ILM introduces a new generation paradigm |
| Qn4HEhezKW.md (Diffusion LM + Scaling + Instruction FT) | 5.00 | R2 | Rejected; applied diffusion scaling without new method; weaker contribution than ILM |
| MJNywBdSDy.md (Discrete Diffusion with Planned Denoising) | 5.75 | R2 | Adds planner to diffusion; ILM is comparable in novelty but with cleaner formulation |
| tyEyYT267x.md (SAR interpolating AR and diffusion) | 8.00 | R1 | State-of-the-art on standard LM benchmarks; substantially stronger empirical scope than ILM |
| sL2F9YCMXf.md (Energy-Based Diffusion LM) | 6.75 | R2 | New energy-based approach to diffusion LM with competitive text8/LM1B benchmarks |

**Round-1 bracket**: 5.5–7.5  
**Round-2 narrowing**: ILM is more novel than NRYgUzSPZz (6.25) and roughly comparable to WNvvwK0tut (6.5) in overall contribution. The length confound concern and the LM1B gap pull it slightly below sL2F9YCMXf (6.75) and 71mqtQdKB9 (6.6), which have stronger text generation results. The planning experiments are ILM's strongest asset; the text generation evidence is noisier than those anchor papers.

**Final position**: ILM is better than the 5.75 anchors (genuine architectural novelty, compelling planning results), roughly comparable to the 6.25–6.5 band (interesting contribution, some evaluation concerns), and below the 6.75+ papers (which achieve cleaner results on standard benchmarks). I place ILM at **6.0**.

**Decision: Accept**. The insertion language model formulation is genuinely novel, the planning task results are compelling and well-explained, and the text generation results are at least consistent with the claims (modulo the length confound, which is a revision-addressable concern). The weaknesses are real but not fatal to the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>