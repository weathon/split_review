Now let me do calibration searches to score the paper.Round 1 bracket: **between 4.5 and 6.5**. The paper is exploratory with some theoretical contributions and limited empirical scope. Let me read key anchors and narrow.Now let me narrow with round 2 searches within the bracket of 4.5–6.5.Based on my calibration, the paper sits around 5.0 — comparable to "How transformers learn structured data" (5.00, Reject) and "Sudden Drops in the Loss" (5.50, Accept). The theoretical contributions are real but modest, and the main practical finding (curriculum learning benefit) disappears at 4 layers.

---

## Summary

This paper initiates the study of how language models learn probabilistic context-free grammars (PCFGs) through the lens of *subgrammar structure*. It defines inner and outer subgrammars, proves that the KL-divergence (language modeling loss) decomposes recursively over subgrammars (Theorems 4.3, 4.6), and empirically investigates parallel subgrammar learning, the representational effects of subgrammar pretraining (via CKA), and depth-vs-length generalization failure in small transformers.

---

## Strengths

- **Novel formalization of inner/outer subgrammars:** Definitions 3.3 and 3.5 give operationally clear, formally usable definitions of inner subgrammars (subtree restrictions) and outer subgrammars (rule-subset restrictions), providing a reusable vocabulary for studying PCFG substructure in learning. The Theorem 4.1 DAG decomposition is likewise a clean structural result.

- **KL loss decomposition and its empirical validation:** Theorem 4.3/Corollary 4.4 establishes that the KL divergence decomposes as a sum over subgrammar KL terms. Figure 1 directly verifies this: curves for total loss and per-subgrammar losses track each other throughout training, confirming that the decomposition holds during actual gradient descent, not merely at convergence.

- **Theorem 4.6 (recursion blow-up):** The formula $D_{\mathrm{KL}} = \frac{\sum_i p_i D_{\mathrm{KL},A_i}}{1-\mathbb{E}[R]}$ is the cleanest individual result in the paper — it shows that higher expected recursion magnifies the total KL divergence, and the paper illustrates this with a simple 2-rule grammar experiment.

- **Depth vs. length generalization failure (Figure 3):** The experiment with nested parentheses cleanly isolates a fundamental difficulty: the model maintains low prediction error on long flat sequences $(a)^i$ but error grows with recursive depth $(^i$, despite both cases having the same next-token distribution. This is a concrete, falsifiable finding that connects to the subgrammar framework.

- **Subgrammar pretraining and representational effects:** Section 5.2 shows that subgrammar pretraining increases CKA alignment across attention layers and, more directly, the cosine similarity analysis (Table 3) shows pretrained models segregate subgrammar sequences from non-subgrammar sequences more sharply — providing concrete evidence of retained internal structure.

- **Position-robustness of pretraining (Section 5.1):** The finding that prefix, suffix, and infix subgrammar pretraining yield comparable downstream performance is a useful empirical observation ruling out the obvious confound that autoregressive ordering drives the benefit.

---

## Weaknesses

### Fatal
None.

### Major

- **Corollary 4.7 is near-tautological as an explanation for parallel learning.** The corollary (stated informally) essentially says: if gradient updates for subgrammar $A_i$ do not hurt performance on other subgrammars $A_j$, then all subgrammars are learned in parallel. This is a restatement of what parallel learning *means* in gradient-descent language, not a mechanistic explanation of *why* it happens. The paper acknowledges it is informal and defers verification to future work — but this makes the theoretical treatment of the paper's most novel empirical observation a promissory note rather than a result. A paper that observes parallel learning and offers only a tautological condition for it has not yet explained the phenomenon.

- **The curriculum learning finding vanishes at 4 layers, undermining its practical scope.** Section 5.2 reports: "This effect diminishes as the model size and representational complexity increase (for instance, this occurs for 2-layer transformers but not 4-layers)." The paper acknowledges this, but the treatment is brief — "as expected, larger models consistently reach lower losses regardless of pretraining" — without examining *why* the effect disappears or whether the representational differences (CKA, cosine similarity) might still confer practical benefits in larger-scale settings. The loss improvement from curriculum pretraining disappears exactly where the finding would become practically relevant, and the paper does not offer a principled account.

### Minor

- **The "context insensitivity" assumption (Corollary 4.5) is informally validated but not quantified.** The assumption — that $Q_\theta$ assigns the same conditional distribution to subgrammar strings regardless of context — enables the clean $D_{\mathrm{KL}} = \sum_i p_i D_{\mathrm{KL},A_i}$ formula but is explicitly "strong." The paper addresses this by noting "varying the prefix did not result in qualitatively different results" (Figure 1 caption), but this is qualitative. A single rigorous measurement — e.g., computing the variance of per-subgrammar KL divergence across different prefix contexts for a fixed trained model — would let readers judge how load-bearing the assumption is.

- **Figure 2a is consistent with an alternative interpretation.** The paper describes the curves as showing "all subgrammars learned in parallel," meaning all decrease simultaneously. But Figure 2a also shows that deeper subgrammars (L1–L4) start at substantially lower initial KL values and converge faster than L0. This is equally consistent with "deeper subgrammars are individually easier and mastered first." The paper does not operationalize "parallel" precisely enough to rule this out, making the comparison to child language acquisition (who learn "sequentially") under-supported.

- **The connection between Theorem 4.3 and the Section 6 failure is asserted but not established.** Section 6 shows that models fail at deep recursion. The paper links this informally to the subgrammar framework, but does not demonstrate that the subgrammar KL decomposition can localize *where* in the DAG the loss blow-up comes from for deep recursion. Closing this loop — even in one experiment — would substantially strengthen the contribution.

- **Table 1 reports CKA means over 30 seeds without uncertainty estimates.** The raw percentages (e.g., +8.9% vs. +21.7% for attention layers under different pretraining durations) are uninterpretable without knowing within-seed variance. Standard deviations or confidence intervals would make these results actionable.

### Trivial

- The GPT-5.1 experiment (Section 6, n=5 each) is clearly labeled as anecdotal in footnote 3, but the surrounding text in the main section could mislead a casual reader into treating it as evidence. The anecdote belongs in a discussion/footnote, not embedded in a section titled "Do LMs Know Syntax?"

---

## Nice-to-Haves

- **Quantitative verification of the decomposition identity.** The paper shows Figure 1 visually, but a numerical check — e.g., reporting the residual $|D_{\mathrm{KL}}(P_G \| Q_\theta) - \sum_i D_{\mathrm{KL},A_i}|$ at several training checkpoints — would demonstrate that the decomposition holds to within finite-sample error, establishing it as an empirical tool rather than a qualitative illustration.

- **Studying when parallel learning breaks down.** A natural and generative follow-up: vary model capacity relative to PCFG complexity and check whether underparameterized models learn subgrammars sequentially rather than in parallel. This would make Corollary 4.7 actionable.

- **Explicitly stating the "clumsy" theorem without context insensitivity.** The paper mentions "a more clumsy theorem can be stated without context-insensitivity" (Section 4, after Theorem 4.6) but does not provide it. Including this — even briefly — would let readers assess how much the assumption buys.

- **The MLP layers in CKA show negligible or negative effects.** Table 1 shows that subgrammar pretraining consistently improves attention CKA (+8.9%–+21.7%) but changes MLP CKA negligibly or negatively (−0.1% to −4.7%). This asymmetry is interesting and unexplained; a brief discussion would strengthen mechanistic interpretation.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The decomposition theorems are trivially derivable from the chain rule"** (Harsh Critic): Partially valid as a framing concern — the algebra in Equations (1)–(5) is not deeply surprising once you have the definitions — but the paper's actual novel contribution is the *definition* of the subgrammar restriction of KL divergence (Definition 4.2) and the subsequent DAG-based recursion, which together constitute a new vocabulary for studying these dynamics. Calling these results merely "a restatement of the chain rule" understates the definitional work. Retained only as a framing caution (the paper does overstate "fundamental theorems"), not as a fatal flaw.

- **"Theorem 4.6's claim that 1 − E[R] < 0 causes unbounded KL divergence is misleading"** (Harsh Critic): The paper itself correctly explains that this condition is exactly when "the PCFG sampling process…will in expectation never terminate." The criticism is a presentation nitpick, not a substantive error; the paper addresses it in the same paragraph.

- **"The anecdotal GPT-5.1 comparison should not appear"** (Harsh Critic): The paper clearly flags this as anecdotal in footnote 3. Retained only as a trivial presentation note (already addressed above), not as a methodological flaw.

- **"Higher CKA means consistency, not subgrammar structure"** (Harsh Critic): This is a valid caution about over-interpretation, but the paper does not rest its representational claim solely on CKA — it follows up with cosine similarity analysis (Table 3) which is a more direct test. The criticism is partially addressed within the paper.

- **"Missing related works"** (not explicitly raised, but preemptively removed per hard rules): Removed per hard rule.

- **"Missing appendix proofs / missing grammar definitions"** (implicit in scope criticism): Removed per hard rule — the parser strips appendices.

- **Strength Finder: "This paper addresses an important problem"** — generic, removed.

- **Strength Finder: "The child language acquisition analogy is insightful"** — the analogy is loose and the comparison is not operationalized rigorously, as noted in the weakness about Figure 2a. Removed.

---

## Novel Insights

The most genuinely novel finding is the clean empirical demonstration (Figure 1) that the KL loss decomposition over subgrammars holds *throughout training*, not merely at convergence — meaning the subgrammar structure imposes a consistent constraint on optimization dynamics, not just on final representations. Theorem 4.6 provides the complementary insight that recursion amplifies divergence in a specific, closed-form way. Together, these suggest that the algebraic structure of a PCFG acts as a persistent inductive structure shaping the loss landscape at every stage of training — a framing that could generalize beyond PCFGs to other compositional hypothesis classes.

---

## Suggestions

1. **Quantify the context-insensitivity violation:** For fixed trained models, compute per-subgrammar KL divergence under 5–10 different prefix contexts and report the variance. This would tell readers how much the elegant Corollary 4.5 formula actually holds in practice.
2. **Numerically verify the decomposition identity** at several training steps: report $|D_{\mathrm{KL,total}} - \sum_i D_{\mathrm{KL},A_i}|$ to validate the theorem as a quantitative tool.
3. **Rephrase the description of Figure 2a**: clarify the definition of "parallel learning" operationally (e.g., all subgrammar losses decrease monotonically from epoch 0, vs. interleaved) to make the comparison to child language acquisition falsifiable.
4. **Add uncertainty estimates to Tables 1 and 3** — 30 seeds is sufficient to report standard deviations.
5. **Move the GPT-5.1 anecdote to a footnote or discussion box**, clearly separated from the empirical results in Section 6.

---

## Score and Decision

**Calibration anchors:**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/F0Zd3knG9j.md` — avg 5.00 (Reject, Round 1/2) — "How transformers learn structured data": nearly identical scope (PCFGs, small transformers, hierarchical learning dynamics). The paper under review has more formal theorems but similarly narrow experiments and a key finding that disappears at larger model sizes. *Comparable.*
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/MO5PiKHELW.md` — avg 5.50 (Accept, Round 2) — "Sudden Drops in the Loss": studies training dynamics of syntax acquisition in real MLMs with clear phase-transition findings. More empirically grounded in real models; paper under review has more formal theory but narrower empirical scope. *Paper under review is slightly weaker empirically.*
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/aWLQTbfFgV.md` — avg 6.25 (Accept, Round 1) — "Training Neural Networks as Recognizers": strong methodology, released benchmark, clean formal-language scope. *Paper under review is weaker on empirical rigor and breadth.*
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/0pLCDJVVRD.md` — avg 7.00 (Accept, Round 1) — "A Percolation Model of Emergence": strong formal-language theory + formal empirical validation of emergent abilities. *Substantially stronger.*
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/tHHzfZSP6T.md` — avg 5.00 (Reject, Round 2) — "How Capable Can a Transformer Become": empirical study on compositional capabilities with similar small-model scope. *Comparable.*
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/b5lXUwZiD3.md` — avg 5.25 (Reject, Round 2) — "On Limitation of Transformer for Learning HMMs": empirical limitation study of transformers on formal sequential models. *Slightly weaker theoretically than paper under review.*

**Round 1 bracket:** 4.5–6.5.  
**Round 2 narrowing:** The paper is most similar to the cluster at 5.0–5.5. It is stronger than the HMM limitation paper (5.25) due to its theoretical contributions, but weaker than "Sudden Drops" (5.50) due to the empirical scope being toy-only and the main curriculum finding disappearing at scale. It is clearly below the 6.25 and 7.00 papers. The tautological Corollary 4.7, the vanishing curriculum benefit, and the informally verified context-insensitivity assumption collectively keep this from a confident accept.

**Originality:** Moderate — the subgrammar definitions are novel, but the theorems are accessible from known techniques. The parallel-learning observation is novel; the depth vs. length finding partially echoes known results.  
**Importance of research question:** Genuine — understanding learning dynamics of CFGs is a meaningful open problem.  
**Support for claims:** Partial — theoretical claims are proven, empirical claims are verified on toy grammars only.  
**Soundness of experiments:** Limited in scope (very small models, synthetic PCFGs), no uncertainty estimates in key tables.  
**Clarity of writing:** Generally clear, with some loose claims (parallel learning definition, child acquisition analogy).  
**Value to community:** This is a useful opening paper; the definitions and decomposition are a platform for future work. But as a standalone contribution, it does not yet deliver a complete or convincing story.

**Final score: 5.0** — this is a marginal paper that sits just at the Reject side of the borderline. The theoretical framework is clean and the empirical validation of the decomposition is honest, but the main practical finding disappears at 4 layers, the central theoretical explanation for the most novel empirical observation (parallel learning) is near-tautological, and the experimental regime is too narrow to support the general claims made in the abstract and introduction.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>