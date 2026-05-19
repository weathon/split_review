## Summary
This paper presents OmniSep, a unified omni-modal sound separation framework that can isolate target sound sources based on text, image, audio, or composed multi-modal queries. The core technical contributions are threefold: (1) a Query-Mixup training strategy that blends query features from different modalities to enable joint optimization across modalities; (2) a negative query mechanism that subtracts undesired sound information from the query embedding to suppress interfering sources; and (3) Query-Aug, a retrieval-augmented method that maps unrestricted natural language descriptions to the nearest in-domain class label for open-vocabulary separation. The architecture builds on CLIPSEP with a frozen ImageBind encoder and a U-Net-based separator. Experiments on MUSIC, VGGSOUND-CLEAN+, and MUSIC-CLEAN+ datasets demonstrate competitive or superior separation performance across text-queried (TQSS), image-queried (IQSS), and audio-queried (AQSS) tasks compared to existing baselines.

**Overall assessment:** The paper tackles a worthwhile problem—unifying multi-modal query-based sound separation—and presents a technically sound framework with reasonable empirical validation. However, several limitations reduce confidence in the claimed contributions: (a) the "state-of-the-art" claim is overstated given overlapping confidence intervals and uncontrolled compute budgets; (b) the "open-vocabulary" capability is retrieval-based rather than generative, which caps its generality; (c) the negative query mechanism is a simple heuristic without theoretical grounding; and (d) several experimental details (splits, significance tests, baselines) are insufficient for full reproducibility.

## Strengths
1. **Timely and relevant problem formulation.** The paper identifies a genuine gap in query-based sound separation: existing methods operate on a single modality, while real-world users often have access to heterogeneous query signals (text descriptions, video frames, audio snippets). Unifying these modalities into a single framework is practically valuable and methodologically interesting.

2. **Simple yet effective Query-Mixup strategy.** The idea of linearly mixing modality embeddings during training to bridge modality gaps is elegant and easy to implement. The ablation study (Table 2) demonstrates that Query-Mixup improves average SDR across TQSS and IQSS compared to standard multi-modal joint training without mixing (6.70 vs. 6.45).

3. **Comprehensive evaluation across three query modalities.** The paper evaluates on TQSS, IQSS, and AQSS separately, as well as composed omni-modal queries, on three dataset variants. This provides a thorough picture of the method's capabilities and limitations.

4. **Negative query analysis (Figure 2).** The systematic exploration of the α parameter and the comparison between direct subtraction and proportional weighting provides useful practical insight for deploying negative queries. The finding that proportional weighting maintains stable performance across a wide range of α values is practically useful.

5. **Reproducibility commitment.** The authors state they will release code and models, and provide a demo page with audio samples, which is commendable for the field.

## Weaknesses
1. **Overclaimed SOTA (major).** The paper repeatedly claims "state-of-the-art" performance across all tasks, but the evidence is weaker than stated. Many improvements fall within overlapping confidence intervals (e.g., OmniSep on VGGSOUND-CLEAN+ TQSS: 6.70±0.66 vs AudioSEP: 6.26±0.87). No statistical significance tests are reported. Baselines come from different years with uncontrolled compute budgets, and OmniSep benefits from a frozen ImageBind backbone pre-trained on large multi-modal data. Missing baseline entries (e.g., i-Query on MUSIC-CLEAN+) make comparisons incomplete.

2. **"Open-vocabulary" is retrieval-based, not generative (major).** Query-Aug (Section 3.4) maps unrestricted text to the nearest in-domain class label via cosine similarity. The model never learns to process free-form text directly. This is fundamentally a retrieval workaround, not open-vocabulary understanding as the term is commonly used (e.g., CLIP-based segmentation). The contribution claim (#3) is misleadingly named and overstates the capability.

3. **Loss function uses unusual X-weighting without justification (major).** Eq. (3) defines WBCE with the mixed magnitude spectrum X as an element-wise weight. This input-dependent weighting scheme is not standard and is not justified or ablated. It may bias the model toward high-energy T-F bins and create gradient conflicts when multiple sources overlap in the same bin.

4. **Negative query is a simple heuristic without theoretical grounding (moderate).** Eq. (4) uses (1+α)Q - αQ_N, which is standard vector arithmetic (analogous to word embeddings analogies). There is no analysis of why proportional weighting preserves local frequency-band information, no discussion of embedding normalization after the operation, and no comparison against a simple learned gating mechanism.

5. **Reproducibility gaps (moderate).** Train/validation/test splits are not specified for MUSIC or VGGSOUND. The AQSS reference selection (S=5 for VGGSOUND, S=1 for MUSIC) introduces randomness that is not quantified across runs. Text query preprocessing details are omitted.

6. **Query-Mixup mixing weights are not analyzed (minor).** The random uniform weights w_a, w_v, w_t ∈ [0,1] are not ablated. No comparison against fixed equal weights, modal dropout, or scheduled mixing. The generalization from mixed (training) to pure (inference) embeddings is not explained.

7. **Related work is a chronological list rather than an organized comparison (minor).** The paper would benefit from grouping methods by technical approach and explicitly comparing against the strongest baselines along defined axes.

## Key Issues
### Issue 1: Overclaimed SOTA (Severity: Major | Validity Risk: High)
**Evidence:** The paper states "achieves state-of-the-art performance across TQSS, IQSS, and AQSS" (Page 1 Abstract, Page 6 Main Results, Page 10 Conclusion). In Table 1, many improvements fall within one standard deviation of baselines. For example, OmniSep TQSS on VGGSOUND-CLEAN+ (6.70±0.66) vs AudioSEP (6.26±0.87) — confidence intervals overlap. No significance tests are reported. Missing baseline entries (i-Query on MUSIC-CLEAN+) create selective comparison gaps. Pre-trained ImageBind provides an uncontrolled data/compute advantage.

**Impact:** This is a core contribution claim (contribution #4). Overclaiming SOTA without proper statistical controls weakens credibility with reviewers and the broader community.

### Issue 2: Misleading "Open-Vocabulary" Claim (Severity: Major | Validity Risk: High)
**Evidence:** Section 3.4 describes Query-Aug as retrieving the nearest in-domain class label via argmax cosine similarity. The model never processes free-form text. The claim "open-vocabulary sound separation" (Page 2, contribution #3) conflicts with the definition in prior work (e.g., CLIP-based segmentation models that directly process arbitrary text). Appendix C.3 shows Query-Aug applied to AudioSep also improves results, confirming the method is a generic retrieval wrapper, not an architectural innovation.

**Impact:** The paper's third contribution is overstated. True open-vocabulary capability would require the model to ingest free-form text directly, which is not achieved.

### Issue 3: Unjustified Loss Weighting (Severity: Major | Validity Risk: Moderate)
**Evidence:** Eq. (3) defines WBCE with X (mixed magnitude spectrum) as element-wise weight. This is an unusual formulation that is not standard in sound separation literature (CLIPSEP, which this paper builds on, uses standard BCE). The weighting is not justified, ablated, or compared against standard BCE.

**Impact:** If the weighting biases training toward high-energy T-F bins, the reported SDR gains may partially reflect this bias rather than the core Query-Mixup or negative query contributions. An ablation is needed.

### Issue 4: Unclear Novelty of Negative Query (Severity: Major | Validity Risk: Moderate)
**Evidence:** Section 3.3 uses (1+α)Q - αQ_N, which is standard vector arithmetic — a linear interpolation/extrapolation operation common in embedding spaces. The paper provides no theoretical analysis of why this preserves frequency-band information. No comparison against a learned gating baseline. The improvement is modest (0.10 to 1.60 SDR) and may not be statistically significant.

**Impact:** The negative query is listed as a core contribution (#2), but its novelty is limited to applying an existing technique (embedding arithmetic) to a new domain without domain-specific adaptation or analysis.

### Issue 5: Reproducibility Gaps (Severity: Moderate | Validity Risk: Moderate)
**Evidence:** Missing train/val/test splits, no specification of random seeds for AQSS reference selection, omitted text query preprocessing details. The result "training on MUSIC...evaluating on itself" (Page 6) is ambiguous.

**Impact:** Makes verification and fair comparison difficult for future work.

## Actionable Suggestions
### S1: Tone down SOTA claims and add statistical rigor (Must)
**Affected:** Abstract, Page 6 Main Results, Page 10 Conclusion
1. Replace "state-of-the-art" with "competitive or superior performance under evaluated conditions" throughout.
2. Add paired bootstrap or Wilcoxon signed-rank tests comparing OmniSep against the strongest baseline per setting.
3. Report SDR improvement significance with p-values in Table 1 footnote.
4. Explicitly acknowledge that ImageBind pre-training provides an uncontrolled data advantage.

### S2: Rename and reframe Query-Aug (Must)
**Affected:** Page 2 contribution #3, Page 5 Section 3.4, Page 9 Table 3 analysis
1. Rename "open-vocabulary sound separation" to "retrieval-augmented open-vocabulary separation" or "query-mapping-based separation."
2. Add a paragraph explaining that this is a practical retrieval workaround, not a generative approach, and discuss its limitation when the nearest class label is a poor semantic match.
3. Analyze failure cases using outlier detection or similarity thresholding.

### S3: Justify or correct the loss function (Must)
**Affected:** Page 5 Eq. (3)
1. If X-weighting is intentional, add a paragraph explaining why magnitude-weighted BCE is beneficial and add an ablation against standard BCE.
2. If X-weighting is unintentional or a notation error, correct the formula to standard BCE.
3. Add a statement on whether any post-processing normalization is applied to the loss.

### S4: Strengthen negative query analysis (Nice-to-have)
**Affected:** Page 5 Section 3.3, Page 7-8 Section 4.3
1. Add a comparison against a simple learned combination (linear layer taking [Q; Q_N]).
2. Report whether Q' is normalized to the original embedding norm after Eq. (4).
3. Add statistical significance markers to Figure 2.
4. Acknowledge that this is a practical heuristic rather than a theoretically grounded contribution, and scale back its prominence in the contribution list if appropriate.

### S5: Improve reproducibility (Must)
**Affected:** Page 6 Section 4.1
1. Report exact train/val/test instance counts and split methodology for all datasets.
2. Fix AQSS reference audio selection (freeze the reference set and release it).
3. Specify text query preprocessing steps.
4. Report results with multiple random seeds and compute variance across both model training and AQSS reference selection.

### S6: Ablate Query-Mixup weighting (Nice-to-have)
**Affected:** Page 4 Eq. (1), Page 6 Table 2
1. Compare uniform random mixing against fixed equal weights, Dirichlet-distributed weights, and modality-dropout training.
2. Add an analysis of training convergence (loss curves per modality) to support the claim that Query-Mixup stabilizes training objectives.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current manuscript follows a standard structure: Abstract → Introduction (chronological survey → three challenges → proposed solution → contributions) → Related Work (three subsections) → Method (four subsections) → Experiments (implementation → main results → negative query analysis → open-vocabulary evaluation → qualitative analysis) → Conclusion. The narrative flows logically but has several weaknesses:
- The Introduction surveys prior work by modalities in sequence without a clear synthesized gap. The problem->solution transition is abrupt.
- Contribution claims are embedded in the introduction without clear signposting of novelty.
- Related Work mixes chronological listing with function-based organization inconsistently.

### Three Alternative Storyline Candidates

**Candidate A (Problem-First):**
Big Picture: "Sound separation is bottlenecked by single-modality queries." → Gap: "No existing system can accept arbitrary multi-modal or composed queries." → Insight: "Query embeddings from different modalities can be mixed during training to learn a unified separation space." → Solution: OmniSep with Query-Mixup → Evidence: Tables 1-3 → Contribution summary.
*Best for*: A broad-audience venue like ICLR. Makes the problem instantly clear.

**Candidate B (Method-First):**
Big Picture: "Query-Mixup is a simple training strategy for multi-modal unification." → Gap: Prior work uses modality-specific training. → Insight: Random convex combinations of query embeddings allow the separator to learn from all modalities simultaneously. → Solution: OmniSep + Negative Query + Query-Aug as practical extensions. → Evidence.
*Best for*: A method-focused venue. Highlights the technical novelty of Query-Mixup.

**Candidate C (Application-First):**
Big Picture: "Users want flexible control over which sounds to extract or suppress from a mixture." → Gap: Current tools require a specific query modality and cannot suppress unwanted sounds. → Solution: OmniSep accepts any modality as query, and negative queries enable suppression. → Evidence: Demo and quantitative results. → Contribution.
*Best for*: A systems/demo-oriented venue.

**Recommended: Candidate A (Problem-First)** — It best aligns with the paper's strength (identifying and addressing the multi-modal query unification gap) while avoiding the impression that the contributions are merely engineering.

### Abstract Outline (Complete)

**S1 (Problem):** "Query-based sound separation has advanced with text, image, and audio queries, but each method is restricted to a single modality, preventing users from leveraging complementary query signals."

**S2 (Gap):** "No existing framework can accept arbitrary combinations of text, image, and audio queries, nor can it suppress undesired sounds using negative information."

**S3 (Solution):** "We propose OmniSep, a unified omni-modal separation framework trained with Query-Mixup—a strategy that blends query features from different modalities—enabling a single model to handle both single-modal and composed multi-modal queries."

**S4 (Components):** "OmniSep further incorporates negative query manipulation for interference suppression and retrieval-augmented query mapping for separation beyond predefined class labels."

**S5 (Evidence + Scope):** "On MUSIC, VGGSOUND-CLEAN+, and MUSIC-CLEAN+ datasets, OmniSep achieves competitive or superior SDR against existing single-modality baselines across text-, image-, and audio-queried tasks."

### Introduction Outline (Complete)

**P1 (Motivation + Landscape):** "Sound separation has progressed from domain-specific to query-based separation. Three query modalities exist (text, image, audio), but each method operates in isolation. This paragraph should condense the current first two intro paragraphs into one."

**P2 (Gap Definition):** "Three specific limitations remain: (1) no unified model for composed multi-modal queries, (2) no mechanism to suppress sounds using negative information, (3) training data with only class labels prevents free-text generalization."

**P3 (Proposed Solution):** "We introduce OmniSep, which addresses (1) via Query-Mixup—mixing query embeddings during training—(2) via negative query vector arithmetic, and (3) via retrieval-augmented query mapping (Query-Aug)."

**P4 (Evidence + Contributions):** "We evaluate on three datasets and four task settings, showing consistent improvements. Our contributions are: [condensed list with bounded claims]."

## Priority Revision Plan
### P0 — Publication-Critical (Must fix before acceptance)

| Priority | Item | Action | Expected Impact | Effort |
|----------|------|--------|----------------|--------|
| P0.1 | Overclaimed SOTA | Replace SOTA claims with bounded wording; add significance tests to Table 1 | High: addresses core credibility issue | Medium (1-2 days) |
| P0.2 | Misleading "open-vocabulary" claim | Rename Query-Aug; add limitation paragraph on retrieval ceiling | High: corrects contribution claim scope | Low (few hours) |
| P0.3 | Reproducibility gaps | Report splits, seeds, AQSS reference set, preprocessing details | High: enables verification | Low (few hours) |
| P0.4 | Loss function justification | Validate or correct Eq. (3) X-weighting; add ablation | High: ensures methodological soundness | Medium (1-2 days) |

### P1 — Important for Quality (Strongly recommended)

| Priority | Item | Action | Expected Impact | Effort |
|----------|------|--------|----------------|--------|
| P1.1 | Negative query analysis | Add learned baseline comparison; discuss normalization | Medium: clarifies mechanism novelty | Medium |
| P1.2 | Related work restructuring | Reorganize by conceptual categories | Medium: improves reader positioning | Low |

### P2 — Quality Polish (Nice to have)

| Priority | Item | Action | Expected Impact | Effort |
|----------|------|--------|----------------|--------|
| P2.1 | Query-Mixup ablation | Compare mixing strategies | Low: strengthens technical depth | Medium |
| P2.2 | Failure analysis | Add Query-Aug failure cases; add negative query failure modes | Low: provides completeness | Medium |

### Revision Strategy Roadmap (ASCII)

```text
[Current manuscript issues]
    |
    ├── P0.1 Overclaimed SOTA
    |       → Replace "SOTA" with bounded language
    |       → Add significance tests
    |       → Expected: credibility restored
    |
    ├── P0.2 Misleading "open-vocabulary"
    |       → Rename to "retrieval-augmented separation"
    |       → Add ceiling limitation
    |       → Expected: claim scope matches evidence
    |
    ├── P0.3 Reproducibility gaps
    |       → Report splits/seeds/preprocessing
    |       → Freeze AQSS reference set
    |       → Expected: reproducible by others
    |
    ├── P0.4 Loss function justification
    |       → Validate X-weighting vs standard BCE
    |       → Add ablation experiment
    |       → Expected: methodological soundness confirmed
    |
    ├── P1.1 Negative query analysis
    |       → Add learned baseline
    |       → Expected: novelty boundary clarified
    |
    └── P2.x Polish items
            → Expected: strengthened manuscript for camera-ready
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 (Table 1) | Main comparison: OmniSep vs baselines across TQSS, IQSS, AQSS | MUSIC, VGGSOUND-CLEAN+, MUSIC-CLEAN+; standard splits | Mean/Med SDR | OmniSep outperforms or matches baselines across most settings | C4 (SOTA claim) | No significance tests; overlapping CIs; missing baseline entries |
| E2 (Table 2) | Ablation: Query-Mixup effect on TQSS/IQSS | VGGSOUND-CLEAN+; modality combinations | Mean/Med SDR, AVG SDR | Query-Mixup improves AVG SDR (6.70 vs 6.45) | C1 (Query-Mixup) | No comparison against fixed-weight mixing |
| E3 (Figure 2) | Negative query analysis: α sensitivity | VGGSOUND-CLEAN+, MUSIC-CLEAN+; α ∈ [0,2] | Mean SDR | Proportional weighting more stable than direct subtraction | C2 (negative query) | No learned baseline; no significance markers |
| E4 (Table 3) | Open-vocabulary: Query-Aug on out-of-domain text | VGGSOUND-CLEAN+; GPT-3.5 rewritten labels | Mean/Med SDR | Query-Aug improves from 4.95 to 6.32 SDR | C3 (Query-Aug) | Retrieval-bound; not true open-vocabulary |
| E5 (Table 9, Appendix C.3) | Query-Aug generalization on AudioSep | AudioCaps, MUSIC, ESC-50, Clotho | SDRi, SI-SDR | Query-Aug improves AudioSep across all | C3 (Query-Aug) | Only tested on one base model |
| E6 (Table 10, Appendix C.4) | AQSS ablation: modality contributions | VGGSOUND-CLEAN+ | Mean/Med SDR | Audio + Text + Image + MixUP best (7.12) | C1 (Query-Mixup) | Small absolute gains |
| E7 (Table 11, Appendix C.5) | ImageBind ablation: frozen vs tuning vs no pretrain | VGGSOUND-CLEAN, MUSIC | SDR per modality | Frozen ImageBind balances performance and generalization | C1 (architecture design) | No analysis of why fine-tuning hurts OOD |

### Research-Theme Gap Diagnosis

| Theme | Current Status | Gap |
|-------|---------------|-----|
| New knowledge | Query-Mixup is novel but simple; negative query is heuristic; Query-Aug is retrieval wrapper | Limited conceptual novelty beyond applying existing techniques |
| Reproducibility | Splits/seeds unspecified; AQSS reference not frozen | Cannot fully reproduce |
| Impact on practice | Unified multi-modal query framework is practically useful | Need open-source code release and broader dataset evaluation to demonstrate real-world utility |

### Proposed Research Experiments (P0/P1/P2)

**Exp-P0.1: Loss Function Ablation (Target: Issue 3)**
- **Target Claim:** The X-weighted BCE loss (Eq. 3) is correctly formulated and beneficial.
- **Hypothesis:** Standard BCE produces similar or better results than X-weighted BCE.
- **Minimal Design:** Train OmniSep with standard BCE loss (remove X weighting); compare with current loss on VGGSOUND-CLEAN+ TQSS.
- **Controls/Baselines:** Same architecture, data, hyperparameters; only loss function changes.
- **Metrics:** Mean SDR, Med SDR.
- **Success Criterion:** If standard BCE yields ≤0.2 SDR difference, the X-weighting is unnecessary and should be replaced for simplicity.
- **Estimated Cost/Time:** ~1 GPU-day.
- **Expected Paper-Quality Gain:** Clarifies a questionable design choice; high impact on methodological soundness.

**Exp-P0.2: Statistical Significance Testing (Target: Issue 1)**
- **Target Claim:** OmniSep significantly outperforms baselines.
- **Hypothesis:** Reported SDR improvements are statistically significant.
- **Minimal Design:** Paired bootstrap test (10k resamples) comparing OmniSep vs best baseline per task in Table 1.
- **Controls/Baselines:** Same test samples.
- **Metrics:** p-value, 95% CI of SDR difference.
- **Success Criterion:** p < 0.05 for at least the primary comparisons.
- **Estimated Cost/Time:** Computational (few hours).
- **Expected Paper-Quality Gain:** Validates or qualifies the SOTA claim.

**Exp-P1.1: Negative Query Learned Baseline (Target: Issue 4)**
- **Target Claim:** The hand-crafted proportional weighting is optimal.
- **Hypothesis:** A learned MLP taking [Q; Q_N] can outperform Eq. (4).
- **Minimal Design:** Train a small 2-layer MLP that predicts Q' from Q and Q_N, using the separation loss. Compare against Eq. (4) at optimal α.
- **Controls/Baselines:** Same Separate-Net; same training budget.
- **Metrics:** Mean SDR.
- **Success Criterion:** If learned baseline outperforms Eq. (4) by >0.3 SDR, the heuristic is suboptimal and should be replaced.
- **Estimated Cost/Time:** ~1 GPU-day.
- **Expected Paper-Quality Gain:** Clarifies the novelty boundary of the negative query contribution.

### Experiment Upgrade Plan (ASCII)

```text
[Current experiments]
    |
    ├── E1 (Table 1): Main comparison → ADD significance tests (P0.2)
    |
    ├── E2 (Table 2): Query-Mixup ablation → ADD fixed-weight baseline (P2.1)
    |
    ├── E3 (Figure 2): Negative query analysis → ADD learned baseline (P1.1)
    |
    ├── E4 (Table 3): Query-Aug → ADD failure case analysis (P2.2)
    |
    └── Current loss (Eq. 3) → ADD standard BCE ablation (P0.1)
    
[Proposed additions]
    P0.1: Loss function ablation (standard BCE vs X-weighted BCE)
    P0.2: Statistical significance tests (bootstrap, all comparisons)
    P1.1: Learned negative query combination (MLP)
    P2.1: Query-Mixup mixing strategy comparison
    P2.2: Query-Aug failure mode analysis
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

*Rationale:* The paper addresses a relevant problem (unified multi-modal query-based sound separation) with a technically sound approach. Query-Mixup is simple yet effective, and the empirical evaluation covers multiple query modalities comprehensively. However, the score is reduced due to: (a) overclaimed SOTA statements without statistical significance verification; (b) misleading "open-vocabulary" framing that overstates the Query-Aug contribution; (c) an unusual loss function (X-weighted BCE) without justification; (d) the negative query contribution being a straightforward embedding heuristic rather than a novel mechanism; and (e) reproducibility gaps in dataset splits and experimental protocols. The paper's research value is moderate—it consolidates existing ideas (multi-modal embeddings, vector arithmetic, retrieval augmentation) into a single framework rather than introducing fundamentally new concepts.

**Post-Revision Target: [7.0, 7.5]/10**

*Rationale:* If the authors address the P0 items (toning down SOTA claims, correcting the open-vocabulary framing, fixing reproducibility gaps, and validating the loss function), the paper would present a clean, well-scoped engineering contribution with solid empirical support. The remaining P1/P2 items would further strengthen technical depth but are not required for acceptance at most venues. The score is capped at ~7.5 because the core methodological novelty is incremental (combining existing techniques) and the negative query and Query-Aug components are simple heuristics with limited theoretical depth.

---

### Page Coverage Audit

| Page | Section | Annotation Count | Coverage Status | Skip Reason (if applicable) |
|------|---------|-----------------|-----------------|----------------------------|
| 1 | Abstract + Introduction (P1) | 3 | Covered | — |
| 2 | Introduction (P2-P3) + Related Work start | 1 | Covered | — |
| 3 | Related Work (Universal + Query-Based + Multi-modal) | 1 | Covered | — |
| 4 | Method (Overview, Query-Net, Separate-Net start) | 1 | Covered | — |
| 5 | Method (Separate-Net cont., Negative Query, Query-Aug) | 2 | Covered | — |
| 6 | Experiments (Implementation, Main Results start) | 2 | Covered | — |
| 7 | Main Results (Table 1, Table 2, Negative Query start) | 0 | Skipped (non-substantive, contains tables primarily) | Tables are annotated via surrounding paragraph text |
| 8 | Negative Query analysis (Figure 2, conclusions) | 1 | Covered | — |
| 9 | Open-Vocabulary (Table 3, analysis) | 1 | Covered | — |
| 10 | Qualitative Analysis + Conclusion | 1 | Covered | — |
| 11-14 | References | 0 | Skipped (bibliography, non-substantive) | — |
| 15-18 | Appendix | 0 | Skipped (supplementary material; minor claims) | Appendix contains implementation details and additional ablations consistent with main claims |

**Note on skipped appendix pages:** Appendix A (implementation details) and C (additional experiments) are informative but do not introduce new claims that contradict or significantly extend the main text. One annotation could be added to Appendix C.5 (ImageBind ablation) if deeper analysis is desired, but the current coverage of main claims is sufficient.

---

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Central Claim: OmniSep enables unified omni-modal sound separation]
    |
    ├── C1: Query-Mixup bridges modality gaps
    |       └── Evidence: Table 2 (#5 vs #4: 6.70 vs 6.45 AVG SDR)
    |       └── Gap: No ablation on mixing weight distribution
    |
    ├── C2: Negative query suppresses interference
    |       └── Evidence: Figure 2, Table 1 (+NQ rows)
    |       └── Gap: No learned baseline; heuristic lacks theory
    |
    ├── C3: Query-Aug enables open-vocabulary separation
    |       └── Evidence: Table 3 (#11 vs #10: 6.32 vs 4.95 SDR)
    |       └── Gap: Retrieval-based, not generative; misleading naming
    |
    └── C4: SOTA across TQSS/IQSS/AQSS
            └── Evidence: Table 1 (numerical improvements)
            └── Gap: Overlapping CIs; missing significance tests; compute uncontrolled
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
Query-Based Sound Separation (Root)
├── Branch 1: Query Modality
│   ├── Leaf 1.1: Text-Query (TQSS)
│   │   ├── Ochiai et al. (Universal Sound Selector)
│   │   ├── Kong et al. (Weakly-labeled separation)
│   │   ├── Liu et al. (Separate What You Describe)
│   │   ├── Liu et al. (AudioSep)
│   │   └── Veluri et al. (Real-time target extraction)
│   ├── Leaf 1.2: Image-Query (IQSS)
│   │   ├── Tzinis et al. (AudioScope)
│   │   ├── Dong et al. (CLIPSEP)
│   │   └── Chen et al. (i-Query)
│   ├── Leaf 1.3: Audio-Query (AQSS)
│   │   ├── Lee et al. (Audio query music separation)
│   │   └── Chen et al. (Zero-shot audio separation)
│   └── Leaf 1.4: Omni-Modal (THIS WORK)
│       └── OmniSep (Query-Mixup + Negative Query + Query-Aug)
│
├── Branch 2: Training Paradigm
│   ├── Leaf 2.1: Fully supervised (most TQSS/IQSS methods)
│   ├── Leaf 2.2: Unsupervised (MixIT)
│   └── Leaf 2.3: Multi-modal joint training (CLIPSEP, OmniSep)
│
└── Branch 3: Multi-modal Representation
    ├── Leaf 3.1: Dual-modal alignment (CLIP, CLAP)
    └── Leaf 3.2: Omni-modal alignment (ImageBind)
        └── Used as frozen encoder in OmniSep
```