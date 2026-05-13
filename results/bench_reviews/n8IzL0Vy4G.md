## Summary
The paper formalizes a three-level "knowledge preference" hierarchy (instruction ≻ context ≻ parametric), assembles a benchmark by adapting IfQA, MQuAKE, and MRQA, and proposes a Wikidata/Wikipedia-grounded synthesis pipeline that produces ~7.4K instruction-tuning examples (counterfactual single- and multi-hop QA) for Mistral-v0.3-7B. Fine-tuning on Alpaca + the synthesized data yields large gains on the constructed benchmarks, including 28.48% → 89.36% F1 on the MQuAKE adaptation and 50.71% → 77.85% F1 on IfQA with mixed passages.

## Strengths
- **Unified problem framing** (Sec. 2 / Sec. 6.1): instruction/context/parametric ordering provides a clean lens that subsumes RAG faithfulness, in-context knowledge editing, and counterfactual QA. The framing helps organize previously fragmented threads.
- **Well-specified synthesis pipeline** (Sec. 4.1–4.3): BFS over Wikidata, recursive counterfactual edits that propagate downstream entity changes (line 170), and probe-then-filter for context-vs-parametric conflict cases (line 219). The recursive edit propagation in particular is a non-trivial design.
- **Internalization vs. prompting**: the trained model achieves ~89 F1 on MQuAKE-Adapted with the normal prompt, essentially matching its explicit-prompt score (89.36 vs. 89.49, Table 2), whereas GPT-4o needs explicit prompting to jump from 86.46 to 93.37. This is consistent with the claim that the hierarchy is internalized rather than prompt-elicited.
- **Robustness to noisy context on IfQA**: while baselines drop sharply from gold to mixed passages (Mistral-Alpaca 67.98 → 50.71), the trained model stays roughly stable (80.53 → 77.85, Table 1). The "−Random Noise Contexts" ablation (Table 3) corroborates that this is an effect of the training-data design.
- **Useful negative result on prompting**: showing that explicit "Assumption-in-X" prompting barely helps open-source models, and can even degrade in mixed-passage settings, is informative.

## Weaknesses

### Fatal
None.

### Major
- **Train–test distributional coupling on the flagship benchmark.** The MQuAKE-Adapted test instances and the multi-hop training instances follow nearly the same recipe: both mine Wikidata fact chains, apply counterfactual edits to intermediate triples, verbalize triples into supporting passages via a GPT model, and use the same templated assumption-in-question format. The paper itself notes (line 444) that MQuAKE-Adapted "is not hard in terms of multi-hop reasoning … it essentially requires testee LLMs to follow the knowledge preference hierarchy." Without an OOD counterfactual evaluation (e.g., human-authored counterfactual prompts over a different template), it is hard to separate "learned the hierarchy" from "learned the format/distribution." This directly threatens the strongest headline number (28.48 → 89.36).
- **Non-comparable Counter-Memory subsets in Table 4.** Table 5 shows the Counter-Memory subset is constructed independently for each model (e.g., BioASQ 661 vs. 610; RE 1,892 vs. 1,787). Since each model's subset excludes instances it already gets right parametrically, the \Ours subset systematically differs from the Alpaca subset. The $\mathbb{P}(U_c)/\mathbb{P}(U_i)$ comparison in Table 4 therefore measures the two models on different populations. A shared (intersection or union) instance set, or per-instance pairing, is required to support the claim that \Ours "outperforms the baseline in correcting wrong parametric answers" (Sec. 5.1).
- **No apples-to-apples training-data baseline isolating the counterfactual design.** \Ours is Alpaca (52K) + 7.4K synthesized counterfactual/conflict instances; the baseline is Alpaca alone. Without an "Alpaca + 7.4K matched-volume, non-counterfactual context-grounded QA" baseline, the gain cannot be attributed specifically to the counterfactual/edit design (which is the methodological novelty). The ablations in Table 3 vary noise/derivation/shuffling but never substitute non-counterfactual instances.
- **Single base model.** All \Ours results are on Mistral-v0.3-7B. The abstract/intro claim that 7.4K examples "unlock the knowledge preference ability of open-source LLMs" (plural) is supported by a single data point. Llama-3, Llama-2, Qwen-2 appear only as reference baselines; \Ours is never re-applied to them.

### Minor
- **Scope/framing overstretch.** Sec. 1 motivates the hierarchy via personalized search/recommendation and "user preferences," but the experiments only cover (i) counterfactual hypothetical conditions and (ii) edit-style fact overrides. Personalization is never evaluated. The "user preference" framing should be tempered or operationalized.
- **Training implicitly assumes context is always trustworthy.** The Sec. 2 footnote (line 85) waves away the case where retrieved context is misleading, and the training pipeline filters in the opposite direction (filters out cases the LLM gets right parametrically, line 219). The resulting model is taught to obey context essentially unconditionally, which is a real limitation for deployed RAG where retrieval errors and misinformation are central concerns. This is worth flagging as a limitation rather than dismissing.
- **The −Random Noise ablation is more important than the text suggests.** Removing random-noise contexts drops Mixed-Passages F1 from 77.85 → 68.99 (−8.9). Most of the mixed-passage robustness may come from "learn to ignore distractors" rather than from the preference hierarchy per se. This deserves discussion in text.
- **No variance estimates.** No seeds or confidence intervals; some differences in Table 3 (e.g., 77.76 vs. 80.55) are small and may be within noise but are read as conclusive.

### Trivial
- None substantive enough to report.

## Nice-to-Haves
- An OOD counterfactual evaluation (e.g., a benchmark where contexts are not GPT-synthesized from Wikidata triples) would dramatically strengthen the headline claim.
- Apply \Ours to at least one additional base model (Llama-3-8B is the obvious candidate).
- Add an evaluation where retrieved context is itself wrong, to characterize how much the model has been trained into unconditional context obedience.
- Failure-mode breakdown on MQuAKE-Adapted: when models fail, do they revert to the parametric answer, hallucinate, or refuse? Aggregate F1 hides this.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- **Harsh critic's "hierarchy conflates three phenomena" critique.** This is a framing-only point; the paper explicitly notes its three settings (Sec. 2 and Sec. 1, lines 37) and only operationalizes (i) and (ii). Already partially captured under the scope-creep minor weakness; the stronger "category error" claim overstates and is set aside.
- **"GPT-4o test contexts synthesized by GPT-3.5, contexts no longer naturalistic" (Sec. 3.1 critique).** The paper is upfront about this trade-off (lines 100–107); the design is a deliberate choice to produce sharper conflicts. Reasonable to mention but not a blocker.
- **Strength: "targets an important problem / important research question."** Generic; dropped per filtering rules.
- **Strength: "controllable multi-hop data synthesis from structured sources."** Kept implicitly via the synthesis-pipeline strength but the standalone framing is partly generic.

## Novel Insights
None beyond the paper's own contributions. The most interesting empirical observation — that random-noise contexts in training drive most of the mixed-passage robustness — is in the paper but under-discussed.

## Suggestions
- Re-do Table 4 on the intersection of the two Counter-Memory subsets (or pair instances) so the comparison is well-defined.
- Add an "Alpaca + 7.4K non-counterfactual context QA" training baseline at matched volume.
- Add an OOD counterfactual evaluation (non-Wikidata-template) for MQuAKE-style claims.
- Apply \Ours to a second base model.
- Either drop the personalization framing or add a personalization-conflict evaluation.
- Report multi-seed variance for the trained model.

---

**Evaluation summary.** *Originality:* moderate — the unified framing is a reorganization rather than a new mechanism; the synthesis recipe combines known ingredients with a non-trivial recursive edit propagation. *Importance:* the problem is timely and applied. *Claims vs. support:* the strongest claim (instilling a general hierarchy) is undercut by train/test distributional coupling, a non-comparable Table 4 comparison, and a single base model. *Soundness:* main experiments are reasonable, but the Counter-Memory comparison has a methodological flaw and the counterfactual-design contribution is not isolated. *Clarity:* generally clear; some key ablation findings are under-discussed. *Value:* the synthesis recipe and benchmark consolidation will be useful to practitioners working on RAG/edit faithfulness for 7B-scale models.

## Score and Decision

Anchors retrieved (read in full: t21RmVmJrT, Igm9bbkzHC, SPS6HzVzyt, hUD9ugK2OH):
- `t21RmVmJrT.md` (avg 5.00, Reject) — Closest topical neighbor: parametric vs. contextual knowledge interplay; rejected at borderline. Very similar in scope and tone to this paper; comparable level of empirical evidence and similar concerns about generality.
- `Igm9bbkzHC.md` (avg 6.75, Accept) — Context sensitivity "knob"; cleaner mechanistic contribution than the paper under review.
- `sl4hOq9wm9.md` (avg 5.50, Reject) — In-context vs. in-parameter knowledge injection; similar borderline outcome.
- `SPS6HzVzyt.md` (avg 8.00, Accept) — Context-parametric inversion during instruction tuning; sharper, more insightful empirical finding than this paper.
- `hUD9ugK2OH.md` (avg 5.75, Reject) — Synthetic context extension via retrieval heads; comparable concern about synthetic data not transferring, mirrors the train/test overlap concern here.
- `8m7p4k6Zeb.md` (avg 6.00, Accept) — Fine-tuning on synthetic key-value retrieval; weaker but cleaner story than this paper, accepted.
- `RjYKTQ0L0W.md` (avg 5.33, Accept) — Content-grounded synthetic data generation; similar method-paper character.
- `jl9lHkQrrI.md` (avg 3.50, Reject) — Industrial-assets synthetic data fine-tuning; substantially weaker than this paper.
- `m9wG6ai2Xk.md` (avg 6.00, Accept) — MQuAKE-Remastered; more focused contribution; benchmark-side rather than method-side.
- `INFfvQArFY.md` (avg 6.25, Reject) — Locate-then-edit multi-hop; weighted higher than this paper but still rejected.
- `YpWV7XRmFB.md` (avg 4.00, Reject) — Edited-fact decoding; weaker than this paper.
- `X5rO5VyTgB.md` (avg 5.60, Accept) — Unstructured knowledge editing; similar borderline.
- `jOmk0uS1hl.md` (avg 8.00, Accept) — "Training on the test task"; directly relevant to the central concern about distributional overlap in this paper.
- `rAylWUIKtu.md` (avg 4.25, Reject) — Benchmark inflation / contamination.
- `PtnttTKgQw.md` (avg 5.00, Reject) — Clever-Hans features in benchmarks.
- `590yfqz1LE.md` (avg 6.75, Accept) — Non-adversarial reproduction.
- `Iyrtb9EJBp.md` (avg 8.00, Accept) — Trustworthiness in RAG with grounded attributions; cleaner empirical story than this paper.
- `K2jOacHUlO.md` (avg 7.25, Accept) — Situated faithfulness; directly addresses the "context can be wrong" failure mode this paper sidesteps.
- `Jjr2Odj8DJ.md` (avg 6.25, Accept) — Sufficient context for RAG.
- `tBZK9BI2GZ.md` (avg 4.50, Reject) — Multimodal knowledge conflicts; weaker.
- `3UB4NaEb1g.md` (avg 4.50, Reject) — Certifying knowledge comprehension; weaker.
- `OdoS6cH8MP.md` (avg 2.00, Reject) — Data valuation; far weaker.
- `kDakBhOaBV.md` (avg 4.00, Reject) — Diversity coefficient; weaker.

Calibration: the paper sits closest to `t21RmVmJrT` (5.00) and `sl4hOq9wm9` (5.50) — credible empirical work on context-vs-parametric with framing/generality issues. It is clearly above the 3.5–4.0 anchors (no real methodological novelty there). It is below the 6.0+ anchors (`Igm9bbkzHC`, `K2jOacHUlO`, `SPS6HzVzyt`), which deliver sharper mechanistic findings or directly tackle the very failure mode this paper sidesteps (untrustworthy context). The Table-4 subset issue and the train/test recipe coupling are real but not fatal.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>