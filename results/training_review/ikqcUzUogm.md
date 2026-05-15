Here is the consolidated final review.

---

## Summary

This paper introduces a benchmark (named BIND in the abstract, RULES in the body) for programmatically evaluating rule-following behavior in LLMs. It comprises 15 text scenarios with explicit rules (e.g., "do not reveal the secret key"), each paired with a concise evaluation program using regex/string matching that can automatically detect violations. Through red-teaming, the authors identify six attack strategy categories and construct a systematic test suite of 862 hand-crafted test cases. Evaluating 13+ proprietary and open models, they find that all models struggle substantially (GPT-4 passes only 73.9%, Llama2-7B only 26.1%), and adversarial suffix optimization drives pass rates to near zero. The core contribution is a scalable, reproducible, human-free evaluation framework for a capability that is distinct from standard instruction-following.

---

## Strengths

- **Scalable programmatic evaluation.** The paper designs 15 scenarios where rule violations can be detected by concise programs using string comparison and regex — "only a few lines of code" (Section 2.3). This enables reproducible, low-cost evaluation without human annotation, directly addressing a key bottleneck in safety evaluation.

- **Systematic taxonomy of attack strategies.** Through extensive red-teaming, the paper distills six distinct categories of attack strategies (Just Ask, Indirection, Legalese, Obfuscation, Rule Change, Simulation) and constructs a targeted test suite of 862 hand-crafted test cases implementing these strategies across all rules (Section 3.3). This structured decomposition goes beyond ad-hoc jailbreaking prompts and provides a reusable resource.

- **Demonstrates broad, severe failures across all models.** The evaluation shows that even the best model (GPT-4) fails 26.1% of test cases, while open models like Llama2-7B fail 73.9% (Figure 2). The gap between proprietary and open models is large but neither is close to reliable. This provides a clear empirical baseline for the community.

- **Adversarially optimized attacks drive performance to zero.** GCG suffixes optimized on 7B models reliably drive pass rates to 0% across multiple scenarios (Table 5), confirming the benchmark's vulnerability to automatic attacks and raising the bar for what a defense must address.

- **Conceptual distinction between rule-following and instruction-following.** Section 4 argues that rule-following is a distinct capability, supported by observed failure modes such as models reaffirming their commitment to rules while inadvertently disclosing secrets. This frames the benchmark as addressing a problem different from standard instruction-following evaluations.

---

## Weaknesses

### Fatal

None.

### Major

- **Evaluation programs lack human validation.** The entire benchmark's pass/fail labels depend on regex and string-matching programs that the authors acknowledge are "more permissive" for negative rules and "more rigorous" for affirmative rules, and "unable to exactly reproduce human judgment in edge cases" (Section 2.3). The claim that "the vast majority of rule-breaking outputs from models are unambiguous" is asserted without supporting evidence. Without a human-annotation study on a random sample of model responses to quantify false-positive and false-negative rates, the numerical pass/fail rates — and any model ranking derived from them — have unknown validity. This limitation affects all experiments (manual test suite, systematic test suite, error detection, and adversarial suffixes).

### Minor

- **Error detection experiment's interpretation is contingent on program quality.** Section 3.5 evaluates whether models can detect rule violations using the evaluation programs' own labels as ground truth. This is not "circular" (it validly tests whether models can replicate the programmatic evaluation), but the reported accuracy/precision/recall/F1 numbers are only as reliable as the programs themselves. Without human validation of the programs, it is unclear whether poor detection performance reflects genuine model limitations or noise from program errors. This experiment would be strengthened by human-annotated ground truth on a subset.

- **Attack strategy coverage is limited to the authors' own red-teaming.** The six strategy categories are derived from a retrospective analysis of the authors' own successful red-teaming attempts (Section 3.3). The paper does not demonstrate that this set spans the space of plausible attacks or benchmark the difficulty against third-party test suites. While this is acknowledged implicitly, it limits confidence that passing the test suite implies robust rule-following in deployment.

- **Naming inconsistency between abstract and body.** The abstract introduces the benchmark as **BIND** (Benchmark for Identifying Non-compliant Decisions), while the introduction (Section 1) and remainder of the paper refer to it as **RULES** (Rule-following Language Evaluation Scenarios). This appears to be an incomplete revision and should be harmonized.

### Trivial

- **GCG experiment is limited and the language is appropriately cautious, but still narrow.** The adversarial suffix experiments test only 7B models on one strategy ("Just Ask") and the claim that transferability was not found is appropriately qualified ("we did not find any evidence"). This is acceptable as a proof-of-concept, though future work should test larger models and more strategies.

---

## Nice-to-Haves

- A human validation study on a random sample of 200–400 model responses (across scenarios and models) to quantify agreement between programmatic and human judgments would strengthen confidence in the results.
- Characterizing false-positive/false-negative patterns per rule type (negative vs. affirmative) would help users calibrate their interpretation of the reported pass rates.
- The variance estimation (10 repetitions, 39 test cases per subset, Section 3.4) is reasonable for standard deviation estimation but could be more precise with more repetitions; this is a minor methodological point that does not affect the paper's conclusions.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Error detection experiment is circular"** — Removed as a mischaracterization. The experiment uses the programmatic labels as ground truth to test whether models can replicate the program's judgment. This is a coherent experimental design (not circular); the valid concern is about program quality, which is already captured in the Major weakness above.
- **"Transferability claim stronger than evidence warrants"** — Removed as inaccurate. The paper's actual language is carefully hedged ("we did not find any evidence of the transferability"), not claiming absence of transferability.
- **"Re-sampling dismissed as unrealistic"** — Removed. The paper is acknowledging its own limitation; this is not a weakness but appropriate self-awareness.
- **"Small sample for variance estimation"** — Moved to Nice-to-Haves. Ten repetitions for standard deviation estimation of pass/fail outcomes across 39 test cases is within normal practice for this type of evaluation.

---

## Novel Insights

None beyond the paper's own contributions. The key insight — that programmatic evaluation of rule-following is both feasible (because rules are simple enough to check with regex/string matching) and revealing (showing catastrophic failures across all models) — is the paper's own contribution, not an emergent pattern from the reviews.

---

## Suggestions

1. **Harmonize the benchmark name** (BIND vs. RULES) throughout the paper. Choose one and use it consistently.
2. **Conduct a human validation study** on a random sample of model responses to quantify the accuracy of the evaluation programs. Even a modest study (200–400 samples) would substantially increase confidence in the reported results.
3. **Acknowledge the attack strategy coverage limitation more explicitly** in the main text, and position the test suite as a "challenging sample" rather than a comprehensive coverage of the attack space.
4. **For the error detection experiment**, add a small human-annotated subset to calibrate the programmatic labels, or at minimum discuss how unknown program error rates affect the detection results.
5. **Expand the GCG experiments** to at least one larger open model (e.g., Llama2-13B or 70B) to strengthen the transferability analysis.

---

## Score and Decision

**Evaluation by axis:**
- **Originality:** Good. The programmatic rule-following benchmark with categorized attack strategies is a novel contribution.
- **Importance of research question:** High. Reliable rule-following is critical for safe LLM deployment.
- **Claims well-supported:** Partially. The main claims (models fail substantially) are supported, but the lack of program validation weakens confidence in the exact numbers.
- **Soundness of experiments:** Adequate but with one significant gap (program validation).
- **Clarity:** Good, aside from the BIND/RULES naming inconsistency.
- **Value to community:** High. The benchmark, test cases, and code will be useful resources.

The core contribution — a clean, scalable benchmark for evaluating rule-following — is valuable and the empirical results convincingly show that all current models perform poorly. The most significant weakness (unvalidated evaluation programs) is addressable in follow-up work / revision but weighs against full acceptance in the current form. This is a solid paper with a real but non-fatal limitation.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>