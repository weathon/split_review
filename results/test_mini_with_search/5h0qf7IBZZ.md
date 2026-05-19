Now I have all the information I need. Let me write the final review.

**Bracketing summary:**

**Round 1 bracket:** The three queries returned anchors in bands: weak (2.5–3.0), middle (4.0–5.5), and strong (8.0). The paper is clearly above the weak band (rejected papers with limited contributions). Among the middle band: CSD (5.50, accepted), GAKD (4.50, rejected), Grafting (5.00, rejected), DAKD (4.67, rejected). The strong-band papers (8.0) are on unrelated topics (transduction, scaling laws, multi-turn conversations). So the initial bracket is roughly 5.5–7.0.

**Round 2 narrowing:** Within 5.5–7.5, I retrieved CSD (5.50, accepted), AMiD (6.00, accepted), Boomerang Distillation (6.00, accepted), and a data-efficient training paper (6.80). MiniLLM is stronger than CSD (more comprehensive experiments, human eval, clearer motivation) and at least comparable to AMiD (similarly rigorous experiments, better writing). The weaknesses in MiniLLM (minor issues about importance weight bias, missing std devs, an unvalidated side claim) are less severe than AMiD's (unclear hyperparameter selection, missing baselines, poor presentation).

**Final score: 6.5** — clearly above the acceptance threshold, comparable to or stronger than accepted KD papers like CSD (5.50) and AMiD (6.00), but not at the 8.0 level of top-tier papers on unrelated topics.

**Anchor listing (all rounds):**

| Paper | Path | Score | Round | Comparison |
|---|---|---|---|---|
| What Makes LLMs Undistillable | QqNHozX7Ad.md | 2.50 | 1 | Much weaker than MiniLLM — withdrawn paper |
| Distill Not Only Data but Also Rewards | tK6VZy5RYr.md | 3.00 | 1 | Much weaker — limited novelty, missing baselines |
| Understanding KD in Post-Training | DvrZRcoT6p.md | 3.00 | 1 | Much weaker — limited scope |
| Flexible Feature Distillation | aiMINHhIiQ.md | 3.00 | 1 | Much weaker |
| To Distill or Not to Distill | AEKji3PwD9.md | 3.00 | 1 | Weaker — different focus (safety) |
| CSD | bZBJFrxH1H.md | 5.50 | 1,2 | Weaker than MiniLLM — less comprehensive experiments, no human eval |
| Don't Ignore the Tail | EYflZV1caL.md | 4.00 | 1 | Weaker — limited evaluation |
| DAKD | nkm3lL8CQE.md | 4.67 | 1 | Weaker — limited gains, extra compute |
| GAKD | 9pfWYxYHAn.md | 4.50 | 1 | Weaker — flawed motivation, unstable training |
| Grafting | h1rCBN6hWi.md | 5.00 | 1 | Comparable weakness profile but less thorough |
| Pedagogically-Inspired Data Synthesis | Bxxdz07CDp.md | 5.50 | 2 | Comparable score but different focus (data synthesis) |
| AMiD | 7WPJ0EgPdW.md | 6.00 | 2 | Similar quality — MiniLLM has more model families, better writing |
| Boomerang Distillation | 4ZU8v4s3IR.md | 6.00 | 2 | Different topic, similar quality tier |
| Data-efficient LLMs | yKUbw7q1IA.md | 6.80 | 2 | Different topic (pre-training), slightly stronger |
| Ultra-Fast Language Generation | mtdyZsa47V.md | 6.67 | 2 | Different topic (diffusion), similar quality |
| LLMs Get Lost In Multi-Turn | VKGTGGcwl6.md | 8.00 | 1 | Unrelated topic, much stronger |
| Transducing Language Models | qOyF214xmg.md | 8.00 | 1 | Unrelated topic |

---

## Final Review

### Summary
This paper proposes MiniLLM, a knowledge distillation method for large language models that replaces the standard forward KL divergence objective with reverse KL divergence, arguing that reverse KL is more suitable for generative LLMs because it avoids overestimating low-probability regions of the teacher distribution. The authors derive a policy-gradient optimization for this objective and introduce three stabilization strategies: single-step decomposition (to reduce variance), teacher-mixed sampling (to prevent reward hacking), and length normalization (to counteract length bias). Experiments across three model families (GPT-2, OPT, LLaMA) at scales from 120M to 13B parameters show consistent improvements over SFT, word-level KD, and sequence-level KD baselines on Rouge-L, GPT-4 feedback, and human evaluation.

### Strengths

**1. Well-motivated, principled contribution.** The paper provides a clear theoretical argument — illustrated with a toy Gaussian mixture experiment (Figure 2) — for why forward KL is suboptimal for generative LLM KD and why reverse KL is more appropriate. The optimization derivations (Section 2.2) are technically sound, and the three stabilization strategies are each motivated by a concrete training pathology.

**2. Extensive and rigorous empirical validation.** The experimental evaluation covers 3 model families (GPT-2, OPT, LLaMA), 4 student sizes (120M–7B), 5 evaluation datasets, and 3 metrics including human evaluation. MiniLLM outperforms all baselines in 44 out of 48 metric-model-size combinations in Table 1. The scaling experiment (Figure 5) shows that gains hold with larger teachers. The analyses of exposure bias (Figure 4) and calibration (Table on calibration) provide mechanistic insight into why the method works.

**3. Component-level ablation confirming each design choice.** The ablation study (Table 5, Figure 6) empirically validates that each of the three optimization strategies contributes to both training stability and final performance, demonstrating the method is a carefully engineered solution rather than a single big idea.

**4. Human evaluation corroboration.** On the LLaMA family (SelfInst dataset), human annotators prefer MiniLLM responses over all baselines and rate them comparably to the teacher model (Figure 3), adding a human judgment dimension beyond automatic metrics.

**5. Exposure bias analysis.** The ExAccErr plot (Figure 4) provides direct evidence that MiniLLM alleviates training-inference mismatch — a core weakness of forward-KL methods — with errors plateauing beyond 150 tokens, unlike baselines where errors grow monotonically.

### Weaknesses

#### Fatal
None.

#### Major
None.

#### Minor

**1. Importance weight approximation in teacher-mixed sampling is unanalyzed.** The paper derives an off-policy gradient estimator using importance weights (Eq. 8), then immediately approximates it by dropping the product over previous tokens (Eq. 9) to reduce variance, citing [deep_rl_chat, offline_rl]. This approximation is no longer an unbiased correction. While the paper acknowledges this, it provides no analysis of the induced bias. The ablation without teacher-mixed sampling still outperforms baselines (20.4 vs. baselines on Dolly, Table 5), which partially mitigates concern, but the degree to which the biased estimator contributes to the reported gains is unclear.

**2. No standard deviations or significance measures in main results.** Table 1 reports averages over 5 random seeds but shows no standard deviations, confidence intervals, or significance tests. Several improvements are small (e.g., GPT-2 340M on DollyEval GPT4: 52.2 vs. 51.9 for SFT, +0.3; GPT-2 340M on VicunaEval GPT4: 42.6 vs. 43.0 for SeqKD, where MiniLLM *loses*). Without variance estimates, the reliability of individual cells cannot be assessed.

**3. Claim about the pre-training loss preserving "canonical NLP benchmarks" is unvalidated.** Section 2.3 introduces \(\mathcal{L}_{\text{PT}}\) "to preserve the model performance on canonical NLP benchmarks," but the experiments never evaluate on standard NLP benchmarks to demonstrate this effect. The calibration analysis uses SST-2 and BoolQ, but these measure calibration, not whether \(\mathcal{L}_{\text{PT}}\) prevents degradation. This is a side component (borrowed from Instruct-GPT) and does not affect the core contribution, but the claim should be validated or retracted.

#### Trivial
None.

### Nice-to-Haves
- **Training cost comparison.** The full-vocabulary summation in the single-step decomposition is \(O(V \cdot T)\) per example. A comparison of training time/FLOPs with baselines would help practitioners assess the cost-benefit trade-off.
- **Sensitivity analysis on \(\alpha\) (teacher mix-in strength).** Only \(\alpha = 0.2\) is used. An analysis of sensitivity to this hyperparameter would strengthen practical guidelines.
- **Discussion of failure cases.** The paper addresses mode-dropping concerns but does not discuss settings where MiniLLM might underperform (e.g., tasks where output diversity matters more than precision, such as creative writing).

### Removed Points
- **Criticism about the "white-box KD for LLMs is yet to be explored" claim being overstated:** Minor phrasing concern; the paper acknowledges concurrent works in Related Work. Removed as it does not affect the paper's contribution.
- **Concern that R-L-based hyperparameter selection advantages MiniLLM:** Speculative, no evidence provided. Removed.
- **Criticism that human evaluation covers only one dataset:** A scope limitation natural for human eval; not a substantive weakness. Removed.
- **Formatting, typo, and presentation nitpicks about missing appendix/proofs:** These are parser artifacts; the original submission contains them. Removed per hard rules.
- **Generic "evaluation lacks rigor" / "method may not be fair" / unmoored speculation about confounders:** Removed as lacking specific anchors in the paper.
- **Strength Finder's generic strengths about "the problem is important" / sycophancy:** Removed as not concrete or specific to this paper's content.

### Novel Insights
None beyond the paper's own contributions. The reviewer inputs largely converge with the paper's own framing; the most notable insight from the reviews is that the teacher-mixed sampling's biased importance weight estimator is a genuine methodological gap that the ablation (w/o teacher-mixed) only partially addresses — this blind spot is worth flagging even though the ablation suggests the method's core value does not depend on it.

### Suggestions
1. Add standard deviations (or IQRs) for the five-seed runs in Table 1.
2. Provide a brief empirical analysis comparing the biased importance weight estimator against the full product (on a small-scale experiment) to bound the bias, or adopt a properly unbiased estimator (e.g., V-trace).
3. Either validate the \(\mathcal{L}_{\text{PT}}\) claim on a standard benchmark or soften the language to acknowledge it is a regularization term borrowed from prior work.
4. Include a training time/FLOPs comparison with baselines — the full-vocabulary summation is a real cost practitioners need to budget for.

### Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>