Now I will produce the final consolidated review.

## Summary

This paper introduces **successor heads**: attention heads that increment tokens in ordinal sequences (numbers, months, days, etc.). The authors define successor heads via an effective OV circuit that includes MLP₀, show they occur across models from 31M to 12B parameters (GPT-2, Pythia, Llama-2), and decompose the numeric representations they operate on into compositional index-domain structures and interpretable mod-10 features validated by three independent methods (SAEs, linear probing, individual neuron analysis). The paper also demonstrates vector arithmetic with these features and shows that successor heads are polysemantic in the wild, performing not just incrementation but also acronym formation and greater-than comparisons.

## Strengths

1. **Cross-scale and cross-architecture universality**: The paper demonstrates successor heads in models spanning 31M to 12B parameters across GPT-2, Pythia, and Llama-2 architectures (Figure 2). This is a rare demonstration of a recurring interpretable component at vastly different scales, directly supporting the weak universality claim.

2. **Compositional numeric subspace with out-of-distribution generalization**: The factoring experiment (Section 3.1, Table 1) shows that learned linear projections decompose MLP₀ representations into independent index and domain components, achieving perfect top-1 accuracy on held-out token pairs and generalizing to Roman numerals (which were never in the training data). This provides genuinely compelling evidence for abstract, transferable numeric representations.

3. **Mod-10 features validated by three convergent methods**: The paper identifies mod-10 features via sparse autoencoders (Section 3.2), linear probing (Section 3.3.1 — probe rows have average cosine similarity 0.70764 to SAE features), and analysis of individual MLP₀ neurons that fire in periodic patterns with period 10 (Section 3.3.2, Figure 5). The convergence of three independent methods on the same mod-10 structure is strong evidence that these are natural features, not artifacts of any single technique.

4. **Causal manipulation via vector arithmetic**: The paper successfully steers the successor head's effective output by adding/subtracting mod-10 features (Section 3.4, Figure 6), e.g., treating "fifth" like "seventh" via MLP₀("fifth") − k·f₅ + k·f₇. The success tables show systematic, predictable effects across multiple ordinal domains.

5. **Interpretably polysemantic attention head in the wild**: The paper identifies that the successor head also performs distinct interpretable behaviors — acronym formation and greater-than operations — on natural-language data (Section 4). The quantitative breakdown (Figures 7 and 8) with concrete examples (Tables 3 and 4) provides one of the clearest documentations to date of an LLM attention head with multiple interpretable functions.

## Weaknesses

### Fatal

None.

### Major

1. **Unvalidated circuit path via MLP₀**: The effective OV circuit is defined as W_U·W_OV·MLP₀(W_E), but the paper never justifies why MLP₀ specifically is the correct input to study. By Layer 12 in Pythia-1.4B, the residual stream is the sum of embeddings, all earlier attention heads, and all earlier MLPs. The paper offers no evidence (attention attribution, activation patching, or overlap analysis) that the head's actual input is dominated by MLP₀'s output for ordinal tokens. This means the factoring experiment, mod-10 features, and vector arithmetic all describe the structure of MLP₀ outputs — which are shown to affect the head's OV output — but may not fully describe how the head operates within the full model. The paper would be strengthened by showing that the features found on MLP₀ outputs are also present in the true residual stream input to the head.

2. **Successor head definition ignores attention**: The successor score is computed solely from the OV circuit and does not check whether the head actually attends to ordinal tokens in practice. While the "in the wild" section does examine attention (using top-5-attended tokens) for the primary head L12H0, the cross-model survey (Figure 2) and the initial definition rely purely on the OV circuit. A head with a perfect OV circuit for incrementation but that never attends to ordinal tokens is not a functionally relevant successor head. The paper should either incorporate attention into the successor head definition or provide evidence that high successor-score heads consistently attend to ordinal tokens.

3. **Vector arithmetic and mod-10 features not validated in the full model**: The steering experiments (Section 3.4) demonstrate that modifying MLP₀ outputs changes the head's effective OV output in predictable ways, but they do not show that these interventions change the model's actual next-token predictions. The claim of "steering the semantics of successor heads' numeric inputs with vector arithmetic" is appropriately scoped to the sub-circuit, but the paper's broader narrative about interpretable features would be substantially stronger if full-model steering were demonstrated (e.g., via residual stream interventions that change model outputs).

### Minor

1. **Universality evidence is unevenly deep**: The paper surveys successor scores across many models (a genuine strength), but the deeper mechanistic analysis (mod-10 features, factoring) is performed almost entirely on Pythia-1.4B. The paper notes that similar representations exist in other models (Appendix reference), but the main text's universality claim rests primarily on successor scores, which per Weakness #2 may not reflect functional behavior. Stronger cross-model evidence that the same mod-10 features exist would substantiate the universality claim.

2. **"In the wild" analysis establishes importance, not mechanism**: The mean ablation experiments show that the successor head is causally important for certain predictions, and the behavioral categories (successorship, acronym, greater-than) are descriptive labels. For the non-successorship categories, the paper does not analyze the mechanism by which the head accomplishes these tasks — it provides no evidence beyond the correlation between the head's importance and the task category. The claim that this is the "cleanest example of polysemantic behavior in an LLM" is somewhat overstated given that only one behavior (successorship) receives mechanistic analysis.

3. **Inconsistent performance of vector arithmetic**: The vector arithmetic works on about 53% of months and 89% of 20-29 numbers, with clear failure patterns (greater-than bias, failure on days/letters noted by the authors). While the authors candidly acknowledge these limitations, the partial success rate and systematic failure modes (the "+10 effect") suggest the mod-10 feature explanation is significantly incomplete, as the authors themselves note.

### Trivial

None.

## Nice-to-Haves

- **Activation patching to validate the MLP₀ circuit**: Using activation patching (e.g., on L12H0) to show that the head's output causally depends on MLP₀ would directly address the most substantial weakness. For instance: patching the MLP₀ output from a prompt with a different ordinal token and observing the model's prediction shift accordingly.
- **Attention verification for the cross-model survey**: For a representative subset of high successor-score heads in non-Pythia models, check whether they attend to ordinal tokens in relevant contexts.
- **Full-model steering**: Demonstrating that modifying mod-10 features in the actual residual stream (not just MLP₀ outputs) changes the model's generated text would strengthen the practical relevance of the feature-level analysis.
- **Systematic evaluation of the informal claims**: The "triangle → 3" and "week → 7" informal tests are intriguing but should either be systematically evaluated or dropped in favor of more rigorous evidence.

## Removed Points

- **Harsh Critic Issue 1 as "fatal"**: The paper does use a standard method (effective OV circuit, as in copy suppression) to identify heads, and the mean ablation experiments provide causal evidence that these heads matter for succession. The specific MLP₀ path is a modeling choice for studying the head's input space, not an unvalidated claim about the exclusive circuit. This is a real concern but not fatal — downgraded to Major.
- **Criticism that "the paper's central mechanistic interpretation is unsupported"**: Overstated. The paper provides convergent evidence from multiple methods (effective OV circuit, mean ablation, factoring, SAE, linear probing, neuron analysis, vector arithmetic). The interpretation is supported at multiple levels even if the exact circuit path is not proven.
- **Criticism that the paper "never provides evidence" for the circuit path**: The paper does provide causal evidence via mean ablation (a standard causal intervention) in the "in the wild" section. It also shows the mod-10 features are causally relevant for the head's OV output (Section 3.2, Figure 3).
- **Criticism that the "in the wild" analysis is purely correlational**: Incorrect. Mean ablation is a causal intervention — it measures the effect of removing the head's contribution on the model's predictions. This is standard practice in mechanistic interpretability.
- **"The paper's claim that this is the cleanest example of polysemantic behavior is not supported"**: The paper does support this claim with quantitative evidence (proportions of behaviors in winning/loss-reducing cases, Figure 7-8) and concrete examples (Tables 3-4). While the mechanism is only analyzed for succession, the behavioral evidence for multiple functions is clear.
- **"The factoring experiment operates entirely on MLP₀ outputs, so it inherits the concerns about relevance"**: The factoring experiment studies the structure of the head's input representation (MLP₀ outputs). Since these inputs demonstrably affect the head's output (verified by OV-circuit analysis), the factorization describes a real property of the computation.
- **"The Roman numeral informal testing is not rigorous and should be dropped"**: The Roman numeral experiment in Table 1 is actually a systematic evaluation (perfect accuracy on held-out classes), not informal. The informal testing mentioned is separate and clearly labeled as such.
- **Missing formatting/style criticisms removed per instructions**.

## Novel Insights

This paper's most novel contribution is demonstrating that a single attention head can implement an abstract, transferable operation (incrementation) that generalizes across token types (digits, number words, ordinals, months, days) using the same underlying mod-10 features. The combination of methods — screening many models via successor scores, then deeply analyzing one head via factoring, SAE, probing, and neuron analysis — provides a template for how to study recurring components in LLMs. The finding that a single head is polysemantic across successorship and acronyms is also noteworthy, as it provides a concrete case study of superposition in attention heads (not just MLP neurons) in a deployed-scale model.

## Suggestions

1. **Justify or replace MLP₀**: Either provide evidence (via direct logit attribution or activation patching) that the successor head's input is dominated by MLP₀'s contribution for ordinal tokens, or generalize the analysis to the full residual stream. This is the single most impactful improvement.

2. **Check attention for the cross-model survey**: For the best successor head in each model in Figure 2, verify that it attends to ordinal tokens on representative prompts. This would make the universality claim substantially stronger.

3. **Provide granular steering validation**: Even if full-model steering is infeasible, show that modifying mod-10 features in the residual stream (before the head, not just in MLP₀'s output space) changes the head's attention-weighted output in the expected direction.

4. **Discuss the MLP₀ choice explicitly**: Add a paragraph explaining why MLP₀ was chosen (e.g., prior work showing its importance, or empirical analysis showing the head's input correlates strongly with MLP₀ output for ordinal tokens), and acknowledge what information may be missed by not considering the full residual stream.

## Score and Decision

This paper makes a genuine contribution: it identifies a recurring, interpretable attention head class across a wide range of model scales and architectures, provides convergent evidence from multiple methods for the structure of the representations these heads operate on, and demonstrates that these heads are causally important on real data. The weaknesses — primarily the lack of causal validation for the specific MLP₀ circuit path and the uneven depth of the cross-model analysis — are real but do not undermine the core contributions. The paper is a solid empirical contribution to mechanistic interpretability that will be of interest to the community and provides a useful template for studying recurring components in LLMs.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>