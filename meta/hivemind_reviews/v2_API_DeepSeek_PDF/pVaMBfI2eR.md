## Summary
# Final Review Report

## Summary

This paper proposes Fed-DPT (Federated Dual Prompt Tuning), a method that combines CLIP-based prompt tuning with federated learning to address domain shift across clients. The key idea is to equip each client with a domain-specific learnable text prompt, while using visual prompts with attention-based weighting to produce domain-adaptive text representations. The method freezes the CLIP backbone and only trains prompt tokens (~17K parameters), making it communication-efficient. Experiments on DomainNet, OfficeHome, and PACS show consistent improvements over prior prompt-based FL methods (PromptFL, FedCLIP) and conventional FL algorithms (FedAvg, FedProx). On DomainNet (6 domains, 345 classes), Fed-DPT achieves 68.4% average accuracy, outperforming PromptFL by 5.2%.

The core methodological contributions are: (C1) a dual prompt tuning framework combining per-domain text prompts with visual prompts in federated learning; (C2) an attention-based mechanism that weights text representations from different domains using visual prompt attention scores; (C3) a communication-efficient aggregation protocol that concatenates text prompts and averages visual prompts. However, several significant concerns exist regarding experimental fairness, formula correctness, statistical rigor, and privacy claims. (Note: novelty verification against external literature is deferred due to retrieval constraints in this review run.)

## Strengths
1. **Relevant Problem Formulation:** The paper addresses an important and realistic gap in federated learning—domain shift at the input feature level rather than label-skew heterogeneity. This is a genuine limitation of prior FL benchmarks that merits investigation.

2. **Parameter Efficiency:** Fed-DPT trains only ~17K prompt tokens while keeping the CLIP backbone frozen. This is a genuine communication-efficiency advantage over full-model FL methods and is well-motivated for cross-silo settings.

3. **Clean Ablation Design:** The ablation study (Table 3) systematically dissects the contribution of each component (visual-only, textual-only, domain-agnostic DPT, full Fed-DPT), clearly isolating the value of the domain-specific mechanism (+4.9% over domain-agnostic DPT).

4. **Informative Decentralization Experiment:** The 30-client experiment (Table 6) demonstrates robustness to further partitioning, showing that the method degrades gracefully when non-i.i.d. label distributions are added on top of domain shift.

5. **Consistent Gains Across Benchmarks:** The method shows positive results on all three datasets, with the largest gains on the most diverse benchmark (DomainNet), which is the primary target setting.

## Weaknesses
The following weaknesses are ranked by severity and research-value impact, from most critical to least critical.

1. **Critical — Optimizer Confound in Baseline Comparisons (Page 7 - Implementation Details):** Fed-DPT uses AdamW while all baselines (PromptFL, FedCLIP, FedAvg, FedProx) use SGD with different learning rates. This is a controlled-experiment violation that could fully or partially explain the reported gains, especially given that AdamW often converges faster for small-parameter prompt tuning. Without optimizer-matched baselines, the claimed superiority is not reliably attributable to the method design.

2. **Major — Formula Error in Eq. (7): Missing Negative Sign (Page 5 - Local Training):** The loss function `L = <fV, fT> / ||fV|| · ||fT||` is defined as a cosine similarity to be *minimized*. To align visual and text features, the cosine similarity must be *maximized*, meaning the loss should be the *negative* cosine similarity. The appendix Eq. (9) confirms this with `L2Loss = -sim(fv, ft)`, but the main text is inconsistent. If implemented as written, the model would learn to push representations apart rather than align them.

3. **Major — No Per-Seed Statistical Variance Reported (Page 7 - Main Results):** The paper reports "average numbers over three trials" but never reports per-seed standard deviations. The standard deviations cited (13.8% vs 16.5%) are across domains, not across runs, and conflate natural domain difficulty with statistical robustness. On PACS, the 0.5% gain over PromptFL could easily be within noise. Without per-seed variance, none of the claimed improvements are statistically verifiable.

4. **Major — Privacy Argument Overclaim (Page 6 - Discussion of Privacy):** The paper claims sharing prompts has "the same level of privacy-preserving capabilities as FedAvg" because prompts are model parameters. This conflates parameter-sharing with privacy protection. Per-domain prompts optimized on client-specific data can encode domain-level distributional information, and sharing unaggregated per-client prompts creates a stronger privacy leakage surface than FedAvg's averaged parameters.

5. **Major — One-Client-One-Domain Assumption (Page 4 - Problem Formulation):** The method assumes each client corresponds to exactly one domain (n clients = n domains). This is a strong restriction that prevents application to settings where a client's data spans multiple domains or multiple clients share the same domain. The paper does not adequately discuss this as a limitation.

6. **Major — Weak Justification for L2 Loss over Cross-Entropy (Page 15 - Appendix Convergence Analysis):** The argument that the CE denominator becomes constant for large class counts is unsubstantiated speculation. No quantitative comparison (L2 vs CE accuracy) is provided, and the convergence plot (Figure 2) is not analyzed. The L2 loss lacks the contrastive property that makes CE effective for multi-class classification.

7. **Major — Ceiling Effect on PACS (Page 8 - Table 2):** All CLIP-based methods exceed 95% on PACS, with Fed-DPT only 0.5% above PromptFL. This weakens the "consistently superior" claim and should be explicitly acknowledged.

8. **Minor — Abstract and Conclusion Use Promotional Language (Page 1, Page 9):** Phrases like "significant effectiveness," "remarkable achievement," and "impressive 14.8% improvement" are subjective and should be replaced with objective, bounded statements. The 14.8% improvement is over zero-shot CLIP (a weak baseline), not the strongest prior method.

## Key Issues
### Issue 1: Optimizer Confound Invalidates Direct Comparison (Critical)
**Evidence:** Page 7 - Implementation Details: "We train the ResNet-based models and prompt tokens by a SGD optimizer with 0.01 learning rate, 0.9 momentum, and 0.005 weight decay. Fed-DPT instead uses AdamW optimizer with ... 5e-4 learning rate, and 0.01 weight decay."
**Impact:** The primary empirical claim (Fed-DPT outperforms PromptFL by 5.2% on DomainNet) may be partially or wholly attributable to optimizer choice rather than the proposed domain-specific mechanism. This is the most serious threat to the paper's validity.
**Fix:** (a) Run PromptFL and FedCLIP with AdamW under the same hyperparameters and re-report. (b) Run Fed-DPT with SGD and report the delta. (c) If the optimizer difference is retained, provide controlled ablation and explicit justification.

### Issue 2: Eq. (7) Contains a Sign Error (Major)
**Evidence:** Page 5, Eq. (7): `L = <fV, fT> / ||fV|| · ||fT||`. Page 15, Eq. (9): `L2Loss = -sim(fv, ft)`.
**Impact:** The main-text equation is missing the negative sign, which means the published formula would cause gradient descent to *decrease* similarity rather than increase it. This contradicts the intended optimization direction.
**Fix:** Add the negative sign to Eq. (7) and add clarifying parentheses. Ensure cross-referencing between main text and appendix is consistent.

### Issue 3: Statistical Significance Not Established (Major)
**Evidence:** Page 7: "all reported results are average numbers over three trials" but only per-domain std (not per-seed std) is reported. On PACS, the gap over PromptFL is 0.5%.
**Impact:** Readers cannot assess whether reported improvements are robust or within noise. This is especially concerning for small-margin gains on OfficeHome (+1.9%) and PACS (+0.5%).
**Fix:** Report per-domain mean ± std over ≥3 seeds. For close comparisons, add paired significance tests.

### Issue 4: Privacy Analysis Is Insufficiently Rigorous (Major)
**Evidence:** Page 6, Section 4.4: "our method with shared prompts has the same level of privacy-preserving capabilities to FedAvg."
**Impact:** Sharing per-domain prompts (not averaged) creates a qualitatively different privacy risk from FedAvg's globally averaged parameters. The claim is misleading without formal privacy analysis.
**Fix:** Replace the unsupported claim with a nuanced discussion: acknowledge that prompts can encode domain statistics, cite relevant privacy literature, and suggest differential privacy as future work.

### Issue 5: Strong Assumption Limits Applicability (Major)
**Evidence:** Page 4, Section 4.1: "The n clients possess their own training data that originate from n distinct domains. In other words, each client stands for a specific domain."
**Impact:** The method cannot handle a client with multi-domain data or multiple clients sharing the same domain without modification. This substantially limits real-world deployment.
**Fix:** Explicitly state this as a limitation in both Section 4.1 and the Conclusion. Propose potential extensions (prompt clustering, domain discovery) as future work.

## Actionable Suggestions
### S1 (P0 — Must Fix): Run Optimizer-Matched Baseline Comparisons
**Problem:** Fed-DPT uses AdamW while PromptFL/FedCLIP use SGD, making comparisons unfair.
**Action:** Re-run PromptFL and FedCLIP with AdamW (lr=5e-4, weight_decay=0.01) using the same training schedule. Report full per-domain results in a new column. If Fed-DPT still outperforms, the claim is substantially strengthened. If the gap narrows or reverses, report honestly and adjust conclusions.
**Expected benefit:** Validates whether the domain-specific mechanism, not optimizer choice, drives improvements.

### S2 (P0 — Must Fix): Correct Eq. (7) Sign Error
**Problem:** Eq. (7) is missing the negative sign needed for cosine similarity maximization.
**Action:** Change Eq. (7) to `L = - <fV, fT> / (||fV|| · ||fT||)`. Add clarifying text that this is negative cosine similarity (alignment loss). Verify consistency with appendix Eq. (9).
**Expected benefit:** Ensures reproducibility and prevents implementation errors.

### S3 (P0 — Must Fix): Report Per-Seed Variance
**Problem:** No per-seed standard deviations are reported, making statistical significance unverifiable.
**Action:** For each table, report mean ± std over ≥3 seeds with different random seeds. For PACS and OfficeHome, add a paired significance test (e.g., corrected t-test) comparing Fed-DPT vs the strongest baseline on each domain.
**Expected benefit:** Allows reviewers and readers to assess whether improvements are robust.

### S4 (P1 — Should Fix): Revise Privacy Discussion
**Problem:** Privacy claim is overconfident and conflates parameter-sharing with privacy.
**Action:** Replace Section 4.4 with a more cautious discussion: acknowledge that per-domain prompts could encode domain-level statistics, note that the nearest-word decoding experiment suggests limited semantic leakage but does not constitute a formal guarantee, and suggest differential privacy integration as future work.

### S5 (P1 — Should Fix): Explicitly State One-Client-One-Domain Limitation
**Problem:** The strong assumption (n clients = n domains) is not discussed as a limitation.
**Action:** Add a paragraph in Section 4.1 acknowledging this assumption. In the Conclusion, propose extensions: (1) prompt clustering for multiple clients per domain, (2) domain discovery when a client spans multiple domains, (3) soft-assignment via attention.

### S6 (P1 — Should Fix): Improve L2 vs CE Justification
**Problem:** The convergence analysis argument is speculative without empirical support.
**Action:** Add a new table comparing L2 loss vs cross-entropy loss under identical hyperparameters, reporting accuracy on DomainNet. Discuss the trade-offs (L2 lacks contrastive property but may suffice when CLIP's embedding space is already well-separated). If the results favor L2, provide a more rigorous theoretical explanation.

### S7 (P2 — Nice to Have): Reframe PACS Results
**Problem:** Ceiling effect on PACS weakens the "consistently superior" narrative.
**Action:** Add a sentence acknowledging that PACS is near-saturated for CLIP-based methods and that the primary evidence for domain-shift robustness comes from DomainNet (6 domains, 345 classes).

### S8 (P2 — Nice to Have): Remove Promotional Language
**Action:** Replace "remarkable achievement," "impressive," "significant effectiveness," and "outstanding effectiveness" with objective, evidence-grounded statements throughout the paper.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows: (P1) FL background → (P2) Label-skew gap → (P3) Domain-shift FL scenario → (P4) Large-model degradation → (P5) CLIP/prompt introduction → (P6) Fed-DPT proposal + contributions. The main issues are: (a) the large-model degradation paragraph (P4) introduces a non-sequitur that is not directly addressed by the method; (b) the contribution paragraph (P6) is dense and lacks explicit claim numbering; (c) the overall narrative jumps from domain-shift motivation to CLIP/prompt without explicitly stating why prompt tuning is the right tool for domain shift.

### Selected Best Storyline (Candidate A: Problem-Solution Focused)

**Abstract Outline (4 sentences):**
- **S1 (Problem):** "Federated learning (FL) faces a critical challenge when client data originate from distinct visual domains: standard FL methods (e.g., FedAvg) suffer severe degradation under domain shift in input space, beyond mere label-skew heterogeneity."
- **S2 (Prior gap):** "Existing prompt-based FL methods (PromptFL, FedCLIP) treat all clients uniformly, missing the opportunity to model per-domain feature distributions."
- **S3 (Method):** "We propose Federated Dual Prompt Tuning (Fed-DPT), which freezes a CLIP backbone and introduces per-client learnable text prompts, coupled with visual prompts whose attention weights produce domain-adaptive text representations—requiring only ~17K trainable parameters per client."
- **S4 (Key result + bound):** "On DomainNet (6 domains, 345 classes), Fed-DPT achieves 68.4% average accuracy, outperforming PromptFL by 5.2% and zero-shot CLIP by 14.8%, with consistent gains on OfficeHome and PACS. These results demonstrate that explicit per-domain prompt personalization is an effective strategy for cross-silo FL under domain shift."

**Introduction Outline (6 paragraphs):**

- **P1 — Territory and Challenge:** "Federated learning enables collaborative model training without centralizing data, but real-world deployments face a fundamental challenge: client data often originate from distinct visual domains (e.g., sketches vs. photographs). Standard FL algorithms like FedAvg assume domain-agnostic feature distributions and consequently suffer large accuracy drops under such domain shift."
  - *Evidence anchor:* DomainNet statistics (6 domains, 345 categories).

- **P2 — Gap in Prior FL Simulation:** "Most prior FL research simulates heterogeneity by partitioning datasets by label distribution (non-i.i.d. labels). While convenient, this practice overlooks a critical real-world dimension: client data differ primarily in *input features* (domain), not just label distributions. This gap means that methods evaluated on label-skew benchmarks may not transfer to domain-shift settings."
  - *Evidence anchor:* Peng et al. (2020) domain-aware FL formulation.

- **P3 — Why Prompt Tuning is a Natural Fit:** "Freezing a strong pre-trained backbone and learning only lightweight prompts has emerged as an effective paradigm for adaptation. For domain-shift FL, prompt tuning offers two distinct advantages: (i) it preserves the pre-trained representation quality across domains, avoiding the optimization conflict that arises when training full models on heterogeneous data; (ii) the tiny parameter footprint (prompts) minimizes communication cost."
  - *Evidence anchor:* CLIP (Radford et al., 2021), CoOp (Zhou et al., 2021), VPT (Jia et al., 2022).

- **P4 — Limitation of Prior Prompt-Based FL Methods:** "Existing CLIP-based FL methods (PromptFL, FedCLIP) are domain-agnostic: they learn a single set of prompts shared across all clients, implicitly assuming that all domains can be represented by a single textual context. This assumption is violated when clients have systematically different visual styles, as each domain requires a distinct prompt to achieve optimal alignment."

- **P5 — Fed-DPT Proposal (Intuition):** "We propose Fed-DPT, which equips each client with its own domain-specific text prompt while visual prompts provide an attention-based mechanism to weight text representations from different domains according to the input image's domain affinity. This enables the model to produce domain-adaptive predictions without requiring explicit domain labels at inference time."

- **P6 — Contributions (Numbered, Bounded):** 
  "(1) A dual prompt tuning framework for FL that combines per-domain text prompts with learnable visual prompts, enabling domain-aware adaptation without full model fine-tuning."
  "(2) An attention-based aggregation mechanism that uses visual prompt attention scores to weight text features from multiple domains, requiring only cosine-similarity optimization."
  "(3) A communication-efficient aggregation protocol (concatenation for text prompts, averaging for visual prompts) that transmits only ~17K parameters per round."
  "(4) Empirical results on three benchmarks showing consistent improvements over domain-agnostic prompt FL methods, with the largest gains on the most diverse domain set."

### Storyline Alignment Check

- **Problem alignment:** The stated problem (domain shift in input space) directly maps to the solution (per-domain prompts + visual attention). ✓
- **Variable alignment:** "Domain-specific prompts," "visual prompt attention weights," and "domain-adaptive text representation" introduced here appear as the core method variables in Section 4. ✓
- **Contribution-evidence alignment:** The three numbered contributions map to: (1) ablation Table 3, (2) attention mechanism Eq. (5)-(6), (3) parameter count (Table 7, Appendix). Contribution (4) maps to Tables 1, 2, 6, 8. ✓

## Priority Revision Plan
### P0 — Publication-Critical (Must Fix Before Acceptance)

| # | Issue | Fix | Expected Impact | Effort |
|---|-------|-----|-----------------|--------|
| 1 | Optimizer confound | Run AdamW-matched baselines (PromptFL, FedCLIP) | Validates primary empirical claim | ~1 day GPU time |
| 2 | Eq. (7) sign error | Add negative sign, fix parentheses | Prevents implementation bug | <1 hour |
| 3 | Missing per-seed variance | Report mean±std over ≥3 seeds + significance tests | Enables statistical verification | ~2 days GPU time |

### P1 — High Priority (Should Fix for Stronger Paper)

| # | Issue | Fix | Expected Impact | Effort |
|---|-------|-----|-----------------|--------|
| 4 | Privacy overclaim | Rewrite Section 4.4 with honest caveats | Corrects misleading claim | 2-3 hours |
| 5 | One-client-one-domain assumption | Add limitation statement + extension proposals | Honestly bounds scope | 1-2 hours |
| 6 | L2 vs CE justification | Add empirical comparison table | Strengthens methodological rigor | ~1 day GPU time |

### P2 — Quality Improvement (Nice to Have)

| # | Issue | Fix | Expected Impact | Effort |
|---|-------|-----|-----------------|--------|
| 7 | PACS ceiling effect | Add acknowledgment + reframe narrative | Prevents overclaim | 1 hour |
| 8 | Promotional language | Replace hype with objective wording | Improves scientific tone | 1 hour |
| 9 | Abstract rewrite | Adopt the 4-sentence structure proposed in Storyline section | Improves first impression | 1 hour |

### ASCII Diagram — Revision Strategy Roadmap

```text
[P0: Optimizer Confound]
    -> Run AdamW baselines
    -> If gap persists: claim validated
    -> If gap narrows: adjust conclusions
    [Gate: All P0 items resolved before resubmission]

[P0: Eq. (7) Sign Error]
    -> Add negative sign
    -> Verify consistency with appendix Eq. (9)
    -> Document in revised manuscript

[P0: Per-Seed Variance]
    -> Rerun 3 seeds per experiment
    -> Report mean±std in Tables 1-2
    -> Add significance tests for close comparisons

[P1: Privacy + Assumptions + L2 Justification]
    -> Parallel workstream (text edits + one experiment)
    -> Can be done concurrently with P0 GPU runs

[P2: Language + Narrative Polish]
    -> Final pass before submission
    -> Apply storyline rewrite to Introduction
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (Data/Protocol/Baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------------------------------|---------|-------------|-----------------|-------------------|
| E1 | DomainNet benchmark | 6 domains, 345 classes, 200 epochs, n=6 clients | Per-domain test acc, avg | 68.4% avg, +5.2% over PromptFL | C1-C3 | Optimizer confound with baselines |
| E2 | OfficeHome benchmark | 4 domains, 65 classes, 200 epochs, n=4 clients | Per-domain test acc, avg | 82.9% avg, +1.9% over PromptFL | C1-C3 | Smaller gap; no variance reported |
| E3 | PACS benchmark | 4 domains, 7 classes, 200 epochs, n=4 clients | Per-domain test acc, avg | 97.2% avg, +0.5% over PromptFL | C1-C3 | Ceiling effect; marginal gain |
| E4 | Ablation: model components | DomainNet, 6 variants (Table 3) | Avg accuracy | Fed-DPT 68.4% vs Domain-Agnostic 63.5% | C2 (domain-specific mechanism) | No per-seed variance |
| E5 | Text prompt update ablation | 3 modes (Table 4a) | Avg accuracy | w/ mtm 68.4, w/o mtm 66.2, train all 64.0 | C2 (momentum update) | No ablation for alpha values |
| E6 | Visual prompt update ablation | 3 modes (Table 4b) | Avg accuracy | average 68.4, split w/ mtm 68.3, split w/o mtm 67.5 | C2 (averaging strategy) | Marginal differences |
| E7 | Prompt length ablation | 3 lengths (Table 4c) | Avg accuracy | 4: 67.5, 16: 68.4, 32: 68.0 | C1 (design choice) | Weak conclusion |
| E8 | Communication frequency | 3 settings (Table 4d) | Avg accuracy | 0.5: 68.4, 1: 68.4, 2: 67.9 | C3 (efficiency claim) | Small effect |
| E9 | Decentralization (30 clients) | DomainNet, Dirichlet split (Table 6) | Avg accuracy | Fed-DPT 66.9 (-1.5%), FedAvg 51.6 (-3.6%) | C3 (robustness to non-i.i.d. labels) | No per-seed variance |
| E10 | Few-shot learning | DomainNet, 1/2/4/8/16-shot (Table 8) | Avg accuracy | Fed-DPT best at all shots | C1 (parameter efficiency advantage) | Only tested on DomainNet |
| E11 | Fine-tuning comparison | DomainNet, CLIP backbone (Table 7) | Acc, learnable params | Fed-DPT: 68.4% with 16.9K params vs full FT 57.6-58.1% | C3 (communication efficiency) | Full FT on CLIP may need different LR |

### Research-Theme Gap Diagnosis

1. **New Knowledge (partially supported):** The core insight—per-domain text prompts improve CLIP-based FL under domain shift—is demonstrated. However, the critical P0 confound (optimizer mismatch) undermines confidence in the attribution of gains to this insight.

2. **Reproducibility (weak):** The formula error in Eq. (7), the missing implementation details (per-seed variance, optimizer configuration for baselines), and the ambiguous L2 vs CE justification reduce reproducibility.

3. **Impact on Practice/Understanding (uncertain):** The strong one-client-one-domain assumption and the lack of formal novelty verification (deferred) make it difficult to assess whether the method changes practice beyond the specific cross-silo setting studied.

### Proposed Research Experiments

#### P0 Experiment: Optimizer-Matched Baseline Comparison
- **Target Claim:** C1 (Fed-DPT outperforms domain-agnostic prompt FL methods)
- **Hypothesis:** The +5.2% gain on DomainNet is primarily due to domain-specific prompts, not optimizer differences
- **Minimal Design:** Run PromptFL and FedCLIP with AdamW (lr=5e-4, weight_decay=0.01) for 200 epochs on DomainNet, keeping all other settings identical
- **Controls:** Same seeds, same data splits, same CLIP backbone
- **Metrics:** Per-domain test accuracy, mean±std over 3 seeds
- **Success Criterion:** If Fed-DPT still outperforms by ≥3% on DomainNet after optimizer match, the claim is substantially validated. If the gap drops below 2%, the paper needs major conclusion revision.
- **Estimated Cost:** ~1-2 GPU days
- **Expected Gain:** Resolves the most critical threat to validity

#### P1 Experiment: L2 vs Cross-Entropy Empirical Comparison
- **Target Claim:** Method design (L2 loss choice)
- **Hypothesis:** L2 loss produces comparable or better accuracy than CE on this task
- **Minimal Design:** Replace L2 loss with CE loss in Fed-DPT, run on DomainNet under identical settings. Report both accuracy and convergence plots.
- **Controls:** Same optimizer (AdamW), same prompt length, same schedule
- **Metrics:** Test accuracy, epochs to convergence
- **Success Criterion:** L2 accuracy within 0.5% of CE (or better); faster convergence confirmed
- **Estimated Cost:** ~0.5 GPU day
- **Expected Gain:** Replaces speculative argument with empirical evidence

#### P1 Experiment: Per-Seed Variance and Significance Report
- **Target Claim:** All empirical claims
- **Hypothesis:** Fed-DPT's improvements are statistically significant
- **Minimal Design:** Rerun Tables 1, 2, 3, 6 with 3 different random seeds, report mean±std. Add paired bootstrap test for Fed-DPT vs strongest baseline per domain.
- **Controls:** Same hyperparameters per run
- **Metrics:** Per-domain accuracy ± std, p-values for head-to-head comparisons
- **Success Criterion:** Gains remain positive across all 3 seeds; p<0.05 for DomainNet gains
- **Estimated Cost:** ~2-3 GPU days
- **Expected Gain:** Enables statistical verification of claimed improvements

#### P2 Experiment: Relaxing the One-Client-One-Domain Assumption
- **Target Claim:** Applicability/generalizability
- **Hypothesis:** Prompt averaging or clustering can handle multi-client-per-domain settings
- **Minimal Design:** On DomainNet, assign 2 clients to the same domain (6 domains → 12 clients). Compare: (a) separate prompts per client, (b) averaged prompts for same-domain clients, (c) k-means clustering of prompts.
- **Controls:** Same total compute, same communication rounds
- **Metrics:** Per-domain accuracy, client-level personalization quality
- **Success Criterion:** Averaging/clustering approaches lose ≤1% accuracy compared to the default one-client-per-domain setup
- **Estimated Cost:** ~1-2 GPU days
- **Expected Gain:** Demonstrates method's scope beyond the strong assumption

### ASCII Diagram — Experiment Upgrade Plan

```text
Stage 1 (P0 — Before Resubmission):
  ├── Run AdamW-matched PromptFL/FedCLIP on DomainNet
  ├── Fix Eq. (7) sign error in manuscript
  └── Rerun 3 seeds for Tables 1, 2, 3, 6
      └── Report mean±std + significance tests

Stage 2 (P1 — Concurrent with Stage 1):
  ├── L2 vs CE comparison table
  └── Privacy discussion rewrite
      └── One-client-one-domain limitation statement

Stage 3 (P2 — Before Final Polish):
  ├── Multi-client-per-domain experiment
  ├── Reframe PACS ceiling effect
  └── Apply storyline rewrite to Abstract + Introduction
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

Reasoning: The paper addresses a relevant problem (domain shift in FL) with a clean methodological idea (per-domain text prompts + visual attention). The ablation study is well-designed and demonstrates the value of the domain-specific mechanism. However, the score is constrained by:

- **Critical issue (optimizer confound)** that directly threatens the primary empirical claim. Without optimizer-matched baselines, the reported gains cannot be reliably attributed to the method.
- **Formula error in Eq. (7)** that would cause incorrect optimization if implemented as written.
- **Missing statistical variance** across all experiments, making significance unverifiable.
- **Overclaimed privacy and novelty language** that needs substantial revision.
- **Strong assumptions** about the one-client-one-domain mapping that limit practical applicability.
- **Novelty verification deferred** (external retrieval unavailable in this run), so the score reflects manuscript-grounded assessment only.

These issues are fixable (P0 items are concrete and bounded), which is reflected in the post-revision target.

**Post-Revision Target: [6.5, 7.5] / 10**

If all P0 items are fully resolved (optimizer-matched baselines confirm the core claim, Eq. (7) is corrected, per-seed variance is reported and supports significance), and P1 items are addressed (privacy rewrite, limitation discussion, L2 vs CE justification), the paper could reach 6.5-7.5/10. The upper bound is constrained by the inherent limitation of the one-client-one-domain assumption and the lack of external novelty verification (which would require a separate literature study).

**Scoring Breakdown:**

| Dimension | Score (0-10) | Rationale |
|-----------|-------------|-----------|
| Research Value / Problem Importance | 7 | Domain shift in FL is a genuine and timely problem |
| Novelty / Methodological Innovation | 6 | Per-domain prompts + attention weighting is a reasonable extension but natural given existing tools |
| Validity / Soundness | 4 | Critical confound (optimizer mismatch) and formula error reduce confidence |
| Reproducibility | 4 | Missing per-seed variance, sign error, ambiguous L2 justification |
| Presentation / Clarity | 6 | Generally clear but promotional language detracts; related work is list-like |
| Overall | 5.5 | Weighted average prioritizing validity and novelty