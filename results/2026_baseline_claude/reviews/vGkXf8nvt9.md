## Summary

The paper proposes *Forget-to-Focus (F2F)*, a two-stage LLM adaptation protocol: first apply machine unlearning (gradient ascent on a "forget set" of irrelevant general data, optionally with a stabilizing retain set), then fine-tune on a domain-specific dataset. The authors argue that proactively suppressing irrelevant pretraining knowledge reduces negative transfer and creates a more favorable optimization landscape. Experiments span five models (0.6B–72B), three domains (coding, medical, mathematics), and four unlearning variants; representational analysis using CKA and SVCCA is offered to substantiate the mechanism.

---

## Strengths

- **Breadth of empirical coverage.** Results span five architecturally diverse models (Qwen-0.6B, Gemma-2B, LLaMA-8B, LLaMA-13B, Qwen-72B) and three domains with six benchmark evaluations, providing consistent evidence that the F2F advantage is not a one-off artifact. Particularly notable are gains at the 72B scale (HumanEval 71.12 → 78.50 over SFT), suggesting the effect survives scale.

- **Multi-faceted analysis.** The paper goes beyond accuracy tables: CKA/SVCCA representational drift analysis, forget-set quality ablations (BC-Select vs. BC-Mixed vs. BC-Cosine), and unlearning-variant comparisons (GA, GA+GD, GA+KL, NPO) collectively paint a richer picture than a purely empirical study would.

- **Practically actionable design.** F2F is modular—it wraps around any existing fine-tuning recipe with no architectural change—and the BC-Cosine automatic forget-set construction provides a practical path when manual curation is infeasible, making the method usable without intimate domain knowledge.

- **Novel framing.** Using machine unlearning as *capacity reallocation for specialization* rather than a privacy tool is a legitimate conceptual reframing that can stimulate a new research direction.

---

## Weaknesses

### Fatal
None that fully invalidate the contribution. The experimental evidence for the empirical trend is real.

### Major

1. **Missing critical ablation — the mechanism is unestablished.** The paper attributes gains to removing domain-irrelevant pretraining priors (negative transfer). However, gradient ascent on any data perturbs the weight initialization before fine-tuning. The paper does not include the single most important control: *applying gradient ascent on randomly selected data with no semantic justification for being irrelevant*. Without this, it is impossible to distinguish "targeted suppression of irrelevant priors" from "generic initialization perturbation / de-anchoring from the original weights." BC-Cosine comes closest to probing this, but it still selects semantically far-from-target data rather than truly random samples.

2. **Theoretical justification is unrealistic.** The Proposition and Corollary are derived under convex, strongly convex, smooth losses with an *orthogonal decomposition* of parameter space into "relevant" and "irrelevant" subspaces, and the assumption that the optimal point lies entirely in the relevant subspace (θ* ∈ V). These are not approximations of LLM training—they are fundamentally different regimes. The paper acknowledges non-convexity but uses "a convex linear surrogate to clarify the mechanism"; the stated properties (strongly convex L_F along U, smooth retain gradient globally bounded on U) have no empirical verification and have essentially no bearing on why the method works in practice. The theory is ornamental rather than explanatory.

3. **Table 2 (fine-tuning variants comparison) does not include F2F.** Table 2 compares SFT, LoRA, CurlLoRA, and DAPT without including F2F results on the same medical benchmarks, making it impossible to assess F2F's advantage over the fine-tuning variants within the same table. The table appears disconnected from the main claim.

4. **Calibration claims lack quantitative grounding in the main body.** The abstract and introduction prominently feature improved calibration on medical QA (reducing overconfidence) as a key contribution. However, the main body contains no ECE or reliability diagram values; these are deferred to the appendix, which is missing from the reviewed text. A claim presented as a primary contribution should be supported in the main paper.

### Minor

1. **Several intermediate (pre-fine-tuning) results raise concerns about method stability.** Gemma-2B after GA+GD shows 0.00 on HumanEval; LLaMA-13B after GA shows 0.00 MBPP; LLaMA-8B after GA shows 1.20 on HumanEval. While the paper explains these as intermediate checkpoints, the level of catastrophic degradation raises questions about how sensitive the method is to hyperparameters, especially since fixed hyperparameters are used across architectures.

2. **Claimed percentage improvements in the abstract are presented without clarifying the denominator.** "32.5% on Qwen3-0.6B" appears to be a relative gain over SFT (31.71 → 42.07), not over the base model—this should be made explicit.

3. **Computational cost of F2F is not discussed.** Adding a full pre-fine-tuning unlearning phase doubles the training cost. A practical comparison (wall-clock time, FLOPs, or GPU-hours) relative to the baselines would clarify whether the accuracy gains justify the overhead.

### Trivial
- Column labels in Table 3 are absent for the "FD" (forget-set domain) dimension, requiring inference from context.

---

## Nice-to-Haves

- A semantic-null ablation: gradient ascent on *random in-domain data* or *random noise* to isolate whether any non-targeted perturbation achieves similar gains.
- Convergence curves during fine-tuning comparing F2F-initialized vs. standard initialization to verify the "cleaner optimization landscape" claim empirically.
- An analysis of how many unlearning steps are required and whether the performance saturates, guiding practitioners on the cost–benefit tradeoff.

---

## Novel Insights

The paper's most genuinely novel observation is that unlearning on a curated, domain-irrelevant corpus (BC-Select) consistently outperforms unlearning on a partially overlapping corpus (BC-Mixed), and that a cosine-similarity-based automatic selection (BC-Cosine) can approximate the hand-curated result. This operationalizes forget-set design as a core hyperparameter of the protocol rather than an afterthought, and suggests that the *semantic alignment* of the forget set matters—which is a testable and practically useful finding. The CKA observation that F2F pushes representations further from the generalist baseline than standard fine-tuning does, consistently across domains, is also a concrete geometric characterization that goes beyond the accuracy numbers. However, whether this additional drift is specifically caused by removal of spurious priors versus any initialization perturbation cannot be concluded from the current evidence.

---

## Suggestions

1. Add a "random-data" forget-set ablation: apply GA+GD on randomly sampled Wikipedia paragraphs (semantically neither close to nor far from the target domain) and compare to BC-Select/BC-Cosine. This single experiment would substantially strengthen or reframe the core claim.
2. Replace or supplement the convex-linear theory with an empirical validation of the key geometric claim: measure the distance between the unlearned initialization and the fine-tuned optimum vs. the standard initialization and the fine-tuned optimum (e.g., using linear mode connectivity or loss-surface analysis).
3. Add calibration results (ECE, reliability diagrams) for the medical domain directly in the main body to support the reliability claims.
4. Provide a timing / FLOP comparison between F2F and the baseline methods so readers can assess the practical overhead.

---

## Score and Decision

The paper tackles a timely and conceptually interesting research question with a notable amount of empirical evidence across models, domains, and scales. The representational geometry analysis and forget-set quality study add depth. However, the most critical ablation—testing whether any initialization perturbation (rather than semantically meaningful unlearning) produces similar gains—is absent, leaving the core mechanistic claim unverified. The theoretical analysis makes assumptions far removed from LLM training without providing any empirical verification of its relevance. The calibration contribution is not supported in the main body. These are substantial gaps that prevent confident acceptance in the current form.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>