## Summary
# Final Review Report

## Summary

This paper introduces **Permute-and-Flip (PF) decoding**, a new LLM decoding method adapted from the differential privacy literature, and a complementary **PF watermarking scheme**. The core technical contribution is transferring the PF selection mechanism (McKenna & Sheldon, 2020) to the LLM decoding context, proving that it matches softmax sampling's (2/T)-stability while achieving provably lower perplexity (up to 2x smaller expected suboptimality at the same stability level). The PF watermark leverages the Report-Noisy-Max equivalence with exponential noise to create a detection scheme with precise false-positive-rate control, analogous to the Gumbel watermark.

The paper is theoretically well-grounded (Theorem 3.1, Theorem 4.3) and provides clean empirical validation on C4 and Alpaca datasets using Llama2-7B and TinyLlama models. The experimental results confirm that PF decoding reduces perplexity versus softmax sampling, and PF watermark offers favorable perplexity-detectability tradeoffs compared to KGW and Gumbel baselines.

**Overall assessment**: The paper makes a solid contribution by bridging DP selection mechanisms to LLM decoding and watermarking. The theoretical analysis is rigorous and the experiments are generally well-designed. Key weaknesses include: (1) overclaim in the abstract ("never worse than any other decoder" vs. only proven against softmax), (2) missing limitations discussion (entropy-dependent detection, computational overhead, per-step vs. sequence-level quality gap), (3) non-standard perplexity outlier removal that could bias results, and (4) lack of empirical stability validation under logit perturbation. These are fixable in revision.

## Strengths
**S1. Theoretically rigorous and well-structured analysis.** The paper provides a clean theoretical framework for PF decoding (Theorem 3.1) covering stability, suboptimality bounds, Pareto optimality, and a formal watermark analysis (Theorem 4.3) with precise FPR control. The mathematical derivations are largely correct and well-referenced to prior work (McKenna & Sheldon, 2020; Ding et al., 2021).

**S2. Novel and practical watermarking contribution.** While PF sampling itself is known from DP literature, the PF watermark (Contribution 3) is genuinely new. The connection between Report-Noisy-Max with exponential noise and watermarking via pseudo-random functions is elegant, and the empirical FPR control (Figure 4) is compelling.

**S3. Clean empirical validation with strong baselines.** The experiments compare PF decoding and PF watermark against three baselines (Greedy, Softmax Sampling/KGW watermark, Gumbel watermark) on two datasets (C4, Alpaca) with two model sizes (7B, 1.1B). The results consistently show PF's perplexity advantage and competitive detectability.

**S4. Transparent novelty disclosure.** The authors honestly acknowledge that PF sampling originates from differential privacy (McKenna & Sheldon, 2020) and do not claim it as their invention. This transparency is commendable in an era where novelty claims are often inflated.

**S5. Practical usability.** PF decoding is presented as a drop-in replacement for softmax sampling in existing decoding frameworks (including nucleus/top-p sampling), which lowers the barrier for adoption. The code is open-sourced.

## Weaknesses
**W1. Abstract overclaim: "never worse than any other decoder" (Page 1).** The abstract claims PF decoding is "never worse than any other decoder," but Theorem 3.1 only proves it is never worse than softmax sampling (Statement 3). Greedy decoding, for instance, achieves zero per-step suboptimality but lacks stability. The Pareto-optimality claim (Statement 5) states that no equally-stable decoder dominates PF, which is a different and weaker claim than the abstract's blanket statement. This is a factual overclaim that must be corrected.

**W2. Perplexity outlier removal introduces potential bias (Page 9, Appendix C).** The paper removes the top and bottom 3% of per-prompt perplexity scores as outliers. This non-standard practice could systematically favor PF over Softmax if PF has lower variance (the presented standard errors suggest this: PF's standard errors are consistently smaller than Sampling's). Raw (unfiltered) perplexity should be reported alongside filtered values to ensure comparability.

**W3. Missing limitations discussion in Conclusion (Page 10).** The conclusion is brief and does not address known limitations that the paper itself demonstrates: (a) PF watermark detection power degrades in low-entropy settings (Example 4.4), (b) PF's perplexity gains come at a measurable diversity cost (MAUVE scores in Table 2 show PF lower than Sampling), (c) computational overhead of vocabulary permutation is not discussed. These should be explicitly acknowledged.

**W4. No empirical validation of stability under logit perturbation.** The stability definition (Definition 2.1) is a core theoretical contribution and is claimed to protect against data poisoning and jailbreaking attacks. Yet no experiment measures the log-probability ratio under perturbed logits for PF vs. softmax vs. non-stable decoders. The practical relevance of stability is asserted but not demonstrated.

**W5. Per-step utility assumption is justified but not validated.** The paper reduces sequence-level decoding to per-step utility maximization, claiming logits "may have already accounted for potential future utility like the Q function in reinforcement learning." This is an unverified assumption for typical LLMs. While theoretically clean, the paper does not test whether PF's per-step perplexity gains translate to improved downstream task performance.

**W6. Detectability-greediness tradeoff analysis is limited to |V|=2 (Page 8).** The theoretical tradeoff comparison (Figure 2b) uses only a two-token vocabulary. While the real-data results validate the overall trend, the paper would benefit from numerical simulation at larger vocabulary sizes to strengthen this analysis.

## Key Issues
### Ranked Defect Board (Top Issues by Severity and Research-Value Impact)

| Rank | Issue | Severity | Location | Impact | Fixable |
|------|-------|----------|----------|--------|---------|
| 1 | Abstract overclaim: "never worse than any other decoder" | Major | Page 1 - Abstract | Misleading; inflates contribution beyond proven scope | Yes — scope-bound wording |
| 2 | Perplexity outlier removal bias | Major | Page 9 - Experiment Metrics, Appendix C | Could distort reported ranking between PF and Sampling | Yes — report raw + filtered |
| 3 | Missing limitations in Conclusion | Major | Page 10 - Conclusion | Reduces scientific rigor; overstates readiness | Yes — add limitations paragraph |
| 4 | No empirical stability validation | Major | Page 2 - Definition 2.1, Page 3-4 - Theorem 3.1 | Core theoretical claim untested empirically | Yes — add logit perturbation experiment |
| 5 | Per-step utility assumption unvalidated | Major | Page 2 - Problem Setup | Claims about "better decoding" may not transfer to downstream tasks | Partial — add task-based evaluation |
| 6 | Detectability tradeoff limited to |V|=2 | Minor | Page 8 - Figure 2 | Reduces theoretical generality | Yes — extend numerical simulation |

### Issue 1 (Top Priority): Abstract Overclaim

**Evidence**: Abstract states PF decoder "is provably up to 2x better in its quality-stability tradeoff than sampling and never worse than any other decoder" (Page 1, lines 15-17). Theorem 3.1 (Page 4) Statement 3 says "PF-sampling is never worse than Softmax-sampling" — not "any other decoder." Statement 5 (Pareto optimality) says PF is not dominated by any equally-stable decoder. The abstract conflates these two distinct claims.

**Impact**: Readers and reviewers may interpret this as a universal dominance claim that is not supported by the theoretical results. This is a clear overclaim that undermines scientific credibility.

**Fix**: Replace with: "PF decoding is provably never worse than softmax sampling at the same stability level, and is Pareto-optimal among equally-stable decoders." See annotation on Page 1 - Abstract.

### Issue 2 (High Priority): Perplexity Outlier Removal

**Evidence**: Appendix C states "we remove the top and bottom 3% of perplexity scores as outliers and then calculate the average perplexity and standard error" (Page 19). This is non-standard and not justified.

**Impact**: If PF has lower perplexity variance (as standard errors suggest), removing high-perplexity outliers could disproportionately benefit baseline methods that generate more diverse (thus sometimes higher-perplexity) text. The relative ranking could be affected.

**Fix**: Report both raw (unfiltered) perplexity and filtered perplexity; or justify the 3% threshold with a systematic sensitivity analysis showing the ranking is unchanged across thresholds.

### Issue 3 (High Priority): Missing Limitations

**Evidence**: The Conclusion (Page 10) does not discuss any limitations of PF decoding or PF watermark. The paper itself demonstrates that PF watermark detection power depends on text entropy (Example 4.4) and that PF reduces diversity (MAUVE scores in Table 2).

**Impact**: The omission of limitations creates an impression that the method is universally superior, which is not supported by the evidence.

**Fix**: Add a dedicated limitations paragraph. See annotation on Page 10 - Conclusion for a Mentor Revised Version.

## Actionable Suggestions
### Suggestion 1: Correct the Abstract's Scope Overclaim (Must)

**Problem**: The abstract claims PF is "never worse than any other decoder" — this is not what Theorem 3.1 proves.

**Action**: Replace the overclaiming sentence with a scoped version. See annotation on Page 1 - Abstract for the full Mentor Revised Version.

**Key replacement text**: 
> "It enjoys stability properties identical to standard softmax sampling, but is provably never worse in expected utility and achieves up to 2x smaller expected suboptimality at the same stability level. No equally-stable decoder can uniformly dominate PF (Pareto optimality)."

### Suggestion 2: Report Raw Perplexity Alongside Filtered Values (Must)

**Problem**: The 3% outlier removal is non-standard and could bias results.

**Action**: Add a supplementary table with raw (unfiltered) perplexity. Also run a sensitivity analysis showing relative rankings are unchanged with 1%, 3%, 5% removal thresholds. Add a brief justification in the main text.

### Suggestion 3: Add Explicit Limitations Paragraph in Conclusion (Must)

**Problem**: The conclusion omits known limitations.

**Action**: Replace the current conclusion with a structured version containing three parts: (1) validated findings, (2) bounded limitations, (3) future work. See annotation on Page 10 - Conclusion for a Mentor Revised Version.

### Suggestion 4: Add Empirical Stability Validation (Nice-to-have / Strongly Recommended)

**Problem**: Stability is a core theoretical concept but never measured.

**Action**: Design a simple experiment: (a) take a set of prompts, (b) compute original logits u, (c) add small perturbations δ (e.g., δ=0.1, 0.5, 1.0 in ∞-norm) to produce ũ, (d) measure the log-probability ratio |log(p_{PF(ũ)}(y)/p_{PF(u)}(y))| for each token y, (e) compare against the theoretical bound Lδ = (2/T)δ. Show that PF and Softmax satisfy the bound while Greedy/Top-k violate it. This would be a compelling empirical demonstration.

### Suggestion 5: Clarify the "First" Claim in Related Work (Nice-to-have)

**Problem**: Page 16 (Appendix A.1) claims "we are the first to introduce a rigorous stability definition."

**Action**: Qualify this as "To our knowledge, we are the first to formulate and study a perturbation-stability property specific to LLM decoding," making explicit that the definition itself builds on DP concepts.

### Suggestion 6: Add Computational Cost Comparison (Nice-to-have)

**Problem**: PF decoding permutes the vocabulary at each step, with O(|V| log |V|) complexity per token.

**Action**: Report wall-clock time per token for PF vs. softmax sampling vs. greedy decoding at the same batch size and sequence length. This would help practitioners assess the practical tradeoff.

### Suggestion 7: Extend Tradeoff Analysis Beyond |V|=2 (Nice-to-have)

**Problem**: The theoretical detectability-greediness tradeoff (Figure 2) is only shown for two-token vocabularies.

**Action**: Add numerical simulation for |V|=10, 100, 1000 with random logits to show that the tradeoff advantage generalizes to larger vocabularies.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current narrative follows this structure:
- **Introduction P1**: LLM background and decoder definition (somewhat generic)
- **Introduction P2**: Problem setup, per-step utility, stability definition
- **Introduction P3**: Multi-constraint analysis leading to research question
- **Introduction P4**: Fourfold contribution list
- **Introduction P5**: Novelty disclosure

**Problems**: The introduction front-loads technical definitions (P1-P2) before establishing the research stakes. The core research question ("Is there a decoding method as stable as softmax but with lower perplexity?") appears only on Page 3, after the stability definition. Readers would benefit from seeing the question earlier.

### Recommended Storyline (Revised)

**Abstract Outline (4-5 sentence structure)**:

S1 (Problem + Domain): "Large language model decoding involves a fundamental tradeoff between text quality, diversity, stability against logit perturbations, and watermarkability."

S2 (Gap): "Among existing methods, only softmax sampling simultaneously satisfies all four desiderata, but its perplexity is substantially higher than more deterministic alternatives."

S3 (Proposed Method): "We introduce Permute-and-Flip (PF) decoding — adapted from the differential privacy literature — which provably matches softmax sampling's stability guarantee while achieving strictly lower expected perplexity (up to 2x smaller suboptimality at the same stability level)."

S4 (Watermark): "We further design a PF watermarking scheme that leverages the Report-Noisy-Max equivalence of PF sampling, enabling precise false-positive-rate control without altering the token distribution."

S5 (Result): "Experiments on C4 and Alpaca datasets with Llama2-7B demonstrate that PF watermark achieves the best known tradeoff between detection accuracy and perplexity compared to Gumbel and Green-Red watermarks."

**Introduction Outline (Paragraph-by-Paragraph)**:

P1 — Big Picture and Stakes (revised): 
Role: Establish why decoding matters for LLM safety and quality. State the four practical desiderata concisely.
Transition: "However, no existing decoding method simultaneously satisfies all four."
Claim: The choice of decoder directly affects text quality, diversity, robustness to adversarial logit perturbations, and the ability to watermark outputs.

P2 — Gap Analysis (revised):
Role: Survey existing methods along the four axes, using a condensed version of Table 1. Show that only softmax sampling checks all boxes.
Transition: "This raises a natural question: can we match softmax sampling's stability while reducing perplexity?"
Claim: There is a known method from differential privacy — Permute-and-Flip — that achieves exactly this.

P3 — Solution Intuition (revised): 
Role: Explain PF decoding intuitively (permute + flip coins) before technical details. Highlight the "without replacement" sampling advantage over Softmax's "with replacement" rejection sampling.
Transition: "We now formalize these properties."
Claim: PF decoding provides (2/T)-stability, never-worse expected utility vs. softmax, and Pareto-optimal tradeoff.

P4 — Watermark Contribution (revised):
Role: State the watermarking motivation and the key technical insight (Report-Noisy-Max with exponential noise enables pseudo-random watermarking).
Transition: None needed — this paragraph ends with the contribution list.
Claim: PF watermark provides computational indistinguishability, precise FPR control, and high detection power.

P5 — Contribution List + Paper Roadmap (retain from current):
Role: Enumerate four contributions clearly. Add sentence about empirical validation scope.
Transition: "Section 2 formalizes the problem; Section 3 presents PF decoding and its theoretical properties; Section 4 develops the PF watermark; Section 5 validates both empirically."

### Comparison: Current vs. Recommended Storyline

| Alignment Check | Current | Recommended |
|----------------|---------|-------------|
| Problem Alignment | Moderate — technical definitions come before stakes | Strong — stakes first, then gap, then solution |
| Variable Alignment | Good — key concepts (logits, stability) are carried through | Same, but stability motivation appears earlier |
| Contribution-Evidence Alignment | Good — claims map to experiments | Improved — abstract S5 explicitly bounds the empirical contribution |

The recommended storyline moves the research question earlier, reduces the front-loaded technical setup, and provides a clearer motivation-to-solution narrative.

## Priority Revision Plan
### P0 — Publication-Critical (Must Fix Before Resubmission)

| Priority | Item | Effort | Impact | Expected Improvement |
|----------|------|--------|--------|---------------------|
| P0.1 | Correct abstract overclaim (W1) | 15 min | High | Removes factual error, aligns with Theorem 3.1 |
| P0.2 | Add limitations paragraph to Conclusion (W3) | 30 min | High | Completes scientific disclosure |
| P0.3 | Report raw perplexity alongside filtered (W2) | 1 hr | High | Removes reproducibility concern about ranking bias |

### P1 — Strongly Recommended (Should Fix Before Resubmission)

| Priority | Item | Effort | Impact | Expected Improvement |
|----------|------|--------|--------|---------------------|
| P1.1 | Add empirical stability validation experiment (W4) | 2-3 days | High | Validates core theoretical claim empirically |
| P1.2 | Clarify "first" claim in related work (Appendix A.1) | 15 min | Medium | Prevents novelty overclaim |
| P1.3 | Add wall-clock time comparison for PF vs baselines | 1 day | Medium | Helps practitioners assess deployment costs |

### P2 — Quality Improvement (Nice-to-Have)

| Priority | Item | Effort | Impact | Expected Improvement |
|----------|------|--------|--------|---------------------|
| P2.1 | Extend tradeoff analysis beyond |V|=2 | 1-2 days | Medium | Strengthens theoretical generality |
| P2.2 | Add downstream task evaluation (QA, summarization) | 3-5 days | Medium | Tests whether per-step gains transfer to tasks |
| P2.3 | Add significance tests for perplexity comparisons | 1 day | Medium | Provides statistical rigor |

### Revision Execution Order

```
Step 1 (today): P0 items — fix abstract, add limitations, report raw perplexity.
Step 2 (this week): P1 items — stability experiment, computational cost, fix related-work claim.
Step 3 (before submission): P2 items — extended tradeoff analysis, downstream tasks, significance tests.
```

### Revision Strategy Roadmap (ASCII Diagram)

```text
[Current manuscript]
    |
    v
[P0: Urgent fixes]
    ├── Abstract: "never worse than any decoder" 
    │   → "never worse than softmax; Pareto-optimal among stable decoders"
    ├── Conclusion: add limitations paragraph 
    │   → entropy-dependent detection, diversity cost, O(|V|log|V|) overhead
    └── Perplexity reporting: add raw (unfiltered) values
        → eliminates ranking bias concern
    |
    v
[P1: Strongly recommended]
    ├── Stability experiment: measure log-prob ratio under ∞-norm perturbation
    │   → validates core theoretical claim empirically
    ├── Related work: scope "first" claim
    │   → prevents overclaim
    └── Wall-clock time comparison
        → enables practitioner adoption decisions
    |
    v
[P2: Quality improvements]
    ├── |V|>2 tradeoff simulation
    ├── Downstream task evaluation
    └── Significance testing
    |
    v
[Revised manuscript — stronger, more defensible]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|--------|-----------|-------|---------|-------------|----------------|------------|
| E1 | Compare PF vs Sampling perplexity (C4, T=1.0) | Llama2-7B, 600 samples from C4, max 256 tokens | PPL1 (7B), PPL2 (13B) | PF: 8.94 vs Sampling: 12.47 | C1: PF reduces perplexity | Outlier removal applied; no significance test |
| E2 | Compare PF vs Sampling perplexity (C4, T=0.8) | Same as E1 | PPL1, PPL2 | PF: 3.54 vs Sampling: 4.23 | C1 | Same as E1 |
| E3 | Compare PF vs Sampling perplexity (Alpaca, T=1.0) | Llama2-7B-Chat, 550 samples | PPL1, PPL2 | PF: 1.65 vs Sampling: 1.74 | C1 | Smaller gap; QA task has lower entropy |
| E4 | Watermark detection performance (C4, T=1.0) | Llama2-7B, 500 watermarked + 500 unwatermarked | AUC, TPR@1%FPR, F1 | PF WM AUC=0.995, TPR=0.984 | C2, C3 | Near-ceiling performance; limited discrimination |
| E5 | Watermark detection (Alpaca, T=1.0) | Same as E4 on Alpaca | AUC, TPR@1%FPR | PF WM AUC=0.979, TPR=0.810 | C2, C3 | Lower TPR; lower entropy setting |
| E6 | FPR control validation | 3000 negative examples (C4+Alpaca+unwatermarked) | Empirical vs theoretical FPR | Tight alignment across seeds | C2 | Validated at multiple α levels |
| E7 | Robustness to paraphrasing (DIPPER-1/2) | C4, 4-token prefix | AUC, TPR | PF comparable to Gumbel under attack | C3 | All methods degrade under strong paraphrase |
| E8 | Impact of text length on detection | C4, truncation to 30-200 tokens | AUC, TPR | AUC=0.980 even at 30 tokens | C3 | Only length, not content type, varied |
| E9 | TinyLlama watermark detection | TinyLlama-1.1B-Chat, Alpaca | AUC, TPR | PF WM AUC=0.999, TPR=0.986 | C3 | Strong results on small model |

### Research-Theme Gap Diagnosis

| Theme | Current Support | Gap |
|-------|----------------|-----|
| New knowledge (theoretical understanding of PF in decoding context) | Strong: Theorem 3.1 provides comprehensive theoretical characterization | Weakness W4: stability claim is untested empirically |
| Reproducibility | Good: code available, algorithms clearly specified | Weakness W2: outlier removal procedure could affect reproducibility of perplexity results |
| Impact on practice/understanding | Moderate: PF shown to reduce perplexity, but practical value for downstream tasks untested | Downstream evaluation (QA accuracy, summarization quality) not performed |
| Watermark robustness under real-world attacks | Moderate: tested only with DIPPER and random deletion | Broader attack surface (substitution, back-translation) not explored |

### Proposed Research Experiments (P0/P1/P2)

**P0 Experiment: Raw Perplexity Sensitivity**
- Target claim: PF perplexity advantage over Sampling
- Hypothesis: The relative ranking (PF < Sampling) is insensitive to outlier removal threshold
- Minimal design: Report mean ± std for unfiltered data and for 1%, 3%, 5% removal thresholds
- Controls: Same datasets, same models
- Metrics: PPL1, PPL2
- Success criterion: Relative ordering PF < Sampling holds across all thresholds
- Estimated cost: ~2 hours (re-running analysis script)
- Expected gain: Removes bias concern (Weakness W2)

**P1 Experiment: Stability Under Logit Perturbation**
- Target claim: C1 — PF is (2/T)-stable (Definition 2.1)
- Hypothesis: The log-probability ratio |log(p_{PF(ũ)}(y)/p_{PF(u)}(y))| ≤ (2/T)·‖ũ−u‖_∞ for all tokens y
- Minimal design: For 100 prompts, compute u, add perturbations δ ∈ {0.1, 0.5, 1.0} in ∞-norm, measure log-prob ratio for each token. Compare PF, Softmax, Greedy, Top-k.
- Controls: Same prompts, same perturbations across all methods
- Metrics: Max observed log-prob ratio vs theoretical bound Lδ
- Success criterion: PF and Softmax satisfy the bound; Greedy/Top-k violate it for some δ
- Estimated cost: 2-3 days
- Expected gain: Validates core theoretical claim (Weakness W4)

**P1 Experiment: Computational Cost Comparison**
- Target claim: PF is practical as drop-in replacement
- Hypothesis: PF wall-clock time per token is comparable to softmax sampling
- Minimal design: Generate 100 sequences of 256 tokens each with each method at batch size 1, measure median tokens-per-second
- Controls: Same hardware (A6000), same model (Llama2-7B)
- Metrics: Tokens/sec, peak GPU memory
- Success criterion: PF is within 2x of softmax sampling
- Estimated cost: 1 day
- Expected gain: Supports practicality claims; enables practitioner decisions

**P2 Experiment: Downstream Task Evaluation**
- Target claim: PF's per-step perplexity improvement benefits end tasks
- Hypothesis: PF-generated text achieves better or competitive performance on QA (e.g., TriviaQA) and summarization (e.g., XSum) vs softmax sampling
- Minimal design: Generate outputs with PF and Sampling (T=1.0), then evaluate using automated metrics (ROUGE-L for summarization, F1 for QA)
- Controls: Same prompts, same model, same temperature
- Metrics: ROUGE-L, F1, human preference (optional)
- Success criterion: PF is not worse than sampling on task metrics
- Estimated cost: 3-5 days
- Expected gain: Tests transfer of per-step gains to sequence-level quality (Weakness W5)

### Experiment Upgrade Plan (ASCII Diagram)

```text
Current experiments
    ├── E1-E3: Perplexity comparison (PF < Sampling) ✓
    ├── E4-E6: Watermark detection ✓
    ├── E7-E8: Robustness & length ✓
    └── E9: Small model validation ✓
           |
           v
P0 additions (urgent)
    └── Raw perplexity sensitivity (remove outlier concern)
           |
           v
P1 additions (strongly recommended)
    ├── Stability perturbation experiment (validate Definition 2.1)
    └── Computational cost comparison (practicality)
           |
           v
P2 additions (quality improvement)
    └── Downstream task evaluation (QA, summarization)
           |
           v
[Complete validation: theory + practice + deployment]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 7/10**

**Score Rationale**: The paper makes a solid theoretical contribution by bridging differential privacy mechanisms to LLM decoding and watermarking. The theoretical analysis is rigorous (Theorem 3.1, Theorem 4.3), the PF watermark is novel, and the empirical validation is reasonably comprehensive with strong baselines. However, the score is constrained by: (1) the abstract overclaim ("never worse than any other decoder") which undermines credibility if uncorrected, (2) the non-standard perplexity outlier removal that raises reproducibility concerns, (3) the absence of empirical stability validation for a core theoretical claim, and (4) missing limitations discussion. All four are fixable, which is reflected in the post-revision target.

**Scoring Dimensions**:
- Research Value / Contribution: 7/10 (solid theoretical + watermark contribution, but PF sampling is known from DP literature)
- Novelty: 7/10 (PF watermark is genuinely new; decoder application is a transfer, not invention)
- Validity / Soundness: 7/10 (theory is correct; experiments have minor methodological concerns)
- Reproducibility: 7/10 (code available, but outlier removal procedure needs clarification)
- Presentation / Clarity: 7/10 (well-structured, but abstract overclaim and missing limitations reduce clarity)

**Post-Revision Target**: [7.5, 8.5]/10

After addressing P0 items (abstract fix, limitations, raw perplexity) and P1 items (stability experiment, computational cost), the paper's score would rise to the 7.5-8.5 range. The upper bound of 8.5 assumes all P0 and P1 items are satisfactorily resolved.