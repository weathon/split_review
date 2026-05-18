Now I have all the information I need. Let me compile the final review.

## Summary

The paper proposes an adaptation recipe (attention mask annealing + shift operation) to convert AR language models (GPT-2, LLaMA2, 127M–7B) into diffusion language models (DiffuGPT, DiffuLLaMA) with less than 200B additional training tokens. The adapted models achieve state-of-the-art results among existing DLMs, demonstrate inference speed advantages for long sequences, and show in-context learning capabilities for the first time in a diffusion language model.

## Strengths

- **Novel and practical adaptation recipe from AR to DLMs via attention mask annealing and shift operation (Sections 3.2–3.3):** The paper identifies and bridges two fundamental architectural differences between AR and diffusion objectives — causal vs. bidirectional masking, and the next-token prediction shift. The mask annealing procedure (progressively opening the causal mask) and retained shift operation are well-motivated engineering contributions that enable leveraging existing large-scale AR model weights.

- **First 7B-parameter DLM with SOTA results among existing DLMs (Table 1):** DiffuLLaMA-7B outperforms all prior DLMs (Plaid 1B, SEDD Large, MD4) across a broad set of reasoning, commonsense, and infilling benchmarks. The training loss curve (Figure 2) shows a clear scaling trend from 127M → 355M → 7B, confirming that increasing model size improves DLM performance.

- **Inference speed advantage over AR models for long sequences (Figure 5):** With 256 diffusion steps, DiffuLLaMA matches or beats LLaMA2-7B single-batch decoding time for sequences ≥1024 tokens. This is a practically meaningful result given the memory-bound nature of KV-cached AR decoding at long lengths.

- **Comprehensive evaluation beyond zero-shot perplexity (Section 4.2, Table 1):** The paper evaluates across 10+ tasks including reading comprehension, commonsense reasoning, math, code infilling, and story infilling — a significant expansion over prior DLM work that focused mainly on perplexity.

- **Ablation validation on GSM8K-symbolic (Table 3):** A controlled experiment where GPT-2 weights are fine-tuned on the same data with AR loss vs. discrete diffusion (DD) loss shows DD outperforming AR (45.4 vs. ~44.5 for small, 49.7 vs. ~47.8 for medium). Removing shift operation or attention mask annealing degrades performance, validating the design choices.

- **First demonstration of in-context learning in a DLM (Table 2):** DiffuLLaMA shows improvement from zero-shot to few-shot settings on math tasks (MAWPS, SATMATH) and benefits from self-consistency — capabilities previously associated primarily with large AR LMs.

## Weaknesses

### Major

- **The central comparison "DiffuGPT outperforms GPT-2" is confounded by additional training data.** DiffuGPT is initialized from GPT-2 weights and then trained on 30B tokens from FineWeb, which the paper describes as "an improved corpus than OpenWebText." The comparison against the original GPT-2 (trained on WebText) conflates the benefit of the diffusion objective with the benefit of additional training on a higher-quality dataset. A controlled baseline — GPT-2 continued on the same 30B tokens with the standard AR objective — is absent. This weakens the paper's headline claim. The GSM8K-symbolic ablation provides some controlled evidence, but only at the fine-tuning scale, not at the pre-training scale where the main results are reported.

- **The shift operation's compatibility with the formal diffusion ELBO is not rigorously justified.** Section 3.3 retains the AR models' next-token prediction shift: the output logit at position $i$ predicts token $i+1$ rather than the clean token at position $i$. The diffusion loss (Eq. 6) is derived assuming the model predicts $\mathbf{x}_0^n$ — the original token at the same position. The paper claims to "align prediction targets" but provides no derivation showing that the shifted loss corresponds to a valid ELBO for the absorbing discrete diffusion process described in Section 2. The sampling procedure (Algorithm 2) compensates with manual shifting and prepending a start token, which is a plausible practical fix but not a formal guarantee. This is not fatal to the paper's contributions (the empirical results stand on their own), but it means the work is better described as an iterative denoising procedure adapted from AR weights rather than a diffusion model in the strict formal sense defined in Section 2.

### Minor

- **Loss metric incomparability across model types for multiple-choice tasks.** For commonsense reasoning tasks (HellaSwag, WinoGrande, etc.), the paper uses the diffusion ELBO (Eq. 6) for DLMs and standard cross-entropy for AR models to score answer choices. These are not directly comparable: the diffusion loss is an upper bound on negative log-likelihood and depends on stochastic sampling of timestep $t$, while the AR loss is exact. The paper acknowledges this issue (Section 4.2: "discrepancies between continuous diffusion, discrete diffusion, and autoregressive loss still hinder fair comparisons") but proceeds with cross-type comparisons anyway. For DLM-to-DLM comparisons the metric is consistent and trustworthy; the issue mainly affects DLM vs. AR comparisons.

- **The 7B model (DiffuLLaMA) is trained on only 65B tokens vs. LLaMA2's ~2T tokens.** The paper honestly acknowledges that "DiffuLLaMA's performance still falls short of the LLaMA2 model" and attributes this to insufficient training. This makes the comparison against LLaMA2 uninformative — the underperformance is expected and doesn't reflect on the diffusion approach. The paper would benefit from training the 7B model to a more comparable compute budget or framing this as a preliminary scaling result rather than a competitive evaluation.

- **Attention mask annealing is omitted for the 7B model** with the justification that a small-model ablation showed "minimal impact." Given the different scale and the fact that the ablation is on a fine-tuning task (GSM8K-symbolic) rather than pre-training, this conclusion may not transfer. The paper acknowledges this but does not verify it.

### Trivial

- The unconditional generation perplexity uses GPT-2 large as the oracle, which may favor models adapted from the GPT-2 family over models trained independently. A multi-oracle evaluation would be more persuasive.

## Nice-to-Haves

- A controlled pre-training experiment: continue GPT-2 on the same 30B FineWeb tokens with the AR objective and compare against DiffuGPT. This would cleanly isolate the benefit of the diffusion objective.
- Variance reporting for the diffusion-loss-based ranking in multiple-choice tasks, given the stochastic timestep sampling.
- Comparison against FIM-trained AR models (e.g., CodeLlama) for infilling tasks, to distinguish the benefit of diffusion from the benefit of bidirectional context.

## Removed Points

The following points from the reviewers were removed after verification against the paper:

- **Harsh critic's Point 1 characterization as "fatal/structural":** The claim that the adapted model "may not be a valid diffusion language model" is overstated. The shift operation is a practical reparameterization that the paper explains in Section 3.3 — output at position $n$ is trained to predict token $n+1$, and this mapping is inverted at sampling time by shifting back and prepending a start token. While a formal ELBO derivation would strengthen the paper, the approach is well-specified and the model demonstrably performs the denoising task. This is a minor theoretical gap, not a structural flaw.

- **Strength Finder's generic strengths** (e.g., "the paper identifies a practical bottleneck," "comprehensive evaluation") — These are retained in condensed form since they are backed by specific evidence.

- **The claim that "DiffuGPT outperforms both SEDD and MD4 models"** is retained as a valid strength because these DLMs are compared under consistent evaluation conditions.

## Novel Insights

The most interesting finding synthesized across the reviews is that the paper's adaptation recipe, while lacking formal theoretical grounding as a valid diffusion model, works surprisingly well in practice. This creates an interesting tension: the practical recipe (retain AR shift operation, anneal causal mask) seems to produce models that behave like diffusion models and outperform other DLMs, even though the formal connection to the diffusion ELBO is hand-waved. This suggests that the community may benefit from a deeper theoretical investigation into when and why next-token prediction AR losses can be repurposed as denoising objectives. Additionally, the finding that DLMs can perform in-context learning (Table 2) — a capability previously tied to AR training — suggests that the emergence of ICL may depend more on scale and data diversity than on the specific left-to-right generation order.

## Suggestions

1. **Run the controlled experiment that would make the paper's central claim rigorous:** Continue-train GPT-2 small on the same 30B FineWeb tokens with the standard AR objective, and compare it directly against DiffuGPT on all tasks. If DiffuGPT still wins, the diffusion advantage is cleanly demonstrated. If not, adjust the claims accordingly.
2. **Provide a formal derivation or at minimum a clear argument** for why the shifted loss function (output at position $n$ trained to predict $\mathbf{x}_0^{n+1}$) corresponds to a valid ELBO for the absorbing discrete diffusion process, or explicitly characterize the adapted model as a related but distinct class of iterative denoising models.
3. **For the multiple-choice evaluations, use a consistent scoring method** across model types — either generation-based accuracy for both, or explicitly note the caveat when comparing ELBO-based scores with exact log-likelihoods.
4. **Train the 7B model on more tokens** (or include a smaller model trained to convergence on a comparable budget) to make the AR comparison meaningful at the 7B scale.

## Score and Decision

**Calibration anchors:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| Interpolating AR and Discrete Diffusion (tyEyYT267x) | 8.0 (Accept) | Much stronger theoretical grounding and controlled experiments; our paper is weaker on rigor but has practical scaling to 7B |
| Scaling up Masked Diffusion Models (WNvvwK0tut) | 6.5 (Accept) | Better scaling law analysis and compute-controlled comparisons; our paper lacks scaling laws but reaches larger model sizes |
| RADD / Your Absorbing Discrete Diffusion (sMyXP8Tanm) | 6.2 (Accept) | Stronger theoretical contribution (reparameterization, formal unification); our paper has broader empirical scope but weaker theory |
| SEDD (71mqtQdKB9) | 6.6 (Reject) | Strong theory but incomplete experiments; our paper has more complete evaluations but weaker theoretical foundation |
| Diffusion LMs with Scaling and Instruction-Finetuning (Qn4HEhezKW) | 5.0 (Reject) | Similar adaptation approach and similar issues with controlled comparisons; our paper trains larger models and evaluates on more tasks |
| Abstract Rules for Reasoning (DLBlR0rea5) | 4.5 (Reject) | Limited scope; our paper is more practically significant |

The paper has genuine contributions — the adaptation recipe is novel and produces the largest DLM to date with demonstrated practical advantages (speed for long sequences, in-context learning, infilling). However, the strongest claimed result ("DiffuGPT outperforms GPT-2") is compromised by a confounded comparison, and the theoretical foundation for the adaptation is incomplete. Relative to the anchors, the paper is substantially stronger than the 5.0-level work but falls short of the 6.5-level work in terms of experimental rigor and controlled evidence.

**Score: 5.5**

**Decision: Reject** — The paper's headline claim is not adequately supported due to the confounded comparison. The contributions are real and the direction is promising, but the evidence as presented does not meet the bar for acceptance. A major revision with a controlled pre-training comparison could strengthen the paper significantly.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>