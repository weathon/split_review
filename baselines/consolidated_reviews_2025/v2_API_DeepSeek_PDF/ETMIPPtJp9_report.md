## Summary
# Final Review Report

## Summary

This paper presents FiDeLiS, a training-free retrieval-augmented reasoning framework for knowledge graph question answering (KGQA). The method combines two components: Path-RAG, which uses LLM-generated keywords to retrieve relevant entities and relations from a vector-indexed KG, and Deductive-Verification Beam Search (DVBS), which replaces traditional logit-based path scoring with deductive reasoning to select and terminate reasoning paths. Experiments on three KGQA benchmarks (WebQSP, CWQ, CR-LT) show that FiDeLiS outperforms both prompting-based and fine-tuned baselines, while reducing LLM calls by approximately 1.7x compared to ToG.

**Core strengths:** The idea of using deductive verification as a beam search stopping criterion is novel and practically motivated. The two-stage architecture (retrieval then deductive-guided search) is clearly structured. The CR-LT-KGQA evaluation on long-tail entities is a thoughtful addition that demonstrates KG value beyond LLM internal knowledge.

**Core weaknesses:** The contributions are somewhat oversold relative to the evidence (claims of "superior generality" from three KGQA datasets; "outperforms all baselines" without backbone-controlled comparisons). Several methodological details are underspecified (what replaces beam search in ablation; how the LLM generates vs selects steps in Eq. 4). The case study overlooks that FiDeLiS misses 2 of 5 ground-truth answers. The α parameter in Eq. 3 is empirically insensitive across a wide range, undermining the claimed importance of the long-term scoring term.

## Strengths
1. **Novel integration of deductive verification into beam search for KGQA.** The core idea of replacing logit-based scoring with a deductive reasoning criterion (C(x, st, s1:t-1)) is a principled way to address the early-stopping problem in graph exploration methods like ToG. This is conceptually cleaner than adequacy-assessment prompts and has measurable impact (Table 4 shows FiDeLiS paths are closer to ground-truth depth than ToG).

2. **Training-free architecture with practical efficiency gains.** The method requires no gradient-based fine-tuning, relying on embedding lookup and LLM prompting. Table 6 shows a 1.7x runtime reduction over ToG (74.26s vs 43.83s on WebQSP), with lower token usage (2,452 vs 6,437). This is a meaningful practical advantage.

3. **Thoughtful evaluation on long-tail entities (CR-LT-KGQA).** The addition of the CR-LT dataset, which contains queries about obscure entities, addresses a known weakness of popular KGQA benchmarks (WebQSP, CWQ) where LLMs may answer from parametric memory alone. FiDeLiS's strong performance here (72.12% Acc vs ToG's 67.24%) validates the KG grounding motivation.

4. **Comprehensive robustness analysis.** The paper includes multiple robustness axes: embedding backbone comparison (Table 3), beam width/depth sensitivity (Figure 2), KG perturbation tests (Appendix H), and path coverage ratio analysis (Figure 3). This is more thorough than typical KGQA papers.

5. **Open-source code release and detailed prompt documentation.** The paper commits to releasing code and provides all prompts in Appendix F, which supports reproducibility.

## Weaknesses
1. **Overclaimed generality and comparison fairness (High severity).** The paper repeatedly claims "superior generality" and "outperforms all baselines" based on three KGQA datasets using different backbone models. Comparisons against fine-tuned methods (DeCAF, RoG) use different backbone architectures (BART-large, Llama-2 vs GPT-4-turbo), making the advantage partly attributable to LLM scale rather than method design. Controlled experiments with identical backbones are missing.

2. **Underspecified ablations (High severity).** The "w/o beam-search" ablation (18.97% drop on WebQSP) does not specify what replaces beam search. Similarly, "w/o deductive-verifier" does not specify the alternative stopping criterion. This makes the ablation results uninterpretable and non-reproducible.

3. **Ambiguous equation notation (Medium severity).** Equation (4) uses LM(st | q, s1:t-1, w) suggesting generation, but the text describes selection from candidates. These are fundamentally different operations with different implications for the method's behavior.

4. **α parameter insensitivity (Medium severity).** Appendix Table 9 shows that varying α from 0.1 to 1.0 changes performance by only 0.84% on WebQSP, contradicting the text's claim that α balances short-term and long-term outcomes.

5. **Circular validation in deductive verification (Medium severity).** The same LLM generates paths, converts queries to declarative statements, and verifies whether deductions hold. No independent verifier is used, introducing risk of self-confirmation bias.

6. **Case study incompleteness (Medium severity).** FiDeLiS finds 3/5 correct answers (F1=0.857) but the paper presents this as "better understanding" without discussing the two missed answers. ToG retrieves similar KG paths but fails on answer aggregation — the comparison conflates different failure modes.

7. **Unvalidated keyword recall (Low-Medium severity).** The "exhaustive keyword list" claim lacks quantitative support. No analysis reports how many keywords are generated, what coverage of ground-truth relations they achieve, or how often keyword generation fails.

8. **Related work is list-style (Low severity).** The section reads as paper-by-paper summaries rather than organized by comparison axes (retrieval vs generation vs exploration), making it harder for readers to understand FiDeLiS's positioning.

## Key Issues
### Ranked Top-5 Core Defects

| Rank | Defect | Severity | Research-Value Impact | Validity Risk | Fixability | Confidence |
|------|--------|----------|----------------------|--------------|------------|------------|
| 1 | Overclaimed generality & uncontrolled baseline comparisons | Major | High | High | Easy (wording + controlled expt) | High |
| 2 | Underspecified ablations (w/o beam-search, w/o deductive-verifier) | Major | Medium | High | Easy (text clarification) | High |
| 3 | Ambiguous Eq. (4): generation vs selection confusion | Major | Medium | Medium | Easy (notation fix) | High |
| 4 | α parameter insensitivity contradicts claimed importance | Major | Low | Medium | Easy (revise text) | High |
| 5 | Circular verification: same LLM for selection and validation | Major | Medium | Medium | Moderate (add independent verifier) | Medium |

### Detailed Explanation of Top Issues

**Issue #1 — Overclaimed generality and uncontrolled comparisons.** The abstract and conclusion state that FiDeLiS "outperforms established strong baselines" with "superior generality." However, the performance comparison pits FiDeLiS (with GPT-4-turbo) against fine-tuned methods using smaller backbones (DeCAF with BART-large; RoG with Llama-2 or Flan-T5). Without a controlled experiment where all methods share the same backbone, the reported advantage is confounded by LLM capability differences. The term "generality" implies cross-task generalization, but only KGQA tasks are evaluated. This overclaiming weakens the paper's scientific credibility and invites immediate reviewer pushback.

**Issue #2 — Underspecified ablations.** The ablation study (Table 2) removes components without describing the replacement. "w/o beam-search" is the most impactful removal (18.97% drop), but readers cannot tell whether the method falls back to greedy decoding, random selection, or early termination. Without this specification, the ablation does not serve its scientific purpose of isolating mechanism effects. The same applies to "w/o deductive-verifier."

**Issue #3 — Equation (4) ambiguity.** The notation LM(st | q, s1:t-1, w) implies the LLM *generates* st from scratch. However, the text describes selection from a pre-filtered candidate set S_t. These are different operations: generation requires the LLM to propose a relation-entity pair, while selection requires ranking given candidates. The current notation could lead to implementation confusion. A corrected formulation like Score(st; q, s1:t-1, w) or a two-stage notation (candidate retrieval + LLM ranking) would resolve this.

**Remaining issues** (α insensitivity, circular verification, case study incompleteness, keyword recall unvalidated) are documented in the Weaknesses section and individual PDF annotations.

## Actionable Suggestions
### S1 (Must) — Add a controlled backbone experiment
Add a comparison where FiDeLiS, ToG, and RoG all use the same backbone LLM (e.g., Llama-2-13B for all three). Report Hits@1 and F1 on WebQSP and CWQ. This single experiment resolves the fairness concern and either confirms or bounds the claimed advantage.

**Location:** Add as a new row in Table 1 after the existing rows.
**Expected benefit:** Removes the primary validity objection about backbone confounding.

### S2 (Must) — Specify ablation replacements
For each ablated component in Table 2, add a footnote or parenthetical description of what replaces it:
- "w/o beam-search: greedy decoding (beam width = 1)."
- "w/o deductive-verifier: beam search continues to max depth D=4."
- "w/o planning: removes planning context w from beam search prompt."
- "w/o last step reasoning: skips final deductive reasoning step."

**Location:** Section 3.2, within the ablation description paragraph.
**Expected benefit:** Makes ablations interpretable and reproducible.

### S3 (Must) — Correct Eq. (4) notation
Replace `LM(st | q, s1:t-1, w)` with a selection-based notation such as:
`Score(st; q, s1:t-1, w) = P_LLM(st is next step | q, s1:t-1, w, candidate_set)`
or equivalently describe a two-stage process: (1) candidates S_t from Path-RAG, (2) LLM scores each candidate.

**Location:** Page 5, Section 2.2, Eq. (4).
**Expected benefit:** Eliminates ambiguity about generation vs selection.

### S4 (Must) — Bound wording of generality and comparison claims
Replace "superior generality" with "competitive performance on three KGQA benchmarks." Replace "outperforms all baselines" with "outperforms all prompting-based baselines under matched settings; comparisons with fine-tuned methods use different backbone models."

**Location:** Abstract, Introduction (contributions), Conclusion.
**Expected benefit:** Prevents reviewer rejection on overclaiming grounds.

### S5 (Must) — Add failure analysis to case study
In the case study (Table 5), explicitly state that FiDeLiS finds 3/5 correct answers (F1=0.857), analyze why "Parliamentary system" and "Presidential system" were missed, and clarify that ToG's limitation is in answer aggregation rather than KG retrieval.

**Location:** Section 3.3, Case Study paragraph.
**Expected benefit:** Improves scientific honesty and provides actionable insight into Path-RAG limitations.

### S6 (Nice-to-have) — Revise α description
Replace "The factor α is used to balance short-term outcomes and long-term potential" with "We introduce α to weight the influence of next-hop information. In practice (Appendix Table 9), performance is relatively stable across α ∈ [0.1, 1.0], suggesting the scoring function is dominated by immediate similarity. We set α = 0.3 as a conservative default."

**Location:** Page 4, below Eq. (3).
**Expected benefit:** Aligns textual claims with empirical evidence.

### S7 (Nice-to-have) — Add keyword recall analysis
Report the average number of generated keywords per query and the recall of ground-truth KG relations achievable by the keyword list. This quantifies the "exhaustive" claim.

**Location:** Add as a small table or paragraph in Section 3.3 or Appendix D.
**Expected benefit:** Strengthens the retrieval contribution claim.

### S8 (Nice-to-have) — Reorganize Related Work
Restructure Section 4 around three comparison axes: (1) graph-retrieval methods, (2) path-generation methods, (3) graph-exploration methods. For each axis, state the specific difference of FiDeLiS.

**Location:** Section 4.
**Expected benefit:** Makes novelty positioning clearer.

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis

The current introduction follows this structure:
- P1: LLMs are powerful but hallucinate.
- P2: KGs provide faithful knowledge. KGQA is a key testbed.
- P3: Challenge (I): How to retrieve from KGs precisely.
- P4: Challenge (II): How to make LLMs utilize KG structure.
- P5: We propose FiDeLiS (Path-RAG + DVBS).
- P6: Contributions.

**Problems:** (1) The two research questions are too broad and not clearly linked to the specific technical solutions. (2) The forward-reference to Section 3.3's 67% error analysis breaks narrative flow. (3) The contribution list mixes methodological novelty with performance outcomes.

### Recommended Storyline

**Candidate A (Recommended): Problem-first, mechanism-driven**
1. **Big Picture:** LLMs hallucinate in complex reasoning; KGs offer grounded facts but integrating them is non-trivial.
2. **Concrete Gap:** Two specific failure modes — (a) retrieved paths may be irrelevant (schema mismatch, missing intermediates), (b) path scoring/stopping is unreliable (either premature or excessive exploration).
3. **Solution Intuition:** Instead of asking the LLM to score paths numerically (logit-based) or assess adequacy (ToG), convert scoring into a deductive verification task: does the current path logically entail the answer?
4. **How it works:** Path-RAG retrieves high-recall candidates; DVBS uses deductive verification for selection and stopping.
5. **Evidence Preview:** Outperforms ToG by 2-3% across three datasets with 1.7x fewer LLM calls; paths are closer to ground-truth depth.

### Abstract Outline (5-Sentence Plan)

**S1 (Problem):** "Large language models (LLMs) frequently generate factually incorrect or hallucinated responses in complex reasoning tasks, limiting their deployment in high-stakes domains."

**S2 (Gap):** "Existing methods that ground LLM reasoning in knowledge graphs (KGs) either retrieve semantically shallow paths or struggle with unreliable path scoring and premature stopping."

**S3 (Method):** "We propose FiDeLiS, a training-free framework that combines keyword-enhanced KG retrieval (Path-RAG) with deductive-verification-guided beam search (DVBS), which replaces traditional logit-based scoring with a deductive reasoning criterion to select and terminate reasoning paths."

**S4 (Key Results):** "On three KGQA benchmarks (WebQSP, CWQ, CR-LT), FiDeLiS achieves 84.39%, 71.47%, and 72.12% accuracy respectively with GPT-4-turbo, outperforming prompting-based baselines while reducing LLM calls by 1.7x versus ToG."

**S5 (Bounded Implication):** "The results demonstrate that deductive verification provides a practical and principled stopping criterion for graph-grounded LLM reasoning, though cross-task generalization remains to be validated."

### Introduction Outline (6-Paragraph Plan)

**P1 — The unreliability problem in LLM reasoning:**
"LLMs exhibit strong reasoning capabilities through step-by-step thinking, yet their outputs frequently conflict with factual knowledge, undermining reliability in high-stakes applications like healthcare and science. This paper addresses the challenge of grounding LLM reasoning in structured, verifiable knowledge sources."
*Evidence anchor: Cite LLM hallucination challenges, cite KG benefits.*

**P2 — KGs as a grounding source and the KGQA task:**
"Knowledge graphs store structured, traceable factual knowledge that can serve as a reliable reasoning substrate. Knowledge Graph Question Answering (KGQA) provides a well-defined testbed for measuring how effectively LLMs can leverage KGs."
*Evidence anchor: Define KGQA, reference WebQSP/CWQ/CR-LT.*

**P3 — Gap (I): Retrieval challenges:**
"Current KG retrieval approaches face two specific limitations. Direct retrieval via cosine similarity may miss semantically relevant paths due to KG schema variations (e.g., machine identifiers vs. descriptive labels). Semantic parsing methods suffer from non-executable or incorrect query generation."
*Evidence anchor: Cite specific limitations in prior work.*

**P4 — Gap (II): Path scoring and stopping challenges:**
"Existing methods that score paths via LLM logits (ToG) or fine-tuned path generation (RoG) are unreliable. ToG's adequacy assessment can lead to premature or excessive stopping; RoG generates paths where only 67% of steps are valid in the KG."
*Evidence anchor: Reference the error analysis (which should be moved to experiments rather than introduced here).*

**P5 — Solution overview:**
"To address both gaps, we propose FiDeLiS, which combines Path-RAG for high-recall KG retrieval with DVBS for deductive-verification-guided beam search. Path-RAG uses LLM-generated keywords to maximize coverage of relevant entities and relations. DVBS converts path scoring into a deductive reasoning task, providing precise termination signals."
*Evidence anchor: Refer to Figure 1 for architecture overview.*

**P6 — Contributions and paper organization:**
"Concretely, our contributions are: (1) a retrieval-augmented framework combining keyword-based KG retrieval with deductive beam search, (2) a step-wise keyword retrieval method that enhances recall of intermediate KG entities, (3) a deductive verification criterion for precise path termination, and (4) empirical validation showing competitive accuracy and reduced computational cost on three benchmarks. The remainder of the paper is organized as follows..."
*Evidence anchor: Forward-reference to Sections 2, 3.*

### Alignment Checks

| Check | Current Storyline | Recommended Storyline |
|-------|------------------|----------------------|
| Problem alignment | Broad: "LLMs hallucinate" | Specific: "Two concrete failure modes (retrieval schema mismatch + unreliable path scoring)" |
| Variable alignment | Keywords and beam search introduced separately | Path-RAG keyword retrieval and DVBS deductive verification introduced as linked components |
| Contribution-evidence alignment | Claims superiority without qualification | Claims competitive performance on bounded setting + efficiency advantage |

## Priority Revision Plan
### P0 — Publication-Critical (Must fix before acceptance)

| Priority | Action | Section | Effort | Impact |
|----------|--------|---------|--------|--------|
| P0.1 | Add controlled backbone experiment (FiDeLiS vs ToG vs RoG with same Llama-2-13B backbone) | Section 3.1, Table 1 | Low (run existing code with changed backbone) | High — resolves fairness objection |
| P0.2 | Specify ablation replacements in text | Section 3.2 | Minimal (add one sentence per ablation) | High — enables interpretability |
| P0.3 | Correct Eq. (4) to reflect selection, not generation | Section 2.2 | Minimal (notation fix) | High — removes technical ambiguity |
| P0.4 | Bound claims: replace "superior generality" and "outperforms all baselines" with qualified wording | Abstract, Introduction, Conclusion | Minimal (word edits) | High — prevents rejection on overclaiming |
| P0.5 | Add failure analysis to case study (missing 2/5 answers) | Section 3.3 | Minimal (2-3 sentences) | Medium-High — improves scientific honesty |

### P1 — High Impact but Moderate Effort

| Priority | Action | Section | Effort | Impact |
|----------|--------|---------|--------|--------|
| P1.1 | Add keyword recall statistics (avg keywords, relation coverage) | Section 3.3 or Appendix | Low (one small table) | Medium — strengthens retrieval contribution |
| P1.2 | Discuss α insensitivity and revise text | Section 2.1, Appendix D.3 | Minimal | Medium — aligns claim with evidence |
| P1.3 | Add discussion of circular validation risk in deductive verification | Section 2.2 | Minimal (one sentence) | Medium — improves defensive writing |

### P2 — Nice-to-Have Improvements

| Priority | Action | Section | Effort | Impact |
|----------|--------|---------|--------|--------|
| P2.1 | Reorganize Related Work by methodological axes | Section 4 | Moderate (restructure) | Medium — clarity |
| P2.2 | Report statistical significance tests for main results | Section 3.1 | Low | Medium — robustness |
| P2.3 | Add edge-case failure analysis (e.g., questions with no valid path) | Section 3.3 | Low-Medium | Medium — completeness |

### Revision Order (Recommended Execution Sequence)

```text
Stage 1 (Today — text edits only, < 2 hours):
  P0.2 + P0.3 + P0.4 + P0.5 + P1.2 + P1.3
  → Improves precision, honesty, and defensibility

Stage 2 (This week — experiments):
  P0.1 (controlled backbone comparison)
  P1.1 (keyword recall analysis)
  P2.2 (significance tests)

Stage 3 (Before submission — restructuring):
  P2.1 (Related Work reorganization)
  P2.3 (failure analysis)
  → Polishes narrative positioning
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (Data/Split/Protocol/Baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|-------------|-----------------|-------------------|
| E1 | Compare FiDeLiS vs prompting-only baselines | WebQSP, CWQ, CR-LT; Zero-shot, Few-shot, CoT | Hits@1, F1, Acc | FiDeLiS outperforms all prompting-only baselines | FiDeLiS improves over LLM-only methods | Different backbone models used across comparisons |
| E2 | Compare FiDeLiS vs KG-augmented baselines (ToG, RoG, DeCAF, NSM, etc.) | WebQSP, CWQ, CR-LT; ToG with same beam width/depth=4 | Hits@1, F1, Acc | FiDeLiS (GPT-4) > ToG > other methods | FiDeLiS is competitive with/beats fine-tuned methods | Backbone mismatch: FiDeLiS uses GPT-4, fine-tuned methods use smaller models |
| E3 | Ablate Path-RAG component | Replace Path-RAG with vanilla retriever or ToG retrieval | Hits@1, F1, Acc | Path-RAG gives 4-8% improvement over alternatives | Path-RAG is more effective than vanilla retrieval | "Vanilla retriever" baseline design not fully specified |
| E4 | Ablate DVBS subcomponents | Remove beam-search, planning, deductive-verifier, last-step reasoning | Hits@1, F1, Acc | Beam search removal causes 19% drop | Beam search is critical | "w/o beam-search" alternative not described |
| E5 | Compare embedding backbones | BM25, SentenceBert, E5, OpenAI-Embedding-Model | Hits@1, Acc | OpenAI embedding best; Path-RAG uniformly better than vanilla retriever | Better embeddings improve retrieval | No analysis of embedding dimension/speed trade-off |
| E6 | Beam width/depth sensitivity | Width 1-4, Depth 1-4 on WebQSP, CWQ | Hits@1 | Performance peaks at depth 3; width consistently helps | Depth beyond 3 unnecessary for these datasets | Only explored up to depth 4 |
| E7 | Path coverage ratio comparison | Path-RAG vs vanilla retriever on CWQ, WebQSP | Coverage Ratio (CR) | Path-RAG achieves higher CR | Path-RAG better aligns with ground-truth paths | Only 2 datasets; CR metric definition may favor longer paths |
| E8 | Deductive verification effectiveness | Compare average path depths of ToG and FiDeLiS | Average depth | FiDeLiS paths closer to GT depth | Deductive verification provides better stopping | No direct comparison with other stopping criteria |
| E9 | Efficiency comparison | FiDeLiS vs ToG; also with GPT-4o, GPT-4o-mini | Avg runtime, tokens, LLM calls | FiDeLiS 1.7x faster than ToG | Path-RAG reduces unnecessary computation | Runtime variance not reported |
| E10 | KG perturbation robustness | Edge deletion, rewiring, relation replacement, swapping at 10-40% | Hits@1 | Performance degrades gracefully | Method is robust to moderate KG noise | Only tested on one dataset; noise type simplified |
| E11 | Open-source LLM evaluation | Llama-2-13B, Mistral-7B | Hits@1, F1, Acc | FiDeLiS works with open-source models | Method is backbone-agnostic | Performance gap vs GPT-4 is large (e.g., 72% vs 84% on WebQSP) |
| E12 | α parameter sensitivity | α from 0.1 to 1.0 on WebQSP | Hits@1 | Only 0.84% variance across full range | α has minimal impact | Contradicts text about "balancing short-term and long-term" |

### Research-Theme Gap Diagnosis

| Research Value Dimension | Current Support | Gap |
|-------------------------|----------------|-----|
| New knowledge | Partially supported | The deductive verification stopping criterion is conceptually new, but similar ideas exist in deductive verification of CoT. Need clearer differentiation. |
| Reproducibility | Mostly supported | Code release + prompt documentation provided. Missing: exact hyperparameters for all datasets, compute hardware details. |
| Impact on practice/understanding | Partially supported | Shows KG grounding helps for long-tail entities. Limited by single task (KGQA) and 3 datasets. Cross-domain validation needed. |

### Proposed Research Experiments (P0/P1/P2)

**Exp-P0.1 — Controlled Backbone Comparison (Must)**
- Target Claim: "FiDeLiS outperforms baselines" (Current Version 1 of this claim)
- Hypothesis: Under identical backbone (Llama-2-13B), FiDeLiS still outperforms ToG and RoG.
- Minimal Design: Run FiDeLiS, ToG, and RoG all with Llama-2-13B on WebQSP and CWQ. Same beam width=4, depth=4.
- Controls: Same few-shot examples, same temperature.
- Metrics: Hits@1, F1.
- Success Criterion: FiDeLiS achieves statistically significant improvement over ToG (>2% Hits@1).
- Estimated Cost: ~$50-100 API calls, 1-2 days.
- Expected Quality Gain: Resolves primary fairness objection.

**Exp-P0.2 — Ablation Specification (Must)**
- Target Claim: Component-level contribution.
- Hypothesis: The described alternatives produce the reported deltas.
- Design: Run three additional conditions: (a) greedy beam=1, (b) no stopping max_depth=4, (c) no planning context.
- Success Criterion: Results confirm Table 2 patterns.
- Estimated Cost: Minimal (already running ablation code; just report the alternative).
- Expected Quality Gain: Ablations become interpretable.

**Exp-P1.1 — Keyword Recall Analysis (High Value)**
- Target Claim: "Exhaustive keyword list" and "high-recall retrieval."
- Hypothesis: The LLM-generated keyword list covers >90% of ground-truth KG relations needed for answers.
- Design: For 100 sampled questions from WebQSP and CWQ, compare generated keyword set against gold KG paths. Report average recall@m for m=5,10,20.
- Controls: Compare with TF-IDF keyword extraction.
- Success Criterion: LLM keyword recall > 85% at m=10.
- Estimated Cost: Low (1-2 days, no new LLM calls needed).
- Expected Quality Gain: Quantifies and strengthens the retrieval contribution.

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2 Sequencing)

Stage 1 (Today-Week 1): Claim Integrity Fixes
  [P0.1 Controlled Backbone Comp.] ──► resolves fairness objection
  [P0.2 Ablation Specification]    ──► ablation interpretability
  
Stage 2 (Week 1-2): Evidence Strengthening
  [P1.1 Keyword Recall Analysis]   ──► quantifies retrieval claim
  [P1.2 α Sensitivity Discussion]  ──► aligns text with evidence
  [P2.2 Significance Tests]        ──► statistical rigor

Stage 3 (Week 2-3): Narrative Polish
  [P2.1 Related Work Reorg]        ──► clearer positioning
  [P2.3 Failure Analysis]         ──► honest limitations
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 5.5 / 10

**Rationale:** The paper presents a genuinely interesting idea (deductive verification for beam search termination in KGQA) with solid empirical evaluation across three datasets. The training-free architecture and 1.7x efficiency gain over ToG are practically meaningful. However, the score is constrained by:

- **Research Value (6/10):** The incremental contribution is moderate. The two main components (keyword retrieval and deductive verification) are adaptations of existing ideas rather than fundamental breakthroughs. The primary novelty is the *combination* and the *application of deductive reasoning as a stopping criterion*, which is well-motivated but not deeply analyzed (e.g., no analysis of verification failures, no independent verifier).

- **Novelty (5/10):** Retrieval-augmented KGQA is a well-studied area. Path-RAG combines LLM keyword generation with vector search, which is effective but not conceptually new. DVBS's deductive verification criterion is the strongest novel component, but it uses the same LLM for both path generation and verification, introducing circularity concerns. **External literature verification was not available in this run (Retrieval-Disabled Mode); novelty verdicts should be treated as provisional pending manual literature review.**

- **Validity/Soundness (5/10):** The paper has several validity concerns: uncontrolled backbone comparisons in main claims, underspecified ablations, ambiguous equation notation, and case study incompleteness. These are fixable but currently weaken confidence in the reported results.

- **Reproducibility (6/10):** Code will be released, prompts are documented, but several implementation details (ablation alternatives, exact candidate filtering thresholds, keyword generation parameters) are missing.

- **Presentation (6/10):** The paper is generally well-written with clear figures, but the introduction overclaims, the related work is list-style, and several typos exist ("presie," "STOA," "Specially").

### Post-Revision Target: [6.5, 7.5] / 10

If all P0 items are addressed (controlled backbone experiment, specified ablations, corrected notation, bounded claims, case study completeness) plus at least P1.1 (keyword recall analysis), the score can rise to the 6.5-7.5 range. The upper bound assumes the controlled experiment confirms the claimed advantage and the authors convincingly address the circular verification concern.

```text
ASCII Diagram — Paper Structure & Evidence Map

[Problem: LLMs hallucinate in complex reasoning]
     │
     ▼
[KG Grounding: KGs provide traceable facts]
     │
     ├──► [Challenge I: Retrieve precise KG paths]
     │        ├── Existing: Direct retrieval misses intermediates (schema mismatch)
     │        └── Existing: Semantic parsing → non-executable queries
     │
     ├──► [Challenge II: Score & stop paths reliably]
     │        ├── Existing: ToG uses logit scores → unreliable adequacy assessment
     │        └── Existing: RoG generates paths → 33% invalid steps
     │
     ▼
[FiDeLiS Solution]
     │
     ├──► Path-RAG: LLM keyword list + vector retrieval + next-hop scoring (Eq 1-3)
     │        └── Evidence: Table 3 (embedding comparison), Figure 3 (coverage ratio)
     │
     └──► DVBS: Natural language plan + beam search + deductive verification (Eq 4-6)
              └── Evidence: Table 2 (ablation), Table 4 (path depth), Table 6 (efficiency)
     │
     ▼
[Empirical Validation: 3 KGQA datasets]
     ├── WebQSP: 84.39% Hits@1 (GPT-4)
     ├── CWQ: 71.47% Hits@1
     └── CR-LT: 72.12% Acc
     │
     ▼
[Key Gaps]
     ├── Backbone-controlled comparison missing
     ├── Ablation alternatives unspecified
     ├── Keyword recall unquantified
     └── Circular verification risk unaddressed


ASCII Diagram — Revision Strategy Roadmap

[Overclaimed Generality]
    └──► Fix: Bound wording + add controlled backbone experiment
         └──► Expected: Removes top validity objection

[Underspecified Ablations]
    └──► Fix: Add one sentence per ablation describing alternative
         └──► Expected: Ablations become interpretable

[Ambiguous Eq (4)]
    └──► Fix: LM(st|...) → Score(st;...) to reflect selection
         └──► Expected: Removes generation vs selection confusion

[Case Study Incompleteness]
    └──► Fix: Report 3/5 correct, analyze 2 missed answers
         └──► Expected: Improves scientific honesty

[No Statistical Significance]
    └──► Fix: Add significance tests for main results
         └──► Expected: Strengthens reliability of reported gains


ASCII Diagram — Related-Work Taxonomy Tree (Layered)

Root: KG-Grounded LLM Reasoning for QA
│
├── Branch 1: Retrieval Paradigm
│   ├── Leaf 1.1: Direct vector retrieval (PullNet, DPR)
│   ├── Leaf 1.2: Semantic parsing → SPARQL (SPARQA, ArcaneQA)
│   └── Leaf 1.3: Keyword-enhanced retrieval ← FiDeLiS Path-RAG
│
├── Branch 2: Path Construction Approach
│   ├── Leaf 2.1: Path generation via fine-tuned LM (RoG, DeCAF, KD-CoT)
│   │   └── Risk: Generated paths may not exist in KG (33% invalid)
│   ├── Leaf 2.2: Iterative graph exploration (ToG, StructGPT, ReAct)
│   │   └── Risk: Unreliable stopping (premature/excessive)
│   └── Leaf 2.3: Retrieval + beam search with deductive stopping ← FiDeLiS DVBS
│       └── Novelty: Deductive verification replaces logit scoring
│
└── Branch 3: Supervision Regime
    ├── Leaf 3.1: Fine-tuned methods (NSM, CBR-KBQA, DeCAF, RoG)
    └── Leaf 3.2: Training-free / prompting-based (ToG, FiDeLiS)
        └── Value: Lower compute barrier, easier adaptation to new KGs

Note: External literature verification was not available in this run (Retrieval-Disabled Mode due to paper_search unavailability). Novelty/comparison conclusions are intentionally deferred — the taxonomy above is a structural skeleton that should be populated with specific paper citations and validated overlap assessments in a manual literature review.
```