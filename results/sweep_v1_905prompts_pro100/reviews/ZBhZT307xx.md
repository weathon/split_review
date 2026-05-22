Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper provides a comprehensive empirical study of rule-based and model-based verifiers used for reinforcement learning with verifiable rewards (RLVR) in mathematical reasoning. It quantifies the false-negative problem in rule-based verifiers (recall as low as 0.78 on challenging datasets), shows that model-based verifiers improve recall but are vulnerable to reward hacking — especially after fine-tuning — and conducts a systematic probing study exposing 13 hacking patterns that reliably compromise generative verifiers. The paper unifies static evaluation, RL training experiments, and adversarial probing into one coherent analysis.

## Strengths

- **Systematic static evaluation of rule-based verifiers with clear, actionable findings.** Figure 1 and Figure 2 quantify that widely used verifiers (Verl, Qwen, HuggingFace) exhibit near-perfect precision (>99%) but recall degrades to 0.78 on Skywork-OR1, and declines further as generation models become stronger. This is a well-motivated and previously under-documented finding that has practical implications for the community.

- **Well-constructed evaluation dataset with oracle validation.** The 8,000-example dataset (§3.1) is curated across four RL math datasets, four generation models (both short-CoT and long-CoT), and annotated with GPT-4o validated against human judgments (Appendix B). The construction pipeline is clearly described and the dataset itself is a contribution.

- **Systematic adversarial probing study is the paper's strongest contribution.** Section 6 constructs 13 distinct hacking patterns and evaluates them against a broad set of verifiers. Table 3 reveals that generative (CoT) verifiers are highly susceptible (e.g., Qwen2.5-Math-7B: 44% success rate on empty symbols), while discriminative verifiers (xVerify) remain near 0%. The finding that fine-tuning increases fragility (R1-Distill-Verifier-1.5B: adversarial prefix rate rises to 35% from 21.7%) is particularly noteworthy.

- **Reward hacking detection via oracle reward divergence is an effective diagnostic.** Figure 3 (right) clearly shows training reward diverging from GPT-4o oracle reward for the fine-tuned verifier after ~450 iterations, while the untrained verifier stays aligned — a clean demonstration of the mismatch between static accuracy and dynamic robustness.

- **Cross-domain replication strengthens the conclusions.** Results on Skywork-OR1 (math) and WebInstruct-Verified (general science) in Appendices I/J show that both the hybrid verifier benefit and reward hacking vulnerability generalize beyond the primary DeepScaleR setting.

## Weaknesses

### Fatal

None.

### Major

- **RL training experiments lack multiple seeds and have limited evaluation protocol.** The paper conducts a single RL training run per verifier condition and evaluates with a single sample per problem (acknowledged in Figure 3 caption: "due to computational constraints"). While single-run RL training is common in this subfield, the 2.3-point average accuracy gap (Table 2) is modest enough that seed-dependent variability could meaningfully affect interpretation. The individual benchmark gaps range from +0.3 (OlympiadBench) to +5.1 (AIME24), and without confidence intervals or multiple seeds, it is difficult to assess which gaps are reliable. This does not invalidate the results — the direction is consistent (hybrid verifier leads on every benchmark) and the reward hacking signal in Figure 3 is visually unambiguous — but it does limit the strength of the claim that "introducing a stronger verifier is essential for achieving higher performance."

### Minor

- **The claim that "the performance gap does not diminish with additional computation" (§4.3) is stated too strongly.** Figure 3 (left) shows the hybrid verifier curve staying above the rule-based curve throughout training, which is consistent with the claim. However, with a single training run and single-sample evaluation, one cannot rule out that the gap might close or reverse with different seeds or at larger compute budgets. The observation is suggestive rather than conclusively demonstrated.

- **The SimpleRL-Zoo baseline comparison is acknowledged as asymmetric but still presented as a reference point.** The paper correctly notes that SimpleRL-Zoo was trained on data "10 times smaller and less challenging" (§4.3), which undermines its value as a comparison. A controlled ablation with identical training data but different verifiers would strengthen the analysis, though the paper's core comparisons (rule-based vs. hybrid on the same data) are internally controlled.

- **Cross-domain RL results are relegated to appendices.** The paper makes claims about generalization to Skywork-OR1 and WebInstruct-Verified, but the supporting RL training results (Tables 6, 8) appear only in appendices. Bringing at least summary results into the main body would better support the generalization narrative.

### Trivial

- The paper states "the untrained verifier, R1-Distill-Verifier-1.5B" in §5.2 when it should say "the untrained verifier, DS-R1-Distill-Qwen-1.5B" — the naming is slightly inconsistent with Table 1 and could confuse readers.

## Nice-to-Haves

- **Validating the oracle (GPT-4o) against the hacking patterns from Section 6** would strengthen confidence that the oracle reward divergence in Figure 3 genuinely reflects reward hacking rather than oracle vulnerability. While the paper validates GPT-4o against humans for general annotation (Appendix B), probing whether GPT-4o is itself susceptible to the 13 hacking patterns would close a potential confound.

- **Reporting statistical tests** (e.g., bootstrap confidence intervals over the 6 benchmark gap estimates) would help readers assess the reliability of the reported improvements even with single-sample evaluation, since the benchmarks differ substantially in size.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Harsh Critic: "RL experiments are critically underpowered... the reported improvements cannot be reliably interpreted" (framed as fatal).** → Demoted to Major. The single-run/single-sample protocol is a legitimate limitation but is within community norms for RL training of LLMs at this scale. The consistent direction of improvement across all 6 benchmarks and the visually clear reward hacking signal in Figure 3 provide meaningful evidence even without multiple seeds. This is not fatal.

- **Harsh Critic: "The baseline comparison with SimpleRL-Zoo is confusing... the observation that the rule-based verifier + DeepScaleR yields only a small gain over this baseline is interesting but not analysed."** → Demoted to Minor. The paper explicitly acknowledges that SimpleRL-Zoo uses 10x smaller data. This is transparent, not confusing. The paper is not hiding the asymmetry.

- **Harsh Critic: "If the oracle model is also vulnerable, then the oracle reward may itself rise spuriously, masking or distorting the hacking signal."** → Moved to Nice-to-Haves. This is a reasonable caution but speculative — there is no evidence in the paper that GPT-4o is actually vulnerable. The oracle reward *declines* in the hacking case (Figure 3, right), which is inconsistent with the oracle being fooled.

- **Harsh Critic: "The validation in Appendix B (not available in the stripped version) would need to demonstrate..."** → Removed. The appendix is stripped by the parser; this is not an author error. The paper references the validation and we assume it exists.

- **Strength Finder: "Rigorous dataset construction with expert oracle validation"** → Kept but caveated. The dataset construction is solid, but "expert oracle" is GPT-4o, not human experts. The paper acknowledges this and validates against humans.

## Novel Insights

The paper's key conceptual contribution is demonstrating that *static classification accuracy is a poor proxy for a verifier's reliability during dynamic RL training* — fine-tuned verifiers that look better in static evaluation can be more exploitable during training. The probing study further reveals that *generative (CoT) verifiers are systematically more fragile than discriminative ones*, independent of their static accuracy, suggesting that the reasoning process itself opens attack surfaces. These are well-supported and genuinely useful insights for practitioners designing RL reward systems.

## Suggestions

- Consider narrowing the RL claims: "hybrid verifier yields consistent improvements" is well-supported; "gap does not diminish with additional computation" and "introducing a stronger verifier is essential" are stronger claims that the current evidence does not fully warrant given the single-run protocol.

- If computational budget permits for a revision, running even one additional seed for the key comparison (rule-based vs. best hybrid verifier) would substantially strengthen the paper's central RL claims.

- Move key cross-domain RL results (at minimum the Skywork-OR1 and WebInstruct-Verified summary numbers) from appendix to main body to support the generalization claims.

- Probe GPT-4o against the 13 hacking patterns to rule out oracle vulnerability as a confound in the reward hacking analysis.

## Score and Decision

### Calibration Anchors

**Round 1 (bracketing):**
- `vBNTeQ7dPP` (RL for Control with Stability Guarantee): 2.50 — not comparable (different domain)
- `jOuHjFw71C` (Planning in Strawberry Fields): 3.00 — evaluation paper but different topic
- `0er6aOyXUD` (Evaluating Robustness of Reward Models for Mathematical Reasoning): 5.40 — closely related; our paper is more comprehensive and systematic
- `OD9pwKQzXl` (VerifierQ): 5.25 — related verifier work; our paper has broader empirical scope
- `mMPMHWOdOy` (WizardMath): 8.00 — strong results paper; our paper has less impressive empirical gains but more systematic analysis

**Round 1 bracket: 5.5 – 7.5**

**Round 2 (narrowing):**
- `F0GNv13ojF` (On Designing Effective RL Reward at Training Time for LLM Reasoning): 5.17 — similar topic (reward hacking in RL math training); our paper is clearly stronger (more comprehensive, systematic probing, cross-domain)
- `j4s6V1dl8m` (Prover-Verifier Games): 6.00 — related (verifier robustness); our paper has broader scope but lacks human studies; comparable quality
- `nDvgHIBRxQ` (MathCheck): 6.25 — evaluation benchmark; different problem but comparable empirical rigor; our paper addresses a more novel problem
- `KUNzEQMWU7` (MathVista): 7.25 — clearly stronger (novel benchmark, multi-modal, larger scale)

**Final score justification:** The paper sits above the 5.0–5.4 tier (more comprehensive than RewardMATH and RL Reward papers) and is comparable to Prover-Verifier Games (6.00). It does not reach the 7.0+ tier of WizardMath or MathVista because the RL experiments have limited statistical rigor and the gains, while consistent, are modest. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>