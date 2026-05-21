---
job_id: d2ea0d00-22f9-4982-9e0d-a0884297c67f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: pNpnqsn0Si.pdf
paper: Thoughtbubbles: An Unsupervised Method for Parallel Thinking in Latent Space
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it proposes a new transformer architecture for adaptive latent-space computation in language modeling and evaluates it on standard pretraining and zero-shot NLP benchmarks.

## Minimum Quality
Pass ✅. The submission contains the required scientific components, including Abstract, Introduction, Methods, Experiments, Results, Related Work, Conclusion, and Limitations; although there are important weaknesses in methodology and exposition, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, manipulative instructions to automated reviewers, or other suspicious content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes Thoughtbubbles, a decoder-only transformer variant that dynamically forks and deletes residual streams during the forward pass, with the goal of allocating more latent computation to tokens that appear to need it. The architecture learns these behaviors during standard LM pretraining, using cumulative per-stream scores that control top-$k$ keep/fork decisions, attention attenuation, residual update attenuation, and final score-weighted output averaging. Experiments on OpenWebText and peS2o at 150M, 319M, and 772M scales show better validation perplexity than a standard transformer and a duplicated-filler-token baseline, along with gains on some zero-shot evaluations such as LAMBADA and HellaSwag.

## Strengths
1. The paper tackles an interesting and timely problem, namely how to obtain adaptive inference-time computation without relying on explicit chain-of-thought tokens. Framing adaptive compute as latent-space residual-stream branching during pretraining is a meaningful architectural direction, and it is clearly relevant to current interest in latent reasoning and compute scaling.

2. The core idea is intuitive and reasonably well motivated. The combination of forking, pruning, score attenuation, and output aggregation does form a coherent system rather than a bag of unrelated tricks. In particular, the discussion around using cumulative scores both for structural decisions and for attenuating attention/residual updates gives the method an internally consistent training signal.

3. The main empirical result, improved perplexity over both the parameter-matched baseline and the copied-token baseline, is potentially interesting. In **Table 1** on Page 6, the gains in perplexity are fairly consistent across both datasets and all three model scales, and the improvements are not tiny at the larger budget settings. For example, on OpenWebText at 772M, the paper reports 21.22 for the baseline, 20.90 for Copy-5, and 19.74 for Ours $(\kappa=4L)$. Even if some evaluation choices need more justification, the perplexity trend is hard to ignore.

4. The paper includes some analysis aimed at understanding what the architecture is doing, which is better than presenting only benchmark tables. **Figure 4** is helpful in showing that the original token strongly attends to its child forks, which at least suggests that the extra streams are participating in computation rather than being dead branches. Similarly, **Figure 5** tries to connect compute allocation to uncertainty, giving a more interpretable story about where the model spends extra capacity.

5. The paper is refreshingly direct about limitations in Section 8. The authors explicitly acknowledge wall-clock inefficiency, the hard top-$k$ gradient bottleneck, and the lack of evaluation on harder reasoning tasks. That honesty is appreciated.

## Weaknesses
1. **The paper’s central comparison is not convincingly fair from a compute and architecture standpoint, especially for the “computation-matched” baseline.**  
   The duplicated-filler-token baseline in Section 3.3 and **Table 1** is too weak to establish that the proposed *adaptive* mechanism, rather than simply architectural complexity or a more favorable inductive bias, is the source of gains. The baseline is described as copying the input residual multiple times before running the transformer and decoding from the rightmost residual. This is a very particular and arguably strawman way of using extra sequence slots. It is not obvious that “copy residuals and decode the rightmost one” is the strongest non-adaptive latent-compute baseline. In fact, the proposed model gets several extra design choices the baseline does not, including learned fork embeddings, score-aware attenuation, score-weighted output mixture, and specialized position handling. So the comparison is not just adaptive vs non-adaptive compute, it is one full new architecture vs a deliberately simple filler-token construction. That matters because the paper repeatedly claims superiority over “computation-matched” methods, but the evidence really supports superiority over one relatively naive instantiation.

2. **The empirical story is narrower and less robust than the paper’s claims suggest.**  
   The abstract and conclusion make broad claims about adaptive computation and better downstream performance, but **Table 1** paints a more mixed picture than the prose admits. On BLiMP, the proposed method often underperforms Copy-3 or Copy-5, sometimes by a nontrivial margin, especially on peS2o. On PIQA, gains are inconsistent and small. Even on HellaSwag, the reported improvements are modest. The strongest and most consistent result is perplexity, not broad zero-shot reasoning quality. That distinction matters because the paper sometimes frames this as progress toward solving harder multi-step reasoning, but the evaluations are mostly language-model quality proxies and relatively lightweight zero-shot tasks. This weakens the significance of the “parallel thinking” framing.

3. **The method relies on hard top-$k$ structural decisions, but the training story around these non-differentiable operations is underspecified and raises optimization concerns.**  
   In Section 2.3, the model computes fork and keep scores, forms a list
   \[
   P=\left[\hat p_{\text{fork},0}^{(k)}, \hat p_{\text{keep},0}^{\prime (k)}, \dots, \hat p_{\text{fork},n}^{(k)}, \hat p_{\text{keep},n}^{\prime (k)}\right],
   \]
   then applies a top-$k$ operator to obtain $P_\kappa$, which determines which streams survive or are created via Equations (5) and (6). But there is no explicit discussion in the main paper of how gradients flow through this discrete selection. The limitation section later gestures at a “Top-K Gradient Bottleneck”, which is exactly the issue, but the main method section does not explain whether gradients are simply zero through dropped decisions, whether any straight-through estimator is used, whether tie-breaking is deterministic, or whether training is sensitive to top-$k$ instability. Since the architecture’s core behavior depends on these decisions, this is not a minor implementation detail, it is central to soundness.

4. **Several equations and notational choices are confusing or inconsistent enough to make the method harder to verify than it should be.**  
   There are multiple examples:
   - In Section 2.2, $L$ is introduced as sequence length, but the text says the embedded input is $x_{1,0}^{(0)}\ldots x_{l,0}^{(0)}$, switching between $L$ and $l$.
   - Equation (4) uses indices $(k,j)$ in $\hat p_{\text{keep},(k,j)}^{\prime}$ in a way that is inconsistent with earlier notation, where superscripts denote layers and subscripts denote token/stream identity. It is clear what the authors intend, but the notation is sloppy exactly where the forking bookkeeping is most delicate.
   - In Equation (11), the left-hand side is written as $x_i^{(k)}$, but the right-hand side is a probability distribution over the vocabulary, not a residual vector. This should be something like $p_\theta(y_i\mid x)$ or similar, not a hidden state symbol.
   - Appendix D, Equation (13), appears to mix indices incorrectly: the vector on the right uses $\binom{x_p^{(i)}}{x_k^{(j)}}$ rather than a consistent $(p,k)$ indexing for both coordinates. If the appendix is taken at face value, the formula is malformed.
   
   These may look cosmetic, but when the contribution is architectural and math-heavy, notation hygiene matters. It is currently too easy to misread what is being kept, forked, attenuated, and decoded.

5. **The attention attenuation formulation in Equation (8) is under-justified and somewhat unusual, and the paper does not adequately explain why this is the right probabilistic or optimization choice.**  
   Equation (8) adds $\mathbbm{1}\log(P^{(k)})^\top$ to the attention logits and also multiplies values by $P^{(k)}$. This means the score affects both the pre-softmax logits and the value magnitudes. In effect, low-score streams are doubly penalized. The paper gives intuition, but not a derivation or ablation showing whether both components are needed. A more careful decomposition would help: for example, what happens if only keys are masked in the logits, or only values are attenuated, or only residual writes are modulated? Since the learning signal for the forking mechanism is indirect, this design choice could have a large impact on performance, yet the paper does not isolate it experimentally.

6. **The output aggregation in Equation (11) is potentially problematic and deserves more discussion.**  
   The model decodes each residual stream separately into a vocabulary distribution, then averages the *probabilities* weighted by cumulative scores. This is a mixture of post-softmax distributions:
   \[
   p(y_i)=\frac{1}{\sum_j p_{\text{cum},(i,j)}^{(f)}}\sum_j p_{\text{cum},(i,j)}^{(f)} \, \mathrm{softmax}(\mathrm{Dec}_\theta(x_{i,j}^{(k)})).
   \]
   This choice is not obviously wrong, but it is materially different from averaging logits or using a learned merge in hidden space. The paper does not justify why probability-space averaging is preferable, nor whether it affects calibration or training stability. Because the proposed architecture creates multiple latent hypotheses per token, the merge operator is a central component, not a minor postprocessing step.

7. **The analysis figures are interesting but not strong enough to support the paper’s more ambitious interpretability claims.**  
   The paper states that the model “correctly allocates computation at interpretable regions” and that high-entropy regions attract more compute. But **Figure 5** on Pages 7-8 actually shows a fairly diffuse heatmap, not a crisp or obviously causal relationship. The text itself concedes a concave pattern where the most uncertain tokens may receive less computation. That is a subtle and potentially important observation, but the paper does not quantify it beyond visual inspection. Likewise, **Figure 4** shows that parent tokens attend to children more than to many other tokens, but that alone does not establish that forks are semantically useful computations rather than an artifact of local positional or representational similarity. The interpretability claims should be toned down or strengthened with more rigorous analysis.

8. **The paper’s use of figures is occasionally helpful, but some figures also expose unresolved questions rather than resolving them.**  
   **Figure 1** and **Figure 2** are useful for building intuition about bubbles of computation and the keep/fork process, but they also highlight how much hidden complexity is packed into the mechanism. For instance, **Figure 2** visually depicts top-$k$ selection over both keep and fork scores, yet the paper does not discuss pathological cases such as repeated deletion and reforking, token-level starvation, or sensitivity to layer placement. The figure is a good conceptual summary, but it also makes the absence of a more systematic ablation on the control mechanism more noticeable.

9. **The paper lacks several ablations that are necessary to understand what is actually driving performance.**  
   The main paper does not isolate the contributions of:  
   - score-attenuated attention vs score-attenuated residual updates,  
   - learned fork embeddings,  
   - the forced keep of the original token in Equation (4),  
   - the partial-RoPE modification,  
   - the output averaging rule,  
   - and the exact placement of forking layers.  
   Given the number of interacting components, the current results do not tell the reader whether the benefit comes from adaptive branching itself or from one or two auxiliary design choices. This is a major omission for a methods paper.

10. **The paper’s positioning against recent latent-space reasoning and pretraining-time pondering work feels incomplete.**  
   The related work section covers pause tokens, chain-of-thought, and adaptive compute broadly, but the paper would benefit from more careful positioning against other latent-thought or continuous-space reasoning approaches that also aim to scale computation without explicit natural-language traces. That omission matters because the paper’s headline claim is not just “we do adaptive compute”, but “we do it unsupervised during pretraining in latent space”. Without sharper contrast to nearby latent-computation methods, the originality story is less convincing than it could be.

11. **The autoregressive evaluation is underdeveloped relative to the claimed use case.**  
   Since this is a decoder LM, practical use depends on autoregressive generation, not just blockwise teacher-forced scoring. Section 5.1 and **Figure 6** show that naive autoregression creates a distribution shift and that a ratio-based budget scaling mitigates it. That is useful, but still shallow. The table below **Figure 6** reports only one model and one dataset slice, and there is no generation-quality evaluation, latency discussion, or stability analysis over long decoding horizons. If the paper wants to argue that train-time and test-time scaling are being unified, autoregressive behavior needs more than a small perplexity check.

12. **Some claims are overstated relative to the evidence.**  
   The title and framing use phrases like “parallel thinking in latent space”, and the conclusion says the model “allows our model to solve more difficult tasks that require scaling inference-time computation.” But there are no experiments on tasks that clearly require extended reasoning, and no direct comparison to explicit test-time scaling methods. The work is better described as a promising adaptive-pretraining architecture with improved perplexity and mixed zero-shot gains. The current rhetoric slightly outruns the empirical support.

## Questions
1. The main paper needs to explain the optimization path through the hard top-$k$ decisions more explicitly. Are the keep/fork scores trained only through the attenuation mechanism and downstream loss on surviving paths, with zero gradients through dropped choices, or is some estimator used? A precise answer here would increase my confidence substantially.

2. Can the authors provide an ablation isolating the components in Equations (8)-(10), specifically:  
   (a) log-score bias in attention logits only,  
   (b) value attenuation only,  
   (c) residual-write attenuation only,  
   (d) all combined?  
   Right now it is difficult to tell which part is essential.

3. What happens if the final merge in Equation (11) is done in hidden space or logit space instead of probability space? A small ablation would help determine whether the reported gains are sensitive to this choice.

4. The baseline story would be much more convincing with stronger alternative non-adaptive baselines. Can the authors clarify whether they considered learned latent filler tokens, layer-recurrent compute, or other equal-budget architectures rather than only input-copying? If such experiments exist, they would materially strengthen the paper.

5. For **Table 1**, are the zero-shot results averaged over multiple seeds or single runs? The table does not report variance or confidence intervals, and several differences are small. Reporting uncertainty would help assess how robust the downstream conclusions are.

6. The paper attributes high-entropy allocation behavior to meaningful dynamic computation. Could the authors quantify the relationship in **Figure 5**, for example with correlation statistics, conditional means, or comparisons against simple heuristics such as punctuation position, token rarity, or attention norm? That would make the interpretation much stronger.

7. The partial-RoPE construction seems important because forks create multiple streams for one token. Can the authors clarify in the main paper, not only outside it, how sensitive performance is to this design? If standard RoPE or no adjustment performs similarly, the mechanism may be simpler than currently presented.

8. The claim that the method can unify train-time and test-time scaling would be more persuasive with stronger autoregressive evidence. Can the authors provide generation-time analyses, longer-context decoding behavior, or wall-clock adjusted comparisons for the dynamic-budget inference rule?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission itself. The paper studies language model architecture and evaluation on standard text corpora and benchmarks, without introducing an obviously new dual-use or human-subject issue beyond those already common to pretrained language models.

## Soundness Rating
2: fair. The core idea is plausible and the empirical gains in perplexity are interesting, but the optimization story around hard top-$k$ decisions, several underspecified design choices, and the lack of key ablations reduce confidence that the central claims are fully supported.

## Presentation Rating
2: fair. The paper is readable at a high level and the diagrams are useful, but notation inconsistencies, equation-level sloppiness, and some overclaiming make the technical presentation weaker than it should be.

## Contribution Rating
2: fair. The proposed architecture is interesting and potentially useful, but the current evidence does not yet establish a sufficiently strong and well-isolated contribution for ICLR, especially given the limited baseline set and incomplete experimental decomposition.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a compelling high-level idea and nontrivial perplexity gains, but too many core questions remain unresolved, especially around the discrete forking mechanism, the fairness of the main baseline comparisons, and the lack of component ablations. I can see why some reviewers may lean positive on novelty and promise, but in its current form I do not think the paper clears the bar cleanly enough.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The main ideas, equations, tables, and figures were carefully checked, and my concerns are mostly about methodological support and technical clarity rather than misunderstanding the paper’s goals.