Now I have all the information I need. Let me verify the reviewer's claims against the paper text and produce the consolidated review.

## Verification Summary

**Reviewer Point 1 (NW not derived from optimization objective):** The paper at lines 57–66 explicitly says: *"Lemma 1 assumed that each component of vector function f(x) is within the RKHS family... However, having arrived at this form, we note that the overall gradient for f(x) is effectively a kernel-weighted average over isolated gradients... We now seek to employ this insight, and move beyond the assumption that f(x) is in a RKHS."* Then Proposition 1 states it is *"a direct application of the Nadaraya–Watson kernel-weighted average... without assumption on the form of f(x), yielding a generalization of (1)."* The paper is transparent about this being a generalization of the update *form*, not a new optimization objective. The reviewer's claim that the paper presents it as rigorous gradient descent from an objective is not supported by the text. The term "Averaged Gradient Descent" is somewhat imprecise but the surrounding text is clear.

**Reviewer Point 2 (Exact claim only for first step):** The paper consistently says *"one functional gradient step"* (line 93), *"exactly implement one functional-gradient step"* (line 100), abstract: *"a functional-gradient step."* The construction is from zero initialization. The paper is accurate. No overstatement.

**Reviewer Point 3 (Multi-layer not validated):** The paper explicitly states at lines 152–153: *"none of the two-layer results are significantly different from those of the one-layer model. This phenomenon was observed in all of our experiments."* And in conclusions (line 172–176): *"we observed that a single-layer model is often sufficient."* The paper is transparent about this finding. This is reported as a result, not a claimed success of the multi-layer theory.

**Language model speculation:** The paper says *"One conjecture is that language models may predict the next token using inference like that considered here"* (line 176). Explicitly labeled as conjecture — transparent.

---

## Summary

This paper extends the functional-gradient-descent interpretation of Transformer in-context learning from real-valued outcomes with Gaussian likelihoods to categorical outcomes with softmax likelihoods. It derives the functional gradient for the categorical case (Lemma 1), proposes a Nadaraya–Watson kernel-averaging generalization that connects to softmax attention (Proposition 1), and constructs a single-layer attention mechanism that exactly implements one functional gradient step from zero initialization (Section 4). Multi-layer extensions are also developed. Experiments on synthetic data and ImageNet classification demonstrate that the structured single-layer model (GD) is effective and often outperforms fully-learned Transformers.

## Strengths

- **Generalizes functional-gradient ICL theory to categorical outcomes with softmax likelihood.** Prior work (von Oswald et al., 2023; Cheng et al., 2024; Mahankali et al., 2023) was restricted to real-valued outcomes and Gaussian noise. This paper derives the functional gradient for categorical Y with softmax p(Y|f(x)) (Eq. 2) and constructs a single attention layer that exactly implements one gradient step for this setting (Section 4). This is a genuine extension of the theory to a practically important class of problems.

- **Connects softmax attention to a Nadaraya–Watson kernel interpretation (Proposition 1).** The paper shows that softmax attention can be understood as a Nadaraya–Watson kernel-weighted average of per-sample functional gradients, without requiring the latent function to lie in an RKHS. This provides a new theoretical bridge between attention mechanisms and nonparametric regression that is distinct from the RKHS analysis in Lemma 1.

- **Demonstrates that a single attention layer is often sufficient for categorical in-context learning.** Synthetic experiments (Figures 1–3) show that one-layer GD-based models match or nearly match two-layer models. The paper provides clear explanations (lines 152–153) — the most-probable category may already be captured after one step — turning this into a practical insight rather than a failure.

- **Identifies and leverages training difficulties for fully-trained Transformers in categorical settings.** The paper shows that randomly-initialized Trained TF underperforms the structured GD model (Figure 1), and that initializing with GD parameters stabilizes training (Figure 2). This connects known Transformer training challenges (Liu et al., 2023) to the theoretical framework and provides a concrete initialization strategy.

- **Validates the theory on a real-world ImageNet classification task.** Unlike most prior ICL work limited to synthetic regression, the paper applies a single-layer GD Transformer to in-context classification of ImageNet VGG features (Figure 4, right), achieving accuracy close to an oracle linear-probing baseline. This demonstrates applicability beyond idealized settings.

- **Shows softmax attention has automatic robustness to varying context size.** While linear and RBF attention require rescaling when test N differs from training N, softmax attention maintains stable performance without adjustment (Figure 4, left). This is traced to the inherent normalization in the Nadaraya–Watson form (Proposition 1 vs. Lemma 1), giving a practical deployment advantage.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The Nadaraya–Watson "gradient descent" framing (Proposition 1) could be clearer about its status.** The paper calls Proposition 1 "Nadaraya-Watson Averaged Gradient Descent." While the surrounding text (lines 57–66) explains that it is a generalization of the RKHS gradient descent *form* — not derived from a loss functional — the terminology could mislead readers into thinking this update is guaranteed to correspond to an optimization objective. The paper would benefit from an explicit statement that this is a heuristic generalization motivated by the form of Lemma 1, not a gradient of any functional in function space. This does not undermine the contribution, but would improve clarity.

- **The multi-layer extensions are approximate and the experiments show no benefit from additional layers.** The linear and nonlinear multi-layer constructions (Section 4) are presented as approximating later gradient steps, but the paper is transparent that they do not implement exact gradient steps. The experiments (Figure 3) confirm that additional layers yield no improvement. While the paper offers plausible explanations (lines 152–153), the multi-layer analysis remains unvalidated as a theory of deeper Transformers. The paper is honest about this, but it limits the scope of the claimed multi-layer contribution.

- **The ImageNet experiment lacks error bars and a standard Transformer baseline.** Results are reported without confidence intervals or standard deviations (Figure 4, right). The comparison to linear probing, while reasonable, does not include a standard off-the-shelf Transformer trained from scratch on ImageNet ICL — this would help calibrate how much the GD structure helps versus the inherent difficulty of the task. The paper acknowledges the linear probing comparison is "not entirely fair" (line 161), but the absence of a Trained TF baseline on ImageNet leaves a gap.

- **Choice of d′=4 for ImageNet is not justified.** The paper sets the embedding dimension to d′=4 without discussing why this value is appropriate or showing an ablation. For a dataset with 100 test classes and 512-dimensional VGG features, this choice merits some explanation.

### Trivial

- The paper could state more explicitly that the exact single-layer gradient step is from zero initialization (f(0)=0). While this is clear from the construction (Section 4), a brief qualifier in the abstract/contributions list would prevent any ambiguity.

## Nice-to-Haves

- **Alignment measurement:** The causal narrative would be strengthened by measuring cosine similarity between the attention output and the true functional gradient at initialization on synthetic data.
- **ImageNet Trained TF baseline:** Adding a Trained TF baseline (initialized randomly) on the ImageNet task would strengthen the empirical story, though training difficulty may make this non-trivial.
- **Confidence intervals:** Adding error bars or confidence intervals to the ImageNet results (Figure 4, right) would strengthen statistical reliability.
- **Pseudocode/diagram** for the multi-layer linear approximation would improve reproducibility, as the notation is dense.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that Proposition 1 is "not derived from any optimization objective" and is a "structural issue":** The paper transparently presents Proposition 1 as a generalization of the gradient descent *form* from Lemma 1, not as a new optimization-derived result. The paper states "without assumption on the form of f(x), yielding a generalization of (1)." The criticism overstates the problem; the paper's logic is clear. **Removed as factually misaligned with the paper's stated framing.**

- **Criticism that the "exact implement" claim could mislead readers about multi-layer applicability:** The paper consistently says "one functional gradient step" and "a functional-gradient step" (abstract, line 93, line 100). The construction is for a single layer from zero initialization. The paper is accurate. **Removed as the paper's claims are correct and qualified.**

- **Criticism that the language model discussion (conclusions) is "very speculative":** The paper explicitly introduces this as "One conjecture is that..." (line 176). It is clearly labeled as a conjecture. **Removed — the paper is transparent about the speculative nature.**

- **Criticism that the paper lacks baseline comparison with a standard off-the-shelf Transformer on ImageNet:** The paper already compares to linear probing (a strong upper bound) and discusses training difficulties. Adding this baseline is a reasonable suggestion but not a weakness given the paper's scope. **Moved to Nice-to-Haves.**

## Novel Insights

Beyond the paper's own contributions, the most interesting observation to emerge from the reviews is that the NW generalization (Proposition 1) and the RKHS derivation (Lemma 1) yield different normalizations (no 1/N in the NW case), and the experiments confirm this difference matters in practice — softmax attention is automatically robust to varying context size (Figure 4, left). This practical consequence of a seemingly subtle theoretical distinction is worth highlighting. The review also surfaced that the sufficiency of a single layer is not a limitation but a meaningful finding about categorical ICL: the most-probable category is often determined in one gradient step, which has implications for designing efficient in-context classifiers.

## Suggestions

1. Add an explicit sentence in Section 2 or the abstract clarifying that Proposition 1 is a heuristic generalization of the gradient descent *form* rather than a gradient of any loss functional. This will preempt the main clarity concern.
2. In the contributions list (Section 1), add "from zero initialization" to the claim about exact gradient-step implementation — this is already implicit but making it explicit avoids any ambiguity.
3. Add standard deviations or confidence intervals to the ImageNet results (Figure 4, right).
4. Briefly justify the choice of d′=4 for ImageNet or add an ablation.
5. Consider adding a cosine-similarity analysis between the attention output and the true functional gradient on synthetic data to provide direct evidence for the interpretation.

## Score and Decision

The paper makes a genuine contribution by extending the functional-gradient framework for Transformer ICL to categorical outcomes with softmax likelihoods, constructing an exact single-layer implementation, and validating it empirically. The weaknesses identified are minor clarity issues and missing experimental details rather than fundamental flaws. The paper's claims are supported by the evidence, and the limitations are transparently discussed.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>