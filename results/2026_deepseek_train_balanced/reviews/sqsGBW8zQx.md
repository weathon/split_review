# Final Consolidated Review

## Summary
This paper scales mechanistic circuit extraction from toy tasks (entity tracking, IOI) to real-world extractive QA. Using causal mediation analysis on a probe dataset, it extracts two circuits — one for context-faithfulness and one for memory-faithfulness. The key finding is that certain attention heads in the context-faithfulness circuit naturally perform data attribution, which the authors convert into AttnAttrib — a single-forward-pass attribution method. The paper also demonstrates model steering by incorporating these attributions into prompts, improving extractive QA accuracy by up to 9%.

## Strengths
- **First work to extract mechanistic circuits for extractive QA**, moving beyond the toy tasks (entity tracking, IOI, greater-than) that dominated prior circuit work. The probe dataset is explicitly designed without fixed templates (Sec. 3.1), a genuine departure from prior templated datasets.
- **Identifies that a specific attention head from the context-faithfulness circuit performs data attribution by default**, and converts this into AttnAttrib — an attribution method needing just one forward pass with no auxiliary model. AttnAttrib achieves ~20% F1 improvement over several reasonable baselines on single-hop HotPotQA (line 118).
- **Extensive cross-model and cross-dataset validation**: circuits extracted and validated across Phi-3B, Vicuna-7B, Llama-3-8B, and Llama-3-70B, with the context-faithfulness circuit ablated on NQ-Swap, Natural-Questions, and HotPotQA (Fig. 4, line 85). This far exceeds the single-model, single-probe-set validation typical of prior circuit papers.
- **Demonstrates sharply distinct circuitry for context-based vs. memory-based answering** with quantitative separation: context faithfulness requires ~10 heads to reach metric score >0.95, while memory faithfulness requires >30 heads, with minimal overlap (Sec. 3.3.1).
- **Delivers a concrete model-steering application**: adding AttnAttrib's attributions to the prompt improves extractive QA accuracy by up to 9% on NQ-Swap and Natural-Questions (Fig. 7), outperforming both baseline prompting and Context-aware Contrastive Decoding.

## Weaknesses

### Fatal
None.

### Major
- **Probe dataset construction is critically underspecified in the main text.** The probe dataset of 200 questions (D_copy, D_memory) is the empirical foundation for all circuit extraction, yet the main text (Sec. 3.1, lines 39–43) says almost nothing about how these examples are constructed: What source documents are used? How are "context-faithfulness" vs. "memory-faithfulness" induced? What corruption procedure is applied? How are parametric-memory questions constructed such that the model would answer from memory? The paper merely states that templating doesn't work and that there are 200 questions. While the appendix (stripped by the parser) likely contains these details, the main text should provide enough to evaluate the methodology. As written, a reader cannot assess whether the probe dataset cleanly isolates the two mechanisms.

- **No measures of variance, stability, or significance anywhere.** The paper reports no error bars, confidence intervals, or significance tests. This is concerning because: (a) the probe dataset has only 200 examples; (b) the greedy circuit selection procedure uses a threshold δ whose value is never stated (line 52); (c) the attribution head is selected based on entropy, which could vary across runs. Without any stability analysis, it is unclear whether the findings are robust to probe dataset construction, random seeds, or threshold choices.

### Minor
- **The "free attribution" framing overstates the practical cost.** The paper repeatedly claims attribution is obtained "for free" and "in just one forward pass" (lines 17, 106, 118). While inference-time attribution is indeed a single forward pass, identifying the right attention head requires the full circuit extraction pipeline: building the probe dataset, running causal mediation analysis across potentially hundreds of model components, and selecting the head with lowest entropy. This upfront cost is non-trivial, especially for larger models like Llama-3-70B. The framing should be qualified.

- **The "state-of-the-art" claim outruns the baseline set.** The paper claims "state-of-the-art data-attribution results" (line 17, abstract) while comparing against four baselines (Self-Attribution, Iterative Prompting, Sentence Similarity, Gradient). These are reasonable baselines for extractive QA attribution, but they are not comprehensive enough to warrant a SOTA claim. The paper would be stronger claiming "strong results against several reasonable baselines" rather than SOTA.

- **The model steering experiment has a confound.** Adding attribution text to the prompt (Sec. 5) improves accuracy by up to 9%, but this improvement could stem from simply providing more context information rather than the specific circuit-derived attribution signal. The paper lacks a control condition where a non-informative sentence from the context is added to the prompt, which would help isolate whether the benefit is specifically from the attribution mechanism.

- **The circuit validation against a "random circuit" baseline is weak.** Ablating the extracted circuit hurts more than ablating random components (line 63, Fig. 4) is a low bar. A stronger validation would compare against ablating the *least important* components (those with lowest patching scores) or a circuit extracted for a different task at the same size.

- **The threshold δ in the greedy circuit selection is never specified.** The algorithm (line 52) uses δ to determine how many components to include, but its value is not reported anywhere in the main text. This parameter directly affects circuit size and all downstream results.

### Trivial
- Several figures (e.g., Fig. 2 at line 41, Fig. 3 at line 47) appear to contain critical visual information (entropy distributions, circuit diagrams) but render as empty references in the text version. While a parser artifact, this leaves gaps in the main text narrative.

## Nice-to-Haves
- A control condition for the model steering experiment (adding a random sentence from context to the prompt) would strengthen the causal interpretation of the improvement.
- Reporting the δ threshold value and showing sensitivity of results to different δ choices would improve reproducibility.
- Adding variance estimates (e.g., bootstrap confidence intervals over the probe set) would increase confidence.

## Removed Points
*These points were flagged by reviewers but removed or demoted after verification against the paper.*

- **Criticism about insufficient comparison to Integrated Gradients, attention rollout, etc.** — Demoted from Major to Minor (folded into the SOTA claim point). The four baselines used are reasonable for the extractive QA attribution task; the issue is primarily the SOTA claim being too strong, not the baseline set being invalid.
- **Criticism that multihop results are presented too optimistically** — Removed. The paper reports F1 of 0.14 (binary) and 0.48 (with supporting tokens) candidly, and the claim is qualified ("provided the model includes supporting context"). This is appropriate scientific communication.
- **Various section-by-section notes (algorithm details, missing parameter values)** — Merged into the δ threshold point; no separate issues remain.
- **Strength Finder: generic strengths** (e.g., "addressed an important problem") — Removed as superficial/sycophantic. Only concrete, evidence-backed strengths are retained.

## Novel Insights
The most noteworthy finding not fully exploited by the paper is the sharp asymmetry between circuit size for context vs. memory faithfulness: context-faithfulness requires remarkably few components (~10 attention heads), suggesting that retrieval-augmented models route information through a narrow, specialized pathway, while memory-based answering recruits >30 heads plus significant MLP involvement. This asymmetry has implications for model debugging and reliability that the paper only touches on briefly. It would be interesting to explore whether the narrow context circuit makes these models more mechanistically scrutable than their parametric-reasoning counterparts, and whether this pattern generalizes to other retrieval-augmented settings.

## Suggestions
1. **Describe the probe dataset construction in 2–3 paragraphs in the main text** — source documents, corruption procedure, and how context/memory faithfulness is induced.
2. **Replace "state-of-the-art" with a more measured claim** (e.g., "strong results against several reasonable baselines") unless additional comparisons are included.
3. **Add a control condition to the model steering experiment** where a random sentence from the context is appended to the prompt.
4. **Report the δ threshold value** and include a brief sensitivity analysis showing how circuit size/composition changes with δ.
5. **Add variance estimates** (e.g., bootstrap confidence intervals) for the main results.
6. **Qualify the "free" framing** to acknowledge the upfront cost of circuit extraction.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>