## Summary
# Final Review Report

## Summary

This paper investigates racial and gender biases in Stable Diffusion XL (SDXL), a widely used text-to-image generative model. The authors make four main contributions: (1) a race/gender classifier (MTCNN + VGGFace + SVM) achieving 73% accuracy on FairFace; (2) a large-scale bias audit across 6 races, 2 genders, 32 professions, and 8 attributes, revealing substantial demographic skews (e.g., 47% White, 65% male) and harmful stereotypes (e.g., associating Middle Eastern faces with terrorism, Black faces with crime); (3) two debiasing solutions—SDXL-Inc (a LORA-fine-tuned ensemble of 12 race-gender-specific models for balanced demographic representation) and SDXL-Div (a diversity-oriented fine-tuned model for reducing intra-race homogenization); and (4) four preregistered user studies (N=135 each) showing that exposure to inclusive AI-generated faces reduces participants' demographic bias estimates, while non-inclusive faces increase them.

**Core strengths:** Large-scale systematic bias documentation across more demographic/professional categories than prior work; direct comparison of model biases against training data (LAION-5B); debiasing solutions with generalization evaluation; the RCT component is a novel methodological contribution to the text-to-image fairness literature.

**Core weaknesses:** The race/gender classifier is only 73% accurate with substantial per-group variation (Latinx recall=58%), creating uncertainty in all downstream measurements; the SDXL-Inc evaluation may have circularity issues (trained on SDXL-generated images, evaluated by the same classifier pipeline); the user studies face demand characteristics; the Discussion over-extrapolates from short-term estimation shifts to broad societal-attitude claims; and "state-of-the-art" classifier claims are based on a marginal 1% advantage over baselines.

## Strengths
**S1. Large-scale, multi-dimensional bias documentation.** The paper systematically audits SDXL across 6 races, 2 genders, 32 professions, and 8 attributes with 10,000 images per condition, making it one of the most comprehensive bias audits of a text-to-image model to date. The inclusion of racial homogenization analysis (intra-race cosine similarity) adds a novel measurement dimension beyond simple demographic counting.

**S2. Comparison of model biases against training data.** By analyzing a subset of LAION-5B (the dataset used to train SDXL) and comparing its demographic distribution against SDXL output distributions, the paper provides evidence that some biases are exacerbated by the model itself rather than simply inherited from training data. This is a valuable methodological contribution to the bias attribution literature.

**S3. Debiasing solutions with generalization testing.** The paper proposes two debiasing solutions (SDXL-Inc for demographic balance, SDXL-Div for intra-race diversity) and evaluates generalization on held-out professions and attributes not seen during fine-tuning. The comparison against ITI-GEN (Appendix D) demonstrates practical advantages in complex-prompt settings.

**S4. Preregistered randomized controlled trials.** The four user studies (N=135 each, preregistered at AsPredicted) provide a rigorous methodological framework for testing whether exposure to AI-generated faces can influence people's demographic estimates. This is a novel approach in the text-to-image fairness literature and opens a new research direction.

**S5. Transparent reporting of confidence intervals, p-values, and statistical tests.** The user study results include detailed statistical reporting with appropriate test selection (t-test vs. Mann-Whitney U based on normality checks), and the box plots provide clear visual communication of distributions.

**S6. Ethical motivation and societal relevance.** The paper addresses a timely and important topic with significant real-world implications, as text-to-image models are increasingly used in media, advertising, and content creation. The open-access release of the debiased models would be a practical contribution to the community.

## Weaknesses
**W1. Classifier accuracy limitations undermine measurement reliability.** The race classifier achieves only 73% accuracy on FairFace, with substantial per-group variation (Asian recall=93%, Latinx recall=58%). Since all downstream bias measurements (profession distributions, attribute associations, homogenization analysis, SDXL-Inc evaluation) depend on this classifier, the error rates introduce systematic measurement uncertainty that is not adequately quantified or discussed.

**W2. Circularity in SDXL-Inc training and evaluation.** SDXL-Inc is trained on SDXL-generated images and evaluated using a classifier (VGG-Face+SVM) trained on real images. The claim that SDXL-Inc produces "inclusive" images is thus a statement about classifier agreement rather than verified demographic diversity. Without human validation of the generated images' perceived demographics, the debiasing claim rests on a single imperfect classifier.

**W3. User study demand characteristics.** The within-subjects design (view 6 homogeneous/heterogeneous images, then immediately estimate a relevant demographic percentage) is transparent to participants, creating demand characteristics. Participants can easily infer the study's purpose and adjust responses accordingly.

**W4. Missing intersectional analysis.** Race and gender are analyzed as separate dimensions. The paper does not examine joint race×gender distributions (e.g., Black women vs. Black men in each profession), missing a well-established fairness framework (intersectionality).

**W5. Overclaimed societal impact in Discussion.** The Discussion extrapolates from short-term percentage estimation shifts in a 6-image exposure experiment to broad claims about "shaping societal attitudes," "normalization of gender stereotypes," and causing "feelings of alienation." These causal claims are not supported by the study design.

**W6. "State-of-the-art" classifier claim is overstated.** The 73% accuracy represents a marginal 1% improvement over FairFace's ResNet34 (72%), without statistical significance testing. The comparison may be unfair, as the proposed method starts from a pre-trained VGGFace embedding (3.31M images) while competitors were trained from scratch.

**W7. Incomplete statistical reporting.** The user studies report p-values but not effect sizes (Cohen's d). Multiple comparisons across four studies and multiple conditions are not corrected. The Study 1 null result (non-inclusive images not increasing bias) is reported without explanation.

**W8. Missing limitation section.** The paper has no dedicated Limitations section. Important caveats—classifier accuracy limitations, demand characteristics, external validity constraints, the (if it exists) hedging contradiction in the introduction—are not discussed.

## Key Issues
### Issue 1 (Severity: Major) — Classifier accuracy creates fundamental uncertainty in all measurements
- **Evidence:** The race classifier has 73% accuracy on FairFace. Latinx recall is 58%; Middle Eastern recall is 61%. The confusion matrix (Appendix Figure 9a) shows systematic misclassifications: Latinx → White (14%), Middle Eastern → White (20%), Indian → Latinx (11%).
- **Impact:** All bias measurements—profession distributions (Section 4.3), attribute analysis (Section 4.4), SDXL-Inc evaluation (Figure 1, 3a-3c), SDXL-Div evaluation (Figure 4)—depend on this classifier. Systematic misclassifications will propagate errors differentially across racial groups. For example, if Latinx faces are frequently misclassified as White, the reported "White dominance" in professions is inflated.
- **Verification status:** [Partially proven] — classifier accuracy is reported but the impact of misclassification on downstream measurements is not quantified.
- **Required action:** Add a sensitivity analysis: (1) report the expected misclassification rate per race conditional on the confusion matrix; (2) compute upper/lower bounds on reported percentages using classifier confidence intervals; (3) provide a subset of images with human-verified labels to validate the key results.

### Issue 2 (Severity: Major) — SDXL-Inc evaluation circularity
- **Evidence:** SDXL-Inc is fine-tuned on SDXL-generated images (using explicit race+gender+profession prompts) and evaluated by a classifier trained on real images. The evaluation shows that SDXL-Inc outputs have more uniform classifier-assigned race/gender distributions.
- **Impact:** The evaluation confirms that the fine-tuning successfully modifies the classifier's perception of the generated images. Whether this corresponds to genuine demographic diversity in the generated faces is unverified because (a) the classifier has only 73% accuracy, (b) the training data for SDXL-Inc used the same race categories as the classifier, creating a closed loop.
- **Verification status:** [Partially proven] — the circularity is a structural concern rather than an empirical error.
- **Required action:** Add a human evaluation study (at minimum, 50 raters label race/gender for 200 images from SDXL vs. SDXL-Inc) to validate that debiasing is perceptual, not just classifier-level.

### Issue 3 (Severity: Major) — User study demand characteristics and causal overclaim
- **Evidence:** Studies 1-2 present 6 images (all the same race/gender vs. one of each) then ask participants to estimate real-world percentages. This experimental design is transparent to participants, who may adjust responses to align with perceived expectations. The Discussion then extrapolates to "shaping societal attitudes," "normalization of stereotypes," and psychological harm without evidence.
- **Impact:** The core RCT finding—that inclusive images "reduce people's racial and gender biases"—is overstated. The study measures short-term estimation shifts, not bias reduction. The societal-impact claims in the Discussion go far beyond what the data supports.
- **Verification status:** [Partially proven]
- **Required action:** (1) Add a limitations paragraph explicitly discussing demand characteristics; (2) replace "reduces people's bias" with "shifts demographic estimates" throughout; (3) substantially temper Discussion claims.

### Issue 4 (Severity: Major) — Missing intersectional analysis
- **Evidence:** Section 4.3 reports race distributions and gender distributions separately for each profession, but never reports the joint distribution (e.g., % Black women vs. % Black men among Doctors).
- **Impact:** The most insidious stereotypes are intersectional (e.g., Asian women as nurses, White men as executives). By reporting race and gender separately, the paper misses its best opportunity to reveal compounded biases. This is a well-established framework in fairness research (Crenshaw 1989, Buolamwini & Gebru 2018).
- **Verification status:** [Proven] — readily observable from existing data; no new data needed.
- **Required action:** Add an intersectional analysis table for at least 8-12 key professions.

### Issue 5 (Severity: Minor) — Introduction gap paragraph contradictions
- **Evidence:** Page 1, Intro paragraph 2: (a) Claims "none of these studies proposed debiasing solutions" but then cites debiasing solutions (Zhang et al., Friedrich et al.); (b) states racial homogenization "has been overlooked" without citation support; (c) hedges "(if it exists)" after asserting the problem exists.
- **Impact:** Weakens the credibility of gap identification at the most critical positioning point.
- **Verification status:** [Proven]
- **Required action:** Restructure to: (i) prior bias measurement work lacked scope/debiasing; (ii) existing debiasing solutions have specific limitations; (iii) racial homogenization has not been systematically quantified; (iv) remove "(if it exists)."

## Actionable Suggestions
### Suggestion 1 (Must) — Add classifier sensitivity analysis and uncertainty bounds
Add a dedicated analysis that propagates classifier uncertainty into all downstream measurements. For each reported race/gender percentage, compute and report:
- The confusion-matrix-conditional expected value and 95% confidence interval.
- Upper/lower bounds assuming worst-case misclassification patterns.

**Where:** Append classifier uncertainty subsection after Section 4.1.

### Suggestion 2 (Must) — Add human validation of SDXL-Inc outputs
Conduct a small-scale human evaluation study where raters (N=50) label perceived race and gender from 200 images (100 SDXL, 100 SDXL-Inc, drawn from the profession-neutral prompt). Compare classifier-assigned vs. human-assigned distributions.

**Expected benefit:** Validates that SDXL-Inc's debiasing is perceptual, not just a classifier artifact. If human labels confirm the balanced distribution, this would substantially strengthen the paper.

**Cost estimate:** ~2 hours of effort for 200 image labeling × 50 raters on Prolific (~$300).

### Suggestion 3 (Must) — Temper Discussion claims and add Limitations section
- Replace "reduces people's racial and gender biases" with "shifts participants' demographic percentage estimates" throughout abstract, introduction, and discussion.
- Remove or substantially qualify speculative claims about "societal attitudes," "normalization of stereotypes," and "feelings of alienation."
- Add a dedicated Limitations subsection covering: classifier accuracy limitations, demand characteristics (user studies), single-model analysis (SDXL only), US-only participant pool, short exposure duration.

### Suggestion 4 (Must) — Add intersectional race×gender analysis
Using the existing data, compute and report the joint race×gender distribution for each profession (or a representative subset of 12 professions). Present as a stacked bar chart or heatmap with 12 categories (6 races × 2 genders).

### Suggestion 5 (Nice-to-have) — Report effect sizes and multiple-testing correction
Add Cohen's d for all pairwise comparisons in the user studies. Apply a Bonferroni or Holm correction for the 4 studies × multiple conditions. Report which comparisons survive correction.

### Suggestion 6 (Must) — Fix Introduction gap contradictions
Restructure the second Introduction paragraph to clearly distinguish:
- What prior bias measurement studies did and what they missed.
- Where prior debiasing solutions fall short.
- Why racial homogenization is a distinct, understudied problem.
- Remove "(if it exists)" hedging.

### Suggestion 7 (Nice-to-have) — Add cosine similarity distribution analysis for SDXL-Div
Report full histograms (not just means) of cosine similarity values for SDXL vs. SDXL-Div. Control for background confounds by computing similarity on face-cropped regions only.

### Suggestion 8 (Nice-to-have) — Restructure Related Work into thematic subsections
Three subsections: (1) Bias measurement in text-to-image models, (2) Debiasing approaches, (3) Human perception of AI-generated content. This makes the novelty positioning clearer than the current paper-by-paper summary format.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current narrative arc is: AI bias examples (4 examples) → SDXL focus → gap statement (debiasing, homogenization, human impact) → classifier → bias audit → debiasing (SDXL-Inc) → diversity (SDXL-Div) → user studies → discussion.

**Problem:** The first Introduction paragraph (4 AI bias examples) delays the paper's focus on text-to-image models by 13 lines, and the transition to SDXL-specific content is abrupt.

### Abstract Outline (Final, Copy-Ready)

**S1 (Problem):** "Text-to-image generative models such as Stable Diffusion are used daily by millions worldwide, yet the extent to which they exhibit racial and gender stereotypes is not fully understood."

**S2 (Gap):** "Prior work has documented demographic biases in earlier Stable Diffusion versions but has not examined biases across multiple races and professions simultaneously, has not quantified intra-racial homogenization, has not proposed automated debiasing solutions, and has not tested whether exposure to AI-generated faces can shape human perceptions."

**S3 (Method):** "Here, we introduce a race/gender classifier (73% accuracy on FairFace) and audit SDXL across 6 races, 2 genders, 32 professions, and 8 attributes. We further propose two debiasing solutions: SDXL-Inc for balanced demographic representation and SDXL-Div for reducing intra-race homogeneity."

**S4 (Key Result):** "We find that SDXL-generated faces are predominantly White (47%) and male (65%), and exhibit profession-specific stereotypes (e.g., 90%+ male for doctors and professors). Racial homogenization is particularly severe for Middle Eastern and Latinx individuals."

**S5 (Impact):** "In four preregistered experiments (N=135 each), we show that exposure to inclusive AI-generated faces shifts participants' demographic percentage estimates toward ground-truth values, while non-inclusive faces shift them away—an effect that persists regardless of whether images are labeled as AI-generated. These findings highlight the dual role of AI as both a potential amplifier and mitigator of demographic biases."

### Introduction Outline (Revised Storyline)

**Paragraph 1 (P1) — Problem and Stakes (2-3 sentences):** 
"Text-to-image generative models are used by millions daily to create visual content for media, advertising, and design. However, these models can perpetuate harmful racial and gender stereotypes if their training data or architecture embeds demographic biases."

**Paragraph 2 (P2) — Specific Gap (4-5 sentences):**
"Prior work has demonstrated that Stable Diffusion underrepresents certain races and genders (Bianchi et al., Ghosh & Caliskan, Wang et al.). However, three gaps remain: (1) no prior study has simultaneously examined biases across a broad set of races (6), professions (32), and attributes (8); (2) the phenomenon of racial homogenization—where same-race individuals are depicted as visually similar—has not been systematically quantified; and (3) no existing work has proposed an automated debiasing solution for SDXL and tested whether debiased AI-generated images can influence human perceptions."

**Paragraph 3 (P3) — Our Approach (3-4 sentences):**
"To address these gaps, we develop a race/gender classifier, conduct the largest-scale bias audit of SDXL to date, and propose two fine-tuned debiasing models (SDXL-Inc and SDXL-Div). We then test the real-world relevance of AI-generated biases through four preregistered randomized controlled trials."

**Paragraph 4 (P4) — Contributions (2-3 sentences):**
"Our paper makes four contributions: (i) a systematic bias audit across 6 races, 2 genders, 32 professions, and 8 attributes; (ii) documentation and quantification of racial homogenization in AI-generated faces; (iii) two debiasing solutions with demonstrated effectiveness and generalization; and (iv) evidence that AI-generated faces can shift demographic perceptions in controlled experiments."

### Alternative Storyline Candidates

**Alternative A — "Impact-first":** Start with the user study finding ("Can AI-generated faces change how people perceive racial and gender distributions?"), then work backward to the bias audit and debiasing. This would increase engagement but risks feeling gimmicky.

**Alternative B — "Problem-first with single hook":** Open with a single striking example of AI bias (e.g., the Cleaner/Doctor racial disparity), use it to motivate the systematic audit, then propose solutions, then test human impact. This would be more focused than the current multi-example opening.

**Chosen storyline:** Alternative B (single-hook opening) is recommended as it is the most reader-friendly while preserving scientific depth. The current version's first paragraph can be reduced from 4 examples to 1-2 tightly connected examples.

## Priority Revision Plan
### P0 (Critical — Must Fix Before Resubmission)

| Priority | Task | Affected Section | Effort | Expected Impact |
|----------|------|------------------|--------|-----------------|
| P0.1 | Add classifier sensitivity analysis with uncertainty bounds on all reported percentages | Sections 4.1-4.5, Appendix | 2-3 days | Quantifies measurement reliability; addresses the most fundamental methodological concern |
| P0.2 | Add human validation study for SDXL-Inc outputs (200 images, 50 raters) | Section 4.4 | 1-2 days, ~$300 | Validates debiasing is perceptual, not just classifier-level |
| P0.3 | Temper Discussion claims; add Limitations subsection | Section 5 | 0.5 day | Brings claims in line with evidence; preempts reviewer pushback |
| P0.4 | Fix Introduction gap paragraph contradictions | Section 1, Paragraph 2 | 0.5 day | Corrects logical inconsistency at the most visible positioning point |
| P0.5 | Add intersectional race×gender analysis | Section 4.3 / Appendix | 1 day | Reveals compounded biases; addresses a well-established fairness framework gap |

### P1 (High Priority — Should Fix)

| Priority | Task | Affected Section | Effort | Expected Impact |
|----------|------|------------------|--------|-----------------|
| P1.1 | Report effect sizes (Cohen's d) for user study comparisons | Section 4.6 | 0.5 day | Allows readers to assess practical significance |
| P1.2 | Add multiple comparison correction for user studies | Section 4.6 | 0.5 day | Reduces false positive risk |
| P1.3 | Restructure Related Work into thematic subsections | Section 2 | 1 day | Improves novelty positioning |
| P1.4 | Replace "state-of-the-art" with bounded claim for classifier | Section 4.1 / Appendix C | 0.5 day | Avoids overclaiming on marginal 1% advantage |

### P2 (Nice-to-Have — Quality Improvement)

| Priority | Task | Affected Section | Effort | Expected Impact |
|----------|------|------------------|--------|-----------------|
| P2.1 | Add cosine similarity histograms and face-cropped control for SDXL-Div | Section 4.5 | 1 day | Strengthens homogenization analysis |
| P2.2 | Discuss Study 1 null result (non-inclusive images not increasing racial bias) | Section 4.6 / 5 | 0.5 day | Improves theoretical completeness |
| P2.3 | Fix typos: "assassination" → "association" (p.10), "as well as the of the two" (p.4) | Various | 0.2 day | Professional polish |
| P2.4 | Add LAION-5B sampling details and keyword-filtering bias discussion | Section 3.1 / 4.2 | 0.5 day | Improves reproducibility |

### Revision Sequence (Recommended Order)

```text
Stage 1 (Textual Corrections — ~0.5 day):
  - Fix Introduction gap paragraph contradictions
  - Fix typos
  - Temper Discussion claims
  - Replace "state-of-the-art" with bounded claim

Stage 2 (Analysis Additions — ~3-4 days):
  - Run classifier sensitivity analysis
  - Run human validation study (Prolific)
  - Compute intersectional race×gender distributions
  - Compute effect sizes and multiple comparison corrections
  - Add cosine similarity histograms

Stage 3 (Structural Improvements — ~2 days):
  - Restructure Related Work
  - Add Limitations subsection
  - Add discussion of Study 1 null result
  - Add LAION-5B sampling details

Stage 4 (Final Polish — ~0.5 day):
  - Re-check all claims against evidence
  - Ensure abstract and conclusion are consistent with tempered claims
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Classifier development & validation | FairFace training (86,744) + validation (10,954); MTCNN detection → VGGFace embedding → SVM | Accuracy, Precision, Recall, F1 | 73% race accuracy, 94% gender accuracy | Race/gender classifier is viable for SDXL audit | 73% accuracy with high per-class variance (Latinx recall=58%); "SOTA" claim overstated |
| E2 | SDXL demographic distribution (neutral prompt) | 10,000 images "a photo of a person"; classifier-assigned race/gender | Race/gender percentages | 47% White, 33% Black, 3% Asian; 65% male | SDXL exhibits strong demographic skew | Only one prompt tested; classifier errors propagate |
| E3 | LAION-5B distribution comparison | 88,714 face images from LAION-5B subset | Race/gender percentages | White 63% LAION vs 47% SDXL; Gender balanced in LAION, male-skewed in SDXL | SDXL biases not fully attributable to training data | 0.002% sample of LAION-5B; keyword filtering bias; single sample |
| E4 | Professional stereotype audit | 320,000 images (10K×32 professions); SDXL | Race/gender percentages per profession | White majority in 21/24 professions; 90%+ male in 16 professions | SDXL exhibits profession-specific stereotypes | Race/gender analyzed separately (no intersectional analysis) |
| E5 | Attribute stereotype audit | 80,000 images (10K×8 attributes); SDXL | Race distribution per attribute | White→success/beauty; Middle Eastern→terrorism; Black→crime/poverty | Harmful attribute-race associations exist | No human perception validation; demand characteristics in user study |
| E6 | SDXL-Inc debiasing evaluation | 10,000 images per model (SDXL vs SDXL-Inc); same neutral prompt | Race/gender percentages; σ across groups | Near-uniform race/gender distribution; σ reduction | SDXL-Inc effectively debiases SDXL | Circular evaluation (trained on SDXL, classified by same pipeline); no human validation |
| E7 | SDXL-Inc generalization (held-out professions) | 8 professions (4 fine-tuned, 4 held-out) | Race distribution per profession | σ reduction in both fine-tuned and held-out | SDXL-Inc generalizes beyond training professions | Small held-out set (4 professions); one-shot evaluation |
| E8 | SDXL-Inc generalization (attributes) | 8 attributes (not seen in fine-tuning) | Race distribution per attribute; σ | σ reduced from ~32 to ~3 on average | SDXL-Inc generalizes to unseen attributes | Only 8 attributes; no human evaluation of attribute relevance |
| E9 | SDXL-Div homogenization reduction | ~10,000 images per race per model (SDXL vs SDXL-Div); VGGFace cosine similarity | Mean pairwise cosine similarity per race | Cosine similarity reduced for all races (e.g., Middle East: 0.61→0.41) | SDXL-Div increases intra-race facial diversity | Cosine similarity confounded by background/lighting; no face-only control analysis |
| E10 | SDXL-Inc vs ITI-GEN comparison | 1,200 images per model × 5 complex prompts | Race/gender percentages; accuracy/recall/precision | SDXL-Inc outperforms ITI-GEN on all metrics and prompts | SDXL-Inc is more robust for complex prompts | Small sample size (200 images per race per prompt); single ITI-GEN training seed |
| E11 | User Study 1 (Racial bias) | N=135 per condition; 6 images (SDXL-all-White vs SDXL-Inc-balanced); Q1: % White in profession | Participant percentage estimate; box plots w/ p-values | Inclusive images reduce White-% estimate vs baseline; non-inclusive show mixed results (Q1 null) | Exposure to inclusive AI faces shifts demographic estimates | Demand characteristics; no effect sizes; no multiple comparison correction; Q1 null unexplained |
| E12 | User Study 2 (Gender bias) | Same design as E11 but professions and Q2 (% men) | Participant percentage estimate; box plots w/ p-values | Inclusive images reduce male-% estimate; non-inclusive increase it | Same as E11 for gender | Same limitations as E11 |
| E13 | User Study 3 (Homogenization - men) | 6 Middle Eastern men images (SDXL-all-bearded vs SDXL-Div-varied); Q3: % bearded | Participant percentage estimate | Inclusive images reduce beard-% estimate | AI-generated stereotypes affect homogenization perception | Only Middle Eastern faces tested; single attribute (beard); 6 images only |
| E14 | User Study 4 (Homogenization - women) | 6 Middle Eastern women images (SDXL-all-headcover vs SDXL-Div-varied); Q4: % wearing headcover | Participant percentage estimate | Inclusive images reduce headcover-% estimate | Same as E13 | Same as E13; headcover as sole attribute |

### Research-Theme Gap Diagnosis

**Gap 1 — New Knowledge (partially addressed):** The paper adds substantial empirical knowledge about SDXL's biases but the fundamental measurement tool (classifier) has limited accuracy. The most novel findings (racial homogenization, human impact of inclusive faces) are also the ones most constrained by measurement uncertainty and experimental demand characteristics.

**Gap 2 — Reproducibility (partially addressed):** Data generation procedures are well-documented (prompts, sample sizes, hyperparameters), but the classifier training details (exact layer for embedding extraction) and LAION-5B sampling procedure are underspecified.

**Gap 3 — Impact on Practice/Understanding (partially addressed):** The user studies provide initial evidence that inclusive AI-generated images can shift demographic estimates. However, the gap between 6-image exposure and real-world attitudinal change remains large and unaddressed.

### Proposed Research Experiments (P0/P1/P2)

| Experiment | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Quality Gain |
|------------|-------------|------------|---------------|-------------------|---------|------------------|-----------|----------------------|
| **P0.1: Human validation of SDXL-Inc outputs** | SDXL-Inc produces more inclusive images | Human raters will assign more balanced race/gender labels to SDXL-Inc vs SDXL outputs | 200 images (100 SDXL, 100 SDXL-Inc, neutral prompt); 50 raters on Prolific; raters label perceived race and gender | SDXL baseline; compare classifier labels vs human labels | Cohen's κ between classifier and human; race/gender distribution balance by human labels | Human-assigned distribution for SDXL-Inc is closer to uniform than SDXL (p<0.05) | ~$300, 2 days | Validates the core debiasing claim; addresses most serious methodological concern |
| **P0.2: Classifier uncertainty propagation** | Measurement uncertainty does not change qualitative conclusions | Bias audit conclusions are robust to classifier misclassification | Compute upper/lower bounds on all reported percentages using confusion-matrix-conditional error model | Point estimates without uncertainty; bootstrapped CIs | Bounded range for each reported percentage; overlap with uniform distribution | Key conclusions (White majority, gender skew, profession stereotypes) hold under worst-case misclassification | 1 day | Quantifies reliability of all downstream measurements |
| **P1.1: Face-only SDXL-Div evaluation** | SDXL-Div genuinely increases facial diversity (not background diversity) | Face-cropped cosine similarity also shows reduction | Crop faces via MTCNN; recompute pairwise cosine similarity on cropped images | Full-image cosine similarity; SDXL baseline | Mean and distribution of face-cropped cosine similarity | Face-cropped similarity also shows significant reduction (p<0.01) for each race | 1 day | Strengthens homogenization analysis by removing background confound |
| **P1.2: Between-subjects user study** | Estimation shifts are not purely demand-driven | Between-subjects design shows similar effect magnitude | Recruit 2×135 participants; each sees only one condition (inclusive OR non-inclusive OR no images); baseline-only group | Within-subjects results from current study; pooled replication | Effect size (Cohen's d) of condition on percentage estimate | d>0.3 (small-to-medium) and consistent direction with current findings | ~$600, 3 days | Rules out demand characteristics as sole explanation; would substantially strengthen paper |

### ASCII Diagram — Experiment Upgrade Plan

```text
Stage 1 (P0 — Before Resubmission):
  [Classifier Sensitivity Analysis]
    ├── Compute per-class misclassification rates
    ├── Propagate to all reported percentages as CIs
    └── Verify key conclusions hold under uncertainty
  [Human Validation of SDXL-Inc]
    ├── 200 images (100 SDXL, 100 SDXL-Inc)
    ├── 50 raters on Prolific
    └── Compare human vs classifier distributions

Stage 2 (P1 — Before or During Review):
  [Face-Only SDXL-Div Evaluation]
    └── MTCNN crop → recompute cosine similarity
  [Between-Subjects User Study Replication]
    └── 2×135 new participants, between-subjects only
    └── Re-estimate effect sizes
  [Intersectional Analysis]
    └── Compute joint race×gender per profession

Stage 3 (P2 — During Revision):
  [Effect Size + Multiple Testing]
  [Related Work Restructure]
  [Cosine Similarity Histograms]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6/10**

The paper addresses a timely and important topic with substantial empirical effort (multiple classifiers, large-scale image generation datasets, four user studies). The core strengths are the breadth of the bias audit (6 races × 2 genders × 32 professions × 8 attributes), the proposed debiasing solutions with generalization testing, and the novel RCT design. However, the score is limited by several factors:

- **Research Value (6/10):** The bias audit is comprehensive but largely confirms patterns established by prior work (Bianchi et al. 2023, Ghosh & Caliskan 2023). The most novel contributions—racial homogenization measurement and human impact studies—are weakened by methodological concerns (classifier accuracy, demand characteristics).
- **Novelty (6/10):** The debiasing solutions are practically useful but technically incremental (LORA fine-tuning of SDXL). The RCT component is the most novel element, but its contribution is constrained by the demand-characteristic confound.
- **Validity & Soundness (6/10):** The classifier accuracy (73%) creates systematic uncertainty in all measurements. The circular evaluation of SDXL-Inc is a structural concern. The user studies are preregistered and well-powered but face demand characteristic limitations.
- **Reproducibility (7/10):** Data generation procedures, hyperparameters, and prompts are well-documented. Missing details: exact VGGFace embedding layer, LAION-5B sampling procedure, full demographic breakdown of filtered vs unfiltered LAION-5B.

**Post-Revision Target: [7.5, 8.5]/10**

If the following are addressed: (1) classifier sensitivity analysis showing all conclusions hold under uncertainty; (2) human validation of SDXL-Inc outputs; (3) tempered Discussion claims; (4) fixed Introduction gap paragraph; (5) intersectional analysis; (6) effect sizes and multiple-testing correction—the paper would be significantly stronger. The combination of large-scale bias documentation, novel debiasing solutions, and RCT evidence for human impact would then merit a score in the 7.5-8.5 range.

**Scoring Rationale (10-point scale):**
- 9-10: Breakthrough; would significantly change research/practice in the field.
- 7-8: Strong paper with minor weaknesses; competitive at top venues.
- 5-6: Solid work with notable concerns; borderline for top venues.
- 3-4: Significant flaws in methodology or claims.
- 1-2: Fatal errors or no scientific contribution.