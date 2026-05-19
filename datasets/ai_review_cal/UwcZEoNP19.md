- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6
Now I have a thorough understanding of the paper and the reviews. Let me write the final consolidated review.

## Summary

The paper proposes TIDE (Triple-Inspired Decomposition and vErification), a method that uses the structured form of (head entity, relation, tail entity) triples to improve both question decomposition and answer verification in LLM-based TableQA. The key ideas are: (1) forcing the LLM to extract entities and relations into triples covers more critical information than direct decomposition, and (2) comparing answer-derived triples against question-derived triples provides a structural consistency check that avoids the known pitfalls of LLM self-correct verification. TIDE is compatible with both Direct Prompting and Agent reasoning modes, and their joint majority voting achieves SOTA results on WikiTableQuestions (62.97%) and TabFact (89.82%).

---

## Strengths

- **SOTA results on two standard TableQA benchmarks.** On WikiTableQuestions, TIDE-DP&Agent achieves 62.97% exact-match accuracy, surpassing the previous best ReAcTable (60.5%) and strong baselines like BINDER (58.6%) and DATER (56.1%). On TabFact, it achieves 89.82%, improving over Cabinet (88.5%). (Tables 1 and 2)

- **Ablation confirms both decomposition and verification components contribute.** Table 3 shows that removing TIDE-Decomposition from TIDE-DP drops accuracy on WTQ from 55.96% to 51.87%, and from TIDE-Agent from 57.19% to 54.15%. Removing TIDE-Verification yields smaller but consistent drops (e.g., TIDE-DP from 55.96% to 54.00%). This provides causal evidence that both triple-structured components add value.

- **Verification approach avoids the known self-correct bias.** The paper replaces LLM self-correct (which prior work shows can bias toward contradictory responses) with an explicit structural comparison between answer triples and question-decomposition triples. The ablation confirms that this verification improves accuracy across all four configurations, demonstrating an alternative to self-correct that empirically works.

- **Method is flexible across two reasoning paradigms.** TIDE integrates with both DP (textual CoT reasoning) and Agent (symbolic code execution) modes, and the joint majority voting consistently yields the best results. The analysis of table size (Figure 5) further shows that TIDE-Agent handles large tables better than TIDE-DP, consistent with the expectation that code-based table access is more robust than serialized text.

---

## Weaknesses

### Fatal
None.

### Major

- **Verification checks structural consistency, not factual correctness — the paper oversells what it does.** The verification condition (Eq. 7–10) accepts an answer if the relation matches AND at least one entity (head or tail) matches between the answer triple and the question triple. In the paper's own examples, the question triple has a variable placeholder (𝕊, stay in, office) where the tail entity "office" is a constant. An answer triple (John, stay in, office) would pass verification even if the correct answer is Mary — the verification only confirms the answer is *on-topic* (right relation, right context entity), not that it is *factually correct* against the table. The paper repeatedly claims this "validates the correctness of the answer" (abstract, Section 4.3), which overstates what the mechanism actually guarantees. The ablation shows the verification does help empirically, which is valuable, but the paper should acknowledge this theoretical limitation rather than presenting the verification as a definitive correctness check. The paper provides no analysis of the verification's precision or recall (e.g., how often it correctly flags errors vs. misses them).

- **The experimental design does not fully isolate the effect of triples from confounding factors.** The ablation (Table 3) removes TIDE components entirely rather than replacing them with non-triple alternatives. A cleaner isolation would compare: (a) full TIDE, (b) same pipeline with *direct* (non-triple) decomposition into the same number of sub-questions, (c) same pipeline with LLM self-correct verification instead of triple verification. Without these controls, it is possible that some of the gain attributed to triples actually comes from having *any* structured decomposition or from majority voting (5 answers per mode are generated). The baselines in Tables 1–2 (BINDER, DATER, ReAcTable, Cabinet) provide cross-system comparisons, but the paper's central claim — that the *triple structure itself* drives the improvement — would be more convincingly supported by a controlled ablation that varies only the presence/absence of triple structure while keeping everything else fixed.

### Minor

- **The claim of "1.35%–20%" improvement is an apples-to-oranges range.** The 20% upper bound comes from comparing to weak baselines (e.g., SASP at 36.8%), while the 1.35% is against the best prior work (ReAcTable). This range gives an inflated impression of the gains. The meaningful comparison is the ~2.5 pp improvement over the previous best on WTQ and ~1.3 pp on TabFact, which are real but modest.

- **No analysis of triple extraction quality or error propagation.** The method makes two LLM calls (entity/relation extraction → triples → sub-questions) before any reasoning. The paper reports no success rate for these steps, no examples of malformed triples, and no analysis of how errors in early stages propagate. Decomposition quality is cited as key (Table 3), so understanding its failure modes is important.

- **Verification relies on exact string matching** (Eq. 7–10 uses `=`). The paper does not discuss how synonyms, paraphrases, or near-matches are handled (e.g., "stayed in" vs. "served in"). For a method whose core mechanism is entity/relation comparison, this is a non-trivial practical concern.

- **Evaluated on only two datasets and one LLM (GPT-3.5).** Results on more recent benchmarks (HybridQA, FeTaQA) or with stronger models (GPT-4) would strengthen generality claims.

### Trivial

- None.

---

## Nice-to-Haves

- **Controlled ablation with non-triple decomposition:** Compare TIDE's triple-based decomposition against a direct decomposition ("break this question into sub-questions") with the same number of sub-questions, keeping DP/Agent reasoning and verification fixed. This would directly test whether the triple structure adds value beyond decomposition itself.
- **Replace verification removal with LLM self-correct in ablation:** Instead of removing verification entirely ("w/o TIDE-V"), replace it with LLM self-check to directly compare the two verification approaches.
- **Precision/recall analysis of verification:** Report how often verification catches an error, how often it misses one, and how often it falsely flags a correct answer.
- **Entity matching robustness:** Discuss or experiment with fuzzy/semantic matching for entity comparison.

---

## Removed Points

These points were flagged by the reviewers but are removed or downgraded from the main weakness list:

1. **Critic's claim that verification flaw is "structural, not fixable by additional experiments alone" and "fatal."** *Removed as overstatement.* The verification is a structural consistency check (not a table-level factual check), and the ablation empirically confirms it improves accuracy. Calling it "fatal" is not supported by the evidence on the page; the issue is real but major, not fatal.

2. **Critic's claim that "the second challenge [self-correct bias] is not really addressed by the proposed verification."** *Removed.* The paper empirically shows the verification improves accuracy over no verification (Table 3), demonstrating that it does address the challenge, even if imperfectly.

3. **Strength Finder's framing of verification as "avoiding the self-correct bias known to degrade performance" without noting its own limitations.** *Nuance retained in the Strengths section.* The strength is kept but the limitations are discussed in Weaknesses.

4. **"Cost and error propagation" criticism about two LLM calls.** *Downgraded to minor and retained above.*

5. **"The gains could easily be driven by majority voting rather than triples."** *Integrated into the Major weakness about experimental design rather than stated as a standalone claim.* The critic speculates without evidence; the paper's ablation does show component contribution, which partially addresses this.

---

## Novel Insights

None beyond the paper's own contributions. The key observation — that forcing LLMs to extract entities and relations into a fixed triple structure during decomposition may capture more information than free-form decomposition — is the paper's own insight, and the structural verification as an alternative to self-correct is also presented by the authors. The reviews do not surface additional novel perspectives beyond what the paper already articulates.

---

## Suggestions

1. **Acknowledge the limitations of the verification mechanism explicitly** in the paper. Clarify that the triple comparison checks structural consistency (same relation, same context entity) rather than factual correctness against the table, and report precision/recall of the verification step.
2. **Add controlled ablations** that replace triple-based decomposition with direct decomposition of equal granularity, and replace triple verification with LLM self-correct, to isolate the specific contribution of triple structure.
3. **Add an analysis of triple extraction quality** — how often are triples malformed, how often does the LLM miss entities or produce incorrect relations?
4. **Narrow the "1.35%–20%" claim** to comparisons against the strongest relevant baselines to avoid giving a misleading impression of the gains.

---
