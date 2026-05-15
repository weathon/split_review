Now I have all the information needed. Let me produce the consolidated review.

---

## Summary

The paper proposes using large language models (LLMs) to extrapolate *truly novel* domains (beyond interpolation of existing source domains) for out-of-distribution generalization. It queries LLMs for class-specific novel domain descriptions, bridges the text-to-pixel gap via text-to-image models (Stable Diffusion), and uses the generated synthetic images to augment training or even train entirely from scratch (data-free DG). Experiments across PACS, VLCS, OfficeHome, and DomainNet show consistent improvements over ERM/ERM+EMA baselines, and an ablation (class-template, class-prompt) isolates the value of LLM-provided domain knowledge.

## Strengths

- **Novel use of LLMs for domain extrapolation.** The paper is the first to systematically leverage LLMs as a source of *truly novel* domain descriptions for OOD generalization, going beyond prior interpolation-based augmentation. The visualization (Figure 5) confirms that generated domains (e.g., "cityscapes") differ substantially from real PACS domains (art painting, cartoon), supporting extrapolation rather than interpolation.

- **Controlled ablation isolates the value of LLM domain knowledge (Table 3).** The comparison against class-template (text-to-image without LLM domains) and class-prompt (LLM prompts without explicit domain extrapolation) directly tests whether LLM-driven domain selection matters. The full method outperforms both (90.3% vs 88.0% on PACS), and the larger-batchsize control rules out a trivial confound. The scaling experiment (Figure 3) further shows that LLM-generated domains scale without saturation, unlike template/prompt baselines — this is the paper's strongest evidence.

- **Consistent empirical gains across multiple settings.** In leave-one-out evaluation, the method improves over ERM+EMA by +2.4% on average (Table 1), with gains as high as +5.2% on OfficeHome. In single-domain generalization (Table 2), improvements exceed +10% across all datasets (e.g., +17.1% on VLCS), demonstrating practical value when source domains are scarce.

- **Robustness across LLM families (Table 5).** Performance is stable across GPT-4, Llama-13B/70B, and Mixtral-8x7B (e.g., 90.3% vs 88.7% on PACS), confirming the paradigm is not tied to a specific model.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical framing (Section 2) is decorative, not operational.** Theorem 1 depends on \(D(\mu, \mu') \le \epsilon\), but this quantity is never computed, bounded, or even qualitatively argued to be small for the LLM approximation. The Rademacher complexity terms are inherited from standard DG bounds without adaptation. The bound neither guides design choices (e.g., how many domains to query, which LLM to use) nor is validated experimentally. The paper's empirical contribution stands independently; the theory section over-promises rigor and should either be substantially tightened (showing how the LLM query procedure controls \(\epsilon\)) or repositioned as high-level motivation.

- **The "data-free" results are uneven and the associated claim is imprecise.** The paper states (line 260) that data-free results have "only less than 1% gap between its multi-domain counterparts." This holds for VLCS (79.9% vs 78.8%) and PACS (86.9% vs 87.8%), but on OfficeHome the gap is 3.1% (67.4% vs 70.5%), and on DomainNet it is a substantial 15.7% (30.3% vs 46.0%). The data-free setting is a valuable contribution, but the headline claim overstates its generality. Furthermore, the paper does not analyze whether LLM-generated domains for VLCS (a small dataset with common real-world scenes like Caltech101, LabelMe) might be semantically close to the test domains, raising a potential distributional leakage concern that the authors should address.

### Minor

- **The main results (Tables 1 and 2) compare against baselines that receive no additional training data.** While the ablation (Table 3, Figure 3) partially controls for this, the headline tables do not. Readers may reasonably ask whether the gains come from "more data" rather than "better (LLM-informed) data." Moving a controlled comparison (e.g., ERM + class-template with matched image budget) into the main table would strengthen the paper's central claim.

- **No experimental comparison against other methods that use external generative models for DG.** The related work cites Wu et al. 2023 and Vidit et al. 2023, but the paper does not directly compare against them under a shared data budget. The class-template and class-prompt baselines partially address this gap, but comparing against existing published methods (e.g., LADS-style generative augmentation) would better contextualize the contribution.

- **The ablation (Table 3) does not explicitly state whether class-template and class-prompt use the same number of synthetic images as the full method.** The scaling experiment (Figure 3) does control for this, but varying practice between tables creates unnecessary ambiguity.

### Trivial
None.

## Nice-to-Haves

- A cost analysis (number of LLM queries, image generation time per sample, API costs) would help ground the claim about "democratizing machine learning."
- Measuring distributional similarity (e.g., FID, domain classifier accuracy) between generated synthetic data and test domains in the data-free setting.
- Statistical significance testing with more than 3 runs for the core comparisons, given the multiple stochastic components.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Unfair comparison — no control for data quantity"** (harsh critic Point 1, as a fatal flaw): The critic argued the paper cannot isolate LLM value from data quantity. However, Table 3 (class-template, class-prompt baselines) and Figure 3 (scaling with matched image budgets) *do* provide this control. The critic's demand for "a proper baseline [that] would augment ERM with the same number of synthetic images generated by a non-LLM method" is exactly what class-template provides. The controlled experiment exists and shows the full method outperforms it (90.3% vs 88.0% on PACS). This criticism is overstated; the paper already addresses it in its ablation.

- **"Typo: missing closing parenthesis"** (harsh critic Section 2 note): This is a PDF-extraction artifact, not a submission error. Removed per hard rules.

- **"Theory section should be removed"** (harsh critic Point 2, as a fatal criticism): The theory does motivate the approach (increasing n, approximating μ via μ'), even if it is not tightly coupled to the method. Calling it "irrelevant" is a strawman — it provides framing for why domain extrapolation matters. The criticism is reduced to a Major weakness above (decorative, not operational), not a reason to remove the section entirely.

- **"Only compares against augmentation methods that use original data"** (harsh critic Point 4): The paper does compare against class-template and class-prompt (both synthetic data baselines) in Table 3 and Figure 3. The absence of specific published methods (e.g., DreamDA, LADS) is a valid gap, but the critic's framing that the paper "lacks comparisons with other methods that also use external synthetic data" ignores the ablations the paper already provides.

- **Strength Finder strength #3 ("Theoretical grounding with generalization bound")**: Conflicts with the verified weakness that the theory is operational. Dropped.

## Novel Insights

The reviewers' disagreement highlights a tension in how to evaluate papers at the intersection of LLMs and vision: the harsh critic evaluates the paper against a strict experimental-design standard (data-controlled comparisons, tight theory-to-method coupling), while the paper itself is a systems-style contribution that introduces a new paradigm (LLM→domain→synthetic data→training). The most informative result is the scaling experiment (Figure 3), which shows that LLM-generated domains avoid the saturation that template-based synthetic data suffers from — this is a genuinely non-obvious finding that deserves emphasis. The data-free setting, while not uniformly successful, is a thought-provoking new benchmark that future work can build on.

## Suggestions

1. Restructure the paper to foreground the controlled ablation (Table 3, Figure 3) — this is the strongest evidence for the core claim. Make Table 3 the primary result table and relegate the uncontrolled comparisons to supplementary.
2. Either substantially strengthen the theory (connect D(μ, μ') to the LLM query design; provide even a heuristic estimate) or reposition it clearly as intuitive motivation rather than a formal guarantee.
3. Add a column to Table 3 explicitly stating the number of synthetic images used per method to remove ambiguity.
4. For the data-free setting, add an analysis of domain similarity (e.g., CLIP-space distance) between generated domains and test domains to address leakage concerns.
5. Discuss the uneven data-free results (especially DomainNet's 15.7% gap) honestly — this makes the contribution more credible, not less.

## Score and Decision

The paper introduces a genuinely novel and timely paradigm for OOD generalization. The core empirical contribution is supported by the controlled ablation (Table 3) and scaling experiment (Figure 3), which isolate the value of LLM-driven domain extrapolation. The weaknesses — decorative theory, imprecise data-free claims, and missing comparisons — are addressable and do not invalidate the central contribution. The paper represents a solid contribution that advances the state of the art.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>