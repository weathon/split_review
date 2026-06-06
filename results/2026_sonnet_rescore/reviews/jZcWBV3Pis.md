## Summary

This paper evaluates the robustness of Chinchilla's (Hoffmann et al., 2022) compute-optimal scaling laws in two parts. First, it uncovers that three valid interpretations of Chinchilla's model parameter counts exist, with discrepancies up to 15.2%, and shows that neither the five scaling-law fit parameters nor the compute-optimal tokens-per-parameter ratio is meaningfully altered by which interpretation is used. Second, it conducts a structured four-perturbation sensitivity analysis (multiplicative, additive constant, systematic bias, and log-normal noise) with analytical derivations, finding that additive and systematic-bias errors can qualitatively alter the ratio's flatness while multiplicative and noise perturbations leave the overall picture intact.

---

## Strengths

- **Discovery of a previously unrecognized parameter ambiguity.** The paper documents a concrete, verifiable discrepancy: comparing Chinchilla's reported model parameters against those re-derived from Table A9's architectural hyperparameters (Eq. 1 vs. the paper's Table 1) yields errors averaging 7.4% and reaching 15.2% for all 50 models. This is a specific, reproducible finding with immediate practical relevance.

- **Scaling-law parameters are demonstrably insensitive to which interpretation is used.** Figure 2 (top row) shows that all five fit parameters $(\hat{E}, \hat{A}, \hat{\alpha}, \hat{B}, \hat{\beta})$ are statistically indistinguishable across the three interpretations, with 4000-bootstrap error bars overlapping. The insensitivity result is supported directly by the replication code of Besiroglu et al. (2024).

- **Standard-formula parameters produce a flatter compute-optimal ratio trend.** Figure 2 (bottom row) quantifies slopes of −0.572, −1.049, and −1.248 per decade for the standard formula, best-fit, and reported parameters respectively — showing the most commonly used formula actually strengthens Chinchilla's key heuristic rather than weakening it.

- **Analytical derivations validate the perturbation trends.** Sections 3.1–3.4 provide mechanistic explanations for each perturbation type: multiplicative errors scale $\hat{A}$ by $c_m^{\alpha}$ while leaving $\hat{\alpha}$ unchanged; additive constants shift $\hat{\alpha}$ linearly; systematic bias multiplies $\hat{\alpha}$ by $s^{-1}$. The systematic-bias derivation (Section 3.3) is verified empirically with $R^2 > 0.999$. These derivations go beyond empirical curve-fitting and add genuine theoretical depth.

- **Bootstrapping is used consistently to quantify uncertainty.** All sensitivity comparisons use 4000-sample bootstrap standard errors (Figure 2, Figure 4) and 80% confidence intervals for the compute-optimal ratio (Figure 5), ensuring reported insensitivity is not an artifact of point estimates.

- **Quantitative alignment with prior empirical work.** The additive-perturbation effects on $\hat{\alpha}$ (0.199 to 0.481 over the tested range) bracket the empirically observed shifts of 0.080–0.231 reported by Porian et al. (2024) and Pearce & Song (2024), anchoring the perturbation analysis in documented, real-world discrepancies.

---

## Weaknesses

### Fatal
None.

### Major

- **The Discussion overclaims robustness given the paper's own findings on additive and systematic-bias perturbations.** Section 3.2 shows that $\hat{\alpha}$ grows from 0.199 to 0.481 — more than doubling — as $c_a$ varies over the tested range (Figure 4, row 2). The paper itself states this "can qualitatively change the compute-optimal scaling strategy by altering the trend of the optimal tokens-to-parameter ratio" (Section 3, last paragraph of Introduction). Yet the Discussion calls the aggregate finding "a powerful confirmation of the original Chinchilla results." The additive perturbation is not a remote hypothetical: the paper explicitly motivates it by noting that inclusion or exclusion of embedding parameters is precisely the documented source of disagreement between Kaplan et al. (2020) and Hoffmann et al. (2022), and the estimated $\alpha$ shifts of 0.080–0.231 from Porian et al. (2024) and Pearce & Song (2024) fall squarely within the range where the paper's Figure 5 shows the ratio ceasing to be flat. "Partial confirmation with clearly identified failure modes" would be a more accurate summary. The tension between the empirical results and the Discussion language risks misleading readers who rely on the conclusion section.

### Minor

- **The best-fit coefficient of 5 is left unexplained.** Equation 3 replaces the standard coefficient 4 in the attention parameter count (4 weight matrices: $W_Q, W_K, W_V, W_O$) with 5. The paper does not identify what architectural element accounts for the extra matrix — bias terms, a position-dependent projection, tied vs. untied output weights, or something else. Crucially, the paper then uses standard-formula parameters (coefficient = 4) as the baseline for all perturbation analyses in Section 3. If the best-fit formula better reflects what Chinchilla actually trained, this baseline choice is itself an assumption that deserves at least a paragraph of justification or investigation. The discrepancy is acknowledged but not resolved, leaving the central ambiguity of Section 2 partially open.

- **No operational definition of "meaningful change" is given.** The paper repeatedly uses "meaningfully change" and "qualitatively change" as its principal verdict criterion, but never defines these in terms practitioners would use — e.g., percentage change in recommended model size at a given compute budget, or change relative to bootstrap confidence intervals. For Figure 2 (bottom row), the slope ranges from −0.572 to −1.248 per decade across the three interpretations; whether this matters for extrapolating to frontier-scale compute budgets is precisely the practical question, and the paper declines to answer it quantitatively. This is a presentation gap that can be addressed with a single worked example at a representative compute level.

- **The multiplicative perturbation sweep range is far wider than empirically motivated.** Section 3.1 sweeps $c_m$ over six orders of magnitude (0.001 to 1000), whereas Section 2's empirical finding motivates a range of only approximately $\pm$15% ($c_m \approx 0.85$ to $1.17$). The broad sweep is visually compelling but mixes the empirically relevant regime with hypothetical extremes, making it harder to read off the practical robustness claim from Figure 5.

### Trivial
None beyond parser artifacts in the extracted text.

---

## Nice-to-Haves

- A worked numerical example in the Discussion quantifying how the slope difference (−0.572 vs. −1.248 per decade) translates to a concrete change in recommended model size at, say, $10^{25}$ FLOP would replace hedged language with a precise answer that practitioners need.
- The Future Directions note about inference-optimized training regimes (Sardana et al., 2024; Gadre et al., 2024) deserves a sentence in the Discussion body. The claim that Chinchilla is "a durable and practical blueprint for the field" sits in tension with the well-documented shift toward deliberate overtraining for inference efficiency, which is mentioned only as a footnote to future work.
- Examining whether the factor-of-5 vs. factor-of-4 discrepancy corresponds to a specific architectural component of Chinchilla (e.g., tied vs. untied embeddings, bias terms in attention) would close the loop on Section 2's otherwise open-ended ambiguity.
- Acknowledging the C ≈ 6ND compute approximation and its interaction with the N definition (as documented in Pearce & Song, 2024) as an explicit scope limitation would make the paper's boundaries more transparent.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Chinchilla remains a durable guide despite practitioners training longer than Chinchilla-optimal."** The paper explicitly names inference-optimized training as a Future Direction, which is appropriate scoping. The Discussion's framing is somewhat loose, but this is primarily a "nice-to-have" note already retained above. Elevating it to a major weakness would be scope creep.

- **Harsh Critic: "The comparison to Pearce & Song and Porian et al. in Sec. 3.2 is 'quantitatively similar' but uses a simplification."** The paper itself acknowledges "assuming an additive constant is a simplification of both analyses" (Section 3.2). The comparison is a sanity check, not a claimed equivalence. This is not a weakness.

- **Strength Finder: "The compute-optimal prescription remains robust, further justifying its widespread use."** This is a paraphrase of the paper's own conclusion, not an independent strength. Dropped as duplicative.

---

## Novel Insights

The most genuinely novel finding is that the standard-formula parameter count — the version anyone would naively compute from Chinchilla's published architecture table — actually *strengthens* the flatness of the compute-optimal ratio compared to Chinchilla's own reported parameters. This reversal of the expected direction (that errors would weaken Chinchilla's conclusions) is non-obvious and gives Section 2 real independent value. The analytical derivation in Section 3.3 — showing that the compute-optimal ratio exponent becomes $(\alpha/s - \beta)/(\alpha/s + \beta)$ under a power-law systematic bias — is a clean theoretical result that generalizes beyond the Chinchilla context and could be directly useful for interpreting discrepancies in future scaling studies.

---

## Suggestions

1. **Revise the Discussion conclusion** to replace "powerful confirmation" with language that acknowledges the additive and systematic-bias failure modes documented in the paper's own Section 3. A honest summary would note robustness to multiplicative errors and noise, sensitivity to additive and systematic errors, and identify the empirically relevant regime (embedding parameter inclusion/exclusion) as lying in the sensitive zone.
2. **Provide an architectural explanation for the best-fit coefficient of 5.** Even a two-sentence investigation (e.g., "If Chinchilla included learnable position-dependent biases in the attention projections, the count increases by one matrix, yielding 5") would close an otherwise open question.
3. **Add one calibration example** in Section 2 or the Discussion: given the slope range (−0.572 to −1.248), what is the implied change in compute-optimal model size at a specific frontier-scale compute budget? This would give practitioners a concrete handle on whether the ambiguity matters for their use case.
4. **Narrow the discussion of multiplicative perturbation** to the empirically motivated range ($c_m \approx 0.8$–$1.2$) in the main text, and relegate the extreme sweep to an appendix. This sharpens the practical story without losing completeness.

---

## Score and Decision

**Originality:** The parameter-ambiguity discovery in Section 2 is genuinely novel. The perturbation framework in Section 3, while systematic, is methodologically standard. *Score: 3/5.*

**Importance of the research question:** Chinchilla underlies a large fraction of current LLM development decisions; a careful robustness study has clear practical value. *Score: 4/5.*

**Claims well supported:** Core findings (parameter insensitivity in Sec. 2, perturbation effects in Sec. 3) are well-supported. The "powerful confirmation" conclusion overreaches given the additive perturbation results. *Score: 3/5.*

**Soundness of experiments:** Methodology is sound throughout. Bootstrapping is appropriate. Analytical derivations are correct and verified. *Score: 4/5.*

**Clarity of writing:** Well-organized; figures are informative and appropriately captioned. The Discussion is the weakest section in terms of precision. *Score: 4/5.*

**Value to the research community:** Provides a concrete, citable answer to whether Chinchilla's parameter ambiguity matters (it doesn't for the scaling law fit); characterizes failure modes for practitioners. Bounded but real. *Score: 3/5.*

The paper makes a genuine empirical contribution with sound methodology and honest data presentation. Its main flaw is interpretive: the Discussion overreads the results as a "powerful confirmation" when two of the four perturbation types demonstrably alter the key ratio's behavior within empirically realistic ranges. This is a fixable framing issue, not a structural failure. The work fills a clear gap in the replication literature and is appropriate for publication at this venue with revisions to the Discussion and clarification of the best-fit coefficient.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>