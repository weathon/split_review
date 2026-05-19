## Summary
# Final Review Report

## Summary

This paper (Binz & Schulz, ICLR 2024) investigates whether large language models can be adapted to predict human decision-making behavior by finetuning a linear probe on top of frozen LLaMA-65B embeddings. The resulting model, CENTaUR, is evaluated on two classic decision-making paradigms (decisions from description using the choices13k dataset, and decisions from experience using the horizon task) and compared against two domain-specific cognitive models (BEAST and a hybrid exploration model). CENTaUR achieves lower negative log-likelihood than these baselines, captures individual-level variation via mixed-effects modeling, and shows some generalization to a held-out experiential-symbolic decision task. The authors argue that LLMs can be "turned into cognitive models."

**Core Contributions (C1-C3):**
- **C1**: Finetuned LLM embeddings (via linear probe) yield better fit to human choices than two baseline cognitive models in two decision-making domains.
- **C2**: LLM embeddings capture individual-level differences in choice behavior.
- **C3**: Multi-task finetuning enables prediction on a held-out task that combines components of the training tasks.

**Strengths**: The paper addresses an important and timely question (bridging LLM capabilities and cognitive modeling). The experimental design is sound: 100-fold cross-validation, multiple baselines, seed stability checks, and model simulations. The individual-differences analysis and hold-out task evaluation extend beyond simple goodness-of-fit comparisons.

**Critical Weaknesses**: (1) The paper's central claim—that CENTaUR is a "cognitive model"—is undermined by the Appendix A.5 finding that performance drops below chance under semantically equivalent prompt modifications. (2) The "state-of-the-art" claim is not supported given only two domain-specific baselines were compared. (3) The hold-out task shares structural components with training tasks, limiting the generality of the cross-task generalization result. (4) The Abstract and Introduction do not caveat these limitations, creating an over-claim problem.

**Novelty**: Deferred—cannot be independently verified in this run (Retrieval-Disabled Mode active). Manual literature verification is required to determine whether prior work on LLM-based cognitive modeling or embedding-based behavior prediction overlaps substantially with this contribution.

## Strengths
1. **Timely and important research question**: The paper asks whether LLMs can serve as models of human cognition, a question at the intersection of AI, cognitive science, and psychology. This direction has high potential impact if successful.

2. **Clean, reproducible methodology**: The approach is straightforward and well-documented: extract frozen LLaMA-65B embeddings from task prompts, train a regularized logistic regression (linear probe), evaluate via 100-fold cross-validation. Data and code are publicly released via GitHub.

3. **Multiple validation layers beyond accuracy**: Beyond simple prediction accuracy, the paper includes model simulations (regret, choice curves), individual-differences analysis (model selection, mixed effects), and a hold-out task generalization test. This multi-faceted evaluation strengthens confidence in the results where they hold.

4. **Honest limitation acknowledgment (Part 1)**: The Discussion acknowledges prompt brittleness (Appendix A.5) and the gap between current results and a domain-general cognitive model. This transparency is valuable, though the Abstract and earlier sections do not reflect these caveats.

5. **Informative post-hoc analysis (Section 3.5)**: The analysis identifying specific choice patterns where CENTaUR outperforms BEAST (loss aversion) and the hybrid model (stickiness) provides concrete, actionable insights for improving cognitive models. This is a creative use of the LLM-based model as a diagnostic tool.

6. **Seed stability**: CENTaUR's near-identical performance across five random seeds (SE = 0.02 NLL) demonstrates the fitting procedure is robust to initialization and data-splitting variation.

## Weaknesses
1. **Fatal-grade robustness failure (Critical)**: CENTaUR's predictions fall below chance level under semantically equivalent prompt modifications (Appendix A.5). Moving instructions to the beginning or reordering probability/outcome phrasing causes NLL to worsen from ~48,000 (original) to ~90,000–150,000 (modified), where random guessing is ~120,000. This directly contradicts the claim that CENTaUR is a "cognitive model"—true cognitive models should be invariant to surface-level presentation changes. This finding is buried in the appendix and not reflected in the Abstract or Introduction.

2. **Overclaimed "state-of-the-art" status**: The paper concludes that LLM representations "attain state-of-the-art results for modeling human decision-making" based on comparison with only two domain-specific models (BEAST and a hybrid model). The authors' own footnote 1 acknowledges other models exist (Bourgin et al., 2019; He et al., 2022; Zhang & Yu, 2013; Wilson et al., 2014) but does not compare against them. The term "state-of-the-art" is therefore unsupported.

3. **Limited baseline set for main comparison**: Only one cognitive model per paradigm is compared. The paper's main quantitative result—that CENTaUR "outperforms traditional cognitive models"—depends entirely on BEAST for choices13k and the hybrid model for the horizon task. Both are relatively simple heuristic models. A 65B-parameter embedding space plus thousands of learned weights may simply have more capacity, not better cognitive alignment.

4. **Hold-out task generalization is overstated (Major)**: The held-out task (Garcia et al., 2023) combines description-based and experience-based elements, both present in training. The paper also selects only "mixed trials of the post-learning phase" (8,624 of 25,872 choices), potentially biasing toward easier predictions. Finally, LLaMA without finetuning performs *below chance* (NLL 6307.9 vs. random 5977.7) on this task—a notable finding the paper does not discuss.

5. **"Cognitive model" terminology is misleading**: The paper uses "cognitive model" to describe what is fundamentally a predictive model of choice behavior. Traditional cognitive models (e.g., prospect theory, reinforcement learning models) provide mechanistic, interpretable accounts of mental processes. CENTaUR provides neither—it is a black-box linear probe on LLM embeddings. The paper would be more accurately framed as "using LLM embeddings to predict human choices."

6. **Mixed-effects model risks overfitting (Major)**: The random-effects structure adds one parameter per participant per embedding dimension (approximately 8192 × 60 = 491,520 parameters) for only ~1,120 trials per participant. No regularization on random effects is reported, and no comparison against simpler participant-level models is provided.

7. **Model size not varied**: Only LLaMA-65B is tested. The paper does not investigate whether smaller models (7B, 13B, 33B) would suffice, leaving open the question of whether the approach requires massive computational resources. This also means the "state-of-the-art" claim is specific to one model size.

8. **Absence of variance reporting for key comparisons**: The p-value for CENTaUR vs. domain-specific models is reported as p < 0.001 but without specifying the test used or reporting per-fold variance. The 1% test split in 100-fold CV yields small test sets, and fold-level variance should be reported.

## Key Issues
**Issue 1 (Critical) — Prompt Brittleness Undermines the Central Claim**
- **Location**: Appendix A.5 (Page 16), and Abstract (Page 1)
- **Problem**: CENTaUR's predictive performance drops below chance under trivial prompt modifications (reordering instructions, swapping probability-outcome phrasing). This means the model does not capture human-like decision-making—it exploits surface-level prompt format correlations.
- **Impact**: If the paper's core claim is that LLMs "can be turned into cognitive models," this finding directly falsifies that claim under the standard that cognitive models should be format-invariant.
- **Fix**: Move robustness analysis to main paper. Substantially revise Abstract, Introduction, and Conclusion to present CENTaUR as a "brittle predictor of human choices under specific prompt conditions" rather than a "cognitive model."

**Issue 2 (Major) — "State-of-the-Art" Claim Overreach**
- **Location**: Section 3.1 (Page 4)
- **Problem**: Only two domain-specific baselines are compared (BEAST and hybrid model). The paper itself acknowledges other models exist but does not include them.
- **Impact**: Reader may assume CENTaUR has been rigorously compared against the full decision-making literature. This is not the case.
- **Fix**: Replace "state-of-the-art" with specific claims about outperforming the chosen baselines. Add comparison to at least one additional cognitive model per paradigm, or explicitly scope the claim to "outperforms BEAST and the hybrid model under comparison."

**Issue 3 (Major) — Misleading "Cognitive Model" Framing**
- **Location**: Title, Abstract, Introduction (Page 1-2), Discussion (Page 7)
- **Problem**: The paper uses "cognitive model" to describe what is fundamentally a predictive model with no mechanistic interpretability. Traditional cognitive models (e.g., prospect theory, reinforcement learning) explain *how* decisions are made. CENTaUR only predicts *what* decisions are made.
- **Impact**: The framing sets an expectation the paper cannot meet, leading to potential rejection from cognitive science venues and skepticism from ML venues.
- **Fix**: Reframe as "predictive model of human choice behavior using LLM embeddings" throughout. Reserve "cognitive model" language for future work where mechanistic interpretability is demonstrated.

**Issue 4 (Major) — Generalization Claim Overstated**
- **Location**: Section 3.4 (Page 6)
- **Problem**: The hold-out task shares structural components with training tasks (description + experience), and only post-learning mixed trials are used. LLaMA performs below chance on this task.
- **Impact**: The claim that the approach "generalizes to previously unseen tasks" is not supported for a fundamentally different cognitive domain.
- **Fix**: Qualify generalization claim: "generalizes to a held-out decision scenario combining trained task components." Add LLaMA below-chance finding to main text.

**Issue 5 (Major) — Mixed-Effects Model Overparameterization Risk**
- **Location**: Section 3.3 (Page 5-6)
- **Problem**: ~500K additional parameters for 60 participants with ~1,120 trials each. No regularization or simpler baseline comparisons.
- **Impact**: The improved NLL may partly reflect overfitting rather than genuine individual-difference capture.
- **Fix**: Report regularization on random effects, compare against participant-level intercept-only model, and test generalization of participant-specific parameters to held-out trials.

## Actionable Suggestions
### S1: Reframe the Paper's Central Claim (Must)

**Problem**: The current title "Turning Large Language Models into Cognitive Models" and Abstract claims create expectations the evidence does not meet due to prompt brittleness.

**Action**: Revise the title, abstract, introduction, and conclusion to describe CENTaUR as a "predictive model of human choice behavior using LLM embeddings" rather than a "cognitive model."

**Mentor Revised Title (option):**
"Predicting Human Decision-Making from Large Language Model Embeddings"

**Mentor Revised Abstract (compact version):**
"Large language models (LLMs) process text but often produce decisions that deviate from human patterns. We investigate whether LLM embeddings can serve as feature representations for predicting human choices. Using frozen LLaMA-65B embeddings with a linear probe finetuned on psychological experiment data, we find that the resulting model (CENTaUR) achieves lower negative log-likelihood than two baseline cognitive models on description-based and experience-based decision tasks. However, this predictive accuracy is brittle: performance drops below chance under semantically equivalent prompt rephrasing. Our results suggest that LLM embeddings provide a useful, albeit task-specific, feature space for predicting human decisions, but are not yet robust enough to serve as general cognitive models."

### S2: Move Prompt Brittleness to Main Text (Must)

**Action**: Move Appendix A.5 (Robustness Checks) to a main-text subsection in Results or Discussion. Present the NLL values for each prompt modification explicitly (not just in a figure). This finding is too central to the paper's limitations to remain in the appendix.

### S3: Replace "State-of-the-Art" with Scoped Claim (Must)

**Action**: Replace the sentence "the representations extracted from large language models are rich enough to attain state-of-the-art results for modeling human decision-making" (Page 4) with:
"These results suggest that LLM embeddings, when adapted via a linear probe, can outperform the domain-specific models we tested (BEAST and the hybrid model). A more comprehensive comparison against a broader set of cognitive models would be needed to establish the relative ranking of CENTaUR within the full decision-making literature."

### S4: Add More Cognitive Model Baselines (Nice-to-have)

**Action**: Include at least 1-2 additional cognitive model baselines per paradigm. For choices13k: Bourgin et al. (2019)'s cognitive model priors or He et al. (2022)'s model crowds. For the horizon task: the uncertainty-directed exploration model or the Bayesian reinforcement learning model. This would substantially strengthen the "outperforming traditional cognitive models" claim.

### S5: Add Multi-Seed Variance for All Reported NLL Values (Must)

**Action**: Report per-fold NLL variance or 95% confidence intervals for all model comparisons, not just for CENTaUR. Currently, only CENTaUR's seed stability is reported (5 seeds). The domain-specific models' variance should also be reported.

### S6: Clarify Hold-Out Task Generalization Scope (Must)

**Action**: Qualify the Section 3.4 claim to: "generalizes to a held-out scenario combining trained task elements." Add a note that LLaMA performs below chance on this task, indicating that the raw LLM is systematically misaligned with human behavior.

### S7: Add Model Size Ablation (Nice-to-have)

**Action**: Compare CENTaUR performance using LLaMA-7B, 13B, 33B, and 65B on at least the choices13k dataset. This would determine whether the approach requires the largest model or can work with smaller, more efficient alternatives.

### S8: Report Overfitting Checks for Mixed-Effects Model (Must)

**Action**: Add a subsection reporting: (a) regularization on random-effect parameters, (b) comparison against a simpler participant-level intercept model, (c) cross-validation of participant-specific parameters (e.g., train on 80% of trials per participant, predict remaining 20%).

### S9: Conduct Multi-Trial Horizon Task Analysis (Nice-to-have)

**Action**: Extend the Section 3.2 choice-curve analysis beyond the first free-choice trial to all trials. Plot CENTaUR's exploration dynamics over the full 1- or 6-trial horizon and compare against human multi-trial trajectories.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows this structure:
- P1: LLMs are powerful and have broad societal impact.
- P2: In-context learning enables LLMs to solve tasks, including psychological experiments (e.g., GPT-3 beats humans).
- P3: But LLMs show non-human characteristics (e.g., GPT-3 is too exploitative).
- P4: Finetuning on domain-specific data can fix this.
- P5: Preview of results.

**Problems**: (a) P1 is too generic—does not directly motivate the cognitive modeling question. (b) P2 creates narrative tension by highlighting GPT-3 outperforming humans, which contradicts the goal of matching human behavior. (c) P4 introduces finetuning without explaining why a linear probe would align LLMs with humans. (d) The research gap ("can we fix behavioral discrepancies?") is stated only in P3-P4, which is late for reader engagement.

### Recommended Storyline: "Empirical Gap → Hypothesis → Evidence → Caveats"

**Abstract Outline (5 sentences):**
- S1 (Problem): "Large language models (LLMs) can solve diverse tasks, but their decision-making patterns often diverge from human behavior."
- S2 (Gap): "Standard cognitive models offer interpretable accounts of human decisions but may miss complex patterns that LLM representations can capture."
- S3 (Method): "We test this by extracting frozen LLaMA-65B embeddings from decision-making task prompts and training a linear probe to predict human choices, producing the CENTaUR model."
- S4 (Result + Caveat): "CENTaUR achieves lower negative log-likelihood than two baseline cognitive models on description-based and experience-based tasks, and captures individual-level variation. However, performance drops below chance under semantically equivalent prompt rephrasing, indicating brittleness."
- S5 (Conclusion): "These results suggest LLM embeddings provide a useful feature space for predicting human decisions in restricted settings, but are not yet robust enough to serve as general cognitive models."

**Introduction Outline (6 paragraphs):**
- P1 (Stakes): "LLMs exhibit remarkable capabilities, yet their decisions frequently deviate from human patterns in systematic ways." [Establishes the problem without hype.]
- P2 (Prior work on LLMs in psychology): "Prior work has placed LLMs in classic psychological experiments, finding a mix of human-like and non-human behavior." [Cite Binz & Schulz 2023, Shiffrin & Mitchell 2023, etc. — focus on behavioral discrepancies.]
- P3 (Concrete gap): "These discrepancies—especially the over-reliance on exploitation and plateauing learning curves—suggest that off-the-shelf LLMs do not yet provide adequate models of human decision-making." [Clear gap statement.]
- P4 (Hypothesis and approach): "We hypothesize that LLM embeddings encode rich semantic representations that can be repurposed to predict human choices, if appropriately adapted. To test this, we freeze LLaMA embeddings and train a linear probe on human behavioral data." [Method intuition first.]
- P5 (Evidence preview): "We find that this approach outperforms two baseline cognitive models in predictive accuracy, captures individual differences, and shows some cross-task generalization. However, we also identify a critical brittleness: performance degrades below chance under trivial prompt variations." [Balanced preview.]
- P6 (Contributions): "Our contributions are (1) demonstrating that LLM embeddings, when adapted, provide competitive predictions of human choice behavior, (2) identifying specific behavioral patterns where CENTaUR outperforms traditional models, and (3) documenting the prompt sensitivity that limits current LLM-based cognitive modeling."

### Why This Storyline Is Better

1. **Problem alignment**: P1 directly states the behavioral discrepancy problem rather than starting with generic LLM capabilities.
2. **Variable alignment**: The core concepts (embeddings, linear probe, human choices) are introduced in P4 before appearing in Methods.
3. **Contribution-evidence alignment**: The preview in P5 sets appropriate expectations by acknowledging both positive results and the key limitation—which is not done in the current version.

## Priority Revision Plan
### P0 — Publication-Critical (Must Fix Before Resubmission)

| Priority | Issue | Location | Action | Expected Impact |
|----------|-------|----------|--------|-----------------|
| P0.1 | Prompt brittleness contradicts "cognitive model" claim | Abstract, Intro, Discussion, Appendix A.5 | Move robustness analysis to main text; revise Abstract/Title/Conclusion to reflect CENTaUR as a "predictive model" not "cognitive model" | Prevents desk rejection or major reviewer pushback |
| P0.2 | "State-of-the-art" claim unsupported | Page 4, Section 3.1 | Replace with scoped claim about outperforming two specific baselines | Avoids factual overreach |
| P0.3 | Overstated "generalization to unseen tasks" | Page 6, Section 3.4 | Qualify generalization scope; add LLaMA below-chance note | Aligns claim with evidence |
| P0.4 | Mixed-effects overfitting risk | Page 5, Section 3.3 | Add regularization info, simpler baseline comparison | Strengthens individual-differences claim |
| P0.5 | Missing variance reporting for comparisons | Page 4, Section 3.1 | Add per-fold NLL variance and CI for all models | Enables statistical reliability assessment |

### P1 — High Priority (Strongly Recommended)

| Priority | Issue | Location | Action | Expected Impact |
|----------|-------|----------|--------|-----------------|
| P1.1 | Introduction narrative too generic | Page 1, Introduction | Restructure per the Storyline Options section | Improves reader engagement and clarity |
| P1.2 | Only two cognitive model baselines | Page 4, Section 3.1 | Add 1-2 additional baselines per paradigm | Strengthens comparative claims |
| P1.3 | No model size comparison | Page 2, Methods | Add LLaMA-7B/13B/33B comparison | Tests computational efficiency |
| P1.4 | Single-trial analysis in choice curves | Page 4, Section 3.2 | Extend to multi-trial trajectories | Strengthens behavioral validation |

### P2 — Quality Improvement (Nice-to-Have)

| Priority | Issue | Location | Action | Expected Impact |
|----------|-------|----------|--------|-----------------|
| P2.1 | Mixed-effects model validation | Page 5, Section 3.3 | Correlate participant-specific params with external measures | Validates individual differences |
| P2.2 | Inverse analysis lacks pattern | Page 17, Appendix A.6 | Clarify limitations of failure-case analysis | Improves transparency |
| P2.3 | t-SNE analysis qualitative only | Page 18, Appendix A.7 | Add quantitative separability metric | Strengthens embedding analysis |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Current paper: "LLMs as cognitive models"]
    |
    |-- Problem 1: Prompt brittleness hidden in appendix
    |   |-- Fix: Move to main text + revise claims
    |   |-- Expected: Aligned evidence-claim structure
    |
    |-- Problem 2: Overclaimed "state-of-the-art"
    |   |-- Fix: Scoped wording + more baselines
    |   |-- Expected: Defensible comparative claims
    |
    |-- Problem 3: "Cognitive model" framing mismatch
    |   |-- Fix: Reframe as "predictive model of human choices"
    |   |-- Expected: Honest positioning, reduced reviewer skepticism
    |
    |-- Problem 4: Generalization overreach
    |   |-- Fix: Qualify scope + note LLaMA below-chance
    |   |-- Expected: Accurate generalization boundaries
    |
    v
[Revised paper: "Predicting human choices from LLM embeddings"]
    |
    |-- Core strength preserved: LLM embeddings + linear probe works
    |-- Limitations transparently acknowledged
    |-- Claims bounded to available evidence
    |-- Clear path to address prompt brittleness in future work
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|--------------|-----------------|-------------------|
| E1 | Main comparison: CENTaUR vs baselines on choices13k | 100-fold CV, 90/9/1 split, L2-regularized logistic regression on LLaMA-65B embeddings | Negative log-likelihood (NLL), accuracy | CENTaUR NLL 48002.3 vs BEAST 49448.1 | C1 (predictive fit) | Only 1 domain-specific baseline; "SOTA" overclaimed |
| E2 | Main comparison: CENTaUR vs baselines on horizon task | Same procedure as E1, using horizon task data (60 participants, 67,200 choices) | NLL, accuracy | CENTaUR NLL 25968.6 vs Hybrid 29042.5 | C1 (predictive fit) | Same as E1 |
| E3 | Seed stability check | Repeated E1/E2 with 5 random seeds | NLL (mean ± SE) | CENTaUR SE = 0.02 for both datasets | C1 robustness | Only CENTaUR checked, not baselines |
| E4 | Model simulations (regret) | Simulated choices from CENTaUR, LLaMA, humans on both tasks | Regret (best - chosen reward) | CENTaUR regret close to human; LLaMA much higher | C1 (human-likeness) | Single-trial analysis only |
| E5 | Choice curves (exploration patterns) | First free-choice trial of horizon task; logistic regression on reward diff × horizon | p(choose more informative) | CENTaUR replicates horizon-dependent exploration effects | C1 (qualitative match) | Only first trial analyzed |
| E6 | Individual differences (fixed effects) | Per-participant NLL comparison across models | NLL per participant | 52/60 participants best fit by CENTaUR | C2 | No external validation of individual parameters |
| E7 | Individual differences (mixed effects) | Random effects per participant × embedding dimension | NLL | Mixed-effects improves NLL (23929.5 vs 25968.6) | C2 | ~500K extra params; overfitting risk unaddressed |
| E8 | Hold-out task generalization | Train on choices13k + horizon; test on Garcia et al. (2023) | NLL, choice curves | CENTaUR NLL 4521.1 vs LLaMA 6307.9 vs random 5977.7 | C3 | Task shares components; LLaMA below chance |
| E9 | Inform cognitive theories (log-likelihood difference analysis) | Rank data points by NLL diff between CENTaUR and domain-specific model | Qualitative pattern analysis | Identified loss aversion (choices13k) and stickiness (horizon) | C1 (mechanistic insight) | Post-hoc, no confirmatory test |
| E10 | Robustness checks (Appendix A.5) | Prompt modifications on choices13k (reorder, rephrase) | NLL | All modifications → below-chance performance (NLL ~90K-150K vs random ~120K) | Limitation documented | Buried in appendix; not reflected in Abstract |

### Research-Theme Gap Diagnosis

- **New knowledge**: The paper's strongest evidence is that LLM embeddings provide a useful feature space for predicting human choices. However, whether this constitutes *new knowledge about human cognition* is limited, since CENTaUR is a black-box predictor without mechanistic interpretability.
- **Reproducibility**: Good. Data and code are publicly released. The method (linear probe on frozen embeddings) is simple and replicable.
- **Impact on practice/understanding**: The paper could influence how cognitive scientists approach human behavior prediction, but the prompt brittleness finding limits practical deployment until robustness is improved.

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|--------|-------------|------------|----------------|-------------------|---------|------------------|-----------|---------------|
| R1 | C1: LLM embeddings provide useful features beyond simpler models | LLaMA-7B/13B/33B will show similar but decreasing performance vs 65B | Repeat E1/E2 with LLaMA-7B, 13B, 33B | Same linear probe, same CV procedure | NLL, accuracy | 7B achieves >50% of 65B improvement over BEAST | Low (1-2 GPU-days) | Tests resource efficiency; determines minimal viable model |
| R2 | C1: Prompt augmentation improves robustness | Training on multiple prompt formats will yield format-invariant representations | For each task, generate 3-5 prompt variants; train on all variants | Single-format training (current) | NLL on held-out prompt variants | NLL on modified prompts does not drop below chance | Medium (2-5 GPU-days) | Directly tests whether brittleness is fixable |
| R3 | C2: CENTaUR captures meaningful individual differences | Participant-specific CENTaUR parameters correlate with external cognitive measures | Extract participant-specific intercepts from mixed model; correlate with questionnaire scores (e.g., CRT, risk preference) | Random-effects model (current) | Correlation coefficient, p-value | Significant correlation (p<0.05) with at least one external measure | Low (compute-free; just analysis) | Validates individual-differences claim |
| R4 | C3: Cross-task generalization to orthogonal domain | CENTaUR trained on choice tasks will NOT generalize to perceptual decision-making | Test on perceptual decision task (e.g., random dot motion) after training on choices13k + horizon | Current hold-out result | NLL vs chance | Establishes boundary conditions of generalization | Low (<1 GPU-day) | Delimits generalization scope |

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 Experiments (Must Fix Current Claims)
├── R2: Prompt robustness augmentation
│   → Tests the core brittleness finding
│   → If successful, strengthens "cognitive model" framing
│
P1 Experiments (Strengthen Existing Evidence)
├── R1: Model size ablation (7B/13B/33B/65B)
├── R3: External validation of individual differences
│
P2 Experiments (Extend Scope)
├── R4: Test generalization boundary (perceptual task)
│
Expected Outcome Distribution:
├── R2 success → Paper can retain "cognitive model" framing
├── R2 failure → Paper MUST reframe as "brittle predictor"
└── R1+R3+R4 success → Overall contribution significantly strengthened
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

*Rationale*: The paper addresses an interesting and timely question with a clean, reproducible methodology. The core finding—that LLM embeddings with a linear probe can predict human choices—is supported by the data and has potential value for cognitive modeling. However, the score is constrained by three major factors:

1. **Critical prompt brittleness finding (Appendix A.5)** directly contradicts the paper's central "cognitive model" framing and is not reflected in the Abstract or Introduction. This claim-evidence mismatch is the most significant weakness.

2. **The "state-of-the-art" claim for human decision-making prediction is unsupported**, as only two domain-specific baselines are compared. The paper's own footnote acknowledges more baselines exist.

3. **The "generalization to unseen tasks" claim is overstated** because the hold-out task shares structural components with training, and LLaMA performs below chance on this task.

The paper's strengths (clean methodology, multiple validation layers, informative post-hoc analysis, seed stability) support a non-rejectable baseline. However, the identified overclaims and buried negative results prevent a higher score without substantial revision.

If the publication venue is a **cognitive science journal** (e.g., Cognitive Science, Nature Human Behaviour), the score would be lower (~4.5/10) due to the "cognitive model" framing mismatch. If the venue is an **ML conference** (e.g., NeurIPS, ICML), the current score of 5.5/10 is appropriate, reflecting solid methodology but overclaimed contributions.

---

**Post-Revision Target: [6.5, 7.5] / 10**

This target assumes the following P0-P1 revisions are fully addressed:
- Reframe claims to align with evidence (prompt brittleness acknowledged in Abstract, no "SOTA" overclaim)
- Move robustness analysis to main text
- Add additional cognitive model baselines (at least 1-2 per paradigm)
- Add variance reporting for all comparisons
- Qualify generalization claims

The upper bound (7.5) is achievable if the authors also demonstrate that prompt augmentation (Proposed Experiment R2) substantially improves robustness. Without addressing the brittleness, the paper cannot exceed 6.0/10 regardless of other improvements.