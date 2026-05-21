---
job_id: ce1d4eca-27f8-4434-83c8-70f747357f4a
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: A4Us8jxVGq.pdf
paper: How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies learning dynamics, representation learning in transformers, and mechanistic interpretability of language models.

## Minimum Quality
Pass ✅. The submission contains all core components expected of a research paper, including abstract, introduction, related work, model/setup, theoretical analysis, experiments, results, and conclusion, and it provides substantial technical and empirical content.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies how semantic token associations emerge during early training in attention-only transformers trained for next-token prediction. The core contribution is a leading-term gradient analysis yielding closed-form approximations for the output, value, query-key, and positional parameters in terms of three corpus-derived basis functions, namely a bigram mapping, an interchangeability mapping, and a context mapping. The paper also provides empirical validation on a small attention-only transformer trained on TinyStories and an analysis of representations and attention statistics in Pythia-1.4B.

## Strengths
The paper has a real technical core. The main theorem in **Section 4.1**, summarized in **Theorem 4.1** on **Page 5**, gives explicit leading-order formulas for multiple parameter classes, not just a single module. In particular, the scaling separation across parameter types, $W_O = O(s\eta)$, $V^{(l)} = O(s^2\eta^2)$, and $W^{(l)}, P^{(l)} = O(s^4\eta^4)$, is interesting and gives a concrete story for why output-layer bigram structure should appear first. This is more informative than papers that stop at qualitative claims about “early features.”

I also appreciated that the paper tries to keep the theoretical setup closer to practice than many training-dynamics papers. The model in **Definition 3.1**, **Equations (1) and (2)** on **Page 4**, retains causal masking, residual connections, and relative positional information. That does not make it fully realistic, but it is meaningfully closer to standard language modeling than many stripped-down analyses.

The basis-function decomposition is conceptually clean and helpful. **Figure 2** on **Page 5** is particularly effective here. It does not just decorate the theorem, it clarifies the computational roles of the three proposed statistics across different weights: $\bar{\mathbf{B}}$ for the output matrix, $\bar{\Phi}^\top \bar{\mathbf{B}}^\top$ for value matrices, and the more involved composition for $\bar{\mathbf{Q}}$ in query-key weights. This figure made the theorem more interpretable than the surrounding prose alone.

The empirical alignment in the controlled TinyStories setup is surprisingly strong. **Table 1** on **Page 8** reports minimum cosine similarities above 0.998 for attention, value, and output weights across epochs, and **Figure 4** shows that similarity remains high even as training progresses. Even if one can debate whether cosine similarity is the right metric, these numbers are strong evidence that the leading-term directions capture a large fraction of learned structure in the toy setting.

The qualitative examples are useful rather than purely anecdotal. In **Figure 5** on **Pages 8-9**, the three basis functions do appear to correspond to distinct token relations: bigram-like continuation, functional interchangeability, and broader contextual association. The “fish $\rightarrow$ pond/lake/water” pattern and the adjective/object examples support the interpretability claim reasonably well.

The attempt to connect the theory to a realistic LLM is ambitious and, within its limitations, nontrivial. **Figure 6** on **Page 9** shows consistent early-training agreement between corpus-derived leading-term features and layerwise token-correlation statistics in Pythia, especially for embeddings. I also found the per-head visualization in **Figure 7** on **Page 10** informative, because it suggests heterogeneity in how heads specialize relative to the leading-term feature, rather than collapsing everything into a single layer average.

Overall, this is one of the more mechanistically interpretable training-dynamics papers I have seen in this area. It gives an explicit story for what transformer weights initially encode, and the story is specific enough to check empirically.

## Weaknesses
1. **The strongest empirical claim is validated only in a setting that does not actually match the theorem’s optimization assumptions.**  
   The theory in **Section 3.3**, especially **Equation (4)** on **Page 4**, is explicitly stated for full-batch gradient descent with constant learning rate. But the main controlled experiment in **Section 5.1** on **Page 8** says the model is trained with “SGD using a batch size of 2048.” That is not a cosmetic mismatch. Early-stage dynamics can be quite sensitive to optimization noise, and the entire point of the theorem is a leading-term description of gradient updates. If the empirical verification is done under minibatch SGD, then the paper should either justify why the same leading-order formulas should remain valid under stochastic gradients, or include a full-batch experiment showing the claimed agreement is not an artifact of a different optimizer regime. As written, the validation is very strong numerically, but it does not directly test the exact theoretical setting.

2. **The main theorem is only presented informally in the main paper, and several key objects are effectively deferred out of view.**  
   **Theorem 4.1** on **Page 5** introduces $\bar{\mathbf{Q}}$ and $\Delta$ only at a high level, and **Section 4.2.2** states that the construction of $\widetilde{\mathbf{Q}}$ is given only as an overview, with details pushed to Appendix A. But $\bar{\mathbf{Q}}$ is the entire leading term for the query-key weights in **Equation (7)**, which is one of the central claims of the paper. In the main text, the construction depends on several operations, including masking, centering, normalization, and a next-to-query shift, yet the exact algebra is omitted. This matters because the paper’s headline contribution is not just that some correlations exist, but that specific weight matrices are characterized by specific composed statistics. For the output and value matrices, the main paper gives reasonably explicit formulas, but for the attention weights the story remains partially schematic.

3. **There are noticeable notation inconsistencies and under-specified mathematical transitions in the main paper.**  
   A few examples:
   - In **Equation (1)** on **Page 4**, the paper defines $\mathbf{F}_\Theta(\mathbf{X}) = \mathbf{h}^{(L)}\mathbf{W}_O$, but the line above uses $\Theta$ while **Equation (3)** later uses $\mathbf{F}_{\theta}(\mathbf{X}_i)$. This is minor, but the notation does drift.
   - In **Equation (8)** on **Page 5**, the norm on $\mathbf{P}^{(l)} - c\Delta$ is written as a Frobenius norm, while $\mathbf{P}^{(l)} \in \mathbb{R}^T$ in **Section 3.2**. This is not wrong if one interprets Frobenius as Euclidean norm for vectors, but it is sloppy and should be clarified.
   - In **Equation (11)** on **Page 6**, the definition of $\bar{\Phi}$ is difficult to parse and appears to mix positional averaging, token events, and centering in a way that is not cleanly formalized in the surrounding text. The prose says the $(i,j)$ entry is the likelihood that token $\mathbf{e}_j$ appears as a prefix of $\mathbf{e}_i$, but the indexing in the displayed formula does not make that interpretation immediately transparent.
   - In **Equation (12)** versus **Equation (13)** on **Page 7**, the notation switches from bars to tildes, and the relation between $\widetilde{\Phi}, \widetilde{B}, \widetilde{Q}$ and the previously defined $\bar{\Phi}, \bar{B}, \bar{Q}$ is not cleanly explained in the main text. Since these equations are presented as the leading-term computation of the full model, this notation drift is more than cosmetic.

4. **The empirical evidence for “generalization to practical LLMs” is indirect and weaker than the rhetoric suggests.**  
   In **Section 5.2** on **Page 9**, the paper is careful to say that direct weight comparison is impossible for Pythia because of MLPs and multi-head attention. Instead, it compares covariance matrices of transformed embeddings and averaged attention maps to covariance matrices of theoretical features. That is a reasonable exploratory analysis, but it is a much weaker statement than saying the theorem “characterizes” practical LLMs. **Figure 6** does show some positive alignment, but the measurement pipeline includes several layers of transformation: averaging query-key products across heads, projecting by token embeddings, converting to token-space matrices, then comparing covariance matrices after row normalization. At that point, agreement is suggestive, not a direct validation of the theorem. The paper should tone down the stronger claims in the introduction and conclusion, or clearly distinguish direct verification from proxy-based analogy.

5. **Some of the quantitative presentation choices hide information that would be important for assessing robustness.**  
   **Table 1** on **Page 8** reports the *minimum* cosine similarity across epochs. This is unusual, because for a quantity that starts near 1 and later decays, the minimum alone hides the full temporal profile, dependence on layer, and sensitivity to initialization or random seed. **Figure 4** helps, but it seems to show the large learning-rate setting only, based on the plot title “Cosine Similarities Large LR,” while the text discusses both $\eta=0.005$ and $\eta=0.05$. If that reading is correct, then the small-learning-rate result, which is presumably closer to the theorem’s regime, is not visualized in the main paper. I would have preferred a table with several checkpoints or an AUC-style summary, plus error bars across seeds. Right now the toy-model empirical story is strong but somewhat cherry-picked in how it is summarized.

6. **The layer-uniformity claim is interesting but under-analyzed empirically.**  
   The theorem states the same leading characterization holds uniformly across layers, see **Theorem 4.1** on **Page 5** and the discussion below it. But the paper does not really interrogate whether this uniformity is substantive or merely a consequence of the early-stage expansion before layers differentiate. **Figure 4** mentions ranges across layers, and **Figure 6** suggests different layers in Pythia drift at different rates, but there is no focused analysis of when layer differentiation begins or how quickly the common leading term stops being equally predictive across depths. That matters because one of the paper’s more intriguing mechanistic claims is that all layers initially encode common associative features before specializing.

7. **The semantic interpretation occasionally overshoots what the statistics strictly establish.**  
   The paper often uses examples like “country-capital” or “animal-habitat” in **Section 4.2.1** on **Pages 6-7**, and phrases the basis functions as uncovering “semantic associations.” But the actual defined objects are corpus statistics over next-token transitions, token-distribution similarities, and smoothed prefix co-occurrences. These can certainly correlate with semantics, but they are still distributional statistics. The qualitative examples in **Figure 5** support this framing, but they do not establish that the method distinguishes semantic association from frequency, topic co-occurrence, or syntax. This is not fatal, but the paper would be more precise if it consistently said “distributional associative features with semantic content” rather than leaning so heavily on semantic language.

8. **The relation to prior mechanistic interpretability work is good but not fully sharpened at the level of claims.**  
   The paper repeatedly claims to provide the “first explicit characterization” of weights in attention-based transformers on real-world text, see the contribution list on **Page 2**. That may be directionally true, but the claim is stated broadly enough that it invites pushback. Prior works on early training dynamics, induction, topic structure, and bigram-style behavior are discussed in **Section 2**, but the paper could do a better job of specifying what exactly is first here: full closed-form leading terms for several weight classes, under natural language data, in an attention-only model with positional encoding and simultaneous training. Without that precision, the novelty claim sounds a bit too sweeping.

9. **The causal intervention result, while interesting, is not integrated into the main paper and leaves an interpretability gap.**  
   Appendix **Table 3** on **Page 16** shows that removing the leading-term component of the output layer hurts loss much more than removing attention components, which is consistent with the theorem’s order analysis. But this also highlights a limitation: if the attention leading term has very small immediate effect on loss, then the practical behavioral importance of the attention characterization remains somewhat unclear in the main text. The paper says these features provide an “anchor” for later training in **Section 4.2.3** on **Page 7**, but this temporal-causal story is not directly demonstrated.

10. **Presentation quality is good overall, but there are several avoidable rough edges in exposition.**  
    There are small but repeated issues, such as uppercase section headings mixed with standard style, inconsistent use of bars and tildes, some references that appear typo-prone in the bibliography, and several dense paragraphs where the intuition and formal object are interleaved too quickly. This does not sink the paper, but for a theory-heavy submission, cleaner notation discipline would materially improve readability.

## Questions
1. The theory is stated for full-batch gradient descent in **Equation (4)**, while the TinyStories verification in **Section 5.1** appears to use SGD with batch size 2048. Can the authors either justify why the same leading-term predictions should remain accurate under minibatch noise, or provide a direct full-batch verification in the rebuttal? A concise empirical comparison would increase my confidence.

2. For the practical-LLM analysis in **Section 5.2**, could the authors better calibrate what exactly is being validated? In particular, how much of the alignment in **Figure 6** survives if one changes the comparison operator, for example comparing without covariance, without row normalization, or without averaging heads? This would clarify whether the result is robust or heavily dependent on the chosen proxy pipeline.

3. Could the authors provide a cleaner main-text definition of $\bar{\mathbf{Q}}$, perhaps as a compact displayed equation rather than a verbal three-step overview plus appendix dependence? Since **Equation (7)** is one of the central theoretical claims, I think the main paper should expose the object more explicitly.

4. How sensitive are the TinyStories cosine results in **Table 1** and **Figure 4** to random seed, vocabulary truncation, and learning rate? Even a small table over a few seeds would help determine whether the extremely high cosine values are generic or somewhat fragile.

5. The paper argues that all layers initially share the same characterization, but later specialize. Can the authors quantify layer differentiation over time in the toy model, for example by plotting per-layer cosine similarity or inter-layer divergence rather than only showing a range? That would sharpen the mechanistic interpretation of the uniform-across-layers theorem.

6. The paper often interprets $\Sigma_{\bar{\mathbf{B}}}$ as “interchangeability.” Could the authors clarify whether this is primarily capturing syntactic substitutability, semantic similarity, or just shared left-context frequency patterns? A controlled analysis on POS categories or synonym sets could make this interpretation more convincing.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper studies training dynamics and interpretability of language models using public text corpora and existing open models. I do not see a concrete ethics issue in the methods or experiments described in the main paper.

## Soundness Rating
3: good. The paper is technically substantial and the central claims are supported reasonably well, but there is still a noticeable gap between the exact theorem setting and parts of the empirical validation, especially the optimization mismatch and the indirect nature of the Pythia analysis.

## Presentation Rating
3: good. The paper is readable and the central ideas come through, with useful figures such as **Figure 2**, **Figure 5**, and **Figure 6**, but several notation inconsistencies and under-specified objects in the main text keep it from being excellent.

## Contribution Rating
3: good. The closed-form leading-term characterization across multiple transformer weight classes is valuable and likely of interest to the ICLR community, though some novelty claims should be stated more carefully and the practical reach should be framed more modestly.

## Overall Rating
8: Accept, good paper (poster). I found this to be a strong paper with real theoretical and interpretability value. The core contribution is meaningful, the toy-model validation is compelling, and the connection to practical LLMs, while more indirect than the paper sometimes suggests, is still informative. I have several technical and presentation reservations, but they do not outweigh the strength of the main result.

## Reviewer Confidence
4: confident. I am confident in my assessment and checked the main equations, theorem statements, and empirical claims carefully, though the full appendix-level proofs are extensive enough that I cannot claim complete formal verification of every step.