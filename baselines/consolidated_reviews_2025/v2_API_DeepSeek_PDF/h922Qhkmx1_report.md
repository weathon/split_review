## Summary
# Final Review Report

## Summary

This paper presents Multi-Source Diffusion Models (MSDM), a diffusion-based generative framework that learns the joint probability distribution of musical source waveforms (Bass, Drums, Guitar, Piano) to simultaneously enable three tasks: unconditional mixture generation, partial generation (source imputation), and source separation. The key methodological contributions are (i) training a score network on the joint distribution p(x1,...,xN) rather than modeling each source independently or modeling mixtures only, (ii) introducing source imputation as a novel application, and (iii) proposing a Dirac delta-based posterior score for source separation that constrains one source to equal the mixture residual.

The paper is technically sound, the joint-distribution modeling approach is well-motivated, and the experimental work on Slakh2100 provides reasonable evidence for the method's capabilities. However, the paper has several notable weaknesses: (1) novelty claims are imprecisely scoped — the "first model to handle both generation and separation" claim overreaches without external literature verification; (2) the separation comparisons are not resource-fair — MSDM uses 405M parameters (10x more than Demucs's 40M) and achieves modestly better SI-SDRI on some stems while being substantially worse on others; (3) the MUSDB18-HQ results, relegated to an appendix, show MSDM is ~3x worse than Demucs on real recordings, which critically undermines the "general audio model" framing; (4) inference speed (4.6s for 12s of audio) is too slow for interactive use but is not discussed as a limitation; and (5) key experimental results lack variance or significance reporting. These issues are fixable with careful revision.

## Strengths
**S1 — Well-motivated joint-distribution framework.** The core idea of training a single model on the joint distribution of sources p(x1,...,xN) is conceptually elegant and principled. Unlike prior work that models either mixtures (p(y)) or independent sources (p_n(x_n)), the joint-distribution approach preserves inter-source dependencies (e.g., bass following drum rhythm) while enabling both generative and discriminative tasks from one model. This is a genuine conceptual advance over both paradigms.

**S2 — Unified multi-task capability from a single network.** The paper demonstrates that a single trained model can perform three distinct tasks — unconditional mixture generation, source imputation, and source separation — without any task-specific architectural modifications or fine-tuning. This unification is the paper's strongest practical contribution and is convincingly demonstrated across Tables 1-3.

**S3 — Rigorous mathematical derivation of the Dirac posterior.** The Dirac likelihood formulation in Appendix A is mathematically well-developed. The derivation traces the posterior score through marginalization, Bayes theorem, and the chain rule to arrive at a clean expression (Eq. 22-23) that is efficiently implementable (Algorithm 1). The connection to the Gaussian likelihood as the γ(t) → 0 limit is clearly explained.

**S4 — Comprehensive evaluation across tasks.** The paper provides both objective metrics (FAD, sub-FAD, SI-SDRI) and subjective listening tests for generation tasks. The listening tests involve 32 and 21 participants respectively for total and partial generation, which is reasonable for a conference paper. The hyperparameter search (Appendix D, Table 5) is thorough and covers both Dirac and Gaussian variants across multiple Schurn values.

**S5 — Strong results on Bass and Drums separation.** ISDM Dirac with correction steps achieves 19.36 dB (Bass) and 20.90 dB (Drums) on Slakh2100, outperforming Demucs + Gibbs (512 steps) by 2.2 dB and 1.29 dB respectively. These are meaningful per-instrument improvements, particularly for the rhythmic foundation of music mixtures.

## Weaknesses
**W1 — Imprecise novelty claims.** The paper makes strong "first" claims ("Our method is the first example of a single model that can handle both generation and separation tasks") without precise scope bounding. Related work such as SingSong (Donahue et al., 2023) demonstrates conditional generation from vocals, blurring the binary generation/separation distinction. The claim also lacks external literature verification (retrieval unavailable in this run). The contributions need tighter bounding: the genuine novelty is in modeling the joint distribution of multiple sources for simultaneous unconditional generation and separation — not the "first model" to address both tasks broadly.

**W2 — Unfair comparison with Demucs baselines.** MSDM uses 405M parameters while Demucs uses only 40M (10x gap). The paper claims "competitive" results but the overall advantage (MSDM Dirac correction: 16.48 dB vs Demucs: 16.11 dB All) is only +0.37 dB despite 10x more parameters. Per-instrument, MSDM underperforms Demucs on Drums (18.68 vs 19.44) and Guitar (barely 15.38 vs 15.30). The ISDM variant uses 4 × 405M = 1.62B parameters. These resource disparities are insufficiently discussed in the main text.

**W3 — MUSDB results contradict "general audio model" narrative.** When trained on the real-recording MUSDB18-HQ dataset, MSDM achieves only 4.24 dB All SI-SDRI vs Demucs v2's 12.55 dB — a nearly 3x gap. Direct transfer from Slakh2100 yields negative SI-SDRI (-0.88 dB). These critical results are buried in Appendix E and directly weaken the claim of being "a step toward general audio models." The paper should prominently discuss this limitation.

**W4 — Missing statistical rigor.** No standard deviations, confidence intervals, or significance tests are reported for any experimental results (Tables 1, 2, 3). The subjective listening tests (32 and 21 participants) report only mean ± std without paired comparisons. Without variance information, it is impossible to determine whether the reported improvements (e.g., FAD 6.55 vs 6.67, or ISDM Dirac 17.27 vs Demucs+Gibbs 17.73) are statistically meaningful.

**W5 — Inference speed not discussed as a limitation.** MSDM requires 4.6 seconds for a 12-second audio segment on an RTX A6000 (Table 4). ISDM requires 18.4 seconds. This makes real-time or interactive use infeasible, contradicting the paper's claim that "this flexibility paves the way for more advanced music composition tools, where users can easily control and manipulate individual sources." The slow inference is a critical practical limitation that is not mentioned in the Limitations section.

**W6 — Incomplete assessment of the Dirac posterior approximation.** The derivation (Appendix A) replaces an integral over y(t) with a point estimate at y(0), and this approximation's error is not analyzed. At high noise levels (large σ(t)), the variance Nσ²(t)I of p(y(t)|y(0)) can be large, making the Dirac constraint potentially inaccurate. The paper does not discuss when or why the Dirac approximation might degrade separation quality.

**W7 — Related Work organized as a list rather than by comparison axes.** Section 2 reads as a chronological survey rather than a categorical comparison. The key conceptual distinction — modeling p(y) vs p(x1,...,xN) vs p_n(x_n) — is not used as the organizing principle, making it harder for readers to quickly understand where MSDM fits in the landscape.

**W8 — Limited scope not fully acknowledged.** The model handles only 4 instrument classes (Bass, Drums, Guitar, Piano) with 12-second context windows. Real-world music involves vocals, many more instruments, and multi-minute structure. The paper's framing as "general audio models" is disproportionate to this narrow scope.

## Key Issues
### Issue 1: MUSDB results contradict main claims [Severity: Critical, Fixability: Medium]
**Anchor:** Page 20 - Appendix E, Table 6
**Evidence:** MSDM trained on MUSDB18-HQ achieves 4.24 dB All SI-SDRI vs Demucs v2's 12.55 dB. Direct Slakh→MUSDB transfer yields -0.88 dB (worse than mixture).
**Impact:** Directly undermines the abstract's claim of being "a step toward general audio models" and the conclusion's claim of "results comparable to state-of-the-art regressor models." The SOTA comparison is only valid on the synthetic Slakh2100 dataset, not on real recordings.
**Required action:** Move MUSDB results to main text, soften generality claims, and add a paragraph analyzing the domain gap.

### Issue 2: Resource-unfair comparison with Demucs [Severity: Critical, Fixability: High]
**Anchor:** Page 18 - Appendix C, Table 4; Page 9 - Table 3
**Evidence:** MSDM uses 405M parameters (10x Demucs's 40M). MSDM Dirac achieves only +0.37 dB overall advantage (16.48 vs 16.11 dB All). Per-instrument: MSDM underperforms on Drums.
**Impact:** The "competitive" and "comparable" framing is misleading without disclosing this 10x resource asymmetry. A 40M-parameter Demucs achieving nearly equal performance to a 405M generative model suggests the generative approach is less parameter-efficient for separation.
**Required action:** Explicitly report parameter count in the main results table caption. Add a parameter-efficiency discussion. Compare apples-to-apples (e.g., same architecture, different training objective) where possible.

### Issue 3: Missing statistical reporting [Severity: Major, Fixability: High]
**Anchor:** Page 8-9 - Tables 1, 2, 3
**Evidence:** No standard deviations, confidence intervals, or significance tests reported for any quantitative result. Subjective tests report variance but without paired comparison.
**Impact:** Without variance information, readers cannot assess the reliability of reported improvements. The FAD gap (6.55 vs 6.67, Δ=0.12) and the subjective coherence gap (6.35 vs 5.67, Δ=0.68) could be within noise.
**Required action:** Add multi-seed experiments (≥3 seeds) with standard deviations for all main results. Report p-values or effect sizes for key comparisons.

### Issue 4: Slow inference undermines claimed application [Severity: Major, Fixability: Low]
**Anchor:** Page 18 - Appendix C, Table 4
**Evidence:** MSDM: 4.6s for 12s audio → ~2.6x real-time. ISDM: 18.4s for 12s audio.
**Impact:** The conclusion states the model "paves the way for more advanced music composition tools, where users can easily control and manipulate individual sources." At 2.6-18.4x real-time, interactive use is not feasible.
**Required action:** Add inference speed to the Limitations section. Qualify the application claims. Consider reporting real-time factor explicitly.

### Issue 5: Overclaimed novelty without retrieval verification [Severity: Major, Fixability: High]
**Anchor:** Page 1 - Abstract; Page 2 - Introduction
**Evidence:** "Our method is the first example of a single model that can handle both generation and separation tasks." "To our knowledge, no model in deep learning literature can perform both tasks simultaneously."
**Impact:** These maximalist claims are difficult to verify without comprehensive literature review. SingSong (cited in the paper) performs accompaniment generation conditioned on vocals — this blurs the binary generation/separation distinction. The lack of precise scope bounding weakens the paper's defense against novelty challenges.
**Required action:** Scope the novelty precisely: "To our knowledge, the first model trained on waveform-level joint source distributions that can perform unconditional multi-source generation and source separation from a single network without architectural conditioning."

## Actionable Suggestions
### Suggestion 1: Revise novelty claims to be precisely scoped
**Target:** Page 1 - Abstract, Page 2 - Introduction "Contribution" paragraph
**Action:** Replace "first example of a single model that can handle both generation and separation tasks" with a precisely bounded statement.
**Copy-ready revision:** "Our method is, to the best of our knowledge, the first model trained on waveform-level joint source distributions that can perform unconditional multi-source generation, source imputation, and source separation from a single network without task-specific architectural conditioning."
**Expected benefit:** Defensible framing that cannot be challenged by tangentially related work.

### Suggestion 2: Add parameter disclosure and fairness discussion to separation results
**Target:** Page 8-9 - Section 5.2 and Table 3 caption
**Action:** Add a footnote to Table 3: "MSDM uses 405M parameters; Demucs uses 40M." Add a paragraph in Section 5.2 discussing parameter-normalized efficiency.
**Copy-ready revision paragraph:** "We note that MSDM (405M parameters) has an order of magnitude more capacity than Demucs (40M). Despite this, MSDM Dirac achieves only a modest overall improvement (+0.37 dB All) while underperforming Demucs on Drums. When controlling for parameter count, deterministic regressors remain substantially more parameter-efficient for the separation task. The weakly-supervised ISDM Dirac variant, despite achieving the highest scores (17.27 dB), requires four independent 405M models (1.62B total parameters)."
**Expected benefit:** Transparent comparison enables readers to make informed judgments about the method's practical utility.

### Suggestion 3: Move MUSDB results to main text and revise generality claims
**Target:** Page 9 - Conclusion; Page 20 - Appendix E
**Action:** Move Table 6 (or a summarized version) into the main experimental section. Add a paragraph discussing the domain gap and its implications.
**Copy-ready revision paragraph:** "When evaluated on the real-recording MUSDB18-HQ dataset (Table X), MSDM trained on MUSDB achieves 4.24 dB All SI-SDRI, substantially below Demucs v2 (12.55 dB). Direct transfer from Slakh2100 yields negative SI-SDRI (-0.88 dB), indicating poor cross-domain generalization. These results suggest that while MSDM's joint-distribution approach is promising, its separation quality heavily depends on large-scale training data and does not yet generalize well to real recordings with diverse instrumentation and production characteristics."
**Expected benefit:** Transparently communicates the method's actual capabilities and avoids overclaiming.

### Suggestion 4: Add multi-seed variance and significance tests
**Target:** Tables 1, 2, 3
**Action:** Run all experiments with at least 3 random seeds and report mean ± std. Add a footnote explaining the seed range and a brief significance statement (e.g., "All improvements over baselines are significant at p < 0.05 under a paired Wilcoxon test unless otherwise noted").
**Expected benefit:** Enables readers to assess the reliability of reported improvements.

### Suggestion 5: Expand Limitations section
**Target:** Page 9 - Section 6.1
**Action:** Add three bullet points covering: (a) inference speed (4.6s for 12s audio), (b) limited instrument classes (4 stems only), (c) synthetic-to-real domain gap demonstrated by MUSDB results.
**Copy-ready revision:** "A practical limitation is inference speed: MSDM requires 4.6 seconds to process 12 seconds of audio, precluding real-time or interactive use. The model currently handles only four instrument classes (Bass, Drums, Guitar, Piano) with a 12-second context window. Finally, as shown in Appendix E, model quality degrades substantially when applied to real recordings, suggesting significant domain mismatch between the synthetic Slakh2100 and real music."
**Expected benefit:** Provides a balanced assessment of the method's capabilities.

### Suggestion 6: Analyze Dirac posterior approximation error
**Target:** Appendix A (after Eq. 18)
**Action:** Add a paragraph analyzing when the Monte Carlo approximation (replacing integral over y(t) with y(0)) is valid and when it may introduce bias.
**Copy-ready revision:** "The approximation in Eq. (18) replaces the integral over y(t) with a point estimate at y(0), the mean of p(y(t)|y(0)) whose variance is Nσ²(t)I. This substitution is most accurate at low noise levels (small σ(t)). At high noise levels, the Dirac constraint enforced by Eq. (18) may deviate from the true posterior. The correction steps in Algorithm 1 (lines 15-18) partially compensate by re-sampling the noisy sources before scoring, but a systematic analysis of this approximation error is left for future work."
**Expected benefit:** Acknowledges the method's limitations and guides users on when to expect degradation.

### Suggestion 7: Restructure Related Work by comparison axes
**Target:** Page 3-4 - Section 2
**Action:** Reorganize Section 2 around three axes: (1) what distribution is modeled (p(y), p(x1,...,xN), or p_n(x_n)), (2) conditioning type (unconditional vs text/melody-conditioned), (3) representation domain (waveform vs latent vs spectrogram).
**Expected benefit:** Makes the paper's positioning much clearer and the novelty claim more apparent.

## Storyline Options + Writing Outlines
### Abstract Outline (complete)

**S1 (Problem + Domain):** "Generative music models and source separation have traditionally been addressed by separate model families — generative models learn mixture distributions but cannot isolate sources, while separation models recover sources from mixtures but cannot generate new coherent compositions."

**S2 (Gap):** "This separation of tasks limits the development of flexible music AI systems that can both compose and decompose musical audio."

**S3 (Proposed Solution):** "We propose Multi-Source Diffusion Models (MSDM), which learn the joint probability distribution of multiple instrument sources sharing a musical context, enabling a single model to perform unconditional mixture generation, source imputation (generating specific stems conditioned on others), and source separation."

**S4 (Key Method):** "Our approach uses denoising score matching on the joint source space and introduces a novel Dirac delta-based posterior score for the separation task that sharpens conditioning on the observed mixture."

**S5 (Key Result + Bounded Claim):** "On the Slakh2100 benchmark, MSDM achieves separation results competitive with strong deterministic baselines when accounting for model capacity, while uniquely offering generative capabilities. On the real-recording MUSDB18-HQ dataset, performance degrades substantially, highlighting the need for larger and more diverse training data."

### Introduction Outline (complete)

**P1 — Big Picture (Generative AI + Audio):** 
*Role:* Establish the broad domain and trending importance of generative models in audio.
*Key claim:* Audio is a rich domain for generative modeling, with the unique property that audio samples are sums of sources.
*Transition:* Point out that musical sources share strong contextual dependencies (bass follows drum rhythm, harmonizes with guitar).

**P2 — Formal Problem Setup:**
*Role:* Define notation and the mathematical relationship between joint distribution and mixture distribution.
*Key claim:* p(x1,...,xN) implies p(y) but the converse is an inverse problem. The joint does not factorize.
*Transition:* This joint structure mirrors human musical ability.

**P3 — Human Ability Analogy + Gap:**
*Role:* Motivate why joint modeling is desirable by analogy to human composition/decomposition ability.
*Key claim:* A composition-assisting model should both generate mixtures and separate them.
*Transition:* "To our knowledge, no prior model achieves both tasks from a single network."

**P4 — Literature Gap Analysis:**
*Role:* Explain why existing approaches fail at the unified objective.
*Key claim:* Generation models learn p(y) and cannot separate. Separation models learn p(x|y) or p_n(x_n) and cannot generate mixtures unconditionally.
*Transition:* This binary landscape motivates a third path.

**P5 — Contribution Summary:**
*Role:* Explicitly list three contributions with concrete scope.
*Key claim:* (i) MSDM learns joint source distribution via score matching, enabling generation + separation. (ii) Source imputation as a new capability. (iii) Dirac posterior score for separation.
*Key qualifier needed:* Scope these precisely: "to our knowledge, the first waveform-level model trained on joint source distributions..."

### Alternative Storyline Options

**Option A (Current — Problem/Gap/Solution):** Works well but P3 (human analogy) is somewhat weak — the argument that composers need both synthesis and analysis is plausible but not empirically validated. Strengthen by citing music information retrieval studies showing that composition tools require both generation and editing capabilities.

**Option B (Practical Application First):** Open with a concrete music production scenario: "A music producer has recorded a drum track and wants to generate a bass line that complements it, then adjust the guitar part without re-recording." This immediately hooks the reader and clarifies what problem the method solves. Then move to formal definition.

**Option C (Mathematical Elegance Angle):** Open with the joint distribution factorization insight: "The key observation is that musical sources are not independent — and this non-factorization is not a bug but a feature to be exploited." Then show how learning p(x1,...,xN) simultaneously solves three tasks. This appeals to mathematically inclined readers.

**Recommended Option:** Option B (Practical First) would work best for an ICLR audience. It immediately clarifies why the unified model matters and makes the contribution tangible before the mathematical details.

## Priority Revision Plan
### P0 — Must Fix (Publication-Critical)

| Priority | Item | Effort | Impact | Key Action |
|----------|------|--------|--------|------------|
| P0.1 | Scope novelty claims precisely | Low | High | Replace "first model" with bounded claim throughout abstract/intro/conclusion |
| P0.2 | Disclose parameter asymmetry in separation comparison | Low | High | Add parameter counts to Table 3 caption and discuss in Section 5.2 |
| P0.3 | Move MUSDB results to main text and soften generality claims | Medium | High | Add Table 6 to main experiments; revise abstract/conclusion generality framing |
| P0.4 | Expand Limitations section with inference speed, 4-stem scope, domain gap | Low | High | Revise Section 6.1 per Suggestion 5 |
| P0.5 | Add statistical reporting (variance, seeds) to Tables 1-3 | Medium | High | Run 3 seeds, report mean±std, add significance statements |

### P1 — Important Quality Improvement

| Priority | Item | Effort | Impact |
|----------|------|--------|--------|
| P1.1 | Analyze Dirac posterior approximation error in Appendix A | Medium | Medium |
| P1.2 | Restructure Related Work around comparison axes (p(y) vs p(x1,...,xN) vs p_n(x_n)) | Medium | Medium |
| P1.3 | Add subjective coherence significance test (paired Wilcoxon) | Low | Medium |
| P1.4 | Report real-time factor explicitly (4.6s/12s → RTF ≈ 0.38) in main text | Low | Medium |

### P2 — Nice-to-Have Enhancements

| Priority | Item | Effort | Impact |
|----------|------|--------|--------|
| P2.1 | Add analysis of partial generation quality vs noise level | Medium | Low-Medium |
| P2.2 | Compare MSDM with a same-architecture mixture model on MUSDB (ablation) | High | Medium |
| P2.3 | Add a user study for the composition tool claim | High | Low-Medium |

### Expected Impact After P0 Fixes
If all P0 items are addressed, the paper's credibility improves substantially: (1) the novelty claim becomes defensible and precisely scoped, (2) the comparison with Demucs becomes transparent and fair, (3) the MUSDB limitation is honestly communicated, (4) the limitations section covers practical constraints, and (5) statistical reliability becomes assessable. The paper would then present a solid, well-scoped contribution rather than an overclaimed one.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|--------------|-----------------|-------------------|
| E1 | Total generation quality (MSDM vs Mixture Model) | Slakh2100, subjective (32 subjects) + FAD | Quality (1-10), Coherence (1-10), FAD | MSDM: 6.55 FAD, 6.51 Quality, 6.35 Coherence | C1 (joint dist. enables generation) | No significance test; coherence gap (0.68) not analyzed |
| E2 | Partial generation (source imputation) | Slakh2100, subjective (21 subjects) + sub-FAD | Quality (1-10), Density (1-10), sub-FAD | sub-FAD ranges 0.11-4.90 across source combos | C2 (source imputation capability) | No baseline; no analysis of which source combinations work best |
| E3 | Source separation (MSDM/ISDM vs Demucs) | Slakh2100 test set, 4s chunks, 2s overlap | SI-SDRI (dB) | MSDM Dirac corr: 16.48 All; ISDM Dirac corr: 17.27 All | C3 (Dirac posterior improves separation) | 10x parameter gap vs Demucs; no variance reported |
| E4 | Hyperparameter search (Schurn, γ) | Slakh2100 subset (100 chunks) | SI-SDRI (dB) | Best: Schurn=20-40 for Dirac; γ=0.75σ(t)-σ(t) for Gaussian | C3 (stochasticity helps) | Limited to 100 chunks; results may not generalize |
| E5 | Data efficiency / MUSDB transfer | MUSDB18-HQ test set | SI-SDRI (dB) | Direct transfer: -0.88 dB; Finetuned: 4.25 dB; Trained: 4.24 dB | Data scaling claim | Results buried in appendix; ~3x worse than Demucs |
| E6 | Inference time comparison | RTX A6000 | Time (s) | MSDM: 4.6s/12s; ISDM: 18.4s/12s; Demucs: 0.11s/12s | Computational efficiency | Not discussed in main text |

### Research-Theme Gap Diagnosis

**Gap 1 — Causal mechanism of joint-distribution advantage:** The paper claims that modeling p(x1,...,xN) is superior to modeling p(y) or independent p_n(x_n) because it preserves inter-source dependencies. However, no experiment directly tests this claim: there is no ablation comparing MSDM vs an identical architecture trained on p(y) (which exists as the "Mixture Model" for generation but is not evaluated for separation), nor a comparison against independent source models with matched capacity. **Missing evidence:** A controlled experiment where MSDM and an independent-source model (with same architecture and total capacity) are compared on both generation coherence and separation accuracy.

**Gap 2 — When does the Dirac approximation hurt?** The Dirac posterior replaces an integral with a point estimate. No experiment analyzes how separation quality varies as a function of noise level, which would reveal when the approximation is valid. **Missing evidence:** A diagnostic experiment comparing Dirac vs Gaussian posterior scores at each noise discretization step.

**Gap 3 — Partial generation quality factors:** The sub-FAD scores vary dramatically across source combinations (0.11 for Guitar alone vs 4.90 for BDG trio), but no analysis explains why. **Missing evidence:** An analysis correlating partial generation quality with acoustic properties of the fixed sources.

### Proposed Research Experiments

**P0 Experiment — Multi-seed variance reporting**
- **Target Claim:** C1, C3 (reported numeric results are reliable)
- **Hypothesis:** Reported improvements are stable across training seeds
- **Minimal Design:** Run MSDM Dirac and MSDM Gaussian training 3 times with different random seeds; evaluate on Slakh2100 test set
- **Controls:** Same architecture, optimizer, data split
- **Metrics:** SI-SDRI mean±std for each instrument; Cohen's d vs Demucs
- **Success Criterion:** Standard deviation < 5% of the mean for all instruments
- **Cost:** ~3x training budget (but can use existing checkpoints if seeds were saved)
- **Expected Gain:** Enables statistical claims; critical for evaluating contribution (iii)

**P1 Experiment — Controlled ablation: MSDM vs independent models with matched total capacity**
- **Target Claim:** C1 (joint distribution modeling is beneficial for both tasks)
- **Hypothesis:** MSDM's joint modeling improves generation coherence and/or separation accuracy over independent models with the same total parameter budget
- **Minimal Design:** Train 4 independent source models with 101.25M parameters each (matching MSDM's 405M total). Compare: (a) generation coherence via subjective test, (b) separation accuracy via SI-SDRI using Gaussian posterior (oracle), (c) cross-source consistency metrics
- **Controls:** Same architecture, training schedule, inference steps
- **Metrics:** FAD, SI-SDRI, cross-source correlation
- **Success Criterion:** MSDM significantly outperforms independent ensemble on coherence while maintaining comparable or better separation
- **Cost:** High (4x training runs) but high-impact
- **Expected Gain:** Directly validates the core conceptual contribution

**P2 Experiment — Dirac vs Gaussian comparison as function of noise level**
- **Target Claim:** C3 (Dirac posterior improves separation)
- **Hypothesis:** Dirac approximation benefits are largest at low noise and diminish at high noise levels
- **Minimal Design:** During the reverse sampling process, record intermediate separation quality (SI-SDRI on partially denoised signals) at each timestep for both Dirac and Gaussian posteriors
- **Controls:** Same initial noise, same schedule
- **Metrics:** SI-SDRI(t) as function of timestep t
- **Success Criterion:** Clear visualization of where Dirac diverges from Gaussian
- **Cost:** Low (post-hoc analysis of existing sampler)
- **Expected Gain:** Reveals when/why the Dirac approximation works; strengthens contribution (iii)

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Rationale:** The paper has a strong conceptual contribution — modeling the joint distribution of musical sources to unify generation and separation — which is technically sound and well-executed on the Slakh2100 benchmark. The Dirac posterior is a theoretically motivated contribution with demonstrated empirical benefits. However, the score is constrained by: (1) imprecise novelty claims that would benefit from external literature verification (deferred in this run), (2) the MUSDB18-HQ results showing a 3x gap vs Demucs on real recordings, which significantly tempers the claimed generality, (3) the 10x parameter asymmetry in the main comparison being insufficiently disclosed, and (4) missing statistical reporting that prevents assessment of result reliability. These issues are substantive but fixable with the revisions recommended above.

**Scoring dimensions:**
- Research value / contribution: 7/10 (joint-distribution modeling is a genuine conceptual advance)
- Novelty strength: 6/10 (the Dirac likelihood is incremental; the unified framework is novel)
- Methodological soundness: 7/10 (mathematically rigorous, well-reasoned)
- Experimental validity: 5/10 (unfair comparison, missing variance, MUSDB results hidden)
- Reproducibility: 6/10 (algorithm specified, but training details insufficient; inference setup clear)
- Presentation: 6/10 (good figures, but overclaimed narrative and list-style related work)

**Post-Revision Target: [7.5, 8.0] / 10**

If the authors address the P0 items (scope novelty claims, disclose parameter asymmetry, move MUSDB results to main text, expand limitations, add statistical reporting), the paper would present a well-scoped, transparent contribution. The conceptual novelty of joint-distribution modeling would stand on its own without overclaiming, and the honest discussion of limitations would increase credibility. At that point, the paper would be a solid acceptance recommendation.