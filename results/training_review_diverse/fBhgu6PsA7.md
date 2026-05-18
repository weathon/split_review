Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes MoFO (Momentum-Filtered Optimizer), a fine-tuning algorithm for LLMs that selects and updates only the parameters with the largest momentum magnitudes at each iteration. By reducing parameter movement through selective updating, MoFO converges closer to the pre-trained initialization than full-parameter fine-tuning, thereby mitigating forgetting of pre-training knowledge. The method requires neither pre-training data (unlike replay) nor loss function modification (unlike regularization), giving it practical appeal. Experiments on Llama-2-7B and TinyLlama-1.1B across instruction fine-tuning and continual fine-tuning show MoFO achieves comparable task performance with substantially less degradation on general capability benchmarks.

## Strengths

1. **Momentum-based parameter selection is empirically validated over alternatives.** Table 5 provides a controlled comparison at α=10% where MoFO (momentum-filtered BCD, GSM8K=45.4) significantly outperforms Gradient-filtered BCD (40.2) and Randomized BCD (35.0), all while maintaining comparable general-capability retention. This directly validates that momentum magnitude is a more effective selection signal than raw gradients for coordinating with Adam's update structure.

2. **Direct geometric evidence that MoFO stays closer to the pre-trained model.** Figure 2 shows that on Pythia-160m, MoFO's final point is approximately 20% as far from the pre-trained model as Adam's final point, while both achieve similar fine-tuning loss. The same figure shows MoFO has lower pre-training loss (Pile), providing direct evidence of knowledge retention for the smaller model. Table 1 then links this reduced distance to better common-sense accuracy retention (MoFO: 31.6 avg vs. Adam: 29.3).

3. **Replay-free and regularization-free design is a practical strength.** MoFO requires neither access to pre-training data (which many open-source LLMs do not release) nor modifications to the loss function (which can impair fine-tuning task performance). Tables 2–3 show MoFO improving or maintaining general capability metrics (e.g., +0.4% average on MetaMathQA) while regularized methods such as L2 still degrade (-0.4% average, with a much larger GSM8K drop of 44.5 vs. MoFO's 47.7).

4. **Consistent benefit across diverse settings.** MoFO's advantage holds across two base models (Llama-2-7B, TinyLlama-1.1B), two instruction fine-tuning datasets (MetaMathQA, Code-Alpaca), and a continual fine-tuning benchmark (TRACE). In TRACE, MoFO achieves OP=41.3 vs. Full FT's 38.4 and combines well with replay (Replay+MoFO: OP=47.0 vs. Replay alone: 45.5).

5. **Ablation study identifies the trade-off clearly.** Figure 4 shows that up to α=20% update fraction, MoFO achieves near-zero forgetting on general capabilities while reaching ~90% of Full FT's GSM8K score, giving practitioners actionable guidance for hyperparameter selection.

## Weaknesses

### Major

1. **The comparison to Half Fine-Tuning (HFT) is confounded by different update fractions.** In Tables 2 and 3, MoFO uses α=10–15% of parameters per iteration while HFT updates ~50%. The paper's own ablation (Fig. 4) shows that increasing the update fraction gradually worsens forgetting — at 40% MoFO's forgetting is significant. Therefore, MoFO's advantages over HFT in the main tables conflate the benefit of momentum-based selection with the benefit of simply updating fewer parameters. The controlled comparison in Table 5 (at matched 10% fraction) does show momentum selection beating random and gradient-based selection, but it compares against Randomized BCD and Gradient-filtered BCD, not HFT specifically. The paper should either (a) add a row to Tables 2–3 with HFT restricted to α% parameters, or (b) explicitly acknowledge this confound and reframe the comparison.

2. **LoRA, a widely-used parameter-efficient fine-tuning method and natural competitor for forgetting mitigation, is absent from the experimental comparison.** The related work (Section 6) mentions LoRA and notes that it "forgets less but learns less," yet no LoRA baseline appears in any experiment. This omission is significant because LoRA is arguably the most common practical alternative that also limits parameter changes during fine-tuning. Including LoRA at multiple ranks would allow readers to assess where MoFO's trade-offs lie relative to this widely-adopted method.

### Minor

1. **The motivation for the momentum-based selection criterion is conceptually simplified.** The paper argues (§2.1) that "momentum directly affects parameter updates, while gradients influence parameter updates indirectly by affecting the momentum." While not incorrect, this framing understates the role of the second-moment normalization in Adam: the actual update is \(\hat{m}_t/(\sqrt{\hat{v}_t}+\epsilon)\), so momentum magnitude alone does not determine update size. A parameter with large momentum but also large variance may receive a smaller update than one with moderate momentum but small variance. The empirical results (Table 5) support the momentum-based rule regardless, but the stated rationale would be stronger if it acknowledged this nuance or adopted a selection criterion based on the full Adam update magnitude.

2. **Pre-training perplexity/loss is not reported for the main Llama-2-7B experiments.** The paper convincingly shows pre-training loss for Pythia-160m (Figure 2b), establishing the mechanism. But for the central Llama-2-7B results (Tables 2–3), forgetting is measured only via general capability benchmarks (MMLU, Commonsense, etc.). While these are reasonable proxies, they are not direct measures of pre-training knowledge retention, and the alternative interpretation that MoFO produces higher benchmark scores partly because it learns less of the fine-tuning task (GSM8K: 47.7 vs. Full FT's 49.4) is not fully ruled out. Reporting perplexity on a held-out pre-training corpus (e.g., a subset of C4 or The Pile) for the main experiments would directly substantiate the core claim.

3. **The convergence analysis addresses a different algorithm than the one proposed.** Theorem 1 proves convergence for a GD version of MoFO that uses gradient magnitude for selection (Algorithm 2), not the momentum-based selection with Adam used in practice. The paper acknowledges this gap ("it seems rather non-trivial to prove the convergence of the original version of MoFO"), which is honest, but it means the theoretical contribution does not directly support the proposed algorithm. A more relevant analysis — e.g., bounds on the distance to the pre-trained solution — would better serve the paper's claims about forgetting mitigation.

4. **No discussion of computational overhead.** Top-k selection per parameter block requires sorting, which has non-negligible cost for large models. The paper states the method partitions parameters "to reduce computational complexity" but provides no wall-time comparison or complexity analysis. Given that MoFO's advantage over Full FT or HFT includes both forgetting mitigation and potential computational savings (fewer parameters updated), a timing comparison would be valuable for practitioners.

### Trivial

- The toy example (Section 5) is too simple (a factorized loss with orthogonal attractors) to provide genuine insight into LLM fine-tuning dynamics. It illustrates a possible mechanism but is disconnected from the complexity of real LLM loss landscapes. The paper would not be weakened if this section were shortened or removed.
- Algorithm 1's pseudocode nests gradient computation inside a partition loop, which mathematically describes obtaining gradients per partition but does not reflect that all gradients come from a single backward pass in implementation. This is a common convention in optimization papers but could be clarified.

## Nice-to-Haves

- Pre-training perplexity for the Llama-2-7B experiments (MetaMathQA and Code-Alpaca) would directly substantiate the forgetting-mitigation claim.
- A controlled comparison where HFT is restricted to α=10–15% update fraction, added to Tables 2–3.
- Wall-time comparison against Full FT, HFT, and LoRA.
- A simple heuristic or sensitivity analysis for choosing the update fraction α (e.g., "start at 10%, increase if fine-tuning performance is low"), rather than reporting task-specific tuned values (15%, 10%, 5%) without explanation.
- An empirical analysis (e.g., a scatter plot) showing the correlation between momentum magnitude and actual Adam update magnitude, to strengthen the motivation.

## Removed Points

- **Criticism about Algorithm 1's backward-pass loop being "not how backpropagation works."** This is a standard notational convention in optimization papers — the mathematical expression of per-partition gradients does not imply separate backward passes. The pseudocode is not misleading within the norms of the field.
- **Criticism that the term "catastrophic forgetting" may overstate the phenomenon.** The term is standard in the literature and the paper's usage is appropriate for its context.
- **Criticism about missing training epochs for main experiments.** The paper references `sec_training_detail` for implementation details; these were in the appendix, which the parser stripped.
- **Generalizability/demands for Y/domain Z coverage that would make the paper a different, broader paper.** The paper is scoped to single-task and continual fine-tuning of LLMs, which is a well-defined scope.

## Novel Insights

The key insight from the reviews is the tension between the paper's simplified conceptual framing (momentum > gradients because it "directly affects updates") and the more complex reality of Adam's per-coordinate normalization. The empirical results in Table 5 resolve this tension in MoFO's favor, but the paper would benefit from either adopting the more principled selection criterion (full Adam update magnitude) or providing empirical evidence (e.g., correlation plots) that momentum magnitude is a sufficient proxy. Additionally, the HFT comparison confound highlights a common weakness in papers comparing sparsity-based methods: claims about "better selection strategy" must be disentangled from claims about "fewer updates being helpful" through controlled experiments.

## Suggestions

1. In the main tables, add a controlled HFT variant that updates α% of parameters, or at minimum explicitly acknowledge the update-fraction confound.
2. Add pre-training perplexity measurements for the Llama-2-7B experiments to directly support the forgetting-mitigation claim.
3. Include LoRA as a baseline in the experiments (at ranks 8, 16, 32) to provide a complete picture of MoFO's position relative to existing PEFT methods.
4. Provide a wall-time comparison or complexity analysis of the top-k selection overhead.
5. Strengthen the motivation by either (a) replacing the selection criterion with |m̂/(√v̂+ε)| and comparing empirically, or (b) showing a scatter plot that momentum magnitude strongly correlates with update magnitude in practice.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>