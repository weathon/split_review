Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper provides a comprehensive empirical analysis of learning dynamics differences between Transformers and modern state-space models (SSMs like Mamba, Hyena, Mamba2, DeltaNet) on two synthetic benchmarks — multi-query associative recall (MQAR) and copying. The central finding is that SSMs exhibit a critically narrow learning-rate window compared to Transformers, and that prior empirical comparisons that reported SSMs as fundamentally less expressive on these tasks were confounded by suboptimal hyperparameter tuning. The paper further documents opposing scaling strategies (width helps SSMs, depth helps Transformers), identifies the 1D convolution as the mechanistic source of Mamba's single-layer expressivity advantage, and shows that DeltaNet achieves Transformer-level LR robustness.

## Strengths

- **Comprehensive and well-controlled empirical study.** Over 3,000 runs (~20,000 GPU hours) across two tasks, six architectures (Attention, Mamba, Mamba2, Hyena, DeltaNet, gated variants), and extensive LR sweeps. This breadth makes the observed patterns — narrow LR window, width-over-depth scaling — unlikely to be artifacts.

- **Figure 2 is a standout result.** By simply expanding the LR grid beyond what prior work (Arora et al., 2023) used, the paper shows Mamba solving MQAR at sequence length 512 with hidden size 64 (~100% accuracy) where the prior grid gave near-zero accuracy. This directly demonstrates that the earlier "failure" was an optimization confound, not an expressivity limit.

- **Clean architectural ablation in Table 2.** Removing the 1D convolution from 1-layer Mamba drops accuracy from 99% to 2% (identical to 1-layer Attention), and adding a convolution to Attention's QKV projections raises it to 99%. This pins down the specific mechanism behind Mamba's single-layer advantage.

- **Opposing scaling strategies with controlled parameter count.** Table 1 shows that Mamba 12×1408 (150M params, width-scaled) achieves 100% on copying while Mamba 24×1024 (150M params, depth-scaled) achieves only 16% — holding total parameters fixed. This is a clean causal demonstration that SSMs require width scaling, not depth matching.

- **DeltaNet finding is forward-looking.** Figure 7 shows DeltaNet maintaining ≈90% accuracy across the full LR sweep, while Mamba and Mamba2 peak only at single LR values. This provides evidence that the instability can be architected away, with a plausible mechanistic hypothesis (Householder vs. decay-gate A matrices).

## Weaknesses

### Major

1. **Central thesis overreach relative to the paper's own evidence.** The introduction states: *"Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics."* Yet the paper's own Section 4 and Table 2 show that a 1-layer Transformer *cannot* solve MQAR at any width, while a 1-layer Mamba (with convolution) can — a genuine expressivity gap. The paper correctly identifies the convolution as the source, but this means the architectures *do* differ in expressive power in the single-layer regime. The 2-layer evidence (Figure 2) strongly supports optimization as a bottleneck, and the central thesis is reasonable as a claim about the 2-layer setting that the community typically studies. But as stated without qualification, the thesis is contradicted by the paper's own single-layer results. The abstract uses the more measured phrasing *"not just in their expressivity but in their fundamental learnability properties"* — the introduction should be adjusted to match this nuance.

### Minor

2. **Induction-head claim is speculative.** Section 6 claims the loss bump in 1-layer Attention *"resembles the formation of an induction head circuit"* and that the model *"attempts to form induction heads."* The only evidence is the shape of the loss curve (a sudden drop and recovery). No attention-pattern analysis, causal tracing, or head-activation visualizations are provided. The paper uses appropriately hedged language (*"resembles," "hypothesize," "attempts"*), which is acceptable, but the introduction bullet point presents this as a key finding without the same hedging. Either add mechanistic evidence or downgrade the claim from a bullet-point finding to an observation in Section 6.

3. **Limited to synthetic benchmarks.** The paper acknowledges this (Section 8: *"Validating these dynamics on downstream language modeling tasks is a critical next step"*), but the central recommendation — *"future research on efficient sequence models should treat optimization stability as a first-class objective"* — would be substantially strengthened by even one modest-scale language modeling experiment (e.g., perplexity on WikiText-103). The paper is transparent about this gap, but it constrains the generality of the conclusions.

4. **No gradient diagnostics for the instability claim.** The paper attributes the narrow LR window to vanishing/exploding gradients inherited from classical RNNs but provides no gradient statistics (e.g., gradient norms across training steps, spectral analysis of the recurrent Jacobian). A simple diagnostic plot would substantially strengthen the mechanistic claim. The DeltaNet discussion also hypothesizes about Householder matrices avoiding vanishing gradients but provides no gradient-norm analysis to confirm.

### Trivial

5. **DeltaNet results limited to dimension ≤256.** The paper reports this as an implementation limitation. It is unclear whether the stability trend holds at larger dimensions (512, 1024). The authors should state explicitly whether they expect the trend to hold and why.

## Nice-to-Haves

- Test whether the narrow LR window widens under learning rate schedules (e.g., cosine decay with warmup), which are standard practice and designed to mitigate instability.
- Provide a gradient-norm analysis (by layer, across training steps) for Mamba vs. Attention to directly support the vanishing/exploding gradient attribution.
- Evaluate DeltaNet at larger model dimensions once the implementation constraint is resolved.

## Removed Points

- *Critic's claim that Mamba's name was misspelled or that a referenced baseline does not correspond to currently available systems.* The paper cites standard, released architectures (Mamba, Mamba2, DeltaNet, Hyena). Per the hard rules, any criticism questioning the existence or availability of cited models is removed.
- *Formatting/style nitpicks (e.g., overlapping points in Figure 4, request for more detailed legends).* Removed as minor presentation issues that do not affect substance.
- *Request for analysis of batch size, optimizer hyperparameters (β₁, β₂, ε), or LR schedule variations.* These are reasonable suggestions but not standard requirements for an empirical paper of this scope; they are moved to Nice-to-Haves.
- *Claim that the paper "does not test or discuss whether the observed optimization instability persists in more realistic settings."* The paper explicitly discusses this limitation in Section 8 ("Validating these dynamics on downstream language modeling tasks is a critical next step"). The limitation is acknowledged, not ignored.
- *Strength Finder's generic strengths about "large-scale systematic empirical study" and "replication with prior work's code."* These are genuine but generic; retained only in condensed form under Strengths.

## Novel Insights

None beyond the paper's own contributions. The individual results (narrow LR window, width-vs-depth scaling, convolution as expressivity enabler, DeltaNet stability) are all well motivated and clearly presented in the paper itself.

## Suggestions

1. Revise the central thesis in the introduction to match the more measured language of the abstract: *"a crucial differentiator lies not just in their expressivity but in their fundamental learnability properties"* rather than *"not in terms of expressive power but mainly because of their optimization dynamics."* This resolves the inconsistency with the single-layer findings.

2. Either (a) add attention-pattern visualizations or causal tracing to support the induction-head interpretation in Section 6, or (b) recharacterize the finding as a "loss non-monotonicity" and remove the induction-head framing from the introduction's bullet list.

3. Consider adding a single language-modeling experiment (e.g., perplexity at small scale on WikiText) to demonstrate that the narrow-LR-window pattern generalizes beyond synthetic tasks. This would significantly strengthen the paper's main claim without requiring large-scale training.

## Score and Decision

### Calibration

**Round 1 — Bracketing.** Queried the human-review corpus for papers on similar topics:
- Weak band (avg < 3.5): comparable papers scored 2.50–3.33 (e.g., "Trading Complexity for Expressivity" 2.50, "On Structured State-Space Duality" 3.33). Our paper is clearly stronger than these.
- Middle band (3.5–7.5): comparable papers scored 4.0–4.5 (e.g., "Memory Determines Learning Direction" 4.50, "Dynamics of learning when learning dynamics" 4.50). Our paper is empirically richer and more directly applicable.
- Strong band (>7.5): papers scored 8.0 but on less related topics (LLM conversation, RL, quantum models). Our paper does not reach this level.

**Round 1 bracket:** 4.5–7.0.

**Round 2 — Narrowing.** Searched within the bracket for more topically similar papers:
- "Learning to Recall with Transformers Beyond Orthogonal Embeddings" (avg 6.50, Accept Poster): theoretical analysis of Transformer recall with simplified assumptions (trigger token, 3 gradient steps). Our paper is more empirically comprehensive but lacks the theoretical depth. Comparable quality.
- "Muon Outperforms Adam in Tail-End Associative Memory Learning" (avg 5.00, Accept Poster): narrower scope, more mixed reviews. Our paper is stronger.
- "On the Expressiveness of SSMs via Temporal Logics" (avg 5.50, Accept Poster): pure theory with no experiments, high variance (scores 2,8,4,8). Our paper has stronger empirical grounding.
- "Tuning the burn-in phase in training RNNs" (avg 5.33, Accept Poster): related but more narrow focus. Our paper is more comprehensive.

**Final calibration:** The paper is comparable to or slightly better than the 6.5 anchor ("Learning to Recall") in empirical breadth and practical relevance, but the framing overreach and lack of any real-LM validation pull it slightly below that anchor. The 5.0–5.5 anchors are below this paper's quality.

**Final score:** 6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>