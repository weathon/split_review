## Summary

This paper presents a large-scale empirical study (400k+ GPU-hours) of RL scaling for LLMs. It proposes a sigmoidal compute-performance curve (Equation 1) to model pass rate as a function of training compute, enabling extrapolation from shorter runs. Through systematic ablations of design choices, the authors develop **SCALERL**, an RL recipe that scales predictably to 100,000 GPU-hours and achieves superior asymptotic performance and compute efficiency compared to several existing recipes (GRPO, DAPO, Magistral, MiniMax). The paper combines a methodological contribution (sigmoid-based predictive scaling for RL) with a practical contribution (the SCALERL recipe and empirical insights about which design choices affect asymptotic performance vs. efficiency).

## Strengths

1. **Massive-scale systematic empirical study**: The paper conducts over 400,000 GPU-hours of RL experiments, which is an order of magnitude larger than comparable studies (e.g., 3.5× ProRL). This scale enables the authors to observe saturating behavior and validate predictions at 100k GPU-hours — a rare and valuable resource for the community.

2. **Sigmoidal scaling framework for RL**: The paper introduces Equation (1) to model RL performance as a saturating function of compute, drawing an explicit parallel to pre-training scaling laws. The central demonstration in Figure 1a — a fit on the first 50k hours accurately predicting performance at 100k hours — is compelling and provides evidence that RL training can be more predictable than the current "art" suggests.

3. **Systematic leave-one-out (LOO) ablations**: Section 4 presents an unusually rigorous ablation where each component of SCALERL is individually reverted. Each LOO variant consumes 16,000 GPU-hours and the extrapolation (fit on 8k hours, verify at 16k) validates both the predictability claim and the individual contribution of each design choice. This goes well beyond typical post-hoc ablations.

4. **Actionable decomposition of design choices into A vs. B effects**: The paper cleanly separates which design choices affect asymptotic performance (A) vs. compute efficiency (B). Findings such as "FP32 precision at logits improves A from 0.52 to 0.61" and "loss aggregation and advantage normalization primarily affect B not A" provide concrete, evidence-based guidance for practitioners.

5. **Cross-axis scaling validation**: Section 5 shows that the sigmoidal framework generalizes across generation length, batch size, and model size (8B dense → 17B×16 MoE), with extrapolated trajectories matching extended training. This strengthens the generality of the approach.

## Weaknesses

### Major

1. **Predictive scaling validation is narrower than the claims**: The paper frames the work as a "scientific framework" for predicting RL scaling, but the validation of extrapolation is limited to SCALERL on Polaris-53k (math). The central demonstration (Figure 1a) validates one extrapolation point (50k→100k hours). The LOO experiments validate fit-on-8k→extrapolate-to-16k, but only for SCALERL variants. The cross-recipe comparison (Figure 2) shows extended points aligning for SCALERL and MiniMax, but crucially, the other methods (GRPO, DAPO, Magistral) either do not show extended points that validate their extrapolated curves or the fit is looser. The claim that the framework enables "cost-effective evaluation of algorithmic improvements" would require systematic demonstration across multiple methods and cutoffs (e.g., fit on T/4, T/2, 3T/4 and measure prediction error). The current evidence supports the claim of predictability for SCALERL specifically, but not yet a general methodology.

2. **The LOO fixed-A re-fitting procedure is not adequately explained**: The paper states "we average the asymptotic reward A across all runs, re-fit the curves with this fixed A" and reports A=0.685. However, the individual A values from the original fits (shown in the same table) range from 0.590 to 0.610, averaging ~0.604 — far from 0.685. The paper does not explain how 0.685 is obtained, nor does it justify why this value (substantially above any observed pass rate) is appropriate for re-fitting. This makes the "fitted B with fixed A" column difficult to interpret and undermines one of the key quantitative comparisons in the paper. The qualitative conclusion (SCALERL is best) holds from the original fits, but the efficiency analysis via re-fitted B values needs clarification.

### Minor

3. **No statistical uncertainty or variance assessment**: All experiments appear to be single runs with no error bars, confidence intervals, or multi-seed comparisons. The fitted parameters A and B will vary with random seed and evaluation noise. While multiple seeds at this compute scale are expensive, the paper draws conclusions from relatively small differences in B (e.g., 2.01 vs. 1.82–1.97 in the LOO analysis) without any uncertainty quantification. At minimum, bootstrapping within-run variation or sensitivity analysis to the early-cutoff choice would strengthen the quantitative claims.

4. **Fairness of baseline comparisons is unclear**: The paper compares SCALERL against GRPO, DAPO, Magistral, and MiniMax (Figure 2) and reports that SCALERL achieves the highest A=0.61 and B=1.97. However, the main text does not describe whether hyperparameters for these baselines were tuned for this specific setting (8B, Polaris-53k, verifiable math) or were taken from default published values. The FP32 precision fix improves A from 0.52 to 0.61 — it is not stated whether baselines were run with or without this fix. While Appendix A.17 (not accessible in the extracted text) may address this, the main text would benefit from a clear statement about baseline configuration and the degree of tuning performed.

5. **Framing overstates generality**: The abstract and introduction frame the contribution as a general "scientific framework" for RL scaling, but the experiments are conducted on a single dataset (Polaris-53k) in a single domain (verifiable math), with a single base model (8B dense). The AIME-24 results (Figure 1b) show a looser fit. The multi-task RL experiment (math + code) is mentioned only in passing. A more bounded framing — e.g., "a framework for analyzing RL scaling in math reasoning" — would better match the evidence presented.

### Trivial

6. The AIME-24 fit in Figure 1b appears noticeably looser than the validation fit. Including the downstream generalization fit quality (error bars or RMS error) would help readers assess how well the iid scaling transfers.

7. The paper does not evaluate whether the forced-interruption phrase choice matters for the scaling behavior. This is acknowledged as future-worthy but not a core flaw.

## Nice-to-Haves

- Systematic evaluation of extrapolation accuracy across multiple early cutoffs (e.g., fit on T/4, T/2, 3T/4) for each run would quantitatively measure how early one can reliably extrapolate.
- Reporting the compute required to reach a fixed pass rate (e.g., 0.55) as a complementary comparison metric alongside the asymptotic analysis would avoid dependence on the fixed-A re-fitting.
- A brief discussion of which design choices cause instability at large compute (referenced in Appendix A.16) would be valuable for practitioners trying to adopt the recipe.

## Removed Points

- **Criticism about sigmoid choice evidence being "only in the appendix"** (harsh critic Section 2.1): Removed per hard rules — the appendix exists in the original submission and is stripped by the parser.
- **Criticism about missing appendix content, missing proofs, or absent references**: Removed per hard rules — the parser strips these sections; they exist in the original submission.
- **Criticism that the paper "does not include a table of training hyperparameters"**: Removed per hard rules — Appendix A.3 likely contains this information; the paper references it.
- **Criticism that baselines may not use FP32 fix (harsh critic Section 3.2)**: Partially addressed — MiniMax et al. (2025) is cited as having identified the issue, so at least that baseline is consistent. The concern about other baselines is kept but demoted to Minor.
- **Speculation about FP32 fix creating "tactical advantage"**: Removed as speculative — the paper cites this as a known issue identified in prior work (MiniMax et al., 2025), not a novel trick.

## Novel Insights

The reviews collectively surface an insight not fully articulated by the paper itself: the sigmoidal scaling curve introduces a useful *separation principle* for RL recipe design — one can now ask separately whether a change raises the ceiling (A) or accelerates the climb (B). This decomposition offers a more structured way to compare RL algorithms than raw performance curves. However, the fact that this separation depends on a curve fit whose reliability varies across methods (some recipes don't follow smooth sigmoidal trajectories) means the framework is most useful as a diagnostic tool for *stable, scalable* recipes rather than as a universal law.

## Suggestions

1. **Clarify the LOO fixed-A computation**: Explain how A=0.685 is derived (joint optimization across all curves? Including a different set of runs?) and acknowledge the discrepancy with the arithmetic average of individual A values (~0.604). Alternatively, supplement or replace the fixed-A analysis with compute-to-reach-threshold comparisons (e.g., GPU hours to reach pass rate 0.55), which are model-free and directly observable.

2. **Add systematic extrapolation error analysis**: For each run, fit on multiple early cutoffs and report the prediction error at the full budget. Even a single additional cutoff (e.g., fit on 25% and 75% of the total compute) would substantially increase confidence in the framework's predictive reliability.

3. **Address baseline tuning transparency**: Add 1-2 sentences in the main text (not just the appendix) clarifying how each baseline's hyperparameters were set — e.g., "We used the default hyperparameters from each baseline's published recipe without further tuning" or "We performed a small grid search over learning rate for each method." Acknowledge explicitly whether the FP32 precision fix was applied to all baselines.

4. **Provide uncertainty estimates**: Report sensitivity of the fitted A and B parameters to the choice of early-cutoff threshold. Bootstrapping evaluation noise or showing the range of values across reasonable cutoff choices would give readers a sense of the stability of the reported advantages.

5. **Tone down the framing in the abstract/introduction**: Replace "scientific framework" and "science of RL scaling" with more measured language like "a methodology for analyzing" or "principled approach to studying" — the current framing promises more generality than the evidence supports.

## Score and Decision

**Round-1 bracket**: I initially bracketed the paper between 4.5 and 6.5 based on topic-anchored queries (scaling laws for RL/post-training/LLMs). The low-band (<3.5) topic anchors were all topically distant and score 3.0-3.33; the middle-band anchors included "Does RLHF Scale?" (5.50), "Inference Scaling Laws" (5.75), "(Mis)Fitting Scaling Laws" (5.75), and "Scaling Laws for Imitation Learning" (6.20).

**Weakness-anchored queries**: Queries probing "single run no error bars" and "baseline tuning unclear" returned anchors spanning 3.0-6.75, confirming that these weaknesses alone do not determine the score but are associated with a wide range. The most relevant comparison is "Does RLHF Scale?" (5.50), which shares the limitation of studying one RL paradigm in a narrow domain and was critiqued for missing baselines and limited generalizability.

**Round-2 narrowing**: Queries within (4.5, 6.0) returned "Does RLHF Scale?" (5.50), "A Hitchhiker's Guide" (5.20), and "(Mis)Fitting Scaling Laws" (5.75). Queries within (6.0, 7.5) returned "Scaling Laws for Imitation Learning" (6.20, Reject), "Scaling Law with LR Annealing" (6.75, Reject), and "Language models scale reliably" (6.50, Accept).

**Anchor list**:
- FIXk0RP960 / 5.50 / round1-topic-mid + round2 / "Does RLHF Scale?" — similar topic and approach, less compute, comparable scope limitations. Paper under review is more comprehensive.
- VNckp7JEHn / 5.75 / round1-topic-mid / "Inference Scaling Laws" — empirical scaling study with error bars, accepted. Paper under review has larger-scale experiments but no error bars.
- LYS3RhIYCq / 6.20 / round1-topic-mid + round2 / "Scaling Laws for Imitation Learning" — rejected despite high avg due to fundamental design issues. Paper under review doesn't share those fundamental flaws.
- xI71dsS3o4 / 5.75 / round2 / "(Mis)Fitting Scaling Laws" — survey paper, different genre.
- xGM5shdGJD / 5.20 / round2 / "A Hitchhiker's Guide to Scaling Law Estimation" — scaling law methodology paper, less directly relevant.
- BDisxnHzRL / 4.25 / round1-topic-mid / "Scaling Laws for Predicting Downstream Performance" — weaker methodology, limited model sizes.
- iZeQBqJamf / 6.50 / round2 / "Language models scale reliably" — stronger methodology, accepted. Paper under review is less methodologically rigorous than this anchor.
- wg1PCg3CUP / 8.00 / round1-topic-high / "Scaling Laws for Precision" — top-tier methodology, accepted.
- FIXk0RP960 / 5.50 / round1-weakness-baseline / "Does RLHF Scale?" — also criticized for baseline and domain concerns.

**What did the low-band anchors fail at, and does the paper under review share any of those failures?** The low-band topic anchors (score 3.0-3.33) were not topically close enough to draw meaningful comparisons. The most relevant low-score anchor from weakness queries was KxQnhe5UuJ (3.00) on hyperparameter optimization, which is about a different problem (continual learning HPO). The paper under review does not share the fundamental flaws that caused those papers to score 3.0. The closest relevant anchor at a lower score is "Does RLHF Scale?" (5.50), whose weaknesses (limited domain, unclear whether results generalize, no error bars in some evaluations) partially overlap with the paper under review.

**Final assessment**: The paper has genuine strengths — a massive compute investment, systematic ablations, and a practical recipe that demonstrably scales. The predictive scaling claim is partially supported but overclaimed relative to the evidence. The LOO fixed-A analysis needs clarification. Compared to "Does RLHF Scale?" (5.50, Reject), this paper is more comprehensive and has a stronger methodological contribution. Compared to "Inference Scaling Laws" (5.75, Accept), this paper has larger-scale experiments but lacks error bars and has a concerning methodological gap in the LOO analysis. I place it at the lower end of the "revise" band.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>