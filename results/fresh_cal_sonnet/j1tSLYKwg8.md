Now let me run the calibration search for bracketing.Let me read the most relevant calibration paper (the AR/diffusion paper at score 8.0):Now let me do the narrowing calibration search:Let me read the two most relevant anchors in full:Now I have sufficient information to write the final review. Let me compile my analysis.Now I have everything I need to write the final consolidated review.

---

## Summary

This paper proposes a practical recipe for converting pre-trained autoregressive (AR) language models—GPT2 (127M–355M) and LLaMA2 (7B)—into discrete diffusion language models (DLMs) via continual pre-training. The two main adaptation components are (1) **attention mask annealing** (gradually transitioning from causal to full bidirectional attention) and (2) a **shift operation** inherited from the AR model (aligning diffusion output logits to predict the next position, avoiding initialization misalignment). The resulting DiffuGPT and DiffuLLaMA models achieve new state-of-the-art performance among DLMs, scale diffusion language modeling to 7B parameters for the first time, and introduce a comprehensive multi-task benchmark for evaluating DLMs beyond perplexity.

---

## Strengths

1. **First 7B discrete diffusion language model (Table 1, §4.1).** DiffuLLaMA is the first DLM demonstrated at 7B parameters, setting new DLM-vs-DLM state-of-the-art results across HellaSwag (70.3%), Winogrande (69.4%), GSM8K (55.4%), and LAMBADA (74.4%). No prior DLM has operated at this parameter count. This is the strongest and best-supported contribution.

2. **Novel and well-motivated shift operation (§3.3, Figure 1).** The insight that AR model logits are already aligned to predict the *next* token (position *n* → target *n+1*) and that naively discarding this alignment when switching to a diffusion objective causes a severe initialization mismatch is concrete and non-trivial. Maintaining the shift and adjusting the loss accordingly (Algorithm 1, line for loss computation) is a practical, well-reasoned solution. Ablation confirms it: removing the shift drops GSM8K-symbolic accuracy from 45.4% to 37.8% (GPT2-small) and 49.7% to 44.0% (GPT2-medium) (§4.4, Table 3).

3. **Comprehensive evaluation beyond perplexity (§4.2).** The authors introduce a multi-task benchmark spanning reading comprehension (TriviaQA, LAMBADA), commonsense reasoning (HellaSwag, Winogrande, SIQA, PIQA), math (GSM8K), story infilling (ROCStories ROUGE), and code infilling (HumanEval). This reveals capability differences invisible to perplexity-only evaluation—e.g., Plaid 1B scores well on unconditional generation perplexity but poorly on conditional tasks (§4.3, Figure 3). This benchmark design is a genuine contribution to the DLM evaluation literature.

4. **In-context learning demonstrated in a 7B DLM (§4.3, Table 2).** DiffuLLaMA shows zero-shot to few-shot improvements on MAWPS (32.7% → 47.8%) and benefits from self-consistency on GSM8K (24.0% → 36.5%), demonstrating that the adapted model retains the base AR model's in-context learning ability—a capability not previously demonstrated in DLMs of this scale.

5. **Competitive or faster inference speed for long sequences (§4.4, Figure 4).** With T=256 decoding steps and FlashAttention-2, DiffuLLaMA is faster than LLaMA2 for generating sequences of length ≥1024 tokens, validating the practical viability of the approach.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing AR-continued-pretraining control — undermines the "DiffuGPT outperforms GPT2" claim (§4.1, §4.2, Table 1, Abstract).** DiffuGPT is initialized from GPT2 and then trained on 30B tokens of FineWeb, which the paper itself describes as "an improved corpus than OpenWebText used in prior DLMs" (§4.1). The original GPT2 was trained on WebText. The abstract claims "DiffuGPT outperforms GPT2 in most tasks," but no ablation baseline exists for *GPT2 continued on the same 30B FineWeb tokens under a standard AR objective*. Without this control, the observed gains could be attributable to the additional high-quality training data rather than the diffusion adaptation. The same gap applies to DiffuLLaMA (65B new tokens vs. LLaMA2's 2T, different mix including Starcoder). This does **not** invalidate the paper's DLM-vs-DLM contributions, where the evidence is strong, but it means the comparative claim versus AR baselines is under-supported. Reframing the DiffuGPT-vs-GPT2 comparison—or adding this control—would significantly strengthen the paper's central thesis.

### Minor

- **Ablation (Table 3) is conducted on GSM8K fine-tuning only, not the main evaluation suite (§4.4).** The paper acknowledges this is due to cost. The GSM8K fine-tuning proxy is reasonable but narrow. Critically, DiffuLLaMA—the paper's largest and most prominent model—omits attention mask annealing entirely (§4.1: "we directly use bi-directional attention without attention mask annealing"), and the ablation was not conducted on the 7B setting at all. The paper does state "The mask annealing has minimal impact" (§4.4), which makes this consistent, but it reduces diagnostic value.

- **Evaluator independence in unconditional generation quality (§4.3, Figure 3).** GPT2-large is used to measure perplexity of DiffuGPT's unconditional generations, following prior work (SEDD). Since DiffuGPT is adapted from GPT2 and shares its tokenizer and training distribution, GPT2-large may systematically score DiffuGPT outputs more favorably than those of SEDD or MD4. The "consistent with prior work" justification is valid, but a note acknowledging this potential evaluator bias would be appropriate.

### Trivial

- **Speed comparison at a single favorable T (§4.4, Figure 4).** The inference speed comparison is presented only for T=256, which is where DiffuLLaMA overtakes LLaMA2. The paper acknowledges the quality–speed tradeoff, but showing the quality at T=256 vs. T=full alongside the speed comparison would make the result more complete. Also, single-batch latency (batch size 1) is shown, while throughput (batch size > 1) might differ due to DLMs' lack of KV caching.

---

## Nice-to-Haves

- A continued AR baseline (GPT2/LLaMA2 trained on the same token budget and data as DiffuGPT/DiffuLLaMA) would resolve the major weakness above and allow clean attribution of performance gains to the diffusion objective vs. improved data.
- Extending the ablation study to at least one commonsense task or LAMBADA from the main eval suite would give the adaptation recipe more diagnostic value beyond the GSM8K proxy.
- A throughput comparison (sequences/second at batch size > 1) would complement the single-batch latency figure and be more informative for practitioners.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Theoretical unification restates known equivalences without new contribution"** (Harsh Critic, §3.2): The paper correctly cites Austin et al. (2021) and Hoogeboom et al. (2022) for the AR-as-special-case-of-diffusion result. The paper is entirely transparent about this derivation being motivational background for adaptation, not a new theoretical result. This is not a weakness.

- **"DiffuLLaMA vs. LLaMA2 performance gap is under-examined"** (Harsh Critic): The paper explicitly states "DiffuLLaMA's performance still falls short of the LLaMA2 model" (§4.2) and attributes this to fewer training tokens (65B vs. 2T). This is honest and consistent with expected scaling behavior. Not a weakness.

- **"ELBO upper bound may introduce systematic error in multiple-choice evaluation"** (Harsh Critic): This is a generic speculative concern without evidence that the bias favors the authors' method. The ELBO-as-scoring methodology is standard across all DLMs evaluated in the same table, so any bias applies uniformly. Removed.

- **"Data mix difference between DiffuLLaMA (SlimPajama + Starcoder) and LLaMA2"** (Harsh Critic, §4.1): The paper acknowledges that LLaMA2 was not trained for fill-in-the-middle and handles this comparison honestly. The Starcoder inclusion is relevant and transparent. Not a methodological flaw.

- **"Sequence packing interaction with diffusion objective deserves justification"** (Harsh Critic): This is a very minor implementation detail. Sequence packing with the diffusion loss is straightforward (per-sequence masking schedules), and requesting a paragraph-level justification for it is a nitpick.

- **"Missing statistical significance tests / variance reporting"** (Harsh Critic): Single-run evaluation without confidence intervals is standard practice in LLM benchmarking at this scale. This is a nice-to-have at best.

- **Strength: "DiffuGPT outperforms GPT2 on 11/12 tasks"** (Strength Finder): Kept as a strength in the paper's own terms, but appropriately caveated given the missing AR-continued-pretraining control. The DLM-vs-DLM version of this strength (DiffuGPT beats all prior DLMs) is better supported and more prominently noted.

---

## Novel Insights

The paper's most transferable insight is the **shift operation**: when initializing a diffusion model from an AR checkpoint, the model's weights already encode the implicit assumption that position *n* predicts position *n+1*. Any deviation from this alignment at the loss level introduces a systematic gradient mismatch that slows adaptation. The solution—maintaining the shift during diffusion training and computing the loss against the next position—is simple and well-motivated, and the ablation confirms its impact. This principle may generalize to any scenario where a trained autoregressive model is adapted to a non-autoregressive or masked prediction objective, regardless of whether the target is a diffusion model.

The paper also surfaces a useful empirical finding: continuous diffusion models (Plaid 1B) and discrete diffusion models (SEDD, DiffuGPT) occupy different capability profiles. Continuous models excel at unconditional generation perplexity but struggle with conditional tasks; discrete models handle conditional tasks well but may lag on unconditional generation. The distinction matters for practitioners choosing between DLM variants.

---

## Suggestions

1. **Add an AR-continued-pretraining baseline** (GPT2 → continued on 30B FineWeb tokens with standard cross-entropy) evaluated on the same Table 1 benchmark suite. If DiffuGPT still outperforms even this baseline, the diffusion adaptation claim is decisively supported. If not, reframe the contribution as "most data-efficient path to a capable DLM from AR initialization" rather than "DLM outperforms AR."
2. **Include ablation results on at least one non-GSM8K task** (e.g., HellaSwag or LAMBADA) to show that the shift operation's benefit generalizes beyond fine-tuning on symbolic math data.
3. **Acknowledge evaluator overlap in Figure 3** and add a note that GPT2-large may not be fully independent for DiffuGPT generation quality measurement.

---

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison to paper under review |
|---|---|---|---|
| `kCnLHHtk1y.md` | 3.0 | R1 (low) | Irrelevant (Chinese building image diffusion) |
| `kKXIYUi8ff.md` | 3.0 | R1 (low) | Irrelevant (molecular dynamics diffusion) |
| `mz8owj4DXu.md` | 6.5 | R1 (mid) | Continual learning LMs — same general area but different problem |
| `F5PlYMC5ik.md` | 7.0 | R1 (mid) | Lifelong learning LMs — different problem |
| `8uXkyWFVum.md` | 4.2 | R1 (mid) | Pre-training/fine-tuning analysis — weaker contribution |
| `tyEyYT267x.md` | 8.0 | R1 (high) | SAR diffusion with stronger theory and SOTA perplexity — paper under review is similar in topic but weaker in theory and missing key ablation |
| `jOmk0uS1hl.md` | 8.0 | R1 (high) | Training on test task — unrelated |
| `Qn4HEhezKW.md` | 5.0 | R2 | Scaling DLMs from MLMs (XLM-R) — similar concept but: no novel methodology, smaller scale, less thorough eval; clearly weaker than paper under review |
| `71mqtQdKB9.md` | 6.6 | R2 | SEDD (used as a baseline in paper under review!): proposes novel score entropy loss, but limited scale, weaker evaluation; paper under review is more comprehensive |
| `WNvvwK0tut.md` | 6.5 | R2 | Scaling MDMs to 1.1B with scaling laws — similar in scope, accepted; paper under review achieves larger scale (7B), adapts AR models (harder problem), but has missing baseline |
| `NRYgUzSPZz.md` | 6.25 | R2 | Discrete diffusion for reasoning — narrower scope than paper under review |
| `90Db4RUBc7.md` | 6.75 | R2 | Cross-architecture distillation to linear models — different architecture, comparable complexity |

**Round 1 bracket: 5–8.**

**Round 2 narrowing:** The most directly comparable anchors are Qn4HEhezKW (5.0, rejected), WNvvwK0tut (6.5, accepted), 71mqtQdKB9 (6.6, rejected), and tyEyYT267x (8.0, accepted).

The paper under review is **clearly better than Qn4HEhezKW (5.0)**: it introduces a specific novel methodology (shift operation + mask annealing for AR-to-DLM adaptation, not just applying an existing recipe), operates at dramatically larger scale (7B vs. encoder-only XLM-R), includes ICL demonstrations, and has a far more comprehensive evaluation suite.

The paper under review is **comparable to or slightly better than WNvvwK0tut (6.5)**: both scale DLMs beyond prior work, both are empirically-driven with modest theoretical novelty. Paper under review has a more innovative starting point (adapting AR LLMs rather than scaling MDMs from scratch) and reaches 7B, but WNvvwK0tut provides scaling laws (more quantitative).

The paper under review is **below tyEyYT267x (8.0)**: the SAR paper has stronger theory (NELBO tightness), cleaner experimental design, and SOTA on benchmarks without a missing control baseline.

The paper sits comfortably above WNvvwK0tut/71mqtQdKB9 (~6.5) and below tyEyYT267x (8.0). The 7B scale is genuinely new, the shift operation is a non-trivial contribution, and the comprehensive evaluation is a service to the field. The missing AR-continued-pretraining baseline is a real gap but does not invalidate the DLM-vs-DLM contributions. **Score: 7.0. Decision: Accept.**

**Axis ratings (qualitative):**
- *Originality*: Moderate-to-high. Adapting AR LLMs (not just MLMs) to diffusion via the shift operation + mask annealing is a specific and non-obvious contribution.
- *Importance of research question*: High. Scaling DLMs to LLM-class sizes is a central open problem.
- *Claims well-supported*: Partially. DLM-vs-DLM claims are well-supported; DiffuGPT-vs-GPT2 claims are not fully isolated from data quality confounds.
- *Soundness of experiments*: Good overall. The ablation scope is limited but sufficient for the core claims.
- *Clarity of writing*: Good. Paper is well-structured and the adaptation components are clearly explained.
- *Value to research community*: High. Open-sourced 7B DLM, evaluation toolkit, and adaptation code are significant resources.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>