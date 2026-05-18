## Summary

This paper uses sparse autoencoders (SAEs) to study the mechanism of in-context learning (ICL) in Gemma-1 2B. Two main contributions: (1) the Task Vector Cleaning (TVC) algorithm, which decomposes task vectors into a sparse sum (~4 features) of SAE latents while preserving steering performance, revealing "task-execution features;" and (2) an adaptation of Sparse Feature Circuits (SFC) to larger models and ICL, which discovers "task-detection features" that activate on completed-task tokens and are causally linked to execution features through attention.

## Strengths

1. **TVC algorithm is a genuine methodological contribution with clear empirical support.** The method consistently reduces active SAE features to <4 on average (versus >10 for naive SAE reconstruction) while matching or exceeding original task-vector steering performance up to layer 14 (Figure 3). The ablation sweeps across multiple model sizes (Gemma 2 2B, 9B) and SAE configurations demonstrate robustness. This makes it a practical tool for sparse decomposition of task vectors.

2. **Discovery of task-detection features as a novel circuit component not reported in prior ICL work.** The paper identifies features that activate specifically on output tokens of completed task examples (Table 2), have distinct token-type activation profiles from execution features (Table 1 vs Table 2), and show task-specific steering effects (Figure 7). Prior ICL circuit work (Todd et al. 2024, Hendel et al. 2023) identified task vectors but did not decompose them into interpretable SAE features with distinct functional roles. This represents genuinely new mechanistic understanding.

3. **Causal evidence linking detection and execution features through attention.** Figure 8 shows that ablating detection directions while fixing attention patterns reduces execution feature activations, with strong effects for most task pairs. This goes beyond correlation to demonstrate a mechanistic relationship. The cross-task ablation heatmap (Figure 6) further shows task-specific circuitry where ablating one task's top features leaves unrelated tasks largely unaffected.

4. **Concrete SFC adaptations that enable scaling to ICL on larger models.** The three modifications—token-position categorization, modified loss function targeting all non-first pairs, and cross-task faithfulness evaluation—are clearly motivated and the cross-task ablation analysis (Figure 6) provides evidence that the adapted SFC discovers task-specific (not generic) circuits.

## Weaknesses

### Fatal
None.

### Major

1. **The central claim "SAEs enable discovery of novel ICL components" is not adequately validated against non-SAE alternatives.** The paper never demonstrates that the task-detection features could not be found through other methods (e.g., direct activation patching on attention heads/neurons, PCA or NMF decomposition of task vectors, or standard circuit discovery like attribution patching without SAEs). Since the paper frames SAE necessity as part of its thesis, the reader cannot assess whether the SAE machinery is essential or merely a convenient reparameterization. The paper would be nearly as valuable if re-framed as "Using SAEs, we discover..." without claiming necessity, but as written the stronger claim is unsubstantiated.

2. **Steering and ablation experiments lack basic control baselines.** The steering experiments (Figures 5, 7) measure relative loss improvement when steering with identified features but do not compare against steering with random SAE features matched for activation norm or frequency. Similarly, the faithfulness ablation (Figure 6) does not report what happens when an equal number of *random* SAE latents or random model components are ablated. Without these baselines, the observed task-specificity could partly reflect that any direction with nonzero projection onto the task vector improves performance, or that any ablation of a non-trivial number of nodes degrades performance.

3. **The TVC algorithm's core technical details are deferred to an appendix figure (Figure 10) with minimal description in the main text.** The objective function, optimization procedure, hyperparameters, and computational cost are not stated in the main text. Given that TVC is a central technical contribution, this makes the paper's core methodology difficult to evaluate from the main text alone. The paper also provides no quantitative comparison showing that the original SFC *fails* on this setup, which would justify the claimed modifications.

### Minor

1. **Missing SAE training configuration details.** The paper does not state sparsity targets, expansion factors, training dataset size, number of tokens used for SAE training, or the specific layers where SAEs were applied. While some of these details may appear in the appendix, their absence from the main text makes the experimental setup incompletely documented.

2. **"30 times as many parameters" claim is imprecise.** The abstract states the model has "30 times as many parameters" compared to Marks et al. (2024). Marks et al. used Pythia models from 70M to 2.8B parameters. The comparison appears to target the smallest model (Pythia-70M), making the factor ~28.5×—but Marks et al. also ran experiments on Gemma-2-2B, a model of comparable size. This phrasing is sloppy and undermines credibility on a minor factual point.

3. **No feature selection bias analysis.** The TVC algorithm selects features based on their ability to steer (i.e., optimize loss on zero-shot prompts). This creates a selection bias: features that *can* steer are selected, and then steering is used as evidence of causal relevance. The paper does not address the possibility that these features are merely correlates that *can* be used for steering rather than being the actual components the model uses during ICL. A control experiment demonstrating that these features are causally necessary during normal ICL (not just zero-shot steering) would strengthen the claim.

### Trivial
None.

## Nice-to-Haves

- A comparison of TVC against sparse coding baselines (e.g., Lasso applied directly to task vectors with matched sparsity) would strengthen the decomposition claim.
- Ablating identified task-execution features during *actual ICL* (not just zero-shot steering) and measuring accuracy drop would directly link features to ICL performance rather than to the derived construct of task vectors.
- Confidence intervals or error bars on the steering and ablation results would help assess result stability, especially given the small number of tasks.

## Removed Points

- *TVC algorithm is "unverifiable" from main text*: The algorithm overview is cited to Figure 10 (appendix), which is standard practice. The main text gives the high-level description and results. This is not a fatal omission, though the main-text description could be more complete.
- *Criticism about missing appendix/proofs*: The parser strips appendix content; these exist in the original submission.
- *Strength Finder's generic strengths about "important problem"*: Removed as superficial/not paper-specific.
- *Criticism about comparing SAE features to PCA/NMF/random directions*: Kept the substance (missing control baselines) but removed the specific demand for PCA/NMF as that is scope-creep—the paper's control issue is the absence of *any* random baseline, not absence of specific decomposition baselines.
- *Missing related work concerns*: Removed per policy (cannot verify existence of omitted references).

## Novel Insights

The harsh critic's most useful observation is that the TVC algorithm's validation loop is circular *only if* one reads the paper as claiming that the *same* features must be the model's actual ICL mechanism. However, a more charitable reading is that TVC finds features that *approximate* task vectors in a sparse and interpretable basis—a valid engineering contribution regardless of whether the features are the "true" causal units. The genuine tension is between two different contributions: (1) SAEs as a tool for *discovering new structure* (task-detection features via SFC), which is supported and genuinely novel; and (2) SAEs as *necessary* for such discovery, which is unsubstantiated. Distinguishing these two claims resolves most of the apparent weaknesses—the paper's strongest result (task-detection features) does not depend on SAEs being uniquely capable, only on SAEs being *one useful tool* for the discovery.

## Suggestions

1. Reframe the paper's central claim from "SAEs *enable* discovery" to "Using SAEs, we discover" — this is more accurate and sidesteps the necessity criticism entirely.
2. Add random-feature steering baselines and random-node ablation baselines to the main experiments. These are low-cost and would substantially strengthen causal claims.
3. Add a small control experiment showing that the identified features are causally implicated during actual ICL (not just zero-shot steering), e.g., by ablating them during ICL forward passes and measuring accuracy degradation.
4. State the imprecise "30× parameters" comparison precisely (specify the reference model size) or remove it.
5. Move the TVC algorithm description from Figure 10 into the main text or provide a formal algorithmic box.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `tcsZt9ZNKD.md` (Scaling SAEs) | 8.2 | Much stronger: clean scaling laws, extensive evaluation, multiple metrics. Not directly comparable in scope. |
| `I4e82CIDxv.md` (Sparse Feature Circuits) | 8.0 | Much stronger: cleaner methodology, SHIFT application, automated pipeline. This paper is an application/extension of that work. |
| `xizpnYNvQq.md` (Revisiting ICL Inference Circuit) | 6.5 | Comparable: both study ICL mechanism. That paper had more thorough experiments but also missing controls. Slightly stronger. |
| `AwyxtyMwaG.md` (Function Vectors) | 6.0 | Comparable: both study ICL representations and decompose them. Function Vectors has cleaner causal evidence but less feature-level analysis. Similar level of contribution. |
| `ikwEDva1JZ.md` (ICL Beyond Simple Functions) | 6.5 | Stronger: includes theoretical construction plus thorough empirical probing on a well-scoped synthetic setup. |
| `fpoAYV6Wsk.md` (Circuit Reuse) | 6.5 | Stronger: cleaner causal evidence through circuit intervention and repair experiments. |
| `0ULf242ApE.md` (Context to Concept) | 6.0 | Comparable overall quality but different approach. Both have missing controls. This paper has somewhat stronger empirical support for its core claims. |
| `Wxl0JMgDoU.md` (Chess SAEs) | 2.5 | Much weaker: unclear methodology, poor presentation, limited claims. This paper is far stronger. |

The paper has genuine contributions (TVC algorithm, task-detection features, SFC scaling) but the major weaknesses—unsubstantiated central claim about SAE necessity, missing control baselines—prevent it from reaching the 6+ tier. It is clearly above the reject-level papers but below the strongest work in the area.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>