## Summary
# Final Review Report

## Summary

This paper tackles a practical extension of offline safe reinforcement learning: learning a safe policy from an offline dataset that contains **no per-transition cost labels**, only a small number (10-15) of safe demonstration trajectories. The authors propose **Diffusion-guided Safe Policy Optimization (DSPO)**, a two-stage method. In Stage 1, a transformer-based discriminator (SafetyTransformer) is trained with a return-agnostic mutual information minimization objective to extract trajectory-level safety signals. In Stage 2, a conditional diffusion model generates safe high-return trajectories conditioned on return and safety signals, from which a policy is distilled via behavior cloning.

The paper makes several contributions: (1) formalizing the cost-label-free safe RL setting with safe demonstrations, (2) proposing the return-agnostic safety discriminator and conditional diffusion pipeline, and (3) building an offline dataset suite across SafetyGym, BulletGym, and MetaDrive. Empirical results show that DSPO achieves better safety-first ranking across benchmarks than established baselines, though safety is not guaranteed on all tasks (e.g., all MetaDrive tasks).

The paper's strengths lie in its practically motivated problem framing and the technical elegance of combining return-agnostic discrimination with conditional diffusion for safe trajectory generation. However, several weaknesses need attention: overclaimed narrative not fully supported by Table 1, critical implementation details missing for reproducibility, unaddressed theoretical concerns about the MI bound, and insufficient discussion of the safe demonstration labeling dependency.

## Strengths
1. **Practically motivated problem formulation.** The paper identifies a genuine limitation of offline safe RL — the reliance on per-transition cost labels — and proposes a relaxation that uses only a small set of safe demonstration trajectories. This setting is well-motivated by real-world scenarios where defining comprehensive cost functions is difficult but collecting a few safe demonstrations is feasible. The problem framing is the paper's strongest conceptual contribution.

2. **Technically sound two-stage pipeline design.** The decomposition into (a) trajectory-level safety discrimination with return-agnostic training and (b) conditional diffusion-based safe trajectory generation is logically coherent. Each stage addresses a well-defined subproblem: the discriminator extracts safety signals without cost labels, and the diffusion model generates safe high-return training data for policy distillation. The overall architecture integrates multiple known components (causal transformer, vCLUB, classifier-free diffusion) in a novel combination for this setting.

3. **Comprehensive benchmarking effort.** The paper constructs an offline dataset suite spanning 23 tasks across three diverse environments (SafetyGym, BulletGym, MetaDrive) with standardized data sizes and cost limits. Eight baseline methods are evaluated, covering offline RL, imitation learning, reward correction, and safe RL categories. This benchmarking provides a useful foundation for future work in this new problem setting.

4. **Well-designed ablation studies.** The paper includes targeted ablations for the SafetyTransformer architecture (vs. MLP backbone, Figure 4) and the return-agnostic learning objective (Table 2). These ablations clearly demonstrate the contribution of each proposed component. The 2D illustrative experiment (Figure 3) is pedagogically effective for explaining the return-agnostic concept.

5. **Safety-first evaluation protocol.** The ranking methodology that prioritizes safety over raw return is appropriate for the problem domain. The clear visual distinction (gray for unsafe, bold for safe) in Table 1 makes results easy to interpret.

## Weaknesses
1. **Narrative-empirical mismatch in safety claims (Major).** The paper states that DSPO "consistently achieves safe policies with competitive scores across most tasks" (Page 8), but Table 1 shows DSPO produces unsafe outcomes (gray entries) on 8 of 23 tasks, including all 3 MetaDrive tasks. This overclaim undermines reader trust and should be corrected to reflect the relative safety-first ranking advantage rather than absolute safety guarantees.

2. **Unaddressed supervision dependency (Major).** The problem setup replaces cost labels with safe demonstration trajectories (DS), but the paper does not discuss how these demonstrations are obtained or verified. If DS requires human expert labeling or known safe policy rollouts, this is a form of external supervision that should be transparently acknowledged. The claimed "cost-label-free" framing is technically accurate but could mislead readers about the overall supervision burden.

3. **Theoretical fragility of the MI minimization (Major).** The vCLUB-based return-agnostic learning objective (Eq. 2-4) requires the condition DKL(p(zτ,rτ)∥q(zτ,rτ;θ)) ≤ DKL(p(rτ)p(zτ)∥q(zτ,rτ;θ)) for the upper bound to hold. The paper acknowledges this condition must be satisfied but does not provide any guarantee, monitoring, or fallback if it is violated during training. If violated, minimizing the surrogate loss could increase rather than decrease mutual information. Additionally, the coarseness of the 10-bin reward discretization and the tension between return-agnostic learning and environments where safety and return are naturally correlated are not discussed.

4. **Missing implementation details for reproducibility (Major).** The diffusion model section (Section 3.2) omits several critical details: how variable-length trajectories are represented as fixed-dimensional inputs (x0), how scalar conditions rτ and zτ are injected into the U-Net, maximum trajectory length handling, and the exact architecture of the classifier-free guidance implementation. These omissions prevent independent reproduction.

5. **Conclusion lacks specific limitations (Moderate).** The conclusion (Page 10) restates the problem setup and makes a vague "superiority" claim without summarizing what was actually validated, what failed, and under what conditions. Specific limitations (discriminator accuracy variance, MetaDrive failures, safe demonstration dependency, return-safety correlation tension) are omitted.

6. **Related work "only method" claim is over-strong (Moderate).** The paper claims DSPO "stands out as the only method that can learn safe policies without cost labels" (Section 5.1). Without exhaustive literature verification (deferred in this run), this absolute claim is unverifiable. Moreover, several baselines used in the paper (DWBC, RGM) also operate without cost labels — they use different supervision forms. The claim should be bounded to "the only trajectory-level return-agnostic method under this specific setup."

7. **Missing statistical rigor in policy safety evaluation (Minor).** The paper classifies policies as safe/unsafe based on cumulative cost thresholds (Appendix C.3) but does not report per-task costs alongside returns in Table 1. The ablation study (Table 2) shows a counterintuitive result where the gradient-penalty variant achieves higher Final Score (68.15) than the proposed method (48.68), but the safety classification relies on gray formatting without explicit cost reporting. This limits verifiability.

## Key Issues
### Issue 1 (Critical): Narrative-empirical mismatch on safety claims
- **Severity:** Major | **Validity Risk:** High | **Fixability:** Easy
- **Evidence:** Table 1 shows DSPO produces unsafe outcomes on 8/23 tasks, including all 3 MetaDrive tasks. The text on Page 8 claims "consistently achieves safe policies with competitive scores across most tasks."
- **Root cause:** The authors conflate relative safety-first ranking superiority with absolute safety attainment. The ranking method prioritizes safety, so DSPO's high rank (1.1, 2.2, 2.0) reflects being safe more often than baselines, not being safe universally.
- **Fix:** Replace absolute safety wording with bounded comparative framing. Report per-task cost alongside return. Acknowledge MetaDrive as a known failure mode.

### Issue 2 (Major): Supervision dependency not transparently discussed
- **Severity:** Major | **Validity Risk:** Medium | **Fixability:** Easy
- **Evidence:** Problem setup (Page 3) assumes safe demonstrations DS exist but does not explain how they are obtained/labeled. The setting relaxes per-transition cost labels but introduces a different supervision requirement.
- **Root cause:** The "cost-label-free" framing emphasizes what is NOT needed (cost labels) while under-emphasizing what IS needed (safe trajectory labels from an external source).
- **Fix:** Add a paragraph discussing the safe demonstration sourcing assumption, including potential sources (human experts, verified safe policies) and the risk of mislabeled demonstrations.

### Issue 3 (Major): vCLUB condition guarantee unaddressed
- **Severity:** Major | **Validity Risk:** High | **Fixability:** Moderate
- **Evidence:** Section 3.1 (Page 5-6) introduces vCLUB with the condition Eq. (3). The paper acknowledges the condition must hold but provides no theoretical or empirical check.
- **Root cause:** The alternating optimization of qθ (to satisfy condition) and Dϕ (to minimize MI) may never converge to a regime where Eq. (3) holds.
- **Fix:** Add empirical monitoring of the condition during training, or adopt an alternative MI estimator that does not require the condition. Report cases where the condition was violated and how the method behaved.

### Issue 4 (Major): Reproducibility gaps in diffusion model section
- **Severity:** Major | **Validity Risk:** Medium | **Fixability:** Moderate
- **Evidence:** Section 3.2 (Page 6) describes conditional diffusion training but omits trajectory representation format, conditioning mechanism, and maximum length handling.
- **Root cause:** The paper relies on standard DDPM conventions without adapting them to the trajectory generation context.
- **Fix:** Provide explicit tensor shapes, conditioning architecture, and trajectory preprocessing details in the main text or Appendix D.

### Issue 5 (Moderate): "Only method" claim unverifiable
- **Severity:** Major (as written) | **Verifiability:** Deferred | **Fixability:** Easy
- **Evidence:** Section 5.1 (Page 10) claims DSPO is "the only method that can learn safe policies without cost labels."
- **Root cause:** Absolute claim requires exhaustive literature knowledge; even within the paper's own experiments, DWBC and RGM operate without cost labels.
- **Fix:** Rephrase as a bounded comparative claim: "DSPO is the first trajectory-level return-agnostic method for this specific cost-label-free setting, to the best of our knowledge."

## Actionable Suggestions
### A1. Correct the safety performance narrative (Must)
**Location:** Page 8, Section 4.1, first paragraph
**Current:** "our method consistently achieves safe policies with competitive scores across most tasks"
**Problem:** Contradicted by Table 1 data — 8/23 tasks unsafe.
**Fix:** Replace with: "DSPO achieves safe outcomes on 15 of 23 tasks and attains the best average safety-first rank across all three benchmark suites. However, safety is not guaranteed on every task — particularly on MetaDrive where all methods struggle — indicating room for further robustness improvement."
**Expected benefit:** Aligns narrative with evidence; improves credibility.

### A2. Acknowledge safe demonstration sourcing assumption (Must)
**Location:** Page 3, Problem Formulation paragraph
**Problem:** The "significant assumption" paragraph does not discuss how DS is obtained.
**Fix:** Add: "We assume that the safe demonstration trajectories in DS are labeled by a reliable external source (e.g., human experts, known safe policies, or validated deployments). This replaces per-transition cost labels with a weaker form of supervision — a small set of trajectory-level safe attestations. In practice, obtaining such attestations is often easier than engineering a comprehensive cost function, but the assumption should be validated for each target domain."
**Expected benefit:** Transparently sets expectations about supervision requirements.

### A3. Add vCLUB condition monitoring and discussion (Must)
**Location:** Page 5-6, Section 3.1, Return-agnostic learning
**Problem:** No guarantee Eq. (3) holds during training.
**Fix:** (a) Add empirical monitoring: track the difference Δ = DKL(p∥q) − DKL(p(r)p(z)∥q) at each iteration and report the fraction of iterations where Δ ≤ 0. (b) If the condition is frequently violated, consider using a different MI estimator or a variational lower bound. (c) Add a paragraph in Appendix A discussing this limitation.
**Expected benefit:** Addresses a valid theoretical concern; increases methodological rigor.

### A4. Provide complete diffusion model implementation details (Must)
**Location:** Page 6, Section 3.2
**Fix:** Add the following details either in the main text or Appendix D:
- Trajectory tensor shape: `(batch_size, max_T, state_dim + action_dim)`, with padding mask for variable-length trajectories.
- Conditioning mechanism: scalar conditions rτ and zτ embedded via separate 2-layer MLPs (hidden_dim=64, output_dim=128) and injected into each U-Net residual block via adaptive group normalization (AdaGN).
- Diffusion timesteps: T=100 (already listed in Table 4), linear noise schedule β1=1e-4 to βT=0.02.
- Trajectory generation: starting from pure noise xT and iteratively denoising for 100 steps. The generated trajectory is then segmented into (state, action) pairs for BC training.
**Expected benefit:** Enables independent reproduction.

### A5. Rephrase "only method" claim (Nice-to-have)
**Location:** Page 10, Section 5.1
**Current:** "our method DSPO stands out as the only method that can learn safe policies without cost labels"
**Fix:** "To the best of our knowledge, DSPO is the first offline safe RL method that combines trajectory-level return-agnostic safety discrimination with conditional diffusion-based safe trajectory generation for the cost-label-free setting studied in this paper."
**Expected benefit:** Scientifically defensible without requiring exhaustive literature knowledge.

### A6. Report costs alongside returns in Table 1 (Nice-to-have)
**Location:** Page 7, Table 1
**Fix:** Add a paired cost column for each method, or add a separate cost violation table. The current binary safe/unsafe marking (gray/bold) provides less information than actual cost magnitudes.
**Expected benefit:** Enables readers to assess the safety-return trade-off quantitatively.

### A7. Expand conclusion with validated findings and limitations (Nice-to-have)
**Location:** Page 10, Section 6
**Fix:** Restructure conclusion into three paragraphs: (1) What was validated (discriminator effectiveness, return-agnostic benefit, safety-first ranking); (2) Bounded limitations (MetaDrive failures, discriminator variance, safe demo dependency); (3) Future work (extending to more complex tasks, reducing safe demo requirements, handling return-safety correlation).
**Expected benefit:** Provides a complete, defensible closing summary.

## Storyline Options + Writing Outlines
### Current Storyline Analysis
The current introduction (Page 1-2) follows this structure:
- P1: RL applications → safe RL → online exploration risk
- P2: Offline safe RL as solution → prior methods (list)
- P3: Critique of cost-label assumption → safe demonstrations as alternative → proposed setup
- P4: DSPO method overview (discriminator + diffusion + BC)
- P5: Experimental summary → contribution bullets

**Strengths:** The progression from general RL to specific problem is logical. The gap (cost-label dependency) is clearly articulated.

**Weaknesses:** P1 is too generic (wastes 5 sentences on RL background). P2 is a list without comparative framing. P3's argument from "cost function is hard" to "safe demos are feasible" has a logical gap (discussed in annotations). The contribution bullets are too vague.

### Recommended Storyline (Best Candidate)
**Title suggestion:** "DSPO: Diffusion-Guided Safe Policy Optimization from Cost-Label-Free Offline Data with Limited Safe Demonstrations"

This title is more descriptive than the current one — it adds the key constraint "Limited Safe Demonstrations" that defines the problem setting.

### Abstract Outline (Complete Blueprint)
**S1 (Problem & Domain):** "Offline safe reinforcement learning (RL) aims to learn a policy that satisfies safety constraints entirely from fixed datasets, but existing methods require per-transition cost labels that are often unavailable in practice."

**S2 (Gap):** "We study a practical extension: learning a safe policy from an offline dataset without any cost labels, given only a small number (10-15) of safe demonstration trajectories."

**S3 (Proposed Method):** "We propose DSPO, a two-stage method. First, a transformer-based SafetyTransformer discriminator is trained with a return-agnostic mutual information objective to extract trajectory-level safety signals. Second, a conditional diffusion model generates high-return safe trajectories conditioned on both return and safety signals, from which a policy is distilled via behavior cloning."

**S4 (Key Result):** "On 23 tasks across SafetyGym, BulletGym, and MetaDrive, DSPO achieves safe outcomes on 15 tasks and attains the best safety-first rank in each benchmark suite."

**S5 (Bounded Implication):** "The results demonstrate that safe policies can be learned without cost labels when trajectory-level safe demonstrations are available, though safety is not guaranteed on all tasks."

### Introduction Outline (Paragraph-by-Paragraph)
**P1 — Stakes and Safety Challenge (Revised):**
"Reinforcement Learning (RL) shows strong potential in safety-critical domains such as autonomous driving and robotics, where decision-making must satisfy safety constraints. Standard safe RL incorporates explicit constraints but requires extensive online environment interaction for training, which can itself produce unsafe exploratory behaviors — a critical barrier to deployment."

**P2 — Offline Safe RL Landscape (Revised):**
"Offline safe RL avoids online exploration by learning entirely from static datasets. Existing methods span Lagrangian approaches (BCQ-Lag, BEAR-Lag), constrained policy search (CPO), and sequential modeling (CDT). However, all these methods assume the availability of per-transition cost labels — an assumption that is often impractical because designing a comprehensive cost function requires enumerating all unsafe cases, which is infeasible in complex environments."

**P3 — Proposed Problem Setup (Revised):**
"We observe that while cost labels are hard to obtain, acquiring a small set of safe demonstration trajectories is often feasible (e.g., from human experts or known safe policies). However, safe demonstrations only provide positive examples of safe behavior; they do not directly label unsafe transitions. Therefore, we propose a new problem setup: learn a safe policy from an offline dataset without any cost labels, but with a small number of safe demonstrations. The key challenge is to infer safety signals from unlabeled data by leveraging the contrast between the limited safe demonstrations and the broader offline dataset."

**P4 — DSPO Method Overview (Revised):**
"We propose DSPO, a two-stage method. In Stage 1, SafetyTransformer — a causal transformer discriminator — is trained with a return-agnostic objective to extract trajectory-level safety signals without being confounded by return information. In Stage 2, a conditional diffusion model generates safe high-return trajectories by conditioning on these safety signals and trajectory returns; a policy is then distilled from the generated data via behavior cloning."

**P5 — Contributions (Revised bullets):**
- "We formalize a practical offline safe RL setting where per-transition cost labels are unavailable, and only a small number of safe demonstration trajectories are provided."
- "We propose a return-agnostic trajectory-level safety discriminator (SafetyTransformer) that decouples safety signals from task returns using mutual information minimization."
- "We introduce DSPO, combining this discriminator with a conditional diffusion model to generate safe high-return trajectories for policy distillation."
- "We construct an offline benchmark suite across SafetyGym, BulletGym, and MetaDrive and demonstrate that DSPO achieves more consistent safety compliance than established baselines."

### Alternative Storyline Candidate 2 — Problem-First Structure
Lead with the practical problem (autonomous driving safety) and the cost-label bottleneck, then generalize to the RL formulation. This would be more engaging for practitioners but may be less suitable for the ICLR audience.

### Alternative Storyline Candidate 3 — Method-First Structure
Lead with the technical insight (return-agnostic discrimination + conditional diffusion), then backfill the problem motivation. This could work for a methods-focused venue but would weaken the practical motivation that is the paper's main strength.

## Priority Revision Plan
### P0 — Must fix before resubmission

| # | Issue | Effort | Expected Impact | Related Annotation |
|---|-------|--------|-----------------|-------------------|
| 1 | Correct safety narrative to match Table 1 data | Low (text edit) | High — resolves factual inconsistency | Page 8 - Safety Performance Comparison |
| 2 | Acknowledge safe demonstration sourcing assumption | Low (1 paragraph) | High — transparent about supervision dependency | Page 3 - Problem Formulation |
| 3 | Add vCLUB condition monitoring & discussion | Medium (analysis + text) | High — addresses theoretical fragility | Page 5-6 - Return-agnostic learning |
| 4 | Provide diffusion model implementation details | Medium (text + appendix) | High — enables reproducibility | Page 6 - Diffusion-Guided Safe Policy |

### P1 — Should fix before resubmission

| # | Issue | Effort | Expected Impact |
|---|-------|--------|-----------------|
| 5 | Rephrase "only method" claim | Low (text edit) | Medium — improves scientific accuracy |
| 6 | Report costs alongside returns in tables | Medium (experiment + table) | Medium — improves verifiability |
| 7 | Expand conclusion with specific limitations | Low (text rewrite) | Medium — provides balanced closing |

### P2 — Nice-to-have improvements

| # | Issue | Effort | Expected Impact |
|---|-------|--------|-----------------|
| 8 | Restructure introduction per recommended outline | Medium | Medium — improves narrative flow |
| 9 | Add reward bin sensitivity analysis | Medium | Low-Medium — strengthens ablation |
| 10 | Broaden related work to discuss safe-RL-without-cost approaches | Medium | Medium — improves positioning |

### Expected Outcome After P0-P1 Fixes
After addressing all P0 and P1 items, the paper would present a more accurate, transparent, and reproducible contribution. The main technical value (trajectory-level return-agnostic discrimination + conditional diffusion for safe policy learning) would remain intact, while the framing and evidence presentation would be more defensible.

```text
ASCII Diagram — Revision Strategy Roadmap

[Problem: Narrative-mismatch in safety claims]
    -> Fix: Replace absolute safety wording with bounded claim
    -> Expected gain: Claim-evidence alignment, reviewer trust

[Problem: Supervision dependency not discussed]
    -> Fix: Add transparent assumption paragraph
    -> Expected gain: Honest framing, no hidden assumptions

[Problem: vCLUB condition guarantee missing]
    -> Fix: Add condition monitoring + limitation discussion
    -> Expected gain: Theoretical rigor, addresses fragility

[Problem: Diffusion implementation not reproducible]
    -> Fix: Add trajectory shape, conditioning, padding details
    -> Expected gain: Reproducibility, methodological soundness

[Problem: "Only method" claim over-strong]
    -> Fix: Rephrase as bounded comparative claim
    -> Expected gain: Scientifically defensible positioning
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Main performance comparison (Table 1) | 23 tasks across SafetyGym, BulletGym, MetaDrive; 8 baselines | Return ± std; binary safe/unsafe classification | DSPO achieves best safety-first rank in all 3 benchmarks | C3 (benchmark outperformance) | Narrative overclaims absolute safety; MetaDrive tasks all unsafe |
| E2 | Transformer vs. MLP discriminator (Figure 4) | Same architecture comparison; per-task accuracy | Binary classification accuracy | SafetyTransformer outperforms MLP on most tasks | C2 (SafetyTransformer design) | Only accuracy reported; no precision/recall or F1 |
| E3 | Return-agnostic ablation (Table 2) | MetaDrive-hardsparse; 3 variants | Recall%, Accuracy%, F1%, Pearson Corr., Final Score | Return-agnostic MI minimization improves all metrics | C2 (return-agnostic design) | Only 1 task tested; Final Score higher for gradient-penalty variant despite being unsafe |
| E4 | 2D illustrative experiment (Figure 3) | Synthetic 2D return-safety data | Decision boundary visualization | Return-agnostic method produces better decision boundary | C2 (conceptual validation) | Synthetic setting may not capture real complexity |
| E5 | Case study on MetaDrive-hardsparse (Figure 5) | Single trajectory analysis | Safety signal output values | Return-agnostic method correctly identifies low-return safe trajectory | C2 (qualitative validation) | Single case; may not generalize |

### Research-Theme Gap Diagnosis

1. **New Knowledge (partial):** The paper demonstrates that trajectory-level safety signals can be learned from safe demonstrations without cost labels. However, the generality of this finding is limited by: (a) only 3 environments tested, (b) safety demonstrations sourced using cost information from the environments (Appendix C.3), and (c) high variance in discriminator accuracy across tasks.

2. **Reproducibility/Reusability (limited):** The diffusion model implementation details are insufficient for independent reproduction (see Issue 4). The offline dataset suite is well-documented and reusable.

3. **Impact on Practice/Understanding (moderate):** The cost-label-free formulation is practically relevant. The finding that return-agnostic learning improves safety signal quality is an interesting conceptual result. However, the practical impact is tempered by the modest fraction of tasks where DSPO achieves safe policies (15/23).

### Proposed Research Experiments

**P0 Experiment: Cost-conditioned Safety Verification**
- **Target Claim:** C1 (problem setup practicality) and C3 (method outperformance)
- **Hypothesis:** Explicit cost reporting alongside return helps verify safety-return trade-off
- **Design:** Add columns for average cumulative cost (over 20 episodes, 5 seeds) for each method in Table 1
- **Metrics:** Average cost ± std, violation rate (% episodes exceeding cost limit)
- **Success Criterion:** Cost values are consistent with safe/unsafe binary classification
- **Cost/Time:** Low (costs are already computed for safety classification; just need to report them)
- **Expected Gain:** Enables quantitative safety-return trade-off analysis; improves verifiability

**P1 Experiment: vCLUB Condition Monitoring**
- **Target Claim:** C2 (return-agnostic discriminator)
- **Hypothesis:** The condition Eq. (3) holds for most training iterations
- **Design:** Track Δ = DKL(p∥q) − DKL(p(r)p(z)∥q) at each iteration during SafetyTransformer training on 3 diverse tasks (CarGoal1, AntCircle, easy-dense)
- **Metrics:** Fraction of iterations where Δ ≤ 0, mean Δ value
- **Success Criterion:** Δ ≤ 0 for ≥90% of iterations
- **Cost/Time:** Low (log values already computed during training)
- **Expected Gain:** Addresses theoretical fragility concern

**P1 Experiment: Reward Bin Sensitivity Analysis**
- **Target Claim:** C2 (return-agnostic learning)
- **Hypothesis:** The 10-bin discretization is sufficiently fine-grained
- **Design:** Train SafetyTransformer with {5, 10, 20} reward bins on 3 tasks; compare Recall%, Accuracy%, Pearson Corr.
- **Metrics:** Recall%, Accuracy%, F1%, Pearson Corr.
- **Success Criterion:** Performance is not significantly different across bin sizes
- **Cost/Time:** Low (3 additional training runs per task)
- **Expected Gain:** Validates design choice; rules out discretization artifact

**P2 Experiment: Discriminator Performance vs. Safe Demo Count**
- **Target Claim:** C1 (practicality of setup)
- **Hypothesis:** Performance degrades gracefully as safe demonstration count decreases
- **Design:** Train SafetyTransformer with {5, 10, 15, 30} safe demonstrations on CarGoal1 and AntCircle
- **Metrics:** Recall%, Accuracy%, F1%, Pearson Corr., Final Policy Score
- **Success Criterion:** Stable performance down to 10 demonstrations
- **Cost/Time:** Medium (4 runs × 2 tasks)
- **Expected Gain:** Provides practical guidance for minimum safe demonstration requirements

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (before resubmission):
  [Cost reporting in Table 1]
    -> Adds cost columns to all methods
    -> Enables direct safety-return trade-off assessment

P1 (this week):
  [vCLUB condition monitoring] -> [Reward bin sensitivity]
    -> Theoretical reassurance           -> Design validation

P2 (before final submission):
  [Safe demo count sensitivity]
    -> Practical deployment guidance
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Rationale:** The score reflects the paper's balanced profile. On the positive side, the problem formulation is practically motivated and timely, the two-stage pipeline is technically well-integrated, and the benchmarking effort is substantial. However, the score is constrained by: (1) a narrative-empirical mismatch where safety claims overstate the actual results (Issue 1), (2) an unaddressed supervision dependency that weakens the "cost-label-free" framing (Issue 2), (3) theoretical fragility in the MI minimization that is not adequately addressed (Issue 3), and (4) missing implementation details that limit reproducibility (Issue 4). The research value is moderate — the problem is important and the proposed pipeline is sensible, but the evidence does not yet establish that the method reliably solves the problem across diverse settings. Novelty is partially overlapping with existing techniques (transformer discriminators, conditional diffusion, BC distillation) combined in a novel way, but this cannot be fully verified without literature search (Retrieval-Disabled Mode active).

**Post-Revision Target: [6.5, 7.5] / 10**

**Rationale:** If all P0 and P1 issues are addressed — particularly correcting the narrative, transparently discussing assumptions, addressing the vCLUB condition, and adding reproducibility details — the paper would present a more defensible and credible contribution. The research value would be clearer, and the empirical results would be more trustworthy. The target range [6.5, 7.5] reflects the paper's solid technical foundation and the feasibility of the required fixes, while acknowledging inherent limitations (not all tasks solvable, discriminator accuracy variance) that cannot be fully resolved without more fundamental algorithmic advances.

**Scoring breakdown:**
- **Research Value / Significance:** 6/10 — Problem is well-motivated and practically relevant; solution is sensible but safety gains are not universal.
- **Novelty:** 5/10 — Combination of known components is novel for the setting; individual components are established (transformer discriminator, vCLUB, conditional diffusion). Full novelty assessment deferred (Retrieval-Disabled Mode).
- **Technical Soundness / Validity:** 5/10 — Pipeline is logically sound but vCLUB condition guarantee and reproducibility gaps reduce confidence.
- **Empirical Quality:** 5/10 — Comprehensive benchmarking but narrative overclaims relative to data; missing cost reporting; MetaDrive failures not discussed.
- **Clarity / Reproducibility:** 4/10 — Missing diffusion implementation details limit reproduction; some writing issues (generic intro, list-style related work).