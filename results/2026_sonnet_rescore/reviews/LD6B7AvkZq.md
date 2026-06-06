## Summary

This paper introduces a framework for studying how language models acquire syntax through the lens of probabilistic context-free grammar (PCFG) *subgrammar structure*. It defines inner and outer subgrammars of PCFGs, proves several theorems showing that the KL-divergence (language modeling loss) decomposes recursively over subgrammar structure, and validates this framework empirically on small transformers. Secondary contributions include an observation that models learn all subgrammars in parallel (unlike child language acquisition), evidence that subgrammar pretraining alters internal representations (via CKA), and a demonstration that transformers fail on depth-based generalization but not length-based generalization.

---

## Strengths

- **Novel and operational subgrammar definitions (Definitions 3.3, 3.5):** Inner and outer subgrammars are formalized in terms of non-terminal restrictions and renormalized rules, providing a concrete handle on CFG substructure that is directly usable for theoretical and empirical analysis. The unique DAG decomposition (Theorem 4.1) connects these to classical work on grammatical levels.

- **Empirical validation of KL decomposition (Figure 1):** Figure 1(a) and (b) show that the total KL divergence of a small transformer trained on synthetic CFGs closely matches the sum of subgrammar divergences at every point in training, confirming that Theorems 4.3/4.4 capture real training dynamics rather than being merely formal.

- **Clear isolation of depth vs. length generalization failure (Figure 3):** The experiment in Section 6 elegantly separates two sources of out-of-distribution difficulty. The model trained on `Nested Parentheses` maintains low error on contexts `(a)^i` (error 0.017 at depth 200) but exhibits sharply growing error on contexts `(^i` (error 0.173 at depth 200), despite the ground-truth next-token distribution being identical for both cases. This is a crisp and well-designed experiment.

- **Position-robustness of subgrammar pretraining (Section 5.1):** The finding that subgrammar pretraining is equally effective whether the subgrammar appears as prefix, suffix, or infix challenges the naive expectation that autoregressive order should strongly bias curriculum learning, and is backed by the experiments in Figure 5.

- **CKA and cosine similarity analysis (Tables 1 and 3):** The representational analysis goes beyond loss curves and shows that subgrammar pretraining yields not only higher inter-seed consistency but also better segregation of subgrammar vs. non-subgrammar sequences, with the cosine similarity analysis in Table 3 providing a more direct test of representational structure.

---

## Weaknesses

### Fatal
None.

### Major

- **The curriculum learning benefit vanishes at 4 layers (Section 5.2).** The paper reports: "this effect diminishes as the model size and representational complexity increase (for instance, this occurs for 2-layer transformers but not 4-layers)." This is arguably the most practically relevant result, but the paper largely dismisses it with "as expected, larger models consistently reach lower losses." It never investigates *why* the effect vanishes — whether this is a capacity effect, an optimization landscape effect, or a consequence of the model already being overparameterized relative to the PCFG. Since all experimental PCFGs are tiny and all transformers are tiny, the regime in which a positive result is reported (2-layer) is the least representative of practical interest. The paper does not grapple with whether the subgrammar framework yields actionable predictions for non-toy regimes.

- **Corollary 4.7 is near-tautological and its theoretical explanation of parallel learning is a promissory note.** The corollary states: if gradient updates for one subgrammar do not hurt performance on other subgrammars, then all subgrammars are learned in parallel. This is a restatement of parallel learning in gradient-descent terminology, not a mechanistic explanation. The paper acknowledges it is stated informally and defers verification to future work. For what the paper describes as the most novel empirical observation (all subgrammars learn in parallel), the theoretical treatment is essentially a placeholder.

### Minor

- **Context-insensitivity assumption is unverified quantitatively.** Corollary 4.5's clean weighted-sum decomposition requires that Q_θ models each subgrammar identically regardless of context. The paper acknowledges this is strong and offers qualitative evidence (Figure 1 with random prefix) and argues statistically that deep prefixes are rare under P_G. However, no systematic quantitative measurement of context-sensitivity is provided for any of the experimental grammars. The gap between the full Theorem 4.3 result and the elegant Corollary 4.5 formula is exactly what the assumption is carrying, and readers cannot assess how tight that gap is in practice.

- **Theorem 4.6's "unbounded KL divergence" characterization is subtly imprecise.** The paper states "if 1 − E[R] < 0, the KL-divergence is unbounded." But when E[R] ≥ 1, the PCFG's own sampling process does not terminate in expectation — meaning P_G itself does not define a proper probability distribution over finite strings, making the KL divergence undefined rather than large. The paper notes the non-termination ("the PCFG sampling process... will in expectation never terminate") but conflates undefined with unbounded. A one-sentence clarification would prevent confusion.

- **CKA interpretation is somewhat over-stated.** Table 1 shows higher CKA across seeds for pretrained models. The paper interprets this as representations being "more aligned with the grammar's substructure." But CKA measures inter-seed *consistency* of representations, not whether those representations track subgrammar structure specifically. The subsequent cosine similarity analysis (Table 3) is the more direct test of structural claim and should be foregrounded.

- **Section 6 does not reconnect to the theoretical framework.** The finding about depth-based generalization failure is interesting, but the paper does not ask what the subgrammar decomposition of Theorem 4.3 predicts about *where* the loss blow-up originates at deep recursion. The theoretical framework is present but unexploited in this section. Making that link would sharpen Section 6 substantially.

- **Statistical uncertainty not reported for Tables 1 and 3.** Both tables report mean CKA and cosine similarity across 30 seeds without confidence intervals or statistical tests, making it difficult to judge whether differences like +8.9% vs +21.7% (attention CKA, Table 1) are significant or within variance.

### Trivial

- The paper notes it could state Theorem 4.6 (and Corollary 4.5) without the context-insensitivity assumption, producing "a more clumsy theorem," but does not state it. Even an informal version in the text would help readers assess how much the assumption loads.

---

## Nice-to-Haves

- A quantitative verification that the KL decomposition (Theorem 4.3/4.4) holds numerically to within measurement error — not just visually — would establish the theorem as a genuine empirical tool. Reporting the sum of subgrammar divergences versus the total KL divergence as a number at several training checkpoints would be compelling.
- The parallel learning experiment (Figure 2a) would benefit from a condition where models are underparameterized relative to the PCFG to test whether parallel learning breaks down, which would make Corollary 4.7 actionable.
- Investigating why the curriculum benefit disappears at 4 layers — even a brief ablation or conjecture — would make Section 5.2 more useful for practitioners.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Central theoretical contribution is mathematically lightweight"** (Harsh Critic): While it is correct that Theorem 4.3/Corollary 4.4 follow fairly directly from the chain rule applied to PCFG factorization, the paper's value is as a *framework paper*, not a theorem paper. The definitions (inner/outer subgrammar, context-insensitivity) are novel and non-trivial, and the subsequent empirical use of the framework is the paper's payoff. The critic's framing treats the paper as claiming deeper mathematical novelty than it does. The paper says in Section 4: "the most important contribution of our work is a suite of fundamental theorems showing that the loss of language modeling... obeys a recurrence" — which is a description of organizational/definitional contribution, not a claim of surprising mathematical depth. This criticism is retained only as a minor framing issue (the paper's self-description could be tempered), not as a substantive weakness.

- **"Anecdotal GPT-5.1 comparison should not appear in a section titled 'Generalization'"** (Harsh Critic): The paper itself footnotes (footnote 3): "These arithmetic tests are purely anecdotal and should not be interpreted as direct evidence about training difficulty on recursive PCFGs." This is self-aware and appropriate. The criticism is valid as a minor presentation concern but the paper has already pre-empted it.

- **"Figure 2(a) equally consistent with 'deeper subgrammars individually easier'"** (Harsh Critic): The paper defines "in parallel" as all subgrammar losses decreasing simultaneously (as opposed to sequential, where one subgrammar must converge before another begins decreasing). The figure supports this definition. That deeper subgrammars start from lower values is consistent with parallel learning (they are subsets of the harder grammar and thus inherently easier), not a competing explanation.

- **Strengths about "important problem" / general framing** (Strength Finder): Generic strengths about the importance of studying language acquisition and CFGs as a surrogate are removed as they apply to any paper in this space without being specific to this paper's contribution.

---

## Novel Insights

The paper's most genuinely novel observation — that small transformers learn *all* subgrammars simultaneously rather than sequentially, even when one might expect a curriculum effect — raises a concrete open question about when and why gradient descent on autoregressive models achieves this decoupled optimization. This observation, combined with the KL decomposition framework, suggests a research agenda of characterizing models and grammars for which Corollary 4.7's independence condition holds, potentially linking overparameterization relative to the PCFG size to parallel convergence. The depth-vs-length generalization dissociation is also sharply operationalized here in a way that connects directly to the subgrammar hierarchy (failure appears at the level of recursive depth in the DAG decomposition), inviting future theoretical work connecting this to Theorem 4.6's blow-up formula.

---

## Suggestions

1. Report the KL decomposition (Theorem 4.3) numerically — compute the sum of subgrammar divergences and compare to the total KL divergence at several checkpoints. This would convert a visual claim into a quantitative one.
2. Add confidence intervals or standard errors to Tables 1 and 3, given 30 seeds are already available.
3. Investigate (briefly) why the curriculum benefit vanishes at 4 layers — a capacity-controlled ablation or a simple conjecture would help practitioners.
4. Frame Section 6's depth-based failure in terms of the subgrammar decomposition: which subgrammar's divergence grows, and does Theorem 4.6's blow-up formula predict the magnitude?
5. Explicitly state (even informally) the version of Corollary 4.5 and 4.6 without the context-insensitivity assumption, so readers can assess how much that assumption loads the elegant formula.

---

## Score and Decision

**Originality:** The subgrammar definitions and KL decomposition framework are genuinely novel organizational contributions. The parallel learning observation is a new empirical finding. The mathematical depth is modest — the theorems follow fairly closely from PCFG factorization and the chain rule — but the definitional framework is non-trivial. **3/5**

**Importance of research question:** The question of how language models acquire syntactic structure, studied through the lens of subgrammar learning dynamics, is a well-motivated and underexplored direction with potential connections to curriculum learning, interpretability, and cognitive science. **4/5**

**Claims supported:** The KL decomposition is supported visually (Figure 1) but not numerically; the parallel learning claim is well-supported empirically; the curriculum benefit claim is over-stated given that it vanishes at 4 layers; the GPT-5.1 anecdote is appropriately caveated. **3/5**

**Soundness:** The theorems are stated correctly; Theorem 4.6's slight imprecision about "unbounded" vs. "undefined" is minor. Context-insensitivity is partially addressed. No fatal errors. **3/5**

**Clarity:** The paper is well-organized and clearly written; definitions are concrete; the limitation acknowledgments are honest. **4/5**

**Community value:** As an opening paper on an underexplored direction, this work provides useful vocabulary (subgrammar definitions, context-insensitivity condition) and empirical baselines that future work can build on. The depth vs. length failure experiment is particularly clean and reproducible. **4/5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>