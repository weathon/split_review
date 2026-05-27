Now let me do calibration searches.## Calibration Notes

**Anchors retrieved**

Round 1 (bracketing):
- `Xagys9QD3T.md` — Pseudo-Probability Unlearning — avg 3.00 (Reject). Much weaker; unrelated methodology.
- `hwXUmwJAq5.md` — UGradSL — avg 3.00 (Reject). Much weaker; thin contribution.
- `BJfIDS5LsS.md` — MASIMU — avg 2.50 (Reject). Much weaker.
- `lZRRfupxYn.md` — Mesoscience — avg 3.00 (Reject). Unrelated.
- `fMNRYBvcQN.md` — Jogging the Memory of Unlearned LLMs — avg 6.75 (Accept). The direct predecessor/BLUR-style work that this paper critiques and extends; this paper goes further with a mitigation and mechanism.
- `CIN2VRxPKU.md` — Evaluating Deep Unlearning — avg 5.33 (Reject). Comparable evaluative re-analysis paper, slightly weaker scope.
- `Q1MHvGmhyT.md` — A Closer Look at Machine Unlearning — avg 6.00 (Accept). Methodological critique + new objectives; comparable contribution shape.
- `uDjuCpQH5N.md` — Do Unlearning Methods Remove Information — avg 5.50 (Reject). Related re-evaluation; the paper at hand is broader and offers a mitigation.
- `51WraMid8K.md` — Probabilistic Perspective on Unlearning — avg 8.00 (Accept). Stronger formal framework.
- `gc8QAQfXv6.md` — Function Vectors / Catastrophic Forgetting — avg 9.00 (Accept). Much stronger.
- `PBjCTeDL6o.md` — Unlearning-based Neural Interpretations — avg 8.00 (Accept). Different topic, stronger.
- `SPS6HzVzyt.md` — Context-Parametric Inversion — avg 8.00 (Accept). Different topic.

**Round-1 bracket: between ~5.0 and ~6.5** — solidly in the "methodological critique + new finding + simple mitigation" band where Jogging (6.75) sits above and the Reject-borderline re-evaluation papers sit below.

Round 2 (narrowing):
- `J9Ofr1PmvX.md` — UnSTAR — avg 5.50 (Reject). New unlearning method, similar scope, weaker analysis.
- `xmQuUqSynb.md` — Rethinking Adversarial Robustness in RTBF — avg 5.75 (Reject). Comparable position; new vulnerability + analysis.
- `KvFk356RpR.md` — Unlearning Mapping Attack — avg 4.80 (Reject). Weaker analysis depth.
- `huo8MqVH6t.md` — Rethinking LLM Unlearning Objectives (G-effect) — avg 6.00 (Accept). Same "rethinking + gradient lens" archetype. The paper at hand has comparable empirical breadth and a working mitigation, but its central terminological framing ("syntactic" = Levenshtein) is weaker than G-effect's formal analysis.
- `wAemQcyWqq.md` — Oblivious Unlearning by Learning — avg 5.67 (Reject).
- `3p4raemLAH.md` — Targeted Unlearning via SLUG — avg 5.75 (Reject).

The paper sits closest to "Rethinking LLM Unlearning Objectives" (6.00, Accept) and "Do Unlearning Methods Remove Information" (5.50, Reject), with comparable methodological critique strength but a notably over-claimed central label and a missing size-matched ablation that the anchors do not share. Final score lands between these two anchors.

---

## Summary
The paper revisits the claim from the BLUR benchmark that "topical relevance" drives benign relearning of unlearned LLMs and argues instead that *syntactic similarity* — operationalized as normalized Levenshtein similarity — is the primary driver. It supports this with (i) a re-evaluation of BLUR with a standardized step budget on WMDP/WHP/RWKU, (ii) a controlled TOFU setup contrasting "topically relevant" vs. "syntactically similar" relearn sets across GA, NPO, and SCRUB, (iii) a mechanistic "loss ratio" analysis between template and keyword tokens, and (iv) a simple mitigation — "syntactic diversification" — that paraphrases the forget set with GPT-4o, improving robustness to relearning and retain-set utility on TOFU.

## Strengths
- **Methodological critique of BLUR is genuinely useful** (§4, Figs. 2–3): the paper points out that BLUR's relearn-tier sets differ in size and that recovery is non-monotonic, and shows that under a fixed step budget evaluated at the best step the supposed $D_{hi} > D_{mid} > D_{low}$ ordering largely collapses on WMDP/WHP/RWKU. This is a real, transferable observation about how relearning experiments should be controlled.
- **Controlled TOFU contrast isolates a clean qualitative effect** (§5.2–5.3, Fig. 4): when the relearn set shares the QA template but uses *different* authors ($D^{syntactic}_{relearn}$), keyword recovery is consistently stronger than when the relearn set shares the *same authors* but a different format ($D^{topic}_{relearn}$). The contrast is consistent across GA, NPO, and SCRUB.
- **The loss-ratio mechanism is the strongest idea in the paper** (§6, Fig. 6): explicitly partitioning answer tokens into template vs. keyword and showing that unlearning under GA/NPO/SCRUB drives the template loss far above the keyword loss gives a concrete, falsifiable mechanism for why template-aligned relearn data restores the keyword.
- **Diversification yields a real improvement on both axes** (§7, Fig. 8, Table 2): on TOFU, unlearning with $D'_{forget}$ delays/eliminates keyword reemergence under syntactic relearning *and* substantially improves retain-set utility (e.g., Retain Avg. 0.16 → 0.31) — a non-trivial joint gain over the usual forget/utility trade-off.
- **Representation + gradient analysis ties the mechanism to optimization** (§6, Fig. 5): syntactically similar sets show much higher gradient cosine to the target than topically relevant sets, linking the loss-ratio story to an optimization-level pathway.

## Weaknesses

### Fatal
None. The paper has real evidential gaps but the core empirical observation (template-aligned relearn data restores keywords; diversification mitigates it on TOFU) is supported by the figures presented.

### Major
- **"Syntactic similarity" is operationalized as character-level Levenshtein, not syntax.** §5.1 defines $\text{Sim}$ as $1 - d_{\text{lev}}/\max(|s_1|,|s_2|)$ — surface-string edit distance, not parse/dependency structure. Combined with the TOFU construction in §5.2 (the "syntactic" relearn set is "name-format questions about retain authors" — i.e., the *same QA template plus the same slot-type filler*), the contrast the paper actually demonstrates is "matching QA-template-plus-slot-type" vs. "non-matching-template." Calling this "syntactic" both overclaims (it is not parse-level) and underclaims (template-and-slot alignment is a more specific, more mechanistic claim, which §6 effectively articulates). The framing affects how the abstract, §1, §5.4, and §8 read.
- **§5.4's reanalysis of BLUR does not produce the positive evidence claimed.** Table 1 reports syntactic-similarity differences of ~0.02–0.05 across the three BLUR tiers (e.g., WHP: 0.1894 / 0.1767 / 0.1818), and §4 simultaneously argues that BLUR's recovery ordering largely *disappears* once budget is controlled. The paper cannot both claim that BLUR's ordering is an artifact (§4) and that the residual ordering is explained by these very small syntactic-similarity differences (§5.4). At minimum §5.4 should be reframed as "topical-relevance ordering is not predictive of Levenshtein-similarity ordering" rather than as positive support for syntax.
- **The critical control for $D'_{forget}$ — size and coverage matched — is missing.** §7.1 says $D'_{forget}$ is built by generating *multiple* GPT-4o paraphrases of each $D_{target}$ query, so it is larger than $D_{forget}$ and covers more query templates. Figure 8 and Table 2 compare against $D_{forget}$ only. Without a matched-size dupe of $D_{forget}$ and/or a low-diversity paraphrase baseline (synonyms only, template preserved), the mechanism cannot be attributed specifically to *template diversification* rather than "more updates over more query formats, one of which happens to overlap with the relearn template." This is a real evidential gap for the central method claim.

### Minor
- **Mechanism evidence is concentrated on TOFU, whose construction is unusually template-uniform.** The loss-ratio analysis (§6, Fig. 6) is mechanistically tight because TOFU is 4,000 QA pairs over 200 authors with near-identical phrasing — exactly the regime where template suppression should dominate. Evidence that the same template/keyword imbalance shows up on a less templated benchmark (the BLUR results in §4 are at most weak positive evidence) would substantially strengthen generality.
- **Keyword-based Relearn Success Rate may inflate "recovery" in the syntactic condition.** §5.2 scores 1 when the *target author's* full name appears in the output, but $D^{syntactic}_{relearn}$ explicitly trains the model to answer "What is the full name of the author born in …?" with a full name (about retain authors). It would tighten the analysis to report what fraction of "successes" are the original target authors' names vs. any plausible full name surfaced from the relearn set.
- **No variance reporting in Figures 2–4 and 8.** Some of the cross-tier gaps in §4 (Figs. 2–3) and the comparisons in Fig. 8 look small enough that seed-level error bars would change the interpretation of "topical ordering disappears" vs. "topical ordering shrinks."
- **§8 "filtering services can detect topic but not syntactic overlap" is plausibility, not evidence.** Auditing for QA-template overlap is not obviously harder than auditing for entity overlap, and the paper provides no analysis to support this deployment claim.

### Trivial
- The example in §6 puts the `[INST]` tag in a position that does not match the standard Llama-2-chat template — a minor presentation issue that does not affect the analysis.

## Nice-to-Haves
- Re-run the loss-ratio measurement on at least one BLUR benchmark; if the template/keyword imbalance reproduces there, the mechanism generalizes beyond TOFU.
- Add a robustness check using a real syntactic metric (constituency/dependency-tree kernel, mentioned in Appendix I) alongside Levenshtein for §5.4's Table 1; this directly counters the "you measured edit distance, not syntax" reading.
- Add a "template-preserving paraphrase" diversification baseline (varied vocabulary, fixed template) — the mechanistic prediction is that the loss ratio should *not* converge to 1 in that condition.
- Reframe the paper around the loss-ratio mechanism (§6) rather than the syntactic-vs-topical framing; the loss-ratio claim is sharper, more falsifiable, and less dependent on what "syntactic" means.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- "The strong, mechanistically-grounded claim is therefore well-supported only on a benchmark whose construction is unusually friendly to it" framed as fatal — kept as Minor because it is real but does not invalidate the on-TOFU finding, and §4's standardized-budget result on three BLUR benchmarks is positive even if interpretive.
- "Diversification cannot be attributed to anything beyond training on more query formats" as a fatal flaw — kept as Major (the actual evidentiary gap) rather than fatal, because the on-figure improvements (Fig. 8, Table 2) and the loss-ratio convergence to 1 (Fig. 9 top) are non-trivial and consistent with the mechanism, even if not isolated from the size confound.
- Strength Finder's "Reinterpretation of BLUR's results via syntactic similarity (§5.4)" listed as a *core* strength — moved here because §5.4's numerical separations in Table 1 are too small to carry this weight, and §4 simultaneously argues the BLUR ordering is largely an artifact, undercutting the §5.4 reinterpretation.

## Novel Insights
The most novel observation surfaced by the reviews is the *loss-ratio between template tokens and keyword tokens* as a diagnostic for *which* part of a templated forget instance unlearning is actually suppressing. Reframed cleanly — "unlearning on rigidly templated forget sets concentrates suppression on the template, leaving keyword suppression weak and the model recoverable by any data that reinstates the template" — this is a falsifiable mechanism that, if it holds on non-TOFU benchmarks, is a publishable contribution on its own and a better-scoped headline than "syntactic vs. topical."

## Suggestions
- Reframe the central claim around the loss-ratio mechanism (§6) and demote "syntactic similarity" to a correlated surface-level signature rather than the headline driver.
- Replace or supplement Levenshtein with a parse-tree/dependency-based similarity in §5.4 to defuse the "you measured edit distance, not syntax" objection.
- Run the size-matched and template-preserving paraphrase ablations for $D'_{forget}$ so that diversification's improvement in Fig. 8 and Table 2 is causally attributed to template-breaking rather than to broader coverage.
- Replicate the loss-ratio measurement on at least one BLUR benchmark (WHP or RWKU) so the mechanism's generality is not solely a TOFU phenomenon.
- Report seed-level variance in Figs. 2–4 and 8; some of the tier-level gaps that §4 leans on may be inside seed noise.

## Evaluation Axes
- **Originality:** Moderate. Reframing relearning vulnerability in terms of template/keyword suppression is a fresh angle, but operationally it overlaps with prior "relearning attack" work and is partly anticipated by the BLUR setup it critiques.
- **Importance of the question:** High. Unlearning robustness is a central, deployment-relevant open problem.
- **Support for claims:** Mixed. The §4 critique and §5.3 TOFU contrast are well-supported; the §5.4 BLUR reinterpretation is weak and the §7 mitigation lacks a size-matched control.
- **Soundness of experiments:** Reasonable but uneven — multiple unlearning methods and a clean TOFU contrast, but a single-benchmark mechanism story and missing ablations.
- **Clarity:** Good overall; the figures are readable and the argumentative arc is clear.
- **Value to community:** The methodological critique of BLUR's protocol and the template-suppression mechanism are both worth circulating; the headline "syntactic" framing is the weakest piece and is what an unrevised version would be (justifiably) criticized for.

## Score and Decision

Round-1 bracket: ~5.0–6.5, sitting near the "Jogging" / "A Closer Look" / "Rethinking LLM Unlearning Objectives" / "Do Unlearning Methods Remove Information" cluster.

Round-2 narrowing: the paper is comparable in scope to *Rethinking LLM Unlearning Objectives* (6.00, Accept) and *A Closer Look* (6.00, Accept) but with a more over-claimed central framing ("syntactic" = Levenshtein) and a missing size-matched ablation that those anchors do not share, pulling it below the 6.0 line. It is meaningfully stronger than *Unlearning Mapping Attack* (4.80) and at least as strong as *Do Unlearning Methods Remove Information* (5.50, Reject) because of the additional mitigation and mechanism analysis. This places it just below the acceptance line — a borderline-reject anchored slightly below 6.0.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>