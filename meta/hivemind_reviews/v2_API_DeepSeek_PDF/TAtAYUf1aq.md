## Summary
This paper presents Memoria, a memory-augmentation module for Transformer-based models that organizes stored vector representations ("engrams") into three tiers — working memory, short-term memory, and long-term memory — inspired by the Multi-Store cognitive model. Connection strengths between engrams are represented as directed edge weights in a graph, where each weight $E_{i\rightarrow j} = \text{Count}_{i,j} / \text{Count}_{i,i}$ estimates the conditional probability that engram $j$ is retrieved when engram $i$ is activated. This update rule is claimed to satisfy six desiderata for Hebbian plasticity models.

The module operates in three stages: **Remind** (querying short-term and long-term memory via working memory using L2-distance correlation, followed by a greedy DFS traversal of the long-term memory graph), **Exploit** (cross-attention over retrieved engrams), and **Memorize & Forget** (updating co-occurrence counts, adjusting engram lifespans based on attention weights, and removing expired engrams).

Memoria is evaluated on three task families: (1) a synthetic sorting task requiring frequency-based order reconstruction for sequences up to 32K tokens, (2) language modeling on WikiText-103, PG-19, and enwik8, and (3) long-document classification on Hyperpartisan. The method shows its strongest gains on the sorting task (63.4% accuracy at 32 segments vs. 39.7% for ∞-former) and WikiText-103 (23.47 perplexity vs. 24.69). However, gains on PG-19 and enwik8 are marginal or nonexistent. The classification results show a statistically significant but marginal improvement (p=0.045) over Longformer.

**Primary contributions:** a three-tier memory architecture with count-based Hebbian weight updates, integration strategies for encoder and decoder Transformers, and empirical results across three task domains.

**Core weaknesses:** overstated Hebbian claims, high GPU memory overhead (~5x Transformer-XL), marginal gains on key language modeling benchmarks, missing variance reporting for LM experiments, and a conclusion that uses hype language unsupported by the evidence.

## Strengths
**1. Novel architectural concept with cognitive inspiration.** The three-tier memory hierarchy (working, short-term, long-term) with directed graph-based retrieval is a well-motivated architectural choice that goes beyond simple segment-level recurrence. The use of count-based co-occurrence to represent Hebbian-style connection strengths provides a clean, interpretable mechanism for memory reinforcement.

**2. Strongest results on the sorting task.** The synthetic sorting benchmark (up to 32K tokens, 32 segments) provides the clearest evidence for Memoria's effectiveness. At 32 segments, Memoria achieves 63.42% accuracy compared to ∞-former's 39.71% — a substantial 23.7 percentage point improvement. The ablation study (Appendix C) convincingly demonstrates that different memory tiers contribute complementary benefits at different sequence lengths, with LTM becoming more important as context grows.

**3. Modular design and integration flexibility.** Memoria is designed as a pluggable module that can be attached to various Transformer architectures, demonstrated with both decoder-only (GPT) and encoder-only (BERT/RoBERTa) models. The Python package implementation supports reusability. The integration strategy is clearly described in Appendix F with architectural diagrams.

**4. Comprehensive ablation and analysis.** The ablation study (Page 17, Appendix C) is a strong point: it separates the contributions of working memory, STM, and LTM, showing how each component's importance shifts with sequence length. The autocorrelation analysis (Appendix D) and the age-of-reminded-engrams analysis (Figure 5) provide useful insights into Memoria's retrieval dynamics. The theoretical complexity analysis (Appendix E) helps understand computational tradeoffs.

**5. Honest empirical analysis of computational cost.** Unlike many papers that only report performance gains, Memoria provides both theoretical and empirical complexity comparisons (Table 9), openly reporting 45.4 GB GPU memory usage and discussing the tradeoffs. This transparency is commendable and helps the community understand deployment feasibility.

## Weaknesses
**W1. Overstated Hebbian claims (Severity: Major).** The paper claims Memoria "applies Hebbian theory" and "satisfies various properties of Hebb's rule, including long-term potentiation." In reality, the weight update $E_{i\rightarrow j} = \text{Count}_{i,j} / \text{Count}_{i,i}$ is a statistical co-occurrence ratio, not a biologically detailed model of spike-timing-dependent plasticity (STDP). The cooperativity property is only partially satisfied because $E_{i\rightarrow j}$ can decrease when $e_i$ fires without $e_j$ (dilution effect), which does not occur in biological LTP for individual synapses. The strong biological framing creates an expectation the method does not fulfill. (See annotation: Page 1 - Abstract, Page 1 - Introduction Paragraph 2, Page 3 - Hebbian attributes.)

**W2. Marginal or absent gains on key language modeling benchmarks (Severity: Major).** On PG-19, Memoria (29.149 PPL) is virtually identical to ∞-former (29.154 PPL). On enwik8, Memoria (1.16 BPC) ties with Compressive Transformer (1.16). These results contradict the abstract's claim that Memoria "outperformed existing methodologies" across all tasks. The paper also does not report variance or confidence intervals for any language modeling experiment (Table 1, Table 2), making it impossible to assess statistical significance. (See annotation: Page 8 - Language Modeling Results.)

**W3. High GPU memory overhead with incomplete analysis (Severity: Major).** Memoria uses 45.4 GB GPU memory — approximately 5x Transformer-XL (8.8 GB). The paper attributes ~30% to the adjacency matrix but does not provide a detailed breakdown. A back-of-the-envelope calculation (float32 adjacency for N≈58K engrams yields ~13.5 GB) suggests the estimate is plausible but unverified. The paper's suggestion to use adjacency lists is mentioned but not validated experimentally. (See annotation: Page 21 - Empirical Analysis.)

**W4. Marginal classification significance with uncontrolled capacity (Severity: Major).** The p-value for Memoria RoBERTa vs. Longformer is 0.045 — barely below the 0.05 threshold. With only 5 runs, this is not strong evidence. Furthermore, Memoria adds extra parameters (memory encoder, cross-attention) that are not present in the baseline RoBERTa or Longformer models, creating a capacity confound. The standard deviations reported (±0.01 to ±0.04) are unusually small for a 5-run experiment on a classification task. (See annotation: Page 9 - Classification results.)

**W5. Formula-level ambiguities affecting reproducibility (Severity: Major).** Several key formulas lack sufficient specification: (a) the memory encoder formula (Page 7) has dimensional ambiguity and time-index inconsistency ($X_t = h_{t-1}$); (b) the lifespan increment formula (Page 6) does not specify how $w_i$ is computed (average over heads × positions?); (c) the Count initialization is unspecified (division by zero risk); (d) the DFS retrieval (Page 5) has no fallback for sink nodes. (See annotations: Page 7 - Memory Encoder, Page 6 - Lifespan increment, Page 4 - Memory Graph weight, Page 5 - DFS retrieval.)

**W6. Overclaimed conclusion (Severity: Major).** The conclusion states Memoria "demonstrates the potential to revolutionize the way deep neural networks process and retain information." This is hype language completely unsupported by the evidence — the method shows modest gains on a subset of benchmarks with substantial computational overhead. (See annotation: Page 9 - Conclusion.)

**W7. Missing critical experimental controls (Severity: Minor-Major).** The paper does not include: (a) parameter-matched baselines to control for added capacity from Memoria; (b) out-of-distribution evaluation (all benchmarks are IID); (c) sensitivity analysis for key hyperparameters ($\alpha$, $N_{\text{depth}}$, initial lifespan, STM capacity); (d) comparison with simpler memory mechanisms (e.g., a fixed-size FIFO buffer without Hebbian updates). (See annotation: Page 8 - Language Modeling Results.)

**W8. Novelty claims require external verification (Severity: Minor — deferred).** Due to Retrieval-Disabled Mode, I cannot verify whether the core ideas (count-based co-occurrence memory, three-tier architecture for Transformers) overlap with existing work in memory-augmented neural networks, Hopfield networks, or Hebbian deep learning. This verification is deferred to manual review.

## Key Issues
### Issue 1: Hebbian claim overreach (Severity: Major, Fixability: Easy)

The paper repeatedly asserts that Memoria's update rule is "Hebbian" and satisfies "long-term potentiation," but the mechanism is a count-based statistical ratio, not a biologically plausible plasticity model. The cooperativity claim in Appendix A is misleading: $E_{i\rightarrow j} \propto \text{Count}_{i,j}$ is true, but $E_{i\rightarrow j}$ can decrease when $e_i$ fires without $e_j$ (because $\text{Count}_{i,i}$ increases), which is not consistent with strict Hebbian LTP at the synaptic level. This overclaim can be fixed by qualifying the biological analogy and explicitly describing the differences.

**Fix:** Replace "Hebbian" with "Hebbian-inspired" throughout; add one paragraph in Section 3 explaining the departures from biological Hebbian plasticity.

### Issue 2: Incomplete statistical evidence for language modeling (Severity: Major, Fixability: Easy)

Table 1 reports perplexity without variance, confidence intervals, or significance tests. On PG-19, Memoria (29.149) and ∞-former (29.154) are essentially tied. The text claims "Memoria outperformed" without caveats. This undermines scientific credibility.

**Fix:** Add 3-seed variance to Table 1, add a significance test (e.g., paired bootstrap) against the strongest baseline for each dataset, and explicitly discuss cases where gains are marginal.

### Issue 3: Capacity confound in classification experiments (Severity: Major, Fixability: Medium)

Memoria RoBERTa adds extra parameters (memory encoder, cross-attention, graph) beyond the base RoBERTa model. The comparison with Longformer and BigBird is therefore not capacity-matched. Part of the gain may come from extra parameters rather than the memory mechanism.

**Fix:** Add a controlled baseline: RoBERTa with additional feedforward layers matching Memoria's added parameter count. Report the number of added parameters for each Memoria variant.

### Issue 4: GPU memory overhead not adequately analyzed (Severity: Major, Fixability: Medium)

Memoria uses 45.4 GB vs. Transformer-XL's 8.8 GB (5x). While the paper acknowledges this, the analysis is incomplete: (a) no detailed memory breakdown, (b) no ablation on graph representation (adjacency list vs. matrix), (c) no practical recommendations for reducing memory under deployment constraints.

**Fix:** Provide a memory breakdown table (base model, adjacency matrix, cross-attention cache, engram storage). Implement and evaluate at least one sparse alternative (top-k adjacency, adjacency list, or CPU offloading).

### Issue 5: Formula ambiguities hurting reproducibility (Severity: Major, Fixability: Easy)

Four formula-level issues need resolution: (a) $X_t = h_{t-1}$ time-index inconsistency, (b) $Inc_i$ formula missing $w_i$ computation detail, (c) Count initialization unspecified, (d) DFS sink node fallback missing.

**Fix:** Address each in a revision as detailed in the relevant annotations.

### Issue 6: Conclusion hype (Severity: Minor, Fixability: Easy)

"Revolutionize" language in the conclusion is inappropriate for the demonstrated contribution. Replace with measured, evidence-bounded claims.

**Fix:** Replace the final paragraph with three concise parts: validated findings, bounded limitations, and concrete next steps.

### Issue 7: Missing hyperparameter sensitivity analysis (Severity: Minor, Fixability: Medium)

The method introduces several hyperparameters ($\alpha$, $N_{\text{depth}}$, initial lifespan, STM capacity, $N_{\text{wm}}$, $N_{\text{stm}}^{\text{rem}}$, $N_{\text{ltm}}^{\text{rem}}$) whose sensitivity is not analyzed. Only one configuration is reported per experiment.

**Fix:** Add a sensitivity study for at least the two most critical hyperparameters ($\alpha$ and $N_{\text{depth}}$) on one dataset, with a recommended default range.

## Actionable Suggestions
### S1 (Must): Qualify Hebbian claims throughout
- **Location:** Abstract, Page 1 Intro Paragraph 2, Page 3 Related Work, Appendix A
- **Current:** "applies Hebbian theory," "satisfies various properties of Hebb's rule including long-term potentiation"
- **Action:** Change to "Hebbian-inspired" or "count-based approximation of Hebbian plasticity." Add a sentence in Section 3 explicitly stating: "Unlike biological STDP, our update does not depend on precise spike timing; it uses statistical co-occurrence frequencies. Consequently, the cooperativity property is satisfied only in expectation, not at the individual synapse level."
- **Expected benefit:** Removes a major reviewer objection about overclaimed biological plausibility.

### S2 (Must): Add variance and significance to language modeling experiments
- **Location:** Page 8, Table 1, Table 2
- **Action:** Run all LM experiments with 3 random seeds and report mean ± std. Add a paired bootstrap test for each dataset comparing Memoria against the strongest baseline. In the text, explicitly discuss PG-19 (tied with ∞-former) and enwik8 (tied with Compressive Transformer) as cases where Memoria does not improve.
- **Expected benefit:** Restores scientific credibility and provides accurate signal for reviewers.

### S3 (Must): Add capacity-controlled baseline for classification
- **Location:** Page 9, Table 3
- **Action:** Report the number of added parameters for Memoria BERT and Memoria RoBERTa. Add a baseline: RoBERTa + extra FFN layers matching the added parameter count. Retain the comparison with Longformer/BigBird as secondary.
- **Expected benefit:** Addresses the capacity confound concern and strengthens the claim that gains come from the memory mechanism, not extra parameters.

### S4 (Must): Fix formula ambiguities
- **Location:** Page 7 (Memory encoder formula), Page 6 (Lifespan increment), Page 4 (Count initialization), Page 5 (DFS algorithm)
- **Actions:**
  - (a) Fix $X_t = h_{t-1}$ notation: rename to $X_t = h_{t-1}$ with an explicit note that $t$ indexes segments.
  - (b) Add: "$w_i = \frac{1}{H \times L} \sum_{h=1}^H \sum_{p=1}^L A_{h,p,i}$ where $A$ is the cross-attention weight for head $h$, query position $p$, and engram $i$."
  - (c) Add: "Count$_{i,i} = 1$ and Count$_{i,j} = 0$ for $i \neq j$ at engram creation."
  - (d) Add: "If a node has no outgoing edges, the DFS terminates at that node."
- **Expected benefit:** Ensures reproducibility, a key acceptance criterion.

### S5 (Must): Rewrite conclusion to remove hype
- **Location:** Page 9, Conclusion
- **Current:** "Memoria demonstrates the potential to revolutionize the way deep neural networks process and retain information, opening avenues for improved performance in a wide range of tasks."
- **Action:** Replace with validated findings summary (sorting + WikiText-103 gains), bounded limitations (high memory cost, marginal gains on some benchmarks), and concrete next steps (sparse graph, interference-based forgetting, OOD evaluation).
- **Expected benefit:** Aligns claims with evidence and avoids reviewer backlash.

### S6 (Nice-to-have): Hyperparameter sensitivity analysis
- **Location:** Add an appendix subsection
- **Action:** Vary $\alpha$ (e.g., {4, 8, 16}) and $N_{\text{depth}}$ (e.g., {5, 10, 20}) on the sorting task (32K length). Report accuracy for each configuration and recommend a default range.
- **Expected benefit:** Demonstrates robustness and helps practitioners configure Memoria.

### S7 (Nice-to-have): Memory cost optimization experiment
- **Location:** Page 21, Appendix E.2
- **Action:** Implement adjacency list representation for the memory graph (store only top-k edges per node). Compare GPU memory and training time with the current dense adjacency matrix. Report the tradeoff between sparsity level and retrieval accuracy.
- **Expected benefit:** Addresses the main practical limitation of the method and provides a deployment-friendly variant.

### S8 (Nice-to-have): Add a simpler memory baseline
- **Location:** All experiments, add a new column
- **Action:** Add a baseline that uses a simple FIFO buffer of past hidden states (without Hebbian graph, without DFS, without lifespan) with cross-attention. This controls for the benefit of the memory mechanism itself vs. the specific Hebbian implementation.
- **Expected benefit:** Isolates the value of the Hebbian-inspired retrieval mechanism from the value of having any external memory at all.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows this sequence:
1. P1: Human memory abilities (descriptive, generic)
2. P2: Hebbian theory explanation (textbook-like)
3. P3: Transformers need memory for long-range tasks
4. P4 (Page 2): Transformer's O(L^2) limitation + Memoria proposal
5. P5: Memoria description and evaluation summary

**Problem:** The first two paragraphs read as motivational filler without establishing a specific technical gap. The reader must wait until Page 2 (P4) to learn what problem is actually being solved. Hebbian theory (P2) and human memory (P1) are introduced independently without showing why they are the *right* solution to the Transformer limitation.

### Recommended Storyline (Candidate A)

**Title:** "Memoria: A Three-Tier Hebbian Memory Module for Long-Range Sequence Processing in Transformers"

**Abstract Outline (S1-S5):**
- **S1 (Problem):** "Transformers are limited to fixed context windows by their quadratic self-attention cost, and segment-level recurrence only partially mitigates this because information degrades across segments."
- **S2 (Prior Gap):** "Existing memory-augmented approaches either compress past information into fixed-size states (Transformer-XL) or rely on sparse attention patterns that still have limited effective range."
- **S3 (Proposed Solution):** "We propose Memoria, a plug-in memory module that stores vector engrams in three tiers — working memory, short-term memory, and long-term memory — and retrieves them via a learned co-occurrence graph inspired by Hebbian plasticity."
- **S4 (Key Result):** "On a synthetic sorting task requiring frequency counting over up to 32K tokens, Memoria achieves 63.4% accuracy, substantially outperforming ∞-former (39.7%). On WikiText-103 language modeling, perplexity improves from 24.69 to 23.47."
- **S5 (Bounded Implication):** "Memoria demonstrates that explicit multi-tier memory with graph-based retrieval can improve long-range dependency modeling, though at a 5x GPU memory cost that requires further optimization."

**Introduction Outline (P1-P5):**

**P1 — Establish the limitation (Big Picture):**
- Role: Define the concrete problem: Transformers cannot efficiently process sequences beyond their pre-trained context window.
- Key claim: "Transformer self-attention scales as O(L^2), making arbitrarily long context windows impractical. Segment-level recurrence (Transformer-XL) propagates hidden states but loses information across segments because there is no persistent, content-addressable store."
- Evidence anchor: O(L^2) complexity, fixed pre-training context lengths (e.g., 512 for BERT).
- Transition: "This structural limitation motivates an explicit external memory module."

**P2 — Identify the gap in prior work (Gap):**
- Role: Review existing solutions and their shortcomings.
- Key claim: "Sparse attention methods (Longformer, BigBird, Reformer) reduce computational cost but still operate within a bounded effective window. Segment-based methods (Transformer-XL, Compressive Transformer, ∞-former, Memorizing Transformers) propagate information across segments but still compress or degrade past information."
- Evidence anchor: Cite key papers; note that Compressive Transformer and ∞-former still use compressed representations.
- Transition: "What is missing is a persistent, content-addressable memory where individual items can be retrieved on demand without degradation."

**P3 — Introduce the solution intuition (Solution):**
- Role: Present Memoria at a high level before diving into technical details.
- Key claim: "Memoria addresses this gap by storing past hidden states as individual engrams in a multi-tier store and retrieving them via learned association weights. Inspired by Hebbian plasticity, connection strengths between co-reminded engrams are reinforced, allowing important patterns to persist."
- Evidence anchor: Brief overview of the three tiers and the graph structure.
- Transition: "We now describe the three operational stages of Memoria."

**P4 — Preview contributions (Contribution summary):**
- Role: List 3 concrete, bounded contributions.
- Key claims:
  1. "A three-tier memory architecture with count-based co-occurrence weights that satisfy five of six desiderata for Hebbian plasticity models."
  2. "Integration strategies for both encoder-only (BERT) and decoder-only (GPT) Transformers via cross-attention over retrieved engrams."
  3. "Empirical gains on sorting and WikiText-103, with marginal gains on PG-19 and enwik8, alongside an analysis of the 5x memory overhead."
- Evidence anchor: Reference specific tables.

**P5 — Paper roadmap (optional, concise):**
- Role: Tell the reader what to expect.
- "Section 3 details the Remind-Exploit-Memorize pipeline. Section 4 reports experiments across three tasks. Section 5 concludes with limitations and future work."

### Alternative Storyline (Candidate B — Results-first)

If the authors want to emphasize the surprising sorting result:
- **P1:** Start with the sorting task difficulty as a motivating example (counting frequencies over 32K tokens)
- **P2:** Show that all existing methods fail (39.7% accuracy for ∞-former) → Gap
- **P3:** Propose Memoria as the solution → 63.4% accuracy
- **P4:** Generalize to language modeling and classification
- **P5:** Position within broader related work

### Why Candidate A is recommended

Candidate A follows the standard "Problem → Gap → Solution → Evidence → Summary" arc that aligns with reviewer expectations at ICLR/NeurIPS. It establishes the technical gap early (P1), surveys existing solutions with their limitations (P2), and clearly positions Memoria's novelty. Candidate B is more attention-grabbing but risks under-motivating the general reader who may not care about the synthetic sorting task. Candidate A is safer and more defensible.

## Priority Revision Plan
### P0 — Must-fix before resubmission (publication-critical)

| Priority | Issue | Effort | Impact | Action |
|----------|-------|--------|--------|--------|
| P0.1 | Hebbian overclaim | Low | High | Reword to "Hebbian-inspired"; add qualification paragraph in Section 3; fix cooperativity claims in Appendix A |
| P0.2 | Missing LM variance | Low | High | Run 3 seeds for Table 1/Table 2; add std; explicitly discuss PG-19 and enwik8 ties |
| P0.3 | Formula ambiguities | Low | High | Fix 4 formula issues (notation, w_i computation, Count init, DFS fallback) |
| P0.4 | Conclusion hype | Low | High | Replace conclusion with validated findings + limitations + future work |
| P0.5 | Capacity confound | Medium | High | Add parameter-matched baseline for classification experiments |

### P1 — Should-fix (strongly recommended)

| Priority | Issue | Effort | Impact | Action |
|----------|-------|--------|--------|--------|
| P1.1 | Memory cost analysis | Medium | Medium | Provide GPU memory breakdown; implement and evaluate sparse adjacency |
| P1.2 | Hyperparameter sensitivity | Medium | Medium | Add sensitivity study for α and N_depth on sorting task |
| P1.3 | Simpler memory baseline | Medium | Medium | Add FIFO buffer baseline without Hebbian graph |

### P2 — Nice-to-have (quality improvement)

| Priority | Issue | Effort | Impact | Action |
|----------|-------|--------|--------|--------|
| P2.1 | OOD evaluation | High | Medium | Add domain-shift test (e.g., WikiText-103 → other text domain) |
| P2.2 | Graph diversity analysis | Low | Low | Analyze entropy of DFS-retrieved engrams |
| P2.3 | Memory reset analysis | Low | Low | Study impact of periodic memory reset (500-step interval) |

### Execution Roadmap

```text
ASCII Diagram — Revision Strategy Roadmap

[Current manuscript]
    |
    v
Phase 1 (Week 1): Claim corrections
    ├── Reword Hebbian claims → "Hebbian-inspired"
    ├── Rewrite conclusion (no hype)
    ├── Fix formula ambiguities (4 items)
    ├── Add Count initialization spec
    └── Add DFS sink node fallback
    |
    v
Phase 2 (Week 2): Experimental controls
    ├── Run 3-seed LM experiments + std
    ├── Add significance tests for Table 1
    ├── Add parameter-matched classification baseline
    └── Compute added parameter counts
    |
    v
Phase 3 (Week 3): Depth analysis
    ├── GPU memory breakdown table
    ├── Sparse adjacency implementation + eval
    ├── Hyperparameter sensitivity (α, N_depth)
    └── Simple FIFO baseline
    |
    v
Phase 4 (Before submission): Final polish
    ├── OOD evaluation (if feasible)
    ├── Copy-edit for precise language
    └── Verify all annotations addressed
    |
    v
Expected outcome: Stronger novelty framing, defensible claims, reproducible formulas
```

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Skip Reason (if applicable) |
|------|-----------------|-----------------|-----------------------------|
| 1 (Abstract + Intro P1-P3) | 4 | Covered | — |
| 2 (Intro P4 + Contributions + Related Work) | 3 | Covered | — |
| 3 (Related Work Hebbian + Memory categorization + Method overview) | 2 | Covered | — |
| 4 (Memory Graph + Remind steps 1-3) | 1 | Covered | — |
| 5 (Remind steps 4-7 + Exploit) | 1 | Covered | — |
| 6 (Memorize & Forget) | 1 | Covered | — |
| 7 (Sorting experiment + Memory encoder formula) | 1 | Covered | — |
| 8 (Language modeling results) | 1 | Covered | — |
| 9 (Classification + Conclusion) | 2 | Covered | — |
| 10-13 (References) | 0 | Skipped | Non-substantive (reference list) |
| 14 (Appendix A: Hebbian attributes) | 0 | Skipped | Covered indirectly via Page 3 annotation |
| 15-16 (Appendix B: Training details) | 0 | Skipped | Hyperparameter listing, covered indirectly |
| 17 (Appendix C: Ablation) | 0 | Skipped | Well-written; no major issues |
| 18 (Appendix D: Autocorrelation) | 0 | Skipped | Analysis section, well-presented |
| 19-20 (Appendix E: Algorithm & Complexity) | 0 | Skipped | Algorithm listing, reference only |
| 21 (Appendix E.2: Empirical analysis) | 1 | Covered | — |
| 22-23 (Appendix F: Architecture diagrams) | 0 | Skipped | Figures with captions, self-explanatory |
| 24-25 (Appendix G: Visualization) | 0 | Skipped | Qualitative visualizations, no actionable issues |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1: Sorting | Maintain frequency counts over long sequences (1K-32K tokens) | Synthetic data, 20-number vocab, segment lengths 256/512/1024, vs. Transformer-XL/Compressive/∞-former | Accuracy | Memoria best at 32-segment: 63.4% (1024 seg.) vs. ∞-former 39.7% | C3 (performance) | Synthetic task; real-world relevance limited |
| E2: WikiText-103 LM | Token-level language modeling | GPT-2 arch, 150-token segments, from scratch | PPL | Memoria 23.47 vs. ∞-former 24.69 (~5% relative) | C3 | No variance reported; single seed |
| E3: PG-19 LM | Token-level LM on books | Similar to E2, first 2000 books | PPL | Memoria 29.149 vs. ∞-former 29.154 (tied) | C3 (weak) | No improvement; contradicts claim |
| E4: enwik8 LM | Character-level LM | 512-char segments, 20 epochs | BPC | Memoria 1.16 vs. Compressive 1.16 (tied) | C3 (weak) | No improvement |
| E5: WikiText-103 short seg. (50 tokens) | Long-term dependency via more segments | 50-token segments | PPL | Memoria 30.01 vs. ∞-former 31.79 | C3 | Single seed, no variance |
| E6: Pre-trained GPT-2 finetuning | Applicability to LLMs | WikiText-103, GPT-2 small/large/xl | PPL | Memoria improves all sizes (e.g., GPT-2 20.50→18.99 PPL) | C2 (integration) | Finetuning only; no pre-training |
| E7: Hyperpartisan classification | Long-doc classification | BERT/RoBERTa base, 512-token segments, 20 epochs | F1, Acc | Memoria RoBERTa 96.51% F1 vs. RoBERTa 95.24% | C2, C3 | p=0.045 marginal; no capacity control |
| E8: Ablation (sorting) | Component contribution | Sorting 4K-48K, add WM/STM/LTM incrementally | Accuracy | WM dominant at short, LTM at long sequences | C1 (design) | Only sorting task |
| E9: Autocorrelation (Appendix D) | Retrieval pattern analysis | WikiText-103 | ACF | High short-term autocorrelation, decaying LTM ACF | C1 (analysis) | Descriptive, not predictive |
| E10: Complexity analysis (Appendix E) | Theoretical cost | Big-O analysis | Time/Space | Remind: O(N_rem_stm × N_ltm × N_depth) | C1 | Empirical validation needed |

### Research-Theme Gap Diagnosis

1. **New Knowledge (Knowledge gap):** The paper's primary claim — that a count-based Hebbian-inspired memory module improves long-range dependency — is partially supported by the sorting and WikiText-103 results. However, the limited gains on PG-19 and enwik8 suggest the claim is task-dependent, which is not adequately discussed.

2. **Reproducibility/Reusability (Method gap):** The modular Python package design is commendable, but the formula ambiguities (4 identified issues) and missing Count initialization reduce reproducibility.

3. **Impact on Practice/Understanding (Value gap):** The 5x GPU memory overhead is a significant barrier to practical adoption. Without a clear path to reducing this cost (e.g., sparse adjacency), the method's practical value is limited. The paper does not provide actionable guidelines for practitioners (e.g., how to choose α, N_depth, STM capacity).

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Before resubmission)
├── Exp-P0.1: 3-seed LM variance (E2-E5)
│   Target: C3 — demonstrate statistical reliability
│   Cost: ~3 GPU-days
│   Success: std < 1.0 PPL for WikiText-103
│
├── Exp-P0.2: Parameter-matched classification baseline (E7)
│   Target: C2 — control for capacity confound
│   Design: RoBERTa + extra FFN layers matching Memoria params
│   Cost: ~1 GPU-day
│   Success: Memoria still outperforms matched-baseline
│
└── Exp-P0.3: Sparse adjacency implementation
    Target: C1 — address main practical limitation
    Design: Replace dense adjacency matrix with top-k per node
    Cost: ~2 GPU-days
    Success: Memory < 20GB with < 1% accuracy drop

P1 (Strongly recommended)
├── Exp-P1.1: Hyperparameter sensitivity (α, N_depth)
│   Target: C1 — guide practitioner configuration
│   Design: Grid search over α∈{4,8,16}, N_depth∈{5,10,20} on sorting
│   Cost: ~1 GPU-day
│
├── Exp-P1.2: FIFO buffer baseline
│   Target: C3 — isolate Hebbian mechanism value
│   Design: Replace graph with simple FIFO + cross-attention
│   Cost: ~1 GPU-day
│
└── Exp-P1.3: OOD evaluation
    Target: C3 — test generalization beyond IID
    Design: Train on WikiText-103, evaluate on PG-19 without finetuning
    Cost: ~0.5 GPU-day

P2 (Improvement)
├── Exp-P2.1: Memory graph sparsity analysis
│   Target: C1 — understand graph structure
│   Design: Report degree distribution, connectivity patterns
│
└── Exp-P2.2: Lifespan distribution analysis
    Target: C1 — understand forgetting dynamics
    Design: Histogram of engram lifespans over training
```

### Experiment Details for Top-3 Proposed Experiments

**Exp-P0.1: Multi-seed Language Modeling**
- Target Claim: C3 (performance)
- Hypothesis: Memoria's gains on WikiText-103 are statistically significant at p < 0.05
- Minimal Design: Run WikiText-103, PG-19, and enwik8 experiments with 3 random seeds each. Report mean ± std perplexity. Compute one-tailed paired t-test against the strongest baseline for each dataset.
- Controls: Same seed sequence for all models; identical hyperparameters
- Metrics: Perplexity (mean ± std), p-value of paired t-test
- Success Criterion: std < 1.0 PPL; consistent directional improvement across seeds for WikiText-103
- Estimated Cost: ~3 GPU-days on A100
- Expected Paper-Quality Gain: High — addresses the most critical missing evidence

**Exp-P0.2: Capacity-Controlled Classification Baseline**
- Target Claim: C2 (integration effectiveness)
- Hypothesis: Memoria's gains are not solely due to added parameters
- Minimal Design: Count Memoria's added parameters (memory encoder Q, Wk, Wv, cross-attention, FFN). Add equivalent parameters to RoBERTa as additional FFN layers after layer 9 (where Memoria inserts cross-attention). Train on Hyperpartisan with same hyperparameters.
- Controls: Same training budget, same learning rate schedule
- Metrics: F1, Accuracy
- Success Criterion: Memoria RoBERTa still outperforms capacity-matched RoBERTa
- Estimated Cost: ~1 GPU-day
- Expected Paper-Quality Gain: High — removes a major reviewer objection

**Exp-P0.3: Sparse Adjacency Matrix**
- Target Claim: C1 (architecture practicality)
- Hypothesis: Top-k adjacency (k=100) preserves retrieval quality while reducing memory by ~100x
- Minimal Design: Replace dense N_ltm × N_ltm adjacency with per-node top-k list. Compare GPU memory, training time, and task accuracy on sorting (32K).
- Controls: Same hyperparameters as dense version
- Metrics: GPU memory (GB), accuracy
- Success Criterion: Memory < 20GB with accuracy drop < 1 percentage point
- Estimated Cost: ~2 GPU-days
- Expected Paper-Quality Gain: Medium — demonstrates deployment feasibility

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 5.5 / 10

**Evidence-grounded rationale (research value + novelty prioritized):**

- **Research Value:** Moderate. The sorting benchmark provides compelling evidence for Memoria's effectiveness (63.4% vs. 39.7%), and the ablation study cleanly separates WM/STM/LTM contributions. However, the real-world language modeling gains are mixed — substantial on WikiText-103 but marginal or absent on PG-19 and enwik8. The 5x GPU memory overhead limits practical applicability. The combination of cognitive inspiration with a count-based graph mechanism is interesting but the biological claims are overreaching.

- **Novelty:** *Deferred — manually verify.* The idea of using a three-tier Hebbian-inspired memory for Transformers is conceptually novel to this reviewer's knowledge, but external literature verification is unavailable in this run (Retrieval-Disabled Mode). The specific count-based update rule with conditional probability interpretation appears to be a new formalization, but similar ideas exist in Hopfield networks, associative memory models, and k-NN memory approaches (Memorizing Transformers). Score accounts for this uncertainty with a conservative default.

- **Validity/Soundness:** Moderate weaknesses. The major issues are (1) overclaimed Hebbian biological plausibility, (2) missing variance in key LM experiments, (3) capacity confound in classification, and (4) formula ambiguities affecting reproducibility. None of these are fatal, but they collectively reduce confidence in the results.

- **Reproducibility:** Moderate. The method is described in reasonable algorithmic detail, but the formula-level ambiguities (4 identified issues) and unspecified Count initialization create barriers to exact reproduction. The code availability statement is positive.

**Score breakdown:**
| Dimension | Score (0-10) | Weight |
|-----------|-------------|--------|
| Research Value / Significance | 5.5 | 35% |
| Novelty (with deferred verification) | 5.0 | 30% |
| Validity / Soundness | 5.0 | 20% |
| Reproducibility / Clarity | 6.0 | 15% |
| **Weighted Total** | **5.5** | **100%** |

### Post-Revision Target: [6.5, 7.5] / 10

If all P0 issues are fully addressed:
- Hebbian claims qualified (removes reviewer skepticism)
- LM variance reported with significance tests (restores credibility)
- Formula ambiguities fixed (enables reproduction)
- Conclusion rewritten (aligns claims with evidence)
- Capacity-controlled classification baseline added (addresses confound)

...the paper could reach a score of **6.5-7.5** (accept-range for ICLR/NeurIPS). The upper bound (7.5) requires addressing P1 items (sensitivity analysis, memory cost optimization). The lower bound (6.5) is achievable with P0 items alone.