- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6
Now I have thoroughly verified the paper content against all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper analyzes the light decoder paradigm for neural VRP solvers (e.g., POMO), identifying the simplistic decoder as the key bottleneck limiting OOD generalization. It argues that the encoder must pack all decision-relevant information into static embeddings (high information density), while the shallow decoder cannot effectively exploit this richness. The proposed remedy — ReLD — adds an identity mapping (direct context injection) and a feed-forward layer to the decoder, along with a distance heuristic and variable-attribute training. Experiments across cross-size, cross-problem (16 VRP variants), and real-world benchmarks (CVRPLib Set-X/XXL) show consistent improvements, substantially narrowing the gap between light and heavy decoder paradigms.

---

## Strengths

1. **Evidence that the decoder is the bottleneck (Table 2 + Section 4.4).** The fine-tuning experiment shows that decoder-only fine-tuning on large instances yields poor results compared to encoder or full fine-tuning; separately, increasing decoder capacity (POMON+FF) significantly improves generalization while increasing encoder capacity (POMON-Enc+) does not. The ablation cleanly isolates that identity mapping primarily boosts OOD size generalization while the feed-forward layer primarily improves in-distribution learning, and their combination yields the best of both. This directly supports the paper's core thesis with controlled evidence.

2. **Simple modifications yield large, consistent gains across many benchmarks.** ReLD reduces the POMO optimality gap on CVRP100 from 0.95% to 0.33%, on CVRP200 from 2.20% to 0.67%, and on CVRP500 from 3.99% to 1.10% (Table 3). On 16 VRP variants (Table 5), ReLD-MTL and ReLD-MoEL outperform all light-decoder baselines on every variant, even surpassing LKH3 on VRPL. These gains are not confined to one scale or one problem type.

3. **Clever experiment demonstrating static embeddings are information-rich (Table 1).** When the encoder processes a graph with 50% additional irrelevant nodes, POMO's performance degrades only marginally (0.02% on CVRP100), while LEHD (heavy decoder) loses 1.56%. This empirically supports the claim that the encoder learns embeddings useful for multiple sub-problems, even if the default decoder fails to exploit them.

4. **Generalization to real-world benchmark instances at very large scales (Table 4).** ReLD-MoEL+ achieves the best results on CVRPLib Set-X across all instance-size ranges and shows significant margins of improvement on Set-XXL instances with 3000–16000 nodes, well beyond the training distribution (40–100).

---

## Weaknesses

### Fatal

None.

### Major

1. **Cross-size comparison to heavy decoders is confounded by training distribution differences.** ReLD is trained on instances of size 40–100 (line 197). The comparisons against LEHD and BQ on CVRP1000 use results taken from their original papers (superscript * in Table 3), where those models were trained on larger sizes (e.g., LEHD on 100–500). Consequently, LEHD's superior performance on CVRP1000 could partly reflect a training distribution advantage rather than architectural superiority. The paper acknowledges that "a performance gap persists" (line 206) but does not isolate whether this gap is due to training data or decoder architecture. This weakens the headline claim about "narrowing the gap with the heavy decoder paradigm" (line 24). The core contribution (improving light decoders) remains intact because the in-house comparisons against POMO and the ablations are fair and controlled — but this cross-size comparison needs more careful treatment.

### Minor

1. **No variance or statistical significance reporting.** All experimental results appear to come from a single training run with no mention of multiple seeds. Given that RL-based training is stochastic, variance over at least 3–5 independent runs should be reported for the main tables. The improvements are large and consistent, so the conclusions are likely robust, but the absence of variance information limits evidential strength.

2. **Table 1 experiment's interpretation is slightly overstated.** The experiment adds irrelevant nodes from the *same distribution* and tests robustness to noise, which is valuable — but the paper interprets it as showing that "static embeddings contain valuable information to solve various sub-problems." Testing with out-of-distribution noise (e.g., different coordinate distributions) would more directly support the sub-problem claim. As presented, the experiment is suggestive but not definitive for the intended interpretation.

3. **"Identity mapping" naming is imprecise.** The function IDT(·) in Eq. 10 is defined as \( h_{\tau_{t-1}} + W^{\text{IDT}}\mathcal{D}_t \), which includes a learned projection of dynamic features. This is a residual/skip connection, not a true identity mapping. The concept is clear, but the label is misleading — "direct context injection" or "residual context connection" would be more accurate.

### Trivial

1. The KV-cache analogy's framing that COP context is "diminishing" (line 87) is slightly imprecise: while the set of unvisited nodes shrinks, the remaining context (vehicle capacity, current location, etc.) is dynamic and still relevant. This does not affect the method or results.

---

## Nice-to-Haves

- **Directly test the information bottleneck hypothesis.** The paper hypothesizes that static embeddings have "high information density" that a simple decoder cannot exploit. This could be investigated via probing classifiers, mutual information estimation, or embedding-space visualizations with and without the proposed decoder modifications.
- **Isolate the training distribution effect in cross-size comparisons.** Retraining LEHD (or a proxy heavy decoder) on the same 40–100 size range, or training ReLD on a distribution that includes larger sizes, would cleanly disentangle architecture from training data.
- **Hyperparameter sensitivity.** The decoder's new parameters (\(W^{\text{IDT}}, W_1, W_2\)) are trained jointly; a brief study of sensitivity to learning rate, initialization, or FF dimension would increase confidence.
- **Computational cost breakdown.** The paper claims decoder modifications are cheap because they are independent of node count (true asymptotically), but a breakdown of encoder vs. decoder per-step runtime would let readers verify the overhead is negligible in practice.

---

## Removed Points

Points that were flagged but removed from the main review:

- **Criticism about Table 4 being presented as an image in the PDF.** This is a parser artifact; the original submission presumably contains readable tables. Removed per Hard Rules.
- **Claim that LEHD's underperformance on Set-X "deserved a brief discussion."** The paper notes this finding (line 225: "Interestingly, heavy decoder methods like LEHD show inferior performance on Set-X instances") but does not explain it. This is an observation, not a weakness — the paper's focus is its own method, not explaining another method's behavior. Removed.
- **Criticism that the fine-tuning experiment's results could be due to decoder having fewer parameters.** The paper partially addresses this via the ablation study (Sec 4.4, POMON-Enc+ vs. POMON+FF comparison), and the claim is a competing explanation rather than a demonstrated flaw. Removed.
- **Criticism about "missing computational cost analysis" and "hyperparameter sensitivity."** These are framed as missing sections; they are moved to Nice-to-Haves as suggestions for strengthening rather than weaknesses of the current submission.
- **Harsh Critic's suggestion to directly test the bottleneck via mutual information/probes.** Moved to Nice-to-Haves.
- **Any mention of missing appendix, proofs, or references.** Per Hard Rules, these are parser artifacts.

---

## Novel Insights

The Strengths Finder appropriately identifies the paper's main contributions but does not surface a genuinely novel observation beyond what the paper itself articulates. The core insight — that the bottleneck in light-decoder VRP solvers is the decoder's insufficient capacity to exploit dense static embeddings, and that simply adding a residual connection and non-linear processing to the decoder yields outsized generalization gains — is the paper's own. The cross-reference between KV caches in LLMs (expanding context) and static embeddings in COPs (diminishing/selective context) is a useful conceptual framing that helps motivate the architecture. No additional novel synthesis emerges from the reviews.

---

## Suggestions

1. **Report results over 3–5 random seeds** with mean and standard deviation for the main tables (at least Tables 3 and 5).
2. **Acknowledge and address the training distribution confound** in cross-size comparisons more explicitly. Either retrain LEHD/BQ on the same distribution (40–100) or train ReLD on a broader range (e.g., including sizes up to 500) to enable a fairer comparison.
3. **Rename "identity mapping"** to something more precise (e.g., "residual context connection" or "direct context injection") to avoid confusion.
4. **Tighten the language around Table 1's interpretation** — frame it as testing robustness to irrelevant nodes / noise, which is a useful finding in its own right.

---
