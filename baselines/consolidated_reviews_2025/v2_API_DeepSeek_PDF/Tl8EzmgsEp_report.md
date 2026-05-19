## Summary
# Final Review Report

## Summary

This paper investigates the learned look-ahead behavior of the Leela Chess Zero policy network, extending prior work (Jenner et al., 2024) from 3-move analysis to 5- and 7-move planning horizons and alternative-move evaluation. Using activation patching, linear probing, and attention head ablation on Lichess puzzle data, the authors demonstrate: (1) the model's look-ahead is highly context-dependent, varying with move-square patterns and checkmate proximity; (2) the same attention heads (notably L12H12) that process the 3rd move also process the 5th and 7th moves via pattern-sensitive, time-invariant mechanisms following AAC/ABC/ACC square-pattern ordering; (3) the model simultaneously evaluates multiple move branches, with L12H12 processing each branch independently. The paper contributes a methodological toolkit (puzzle set notation, adapted corruption techniques) and provides new evidence about planning-like computations in self-play-trained transformers.

The study is technically well-executed within its scope, with rigorous application of three complementary interpretability techniques. However, several concerns affect the strength of its claims: the 7th-move evidence lacks statistical quantification, the alternative-moves analysis rests on a tiny filtered dataset (~300 puzzles from 4M), the "similar mechanisms" claim across depths is correlational rather than causally tested, and the use of a finetuned model without disclosed finetuning details limits reproducibility. The paper over-claims in some places (e.g., generalization to robotics, "sophisticated planning" language) and the Related Work section reads as a citation list rather than a genuine comparative analysis.

## Strengths
1. **Technically rigorous multi-method analysis.** The paper combines three complementary interpretability techniques (activation patching, probing, ablation) in a well-structured pipeline. Each method provides a different type of evidence (causal, correlational, mechanistic), and the paper explicitly discusses cases where methods converge or diverge (e.g., opponent moves are probe-detectable but patch-invisible). This multi-faceted approach is a methodological strength.

2. **Novel puzzle set notation enables fine-grained analysis.** The s1s2...sn labeling scheme and its AAC/ABC/ACC pattern taxonomy provide a systematic way to disentangle the model's behavior across different tactical configurations. This notation is a genuine methodological contribution that enables the paper's key finding about time-invariant pattern-sensitive mechanisms.

3. **Clear evidence of attention head specialization.** The paper convincingly demonstrates that L12H12 and L12H17 have distinct functional roles (checkmate vs. non-checkmate) and that these heads move information "backward in time" according to specific square-pattern rules. The ablation results showing differential effects for different puzzle sets provide strong evidence that the model has learned specialized rather than monolithic processing.

4. **Alternative-move evaluation evidence, though limited, is methodologically creative.** The adaptation of the corruption technique to two-branch puzzles and the finding of independent branch processing by L12H12 is a clever experimental design that provides a template for future studies.

5. **Well-structured reproducibility appendix.** The paper includes comprehensive appendix materials with additional puzzle sets, ablation results for multiple heads, and implementation details (though the finetuning detail gap is noted as a weakness).

## Weaknesses
1. **Reproducibility gap: undisclosed finetuning of the target model (Page 3 - Section 2.1).** The paper uses a finetuned version of Leela without specifying the finetuning procedure, data, or rationale beyond "due to peculiarities." This is a major reproducibility concern because the observed attention head behavior could be specific to the finetuned model rather than the original Leela.

2. **7th-move look-ahead claim lacks statistical quantification (Page 6 - Results, Fig. 3).** The central claim that the model "considers up to the seventh future move" is supported by probing that is described qualitatively ("non-negligible") without reporting actual accuracy values, confidence intervals, or significance tests. The patching effect for the 7th move (Fig. 14) is very small (~0.2-0.3 log odds reduction vs ~4-6 for move 1), raising the question of whether it is functionally meaningful.

3. **Alternative-moves analysis (C3) is based on a tiny, heavily filtered dataset (Page 8, Appendix F).** From 4,062,423 puzzles, only ~600 survive the filtering criteria, and the paper acknowledges that ~50-66% of those have "non-negligible" probability differences between branches, leaving potentially only ~200-300 effective samples. No cross-validation or stability analysis is reported.

4. **"Similar mechanisms" claim across move depths is correlational, not causal (Page 7).** The claim that the model processes 3rd, 5th, and 7th moves using "similar mechanisms" rests on observing the same ACC < ABC < AAC patching pattern at different depths. This is consistent with shared mechanisms but does not establish mechanism identity. The paper acknowledges exceptions (e.g., 12334, 7-move 123VWXY sets) in Appendix D but does not discuss them in the main text.

5. **Context-dependence finding (C1) is descriptive rather than mechanistic.** The claim that "look-ahead behavior is highly dependent on the specific type of chess position" is a valid observation but does not explain *why* different puzzle sets produce different patterns. The paper identifies *that* attention heads differ across sets but does not identify what features of the position (beyond square overlap) drive these differences.

6. **Over-claiming in motivation and broader impacts.** The introduction claims findings "may generalize to other domains where long-term planning is essential, such as robotics or strategic decision-making" without any argument for why chess-derived mechanisms would transfer to partially-observable, stochastic domains. The "cognitive-like processes" language in the abstract is evocative but not operationalized.

7. **Related Work is a citation list without comparative depth (Page 9).** The Related Work section lacks side-by-side comparison with the strongest prior work (Karvonen 2024, Jenner et al. 2024 on chess interpretability; Li et al. 2023a on Othello). It does not explain what specific gaps this paper fills relative to each cited work.

## Key Issues
### Issue 1 (Major): Reproducibility — Undisclosed Model Finetuning
**Location:** Page 3 - Section 2.1 (Chess Model)
**Evidence:** The paper states "Due to peculiarities of this particular model, previously discussed in Jenner et al. (2024), we use a finetuned version of the model, trained and used by Jenner et al. (2024)."
**Risk:** The core empirical findings (attention head roles, look-ahead depth) may be artifacts of the finetuning procedure rather than properties of the original Leela model. Without finetuning details, no independent verification is possible.
**Fix:** Disclose finetuning data, objective, hyperparameters, and rationale in Appendix. Run one key validation experiment (e.g., L12H12 ablation on set 112) with the original unfinetuned model.

### Issue 2 (Major): 7th-Move Look-Ahead Claim is Quantitatively Unsupported
**Location:** Page 6 - Results section, Fig. 3, Fig. 14
**Evidence:** Probing accuracy for the 7th move is described only as "considerably low, but still non-negligible" without reporting actual values. Patching effects for the 7th move (Fig. 14) show log odds reductions of ~0.2-0.3, compared to ~4-6 for move 1.
**Risk:** The paper's headline quantitative finding (7-move look-ahead) rests on an effect that may be statistically significant but practically negligible. The "non-negligible" descriptor is subjective.
**Fix:** Report exact probing accuracies with confidence intervals, add significance tests against random baseline, and establish a functionally meaningful effect size threshold.

### Issue 3 (Major): Alternative-Moves Analysis (C3) on Brittle Data
**Location:** Page 8 - Section "The model considers alternative move sequences," Appendix F
**Evidence:** From 4,062,423 initial puzzles, only ~600 survive filtering (0.015%). The paper acknowledges ~50-66% show non-negligible probability imbalance between branches, leaving potentially ~200-300 effective samples.
**Risk:** The finding that the model "considers multiple move sequences" may not generalize beyond this tiny, heavily constrained subset. No cross-validation or stability analysis is provided.
**Fix:** Report split-half reliability or bootstrap confidence intervals for the patching effects. Explicitly acknowledge the limited scope in the main text.

### Issue 4 (Major): "Similar Mechanisms" Claim Over-Reaches Evidence
**Location:** Page 7 - Section "The model processes 3rd, 5th, and 7th moves similarly"
**Evidence:** The claim is based on observing the same ordering of patching effect sizes (ACC < ABC < AAC) at different depths. Appendix D documents exceptions (e.g., set 12334, 7-move 123VWXY sets) that are not discussed in the main text.
**Risk:** Readers may over-interpret the evidence as demonstrating shared mechanism identity when only consistent sensitivity patterns have been shown. The exceptions suggest the picture is more nuanced.
**Fix:** Either (a) downgrade the claim to "consistent sensitivity patterns" with mechanism identity as a speculation, or (b) add direct representational similarity analysis (e.g., CKA) across depths.

### Issue 5 (Minor-to-Moderate): Context-Dependence Finding is Descriptive
**Location:** Page 6 - Results, Contribution C1
**Evidence:** The paper shows that different puzzle sets produce different patching profiles but does not identify what board features drive these differences beyond square-pattern taxonomy.
**Risk:** The contribution remains at the level of observation rather than explanation.
**Fix:** Use feature attribution or embedding analysis to identify what tactical features (e.g., piece types under attack, king safety, material balance) correlate with different attention head recruitment patterns.

## Actionable Suggestions
### S1 (Must): Add Finetuning Disclosure and Validation
**What:** In Appendix H, add a subsection detailing the finetuning procedure: training data distribution, objective function, number of epochs, hyperparameters, and the "peculiarities" that necessitated finetuning. Add a note on model availability (e.g., a HuggingFace link upon publication).
**Why:** Without this, the paper's core results are not independently verifiable.
**Expected benefit:** Major improvement in reproducibility and reviewer confidence.

### S2 (Must): Quantify the 7th-Move Evidence
**What:** Report exact probing accuracies for the 7th move (and all other moves) as mean ± std across cross-validation folds or random seeds. Add a statistical significance test (e.g., permutation test comparing trained vs. random probe accuracy). For activation patching, report the effect size and compare to a noise baseline (patching an irrelevant square).
**Why:** The paper's headline finding requires quantitative rather than qualitative support.
**Expected benefit:** Transforms a subjective "non-negligible" claim into a verifiable quantitative result.

### S3 (Must): Acknowledge and Bound the Alternative-Moves Dataset Limitation
**What:** Move the data filtering attrition statistics from Appendix F to the main text (Page 8). Add a sentence: "These results are based on approximately 200-600 puzzles that satisfy all constraints, representing less than 0.02% of the original dataset; generalizability to other puzzle types may be limited." Add bootstrap confidence intervals or split-half reliability for the patching effects.
**Why:** The current presentation overstates the robustness of the alternative-moves evidence.
**Expected benefit:** Prevents reviewer criticism about hidden data limitations.

### S4 (Must): Tone Down Over-Claims in Introduction and Conclusion
**What:** 
- Replace "may generalize to other domains such as robotics or strategic decision-making" with "whether these findings transfer to imperfect-information domains remains an open question requiring explicit investigation."
- Replace "cognitive-like processes" in the abstract with a specific description of what was measured (e.g., "encoding of future move square information in attention head activations").
- In the conclusion, replace "sophisticated planning capabilities" with "context-dependent, pattern-sensitive future move encoding."
**Why:** Over-claiming reduces credibility with reviewers familiar with the planning literature.
**Expected benefit:** More defensible, bounded claims that will pass reviewer scrutiny.

### S5 (Nice-to-have): Validate Puzzle Set Notation Internal Consistency
**What:** Add a brief analysis (can go in Appendix A) showing that residual stream activations within a puzzle set are more similar (e.g., via cosine similarity or CKA) than across different puzzle sets. This would validate that the destination-square-based grouping captures a genuine representational invariant.
**Why:** The paper's analytical framework assumes the puzzle set notation captures meaningful model behavior; this assumption is currently untested.
**Expected benefit:** Strengthens the methodological contribution of the puzzle set notation.

### S6 (Nice-to-have): Direct Mechanism Comparison Across Depths
**What:** Compute representational similarity (CKA or activation correlation) between L12H12's attention patterns on 3-move vs. 5-move vs. 7-move puzzles that share the same AAC/ABC/ACC pattern. If correlations are high, this supports the shared mechanism claim; if low, it suggests different mechanisms with similar sensitivity profiles.
**Why:** Addresses the gap between correlational and causal evidence for the "similar mechanisms" claim.
**Expected benefit:** Either strengthens one of the paper's key claims or avoids over-interpretation.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction uses a 5-paragraph structure: (P1) broad AI motivation and planning-vs-pattern-matching framing; (P2) builds on Jenner et al. with specific goals; (P3) three generic reasons for importance; (P4) scaling reasons; (P5) mechanistic interpretability gap and chess as testbed. The contribution list then appears before the method preview. The narrative arc is somewhat diffuse — the specific research gap (what Jenner et al. did not do) is not sharp until late.

### Recommended Storyline Candidate (Best)
**Arc:** Specific gap → Method extension → Key empirical findings → Scoped implications.

**Abstract Outline (5 sentences):**
- S1 (Problem): Neural networks trained on strategic games exhibit internal computations that are not well understood, particularly whether they implement multi-step planning or pattern matching.
- S2 (Gap): Prior work (Jenner et al., 2024) demonstrated 3-move look-ahead in a chess policy network, but left open whether this capability extends to longer horizons and alternative branches.
- S3 (Method): Using activation patching, probing, and ablation on a curated puzzle dataset with a novel square-pattern taxonomy, we analyze the Leela Chess Zero policy network's internal representations across 3-, 5-, and 7-move puzzles.
- S4 (Key Result): We find that the model processes future moves up to 7 plies ahead through time-invariant, pattern-sensitive attention mechanisms, with different heads specializing in checkmate vs. non-checkmate scenarios.
- S5 (Conclusion): These findings reveal that neural networks can develop context-dependent, multi-branch look-ahead capabilities through self-play training, with implications for mechanistic interpretability methodology.

**Introduction Outline (6 paragraphs):**
- P1 (Territory + Specific Gap): Opening establishing that recent work (Jenner et al., 2024) found evidence of 3-move look-ahead in a chess policy network, but fundamental questions remain about whether this capability scales to longer horizons and whether it genuinely evaluates alternatives. This sharpens the gap immediately rather than starting with generic AI motivation.
- P2 (What We Do): State that this paper extends the prior analysis to 5th and 7th moves, introduces a puzzle set notation to disentangle context-dependent behavior, and examines alternative-move evaluation. State the three contributions concisely.
- P3 (Methodological Approach): Briefly describe the three complementary techniques (patching, probing, ablation) and why they are combined (causal necessity, representational availability, mechanism localization).
- P4 (Why Chess): Explain that chess provides ground-truth optimal sequences (principal variations) and a single-forward-pass architecture, enabling precise mechanistic analysis that is harder in language models. Acknowledge limitations (perfect information, fixed rules).
- P5 (Key Findings Preview): Pre-view the three main results — (i) 5th/7th move processing via time-invariant pattern matching, (ii) head specialization (L12H12 vs L12H17), (iii) multi-branch evaluation.
- P6 (Related Work Positioning): Brief sentence mapping the paper relative to key prior work (Jenner 2024, Karvonen 2024, Li 2023a) and stating the incremental advance.

### Alternative Storyline Candidate 2: Mechanism-First
**Arc:** Specific mechanism (attention head specialization) → varied contexts → broader implications.
Start with the L12H12/L12H17 finding, then show it generalizes across depths and branches, then discuss implications for neural network planning. This is more exciting but requires the reader to absorb a detailed finding before understanding the problem. Not recommended for a general audience.

### Alternative Storyline Candidate 3: Methodology-First
**Arc:** Methodological challenge → puzzle set notation + multi-technique approach → empirical demonstration.
Start with the puzzle set notation as a solution to the problem of analyzing context-dependent behavior, then show what it reveals. This positions the paper as primarily a methodological contribution. Suitable if the authors want to emphasize the interpretability toolkit, but risks downplaying the empirical findings.

## Priority Revision Plan
### P0 — Submission-Blocking (Must Fix Before Resubmission)

| Priority | Issue | Fix | Expected Impact |
|----------|-------|-----|-----------------|
| P0 | Undisclosed finetuning (Page 3) | Add finetuning details to Appendix H; run validation with original model | Prevents desk rejection due to reproducibility concerns |
| P0 | 7th-move claim unquantified (Page 6) | Report exact probing accuracies ± confidence intervals; add significance test | Transforms subjective claim into verifiable result |

### P1 — High Impact (Should Fix)

| Priority | Issue | Fix | Expected Impact |
|----------|-------|-----|-----------------|
| P1 | Alternative-moves dataset limitations hidden (Page 8) | Move filtering statistics to main text; add bootstrap CIs | Prevents "cherry-picked data" criticism |
| P1 | Over-claims in intro/conclusion | Replace unsupported generalization language with bounded claims | Improves defensibility during review |
| P1 | "Similar mechanisms" claim over-reaches (Page 7) | Downgrade to "consistent sensitivity patterns" or add CKA analysis | Aligns claim strength with evidence |

### P2 — Quality Improvement (Nice to Have)

| Priority | Issue | Fix | Expected Impact |
|----------|-------|-----|-----------------|
| P2 | Puzzle set notation not validated (Page 4) | Add activation similarity analysis within vs. across sets | Strengthens methodological contribution |
| P2 | Related Work reads as list (Page 9) | Restructure with explicit comparison axes | Better novelty positioning |
| P2 | Context-dependence is descriptive (C1) | Add feature attribution analysis | Moves from observation to explanation |
| P2 | Generic broader implications (Page 10) | Replace with specific architectural insights | Stronger conclusion |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|--------|-----------|-------|---------|--------------|-----------------|------------|
| E1 | Activation patching — 3-move puzzles | Clean vs. corrupted board, residual stream patching across 15 layers | Log odds reduction per move square | L12H12 important for set 112; 122/123 show weak effects | C1 (context-dependence) | Only 4 puzzle sets analyzed (111, 112, 122, 123) |
| E2 | Activation patching — 5-move puzzles | Same as E1, extended to 5-move sequences | Log odds reduction | ACC < ABC < AAC pattern holds; 11223 shows strongest 5th-move effect | C2 (extension to longer horizons) | No statistical comparison across sets |
| E3 | Activation patching — 7-move puzzles | Same as E1, extended to 7-move sequences | Log odds reduction | 7th-move effects small (~0.2-0.3); near look-ahead limit | C2 | Very small effect sizes; not statistically quantified |
| E4 | Probing — residual stream | Linear probe trained on layer-wise activations to predict future move square | Classification accuracy over 64 squares | Accuracy decreases with move depth; 7th-move above random but low | C2 | No confidence intervals; random baseline definition unclear |
| E5 | Attention head ablation — zero ablation | Set individual attention head weights to zero, measure log odds change | Log odds reduction per head | L12H12, L12H17, L13H3 identified as important; roles vary by puzzle set | C1, C2 | Ablation disrupts model; cannot assess compensation |
| E6 | Alternative-move patching | Two-branch puzzles with corrupted squares from alternative branch | Log odds reduction for main vs. alternative branch | Patching 1B/3B improves main branch accuracy | C3 (multi-branch evaluation) | ~600 puzzles from 4M; no cross-validation |
| E7 | Checkmate vs. non-checkmate ablation | Split puzzles by M/N prefix, compare L12H12 and L12H17 ablation effects | Log odds reduction | L12H12 stronger in checkmate; L12H17 stronger in non-checkmate | C1 | Hand-crafted puzzles used for some checkmate scenarios (Appendix G) |

### Research-Theme Gap Diagnosis

- **New Knowledge:** Moderately supported. The paper provides original evidence that look-ahead mechanisms in Leela are time-invariant pattern matchers. However, the novelty magnitude is incremental over Jenner et al. (2024) — the core discovery (backward information movement via specialized heads) was established there.
- **Reproducibility:** Weak. The undisclosed finetuning is the primary gap. Code availability is promised but not yet provided.
- **Impact on Practice/Understanding:** Moderate. The finding that L12H12 processes branches independently could inform architecture design for planning modules. The puzzle set notation is a reusable methodological contribution.

### Proposed Research Experiments (P0/P1/P2)

#### P0 Experiment: Finetuning Validation
- **Target Claim:** C1, C2, C3 (all)
- **Hypothesis:** The observed attention head behavior is not an artifact of finetuning.
- **Minimal Design:** Run L12H12 ablation on the original (unfinetuned) Leela model for puzzle set 112 and compare log odds reduction profiles.
- **Controls:** Same puzzles, same random seed.
- **Metrics:** Log odds reduction curves for 3rd→1st vs. other squares.
- **Success Criterion:** Curves are qualitatively similar (Spearman ρ > 0.7 across layers).
- **Estimated Cost:** ~1 day compute (RTX 3070Ti).
- **Expected Gain:** Reproducibility confidence — addresses most critical reviewer concern.

#### P0 Experiment: 7th-Move Statistical Quantification
- **Target Claim:** C2 — "model processes up to seventh move"
- **Hypothesis:** Probe accuracy for 7th-move square is significantly above random baseline.
- **Minimal Design:** Run probing with 5-fold cross-validation; report mean ± std accuracy per move. Compute permutation test p-value (trained vs. random probe).
- **Controls:** Random model baseline (same architecture, untrained).
- **Metrics:** Accuracy, p-value, effect size (Cohen's d).
- **Success Criterion:** p < 0.05 after Bonferroni correction for multiple moves.
- **Estimated Cost:** ~0.5 day compute.
- **Expected Gain:** Converts qualitative claim to quantitative evidence.

#### P1 Experiment: Alternative-Moves Robustness
- **Target Claim:** C3 — "model considers multiple move sequences"
- **Hypothesis:** Patching effects on alternative-branch squares are stable across random splits.
- **Minimal Design:** Bootstrap 90% confidence intervals for the log odds reduction of 1B and 3B squares across 1000 resamples of the 609 puzzles.
- **Controls:** Compare against patching a random irrelevant square.
- **Metrics:** CI width, coverage, effect size.
- **Success Criterion:** 90% CI does not include zero for at least one alternative branch square.
- **Estimated Cost:** ~1 day compute (rerunning patching for bootstraps).
- **Expected Gain:** Quantifies reliability of the alternative-moves claim.

#### P1 Experiment: Mechanism Identity Test
- **Target Claim:** "Similar mechanisms" for 3rd, 5th, 7th moves
- **Hypothesis:** L12H12 attention weight patterns are correlated across puzzles that share the same AAC pattern at different depths.
- **Minimal Design:** Extract L12H12 attention weights for 3-move and 5-move puzzles with AAC pattern; compute CKA similarity between attention matrices.
- **Controls:** Compare cross-depth similarity to within-depth similarity.
- **Metrics:** CKA similarity score.
- **Success Criterion:** Cross-depth CKA > 0.5 (within-depth CKA baseline).
- **Estimated Cost:** ~0.5 day compute.
- **Expected Gain:** Either validates or refines the "similar mechanisms" claim.

#### P2 Experiment: Feature Attribution for Context-Dependence
- **Target Claim:** C1 — "context-dependent look-ahead"
- **Hypothesis:** Board features (piece type under attack, king safety, material balance, check proximity) predict which attention heads are recruited.
- **Minimal Design:** Train a linear classifier to predict which attention head is most important (from ablation) based on board feature vector. Use SHAP values to identify top predictive features.
- **Controls:** Permutation test for feature significance.
- **Metrics:** Classification accuracy, top-3 feature importance.
- **Success Criterion:** Above-chance classification accuracy.
- **Estimated Cost:** ~1 day compute (feature extraction + training).
- **Expected Gain:** Transforms C1 from descriptive observation to explanatory account.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

**Rationale:** The paper presents a technically sound extension of prior work with well-executed interpretability analysis. Strengths include the multi-method approach, the novel puzzle set notation, and clear evidence of attention head specialization. However, the score is constrained by: (1) the undisclosed model finetuning creates a reproducibility wall that prevents full confidence in the results; (2) the headline 7th-move claim lacks statistical quantification; (3) the alternative-moves analysis rests on a tiny, heavily filtered dataset; (4) the "similar mechanisms" claim over-reaches the correlational evidence; and (5) the novelty is incremental over Jenner et al. (2024) and Karvonen (2024). The paper's primary value is methodological — the puzzle set notation and multi-branch patching adaptation are reusable contributions — rather than in fundamentally new discoveries about neural network planning.

**Post-Revision Target: [7.0, 7.5]/10**

**Rationale:** If the authors fully address the P0 issues (finetuning disclosure, 7th-move quantification), tone down over-claims, and add robustness validation for the alternative-moves analysis, the score could rise to 7.0-7.5. Reaching above 7.5 would require either direct mechanism identity evidence (CKA analysis) or a more explanatory account of the context-dependence finding beyond descriptive taxonomy.

### Page Coverage Audit

| Page | Section | Annotations | Coverage Status |
|------|---------|-------------|-----------------|
| 1 | Abstract + Introduction (P1-P3) | 4 | Covered |
| 2 | Introduction (P5, Contributions, Method preview) + Start of Setup | 3 | Covered |
| 3 | Setup (Model, Dataset, Analysis Techniques, Puzzle Notation) | 1 | Covered |
| 4 | Puzzle Set Notation (continued) | 1 | Covered |
| 5 | Results (starting squares, patching figures) | 0 | Skipped — contains figures with limited text |
| 6 | Results (probing, 7th-move claim, context-dependence) | 1 | Covered |
| 7 | Results (similar mechanisms, L12H12, other heads) | 1 | Covered |
| 8 | Results (alternative move sequences) | 1 | Covered |
| 9 | Related Work + Start of Conclusion | 1 | Covered |
| 10 | Conclusion, Reproducibility Statement | 1 | Covered |
| 11-12 | References | 0 | Skipped — reference list, no substantive content |
| 13-39 | Appendices A-H | 0 | Skipped — substantive but covered by main-text annotations referencing appendix findings |

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Problem: How does Leela encode future moves?]
    |
    ├── [C1: Context-dependent look-ahead]
    |       └── Evidence: Patching profiles differ across puzzle sets (112 vs 122 vs 123)
    |       └── Gap: What features drive these differences? (descriptive, not explanatory)
    |
    ├── [C2: Look-ahead extends to 5th/7th moves]
    |       └── Evidence: Probing accuracy for 7th-move > random (unquantified)
    |       └── Evidence: ACC < ABC < AAC pattern holds across depths
    |       └── Gap: No statistical tests; "similar mechanisms" claim is correlational
    |
    └── [C3: Multi-branch evaluation]
            └── Evidence: Patching 1B/3B shifts move preferences
            └── Evidence: L12H12 processes branches independently
            └── Gap: Dataset filtered from 4M to ~600 puzzles (0.015%)
```

### ASCII Diagram — Revision Strategy Roadmap

```text
Revision Priority Flow
    P0 (Submission-Blocking)
    ├── [Finetuning disclosure] → Reproducibility restored
    └── [7th-move quantification] → Headline claim verifiable
        │
        ▼
    P1 (High Impact)
    ├── [Alternative-moves robustness] → Prevents cherry-picking criticism
    ├── [Tone down over-claims] → Defensible rhetoric
    └── [Similar mechanisms → CIP or downgrade] → Evidence-claim alignment
        │
        ▼
    P2 (Quality Improvement)
    ├── [Validate puzzle set notation] → Stronger methodology
    ├── [Restructure Related Work] → Better novelty positioning
    └── [Feature attribution for context-dependence] → Explanatory depth
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
Mechanistic Interpretability of Game-Playing Models (Root)
│
├── Branch 1: Static Representation Discovery
│   ├── Leaf 1.1: World models in Othello-GPT
│   │   └── Li et al. (2023a), Nanda et al. (2023)
│   └── Leaf 1.2: Latent variable encoding in chess
│       └── Karvonen (2024)
│
├── Branch 2: Dynamic Planning/Reasoning Analysis
│   ├── Leaf 2.1: One-step look-ahead (3-move)
│   │   └── Jenner et al. (2024) ← This paper's direct predecessor
│   └── Leaf 2.2: Multi-step look-ahead (5th/7th moves)
│       └── Current manuscript (C2, C3)
│
├── Branch 3: Architectural & Training Studies
│   ├── Leaf 3.1: Efficient chess architectures
│   │   └── Czech et al. (2024)
│   └── Leaf 3.2: Search-free chess
│       └── Ruoss et al. (2024)
│
└── Branch 4: Broader AI Planning
    ├── Leaf 4.1: Multi-step planning in transformers
    │   └── Chen et al. (2021), Hao et al. (2023)
    └── Leaf 4.2: LLM planning/future-token anticipation
        └── Pal et al. (2023), Wu et al. (2024), Yao et al. (2024)
```

### Novelty Verification & Related-Work Matrix

(External literature verification unavailable in this run — paper_search not started due to Retrieval-Disabled Mode. Novelty/comparison conclusions are intentionally deferred for manual verification. The section below is a placeholder structure based on manuscript-internal evidence only.)

#### Contribution Novelty Verdict Board

| Claim ID | Author Claim | Verdict | Why | Confidence |
|----------|-------------|---------|-----|------------|
| C1 | Context-dependent look-ahead behavior | unclear | Descriptive observation; overlaps with Jenner et al. (2024) findings on puzzle-set differences; residual novelty lies in extending pattern taxonomy to 5th/7th moves | Low (manual verification needed) |
| C2 | Extended look-ahead to 5th/7th moves | unclear | Incremental extension of Jenner et al. (2024); 7th-move evidence is weak; "similar mechanisms" claim needs direct testing | Low (manual verification needed) |
| C3 | Model considers multiple move sequences | unclear | Creative experimental design but very small dataset; no known direct prior for this specific analysis in chess policy networks | Moderate (manual verification needed) |

#### Contribution-level Novelty Conclusion
**Deferred to manual literature verification.** Based on manuscript-internal evidence, the paper's novelty appears incremental over Jenner et al. (2024) in terms of core findings (extending horizon length, showing similar mechanisms), with genuine methodological novelty in the puzzle set notation and multi-branch patching adaptation. A thorough assessment requires comparing against Karvonen (2024), concurrent work on chess transformer representations, and the broader mechanistic interpretability literature on planning in game-playing models.

### References

This run operates in Retrieval-Disabled Mode (paper_search not started). External literature verification unavailable. Novelty/comparison conclusions are intentionally deferred. The paper's own reference list (pages 11-12) includes the relevant prior work, but independent verification was not performed in this run.