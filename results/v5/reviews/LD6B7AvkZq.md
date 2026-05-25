Now I have all the evidence I need. Let me write the consolidated review.

## Summary

The paper investigates how language models learn context-free grammars by introducing the notion of "subgrammars" — inner (compositional) and outer (simplified) grammars derived from a PCFG's non-terminal structure. It proves that the KL divergence (equivalently, language modeling loss) between a PCFG and an autoregressive language model decomposes recursively over these subgrammars (Theorem 4.3), and demonstrates this decomposition empirically with small transformers. The paper also explores curriculum learning via subgrammar pretraining with CKA-based representation analysis, and studies how transformers struggle with recursive depth but not length. The subgrammar definitions and the decomposition framework are clean contributions, but the paper's significance is substantially undercut by overclaimed framing ("fundamental theorems," "definitively show," "unlike children") that the evidence does not support, by theoretical results that are essentially identities following from definitions rather than surprising discoveries, and by empirical findings that are either unsurprising (parallel loss reduction on a sum of losses) or well-known (depth difficulty).

## Strengths

- **Clean formalization of subgrammars and their decomposition.** Definitions 3.3–3.5 introduce inner and outer subgrammars in a rigorous, well-motivated way, and Theorem 4.1 proves that any PCFG can be uniquely decomposed into a DAG of inner subgrammars. This provides a precise language for talking about the substructure of CFGs that was missing from prior work. (Section 3.1, Theorem 4.1)

- **KL-decomposition framework.** Theorem 4.3 and its corollaries show that the KL divergence between a PCFG and a language model can be expressed as a sum of conditioned divergences over subgrammar components. While this follows from the chain rule and the PCFG's recursive definition, having the decomposition written out explicitly and linked to subgrammar structure is a useful analytical tool. The empirical validation in Figure 1 that the sum of subgrammar KLs tracks the total KL throughout training adds concrete support. (Section 4.2, Figure 1)

- **CKA-based representation analysis.** The analysis in Section 5.2 showing that subgrammar-pretrained models exhibit higher CKA similarity across attention layers and better segregation of subgrammar vs. non-subgrammar strings is genuinely interesting. Table 1's percentage changes, while modest (8–22% for attention), are systematic across conditions and suggest that pretraining does imprint subgrammar structure on internal representations. This is the paper's most novel empirical contribution.

- **Curriculum learning results.** The finding that subgrammar pretraining can produce modest improvements in final loss for small models (2-layer transformers), and that this benefit is robust to subgrammar position (prefix/infix/suffix), is a practically useful observation. The acknowledgment that the benefit diminishes for larger models adds credibility.

## Weaknesses

### Major

- **The theoretical results are framed as far more significant than they are.** The paper calls Theorem 4.3 and its corollaries "a suite of fundamental theorems" and "the most important contribution of our work." In reality, these results are mathematical identities that follow from the chain rule of probability applied to a PCFG's recursive definition and an autoregressive model's left-to-right factorization. The KL divergence between a recursively-defined distribution and a factorized distribution inherits both structures, and the decomposition into subgrammar terms is a direct algebraic consequence. This is a useful reformulation — analogous to noting that the loss on a mixture distribution equals the weighted sum of per-component losses — but it does not constitute a theoretical discovery that rewrites our understanding of grammar learning. The paper would be stronger if it presented this as a clean analytical framework rather than "fundamental theorems." The rhetoric of "fundamental" (used 5+ times in Sections 1 and 4) inflates reader expectations that the experiments cannot meet. (Abstract, Section 1, Section 4.2)

- **The "parallel learning" claim is overstated and lacks a meaningful baseline.** The paper states that "small transformers learn all subgrammars in parallel, unlike children" and presents this as a surprising discovery. What Figure 1 actually shows is that several loss curves decrease simultaneously — which is precisely what gradient descent does when optimizing a sum of loss terms that all contribute positive gradient. The paper never establishes why sequential learning would be expected, presents no theoretical rationale for it, and provides no control experiment (e.g., a modular architecture where subgrammars could be learned separately) that could distinguish parallel from sequential learning. Corollary 4.7, offered as a theoretical condition for parallel learning, is essentially tautological: "if gradient updates for one subgrammar do not harm others, then all are learned simultaneously." The comparison to child language acquisition ("unlike children") is made repeatedly but entirely unsupported — no developmental data, no argument for why subgrammar learning in PCFGs maps onto child development, and no discussion of what sequential learning would even look like in this setting. (Abstract, Section 4, Figure 1, Corollary 4.7)

- **The connection to natural language acquisition is asserted without warrant.** The abstract and introduction situate the work in the context of how language models "acquire syntax" and how children learn language, but all experiments use tiny transformers (2-layer, 2-head) trained on toy PCFGs (nested parentheses, simple arithmetic-like grammars). The leap from these settings to natural language syntax is immense and entirely unbridged. If the paper were scoped as a study of how transformers learn PCFGs — a valid topic — this would be less of an issue. As written, the language-acquisition framing amplifies perceived significance beyond what the evidence can support. (Abstract, Introduction, Section 6, Section 7)

- **The depth-difficulty result replicates well-known findings.** Section 6 shows that transformers struggle with deeply nested structures while handling long non-recursive sequences well. The paper's own related work section cites Bhattamishra et al. (2020) and Lampinen (2024) demonstrating exactly this phenomenon. Presenting it as a novel finding about "whether LMs 'know syntax'" overclaims significance. The controlled experiment (Figure 3) is clean but incremental. (Section 6, Figure 3, Related Work)

### Minor

- **No statistical rigor in empirical results.** The paper reports CKA similarities across 30 random seeds (Table 1) and KL divergence curves (Figure 1) without any error bars, confidence intervals, or significance tests. Basic statistical reporting is expected when multiple seeds are available. This is particularly important given the modest effect sizes (e.g., +8.9% CKA change for attention layers) and the qualitative nature of the "parallel learning" claim. (Table 1, Figure 1, Section 5.2)

- **Anecdotal GPT-5.1 experiments add no scientific value.** Section 6 tests GPT-5.1 on 10 arithmetic expressions (5 deep, 5 non-deep) and reports accuracy (2/5 vs. 5/5). The paper itself acknowledges these are "purely anecdotal." Including such thin, non-rigorous results in a research paper weakens rather than strengthens the manuscript. (Section 6)

### Trivial

- The equation (4) expression is garbled by PDF extraction, though the intended meaning (sum of P log(P/Q) terms) is recoverable from context.
- Several figures are referenced (Figures 5, 6 for the curriculum results) that are described in prose but whose content is difficult to verify from the extracted text.

## Nice-to-Haves

- **Derive a testable prediction from the theoretical framework.** As it stands, the theorems restate what is implicit in the definitions. A stronger version would predict something nontrivial — e.g., that the order in which subgrammar losses decrease follows the DAG depth, or that grammars with certain subgrammar topologies are provably harder to learn.
- **Compare to a non-parallel baseline.** To make the parallel-learning claim meaningful, construct a setting where subgrammars could be learned sequentially (e.g., by freezing parts of the network) and show that the default transformer learns everything at once.
- **Substantiate the child-language analogy or remove it.** Either provide developmental evidence or a rigorous mapping argument, or drop the comparison entirely.

## Removed Points

The following points from the inputs are not included as weaknesses in the main review for the reasons indicated:

- **"Equation (4) appears to have structural issues"** — The garbled `\frac{\log P}{\log Q}` notation is a PDF-extraction artifact; the intended expression (sum of P log(P/Q) terms) is clear from context. Removed per parser-artifact rule.
- **"Missing hyperparameter and architecture details"** — The paper states these are in the appendix. The appendix was stripped during PDF processing. The paper as submitted almost certainly contains these details. Removed per parser-artifact rule.
- **"Missing related works"** — The instructions forbid mentioning missing related works as we cannot verify their existence.
- **"Grammatical error / typo / capitalization"** — The extracted text has standard PDF-extraction artifacts. Removed per parser-artifact rule.
- **"The scope of the contribution is too narrow" as a fatal issue** — While the scope is limited (toy PCFGs, tiny transformers), the paper does not claim more scope than it investigates in its experiments; the overclaiming is in the framing, not the stated scope. This is already captured in the Major weaknesses about framing and the natural-language connection.

## Novel Insights

The reviews do not surface any genuinely novel observation about the paper that goes beyond the paper's own contributions. The harsh critic's identification that the theoretical results are identities following from definitions is a correct characterization rather than a novel insight about the method. The tension between the clean subgrammar formalism and the overblown framing is noted by both inputs but is a meta-observation about the paper's presentation, not a scientific insight.

## Suggestions

1. **Scale back the rhetoric.** Replace "fundamental theorems" with "analytical decomposition" or "recurrence relations." Remove "definitively show" and "unlike children" unless substantially supported.
2. **Add error bars to all quantitative results.** With 30 seeds available for CKA and multiple runs for the KL curves, basic statistical reporting is essential.
3. **Either support or remove the child-language framing.** If the comparison is retained, provide developmental evidence or a rigorous argument for why subgrammar learning in PCFGs maps onto child language acquisition.
4. **Remove the anecdotal GPT-5.1 experiments** or replace them with a systematic evaluation.
5. **Explicitly verify the additive decomposition** by plotting the weighted sum of subgrammar KLs against the total KL on the same axes, as a direct validation of Theorem 4.3.
6. **Add a non-parallel baseline** to make the parallel-learning claim meaningful.
7. **Reframe the depth-difficulty experiment** as a replication and extension of known results, with clear attribution.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Query Bucket | Comparison |
|--------|-----------|-------|-------------|-----------|
| F0Zd3knG9j — "How transformers learn structured data" | 5.00 | R1 | Topic-mid | Similar topic (PCFG-based study of hierarchical learning). That paper had cleaner experiments and less overclaiming; the paper under review is weaker. |
| b5lXUwZiD3 — "On Limitation of Transformer for Learning HMMs" | 5.25 | R1 | Weakness | Empirical study of transformer limitations with better rigor; the paper under review is weaker. |
| fp77Ln5Hcc — "Depth Extrapolation of Decoders Trained on Nested Structures" | 4.50 | R2 | Narrowed | Similar quality level — both have some theoretical interest but limited scope and overclaiming issues. Comparable. |
| eRkNNQRppH — "(Pre-)training Dynamics: Scaling Generalization with FOL" | 3.50 | R1 | Topic-low, R2 | Heavily criticized for vague claims and lack of rigor. The paper under review is stronger (has cleaner theory). |
| uOnElfFuey — "Recovering Knowledge by Hardening Language Models" | 3.00 | R1 | Topic-low | Language extraction study; not closely comparable. |
| XVhm3X8Fum — "Stack Attention" | 6.67 | R1 | Topic-mid | Strong architectural contribution with rigorous evaluation. The paper under review is significantly weaker. |
| aWLQTbfFgV — "Training Neural Networks as Recognizers of Formal Languages" | 6.25 | R1 | Topic-mid | Methodologically rigorous. The paper under review is weaker. |
| 0pLCDJVVRD — "Percolation Model of Emergence" | 7.00 | R1 | Topic-high | Strong theoretical model with thorough experiments. The paper under review is much weaker. |

**Round-1 bracket:** 3.0–5.5, initially centered around 4–5 based on the closest topical anchor (F0Zd3knG9j, 5.0) and the observation that the paper under review has more overclaiming issues.

**Round-2 narrowing:** fp77Ln5Hcc (4.5) and eRkNNQRppH (3.5) provided lower and upper bounds within the bracket. The paper under review is better than eRkNNQRppH (which was heavily criticized for vague claims) but weaker than F0Zd3knG9j (which had cleaner experiments). The weakness-anchored evidence from the HMM-limitation paper (5.25) and the depth-extrapolation paper (4.5) confirms that papers with similar levels of overclaiming and limited empirical scope score around 4–5.

**What the low-band anchors failed at:** eRkNNQRppH (3.5) was criticized for having post-hoc interpretations of noisy curves, vague hypotheses, and unclear contributions. uOnElfFuey (3.0) had weak experimental validation. The paper under review shares some of these failures — it overinterprets its empirical observations (parallel learning as a discovery rather than expected gradient descent behavior) and overclaims the significance of its theoretical results. However, it has clearer theoretical foundations and more focused experiments than the lowest-band anchors, which prevents it from falling to their level.

**Final score determination:** The paper's clean subgrammar formalism and the CKA-based representation analysis are genuine contributions that place it above the 3.0–3.5 range. However, the significant overclaiming, the unsurprising nature of the core theoretical results, the lack of statistical rigor, and the replication of known findings limit its contributions to an incremental level. The most comparable anchor is F0Zd3knG9j (5.0) but the paper under review has more severe overclaiming issues, suggesting a score of 4.0 — below that anchor but above the 3.5 anchor.

<score>4.0</score>
<decision>Reject</decision>