## Summary

The paper proposes Knowledge Tracing Set Transformers (KTSTs), a transformer-based model class for knowledge tracing that uses principled set representations of student interactions (mean, unique set, and MHSA embeddings) to fix the "expanded representation" flaw in prior work — label leakage and distribution shift caused by duplicating interactions for each knowledge component. The model also introduces a learnable variant of ALiBi attention (learnable decay parameter per head). KTSTs achieve SOTA AUC on 7 of 8 standard benchmark datasets against 22 baselines, with statistical significance testing and a shared evaluation framework.

## Strengths

- **Principled set representations that fix a genuine flaw in prior work**: The paper precisely identifies and formalizes the "expanded representation" problem — label leakage and distribution shift from duplicating interactions per knowledge component (Section 3, lines 36–63). The proposed set-based representations (Section 4.3) satisfy permutation invariance and avoid both issues. The empirical payoff is clearest on Ednet (KC-to-question ratio 2.30), where KTST substantially outperforms expanded-representation baselines (Table 1), and where IEKT, LPKT, and QIKT — the only baselines that compete — also use set representations.

- **Comprehensive SOTA results against 22 baselines on 8 datasets**: KTST achieves SOTA AUC on 7 of 8 datasets with paired t-tests at the 0.01 level confirming statistical significance (Tables 1 and 2). All baselines are reproduced within the pykt framework using the same splits and preprocessing, which is rare and thorough in the knowledge tracing literature. The paper honestly reports Statics2011 as an exception.

- **Thorough documentation of specific flaws in prior work**: Rather than generic critique, the paper catalogues four concrete issues — label leakage, distribution shift, permutation invariance violation, and unnecessary complexity from domain-inspired components — each tied to specific equations, citations, and architectural elements (Sections 3, 4.1, 4.3). This sharply delineates the contribution and motivates why a simpler model can outperform complex domain-inspired alternatives.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Ablation study validating architectural choices is confined to a single dataset (AS2009)**: The paper validates three design choices — learnable vs. fixed ALiBi, query=key in cross-attention, encoder-decoder vs. decoder-only — only on ASSISTments2009 (Table 3, Section 5.2). The paper then generalizes these as "best for KTSTs" (Section 4.2) without evidence on datasets with different KC-to-question ratios (e.g., Ednet at 2.30 or AL2005 at 1.46). If optimal architecture differs per data regime (e.g., the decoder-only variant might perform relatively better on some datasets), the claim of general optimality is over-broad. Extending the ablation to at least one high-ratio dataset would substantially strengthen the paper. This does not undermine the core SOTA claim (which is supported by comprehensive benchmark results), but it weakens the specificity of the architectural conclusions.

- **Learnable ALiBi's advantage over fixed ALiBi has thin empirical support**: The learnable ALiBi mechanism differs from Press et al. (2021)'s fixed ALiBi only in that the per-head decay θ is learned rather than fixed. Its superiority is demonstrated on only AS2009, and the paper does not report what values θ converges to, making it unclear whether the learned values differ meaningfully from the initialization. Reporting learned θ values (e.g., as a function of head and dataset) would meaningfully strengthen this contribution.

- **Synthetic MIRT experiments are limited in scale**: The synthetic experiments use only 10 knowledge components, which is far smaller than real-world datasets (e.g., Ednet has hundreds). The claim that MHSA embeddings "perform best in more complicated settings" (Section 5.3, line 214) is supported by a suggestive but underpowered simulation — the standard errors in Figure 3 likely overlap substantially, and the experiment shows MHSA catching up rather than clearly dominating. The paper appropriately frames this as a "conjecture," but the evidence is weaker than the language ("supported by experiments on synthetic data," line 154) suggests.

- **No efficiency comparison**: The paper claims KTSTs are "conceptually simpler" but does not report model size, training time, or inference throughput relative to baselines. Since the expanded representation increases sequence length by the average KC-per-question factor, KTSTs should have a concrete efficiency advantage on datasets like Ednet. Reporting this would strengthen the practical case for the method.

### Trivial
None.

## Nice-to-Haves
- Analysis of what the learned θ values converge to for the learnable ALiBi mechanism, to demonstrate whether learning actually changes behavior.
- Efficiency comparison (model size, training time, throughput) against baselines.
- Hyperparameter sensitivity analysis (e.g., number of layers, embedding dimension).
- Brief intuition for why query=key in cross-attention is beneficial (the paper adopts this from Pandey & Karypis 2019 but offers no reasoning for why it works, which feels slightly ad-hoc relative to the otherwise principled narrative).

## Removed Points
The following points from the reviewers were removed after verification:
- Criticism that the abstract language overstates label leakage as still present: The paper explicitly acknowledges the fix (line 57–58) and pivots to distribution shift, which is a valid subtler argument. This is a nuanced reading difference, not a concrete weakness.
- Criticism about data being in the appended/stripped appendix: This is a parser artifact, not a paper flaw.
- "Learnable ALiBi contribution is incremental" as a standalone weakness: Incremental improvements over a known baseline are perfectly acceptable; this was folded into the ablation-coverage concern rather than treated as an independent flaw.
- Strength Finder's praise of the synthetic experiments as a strength: The experiments are limited in scale; this strength was dropped as the evidence is weaker than claimed.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface an unexpected connection or reframing.

## Suggestions
- Extend the ablation study (Table 3) to at least one additional dataset with a high KC-to-question ratio (e.g., Ednet or AL2005) to validate that the architectural choices generalize across data regimes.
- Report the learned θ values for the learnable ALiBi mechanism across heads and datasets, with a brief analysis of whether they diverge meaningfully from the ALiBi initialization.
- Include a simple efficiency table (parameters, training time, inference throughput) to support the claim that KTSTs are "conceptually simpler" and more efficient than expanded-representation models.
- Add a sentence of intuition for the query=key design in cross-attention to complete the otherwise principled narrative.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>