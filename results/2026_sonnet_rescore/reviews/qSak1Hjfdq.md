Now I have enough information to write the consolidated final review. Let me analyze the key claims from the reviewers against the paper content.

---

## Summary

This paper formalizes the All-day Multi-scenes Lifelong Vision-and-Language Navigation (AML-VLN) problem, wherein an agent must sequentially learn navigation across multiple scenes (e.g., sim and real-world) and illumination environments (normal, low-light, overexposure, scattering) without catastrophic forgetting. The authors propose Tucker Adaptation (TuKA), a parameter-efficient fine-tuning method that lifts adaptation weights into a 4th-order tensor and uses Tucker decomposition to separate shared core navigation skills from scene-specific and environment-specific experts. A Decoupled Knowledge Incremental Learning (DKIL) strategy applies EWC to shared subspaces and orthogonality/consistency constraints to task-specific experts. The resulting AllDayWalker agent achieves 65% average SR over 24 tasks, substantially outperforming LoRA-based baselines.

---

## Strengths

- **Compelling problem formulation backed by concrete evidence of forgetting.** Figure 2 documents that sequential fine-tuning causes forgetting rates rising to 79% across 10 tasks, directly motivating the AML-VLN formalization. The setting (task-id agnostic at test time, 24 sequentially-encountered scene × environment pairs) is a realistic and underexplored challenge.

- **Novel 4th-order Tucker adaptation architecture with principled dimensional alignment.** TuKA lifts adaptation to $\mathcal{X}^l \in \mathbb{R}^{a_l \times b_l \times M \times N}$ and uses Tucker decomposition (Eq. 2–3) to decouple a shared core tensor $\mathcal{G}$, shared encoder/decoder $U^1, U^2$, and scene/environment expert vectors $U^3[s,:], U^4[e,:]$. This is a genuinely novel approach to parameter-efficient fine-tuning in LLM-based agents, going beyond LoRA and MoE-LoRA's two-hierarchical matrix form.

- **Effective continual learning strategy with measurable forgetting reduction.** Table 2 confirms that AllDayWalker achieves an average F-SR of 11%, substantially below the next-best baseline — a concrete and reliable result since O-LoRA (23%) and SD-LoRA (18%) have complete F-SR columns with full 24-task data.

- **Ablations validate the benefit of 4th-order over 3rd-order tensor decomposition.** Figure 8 shows consistent SR improvement of the 4th-order model across all 20 simulation tasks, and Table 3 confirms that sharing $\mathcal{G}$ and $U^2$ significantly improves SR (from 55% to 65%).

- **Generalization to unseen scenarios.** Table 5 shows AllDayWalker achieves 55% avg SR on six fully unseen scene/environment pairs versus 39–40% for the best competitors, demonstrating the learned representation transfers beyond the training task distribution.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing aggregate averages for key baselines prevent verification of the headline claim.** In Table 1, the "Avg." column is blank for Seq-FT, Lwf-LoRA, EWC-LoRA, Sparse MoLE, O-LoRA, SD-LoRA, and FeedTTA. Critically, SD-LoRA is also missing per-task data for T22–T24, making it the one competitor whose overall average genuinely cannot be estimated. SD-LoRA shows strong numbers on several tasks (T8: 74 vs. AllDayWalker's 38; T12: 75 vs. 67), and its partial 21-task mean is approximately 57%, significantly closer to AllDayWalker's 65% than it appears from the paper's narrative. Without a complete average, the magnitude of AllDayWalker's win over its nearest competitor cannot be confirmed from the table. This is an evidential gap in the central quantitative claim and must be addressed.

- **The Tucker-structure benefit is not isolated from the DKIL regularization benefit.** The paper's core mechanistic claim is that 4th-order Tucker structure is superior for multi-hierarchical knowledge because it explicitly decouples scene and environment. However, the ablations in Table 3 only vary which TuKA components are shared; they do not compare TuKA against an obvious structural alternative: two independent LoRA adapters (one scene-specific, one environment-specific) with the same EWC and orthogonality losses applied to each. This design would also separate scene and environment subspaces using the same regularizers. Without this control, it is unclear whether the gains over SD-LoRA and O-LoRA in Table 1 stem from the Tucker tensor structure itself or primarily from the DKIL losses.

### Minor

- **Formal problem definition is in tension with the benchmark design.** The AML-VLN non-overlap condition (§2) is written as $\{S_t, E_t\} \cap (\bigcup_{j=1}^{t-1} \{S_j, E_j\}) = \emptyset$, which as a set union of scenes and environments would prohibit any scene from being reused across tasks. Yet Figure 6 clearly shows all five scenes each appearing under four different environments (e.g., sim-world-v1 appears in tasks with Normal, Low-light, Overexposure, Scattering), and Section 3.3 explicitly handles this: "we also initialize the current scene expert $U^3[s,:]$... if previous scenario has learned the same experts." The formal definition and learning algorithm are semantically inconsistent and need reconciliation — the condition should state that the (scene, environment) *pair* must be new, not every constituent.

- **Figure 7 labels five retrieval-strategy variants (Ours, BaseModel, Recall, Task2Vec, CLIP) without explanation.** Section 5.2 states "results on SPL, F-SPL, OSR, and F-OSR are presented in Figure 7," but the legend names (BaseModel, Recall, Task2Vec, CLIP) do not match any of the baselines in Table 1. These appear to be expert-search ablations (different retrieval strategies), not the continual learning baselines. Without a caption explanation, the figure is confusing and conflicts with the surrounding discussion.

- **The F-SR = 0 for the final task (T24) across all methods is mechanical and unacknowledged.** Because $M\text{-}SR_{24}$ denotes joint training on all tasks including $T_{24}$, and sequential training also ends on $T_{24}$ (the model's weights reflect that task), forgetting on the final task is structurally near-zero. Table 2 confirms this: every method scores 0 on T24. The paper does not acknowledge this artifact, which slightly inflates the apparent non-forgetting performance.

### Trivial

- **Notation inconsistency in §3.4**: The environment expert matching formula is written as $e = \arg\max \text{Sim}(Fe_q, \{Fe_{e1}, \dots, Fe_{eM}\})$, using $M$ (scene count) for the environment feature set cardinality; it should be $N$ (environment count, defined in §2).

- **Duplicate row in Table 3**: Both the 3rd and 6th rows show ✓✓✓ for all three shared components (Sd-$\mathcal{G}$, Sd-$U^1$, Sd-$U^2$) with SR=65, F-SR=11, SPL=58, F-SPL=18 but OSR=69 vs. 68, suggesting a copy-paste error. One row appears redundant.

---

## Nice-to-Haves

- Reporting retrieval accuracy (how often the correct scene/environment expert is selected) broken down by condition type would strengthen the claim that the inference-time expert search is reliable. Figure 7 appears to compare retrieval strategies, but explicit retrieval accuracy rates are absent. Showing that navigation failure rather than mis-retrieval drives errors would substantially validate the system's robustness.

- The "all-day" framing in the title implies scattering and overexposure are validated in deployment conditions, but the two real-world scenes only cover normal and low-light environments. Noting this limitation and discussing the sim-to-real gap for scattering/overexposure conditions would make the practical claims more honest.

- Extending Table 4's 30-task comparison with forgetting metrics (not just SR) would more fully demonstrate stability under scale-up.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **[Removed — addressed by Figure 7]** The harsh critic stated that inference-time retrieval accuracy is "never characterized." In fact, Figure 7 appears to compare multiple expert-search variants (Ours, BaseModel, Recall, Task2Vec, CLIP) on SPL, F-SPL, OSR, and F-OSR, constituting a partial retrieval strategy ablation. The absolute retrieval accuracy is still unreported (retained as a Nice-to-Have), but the claim that retrieval is entirely uncharacterized is too strong.

- **[Removed — within scope]** The harsh critic's "Strengthening" section requests an independent scene-LoRA + environment-LoRA ablation. This is retained as a Major weakness (the Tucker-vs.-independent-adapter comparison). The specific framing of it as a "strengthening" suggestion is subsumed there.

- **[Removed — Strength Finder's specific figure of "SD-LoRA: 52%" average]** Table 1 does not show SD-LoRA's average (it is blank), and T22–T24 are missing. The figure "52%" cited in the Strength Finder's summary cannot be verified from the paper and may be confused with O-LoRA (whose computable 24-task average is ~51%). This specific numerical claim is dropped from the Strengths section; the directional claim that AllDayWalker leads SD-LoRA is retained based on per-task data.

- **[Removed — missing appendix rule]** Any criticisms about missing proof details, hyperparameter tables, or extended ablation results that are explicitly deferred to appendix sections (§C, §E, §G, §H, §I, §J, §K) are excluded per policy.

---

## Novel Insights

The most genuinely novel conceptual move in this paper is the lifting of PEFT from a 2D matrix space (LoRA/MoE-LoRA) to a 4th-order Tucker tensor space as the natural container for multi-hierarchical navigation knowledge, with the key insight that the tensor's third and fourth modes can be assigned to scene- and environment-specific factors respectively. The dimensional alignment via Tucker decomposition — reducing to a 2D matrix for compatibility with LLM weight updates (Eq. 3) — is an elegant resolution to a real engineering challenge. The DKIL strategy's asymmetric treatment (EWC for shared subspaces, consistency+orthogonality for task-specific experts) reflects a nuanced understanding of what must be stable (shared skills) versus separable (scene/environment identity). Together these ideas suggest a broader design principle: the order of the fine-tuning tensor should match the number of meaningful knowledge hierarchies in the target domain, a principle worth studying in other multi-attribute continual learning settings.

---

## Suggestions

1. **Complete Table 1** by filling in all missing averages and the missing T22–T24 cells for SD-LoRA. If SD-LoRA was unstable or crashed on those tasks, state so explicitly with a footnote.
2. **Add the independent-adapter ablation**: train two separate LoRA modules (one scene-specific, one environment-specific) with the same EWC and orthogonality losses as DKIL, and compare to TuKA in Table 3. This would directly validate that the Tucker tensor structure, rather than the regularization losses alone, drives the gains.
3. **Fix the formal non-overlap condition** in §2 to explicitly state that the (scene, environment) *combination* must be new, not that either scene or environment must be new. Add a brief note clarifying the inheritance mechanism in §3.3 is designed for the common case where a scene or environment type recurs in a new pairing.
4. **Add a caption or inline explanation for Figure 7** clarifying that the five comparison curves are expert-search strategy variants (retrieval ablations), not the continual learning baselines from Table 1. Report retrieval matching accuracy for each strategy if space allows.
5. **Acknowledge the mechanical T24 zero in F-SR** and restate the forgetting claim in terms of tasks T1–T23, which is where actual forgetting is measured.

---

## Score and Decision

**Originality:** The Tucker tensor formulation for PEFT is a concrete and non-trivial novel contribution; MoE-LoRA extensions are incremental, but the 4th-order tensor idea with dimensional alignment is original. *Score: 4/5*

**Importance of Research Question:** Lifelong VLN across diverse illumination conditions and scenes is a genuine gap and practically relevant for real robot deployment. *Score: 4/5*

**Claims Well-Supported:** The main SR/F-SR claims are broadly supported by Tables 1–4, but the missing SD-LoRA average and the absence of the structural ablation leave the headline claims partially unverified. *Score: 3/5*

**Soundness of Experiments:** The benchmark design is methodologically transparent (24 tasks, clearly specified scenes/environments, 8 GPU setup), and ablations cover key design choices. The notation error, duplicate ablation row, and formal definition inconsistency introduce minor noise. *Score: 3/5*

**Clarity of Writing:** The method is generally well-explained, but Figure 7's ambiguous legend and the §2 formal definition inconsistency are genuine clarity failures for the reader. *Score: 3/5*

**Value to Community:** The benchmark (AllDay-Habitat), the TuKA method, and the DKIL strategy are all releasable artifacts with independent utility. *Score: 4/5*

The paper makes a substantive and well-motivated contribution with strong empirical results across most comparisons. The two Major weaknesses (missing averages and the missing structural ablation) are material but addressable without new experiments — completing Table 1 costs nothing, and the independent-adapter ablation is a straightforward addition. No weakness rises to the level of invalidating the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>