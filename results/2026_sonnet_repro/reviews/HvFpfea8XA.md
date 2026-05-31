Now let me run calibration searches to properly score this paper.Round 1 bracket: **4 to 6**. Let me read key anchors and narrow the bracket.Now I have enough to write the final review. The paper sits closest to the Late Chunking (4.75) and DialSim (5.0) anchors, but has more severe methodological issues (GPT-4.1 injection in GS/AE, no downstream component ablation). I'll place it at **4.5**.

---

## Summary

AMADEUS is a training-free RAG framework for fictional character role-playing agents (RPAs), comprising three components: Adaptive Context-aware Text Splitter (ACTS), Guided Selection (GS), and Attribute Extractor (AE). The paper also introduces CharacterRAG, a manually curated dataset of 15 fictional characters with 976K written characters and 450 QA pairs sourced from Namuwiki (Korean). The core thesis is that AMADEUS maintains persona consistency even for queries that fall outside a character's explicit knowledge, validated through MBTI/BFI personality assessments and an in-knowledge QA benchmark.

---

## Strengths

- **CharacterRAG fills a genuine dataset gap.** No prior benchmark provides long-form character personas designed for RAG-based role-playing evaluation. The dataset's careful removal of editor-perspective content and reconstruction from each character's first-person viewpoint is methodologically motivated. The "w/o RAG" experiments (Table 4: ACC ≤ 49.56% across all three LLMs) validate the dataset's difficulty and confirm it tests genuine external-knowledge usage.

- **ACTS ablation is clean and multi-faceted.** Table 2 compares ACTS against four chunking alternatives (RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter, SemanticChunker, and ablated ATS without hierarchical context) across three embedding models. ACTS consistently achieves higher mean similarity and lower variance in all nine cells, providing solid evidence for the chunking contribution.

- **Human evaluation of GS+AE is methodologically careful.** Table 3 reports Cronbach's α > 0.81 (well above the 0.7 threshold) from 14 human evaluators over 60 randomly selected samples, giving direct support to the sub-claim that GS and AE extract personality-relevant attributes reliably. This is the strongest piece of direct evidence in the paper.

- **Multi-paradigm RAG analysis is informative.** The paper demonstrates that graph-based RAG (LightRAG) and web-search RAG (CRAG) degrade role-playing performance (Tables 1 and 4), providing actionable guidance for RAG-RPA research. For example, LightRAG's MBTI accuracy falls to 34.67% on BFI vs AMADEUS's 81.33%, a clear practical finding.

---

## Weaknesses

### Fatal
None.

### Major

- **GPT-4.1 is injected into GS and AE regardless of the backbone LLM, making cross-backbone comparisons misleading.** Section 5.1 explicitly states: *"We implement Guided Selection (GS) and Attribute Extractor (AE) using GPT-4.1 ('gpt-4.1-2025-04-14')."* This means that in Table 4, "AMADEUS (Gemma3-27B)" uses Gemma3-27B only for final generation, while GPT-4.1 performs chunk selection and attribute extraction — the two core novel steps of the method. Comparing this to "Naive RAG (Gemma3-27B)" conflates method differences with model-capability differences. The improvement AMADEUS shows over Gemma3 and Qwen3 baselines is partly attributable to injecting a superior model (GPT-4.1) into AMADEUS's intermediate steps. Without a configuration that uses the same backbone for all components, the headline multi-LLM results in Table 4 do not cleanly support the claimed method advantage.

- **No component-level ablation for GS and AE on downstream task metrics.** Table 2 ablates chunking strategies on embedding similarity scores, but no experiment isolates GS, AE, or their combination on the metrics in Table 4 (ACC, ACC_L, HS). The paper presents ACTS, GS, and AE as three individually necessary contributions (Section 1, bullet points), but the only ablation isolates the ACTS component on a proxy metric. Given that the in-knowledge improvement of AMADEUS over Naive RAG is small (ACC: 91.33%→92.67%, ACC_L: 9.23→9.26 for GPT-4.1), it is unclear whether GS and AE individually contribute positively, neutrally, or negatively to downstream task performance.

### Minor

- **MBTI type-matching as proxy for out-of-knowledge persona consistency has validity limitations.** The paper's primary claim is that AMADEUS maintains persona consistency for out-of-knowledge questions, and the main evidence is MBTI/BFI type prediction accuracy (Table 1). The paper acknowledges using crowd-sourced votes from personality-database.com as ground truth (Section 5.2, footnote 4). Predicting a character's 4-letter MBTI type correctly is structurally different from generating persona-consistent responses in dialogue. That said, this is an accepted evaluation protocol in prior work (Wang et al., 2024b; Park et al., 2025), and Table 3's human evaluation partially mitigates the concern by directly verifying whether extracted attributes are reasonable. The issue is real but not novel to this paper.

- **Potential self-evaluation bias: GPT-4.1 evaluates outputs that were partially generated by GPT-4.1.** Section 5.2 describes ACC, ACC_L, and HS as LLM-based metrics; GPT-4.1 is the likely evaluator. Since GPT-4.1 also drives GS and AE for AMADEUS, it may rate outputs shaped by its own reasoning more favorably. This is not acknowledged in the paper and represents a confound in the metric design.

- **Small improvements on in-knowledge tasks without significance testing.** For GPT-4.1, AMADEUS improves ACC by 1.34 percentage points and ACC_L by 0.03 over Naive RAG (Table 4). The evaluation set has only 450 total QA pairs (30 per character), and no confidence intervals or significance tests are provided. Claims of "best performance across all three LLMs" (Section 5.3) are factually correct but not supported by statistical rigor for these margins.

### Trivial

- The GS fallback frequency (how often the slot remains empty and falls back to top-K+1) is not reported. This would help assess how often GS actually fires vs. degrades to standard retrieval.

---

## Nice-to-Haves

- Providing a single ablation table (ACTS-only, ACTS+GS, ACTS+AE, ACTS+GS+AE) using the same backbone for all components would directly address the two major weaknesses above and would substantially increase confidence in the three-part contribution.
- Reporting wall-clock or token cost comparison between AMADEUS and Naive RAG: GS makes up to 30 sequential LLM calls per query, which matters for practical deployment claims.
- Extending the CharacterRAG dataset beyond anime/manga characters (all 15 sourced from Japanese animation/manga via Korean Namuwiki) would broaden the generalizability of the conclusions.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Reviewer concern that α=2 is not meaningfully superior to α=5/10/15**: While Figure 4's legend shows nearly identical log sim values (5.916 vs 5.92), the paper also reports variance as a criterion, and α=2 does show lower variance. The claim of "optimal" is marginally supported; the concern is valid as a minor point but was already absorbed into the Trivial section.

- **Reviewer concern about missing appendix/proofs**: Per policy, the parser strips appendix sections. Not included.

- **Reprodicibility concerns about GS prompt details**: Per policy, hyperparameter/prompt specification concerns are removed.

- **Strength Finder claims about "opening new possibilities for RAG-based RPAs" and "the first dataset designed for building and evaluating RAG-based RPAs"**: Kept partially but as the specific CharacterRAG gap claim, not as a broad first-ever claim.

- **Dataset sourcing from Namuwiki (Korean)** noted as a domain-coverage limitation: Retained as a Nice-to-Have but not elevated to a weakness since the paper does not claim universality.

---

## Novel Insights

None beyond the paper's own contributions. The finding that graph-based and web-search RAG paradigms are unsuitable for role-playing (due to entity ambiguity and persona-polluting web results respectively) is a practical insight, but the paper presents it as a result rather than a central contribution. The use of personality-questionnaire interviews as a proxy for out-of-knowledge persona evaluation is borrowed from prior work (Wang et al., 2024b).

---

## Suggestions

1. **Run AMADEUS with matched backbones**: For Gemma3-27B and Qwen3-32B rows, also implement GS and AE using those same models. This separates the method contribution from the GPT-4.1 contribution and directly addresses the major methodological concern.
2. **Add a 2×2 ablation table on Table 4 metrics**: Report ACTS-only, ACTS+GS, ACTS+AE, ACTS+GS+AE (with matched backbone) to establish individual component contributions.
3. **Supplement Table 1 with direct out-of-knowledge response quality**: A small human evaluation (extending the Table 3 protocol) judging whether individual responses to MBTI/BFI questions are persona-consistent would provide more direct evidence for the core out-of-knowledge claim.
4. **Report GS activation rate**: For each character and query type, report how often the slot is non-empty (GS fires) vs. empty (falls back to top-K+1). This clarifies when the method adds value.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| oqRe1KvD17.md (Reward-RAG) | 3.0 | 1 | Clearly weaker — incremental RAG approach, weaker dataset |
| fMaEbeJGpp.md (Multimodal RAG QA) | 2.5 | 1 | Much weaker — narrow system, no novel insight |
| rKMQhP6iAv.md (Personas/Truthfulness) | 4.25 | 1 | Similar: persona-related LLM paper, less experimentally comprehensive |
| 87DtYFaH2d.md (RPA Refusal) | 5.2 | 1 | Similar scope; that paper has cleaner mechanistic insight and no model-asymmetry issue |
| QYvtX2XA8p.md (CtrlA Adaptive RAG) | 4.5 | 1 | Comparable: adaptive RAG paper with methodological concerns |
| wZbkQStAXj.md (PersonaEval) | 4.0 | 1 | Slightly weaker — narrower benchmark |
| W1x77vRucB.md (DialSim) | 5.0 | 2 | Comparable scope (dialogue simulator + dataset), larger scale but has data-leakage concern; broadly comparable |
| 74QmBTV0Zf.md (Late Chunking) | 4.75 | 2 | Close match: chunking method with clean ablation but limited scope; the present paper is broader in scope but has more severe methodological concerns |
| TqwTzLjzGS.md (BIG5-CHAT) | 5.25 | 2 | Slightly stronger: 100K dialogues, cleaner train/eval separation, BFI evaluation properly tied to training signal |
| KZaEdLM4Gn.md (TPE multi-persona) | 4.67 | 2 | Roughly similar: method + framework paper, mixed reviews |
| Iyrtb9EJBp.md (RAG Trustworthiness) | 8.0 | 1 | Much stronger: rigorous metric, training methodology, broad benchmarks |

**Round 1 bracket:** 4–6

**Round 2 narrowing:** The paper sits between Late Chunking (4.75) and DialSim (5.0). The GPT-4.1 injection issue in GS/AE for non-GPT backbones is a more severe methodological problem than anything in those anchor papers — it directly undermines the multi-LLM evidence, which is the main scope-expansion experiment. Combined with the missing component ablation on downstream metrics, the paper falls slightly below the 4.75 anchor. The CharacterRAG dataset and ACTS ablation are solid contributions that keep it above the 4.0–4.25 band.

**Final score: 4.5 — Reject**

The paper addresses a genuine problem and makes real contributions (CharacterRAG dataset, ACTS chunking with clean ablation, informative RAG-paradigm analysis). However, the paper's multi-LLM claims are substantially undermined by the GPT-4.1 injection in GS/AE when evaluating non-GPT backbones, and the three-part contribution is not individually ablated on downstream task metrics. These gaps require new experiments rather than textual revision to resolve.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>