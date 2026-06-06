## Summary

This paper introduces the Task-Method-Knowledge (TMK) framework from cognitive science as a structured JSON prompt for LLM planning tasks, evaluated on the PlanBench Blocksworld benchmark across five OpenAI models (GPT-4, GPT-4o, o1-mini, o1, GPT-5) and three obfuscation levels. The headline empirical finding is that TMK improves o1 on Random Blocksworld from 31.5% to 97.33%, and that all three tested LRMs (but no LLMs) show a "performance inversion" under TMK whereby Random becomes easier than Mystery. The paper interprets this inversion as evidence that TMK steers models from linguistic to symbolic/code-execution reasoning.

---

## Rebuttal Assessment

### Weakness 1: Content/format confound
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author points to Section 5.2.1's argument that pure content enrichment would predict "uniform gains across domains," so the inversion itself is evidence for something beyond content. This argument exists verbatim in the paper (line 282). However, the rebuttal's reasoning is incomplete: a content × semantic-interference interaction can explain the inversion just as well. Content enrichment (richer preconditions/effects) would help most when semantic interference is absent (Random) and least when misleading semantics actively interfere (Mystery), producing the exact inversion pattern without invoking any structural/format mechanism. The author does not address this alternative. No new experiments were conducted.
- **Score impact:** Weakness unchanged

### Weakness 2: Modified extractor creating unvalidated advantage on headline result
- **Author's response:** Partially address
- **Assessment:** Unconvincing — The rebuttal restates the paper's existing Section 3.2 justifications (ICAPS citation, sequential correctness preserved, Valmeekam et al. 2023c as precedent) and explicitly acknowledges the gap: "a side-by-side comparison…would allow readers to bound the effect…we acknowledge this is a gap." No new data, no dual-extractor comparison. The reviewer's core concern — that the TMK JSON structure may produce outputs whose formatting artifacts are exactly what the lenient extractor tolerates — remains entirely unaddressed empirically. The 97.33% headline number is still unvalidated.
- **Score impact:** Weakness unchanged

### Weakness 3: TMK zero-shot not tested
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The rebuttal correctly points to Section 5.1's argument (plain-text zero-shot > plain-text one-shot, hence the conservative baseline direction is correct) and the deliberate mismatch of the one-shot example (verified at line 181: "random and not tailored to the problem at hand"). These were already in the paper and reduce the plausibility of the format-teaching explanation. However, the author explicitly concedes: "Testing TMK zero-shot was not done, and we acknowledge it would have provided a cleaner decomposition." The one-shot/zero-shot asymmetry for the TMK format specifically remains unresolved.
- **Score impact:** Weakness unchanged (downgraded marginally — the paper's existing defense is reasonable though incomplete)

### Weakness 4: No statistical significance testing
- **Author's response:** Acknowledge
- **Assessment:** Honest acknowledgment with no new evidence. The label "significantly improvements" in Table 2 without any test or sample size remains in the paper. For large gains this is inconsequential; for 3–9 pp gains it matters.
- **Score impact:** Weakness unchanged

### Weakness 5: Steering mechanism hypothesis overstated
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author acknowledges the conclusion language (line 300: "This confirms that TMK acts as a symbolic scaffold, effectively steering reasoning models toward formal code-like manipulation") is stronger than the evidence warrants, and points to the hedged body text (Section 5.2.1: "should be tested in models that have transparent reasoning tokens as part of future work"; Section 6: "the cause of that increase is left to future work"). The tension between the strong conclusion and the hedged body is real and acknowledged. No revision was submitted.
- **Score impact:** Weakness unchanged (presentation issue, no revision)

---

## Strengths
- **Consistent inversion across all three LRMs**: Under TMK, all three LRMs (o1: Random 97.33% > Mystery 83.3%; o1-mini: Random 27% > Mystery 16.83%; GPT-5: Random 99.0% > Mystery 98.3%) exhibit the inversion, while neither LLM does. This 3/3 vs 0/2 split is a real and interesting empirical pattern (Table 2 verified).
- **Conservative baseline design**: The paper explicitly argues and demonstrates (in OSF results) that plain-text zero-shot > plain-text one-shot, so it compares one-shot TMK against zero-shot plain text, disadvantaging TMK directionally (lines 178–182, verified).
- **Transparent disclosure**: Section 3.2 openly discloses the extractor modification, its rationale, and its scope, providing readers the information needed to assess it even though no validation comparison is reported.
- **Large headline gains**: The o1 Random Blocksworld improvement (31.5% → 97.33%, +65.8 pp) is among the largest reported in LLM planning literature.

---

## Weaknesses

### Fatal
None.

### Major
- **Content/format confound**: The TMK prompt simultaneously adds richer semantic content (explicit preconditions, postconditions, teleological links — Sections 3.1.1–3.1.3, Figure 1) and reformats into JSON. The "symbolic steering" hypothesis and the "content enrichment plus semantic-interference differential" hypothesis both predict the observed inversion. No ablation holds one variable constant. The author's Section 5.2.1 argument ("uniform gains expected under content-only") is not logically sound because content × semantic-interference interaction predicts non-uniform gains without invoking structure effects. Weakness fully persists.

- **Unvalidated modified extractor for headline result**: The paper modifies the PlanBench extraction function to accept symbol variants ("-", "_"), word variants ("obj"), and action-name formatting variations for Random Blocksworld specifically (Section 3.2, lines 183–191). The TMK JSON/code-like output structure may naturally produce the formatting variants the modified extractor is more tolerant of, inflating TMK gains on Random relative to the plain-text baseline. No side-by-side comparison of original vs. modified extractor for any model is reported. The 97.33% headline result is unvalidated. The author explicitly acknowledges this as "a gap."

- **TMK zero-shot not tested**: The contribution of the TMK structural framework cannot be separated from the contribution of the in-context example. The author's defense (plain-text zero-shot > one-shot baseline direction; deliberately mismatched example) is reasonable but does not close the question, particularly in interaction with the modified extractor. Author explicitly acknowledges this.

### Minor
- **No statistical testing for small gains**: Table 2 labels gains as "significant" without sample sizes, confidence intervals, or formal tests. Gains of 3–9 pp (GPT-4 Classic: 34.6% → 39.7%; GPT-4 Mystery: 0% → 3.8%; GPT-4o Mystery: 0% → 5.5%) cannot be distinguished from noise at typical PlanBench sample sizes. Fully acknowledged by authors.
- **Mechanistic language stronger in conclusion than in body**: The conclusion (line 300) states the results "confirm" the symbolic steering hypothesis while Section 5.2.1 says it "should be tested… as part of future work." This inconsistency is acknowledged but not revised.

### Trivial
None.

---

## Nice-to-Haves
- A "rich plain-text" ablation condition providing all TMK content (preconditions, effects, teleological links) in natural-language prose would be the single most informative follow-up.
- A side-by-side table comparing original and modified PlanBench extractor results for Random Blocksworld would validate or qualify the headline number.
- TMK zero-shot condition to separate structural effect from example effect.
- Evaluation on Logistics domain within PlanBench to establish generalizability beyond Blocksworld.

---

## Novel Insights
The consistent performance inversion across all three tested LRMs — but not in either tested LLM — is a genuinely novel empirical finding not previously documented in PlanBench literature. The 3/3 LRM inversion and 0/2 LLM non-inversion pattern is striking and warrants serious investigation. The most likely mechanistic explanations (code-pathway activation vs. content enrichment differential vs. cognitive scaffolding) remain unresolved by the current experiment, but the differential response of reasoning-specialized models to structured formal prompts hints at something meaningfully different in how LRMs process formal representations. The paper's inability to isolate the mechanism is a legitimate gap, but the empirical observation itself merits follow-up with properly controlled ablations.

---

## Suggestions
1. **Priority**: Run the content-controlled ablation — same precondition/effect/teleological information presented in natural English prose, compared directly to TMK JSON. This single experiment would substantially clarify whether format or content drives the inversion.
2. **Priority**: Re-run all Random Blocksworld conditions with both the original and modified extractor and report both in a comparison table. This would bound the extractor's contribution to the headline result.
3. Run TMK zero-shot (no in-context example) to isolate the structural prompt from the example contribution.
4. Revise the conclusion to match the hedged language already present in Section 5.2.1 — replace "confirms" with "is consistent with."
5. Add a supplementary table reporting sample sizes per condition and confidence intervals for all results in Table 2.

---

## Score and Decision

**Post-rebuttal calibration:**

The author's rebuttal is honest, non-adversarial, and presents the strongest available defense using existing paper content. All five weaknesses from the original review are explicitly acknowledged. No new experiments were run. The three Major weaknesses are unchanged:

1. The content/format confound argument in the rebuttal is the same argument already present in Section 5.2.1 — the reviewer already read it and still found it insufficient. Verifying the paper confirms the reviewer was right: the "no uniform gains expected" argument does not rule out a content × semantic-interference interaction account.
2. The modified extractor gap is explicitly conceded with no new evidence.
3. The zero-shot TMK gap is explicitly conceded with no new evidence.

The rebuttal introduces no reason to revise the original assessment upward or downward. The paper remains a genuine empirical contribution with striking headline numbers, hampered by methodological gaps that prevent acceptance of its central interpretive claim.

**Original score: 3.5 — maintained.**

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>