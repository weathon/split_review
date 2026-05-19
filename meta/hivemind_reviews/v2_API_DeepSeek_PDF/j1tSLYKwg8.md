## Summary
# Final Review Report

## Summary

This paper proposes a method to adapt pretrained autoregressive (AR) language models (GPT2, LLaMA2) into diffusion language models (DLMs) through continual pre-training. The key technical contributions are: (1) attention mask annealing to transition from causal to bidirectional attention, (2) retaining the shift operation from AR training to maintain alignment between inputs and prediction targets, and (3) a time-embedding-free architecture that leverages the AR model's existing weights. The authors demonstrate adaptation at scales from 127M to 7B parameters using under 200B training tokens, producing DiffuGPT and DiffuLLaMA.

The paper has several strengths: it addresses an important scaling problem for DLMs, the adaptation recipe is conceptually simple and practically demonstrated at non-trivial scale (7B), and the released model suite and code are valuable for the community. The evaluation across language modeling, reasoning, commonsense, math, and infilling tasks is more comprehensive than prior DLM work that relied solely on perplexity.

However, significant weaknesses affect the core claims: (1) The infilling comparison is structurally unfair — AR baselines receive only prefix information while DLMs receive bidirectional context — undermining the claimed superiority of DLMs for infilling. (2) The "state-of-the-art DLM" and "competitive with AR counterparts" claims in the abstract and contributions are overstatements given that DiffuLLaMA substantially underperforms LLaMA2 on 5 of 7 zero-shot tasks. (3) The attention mask annealing procedure is underspecified, preventing reproduction. (4) The ablation study is conducted on a proxy finetuning task rather than the actual adaptation process. (5) The ICL evaluation lacks controlled baselines to distinguish format-following from genuine in-context learning.

**Overall assessment:** The paper presents a practically useful engineering recipe for converting AR LMs into DLMs and provides valuable open-source resources. The core technical contribution (bridging the AR-DLM gap via annealing + shift) is interesting but not deeply theoretically grounded. The main research value lies in demonstrating feasibility at 7B scale and releasing the models, rather than in advancing a new learning principle. Novelty claims require external verification (deferred in this run due to disabled retrieval).

## Strengths
**S1. Important problem and practical framing.** The paper tackles a genuine challenge: DLMs have not reached the scale of AR LMs, and training them from scratch at 7B+ scale is prohibitively expensive. Using off-the-shelf AR LMs as initialization is a well-motivated, resource-efficient strategy.

**S2. Demonstrated feasibility at 7B scale.** The adaptation of LLaMA2-7B into DiffuLLaMA is, to the knowledge of this review, the largest reported discrete diffusion LM. The authors show non-trivial scaling behavior (loss decreasing with model size) and release the 7B model, which is a valuable community resource.

**S3. Technical simplicity.** The three-component adaptation recipe (mask annealing + shift operation + time-embedding-free design) is clean and intuitive. The shift operation retention is particularly well-motivated: it allows the AR-pretrained weights to function naturally within the diffusion framework.

**S4. Comprehensive evaluation compared to prior DLM work.** The paper goes beyond zero-shot perplexity (the dominant metric in prior DLM papers) and evaluates across multiple task types: QA (TriviaQA), word completion (Lambada), commonsense reasoning (HellaSwag, Winogrande, SIQA, PIQA), math (GSM8K), and infilling (ROCStories, HumanEval). This provides a more nuanced picture of DLM capabilities.

**S5. Open-source release.** Releasing three model sizes (127M, 355M, 7B) along with adaptation code, finetuning scripts, and evaluation toolkits provides substantial value for reproducibility and follow-up research.

**S6. Interesting qualitative observations.** The self-correction case study (Appendix Table 6) and the global planning experiment on CD4 (Table 7, 87.5% vs GPT2-scratch 45.8%) provide compelling evidence for DLM advantages in iterative refinement.

## Weaknesses
**W1. Unfair infilling comparison undermines a core claim [Major].** AR baselines in Table 1 are given only prefix context for infilling tasks, while DLMs naturally receive bidirectional context (both prefix and suffix). The paper acknowledges this ("which might result in an unfair comparison," Page 7) yet still presents the results as evidence that "DLMs demonstrate their strengths in infilling tasks." The claim that DLMs are superior for infilling is a foregone conclusion given the asymmetric setup. A proper comparison would require FIM-trained AR models (e.g., CodeLLaMA with SPM/PSM formats, which the paper does attempt in Appendix Table 8 but on only 100M tokens of training).

**W2. Abstract overclaims competitiveness [Major].** The abstract states the models "are competitive with their AR counterparts," but Table 1 shows DiffuLLaMA underperforms LLaMA2 by large margins on TriviaQA (18.5 vs 45.4), HellaSwag (58.7 vs 74.9), Winogrande (56.4 vs 67.1), PIQA (63.3 vs 78.3), and SIQA (43.2 vs 44.8). Only on Lambada (70.9 vs 68.8) and GSM8K (63.1 vs 58.6) does DiffuLLaMA match or exceed LLaMA2. "Competitive" is accurate for a subset of tasks but misleading as a blanket claim.

**W3. Attention mask annealing is underspecified [Major].** The description in §3.3 (Page 5) states "at each training step, we sample the amount of context from the right side and progressively increase this amount," but does not specify: (a) the annealing schedule (linear, cosine?); (b) the sampling distribution over context amount; (c) the starting ratio; (d) whether it is per-layer or global; and (e) the starting/ending steps. The exact procedure is neither given in the main text nor in the appendix Algorithm 1. This makes the core technical contribution unreproducible.

**W4. Ablation on proxy task instead of adaptation training [Minor].** Table 3 ablates shift and annealing on GSM8K-symbolic finetuning, not on the actual adaptation pre-training. The paper acknowledges this ("Direct ablation on adaptation training is costly"), but this means the ablation conclusions about annealing and shift efficacy may not generalize to the 200B-token adaptation setting.

**W5. ICL evaluation lacks controls [Major].** The improvement from zero-shot to few-shot on math tasks (Page 9, Table 2) is presented as evidence that DiffuLLaMA "can learn from ICL examples." However, no random-label control or permutation test is conducted to distinguish format-following from genuine in-context learning. The CoT performance drop is attributed to "absence of instruction tuning" without considering alternative explanations (e.g., longer outputs exceeding fixed-step sampling capacity).

**W6. Inconsistent adaptation recipe across model sizes [Minor].** DiffuLLaMA-7B directly uses bi-directional attention "without attention mask annealing" (Page 6) for "efficient implementation." This means the 7B model does not use one of the three claimed core techniques, weakening the general claim that mask annealing is necessary for adaptation.

**W7. Missing variance and significance metrics [Minor].** All results in Table 1 and Table 2 are point estimates without standard deviations, confidence intervals, or significance tests. For narrow margins (e.g., SEDD-S vs DiffuGPT-S on Wino: 50.1 vs 50.8), it is impossible to assess whether differences are statistically meaningful.

**W8. Generative perplexity evaluation bias [Minor].** The unconditional generation evaluation in Figure 3 uses GPT2-large (an AR model) to compute perplexity of DLM-generated text. This may systematically favor AR-like (left-to-right) text patterns over the iterative refinement patterns produced by DLMs. Diversity metrics are only reported for two models, not all compared methods.

## Key Issues
The following ranked error board prioritizes the most impactful issues based on their effect on validity, research value, and reproducibility.

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence |
|------|-------|----------|--------------|------------|------------|
| 1 | Abstract overclaims "competitive with AR counterparts" and "SOTA DLM" | Major | High — misrepresents empirical findings | Easy — bound claims to evidence | High |
| 2 | Infilling comparison structurally unfair (prefix-only AR vs full-context DLM) | Major | High — undermines a core comparative claim | Moderate — add FIM-trained AR baselines | High |
| 3 | Attention mask annealing underspecified (schedule, distribution, ratio) | Major | Medium — prevents reproduction | Easy — add explicit schedule in text/appendix | High |
| 4 | ICL evaluation lacks random-label control to distinguish format-following from genuine learning | Major | Medium — overstates ICL capability claim | Easy — add control experiment | High |
| 5 | Training inconsistencies across sizes (7B skips annealing) | Minor | Low — does not invalidate main result | Moderate — acknowledge and justify | High |
| 6 | Missing variance/significance metrics in all tables | Minor | Medium — prevents statistical reliability assessment | Easy — add multi-seed results | High |
| 7 | Ablation performed on proxy task (GSM8K finetuning) not on adaptation training | Minor | Low — conclusions may not generalize | Hard — costly to re-run at scale | Medium |
| 8 | GPT2-large perplexity for DLM evaluation may be biased | Minor | Low — acknowledged evaluation concern | Easy — add MAUVE/self-BLEU | Medium |

## Actionable Suggestions
### Suggestion 1: Bound all comparative claims to evidence (Must)
**Location**: Abstract, Page 1 and Contribution bullets, Page 2.
**Problem**: "Competitive with AR counterparts" and "state-of-the-art DLM" are unqualified and overbroad.
**Action**: Replace with bounded wording.

**Mentor Revised Version (Abstract sentence)**:
"Our experimental results reveal that these models outperform earlier DLMs and achieve competitive results on Lambada, math reasoning (GSM8K), and infilling tasks. On knowledge-intensive and commonsense benchmarks, DiffuLLaMA underperforms LLaMA2, likely due to the reduced training budget."

**Mentor Revised Version (Contribution bullet 2)**:
"We adapt 7B AR models to DLMs. Compared to prior DLMs (SEDD, Plaid1B, MD4), DiffuLLaMA achieves the best overall results under our evaluation. It demonstrates in-context learning and infilling capabilities, with generation speed competitive with AR models for sequences of 1024+ tokens using 256 diffusion steps."

### Suggestion 2: Add fair infilling baselines (Must)
**Location**: Section 4.3, Page 7-8 and Table 1.
**Problem**: AR baselines get prefix-only, DLMs get bidirectional context.
**Action**: Either (a) train AR baselines with FIM (as done in Appendix Table 8 but with more data), or (b) reframe the comparison honestly: "DLMs support infilling without special training, unlike AR models that require FIM adaptation."

### Suggestion 3: Specify attention mask annealing in full detail (Must)
**Location**: Section 3.3, Page 5.
**Problem**: Annealing schedule, ratio, distribution, and per-layer behavior are unspecified.
**Action**: Add one paragraph specifying:
- Start ratio: full causal mask (r=1.0)
- End: full attention (r=0.0) after K_anneal steps
- Schedule: linear decay r(k) = max(0, 1 - k/K_anneal)
- Per-step: for each position i, allow attending to the next (1-r)×(N-i) future tokens
- K_anneal: 10,000 for DiffuGPT, 0 for DiffuLLaMA-7B

### Suggestion 4: Add random-label control for ICL evaluation (Must)
**Location**: Section 4.4, Page 9.
**Problem**: Cannot distinguish format-following from genuine ICL.
**Action**: Add a control condition where in-context examples have randomly shuffled labels. If accuracy drops to near zero-shot level, the model is genuinely learning from demonstrations; if it stays similar, the model is primarily mimicking format.

### Suggestion 5: Add variance reporting (Nice-to-have)
**Location**: All tables.
**Action**: Report mean±std over ≥3 seeds for all results. For Table 1's narrow margins, add a paired significance test (McNemar's test) between closest baselines.

### Suggestion 6: Add pre-adaptation loss baseline to Figure 2 (Nice-to-have)
**Location**: Section 4.1, Page 6.
**Action**: Add a horizontal line showing LLaMA2's AR loss at initialization. This shows how much the model "forgets" at the start of adaptation and how quickly the DLM training objective converges.

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis
The current introduction follows: (P1) LLMs are great but AR has limits → (P2) DLMs are promising → (P3) DLMs are too small → (P4) Our approach bridges AR-DLM gap → (P5) Contributions. The main weakness is that P1 is too broad (general LLM praise), P2 could integrate with P3, and the "gap" is stated only after praising DLMs for too long. The reader doesn't learn the concrete technical problem until paragraph 4.

### Recommended Storyline (Option B: Problem-first)
A tighter structure that centers on the scaling problem from the start:

**P1 (Problem + Motivation)**: "Diffusion language models offer potential advantages over autoregressive models—bidirectional context, iterative refinement, and natural infilling capability—but have remained an order of magnitude smaller than their AR counterparts. Training large DLMs from scratch is prohibitively expensive, and prior adaptation attempts from masked LMs lose base model capabilities."

**P2 (Gap + Prior Attempts)**: "Existing DLMs (Plaid1B, SEDD) are limited to 1B parameters and under-trained. Recent attempts to initialize DLMs from pretrained models (DiffusionBERT, Ye et al. 2023) use masked LMs, which are closer to diffusion objectives. Adapting from AR LMs—the most widely available pretrained models—is more challenging due to causal masking and objective mismatches."

**P3 (Our Approach)**: "We propose a simple adaptation recipe with three components: (1) attention mask annealing to transition from causal to bidirectional attention, (2) retaining the shift operation for consistent prediction targets, and (3) time-embedding-free design to use AR weights as-is. This converts GPT2 and LLaMA2 into DiffuGPT and DiffuLLaMA at 127M-7B scales with under 200B tokens."

**P4 (Key Results + Contributions)**: Bulleted contributions with bounded language.

### Abstract Outline (Complete)
**S1 (Problem and Domain)**: "Diffusion language models (DLMs) offer bidirectional context and iterative refinement but have lagged behind autoregressive (AR) models in scale."
**S2 (Significance/Gap)**: "Training large DLMs from scratch is resource-intensive, and existing DLMs are limited to 1B parameters."
**S3 (Prior Work Limitation)**: "Prior adaptation attempts rely on masked language models, while the most widely available pretrained models use AR objectives."
**S4 (Proposed Method)**: "We bridge the gap between AR and diffusion objectives through attention mask annealing, shift operation retention, and a time-embedding-free architecture, converting GPT2 and LLaMA2 (127M-7B) into DLMs with under 200B training tokens."
**S5 (Key Result, Bounded)**: "The resulting models, DiffuGPT and DiffuLLaMA, outperform prior DLMs on language modeling, reasoning, and infilling benchmarks, and match AR counterparts on tasks benefiting from bidirectional context."

### Revised Introduction (Paragraph-by-Paragraph Plan)
**P1 — The scaling challenge for DLMs**:
Role: Establish concrete problem (DLMs are too small) and its significance.
Claim: Despite advantages (bidirectional, iterative refinement), DLMs have not reached AR scale because training from scratch is expensive.
Transition to: Why can't we initialize DLMs from existing AR LMs?

**P2 — The AR-DLM gap**:
Role: Explain the two core technical hurdles (causal vs bidirectional masking; clean vs noisy inputs).
Claim: These differences prevent direct parameter reuse of AR models for diffusion.
Transition to: We show these gaps can be bridged.

**P3 — Our adaptation bridge**:
Role: Present the three technical components at a high level.
Claim: Attention mask annealing + shift operation + no time embedding = effective adaptation.
Transition to: We demonstrate this at scale.

**P4 — Results and contributions**:
Role: Preview key empirical findings with bounded claims.
Claim: DiffuGPT outperforms GPT2 on most tasks; DiffuLLaMA is the best-performing DLM among compared baselines; speed is competitive for long sequences.

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[P0: Fix claim-evidence mismatch] -> [Abstract + Contributions repaire]
    -> Expected impact: Accurate framing avoids reviewer rejection for overclaim
[P1: Fair infilling comparison]  -> [Add FIM baselines or reframe claim]
    -> Expected impact: Core DLM advantage claim becomes defensible
[P1: Specify mask annealing]     -> [Add explicit schedule in §3.3]
    -> Expected impact: Reproducibility + reviewer confidence
[P2: ICL control experiment]     -> [Add random-label baseline]
    -> Expected impact: Strengthen ICL capability evidence
[P2: Add variance metrics]       -> [Multi-seed reporting in all tables]
    -> Expected impact: Statistical reliability assessment possible
[P3: Resolve training inconsistency] -> [Acknowledge 7B annealing skip]
    -> Expected impact: Methodological consistency
```

### Immediate Fixes (P0, before resubmission)
| Action | Location | Effort | Impact |
|--------|----------|--------|--------|
| Reword Abstract "competitive" and "SOTA DLM" claims | Abstract + Page 2 bullets | Low (text edit) | High — directly addresses overclaim |
| Add explicit annealing schedule | §3.3, Page 5 | Low (text addition) | High — enables reproduction |
| Reframe infilling comparison | §4.3, Page 7-8 | Low (text edit) | High — fixes unfair comparison |

### Short-term Improvements (P1, within 1-2 weeks)
| Action | Location | Effort | Impact |
|--------|----------|--------|--------|
| Add FIM-trained AR baseline on 1B+ tokens of Starcoder for infilling | Appendix | Medium (requires training) | High — validates infilling claims |
| Add random-label ICL control | §4.4, Page 9 | Low (evaluation only) | Medium — strengthens ICL evidence |
| Report mean±std over 3 seeds for all tables | All tables | Medium (re-run some evals) | Medium — enables significance checks |

### Longer-term Enhancements (P2, before next major submission)
| Action | Location | Effort | Impact |
|--------|----------|--------|--------|
| Pre-adaptation loss baseline in Figure 2 | §4.1 | Low (plot update) | Medium — shows adaptation shock |
| Instruction tuning for DiffuLLaMA | New section | High (requires new experiment) | High — improves task performance |
| Inference throughput with batched decoding | §4.5 / Appendix | Low (additional measurement) | Medium — more realistic speed comparison |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|-------------|-----------------|-------------------|
| E1 | Language modeling capacity (zero-shot) | 8 tasks (TriQA, Lambada, HSwag, Wino, SIQA, PIQA, ROCStories, HumanEval) | Accuracy (or ROUGE for infill) | DiffuGPT/DiffuLLaMA best among DLMs; below LLaMA2 on knowledge tasks | C1, C2 | No variance reported; AR infilling baselines unfair |
| E2 | Unconditional generation quality | GPT2-large perplexity + distinct 2-gram | PPL, Dist-2 | DiffuGPT achieves low PPL with high diversity | C1 | Evaluator (GPT2-large) is AR model, potential bias |
| E3 | ICL and reasoning (DiffuLLaMA) | MAWPS, SATMath, TriviaQA (ZS/FS/SC/@k/CoT) | Exact match accuracy | FS > ZS; SC improves; CoT degrades | C2 | No random-label control; CoT drop unexplained |
| E4 | Ablation (adaptation components) | GSM8K-symbolic finetuning (proxy task) | Accuracy | DD > CD; shift + anneal both help ablation | Method components | Proxy task may not reflect adaptation at scale |
| E5 | Inference speed | Single-batch, various lengths, flash-attention 2 | Wall-clock time (sec) | DiffuLLaMA competitive for >=1024 tokens at T=256 | C2 | Batch size 1 only; no memory measurement |
| E6 | Self-correction (qualitative) | DoT trajectory case study | Qualitative | DLM refines intermediate numbers | DLM advantage | Single case; not systematic |
| E7 | Global planning (CD4) | Counting down (CD4) dataset | Accuracy | DiffuGPT 87.5% vs GPT2-scratch 45.8% | DLM advantage | Small model (355M) only |
| E8 | Code infilling (controlled) | CodeLLaMA + Starcoder 100M tokens | Pass@1 | Diffu-CodeLLaMA 0.76 vs SPM 0.80 / PSM 0.74 | DLM advantage | Small training budget (100M tokens) |

### Research-Theme Gap Diagnosis

**New knowledge**: The paper demonstrates a practical engineering recipe (AR → DLM adaptation) that is useful but not deeply novel from a theoretical standpoint. The attention mask annealing technique is intuitive (gradually removing causal masking) and the shift operation retention is straightforward. The main new knowledge contribution is the empirical demonstration that AR models can be converted to DLMs at 7B scale with limited training.

**Reproducibility**: The paper provides code and model releases, which is strong. However, the underspecified annealing schedule weakens reproducibility of the core technical method.

**Impact on practice/understanding**: The released models enable broader experimentation with DLMs at 7B scale. However, the paper does not provide sufficient analysis of *why* the adaptation works (e.g., does the model retain specific AR capabilities that from-scratch DLMs lack?) or *when* it fails.

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

[P0: Text edits & re-evaluation (low effort)]
    ├── Fix claim wording in Abstract/Contributions
    ├── Add random-label ICL control
    └── Report multi-seed variance for Table 1

[P1: Controlled infilling (medium effort)]
    ├── Train AR model with FIM on 1B+ tokens
    └── Compare DiffuLLaMA vs FIM-AR on HumanEval + ROCStories

[P2: Deeper analysis (higher effort)]
    ├── Instruction tuning for DiffuLLaMA
    ├── Analysis: which AR capabilities are preserved?
    └── Batched throughput comparison
```

| Experiment | Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Est. Cost | Expected Gain |
|-----------|-------------|------------|---------------|----------|---------|------------------|-----------|---------------|
| Random-label ICL control (P0) | ICL capability (C2) | Format-following, not genuine ICL | Compare FS accuracy with correct labels vs shuffled labels | Same prompts, same sampling | Accuracy | If shuffled-label accuracy drops to ZS level → genuine ICL | 1-2 GPU hours | Strengthens ICL evidence |
| Multi-seed variance (P0) | All empirical claims | Results are stable | Re-run Table 1 key comparisons with 3 seeds | Identical config | Mean±std | Within 1% std for all tasks | 2-5 GPU days | Statistical grounding |
| FIM-trained AR infilling (P1) | DLM infilling advantage | FIM-AR can match DLMs given sufficient data | Train LLaMA2 with FIM (SPM) on 50B tokens; evaluate on infilling | Same eval protocol | ROUGE, Pass@1 | DiffuLLaMA outperforms FIM-AR | ~500 GPU hours | Validates/falsifies core DLM advantage |
| Instruction tuning (P2) | DLM task performance | Instruction tuning improves DiffuLLaMA | Apply LoRA on instruction data; eval on all tasks | Untuned DiffuLLaMA | All metrics in Table 1 | >=5% improvement on 4+ tasks | ~100 GPU hours | Practical usability

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

**Scoring rationale:**
- **Research Value (primary): 5/10** — The paper addresses an important practical problem (scaling DLMs) and provides a working engineering recipe. The released models and code are valuable community assets. However, the conceptual novelty is incremental (mask annealing + shift operation retention is straightforward once the connection between AR and diffusion objectives is noted). The paper does not provide deep theoretical insights into *why* adaptation works or what is preserved/lost during conversion.
- **Novelty: 5/10** (deferred confirmation note: external retrieval was disabled in this run, so novelty vs the complete literature cannot be fully verified). Compared to baselines discussed in the paper (SEDD, Plaid1B, MD4), the adaptation approach is novel in the DLM space. However, MLM-based initialization (DiffusionBERT, Ye et al. 2023) is conceptually similar, and the step from MLM→DLM to AR→DLM is evolutionary. The attention mask annealing idea shares conceptual similarity with curriculum learning for NAR (Guo et al. 2020).
- **Validity/Soundness: 5/10** — The core empirical claims are partially supported, but the infilling comparison is structurally unfair, the ICL evidence lacks controls, and variance metrics are absent.
- **Reproducibility: 6/10** — Code and models are released, which is strong. However, the annealing schedule is underspecified, and the 7B model skips a core component.
- **Clarity: 6/10** — Generally well-written, but the introduction storyline could be sharper. The disparity between abstract claims and empirical evidence creates confusion.

**Post-Revision Target: [6.5, 7.5]/10**

This target is grounded in the following reasoning:
- Lower bound (6.5): Achievable by addressing P0 items (claim bounding, annealing specification, infilling reframing). These changes would fix the major validity concerns and align claims with evidence.
- Upper bound (7.5): Achievable by additionally completing P1 items (multi-seed variance, ICL control, stronger infilling baseline). The paper would then be a solid empirical contribution with defensible claims.
- The upper bound is not higher because the conceptual novelty of the approach remains incremental, and deeper theoretical analysis of the adaptation mechanism would require a separate study beyond the scope of reasonable revision.