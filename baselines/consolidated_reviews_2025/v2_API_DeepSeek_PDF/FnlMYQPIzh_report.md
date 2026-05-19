## Summary
# Final Review Report

## Summary

This paper presents ConvINT (Conversational INTention), a semi-structured intention framework for conversational understanding that decomposes user intentions into four aspects: situation, emotion, action, and knowledge. The framework draws inspiration from psychological theories of semantic pointers. To scale annotation of this framework, the authors propose Weakly-supervised Reinforced Generation (WeRG), which combines coarse-level labels (mapped from existing structured intents), mid-level labels (GPT-3.5-turbo annotations), and fine-level labels (human annotations) as weak supervision signals with tiered quadruple rewards. A Llama-2-7B model is fine-tuned with KL-regularized reinforcement learning to generate ConvINT annotations. Experiments on DuRecDial (recommendation dialogues) and ESConv (emotional support dialogues) show that ConvINT+WeRG outperforms direct/CoT prompting baselines on both automatic metrics (F1, BLEU, BERTScore) and human evaluations. Downstream response generation experiments using ChatGPT show improved Success Rate and reduced conversation turns when ConvINT annotations are integrated as additional context.

The paper addresses a meaningful problem — bridging rigid structured ontologies and unstructured free-text for conversational understanding — and the proposed framework has clear practical potential. However, several methodological and evidential weaknesses limit the current contribution. The main concerns are: (1) statistical reliability is unclear due to missing variance reporting; (2) the downstream evaluation confounds ConvINT content with prompt length; (3) ablation analysis reveals heavy dependence on LLM annotations, raising robustness questions; (4) novelty claims cannot be fully assessed without external literature verification; and (5) several writing/scientific presentation issues reduce clarity.

## Strengths
**S1 — Well-motivated problem framing.** The paper convincingly identifies a genuine tension in conversational understanding: rigid slot-value ontologies are too inflexible for nuanced real-world dialogues, while completely unstructured free-text summaries are hard to evaluate and prone to drift. The proposed semi-structured approach (fixed intention aspects expressed in free-form language) is a reasonable and interesting middle ground.

**S2 — Interdisciplinary grounding.** Drawing on psychological and cognitive intention theories (semantic pointers) to motivate the four-aspect framework is a distinguishing feature. This provides a principled basis for aspect selection rather than relying on purely empirical design.

**S3 — Practical annotation pipeline.** The WeRG mechanism addresses a real scalability problem: human annotation of four-aspect intentions is expensive. The tiered reward approach that combines coarse (existing intents), mid (LLM-annotated), and fine (human) supervision signals is a clever engineering contribution with practical value for dataset construction.

**S4 — Comprehensive evaluation scope.** The paper includes both automatic metrics (F1, BLEU, BERTScore, BARTScore) and human evaluation, and validates ConvINT in downstream response generation. The aspect removal analysis (Table 5) provides useful insight into the relative contribution of each aspect.

**S5 — Reproducibility effort.** The appendix provides prompts, implementation details (LoRA rank, learning rate), reward weights, and case study examples, which helps others build on this work.

## Weaknesses
**W1 — Missing variance and statistical significance (Severity: Major).** All reported metrics (F1, BLEU, BERTScore, BARTScore) in Tables 1, 3, 4, and 5 are presented as point estimates without standard deviations, confidence intervals, or significance tests. Given that the absolute gains over the strongest baseline are modest (~0.03 F1 on DuRecDial, ~0.026 F1 on ESConv), it is unclear whether these differences are statistically reliable or within noise range. This is the most critical threat to the paper's central claim of superiority. (See Annotation: Page 8 - Table 1)

**W2 — Downstream evaluation confound (Severity: Major).** The downstream response generation experiment (Table 4) compares Direct Prompt, CoT Prompt, and CoT ConvINT using ChatGPT. CoT ConvINT includes additional structured context that is absent in the CoT Prompt baseline. The observed improvement may partially or entirely come from having more context tokens rather than from ConvINT's aspect-specific content. A proper control (equal-length non-ConvINT context) is missing. (See Annotation: Page 10 - Table 4)

**W3 — Heavy dependence on LLM annotations (Severity: Major).** The ablation study (Table 3) shows catastrophic collapse when Dmid (LLM-annotated data) is removed (F1 drops from 0.5814 to 0.2355, a 59.5% decline), while removing Dfine (human annotations) causes only a 5.6% drop. This indicates the model learns primarily from GPT-3.5-turbo annotations, inheriting potential biases, and that human annotations provide marginal added value. This dependence pattern is not adequately discussed. (See Annotation: Page 9 - Ablation Table 3)

**W4 — Test set ground truth annotation details missing (Severity: Major).** The evaluation protocol states that human annotators labeled the test set for ground truth, but critical details are absent: number of annotators, inter-annotator agreement on the test set labels, disagreement resolution method, and exact test set size. Since all ConvINT generation quality metrics depend on this ground truth, missing these details reduces confidence in the entire evaluation. (See Annotation: Page 6 - Evaluation Protocols)

**W5 — Novelty assessment deferred (Severity: Informational).** External literature search is unavailable in this review run. Claims of novelty (e.g., 'first' ConvINT dataset, 'novel semi-structured framework') and positioning against the strongest related baselines cannot be independently verified. The authors should ensure precise scope bounding for all novelty claims. (See Annotation: Page 3 - Contributions)

**W6 — Related work is citation-list style, not comparative (Severity: Moderate).** The Related Work section for CU reads as a chronological survey with dense citations rather than organizing around decision-relevant comparison axes. It does not explicitly differentiate ConvINT from the closest prior methods. (See Annotation: Page 3 - Related Works)

**W7 — Conclusion is generic and lacks specificity (Severity: Moderate).** The conclusion uses broad language ('extensive experiments demonstrate the advantages') without numeric anchors, bounded limitations, or prioritized future work. This weakens the paper's closing impact. (See Annotation: Page 10 - Conclusion)

## Key Issues
**Issue 1 (Critical): Missing statistical reliability — all results are point estimates without variance.** Tables 1–5 report only single-run metrics. The F1 gain over the strongest baseline is small (+0.0295 on DuRecDial, +0.0256 on ESConv). Without multi-seed standard deviations or significance tests, readers cannot assess whether these differences are meaningful. This issue affects the paper's core claim that ConvINT+WeRG outperforms baselines.

*Root cause:* Either experiments were run once due to cost, or variance was omitted during reporting. Single-run results in neural generation tasks can fluctuate substantially.

*Impact if unfixed:* The main empirical claim is not falsifiable. Reviewers may reasonably challenge whether the reported gains exceed training noise.

*Fix:* Report mean±std over ≥3 random seeds for all main tables. Add a paired significance test (bootstrap or t-test) comparing the proposed method against the strongest baseline. If multi-seed runs are genuinely infeasible, state this clearly and use conservative language.

---

**Issue 2 (Major): Downstream evaluation confounds ConvINT content with prompt length.** Table 4 compares Direct Prompt → CoT Prompt → CoT ConvINT, where CoT ConvINT receives substantially more structured context. The improvement may be driven by increased context length rather than ConvINT's aspect-specific content. This undermines the claim that 'ConvINT markedly improves the ability of downstream response generation models.'

*Root cause:* The control condition (CoT Prompt) does not match the CoT ConvINT condition on prompt length and structure.

*Impact if unfixed:* The downstream evaluation cannot distinguish between 'ConvINT content helps' and 'more context helps,' weakening a key contribution claim.

*Fix:* Add a control: CoT Prompt + equal-length non-ConvINT context. Alternatively, add a 'CoT Prompt + generic dialogue summary' condition.

---

**Issue 3 (Major): Ablation reveals overwhelming reliance on LLM annotations without sufficient discussion.** Removing Dmid (GPT-3.5-turbo annotations) causes a 59.5% F1 collapse, while removing Dfine (human annotations) causes only a 5.6% drop. This suggests: (a) the model learns primarily from noisy LLM data, (b) human annotation provides marginal benefit relative to cost, and (c) the model inherits GPT-3.5-turbo's biases.

*Root cause:* The Dmid data likely dominates in volume and coverage, creating heavy dependence.

*Impact if unfixed:* The claimed value of the WeRG mechanism's tiered reward design is questionable if the model can function almost without human data.

*Fix:* Add discussion of this dependence. Test a Dfine-only + Dcoarse (without Dmid) configuration. Report the relative sizes of Dcoarse, Dmid, Dfine.

---

**Issue 4 (Major): Test set ground truth annotation is underspecified.** The paper states 'we engage human annotators to label the ConvINT labels for the test set' but omits: number of annotators, inter-annotator agreement, disagreement resolution, and test set size. All generation metrics depend on this ground truth.

*Root cause:* Oversight in reporting; the human evaluation section (Table 2) reports Fleiss' Kappa for evaluation annotations but not for test set labels.

*Impact if unfixed:* The entire quantitative evaluation rests on unverified annotation quality.

*Fix:* Add a dedicated paragraph describing test set annotation protocol with inter-annotator agreement scores.

---

**Issue 5 (Moderate): Conclusion and abstract lack quantitative specificity.** The abstract states 'markedly improves ... yielding significant gains' without concrete numbers. The conclusion says 'extensive experiments demonstrate the advantages' without numeric anchors or bounded limitations.

*Root cause:* Template-level writing that does not incorporate specific results.

*Impact if unfixed:* Reduced reader confidence and weaker memorability.

*Fix:* Add compact numeric anchors (F1 scores, SR improvements) to both abstract and conclusion. Add explicit limitations.

## Actionable Suggestions
**Suggestion 1 (Must): Add multi-seed variance and statistical significance.** Run all main experiments (Tables 1, 3, 4) with at least 3 random seeds. Report mean±std for each metric. For Table 1, add a paired bootstrap test comparing Ours vs. CoT w/ example, and report the p-value. This single change would substantially increase the paper's empirical credibility.

**Suggestion 2 (Must): Add prompt-length control for downstream evaluation.** Add a new condition to Table 4: 'CoT Prompt + extra context' where the response generation model receives additional non-ConvINT context of matched length (e.g., a generic dialogue summary). If CoT ConvINT still outperforms this control, the claim that ConvINT content specifically drives improvement is strongly supported.

**Suggestion 3 (Must): Document test set ground truth annotation thoroughly.** Add a paragraph in Section 4.2 specifying: (a) number of annotators, (b) inter-annotator agreement (Fleiss' Kappa) for test set labels, (c) disagreement resolution procedure, (d) test set size in turns/utterances. This is necessary to validate the evaluation foundation.

**Suggestion 4 (Must): Discuss Dmid dependence and test alternative configurations.** Add a paragraph analyzing why Dmid removal causes catastrophic collapse. Report the relative sizes of Dcoarse, Dmid, Dfine. Test a Dfine-only + Dcoarse configuration (without Dmid) to determine whether the model can learn from higher-quality but smaller data. If Dmid dependence is inevitable, state this as a limitation.

**Suggestion 5 (Should): Restructure Related Work around comparison axes.** Replace the current chronological citation listing with 2-3 comparative axes: structured ontology methods, free-text summarization, and aspect-based frameworks. For each axis, explicitly state the common assumptions and how ConvINT differs.

**Suggestion 6 (Should): Add quantitative anchors to Abstract and Conclusion.** Replace generic statements ('markedly improves,' 'extensive experiments demonstrate') with specific numbers: e.g., 'ConvINT with WeRG achieves F1 of 0.5814 on DuRecDial and 0.6324 on ESConv, improving Success Rate in downstream response generation from 0.7952 to 0.8537.'

**Suggestion 7 (Should): Fix Equation (4) notation.** Replace `arg max_θ J_WeRG(θ)` with the standard closed-form solution: `π*(o|h,x,c) ∝ π_w(o|h,x,c) exp((1/β) * rc(h,x,o))` to avoid conflating the optimal policy with the parameterized policy.

**Suggestion 8 (Nice-to-have): Expand human evaluation sample size.** Increase from 50 to at least 200 conversations per dataset, and report confidence intervals for human evaluation scores. Clarify whether annotators were blinded to method identity.

**Suggestion 9 (Nice-to-have): Add OOD/robustness experiments.** Test ConvINT annotation quality on held-out dialogue domains not seen during training to assess generalization. This would strengthen the claim of practical applicability.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows this structure:
- P1: CU background and structured ontology approaches (heavy citation listing)
- P2: LLMs demand richer CU; free-text alternative has limitations
- P3: ConvINT framework introduced
- P4: WeRG mechanism preview
- P5: Contributions

**Strengths of current storyline:** Covers all necessary components. The ConvINT introduction is well-placed after establishing the limitations of both extremes.

**Weaknesses:** P1 reads as a citation-heavy literature survey rather than a problem-driven opening. The gap between 'structured ontologies fail' and 'our solution works' could be tighter. The contribution list uses 'first' (C3) without scope qualifier.

### Alternative Storyline 1 (Recommended): Problem-Gap-Solution-Evidence

This storyline reorganizes the introduction to foreground the problem and evidence earlier.

**Abstract Outline (complete):**
- S1: Conversational understanding is critical for LLM-based dialogue systems, but current methods either use rigid slot-value ontologies (inflexible) or unstructured free-text (hard to evaluate).
- S2: We propose ConvINT, a semi-structured framework that organizes user intentions into four aspects — situation, emotion, action, knowledge — each expressed in free-form language.
- S3: To scale annotation, we introduce WeRG, a weakly-supervised RL method combining coarse, mid, and fine annotations with tiered rewards.
- S4: On DuRecDial and ESConv, ConvINT+WeRG achieves F1 of 0.5814 and 0.6324 respectively, outperforming few-shot CoT prompting by 2.95 and 2.56 points.
- S5: Downstream response generation with ConvINT improves Success Rate from 0.7952 to 0.8537, demonstrating practical value.

**Introduction Outline (complete):**
- P1 (Problem): 'LLM-based conversational systems need to understand nuanced user intentions — emotions, situational context, evolving knowledge — but current CU methods parse inputs into rigid slot-value pairs within static ontologies. This fundamental mismatch limits real-world deployment.'
- P2 (Gap): 'Free-text summarization offers flexibility but produces outputs that are hard to evaluate systematically, and without explicit aspect guidance, may drift from core intent elements. What is missing is a middle ground: fixed intention aspects expressed in natural language.'
- P3 (Solution): 'We introduce ConvINT, which decomposes user intentions into situation, emotion, action, and knowledge — inspired by the semantic pointer theory of intentions. Unlike structured ontologies, each aspect is free-form; unlike free-text, the framework provides structural guidance.'
- P4 (Method preview + Evidence): 'To generate ConvINT annotations at scale, we develop WeRG, which integrates coarse (existing intents), mid (LLM-annotated), and fine (human) supervision via tiered rewards. We show that ConvINT+WeRG achieves F1 of 0.5814/0.6324 on two datasets and improves downstream response SR to 0.8537.'
- P5 (Contributions): Three concise, bounded statements without 'first'.

### Alternative Storyline 2: Application-First

Open with a concrete dialogue example showing the failure of existing methods (already present in Figure 1, but foregrounded as a narrative hook in the introduction text). Then derive the framework requirements from this example. This may be more engaging for a conference audience.

### Three Alignment Checks for Recommended Storyline

- [x] Problem alignment: The stated challenge (rigid vs unstructured) maps directly to the proposed solution (semi-structured with fixed aspects).
- [x] Variable alignment: Situation, emotion, action, knowledge appear as the core output variables in the Method section.
- [x] Contribution-evidence alignment: F1/SR metrics in Experiments directly support the claims about annotation quality and downstream improvement.

## Priority Revision Plan
### P0 Items (Publication-Critical — Must Fix Before Acceptance)

| Priority | Issue | Fix | Effort | Expected Impact |
|----------|-------|-----|--------|-----------------|
| P0-1 | Missing variance/significance (Tables 1-5) | Run 3+ seeds, report mean±std, add significance test | Medium (compute cost) | High — resolves biggest validity threat |
| P0-2 | Downstream eval confound (Table 4) | Add prompt-length control condition | Low (prompt engineering + API calls) | High — clarifies whether ConvINT content drives gains |
| P0-3 | Test set annotation underspecified | Add annotation protocol + inter-annotator agreement | Low (documentation only) | High — validates evaluation foundation |
| P0-4 | Dmid dependence not discussed | Add analysis paragraph + test Dfine-only config | Medium (1 extra experiment) | Medium — addresses robustness concern |

### P1 Items (High Importance — Should Fix)

| Priority | Issue | Fix | Effort | Expected Impact |
|----------|-------|-----|--------|-----------------|
| P1-1 | Abstract lacks quantitative anchors | Add F1 and SR numbers | Low | Medium — improves first impression |
| P1-2 | Conclusion generic | Rewrite with validated findings, limitations, future work | Low | Medium — strengthens closing impact |
| P1-3 | Related Work is citation-list style | Reorganize around 2-3 comparison axes | Medium | Medium — clarifies positioning |
| P1-4 | Eq(4) notation issue | Fix `arg max_θ` to closed-form | Low | Low — resolves derivation clarity |

### P2 Items (Nice to Have)

| Priority | Issue | Fix | Effort | Expected Impact |
|----------|-------|-----|--------|-----------------|
| P2-1 | 'First' claim unbounded | Remove or scope-qualify | Low | Low — avoids reviewer challenge |
| P2-2 | Human evaluation small scale | Expand to 200+ samples | Medium | Low-Medium |
| P2-3 | OOD/robustness missing | Add cross-domain test | High | Medium |

### Revision Order

1. **P0-3** (documentation only, quickest win)
2. **P0-1** (most critical for validity)
3. **P0-2** (second most critical for claims)
4. **P0-4** (important for robustness)
5. **P1-1, P1-2** (quick writing fixes)
6. **P1-3, P1-4** (structural improvements)
7. **P2 items** (if time permits)

### Expected Outcome After Full Revision

If P0 and P1 items are addressed: the paper would have statistically grounded empirical claims, a controlled downstream evaluation, and clearly scoped novelty positioning. The core idea (semi-structured intention framework with tiered weak supervision) would be solidly supported. Remaining limitations (e.g., single LLM annotator, two English datasets) would be transparently stated.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1 | ConvINT generation quality (Table 1) | DuRecDial + ESConv; compare Direct/CoT Prompt baselines | F1, BLEU-1/2, BERTScore, BARTScore | Ours outperforms baselines on all metrics | C2 (WeRG superiority) | Single run, no variance |
| E2 | Human evaluation (Table 2) | 50 conversations, 3 annotators, 3 criteria | Info, Und, Con (0-5) | Ours scores highest on all criteria | C2 (WeRG quality) | Small sample, ceiling on Und |
| E3 | Ablation: data composition (Table 3) | Remove Dcoarse/Dmid/Dfine/rc | F1, BLEU-1/2, BERTScore, BARTScore | Dmid removal causes catastrophic drop; rc removal degrades moderately | C2 (WeRG design) | No Dfine-only + Dcoarse config |
| E4 | Fine-annotated proportion (Fig 3) | Vary Dfine from 10%-30% | F1, BLEU-1/2, BERTScore, BARTScore | Performance improves with more fine data | C2 (human annotation value) | Only tested on DuRecDial |
| E5 | Downstream response gen (Table 4) | DuRecDial; ChatGPT backbone; Direct/CoT/CoT-ConvINT | F1, BLEU-1/2, SR, Avg Turns | CoT ConvINT improves SR from 0.7952 to 0.8537 | C3 (ConvINT helps downstream) | Confounded with prompt length |
| E6 | Aspect removal (Table 5) | ESConv; remove one aspect at a time | F1, BLEU-1/2, SR, Avg Turns | Removal of EMOTION causes largest drop | C1 (aspect value) | Only on ESConv |

### Research-Theme Gap Diagnosis

- **New knowledge:** The paper's core knowledge contribution — that a semi-structured four-aspect framework improves CU — is directionally supported but the evidence is weakened by missing variance (E1) and confounded controls (E5).
- **Reproducibility:** Implementation details are provided (LoRA config, learning rate, prompts), which is good. However, the lack of multi-seed results and test set annotation details reduces exact reproducibility.
- **Impact on practice:** The WeRG annotation pipeline has practical value for dataset construction. The claim that 'only 10% human annotation is needed' is interesting but needs stronger evidence given the Dmid dependence finding.

### Proposed Research Experiments

**P0 Experiment A: Multi-seed evaluation of main results**
- *Target Claim:* C2 — WeRG generates higher-quality ConvINT data than baselines
- *Hypothesis:* The observed gains exceed training noise
- *Minimal Design:* Run Ours + CoT w/ example on DuRecDial with 3 seeds each; report mean±std for F1, BLEU-1/2
- *Controls/Baselines:* Same seed set, same hyperparameters
- *Metrics:* F1 mean±std, paired bootstrap p-value
- *Success Criterion:* Gain > 2× std and p < 0.05
- *Estimated Cost:* ~3× current compute (can reuse existing code)
- *Expected Quality Gain:* High — resolves the most critical validity threat

**P0 Experiment B: Prompt-length control for downstream evaluation**
- *Target Claim:* C3 — ConvINT content improves downstream response generation
- *Hypothesis:* ConvINT provides task-relevant aspect information beyond generic context
- *Minimal Design:* Add condition 'CoT Prompt + matched-length generic summary' to Table 4
- *Controls/Baselines:* CoT Prompt (shorter), CoT ConvINT (aspect-specific), generic summary (matched length)
- *Metrics:* SR, Avg Turns, F1
- *Success Criterion:* CoT ConvINT outperforms both CoT Prompt and generic summary
- *Estimated Cost:* Low — ChatGPT API calls for new condition
- *Expected Quality Gain:* High — resolves confound, supports causal claim

**P1 Experiment C: Dfine-only + Dcoarse (without Dmid)**
- *Target Claim:* C2 — WeRG's tiered reward mechanism effectively leverages human annotations
- *Hypothesis:* Even without LLM annotations, the model can learn from human annotations combined with coarse labels
- *Minimal Design:* Train WeRG with Dfine + Dcoarse only (no Dmid), compare to full WeRG
- *Controls/Baselines:* Full WeRG, WeRG w/o Dfine
- *Metrics:* F1, BLEU-1/2
- *Success Criterion:* If Dfine+Dcoarse outperforms w/o Dfine, then human annotations provide independent value
- *Estimated Cost:* Low — one additional fine-tuning run
- *Expected Quality Gain:* Medium — clarifies the role of human annotation

**P1 Experiment D: Cross-domain OOD test**
- *Target Claim:* C1 — ConvINT framework is general and flexible
- *Hypothesis:* ConvINT annotations generalize to unseen dialogue domains
- *Minimal Design:* Train on DuRecDial, test on ESConv or a third unseen domain (e.g., task-oriented dialogues)
- *Controls/Baselines:* In-domain performance as reference
- *Metrics:* F1 drop from in-domain
- *Success Criterion:* F1 drop < 15% relative
- *Estimated Cost:* Low-Medium (need third dataset)
- *Expected Quality Gain:* Medium — demonstrates practical generality

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 Experiments (Before acceptance)
├── P0-A: Multi-seed runs (+3 seeds each)
│   ├── Ours vs CoT w/ example on DuRecDial
│   └── → mean±std F1 + bootstrap p-value
└── P0-B: Prompt-length control
    ├── Add "CoT + generic summary" to Table 4
    └── → Isolate ConvINT-specific improvement

P1 Experiments (High priority)
├── P1-C: Dfine-only + Dcoarse ablation
│   └── → Test independent value of human annotations
└── P1-D: Cross-domain OOD test
    └── → Test generality beyond trained domain
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

*Rationale:* The paper proposes a well-motivated and practically plausible semi-structured intention framework (ConvINT) combined with a clever weakly-supervised annotation pipeline (WeRG). The core ideas have clear value for conversational understanding. However, the empirical validation has critical limitations that prevent higher scoring:
- All reported metrics lack variance estimates and significance tests, making the claimed superiority unverifiable (Issue 1).
- The downstream evaluation confounds ConvINT content with prompt length (Issue 2).
- The ablation reveals heavy dependence on LLM annotations without adequate analysis (Issue 3).
- The test set ground truth annotation procedure is underspecified (Issue 4).
- Novelty cannot be independently assessed (Retrieval-Disabled Mode).

The paper's research contribution (new framework + annotation method) is solid in concept but the current evidence level is insufficient to fully support the claims. The writing quality is adequate but the conclusion and abstract lack quantitative specificity.

**Post-Revision Target: [6.5, 7.5]/10**

*Rationale:* If P0 items are fully addressed (multi-seed variance, prompt-length control, test set annotation documentation, Dmid dependence analysis) and P1 items are substantially improved (quantitative abstract/conclusion, restructured related work), the paper's empirical foundation would become solid. The core ideas are strong enough to support a score in this range after evidence strengthening. The upper bound is limited by the reliance on GPT-3.5-turbo (proprietary model) as mid annotator and the restriction to two English datasets, which are inherent scope constraints.