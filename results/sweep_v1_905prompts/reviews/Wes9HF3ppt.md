Now I have sufficient context. Let me write the final consolidated review.

---

## Summary

This paper introduces Insertion Language Models (ILMs), which generate sequences by inserting one token at a time at arbitrary positions, jointly selecting both the insertion position and the vocabulary element. The training uses a denoising objective with a counting-based approximation to avoid high-variance Monte Carlo estimates, paired with a standard transformer parameterization. Evaluation on planning tasks (star graph path generation, zebra puzzles) shows ILM dramatically outperforming both ARMs and MDMs (e.g., 99.1% exact match on Star_hard vs. 21–23%), while on unconditional text generation (LM1B, TinyStories) ILM is competitive with ARMs and better than MDMs on multiple LLM-judged quality axes, and offers more flexible arbitrary-length infilling.

## Strengths

- **Near-perfect accuracy on variable-length planning tasks where both ARMs and MDMs collapse.** Table 1: ILM achieves 100% on Star_medium (MDM 36.5%, ARM 75%) and 99.1% on Star_hard (MDM 21%, ARM 23%). The experimental design cleanly isolates the failure modes — fixed generation order (ARM) and fixed-length masking with simultaneous unmasking (MDM) — and shows ILM overcomes both through iterative insertion with relative positions.

- **Outperforms both ARMs and MDMs on constraint satisfaction without oracle ordering.** On zebra puzzles (Table 1), ILM obtains 90.0% sequence accuracy vs. ARM 81.2% and MDM 82.6%, while an ARM trained with oracle solver-decomposed order reaches 91.2% — meaning ILM achieves comparable accuracy without privileged ordering information.

- **Demonstrably better arbitrary-length infilling than MDMs, especially multi-segment.** Table 3: ILM has lower ΔNLL_gt on all infilling settings (e.g., +12.27 vs. +14.36 on TinyStories single-segment; +23.52 vs. +25.64 on LM1B multi-segment) and improves ΔNLL_inp more strongly (e.g., −3.57% vs. −0.49% on LM1B single-segment). This directly demonstrates the advantage of not requiring a fixed number of mask tokens.

- **Multi-metric evaluation with an LLM judge provides evidence beyond NLL.** Figure 5 uses Prometheus 2 7B across five linguistic axes (coherence, consistency, fluency, grammaticality, non-redundancy), where ILM consistently matches or outperforms the ARM and beats the MDM, strengthening the text generation claims beyond the NLL metric alone.

- **Clean, well-motivated method.** The insertion-based formulation with dedicated stopping classifier and the counting-based training objective is conceptually simple and connects naturally to the identified failure modes of ARMs and MDMs.

## Weaknesses

### Major

- **No ablation studies.** The paper does not isolate the contribution of any component — the stopping classifier, the counting-based objective, the insertion parameterization, or the denoising scheme. An ablation on a small-scale task (e.g., ILM without the stop loss, or with a uniform target distribution) would significantly strengthen the method's justification and is standard practice for an empirical methods paper. This is the most significant gap.

- **No confidence intervals or statistical significance for any metric.** Table 2, Table 3, and Figure 5 report point estimates without error bars or significance tests, making it impossible to assess whether the reported differences (e.g., ILM vs. ARM on Stories NLL: 2.14 vs. 2.11) are meaningful. This is a notable methodological shortcoming even by the community's typical standards for empirical ML papers.

### Minor

- **Abstract overstates text generation results.** The abstract claims ILMs "perform on par with ARMs" in unconditional text generation, but Table 2 shows a 0.73 nats/token gap on LM1B (ILM 4.67 vs. ARM 3.94). The Prometheus judge (Figure 5) tells a more nuanced story where ILM leads on several quality axes, but the blanket "on par" phrasing is misleading for the LM1B NLL result. The introduction's phrasing ("competitive with ARMs") is more accurate. The paper body's own conclusion says "slightly worse." This inconsistency should be resolved.

- **Imprecise explanation for MDM failure on star graphs.** The paper attributes MDM's poor performance on variable-length star graphs to "absolute token positions" (Section 5.1.1), yet Section 5 states the DDiT architecture used for MDMs is "RoPE based" — the same relative position encoding used by ILMs. The more accurate explanation (which the paper also alludes to elsewhere) is MDM's fixed-length masking constraint, not absolute vs. relative positions. This internal inconsistency is confusing.

- **Inference stopping mechanism underspecified.** The stopping classifier is trained with a binary cross-entropy loss, but Algorithm 2 (inference) does not specify a stopping threshold or how the model decides when to stop during generation. The average generated lengths in Table 2 suggest ILM stops well short of the training-data average on Stories (119 vs. 205), indicating the threshold meaningfully affects output. A sensitivity analysis or explicit description of the stopping criterion is needed.

- **Biased training objective receives no analysis.** The paper acknowledges the objective is biased (Section 3) and references Appendix D for variance discussion, but provides no analysis of the bias itself — e.g., whether it exactly recovers the true denoising distribution under any condition, or whether pathological cases (repeated tokens, spurious gradients) exist. The method works empirically, so this is not a fatal gap, but it leaves a theoretical loose end.

- **Number of MDM sampling steps for main text results (Table 2) not specified.** Steps are listed for the Figure 6 timing analysis but not for the primary unconditional generation comparison, making it harder to assess whether the comparison favors one method.

### Trivial

- None beyond the specific points above.

## Nice-to-Haves

- Reporting generation diversity metrics (distinct-1/2, self-BLEU) alongside NLL and entropy would help contextualize the text quality comparison.
- A comparison on planing tasks to insertion-based predecessors (Insertion Transformer, Stern et al. 2019) beyond the star graph results would be welcome.
- A sensitivity analysis of the stopping threshold on generation length and quality.

## Removed Points

- **Criticism about missing comparison with improved MDM variants (Ye et al. 2025, Campbell et al. 2024).** These are discussed in Related Work; a direct comparison on every variant is scope-creep for a paper introducing a new method class.
- **Complaints about qualitative examples being in the appendix.** The parser strips appendices; these exist in the original submission.
- **The assertion that the MDM baseline in infilling is "inherently disadvantaged" as a weakness.** This is the point of the comparison — the paper's claim is that ILM offers greater flexibility, which Table 3 supports.
- **Demand for theoretical proofs of the training objective's properties.** The paper is an empirical methods paper; the absence of a full theoretical characterization is not a flaw given the empirical support.
- **Criticism that the paper doesn't discuss failure cases of the biased objective on complex tasks.** Speculative; the paper reports on the tasks it tests.

## Novel Insights

None beyond the paper's own contributions. The observation that counting-based target distributions can substitute for trajectory marginalization in insertion-based denoising is the paper's core insight and is well-articulated.

## Suggestions

1. Add ablation studies on a small-scale planning task (e.g., Star_easy or a simplified zebra puzzle) isolating the stopping classifier, the counting-based objective vs. uniform target, and the insertion parameterization.
2. Report standard errors or confidence intervals for Table 2 and Table 3 results.
3. Revise the abstract's "on par with ARMs" to "competitive with ARMs" to match the paper body's own language and the actual NLL gap on LM1B.
4. Clarify the stopping threshold used during inference and provide a brief sensitivity analysis.
5. Correct the inconsistent explanation of MDM's star-graph failure: attribute it to the fixed-length masking constraint rather than "absolute positions," since DDiT uses RoPE.

## Score and Decision

**Calibration Summary.** Round 1 bracketing placed the paper between 3.5 and 7.5. Weak anchors (<3.5) included low-quality generation papers with scores 2.5–3.0. Middle anchors (3.5–7.5) included FiLM (4.25, reject), COrAL (5.75, reject), SequenceMatch (6.00, accept), and Energy-Based Diffusion LM (6.75, accept). Strong anchors (>7.5) included SAR diffusion models and Transfusion at 7.6–8.0.

Round 2 narrowing searched within (5.0, 7.5) and retrieved: COrAL (5.75, reject), SequenceMatch (6.00, accept), Reparameterized Discrete Diffusion (5.50, reject), Fast Sampling for Discrete Diffusion (5.50, reject), Planned Denoising (5.75, accept), and Retrieval is Accurate Generation (7.00, accept). Reading these in full:

- **FiLM (4.25, reject):** Similar topic (non-causal generation) but much simpler method. **ILM is clearly stronger** — more sophisticated method, broader evaluation, planning tasks.
- **COrAL (5.75, reject):** Order-agnostic modeling with context windows. Messy evaluation, limited novelty. **ILM is clearly stronger** — cleaner method, stronger empirical evidence.
- **SequenceMatch (6.00, accept):** Novel training objective for AR models. Clean paper, comparable quality. **ILM comparable** — broader evaluation but missing ablations SequenceMatch doesn't need.
- **Reparameterized Discrete Diffusion (5.50, reject):** Incremental diffusion variant. **ILM is stronger** — more novel contribution.
- **Planned Denoising (5.75, accept):** Planner+denoiser for discrete diffusion. Mixed reviews (3,6,6,8). **ILM comparable** — both have genuine novelty, similar weakness profiles.
- **Retrieval is Accurate Generation (7.00, accept):** Higher quality paper with iterative self-reinforcement. **ILM is below this anchor** — less polished evaluation.

The paper's genuine novelty and strong planning results place it above the mid-5s, but the missing ablations and lack of statistical rigor prevent it from reaching the 7.0+ tier. The closest anchor is SequenceMatch (6.00).

**Final Score:** 6.0 — A solid accept. The method is novel, the planning-task evidence is clean and compelling, and the text generation/infilling results show consistent advantages over MDMs while being competitive with ARMs. The weaknesses (missing ablations, no confidence intervals, imprecise explanations) are real but addressable and do not undermine the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>