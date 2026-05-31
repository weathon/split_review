Now let me check the appendix/algorithm section to see if GS prompt details are present.## Summary

The paper introduces AMADEUS, a training-free three-stage RAG pipeline for role-playing agents — Adaptive Context-aware Text Splitter (ACTS), Guided Selection (GS using an LLM relevance judge), and Attribute Extractor (AE) — and CharacterRAG, a manually-curated Korean dataset of 15 anime/manga characters (~976K characters of persona text, 450 QA pairs). The headline empirical claim is that AMADEUS preserves persona consistency on out-of-knowledge questions (MBTI/BFI personality inference) where naive RAG fails, while modestly improving QA accuracy on in-knowledge questions.

## Strengths
- **High human inter-rater reliability for AE/GS output** (Table 3): Cronbach's α = 0.825 (BFI) and 0.810 (MBTI) cross the 0.8 "high internal consistency" threshold, providing real evidence that the attributes AE infers from GS-selected chunks are judged reasonable by 14 evaluators.
- **Substantial improvement on MBTI/BFI personality inference** (Table 1): AMADEUS reaches 85.00% MBTI accuracy (∑|d| = 9) vs. 65.00% for Naive RAG (∑|d| = 21), with similar gains in BFI (81.33% vs. 72.00%). The size of this gap on out-of-knowledge queries is the paper's most distinctive empirical result.
- **Consistent hallucination-score reduction across three LLMs** (Table 4): AMADEUS yields the lowest HS for GPT-4.1 (2.89 vs. 3.13/3.21), Gemma3-27B (3.26 vs. 3.27/4.09), and Qwen3-32B (4.66 vs. 5.05/8.68), so the HS effect is not single-model-specific.
- **Manual dataset construction with persona-perspective rewriting**: Section 2.1 documents removing editor commentary and popularity polls so the persona corpus is what the character would plausibly know — a non-trivial annotation effort that is well-aligned with the task.

## Weaknesses

### Fatal
None. The methodological concerns below threaten the strength of the attribution but do not invalidate that the system produces measurably different behavior.

### Major
- **ACTS is validated by a metric that mechanically rewards its own design choice.** Section 4.1 sets chunk length = l_max (the maximum paragraph length in the persona) and overlap = l_max/2. Table 2 then declares ACTS best because it has the highest ∑μ and lowest ∑σ² of cosine similarity between query and retrieved chunks. Larger chunks contain more text and therefore mechanically tend to score higher in cosine similarity against arbitrary queries; the same logic applies to Figure 4's α=2 "optimum," which optimizes the same similarity-sum metric that rewards larger overlaps. A retrieval-quality measurement against human-marked relevant chunks (recall@K) — or downstream task accuracy at matched chunk budgets — would be the appropriate test, and is missing. This matters because the chunking contribution is one of the three pillars of the framework.
- **The three-component framework is never decomposed.** Tables 4 and 5 only report AMADEUS as a bundle vs. Naive RAG / CRAG / LightRAG; no ACTS-only, GS-only, or AE-only rows appear. On CharacterRAG with GPT-4.1 the gain over Naive RAG is 91.33% → 92.67% (≈1.3 points); with Qwen3-32B it is 78.44% → 78.89% (≈0.5 points). With margins this small the reader cannot tell whether the modest in-knowledge improvement is due to chunking, the LLM re-ranker (GS), the attribute prompting (AE), or simply the extra prompting. Likewise, the large MBTI/BFI gain could plausibly come from AE alone (i.e., explicitly inferring personality traits before answering). Without component-isolation rows the "three substages" claim is not evidentially supported.
- **Inference-cost asymmetric comparison.** Algorithm 1 uses up to N=30 GPT-4.1 relevance judgments per query, plus AE adds further GPT-4.1 calls for attribute extraction. Naive RAG, CRAG, and LightRAG do none of this. A fair comparator would be Naive RAG + an LLM reranker at matched cost, or Naive RAG + AE bolt-on. As reported it is unclear whether the gains reflect the algorithmic ideas or simply more GPT-4.1 calls in the pipeline.

### Minor
- **Baselines are not the strongest for the task.** Section 5.1 admits CRAG (web search) and LightRAG (graph-based RAG for arbitrary corpora) were chosen "to investigate the effects of web search and graph-based knowledge systems." Neither targets retrieval from a curated single-character persona document, so showing them underperforming is weak evidence that AMADEUS beats a well-configured persona-RAG. A naive-RAG-with-reranker baseline would be more informative.
- **AE uses only 2 of 6 attributes with thin justification.** Footnote 3 says *Belief and Value* and *Psychological Traits* "directly influence behavior," but Section 2.2 introduces six attributes (e.g., *Skill and Expertise* would seem relevant to skill questions, *Activity* to narrative continuity). The omission is unargued and not ablated.
- **In-knowledge vs out-of-knowledge framing-evaluation mismatch.** The motivating story is out-of-knowledge queries (Figure 1, Section 1), but CharacterRAG QA pairs are "derived from the character's knowledge" (Section 2.2), so Table 4 evaluates the in-knowledge regime. The out-of-knowledge regime is evaluated only via MBTI/BFI — a specific personality-inference subtype, not, e.g., novel hypothetical scenarios. This narrows the scope of the empirical claim relative to the framing.
- **Evaluation chain is dense in LLM judgment.** GS/AE use GPT-4.1; ACC_L and HS are LLM-judged; the MBTI/BFI "ground truth" is fan-poll personality typings from personality-database.com, not validated psychometrics. The paper does not interrogate this — a sentence or two acknowledging the LLM-in-the-loop circularity in the discussion would be appropriate.
- **Single-run reporting with small margins.** Every metric in Tables 4–5 is a single number; with Naive-vs-AMADEUS gaps under ~2 points on CharacterRAG, run-to-run variance is a plausible alternative explanation. Reporting variance across a few seeds (or even temperature sampling) would help.

### Trivial
- The "intra-level / hierarchical context" terminology (Section 4.1) reduces to prepending heading hierarchy to each chunk. This is close to known "contextual retrieval" techniques; positioning the contribution against that line would be honest.
- The slot size M=2 (Section 5.1) is a tight bottleneck never ablated.

## Nice-to-Haves
- **A clean ACTS-only / GS-only / AE-only ablation grid on both CharacterRAG QA and MBTI/BFI.** This would directly resolve which substage drives which gain.
- **A retrieval-quality measurement for ACTS that does not depend on raw similarity magnitudes** — e.g., recall against human-marked answer-bearing chunks, or downstream accuracy at matched chunk-token budgets across chunkers.
- **An inference-cost-matched baseline**: Naive RAG + LLM reranker (matching GS's ~30 GPT-4.1 calls), or Naive RAG + AE-only attribute prompting.
- **Variance across runs** for the headline numbers; the 0.5–1.5-point margins demand it.
- **Broader coverage**: the dataset is 15 anime/manga characters in Korean. A small English-character extension or even one Western literary character would let the paper credibly support the "RAG-based RPAs" framing instead of a single subgenre claim.
- A discussion of the risk that the evaluated LLMs already know these well-known anime characters from pre-training, which interacts strangely with measuring persona consistency from retrieved knowledge.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **Figure 1 MBTI labels appear duplicated ("ENTJ, ESTJ, ISTJ, ISTP, INTP, …" repeated).** Parser/OCR artifact; the original figure presumably labels each subplot with a unique character, not 15 personality types. Removed per hard-rule on formatting artifacts.
- **"GS prompt and exact wording not specified."** Reproducibility concern reducible to a deferred/appendix-only detail per the rules; the algorithm-level description in Algorithm 1 is adequate for the main text.
- **"CharacterRAG dataset is narrow (15 anime, Korean only)."** Real, but it is a *first* RAG-for-RP dataset and the authors are explicit about scope; demoted to nice-to-have rather than a substantive weakness.
- **Empirical evidence for α=2 (strength claimed by Strength Finder).** Removed because Figure 4 optimizes the same circular similarity metric as Table 2, and a verified weakness wins over this strength.
- **Systematic chunking ablation (strength claimed).** Removed for the same reason — the chunking comparison shares the circularity problem and so cannot stand as an unqualified strength.
- **LightRAG/CRAG controlled comparison (strength claimed).** Demoted because the authors themselves admit these baselines were chosen to study graph-based and web-search RAG, not as the best persona-RAG comparators; "graph RAG underperforms" is not surprising and not strong support for AMADEUS.

## Novel Insights
None beyond the paper's own contributions. The observation that naive RAG over-uses a few chunks on out-of-distribution queries (Figure 1) is a useful framing, but the reviewers' analyses surface methodological concerns rather than independent positive insights.

## Suggestions
- Add an ablation grid: {Naive RAG, +ACTS, +GS, +AE, +ACTS+GS, +ACTS+AE, +GS+AE, full} × {CharacterRAG, MBTI, BFI}.
- Replace the similarity-sum chunking metric with a recall-based or downstream-accuracy-based evaluation at matched chunk-token budget.
- Add a Naive-RAG-with-LLM-reranker baseline using the same GPT-4.1 call budget as GS.
- Report at least 3-seed variance for the headline numbers.
- Specify the GS LLM prompt template and the M=2 slot-size sensitivity.
- Acknowledge the LLM-judge / LLM-component / fan-poll-GT chain in the limitations.
- Discuss the contextual-retrieval prior art and position ACTS' hierarchical-prefix step relative to it.

## Evaluation on Standard Axes
- **Originality**: Moderate. Framing RAG specifically for role-playing and addressing out-of-knowledge retrieval is a sensible niche; the individual building blocks (hierarchical-context chunking, LLM-as-reranker, attribute prompting) are individually familiar.
- **Importance of question**: Real and reasonable — RAG-RPAs are under-explored relative to fine-tuned RPAs.
- **Claims well supported**: Partially. The MBTI/BFI claim is striking but mediated by LLM judging and fan-poll GT; the CharacterRAG gains are small (0.5–1.5 points) and confounded by inference-cost asymmetry; the ACTS-best claim relies on a circular metric.
- **Soundness of experiments**: Weakest axis — no component ablation, mechanically-favored chunker metric, cost-asymmetric baselines, single-run reporting.
- **Clarity of writing**: Adequate; the framework is easy to follow and the dataset is well documented.
- **Value to community**: A modest curated dataset and a reasonable starting framework, but the methodological gaps mean other researchers would need to redo most of the attribution analysis before building on the specific design choices.

## Score and Decision

**Calibration anchors retrieved (all rounds):**

Round 1 (bracketing):
- `oqRe1KvD17.md` — Reward-RAG, avg 3.00, reject. Read in full? No (only first 1000 chars). RAG-focused reject; weaker than this paper.
- `fMaEbeJGpp.md` — Multimodal RAG QA, avg 2.50, reject. Much weaker; less rigorous.
- `RfYD6v829Y.md` — TrojanRAG, avg 3.40, reject. RAG security; not directly comparable.
- `a2rSx6t4EV.md` — EDU-RAG, avg 2.33, reject. Education RAG benchmark; weaker.
- `wZbkQStAXj.md` — PersonaEval, avg 4.00, reject. Read in full. Benchmark-only RP paper; this paper is broader (method + dataset).
- `FGSgsefE0Y.md` — MMRole, avg 6.50, accept. Read in full. Bigger dataset (85 chars, 11K images, 14K dialogues) and more comprehensive than this paper.
- `BCP5nAHXqs.md` — Human Simulacra, avg 5.60, accept. Personification benchmark; broader scope.
- `fp6t3F669F.md` — AgentQuest, avg 6.25, accept. Different domain (agentic tasks).
- `Iyrtb9EJBp.md` — Trustworthy RAG, avg 8.00, accept. Much more rigorous RAG paper; this paper is below it.
- `WbWtOYIzIK.md` — Knowledge Card, avg 8.00, accept. Stronger contribution.
- `bnINPG5A32.md` — RB-Modulation, avg 8.00, accept. Off-topic.
- `7gUrYE50Rb.md` — EQA-MX, avg 8.00, accept. Off-topic.

Round-1 bracket: **between 4 and 6**, because the paper is clearly above thin benchmark-only PersonaEval (4.0) and weak-RAG papers (2.5–3.5) — it has a real method and dataset — but well below MMRole (6.5) and the 8.0 strong-RAG anchors, which have richer evaluation and broader scope.

Round 2 (narrowing within 4–6):
- `wZbkQStAXj.md` — PersonaEval, avg 4.00, reject. This paper is somewhat stronger (introduces a method, not just a benchmark).
- `rKMQhP6iAv.md` — Personas as Truthfulness, avg 4.25, reject. Different focus.
- `TqwTzLjzGS.md` — BIG5-CHAT, avg 5.25, reject. Read in full. Much larger dataset (100K dialogues) and a training-based approach for shaping LLM personalities — broader and richer evaluation than this paper; was nonetheless rejected. AMADEUS is narrower in scope (15 chars, 450 QA) and has the circularity/ablation issues.
- `VZzx0MPA85.md` — PersonaMath, avg 3.80, reject. Different domain.
- `74QmBTV0Zf.md` — Late Chunking, avg 4.75, reject. Read in full. Similar genre — a chunking-method RAG paper — also flagged for circular/insufficient retrieval-quality evidence (lacks downstream task evaluation); rejected at 4.75. This paper has analogous issues, but adds a dataset.
- `KDXj60FpJr.md` — RAGGED, avg 5.00, reject. RAG configuration framework; not directly comparable.
- `SR8LFpmVun.md` — UncertaintyRAG, avg 4.75, reject. Comparable RAG-method paper.
- `56mg1JFd3n.md` — Writing in the Margins, avg 6.00, reject. Stronger RAG method paper still rejected.
- `cxt2Auexc3.md` — Editing Personality, avg 5.75, reject. Personality-editing benchmark with comparable scope.
- `kGteeZ18Ir.md` — Bias Runs Deep, avg 5.75, accept. Larger-scale persona-LLM study (24 reasoning datasets, 4 LLMs, 19 personas).
- `vbmSSIhKAM.md` — VoxDialogue, avg 6.60, accept. Off-topic (spoken dialogue).

Narrowing: The paper is comparable to Late Chunking (4.75) — chunking-method-with-similarity-metric-circularity, no downstream-task validation, rejected. It is also comparable to BIG5-CHAT (5.25, reject), but BIG5-CHAT has a 100K-dialogue dataset and trained methods, while AMADEUS has only 450 QA pairs and weaker ablations. AMADEUS is stronger than PersonaEval (4.0) because it contributes a method, not just a benchmark. It is weaker than the accept-track Bias Runs Deep (5.75) and MMRole (6.5) due to evaluation/ablation gaps.

Settling **between 4.0 and 5.0**: the paper sits a bit above Late Chunking (similar core methodological circularity, but with a useful dataset contribution and a more striking MBTI result) and a bit below BIG5-CHAT (5.25, reject) due to narrower scope.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>