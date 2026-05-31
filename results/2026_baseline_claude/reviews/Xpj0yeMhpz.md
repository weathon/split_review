## Summary

This paper decouples the class label and target concept in class-wise machine unlearning, identifying three novel scenarios beyond the conventional "all matched" setting: *target mismatch* (data and model at class level, target at superclass level), *model mismatch* (data and target at class level, model trained on superclass), and *data mismatch* (data at class level, target and model at superclass level). The authors formalize these via label domain relationships, prove a "representation gravity" theorem showing gradient ascent on one subset proportionally affects semantically nearby subsets, and propose TARF—a three-phase framework using annealed gradient ascent and target-aware gradient descent to identify and separate target concepts. Comprehensive experiments on CIFAR-10/100, ImageNet, stable diffusion, and LLaMA3.2 demonstrate TARF's effectiveness.

---

## Strengths

- **Novel, well-motivated problem formulation.** The decoupling of forgetting-data label domain (ℒ_D), model output domain (ℒ_M), and target concept domain (ℒ_T) into a clean three-way taxonomy is a genuinely original contribution. The practical motivation—GDPR-style requests may identify specific instances of a concept while the target to remove is broader or narrower—is compelling and underexplored. The case study using CIFAR-100's fine/superclass structure provides a clean and reproducible instantiation.

- **Principled theoretical analysis supporting algorithm design.** Theorem 3.2 establishes that gradient ascent on subset s₁ affects s₂ proportionally to their representation distance d_h(x₁, x₂), providing a formal basis for the "representation gravity" phenomenon. This directly motivates both why existing methods fail in mismatch scenarios (over-entanglement or under-representation) and how TARF's target identification via loss-change monitoring addresses them.

- **Comprehensive and convincing empirical evaluation.** The main results (Table 3) show TARF achieving Gaps of ≤1.23% in target mismatch vs. ≥8.86% for the next best method (GA on CIFAR-100), and similarly dominant margins in data mismatch, while remaining competitive in the all-matched benchmark. Evaluation spans CIFAR-10/100, TinyImageNet, ImageNet-1k (Table 4), stable diffusion concept removal, and LLaMA3.2 on TOFU. The fine-grained UA-F/UA-R split in Table 2 provides additional diagnostic insight for model mismatch.

- **Algorithm design is grounded in empirical analysis.** Figures 3 and 5 empirically verify the representation gravity dynamics (tSNE, loss trajectory, class-wise accuracy drops) before designing the algorithm. The ablation studies (Figure 7) systematically characterize the roles of k(t), phase length t₀/t₁, and the choice of gradient operation on identified data.

---

## Weaknesses

### Fatal
None.

### Major

- **Oracle assumption in target mismatch setting.** The paper explicitly states: *"we assume that the number of classes in D_un belonging to the target concept is known in target mismatch forgetting."* This is used to threshold β for identifying false retaining data. In practice, the developer typically would not know how many subclasses belong to the concept they are trying to forget—this oracle information is precisely the kind of knowledge the unlearning request is meant to avoid. The weakly-supervised experiments are deferred to the appendix and only briefly mentioned; they should be elevated to the main text since they determine the actual practical applicability.

- **LLM experiments (Table 5) are inconclusive.** Across most settings in Table 5 (particularly representation mismatch and data mismatch rows), TARF (GA) produces identical or near-identical values to the baseline GA, and TARF (NPO) similarly matches NPO. In several rows, TARF does not show any improvement over the vanilla baseline. The paper attributes this to "limited space" and defers to the appendix but provides no explanation for why the method's gains disappear in LLMs relative to classification. This undermines the claim of broad applicability.

### Minor

- **Sensitivity to hyperparameters t₀ and t₁ not characterized in main text.** The annealing parameters controlling when phases begin/end are described in Appendix E, but their sensitivity is only shown for k in Figure 7. Given that the three-phase timing is critical to the framework's operation, some characterization of t₀/t₁ sensitivity in the main body would strengthen confidence in the method's robustness.

- **Aggregate Gap metric may obscure task-critical failures.** The "Gap" averages over UA, RA, TA, and MIA uniformly. In safety-critical applications, a near-zero UA gap but large RA degradation could be an acceptable trade-off, whereas the same overall Gap could mask a failing UA (poor forgetting). A brief discussion of this limitation or a weighted variant would be informative.

### Trivial

- The notation (ℒ_D, ℒ_M, ℒ_T, ≺ relation) is dense initially but clarified well by Figure 1 and Table 1.

---

## Nice-to-Haves

- Move the weakly-supervised scenario results from the appendix to the main paper, as they directly address the strongest practical concern about the oracle assumption.
- For the LLM application, provide at least a brief analysis of *why* TARF does not show improvement over vanilla GA/NPO—whether it is due to the nature of transformer representations, the TOFU task structure, or the way mismatch scenarios are constructed for LLMs.
- A unified failure analysis: under what representation conditions does TARF's target identification degrade? The paper briefly discusses weakly clustered concepts in the conclusion but a quantitative characterization would be useful.

---

## Novel Insights

The most genuinely novel insight beyond the paper's own stated contributions is the representation gravity theorem and its implications for the *design space* of unlearning algorithms more broadly. Specifically, Theorem 3.2 implies that any gradient-based unlearning method's collateral effect on non-target data is fundamentally bounded by representation proximity rather than label proximity. This means that architectural choices and pre-training objectives—which shape the representation geometry—indirectly govern unlearning efficacy in ways not previously formalized. The finding that a coarser training taxonomy (superclass labels) entangles subclass features and makes selective forgetting harder is a direct practical corollary: the label granularity used during training is a hidden variable that determines the difficulty of future unlearning requests. This suggests that anticipating downstream unlearning needs at pre-training time (e.g., by encouraging within-superclass discriminability) could be a fruitful research direction.

---

## Suggestions

- Directly report weakly-supervised target identification results (from appendix) in the main paper, with a brief experiment quantifying performance as a function of how much oracle knowledge about the number of target classes is provided.
- Provide an error analysis for the LLM setting: compare representation geometry (e.g., nearest-neighbor distances in the forgetting/false-retaining split) between classification and LLM settings to explain the reduced gains.
- Consider a brief experiment on whether TARF can be applied to concept unlearning without any label structure (e.g., using clip embeddings to define concept membership), which would directly address the oracle assumption concern.

---

## Score and Decision

The paper makes a clear and original contribution: a formalized taxonomy of mismatch scenarios in class-wise unlearning, a theoretically grounded framework (TARF) that addresses them, and empirical results showing large improvements over baselines in the newly introduced settings. The core weakness—an oracle assumption in the target mismatch setting—is partially mitigated by the weakly-supervised experiments in the appendix, and the LLM results, while inconclusive, do not undermine the primary classification contributions. The work fills a genuine and practically motivated gap in the unlearning literature and should be of broad interest to the community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>