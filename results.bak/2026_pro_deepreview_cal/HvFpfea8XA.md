Now I have sufficient calibration data. Let me synthesize everything and write the final review.

---

## Summary

This paper proposes AMADEUS, a training-free RAG framework for role-playing agents that aims to maintain persona consistency when answering questions beyond a character's explicit knowledge. AMADEUS consists of three stages: Adaptive Context-aware Text Splitter (ACTS) for persona chunking with hierarchical context, Guided Selection (GS) for selecting inference-relevant chunks via LLM, and Attribute Extractor (AE) for extracting behavioral attributes. The paper also introduces CharacterRAG, a manually constructed dataset of 15 fictional characters (976K characters, 450 QA pairs) for evaluating RAG-based RPAs. Results show improvements on both in-knowledge QA (CharacterRAG) and out-of-knowledge personality assessments (MBTI/BFI).

## Strengths

- **ACTS is a well-motivated and empirically validated text-splitting approach.** Section 4.1 provides a concrete algorithm: maximum paragraph length as chunk size, half-length overlap, and recursive hierarchical context prepending. Table 2 confirms ACTS achieves higher mean similarity and lower variance than four alternative splitters across three embedding models, and Figure 4 systematically validates the overlap coefficient choice (α=2).

- **Human evaluation demonstrates that GS+AE extracts reasonable attributes.** Table 3 reports 14 evaluators rating 60 randomly selected GS+AE output pairs on a 5-point Likert scale, yielding means near 4.0 and Cronbach's α > 0.8 for both BFI and MBTI. This provides independent validation that the pipeline produces sensible character-attribute inferences, even when the extraction mechanism itself is underspecified.

- **AMADEUS shows substantial improvement on out-of-knowledge personality assessment (Table 1).** MBTI accuracy rises from 65% (Naïve RAG) to 85%, BFI accuracy from 72% to 81.33%, with Σ|d| dropping from 21 to 9 (MBTI) and 21 to 14 (BFI). These are the largest margins in the paper and directly support the core claim about maintaining persona consistency beyond explicit knowledge.

- **CharacterRAG fills a clear gap as the first purpose-built dataset for RAG-based role-playing evaluation.** The dataset is manually constructed with persona documents reconstructed from the character's perspective (Section 2.1), covers six attribute categories (Section 2.2), and enables reproducible benchmarking across multiple LLMs and RAG methods.

- **The paper usefully demonstrates that graph-based RAG (LightRAG) and web-search RAG (CRAG) are unsuitable for role-playing.** Table 1 shows LightRAG achieving only 34.67% BFI accuracy, and CRAG underperforming Naïve RAG on CharacterRAG (Table 4, e.g., 70% vs 91.33% on GPT-4.1). These empirical findings are informative for the community.

## Weaknesses

### Major

- **The Attribute Extractor (AE) is not specified.** Section 4.3 describes what AE does (extracts Belief and Value, and Psychological Traits) and why (these directly influence behavior), but provides no prompt template, extraction algorithm, or description of how the LLM call is structured. Section 5.1 states GS and AE are "implemented using GPT-4.1" but this is the extent of specification. Since AE is the component responsible for the attributes that are claimed to enable out-of-knowledge persona consistency, its opacity makes the method's core contribution impossible to fully evaluate or reproduce from the paper alone. This is the single most significant gap in the paper.

- **The MBTI/BFI scoring protocol is not described.** Table 1 is the paper's primary evidence for out-of-knowledge persona consistency, showing how characters' interview responses map to personality types. However, the paper never explains how free-text responses to 60 MBTI and 120 BFI questions are converted into a 4-letter MBTI type or a Big Five SLOAN type. The evaluation says it "compare[s] the results to psychological test outcomes" (Section 5.2) but the aggregation/scoring procedure is opaque. Without this, the headline result (85% MBTI accuracy) cannot be interpreted or replicated.

- **No component ablation on downstream metrics.** The paper ablates the text splitter (Table 2, comparing ACTS vs. RCTS, MHTS, SC, ATS) and the overlap coefficient (Figure 4), but there is no experiment that removes GS alone, removes AE alone, or replaces GS+AE with a simpler alternative (e.g., direct top-K retrieval plus a prompt to maintain persona consistency). Without such ablations on the actual role-playing metrics (ACC, HS, or the MBTI/BFI accuracy), it is impossible to attribute the observed gains to GS and AE rather than to ACTS or to properties of the underlying LLM. This is a significant evaluative gap.

### Minor

- **CharacterRAG ceiling effects limit the dataset's discriminative power.** On GPT-4.1, Naïve RAG already achieves 91.33% ACC, leaving only 1.34 percentage points of headroom for AMADEUS (92.67%). The margins are similarly small for Gemma3-27B (1.56 pp). This does not invalidate the dataset's utility — it still supports systematic comparison across models and methods, and the weaker models (Qwen3-32B: 78.44% Naïve RAG) leave more room — but it limits CharacterRAG's value as a challenging benchmark for strong models.

- **Several implementation details needed for reproducibility are absent.** The GS LLM judge prompt (Algorithm 1, line 8: "With an LLM, determine if chunk c contains information from which the character's attributes can be inferred") is not provided. The Hallucination Score (HS) is described as an LLM-based metric (Section 5.2) but the prompt is not given. The final response generation prompt (Figure 3 shows only a schematic) is incomplete. These would be addressable with code release but limit paper-only reproducibility.

- **The slot size M=2 is stated without justification.** Section 5.1 sets M=2 with no ablation or rationale, despite it being a restrictive choice that limits how many chunks contribute to attribute extraction.

- **F1 is reported for 16-class MBTI and Big Five SLOAN classification over only 15 test instances (Table 1).** With fewer instances than classes, most classes have zero predictions, making the F1 measure poorly defined. The primary metrics (Accuracy, Σ|d|) are more appropriate, but reporting F1 alongside them without caveats is misleading.

### Trivial

- **The personality-database.com ground truth for fictional characters is inherently noisy**, but this follows prior work (Wang et al., 2024b) and is a domain limitation rather than a paper-specific flaw. The paper acknowledges its source.

## Nice-to-Haves

- A test of out-of-knowledge but non-personality queries (e.g., real-world factual questions the character would not know) would more broadly test the "persona consistency beyond knowledge" claim.
- Annotator agreement or quality control documentation for the CharacterRAG dataset construction.
- Discussion of the cost implications of using GPT-4.1 for both GS and AE at inference time.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The core Attribute Extractor (AE) component is not described" — harsh critic framing as "structural problem that makes the contribution non-viable"** — Retained the core observation (AE is underspecified) but demoted from "fatal/structural" to Major. The AE is implemented using GPT-4.1 (stated in Section 5.1), so it exists and operates; the problem is missing specification, not missing existence.

- **"MBTI/BFI ground-truth itself is weak — using crowdsourced personality votes for fictional characters as a gold standard makes the evaluation noisy and conceptually questionable"** — Moved to Trivial/Nice-to-Have. This follows prior work (Wang et al., 2024b; Sang et al., 2022) and is an inherent limitation of the domain. The paper explicitly cites its source (personality-database.com). Not a paper-specific flaw.

- **"LightRAG and CRAG are somewhat artificial for this task and it is unclear whether they were given fair configurations"** — Removed. These are standard off-the-shelf RAG baselines evaluated in their default configurations. The paper's goal is to show they are unsuitable, which is a finding, not an unfair comparison. If anything, the asymmetry favors the baselines (they can use web search / graph structures that AMADEUS cannot).

- **"The hyperparameter choices (M=2, N=30, lₒ = l_max/2) are presented as though they were obtained by tuning on the evaluation data, which would constitute overfitting"** — Removed as speculative. The paper does not claim these were tuned on evaluation data, and the overlap coefficient is justified through Figure 4's empirical analysis. M=2 is stated without justification but there is no evidence of overfitting.

- **"Dataset documentation does not discuss annotator agreement or quality control beyond 'manually constructed'"** — Moved to Nice-to-Haves. This is a reasonable suggestion but not a core weakness for a dataset that is explicitly manually constructed from wiki sources.

- **"The reliance on a paid GPT-4.1 endpoint introduces cost and reproducibility barriers"** — Moved to Nice-to-Haves. Cost is a practical concern, not a scientific weakness.

- **Strength Finder: "The work exposes fundamental limitations of graph-based and web-search RAG"** — Retained (strength 5).

- **Strength Finder: "AMADEUS substantially improves persona consistency on both in-knowledge and out-of-knowledge questions"** — Retained but qualified. The CharacterRAG margin is small; the MBTI/BFI margin is large.

- **Harsh Critic: "The paper over-claims in the abstract and introduction"** — Demoted. The abstract claim of "significantly enhance persona consistency even when responding to questions beyond a character's knowledge" is supported by Table 1 results, though the evaluation scope (personality questionnaires) is narrower than the phrasing suggests. The paper acknowledges this scope in Section 5.2.

- **Harsh Critic: "Essential implementation details for reproducibility are missing across the board"** — Retained as Minor weakness 2, but the claim about "the failure to provide these details prevents replication and prevents a reader from assessing whether the evaluation metrics themselves are sound" is softened — these are addressable with code release.

## Novel Insights

The paper's most interesting empirical finding is that graph-based RAG (LightRAG) catastrophically fails at role-playing persona retrieval (34.67% BFI accuracy, vs. 72% for Naïve RAG), while web-search RAG (CRAG) introduces persona-inconsistent noise. This is a specific, well-documented observation that goes beyond the expected result that "RAG helps" — it identifies a genuine failure mode of popular RAG paradigms when applied to persona-consistency tasks, where retrieved content can actively undermine character fidelity. This insight is practically valuable for anyone building RAG-based character systems.

## Suggestions

- Provide the full prompt templates for AE, GS, and HS evaluation. Even a one-paragraph description of how AE structures its LLM call would substantially improve reproducibility.
- Add a minimal component ablation: compare AMADEUS vs. AMADEUS without GS vs. AMADEUS without AE on the MBTI/BFI task. Even on a subset of characters, this would clarify where the gains originate.
- Describe the MBTI/BFI scoring protocol — is it another LLM call that classifies interview responses? A rule-based mapping from Likert responses? A prompt that asks the LLM to self-report a type? Clarifying this is essential for interpreting Table 1.
- Justify or ablate the M=2 choice, which appears arbitrarily restrictive.

## Score and Decision

**Round 1 calibration bracket:** The paper sits between the weak anchors (~2.3-3.4) and the strong anchors (~6.0-8.0), with the most comparable paper being MMRole (6.50, Accept). Initial bracket: 4.0–6.0.

**Round 2 narrowing anchors:**
- *Human Simulacra* (5.60, Accept) — character personality simulation with psychology-grounded evaluation. More sophisticated psychological framework but similar evaluation limitations. AMADEUS is somewhat weaker due to underspecified AE and missing component ablation. 
- *BIG5-CHAT* (5.25, Reject) — personality dataset + training methods. Good dataset but rejected for limited novelty and lack of human evaluation. AMADEUS has human evaluation (Table 3) and a training-free RAG approach, making it marginally stronger.
- *Tell Me What You Don't Know* (5.20, Reject) — RPA refusal capabilities with representation editing. Similar profile: interesting problem, some methodological gaps led to rejection.
- *Bias Runs Deep* (5.75, Accept) — persona-assigned LLMs with reasoning evaluation. Stronger experimental breadth.

AMADEUS is most comparable to BIG5-CHAT (5.25) and Human Simulacra (5.60). It is clearly stronger than CRAG (3.75) — which had fundamental issues with missing baselines and limited contribution — and clearly weaker than MMRole (6.50), which had a larger dataset and more comprehensive evaluation framework. The paper is somewhat weaker than Human Simulacra due to the underspecified AE and missing component ablation, but comparable to BIG5-CHAT with the advantage of human evaluation and a clearer technical contribution. 

**Final score: 5.0.** The three Major weaknesses (underspecified AE, opaque MBTI/BFI scoring, no component ablation) collectively prevent the paper from supporting its central claims as strongly as it should, but the contributions (ACTS, CharacterRAG dataset, human evaluation, empirical findings about LightRAG/CRAG) are real and valuable. A Reject recommendation reflects the severity of the Major issues, particularly that the core method component (AE) and the primary evaluation protocol (MBTI/BFI scoring) are not sufficiently described to evaluate or reproduce the work.

**Anchor summary:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EDU-RAG (a2rSx6t4EV) | 2.33 | R1 | Much weaker — trivial dataset extension, shallow |
| CRAG (JnWJbrnaUE) | 3.75 | R1 | Weaker — fundamental baseline/novelty issues |
| RAG-DDR (Pnktu2PBXD) | 6.00 | R1 | Stronger — clearer technical contribution |
| MMRole (FGSgsefE0Y) | 6.50 | R1 | Stronger — larger dataset, multimodal, comprehensive eval |
| Tell Me What You Don't Know (87DtYFaH2d) | 5.20 | R2 | Comparable — interesting problem, methodological gaps |
| Human Simulacra (BCP5nAHXqs) | 5.60 | R2 | Slightly stronger — richer psychological grounding |
| BIG5-CHAT (TqwTzLjzGS) | 5.25 | R2 | Comparable — personality dataset, rejected for limited novelty, no human eval |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>