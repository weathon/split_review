- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 5, 6
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

TREANT presents an automated red-teaming framework for text-to-image (T2I) models that uses a novel tree-based prompt representation (Prompt Parse Tree, or PPT) and two transformation strategies — semantic decomposition (spreading sensitive terms through a prompt) and sensitive element drowning (overwhelming image filters with benign content) — to bypass safety filters while preserving generation intent. The framework uses LLMs to orchestrate prompt construction, evaluation, and refinement, and reports high success rates against DALL·E 3 and multiple Stable Diffusion variants.

## Strengths

1. **Novel Prompt Parse Tree (PPT) representation.** The paper formally defines a tree-based encoding with Object, Attribute, and Relation node types (Section 3.2, Figure 2). This is a structural advance over flat perturbation methods (synonym replacement, token masking) because it enables systematic hierarchical transformations rather than local edits. The formalism is concrete and reproducible.

2. **Demonstrated synergy between the two strategies.** The ablation study (Table 1, comparing TREANT-SD, TREANT-SED, and full TREANT) confirms that combining semantic decomposition and sensitive element drowning substantially outperforms either in isolation. On the full NSFW-1k dataset, full TREANT achieves 85% overall success vs. 53% for decomposition alone and 47% for drowning alone. This provides direct evidence that the dual-strategy design is effective and justifies the framework's complexity.

3. **High query efficiency.** Figure 5 shows TREANT reaching ~88% success within 5 queries, while baselines (SneakyPrompt, TextFooler, BAE) plateau at 70–75% over the same query budget. This directly supports the paper's claim of reducing testing cost.

4. **Consistent outperformance across diverse prohibited scenarios.** On DALL·E 3 over 11 prohibited categories (Table 1), TREANT achieves the highest success rate in every category — e.g., 67% in "Sexual" vs. next best 27%; 94% in "Shocking" vs. 35%. This broad empirical coverage supports the generality claim.

5. **Fully automated pipeline with clear methodology.** The framework uses LLMs for PPT construction, refinement, and evaluation without requiring internal model access. The design is described step-by-step (Section 3.1–3.5), and the codebase is released.

## Weaknesses

### Fatal

None.

### Major

- **The headline 88.5% success rate is overgeneralized.** The abstract and conclusion state the method achieves "an overall success rate of 88.5% on leading T2I models, including DALL·E 3 and Stable Diffusion" and "on a range of platforms, including DALL·E 3 and three versions of Stable Diffusion." In fact, the 88.5% figure is from **DALL·E 3 on the NSFW-1k dataset** (Table 1). The cross-model results on NSFW-200 (Table 2) show a widely varying picture: DALL·E 3 (63.0%), SD XL (92.0%), SD v1.4 (28.0%), SD v2.1 (42.0%). The 88.5% number is not the average across models and datasets; the conclusion's phrasing is misleading. This overclaiming weakens the paper's credibility and needs correction.

- **The "first fully automated" claim is inconsistent with the paper's own baselines.** Line 16 states TREANT is "to our best knowledge, the first fully automated red teaming framework dedicated to assessing the robustness of T2I models against the generation of NSFW content in a black-box setting." Yet SneakyPrompt (Yang et al., 2023) — cited as a baseline and described as an automated method that "utilizes reinforcement learning to iteratively refine adversarial prompts" — is itself a fully automated black-box T2I red-teaming method. No distinction is drawn between TREANT and SneakyPrompt on automation grounds, making this claim internally contradictory. The authors should qualify it or explain what differentiates TREANT (e.g., dedicated to tree-based semantic transformation rather than RL-based token perturbation).

- **The 6-query limit constrains the comparison with baselines.** The paper imposes a uniform query limit of 6 for all methods (Section 4, line 78) with only a brief fairness rationale. Figure 5 does provide per-query success curves for 1–5 queries (where TREANT reaches ~88% and baselines reach 70–75%), which partially addresses this concern. However, without knowing how baselines would perform with a more generous budget (e.g., 20–100 queries), it is unclear whether the gap reflects TREANT's true advantage or merely that some methods are throttled below their effective operating range. The paper should either (a) report success-rate vs. number-of-queries curves over a wider range for all methods, or (b) justify the 6-query choice empirically.

### Minor

- **No ablation isolating the tree structure itself.** The paper does not compare the tree-based PPT to a flat (non-hierarchical) decomposition that uses the same number of sub-elements. Without this, it is unclear whether the benefit shown in Figure 6 (increasing success with more PPT nodes) comes from the hierarchical tree structure or simply from having more sub-elements in the prompt. A flat-list baseline would cleanly isolate this.

- **Limited discussion of failure modes.** The paper notes (Section 4.1) that performance is lower on "Self-harm" and "Violence" categories, and lower on SD v1.4/v2.1, but provides no qualitative analysis of *why* these cases fail. Understanding failure modes is important for a scientific contribution in red-teaming.

- **No reporting of LLM API cost.** TREANT relies on LLM calls for PPT construction, refinement, and evaluation. The number of LLM queries required per adversarial prompt is not reported, which affects the practical scalability claim.

- **Inter-rater reliability for manual checks is not reported.** The evaluation uses GPT-4V + manual checks (Section 4, line 84), but the fraction manually verified and the agreement rate are not stated. This makes it hard to assess the rigor of the NSFW classification.

- **The ablation of PPT complexity (Figure 6) stops at 12 nodes** with no explanation of why this ceiling was chosen or what happens beyond it.

### Trivial

None.

## Nice-to-Haves

- A per-query success analysis over a wider range (e.g., 1–50 queries) for all methods, allowing readers to assess the trade-off directly.
- A flat-list (non-hierarchical) ablation to isolate the benefit of the tree structure itself.
- A proper limitations paragraph in Section 5 that discusses TREANT's reliance on LLM quality, potential for dual use, and generalizability to non-English prompts.
- Testing on an independently sourced prompt set (not generated via ChatGPT from the same Reddit post) to rule out dataset-specific artifacts.

## Removed Points

*Points moved here from the input reviews that do not survive the filtering criteria.*

- **"The motivation observations are stated as facts without citations"** (Harsh Critic, Section-by-Section Notes). The two observations in Section 3.1 are presented as design heuristics that inspired the method, not as cited empirical findings. This is standard for practical system papers. **Removed** — not a genuine weakness.
- **"Algorithm 1 is cut off, §3.4 is missing."** Noted as a parser artifact by the critic. **Removed** — does not reflect on the paper's content.
- **"The fraction manually verified is not stated."** Partially subsumed into the minor point about inter-rater reliability, but the critic's framing as a missing number is a disclosure suggestion, not a weakness of the method. **Moved** to Nice-to-Haves.
- **"The evaluation metric is at risk of being biased because TREANT's own refinement uses an LLM."** GPT-4V evaluates the *output image*, not the prompt, and manual checks are performed. The concern conflates prompt generation with output evaluation. **Removed** — not a valid concern as stated.
- **"TREANT could be used to generate actual harmful content."** This is a standard red-teaming consideration acknowledged implicitly by the paper's existence; does not constitute a weakness of the method. **Removed**.
- **Generic strengths from Strength Finder.** Strengths about "addressing an important problem" or "targeting an interesting question" are dropped as generic. Only concrete, evidence-backed strengths are retained above.

## Novel Insights

*None beyond the paper's own contributions.* The core synthesis from the reviews is that the paper has a genuine and reasonably well-supported contribution (PPT + dual strategies, with an ablation study confirming synergy), but undermines itself through overclaiming (88.5% overgeneralized, "first fully automated" contradicted by its own baseline) and comparison limitations (query budget cap). These are presentation and methodology issues that can be fixed without changing the underlying approach, but they do reduce confidence in the headline claims as currently stated.

## Suggestions

1. **Correct the overclaiming.** Report the per-model, per-dataset success rates everywhere you state the 88.5% figure. If you want an overall number, compute a properly weighted average across all models and datasets, or explicitly qualify that 88.5% is on DALL·E 3 with NSFW-1k.

2. **Fix the "first fully automated" claim.** Either remove it or explicitly qualify how TREANT differs from SneakyPrompt and other automated black-box methods (e.g., "first fully automated method to use tree-based semantic transformations").

3. **Address the tree-structure ablation gap.** Add a "flat list" baseline where the same number of sub-elements is used but without hierarchical structure. This cleanly tests whether the tree matters beyond decomposition depth.

4. **Report LLM call cost per successful adversarial prompt** to substantiate the scalability claim.

5. **Add a qualitative failure analysis** for the categories and models where TREANT underperforms.
