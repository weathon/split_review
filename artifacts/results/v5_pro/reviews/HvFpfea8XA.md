Now let me synthesize everything into the final review.

---

## Summary

AMADEUS is a training-free RAG framework for role-playing agents (RPAs) with three components: Adaptive Context-aware Text Splitter (ACTS) for character-specific chunking with hierarchical context, Guided Selection (GS) for LLM-based chunk filtering, and Attribute Extractor (AE) for extracting personality-relevant attributes. The paper also introduces CharacterRAG, a manually constructed dataset of 15 fictional characters with 976K characters of persona documents and 450 QA pairs. The claimed contribution is improved persona consistency for out-of-knowledge queries, evaluated via MBTI and BFI personality-type prediction against crowdsourced ground-truth labels, along with standard in-knowledge QA accuracy.

## Strengths

- **Novel problem formulation and framework.** The paper identifies a real gap — RAG-based role-playing agents that maintain persona consistency beyond explicit knowledge — and proposes a coherent three-stage pipeline (ACTS, GS, AE) that is training-free and directly motivated by observed failure modes of naive RAG (chunk over-duplication in Figure 1).

- **Valuable dataset contribution.** CharacterRAG fills a genuine gap: no existing dataset is explicitly designed for building and evaluating RAG-based RPAs. The dataset construction is manual and tied to character perspectives, and the w/o-RAG baseline in Table 4 (18.89–49.56% accuracy across LLMs) confirms that the dataset contains knowledge not memorized by current models, making it a meaningful benchmark.

- **Human evaluation of attribute extraction.** Table 3 reports Likert-scale scores near 4.0/5.0 for AE attribute quality with Cronbach's α > 0.8 across 14 evaluators, providing credible evidence that GS+AE produces reasonable attribute inferences from retrieved chunks.

- **ACTS chunking is empirically validated across embedders.** Table 2 shows ACTS outperforms four alternative chunking strategies (RCTS, MHTS, SC, ATS) on mean similarity and variance across three embedding models (BGE-M3, Qwen3-0.6B, mE5-large-instruct), and Figure 4 provides density analysis supporting the overlap coefficient choice.

- **Clear writing and motivation.** The paper is well-structured, the problem is motivated with concrete evidence (Figure 1 chunk duplication distributions), and the framework diagram (Figure 3) effectively communicates the pipeline.

## Weaknesses

### Fatal

None.

### Major

- **No ablation isolates the contributions of ACTS, GS, and AE.** The paper presents AMADEUS as a three-component framework but provides no end-to-end results with any component removed. Table 2 evaluates chunking strategies in isolation (similarity scores, not role-playing quality) and Table 3 evaluates GS+AE output quality alone — neither tells us whether GS or AE actually improves downstream persona consistency. Without ablations, it is impossible to determine whether the gains in Table 1 and Table 4 arise from the adaptive chunking, the LLM-based filtering, the attribute extraction, or some interaction. The paper therefore cannot justify the complexity it introduces. *Why it matters:* A core contribution claim is that all three stages are necessary; the paper provides no evidence for this.

- **Unequal LLM budget between AMADEUS and baselines.** GS and AE are implemented using GPT-4.1, the same model used for final response generation in the GPT-4.1 experiments. The baselines (Naive RAG, CRAG, LightRAG) receive no equivalent LLM-based post-retrieval refinement step. The observed improvements in Table 1 and Table 4 could therefore be driven by the additional reasoning power of an LLM re-processing step rather than by the specific GS/AE design. A controlled baseline — e.g., Naive RAG augmented with a comparable LLM re-ranker or attribute-extraction step — is needed to isolate the contribution of the proposed architecture from the contribution of additional compute. *Why it matters:* This confound undermines the paper's claim that the specific proposed mechanisms (GS, AE) are responsible for the gains.

- **Personality-type evaluation methodology is insufficiently described.** Table 1 reports MBTI and BFI SLOAN type prediction accuracy (65% → 85% for MBTI). However, the paper never explains how the 60 or 120 free-text answers per character are mapped to a discrete personality type — a non-trivial step (e.g., majority voting per dimension, scoring rules, tie-breaking). The ground-truth labels come from personality-database.com, a crowdsourced voting website whose reliability is unverified by the paper. Section 5.2 cites prior work (Wang et al., 2024b) for the interview-assessment protocol, but the mapping procedure itself is not summarized or referenced. *Why it matters:* The headline result (Table 1) is the strongest empirical claim in the paper; without understanding how it is computed, readers cannot evaluate its validity.

### Minor

- **In-knowledge gains are marginal and lack statistical backing.** Table 4 shows AMADEUS improves over Naive RAG by only ~1 percentage point on GPT-4.1 (91.33% → 92.67% ACC) and similarly narrow margins on other LLMs. No confidence intervals, standard deviations, or statistical tests are reported for any result in the paper. With only 450 questions, these differences could plausibly be noise. The paper's framing of these as consequential gains is overstated.

- **Evaluator model and prompts for LLM-based metrics are undisclosed.** ACC, ACCL, and HS are computed by an unspecified LLM evaluator with no prompts provided (Section 5.2). Reproducibility of the evaluation pipeline is therefore limited.

- **Korean-to-English translation process is not documented.** The CharacterRAG dataset is sourced from Namuwiki (Korean wiki, Section 2.1), yet all examples and experiments use English. The paper does not state whether translation was applied, which tool was used, or whether quality checks were performed. This affects reproducibility and raises questions about fidelity of the persona content.

- **No computational cost analysis for GS.** GS iterates over retrieved chunks with an LLM call per chunk (up to N=30 iterations, Section 5.1). The paper reports no latency or API cost measurements, which matters for a framework positioned as practical for real-time conversation.

- **Table 1 accuracy metric is ambiguous.** The paper reports "Accuracy" without specifying whether it means exact type match or partial credit (e.g., 3/4 MBTI dimensions correct). The distinction is consequential: many predicted types differ by only one letter, and a lenient metric would inflate reported figures.

- **CharacterRAG scope is modest.** With 15 characters (primarily from a small set of anime franchises) and 450 QA pairs, the dataset's coverage of diverse role-playing scenarios is limited, though this is partially mitigated by the paper being the first of its kind.

### Trivial

- Figure 1 caption repeats text across multiple panels and contains typos in character-type labels (duplicate ISTP/INTP listings).
- Section 6 (Related Work) is cursory; several cited works are listed without substantive discussion of how they relate to AMADEUS.

## Nice-to-Haves

- Adding a baseline that gives Naive RAG an equivalent LLM budget (e.g., LLM re-ranking of top-K chunks or a single "extract attributes from retrieved context" prompt) would cleanly separate the contribution of extra compute from the specific GS/AE architecture.
- Reporting character-wise failure analysis for Table 1 (e.g., why Edward Elric, Megumin, and Mikoto Misaka are still misclassified) would add credibility and insight.
- Including pairwise human evaluation of final response quality (AMADEUS vs. baseline) on a sample of out-of-knowledge queries would provide more direct evidence than personality-type classification alone.

## Removed Points

These points were flagged from the inputs but are removed; treat them with caution:

- **"Ground-truth itself is subjective and unverified; there is no evidence that an LLM-based system recovering that crowdsourced type indicates genuine persona fidelity."** This concern about the crowdsourced labels is partly retained (as Major weakness #3) but the claim that the evaluation is *structurally unsound* is softened — the interview-based assessment methodology is established in prior work the paper cites. The weakness is insufficient description, not fundamental invalidity.

- **"Why a more uniform chunk usage is inherently better for persona consistency"** — The paper's Figure 1 is presented as motivation rather than proof, and the text states that excessive reliance on less-relevant chunks leads to hallucination (Section 1). While not rigorously proven, this is a reasonable motivating observation, not a flaw.

- **"The paper does not report the computational cost of this filtering (GPT-4.1 calls per query), nor does it discuss latency"** — Retained as Minor, not Major, because latency analysis is a nice-to-have for a training-free framework but not a methodological requirement for its validity.

- **"Thinging-mode experiment with Qwen3-32B contributes little to the argument; its inclusion dilutes the evaluation without adding insight"** — Removed; this is a subjective judgment about an experimental detail that at worst is harmless, not a weakness. The paper briefly reports this finding and moves on.

- **"The relationship between the Korean source data and the English experiments should be clarified"** — Retained as Minor.

- **"Evidence for in-knowledge improvement is weak and unreplicated"** — Retained as Minor. The harsh critic's framing as a "structural" problem is excessive; the paper's main contribution claim is about out-of-knowledge consistency, and the in-knowledge results serve as a sanity check.

- **Harsh critic's "Section-by-Section Notes" about ACTS overlap recipe being character-agnostic** — The paper validates the overlap coefficient empirically in Figure 4 across all characters. Character-specific tuning would be a nice-to-have but the current validation is reasonable. Demoted from concern to no weakness.

## Novel Insights

The review process surfaces an important tension in RAG-based role-playing evaluation: personality-type prediction from free-text interview responses (the MBTI/BFI protocol) is an appealingly scalable evaluation paradigm, but the chain from raw model outputs → aggregated personality type → comparison with crowdsourced labels has multiple unexamined links. Future work in this area would benefit from establishing a standardized, documented mapping protocol with known reliability characteristics, ideally validated against human judgments of response quality on a held-out sample. The paper's CharacterRAG dataset — which separates in-knowledge from out-of-knowledge evaluation — is a step in the right direction, but the field needs clearer methodological standards for the out-of-knowledge case.

## Suggestions

- **Restructure evaluation around controlled ablations.** At minimum, report: (i) Naive RAG + ACTS alone, (ii) Naive RAG + ACTS + GS (no AE), (iii) Naive RAG + ACTS + AE (no GS), and (iv) full AMADEUS, all on both Table 1 and Table 4 metrics. This would show which components are load-bearing.

- **Add an LLM-budget-controlled baseline.** Implement a simple baseline that post-processes Naive RAG's top-K chunks with a single GPT-4.1 call to extract relevant attributes before answering, matching the LLM budget of GS+AE. This isolates architecture from compute.

- **Document the personality-type mapping procedure.** Explain: (a) how each free-text answer is scored per MBTI/BFI dimension, (b) how dimension scores are aggregated into a final type, (c) any threshold choices. Cite the relevant protocol from Wang et al., 2024b explicitly.

- **Report variance and/or statistical tests** for all main results (Tables 1, 2, 4) to give readers a basis for interpreting the reported differences.

- **Clarify the translation pipeline** for Korean→English conversion and include the evaluator prompts in supplementary material.

---

## Calibration Notes

### Anchor comparison set:

| Anchor ID | Avg Score | Round / Query Bucket | Comparison |
|---|---|---|---|
| oqRe1KvD17 (Reward-RAG) | 3.00 | R1-topic-low | Below our paper — limited novelty, narrow evaluation |
| fMaEbeJGpp (Multimodal RAG QA) | 2.50 | R1-topic-low | Below our paper — basic RAG system with limited contribution |
| wZbkQStAXj (PersonaEval) | 4.00 | R1-topic-mid, R2 | Below our paper — benchmark-only, weak connection to actual role-playing |
| 87DtYFaH2d (Tell Me What You Don't Know) | 5.20 | R1-topic-mid, R2 | Comparable scope (RPA); our paper has more practical contribution but more evaluation gaps |
| TqwTzLjzGS (BIG5-CHAT) | 5.25 | R1-weakness-personality, R2 | Comparable — personality evaluation focus, similar score range; we have more novelty but weaker evaluation controls |
| FGSgsefE0Y (MMRole) | 6.50 | R1-topic-mid | Above our paper — larger scope, multimodal, more comprehensive evaluation, specialized model training |
| rKMQhP6iAv (Personas as Truthfulness) | 4.25 | R1-topic-mid | Below our paper — theoretical framing, no practical system or dataset |

### Round-1 bracket: 4.0–5.5

The paper was placed between PersonaEval (4.00, benchmark with limited contribution) and MMRole (6.50, comprehensive multimodal framework). Round-2 narrowing within (4.5, 5.5) pulled comparable role-playing and RAG-configuration papers clustering at 5.0–5.25, confirming the bracket.

### What did the low-band anchors fail at, and does this paper share those failures?

Round-1 low-band topic anchors (2.33–3.00) failed primarily on limited novelty and narrow or simplistic evaluation — e.g., Reward-RAG contributed a straightforward reward-driven supervision approach without meaningful ablations, and EDU-RAG was a domain-specific benchmark with minimal technical contribution. The paper under review does **not** share these failures: it proposes a genuinely novel three-component RAG framework with hierarchical chunking, LLM-based selection, and attribute extraction, supported by a manually constructed dataset and human evaluation. However, the paper **does** share one pattern with borderline-reject anchors in the 5.0–5.25 range: incomplete evaluation controls (missing ablations in "Tell Me What You Don't Know" led to a reviewer score of 3; BIG5-CHAT's lack of human evaluation for dataset quality and limited novelty held it to 5.25). The paper's missing ablations and uncontrolled LLM budget are analogous gaps that prevent its novel framework from being fully substantiated.

### Score justification:

Compared to BIG5-CHAT (5.25) — which was rejected for limited novelty and dataset quality concerns but had a larger-scale dataset (100K dialogues) — our paper has more methodological novelty (training-free RAG framework vs. applying existing SFT/DPO) but shares the issue of insufficient evaluation controls. The missing ablations (Major) and unequal LLM budget (Major) in our paper are more structural than BIG5-CHAT's weaknesses, pulling us slightly below that anchor. Compared to "Tell Me What You Don't Know" (5.20), our paper lacks the depth of analysis (no representation-level investigation) and has similar evaluation gaps, putting us at a comparable or slightly lower level. The paper is clearly above PersonaEval (4.00) due to its practical framework, dataset, and human evaluation. 

**Final score: 5.0**, reflecting a paper with genuine contributions (novel framework, new dataset, human evaluation) but with significant evaluation gaps (no ablations, unequal compute budget, incomplete methodology description) that prevent the core claims from being fully established.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>