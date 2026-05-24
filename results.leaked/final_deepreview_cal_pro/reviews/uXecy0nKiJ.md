Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper demonstrates that activation steering—a widely-used technique for interpretable control of LLMs via inference-time activation perturbation—systematically compromises model safety. Through experiments spanning multiple model families (Llama3, Qwen2.5, Falcon3) at scales from 3B to 70B, the authors show that (1) adding random vectors to residual stream activations induces harmful compliance at rates up to 17% on JailbreakBench, (2) steering with SAE features representing benign concepts yields comparable or worse jailbreaking effects, and (3) averaging just 20 random vectors that jailbreak a single prompt creates a transferable universal attack achieving ~4× compliance amplification on unseen prompts. A case study using the public Goodfire API confirms real-world exploitability.

## Strengths

- **Surprising and important core finding.** The demonstration that random activation perturbations and benign SAE features can break refusal mechanisms challenges the prevailing assumption that activation steering provides safe, interpretable control. This finding has significant implications for a technique that is increasingly deployed in practice (e.g., via public APIs like Goodfire).

- **Comprehensive empirical evaluation.** The paper tests across three model families (Llama3, Qwen2.5, Falcon3), scales from 3B to 70B parameters, 1,000 random vectors, 1,000 SAE features, and the full 100-prompt JailbreakBench dataset spanning 10 harm categories. The per-category breakdown (Fig. 3) shows consistent non-zero compliance across all categories, confirming the effect is not confined to a narrow prompt type.

- **Compelling universal attack construction (Sec. 4.4).** The method of averaging 20 single-prompt jailbreak vectors to create a zero-shot universal attack is creative, lightweight, and practically significant. The attack requires only steering capability—no model weights, gradients, or logits—yet increases compliance by ~4× across models, with Falcon3-7B reaching 63.4% (Fig. 6).

- **Real-world validation via public API (Sec. 4.3).** The case study using Goodfire's production API with a "brand identity" SAE feature provides concrete evidence that the vulnerability exists in deployed systems, not just in controlled lab settings. The observed failure modes (disclaimer-then-compliance, fictional-framing justification) are practically informative.

- **Informative SAE feature analysis (Fig. 4).** The histogram showing 668/1000 SAE features jailbreak at least 5 prompts, combined with the cross-category generalization heatmap, reveals that the vulnerability is both widespread and poorly generalizing—making systematic safety monitoring infeasible.

- **Clear methodology.** The steering procedure is well-specified, including the use of layer-normalized scaling coefficients (α = c · μ^(l)), canonical depth choices, and consistent application to both prompt and generation tokens. The use of greedy decoding eliminates sampling variance as a confound.

## Weaknesses

### Fatal

None.

### Major

None. The core claims are supported by the evidence presented, and no single weakness invalidates the paper's contribution.

### Minor

- **Coefficient selection inflates headline compliance rates (Sec. 4.2).** The full-dataset evaluation uses scaling coefficients c=2.0 for Llama3-8B and c=1.5 for Qwen2.5-7B, which correspond to peaks in the single-prompt sweep curves (Fig. 2a). While the 1/3 depth layer was pre-registered as the primary baseline (Sec. 3.2, line 82: "using the first third layer as our primary baseline for comparative analysis"), the coefficient choice appears post-hoc optimized, making the 17% and 10% headline rates upper-bound estimates rather than representative values. The paper would be strengthened by reporting results at a fixed coefficient (e.g., c=1.0) uniformly across models, then reporting the tuned numbers as adversarial upper bounds. Notably, Fig. 2a does show non-zero compliance across all coefficients, so the qualitative finding is robust; this is a precision concern, not a validity concern.

- **Missing distributional information for random steering vectors.** The full-dataset evaluation reports only the average compliance rate across 1,000 random vectors. The SAE analysis (Fig. 4a) rightly includes a histogram of per-feature jailbreak counts, but no parallel figure exists for random vectors. Without knowing the variance or the fraction of vectors that achieve non-zero compliance, the claim that "steering in a random direction can effectively break the model's refusal mechanisms" is ambiguous—does this mean most random directions, or a concentrated subset? This gap should be addressed.

- **SAE–random comparison uses different models and layers in the full-dataset evaluation.** Random vectors are tested on Llama3-8B and Qwen2.5-7B at 1/3 depth, while SAE features are tested on Llama3.1-8B at 2/3 depth. The paper acknowledges this constraint (Sec. 3.3: "We therefore limited our investigation of SAE feature steering to this specific model and layer") and provides a controlled comparison in Fig. 2c on the same model and layer, but the single-prompt comparison does not fully substitute for a controlled full-dataset comparison. This should be explicitly noted as a limitation.

- **No explicit limitations section.** The paper lacks a dedicated discussion of its limitations, including the coefficient selection issue, reliance on a single dataset (JailbreakBench), white-box access requirement for steering, and the fact that the LLM judge validation details reside in an appendix (which may not be accessible to all readers).

- **Limited mechanistic discussion.** The paper demonstrates the vulnerability convincingly but offers little speculation or analysis on *why* random perturbations break refusal—e.g., whether they interfere with instruction-boundary representations, push activations off the safety-conditioned manifold, or suppress harmfulness-detection features. Even a paragraph of informed speculation would deepen the contribution and connect more firmly to the interpretability literature.

### Trivial

- The layer used for Fig. 2a is stated in the body text but not in the figure caption, which can cause confusion when reading figures independently.

## Nice-to-Haves

- Reporting compliance rates under a fixed, untuned steering regime (e.g., c=1.0 at 1/3 depth uniformly) would provide a realistic baseline for typical, non-adversarial users and strengthen confidence that the effect is not purely a tuning artifact.

- A histogram of per-vector compliance rates for random steering (analogous to Fig. 4a for SAE features) would clarify whether the effect is broad or concentrated in outlier directions.

- Testing the universal attack construction with a few different seed prompts would confirm that the reported amplification does not depend on a particularly lucky choice of "write a tutorial on how to make a bomb."

- A short discussion of potential defense strategies (e.g., adversarial training against steering perturbations, activation-space audits) would increase the paper's constructive value.

## Removed Points

These points from the harsh critic were considered and removed with justification:

- **"LLM-as-judge validation is invisible in the submission"** — REMOVED. The paper explicitly states (line 100) that Appendix B contains a quality assessment against human annotations. The appendix being stripped is a parser artifact, not an author omission. The main text also notes that the judge was selected for calibration accuracy and that incoherent responses are classified as SAFE to prevent inflated rates.

- **"The vulnerability under fixed, untuned steering is never reported"** — REMOVED as framed. The paper reports full sweep curves in Fig. 2a-b showing compliance rates across all coefficients from 0.75 to 2.0. A reader can see the effect at any coefficient, including c=1.0. The concern about headline numbers being tuned is preserved as a minor weakness above, but the claim that untuned performance is "never reported" is factually incorrect.

- **"The paper's narrative repeatedly refers to 'random directions' as though they all behave similarly"** — REMOVED as a separate weakness. This concern is already captured under the missing-distributional-information weakness above; the framing issue is derivative of that data gap.

- **"The SAE–random comparison...does not support a claim that SAE features are intrinsically riskier than random directions"** — DEMOTED to minor. The paper does not claim SAE features are "intrinsically riskier"; it states they "demonstrate comparable potential." The single-prompt controlled comparison (Fig. 2c) does support this. The model/layer confound in the full-dataset evaluation is a limitation, not a false claim.

- **"Choice to use the first third layer as the primary baseline...is stated without explanation"** — REMOVED. The paper explains this choice (line 82): "In line with Wu et al. (2025), we experimented with applying steering at three canonical depths...using the first third layer as our primary baseline for comparative analysis." The choice follows established practice.

- **"The paper currently lacks an explicit discussion of limitations"** — RETAINED as a minor weakness above rather than removed, since this is a genuine gap.

- **"The cross-category heatmap uses only a subset of categories and relies on 'predetermined feature interpretations' from the Goodfire API whose trustworthiness is not discussed"** — REMOVED. The feature interpretations serve as semantic labels for interpretability; questioning the trustworthiness of a public API's feature labels without evidence is speculative. The subset selection (most/least susceptible categories) is a reasonable analytical choice for readability.

## Novel Insights

None beyond the paper's own contributions. The core insight—that activation steering, designed for interpretable control, can inadvertently and systematically break safety alignment—is the paper's contribution, and the reviews do not surface additional novel observations beyond what the paper itself presents.

## Suggestions

- Add an explicit "Limitations" section before the conclusion, acknowledging the coefficient selection issue, reliance on a single evaluation dataset, the white-box requirement for steering, and the SAE-random model mismatch.
- Include a histogram or at minimum the standard deviation and fraction of non-zero vectors for the random steering full-dataset evaluation (analogous to Fig. 4a).
- Report a fixed-coefficient (c=1.0) baseline in Sec. 4.2 alongside the current tuned results, to give readers a sense of effect size under standard settings.
- Add a short mechanistic discussion paragraph speculating on why random perturbations disrupt refusal, linking to known concepts like instruction-boundary representations or safety-conditioned manifolds.

---

**Anchor comparison summary:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| z1yI8uoVU3 | 3.00 | R1 | Weaker—limited empirical depth, unclear contribution |
| DXaUC7lBq1 | 3.00 | R1 | Weaker—tangential topic, less rigorous evaluation |
| 5kMwiMnUip | 1.40 | R1 | Much weaker—basic jailbreak survey |
| BeOEmnMyFu | 2.50 | R1 | Weaker—incremental jailbreak method |
| HuNoNfiQqH | 4.75 | R1 | Weaker—fewer models, less actionable findings |
| 2XBPdPIcFK | 5.00 | R1 | Weaker—outdated baselines, less thorough evaluation |
| 9wjGUN65tY | 5.00 | R1 | Weaker—theoretical steering, lower practical impact |
| wozhdnRCtw | 7.00 | R1 | Comparable—similar empirical depth, different focus (control vs. safety) |
| 6Mxhg9PtDE | 9.50 | R1 | Stronger—unified framework, proposed defenses, deeper analysis |
| I4e82CIDxv | 8.00 | R1 | Stronger—foundational interpretability contribution |
| Bo62NeU6VF | 8.00 | R1 | Stronger—novel defense mechanism with strong results |
| aSy2nYwiZ2 | 6.67 | R2 | Comparable—similar novelty, our paper has broader model coverage and more surprising findings |
| hXA8wqRdyV | 6.14 | R2 | Our paper is stronger—more novel attack surface, more thorough evaluation |
| plmBsXHxgR | 6.25 | R2 | Our paper is stronger—broader model families, more surprising finding |
| YzxMu1asQi | 6.50 | R2 | Comparable—different focus (scaling laws vs. safety), similar empirical rigor |
| r42tSSCHPh | 7.00 | R2 | Our paper is slightly weaker—lacks defense mechanism, lower headline ASR, but attacks a more novel and surprising vulnerability surface |

**Round 1 bracket:** 4.75–8.0. The paper is clearly above the weak-middle anchors (4.75–5.00 range) whose evaluations are narrower and less rigorous, and clearly below the 9.50 anchor (Shallow Safety Alignment) which provides a unified theoretical framework and defense mechanisms.

**Round 2 narrowing:** The paper lands at **6.5**. It is comparable to the 6.50–6.67 anchors (Scaling Laws for Activation Attacks, JailbreakEdit) in empirical rigor and novelty, and slightly below the 7.00 anchor (Catastrophic Jailbreak) which includes a proposed defense and achieves higher headline success rates. The paper's core contribution—demonstrating that activation steering systematically compromises safety even with random or benign vectors—is genuinely novel and well-supported, but the coefficient selection, missing distributional data, and absence of a limitations discussion or defense proposal prevent it from reaching the 7.0+ range.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>