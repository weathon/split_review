Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces Insertion Language Models (ILMs), which generate sequences by inserting one token at a time at arbitrary positions. Unlike ARMs (fixed left-to-right order) and MDMs (fixed-length masking, simultaneous unmasking), ILMs learn to jointly predict *where* to insert and *what* to insert using a denoising objective that drops tokens and predicts the missing ones. The authors propose a simple transformer-based parameterization, a dedicated stopping classifier for variable-length generation, and a biased training objective to avoid the high variance of exact trajectory marginalization. Experiments on synthetic planning tasks (star graphs, zebra puzzles) show ILM overcoming failure modes of both ARMs and MDMs, while on text tasks ILM is competitive with ARMs and better than MDMs on infilling and several linguistic quality metrics.

## Strengths

- **Near-perfect accuracy on variable-length planning tasks where ARMs and MDMs fail.** On Star_medium and Star_hard, ILM achieves 100% and 99.1% exact match, while MDM drops to 36.5% and 21.0% and standard ARM to 75.0% and 23.0% (Table 1). This is a compelling existence proof that the combination of out-of-order generation and iterative insertion can solve problems that fundamentally challenge both families of models.

- **The paper provides a clean, self-contained framework** — training objective (Section 3, Eq. 2–4), network parameterization (simple transformer encoder + unembedding, no custom backbones), inference algorithm (Algorithm 2), and stopping mechanism — that other researchers can build on. The architecture is notably simpler than the DiT-based backbone required by MDMs.

- **Demonstrates a realistic advantage over MDMs on multi-segment infilling.** On LM1B multi-segment infilling, ILM achieves ΔNLL_inp of –7.93% vs MDM's –6.02% (Table 3). Because MDMs require a fixed number of mask tokens in the input, they cannot naturally handle unknown token counts; ILM avoids this limitation through its insertion mechanism.

- **Zebra puzzle results are strong and not purely synthetic.** ILM achieves 90.0% exact match, competitive with an oracle-decomposed ARM (91.2%) and outperforming both the standard ARM (81.2%) and MDM (82.6%). This demonstrates ILM's advantage on a realistic constraint satisfaction task.

## Weaknesses

### Major

1. **The stopping classifier produces sequences that are systematically too short, and this failure mode is not analyzed.** On the Stories dataset, ILM generates an average length of 119 tokens — only 58% of the dataset mean of 205 (Table 2). On LM1B, ILM's average length is 21 vs the dataset mean of 28 (75%). This undershoot is severe and could explain why Prometheus scores favor ILM (shorter completions are easier to keep coherent). The paper acknowledges the length discrepancy for MDM (985 tokens) but does not examine ILM's own undershoot, report the stopping classifier's accuracy, or analyze whether a threshold adjustment could match the data length distribution. Given that the Insertion Transformer baseline's failure was partly attributed to its poorer stopping mechanism (EOS token vs. learned classifier), the ILM's own stopping behavior warrants scrutiny.

2. **No comparison against a fill-in-the-middle (FIM) trained ARM for infilling.** The infilling experiments (Table 3) compare ILM only against MDM. The paper discusses Bavarian et al. (2022)'s FIM objective in Related Work, noting that it "is not capable of performing arbitrary infilling, for example, filling two blanks at separate places." However, a single-segment FIM comparison is the natural baseline for the single-segment infilling experiments. Without it, the contribution on infilling is significantly weakened — the claim is that ILM is more flexible than MDMs for infilling, but the practical question of whether a FIM-ARM achieves comparable or better quality on single-segment infilling goes unanswered.

3. **The training objective is an acknowledged approximation whose bias is not characterized.** The paper states (Section 3) that exact trajectory marginalization has high variance and replaces it with a "biased training objective" that predicts normalized counts of dropped tokens. However, it provides no analysis (beyond what is deferred to the stripped Appendix D) of how this bias affects the learned distribution, whether it systematically favors certain insertion orders, or how it interacts with the stopping classifier. For the core technical contribution of the paper, this level of justification is thin. The concern is not that the paper uses an approximation — which is pragmatically reasonable — but that the nature and severity of the bias are entirely unmeasured.

### Minor

4. **Text generation NLL underperforms ARMs, especially on LM1B.** On Stories, ILM's NLL (2.14) is close to ARM (2.11), but on LM1B the gap is larger (4.67 vs 3.94). Combined with the length undershoot, the text generation evidence is mixed. The Prometheus scores (Figure 5) show ILM ahead of ARM on coherence and consistency, but without length-controlled analysis it is unclear whether this reflects genuine quality or an artifact of shorter outputs.

5. **Experiments are limited to 85M parameter models with no scaling study.** It is an open question whether ILM's text quality gap with ARMs widens or narrows at larger scales. Given that the related work on MDMs (e.g., Ye et al., 2025; Nie et al., 2024) includes scaling analyses, the absence of even a small-scale scaling experiment (e.g., 3–4 sizes on LM1B) limits the contribution's breadth.

6. **The star graph planning advantage is partly by design** — as the paper acknowledges ("carefully chosen synthetic tasks"). The task exposes MDMs' fixed-length masking limitation and ARMs' left-to-right ordering limitation in a setting where ILM's relative-position, iterative insertion mechanism is particularly well-suited. While this is a legitimate demonstration of the paper's thesis, it does not automatically generalize to complex real-world planning tasks (code generation, math reasoning) where the constraints are less structured.

### Trivial

None.

## Nice-to-Haves

- An ablation of the stopping classifier vs. an EOS token on the text datasets would isolate whether the length control benefit observed on star graphs (IT vs. ILM) carries over to language modeling.
- Sensitivity analysis for the top-k position sampling and nucleus token sampling hyperparameters in Algorithm 2.

## Removed Points

These points from the reviewers were removed for the reasons stated:

1. **"The chef example is a strawman"** — The paper acknowledges that greedy unmasking is possible but notes it requires a full forward pass per token, making it slow. This is a valid limitation, not a strawman.

2. **"MDM uses absolute positions while ILM uses RoPE"** — The paper states MDM uses DDiT, which is "based on the DiT architecture that inserts adaptive layer-norm (AdaLN) in the RoPE based transformer." Both model families use RoPE-based transformers. The claimed architectural asymmetry does not exist as framed.

3. **Missing related works / formatting / typos / reproducibility nitpicks** — Removed per hard rules (the parser strips appendices; missing related works cannot be authoritatively confirmed; typos are parser artifacts).

4. **"Training/inference discrepancy" framing** — The paper explicitly acknowledges the objective is biased and is transparent about the approximation. The criticism that the paper hides this is inaccurate; the criticism that the bias is unanalyzed is retained in Major weakness #3.

5. **"Prometheus scores are suspect"** — The claim that shorter sequences inflate Prometheus scores is speculative. The paper does not control for length, so this is a valid concern but not a confirmed flaw. I have downgraded it to a minor concern in weakness #4.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Diagnose and fix the stopping classifier.** Report the classifier's accuracy on validation data, plot generation length distributions for ILM alongside the training data, and show that a tunable threshold can match the target length distribution. Evaluate whether changing the threshold affects NLL and Prometheus scores.

2. **Add a FIM-trained ARM baseline** (Bavarian et al., 2022) to the single-segment infilling evaluation. This directly addresses whether ILM's infilling advantage is over MDMs specifically, or over all existing approaches.

3. **Characterize the training objective bias** on a small formal-language dataset where exact marginalization is tractable. Compare the biased ILM objective against an unbiased high-variance estimator and an oracle, quantifying the bias-variance tradeoff.

4. **Include a scaling experiment** training 2–3 additional model sizes (e.g., 25M, 85M, 200M) on LM1B to show whether ILM's text gap with ARMs grows or shrinks with scale.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|-------------------------|
| FiLM (UbOzNf6hGq) | 4.25 (REJECT) | 1 | Much weaker; ILM has a more novel paradigm, better architecture, and stronger results on planning. |
| COrAL (0JjsZC0w8x) | 5.75 (REJECT) | 1,2 | Comparable topic (order-agnostic generation). ILM has a more complete framework and stronger empirical evidence on planning. |
| SequenceMatch (FJWT0692hw) | 6.00 (ACCEPT) | 1,2 | Both have novel ideas with mixed empirical results. SequenceMatch had cleaner theoretical framing; ILM has stronger differentiation on planning but a less rigorous analysis. Comparable. |
| Energy-based Diffusion (sL2F9YCMXf) | 6.75 (ACCEPT) | 1 | Cleaner theoretical analysis and stronger text results. ILM is weaker. |
| RADD (sMyXP8Tanm) | 6.20 (ACCEPT) | 2 | Stronger theoretical contribution and better text results. ILM is weaker. |
| Learning Extrapolative (DQfHkEcUqV) | 4.75 (REJECT) | 2 | Weaker paper with methodological issues. ILM is stronger. |

**Round-1 bracket:** [4.5, 6.5]. The paper is clearly stronger than FiLM (4.25, REJECT) and the Extrapolative Transformations paper (4.75, REJECT), but weaker than EBDLM (6.75, ACCEPT) and RADD (6.20, ACCEPT).

**Round-2 narrowing:** Comparing against COrAL (5.75, REJECT) and SequenceMatch (6.00, ACCEPT): ILM has a cleaner and more complete framework than COrAL, and comparable novelty to SequenceMatch. However, the stopping classifier undershoot (119 vs 205 tokens on Stories) and the unanalyzed biased training objective create real concerns that the COrAL and SequenceMatch papers did not face. The paper falls slightly below SequenceMatch in overall execution rigor.

**Final score: 5.5.** The paper introduces a genuinely novel paradigm and provides a compelling existence proof on planning tasks, which is a real contribution. However, the stopping classifier issue, the absence of a FIM baseline, and the uncharacterized training objective bias collectively prevent the paper from making a fully convincing case for acceptance. The contribution is real but the validation is incomplete in important ways.

MY FINAL SCORE: 5.5
MY FINAL DECISION: Reject