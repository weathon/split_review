Now I have all the information I need. Let me write the final consolidated review.

---

## Summary
This paper initiates the study of how language models learn PCFGs with respect to the grammar's *substructure*. The authors define *inner* and *outer* subgrammars (corresponding to subtrees of derivations and subsets of rules, respectively), and prove a suite of theorems showing that the KL divergence of a language model trained on a PCFG decomposes recursively as a sum over subgrammar-restricted divergences. They train small transformers on several hand-crafted PCFGs and show empirically that (a) the decomposition holds throughout training, (b) subgrammars appear to be learned in parallel, (c) subgrammar pretraining can aid curriculum learning, and (d) models struggle with recursion depth rather than sequence length.

## Strengths
- **Novel theoretical framework**: The definitions of inner and outer subgrammars (Definitions 3.3, 3.5) and the recursive KL-divergence decomposition (Theorem 4.3, Corollary 4.4, Theorem 4.6) are genuinely original. The idea of relating the substructure of a PCFG to the loss of an autoregressive model is insightful and opens a new lens for studying learning dynamics — one not explored by prior work on transformers and CFGs (Allen-Zhu & Li, 2023; Cagnetta & Wyart, 2024).
- **Empirical validation of the decomposition**: Figure 1 convincingly demonstrates that during training, the total KL divergence equals the sum of per-subgrammar divergences plus overhead. The curves track together across epochs, confirming that the decomposition is not just a theoretical artifact but is realized in practice.
- **Clean isolation of depth vs. length**: Figure 3 provides a crisp controlled experiment: on a Nested Parentheses grammar, extending context length at depth 0 yields near-zero error while increasing recursion depth causes sharply growing error. This cleanly separates depth of recursion from sequence length as the primary difficulty.
- **Interesting parallel-learning observation**: Figure 2(a) shows that in a depth-4 recursion grammar, all subgrammar losses decrease simultaneously from early epochs rather than sequentially. This is a genuinely surprising empirical finding that raises interesting questions about optimization dynamics.

## Weaknesses

### Major
- **Theoretical exposition in the main body is too sketchy for the paper's primary claimed contribution.** The paper states that "the most important contribution is a suite of fundamental theorems," yet the main text derives the decomposition only for a single oversimplified case (S → α A β in equations (1)–(5)) and then asserts Theorem 4.3 for the general case without showing how the argument extends. Key definitions needed for the general statement — "top-level subgrammars" and the set C of fixed terminal substrings — are given but the construction connecting them to the KL decomposition is not walked through. The proof is deferred entirely to the appendix (which is unavailable). For a paper whose central claim is theoretical, the main body must at minimum make the structure of the argument and its assumptions clear; the current version does not meet that bar.
- **Experiments are limited to a few hand-crafted CFGs and tiny transformers (2-layer, occasionally 4-layer).** The empirical evidence is suggestive but too narrow to robustly support the broader conclusions. The parallel-learning observation rests on visual inspection of a handful of learning curves (Figures 1–2). No experiment is designed to test whether sequential learning *could* have been observed (e.g., by varying subgrammar difficulty or data frequency). The curriculum-learning results are reported for a single architecture scale. It is unclear whether the observed effects generalize to other architectures (LSTMs, RNNs) or scale consistently. The narrow empirical scope limits the strength of the conclusions that can be drawn.

### Minor
- **Claims about children are unsupported.** The abstract and introduction assert that small transformers learn subgrammars "in parallel, unlike children — who first master simple substructures before progressing to more complex constructions." No child data, model of child acquisition, or empirical comparison with developmental findings is provided. This rhetorical comparison should be removed or heavily qualified.
- **Overstated interpretation of CKA results.** The paper states that CKA analysis "quite definitively" shows pretraining yields representations more aligned with grammar substructure. However, the absolute CKA differences are modest (e.g., attention CKA on full-grammar sequences increases from 0.258 to 0.281, or 0.249 to 0.303; Table 1). While the relative changes (+8.9%, +21.7%) are noticeable, describing these as definitive evidence overstates what the numbers support, especially without significance testing or confidence intervals. The paper also does not control for the possibility that additional training steps, rather than subgrammar structure specifically, could drive some of the alignment increase.
- **Missing methodological details.** The paper does not specify how empirical KL divergences are computed — whether by exact inference over the PCFG or by sampling, and if sampling, what sample sizes are used and how variance is handled. The grammar definitions and model architecture details (dimensions, learning rates, etc.) are in the appendix and therefore not visible. These omissions make the experiments difficult to evaluate or reproduce.
- **Figure 6 and Table 3 are mentioned but not shown in the main text.** The claim that subgrammar pretraining can "help achieve a lower final loss" references Figure 6, which is not visible. Table 3 (sequence segregation analysis) is discussed in prose but its data are absent. These evidential gaps weaken the corresponding claims.
- **No discussion of grammar ambiguity.** The derivation of the KL decomposition relies on the autoregressive factorization, but the paper never addresses whether ambiguity in the PCFG (multiple valid parse trees for the same string) affects the decomposition. The class of grammars to which the theorems apply is left unspecified.

### Trivial
- **Definition 3.5 (Outer Subgrammar) contains an incomplete sentence.** The definition ends with "and for each of its non-terminals." — the intended condition is not stated. This is a drafting error that should be fixed.
- **The "context-insensitivity" assumption in Corollary 4.5 is acknowledged as strong**, and the paper's discussion of statistical relaxations is somewhat hand-wavy. This is not a flaw per se (the paper is upfront about it), but the exposition could be tightened.
- **Corollary 4.7 is stated informally** and its condition is not tested empirically; the paper explicitly notes this as future work, so this is not a weakness but a scope limitation.

## Nice-to-Haves
- A systematic study varying grammar complexity, model architecture (LSTM, RNN), and model scale would substantially strengthen the empirical claims and is a natural next step.
- Designing an experiment that *could* show sequential subgrammar learning (e.g., by making one subgrammar much harder or rarer) would make the parallel-learning finding more compelling than the current visual observation.
- Connecting the CKA representational alignment results back to the theoretical decomposition — e.g., showing that higher alignment corresponds to more accurate subgrammar-specific KL terms — would unify the theory and experiments more tightly.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"The appendix is said to contain the proofs, but the main paper must at minimum make the assumptions and the structure of the argument clear"** — The concern about proofs being in appendix is partially retained (as Major), but the specific complaint that the appendix is missing is not the authors' fault (the parser strips appendices). The retained version focuses on what *is* in the main body being insufficient, not on the absence of the appendix.
- **Criticism about GPT-5.1 anecdotal test** — REMOVED. The authors explicitly label this test as "purely anecdotal" and state it "should not be interpreted as direct evidence." A reviewer criticizing something the authors already disclaimed is redundant.
- **"No empirical check of whether Corollary 4.7 condition holds"** — DEMOTED and partially removed. The paper explicitly says this is "an immediate future direction." Criticizing a paper for not doing what it identifies as future work is scope creep.
- **Strength about "curriculum learning yields both better final loss and structurally aligned representations"** — Figure 6 data not visible; the strength is retained but qualified.
- **Generic strength about "this paper addresses an important problem"** — REMOVED as superficial.
- **"The CKA analysis does not control for the trivial effect that pretraining forces the model into a region of weight space"** — This is speculative (depends on how the comparison is structured; pretrained and from-scratch models may have similar total training epochs). Kept a softened version under Minor.
- **Criticism about "missing related works"** — REMOVED per hard rule (do not mention missing related works).
- **Grammar ambiguity concerns as "fatal"** — DEMOTED from fatal to Minor. The concern is real but the harsh critic frames it as potentially fatal without demonstrating that ambiguity actually breaks the decomposition in the grammars tested. The PCFGs used may well be unambiguous; the paper simply doesn't say.
- **"The derivation assumes the prefix uniquely determines the subgrammar being expanded"** — REMOVED. The autoregressive factorization does not require unique determination; it conditions on the actual observed prefix. The KL decomposition follows from the fact that both P_G and Q_θ factorize autoregressively, which is always valid. This criticism reflects a misunderstanding.

## Novel Insights
The parallel-learning observation (Figure 2a) — that all subgrammar losses decrease simultaneously rather than sequentially — is genuinely striking and not predicted by the theoretical decomposition alone (which only says the sum decomposes, not whether optimization of components happens in parallel or sequence). The paper provides a plausible sufficient condition (Corollary 4.7, the "independence" of gradient updates across subgrammars) that could explain this phenomenon. Whether overparameterization in small transformers naturally satisfies this condition is an open question the paper poses explicitly, and it represents a novel connection between optimization dynamics and grammatical structure.

## Suggestions
- **Strengthen the theoretical exposition in the main body.** Walk through how the decomposition extends from the simple S → α A β case to the general case with multiple top-level subgrammars, even if at a higher level of abstraction than the full proof. State explicitly what class of PCFGs the theorems apply to (e.g., are they required to be unambiguous? In a particular normal form?).
- **Expand the empirical scope.** Test on at least one more grammar family (e.g., a grammar with ambiguity, or a grammar drawn from natural language syntax) and at least one non-transformer architecture (LSTM). This would substantially increase confidence in the generality of the findings.
- **Tone down unsupported claims.** Remove or heavily qualify the "unlike children" comparison, soften "quite definitively" for the CKA results, and ensure Figure 6 and Table 3 data are visible in the main text or clearly referenced as appendix material.
- **Report how empirical KL divergences are computed** — exact inference or sampling, and if sampling, sample sizes and variance estimates.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| F0Zd3knG9j (PCFG + hierarchical filtering + transformers) | 5.00 | R1, R2 | Most directly comparable: similar domain (PCFG + transformer learning dynamics), similar mix of theory and limited experiments. Our paper has more novel theory; F0Zd3knG9j has more thorough attention analysis. Comparable quality. |
| MO5PiKHELW (Syntax acquisition, phase transitions in MLMs) | 5.50 | R2 | Studies syntax acquisition dynamics in BERT with causal interventions. Stronger empirical validation (real models, real benchmarks), but our paper has more theoretical novelty. Our paper is weaker empirically. |
| fp77Ln5Hcc (Depth extrapolation on nested structures) | 4.50 | R1, R2 | Similar topic (depth extrapolation on Dyck/parentheses), but had serious presentation issues and narrower scope. Our paper is stronger. |
| 0pLCDJVVRD (Percolation model of emergence) | 7.00 | R1 | Well-written, clear theory+experiments on formal language learning with transformers. Significantly stronger than our paper in execution quality. |
| aWLQTbfFgV (Neural networks as formal language recognizers) | 6.25 | R2 | Thorough, systematic evaluation across many languages and architectures. Our paper is narrower and less systematic. |
| STUGfUz8ob (Transformers reasoning with abstract symbols) | 7.60 | R1 | Rigorous theory with proofs in main body, clean experiments, architectural innovation. Much stronger than our paper. |

**Round 1 bracket:** 4.5 – 7.0. The paper sits above fp77Ln5Hcc (4.50, narrower scope, serious presentation issues) and below 0pLCDJVVRD (7.00, significantly better execution).

**Round 2 narrowing:** The paper is most comparable to F0Zd3knG9j (5.00) — both study transformer learning on PCFG-structured data with a mix of theory and limited experiments. Our paper has a more original theoretical contribution (subgrammar KL decomposition vs. belief propagation, which was already known). It sits slightly below MO5PiKHELW (5.50) which had more thorough empirical validation with real models. The final score is **5.0**.

The theoretical ideas (subgrammar decomposition of KL divergence) are genuinely novel and interesting, but the main body does not present the theoretical argument with sufficient rigor for a paper whose primary contribution is theoretical. The empirical validation, while providing supporting evidence for the decomposition and some interesting phenomena (parallel learning, depth vs. length), is too narrow in scope. The paper has clear merit and opens promising directions, but in its current form the execution does not fully support the strength of the claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>