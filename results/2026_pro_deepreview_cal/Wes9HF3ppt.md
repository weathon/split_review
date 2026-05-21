Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary

This paper introduces Insertion Language Models (ILMs), a new sequence generation paradigm where models generate text by inserting tokens at arbitrary positions — jointly choosing where to insert and which token to insert — rather than generating left-to-right (ARMs) or using fixed-length masking (MDMs). The authors propose a simple transformer-based parameterization with a biased denoising training objective and a stop classifier, and evaluate on synthetic planning tasks (star graphs, zebra puzzles), unconditional text generation (LM1B, TinyStories), and text infilling. ILMs achieve near-perfect accuracy on difficult variable-length planning tasks where both ARMs and MDMs fail dramatically, and outperform MDMs on text generation while approaching ARM quality on some metrics.

## Strengths

- **Compelling synthetic results demonstrating clear advantages over ARMs and MDMs.** On the Star_hard task (variable-length paths on asymmetric star graphs), ILM achieves 99.1% exact-match accuracy versus 21% for MDM and 23% for ARM (Table 1). On Zebra Puzzles, ILM achieves 90.0% versus 82.6% (MDM) and 81.2% (ARM). These results directly validate the paper's central motivation: insertion-based generation handles strong token dependencies and variable sequence lengths where both left-to-right generation and fixed-length masking fall short.

- **Higher unconditional text generation quality than MDMs.** On both Stories and LM1B, ILMs obtain lower per-token NLL under Llama-3.2-3B than MDMs (e.g., 2.14 vs. 2.54 on Stories; Table 2), and are rated superior in coherence and consistency by a Prometheus-2-7B LLM judge (Figure 5). The ILM also avoids the length-explosion problem observed in the MDM (MDM outputs average 985 tokens on Stories vs. 119 for ILM and 205 in the training data).

- **Novel and practical training formulation.** The combination of a direct regression on the empirical insertion distribution (avoiding high-variance trajectory marginalization, Eq. 2) with a dedicated stop classifier (Eq. 3) and a clean transformer parameterization (Eqs. 3–4) is a genuine algorithmic contribution. The design is simple, implementable, and the paper shows it works across multiple domains.

- **Well-scoped motivation with clear contrast to existing paradigms.** The paper carefully identifies specific failure modes of ARMs (left-to-right rigidity) and MDMs (fixed-length masking, simultaneous unmasking) and designs ILMs to address precisely these limitations. Figure 1 and the running example in the introduction effectively communicate the key differences.

## Weaknesses

### Fatal

None.

### Major

- **The infilling evaluation does not test the core claimed advantage over MDMs.** The paper's central motivation is that ILMs support arbitrary-length infilling without knowing how many tokens to fill, while MDMs require a fixed number of mask tokens. However, the infilling experiments (Section 5.3.2) construct test examples by removing known segments from clean text — the ground-truth number of tokens to insert is therefore known. The paper never specifies how the MDM was provided with the infilling task (e.g., whether it was given exactly the ground-truth number of mask tokens or a fixed number). If the MDM was given the correct number of masks, the task reduces to fixed-length infilling and the experiment does not test the very flexibility that the paper claims distinguishes ILMs from MDMs. This is a significant evidential gap that undermines one of the paper's main claimed contributions. *The results still show ILM outperforming MDM on infilling metrics, but the experiment as described cannot substantiate the "arbitrary-length" claim.*

- **The explanation of MDM failure on variable-length star graphs is inconsistent with the model description.** Section 5.1.1 states that the MDM's degraded performance on Star_medium and Star_hard "can be attributed to a deeper limitation of MDMs, which work with absolute token positions" and that "ILM continues to perform well... because it utilizes relative positions." However, Section 5 specifies that MDMs use the DDiT architecture with RoPE-based transformers — RoPE encodes relative, not absolute, positions. The claimed mechanism for MDM failure is therefore not credible as stated. The MDM likely fails for other reasons (e.g., the fixed-length masking structure, the need to predict token identities and positions jointly in one pass), but the paper's analysis conflates these with positional encoding, weakening the argument for ILM's systematic advantage.

### Minor

- **The abstract claim of "on par with ARMs" overstates the text generation results.** On LM1B, the ILM achieves NLL of 4.67 versus 3.94 for the ARM — a gap of 0.73, which is substantial relative to the training-data NLL of 3.71. On Stories the gap is much smaller (2.14 vs. 2.11), and the introduction itself uses the more measured "competitive with ARMs." However, the abstract's "on par" language is misleading for the LM1B result and should be calibrated. The paper's own Discussion section acknowledges that "ILMs still perform slightly worse than ARMs trained for the same number of gradient steps," which contradicts the abstract's framing.

- **The biased training objective is not analyzed.** The paper acknowledges (Section 3) that the training objective replaces trajectory marginalization with a direct regression on the empirical insertion distribution, introducing bias. No ablation or analysis is provided on how this bias affects generation quality — e.g., whether the approximate loss leads to mode-averaging or incoherence when insertions are performed sequentially at test time. While the method works empirically on the presented tasks, the lack of investigation into this central approximation makes it unclear whether the approach will remain reliable at larger scales.

- **The shorter average generation length of ILMs may confound per-token NLL comparisons.** Table 2 shows that ILM-generated sequences are consistently shorter than ARM-generated ones (e.g., 21 vs. 30 tokens on LM1B, 119 vs. 201 on Stories). Shorter sequences may be inherently easier to score well on per-token NLL. The paper notes this but does not control for it or discuss how it affects the fairness of the comparison.

### Trivial

- The paper refers to "Star_small" in the text of Section 5.1.1 but the corresponding row in Table 1 is labeled "Star_easy" — the naming is inconsistent.

## Nice-to-Haves

- Redesigning the infilling evaluation to genuinely test the ability to insert an unknown number of tokens (e.g., provide only surrounding context without revealing the ground-truth token count, and measure whether the MDM fails or produces lower-quality completions when given an incorrect number of masks) would directly validate the paper's core motivation.
- An ablation comparing the biased training objective against a more faithful (even if higher-variance) estimator would increase confidence in the training method.
- A clearer discussion of what specifically causes MDMs to fail on variable-length star graphs — disentangling fixed-length masking structure from positional encoding — would strengthen the analysis.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about `n ~ U[L]` potentially being zero:** The paper explicitly defines `U[L]` as uniform over `{1,...,L}`, so `n=0` is excluded by definition. This was a misreading. REMOVED.

- **Speculation about tokenization artifacts confounding the infilling comparison:** The harsh critic suggested that the ΔNLL comparison may be confounded by tokenization differences between mask tokens and clean text. This is speculative without evidence of actual tokenization issues, and the paper's metric design (percentage change relative to reference) already partially controls for this. REMOVED.

- **Criticism about missing appendix/inference algorithm:** The parser strips appendices; Algorithm 2 is referenced in the main text and described in prose. The harsh critic notes it "is not shown" but this is a parser artifact. REMOVED (though noting that the core inference behavior — particularly how the empty-sequence starting point works — could be clearer in the main text).

- **"On par with ARMs" criticism applied uniformly:** The harsh critic framed this as applying to the whole paper, but the introduction uses "competitive" which is more accurate. The abstract is the primary offender. DEMOTED from Major to Minor with this nuance preserved.

- **Criticism about missing quantitative comparison with Insertion Transformer:** The paper does provide quantitative comparison in Table 1 (IT achieves 35.2%, 22.1%, 17.5% on Star tasks vs. ILM's 100%, 100%, 99.1%). The harsh critic asked for more qualitative breakdown, which is a nice-to-have, not a weakness. REMOVED.

- **Strength about "the problem is important":** Generic. REMOVED.

## Novel Insights

The most interesting emergent finding is that ILMs on the star graph task "tend to start the generation from both ends, leaving the most challenging edges... to latter steps" (Section 5.1.1). This suggests that the insertion-based generation process naturally implements a form of iterative refinement where easy decisions are made early and hard ones deferred — a behavior that emerges from the training objective rather than being explicitly programmed. This contrasts interestingly with MDMs, which must commit to all positions simultaneously. Understanding whether this "easy-first" behavior generalizes to other domains could be a fruitful direction.

## Suggestions

- The most impactful revision would be to add an infilling experiment where the MDM is given a deliberately wrong number of mask tokens (or a fixed budget) and ILM's flexibility advantage is directly measured. This would transform the infilling section from suggestive to conclusive.
- Tone down the abstract's "on par with ARMs" to match the introduction's "competitive with ARMs" — or better, state the specific conditions (close on Stories, gap remains on LM1B).
- Clarify the star-graph analysis: the real limitation of MDMs is likely the fixed-length masking structure (needing to predict variable-length paths given a fixed input length), not "absolute token positions." Revise the explanation to accurately reflect the architecture used.

## Score and Decision

**Anchor comparison:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| `NRYgUzSPZz` (Beyond Autoregression: Discrete Diffusion for Planning) | 6.25 | R2 | Similar in spirit (diffusion for planning vs. ARMs) with better theoretical framing but narrower evaluation. ILM has broader evaluation (adds text + infilling) but weaker analysis in places. ILM is slightly below this. |
| `71mqtQdKB9` (SEDD) | 6.60 | R1/R2 | Stronger theoretical contribution (score entropy framework), competitive GPT-2 results, but incomplete training. ILM has complete training and broader tasks but less theoretical depth. ILM is below this. |
| `sL2F9YCMXf` (EDLM) | 6.75 | R1 | Energy-based diffusion LMs, strong results but requires pretrained models. ILM is below this in execution quality. |
| `tyEyYT267x` (SAD3-LM) | 8.00 | R1 | Semi-autoregressive diffusion, comprehensive ablations, strong results. ILM is clearly below this. |
| `MJNywBdSDy` (Think while You Generate) | 5.75 | R2 | Discrete diffusion with planned denoising, solid results. ILM is roughly comparable — ILM has a more novel paradigm but similar-level evaluation gaps. |
| `9QPH1YQCMn` (Infilling Score) | 6.25 | R2 | Different topic. Not directly comparable. |

**Round 1 bracket:** 5.0–7.0  
**Round 2 narrowing:** The closest comparators are "Beyond Autoregression" (6.25) and "Think while You Generate" (5.75). The ILM paper has a more novel paradigm than both but suffers from an untested central claim (arbitrary-length infilling), an inconsistent analysis (MDM position encoding), and an overstated abstract. These issues place it below "Beyond Autoregression" and roughly at the level of "Think while You Generate."

**Originality:** The insertion-based paradigm is genuinely novel in the context of modern language modeling. The parameterization and training objective are clean contributions.

**Importance:** The problem — overcoming the limitations of both ARMs and MDMs — is significant. If the method scales, it could be impactful.

**Claims supported:** The planning-task claims are well supported. The text-generation claims are partially supported but the abstract overstates parity with ARMs. The infilling flexibility claim is not adequately tested by the experimental design.

**Soundness:** The methodology is sound at its core, but the MDM failure analysis on star graphs is inconsistent with the described architecture, and the biased training objective is unexamined.

**Clarity:** The paper is generally well-written and well-structured, though some details (e.g., empty-sequence initialization, MDM infilling protocol) are missing.

**Value to community:** The ILM paradigm offers a fresh direction for non-autoregressive generation that genuinely addresses limitations of both ARMs and MDMs. Even with the current evaluation gaps, the synthetic results are compelling enough to make this a valuable contribution that could inspire follow-up work.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>