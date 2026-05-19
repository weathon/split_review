## Summary
# Final Review Report

## Summary

This paper introduces PATTERN-MARK, a watermarking framework designed specifically for order-agnostic language models (LMs) — models where tokens are not generated sequentially left-to-right, such as ProteinMPNN for protein design and CMLM for machine translation. The core innovation is a Markov-chain-based key sequence generator that produces keys with elevated pattern frequencies, enabling a statistical pattern-based detection algorithm. The vocabulary is partitioned into groups corresponding to each key, and token probabilities are biased toward the group matching the current key. Detection recovers the key sequence from the generated text and uses a hypothesis test on pattern occurrence frequency to determine if a watermark is present.

The paper addresses a genuine gap: existing watermarking methods for sequential LMs rely on n-gram context that is unavailable in order-agnostic generation. The technical approach is well-motivated, with clear reasoning about why both n-gram-based and distortion-free watermarks cannot be directly adapted. Experiments on two tasks (protein generation and machine translation) with three adapted baselines (Soft watermark, Multikey, Unigram) show that PATTERN-MARK achieves competitive detection accuracy at moderate quality cost.

**Key Strengths**: (1) Novel problem formulation — first systematic watermarking approach for order-agnostic LMs, with clear identification of the technical barrier. (2) Clean methodological integration of Markov chains and statistical hypothesis testing. (3) Reasonably comprehensive experiments across two distinct domains.

**Major Weaknesses**: (1) No variance reporting or statistical significance tests for TPR results, making comparison claims weaker than stated. (2) Conclusion and abstract use unqualified superiority language ("superior", "proven") that exceeds what the limited evaluation (2 models, 2 tasks) supports. (3) Robustness evaluation is limited to two attack types with no mechanism-level analysis of why the method is robust. (4) No explicit limitations section, leaving important scope boundaries unstated. (5) Novelty claim as "first work on watermarking for order-agnostic LMs" requires external literature verification that was unavailable in this review run.

**Overall Assessment**: The paper presents a sound and well-motivated technical contribution. The main revision priorities are: (i) adding statistical rigor to experiments, (ii) bounding all superiority claims to match the evidence, (iii) adding a limitations section, and (iv) improving the introduction narrative structure for clearer gap-to-solution mapping.

## Strengths
1. **Novel problem identification and formulation.** The paper correctly identifies that existing watermarking techniques for sequential LMs fundamentally cannot handle order-agnostic generation, and provides a clear technical explanation for why n-gram-based key derivation and distortion-free schemes fail. This problem diagnosis is a genuine contribution to the watermarking literature.

2. **Clean technical design.** The Markov-chain-based key generator paired with statistical pattern detection is an elegant solution. The generator produces key sequences with known pattern statistics, enabling a controlled false positive rate through hypothesis testing. The DP algorithm for computing pattern occurrence probabilities (Alg. 3, Alg. 4) is technically sound and the optimization for alternating patterns (reducing complexity from O(n²2^m) to O(n²m)) is a meaningful practical improvement.

3. **Cross-domain evaluation.** Testing on both protein generation (ProteinMPNN) and machine translation (CMLM) demonstrates applicability across qualitatively different domains — biological sequences and natural language. This strengthens the generality claim more than single-domain evaluations would.

4. **Robustness comparisons under multiple attack types.** The inclusion of both random token modification (protein) and ChatGPT paraphrasing (MT) attacks provides initial evidence about watermark resilience. The observation that PATTERN-MARK maintains detection at moderate attack strengths is informative, even if the analysis depth can be improved.

5. **Reproducibility-oriented details.** The paper provides complete pseudocode for generation (Alg. 1), detection (Alg. 2), and pattern probability computation (Alg. 3, Alg. 4). Ablation studies on pattern length m and transition matrix a11 offer useful guidance for practitioners deploying the method.

## Weaknesses
1. **Insufficient statistical rigor in experimental reporting (Major).** All TPR values in Tables 1-6 are reported as point estimates without standard deviations, confidence intervals, or significance tests. With ~800-1000 sequences per condition, the TPR estimates have measurable sampling variance, especially at moderate TPR levels (30-70%). The claim "consistently outperforms baselines" is not statistically supported for all delta settings. See annotations: Page 8 - Detection Efficiency paragraph.

2. **Unqualified superiority language exceeding evidence scope (Major).** The abstract states "positioning it as a superior watermarking technique" and the conclusion says "has proven to be superior." These claims are not bounded to the evaluated settings (2 models, 2 tasks, specific attack configurations). The word "proven" is particularly inappropriate given the absence of statistical tests and limited evaluation scope. See annotations: Page 1 - Abstract, Page 10 - Conclusion.

3. **Limited robustness analysis (Major).** Only two attack types are tested across two tasks, with no robustness evaluation for protein generation under paraphrasing (acknowledged but not mitigated). More critically, there is no analysis of *why* PATTERN-MARK is more robust — the paper presents numbers but does not explain the mechanism (e.g., pattern distribution across positions provides redundancy against isolated token changes). Quality-matched robustness comparisons are missing. See annotation: Page 9 - Robustness paragraph.

4. **Missing limitations section (Major).** The conclusion does not include a dedicated limitations subsection. Important boundaries left unstated include: (a) only 2 of many order-agnostic architectures tested, (b) optimal pattern length depends on task and sequence length, (c) no evaluation on diffusion-based or fully non-autoregressive models, (d) the distortion-free impossibility proof applies only to exact schemes. See annotation: Page 10 - Conclusion.

5. **Novelty claim requires external verification (Moderate).** The "first work to explore watermarking for order-agnostic LMs" claim cannot be verified without external literature search (unavailable in this run). While the claim appears scoped and plausible, the authors should add a dedicated novelty verification discussion with explicit comparison to any related parallel-decoded or non-autoregressive watermarking approaches.

6. **Introduction narrative structure could be sharper (Minor).** The opening paragraph is generic (AI safety framing) and delays the paper's specific problem until paragraph 2. The technical intuition for why Markov chains solve the key recovery problem is grammatically tangled and logically under-explained. See annotations: Page 1 - Introduction paragraphs.

7. **Related work is a chronological list rather than a thematic comparison (Minor).** The "Statistical watermarks" paragraph lists methods sequentially without organizing them by comparison axes (context-dependent vs. context-independent, distortion-free vs. distortion-based). This makes it harder for readers to see where PATTERN-MARK fits into the landscape. See annotation: Page 2 - Related Work paragraph.

## Key Issues
### Issue 1 (Major): Missing statistical confidence in experimental comparisons
- **Location**: Page 7-8, Section 4.2 Detection Efficiency, Tables 1-2
- **Evidence**: TPR values are reported as single numbers without standard deviation, confidence intervals, or significance tests. For example, Table 1 shows PATTERN-MARK at delta=1.25 achieving 98.80% TPR@FPR=1% but there is no way to assess whether this is statistically distinguishable from Unigram's 92.10% under the same FPR.
- **Root cause**: The paper treats each (model, delta, FPR) combination as producing a deterministic TPR, when in fact the TPR is an empirical estimate with sampling variance across generated sequences.
- **Impact**: Without variance information, readers cannot assess whether the reported advantages are reliable or within noise range. The claim of "consistently outperforms" is weaker than stated.
- **Fix**: Report mean +- std over at least 3 independent runs (or bootstrapped confidence intervals). Add a statistical significance test (e.g., McNemar's test for paired detection outcomes) between PATTERN-MARK and the best baseline at comparable quality levels.

### Issue 2 (Major): Unqualified superiority claims that overstate evidence
- **Location**: Page 1 Abstract, Page 10 Conclusion, Page 2 Contribution list
- **Evidence**: Abstract: "positioning it as a superior watermarking technique." Conclusion: "has proven to be superior in terms of detection accuracy and reliability." Contribution: "superiority of PATTERN-MARK in terms of detection efficiency, generation quality, and robustness."
- **Root cause**: Authors use absolute superiority language that is not bounded to the evaluated settings, models, and attack configurations.
- **Impact**: This language can mislead readers about the maturity of the method. If a reviewer finds a single setting where PATTERN-MARK does not dominate, the entire claim structure is undermined.
- **Fix**: Replace all "superior" claims with bounded comparative statements. E.g., "PATTERN-MARK achieves higher TPR at equivalent or better generation quality on ProteinMPNN and CMLM under the evaluated settings."

### Issue 3 (Major): No limitations section and incomplete robustness analysis
- **Location**: Page 10 Conclusion, Page 9 Robustness section
- **Evidence**: The conclusion is entirely forward-promotional and does not contain a single sentence about the method's limitations. The robustness section only tests 2 attack types and acknowledges but does not mitigate the missing protein-domain paraphrasing evaluation.
- **Root cause**: The paper lacks a dedicated limitations paragraph, which is expected for a methods paper at a top venue.
- **Impact**: Reviewers and readers cannot quickly assess the method's boundary conditions, weakening the paper's scientific completeness.
- **Fix**: Add a "Limitations and Future Work" subsection after the conclusion that explicitly discusses: (a) limited evaluation scope (2 models, 2 tasks), (b) pattern length sensitivity, (c) missing attack types, (d) approximate distortion-free trade-offs.

### Issue 4 (Moderate): Novelty claim verification deferred
- **Location**: Page 2, Contribution list
- **Evidence**: "To the best of our knowledge, this is the first work to explore watermarking for order-agnostic LMs."
- **Root cause**: External literature verification was unavailable in this review run, so the first-claim cannot be confirmed or refuted here.
- **Impact**: If prior work on watermarking non-autoregressive or parallel-decoded LMs exists, the novelty claim would need significant narrowing.
- **Fix**: Authors should proactively add a comparative discussion against any related methods for non-autoregressive or parallel-decoded models, clearly stating overlap and residual novelty.

### Issue 5 (Moderate): Missing mechanism-level robustness analysis
- **Location**: Page 9, Section 4.4 Robustness
- **Evidence**: The paper shows that PATTERN-MARK maintains higher TPR under attacks but offers no explanation of *why* pattern-based detection is more robust than key-recovery-based methods.
- **Root cause**: The paper treats robustness as an empirical observation rather than a design property to be analyzed.
- **Impact**: Without mechanism analysis, readers cannot predict how the method will behave under unseen attack types.
- **Fix**: Add a paragraph analyzing the theoretical robustness advantage: pattern occurrences are distributed across multiple positions, so isolated token modifications only partially disrupt the pattern count statistic, whereas single-key recovery errors can fully break detection in baseline methods.

## Actionable Suggestions
### S1 (Must): Add statistical significance to all TPR comparisons
Add standard deviations and statistical tests to Tables 1-6. Specifically:
- Run watermark generation and detection 3-5 times with different random seeds for each (model, delta, FPR) configuration.
- Report TPR as mean +- std across runs.
- Add a paired significance test (McNemar's test) between PATTERN-MARK and the strongest baseline at matched pLDDT/BLEU levels.
- In the narrative, replace "consistently outperforms" with "achieves higher TPR with p < 0.05 under [specific conditions]."

### S2 (Must): Revise all superiority claims to be evidence-bounded
Replace every instance of "superior", "superiority", and "proven to be superior" with bounded comparative language. Example replacements:
- Abstract: "positioning it as a superior watermarking technique for order-agnostic LMs" → "demonstrating competitive detection accuracy and generation quality on ProteinMPNN and CMLM relative to adapted baselines."
- Conclusion: "has proven to be superior" → "shows competitive detection accuracy under the evaluated settings."
- Contribution list: "superiority of PATTERN-MARK" → "competitive performance of PATTERN-MARK."

### S3 (Must): Add a dedicated limitations subsection
Insert after the Conclusion paragraph:
"**Limitations and Future Work.** This study has several limitations. First, evaluation is limited to two order-agnostic architectures (ProteinMPNN, CMLM) and two tasks; diffusion-based or fully non-autoregressive models may present different challenges. Second, the optimal pattern length m is task-dependent (m=5 for protein, m=4 for MT), requiring tuning for new domains. Third, robustness is evaluated against only two attack types; stronger attacks (e.g., structure-guided protein mutations) remain untested. Fourth, the distortion-free impossibility result applies only to exact schemes; approximate distortion-free approaches may still be feasible and warrant investigation."

### S4 (Must): Add mechanism-level robustness analysis
Insert a paragraph in Section 4.4:
"The improved robustness of PATTERN-MARK can be attributed to the distributed nature of pattern-based detection. Unlike key-recovery methods where a single erroneous key can invalidate detection, PATTERN-MARK's detection statistic aggregates pattern occurrences across the entire sequence. A random token modification at position i affects only the key at position i and at most 2m neighboring pattern windows. Consequently, the pattern count statistic degrades gracefully with attack strength rather than collapsing at a threshold. This explains the gradual TPR decline observed in Tables 3-4."

### S5 (Nice-to-have): Improve introduction narrative structure
Restructure Page 1 Introduction as follows:
- **Sentence 1-2**: Define the problem domain (watermarking for order-agnostic LMs) and why it matters.
- **Sentence 3-4**: State the concrete technical gap (n-gram context unavailable, key recovery impossible).
- **Sentence 5-7**: Present PATTERN-MARK's core idea and why it works (Markov chain enables key recovery through pattern statistics).
- **Sentence 8**: Preview key results.

This front-loads the paper's specific contribution rather than starting with generic AI safety framing.

### S6 (Nice-to-have): Reorganize related work by thematic axes
Restructure the "Statistical watermarks" paragraph into thematic categories:
- Context-dependent methods (requires autoregressive generation) → not applicable.
- Distortion-free methods (requires independent per-token distributions) → not applicable.
- Context-independent methods (Unigram, SelfHash) → applicable but quality-degrading.
- Our method → fills the gap with context-independent but quality-preserving pattern detection.

### S7 (Nice-to-have): Clean up Eq. 1 presentation
Define the shared denominator D once, and add a sentence clarifying that vocabulary partitions are disjoint and exhaustive for deterministic key recovery during detection.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows: (P1) General AI safety + watermarking background → (P2) Order-agnostic LMs and their applications → (P3) PATTERN-MARK proposal → Contribution list. While all components are present, the problem-specific content only begins at line 32 (P2). The first paragraph (P1) reads as generic framing that could open any watermarking paper.

**Three alignment checks:**
- Problem alignment: The stated challenge (no n-gram context in order-agnostic LMs) directly maps to the proposed solution (Markov-chain key generator that does not need n-gram context). ✓
- Variable alignment: Core intro concepts (key sequence, Markov chain, pattern detection) appear as method objects. ✓
- Contribution-evidence alignment: Abstract/intro claims are broadly supported by experiments, but the strength of language ("superior") exceeds evidence. ✗

### Recommended Storyline Candidate (Selected)

**"Problem-Context-Solution-Evidence" structure:**

- P1: State the specific problem domain. Not "watermarking for LMs" but "watermarking for order-agnostic LMs." Explain why order-agnostic generation creates a unique key-recovery problem.
- P2: Show why existing solutions fail. Contrast sequential LM watermarking (works because n-gram context is available) with order-agnostic LM watermarking (fails because context is unavailable). Explain why simple adaptations (e.g., fixed key, Unigram) degrade quality.
- P3: Present PATTERN-MARK's core insight: use a Markov chain to generate keys with known pattern statistics, so detection can work on pattern frequency rather than individual key recovery. Explain the intuition in one clear sentence.
- P4: Summarize contributions with bounded claims and evidence preview.

This structure front-loads the paper's specific novelty, ensures readers understand the gap before the solution, and avoids generic framing.

### Abstract Outline (Complete)

**S1 (Problem + Domain):** "Statistical watermarking for sequentially decoded LMs relies on n-gram context that is unavailable when tokens are generated without a fixed order."

**S2 (Significance + Gap):** "Order-agnostic LMs, used in protein design, machine translation, and speech generation, therefore lack a watermarking method that preserves generation quality while enabling reliable detection."

**S3 (Proposed Method):** "We propose PATTERN-MARK, a watermarking framework that uses a Markov chain to generate key sequences with elevated pattern frequencies, enabling statistical detection based on pattern occurrence counts."

**S4 (Detection + Theory):** "A hypothesis test on the recovered key sequence provides a controlled false positive rate, and the pattern-based statistic degrades gracefully under token modifications."

**S5 (Key Result + Bounded Implication):** "On ProteinMPNN and CMLM, PATTERN-MARK achieves competitive detection accuracy and generation quality relative to adapted baselines under the evaluated settings."

### Introduction Outline (Complete, Paragraph-by-Paragraph)

**P1 — Role: Problem domain and technical barrier (1 paragraph, ~6 sentences)**
- S1: Watermarking for sequential LMs works by deriving keys from n-gram context.
- S2: In order-agnostic LMs, tokens are generated without a fixed left-to-right order.
- S3: This means the n-gram context needed for key derivation and recovery is unavailable.
- S4: Simple adaptations (fixed keys, Unigram) degrade generation quality by applying uniform bias.
- S5: No existing method simultaneously achieves reliable detection and quality preservation for order-agnostic LMs.
- Transition: "In this work, we address this gap with a pattern-based watermarking framework."

**P2 — Role: Method intuition and core idea (1 paragraph, ~6 sentences)**
- S1: Key insight — watermark detection can be based on the *frequency* of key patterns rather than individual key recovery.
- S2: A Markov chain generates key sequences where certain patterns (e.g., alternating keys) appear more frequently than under uniform randomness.
- S3: Each key biases token sampling toward its corresponding vocabulary partition.
- S4: During detection, the key sequence is recovered from generated tokens via partition membership.
- S5: A hypothesis test on the number of pattern occurrences determines whether the text is watermarked.
- S6: This pattern-based approach does not need n-gram context, making it suitable for order-agnostic LMs.
- Transition: "We now describe the framework in detail."

**P3 — Role: Contribution summary with bounded evidence preview (1 paragraph, ~4 sentences)**
- S1: We introduce PATTERN-MARK, a pattern-based watermarking framework for order-agnostic LMs.
- S2: We provide a statistical detection algorithm with controlled false positive rate and an optimized DP computation for alternating patterns.
- S3: Experiments on ProteinMPNN (protein design) and CMLM (machine translation) demonstrate competitive TPR at matched quality levels compared to adapted baselines.
- S4: We analyze robustness under random token modification and paraphrasing attacks.
- Transition: (None — section break to Related Work or Method)

## Priority Revision Plan
### P0 Items (Publication-Critical — Must Address Before Resubmission)

1. **Add statistical significance to TPR comparisons** (Weakness 1, Issue 1)
   - Action: Add mean +- std over 3-5 runs for all TPR values. Add McNemar's test or bootstrapped confidence intervals.
   - Affected sections: Tables 1-6, Section 4.2 text.
   - Expected impact: Strengthens reliability of all comparison claims.
   - Effort: Moderate (requires re-running experiments with multiple seeds).

2. **Revise superiority claims to bounded language** (Weakness 2, Issue 2)
   - Action: Replace all "superior"/"proven"/"superiority" with bounded comparative claims throughout Abstract, Conclusion, and Contribution list.
   - Affected sections: Abstract (Page 1), Contribution list (Page 2), Conclusion (Page 10).
   - Expected impact: Prevents overclaim rejection, aligns language with evidence.
   - Effort: Low (text edits only).

3. **Add limitations subsection** (Weakness 4, Issue 3)
   - Action: Insert a "Limitations and Future Work" paragraph after Conclusion. Cover: limited architectures, task-dependent pattern length, robustness gaps, distortion-free scope.
   - Affected sections: End of Section 5 (Page 10).
   - Expected impact: Demonstrates scientific maturity, preempts reviewer concerns.
   - Effort: Low (one paragraph).

### P1 Items (High Priority — Strongly Recommended)

4. **Add mechanism-level robustness analysis** (Weakness 3, Issue 5)
   - Action: Insert analysis paragraph in Section 4.4 explaining why pattern-based detection provides graceful degradation under attacks.
   - Expected impact: Transforms robustness from an empirical observation to a design insight.
   - Effort: Low-Medium (narrative analysis, no new experiments required).

5. **Improve introduction narrative structure** (Weakness 6)
   - Action: Restructure opening to highlight the specific problem immediately (see Storyline Options section).
   - Expected impact: Better reader engagement, clearer gap-to-solution mapping.
   - Effort: Low (text reorganization).

### P2 Items (Nice-to-Have — Quality Improvement)

6. **Reorganize related work thematically** (Weakness 7)
   - Action: Group references by comparison axes (context-dependent, distortion-free, context-independent).
   - Expected impact: Makes positioning clearer.
   - Effort: Low.

7. **Quality-matched robustness comparison**
   - Action: Add a table comparing TPR@FPR=0.1% for all methods at equal pLDDT/BLEU levels (not equal delta).
   - Expected impact: Fairer comparison, addresses potential reviewer concern about delta-mismatch.
   - Effort: Moderate (requires additional experimental configurations).

8. **Clean up Eq. 1 notation and add partition property statement**
   - Action: Define denominator D once; add sentence that {V_i} are disjoint and exhaustive.
   - Expected impact: Improved reproducibility.
   - Effort: Low.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 (Sec 4.2) | Compare detection TPR across methods | ProteinMPNN (protein, ~800 seq), CMLM (MT, ~1000 seq). Baselines: Soft, Multikey, Unigram | TPR@FPR = {10%, 1%, 0.1%, 0.01%, 0.001%}, pLDDT, BLEU | PATTERN-MARK achieves higher TPR at comparable delta | C2 (detection efficiency) | No variance/std reported; single delta per row; delta ranges differ across methods |
| E2 (Sec 4.3) | Quality-detectability trade-off | Same setup as E1 | pLDDT vs TPR@FPR=0.1% (protein), BLEU vs TPR@FPR=0.1% (MT) | PATTERN-MARK shows favorable trade-off frontier | C2 (trade-off superiority) | No error bars on trade-off curves; "superior" overclaim |
| E3 (Sec 4.4) | Robustness under attacks | Protein: random token modification (epsilon=0-0.3). MT: ChatGPT paraphrasing (epsilon=0-0.3) | TPR@FPR=0.1% | PATTERN-MARK maintains higher TPR under attacks | C2 (robustness) | Only 2 attack types; no protein-domain paraphrasing; no mechanism analysis |
| E4 (Sec 4.5) | Pattern length m sensitivity | Vary m from 2-10 for both tasks | TPR@FPR=0.1% | Optimal m=5 (protein), m=4 (MT) | C1 (method design) | No analysis of why optimum differs by task |
| E5 (Sec 4.5) | Transition matrix a11 sensitivity | Vary a11 from 0-0.5 | pLDDT (protein), BLEU (MT) | Quality stable across a11; a11=0 chosen for max signal | C1 (method design) | a11>0.5 not tested (acknowledged) |
| E6 (Appendix C.1) | Quality comparison: protein diversity | PATTERN-MARK vs baselines at delta=1.50 | 1-gram/2-gram/3-gram entropy | PATTERN-MARK preserves diversity close to no-watermark | C2 (generation quality) | Only one delta value tested |

### Research-Theme Gap Diagnosis

**New Knowledge Contribution**: The paper's primary contribution is a new method for a previously unaddressed problem setting. This is genuine new knowledge if no prior watermarking work targets order-agnostic LMs (requires external verification). The technical novelty lies in the Markov-chain key generation + pattern-based detection, which is a non-trivial adaptation of existing watermarking ideas.

**Reproducibility**: The paper provides complete algorithm pseudocode and dataset descriptions. However, critical low-level details are missing: exact vocabulary partition strategy (random vs. hash-based), handling of <pad> tokens during key recovery in partially generated sequences, and numerical precision for the delta-weighted softmax.

**Potential to Change Practice**: Moderate. Watermarking for protein design (e.g., tracking AI-designed protein sequences for biosecurity) is a real application. The method's ability to work with ProteinMPNN specifically addresses this. However, real-world adoption would require validation on larger, more diverse models and under stronger adversarial assumptions.

### Proposed Research Experiments (P0/P1/P2)

| Experiment ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|--------------|-------------|-----------|---------------|-------------------|---------|------------------|-----------|---------------|
| P0-EXP1 | C2 (detection superiority) | TPR differences are statistically significant | 5 random seeds per (model, delta, FPR) config. Report mean +- std. | Same baselines, same seeds | TPR mean, std, p-value from McNemar's test | p < 0.05 for PATTERN-MARK vs best baseline at comparable quality | 2-3 GPU-days | Converts qualitative comparison to statistically rigorous evidence |
| P0-EXP2 | C2 (robustness mechanism) | Pattern-based detection degrades gracefully because patterns span multiple positions | Compute per-position key recovery accuracy vs pattern occurrence count after token modifications | Compare PATTERN-MARK TPR drop rate to Unigram TPR drop rate | Delta-TPR per epsilon unit | PATTERN-MARK's TPR drop rate is lower than baselines' at epsilon > 0.1 | 1 GPU-day | Provides mechanism-level understanding of robustness |
| P1-EXP3 | C2 (generalizability) | PATTERN-MARK works on other order-agnostic architectures | Test on Mask-Predict (full CMLM) and a diffusion-based protein model (e.g., ESM-IF) | Same baselines, same evaluation protocol | TPR@FPR, pLDDT/BLEU | TPR@FPR=0.1% > 80% with quality drop < 5% | 5-10 GPU-days | Significantly strengthens generalizability claim |
| P1-EXP4 | C2 (robustness completeness) | Stronger attacks (e.g., beam-search paraphrase, structure-guided mutations) reduce but do not eliminate detectability | Evaluate under stronger attack models: beam-search paraphrasing for MT, inverse-folding-based mutations for protein | Same as current robustness experiments | TPR@FPR=0.1% | TPR > 50% at moderate attack strength | 3-5 GPU-days | Addresses the most obvious reviewer counter-argument |
| P2-EXP5 | C1 (distortion-free boundary) | Approximate distortion-free watermark is achievable with acceptance-rejection sampling | Implement a coupling-based approximate distortion-free variant of PATTERN-MARK | Compare to exact PATTERN-MARK and exact distortion-free baselines | KL divergence between P_W and P_M, TPR@FPR | KL < 0.01 nats while maintaining TPR > 80% | 5-7 GPU-days | Explores a boundary condition acknowledged but not tested |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

The paper presents a well-motivated technical contribution to a genuine problem gap (watermarking for order-agnostic LMs). The Markov-chain + pattern-detection approach is clean and the cross-domain evaluation is a strength. However, the score is constrained by: (1) missing statistical rigor in experimental comparisons (variance, significance tests), which weakens the core comparative claims; (2) unqualified superiority language that overstates what the evidence supports; (3) no limitations section, reducing scientific completeness; and (4) the novelty "first work" claim requires external verification that is currently deferred. The research value is moderate: the method is novel for the problem setting, but the evaluation scope (2 models, 2 tasks, 2 attack types) is still narrow for a top-venue paper.

**Post-Revision Target: [7.5, 8.0] / 10**

If the authors address the P0 items (statistical significance, bounded language, limitations section) and at least one P1 item (robustness mechanism analysis), the paper would become a solid 7.5-8.0 submission. Full resolution of the novelty claim and 1-2 P1 experiments (generalizability to another model, stronger attack evaluation) could push the target higher.

```text
ASCII Diagram — Paper Structure & Evidence Map

[Problem: Watermarking for order-agnostic LMs]
    |
    v
[Gap: n-gram context unavailable; existing methods fail]
    |
    v
[Solution: PATTERN-MARK framework]
    |
    +-- Markov-chain key generator (produces pattern-rich key seq)
    +-- Vocabulary partition + probability promotion (Eq. 1)
    +-- Pattern-based statistical detection (Alg. 2)
    +-- DP-based p-value computation (Alg. 3, Alg. 4)
    |
    v
[Evidence]
    +-- Detection efficiency (Tables 1-2) — NO std/significance ✗
    +-- Quality-detectability trade-off (Fig. 3) — promising but unverified ✓/✗
    +-- Robustness (Tables 3-4) — limited attacks, no mechanism ✗
    +-- Ablation: pattern length m, transition matrix a11 (Fig. 4-5) ✓
    |
    v
[Overclaim Risk: "superior"/"proven" language exceeds evidence scope]
```

```text
ASCII Diagram — Revision Strategy Roadmap

[Current issues]                    [Fix]                         [Expected gain]
Missing statistical rigor    -->   Add std + significance tests   Reliable comparisons
Superiority language         -->   Bound claims to evidence       No overclaim rejection
No limitations section       -->   Add limitations paragraph      Scientific completeness
Minimal robustness analysis  -->   Add mechanism analysis         Reviewer confidence
Generic intro narrative      -->   Problem-first structure        Clearer contribution signal
Novelty unverified           -->   Add literature comparison      Confirm/refine novelty claim
```

```text
ASCII Diagram — Related-Work Taxonomy Tree (Layered)

Related Work: Watermarking for LMs
├── Branch 1: Context-Dependent (n-gram based)
│   ├── Leaf 1.1: Gumbel-sampling [Aaronson 2022]
│   ├── Leaf 1.2: Red-green list [Kirchenbauer 2023a]
│   ├── Leaf 1.3: Token-specific learnable [Huo 2024]
│   └── Leaf 1.4: Semantic-key [Liu 2023b]
│   └── Limitation for order-agnostic: key not recoverable
├── Branch 2: Distortion-Free
│   ├── Leaf 2.1: Undetectable [Christ 2023]
│   ├── Leaf 2.2: Unbiased [Hu 2023a, Wu 2023b]
│   └── Leaf 2.3: Robust distortion-free [Kuditipudi 2023]
│   └── Limitation: requires independent token probs + non-repeating keys
├── Branch 3: Context-Independent (no n-gram needed)
│   ├── Leaf 3.1: Unigram [Zhao 2023]
│   └── Leaf 3.2: SelfHash [Kirchenbauer 2023b]
│   └── Limitation: fixed vocabulary split degrades quality
└── Branch 4: Our Work — Pattern-Based (order-agnostic)
    └── PATTERN-MARK: Markov-chain keys + pattern detection
        └── Value: Works without sequential context; preserves quality
```