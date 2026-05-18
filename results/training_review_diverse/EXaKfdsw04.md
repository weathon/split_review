Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

The paper proposes StepProof, a method for sentence-level autoformalization verification of natural language mathematical proofs. Instead of formalizing and verifying an entire proof at once (FULL-PROOF), StepProof decomposes the proof into individual sentences, formalizes each, pushes them onto a formal proof stack, and verifies them incrementally using Isabelle. On GSM8K with Llama3 8B-Instruct, StepProof improves the one-attempt proof pass rate by 15.1% and reduces formalization and proof time by roughly 39% compared to FULL-PROOF. The paper also tests on 100 MATH Number Theory problems with manually tailored proofs and reports a step-level passing rate metric.

## Strengths

- **Novel and well-motivated method for step-by-step autoformalization.** The paper identifies a genuine limitation of existing FULL-PROOF approaches — they cannot localize errors, and a single mistake in one step fails the entire proof. StepProof's sentence-level decomposition with incremental verification and a formal proof stack is a clean solution to this problem. This is a genuinely new strategy in the autoformalization literature.

- **Controlled strategy comparison shows clear empirical gains.** The within-model comparison of StepProof vs. FULL-PROOF (Table 1, using Llama3 8B-Instruct on the same GSM8K dataset) is properly controlled. StepProof improves the one-attempt pass rate by 15.1% while reducing formalization time by 38.9% and proof time by 39.5%, with lower variance. These results directly validate the method's core claims about improved efficiency and robustness. (Section 4.2)

- **First autoformalization evaluation on a small open-source LLM.** Prior work (Majority Voting, DTV, DSP) used the closed-source Minerva (540B). The paper explicitly fills this gap by testing on Llama3 8B-Instruct, demonstrating that autoformalization is viable without large proprietary models. This is a useful contribution to the community. (Sections 2, 4.1)

- **Introduces the step passing rate metric $r_s$.** The paper proposes a finer-grained metric beyond binary proof success/failure, tracking the proportion of steps verified within each proof. This captures partial progress that FULL-PROOF cannot provide. The paper reports that after 10 attempts, 38.1% of proofs completed over half their steps (Table 3). (Section 4.2)

## Weaknesses

### Fatal
None.

### Major

- **The evaluation dataset (GSM8K) does not match the paper's claimed scope of "mathematical proofs."** GSM8K contains grade-school arithmetic word problems with chain-of-thought reasoning traces ("Alice has 3 apples, Bob gives her 2 more, now she has 5"). These are solution narratives, not mathematical proofs. The paper's title and abstract claim "step-by-step verification of natural language mathematical proofs," and the introduction frames the work in the context of verifying complex mathematical reasoning (lines 10-14). Yet the primary evaluation is on a dataset that does not contain actual proofs (e.g., from MiniF2F, ProofNet, or competition solutions). The MATH Number Theory subset (100 problems) partially addresses this, but the manual rewriting of those proofs (Issue below) undermines the generalizability. **Why this matters**: The core claim — that StepProof verifies "mathematical proofs" — is not supported by the primary evidence. A reader cannot tell whether the method works on actual mathematical argumentation or only on short arithmetic reasoning chains.

- **The baseline comparison against DTV/Majority Voting is uninformative due to mismatched model backbones.** The paper claims that StepProof "surpassed DTV in multi-round verification tests on GSM8K, achieving a 10.3% performance improvement" (Section 4.2). However, DTV and Majority Voting were evaluated using Minerva (a ~540B closed-source model), while StepProof uses Llama3 8B. Without re-implementing these baselines with the same Llama3 8B backbone, the comparison does not control for model capability. The different model sizes, training data, and closed-source nature make any direct comparison meaningless for evaluating the *method*. The only properly controlled comparison is StepProof vs. FULL-PROOF (Table 1). **Why this matters**: The "10.3% improvement" claim in the abstract and body is potentially misleading because it attributes the gain to the method when the model disparity alone prevents any such attribution.

### Minor

- **The method is somewhat underspecified for exact reproducibility.** While the high-level workflow is clear (break into sentences, formalize each, push onto a stack, verify with Isabelle, HOLD for suspended steps, QED for final verification), several details are missing: the exact few-shot prompt template used for LLM formalization, how the "formal proof stack" is implemented in code (how previously verified steps are combined for the next step's context), and how HOLD steps interact with the final QED verification (are they simply assumed true, or is there a separate mechanism?). The paper mentions "one example for few-shot" (Section 4.1) but does not provide it. These gaps would make re-implementation unnecessarily difficult. (Section 3)

- **The manual proof tailoring experiment (Table 4) is not well-controlled.** The paper takes 100 MATH Number Theory problems, makes "simple manual modifications" to make proofs more step-friendly, and observes improved pass rates. The modifications are not described, the number and nature of changes are not documented, and there is no evidence that an independent annotator or objective criteria were used. This experiment shows that hand-rewriting proofs to fit StepProof helps StepProof — which is unsurprising — but does not provide generalizable insight about when natural proofs are formalizable. (Section 4.2)

- **Absolute pass rates are reported only in the table images, not the text.** The text reports relative improvements (15.1% improvement in pass rate) but does not state the absolute one-attempt pass rates for FULL-PROOF and StepProof in the prose. While the absolute numbers are present in the tables (as images), having them in the body would improve readability and assessment. (Section 4.2)

- **The 27.9% full-verification rate after 10 attempts is contextualized as a "significant improvement" without discussing whether this is practically useful.** The paper reports that after 10 retry rounds, only 27.9% of GSM8K proofs complete full verification (Table 3). While this is an improvement over single-attempt baselines, the absolute performance is low, and the paper does not discuss whether this suffices for any practical application. (Section 4.2)

### Trivial
None.

## Nice-to-Haves

- A concrete worked example walking through one problem from the dataset, showing each informal sentence, its Isabelle formalization, the stack state, and how verification proceeds, would greatly improve clarity and address reproducibility concerns.
- Re-implementing DTV with the same Llama3 8B backbone would make the baseline comparison meaningful.
- Reporting error bars or confidence intervals (e.g., over multiple seeds or dataset splits) would strengthen the statistical grounding of the results.
- Evaluating on MiniF2F or another dataset designed for theorem proving (where the informal proofs are genuine mathematical arguments) would directly address the biggest weakness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Table 1 is garbled in the parsed text, so absolute pass rates are unclear"** — The table exists in the paper as an image. The parsing artifact is not an author error. The absolute numbers are present in the original submission.
- **"The paper does not compare step passing rate against any baseline"** — The step passing rate is a new metric introduced by the paper; there are no existing baselines for it. This is a feature, not a weakness.
- **"The paper claims to be 'the first to realize the test of automatic formalization capabilities on small open-source LLMs' — this is a narrow contribution"** — This is a stated contribution, not a weakness. The paper's own framing acknowledges this is a previously unfilled gap.
- **"Missing related works"** — Cannot verify without external sources. The paper covers DSP, DTV, Majority Voting, LEGO-Prover, SlideRule, and the key autoformalization literature.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Temper the scope claims or change the evaluation.** Either rename the paper to reflect that evaluation is on "natural language solution steps" (rather than "mathematical proofs") and use GSM8K as-is, or replace the primary evaluation with a dataset of genuine mathematical proofs (MiniF2F, ProofNet) to support the claimed scope. The controlled StepProof vs. FULL-PROOF comparison is the paper's strongest experiment — porting it to a more appropriate dataset would dramatically strengthen the paper.

2. **Drop or rigorously document the manual tailoring experiment.** Either remove Table 4 entirely (it does not establish generalizability), or turn it into a controlled study with documented modification rules, an independent annotator, and measurement of both FULL-PROOF and StepProof on original vs. modified proofs.

3. **Provide the exact few-shot prompt and a concrete worked example** in an appendix. This would address reproducibility concerns and clarify how the formal proof stack, HOLD, and QED mechanisms work in practice.

4. **Remove or clearly qualify the DTV comparison.** Acknowledge that the comparison is confounded by different model backbones and either report it as "for context only" or re-implement DTV's approach with Llama3 8B.

---

## Score and Decision

The paper proposes a genuinely novel and well-motivated method for step-by-step autoformalization, and the controlled comparison against FULL-PROOF on GSM8K provides valid evidence of its effectiveness on the tested domain. However, the paper's central claim — that it verifies "mathematical proofs" — is not supported by an evaluation on GSM8K (which contains arithmetic solution narratives, not proofs), and the headline comparison against DTV is invalidated by mismatched model backbones. These are fixable issues, but as presented, the evidence does not match the scope of the claims. The core idea has clear merit and could form the basis of a strong resubmission with a more appropriate evaluation.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>