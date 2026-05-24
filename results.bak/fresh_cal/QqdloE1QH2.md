Now I have all the information needed. Let me compile the final consolidated review.

---

## Summary

This paper introduces MMA, a large-scale multilingual dataset (332K informal-formal pairs across Isabelle and Lean4) for autoformalization, created by using GPT-4 to "informalize" (translate in the reverse direction) statements from the Archive of Formal Proofs and mathlib4. The authors fine-tune LLaMA-33B on MMA and manually evaluate the resulting models on 100 problems from miniF2F and ProofNet. The core findings are that fine-tuning on MMA yields meaningful autoformalization ability (16-18% acceptable formalizations with minimal corrections, vs. 0% for the base model), and that joint training on both formal languages outperforms monolingual training (16-18% vs. 6-11%).

---

## Strengths

1. **First large-scale multilingual autoformalization dataset.** MMA is the first parallel dataset containing more than one formal language (Isabelle + Lean4), with 332K pairs — 4× larger than the biggest existing dataset (ProofNet). This directly addresses the data scarcity bottleneck identified in prior work (Section 3, Table 1).

2. **Empirical evidence that multilingual training improves autoformalization.** The joint (Isabelle + Lean4) model achieves 16-18% acceptable formalizations on miniF2F and ProofNet, compared to 6-11% for monolingual models and 0% for the base model (Figure 3, Section 5). This is measured under blinded evaluation by two expert-level formal proof assistant users (line 229) using a more nuanced 0-4 effort scale rather than binary correctness.

3. **Principled reverse-translation methodology.** The paper provides both an analytical argument (formal languages are precise and syntactically rigid, making informalization easier than formalization) and empirical justification (citing prior work finding 62.3% informalization accuracy vs. 13.4% formalization accuracy) for using GPT-4 to informalize, which is a scalable approach to dataset creation (Section 3).

4. **Nuanced evaluation with correction-effort scale.** The 0-4 Likert scale for human correction effort is more informative than the binary correctness judgments used in prior autoformalization work (Wu et al. 2022, Azerbayev et al. 2023), enabling finer-grained assessment of practical utility (Section 5).

5. **Open release of dataset and models.** The paper commits to releasing both the MMA dataset and fine-tuned model weights, enabling reproducibility and downstream use.

---

## Weaknesses

### Fatal
None.

### Major

1. **Human evaluation of the multilingual advantage lacks statistical characterization.** The headline claim that joint training yields 16-18% acceptable formalizations vs. 6-11% for monolingual training rests on a manual evaluation of only 100 problems (50 miniF2F + 50 ProofNet) with no confidence intervals, significance tests, or inter-annotator agreement metrics. The paper acknowledges this limitation (lines 357-358: "If we had more resources to inspect all generated formalisations, this could reduce the sampling variance"), but the central experimental finding remains undersupported. While the observed differences are directionally plausible and the dataset contribution is independent of this finding, the paper's strongest claim — that multilingual data is decisively better — would benefit substantially from a larger sample or bootstrapped interval estimates. This is a significant weakness in an otherwise well-motivated experimental design.

### Minor

2. **Dataset quality is not systematically characterized.** The paper acknowledges that GPT-4's informalisations can be noisy (Section 3, "eint" example) and treats them as "noisy approximations" (line 173), but does not provide any systematic human evaluation of the informalisations' correctness, faithfulness, or diversity. For a dataset paper, users would benefit from knowing, e.g., what fraction of the 332K informalisations are fully correct, partially correct, or misleading. The downstream task performance provides indirect validation, but direct quality characterization is absent.

3. **Data-efficiency claim conflates mechanism with observation.** The paper states that multilingual training is "much more data-efficient" (line 216) because the joint model achieves better validation loss despite seeing fewer tokens per language. This is a valid empirical observation, but the effect could equally arise from regularization through multitask learning. The paper does not disentangle these mechanisms or provide a token-matched benchmark comparison. The claim would be strengthened by comparing joint vs. monolingual models at equal token budgets per language, not just equal step counts.

4. **The compilation rate finding is noted but not explored.** The joint model compiles less than the Isabelle-only model on Isabelle (24% vs. 36% on miniF2F) but compiles more than the Lean4-only model on Lean4 miniF2F (20% vs. 14%). The paper attributes the Isabelle drop to tighter type-checking of the joint model's output (line 256) but does not investigate this pattern or its relationship to the quality results.

5. **Effort-level intermediate distinctions are underspecified.** The 0-4 Likert scale defines only the endpoints (0: no correction; 4: "similar or more effort than formalising from scratch") and groups 0-1 as "acceptable." The distinction between effort levels 1, 2, and 3 is not described, making it hard for readers to interpret the histograms or replicate the evaluation.

### Trivial

- Figure 3 (effort histograms) does not include numeric y-axis labels in the text description, making the precise bar heights only approximately interpretable from the prose.
- The relation between epochs and training steps (Section 4) is mathematically correct but could be stated more explicitly: the three models are trained for the same number of gradient updates, and the differing epoch counts naturally follow from the differing dataset sizes.

---

## Nice-to-Haves

- A bootstrapped confidence interval or power analysis for the 100-sample human evaluation would substantially strengthen the paper's central claim.
- A human quality-rating of a random sample of 200-300 informalisations from MMA (for correctness, faithfulness, and naturalness) would be a valuable resource for future users.
- A comparison at equal token budgets per language (not just equal step counts) would clarify the data-efficiency claim.
- Qualitative error analysis characterizing the recurring failure modes of joint vs. monolingual models.

---

## Removed Points

- The harsh critic's concern that "the observed improvement could easily arise from sampling variance" is speculative overstatement: with n=100, a 10-point difference (16% vs. 6%) is meaningful, but the review retains the legitimate core concern that statistical significance is not established.
- The complaint that the paper "does not explain how MMA goes beyond simply scaling up the approach of Azerbayev et al. (2023)" is factually addressed — the paper explicitly states MMA is the first multilingual dataset and is 4× larger (Section 2, line 102).
- The Strength Finder's claim that the paper provides a "concrete case study illustrating multilingual advantage" is kept in weakened form (it's one example); the claim that Figure 3 (case study) demonstrates the joint model "makes fewer mistakes" is accurate as stated.

---

## Novel Insights

None beyond the paper's own contributions. The key insight — that informalization is easier than formalization and can be used to create parallel data at scale, and that multilingual training transfers across formal languages — is the paper's own contribution, well-articulated in the paper.

---

## Suggestions

1. **Strengthen the human evaluation.** Report confidence intervals (e.g., bootstrapped 95% CIs) for the effort-level proportions and inter-annotator agreement (Cohen's kappa or Krippendorff's alpha) for the two expert raters. Even a brief justification of the 100-sample size via expected effect size would help.
2. **Sample and rate informalisations.** Have human raters evaluate 200-300 randomly sampled informalisations from MMA for correctness and naturalness, and report the distribution. This directly addresses a core expectation for a dataset paper.
3. **Clarify the mechanism behind the multilingual benefit.** Add a discussion of whether the improvement comes from data efficiency, regularization, or both, and ideally add a token-matched baseline.
4. **Provide explicit effort-level rubrics.** Define what distinguishes effort levels 1, 2, and 3 with concrete examples, to improve reproducibility.

---

## Score and Decision

**Overall assessment:** The paper makes a genuine contribution with the MMA dataset — it is the first multilingual autoformalization dataset of substantial scale, and it is released openly. The experiments convincingly show that the dataset enables models to acquire autoformalization ability (from 0% to 16-18% acceptable formalizations). The claim that multilingual training specifically outperforms monolingual training is directionally supported but rests on a human evaluation with limited statistical characterization. The paper is transparent about its limitations. The dataset contribution alone is strong enough to warrant acceptance, and the experimental findings, while not definitive, are suggestive and consistent with the paper's thesis. With strengthened evaluation, the paper would be stronger, but in its current form it makes a solid contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>