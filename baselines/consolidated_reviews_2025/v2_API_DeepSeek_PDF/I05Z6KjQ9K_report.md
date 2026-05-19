## Summary
# Final Review Report

## Summary

This paper studies the problem of cross-prompt adversarial attacks on vision-language models (VLMs). The authors identify that when generating visual adversarial perturbations using multiple prompts, the optimization process suffers from severe non-stationarity (fluctuating attack success rates across iterations). They attribute this phenomenon to overfitting and propose Gradient Regularization-based Cross-Prompt Attack (GrCPA), which clips extreme gradient values in the Attention and MLP components of LLM Transformer blocks during backpropagation. Evaluated on Flamingo, BLIP-2, LLaVA, and InstructBLIP across VQA, classification, and captioning tasks, GrCPA achieves consistent improvements over prior methods (CroPA, Multi-P, Single-P) with average ASR gains of 4-8 absolute points.

**Core contributions (from manuscript):** (1) identifying and characterizing optimization non-stationarity in multi-prompt VLM attacks; (2) a gradient regularization method for cross-prompt transferability; (3) experimental validation. However, due to Retrieval-Disabled Mode (external paper search unavailable), novelty claims (especially "first" identification) cannot be externally verified and are marked as deferred.

**Key strengths:** Clear problem identification (cross-prompt brittleness), simple and intuitive method (gradient extreme-value clipping), comprehensive evaluation across 4 models and 4 task types, and ablation studies showing the contribution of both visual and textual regularization.

**Key weaknesses:** (1) Results lack variance reporting and statistical significance testing, weakening empirical claims; (2) Overfitting diagnosis is asserted without direct evidence (no loss landscape or gradient norm analysis); (3) Iteration count inconsistency (10,000 stated in Introduction vs 1000 used in experiments); (4) λ ablation results contradict the "low-level feature preservation" hypothesis; (5) Conclusion overgeneralizes beyond evidence; (6) Contribution Claim 1 ("first") is unverifiable; (7) No defense evaluation or OOD testing; (8) Cross-model transferability is very weak (<10% ASR).

## Strengths
**S1. Well-motivated problem formulation.** The paper identifies a genuine practical issue: adversarial perturbations optimized for one prompt fail under different prompts, which is critical for VLM deployment where users naturally vary their language. The three empirical observations (non-stationarity, loss sensitivity, failure of single-modal transfer methods) provide concrete motivation for the proposed approach.

**S2. Simple and computationally lightweight method.** GrCPA's gradient regularization—zeroing the k largest and smallest gradient values per token during backpropagation—is simple to implement, requires negligible overhead (modifying only 2/d gradient entries per token with k=1), and can be integrated into existing attack pipelines. The ablation in Table 4 shows that adding GR to Single-P and Multi-P consistently improves ASR, demonstrating the method's versatility.

**S3. Comprehensive evaluation scope.** The paper evaluates on four diverse VLMs (OpenFlamingo-9B, BLIP-2 OPT-2.7B, LLaVA-1.5-7B, InstructBLIP-Vicuna-7B) across four task types (VQA general, VQA specific, classification, captioning) with multiple target answers. This breadth strengthens confidence that the findings are not model- or task-specific.

**S4. Informative ablations.** The ablation studies (Tables 4-6) decompose the contribution of gradient regularization, the role of single-modality vs dual-modality regularization, and the sensitivity to the layer proportion λ. Table 5's finding that dual-modality regularization outperforms either visual-only or text-only regularization is a practically useful design insight.

**S5. Stability analysis.** Table 2 provides a quantitative measure of attack stability (consistency across iteration checkpoints), which goes beyond standard ASR reporting and addresses the non-stationarity problem directly.

## Weaknesses
**W1. Missing statistical evidence for all empirical claims (High severity).** All results (Tables 1-6, Figure 3) are reported as single point estimates without variance, confidence intervals, or significance tests. Reported gains over CroPA are often 3-8 absolute points; without multi-seed variance, these could be within noise range. This is the most consequential weakness because it undermines the paper's central empirical contribution. [Anchored: Page 6-7 - Experimental Results and Table 1]

**W2. Overfitting diagnosis is asserted without direct evidence (High severity).** The paper attributes non-stationarity to "overfitting" but provides no direct evidence: no loss landscape analysis, no gradient norm tracking, no train/test gap monitoring. The term "overfitting" is used loosely to describe optimization instability, which could equally be caused by noisy gradients, multi-objective conflict, or mode switching. [Anchored: Page 2 - Introduction, paragraph beginning "An intuitive method to enhance across-prompts transferability"]

**W3. Iteration count inconsistency (Medium severity).** The Introduction states "adversarial attacks on VLMs usually require a large number of iterations, such as 10,000, to succeed" (Page 2), but the experimental setup uses only 1000 iterations (Page 6, Section 4.1). This discrepancy is not explained and undermines the motivation for the overfitting diagnosis. [Anchored: Page 2 - Introduction vs Page 6 - Experimental Settings]

**W4. λ ablation contradicts the "low-level features" hypothesis (Medium severity).** Table 6 shows ASR varying only from 0.863 to 0.875 across λ=1 (all layers) to λ=1/6 (last 1/6 of layers). The flat trend contradicts the claim (Section 3.3) that preserving low-level features by regularizing only high layers is beneficial. If that hypothesis held, λ=1 should perform substantially worse than λ=1/6. [Anchored: Page 9 - Ablation Studies, Table 6]

**W5. Mathematical notation imprecision (Medium severity).** Equation (3) uses "imax,imin = arg max_k G, arg min_k G" without clearly defining the operation. The notation is ambiguous about whether imax and imin are single indices or sets, and whether top-k and bottom-k are guaranteed disjoint. [Anchored: Page 5 - Method, Equation (3)]

**W6. Conclusion overgeneralizes (Medium severity).** The conclusion claims VLMs "can be easily attacked" and calls for "thoroughly evaluate the adversarial robustness...especially in life-critical scenarios" based on experiments limited to 4 models, 1 dataset (MS-COCO), 1 perturbation budget, white-box access only, and no defense evaluation. [Anchored: Page 9 - Conclusion]

**W7. Related work reads as a chronological list (Low severity).** The adversarial transferability paragraph lists methods in chronological order rather than organizing them by mechanism (gradient optimization vs input augmentation). This reduces readability and makes it harder for readers to position the paper. [Anchored: Page 3 - Related Work, "Adversarial Transferability"]

**W8. Citation density impairs readability (Low severity).** Paragraph 2 of the Introduction (Page 1) contains 14+ citations in ~6 sentences, making it hard to extract the core motivational claim. [Anchored: Page 1 - Introduction, second paragraph]

## Key Issues
This section consolidates the most impactful defects identified during audit, ordered by severity (highest first).

### Issue 1 (Critical/Major): Absence of Statistical Rigor in All Empirical Results
**Severity:** Major | **Location:** Page 6-7, Tables 1-4 and Figure 3

All results are single-run point estimates without variance, confidence intervals, or significance tests. Gains over CroPA are often 3-8 absolute ASR points; without multi-seed reporting, these differences cannot be distinguished from noise. This is the single most impactful weakness because: (a) the paper's central claim is empirical ("GrCPA outperforms previous SOTA"), (b) the absolute ASR values are high (0.75-0.99) where ceiling effects may compress differences, (c) Table 2's "stability" measure itself has no variance. **Fix required:** Report mean ± std over ≥3 seeds; add McNemar's test or paired bootstrap comparing GrCPA vs CroPA for each task-target combination.

### Issue 2 (Major): Unsupported Overfitting Diagnosis
**Severity:** Major | **Location:** Page 2 - Introduction, paragraph starting "An intuitive method"

The paper attributes non-stationarity to "overfitting" but provides no direct evidence. Alternative explanations include: gradient noise from sampling different prompts each step, multi-objective conflict between prompts, or mode switching in the LLM's discrete output space. **Fix required:** (a) Provide gradient norm analysis across iterations; (b) Compare training-set vs held-out-prompt ASR to measure true overfitting; (c) Show loss landscape visualizations or at minimum gradient variance plots.

### Issue 3 (Major): Iteration Count Discrepancy
**Severity:** Major | **Location:** Page 2 (line 77: "10,000 iterations") vs Page 6 (Section 4.1: "1000 iterations")

The Introduction motivates overfitting by citing the need for "10,000 iterations," but experiments use only 1000. If 1000 iterations suffice, the 10,000 claim is misleading. If 10,000 is needed, the experiments are not comparable. **Fix required:** Either align the Introduction claim with the experimental setup, or add experiments showing that the non-stationarity persists at 10,000 iterations.

### Issue 4 (Major): Contradictory Ablation Evidence for Low-Level Feature Hypothesis
**Severity:** Major | **Location:** Page 9 - Ablation, Table 6

Table 6 shows ASR is essentially flat (range 0.012) across λ=1 to λ=1/6. This directly contradicts the paper's claim (Section 3.3, citing Deng et al. 2023) that regularizing only high-level layers preserves low-level features and improves transferability. If true, λ=1 would substantially underperform λ=1/6. **Fix required:** Either (a) acknowledge that the low-level feature preservation hypothesis is not supported by evidence and remove the claim, or (b) provide an alternative explanation for the λ-insensitivity.

### Issue 5 (Major): Unverifiable Novelty Claim
**Severity:** Major | **Location:** Page 3 - Contribution Claim 1

Claim 1 states "To the best of our knowledge, we first identify the non-stationary phenomenon." Due to Retrieval-Disabled Mode, external literature verification is unavailable. CroPA (Luo et al., 2024a), cited in the paper itself, addresses cross-prompt attacks and may have implicitly observed similar instability. **Fix required:** Add a scoping qualifier (e.g., "To our knowledge, we are the first to explicitly characterize and attribute optimization non-stationarity to overfitting in multi-prompt VLM attacks") or remove "first" pending literature verification.

## Actionable Suggestions
### Suggestion 1: Add Multi-Seed Variance and Significance Testing (Must)
**Target:** All main results (Tables 1-4, Figure 3)
**Action:** Run each experiment configuration with at least 3 random seeds. Report mean ± std. Add McNemar's test (paired, per-image) comparing GrCPA vs CroPA for each (task, target-answer) combination. Report the proportion of configurations where GrCPA is statistically significantly better (p<0.05).
**Expected benefit:** Transforms empirical claims from correlational to statistically grounded.

### Suggestion 2: Provide Direct Evidence for Overfitting Diagnosis (Must)
**Target:** Page 2, paragraph starting "An intuitive method"
**Action:** Add an analysis paragraph with: (a) gradient L2 norm across iterations for Single-P vs GrCPA, (b) ASR on held-out prompts vs training prompts to measure the overfitting gap, (c) comparison with a known regularization baseline (e.g., weight decay or dropout on gradients) to confirm the overfitting hypothesis.
**Expected benefit:** Turns an asserted hypothesis into a validated diagnosis, strengthening the paper's theoretical contribution.

### Suggestion 3: Resolve Iteration Count Discrepancy (Must)
**Target:** Page 2 (line 77) vs Page 6 (Section 4.1)
**Action:** Either (a) change "10,000" to "1,000" in the Introduction and add a note that experiments found 1,000 iterations sufficient, or (b) add a supplementary experiment at 10,000 iterations showing that non-stationarity persists and GrCPA still helps. Option (a) is simpler and sufficient.
**Expected benefit:** Eliminates a self-contradiction that could confuse reviewers.

### Suggestion 4: Reconcile λ Ablation with Low-Level Feature Hypothesis (Must)
**Target:** Page 9, Table 6 and Page 5, Section 3.3 "Preserving low-level features"
**Action:** Either (a) remove or qualify the claim that "preserving low-level features" is the mechanism, since Table 6 shows λ has negligible effect; or (b) add an experiment measuring feature-level differences (e.g., CKA similarity between regularized and unregularized features at different layers) to test the hypothesis directly.
**Expected benefit:** Removes a contradictory claim that weakens the paper's internal consistency.

### Suggestion 5: Reposition Novelty Claims (Must)
**Target:** Page 3, Contribution Claim 1
**Action:** Replace "we first identify the non-stationary phenomenon" with a scoped claim (e.g., "We provide the first explicit characterization and attribution of optimization non-stationarity to overfitting in multi-prompt VLM attacks"). Add a sentence acknowledging CroPA (Luo et al., 2024a) as concurrent work on cross-prompt attacks and clearly delineating the difference (gradient regularization vs max-min optimization).
**Expected benefit:** Makes novelty claims defensible without requiring external verification.

### Suggestion 6: Bound Conclusion Claims (Nice-to-have)
**Target:** Page 9, Conclusion
**Action:** Replace the generic call to action with three concrete subsections: (1) validated findings (what was shown, under what conditions), (2) limitations (cross-model transfer <10%, single dataset, no defenses), (3) recommended robustness evaluation protocol (diverse prompts, multi-seed reporting, GrCPA-style attacks as one evaluation tool).
**Expected benefit:** Improves scientific credibility and provides actionable guidance to practitioners.

### Suggestion 7: Restructure Related Work by Mechanism (Nice-to-have)
**Target:** Page 3, "Adversarial Transferability" paragraph
**Action:** Split into two sub-paragraphs: (1) gradient optimization methods (FGSM, I-FGSM, PGD, MI-FGSM) and (2) input augmentation methods (DIM, SIM, TIM). End with a clear takeaway sentence explaining why neither family addresses the cross-prompt VLM challenge.
**Expected benefit:** Makes the literature positioning clearer and easier to follow.

### Suggestion 8: Tighten Equation (3) Notation (Nice-to-have)
**Target:** Page 5, Equation (3)
**Action:** Replace the ambiguous notation with: "Let I_top = argsort(-G)[:k] and I_bottom = argsort(G)[:k]. Set G[i] = 0 for all i in I_top ∪ I_bottom."
**Expected benefit:** Eliminates implementation ambiguity.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current paper follows: Big Picture (VLM capabilities) → Vulnerability → White-box vs Black-box → Cross-prompt problem → Three issues with naive multi-prompt → Proposed GrCPA → Experiments → Conclusion.

**Problems with current storyline:**
1. The first two paragraphs of the Introduction do not lead directly to the cross-prompt problem; they discuss general VLM capabilities and general adversarial attacks first, delaying the paper's specific focus.
2. The transition from "three issues with naive approach" to "our method" is abrupt—the overfitting diagnosis connects them, but the connection is not clearly stated.
3. Contribution Claim 3 ("new perspective") is too vague to serve as a memorable takeaway.

### Recommended Storyline (Candidate A — Problem-Driven)

This is the recommended option for revision.

**Abstract Outline (4-5 sentences):**
- S1 (Problem): "Large vision-language models (VLMs) are vulnerable to visual adversarial perturbations, but the effectiveness of these perturbations depends heavily on the text prompt—a critical limitation when users vary prompts during deployment."
- S2 (Challenge): "We find that naively optimizing a single perturbation over multiple prompts leads to severe optimization non-stationarity, with attack success rates fluctuating drastically across iterations, which we attribute to overfitting."
- S3 (Gap): "Existing single-modal transferability enhancement methods (MI-FGSM, DIM, Variance Tuning) fail to improve cross-prompt transfer in VLMs."
- S4 (Method): "We propose GrCPA, which clips extreme gradient values in the Attention and MLP components of LLM Transformer blocks during backpropagation, jointly regularizing visual and textual gradient pathways."
- S5 (Result + Bound): "On Flamingo, BLIP-2, LLaVA and InstructBLIP, GrCPA improves average cross-prompt attack success rate by 4-8 absolute points over CroPA (from 0.74 to 0.78+). These gains are consistent across four task types and six target answers."

**Introduction Outline (5 paragraphs):**

**P1 — The cross-prompt vulnerability (revised role):**
*Hook:* State the specific problem: adversarial perturbations that work for one prompt fail under different prompts.
*Claim:* This prompt-sensitivity is a critical but understudied vulnerability in VLM deployment.
*Evidence:* Cite Cui et al. (2023) and motivate why this matters for security evaluation.
*Transition:* "In this paper, we systematically study this cross-prompt vulnerability."

**P2 — Why naive multi-prompt optimization fails (revised role):**
*Problem:* The natural approach—optimizing over multiple prompts jointly—suffers from three issues.
*Issue (a):* Non-stationarity (ASR fluctuates wildly). Present Figure 1 evidence and hypothesize overfitting.
*Issue (b):* Loss computation is subtle (teacher forcing fails; only output-token loss works).
*Issue (c):* Prior single-modal transferability methods degrade performance (cite Table 7 in appendix).
*Transition:* "These observations motivate a method that directly addresses overfitting in the Transformer blocks."

**P3 — GrCPA method intuition (new, currently missing):**
*Intuition:* "We hypothesize that extreme gradient values in deep Transformer layers correspond to features overly specialized to individual prompt-image pairs. Clipping these extreme values should force the optimization to rely on features shared across prompts."
*High-level description:* "GrCPA performs gradient regularization during backpropagation: for each token in each Attention and MLP layer, it identifies the k largest and smallest gradient values and sets them to zero."
*Why this differs from prior work:* "Unlike CroPA which uses max-min optimization over text perturbations, GrCPA operates purely on gradient statistics, making it simpler and adding negligible overhead."
*Transition:* "We now formalize this approach."

**P4 — Evaluation scope and key result:**
*Setup:* "We evaluate on Flamingo, BLIP-2, LLaVA-1.5, and InstructBLIP across VQA (general and specific), image classification, and captioning tasks, using 100 prompts per sample."
*Key finding:* "GrCPA consistently outperforms Single-P, Multi-P, and CroPA across all target answers and tasks, with the largest gains on captioning (where cross-prompt transfer is hardest)."
*Stability result:* "GrCPA also improves optimization stability (consistency from 0.57 to 0.62 in Table 2)."

**P5 — Contributions (revised):**
1. "We identify and characterize optimization non-stationarity as a key barrier in multi-prompt VLM attacks, providing evidence linking it to overfitting and showing that existing single-modal methods are ineffective."
2. "We propose GrCPA, a gradient regularization method that clips extreme gradient values in Transformer blocks, improving cross-prompt transferability with minimal computational overhead."
3. "Through systematic ablations, we demonstrate that jointly regularizing visual and textual gradient pathways is critical for cross-prompt transfer, offering a practical principle for future VLM attack design."

### Candidate B (Method-Focused — Alternate)

Follow the same structure as Candidate A but lead with the method insight in P1:
**P1:** "The core challenge in cross-prompt VLM attacks is overfitting: the perturbation becomes overly specialized to the prompts used during optimization." Then explain why this overfitting happens (deep Transformer blocks, large number of iterations), then present GrCPA as the solution. This structure works better for an audience familiar with adversarial attacks but less familiar with VLMs.

### Recommended Choice: Candidate A

Candidate A is recommended because it leads with the practical problem (prompt brittleness) that is accessible to a broader audience, then builds up to the technical solution. This aligns with ICLR's interdisciplinary readership.

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[Problem]                                             [Fix]                                           [Expected Gain]
                                                    
W1: No statistical rigor                             Run 3+ seeds, add significance tests           Empirical claims become statistically grounded
    in results (Tables 1-6)                         → Report mean±std, McNemar's test              → Core finding defensible against reviewer challenge

W2: Overfitting diagnosis                           Add gradient norm analysis, train/holdout       Turns asserted hypothesis into validated diagnosis
    asserted without evidence                       prompt ASR gap, compare vs weight decay         → Strengthens theoretical contribution

W3: Iteration count                                  Change Intro "10,000" to "1,000" or            Eliminates self-contradiction
    discrepancy (10k vs 1k)                         add 10k experiment                             → Improves consistency

W4: λ ablation contradicts                          Remove/qualify "low-level features" claim,      Removes contradictory evidence
    low-level feature hypothesis                    or add CKA feature analysis                     → Internal consistency restored

W5: Imprecise Eq.(3) notation                       Replace with argsort-based notation             → Implementation ambiguity resolved

W6: Conclusion overgeneralization                   Restructure: validated findings → limitations   → Credibility improved
                                                    → recommended protocol

W7-W8: Writing polish                               Restructure related work, reduce citation       → Readability improved
                                                    density
```

### Priority Order (P0/P1/P2)

| Priority | Item | Effort | Impact | Action |
|----------|------|--------|--------|--------|
| P0 (Must) | W1: Statistical rigor | Medium (re-run experiments with 3 seeds) | High (validates all empirical claims) | Run 3-seed experiments, add significance tests |
| P0 (Must) | W3: Iteration discrepancy | Low (text change) | High (removes self-contradiction) | Align number in Introduction |
| P0 (Must) | W5: Equation notation | Low (text change) | Medium (eliminates ambiguity) | Replace with precise notation |
| P1 (Should) | W2: Overfitting diagnosis | Medium (add analysis paragraph) | High (strengthens theoretical contribution) | Add gradient norm and held-out analysis |
| P1 (Should) | W4: λ contradiction | Medium (revise claim or add analysis) | Medium (internal consistency) | Qualify or remove low-level features claim |
| P1 (Should) | W6: Conclusion revise | Low (restructure paragraph) | Medium (improves credibility) | Add limitations section |
| P2 (Nice) | W7: Related work restructure | Low | Low-Medium (readability) | Reorganize by mechanism |
| P2 (Nice) | W8: Citation density | Low | Low (presentation) | Reduce to 2-3 cites per claim |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (Data/Split/Protocol/Baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|-------------|-----------------|-------------------|
| E1 (Table 1) | Compare GrCPA vs Single-P, Multi-P, CroPA on Flamingo across 6 target answers | MS-COCO val, 4 tasks (VQA-gen, VQA-spec, Classif, Caption), 100 prompts, L∞ 16/255, 1000 iter | ASR (point est.) | GrCPA highest avg ASR for all targets (e.g., 0.78 vs 0.74 CroPA for "unknown") | C2: GrCPA improves cross-prompt transfer | Single run, no variance; ceiling effects on VQA-spec (0.99) |
| E2 (Table 2) | Measure attack stability (output consistency at 900/925/950/975/1000 steps) | Same as E1 | Consistency rate | GrCPA 0.62 vs CroPA 0.57 avg | C2: GrCPA improves stability | 5 checkpoints only; no variance |
| E3 (Table 3) | Impact of prompt count (1,5,10,50,100) on BLIP-2 | Same as E1 but BLIP-2, target "unknown" | ASR | ↑prompts → ↑ASR; GrCPA best at all counts | C2: GrCPA effective across prompt counts | Only 1 target, 1 model |
| E4 (Figure 3) | Convergence wrt iterations | Same as E1, 10 prompts, up to 1800 iter | ASR curve | GrCPA stabilizes after 1000 iter | C2: Computational efficiency | Only shown for 1 setting |
| E5 (Table 4) | Ablate gradient regularization on Single-P and Multi-P | Same as E1, Flamingo | ASR | Single-P(GR) 0.27 vs Single-P 0.22; Multi-P(GR) 0.78 vs Multi-P 0.62 | C2: GR provides cross-prompt transfer | Single run |
| E6 (Table 5) | Ablate single-modality vs dual-modality regularization | Same as E1, 100 prompts, BLIP-2 | ASR | Dual (0.96) > Image-only (0.92) > Text-only (0.89) | C2: Both modalities needed | Single run |
| E7 (Table 6) | Ablate λ (layer proportion) | Same as E1, BLIP-2 | ASR | Flat across λ (0.863-0.875) | - | Contradicts low-level feature hypothesis |
| E8 (Appendix A.5) | Generalization to LLaVA-1.5 and InstructBLIP | Same as E1 but LLaVA/InstructBLIP | ASR | GrCPA 0.98/0.97 | C2: Generalizes | Single run, 2 models |
| E9 (Appendix A.7) | Cross-model transfer (BLIP2→InstructBLIP) | Same as E1 | ASR | All methods <10% | - | Very weak transfer |
| E10 (Appendix A.8) | Defense: random rotation | Same as E1 | ASR | GrCPA 0.71 under rotation vs 0.74 no defense | - | Only 1 defense tested |

### Research-Theme Gap Diagnosis

1. **New knowledge (adequacy: LOW):** The core new knowledge claim—that gradient extreme-value clipping improves cross-prompt transfer—is interesting but insufficiently explained. The mechanism (overfitting reduction) is hypothesized but not validated. The novel knowledge would be significantly strengthened by the overfitting analysis proposed in Suggestion 2.

2. **Reproducibility (adequacy: MEDIUM):** The paper reports datasets (MS-COCO), models (all open-source), and parameter settings. However, the imprecise notation in Equation (3) and lack of variance reporting reduce full reproducibility.

3. **Potential to change practice/understanding (adequacy: LOW-MEDIUM):** The paper identifies a real problem and provides a simple fix. However, without statistical rigor, practitioners cannot confidently adopt GrCPA over CroPA. The weak cross-model transferability (<10%) also limits practical impact.

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Before next submission)                 P1 (Strengthen contribution)            P2 (Broaden impact)
├── Multi-seed re-run (all tables)          ├── Overfitting analysis                 ├── OOD dataset eval
│   └── 3 seeds, mean±std                   │   ├── Gradient norm tracking           │   └── ImageNet, COCO-O, etc.
├── Significance tests                      │   ├── Train/heldout prompt ASR         ├── Defense evaluation
│   └── McNemar's test GrCPA vs CroPA       │   └── Comparison w/ weight decay       │   └── JPEG compression, random resizing
├── Iteration count fix                     ├── Feature-level λ analysis             ├── Cross-model transfer study
│   └── Align Intro/Experiments             │   └── CKA similarity by layer          │   └── More model pairs
└── Equation (3) notation fix               └── Target answer sensitivity            └── Black-box attack extension
    └── argsort-based specification             └── Uniform vs selected targets
```

| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Gain |
|-------------|-----------|---------------|-------------------|---------|------------------|---------------|---------------|
| C2: GrCPA > CroPA (statistically) | Gains hold across seeds | Run all Table 1 experiments with 3 seeds | Same CroPA 3-seed baseline | Mean ASR ± std, p-value from McNemar's test | GrCPA mean > CroPA mean at p<0.05 for ≥75% of (task, target) combos | 3× compute (3 GPUs × 3 days) | Transforms core claim from plausible to statistically validated |
| C1: Non-stationarity = overfitting | Overfitting gap (train ASR - heldout ASR) measurable | Record train-prompt ASR and heldout-prompt ASR every 100 iter | Compare GrCPA vs Multi-P on both curves | Train-heldout ASR gap, gradient L2 norm | GrCPA reduces train-heldout gap by ≥30% vs Multi-P | 1 GPU × 1 day | Turns asserted hypothesis into validated mechanism |
| C2: Dual-modality regularization necessary | Visual-only or text-only GR underperforms joint | Add Table 5 experiments with full variance | Same GrCPA dual-modality baseline | ASR for each modality condition | Both p<0.05 in pairwise test vs dual | Already computed; add 3 seeds | Strengthens design principle claim |
| C2: Low-level features hypothesis | Layer-wise feature similarity differs by λ | Compute CKA between regularized and unregularized features per layer | No-regularization baseline | CKA per layer, ASR per λ | If hypothesis holds: CKA higher in early layers with λ=1/4 vs λ=1 | 1 GPU × 1 day | Resolves internal contradiction |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Rationale:** The paper identifies a meaningful problem (cross-prompt adversarial brittleness in VLMs) and proposes a simple, computationally lightweight method (gradient extreme-value clipping) that consistently improves ASR across multiple models and tasks. The core idea is intuitive and the evaluation is broad in scope (4 models, 4 tasks, 6 target answers). The ablations provide useful design insights (dual-modality regularization, λ robustness).

However, the paper has several critical weaknesses that prevent a higher score:
- **No statistical rigor:** All results are single-run point estimates without variance or significance testing. The core empirical claim ("GrCPA outperforms previous SOTA") cannot be properly evaluated.
- **Unsupported mechanism diagnosis:** The overfitting attribution is asserted without direct evidence, weakening the theoretical contribution.
- **Internal inconsistencies:** Iteration count discrepancy (10k vs 1k) and contradictory λ ablation evidence undermine trust.
- **Unverifiable novelty claim:** The "first" identification of non-stationarity cannot be verified (Retrieval-Disabled Mode), and concurrent work (CroPA) already addresses cross-prompt attacks.
- **Limited practical impact demonstrated:** Cross-model transfer <10% ASR, no defense evaluation, single dataset (MS-COCO).

**Post-Revision Target: [6.5, 7.5] / 10**

If the authors address all P0 items (multi-seed variance, iteration count fix, equation notation fix), add overfitting analysis (P1), and restructure the conclusion and claims (P1), the paper could reach 6.5-7.5/10. The remaining gap depends on whether the novelty holds under external literature verification and whether the method's practical significance (given weak cross-model transfer) can be better framed.