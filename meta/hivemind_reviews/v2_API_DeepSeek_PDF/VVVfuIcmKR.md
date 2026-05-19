## Summary
# Final Review Report

## Summary

This paper identifies and systematically studies the phenomenon of **intra-modal misalignment** in CLIP-style vision-language models (VLMs). The core observation is that CLIP's inter-modal contrastive loss enforces alignment only between cross-modal pairs (image-text), leaving intra-modal similarities (image-image, text-text) unconstrained and therefore unreliable. To demonstrate this, the authors adapt Optimization-based Textual Inversion (OTI) and introduce Optimization-based Visual Inversion (OVI) — single-feature-level modality inversion techniques that map features from one modality into the complementary encoder's space without external data. By transforming intra-modal tasks (image-to-image and text-to-text retrieval) into inter-modal ones, they achieve consistent 2-5% mAP improvements across 15+ datasets and multiple VLM backbones. Controlled experiments confirm that the same OTI-inverted features that improve intra-modal retrieval harm inter-modal tasks (zero-shot classification), consistent with the misalignment hypothesis. Additional experiments with SLIP (which includes an intra-modal loss) and temperature-based modality gap manipulation further support the diagnosis.

**Primary strengths:** The paper addresses a genuinely important and under-appreciated problem — the systematic unreliability of intra-modal CLIP similarities — with a clear diagnostic methodology and extensive empirical validation across diverse models, datasets, and tasks. The modality inversion diagnostic framework (cross-task comparison showing opposite effects) is elegant and provides compelling evidence for the central claim.

**Primary weaknesses:** (1) The strongest causal claim — that improvement is "solely attributable to inter-modal alignment" — is not fully supported, as optimization-induced feature re-weighting is a confound. (2) The modality gap experiment (Sec. 5.6) has a confound between temperature and fine-tuning dataset, weakening the causal link. (3) The practical utility is limited: OTI/OVI are computationally expensive (150-1000 optimization steps per query) and require hyperparameter tuning, acknowledged but not adequately addressed. (4) The drift analysis (Sec. 5.4) only shows two snapshots rather than a continuous evolution, and the performance peak at step 17 (out of 1000) raises stability concerns.

## Strengths
**S1. Important and under-appreciated problem.** The paper identifies a genuine limitation of CLIP-style models: intra-modal similarities are unreliable because the training objective never constrains them. This is a conceptually important point that has practical implications for the many applications that use CLIP for intra-modal comparisons (e.g., KNN classification, temporal consistency metrics in video generation, personalization quality metrics).

**S2. Clean diagnostic methodology.** The core experimental design — comparing intra-modal vs. inter-modal approaches by using modality inversion as a bridge — is elegant. The cross-task control (same OTI-inverted features improve retrieval but hurt classification) is particularly compelling because it rules out the concern that modality inversion inherently improves feature quality.

**S3. Extensive and diverse empirical evaluation.** The experiments span 15+ datasets across image retrieval, text retrieval, and zero-shot classification, with multiple VLM backbones (CLIP, OpenCLIP, SigLIP, SLIP). This breadth convincingly shows that intra-modal misalignment is a general phenomenon, not an artifact of a specific model or dataset.

**S4. Mechanistic analysis of drift (Section 5.4).** The analysis of how OTI-inverted features drift from text manifold to image manifold as optimization progresses, and the connection to cosine similarity distributions, provides a clear mechanistic explanation for why early stopping is necessary and why inter-modal alignment matters.

**S5. Candid limitations section.** The paper acknowledges computational cost (150-1000 steps per query) and the lack of practical alternatives, which sets realistic expectations for applicability.

**S6. Reproducibility focus.** Code is publicly released, all models/datasets are publicly available, random seeds are fixed, and hyperparameters are clearly documented (Appendix A).

## Weaknesses
**W1. Causal over-claim: "solely attributable to inter-modal alignment" (Page 7, Section 5.1).** The paper claims the performance improvement from OTI is "solely attributable to inter-modal alignment" rather than enriched representations. However, OTI's optimization process can act as a soft feature selector, emphasizing discriminative patterns while suppressing noise — a confound not ruled out. A random projection control (mapping ψ_I to text space via a fixed random matrix) is needed to isolate the alignment effect from optimization artifacts.

**W2. Temperature experiment confound (Page 10, Section 5.6).** The high-temperature (τ=1) experiment reduces the modality gap, but the model is also fine-tuned on COCO, which could independently improve intra-modal alignment for COCO-like images. Controls (e.g., fine-tuning on a different dataset like Flickr30K, or manipulating temperature in a lightweight head only) are missing.

**W3. Drift analysis selection bias (Page 9, Section 5.4).** The distribution analysis (Fig. 2c) only shows two snapshots: at the peak performance step (17) and convergence (1000). The claim that OTI features "continuously drift" is supported by only two data points. Additional intermediate steps (50, 100, 500) are needed to show continuous evolution and rule out a sudden switch.

**W4. Practical utility vs. diagnostic value gap.** The paper positions as both a diagnostic study and a practical method, but OTI/OVI are too expensive for real-world deployment (150-1000 steps per query, ~0.2-0.5 seconds per sample). The diagnostic contribution is strong, but the practical claim would be better framed as "demonstration of concept" rather than a deployable solution.

**W5. Variance and significance reporting missing.** None of the main tables (Tables 1-4) include variance estimates, confidence intervals, or significance tests. Many improvements are 1-3%, and some datasets actually show degradation (Aircraft in Table 1: 14.5→14.4). Without statistical testing, readers cannot assess reliability.

**W6. Cross-model degradation variation unanalyzed (Page 8, Table 2 right).** The zero-shot classification degradation varies dramatically across models (1.9 pts for OPEN L/14 vs 8.8 pts for SigLIP). This variation should be correlated with modality gap magnitudes (Table A2) to strengthen the mechanistic claim — currently the authors present it as uniform evidence but do not analyze the heterogeneous pattern.

## Key Issues
### Issue 1 (Major): Causal attribution not fully established [W1, W4]
The central claim that intra-modal improvement is "solely attributable to inter-modal alignment" (Page 7) is overstated. The OTI optimization process could re-weight feature dimensions beyond what inter-modal alignment alone would produce. The Intra-OTI control (Appendix G, Table A8) partially addresses this but does not isolate the alignment effect from the optimization-induced feature selection effect. **Impact on core thesis:** If the improvement partially comes from optimization dynamics rather than alignment, the paper's diagnostic conclusion is weakened.

### Issue 2 (Major): Temperature-modality gap experiment confounded by fine-tuning dataset [W2]
Section 5.6 fine-tunes CLIP on COCO with τ=1.0 to close the modality gap. But fine-tuning on a single dataset (COCO) could independently improve intra-modal alignment for COCO-like images through overfitting, making it unclear whether the reduced OTI benefit is due to modality gap closure or dataset-specific adaptation. **Required control:** Repeat with fine-tuning on a different dataset (e.g., Flickr30K) to show the pattern holds.

### Issue 3 (Major): Drift analysis lacks temporal continuity [W3]
Fig. 2c shows only two optimization steps (17 and 1000) to support the claim that OTI features continuously drift from text manifold to image manifold. Two snapshots cannot distinguish between continuous drift and an abrupt transition near convergence. Adding 3-4 intermediate steps would substantially strengthen this key mechanistic evidence.

### Issue 4 (Medium): Statistical reliability not assessed [W5]
No variance, confidence intervals, or significance tests are reported anywhere in the main tables. Many improvements are 1-3% mAP (e.g., ROxford: 42.6→43.0 for CLIP B/32), and some datasets show degradation (Aircraft: 14.5→14.4). Without statistical evidence, small improvements may not be meaningful.

### Issue 5 (Medium): Hyperparameter sensitivity under-discussed [W4]
OTI's optimal R and OVI's optimal P vary across backbones (Appendix D). The peak performance occurs at only 17 steps for R=4, far from convergence. This sensitivity means the method requires per-dataset tuning, which is expensive and limits practical applicability. The limitations section should explicitly address this.

### Issue 6 (Minor): Cross-model degradation variation unexplained [W6]
The zero-shot classification degradation varies widely (SigLIP: 8.8 pts vs OPEN L/14: 1.9 pts). This heterogeneity, if correlated with modality gap magnitude (Table A2), could strengthen or challenge the paper's claims, but it is not analyzed.

## Actionable Suggestions
### Suggestion 1 (Must): Soften causal claim and add random projection control
**What:** On Page 7 (Section 5.1 results paragraph), the statement "the observed improvement is solely attributable to inter-modal alignment rather than to a more enriched representation" should be softened to "the observed improvement is primarily attributable to inter-modal alignment, though the optimization process may also contribute through feature re-weighting."

**Why:** The current wording implies a level of causal certainty that the experimental design does not support. The OTI optimization process could act as a soft feature selector.

**Add as supporting control:** Compare three feature types: (a) native ψ_I, (b) OTI-inverted ψ_T, (c) **randomly projected** ψ_I → ψ_T' via a fixed random matrix R ∈ R^{d×d} with orthonormal rows, using the same text encoder space. If (b) ≈ (c) > (a), then alignment is the dominant factor. If (b) >> (c), then optimization dynamics contribute meaningfully.

### Suggestion 2 (Must): Deconfound the temperature-modality gap experiment
**What:** Add at least one additional fine-tuning condition where CLIP is fine-tuned on a different dataset (e.g., Flickr30K or Conceptual Captions) at τ=1.0 and τ=0.01, then repeat the image retrieval evaluation.

**Why:** This separates the temperature effect from dataset-specific adaptation effects. If both datasets show the same pattern (no OTI gain at τ=1.0), the modality gap explanation is robust.

### Suggestion 3 (Must): Add intermediate steps to drift analysis
**What:** In Fig. 2c, add OTI-image similarity distributions at 3-4 intermediate optimization steps (e.g., steps 50, 100, 250, 500) using R=4.

**Why:** Two snapshots (steps 17 and 1000) cannot rule out an abrupt transition near convergence. Continuous evolution from text-image matching to image-image matching would substantially strengthen the mechanistic claim.

### Suggestion 4 (Must): Report variance and significance
**What:** For all main tables (Tables 1-4), add either (a) mean±std over 3-5 random seeds, or (b) bootstrapped 95% confidence intervals. For the strongest comparisons (OTI vs baseline), add a paired significance test.

**Why:** Many improvements are small (1-3%), and some datasets show degradation. Without variance, readers cannot assess statistical reliability of the reported gains.

### Suggestion 5 (Nice-to-have): Analyze cross-model degradation heterogeneity
**What:** In Section 5.3, add a correlation analysis between model-wise modality gap magnitude (from Table A2) and classification degradation magnitude (from Table 2 right). Use either a scatter plot or a small table.

**Why:** If the correlation is strong (models with larger gap → more degradation), this independently validates the theoretical connection between modality gap and intra-modal misalignment. If weak, it suggests additional factors exist — either way, the analysis is informative.

### Suggestion 6 (Nice-to-have): Expand limitations section
**What:** Add to the Limitations paragraph (Page 10) a note that OTI/OVI hyperparameters (R, P, S) require tuning per backbone/dataset, and that optimal performance often occurs far from convergence (e.g., step 17 out of 1000 for R=4), making early stopping a critical hyperparameter.

**Why:** This gives readers a realistic understanding of deployment challenges and helps frame the contribution as primarily diagnostic rather than practical.

### Suggestion 7 (Nice-to-have): Clarify Related Work connections
**What:** In each Related Work subsection (Page 3), add one sentence connecting literature gaps to the paper's specific experiments. For example, in the Modality Gap subsection: "While these works characterize the gap's existence, none investigate whether closing it improves intra-modal task performance — we examine this in Section 5.6."

**Why:** This transforms the current list-style summaries into a motivated narrative that strengthens the paper's positioning.

## Storyline Options + Writing Outlines
The current storyline follows: Big Picture (VLMs are successful) → Gap (intra-modal misalignment exists) → Method (OTI/OVI) → Evidence (improvements on 15+ datasets) → Analysis (drift, SLIP, modality gap) → Conclusion. This is functional but can be improved in framing and narrative clarity.

### Storyline Option A (Recommended): Diagnostic-first structure
Organize around the *diagnosis* as the primary contribution, with OTI/OVI as tools rather than methods.

**Abstract Outline (S1-S5):**
- S1: "Pre-trained Vision-Language Models like CLIP are widely used for intra-modal tasks such as image retrieval by directly comparing embeddings from a single encoder."
- S2: "We show this practice is systematically unreliable because CLIP's contrastive loss, which enforces inter-modal (image-text) alignment, imposes no constraints on intra-modal (image-image, text-text) similarity structure."
- S3: "We term this issue intra-modal misalignment and demonstrate it through a novel diagnostic framework: by using optimization-based modality inversion (OTI and OVI) to transform intra-modal tasks into inter-modal ones, we circumvent the misalignment."
- S4: "On over fifteen retrieval datasets and multiple VLM backbones, this inter-modal approach achieves consistent 2-5% mAP gains over intra-modal baselines."
- S5: "Controlled experiments confirm that the improvement stems from exploiting CLIP's inter-modal alignment, and that incorporating intra-modal constraints during pre-training or reducing the modality gap mitigates the problem — though practical mitigation remains an open challenge."

**Introduction Outline (P1-P5):**
- P1 (Motivation): VLMs are foundation models; many applications use CLIP for intra-modal similarity. Establish why intra-modal similarity matters (KNN classification, consistency metrics, retrieval). **Evidence anchor:** Figure 1.
- P2 (Problem): The CLIP loss aligns cross-modal pairs but ignores intra-modal structure. Formalize the modality gap and intra-modal misalignment. Provide the geometric intuition (ψ^1_T, ψ^2_T on hypersphere). **Evidence anchor:** Equation 1 + geometric example.
- P3 (Gap): Prior work has noted related issues (Udandarao et al.; CODER) but only for classification. The phenomenon's full scope — across modalities, tasks, and architectures — is unknown. **Evidence anchor:** Related work paragraph.
- P4 (Solution — diagnostic): We use OTI/OVI to convert intra-modal tasks to inter-modal ones, enabling us to measure the impact of misalignment. Introduce OTI (adapted) and OVI (new). **Evidence anchor:** Sections 4.1-4.2.
- P5 (Contributions): Summarize four contributions as in current paper, but reorder to emphasize diagnostic insight first.

### Storyline Option B: Practical-problem-first structure
Frame around the practical inconvenience of expensive modality inversion, motivating the search for cheaper alternatives (intra-modal loss, temperature manipulation).

### Comparison: Current vs. Option A
| Dimension | Current | Option A |
|---|---|---|
| Entry point | VLMs are popular | Intra-modal similarity is widely used but broken |
| Gap clarity | Mixed into 1st paragraph | Dedicated paragraph (P3) |
| Contribution emphasis | OTI/OVI as methods | Diagnostic insight as primary |
| Readability | Good | Better for non-expert audience |

## Priority Revision Plan
### P0: Required before resubmission (high impact on validity)

| Priority | Item | Action | Expected Impact | Effort |
|---|---|---|---|---|
| P0.1 | Soften causal claim (Section 5.1) | Replace "solely attributable" with "primarily attributable" + add random projection control experiment (Suggestion 1) | Reduces vulnerability to reviewer criticism about confounded causal attribution | Medium |
| P0.2 | Deconfound temperature experiment (Section 5.6) | Add control fine-tuning on Flickr30K/CC3M with τ=1.0 and τ=0.01 (Suggestion 2) | Strengthens the modality gap → misalignment causal chain; addresses a central mechanistic claim | Medium |
| P0.3 | Add intermediate drift analysis steps (Section 5.4, Fig. 2c) | Add OTI-image distribution at steps 50, 100, 250, 500 (Suggestion 3) | Transforms binary snapshot evidence into continuous evolution evidence; strengthens mechanistic story | Low |
| P0.4 | Report variance/significance (Tables 1-4) | Add mean±std over 3 seeds or bootstrapped CI (Suggestion 4) | Enables readers to assess reliability of 1-3% gains; prevents dismissal of results as noise | Medium |

### P1: High priority (strengthens claims)

| Priority | Item | Action | Expected Impact | Effort |
|---|---|---|---|---|
| P1.1 | Analyze cross-model degradation variation (Section 5.3) | Add correlation table: modality gap magnitude vs classification degradation per model (Suggestion 5) | Independently validates (or challenges) the modality gap–misalignment connection | Low |
| P1.2 | Restructure contributions list (Page 3) | Merge C3 and C4 into one; reorder to emphasize diagnostic insight first (see Storyline Option A) | Improves narrative clarity and avoids diluting contributions with confirmatory results | Low |
| P1.3 | Expand Related Work connections (Page 3) | Add one bridging sentence per subsection linking literature to the paper's experiments (Suggestion 7) | Transforms list-style summaries into motivated narrative | Low |

### P2: Nice-to-have (quality improvements)

| Priority | Item | Action | Expected Impact | Effort |
|---|---|---|---|---|
| P2.1 | Expand Limitations (Page 10) | Add note about hyperparameter sensitivity (R, P, early stopping) and per-dataset tuning requirement (Suggestion 6) | Sets realistic expectations for applicability | Low |
| P2.2 | Clarify inter-modal definition (Page 6) | Add clarifying sentence: OTI-image vs image is inter-modal because features come from different encoders | Reduces reader confusion about non-standard terminology | Low |
| P2.3 | Add abstract variance caveat (Page 1) | Qualify "highly suboptimal" with explicit delta range: "2-3% mAP improvement across 15+ datasets" | Prevents overclaim perception | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Image-to-image retrieval: OTI improves over intra-modal baseline | 15 datasets, 5 VLMs, OTI (R=1, 150 steps) | mAP | +2-3% avg improvement | C1, C2 | No variance reported; one dataset (Aircraft) shows degradation |
| E2 | Text-to-text retrieval: OVI improves over intra-modal baseline | Flickr30K, COCO, nocaps; 5 VLMs; OVI (P=1-4, 1000 steps) | mAP | +1-5% improvement | C1, C2 | Text-only datasets require LLM summarization (Appendix G); introduces confound |
| E3 | Zero-shot classification: OTI degrades inter-modal task | 11 datasets, 5 VLMs; same OTI features as E1 | Accuracy | -3 to -9 pts degradation | C1 (diagnostic) | Degradation varies 2x-4x across models, unanalyzed |
| E4 | Modality inversion drift analysis (OTI) | Cars dataset, CLIP B/32; vary R and steps | L_cos, mAP, cosine sim distributions | Drift from text to image manifold as steps increase | C2 (mechanism) | Only 2 snapshots in Fig. 2c; no continuous evolution |
| E5 | SLIP intra-modal loss analysis | SLIP B/16, L/16; 15 datasets; OTI | mAP | OTI ≈ baseline (no gain) | C3 | SLIP is only one model with intra-modal loss; no SigLIP variant tested |
| E6 | Modality gap temperature experiment | CLIP B/32 fine-tuned on COCO with τ=1.0 and τ=0.01 | mAP on 5 datasets | No OTI gain at τ=1.0 | C3 | Confounded by COCO fine-tuning; single dataset |
| E7 | Adapter-based modality inversion (Appendix G) | Single-layer linear adapter trained on LLaVA-CC3M | mAP | Adapter improves but less than OTI/OVI | C2 (ablation) | Adapter requires training data; OTI/OVI require optimization |
| E8 | Captioning-based modality inversion (Appendix G) | DeCap, CoCa (LAION), CoCa (COCO) | mAP | Captioning fails (mAP ~2-16%) | C2 (negative control) | Captions lack discriminative detail for fine-grained retrieval |
| E9 | Intra-OTI control (Appendix G) | OTI applied to both query and gallery | mAP | Worse than inter-modal OTI | C2 (mechanism) | Does not isolate alignment from optimization effects |
| E10 | OVI on purely textual datasets (Appendix G) | 9 datasets from NanoBEIR + IMDB + 20News; Llama summarization | mAP | +7% avg improvement | C1, C2 | LLM summarization introduces a strong confound (summary quality affects results) |

### Research-Theme Gap Diagnosis
The paper's three research-value claims — new knowledge about intra-modal misalignment (C1), methodological framework for mitigation (C2), and understanding of factors that affect misalignment (C3) — are unevenly supported:
- **C1 (new knowledge)** is the strongest claim, well-supported by consistent cross-model/cross-task evidence.
- **C2 (methodological framework)** is a diagnostic tool rather than a practical solution; OTI/OVI are too expensive for deployment.
- **C3 (factors)** is partially supported but the temperature experiment has a confound, and the SLIP analysis is limited to one model.

### Proposed Research Experiments (P0/P1/P2)

| Experiment | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Success Criterion | Est. Effort |
|---|---|---|---|---|---|---|
| **P0.1: Random projection control** | C2 (alignment vs optimization) | If inter-modal alignment is the dominant cause of OTI gains, a random projection to text space should also improve performance | Replace OTI with random orthonormal matrix R∈R^{d×d}; compute ψ_T' = R·ψ_I; evaluate on 5 retrieval datasets | Intra-modal baseline, OTI baseline | Random projection outperforms intra-modal baseline, even if less than OTI | 1-2 GPU hours |
| **P0.2: Multi-dataset temperature control** | C3 (modality gap → misalignment) | If temperature-induced gap closure (not dataset adaptation) causes reduced OTI benefit, pattern should hold across datasets | Fine-tune CLIP B/32 on Flickr30K with τ=1.0 and τ=0.01; evaluate same 5 datasets as Table 4 | COCO fine-tuned models from current paper | Both datasets show same pattern: no OTI gain at τ=1.0 | 4-6 GPU hours |
| **P1.1: Intermediate drift steps** | C2 (mechanism: continuous drift) | OTI-image similarity distribution evolves continuously from text-image matching to image-image matching | Extract OTI-inverted features at steps 50, 100, 250, 500 (R=4); plot cosine similarity distributions (like Fig. 2c) | Steps 17 and 1000 from current paper | Distributions show gradual shift, not abrupt transition | Minimal |
| **P1.2: Modality gap–degradation correlation** | C1 (misalignment diagnostic) | Model-level modality gap magnitude (Table A2) positively correlates with classification degradation (Table 2 right) | Compute per-model gap magnitude and degradation; produce scatter plot and Pearson r | N/A | r > 0.5 with p < 0.1 (given small N=5 models) | Minimal |
| **P2.1: Statistical significance package** | All claims | 1-3% gains are significant above noise | Repeat 3 key experiments (image retrieval, text retrieval, classification) with 3 seeds each; report mean±std | Current single-seed results | Gains remain positive for >80% of datasets with non-overlapping CI | 8-12 GPU hours |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### ASCII Diagrams

**ASCII Diagram A — Paper Structure & Evidence Map**

```text
[Core Claim: Intra-modal CLIP similarities are suboptimal due to intra-modal misalignment]
    |
    ├── Evidence 1: Image retrieval improves 2-3% mAP via inter-modal OTI (Table 1)
    │   └── Gap: No variance/CI reported; small gains may not be significant
    │
    ├── Evidence 2: Text retrieval improves 1-5% mAP via inter-modal OVI (Table 2 left)
    │   └── Gap: LLM summarization confound for text-only datasets
    │
    ├── Evidence 3: Same OTI features degrade classification (Table 2 right)
    │   └── Strongest diagnostic evidence; but 2x-4x variation across models unanalyzed
    │
    ├── Evidence 4: Drift analysis (Fig 2) — OTI at peak matches text-image distribution
    │   └── Gap: Only 2 snapshots; selection bias risk
    │
    ├── Evidence 5: SLIP intra-modal loss eliminates OTI gain (Table 3)
    │   └── Gap: Only one model tested (SLIP)
    │
    └── Evidence 6: τ=1.0 closes gap, eliminates OTI gain (Table 4)
        └── Gap: Confounded by COCO fine-tuning
```

**ASCII Diagram B — Revision Strategy Roadmap**

```text
[Current manuscript]
    |
    ├── Issue 1: "Solely attributable" overclaim
    │   └── Fix: Soften wording + random projection control experiment
    │       └── Expected: Claim becomes defensible, still strong
    |
    ├── Issue 2: Temperature experiment confound
    │   └── Fix: Add Flickr30K fine-tuning control
    │       └── Expected: Causal chain robustly established
    |
    ├── Issue 3: Drift analysis limited to 2 snapshots
    │   └── Fix: Add intermediate steps 50, 100, 250, 500
    │       └── Expected: Continuous evolution demonstrated
    |
    └── Issue 4: No variance reporting
        └── Fix: Add 3-seed std or bootstrapped CI
            └── Expected: Statistical reliability assessable
```

**ASCII Diagram C — Related-Work Taxonomy Tree (Layered)**

```text
Related Work (Root: Intra-modal misalignment in CLIP-style VLMs)
├── Branch 1: Contrastive Vision-Language Models
│   ├── Leaf 1.1: Standard contrastive (CLIP, SigLIP)
│   │   └── Inter-modal loss only; no intra-modal constraints
│   └── Leaf 1.2: Intra-modal enhanced (SLIP, Li et al.)
│       └── Adds intra-modal loss; reduces misalignment
│
├── Branch 2: Modality Gap Analysis
│   ├── Leaf 2.1: Origin & characterization (Liang et al., Shi et al.)
│   │   └── Gap from initialization + contrastive loss
│   ├── Leaf 2.2: Dimensional analysis (Schrodi et al.)
│   │   └── Minimal dimensions suffice to separate modalities
│   └── Leaf 2.3: Diagnostic/rectification (Zhang et al.)
│       └── Language-based diagnosis of vision models
│
└── Branch 3: Intra-modal Misalignment Mitigation
    ├── Leaf 3.1: Classification-specific (Udandarao et al., CODER/Yi et al.)
    │   └── Image-text space similarities; limited to classification
    └── Leaf 3.2: Modality inversion (This paper: OTI/OVI)
        └── General diagnostic framework; single-feature level; no external data
```

**This paper's contribution** sits in Branch 3, Leaf 3.2, extending beyond prior classification-only work (Leaf 3.1) to a general diagnostic framework spanning retrieval tasks, both modalities, and multiple backbones. The primary novelty is the *demonstration framework* rather than a deployable method.

**ASCII Diagram D — Experiment Upgrade Plan**

```text
Stage 1 (P0 — before resubmission):
├── Random projection control → isolates alignment effect
├── Multi-dataset temperature control → deconfounds modality gap experiment
├── Intermediate drift steps → continuous evolution evidence
└── Statistical variance reporting → reliability assessment

Stage 2 (P1 — high priority):
├── Modality gap–degradation correlation → independent validation
├── Restructure contributions → narrative clarity
└── Related Work connections → motivated narrative

Stage 3 (P2 — quality polish):
├── Expanded Limitations → realistic expectations
├── Clarify inter-modal definition → reader clarity
└── Abstract variance caveat → prevents overclaim perception
```

### Page Coverage Audit

| Page | Section | Annotations Count | Status | Skip Reason (if any) |
|---|---|---|---|---|
| 1 | Abstract + Introduction (P1) | 2 | Covered | — |
| 2 | Introduction (P2-P5) + Figure 1 | 1 | Covered (Fig 1 is visual aid) | — |
| 3 | Contributions + Related Work + "Our contribution" | 2 | Covered | — |
| 4 | CLIP Preliminaries (Eq. 1, geometric intuition) | 1 | Covered | — |
| 5 | Modality Inversion (OTI, OVI) | 1 | Covered | — |
| 6 | OVI details (Eq. 3) + Experimental setup | 1 | Covered | — |
| 7 | Image retrieval results (Table 1) | 1 | Covered | — |
| 8 | Text retrieval + Zero-shot classification (Table 2) | 1 | Covered | — |
| 9 | Drift analysis (Fig 2) | 1 | Covered | — |
| 10 | SLIP experiment (Table 3) + Modality gap + Conclusion | 3 | Covered | — |
| 11-14 | References + Appendix A/B | 0 | Skipped | Boilerplate: references only |
| 15-22 | Appendices C-G | 0 | Covered via inline annotations | Annotations reference appendix content where relevant |

### Final Score

**Final Score: 6.5/10**

**Rationale:** The paper addresses a genuinely important and under-appreciated problem with a clean diagnostic methodology and extensive empirical validation. The core insight — that CLIP intra-modal similarities are systematically unreliable — is well-supported and practically significant. However, the score is constrained by: (1) overclaimed causal attribution ("solely attributable") that is not fully supported by the experimental design; (2) a confound in the key temperature experiment that weakens the mechanistic claim; (3) lack of statistical variance reporting for small-margin improvements; and (4) the limited practical utility of OTI/OVI for real deployment. The novelty is moderate: the intra-modal misalignment concept is clearly articulated but partially overlaps with known modality gap literature, and the diagnostic methodology (modality inversion) is adapted from existing work (OTI). The primary contribution is empirical characterization rather than a new algorithm.

**Post-Revision Target: [7.5, 8.5]/10**

If the authors address the four P0 items (soften causal claim + random projection control, deconfound temperature experiment, add intermediate drift steps, add variance reporting), the paper's claims become defensible and the evidence base becomes substantially stronger. The research value would still be primarily diagnostic rather than practical, but a well-executed diagnosis with rigorous causal evidence is publishable at a top venue.