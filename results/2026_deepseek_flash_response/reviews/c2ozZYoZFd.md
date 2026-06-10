## Summary

This paper presents a detailed case study re-analyzing the ICLR 2025 Oral min-p sampling paper (Nguyen et al., 2024). Across four independent lines of evidence—human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community adoption claims—the re-analysis shows that the original paper's conclusions are not supported by its own data. The paper also introduces a reusable "Best-of-N" hyperparameter equalization methodology and derives general lessons for rigorous empirical ML research.

## Strengths

- **Best-of-N hyperparameter control methodology (Section 3.1, Figures 4–5):** The paper introduces a novel, reusable procedure for fairly comparing methods with unequal hyperparameter budgets. Instead of merely noting that min-p was tuned more extensively, the authors subsample equal numbers of hyperparameters per sampler, compute maximum scores, and repeat with 150 resamples. This provides a concrete tool the community can adopt to detect cherry-picking, and it is the paper's most original technical contribution.

- **Rigorous statistical re-analysis of human evaluations (Section 2.2, Table 1):** The paper applies Bonferroni correction (showing significance drops from 5/12 to 1/12 comparisons) and, more pointedly, an Intersection-Union Test (IUT) that specifically tests whether min-p outperforms baselines *in all 12 comparisons simultaneously*—the actual claim the original paper made ("consistently scored higher across all settings"). Since the largest *p*-value among the 12 tests is 0.378, the IUT cleanly rejects min-p's superiority claim. This goes well beyond standard multiple-comparison correction.

- **Discovery of one-third omitted human evaluation data (Section 2.1):** The paper audited the original data and found that scores for a second baseline sampler (basic sampling) were excluded from the methodology, analysis, and results without justification. This omission was confirmed with the authors. Including the omitted data (subsequently added to the Camera Ready but without updating conclusions) changes the paper's findings.

- **Independent verification and documented retraction of community-adoption claims (Section 5):** The paper provides concrete counter-evidence: the combined GitHub stars of eight major LM repositories sum to 453k—less than half the claimed 1.1M stars. This led to retraction of both claims from the ICLR 2025 Camera Ready. The paper further notes that 3 of 4 ICLR 2025 reviewers cited these retracted numbers as justification for their strong endorsement, demonstrating the field-level harm of unsubstantiated claims.

## Weaknesses

### Major

- **Overclaim in the "samplers perform approximately equally" conclusion (Section 6):** The Discussion states that "samplers perform approximately equally if given equal hyperparameter tuning." This is the paper's most sweeping negative claim, but the evidence directly supporting it covers only GSM8K CoT across 9 models (up to ~9B parameters). The original paper also evaluated GPQA, which was not tested here due to compute budget. While the GSM8K sweep is extensive, claiming that *samplers generally perform equally* goes beyond what single-benchmark evidence can support. This is fixable with tighter scoping (e.g., "on GSM8K CoT under the conditions tested, samplers perform approximately equally..."), but as written, it overstates the evidential reach.

### Minor

- **Selective reporting claim in Section 4.3 rests on a Telegram link, not independently verifiable data:** The paper documents that the first author shared a Telegram link showing the higher of two win rates was reported for min-p and the lower for top-p. This is a specific, source-documented finding, but its provenance is weaker than the paper's other evidence (which is based on the authors' own re-analyses of published data). The paper presents this alongside its own analysis without clearly demarcating the different evidentiary tiers. At minimum, the authors should report whether the original authors have confirmed or contested this characterization and make the raw data from that communication available.

- **The "blueprint" (Section 6) is thinner than the title and abstract suggest:** The paper is titled "A Min-P Blueprint for More Rigorous Science," but the six lessons are a one-page list of well-established best practices (control hyperparameter tuning, correct for multiple comparisons, share data, scrutinize qualitative claims, ensure methodological clarity, watch for selective reporting). None of these are novel. The paper's real contribution is the *case study*—the concrete demonstration of how these principles were violated. This framing mismatch does not undermine the paper's value, but it sets an expectation the paper does not fully meet. Developing the lessons into an operational rubric or checklist would strengthen the paper.

### Trivial

None.

## Nice-to-Haves

- Testing GPQA with even a reduced sweep (fewer models or seeds) would substantially strengthen Section 3's conclusions.
- A sensitivity analysis for the Best-of-N hyperparameter selection (e.g., how results change when one hyperparameter value is added or removed) would address a natural concern about the method's robustness.
- Turning the six lessons into a concrete reviewer checklist or decision tree would make the blueprint more actionable and increase the paper's impact as a reference document.

## Removed Points

- *"The paper treats the four lines of evidence as more uniformly conclusive than the evidence warrants"*: Not supported by the paper—each section is self-contained, limitations are acknowledged, and the abstract states the findings with appropriate specificity.
- *Calls to test additional models or datasets beyond reasonable scope*: The sweep covering 9 models × 2 stages × 31 temperatures × 4 samplers × 3 seeds (~6000 A100-hours) is already extensive for a re-analysis paper.
- *Formatting, typos, and presentation nitpicks*: These are parser artifacts, not author errors.

## Novel Insights

The reviewer inputs do not surface any genuinely novel insight beyond the paper's own contributions. The paper itself makes an interesting methodological point worth noting: the Best-of-N analysis can be seen not only as a fairness technique but also as a diagnostic tool—if a method's advantage disappears when its hyperparameter budget is equalized, that is strong evidence that the reported advantage was an artifact of unequal tuning rather than genuine methodological superiority.

## Suggestions

1. **Scope the "samplers perform approximately equally" claim** to the evaluated conditions (GSM8K CoT, models up to ~9B) rather than asserting it as a general finding about sampling methods.
2. **Strengthen Section 4.3** by either (a) obtaining and presenting the full data from the Telegram exchange transparently, or (b) clearly demarcating this as a less-verifiable claim based on informal communication.
3. **Develop the six lessons into a more operational form**—e.g., a checklist of questions reviewers could ask about human evaluation design, a template for reporting LLM-as-a-Judge experiments, or a decision tree for when hyperparameter equalization is needed.

## Score and Decision

**Calibration:** Round 1 bracketing identified the most comparable anchors as re-analysis/critique papers: "Is Memorization Actually Necessary for Generalization?" (avg 3.75–4.40, Reject), "Reevaluating Theoretical Analysis Methods for Optimization" (avg 5.75, Reject), and "On the Disconnect Between Theory and Practice of Overparametrized Neural Networks" (avg 6.00, Reject). Round 2 narrowed to "On Evaluating the Durability of Safeguards for Open-Weight LLMs" (avg 6.50, Accept) and "Dissecting Sample Hardness" (avg 6.20, Accept), both of which are critique/evaluation-focused papers accepted at top venues. The paper under review is clearly stronger than the Memorization re-analyses (more comprehensive evidence, genuine methodological contribution) and comparable to the Safeguards evaluation paper (similar genre, similar rigor, similar contribution type).

**All anchors retrieved:**
- eRAXvtP0gA (avg 2.50, Round 1): Weak paper, not comparable.
- OXIIFZqiiN (avg 1.50, Round 1): Not comparable.
- qcyn7ESaM8 (avg 2.50, Round 1): Not comparable.
- dIaykjbiiL (avg 2.50, Round 1): Not comparable.
- GbEmJmnQCz (avg 4.40, Rounds 1&2): Memorization re-analysis—weaker evidence and less comprehensive than min-p paper.
- lf8QQ2KMgv (avg 3.75, Round 1): Memorization re-analysis variant—similar weakness.
- RW37MMrNAi (avg 5.60, Round 1): Class-wise Autoencoders—different genre (method paper).
- v675Iyu0ta (avg 5.60, Round 1): Interpretability Illusions—different genre.
- EUSkm2sVJ6 (avg 7.60, Round 1): Data Usage Inference—stronger method contribution, different genre.
- et5l9qPUhm (avg 8.00, Round 1): Strong Model Collapse—different genre (theory + experiments).
- SctfBCLmWo (avg 8.00, Round 1): Dataset Bias—different genre.
- P7KIGdgW8S (avg 8.00, Round 1): Graph Neural Networks—different genre.
- om5z1n0mXA (avg 6.00, Round 2): Graph Classification critique—similar genre, comparable quality.
- T97kxctihq (avg 5.00, Round 2): Long-term Forecasting critique—less comprehensive.
- Dtxc7mlKRg (avg 4.60, Round 2): Conformal Prediction—different genre.
- JslyktsKMY (avg 5.75, Round 2): Optimization Theory critique—similar genre, partially duplicative of prior work.
- GqI4fTVUXC (avg 6.00, Round 2): NTK Theory critique—similar genre, weaker logical connection between evidence and claims.
- 5jWsW08zUh (avg 5.75, Round 2): Lipschitz continuity—different genre.
- PlZIXgfWPH (avg 5.75, Round 2): Hyperparameter landscapes—different genre.
- fXJCqdUSVG (avg 6.50, Round 2): Safeguards evaluation—most comparable anchor, similar rigor and contribution type.
- icTZCUbtD6 (avg 6.20, Round 2): Sample Hardness—different genre but similar evaluation-focused contribution.
- ox2ATRM90I (avg 6.20, Round 2): ICU Benchmark—different genre.
- G3CpBCQwNh (avg 6.50, Round 3): PhysPDE—different genre (new method).

The paper is a well-executed, methodologically sound re-analysis with a genuine technical contribution (Best-of-N). Its weaknesses (overclaim on the equal-performance conclusion, Telegram-link evidence for one sub-claim, thin blueprint section) are bounded and addressable. It is comparable to accepted critique papers scoring 6.0–6.5 and clearly stronger than rejected re-analysis papers scoring 3.75–4.40.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>