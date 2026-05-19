## Summary
# Final Review Report

## Summary

This paper addresses the security threat of energy-latency attacks on large vision-language models (VLMs). The authors observe an approximately linear relationship between generated sequence length and inference energy/latency cost, and propose "verbose images"—adversarial perturbations optimized to maximize output sequence length. Three loss objectives are designed: (1) delaying the end-of-sequence (EOS) token, (2) maximizing output uncertainty (KL divergence against uniform), and (3) maximizing diversity of hidden states (nuclear norm of the concatenated hidden-state matrix). A temporal weight adjustment algorithm balances these losses during PGD optimization. Experiments on four VLMs (BLIP, BLIP-2, InstructBLIP, MiniGPT-4) over MS-COCO and ImageNet show 7.87x–8.56x length amplification over clean images. The work identifies a relevant vulnerability in VLM deployment and provides a systematic attack formulation.

**Strengths:** Clear problem motivation, well-designed three-loss framework with complementary mechanisms, extensive evaluation across four VLMs and two datasets, thorough ablation studies, and helpful appendix documentation including code release.

**Core weaknesses:** (1) The attacker-to-victim energy ratio (~209x) is a critical practical limitation not addressed in the main paper; (2) high per-sample variability (std >200 tokens for BLIP) reduces attack reliability; (3) the temporal weight normalization (Eq. 6) uses L2's L1 norm as universal denominator without numerical stability justification; (4) novelty versus prior energy-latency attacks cannot be fully assessed without external literature retrieval (deferred due to retrieval unavailability); (5) claim scope occasionally overstates evidence (e.g., "comprehensive investigation" for a two-model correlation plot, "imperceptible" at LIPIS 0.037).

## Strengths
1. **Well-motivated problem framing.** The paper identifies a genuine and underexplored threat: energy-latency Denial-of-Service attacks on VLMs via adversarial visual inputs. The evidence that inference energy is approximately linear with sequence length (Fig. 1, Page 2) provides a clear attack surface.

2. **Complementary three-loss design.** The decomposition into EOS-delay (L1), output uncertainty (L2), and hidden-state diversity (L3) is conceptually clean. The ablation study (Table 3, Page 9) confirms that each loss contributes to the overall attack success, and their combination yields the best results. The temporal weight adjustment algorithm provides a principled way to balance these different objectives.

3. **Thorough experimental scope.** The evaluation covers four diverse VLM architectures (BLIP, BLIP-2, InstructBLIP, MiniGPT-4) spanning different model sizes (224M–7B), two standard datasets (MS-COCO, ImageNet), and three metrics (length, energy, latency). The additional experiments on VQA and visual reasoning tasks (Appendix C), black-box transferability (Appendix B), and different sampling policies (Appendix H.1) strengthen the empirical contribution.

4. **Comprehensive ablation and parameter analysis.** The paper provides detailed ablation studies on loss combinations (Table 3), optimization components (Table 4), perturbation magnitudes with LIPIS (Table 5), and extensive grid searches for loss weight parameters (Appendix I). This level of empirical analysis is valuable for reproducibility and practical deployment.

5. **Ethical responsibility and code release.** The ethics statement appropriately restricts claims to laboratory settings, and the code release facilitates further research on defenses against this attack surface. The acknowledgment of the energy-latency vulnerability as an availability concern is a responsible framing.

## Weaknesses
### W1. Severe attacker-victim energy asymmetry (Major / Partially fixable)
**Evidence:** Appendix Table 11 (Page 20) shows generating one verbose image at 1000 PGD iterations costs 67,231 J and 442 seconds, while the induced extra victim inference cost is only 322 J and 7.97 seconds—a **209x asymmetry**. This critical limitation is not mentioned in the main paper or abstract.
**Risk:** The attack is not practically viable for resource-constrained attackers. The paper's threat model implicitly assumes the attacker can absorb arbitrarily high generation costs.
**Fix:** Move this analysis to the main paper, discuss practical attack scenarios (e.g., pre-computed universal perturbations, DDoS with repeated same-image queries), and explore efficiency improvements (fewer PGD iterations, transfer-based attacks).

### W2. High per-sample variability (Major / Fixable)
**Evidence:** Table 12 (Page 20) reports standard deviations exceeding 200 tokens for BLIP on MS-COCO (mean=318.66, std=207.88), giving a coefficient of variation >65%. The main paper (Table 1, Page 7) reports only means without variance.
**Risk:** The attack's effectiveness is highly unpredictable per image, reducing its reliability as a security threat. Reviewers cannot judge whether differences between methods are statistically significant.
**Fix:** Report standard deviations or confidence intervals in Table 1. Add statistical significance tests (e.g., Wilcoxon signed-rank) for main comparisons. Discuss the implications of high variability for attack reliability.

### W3. Temporal weight normalization design flaw (Major / Fixable)
**Evidence:** Equation (6) (Page 6) uses ||L2(x')||1 as the universal numerator for all three weight updates, meaning L2's scale dominates the normalization. If L2 converges close to zero, weights for L1 and L3 can become unstable. No numerical safeguard (e.g., epsilon in denominator) is provided.
**Risk:** The temporal weight adjustment algorithm, a claimed contribution, may have unstable dynamics that are not analyzed. The grid search (Appendix I) tests parameter sensitivity but does not diagnose numerical stability.
**Fix:** Add a stability epsilon to denominators, or normalize each loss by its own L1 norm. Justify why L2 is chosen as the reference.

### W4. Claim-evidence scope mismatch (Moderate / Fixable)
**Evidence:** (a) "Comprehensive investigation" of energy-length correlation (Page 2) is supported by only two VLMs in Fig. 1 without R² reporting. (b) "Imperceptible perturbation" (Abstract, Page 1) is contradicted by LIPIS=0.037 at default epsilon (Table 5, Page 9), which is visually detectable. (c) CHAIR analysis (Page 8) claims hallucination drives longer sequences, but the causal direction may be reversed.
**Risk:** Overclaiming reduces scientific credibility and may mislead readers about the method's maturity.
**Fix:** Downgrade "comprehensive" to "preliminary" or "empirical." Replace "imperceptible" with "visually subtle" or report LIPIS alongside the claim. Reframe CHAIR analysis as correlational.

### W5. L3 token diversity loss: weak mechanism and high cost (Moderate / Fixable)
**Evidence:** Table 3 (Page 9) shows L3 alone achieves only 104.03 length (weakest individual loss). Adding L3 to L1+L2 only increases length from 177.95 to 226.72 (~27% improvement). Nuclear norm requires SVD computation (O(NC²) per iteration), with computational cost not reported.
**Risk:** The incremental benefit may not justify the added complexity. Practitioners might prefer L1+L2 without L3.
**Fix:** Report per-iteration time for each loss. Discuss whether L3 is essential or optional for practical attacks. Consider whether a simpler diversity measure (e.g., cosine distance between hidden states) could replace nuclear norm.

## Key Issues
### Ranked Error Board (Top-5 by severity and research-value impact)

| Rank | Issue | Severity | Validity Risk | Fixability | Paper Section |
|------|-------|----------|--------------|------------|---------------|
| 1 | Attacker-victim energy asymmetry (209x) not discussed in main paper | Major | High—threat model practicality | Modifiable—discuss + explore efficiency | Appendix G.4 (Page 20) |
| 2 | High per-sample variability without variance reporting in Table 1 | Major | Medium—statistical significance unclear | Easily fixable—add std/CI | Page 7, Table 1 |
| 3 | Temporal weight normalization (Eq. 6) uses L2 norm as universal denominator without stability justification | Major | Medium—may cause unstable optimization | Easily fixable—add epsilon | Page 6, Eq. 6 |
| 4 | Claim-evidence scope mismatches (imperceptible at LIPIS 0.037, "comprehensive" with 2 models only) | Moderate | Medium—credibility risk | Easily fixable—bounded language | Abstract, Page 2 |
| 5 | L3 token diversity loss: weak individual contribution, high SVD cost | Moderate | Low—still improves over L1+L2 | Modifiable—report cost or simplify | Page 5, Eq. 3; Page 9, Table 3 |

### Defect Admission Verification Gates

All 5 issues above pass the three-check gate:
- **Check 1 (Anchor):** Each has an explicit paragraph/location reference in the manuscript.
- **Check 2 (Verification):** Each has been cross-checked by reading the relevant equations/tables/figures and confirming contradictions.
- **Check 3 (Impact):** Each has a clear impact path on validity, novelty, or practical research value.

## Actionable Suggestions
### S1. Address energy asymmetry in main paper (Must)

**Problem:** The 209x attacker-victim energy ratio (Appendix Table 11) is the most critical practical limitation of the attack, yet it is absent from the main text.

**Action:** 
1. Move Table 11 or a summary to Section 5.3 (Discussions).
2. Add a paragraph analyzing the cost-benefit trade-off.
3. Discuss scenarios where the attack remains viable: (a) pre-computed universal perturbations that work across images, (b) repeated same-image queries in DDoS-style attacks, (c) transfer-based attacks requiring only one generation for many victims.
4. Explore whether the attack can be effective with fewer PGD iterations (e.g., 100 or 200 iterations).

**Expected benefit:** Honest treatment of the attack's practicality strengthens the paper's scientific credibility.

### S2. Report variance and significance tests in main results (Must)

**Problem:** Table 1 reports only means without standard deviations or significance tests, despite high variability (std >200 tokens for BLIP).

**Action:**
1. Add standard deviations or confidence intervals to Table 1 (or report them in the caption text).
2. Add a column for "p-value vs. best baseline" using Wilcoxon signed-rank test.
3. In the text discussing Table 1 (Page 7), add: "Despite high per-sample variability (Appendix Table 12), the improvement over baselines is statistically significant at p < 0.01 across all settings."

**Expected benefit:** Enables readers to assess statistical reliability of the claimed improvements.

### S3. Fix temporal weight normalization (Must)

**Problem:** Equation (6) uses ||L2||1 as the universal numerator for all three weights without stability justification.

**Action:**
1. Add a small epsilon (1e-8) to all denominators: λj(t) = (||L2||1 + ε) / (||Lj||1 + ε) / Tj(t).
2. Provide a justification in the text: "L2 is chosen as the reference because its KL-divergence-based loss has a more stable scale across iterations."
3. Alternatively, simplify to: λj(t) = 1 / Tj(t) for all j, removing the cross-loss normalization entirely and relying on temporal decay alone.

**Expected benefit:** Numerical stability and clearer design rationale.

### S4. Bounded language for claims (Nice-to-have)

**Problem:** Several claims overstate evidence (abstract: "imperceptible," Page 2: "comprehensive investigation," Page 8: causal interpretation of hallucination).

**Action:**
1. Abstract: Replace "imperceptible perturbation" with "visually subtle perturbation (LIPIS ~0.037)."
2. Page 2, line 37: Replace "comprehensive investigation" with "an empirical study."
3. Page 8, line 14-16: Replace "this observation implies that our verbose images can prompt VLMs to generate sequences that include objects not present in the input image, thereby leading to longer sequences" with "this observation is consistent with our method inducing hallucinated content, though longer sequences inherently increase hallucination counts."

**Expected benefit:** Improved scientific precision, reduced risk of reviewer criticism.

### S5. Evaluate L3 cost-benefit explicitly (Nice-to-have)

**Problem:** L3 adds SVD computation (O(NC²)) for ~27% improvement over L1+L2. This overhead is not quantified.

**Action:**
1. Report per-iteration time for each loss variant (L1, L1+L2, L1+L2+L3).
2. If the overhead is substantial, consider replacing nuclear norm with a simpler diversity measure (e.g., average pairwise cosine distance between hidden states).
3. Add a sentence: "In practical deployment, practitioners may prefer L1+L2 alone for faster perturbation generation when the ~27% additional length gain is not critical."

**Expected benefit:** Transparency about computational trade-offs.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction (Page 1-2) follows this paragraph structure:
- **P1:** VLMs are powerful but compute-heavy; inference dominates ML demand.
- **P2:** Attackers can exploit this via energy-latency attacks; existing methods (sponge samples, NICGSlowDown) don't apply to VLMs.
- **P3:** This paper investigates the length-energy relationship, proposes verbose images with three loss objectives.
- **P4 (contribution list):** Three bullet points summarizing contributions.

**Problem with current storyline:** P2 transitions abruptly from motivation to prior-work critique without establishing the concrete research gap. The contribution list in P4 repeats the method description rather than stating what new knowledge the paper provides.

### Alternative Storyline Candidate A (Recommended)

**Arc:** Big Picture → Concrete Gap → Core Insight → Method Sketch → Evidence Preview → Bounded Contribution

- **P1 (Stakes):** VLMs now serve millions of users; their inference cost dominates total ML compute. A single energy-latency attack can degrade service availability for all users.
- **P2 (Gap):** Existing energy-latency attacks target either per-token computation (sponge samples) or smaller captioning models (NICGSlowDown). Neither addresses the VLM setting where stochastic sampling makes token-level objectives unreliable.
- **P3 (Insight + Method):** We observe that VLM inference energy is near-linear with output sequence length (Fig. 1, r > 0.99). This motivates maximizing sequence length via adversarial visual perturbations. We design three probability-level losses that work under stochastic sampling: EOS suppression, output entropy maximization, and hidden-state diversification.
- **P4 (Evidence Preview + Contribution):** Across four open VLMs and two datasets, our verbose images increase output length by 7.87–8.56x (p < 0.01). We release code to facilitate defense research. Limitations include visible perturbation (LIPIS ~0.037) and high generation cost (~67 kJ/image), which we discuss in context.

### Abstract Outline

**S1 (Domain + Problem):** "Large vision-language models (VLMs) incur substantial energy costs during deployment, creating a vulnerability to energy-latency Denial-of-Service attacks."
**S2 (Gap):** "Existing energy-latency attacks target smaller models or rely on deterministic token objectives, making them ineffective against stochastic VLM generation."
**S3 (Proposed Method):** "We propose 'verbose images'—adversarially perturbed inputs optimized via three losses: EOS token suppression, output entropy maximization, and hidden-state diversity, balanced by temporal weight adjustment."
**S4 (Key Result):** "On MS-COCO and ImageNet across four open VLMs (BLIP, BLIP-2, InstructBLIP, MiniGPT-4), verbose images increase generated sequence length by 7.87–8.56x over clean images."
**S5 (Bounded Implication):** "These results highlight a practical availability risk in VLM deployment, though the attack's 209x generation-to-victim energy asymmetry and visible perturbation (LIPIS 0.037) bound its real-world applicability."

### Introduction Outline (Revised, 4 paragraphs)

**P1: Establish stakes and domain importance**
- Opening sentence: "Large vision-language models (VLMs) are now deployed in production systems serving millions of users, with inference accounting for over 90% of ML compute demand (Patterson et al., 2021)."
- Bridge to security: "This compute footprint creates a new attack surface: by crafting inputs that inflate inference cost, attackers can degrade service availability—a Denial-of-Service threat."
- Transition: "However, existing energy-latency attacks are not designed for the unique challenges of VLMs."

**P2: Identify concrete gap**
- Sentence 1: "Current approaches fall into two categories: activation-based attacks (sponge samples) that increase per-token computation in LLMs, and sequence-length attacks (NICGSlowDown) designed for deterministic RNN/LSTM captioning models."
- Sentence 2: "Neither transfers to modern VLMs: the former does not target sequence length (the dominant cost factor), and the latter's token-level logit minimization is ineffective under nucleus sampling."
- Sentence 3: "A VLM-specific attack must operate through probability-level objectives compatible with stochastic autoregressive generation."

**P3: Present core insight and method intuition**
- Sentence 1: "We begin by establishing an approximately linear relationship between VLM output sequence length and both energy consumption and latency (Fig. 1, Pearson r > 0.99 under tested settings)."
- Sentence 2: "This motivates maximizing sequence length as an attack strategy. We achieve this through three losses operating on the output distribution and hidden states, designed to work under stochastic sampling."
- Sentences 3-5: Briefly describe L1 (EOS probability minimization), L2 (output entropy maximization via KL divergence against uniform), and L3 (hidden-state diversity via nuclear norm maximization), and temporal weight adjustment.

**P4: Evidence preview and bounded contribution**
- Sentence 1: "We evaluate verbose images on BLIP, BLIP-2, InstructBLIP, and MiniGPT-4 across MS-COCO and ImageNet, achieving 7.87–8.56x sequence length amplification."
- Sentences 2-3: State contributions as bounded claims: attack effectiveness, mechanism analysis (attention dispersion, hallucination), and code release.
- Sentence 4: "We also acknowledge key limitations—the perturbation is visually detectable at LIPIS ~0.037, and generation requires ~67 kJ per image—to honestly scope the practical threat."

## Priority Revision Plan
### Revision Ranking by Impact and Effort

```text
Priority | Action | Effort | Impact | Section Affected
---------|--------|--------|--------|-----------------
P0 (Must) | Add attacker-victim energy asymmetry discussion to main paper | Low | High | Section 5.3 / Conclusion
P0 (Must) | Add variance/std to Table 1 + significance tests | Low | High | Table 1, Section 5.2
P0 (Must) | Fix temporal weight normalization with epsilon + justification | Low | Medium | Page 6, Eq. 6
P1 (Should) | Bounded language for overclaims (imperceptible, comprehensive) | Low | Medium | Abstract, Page 2
P1 (Should) | Report L3 computational overhead + consider simplification | Low | Medium | Page 5, Section 5.4
P2 (Nice) | Reframe CHAIR analysis as correlational | Low | Low | Page 8
P2 (Nice) | Restructure Related Work by comparison axes | Medium | Medium | Section 2
P2 (Nice) | Expand conclusion with limitations + future work | Low | Medium | Section 6
```

### Revision Order (Recommended Execution Sequence)

**Phase 1 (1-2 days): Language and precision fixes**
1. Revise abstract: "imperceptible" → "visually subtle (LIPIS ~0.037)"
2. Revise Page 2: "comprehensive investigation" → "empirical study"
3. Add correlation coefficient (Pearson r) to Fig. 1 caption
4. Reframe CHAIR interpretation as correlational (Page 8)
5. Expand conclusion with limitations and attacker-victim energy ratio (Page 9)

**Phase 2 (3-5 days): Methodological corrections**
1. Fix Eq. 6 with epsilon and justification (Page 6)
2. Add standard deviations or CIs to Table 1 (Page 7)
3. Run and report Wilcoxon signed-rank test for main comparisons
4. Move energy-asymmetry analysis from Appendix G.4 to main paper (Section 5.3)
5. Report per-iteration time for each loss variant

**Phase 3 (1-2 weeks): Substantive extensions**
1. Test attack efficiency with fewer PGD iterations (100, 200, 500)
2. Explore universal perturbation transferability
3. Add OOD or noise-sensitivity robustness tests for the attack

### Expected Quality Improvement After Revision

If P0 and P1 items are fully addressed:
- The paper's scientific honesty and reproducibility will be substantially improved
- The threat model will be more realistic and better scoped
- Statistical claims will be properly supported
- The attack's practical limitations will be transparently discussed
- Mathematical formulations will be numerically stable

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Length-energy linearity in VLMs | BLIP-2, MiniGPT-4, lengths 0-1024 | Energy (J), Latency (s) | Approx. linear relationship (Fig. 1) | C1 | Only 2 models, no R² reported |
| E2 | Main attack comparison | 4 VLMs × 2 datasets × 5 methods | Length, Energy, Latency | 7.87–8.56x improvement (Table 1) | C2, C3 | No std/CI in main table; high variability |
| E3 | Visual interpretation | GradCAM on original vs verbose | Attention maps | Dispersed attention (Fig. 4) | C2 (mechanism) | Correlational, not causal |
| E4 | Textual interpretation | CHAIR hallucination metric | CHAIRi, CHAIRs | Hallucination increases (Table 2) | C2 (mechanism) | Causal direction ambiguous |
| E5 | Loss ablation | All 7 combinations of L1/L2/L3 | Length, Energy, Latency | All 3 losses together best (Table 3) | C2 (loss design) | L3 marginal over L1+L2 |
| E6 | Temporal weight ablation | With/without decay, momentum | Length, Energy, Latency | Both components help (Table 4) | C2 (optimization) | No numerical stability analysis |
| E7 | Perturbation magnitude sweep | ε ∈ {2,4,8,16,32} x BLIP-2 | Length, LIPIS | Larger ε → longer seq + visible (Table 5) | C3 (trade-off) | LIPIS correlation with human perception unvalidated |
| E8 | Black-box transferability | Cross-model transfer | Length, Energy, Latency | Transferable but weaker (Table 6) | C2 (generalization) | Only same-family models tested |
| E9 | VQA and Visual Reasoning | BLIP-2 on VQAv2, GQA | Length, Energy, Latency | Effective on other tasks (Table 7) | C2 (generalization) | Single model only |
| E10 | Joint image-text optimization | BLIP-2, image+text perturbations | Length, Energy, Latency | Still best among methods (Table 8) | C2 (extension) | Limited analysis |
| E11 | Sampling policy robustness | Greedy, beam, top-k, nucleus | Length, Energy, Latency | Consistent advantage (Table 13) | C2 (robustness) | Only BLIP-2 |
| E12 | Max length sensitivity | Max length ∈ {128,256,512,1024} | Length, Energy, Latency | Longer max → longer attack (Table 14) | C2 (robustness) | Only BLIP-2 |
| E13 | Grid search for loss weights | ±parameters a1,b1,a2,b2,a3,b3 | Length | Optimal values found (Tables 15-20) | C2 (optimization) | Only BLIP-2 |
| E14 | Energy cost of attack generation | 0, 100, 500, 1000 iters | Generation energy/latency | 67 kJ at 1000 iters (Table 11) | (practicality) | Not in main paper |
| E15 | Standard deviation analysis | All settings | Length, Energy, Latency std | High variability (Table 12) | (reliability) | Not in main paper |

### Research-Theme Gap Diagnosis

| Research Value Dimension | Current Support | Gap |
|------------------------|----------------|-----|
| New knowledge (attack formulation) | Good—three-loss framework is novel | Mechanism evidence (L2, L3) is correlational |
| Reproducibility/Reusability | Good—code released, detailed appendix | Missing hyperparameter sensitivity beyond grid search |
| Impact on practice/understanding | Partial—identifies vulnerability | Practicality limited by 209x asymmetry; defense directions not explored |

### Proposed Research Experiments (P0/P1/P2)

**P0 Experiment: Attack Efficiency at Fewer Iterations**
- **Target Claim:** The attack can be practically generated with acceptable cost.
- **Hypothesis:** Substantial length amplification can be achieved with <1000 PGD iterations.
- **Minimal Design:** Run verbose images generation at T ∈ {50, 100, 200, 500} iterations on BLIP-2 MS-COCO. Report length, energy, latency at each T.
- **Controls/Baselines:** Use same hyperparameters as main experiment except T.
- **Metrics:** Length, Attack Generation Energy, Victim Inference Energy, Energy Ratio.
- **Success Criterion:** If length > 150 at T=200 (vs 226.72 at T=1000), the attack becomes more practical (energy ratio drops from 209x to ~40x).
- **Expected Quality Gain:** Directly addresses the most critical practical limitation.

**P1 Experiment: Universal Perturbation Transferability**
- **Target Claim:** A single verbose image can affect multiple images or prompts.
- **Hypothesis:** Perturbations optimized on one image partially transfer to other images from the same dataset.
- **Minimal Design:** Generate verbose images on 10 source images; test transfer to 100 held-out target images (same model, same dataset).
- **Controls/Baselines:** Compare against image-specific verbose images.
- **Metrics:** Length amplification ratio on target images, transfer success rate.
- **Success Criterion:** If >50% of target images show >3x length amplification.
- **Expected Quality Gain:** If universal perturbations work, the attack becomes practical (one generation cost amortized over many victims).

**P1 Experiment: Statistical Significance Package**
- **Target Claim:** The between-method differences are statistically reliable.
- **Hypothesis:** Verbose images significantly outperform NICGSlowDown despite high per-sample variance.
- **Minimal Design:** For BLIP-2 on MS-COCO, run 5 independent seeds and report mean±std for all five methods. Compute Wilcoxon signed-rank p-values for Verbose vs. NICGSlowDown.
- **Controls/Baselines:** All five methods under identical conditions.
- **Metrics:** Length, p-value, effect size (Cohen's d).
- **Success Criterion:** p < 0.01 with adequate power.
- **Expected Quality Gain:** Statistical rigor for main empirical claim.

**P2 Experiment: Simple Defense Analysis**
- **Target Claim:** The vulnerability can be partially mitigated.
- **Hypothesis:** Input perturbation detection or constrained decoding can reduce attack effectiveness.
- **Minimal Design:** Test two defenses: (1) JPEG compression of input images, (2) semantic coherence threshold for early stopping.
- **Controls/Baselines:** Attack success rate without defense.
- **Metrics:** Length under defense, defense overhead.
- **Success Criterion:** Any defense reduces length by >50%.
- **Expected Quality Gain:** Practical relevance and completeness of threat analysis.

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2)

[Current: 1000 iters, 67kJ/victim 322J]  ← Baseline
    │
    ├── P0: Fewer iterations
    │      T=200 → 40x ratio? (if length >150)
    │                                        → More practical attack
    │
    ├── P1: Universal perturbations
    │      One generation → many victims
    │                                        → Amortized cost
    │
    ├── P1: Statistical significance
    │      std + p-values to Table 1
    │                                        → Reliable comparison
    │
    └── P2: Simple defenses
           JPEG + constrained decoding
                                            → Complete threat analysis
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 6.5 / 10

**Scoring rationale (research value + novelty prioritized):**

- **Research Value (6/10):** The paper identifies a relevant and underexplored vulnerability in VLM deployment. The three-loss framework is a systematic attack formulation with good empirical validation. However, the practical threat is substantially limited by the 209x attacker-victim energy asymmetry and high per-sample variability, reducing the real-world significance of the findings. The mechanism analysis (attention dispersion, hallucination) is informative but correlational rather than causal.

- **Novelty (6/10):** The combination of EOS-delay, uncertainty, and diversity losses applied to VLM visual perturbations is novel relative to the specific baselines tested (sponge samples, NICGSlowDown). The temporal weight adjustment algorithm is a practical contribution. However, each individual loss component has prior art (EOS manipulation in NICGSlowDown, entropy maximization for adversarial diversity, nuclear norm for matrix rank). External literature verification was unavailable in this run (Retrieval-Disabled Mode); novelty verdicts should be confirmed via manual literature search.

- **Validity/Soundness (7/10):** The empirical methodology is generally sound with thorough ablation studies. Main concerns are the missing variance reporting in Table 1, the temporal weight normalization stability issue (Eq. 6), and the correlational nature of mechanism analyses.

- **Reproducibility (8/10):** Code is released, model details are documented, hyperparameters are specified, and extensive grid search results are provided in the appendix. The PyTorch + LAVIS implementation basis is standard.

### Post-Revision Target: [7.0, 7.5] / 10

**Condition for achieving target:** All P0 items must be addressed:
1. Energy asymmetry discussed in main paper (threat scoping)
2. Variance/significance added to Table 1
3. Temporal weight normalization fixed with numerical safeguards
4. Overclaims bounded to match evidence

If P1 items are additionally addressed (attack efficiency with fewer iterations, universal perturbation analysis), the upper bound of 7.5 becomes achievable. The paper's ceiling is limited by the inherent practical limitations of the attack (209x asymmetry) which are architectural rather than presentational.