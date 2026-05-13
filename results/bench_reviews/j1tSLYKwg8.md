Now let me run calibration search and verify key reviewer claims simultaneously.Now I have enough information to write the comprehensive final review.

---

## Summary

This paper proposes adapting pre-trained autoregressive (AR) language models into discrete diffusion language models (DLMs) via continual pre-training, addressing the challenge that DLMs have historically been trained at smaller scale than AR models. The two key technical components are (1) attention mask annealing, which gradually transitions causal to full bidirectional attention, and (2) a shift operation that preserves the AR-style token-prediction alignment during diffusion fine-tuning. Using these techniques, the authors convert GPT2 (127M/355M) into DiffuGPT using ~30B FineWeb tokens, and LLaMA2-7B into DiffuLLaMA using ~65B tokens, releasing all models and training code.

---

## Strengths

- **First 7B-scale DLM with comprehensive evaluation:** DiffuLLaMA at 7B parameters substantially extends prior DLM work (SEDD, PLAID capped at ~1B). The paper evaluates across commonsense reasoning, math, code infilling, story infilling, and zero/few-shot tasks—significantly more breadth than previous DLM papers that relied primarily on perplexity. This evaluation framework is itself a useful community contribution.

- **Ablation-validated adaptation recipe (Table 3):** The GSM8K-symbolic ablation concretely validates each component. Removing the shift operation degrades performance, and the comparison of direct DD fine-tuning vs. adaptation-then-fine-tune (50.2/61.8 for DiffuGPT-S/M vs. 45.4/49.7 for direct DD) demonstrates that a well-adapted base DLM provides a stronger foundation. This is direct experimental evidence supporting the recipe's value.

- **Evidence of in-context learning in a 7B DLM (Table 2):** DiffuLLaMA's zero-shot→few-shot improvement on TriviaQA (0→15.8), MAWPS (25.7→34.0), and SATMATH (8.3→16.7) provides the first large-scale evidence that DLMs can leverage in-context demonstrations, a capability previously untested at this scale.

- **Practical mathematical unification (Section 3.2):** The paper precisely identifies that the AR cross-entropy and the discrete diffusion ELBO differ only by a reweighting term (1/t) and the masked-token indicator δ, providing a principled—rather than heuristic—justification for why AR→diffusion adaptation is feasible. While the underlying equivalence is known from prior work, its use here as a concrete engineering bridge between AR and DLM objectives is legitimate.

- **Model and code release:** Releasing DiffuGPT (127M, 355M) and DiffuLLaMA (7B) with training and evaluation code is a substantive community contribution that other DLM researchers can build directly upon.

---

## Weaknesses

### Fatal
None.

### Major

- **Data quality confound undermines the headline "DiffuGPT outperforms GPT2" claim.** DiffuGPT is initialized from GPT2 and then trained on 30B tokens from FineWeb—an explicitly higher-quality corpus than the OpenWebText data used for GPT2's original training. The paper itself notes this is "an improved corpus than OpenWebText used in prior DLMs." Without a baseline GPT2 model continual pre-trained on FineWeb under the *autoregressive* objective (GPT2-FT-AR), one cannot determine whether the performance gains on HellaSwag (+1.3/+2.0), Winogrande (+1.8/+3.0), and SIQA (+1.8/+0.7) stem from the diffusion adaptation or from the better data. This concern is especially sharp because the paper lists "DiffuGPT outperforms GPT2 in most tasks" as a bullet-point contribution in the abstract and introduction. Note that DiffuGPT still clearly outperforms SEDD (a properly controlled DLM comparison) and the adaptation recipe's internal ablations are valid—but the specific claim of superiority over the AR base model is confounded. A closely related paper on scaling masked diffusion models (reviewed at similar venues) faced exactly the same criticism and addressed it with an additional disentangling experiment.

- **Infilling superiority claim is not validly established.** Section 4.2 and Table 1 include ROCStories (+18.7/+15.9 ROUGE-L) and HumanEval code infilling comparisons that are then used to argue DLMs "demonstrate their strengths in infilling tasks." However, the paper explicitly states: "we do not provide the suffix information to [the AR] model, which might result in an unfair comparison." Depriving the AR baseline of suffix context while giving the diffusion model full bidirectional access renders this comparison uninformative. Fill-in-the-middle (FIM) pretrained AR models (e.g., models using the FIM objective) are the appropriate baseline, and none are evaluated. The honest phrasing should be that DLMs *naturally support* infilling without special FIM training—not that they *outperform* AR models at infilling.

### Minor

- **DiffuLLaMA omits attention mask annealing without sufficient justification.** Section 4.1 states: "we directly use bi-directional attention without attention mask annealing" for the 7B model, citing flash-attention 2 implementation convenience. The paper argues "mask annealing has minimal impact" based on the small-scale (127M/355M) ablation in Table 3, but this extrapolation to 7B is untested. Since attention mask annealing is one of only two core technical contributions, skipping it for the flagship model—without even a brief experiment or analysis—leaves the contribution's relevance at scale unvalidated.

- **Multiple-choice scoring via diffusion ELBO is non-standard and unvalidated.** For HellaSwag, Winogrande, SIQA, and PIQA—four of the six main benchmark tasks—the paper selects answers by choosing the candidate with minimum diffusion ELBO loss (averaged by token length). The ELBO is an upper bound on NLL, and it is unclear whether this upper bound reliably ranks candidates the same way exact likelihood scoring would. No calibration or validation of this scoring method against AR likelihood scoring on the same items is provided. This concern affects a large fraction of Table 1 results.

- **CoT underperformance is attributed away without analysis.** Table 2 shows CoT hurts DiffuLLaMA, attributed to "absence of instruction tuning." But AR base models without instruction tuning typically *do* benefit from CoT examples, making this explanation insufficient. This is an interesting and potentially fundamental signal about DLM reasoning behavior that deserves analysis rather than attribution.

### Trivial

- **Inference speed comparison at batch size 1 only (Figure 3):** The speed advantage of DiffuLLaMA is demonstrated only for 1024-token generation with T=256 steps at batch size 1. At higher batch sizes, AR KV-cache efficiency improves substantially. The crossover point also depends on sequence length and T values. The current comparison shows a scenario favorable to diffusion but does not present the full speed-quality-length tradeoff picture.

---

## Nice-to-Haves

- A GPT2 continual pre-trained on FineWeb under the AR objective (GPT2-FT-AR) would cleanly resolve the data confound and strengthen or qualify the paper's headline claim.
- A FIM-trained AR baseline (or a proper comparison against code models that support fill-in-the-middle) for the infilling tasks would put the infilling comparisons on sound footing.
- Further analysis of why CoT hurts DiffuLLaMA—e.g., testing whether the issue is specific to step-by-step chain reasoning vs. format following—could yield interesting insights about fundamental AR vs. DLM behavioral differences.
- Speed-quality tradeoffs reported across varying sequence lengths and T values to characterize the diffusion vs. AR efficiency regime more completely.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **[Harsh Critic] "Section 3.2 overrepresents mathematical novelty"**: The paper explicitly cites Austin et al. (2021) and Hoogeboom et al. (2022) for the objective equivalence and states "As discussed in Austin et al. (2021), the loss objective of this diffusion process is equivalent to standard cross-entropy." The paper is honest about what is novel (the practical framing as a bridge for adaptation) vs. prior work. This is not an overstatement. **Removed as strawman.**

- **[Harsh Critic] Flash-attention 2 doesn't require full attention as an excuse**: The paper says it uses full bidirectional attention "for efficient implementation" with flash-attention 2, not that it *cannot* do custom masking. The reason given is implementation simplicity. This is an acceptable engineering decision even if not ideal. **Removed as minor nitpick conflated with a real point, which is kept under Minor.**

- **[Strength Finder] "Theoretical unification of AR and diffusion objectives"** as a standalone strength: While the equations in Section 3.2 are correct and useful, the mathematical equivalence itself is not new—the paper's own text credits Austin et al. (2021). The genuine contribution is the practical engineering bridge, which is captured in the ablation-validated recipe strength. **Removed as an overstated standalone strength; merged into the practical unification strength above.**

- **[Strength Finder] "Competitive inference speed for long sequences"**: This is only shown at batch size 1, T=256, length 1024—a configuration favorable to diffusion. As noted in the minor weaknesses, the speed advantage is not shown to generalize robustly. **Removed as strength conflicting with a verified weakness.**

---

## Novel Insights

The most genuinely interesting finding is the CoT performance drop in DiffuLLaMA. While the paper attributes it to missing instruction tuning, the fact that AR base models typically benefit from CoT examples even without instruction tuning suggests something more fundamental: bidirectional diffusion models may process extended reasoning chains differently than left-to-right models, possibly because the iterative denoising objective is not well-aligned with the sequential, step-dependent structure of CoT reasoning. Investigating whether this is architectural (bidirectionality disrupting logical dependency chains), training-data (DLMs seeing text without directional reasoning supervision), or a decoding artifact would substantially advance understanding of DLMs' reasoning capabilities and limitations. The hit-rate @3 results in Table 2 also suggest high uncertainty in DiffuLLaMA outputs, pointing toward a role for diversity-based decoding or self-consistency as a key lever for this model class.

---

## Suggestions

1. **Add a GPT2-FT-AR baseline**: Train GPT2 on the same 30B FineWeb tokens under the AR objective and include it in Table 1. This single experiment would resolve the main confound and either strengthen the DiffuGPT story or appropriately recalibrate expectations.
2. **Reframe infilling results honestly**: Rather than claiming superiority over AR models at infilling, frame the result as DLMs natively supporting infilling without requiring FIM-style retraining. Acknowledge that a fair comparison requires an AR+FIM baseline.
3. **Validate ELBO-based multiple-choice scoring**: Include a sanity check comparing ELBO-based ranking vs. AR teacher scoring on a sample of MCQ items, or cite prior work that validates this protocol.
4. **Analyze CoT failure more deeply**: At minimum, compare DiffuLLaMA with CoT against a same-scale AR base model (no instruction tuning) with CoT to test whether the failure is diffusion-specific.

---

## Score and Decision

**Anchor Comparison:**

| Path | Avg Human Score | Comparison to paper under review |
|---|---|---|
| `tyEyYT267x.md` | 8.0 (Accept) | Stronger: cleaner novel methodology (gradient variance, data-driven noise schedules), sets new SOTA LM PPL; our paper has more practical scale but weaker theoretical rigor |
| `WNvvwK0tut.md` | 6.5 (Accept) | Comparable: also scales a DLM family and evaluates vs. ARMs; faces the same "disentangle masking vs. diffusion" confound (addressed in rebuttal); establishes scaling laws which our paper does not |
| `sL2F9YCMXf.md` | 6.75 (Accept) | Comparable scope (energy-based improvements to discrete DLMs, ~similar benchmark suite); stronger methodological novelty in EBM formulation |
| `71mqtQdKB9.md` | 6.6 (Reject) | Comparable: SEDD proposes a novel discrete diffusion loss; stronger theoretical contribution but at smaller scale; our paper is at larger scale with weaker theory |
| `Qn4HEhezKW.md` | 5.0 (Reject) | Very close analogue: also adapts pre-trained LMs to DLMs via scaling, criticized for lacking methodological novelty and confounding pre-training quality with diffusion gains; our paper is better (larger scale, causal LM adaptation, more comprehensive eval) |
| `1pTlvxIfuV.md` | 5.5 (Reject) | Reparameterized discrete diffusion for text; stronger single methodological contribution (reparameterization); our paper broader scope |
| `PvvQlhBbgu.md` | 4.0 (Reject) | Below our paper: work on continual diffusion model learning with weaker novelty and contributions |
| `IeZpJNc3uy.md` | 3.5 (Reject) | Well below: symbolic music model updating with limited scope and novelty |

**Calibrated Score:** The paper sits between `Qn4HEhezKW.md` (5.0, reject) and `WNvvwK0tut.md` (6.5, accept). The paper under review is clearly stronger than the 5.0 anchor: it addresses the harder problem of adapting causal LMs (not encoder-only MLMs), achieves genuinely novel scale (7B DLM), and releases models used by the community. However, the unresolved data confound for the headline DiffuGPT claim and the infilling comparison weakness keep it below the 6.5 anchor (which addressed its analogous confound in rebuttal). Evaluating on the six criteria: originality (moderate—building on known equivalence with two practical techniques), importance (high—scaling DLMs is a key open problem), claim support (partially—DLM vs. DLM comparisons are fair, but DLM vs. AR base model comparisons are confounded), experimental soundness (fair—MCQ scoring is non-standard but deployed, infilling baselines are acknowledged as unfair), clarity (good), community value (high—7B model release, comprehensive benchmark, code release). Final score: **5.5**.

**Decision: Borderline Accept** — The practical contribution of a released 7B DLM with a clear adaptation recipe and comprehensive evaluation is real and valued by the community. The data confound does not invalidate the recipe or the DLM-vs-DLM comparisons; it mainly affects one headline claim that the paper could reframe more carefully.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>