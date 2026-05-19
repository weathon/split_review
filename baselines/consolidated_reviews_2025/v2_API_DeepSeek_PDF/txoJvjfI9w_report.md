## Summary
# Final Review Report

## Summary

This paper introduces PEARL (Permutation-resilient learning), a framework that enhances LLM robustness to the ordering of in-context learning demonstrations. PEARL casts the permutation-robustness problem as a distributionally robust optimization (DRO) task: it trains an LLM to perform well under worst-case permutations rather than average-case ones. The framework operationalizes DRO through a two-player adversarial game between (1) a permutation-proposal network (P-Net) that learns to generate challenging permutations using a Sinkhorn-based optimal transport solver, and (2) the LLM that learns to minimize loss under these challenging permutations. Experiments on synthetic linear-function ICL and real-world instruction tuning (Super-Natural Instructions) across five LLM families demonstrate that PEARL improves both average and worst-case performance, with notable gains in many-shot and long-context generalization. The paper is accepted at ICLR 2025.

**Primary Strengths:** The problem is well-motivated (permutation vulnerability is a genuine LLM reliability concern), the DRO framing provides a principled theoretical lens, empirical evaluation covers multiple LLM families (LLaMA-2/3, Mistral, Gemma), and the many-shot generalization results (24-40% worst-case gains with limited training) are impressive.

**Primary Weaknesses:** (1) The formal DRO formulation (distribution-level sup over ambiguity set) does not cleanly align with the implemented instance-level adversarial training algorithm — this gap weakens the claimed theoretical grounding. (2) The P-Net's cross-demonstration layer (bilinear form) lacks clear justification for how it maps to permutation difficulty. (3) The linear-function experiment uses only one baseline while the instruction-tuning experiments use four, creating cross-experiment incomparability. (4) Statistical significance and variance are not reported for any experimental results. (5) The vulnerability analysis motivating the paper uses only 2 small datasets (100 samples each), undercutting the "extensive" claim. (6) Novelty cannot be fully verified without external literature comparison (paper_search unavailable in this run).

## Strengths
**S1. Well-motivated problem with practical significance.** The paper identifies a genuine and underexplored vulnerability in LLMs — that simple permutation of ICL demonstrations can serve as a natural, undetectable attack degrading performance by over 80% in certain settings. This is a realistic threat model since an adversary only needs to reorder existing examples without introducing adversarial content.

**S2. Principled DRO framework.** Applying distributionally robust optimization to the permutation-robustness problem provides a clean conceptual framing. The ambiguity set over all possible permutations (Eq 6-7) offers a theoretical language for formalizing what it means to be robust to any ordering. The illustrative Figure 2 effectively conveys the intuition that DRO yields more uniform coverage across permutations compared to ERM.

**S3. Comprehensive LLM evaluation.** The paper evaluates PEARL across five LLMs spanning three families (LLaMA-2/3, Mistral, Gemma) and two scales (7B, 8B, 13B). This breadth strengthens the claim that the method generalizes across model architectures and sizes. The consistent >10% worst-case improvement across all models is convincing evidence of broad applicability.

**S4. Impressive many-shot generalization.** The finding that PEARL trained on only 5 shots and 512-token sequences generalizes to 64-shot, 8K-token settings with 24-40% worst-case gains is the paper's strongest empirical result. This suggests that the framework learns genuinely robust features rather than overfitting to specific permutation patterns. The shot-efficiency finding (Table 4) — PEARL matches ERM's average performance with 2-4x fewer shots — has practical value for cost-sensitive deployment.

**S5. Inference-time efficiency.** PEARL incurs training-time overhead (adversarial co-training) but requires no modification to the LLM architecture and no additional computation at inference time — the P-Net is discarded after training. This is a clear practical advantage over inference-stage methods like output calibration or order optimization that add per-query cost.

**S6. Clear writing and reproducibility.** The method description is generally clear, with explicit equations, a well-structured algorithm box (Algorithm 1), and a detailed appendix covering hyperparameters, dataset construction, and additional results. The code is publicly available on GitHub.

## Weaknesses
**W1. Theory-algorithm gap (Major).** The paper presents a formal DRO objective (Eq 6-7) as the theoretical foundation but implements an instance-level adversarial permutation training algorithm (Algorithm 1) that differs from the stated DRO formulation. The formal DRO minimizes risk under the worst-case *distribution* in the ambiguity set (a convex combination of permutation pushforwards), while the algorithm generates permutations *per instance* via the P-Net. This distribution-to-instance gap means the formal DRO guarantees do not directly transfer, and the "DRO" framing is more of a conceptual inspiration than a rigorously implemented optimization. The paper should explicitly acknowledge this gap and either align the algorithm with the theory or revise the theory to match the algorithm.

**W2. P-Net component justification (Major).** The cross-demonstration layer (Eq 9, R = g(H W H^T)) uses a bilinear form to compute pairwise "swap difficulty." However, (a) the bilinear similarity h_i^T W h_j captures semantic similarity between demonstrations, which does not directly correspond to how difficult a swap would be for the LLM — difficulty depends on the full permutation context, not pairwise similarity; (b) the mapping from this pairwise score matrix to the permutation distribution via Sinkhorn normalization (Eq 10-12) is a generic differentiable sorting mechanism without any learned connection to LLM loss. The paper would benefit from a more direct supervision signal linking P-Net outputs to actual LLM loss.

**W3. Baseline inconsistency across experiments (Major).** The linear-function ICL experiment (Section 4, Table 1) compares only against ERM+CL (one baseline), while the instruction-tuning experiment (Section 5, Table 3) compares against four baselines including InfoAC and demonstration shuffling. This asymmetry makes it difficult to assess whether PEARL's gains in the linear setting would hold against stronger baselines. Since InfoAC directly targets permutation sensitivity, its absence in the linear experiment is a notable gap.

**W4. Missing statistical significance (Major).** No experiment reports variance, standard deviations, or significance tests. Results in Table 3 show single-point estimates, making it impossible to assess whether PEARL's improvements (e.g., 5.7% average gain at 4 shots) are statistically reliable. Given the small test set sizes (100 samples per task), variance could be high. The many-shot scaling results (Figure 5) similarly lack error bars. Multi-seed evaluation is standard practice for LLM fine-tuning experiments.

**W5. Narrow vulnerability motivation (Minor).** The motivating vulnerability analysis (Section 2) uses only 2 tasks (CurDial, TMW) with 100 samples each from Super-Natural Instructions. The claim of "extensive experiments on LLaMA-3" overstates the scope. The paper would benefit from demonstrating permutation vulnerability on additional tasks and datasets to strengthen the motivation.

**W6. Unbounded generalization claims (Minor).** The conclusion claims applicability to "multiple documents, images, or videos" without any supporting evidence. The abstract states "performance gains of up to 40%" without specifying the baseline or setting. These claims should be scoped to tested conditions.

**W7. Novelty verification incomplete.** Due to external literature search being unavailable in this run, the novelty of all three contribution claims (C1: DRO for permutation robustness, C2: P-Net with Sinkhorn, C3: adversarial co-training) could not be verified against prior art. This is a deferred verification item that authors should strengthen by providing explicit comparisons with the closest prior methods.

## Key Issues
### Ranked Defect Board (Top 5 by Severity and Research-Value Impact)

| Rank | Issue | Location | Severity | Validity Risk | Fixability | Confidence |
|------|-------|----------|----------|---------------|------------|------------|
| 1 | Theory-algorithm gap: DRO formalization vs instance-level implementation | Page 4, Section 3.1 (Eq 6-7) vs Algorithm 1 | Major | High | Fixable (revise framing) | High |
| 2 | P-Net cross-demonstration layer lacks direct link to permutation difficulty | Page 5, Section 3.2 (Eq 9-13) | Major | Medium | Fixable (add justification/ablation) | High |
| 3 | Missing statistical significance across all experiments | Pages 7-9, Tables 1, 3, 4; Figure 5 | Major | High | Fixable (multi-seed eval) | High |
| 4 | Baseline inconsistency: linear experiment uses 1 baseline vs 4 in instruction tuning | Page 7, Section 4.2-4.3, Table 1 | Major | Medium | Fixable (add baselines or caveat) | High |
| 5 | Vulnerability motivation uses only 2 small datasets | Page 3, Section 2 | Minor | Low | Fixable (expand or caveat) | High |

### Issue 1 — Theory-Algorithm Gap (Major, P0)

The formal DRO objective (Eq 6) solves $\min_\theta \sup_{Q_\Pi \in \mathcal{Q}} \mathbb{E}_{(p,x,y)\sim Q_\Pi}[\ell(\theta; p, x, y)]$ where $\mathcal{Q}$ is the convex hull of permuted empirical distributions. The implemented algorithm (Alg 1) instead performs instance-level adversarial permutation sampling: for each sample $(p,x,y)$, P-Net generates a permutation $\Pi$ and the LLM loss is computed on $(\Pi\cdot p, x, y)$. The connection between these two is not formally established.

**Root cause:** The paper conflates distribution-level robustness (DRO's worst-case distribution in an ambiguity set) with instance-level adversarial augmentation (worst-case permutation per sample). These are fundamentally different optimization problems.

**Repair path:** Either (a) reformulate the paper's contribution as adversarial permutation training *inspired by* DRO (dropping formal guarantee claims), or (b) add theory showing how instance-level sampling with the P-Net approximates or bounds the distribution-level DRO objective.

### Issue 2 — P-Net Justification (Major, P1)

The bilinear form $R = g(H W H^\top)$ maps demonstration representations to pairwise scores interpreted as "swap difficulty." There is no theoretical or empirical evidence that semantic similarity between demonstrations, as captured by this bilinear form, correlates with how difficult a swap would be for the LLM. The Sinkhorn operator then converts these scores into permutation probabilities via a generic differentiable sorting mechanism that is task-agnostic.

**Root cause:** The P-Net's ability to generate challenging permutations is learned through the adversarial loss signal (maximizing LLM loss), but the architectural inductive bias (bilinear similarity + Sinkhorn) is not directly tied to the permutation difficulty concept. The network could be learning arbitrary patterns unrelated to the intended "swap difficulty" interpretation.

**Repair path:** Add an ablation study isolating the P-Net's learned component from random permutation baselines. Compare: (a) random permutations, (b) P-Net with learned W, (c) P-Net with fixed random W, (d) heuristic difficulty (e.g., reverse order by label diversity). This would validate whether the learned component provides meaningful benefit.

### Issue 3 — Statistical Significance (Major, P1)

All results are single-point estimates without standard deviations, confidence intervals, or significance tests. Given the small per-task test sets (100 samples), variance could be substantial. The claimed gains of 5.7-9.8% in average performance and 14.2-29.4% in worst-case performance (Table 3) may not be statistically significant.

**Root cause:** Single-run evaluation without multi-seed reporting is common in LLM fine-tuning but becomes problematic when gains are modest (e.g., 2.5 points on TMW at 4 shots) and baselines are close.

**Repair path:** Report mean $\pm$ std over 3-5 random seeds for the main comparison (Table 3). At minimum, provide standard deviations for the aggregate average and worst-case columns.

## Actionable Suggestions
### Suggestion 1: Align DRO Theory with Algorithm (Must)
**Location:** Page 4, Section 3.1 (Eq 6-7) and Algorithm 1
**Defect:** Distribution-level DRO formulation does not match instance-level implementation.

**Action:** Replace "distributionally robust optimization" framing with a more precise description, such as "adversarial permutation training inspired by DRO." Add an explicit paragraph acknowledging that the algorithm is a practical approximation:
- "Our theoretical formulation follows the DRO principle of optimizing under worst-case distributions within an ambiguity set. In practice, we approximate this by training a permutation-proposal network to find challenging permutations per instance, then updating the LLM against them. While this does not exactly solve Eq (6), the empirical results demonstrate its effectiveness."

### Suggestion 2: Add P-Net Ablation Study (Must)
**Location:** Page 5, Section 3.2
**Defect:** P-Net's learned component vs random permutation baselines not isolated.

**Action:** Add an ablation experiment comparing:
1. Random permutations (no P-Net)
2. P-Net with learned W (current method)
3. P-Net with fixed random W
4. Heuristic ordering (e.g., reverse input order)
Expected outcome: If condition 2 significantly outperforms 3 and 4, this validates the learned cross-demonstration component.

### Suggestion 3: Report Statistical Significance (Must)
**Location:** Pages 7-9, Tables 1 and 3, Figure 5
**Defect:** No variance or significance measures reported.

**Action:** Run all main experiments with 3 random seeds and report mean $\pm$ standard deviation. For the key results in Table 3, add a column for standard deviation. For the many-shot scaling (Figure 5), add error bars.

### Suggestion 4: Add Baselines to Linear Function Experiment (Nice-to-have)
**Location:** Page 7, Section 4.2-4.3, Table 1
**Defect:** Only one baseline (ERM+CL) used.

**Action:** Add at least ERM+DS (demonstration shuffling) and InfoAC as baselines to Table 1. If computational cost is prohibitive, add a caveat: "We note that stronger baselines (demonstration shuffling, InfoAC) are evaluated in the instruction tuning experiments (Section 5) as the primary comparison setting."

### Suggestion 5: Expand Vulnerability Motivation (Nice-to-have)
**Location:** Page 3, Section 2
**Defect:** Only 2 small datasets used.

**Action:** Add 2-4 additional tasks from Super-Natural Instructions to the vulnerability analysis. Alternatively, replace "extensive experiments" with "experiments on two representative tasks" in the introduction.

### Suggestion 6: Scoping Conclusion Claims (Must)
**Location:** Page 10, Conclusion
**Defect:** Unsupported generalization to images/videos.

**Action:** Replace the broad generalization statement with a bounded research outlook focused on text-domain extensions (longer reasoning chains, multi-document QA, structured prediction). Remove or substantially qualify the image/video claim.

## Storyline Options + Writing Outlines
### Abstract Outline (5-sentence structure)

**S1 — Problem & Domain:** "The in-context learning (ICL) capability of large language models (LLMs) is highly sensitive to the ordering of demonstrations, causing prediction instability that poses reliability risks in deployment."

**S2 — Significance & Attack Vector:** "This sensitivity can be exploited as a natural, undetectable attack: simply permuting demonstration order degrades performance with success rates exceeding 80% on LLaMA-3 under standard evaluation, yet the manipulation preserves semantic content."

**S3 — Prior Work Gap:** "Existing mitigation methods either modify the underlying architecture at the cost of scalability or add post-processing overhead during inference, leaving a gap in approaches that enhance intrinsic LLM robustness without architectural changes or inference-time cost."

**S4 — Proposed Method:** "We propose PEARL (Permutation-resilient learning), a framework that trains LLMs to perform well under worst-case input permutations. PEARL employs a permutation-proposal network (P-Net) that learns challenging permutations via entropy-constrained optimal transport, and the LLM is adversarially trained against these permutations through minimax optimization."

**S5 — Key Results:** "On synthetic pre-training and real-world instruction tuning tasks, PEARL improves both average and worst-case performance across five LLM families (LLaMA-2/3, Mistral, Gemma). When trained on only 5-shot, 512-token sequences and evaluated on up to 64-shot, 8K-token settings, PEARL achieves 24-40% worst-case performance gains over ERM, demonstrating strong generalization efficiency."

### Introduction Outline (5 paragraphs)

**P1 — Hook & Problem (Page 1)**
Role: Establish the practical importance of ICL and identify permutation sensitivity as a critical reliability gap.
Key claim: LLMs are surprisingly fragile to demonstration order despite impressive ICL capabilities.
Transition: "This fragility is not merely a prompt engineering nuisance—it creates a security vulnerability."

**P2 — Attack Motivation (revised, current P2+attack preview)**
Role: Demonstrate that permutation sensitivity is an exploitable attack vector with real consequences.
Key claim: Simple permutation attacks achieve >80% success rate while being undetectable.
Evidence: §2 results on CurDial and TMW with exhaustive and neural search attacks.
Transition: "Existing defenses against this vulnerability fall into two categories, each with limitations."

**P3 — Prior Work & Gap (current P2 but expanded)**
Role: Review training-stage and inference-stage methods and identify the gap for a general, scalable, training-stage solution.
Key claim: No existing method simultaneously achieves (a) architectural generality, (b) no inference overhead, (c) applicability to generation tasks, and (d) worst-case robustness guarantees.
Evidence: InfoAC limited to classification, DeepSet not scalable, calibration overhead costly.
Transition: "To address this gap, we propose PEARL..."

**P4 — Method Preview (current P3-P4 split)**
Role: Provide high-level intuition of PEARL before the formal method section.
Key claim: DRO-inspired adversarial permutation training via P-Net and Sinkhorn optimal transport.
Evidence: Conceptual description—formal details in §3.
Transition: "We validate PEARL in two complementary settings."

**P5 — Contributions & Results Preview (restructured closing paragraph)**
Role: Summarize key findings, bounded contributions, and paper organization.
Key claim: Consistent improvements across LLM families, many-shot generalization, and inference efficiency.
Transition to paper structure: "Our code is available at..."

### Alternative Storyline Candidate

**Alternative A — "Security-First" Narrative**
Reorder to foreground the attack angle: §2 (vulnerability demonstration) → §1 (problem and gap) → §3 (defense via PEARL). This would make the paper more accessible to a security/robustness audience and would better match the paper's strongest hook (the >80% ASR finding). However, it would require restructuring the current flow.

**Selected Storyline:** Current flow (Problem → Prior Work → Vulnerability Analysis → Method → Experiments) is standard and effective for the target ML audience. The main revision needed is in the Introduction paragraphs (P2 current) where the prior work survey and the attack analysis need clearer separation and more precise positioning of PEARL's contributions.

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[P0: Theory-Alignment Gap]
    -> Fix: Revise DRO framing from formal guarantee to "inspired by" 
    -> Expected: Stronger alignment between claims and implementation
    -> Effort: Low (text revision only)
    
[P1: Statistical Significance]
    -> Fix: Run 3-seed evaluation for Tables 1, 3; add error bars to Fig 5
    -> Expected: Verified reliability of reported gains
    -> Effort: Medium (3x compute, ~3 GPU-days)
    
[P1: P-Net Ablation]
    -> Fix: Add controlled comparison (learned vs fixed vs random vs heuristic permutations)
    -> Expected: Validates the learned P-Net component
    -> Effort: Low-Medium (add 3-4 rows to appendix table)
    
[P1: Baseline Consistency]
    -> Fix: Add ERM+DS baseline to linear function experiment (or add caveat)
    -> Expected: Cross-experiment comparability
    -> Effort: Low
    
[P2: Vulnerability Scope]
    -> Fix: Expand to 4-6 tasks or soften "extensive" claim
    -> Expected: Stronger motivation or more honest scoping
    -> Effort: Low-Medium
    
[P2: Conclusion Scoping]
    -> Fix: Remove/bound image/video generalization claim
    -> Expected: Defensible conclusion
    -> Effort: Low (text revision only)
```

### Execution Order

**Phase 1 (Day 1-2): Text Revisions (Low Effort)**
1. Revise Introduction: replace "extensive experiments" with specific scope, bound ASR claims to δ=50% condition, add precise gap statement (§2 motivation)
2. Revise DRO section (3.1): add paragraph acknowledging instance-level approximation of distribution-level DRO
3. Revise Conclusion: remove unsupported image/video claim, replace with bounded text-domain outlook
4. Add linear experiment caveat about single baseline

**Phase 2 (Day 3-7): Experimental Additions (Medium Effort)**
5. Run 3-seed evaluation for Llama3-8B experiments (Table 3): report mean ± std
6. Add P-Net ablation comparing learned vs fixed vs random vs heuristic permutations (Appendix)
7. Expand vulnerability analysis to 2-4 additional Super-Natural Instructions tasks

**Phase 3 (Day 8-10): Analysis & Writing (Low-Medium Effort)**
8. Update Figure 5 with error bars
9. Revise Abstract to incorporate bounded claims
10. Final consistency pass across all sections

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Linear function ICL: PEARL vs ERM+CL on permutation robustness | GPT-2, synthetic linear functions (d=?), 3-5 shots, 40K functions, 500K steps | Normalized MSE | PEARL reduces worst-case MSE by 65.5-73.6% | C1, C2, C3 | Only 1 baseline; synthetic task limited generalizability |
| E2 | Instruction tuning: PEARL vs ERM/ERM+DS/ERM+IM/InfoAC | Llama3-8B, 4 held-out tasks (CSQA, CurDial, CoLA, TMW), 2-4 shots, ROUGE-L | Average & Worst ROUGE-L | PEARL improves worst-case 14.2-29.4% over ERM | C1, C2, C3 | No variance/std reported; single run |
| E3 | Cross-LLM generalization | Mistral-7B, Gemma-7B, Llama2-7B, Llama2-13B; 3-shot | Worst-case ROUGE-L | >10% worst-case improvement across all LLMs | C1 (general) | Some models (e.g., Gemma 2-shot) show small gains (0-2%) |
| E4 | Many-shot scaling (8-64 shots, 8K tokens) | Llama3-8B, trained on 5-shot/512 tokens | Average & Worst ROUGE-L | 24-40% worst-case gains | C1 (generalization) | No control for training-evaluation shot mismatch effects |
| E5 | Shot efficiency | Llama3-8B, 2-64 shots | Average ROUGE-L | PEARL matches ERM with 2-4x fewer shots | C1 (efficiency) | Only average (not worst-case) efficiency reported |
| E6 | Hyperparameter analysis (Sinkhorn iterations, temperature, entropy coefficient) | Ablation on instruction tuning | Gradient norm, avg/worst performance | Sinkhorn robust to parameter variations; β=1.0 optimal | C2 | Only gradient norm analyzed; direct performance impact not shown for all conditions |
| E7 | Best-case performance (Appendix F) | Llama3-8B, 2-5 shots | Best ROUGE-L | PEARL slightly improves best-case too | C1 | Not a primary claim; incremental |

### Research-Theme Gap Diagnosis

**Gap 1 — Causal Validation:** The paper claims that P-Net's learned cross-demonstration layer identifies "challenging permutations." However, no experiment directly validates this claim — e.g., by comparing permutations selected by P-Net against random or heuristic baselines in terms of their effect on LLM loss. Without this, the P-Net's learned component could be unnecessary.

**Gap 2 — Statistical Reliability:** All claims about PEARL's superiority over baselines rest on single-run point estimates. For the key result in Table 3 (4-shot, 29.4% worst-case gain), it is unknown whether this gain is reproducible under different random seeds.

**Gap 3 — Ablation of DRO vs Adversarial Training:** The paper jointly introduces DRO framing + P-Net + adversarial training. It does not isolate the contribution of each component. A minimal ablation would compare: (a) ERM, (b) ERM + random permutations (data augmentation), (c) ERM + adversarial P-Net permutations (current method), (d) DRO-style distribution-level weighting (if implementable).

### Proposed Research Experiments

**P0 Experiment: Multi-Seed Evaluation**
- **Target Claim:** C1 (PEARL consistently improves worst-case performance)
- **Hypothesis:** PEARL's gains over ERM are statistically significant (p < 0.05)
- **Minimal Design:** Run 3 random seeds for Llama3-8B at 3-shot, 4-shot on all 4 test tasks
- **Controls:** Same seed initialization for both PEARL and ERM
- **Metrics:** Mean $\pm$ std ROUGE-L, paired t-test or bootstrap significance
- **Success Criterion:** All gains with p < 0.05 (one-tailed, PEARL > ERM)
- **Estimated Cost:** ~3 GPU-days on A40
- **Expected Quality Gain:** High — validates core claims

**P1 Experiment: P-Net Ablation**
- **Target Claim:** C2 (P-Net's learned component improves against baselines)
- **Hypothesis:** P-Net with learned W generates more challenging permutations than random/fixed baselines
- **Minimal Design:** Compare 4 conditions: (1) random permutation, (2) fixed random W, (3) learned W, (4) reverse order by label entropy
- **Controls:** Same LLM training budget across conditions
- **Metrics:** LLM loss under generated permutation, final worst-case ROUGE-L
- **Success Criterion:** Learned W significantly outperforms fixed/random/heuristic in generating high-loss permutations
- **Estimated Cost:** ~2 GPU-days
- **Expected Quality Gain:** High — validates the core P-Net mechanism

**P1 Experiment: Many-Shot Generalization Control**
- **Target Claim:** C1 (generalization from 5-shot training to 64-shot evaluation)
- **Hypothesis:** The 24-40% gains are not artifacts of training-evaluation shot mismatch
- **Minimal Design:** Compare (a) PEARL 5-shot train → 64-shot eval, (b) PEARL 64-shot train → 64-shot eval, (c) ERM 64-shot train → 64-shot eval
- **Controls:** Same total training tokens across conditions
- **Metrics:** Average and worst-case ROUGE-L at 64 shots
- **Success Criterion:** PEARL 5→64 achieves ≥80% of PEARL 64→64 gain
- **Estimated Cost:** ~5 GPU-days
- **Expected Quality Gain:** Medium — validates the efficiency claim

**P2 Experiment: Vulnerability Expansion**
- **Target Claim:** "Permutation attacks are a widespread concern"
- **Hypothesis:** Vulnerability pattern holds across 6+ diverse NLP tasks
- **Minimal Design:** Add 4 tasks from Super-Natural Instructions (different categories: reasoning, classification, summarization, QA)
- **Controls:** Same 100-sample evaluation protocol
- **Metrics:** ASR at δ=50% for exhaustive search
- **Success Criterion:** ASR > 50% on at least 5/6 tasks
- **Estimated Cost:** ~1 GPU-day
- **Expected Quality Gain:** Medium — strengthens motivation

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 6.5 / 10

**Rationale:** The paper tackles a well-motivated problem (permutation robustness in ICL) and presents a technically sound framework (PEARL) with generally positive empirical results across multiple LLM families. The many-shot generalization findings are particularly noteworthy. However, the score is constrained by:

1. **Theory-algorithm gap (major):** The claimed DRO theoretical foundation does not cleanly match the implemented algorithm. This reduces confidence in the paper's primary framing.
2. **Missing statistical evidence (major):** No variance or significance testing across all experiments makes it impossible to assess result reliability.
3. **Baseline inconsistency (major):** The linear-function experiment, which is presented as a core validation, uses only one baseline.
4. **Novelty uncertainty (deferred):** Without external literature verification, contribution novelty cannot be confirmed.

These issues are *fixable* with moderate-effort revisions (multi-seed evaluation, textual clarification of the DRO-algorithm relationship, P-Net ablation). The core technical contribution—adversarial permutation training with Sinkhorn-based permutation generation—is sound and empirically supported. The overall research value (demonstrating that training-stage permutation robustness is achievable without architectural change) is solid.

### Post-Revision Target: [7.0, 7.5] / 10

**Conditional on:** (a) Adding 3-seed evaluation with statistical significance for main results, (b) aligning the DRO framing with the actual algorithm or explicitly acknowledging the gap, (c) adding P-Net ablation, (d) expanding vulnerability analysis or scoping claims, and (e) scoping the conclusion to tested domains. With these revisions, the paper would provide a well-validated, clearly-framed contribution to LLM robustness that would merit a score of 7.0-7.5, reflecting solid empirical work with a clear practical angle but moderate novelty increment over existing adversarial training and data augmentation approaches.

### Page Coverage Audit

| Page | Main Section | Annotation Count | Coverage Status | Skip Reason |
|------|-------------|-----------------|-----------------|-------------|
| 1 | Abstract, Introduction (P1-P3) | 4 | Covered | - |
| 2 | Introduction (P4-P5), Figure 1 | 1 | Covered | - |
| 3 | Section 2 (Vulnerability Analysis) | 1 | Covered | - |
| 4 | Section 3.1 (DRO Formulation) | 1 | Covered | - |
| 5 | Section 3.2 (P-Net Architecture) | 1 | Covered | - |
| 6 | Section 3.3 (Adversarial Opt, Alg 1) | 1 | Covered | - |
| 7 | Section 4 (Linear Functions Exp) | 1 | Covered | - |
| 8 | Section 5.1-5.2 (Instruction Tuning) | 1 | Covered | - |
| 9 | Section 5.2 (Many-shot scaling) | 1 | Covered | - |
| 10 | Section 6-7 (Related Work, Conclusion) | 2 | Covered | - |
| 16-20 | Appendix (A-F) | 0 | Skipped | Appendix contains implementation details and extended tables; no new claims requiring annotation beyond those covered in main text. |

**Total annotations: 14 (within recommended range 12-25). Distribution is reasonably balanced across sections with no front-loading or clustering issues.**