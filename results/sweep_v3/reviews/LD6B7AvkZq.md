Now I'll produce the final consolidated review.

## Summary

This paper introduces a framework for studying how language models learn context-free grammars by decomposing the language modeling loss (KL divergence) across the subgrammar structure of a PCFG. It defines inner and outer subgrammars, states recurrence theorems relating KL divergence to subgrammar structure, and presents experiments showing that small transformers learn subgrammars in parallel (unlike children), that pretraining on a subgrammar yields representational differences detectable via CKA, and that depth of recursion (not length) is the primary bottleneck for generalization.

## Strengths

- **Novel theoretical framing for CFG learning**: The definitions of inner and outer subgrammars (Defs. 3.3, 3.5) and the proposal that LM loss decomposes recursively over a CFG's subgrammar DAG (Theorems 4.3, 4.6) are genuinely original. Prior work on CFG learning studied trained models' representations (Allen-Zhu & Li, 2023) or learning curves (Cagnetta & Wyart, 2024) but did not attempt a formal decomposition along grammar substructure. This work opens a new lens that could be productive for future research.

- **Clear experimental demonstration of depth-bottleneck in recursive generalization**: Figure 3 cleanly separates the effects of length vs. depth on prediction error, showing that error grows with recursion depth but remains low for equally long linear contexts. This finding is solid, uncontroversial, and presented with clear variance bands.

- **Parallel subgrammar learning is an interesting empirical observation**: The KL divergence curves in Figures 1–2 show that all subgrammar contributions decrease together during training, rather than simpler subgrammars saturating first. While the paper does not rigorously prove this is intrinsic rather than coincidental, the observation is genuinely striking and motivates a concrete open problem (Corollary 4.7).

- **Pretraining CKA analysis, while modest, shows a replicable effect**: Table 1 reports a consistent pattern across 30 seeds: pretrained models have higher attention-layer CKA similarity than scratch-trained models, with percentage changes up to ~21% for longer pretraining. This is preliminary evidence that subgrammar pretraining shapes internal representations.

## Weaknesses

### Major

- **Theoretical presentation lacks precision, making the core contribution difficult to evaluate**: The derivation in Section 4.2 (equations 1–4) is presented as intuition but the notation is unclear. The paper states "in an abuse of notation" (line 143) and gives informal explanations, but terms like $P_G(\alpha|\epsilon)$ and $P_G(a|\alpha)$ are not given a proper measure-theoretic grounding, and it is not clear what probability space they are defined over. More critically, Definition 4.2 of $D_{\text{KL}}(P_G \parallel Q)_A$ uses the notation $D_{\text{KL}}(P_G \parallel Q | \neg s)$ which is never defined. Since the restricted KL divergence is the central building block for all subsequent theorems, the lack of a clear definition makes it difficult to verify what the theorems actually claim. The proof of Theorem 4.3 is deferred to the (stripped) appendix, but even the statement's interpretation depends on a definition that is not well-specified.

- **Corollary 4.5's "context insensitivity" assumption is not tested in the experiments, yet is invoked to interpret results**: The paper derives a clean decomposition under the assumption that $Q_\theta$ is "context insensitive" — i.e., the model's conditional distribution over subgrammar $A_i$ strings is independent of the surrounding context. This is a strong assumption (explicitly acknowledged, line 179). The paper then claims in the Figure 1 caption that "varying the prefix did not result in qualitatively different results, suggesting these models are largely 'context-insensitive'". But this is a post-hoc visual assessment, not a quantitative test. Without a systematic comparison of $Q_\theta(A_i|s)$ across different contexts $s$, the claim that the theory "explains" the Figure 1 curves is not supported.

- **The "parallel learning" claim is observational and not adequately tested**: The paper's claim that transformers "learn all subgrammars in parallel" rests entirely on visual inspection of Figures 1–2. Corollary 4.7 gives a formal sufficient condition for parallel learning but is stated informally, and the paper explicitly says "An immediate future direction would be to study whether the small transformers and PCFGs of this paper learn subgrammars in parallel because they satisfy the independence condition of 4.7" (line 225). This is honest, but it means the central qualitative conclusion of Section 4 is an untested hypothesis, not a finding. A controlled experiment (e.g., ablating gradients from one subgrammar, or comparing convergence rates across subgrammars quantitatively) would be needed to support the claim.

- **CKA analysis lacks statistical rigor**: Table 1 reports percentage changes in CKA similarity without confidence intervals, effect sizes, or significance tests, despite running 30 random seeds. The MLP-layer changes are often negative (−0.2%, −4.7%, −2.6%, +1.0%) and within the noise. The paper claims the analysis "show[s] definitively" (abstract, line 19) that pretraining aligns representations with grammar substructure — this language is not supported by the reported numbers.

### Minor

- **The GPT-5.1 anecdote adds no scientific value and weakens the paper's impact**: Section 6 reports 2/5 correct on deep arithmetic expressions vs. 5/5 on non-deep ones, with n=5 per condition and unreported selection method. The paper's own footnote 3 calls this "purely anecdotal." Moreover, the paper immediately notes that GPT-5.1 Thinking solves all examples given longer processing time, undercutting even the informal point. The depth-vs-length finding from the controlled transformer experiment (Figure 3) is already sufficient; the LLM anecdote should be removed or replaced with a systematic evaluation.

- **Experimental specification is insufficient for reproducibility**: The paper describes subgrammar KL computation as using "a random (but likely) prefix" (Figure 1 caption) without specifying how prefixes are sampled, what "likely" means, or how the subgrammar-conditional probabilities $Q_\theta(A_i|\text{prefix})$ are extracted from the model. The grammar definitions and training hyperparameters (epochs, learning rate, optimizer, batch size) are not stated in the main text. The "robustness to location" experiment is referenced as "Figure 5" but only Figures 1–3 appear in the main body.

- **Abstract overclaims relative to what is demonstrated**: The abstract says "show definitively that such pre-training results in internal representations that are more aligned with the grammar's substructure." Given the small and inconsistently signed CKA changes and lack of statistical testing, "definitively" is too strong.

### Trivial

- Figure 1's y-axis uses a broken scale (break between 12 and 19) which makes it harder to read the convergence behavior where most of the action occurs.
- There is a numbering inconsistency: the text refers to "Theorem 4.2" in Corollary 4.4 and elsewhere, but Theorem 4.2 is not stated before it is referenced (it appears Theorem 4.1 is followed by 4.3, with 4.2 possibly a renumbering glitch).

## Nice-to-Haves

- Provide a precise, measure-theoretic definition of the restricted KL divergence $D_{\text{KL}}(P_G \parallel Q)_A$ with explicit clarification of what probability distribution is being summed/integrated over.
- Add a controlled experiment for parallel learning: e.g., compare gradient updates from different subgrammars, or train a model where gradients from one subgrammar are blocked.
- Report confidence intervals or bootstrapped effect sizes for the CKA analysis.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The derivation assumes independence across subgrammars that does not hold for general PCFGs"** — This criticism is not verifiable from the paper as written. The proof is in the (stripped) appendix. The paper acknowledges context-insensitivity is a strong assumption (line 179) and presents Corollary 4.5 with explicit condition. The harsh critic's assertion that "the paper's derivation seems to assume independence" is an interpretation, not a verified flaw.

- **"Missing proofs in appendix"** — The parser strips appendix content. The paper states proofs are in Appendix A (lines 167, 191). Per review guidelines, missing appendix content is a parser artifact, not a paper flaw.

- **"The CKA analysis shows very small percentage changes (most under 10%)"** — This is factually wrong for the attention-layer results: changes of +21.7% and +20.8% are reported, which are substantial.

- **"Section 6's nested parentheses experiment is purely replicatory; the paper's contribution here is purely replicatory"** — The experiment is confirmatory, but it serves as evidence for the paper's depth-vs-length claim in a controlled setting, which is a legitimate contribution in context.

- **"Pure formatting/style nitpicks"** — Removed per guidelines.

- **"Missing related works"** — Removed per guidelines (no external sources to confirm).

- **"Definition 3.3 is incomplete because it does not specify Σ' must contain all terminals in P'"** — Upon reading, Definition 3.3 does restrict $\Sigma' \subseteq \Sigma$ and $\mathcal{P}'$ is "the set of all rules with non-terminals in $\mathcal{N}'$." The definition is coherent as stated — terminals not in $\Sigma'$ would not appear in derivations from $\mathcal{S}'$ because the rules in $\mathcal{P}'$ only use non-terminals from $\mathcal{N}'$, and the corresponding right-hand sides are subsets of the original grammar's right-hand sides, which are built from $\Sigma \cup \mathcal{N}$. The oversight is minor and the intended meaning is clear.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface any genuinely novel observations beyond what the paper itself provides.

## Suggestions

1. **Sharpen the theoretical contribution**: Replace the current informal derivation (equations 1–4) with a single clean theorem for a restricted but well-defined case (e.g., chain-structured subgrammars with fixed terminal context). State the assumptions precisely and prove this case. Then discuss how the general case could be approached as future work.

2. **Remove the GPT-5.1 anecdote**; replace it with either nothing (the controlled experiment stands on its own) or a systematic evaluation across model scales with proper sample sizes.

3. **Add statistical rigor to the CKA analysis**: Report 95% confidence intervals or bootstrapped effect sizes; define what "top quantile of seeds" means; clarify the cosine similarity comparisons.

4. **Provide experimental details in the main text**: At minimum, state the grammar(s) used, model architecture (embedding dimension, number of heads, etc.), training hyperparameters, and how subgrammar-conditional probabilities are computed from the model's next-token distribution.

5. **Tone down the abstract**: Replace "definitively" with a more measured description of what the CKA analysis shows.

## Score and Decision

I calibrated against the following anchors from the review corpus:

- **qyU5s4fzLg.md** (avg 7.50, Accept): Unsupervised parsing with SemInfo. Cleaner, more rigorous empirical contribution with clear improvements across multiple languages. **Stronger than the reviewed paper.**
- **0pLCDJVVRD.md** (avg 7.00, Accept): Emergence in transformers trained on formal languages. Well-executed mix of theory and experiments. **Stronger than the reviewed paper.**
- **XVhm3X8Fum.md** (avg 6.67, Accept): Stack attention for hierarchical patterns. Clear architectural contribution with strong empirical results on formal languages. **Stronger than the reviewed paper.**
- **aWLQTbfFgV.md** (avg 6.25, Accept): Training neural nets as formal language recognizers. Thorough benchmarking with clean methodology. **Stronger in experimental rigor, comparable in ambition.**
- **F0Zd3knG9j.md** (avg 5.00, Reject): Transformers learning structured data via hierarchical filtering. Interesting data generation but limited claims and alternative interpretations. **Comparable — both have interesting ideas but incomplete evidence.**
- **fp77Ln5Hcc.md** (avg 4.50, Reject): Depth extrapolation of decoders. Has theory + experiments but theory is overly simplistic. **Comparable — both have theoretical gaps and mixed empirical support.**
- **eRkNNQRppH.md** (avg 3.50, Reject): FOL pretraining dynamics. Unclear presentation, weak claims. **Weaker than the reviewed paper.**
- **uOnElfFuey.md** (avg 3.00, Reject): Recovering DFAs from LMs. Weak empirical results. **Weaker than the reviewed paper.**

The paper under review has genuine novelty (subgrammar decomposition framework) and interesting observations (parallel learning curves, depth bottleneck), but the theoretical core is imprecisely specified, key claims are not adequately tested, and the experimental execution lacks rigor in several places. It is stronger than the low-scoring anchors but weaker than the high-scoring ones, and sits at the boundary with the mid-range anchors.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>