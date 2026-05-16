Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes a probabilistic graphical model (PGM) perspective on Sparse Mixture of Experts (SMoE) and introduces two routing mechanisms — Similarity-Inform SMoE and Attention-Inform SMoE — that allow tokens to influence each other's expert assignments rather than making conditionally independent decisions. The aim is to reduce routing fluctuation, a known stability problem in SMoE. The paper provides a theoretical entropy bound (Proposition 1) and presents experiments on ImageNet classification and Wikitext-103 language modeling demonstrating reduced routing fluctuation, improved accuracy/perplexity, and robustness gains on corrupted/adversarial variants.

## Strengths

- **Novel method for token-aware routing that demonstrably reduces fluctuation.** Figure 2 (Left) directly measures the proportion of tokens switching expert assignments between consecutive training epochs: baseline SMoE shows up to ~20% fluctuation in early layers, while both Mutual-Inform variants cut this to near zero. This is the paper's most direct and compelling evidence.

- **Theoretical entropy bound (Proposition 1).** The paper proves that under the Mutual-Inform mechanism, as the temperature parameters approach zero, the entropy of the final routing distribution is bounded above by the entropy of the original (independent) routing scores. This provides formal backing for the intuition that token-token interaction yields more confident (less fluctuation-prone) decisions.

- **Consistent empirical gains across two tasks and multiple robustness benchmarks.** Tables 1 and 2 report improvements on Wikitext-103 (perplexity, clean and adversarial) and ImageNet (clean, ImageNet‑C, ‑A, ‑R, ‑O) over SMoE, GLAM, and V‑MoE baselines. The breadth of the robustness evaluation (five ImageNet variants) is a genuine strength.

- **Principled connection between attention and mixture-of-experts regression.** The PGM derivation showing that multihead attention can be interpreted as a point estimate of a 2-layer hierarchical mixture-of-experts regression (Section 2.1) and that attention-SMoE extends this to a 3-layer model is a novel conceptual contribution, regardless of whether one agrees that the PGM is the most parsimonious explanation.

## Weaknesses

### Fatal

None.

### Major

- **No experimental comparison to existing routing-stability methods.** The paper identifies routing fluctuation as the target problem, cites StableMoE, SMoE-dropout, router Z‑loss, and hash layers in Section 5, and claims its approach is "orthogonal" — yet provides zero empirical comparison to any of them. Without a head-to-head comparison (or at least a combination study), the reader cannot assess whether Mutual-Inform SMoE is better, worse, complementary, or simply redundant with prior solutions. This is the single biggest gap in the evaluation.

- **No ablation studies to isolate which components drive the improvement.** The proposed methods combine multiple design choices: (a) the similarity/attention weighting, (b) the temperature/hyperparameters, (c) the head-selection heuristic for Attention-Inform, and (d) the specific form of the routing aggregation. There is no ablation that separates, e.g., similarity-based weighting from a simpler uniform smoothing over neighbor tokens, or that compares the full posterior to the single-head approximation. Without such ablations, the paper cannot attribute the gains to the claimed mechanism rather than to generic smoothing or hyperparameter differences.

### Minor

- **The PGM framework is a post-hoc interpretation, not a causal derivation.** The paper constructs a graphical model whose conditional expectations reproduce the MoE computation by design, then asserts that the conditional independence implied by this model "can lead to routing fluctuation." No formal argument links conditional independence to instability; the link is observational (SMoE fluctuates; Mutual-Inform removes independence and fluctuates less). The PGM provides a useful conceptual vocabulary but does not *derive* the methods or *explain* the root cause. The paper would not lose substance if the PGM were de-emphasized and the methods presented directly as token-aware routing heuristics.

- **The theoretical guarantee in Proposition 1 is weakened in practice.** The proposition requires $J_i$ to contain only tokens with entropy $\leq$ token $i$'s entropy. The paper states "In practice, we relax constraints by letting $J_i = \{1,\ldots,N\}$." This relaxation breaks the inequality, and the paper does not discuss whether the entropy bound still holds empirically or whether the method could increase entropy for some tokens. The theory is used to motivate the approach, but the actual implementation may not satisfy the stated condition.

- **The Attention-Inform head-selection heuristic is not well justified.** The paper approximates the full multi-head posterior by selecting only the head with the lowest average attention entropy, with the justification that this "enhances posterior certainty while reducing computational overhead." No argument or experiment shows why the lowest-entropy head is the most informative for routing — one could equally argue that a diverse or high-entropy head captures richer token relationships. This is a practical design choice that should be validated or at least discussed.

- **Confusing mention of the DeiT baseline.** In Section 4 (ImageNet results), the text says methods are "consistently more robust than the DeiT baseline." DeiT is a vanilla Transformer, not an MoE model, and this comparison is not meaningful for assessing routing improvements. The primary comparison is against V‑MoE, which is sufficient; the DeiT reference should be clarified or removed.

### Trivial

- Some notation inconsistencies (e.g., the symbol $\bar{\mathbf{U}}$ is used both as the MHA output and as the conditional expectation $\mathbb{E}[\tilde{\mathbf{U}} \mid \mathbf{X}]$, which is fine but could be made more explicit).

## Nice-to-Haves

- A simple baseline where each token's routing scores are averaged with a fixed (non-learned) kernel (e.g., uniform or Gaussian over a local window) would test whether the specific learned similarity/attention weighting matters, or whether any form of token-to-token smoothing suffices.

- Hyperparameter sensitivity analysis for the temperature parameters $\tau$ and $\sigma$ (which control the theoretical entropy bound) would help practitioners understand how to set these values.

- Comparison to StableMoE on the same backbone would directly position the contribution relative to the most related prior work.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The PGM framework is circular / does not establish causality"** — The harsh critic frames the PGM motivation as a "structural flaw." However, the paper does not claim to *prove* that conditional independence causes fluctuation; it observes fluctuation empirically (33% token switch rate), notes the PGM implies conditional independence, proposes removing that independence, and shows empirically that fluctuation decreases. This is a standard scientific workflow (observe → hypothesize → intervene → evaluate). The PGM is a conceptual lens, not a causal proof. The criticism overstates the flaw.

- **"The generative process is engineered to match attention-MoE computation"** — This is the entire point of the derivation: showing that MHA *can be interpreted as* a specific PGM. Calling this circular misunderstands the nature of constructive proofs in probabilistic modeling.

- **"Uniform prior over heads is not true in learned attention"** — Misunderstands Bayesian modeling. The prior $1/H$ is a modeling choice that yields the correct MHA formula ($\frac{1}{H}\sum_h$). Priors do not need to match learned posteriors.

- **"The Gaussian likelihood is introduced only to make the posterior tractable"** — This is standard Bayesian practice (conjugate likelihoods), not a weakness.

- **"Actual computation uses attention weights $A_h$ directly, not $A'_h$"** — Factually incorrect. Equation 10 defines $A'_h$ with Gaussian weighting, and Definition 2 explicitly uses $A'_{h^*}$.

- **"No baseline details / missing hyperparameters / missing model architecture specifics"** — The Reproducibility Statement says code is in supplementary materials, and experimental details likely appeared in the appendix (which the parser strips). The paper provides enough information for an informed assessment in the main text. However, the *absence of comparison to existing methods* and *absence of ablations* remain valid structural gaps.

- **Strength from Strength Finder: "Orthogonality to prior stabilization methods"** — The paper claims orthogonality but does not demonstrate it experimentally. Since this strength conflicts with the verified weakness (no comparison to existing methods), the weakness prevails. Moved here.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent tension: the paper has a genuinely interesting core idea (token-aware routing with similarity/attention weighting) and half-convincing evidence, but the evaluation lacks the rigor and breadth needed to fully establish the contribution, and the PGM framing is more decorative than explanatory. No reviewer identified a use or implication of the work that the paper itself does not discuss.

## Suggestions

1. **The highest-priority revision is to add experimental comparisons to StableMoE and SMoE-dropout** on the same backbone (V‑MoE). Even a single comparison showing that Mutual-Inform SMoE matches or complements these baselines would substantially strengthen the paper. If computing budget is limited, at least discuss why a direct comparison is difficult and provide a qualitative comparison.

2. **Add ablation studies** that isolate: (a) similarity weighting vs. uniform smoothing, (b) the effect of the temperature $\tau$, and (c) the single-head approximation vs. the full multi-head posterior. This would establish that the specific form of the routing interaction matters.

3. **Either constrain $J_i$ as Proposition 1 requires (tokens with lower entropy) and compare performance, or explicitly discuss why the relaxation is benign and provide empirical evidence that the entropy bound still holds in practice.** The current treatment leaves a gap between theory and implementation.

4. **De-emphasize the PGM framework in the title/abstract if it is not essential to the method's justification.** The methods can be presented directly as token-aware routing with similarity/attention weighting, and the paper would be cleaner and more honest. The PGM can remain as a conceptual interpretation in a dedicated subsection.

5. **Clarify or remove the DeiT baseline reference** in the ImageNet results section — it is confusing and does not serve the paper's narrative.

## Score and Decision

**Originality:** Moderate. Token-aware routing is a natural idea but the specific formulation (weighted aggregation of peer routing scores via similarity/attention) is new.

**Importance of research question:** High. Routing fluctuation is a recognized problem in SMoE, and improvements in stability have practical implications for large-scale deployment.

**Claims supported:** Partially. The fluctuation reduction is convincingly shown (Figure 2). The performance/robustness gains are reported but the evidence is weakened by the absence of ablations and comparisons to existing methods.

**Soundness of experiments:** Moderate. The core experiment (fluctuation measurement) is well-designed. The absence of confidence intervals, ablations, and head-to-head comparisons limits the conclusions that can be drawn.

**Clarity of writing:** Fair. The PGM notation is heavy and occasionally obscures the intuitive simplicity of the method. The paper would benefit from clearer exposition of the core idea before diving into the formalism.

**Value to community:** Moderate. If the method proves robust under more rigorous evaluation, it could become a useful tool in the SMoE toolkit. In its current form, the contribution is promising but not yet established at a conference-level bar.

The paper presents a genuinely interesting approach to a real problem, with preliminary evidence that the core idea works, but the evaluation is incomplete in ways that prevent a strong accept. The biggest gaps are the absence of comparison to existing routing-stability methods and the lack of ablations. These are addressable in a major revision, but in the current form the contribution is not convincingly situated relative to prior work.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>