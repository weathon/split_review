- Decision: Reject
- Avg Score: 3.57
- Scores: 5, 3, 3, 3, 5, 3, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper extends the functional-gradient-descent interpretation of Transformer in-context learning from real-valued outcomes with Gaussian noise to categorical outcomes with softmax probability. It shows that a single attention layer can exactly implement one step of functional gradient descent for categorical Y, and connects softmax attention to Nadaraya-Watson kernel-weighted averaging. The paper provides explicit constructions for single- and multi-layer Transformers and validates them on synthetic data and ImageNet classification.

## Strengths

- **First exact functional-gradient construction for categorical Y with softmax**: Lemma 1 derives the RKHS gradient update for general $p(Y|f(x))$, and equation (2) gives the specific gradient $w_{y_j} - \mathbb{E}(w_c)_{|f_k(x_j)}$ for categorical Y. Section 4 then shows how to encode this gradient into a single attention layer via the encoding $h_i^{(0)} = (x_i, 0_{d'}, w_{y_i} - \frac{1}{C}\sum_c w_c)^T$ and designing $W_V$ to produce the gradient. This extends prior work (Mahankali et al., 2023) from real-valued Y with Gaussian noise to categorical Y with softmax, and the construction is cleanly argued.

- **Novel connection between softmax attention and Nadaraya-Watson kernel averaging**: Proposition 1 shows that for $K_\lambda(x_j,x) = \exp(\lambda x^T x_j)$, the Nadaraya–Watson averaged gradient becomes exactly the softmax attention mechanism. This provides a principled interpretation of softmax attention as kernel-weighted averaging without requiring the latent function to live in an RKHS, and the paper is transparent that this is a heuristic generalization motivated by the RKHS case.

- **Practical advantage of softmax attention for varying context sizes**: Figure 4 (left) demonstrates that softmax attention maintains stable performance as test context size N varies from 25 to 300 (trained on N=125) without requiring the $1/N$ rescaling that RBF and linear attention need. This practical benefit follows directly from the inherent normalization in the Nadaraya–Watson formulation and is cleanly validated experimentally.

- **GD construction provides a strong, principled baseline**: The parameter-efficient GD model (which implements the functional gradient step) outperforms a fully trained Transformer from random initialization (Figure 1). When the trained Transformer is initialized from the GD parameters, its performance barely moves (Figure 2), confirming that the theoretical construction captures an effective solution. This provides concrete evidence that the theoretically-motivated design is practically useful.

## Weaknesses

### Fatal
None.

### Major

- **The "upper bound" framing of GD over Trained TF is imprecise, and the GD-vs-Trained-TF comparison does not cleanly validate the theory as claimed.** The paper states that GD "may be viewed as an upper bound on what Trained TF could achieve" (line 140). However, the GD model's weight matrices $W_Q, W_K, W_V, P$ are fixed to exactly implement the functional gradient step, and the synthetic data was explicitly constructed to match this structure (RBF kernel-based latent functions with anchor points). That GD outperforms a randomly-initialized Trained TF partly reflects that GD has the correct inductive bias for this specific data generation process, not purely that the functional-gradient interpretation is the "right" explanation. The paper does discuss training difficulties for Trained TF, but a more informative comparison would be: (a) testing whether Trained TF with better optimization (systematic hyperparameter search, learning rate schedules) can close the gap, or (b) comparing GD to a Trained TF that has the same architectural constraints but learns all parameters from scratch. Without such controls, the experiment primarily validates that the design works for its intended generative model, which is useful but more limited than the "upper bound" language suggests.

- **The claim that "a single-layer model is often sufficient" rests on limited experimental evidence.** The paper asserts this in the abstract, introduction, and conclusions, but the supporting evidence comes almost entirely from one synthetic configuration ($C=25$, $d'=5$, $N=125$, one RBF-based generative model). Figure 3 shows no improvement from two layers, and the ImageNet experiment uses only one layer, but this is insufficient to establish "often" as a general claim. Alternative explanations are not ruled out: the data generation procedure may make the problem too easy (the anchor-point design with $\lambda=10$ ensures each category is clearly most probable near its anchor), the two-layer approximations (linearized expectation and FF-based) may be poorly designed, and only top-1 accuracy is reported (log-likelihood could reveal improvements that accuracy misses). The paper should test multiple settings with varying difficulty (more categories, overlapping decision boundaries, higher noise) and report log-likelihood, not just accuracy, before generalizing.

### Minor

- **The ImageNet experiment lacks meaningful baselines and is primarily a proof-of-concept.** The paper compares only to linear probing, which it explicitly acknowledges is "not an entirely fair comparison" since it trains a new model per task. Standard meta-learning or few-shot baselines that also do not fine-tune per task (e.g., k-NN on the VGG features, Prototypical Networks, Matching Networks) would provide useful context. Without these, the experiment demonstrates feasibility but does not convincingly show broad applicability or competitiveness. The experiment is still a useful large-scale demonstration; it simply does not support the weight of the claims attached to it.

- **The varying-context-size experiment (Figure 4 left) is only tested with GD models, not Trained TF.** The paper argues that softmax attention avoids the need for $1/N$ rescaling, but this is validated only for the GD model where the attention mechanism is fixed. It is plausible that a trained Transformer with learned attention would also handle varying N, but this is not tested. Given that the paper highlights this as a practical advantage of its framework, testing on Trained TF would strengthen the claim.

- **The connection to standard Transformer attention lacks discussion of the $\sqrt{d_k}$ scaling factor.** The paper uses $K_\lambda(x_j,x) = \exp(\lambda x^T x_j)$ as the softmax attention kernel, but standard Transformer attention uses $(W_Q x)^T (W_K x_j) / \sqrt{d_k}$. The omission of the scaling factor and the role of learned key/query projections (which the GD model fixes) limits the precision of the claimed connection to actual Transformers. This is a minor technical gap in an otherwise clear exposition.

### Trivial
None.

## Nice-to-Haves

- Test more synthetic configurations with varying difficulty (more categories $C$, overlapping decision boundaries, lower $\lambda$ for less separable classes) to establish when single layers suffice and when deeper layers matter.
- Include a simple non-parametric baseline (e.g., k-NN on VGG features) for the ImageNet experiment to contextualize the Transformer's performance.
- Report log-likelihood on held-out test data alongside accuracy for the synthetic experiments, to detect improvements in probability calibration that deeper layers might provide.
- Explore whether Trained TF with more systematic hyperparameter optimization (beyond early stopping) can close the gap with GD from random initialization, which would strengthen the paper's claims about the theory's explanatory value.

## Removed Points

*"The comparison to linear probing is explicitly acknowledged as unfair, yet the paper still highlights that the Transformer is 'close' to linear probing."* — **Removed** because the paper explicitly and transparently discusses the limitations of this comparison (lines 160–162). The authors do not misrepresent the result; they highlight it with appropriate caveats.

*"Proposition 1 is not derived from any function-space gradient descent; it is simply a kernel-weighted averaging."* — **Removed** because the paper is explicit that this is a direct application of Nadaraya-Watson averaging that "move[s] beyond the assumption that f(x) is in a RKHS" (lines 57–66). The paper does not claim it is a rigorous functional gradient descent step; it transparently presents it as a heuristic generalization.

*"The paper does not explore learning rate schedules, weight decay, or other standard practices."* — **Removed** because the paper uses Adam with early stopping (line 125) and cites relevant literature on training difficulties (Liu et al., 2023). Specific hyperparameter tuning is best addressed in supplementary materials, and the paper provides sufficient training details for reproducibility.

*"The synthetic data is too favorable to the proposed method."* — **Removed** as formulated because this is a critique of the experimental design choice, not an error. The paper explicitly constructed the data to match the theoretical assumptions, which is a standard and valid approach for validating a theory. The point is partially subsumed under the Major weakness about limited evidence for single-layer sufficiency.

*"Missing related works" and "Missing appendix content"* — **Removed** per instructions (parser strips appendices; the reviewer cannot know what was omitted).

*Various unspecified reproducibility concerns about undisclosed hyperparameters* — **Removed** per instructions (trivial implementation details not required for a submission).

*Strengths that are generic or conflict with verified weaknesses* — **Removed** the strength about "Demonstration on real-world ImageNet classification" being a core strength; it is retained as acknowledged but qualified. The strength about "Single-layer model often sufficient, validated experimentally" is partially retained but qualified under the Minor weakness that the evidence is limited.

## Novel Insights
None beyond the paper's own contributions. The two reviews surface no observation about the paper that the paper does not already state or imply about its own limitations. The main value of the synthesis is in separating the harsh critic's valid concerns (limited evidence for "often sufficient," imprecise "upper bound" framing) from the noise (criticisms that the paper already addresses, or that are speculative).

## Suggestions

1. **Tighten the interpretation of the GD-vs-Trained-TF comparison.** Replace the "upper bound" framing with a more precise description: GD provides a theoretically-motivated structured model that captures the data-generating process, and its strong performance relative to a fully learned Transformer demonstrates that the functional-gradient construction is a useful inductive bias. Remove the implication that this validates the theory over alternatives.

2. **Broaden the experimental support for the "single-layer sufficiency" claim.** Test at least 2–3 additional synthetic configurations (e.g., more categories $C=50$, lower $\lambda$ for less separable classes, higher noise) and report log-likelihood in addition to accuracy. If the claim holds across these settings, it is much stronger; if not, qualify the claim appropriately.

3. **Add simple baselines to the ImageNet experiment.** A k-nearest-neighbor classifier on the VGG features (which also does not fine-tune per task) would provide a natural and informative comparison that respects the same constraints as the Transformer. This would make the ImageNet results more self-contained and interpretable.

4. **Test the varying-context-size experiment with Trained TF in addition to GD.** This would confirm that the practical advantage of softmax attention generalizes beyond the constrained GD setting and applies to learned attention as well.
