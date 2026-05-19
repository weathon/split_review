## Summary
This paper presents **Tree-of-Table**, a prompting framework for enhancing LLM reasoning over large-scale relational tables. The method consists of three stages: (1) **Table Condensation** — schema-linking-based merging of relevant columns from multi-table databases into a single reduced sub-table; (2) **Table-Tree Construction** — breadth-first decomposition of the question into a hierarchical tree of reasoning sub-goals, with leaf nodes sampling executable operations (sum, filter, group-by, etc.) from a predefined pool; and (3) **Table-Tree Execution** — depth-first traversal of the tree, processing subtrees independently and combining intermediate results.

The method is evaluated on four datasets (WikiTQ, TabFact, FeTaQA, BIRD) using three LLM backbones (GPT-3.5, PaLM 2, LLaMA 2). Results show consistent improvements over the strongest baseline Chain-of-Table, with larger gains on the large-scale BIRD dataset. Ablation studies examine robustness to table size, hyperparameter sensitivity (MAXDepth, MAXDegree), encoding format, and error propagation.

**Key Strengths:** The tree-structured decomposition is a principled departure from linear chain methods; the Table Condensation step explicitly addresses multi-table foreign-key scenarios that prior work largely ignores; experimental coverage across multiple LLMs provides robustness evidence.

**Key Weaknesses:** Reproducibility gaps in schema-linking and execution details; efficiency claims rely on sample count while per-sample cost is higher; novelty positioning against Chain-of-Table is overstated in scope; formulation equations do not capture multi-table complexity; state-of-the-art and generalization claims exceed evidence boundaries.

## Strengths
**1. Principled tree-structured decomposition for table reasoning.**  
The core idea of replacing linear reasoning chains (Chain-of-Table) with a hierarchical tree structure is well-motivated. By limiting each node's context to its parent chain, the method avoids the growing-history problem that linear methods face with multi-branch queries. This architectural difference is clearly explained in Section 3.6 and Figure 1, making the contribution easy to understand.

**2. Explicit handling of multi-table foreign-key scenarios.**  
The Table Condensation step (Section 3.3.1) directly addresses a realistic and underexplored challenge: large-scale table understanding often involves multiple tables connected by foreign keys. The paper provides concrete statistics from the BIRD dataset (over 90% of questions involve at least two tables) to justify this component. This distinguishes Tree-of-Table from Chain-of-Table, which assumes a single input table.

**3. Multi-backbone evaluation across four datasets.**  
The paper evaluates on three LLMs (GPT-3.5, PaLM 2, LLaMA 2) and four datasets spanning different task formats (denotation accuracy, free-form QA, text-to-SQL). The consistent improvements across all backbones (Table 1, Table 2) suggest the method's benefits are not tied to a specific model architecture. The BIRD results (15.70 BLEU vs. Chain-of-Table's 12.12) are particularly noteworthy.

**4. Informative ablation studies.**  
The ablation on table size generalization (Figure 4a) shows that Tree-of-Table degrades more gracefully than baselines as table size increases. The hyperparameter sensitivity analysis (Appendix Tables 8-9) and error propagation study (Table 10) provide useful practical guidance for deployment. The case studies (Table 11) give concrete insight into when the method succeeds or fails.

**5. Efficiency analysis with multiple perspectives.**  
While the efficiency claim has caveats (see Weaknesses), the paper provides two complementary efficiency measures: number of generated samples (Table 5) and time cost (Table 6). This multi-metric approach is more informative than a single metric.

## Weaknesses
**W1. Reproducibility gaps in critical method components (High Severity).**  
Several algorithmic steps are described too abstractly for independent reproduction. Schema-linking (Section 3.3.1) is central to the pipeline but lacks prompt design, candidate selection criteria, rejection handling, and fallback strategy when condensation fails. The Table-Tree Execution (Section 3.5) states "LLMs can implicitly generate tables and save intermediary results" without specifying representation format, subtree merging logic, or shared-result handling. These omissions reduce the paper's value as a reproducible contribution.

**W2. Overclaimed novelty positioning (Medium-High Severity).**  
The introduction characterizes Chain-of-Table as "limited to understanding smaller tables" (Page 2), but Tree-of-Table outperforms it on small datasets too (WikiTQ: +1.17, TabFact: +1.72). The actual advantage appears to be structural (tree vs. chain), not size-dependent. This mischaracterization weakens the paper's own narrative coherence. Additionally, the method heavily borrows from Chain-of-Table's operation pool (Section 3.4.2: "based it on (Wang et al., 2024)") and Tree-of-Thought (Yao et al., 2023a), yet the novelty claim is framed as a new paradigm rather than an incremental structural improvement.

**W3. Efficiency claim conflates sample count with total cost (Medium Severity).**  
The paper prominently claims efficiency based on "number of generated samples" (Table 5). However, Appendix Table 6 shows Tree-of-Table has *higher* per-sample latency (7.8s vs. 5.7s for Chain-of-Table). If Tree-of-Table uses fewer samples but each sample costs more (because each node carries multi-level parent context), the total compute may be comparable or higher. The paper does not provide total token consumption or end-to-end wall-clock time for full dataset evaluation.

**W4. State-of-the-art and generalization claims exceed evidence (Medium Severity).**  
The abstract and conclusion claim "state-of-the-art performance" and "remarkable generalization capabilities." The SOTA claim is only valid within the family of prompting-based table reasoning methods — not against all table understanding approaches. The generalization evidence is limited to table size variation on two datasets, not distribution shift or unseen schema types. Appendix Table 7 compares against Text-to-SQL methods under potentially different accuracy metrics, which could mislead readers about cross-paradigm superiority.

**W5. Formulation does not capture the multi-table problem (Low-Medium Severity).**  
Equations (1)-(2) define S = f(Q, ⟨H,D⟩|θ), which represents a single table. The paper's core contribution addresses multi-table foreign-key scenarios, but this complexity is not reflected in the problem formulation. This disconnect between formalism and method undermines the theoretical framing.

**W6. No variance or significance testing (Low-Medium Severity).**  
No confidence intervals, standard deviations, or significance tests are reported for any metric. While the BIRD BLEU gap (+3.58) is large enough to be likely significant, the smaller WikiTQ gains (+1.17 accuracy) could fall within normal LLM output variance. Without multi-seed reporting, the statistical reliability of claims is uncertain.

**W7. Missing ablation on the tree structure itself (Low Severity).**  
The paper does not include an ablation that replaces the tree with a linear chain (using the same condensation and operation pool) to isolate the benefit of tree-structured reasoning. The current comparison is against Chain-of-Table, which uses a different operation pool and no condensation — conflating multiple factors.

## Key Issues
### Issue 1: Schema-linking and Table Condensation are not reproducible (W1, Must-fix)
- **Location:** Page 5 — Section 3.3.1
- **Risk:** The method's first stage is described at the level of "employs LLMs to identify one sub-table relevant to Q through schema-linking." No prompt template, example inputs/outputs, or success rate is provided. The only detail is a reference to (Lei et al., 2020).
- **Impact:** A practitioner cannot implement or validate the condensation step. Since condensation affects all downstream reasoning, the entire pipeline is unverifiable.
- **Fix:** Provide the schema-linking prompt (full or abbreviated) in the appendix, report schema-linking success rate on BIRD, and describe the fallback when condensation fails to reduce table size below the LLM context limit.

### Issue 2: Efficiency claim is internally inconsistent (W3, Must-fix)
- **Location:** Page 9-10 — Section 4.3 and Appendix A.1.1 (Tables 5, 6)
- **Risk:** The main text (Table 5) uses "Generate Samples" as the efficiency metric, claiming Tree-of-Table is more efficient (90 vs. 120 vs. 300). Appendix Table 6 shows Tree-of-Table has 37% higher per-sample latency (7.8s vs. 5.7s). The paper does not reconcile these two metrics.
- **Impact:** A reader or reviewer may conclude the efficiency claim is selectively reported. The total cost (samples × per-sample cost) could favor Tree-of-Table, be comparable, or even be worse — we cannot tell.
- **Fix:** Report total end-to-end compute (total tokens consumed or total wall-clock time for full evaluation), and add a sentence explaining the trade-off: "Tree-of-Table uses fewer samples but each sample is more expensive due to multi-level parent context."

### Issue 3: SOTA and generalization claims overreach evidence (W4, Must-fix)
- **Location:** Page 1 Abstract, Page 10 Conclusion
- **Risk:** The paper claims "sets a new benchmark with superior performance" and "remarkable improvements in efficiency and generalizability." The generalization evidence is limited to table size variation (Figure 4a). The SOTA claim is only valid within prompting-based table methods.
- **Impact:** Overclaimed conclusions reduce scientific credibility and invite rejection.
- **Fix:** Replace with bounded claims: "competitive with prior prompting-based methods," "gains are largest on the large-scale BIRD dataset," and "robustness to table size variation within evaluated datasets."

### Issue 4: Backtracking and failure recovery are unspecified (W2/W7, Should-fix)
- **Location:** Page 6 — Section 3.4.1 (Eq. 5)
- **Risk:** The breadth-first decomposition is strictly forward, with no backtracking mechanism when a sub-problem cannot be resolved or a leaf operation fails. Real table reasoning often requires re-planning.
- **Impact:** The method may fail silently on complex questions that require adaptive reasoning. The error propagation study (Table 10) tests information removal but not decomposition failures.
- **Fix:** Add a one-paragraph discussion of backtracking or re-planning strategy, or explicitly state that the method uses single-pass decomposition without backtracking as a design choice (with empirical justification).

### Issue 5: No statistical significance or variance reporting (W6, Should-fix)
- **Location:** Page 8 — Section 4.2 (Tables 1, 2)
- **Risk:** No confidence intervals, standard deviations, or significance tests are reported for any metric. On small-gap comparisons (e.g., WikiTQ GPT-3.5: 61.11 vs. 59.94), the gain could be within LLM output variance.
- **Impact:** Readers cannot assess whether improvements are statistically reliable.
- **Fix:** Report at least 3 runs with mean and standard deviation for main results, or provide a paired bootstrap confidence interval for the primary comparison (Tree-of-Table vs. Chain-of-Table).

### Issue 6: Missing controlled ablation isolating tree structure benefit (W7, Nice-to-have)
- **Location:** Page 9 — Section 4.3
- **Risk:** The paper compares Tree-of-Table against Chain-of-Table, but these differ in multiple dimensions: (a) tree vs. chain structure, (b) Table Condensation, (c) operation pool selection. Without a controlled ablation (Tree-of-Table without condensation, or Chain-of-Table with condensation), the contribution of each component is unclear.
- **Fix:** Add one ablation: "Tree-of-Table (chain-structured)" — replace tree with a linear chain while keeping condensation and operation pool identical.

## Actionable Suggestions
### S1 — Add schema-linking prompt and success rate (P0 Must)
**Target:** Page 5 — Section 3.3.1  
**Action:** Include the full schema-linking prompt in Appendix A.2 (extending the existing prompt template). Report the percentage of BIRD questions where schema-linking correctly identified the relevant columns (e.g., by comparing against gold SQL schema). Specify fallback: what happens when condensation output still exceeds the LLM context limit.  
**Expected benefit:** Reproducibility — the first pipeline stage becomes verifiable.

### S2 — Reconcile efficiency metrics (P0 Must)
**Target:** Page 10 — Section 4.3 (Efficiency Analysis)  
**Action:** Add one sentence acknowledging the per-sample time trade-off identified in Appendix Table 6: "Tree-of-Table uses fewer generation samples than Chain-of-Table, but each sample incurs higher per-step cost due to multi-level parent context. Total wall-clock time per query is 7.8s vs. 5.7s; the net efficiency benefit depends on whether sample count or latency is the binding constraint."  
**Expected benefit:** Resolves internal inconsistency and improves reviewer trust.

### S3 — Bound SOTA claims (P0 Must)
**Target:** Abstract + Conclusion  
**Action:** Replace "sets a new benchmark with superior performance" with "outperforms prior prompting-based table reasoning methods on the evaluated benchmarks." Replace "remarkable generalization capabilities" with "shows robustness to table size variation within WikiTQ and BIRD."  
**Expected benefit:** Aligns claims with evidence, removing a likely rejection risk.

### S4 — Add variance reporting to main results (P1 Should)
**Target:** Tables 1 and 2  
**Action:** For the primary LLM (GPT-3.5), run Tree-of-Table 3 times with different few-shot example sets and report mean ± std. For the BIRD BLEU comparison, also provide a bootstrapped 95% confidence interval.  
**Expected benefit:** Statistical grounding for performance claims.

### S5 — Add controlled tree-vs-chain ablation (P1 Should)
**Target:** Page 9 — Section 4.3  
**Action:** Add one ablation row: "Tree-of-Table (linear chain)" — same condensation and operation pool but arranged as a sequential chain rather than a tree. Report on BIRD (BLEU) and WikiTQ (accuracy). If the tree structure provides a clear benefit, this strengthens the core contribution. If not, the advantage may come from condensation alone.  
**Expected benefit:** Isolates the value of tree-structured reasoning from condensation benefits.

### S6 — Describe backtracking / failure handling (P2 Nice-to-have)
**Target:** Page 6 — Section 3.4.1  
**Action:** Add 2-3 sentences explaining what happens when a leaf operation fails (e.g., SQL syntax error, missing column). If no backtracking is implemented, state this explicitly as a design choice and discuss limitations.  
**Expected benefit:** Completeness — reviewers won't need to guess how error handling works.

### S7 — Revise Introduction paragraph 2 to mention foreign-key challenge (P2 Nice-to-have)
**Target:** Page 1 — Introduction, paragraph 2  
**Action:** Add one sentence: "Three challenges arise: (1) table size exceeds context limits, (2) multiple tables connected by foreign keys require schema-level understanding, and (3) complex questions need multi-step reasoning over disparate sub-tables."  
**Expected benefit:** Aligns problem statement with the three-component solution.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows: **Big Picture (P1) -> Challenge (P2) -> Existing Approaches (P3) -> Our Method (P4)**.

**Strengths:** Logical progression, covers necessary background.

**Weaknesses:** (a) The Big Picture paragraph (P1) is too generic and does not clearly state the specific technical gap. (b) P2 identifies context limits but omits the foreign-key challenge that the method later addresses. (c) P3 mischaracterizes Chain-of-Table as "limited to smaller tables" while the paper's own results show gains on small tables too. (d) P4 uses metaphorical language ("tree acts as a roadmap") without technical specificity.

### Recommended Storyline: "Problem-Motivation-Solution-Evidence" (Candidate A — Best)

**Abstract Outline (5 sentences):**

- **S1 (Problem):** "Tables are a ubiquitous semi-structured data format, but existing LLM-based methods for table understanding degrade sharply when tables exceed context limits or involve multiple tables connected by foreign keys."
- **S2 (Gap):** "Linear chain reasoning methods accumulate context across all steps, becoming inefficient for multi-branch questions; prior work also lacks explicit handling of multi-table schema linking."
- **S3 (Solution):** "We propose Tree-of-Table, which condenses multi-table databases into a relevant sub-table via schema linking, then builds a hierarchical Table-Tree by recursively decomposing the question — each node limited to its parent-chain context."
- **S4 (Execution):** "A depth-first traversal executes the tree subtree by subtree, producing answer through stepwise combination of intermediate results."
- **S5 (Result + Scope):** "Experiments on WikiTQ, TabFact, FeTaQA, and BIRD show consistent improvements over prior prompting-based methods, with the largest gains on the large-scale BIRD dataset (+3.58 BLEU). The method uses fewer generation samples while maintaining competitive per-query latency."

**Introduction Outline (4 paragraphs):**

- **P1 (Motivation):** "Tables are essential across domains, but large-scale table reasoning remains unsolved." State the three-part challenge: context limits, foreign-key complexity, and multi-step reasoning. Cite BIRD as the benchmark that exposes these challenges.
  - *Transition:* "These challenges stem from a common root: existing reasoning paradigms cannot efficiently handle structured multi-table queries."
  
- **P2 (Existing work and its limits):** "Current methods fall into two paradigms: program-aided (SQL/Python) and prompting-based (chain-of-thought). SQL methods are brittle for long-form code; prompting methods use linear chains that accumulate history across all steps. Chain-of-Table is the strongest linear-chain method, but its per-step context grows with chain length." This paragraph should explicitly define the *linear-context-accumulation* problem.
  - *Transition:* "We hypothesize that a tree-structured approach, where each node's context is bounded by its parent path, can overcome this limitation."
  
- **P3 (Proposed method — intuitive):** "Tree-of-Table replaces the linear chain with a hierarchical tree. First, Table Condensation uses LLMs for schema linking to merge relevant columns across tables into a single sub-table. Second, the question is recursively decomposed breadth-first into sub-goals, forming a tree. Third, a depth-first traversal executes the tree, processing subtrees independently."
  - *Transition:* "We evaluate this design against prior methods on four benchmarks."
  
- **P4 (Results preview):** "Tree-of-Table outperforms Chain-of-Table and earlier methods on all four datasets and three LLM backbones. The gains are most pronounced on BIRD (+3.58 BLEU, +0.04 ROUGE-L). The tree structure reduces generated samples by 25% vs. Chain-of-Table, while maintaining acceptable per-query latency (7.8s)."

### Alternative Storyline B: "Capability-Driven" (for a more applied audience)

**Abstract:** Start with the BIRD benchmark's difficulty (current LLMs achieve low accuracy), then introduce Tree-of-Table as the method that bridges this gap, then summarize results.

**Introduction:** Lead with a concrete example (the fuel consumption question from Figure 1) showing how the same question gets different answers under different methods. Use this example as a narrative hook before zooming out to the general problem.

*Advantage:* More engaging for practitioners.  
*Disadvantage:* Less aligned with the paper's current academic framing.

### Recommended Choice: Candidate A

Candidate A provides the clearest alignment between the stated problem (context limits + foreign-key complexity + multi-step reasoning) and the three method components (condensation + tree construction + DFS execution). It also avoids the current mischaracterization of Chain-of-Table as purely small-table-limited.

## Priority Revision Plan
### P0 — Must-fix before resubmission (critical for validity and acceptance)

| # | Task | Location | Effort | Impact | Key Issue |
|---|------|----------|--------|--------|-----------|
| 1 | Provide schema-linking prompt + success rate + fallback | Sec 3.3.1, Appendix | Low (add text + prompt) | High (reproducibility) | Issue 1 |
| 2 | Reconcile efficiency metrics: add total-cost reporting | Sec 4.3, Tables 5-6 | Low (add 2 sentences) | High (internal consistency) | Issue 2 |
| 3 | Bound SOTA and generalization claims | Abstract, Conclusion | Low (rewrite ~3 sentences) | High (credibility) | Issue 3 |
| 4 | Add variance reporting to main results | Tables 1, 2 | Medium (3 runs) | Medium (statistical grounding) | Issue 5 |

### P1 — Should-fix before resubmission (strengthens contribution)

| # | Task | Location | Effort | Impact | Key Issue |
|---|------|----------|--------|--------|-----------|
| 5 | Add controlled tree-vs-chain ablation | Sec 4.3 | Medium (new experiment row) | High (isolates contribution) | Issue 6 |
| 6 | Clarify metric definition for Table 7 comparison | Appendix A.1.2 | Low (footnote) | Medium (avoids misleading comparison) | — |
| 7 | Add backtracking / re-planning discussion | Sec 3.4.1 | Low (2-3 sentences) | Medium (completeness) | Issue 4 |

### P2 — Nice-to-have (improves clarity and polish)

| # | Task | Location | Effort | Impact |
|---|------|----------|--------|--------|
| 8 | Revise Intro P1 to state the three-part challenge explicitly | P1 Introduction | Low (2 sentences) | Medium (alignment) |
| 9 | Add intermediate result representation details | Sec 3.5 | Low (3-4 sentences) | Medium (reproducibility) |
| 10 | Add limitation on tree height vs. total operations | Sec 4.3 (Table 3 discussion) | Low (2 sentences) | Low (clarification) |

### Revision Order Recommendation

**Phase 1 (2-3 days):** Tasks 1, 2, 3, 8 — textual revisions only, high impact per unit effort.

**Phase 2 (1 week):** Tasks 4, 5 — experimental additions. Task 5 (controlled ablation) is the single most informative experiment to strengthen the core contribution.

**Phase 3 (polish):** Tasks 6, 7, 9, 10 — text improvements and minor clarifications.

### Expected Outcome After P0 Fixes

The paper would have: (a) a reproducible pipeline with documented schema linking, (b) internally consistent efficiency claims, (c) appropriately bounded contribution statements, and (d) variance-anchored results. These changes would address the most common reviewer concerns (reproducibility, overclaiming, statistical rigor) without requiring new dataset collection or model development.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Main comparison on small benchmarks | WikiTQ, TabFact; GPT-3.5/PaLM2/LLaMA2 | Denotation accuracy | Tree-of-Table > all baselines (WikiTQ: 61.11, TabFact: 81.92 with GPT-3.5) | Method outperforms prior prompting methods | No variance reported; small gains on WikiTQ (+1.17) may be within noise |
| E2 | Main comparison on free-form QA + large-scale | FeTaQA, BIRD; GPT-3.5 | BLEU, ROUGE-1/2/L | Tree-of-Table > Chain-of-Table (BIRD BLEU: 15.70 vs. 12.12) | Method effective on large-scale tables | Metric definition mismatch vs. Text-to-SQL methods not clarified |
| E3 | Generalization across table sizes | WikiTQ (small/medium/large), BIRD (small/medium/large) | Accuracy (WikiTQ), BLEU (BIRD) | Tree-of-Table degrades more gracefully than baselines | Robustness to table size variation | Only 2 datasets; size bins not precisely defined |
| E4 | Table Condensation effectiveness | All 4 datasets | Table cell count before/after | >60% of long questions reduced below LLM limit | Condensation reduces table size | ~40% still above limit; no fallback analysis |
| E5 | Efficiency (sample count) | BIRD | Number of generated samples | Tree-of-Table: 90, Chain-of-Table: 120, Dater: 300 | Fewer samples needed | Per-sample cost is higher (7.8s vs. 5.7s) |
| E6 | Hyperparameter sensitivity | WikiTQ | Accuracy at MAXDepth={6,8,10}, MAXDegree={3,4,5} | Max at 8/4; relatively stable (±1.1) | Robust to hyperparameter choice | Tested on WikiTQ only; BIRD sensitivity unknown |
| E7 | Error propagation | WikiTQ | Accuracy at removal rates 5-15% | Accuracy drops from 61.09 to 59.45 (1.64 drop at 15%) | Some robustness to information loss | Manual removal may not reflect real schema-linking errors |
| E8 | Time cost comparison | BIRD | Wall-clock time per query | Tree-of-Table: 7.8s, Chain-of-Table: 5.7s | Baseline for latency comparison | Only one setting tested; no breakdown by tree depth |
| E9 | Table format encoding | WikiTQ | Accuracy for HTML/TSV/PIPE/Markdown | Markdown best (69.77) | Encoding format affects performance | Tested on WikiTQ only |
| E10 | Accuracy vs. Text-to-SQL methods | BIRD | Accuracy % | Tree-of-Table: 65.07%, MCS-SQL: 63.36% | Competitive with SQL-specialized methods | Metric alignment unclear (execution accuracy vs. denotation accuracy) |

### Research-Theme Gap Diagnosis

1. **New Knowledge (Medium gap):** The paper introduces tree-structured decomposition for table reasoning, which is a structural contribution. However, the core ideas (schema linking, operation pool, tree-of-thought) are adapted from prior work. The *specific novelty* — that tree-structured context limiting improves efficiency over linear chains — is not isolated in ablation (see E3 limitation).

2. **Reproducibility (Large gap):** Schema-linking, intermediate result handling, and error recovery are underspecified. A practitioner cannot reproduce the pipeline from the current manuscript.

3. **Impact on Practice/Understanding (Medium gap):** The method clearly improves BIRD BLEU by +3.58, which is practically meaningful. However, the lack of compute cost transparency and the overclaimed generalization limit the paper's impact on practice.

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Gain |
|--------|-------------|-----------|---------------|-------------------|---------|------------------|---------------|--------------|
| P0-E1 | Tree structure is crucial for gains | If tree is replaced by a linear chain with same condensation, performance drops | Tree-of-Table with chain-structured decomposition (no tree) on BIRD + WikiTQ | Chain-of-Table; standard Tree-of-Table | BLEU (BIRD), Accuracy (WikiTQ) | Chain-structured variant underperforms tree by >1.5 BLEU | 1-2 days | Isolates core contribution; may reveal true source of gains |
| P0-E2 | Gains are statistically significant | 3-run variance is small relative to delta | 3 runs of Tree-of-Table + Chain-of-Table on WikiTQ/BIRD with GPT-3.5 | Same baselines, 3 seeds | Mean ± std BLEU/Accuracy | Std < 0.5 × delta for primary comparisons | 2-3 days | Statistical grounding for all performance claims |
| P1-E3 | Condensation helps independently | Schema-linking alone accounts for part of gains | Tree-of-Table without condensation (chain-only) vs. with condensation | Standard Tree-of-Table | BLEU (BIRD) | Condensation adds >1.0 BLEU | 1 day | Disentangles condensation benefit from tree benefit |
| P1-E4 | Efficiency holds under total-cost metric | Total tokens consumed is lower for Tree-of-Table | Log total input+output tokens per query for both methods | Chain-of-Table | Total tokens per query | Tree-of-Table total tokens ≤ Chain-of-Table | 0.5 day (logging only) | Reconciles sample-count vs. latency metrics |
| P2-E5 | Robustness to schema linking errors | Schema-linking accuracy affects overall accuracy | Introduce synthetic schema-linking errors at varying rates and measure accuracy drop | Clean schema-linking | Accuracy degradation curve | Graceful degradation (≤5% drop at 10% error rate) | 1-2 days | Quantifies condensation robustness |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Scoring Rationale

The paper presents a well-motivated and structurally sound method (Tree-of-Table) for an important problem (large-scale table understanding). The experimental evaluation is broad, covering four datasets and three LLM backbones, with consistent improvements over strong baselines. However, several issues prevent a higher score:

1. **Reproducibility gaps** (schema-linking, intermediate results, error handling) reduce the paper's value as a scientific contribution.
2. **Overclaimed novelty positioning** (mischaracterization of Chain-of-Table; SOTA/generalization claims exceeding evidence).
3. **Inconsistent efficiency narrative** (sample count vs. per-sample latency trade-off unaddressed).
4. **Missing statistical rigor** (no variance or significance testing).
5. **Novelty verification is deferred** due to retrieval-disabled mode in this run — external literature comparison was not performed.

The paper's core idea (tree-structured decomposition for table reasoning) is sound and the empirical results on BIRD are practically meaningful. With the P0/P1 revisions outlined in the Priority Revision Plan, the paper could become a solid contribution to the prompting-based table understanding literature.

### Final Score and Post-Revision Target

**Final Score: 6.5 / 10**

*(Score emphasizes research value + novelty as primary dimensions. The method's empirical contribution is meaningful, but reproducibility gaps and overclaims reduce confidence.)*

- Research Value: 7/10 — addresses an important problem with a well-reasoned approach; strong BIRD results.
- Novelty: 6/10 — incremental but principled improvement over Chain-of-Table; borrows from Tree-of-Thought and Chain-of-Table's operation pool.
- Soundness: 6/10 — method is logically sound but underspecified in critical components; efficiency narrative is inconsistent.
- Reproducibility: 5/10 — schema-linking prompt, intermediate representation, and error handling are not specified.
- Presentation: 7/10 — generally well-written but introduction could be sharper; overclaiming reduces credibility.

**Post-Revision Target: [7.5, 8.0] / 10**

*(Achievable if P0 fixes are completed: schema-linking details added, efficiency metrics reconciled, claims bounded, variance reported, and controlled ablation added.)*