Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

The paper extends the training-loss-curve (TLC) collapse phenomenon—where normalized loss curves from different model sizes align onto a universal trajectory—from small-scale µP experiments to practical LLM training with AdamW, weight decay, and jointly scaled width/depth/batch size/decay. It identifies three controls (AdamW timescale τ, tokens-per-parameter ratio TPP, and LR schedule) that must be held fixed across scales for collapse, instantiates this in the Celerity model family (300M–3.9B), and demonstrates two applications: using collapse residuals for early anomaly detection and enabling early stopping in hyperparameter tuning via a parametric model fit at small scale.

## Strengths

1. **Extends TLC collapse to practical LLM training regimes.** Prior work (Qiu et al., 2025) was limited to small models with vanilla Adam and no weight decay. This paper demonstrates collapse under AdamW with weight decay, co-scaled width/depth/batch size, at up to 3.9B parameters—directly addressing the gap Qiu et al. called for. Figure 6 shows tight collapse at 20 TPP (r=0.175) and 80 TPP (r=0.087), and Figure 1 (middle) shows the 234 TPP band.

2. **Identifies τ, TPP, and LR schedule as the three scale-invariant controls governing TLC shape.** The paper provides a clear analysis: τ controls the bias–variance trade-off (formalized via a noisy-quadratic model, Eq. 3), TPP sets the relative improvement pace via power laws, and the LR schedule phases these effects. Figure 3 convincingly shows that sweeping η, λ, or B independently while matching τ yields nearly identical TLC shapes—unifying disparate hyperparameters under a single timescale.

3. **Introduces Celerity, a competitive LLM family trained in a collapse regime, with a concrete debugging success story.** The 1.8B run's numerical instability was invisible in the raw loss until ~90% of training, but collapse residuals showed clear deviation starting at ~60% (Figure 1 right). This localized the cause (a loss kernel bug triggered at specific microbatch sizes) and guided a repair that brought the rerun onto the reference trajectory. Celerity also sits on the compute-accuracy Pareto frontier against comparable open models (Figure 2), showing collapse is compatible with practical efficiency.

4. **Proposes an early-stopping method for hyperparameter tuning that exploits collapse.** The six-step procedure (align partial large-scale curves to a small-scale reference or parametric surrogate to predict final loss) is novel and principled. Figure 9 shows the "predicted best" method achieves near-zero loss gap after only 10–30% of λ-sweep training, while the "current best" heuristic consistently fails. The parametric surrogate (Eq. 4–5) generalizes from 111M to 3.3B with low MAE (Table 11, cited), enabling tuning without full-scale sweeps.

5. **Provides theoretical grounding for τ's role via a noisy-quadratic model and scale-invariance argument.** The derivation in Appendix B.3 (Eq. 3) formalizes how τ controls the bias–variance trade-off, and Appendix B.2 explains TPP's effect through power laws of effective training budgets. This goes beyond a purely phenomenological description.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Ambiguity in the definition of batch size.** Table 1 defines B as *"Batch size (tokens per optimization step)."* Yet the values in Table 2 (e.g., 176 for the 300M model) are almost certainly numbers of sequences, not tokens: with seq_len=8192 and 234 TPP, treating 176 as tokens would imply ≈400M steps, which is computationally implausible. The same mismatch appears in the Fig. 3 experiments (B values 126–2016 with context length 2048). This inconsistency does not invalidate the results—because τ is computed and held fixed using a consistent definition throughout—but it creates confusion about a central quantity and undermines reproducibility. The paper should clarify whether "Batch Size" in tables/figures is sequences or tokens, and if sequences, state the effective token batch size explicitly.

2. **Rhetorical overclaim linking collapse to compute-efficiency.** The abstract states collapse "emerges as a signature of compute-efficient training," and the introduction calls it a "robust marker of compute-efficient and stable pre-training." However, the paper's own analysis (Sec. 3) establishes that collapse follows from fixing τ, TPP, and the LR schedule—a condition of *consistency*, not optimality. Celerity uses optimal τ (which happens to depend on TPP), so collapse and efficiency co-occur in practice, but the paper would benefit from clearly separating the two claims: collapse is a consequence of fixed controls, and Celerity's efficiency is a separate (well-supported) finding from Figure 2 and the compute-tradeoff analysis in Figure 5.

3. **Early-stopping validation is limited to λ sweeps.** The core early-stopping results (Figure 9) validate the method only on weight-decay sweeps at two model sizes (1.7B and 3.3B). The paper references "further experiments" in Appendix D.2 (not available in the main text), but the main argument would be strengthened by at least mentioning results for learning-rate or batch-size sweeps, or briefly discussing when the method may fail (e.g., when τ varies beyond the fitted range, or when the LR schedule deviates from linear decay).

4. **The switch from µP to CompleteP is noted but not reconciled with the collapse framework.** The theory and initial experiments (Sec. 3) are built on µP, but Celerity uses CompleteP for "more efficient/reliable" hyperparameter transfer (Fig. 15 cited). The paper does not discuss whether the three identified controls (τ, TPP, LR schedule) still govern collapse under CompleteP, or whether the change in parameterization could affect the normalization or scale-invariance arguments. A brief comment on compatibility would strengthen the paper.

5. **Architectural differences between the Sec. 3 probe experiments and Celerity.** The probe experiments use a GPT2-like model with ALiBi embeddings and SwiGLU, while Celerity uses Squared ReLU, Llama‑3 vocabulary, and ALiBi with untied embeddings. The paper does not discuss whether the same three controls govern collapse under these architectural changes, leaving a gap in generalizability.

6. **The compute-frontier claim (Figure 2) is an uncontrolled comparison.** Celerity models are positioned on the Pareto frontier against other open models, but data mixtures, training durations, and evaluation protocols differ across families. The paper acknowledges Celerity's philosophy (not targeting specific benchmarks) and the comparison is reasonable, but the "frontier" claim is observational rather than rigorously controlled. This should be caveated more explicitly.

7. **The diagnostic application rests on a single anecdote.** The 1.8B case study is compelling but is a single incident. The claim that collapse residuals "provide a sensitive, early diagnostic of training pathologies" (abstract) would be more convincing with at least one additional example or a systematic characterization (e.g., what kinds of anomalies are detectable, at what residual magnitudes).

### Trivial
None.

## Nice-to-Haves

- **Inter-run variability.** The paper would be stronger with multiple-seed plots for at least one scale, to quantify whether the observed collapse is within noise (as Qiu et al. (2025) did with "supercollapse"). Currently the tightness of collapse is assessed visually.
- **Parametric model derivation.** Eq. 4 is presented as a phenomenological fit; a sketch of how the noisy-quadratic model (Eq. 3) motivates the chosen functional form would be helpful.
- **Absolute loss differences in Figure 9.** Reporting the actual loss gaps (not just percentages) would help readers gauge practical significance.

## Removed Points

These points were flagged by one or both reviewers but are excluded from the main weaknesses for the reasons stated below:

- **"$1B runs" as a draft remnant** — The Conclusion says "For \$1B runs, collapse provides a valuable reference trajectory." The critic interpreted this as a stray dollar amount, but in context it refers to billion-dollar (very expensive) LLM runs, which is a legitimate and deliberate point. Not a weakness.
- **"No analysis of when collapse fails"** — The paper explicitly discusses when collapse does not occur (Llama-2, because τ and TPP vary across sizes) and identifies the conditions for collapse. The suggestion to explore whether partial collapse is possible by adjusting τ per model while keeping TPP fixed is a reasonable future direction, not a missing analysis.
- **Parametric model lacks theoretical grounding** — The paper provides a justification for each term in Eq. 4 (power-law improvement from Appendix B.2, LR-schedule modulation from Appendix B.3). Demanding a derivation "from first principles" would be excessive for an empirical systems paper.
- **Statistical significance / confidence intervals** — Single-run evaluation is standard for large-scale LLM training. Requesting multiple seeds is a nice-to-have but not a weakness.
- **Formatting, appendix, missing proof complaints** — These are artifacts of the PDF extraction process (appendix was stripped by the parser) or are style nitpicks that do not affect scientific content.
- **Missing related works** — Cannot be verified externally and may not exist.
- **Reproducibility nitpicks** (hyperparameters, implementation details) — These are standard for the scale of experiments in this paper.

## Novel Insights

The most striking insight that emerges from the reviews is that the paper's core finding—τ as a unifying timescale that subsumes η, λ, and B—is itself a practical tool. The observation that fixing τ (rather than λ) during batch-size sweeps preserves TLC ordering (Figure 7) directly challenges standard practice and provides an actionable rule for practitioners. This is a case where a theoretical reframing (τ as an EMA timescale) yields an immediate experimental design improvement. The merger of the bias–variance trade-off perspective (Eq. 3) with the power-law improvement from TPP (Appendix B.2) into a single parametric form (Eq. 4) also stands out as a compact and usable model.

## Suggestions

1. **Clarify the batch-size definition.** Specify in Table 2's caption or a footnote that batch sizes are in sequences (microbatches), and define the effective token batch size = B × seq_len. Include the corrected τ formula if needed.

2. **Reframe the collapse–efficiency link.** In the abstract and introduction, state that collapse follows from fixed τ, TPP, and LR schedule, and that Celerity *additionally* achieves compute-efficiency by choosing τ optimally for its TPP. This separates the descriptive claim from the normative one.

3. **Broaden early-stopping validation or caveat it.** If Appendix D.2 contains results for other hyperparameters (η, B), mention them in the main text. If not, add a brief discussion of expected failure modes (e.g., when τ varies across settings being compared).

4. **Add a brief comment on CompleteP compatibility.** Even a single sentence noting that the τ/TPP/schedule controls appear to transfer across parameterizations (with a reference to the appendix) would address the concern.

5. **Acknowledge the uncontrolled nature of the frontier comparison** more explicitly in the Figure 2 caption or main text, noting that different training data and protocols prevent a fully controlled comparison.

## Score and Decision

MY FINAL SCORE: 7.5
MY FINAL DECISION: Accept