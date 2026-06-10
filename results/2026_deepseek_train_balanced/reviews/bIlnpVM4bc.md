## Summary

Samba proposes a simple hybrid architecture that interleaves Mamba (SSM), SwiGLU MLP, and Sliding Window Attention (SWA) layers for language modeling. The key claims are: (1) this specific layer-wise arrangement outperforms both pure Transformer and pure SSM architectures, (2) it achieves strong length extrapolation (improved perplexity up to 1M tokens in zero-shot and perfect memory recall at 256K after fine-tuning), and (3) it provides significant throughput advantages over Transformers for long sequences. The paper provides extensive ablations at 1.3–1.7B scale and scales to 3.8B.

## Strengths

1. **Controlled architecture ablation at 1.7B scale is thorough and well-executed**: Table 2 compares 6 architectures (Samba, Mamba-SWA-MLP, Mamba-MLP, Mamba, Llama-3, Mistral) trained on the same 230B tokens of Phi2 data with matched parameter counts (~1.7B). Samba achieves the highest average score (54.33) across 15 benchmarks. This controlled comparison isolates the effect of the layer-wise arrangement, directly supporting the claim that Samba's specific interleaving is superior at this scale.

2. **Zero-shot perplexity extrapolation with improving trends is genuinely impressive**: Table 3 shows Samba 421M achieves perplexity of 10.06 (4K), 9.65 (8K), 9.57 (16K) — monotonically *decreasing* with context length — whereas Llama-2 explodes from 11.14 to 249.03. This holds at both 438M and 1.3B scales. The extrapolation to 1M tokens on Proof-Pile (Figure 4) at 256× the training length is a strong result, reinforced by the Samba-NoPE ablation showing RoPE is critical.

3. **Passkey Retrieval at 256K after only 500 steps of 4K fine-tuning**: Figure 5 shows Samba 1.7B maintains perfect retrieval across all key positions up to 256K while Mistral 1.6B (SWA-only) fails entirely beyond its training length. The paper reports near-perfect retrieval at just 150 training steps versus Mistral plateauing at ~30%. This directly demonstrates that the hybrid's recurrent states carry useful signal across very long distances.

4. **Concrete throughput measurements with clear methodology**: The paper reports 3.73× faster prompt processing (128K prompts) and 3.64× faster decoding (64K generation) versus Llama-3 1.6B, measured on a single A100 with bfloat16, repeated 10 times. These are specific, reproducible efficiency numbers.

5. **Systematic exploration of the design space at smaller scales**: Beyond the main architecture comparison, the paper compares against alternative linear recurrent layers (GLA, RetNet, Mega-S6), tests full-attention hybrids (Table 5, demonstrating they cannot extrapolate), and shows Samba works well with very few KV heads (Table 6, down to 1 KV head). These ablations provide useful guidance for future hybrid designs.

## Weaknesses

### Major

1. **The headline comparison at 3.8B is a controlled architecture swap with Phi-3-mini, but the paper frames it as "substantially outperforming SOTA" without qualifying this**: Samba-3.8B-IT is trained on the same data and with the same multiphase pretraining and post-training recipes as Phi-3-mini (lines 116–117). The comparison in Table 1 is therefore an *architecture* comparison — replacing Phi-3's Transformer with Samba's hybrid yields better results on MMLU (71.9 vs 68.8), GSM8K (87.6 vs 82.5), HumanEval (62.8 vs 58.5), and GovReport (18.9 vs 14.4). This is a legitimate and valuable result, but the abstract's claim that Samba "significantly outperforms state-of-the-art models across a variety of benchmarks" reads as a claim against the broader model landscape (Gemma, Qwen, StableLM, etc.), not just against the architecture that was directly replaced. The paper should clearly state this is an apple-to-apple architecture comparison, not a claim of dominance over the entire SOTA landscape.

2. **The "substantially outperforming models up to 8B parameters" claim is not supported by evidence visible in the main paper**: The abstract (line 22) references an appendix table (\Cref{tab:benchmark-comparison-3.5}) for this claim. The only 8B-scale comparison visible in the main body is the Phonebook task (Figure 6), where Samba-3.8B-FT (fine-tuned 100 steps on Phonebook) closes most of the gap with Llama2 7B (a 2023 model, not fine-tuned on this task). While this is a reasonable result, it supports a narrower claim. The broad "outperforms up to 8B" claim should either be backed by results in the main paper or tempered.

3. **No hybrid architecture comparison at the 3.8B scale**: The paper's central claim — that Samba's *specific* layer-wise pattern (Mamba-MLP-SWA-MLP) is superior to alternatives — is thoroughly supported at 1.3–1.7B, but no Mamba-SWA-MLP or pure Mamba baseline is presented at 3.8B. The reader cannot tell whether the advantage of Samba's particular arrangement persists at larger scale or whether any hybridization would achieve similar results. Given the 3.8B model carries the headline claims, this is a notable gap.

### Minor

4. **The "unlimited context" title and framing overstate what the 1M-token experiment measures**: The 1M-token perplexity evaluation (Section 3.3, Figure 4) uses a sliding window of 4096 tokens (line 281). This measures whether the model maintains stable representations across very long sequences, not whether it can retrieve or use information from 1M tokens ago. The paper's Passkey Retrieval experiment (which does test functional memory use) goes up to 256K, not 1M. The title "Unlimited Context Language Modeling" and phrasing like "infinite length extrapolation" (line 20) should be qualified — "extreme length extrapolation" would be more precise. The sliding-window result is still valuable (representational stability at 256× training length is non-trivial), but the framing invites misinterpretation.

5. **The difference between Samba and Mamba-SWA-MLP in Table 2 is modest and may benefit from variance reporting**: Samba averages 54.33 vs Mamba-SWA-MLP's 53.77 across 15 tasks — a 0.56-point advantage. Mamba-SWA-MLP actually beats Samba on individual tasks (PIQA, WinoGrande, SIQA, GSM8K). Without variance estimates or multiple seeds, it is unclear whether this average advantage is robust. The paper states perplexity results have ±0.3% fluctuation (Table 3 caption) but no such qualification appears for the downstream evaluation.

6. **The Phonebook comparison mixes fine-tuned and base models without sufficient disambiguation**: Samba-3.8B-FT is fine-tuned on the Phonebook task itself (100 steps), while the comparison baselines (Phi3 base, Llama2 7B) are zero-shot base models. The paper states this in the text but the figure caption and discussion could more clearly separate what is fine-tuning advantage versus architectural advantage. The result that Samba can be fine-tuned to match a larger full-attention model is still a genuine contribution, but the presentation risks being read as a base-model comparison.

### Trivial

None worth enumerating. The paper is well-written; formatting artifacts present in this parsed version are parser issues, not author errors.

## Nice-to-Haves

- Compare with a similarly scaled pure Mamba and Mamba-SWA-MLP at 3.8B to confirm the architecture choice generalizes (acknowledging the cost).
- Clarify what "preview" in "Samba-3.8B-IT (preview)" means — the paper says it uses the "original Phi-3-mini post-training recipe" but the label is ambiguous about whether this is a final or intermediate model.
- A brief discussion of how Samba's design differs from Jamba (different layer-level pattern, SWA vs full attention, scaling strategy) would help contextualize the contribution among hybrid SSM-attention models.

## Removed Points

These were flagged in the inputs but removed for the reasons stated. Treat them with caution.

- **No comparison with Jamba**: Jamba is cited in the paper (lieber2024jamba, line 321) at a much larger scale (12B). Direct comparison is not feasible, and omitting it is not a weakness.
- **No multi-seed results**: Single-seed training is the norm in large-scale LM training at these scales. Requesting variance reporting is a generic expectation applicable to nearly all papers in this area.
- **Training data composition not fully described**: "The same data set used by Phi3" is an adequate description for this venue; many LLM papers reference proprietary datasets similarly.
- **"SWA window size tied to engineering consideration" as a weakness**: The paper transparently explains this choice (lines 80–81: "choose the 2048 sliding window size for efficiency consideration"). This is transparency, not a flaw.
- **"No full-attention baseline on Passkey Retrieval"**: Evaluating full attention at 256K context length would require quadratic compute, making this impractical. This is scope creep.
- **"Mamba's increasing perplexity at 1M is an odd inclusion"**: The paper's observation (line 285) about Mamba's slowly increasing perplexity is simply reporting a baseline behavior, not a contradiction of their claims.

## Novel Insights

The reviews surface two observations that go beyond the paper's own contributions. First, the controlled comparison at 3.8B (same data, same recipe as Phi-3-mini) means the results are primarily an *architectural* comparison — a genuine contribution, but narrower than the broad "outperforms SOTA" framing suggests. Second, the sliding-window caveat on the 1M perplexity evaluation highlights a recurring ambiguity in the length extrapolation literature: papers often conflate "the model does not崩溃 on very long sequences" with "the model can functionally use very long context." Samba's Passkey experiment (256K) does address functional use, but at a shorter range than the perplexity experiment (1M). Separating these two evaluation dimensions more carefully would strengthen not just this paper but the field's standard practices.

## Suggestions

1. Reframe the abstract and introduction to make clear that the 3.8B comparison with Phi-3-mini is an architecture-controlled comparison (same data, same recipe), and qualify the "substantially outperforms state-of-the-art" language.
2. Either include a 3.8B Mamba-SWA-MLP baseline or explicitly state that the architecture choice at 3.8B is inherited from the 1.7B ablations (and acknowledge the extrapolation).
3. Add a brief statement in the abstract clarifying that the 1M perplexity evaluation uses a sliding window, and distinguish it from the Passkey Retrieval experiment which tests functional long-context use.
4. Clarify the "preview" designation and move the Samba-3.8B (June) results into the main paper.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>