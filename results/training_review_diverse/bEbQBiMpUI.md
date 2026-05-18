Now I have a thorough understanding of the paper. Let me construct the final review.

---

## Summary

This paper studies the mechanism behind intrinsic self-correction in LLMs — where a model improves its own responses using only task-level instructions without external feedback. The authors empirically demonstrate that across six diverse tasks (social bias mitigation, jailbreak defense, text detoxification, commonsense generation, VQA, visual grounding), iteratively applying self-correction instructions leads to converged performance. They link this convergence to reduced model uncertainty and calibration error, and propose that the mechanism involves "latent concepts" (moral orientation in hidden states) activated by instructions, which in turn drive uncertainty reduction. The evidence includes probing experiments showing concept convergence, a simulation task showing concept shifts predict uncertainty changes (83% accuracy), and a mathematical formulation of how repeated instructions affect the activated concept.

## Strengths

1. **Comprehensive empirical demonstration of convergence across diverse tasks.** The paper evaluates six distinct tasks spanning multi-choice QA (social bias mitigation, jailbreak defense), generation (text detoxification, commonsense generation), and multimodal settings (VQA, visual grounding). Figure 3 provides clear convergence curves, and the authors explicitly document that QA tasks converge within 1 round while generation tasks require 6–10 rounds. This goes beyond prior work (e.g., Huang et al. 2023a, which emphasized LLMs' difficulty in amending responses) by systematically documenting that intrinsic self-correction does converge to a stable state.

2. **Empirical linking of convergence to uncertainty and calibration.** Section 4 connects convergence of performance (Figure 3) to reductions in model uncertainty and calibration error (Figure 4), with the temporal alignment between the two sets of curves providing convergent evidence for the proposed mechanism. The use of both ECE (for QA) and Rank-calibration (for generation) is reasonable and appropriately adapted to the task format.

3. **Probing analysis of latent concepts.** Section 5 operationalizes "latent concepts" via linear probing vectors and demonstrates both convergence (concept stability under consistent instructions) and steerability (concept responds to instruction morality). The intervention experiments where immoral instructions are injected at specific rounds (2, 5, 8) provide a clear demonstration that the activated concept tracks instruction morality, which supports the logical framework in Figure 2.

4. **Simulation task quantifying concept–uncertainty dependence.** The logistic regression experiment (Section 6.1) using 2,000 samples from RealToxicityPrompts achieves 83.18% accuracy with very low variance (0.00024) in predicting uncertainty change from concept change. This provides a clean quantitative validation of the dependence formalized in Equation 1, showing that concept shifts carry predictive information about uncertainty movements.

## Weaknesses

### Fatal
None.

### Major

1. **The mathematical derivation in Section 6.2 is not properly derived and should not be presented as a valid theoretical foundation.** The derivation of \(p(C_p|q_k)\) as proportional to \((c_i c_y)^{t-1} p(C_p|q_0)\) makes conditional independence assumptions that, when correctly expanded via Bayes' rule, yield a denominator involving powers of \(c_p\) (not just \(c_p\) once). The specific expression \(p(C_p|q_k) = (c_i c_y)^{t-1} p(C_p|q_0)\) is not what the stated assumptions and Bayes' rule produce under proper normalization. Furthermore, the paper claims that \(p(C_p|q_k) \approx 0\) while still maintaining \(p(C_p|q_k) > p(C_n|q_k)\) — these statements are internally inconsistent if the probabilities sum to 1. The paper presents this as a formal explanation ("This formulation explains why model uncertainty evolves towards convergence"), but the math does not hold up to scrutiny. **Why this matters:** While the paper's empirical contributions are largely independent of this theory, the paper frames the theoretical analysis as a core part of "unveiling" the mechanism. Presenting a mathematically unsound derivation weakens rather than strengthens the paper's explanatory ambition. The authors should either provide a correct derivation with proper normalization and clearly stated assumptions, or explicitly reframe this section as an illustrative sketch (not a derivation).

2. **Causal claims about the concept–uncertainty relationship are not supported by the evidence.** Section 6.1 states its goal is to "empirically validate the strong causal relationship between concept and uncertainty," and the conclusion states the concept is "a strong driving force for the change in model uncertainty." However, the experiment only shows that concept shifts *predict* uncertainty changes — it is a correlational finding. Both concept and uncertainty could be driven by a third variable (e.g., the instruction itself or the model's internal state). Causal claims require intervention (e.g., steering the concept independently of the instruction and measuring downstream effects on uncertainty). **Why this matters:** The paper's logical framework (Figure 2) posits a causal chain: instructions → concept → uncertainty → calibration → performance. Without causal evidence for the concept→uncertainty link, the mechanism remains a correlation story. This is a gap in the paper's central explanatory narrative.

### Minor

3. **Convergence "guarantee" claims are stronger than the evidence supports.** The paper states that "intrinsic self-correction offers convergence guarantees across a variety of tasks" and uses the section title "THE GENERAL CONVERGENCE OF INTRINSIC SELF-CORRECTION." The evidence comes from a single language model (zephyr-7b-sft-full) for all language tasks (GPT-4 is only used for vision-language tasks). No multiple-seed runs are reported for the main experiments (Figures 3, 4). Convergence patterns also vary substantially across tasks (1 round for QA vs. 6–10 for generation), suggesting the phenomenon may be task-dependent. The authors should qualify these claims to reflect the actual empirical scope (e.g., "we observe convergence in the tasks and models studied") rather than implying a universal property.

4. **The "uncertainty = 1 − ECE" transformation in Figure 4 hinders interpretation.** For QA tasks, the paper plots uncertainty as \(1 - \text{ECE}\) rather than reporting ECE directly. This transformation obscures the absolute calibration level — it is unclear whether the baseline ECE is plausibly in the 0.8–0.9 range (which would be very high for an instruction-tuned model) or whether the transformation is simply an unusual presentation choice. The convergence conclusion may still hold, but the figure would be more interpretable if ECE were reported in its standard form.

5. **Missing details for vision-language experiments.** The paper includes VQA and visual grounding but does not describe how self-correction instructions are applied in the multimodal setting (e.g., are instructions appended to the text portion of the prompt? How is the visual input handled across rounds?). Without this information, the VL results cannot be properly compared to the language-only tasks, and the reader cannot assess whether the same mechanism applies.

6. **Error bars are absent from the main convergence results.** The simulation task includes variance (0.00024), and Figure 5 reports mean and standard variance for concept probing. But Figures 3 and 4 (the central empirical results) do not report any measure of variability across runs, questions, or seeds. Standard deviations or confidence intervals would significantly strengthen the convergence claim.

### Trivial

7. **"Irreversibility" is a misnomer.** The intervention experiments show that when an immoral instruction is injected, the activated concept switches to negative and stabilizes there. This demonstrates *instruction-steerability* (the concept tracks the current instruction's morality), not *irreversibility* (which would imply the concept cannot be changed once set). The property that matters for the paper's argument is that under *consistent* instructions the concept converges and remains stable — which is well demonstrated, but the term "irreversibility" overstates what is shown.

## Nice-to-Haves

- A small-scale causal intervention experiment (e.g., activation steering or adversarial prefixes that independently manipulate the concept while keeping the instruction fixed) would transform the correlational concept→uncertainty evidence into genuinely causal support.
- A discussion of why convergence speed differs between QA and generation tasks — is it tied to output space size, number of tokens, or some other factor? A brief analysis correlating uncertainty reduction rate with task complexity would strengthen the paper.
- If the paper's claims are to be titled "general convergence," additional model families (e.g., Llama, GPT-3.5) would add weight. Within the scope of a single paper this is a reasonable limitation, but the claims should be scoped accordingly.

## Removed Points

- **Reviewer criticism about normalization missing a "marginal probability of q_t":** Partially correct — the derivation does have normalization issues — but kept in Major weakness #1 with proper analysis rather than the reviewer's specific phrasing. The reviewer's framing that the expression "is not a valid probability" is correct in that the denominator is wrong, but the qualitative pattern (decay with rounds) is still plausible.
- **Reviewer claim that baseline ECE "seems implausible":** This is speculation without evidence. The paper reports ECE-derived uncertainty, and without seeing the actual ECE values, this criticism is unsubstantiated.
- **Reviewer claim about "no cross-family replications":** The paper uses zephyr-7b-sft-full (Mistral-7B based) for language and GPT-4 for vision-language, which are from different families. The concern is valid but not as extreme as stated — kept as Minor weakness #3 with appropriate nuance.
- **Strength Finder's claim that the mathematical derivation "formally shows" the mechanism:** Removed because the derivation is flawed. The strength about the causal chain framework is kept but without the mathematical derivation component.

## Novel Insights

The paper's most novel insight is the empirical demonstration that intrinsic self-correction converges to a stable state — a finding that nuances prior work (Huang et al. 2023a) which emphasized LLMs' inability to amend responses. The temporal alignment between concept convergence (Figure 5), uncertainty reduction (Figure 4), and performance stabilization (Figure 3) across multiple tasks is a genuinely interesting observation. The logistic regression result (83% accuracy predicting uncertainty change from concept change) provides a clean quantitative link between two variables that are usually studied separately. However, the paper's attempt to elevate this to a formal causal mechanism is where it overreaches; the descriptive findings are the true contribution.

## Suggestions

1. **Fix or remove the mathematical derivation in Section 6.2.** Either provide a correctly normalized derivation with explicit, justified conditional independence assumptions, or reframe the section as an intuitive sketch with no pretense of formal proof. The empirical contributions are strong enough to stand alone.

2. **Replace "causal" language in Section 6.1 with "predictive" or "dependent."** The logistic regression shows that concept changes predict uncertainty changes. This is valuable on its own. Calling it causal without an intervention experiment is misleading.

3. **Temper the convergence claims** to match the empirical scope: "we observe convergence in the tasks and models studied" rather than "convergence guarantees."

4. **Report ECE directly** in Figure 4 (or alongside the \(1-\text{ECE}\) transformation) and add error bars or confidence intervals to the main experimental figures.

5. **Add a paragraph describing the VL self-correction pipeline** — how instructions are formatted, whether the visual modality is involved in the correction, and how this compares to the language-only setup.

6. **Rename "irreversibility"** to something more precise, such as "instruction-steerability" or "concept stability under consistent instructions."

## Score and Decision

This paper makes a genuine empirical contribution by systematically documenting the convergence of intrinsic self-correction across diverse tasks and linking it to uncertainty, calibration, and latent concepts. The probing experiments and simulation task are well-designed. However, the paper overreaches in two important ways: (1) the mathematical derivation in Section 6.2 is not valid as presented, and (2) the causal claims about the concept→uncertainty relationship are not supported by the correlational evidence. These weaknesses are addressable through revisions. The empirical findings are valuable enough to warrant publication, but the paper needs significant revision to align its claims with its evidence.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>