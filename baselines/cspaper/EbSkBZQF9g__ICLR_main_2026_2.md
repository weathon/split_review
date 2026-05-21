---
job_id: acc9e7b5-c251-49b8-b104-22dc37bfacd6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: EbSkBZQF9g.pdf
paper: Mechanistic Interpretability Analysis of a Single-Layer Transformer on 0-1 Knapsack
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies mechanistic interpretability of transformers on an algorithmic reasoning task and discusses generalization behavior of learned representations.

## Minimum Quality
Pass ✅. The manuscript contains the core scientific components expected for review, including abstract, introduction with related-work discussion, experimental setup, empirical observations/results, and conclusion; while the paper is weak, I do not see a desk-reject-level structural omission or a definitive integrity flaw from the text alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies a single-layer Transformer trained with TransformerLens on a small, algorithmically generated 0-1 knapsack task with four items, where the model predicts the optimal knapsack value from tokenized weights, prices, and capacity. The authors report that the model does not exhibit grokking and use a set of mechanistic interpretability tools, including attention visualization, singular value and principal component analyses, logit lens, probing, and activation patching, to analyze why the model fails. The paper closes with broader hypotheses about transformer limitations on NP-complete tasks and implications for AI deployment in planning-heavy settings.

## Strengths
The paper is commendably transparent about presenting a negative result. Many submissions try to dress up failure as success; here the central claim is simply that, in the tested setting, a shallow transformer did not grok 0-1 knapsack, and the paper does at least attempt to investigate that failure rather than just report a bad curve and move on.

The use of multiple interpretability tools is a genuine positive. The combination of attention analysis, logit lens, probing, activation patching, and spectral inspection provides several complementary windows into model behavior. Even if I am not convinced by all interpretations, the paper is trying to connect training behavior to internal structure rather than stopping at accuracy metrics.

Some figures are useful for orienting the reader. In particular, **Figure 3** makes the basic empirical claim legible: train loss falls sharply while test loss stays high, so the paper is indeed about a failure to generalize rather than a training instability. Likewise, **Figure 4** gives a simple summary of the model’s aggregate attention pattern and supports the narrower descriptive statement that the model attends disproportionately to the capacity token and some price positions.

The paper also includes some concrete supplementary quantitative artifacts rather than purely qualitative storytelling. For example, the probing results shown in **Figure 8** indicate near-perfect linear recoverability for some early item attributes and failure on later ones/capacity, which is at least a more falsifiable statement than vague claims about “not understanding the task.” Similarly, the activation-patching table in **Figure 9** shows a very large loss change when patching the reported layer/index, which does provide some evidence that a specific activation is important for the model’s prediction.

The limitations section is brief but honest. The authors explicitly state that compute constraints prevented scaling to deeper models and wider task families, which is important context for interpreting the ambition of the conclusions.

## Weaknesses
1. **The empirical scope is far too narrow for the paper’s headline claims, and this gap is not small, it is the central problem.**  
   The title and abstract frame the work as an analysis of a single-layer transformer on knapsack, which would be acceptable if the paper stayed there. But the abstract and conclusion go much further, claiming that this “shows how transformer-based models struggle to generalize on NP-complete problems” and that such models are unsuitable for tasks requiring substantial computation (**Page 1, Abstract**; **Page 4, Section 3**). The actual evidence is one architecture, one depth, one tiny setting with only **4 objects** (**Page 2**), and no comparison against deeper transformers, different widths, alternative positional encodings, different tokenizations, or even non-transformer baselines.  
   Why this matters: from the presented evidence, the only well-supported conclusion is something like “this particular 1-layer model did not grok this small knapsack setup.” Anything broader about transformers, NP-complete problems, or planning-heavy AI systems is speculative. The paper repeatedly overshoots its evidence.

2. **The task setup is underspecified in critical ways, which makes the experimental claims hard to evaluate or reproduce.**  
   On **Page 2**, the authors describe the input as \(W_1,\dots,W_4,P_1,\dots,P_4,C\) and output \(BP\), but they do not properly define the learning objective. Is the model trained as a next-token classifier with cross-entropy, as implied by “log-loss” in **Figure 3**, or as a regression model over the best value? What is the exact loss, for example  
   \[
   \mathcal{L}(\theta) = - \mathbb{E}_{(x,y)} \log p_\theta(y \mid x),
   \]
   or something else?  
   Related details are also missing or too implicit: how are integer values tokenized, what is the vocabulary mapping, what is the train/test split, how large are the train and test sets, whether the split is random or structured, whether all permutations appear in both splits, and whether there is any out-of-distribution evaluation. The code snippet on **Page 16** suggests exhaustive combinatorial generation over weight permutations, price permutations, and capacities, which raises a serious question about what exactly “generalization” means here. If the training set and test set are drawn from the same exhaustive family with heavy overlap in local statistics, then failure to grok may mean something very different from failure on genuinely novel compositions.

3. **The notion of “grokking” is used loosely, without the level of evidence normally expected for such a claim.**  
   The paper says the model was trained for up to 100k epochs and “was unable to grok” (**Page 2**). But grokking is not just “the test curve did not improve in one run.” The paper does not report sensitivity to weight decay, dataset size, optimizer settings, initialization, label noise, batch size, or training duration beyond the single reported regime. **Figure 3** indeed shows no delayed generalization in the reported setting, but that only establishes absence of grokking under that specific configuration.  
   Why this matters: for a paper explicitly about inability to grok, one wants much stronger evidence that the phenomenon was actually sought under reasonable conditions rather than inferred from one failed training recipe.

4. **Several interpretability claims are weaker than the paper presents them, because the analyses are descriptive and under-quantified.**  
   Consider **Figure 4** on **Page 3**. The heatmap does suggest elevated attention toward the capacity token, especially for one head, but aggregate attention alone is not enough to conclude that the model “places more importance” on that token in a causal sense. Attention is not equivalent to contribution. The paper partly tries to address this with activation patching, but the actual patching evidence presented in **Figure 9** is extremely limited, a single row with one layer/index and a large loss change, rather than a systematic sweep over positions, heads, or components.  
   Similarly, the statement that the MLP has the highest impact from logit lens analysis is not really substantiated in the main paper. On **Page 3** the authors describe outputs after embedding, attention, and MLP, but the supplementary **Figure 7** just prints three vectors for one example. That is not a robust quantitative comparison. If the claim is that the MLP contributes more than attention on average, the paper should report an aggregate statistic over many samples, not a single illustrative logit vector.

5. **The spectral analysis is suggestive at best, but the manuscript treats it as if it diagnoses representational failure.**  
   **Figure 5** compares singular values of the learned embedding matrix to a random matrix and to a modular-subtraction model. The authors infer that similarity to random implies the embedding learned little useful structure. This is a large interpretive leap. Singular value decay depends on many factors, including scale, parameterization, training dynamics, and the symmetry structure of the task. The comparison to modular subtraction is not obviously apples-to-apples, because modular arithmetic tasks have strong known periodic structure that one expects to show up spectrally.  
   The same issue appears in **Figure 6**, where the lack of smooth sinusoidal principal-component patterns is taken as evidence that the model failed to form a robust internal representation. But there is no reason to assume that knapsack should produce sinusoidal PC structure analogous to modular arithmetic. The absence of a familiar pattern from another task is not, by itself, evidence of failure. This part reads more like pattern-matching to previous interpretability work than a task-grounded analysis.

6. **The probing results raise questions that the paper does not investigate.**  
   In the supplementary probing table (**Figure 8**, **Page 6**), the linear probe can apparently recover \(W_1,P_1,W_2,P_2\) almost perfectly, while later items and capacity are near zero or negative. If that result is accurate, it is actually quite interesting, but the paper does not analyze whether this is due to positional bias, data ordering, optimization artifacts, or probe setup. Why the first half of the sequence is linearly recoverable while the latter half is not should be a central clue. Instead, the paper just states that the model “is able to perfectly store upto half of the weights and prices” (**Page 3**) and moves on.  
   Why this matters: the most informative result in the paper is left under-explained.

7. **The paper lacks essential baselines and comparison points.**  
   There is no deeper transformer baseline, no width/depth ablation, no non-transformer baseline, and no dynamic-programming-inspired or structured baseline. Even one additional model, for example a 2-layer transformer or a simple MLP, would help establish whether the failure is due to task complexity, architectural depth, training setup, or some accidental design choice. The concluding claim on **Page 4** that “lack of layers” restricts the model’s power is especially awkward because the paper does not actually test more layers. The argument is plausible, but it is still an untested hypothesis within this manuscript.

8. **The mathematical and algorithmic presentation is too thin for a paper making mechanism-level claims.**  
   There are almost no formal definitions beyond listing the tokens. The paper should define the target function \(f(w_1,\dots,w_4,p_1,\dots,p_4,C)=BP\), the distribution over examples, the optimizer hyperparameters, and the exact architecture in the main text. At present, some details only become inferable from **Figure 10** in the appendix, which shows a configuration with \(n_{\text{layers}}=1\), \(n_{\text{heads}}=4\), \(d_{\text{model}}=128\), \(d_{\text{mlp}}=512\), and \(n_{\text{ctx}}=3n+1\). This is useful, but key methodological details should not be buried in a screenshot.  
   More importantly, the paper makes a complexity-flavored hypothesis on **Page 4**: “Transformer-based models with \(k\) layers will only be able to generalize to tasks which can be solved using \(O(n^k)\) time complexity algorithms.” This is a very strong statement, and the paper offers neither theorem nor empirical scaling evidence for it. As written, this is not a supported result, it is an ambitious speculation.

9. **The train/test data construction may inadvertently make the task both tiny and idiosyncratic, yet the paper does not discuss the implications.**  
   The dataset uses weights and prices as permutations of \(1,\ldots,n\) and capacities as all unique subset sums from the superset of \(\{1,\ldots,n\}\) (**Page 2**). With only four objects, this induces a very particular combinatorial regime. It is not obvious whether this setup is representative of knapsack difficulty, because the item values and weights are highly structured, repeated across examples, and bounded in a tiny range. A single-layer transformer failing here could mean many things: insufficient depth, poor encoding of arithmetic relations, lack of training signal, or just a mismatch between architecture and tokenization. The paper treats it as evidence about NP-completeness, which is a stretch.

10. **The writing overreaches into policy claims that the experiments do not justify.**  
   The abstract and introduction invoke autonomous vehicles, criminal justice, and safety regulation, then the conclusion argues that the results “raise major doubts about the ability of LLM-based AI systems to reliably act as agents” and support limiting exposure of such systems through regulations and laws (**Pages 1 and 4**). This is rhetorically dramatic, but scientifically disconnected from the evidence. A failed single-layer toy transformer on 4-item knapsack does not bear that argumentative weight.  
   Why this matters: overclaiming does not just annoy reviewers, it weakens trust in the narrower, potentially interesting negative result the paper actually has.

11. **Presentation quality is uneven and sometimes sloppy enough to interfere with confidence.**  
   There are multiple typos and awkward phrases, for example “small lanugage models” in the abstract, “progaes” on **Page 3**, “shaping’s” on **Page 3**, and several grammar issues throughout. Some figure captions are minimal to the point of being unhelpful, especially many appendix figures that are just titled by attention pattern type without interpretation. Also, the paper introduces several analyses but often reports them in one or two sentences without enough methodological detail to judge whether the interpretation is sound.

12. **The literature positioning is incomplete for the claims being made.**  
   The paper cites some core mechanistic-interpretability and grokking references, but it does not adequately position itself relative to more directly comparable work on mechanistic analysis of reasoning/circuit formation and transformer limits on structured tasks. This matters because the paper’s main value is not a new method, it is the framing and interpretation of a negative mechanistic result. When positioning is thin, the contribution risks being a case study without a clear scientific takeaway.

## Questions
1. Please precisely define the training objective and evaluation setup in the main paper. Is this a categorical next-token prediction problem with cross-entropy over possible \(BP\) values, or a regression task? What exactly is the loss plotted in **Figure 3**?

2. What are the exact train/validation/test splits? Given the combinatorial data generation shown on **Page 16**, how do you prevent leakage of local patterns across train and test? A precise accounting of dataset sizes and split logic would substantially increase my confidence.

3. Did you try any standard settings known to affect grokking behavior, especially weight decay, different dataset fractions, longer training, different learning rates, or multiple random seeds? If the answer is yes, even a compact table of outcomes would help justify the claim that the model truly fails to grok rather than merely failing under one configuration.

4. Can you provide comparisons to at least one additional architecture, ideally a 2-layer transformer trained on the same task? This would directly test your own conclusion that lack of layers is the bottleneck.

5. For the probing analysis in **Figure 8**, why are the first two item pairs perfectly recoverable while the later pairs and capacity are not? Please clarify the probe target, the train/test protocol for the probe, and whether this asymmetry is consistent across seeds.

6. For the activation patching result in **Figure 9**, can you report a full map across layers, heads, and token positions rather than a single entry? As it stands, the evidence for the claimed dependence on capacity is too thin.

7. The conclusions on NP-complete tasks and the \(O(n^k)\) hypothesis are currently much stronger than the evidence. Would you be willing to substantially narrow these claims to the tested setting, or provide additional empirical/theoretical support?

8. Why should one expect the learned embedding for knapsack to exhibit the same kind of spectral or sinusoidal structure seen in modular arithmetic? A more task-specific justification for interpreting **Figures 5 and 6** would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
2: fair. The core negative observation in **Figure 3** is believable, and some mechanistic analyses are competently attempted, but the methodology is underspecified and several conclusions are not adequately supported by the evidence presented.

## Presentation Rating
2: fair. The paper is readable at a high level, but important experimental details are missing from the main text, the interpretation of figures is often underdeveloped, and the writing contains enough sloppiness to reduce confidence.

## Contribution Rating
1: poor. As currently written, the paper’s contribution is a narrow case study with limited empirical scope and substantial overclaiming beyond what the experiments can justify.

## Overall Rating
2: Reject, not good enough. There is a potentially interesting negative result here, and I appreciate the attempt to analyze failure mechanistically, but the paper is underpowered, underspecified, and overclaimed. The strongest evidence supports only a modest conclusion about one shallow model on one tiny knapsack setup, while the manuscript repeatedly generalizes to transformers, NP-complete problems, and AI policy in ways that are not earned by the experiments.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The main concerns are broad and evidence-based: limited experimental scope, insufficient methodological detail, weak support for interpretability claims, and conclusions that substantially outrun the presented results.