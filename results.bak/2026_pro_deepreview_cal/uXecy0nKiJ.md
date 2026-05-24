Now I have enough calibration data. Let me synthesize.

**Round 1 Bracketing:**
- Weak anchor (3.00): `z1yI8uoVU3` — limited contribution, vague experiments, only 8B models
- Middle anchor (5.00): `2XBPdPIcFK` (ActAdd) — novel idea but inconsistent baselines, outdated models, presentation issues
- Strong anchor (9.50): `6Mxhg9PtDE` (Shallow Safety) — comprehensive diagnosis + mitigation strategies, excellent execution

**Initial bracket:** 6.0–8.0

**Round 2 Narrowing:**
- `aSy2nYwiZ2` (6.67, JailbreakEdit) — white-box only, threat model issues, less systematic
- `hXA8wqRdyV` (6.14, Adaptive Attacks) — limited novelty, organizational issues
- `Oi47wc10sm` (7.33, CAST) — excellent execution but only ≤8B models, narrower scope

The Rogue Scalpel is clearly above the 6.14–6.67 range (more systematic, broader models, real-world case study), comparable to CAST (7.33) but with broader model coverage (3B–70B vs ≤8B) and a more striking finding. I settle at **7.5**.

---

## Summary
This paper investigates whether activation steering—a technique for controlling LLM behavior by injecting direction vectors into hidden states—can inadvertently compromise safety alignment. Through extensive experiments across multiple model families (Llama3, Qwen2.5, Falcon3 at 3B–70B scales), the authors demonstrate that (1) even random-direction steering systematically breaks refusal mechanisms, (2) SAE-based steering with benign, interpretable features is comparably dangerous, and (3) averaging just 20 random vectors that jailbreak a single prompt creates a universal attack vector that generalizes to unseen harmful prompts. A case study using the public Goodfire API confirms practical exploitability.

## Strengths
- **Comprehensive empirical demonstration that random-direction steering reliably bypasses alignment safeguards.** The paper conducts systematic sweeps across model families, intervention depths, and steering coefficients (Sec. 4.1, Fig. 2), showing that completely random, unoptimized vectors increase harmful compliance from 0% to 2–27%. On the full JailbreakBench (100 prompts, 10 categories), overall compliance reaches 17% for Llama3-8B and 10% for Qwen2.5-7B (Fig. 3). This goes substantially beyond prior work on intentionally adversarial vectors.
- **Convincing evidence that SAE-based steering is as dangerous as random vectors, with benign features acting as effective jailbreaks.** Under identical conditions, SAE feature steering yields compliance rates comparable to random directions (Fig. 2c) and an overall 10% rate on Llama3.1-8B (Fig. 3). The most potent SAE features correspond to innocuous concepts ("brand identity," "physical positioning") and show poor cross-prompt generalization (Fig. 4), challenging the assumption that interpretability ensures safe control.
- **Novel construction of universal attack vectors from a handful of random vectors.** Averaging 20 randomly sampled vectors that each jailbreak a single bomb-making prompt produces a universal steering vector that boosts compliance by up to 4× over raw random steering (e.g., Falcon3-7B: 5.7% → 63.4%, Llama3-70B: 22.2% → 50.4%; Fig. 6), without requiring model weights, gradients, or per-prompt optimization. This is a concrete, low-effort attack construction.
- **Rigorous evaluation protocol with clean baseline.** The paper uses JailbreakBench categories, an LLM-as-judge (Qwen3-8B in reasoning mode) with a rubric that classifies incoherent outputs as SAFE, and confirms 0% baseline compliance for all unsteered models (Sec. 3.4, Fig. 3). The real-world case study via the Goodfire API (Sec. 4.3) demonstrates disclaimer-then-compliance and fictional-framing failure modes, grounding the findings in practical deployment settings.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **The claim that systematic safety monitoring is "practically infeasible" is overstated (Sec. 4.2, Fig. 4b discussion).** The paper argues that poor cross-prompt generalization of dangerous SAE features means "comprehensively screening for dangerous features would require exhaustive testing against a vast and ever-growing set of harmful prompts—a practically infeasible task." However, a developer could test candidate features on a fixed set like JailbreakBench (100 prompts) and detect features that break many prompts (e.g., the 49-prompt-breaking feature). The real limitation is that passing such a test does not *guarantee* safety on unseen prompts, not that testing itself is infeasible. The core observation (poor generalization makes safety guarantees difficult) is valid; the word "infeasible" should be tempered.
- **The universal attack is described as having "black-box access" (line 245), overstating the ease of weaponization.** The paper correctly states the requirements in the same paragraph: "only the ability to perform activation steering and observe model outputs" (line 243). However, calling this "black-box access" in the concluding sentence of Section 4.4 is misleading—standard definitions of black-box access do not include the ability to inject vectors into hidden states. The abstract and framing should consistently reflect that steering capability (as offered by a public steering API) is required.
- **Layer and coefficient choices for the scaled evaluation (Sec. 4.2) could be better motivated.** The scaled experiments use coefficient 2.0 for Llama3-8B and 1.5 for Qwen2.5-7B at 1/3 depth, but the single-prompt sweep at 1/3 depth (Fig. 2a) shows Llama3-8B peaking near coefficient 1.0 (~4%) and dropping to ~1% at 2.0. The paper would benefit from a brief justification of why these specific coefficients were selected for the full-dataset evaluation, or a note that different prompts have different optimal strengths. The SAE depth (2/3) is constrained by the SAE training layer (layer 19 of 32), which is a reasonable constraint, but this rationale should be made explicit.

### Trivial
None.

## Nice-to-Haves
- The paper notes that Qwen2.5-32B shows no benefit from the universal attack (Fig. 6) but does not analyze why. A brief discussion of what properties make certain models more resistant would enrich the analysis and could inform defensive strategies.
- Reporting the fraction of incoherent outputs at extreme steering coefficients (where compliance drops in Fig. 2) would help distinguish safety-bypass from output degradation.
- A paragraph sketching possible mitigation strategies (clamping activation norms, anomaly detection on steering vectors, adversarial training against perturbations) would make the paper more constructive without requiring new experiments.

## Removed Points
These points are flagged to be removed; treat them with caution:

- **LLM-as-judge validation concern** (Harsh Critic point i): The reviewer noted that Appendix B (quality assessment against human annotations) was not available. Per review protocol, appendix-stripped content is not a valid weakness—the validation exists in the original submission. The paper does reference it ("see Appx. B for prompt details and quality assessment against human annotations"). Removed.
- **"Missing appendix" for mechanism analysis** (Harsh Critic section-by-section notes): The paper references Appendix E for preliminary mechanism analysis. The appendix exists in the original; removed per hard rules.
- **"Steering" vs "perturbing" terminology nitpick** (Harsh Critic section-by-section notes): The reviewer suggested "perturbing" for random case. This is a stylistic preference, not a substantive issue. Removed.
- **Strength Finder generic strength about "important problem"**: The claim that "this paper addressed an important problem" is generic and lacks concrete anchoring. Removed.

## Novel Insights
The review process surfaces an important calibration point: the paper's most significant contribution is not merely that activation steering can jailbreak models (prior work on adversarial vectors already showed this), but that *benign, interpretable, and legitimately-deployed steering vectors*—the kind users apply through public APIs for legitimate control—carry comparable risk. The finding that random noise, SAE features, and aggregated prompt-specific vectors all converge on the same vulnerability suggests this is not a failure of specific vectors but a structural property of how steering interacts with refusal mechanisms. This reframes the safety discussion around activation steering from "watch out for adversarial vectors" to "any steering is potentially dangerous."

## Suggestions
- Temper the "practically infeasible" claim about safety monitoring to reflect that testing on a fixed benchmark is feasible but insufficient to guarantee safety on unseen prompts.
- Replace "black-box access" (line 245) with precise language describing the required capabilities (activation steering + output observation), consistent with the sentence on line 243.
- Add a sentence in Sec. 4.2 explaining why the specific coefficients were chosen for the scaled evaluation, referencing the single-prompt sweep results and noting that optimal strengths vary across prompts.
- Consider a brief paragraph in the conclusion or discussion sketching possible defensive directions.

## Score and Decision

**Anchor comparison summary:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `z1yI8uoVU3` (Measuring Effects of Steered Rep.) | 3.00 | R1 | Paper is substantially stronger in contribution, scope, and execution |
| `2XBPdPIcFK` (ActAdd) | 5.00 | R1 | Paper has cleaner methodology, broader model coverage, and more focused contribution |
| `hXA8wqRdyV` (Adaptive Attacks) | 6.14 | R2 | Paper has more systematic methodology and more novel findings |
| `aSy2nYwiZ2` (JailbreakEdit) | 6.67 | R2 | Paper has broader experiments, clearer threat model, and real-world validation |
| `Oi47wc10sm` (CAST) | 7.33 | R2 | Comparable quality; paper has broader model scale (3B–70B vs ≤8B) and real-world API case study |
| `6Mxhg9PtDE` (Shallow Safety) | 9.50 | R1 | Strong anchor offers both diagnosis and mitigation; paper is primarily diagnostic |

This paper makes a genuine, timely contribution to the safety-interpretability literature. The central finding—that activation steering, even with benign vectors, systematically undermines refusal mechanisms—is demonstrated through broad experiments and supported by a realistic case study. The weaknesses are minor and addressable: overstated monitoring-infeasibility claim, misleading "black-box" terminology for the universal attack, and under-justified coefficient choices in the scaled evaluation. None invalidate the core claims. The paper is original, addresses an important research question, is well-supported by experiments, is clearly written, and offers significant value to the safety and interpretability communities. Score: 7.5.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>