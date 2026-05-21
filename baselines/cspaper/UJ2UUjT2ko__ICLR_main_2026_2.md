---
job_id: 721c2c12-2efb-4c10-af39-5f11c584b988
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: UJ2UUjT2ko.pdf
paper: Mixing Mechanisms: How Language Models Retrieve Bound Entities In-Context
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on mechanistic interpretability, causal abstraction, and representation/retrieval mechanisms in language models.

## Minimum Quality
Pass ✅. The paper contains the necessary research components, including abstract, introduction, prior work positioning, methodology, experiments, quantitative results, and conclusion, and it presents a technically coherent empirical study with sufficient evidence to merit full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious reviewer-targeting content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies how language models retrieve bound entities in-context, arguing that retrieval is not explained by a purely positional mechanism once contexts become longer or more complex. Through interchange interventions across nine models and ten templated binding tasks, the authors identify and characterize three mechanisms, positional, lexical, and reflexive, and then fit a simple causal mixture model over these mechanisms that approximates next-token distributions well. The paper also evaluates how these mechanisms vary with entity position, number of groups in context, and the insertion of filler text.

## Strengths
The paper asks a concrete and important mechanistic question. Entity binding and retrieval are central to in-context reasoning, and the work directly targets a specific claim in prior literature, namely that retrieval is mainly positional, then shows in a fairly systematic way where that picture breaks down.

The intervention design is thoughtful. Section 3.2 constructs counterfactual pairs so that positional, lexical, and reflexive mechanisms predict different outputs under patching. This is a good experimental design choice because it turns what could have been a vague interpretability story into falsifiable causal hypotheses. Figure 1 is particularly effective here, not just as illustration but as an operational description of the core intervention logic. It makes clear why the three mechanisms can be separated under the chosen counterfactual construction.

The empirical coverage is strong for a mechanistic interpretability paper. The authors test across three model families, multiple sizes, and ten tasks. Even though the tasks are templatic, the consistency across models in Figures 8, 9, 10, and 11 strengthens the claim that the observed pattern is not a one-model artifact. Figure 10 is especially useful because it compresses the cross-family evidence into a directly comparable format and shows that the U-shaped dependence on entity-group index is not isolated to gemma-2-2b-it.

The paper contains several genuinely informative visual analyses. Figure 2 is one of the strongest parts of the paper. The left panel localizes where binding information sits in the last-token residual stream, and the right panel makes the central empirical claim vivid: positional effects are stronger at the ends, while lexical/reflexive contributions rise in the middle. Figure 3 then adds an important nuance by showing that the positional mechanism does not simply disappear in the middle, it becomes diffuse. That distinction matters mechanistically.

The causal mixture model in Section 4 is simple, interpretable, and surprisingly effective. Equation (2) is easy to understand, and the decomposition into a Gaussian positional term plus one-hot lexical and reflexive terms is well motivated by the intervention results. The results table on Page 9 is compelling: the full model achieves JSS around 0.94 to 0.96, while the prevailing-view positional one-hot baseline is around 0.42 to 0.46. The ablations in the same table are also informative, because they show asymmetric importance of lexical vs reflexive mechanisms depending on \(t_{\text{entity}}\), which matches the earlier mechanistic story.

The reflexive mechanism is not merely asserted; the paper makes a real effort to separate it from a trivial “copied answer token” explanation. Figure 4 is a good example of this. The layer-\(\ell\) versus layer-\(\ell+1\) comparison is exactly the right kind of sanity check to address a confounder in the counterfactual design.

The paper is generally readable despite the amount of intervention machinery. The main narrative progresses cleanly from hypothesis, to dataset construction, to intervention evidence, to a compact fitted model, then to a limited generalization test with free-form filler text.

## Weaknesses
My main reservation is about external validity. The paper repeatedly uses broad language about how “LMs” retrieve bound entities, but essentially all evidence comes from highly controlled templatic binding tasks with distinct entities and carefully engineered counterfactuals. This is acknowledged only partially in Section 5. Even there, the “free form text” setup still consists of templated entity groups plus inserted “entity-less” filler sentences, which is not close to naturally occurring long-form documents with competing referents, coreference, paraphrase, and entity re-mention. So while the paper convincingly demonstrates a mixed-mechanism picture on these synthetic binding tasks, the jump from that to a general account of in-context entity retrieval in language models is still somewhat overstated. This matters because the title and conclusion are broader than the evidence base.

Relatedly, the taxonomy of exactly three mechanisms may be less definitive than the paper suggests. Section 3 frames positional, lexical, and reflexive as “the” mechanisms, and Section 6 states that LMs “rely on a mixture of three mechanisms.” But the intervention method mostly shows that these three explanatory variables are sufficient to account for a large fraction of observed behavior under the specific TargetRebind setup. It does not really establish exhaustiveness. In particular, the “mixed” mass in Figure 2 and the competitive effects in Figure 3 suggest that the underlying circuitry may not factor cleanly into three independent channels. A more careful phrasing would be that these three mechanisms provide a strong low-dimensional causal abstraction under the tested tasks, not necessarily the complete ontology of retrieval.

I have some concerns about how sharply the interventions isolate mechanisms. The paper uses full last-token residual stream patching at layer \(\ell\) as the main intervention in Section 3.3. That is a powerful probe, but it is also coarse. Patching the whole residual stream can simultaneously move several latent features, not just a single mechanism-specific variable. The authors partly embrace this by later fitting a mixture model, but then some of the causal interpretation becomes less clean than the prose implies. For example, the text around Figure 2 often reads as if the patch effect proportions are directly attributable to distinct mechanism activations, when in reality they are inferred by matching outputs induced by a composite intervention. This does not invalidate the findings, but it does limit how strong the mechanistic identification claim should be.

The mathematical formulation in Section 4 is intuitive but underspecified in a few ways that matter for reproducibility and interpretation. In Equation (2), \(Y_i\) is called a “logit value,” but the positional term is written as \(w_{\text{pos}}\cdot \mathcal{N}(i\mid i_P,\sigma(i_P)^2)\). It is unclear whether \(\mathcal{N}\) denotes a normalized Gaussian density over discrete indices \(i\in\{1,\dots,n\}\), an unnormalized kernel, or a discretized probability mass later rescaled into logits. Since the model is trained against distributions, this distinction matters. Similarly, the text says the authors “collected the logit distributions per index combination, and averaged them into mean probability distributions by first applying a softmax over the entity group indices and then taking the mean” (Page 9). That averaging order is a modeling choice with consequences, because \(\mathbb{E}[\mathrm{softmax}(z)] \neq \mathrm{softmax}(\mathbb{E}[z])\). The paper should justify this choice and clarify exactly what object Equation (2) is predicting before the final softmax. As written, the relation between patched LM logits, averaged probabilities, and the learned surrogate “logits” is a bit slippery.

There is also some notation inconsistency and avoidable ambiguity in Section 2. On Page 3, the template definition introduces \(t_{\text{entry}}\neq q_{\text{entity}}\) in prose, while the equations and later sections use \(t_{\text{entity}}\) and \(q_{\text{entity}}\). The indexing convention in \(\mathbf{G}_i^j\) is also easy to misread because the text says \(\mathbf{G}_i^j\) denotes the \(j\)-th entity in the \(i\)-th group, but later prose mixes “entry,” “entity,” and “group” terminology. These are not fatal issues, but for a paper whose core contribution is a mechanistic decomposition over indices, notation should be tighter than this.

The evidence for the fitted causal model is strong on the single main benchmark reported in the main paper, but still narrower than the prose suggests. The central results table on Page 9 reports JSS only for gemma-2-2b-it on the music task. The paper points to additional results in Section E, but the main-paper case for the surrogate model would be stronger if at least one cross-model table were included in the body rather than pushed out of the main narrative. Right now, the broad claim that the causal model “generalizes” across settings relies heavily on appendical support, whereas the main paper primarily demonstrates that the model works very well in one setup.

I am also not fully convinced by the treatment of the “lost in the middle” connection. Section 5 suggests that weakening lexical mechanisms and noisy positional mechanisms may offer a mechanistic explanation of the lost-in-the-middle effect. This is an interesting hypothesis, but the evidence in Figure 6 is indirect. The setup is still a synthetic interleaving task, and the figure shows changing confusion patterns under heavy padding, not an actual evaluation on retrieval or reasoning benchmarks where lost-in-the-middle is established. I would tone this down to a suggestive connection rather than an explanation.

Some results are persuasive qualitatively but a bit thin quantitatively in the main text. For instance, Figure 3’s right panel is used to argue for “competitive synergy,” meaning both amplification and suppression between mechanisms. I can see the qualitative pattern in the plotted mean logit distributions, but the paper does not provide a more explicit quantitative interaction analysis, such as deviations from an additive baseline or a formal interaction score. Since this interaction claim is one of the more interesting conceptual takeaways, it deserves more than a visual reading of a few selected curves.

Finally, the paper could do a better job positioning itself relative to broader entity-tracking literature beyond the mechanistic-interpretability line it cites heavily. The current prior work discussion is solid for causal intervention studies on binding circuits, but the framing would be stronger if the authors more clearly articulated how their notion of “binding and retrieval” relates to the larger body of work on entity tracking and state tracking in language models. Without that, the contribution can feel narrower than the title suggests.

## Questions
1. The strongest way to increase my confidence would be to clarify the exact semantics of Equation (2). Is \(\mathcal{N}(i\mid i_P,\sigma(i_P)^2)\) a normalized discrete distribution over entity-group indices, a continuous density evaluated on integers, or simply an unnormalized kernel feature? Please spell out how \(Y_i\) is converted into a probability distribution and how this matches the target distributions derived from patching.

2. On Page 9, you average \(\mathrm{softmax}\)-transformed patched outputs across 150 interventions for each \((i_P,i_L,i_R)\). Why is averaging probabilities the right target for the surrogate model, instead of averaging logits first or fitting to the full set of intervention-specific distributions? A short justification here would help.

3. How much of the explanatory power of the three-mechanism model survives if interventions are made more local, for example patching only selected attention head outputs, MLP outputs, or subspaces rather than the full last-token residual stream? This would help assess whether the proposed variables are truly isolated mechanisms or an effective summary of co-moving features.

4. The free-form filler experiment in Section 5 is directionally useful, but could you provide at least one main-text example closer to natural documents, with genuine entity mentions and re-mentions rather than “entity-less” padding? Even a smaller-scale qualitative or quantitative check would improve the paper’s external-validity story.

5. Figure 3 is used to support “competitive synergy.” Could you quantify this interaction more explicitly, for example by comparing observed combined effects against an additive model of separate mechanism contributions? A simple interaction metric would make the claim more rigorous.

6. The paper often phrases the three mechanisms as if they are exhaustive. Do you mean that literally, or only that these are the three dominant mechanisms identifiable under your intervention dataset? I would like the rebuttal to state this precisely, because it affects how broadly the conclusions should be read.

7. The central causal-model table in the main paper uses one model and one task. Could you add, in the rebuttal, a compact summary of whether the main JSS gap between \(\mathcal{M}\) and the positional baseline holds comparably across another model family in the main experimental setup?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are raised by the paper as presented. The work is an interpretability study on existing language models using synthetic and controlled prompts, and I did not see human-subjects, privacy, safety, or licensing issues that would require special ethics review based on the main text.

## Soundness Rating
3: good. The intervention methodology is careful and the main empirical claims are supported, but some causal interpretations are stronger than what the coarse patching setup strictly establishes, and the surrogate model formulation needs clearer specification.

## Presentation Rating
3: good. The paper is generally well organized and the figures are helpful, but notation is occasionally inconsistent and some important modeling details, especially around Equation (2) and target distribution construction, are not explained as clearly as they should be.

## Contribution Rating
4: excellent. The paper makes a meaningful contribution to mechanistic understanding of in-context entity retrieval by moving beyond a purely positional story and showing a robust mixed-mechanism account across several models and tasks.

## Overall Rating
8: Accept, good paper (poster). I found this to be a strong and informative mechanistic study with a clear empirical story, good figures, and a useful causal abstraction. The main caveats are about scope, strength of mechanistic identification, and some underspecified modeling details, but overall this is valuable for the ICLR community.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the relevant area, though a few implementation-level details of the intervention targets and surrogate model would benefit from clarification.