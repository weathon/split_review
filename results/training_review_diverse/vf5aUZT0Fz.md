Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes DEPT (Decoupled Embeddings for Pre-training), a framework for pre-training language models on heterogeneous data (multiple domains/languages) by decoupling token and positional embeddings from the transformer body during training. Three variants — Glob, Trim, Spec — offer progressively stronger specialization, from shared global embeddings (Glob) to fully per-source embeddings with separate vocabularies (Spec). The training uses a federated-style iterative aggregation (FedAvg/Local SGD). The paper reports perplexity improvements, robustness to heterogeneity, reduced embedding parameters (up to 80%), and large communication savings.

## Strengths

1. **Novel and well-motivated framework**: The idea of decoupling embeddings during pre-training to combat negative interference and the curse of multilinguality is creative and grounded in prior evidence (e.g., MonolingualTransferArtetxe, ActiveForgetting). The three-variant design (Glob → Trim → Spec) provides a clear design spectrum.

2. **Superior transformer body quality under random embeddings**: When evaluated with randomly initialized embeddings (isolating body quality), all DEPT variants significantly outperform all baselines across every multilingual and multi-domain validation set (Tables mc4_125M_r, the_pile_350M_r). This provides the strongest evidence that DEPT produces a fundamentally better foundation model.

3. **Substantial practical efficiency gains**: The paper quantifies memory savings (up to 80% reduction in embedding parameters), communication reduction (up to 675× vs standard DDP, 25% vs Local SGD), and the enabling of vocabulary-agnostic training. Trim and Spec maintain performance comparable to Glob while using significantly fewer parameters, making them practical drop-in replacements.

4. **Clear evidence of robustness and stability under heterogeneity**: Figure 2 shows that standard pre-training diverges (activation spikes, norm explosion) on heterogeneous data while DEPT remains stable, enabling training where standard methods fail. This is a concrete and demonstrable advantage.

5. **Better plasticity demonstrated**: Adaptation curves (Figure 3) show DEPT variants are both faster to converge and reach lower perplexity when adapting to new languages (HI, DE) and low-resource languages (SW), confirming genuine plasticity benefits.

## Weaknesses

### Fatal
None.

### Major

1. **The contribution of decoupling per se is conflated with the iterative training algorithm.** Glob uses the *same iterative aggregation* (FedAvg-style outer loop) as Trim and Spec but with *fully shared embeddings* — yet it already outperforms all standard pre-training baselines. The paper results* indicate that Trim and Spec perform *comparably* to Glob (the paper states they are "similar in effectiveness"). This means the primary driver of improvement over standard pre-training may be the iterative training algorithm itself, not the decoupling of embeddings. The paper's narrative and title foreground decoupling as the core innovation, but the evidence is consistent with a different interpretation: the federated aggregation scheme provides regularization and stability, and decoupling beyond Glob adds practical benefits (vocabulary-agnostic, memory savings) without degrading quality. The paper would be strengthened by a more honest framing and by directly comparing Glob (as a shared-embedding control) against Trim/Spec under varying levels of data heterogeneity to demonstrate where decoupling specifically matters.

2. **No downstream task evaluation.** The paper reports only perplexity on validation and OOD sets. For a pre-training method intended to serve as a foundation model, downstream task performance (e.g., classification, QA, translation on benchmarks like XNLI, MLQA, or Pile-related tasks) is the standard measure of practical utility. Perplexity is a useful proxy but can be misleading, especially when the training procedure differs substantially from standard LMs. The paper claims improved "generalization" and "plasticity" but only demonstrates the former via perplexity. Adding 3–4 established benchmarks would significantly strengthen the contribution.

### Minor

3. **Plasticity evaluation confounds pre-training algorithm with adaptation benefits.** In the plasticity experiments (Figure 3), the DEPT models' transformer bodies were themselves pre-trained via iterative aggregation, while baseline bodies were pre-trained via standard mixed sampling. The faster adaptation of DEPT could thus be partly attributable to the iterative pre-training algorithm rather than decoupling. An experiment where both DEPT and baseline models start from the *same* pre-trained body and then undergo adaptation would isolate the decoupling effect.

4. **No hyperparameter sensitivity analysis.** DEPT introduces new hyperparameters (number of local steps per round, subset selection frequency, outer optimizer configuration) beyond those of standard pre-training. These are used at fixed values without justification or ablation. A sensitivity analysis would strengthen reproducibility and help practitioners deploy the method.

5. **Plasticity measured only via perplexity, not downstream adaptation.** The adaptation experiments (Figure 3) measure perplexity during continued pre-training on new languages/domains. Showing that the adapted model also performs better on downstream tasks in those languages/domains would provide stronger evidence for the plasticity claim.

### Trivial
None.

## Nice-to-Haves
- A case study showing a specific setting where Glob (shared embeddings) fails or underperforms compared to Trim/Spec (e.g., languages with very different scripts, domains with disjoint vocabularies), to clearly demonstrate when the extra decoupling is critical.
- Analysis of the impact of tokenizer choice and vocabulary construction in the Spec variant.
- Empirical comparison of communication costs against a Local SGD baseline (the current comparison is analytical/formula-based).

## Removed Points
- **"Billion-scale model claim is unsupported"**: The paper references results in \cref{app:big_model}, which exists in the original submission but was stripped by the parser. Per the rules, this weakness is removed.
- **"Local SGD not included in experiments"**: The paper uses Local SGD / FedAvg as the outer optimizer (Section 3). The communication efficiency comparison to Local SGD is analytical (Table 1), not an omitted experimental baseline. This criticism misunderstands the paper.
- **"Missing appendix details"**: Multiple references to appendix sections for experimental details (tab:model_architectures, tab:dept_params) are standard for conference submissions; the parser strips these. Not a valid weakness.
- **"The authors should also cover Y / domain Z / additional tasks"**: Scope-creep demands for broader coverage beyond the paper's stated scope.
- **"Formatting/style nitpicks"**: Parser artifacts, not author errors.

## Novel Insights
The most insightful observation from the reviews is the conflation between the iterative training algorithm and decoupling. The Glob variant — which uses shared embeddings but the same iterative aggregation as Trim/Spec — already beats all standard baselines. This suggests the paper's primary finding could be reframed: *federated-style iterative pre-training* is highly effective for heterogeneous data, and embedding decoupling (Trim/Spec) adds practical efficiency benefits without sacrificing quality, rather than being the primary source of perplexity gains. This reframing would make the contribution clearer and more honest.

## Suggestions
1. **Reframe the contribution**: Acknowledge explicitly that the iterative aggregation scheme (FedAvg/Local SGD) provides regularization and stability that is a key driver of the observed improvement, and that decoupling (Trim/Spec) is valuable primarily for enabling practical benefits (memory, communication, vocabulary-agnostic training) without harming model quality.
2. **Add a dedicated Glob-as-control experiment**: Run Glob vs Trim vs Spec under varying data heterogeneity levels (e.g., increasing number of languages, decreasing vocabulary overlap) to show the specific conditions where further decoupling beyond Glob matters.
3. **Add 3–4 downstream benchmarks** (e.g., XNLI for multilingual, a couple of Pile-based classification tasks) comparing DEPT fine-tuned against standard pre-training baselines.
4. **Add hyperparameter sensitivity** for the number of local steps and subset selection frequency — two key algorithmic knobs introduced by DEPT.

## Score and Decision

The paper presents a creative idea and solid empirical evidence that the DEPT pipeline outperforms standard pre-training under data heterogeneity. The efficiency gains are substantial and practically valuable. However, the primary weakness is a framing gap: the paper claims decoupling as the central contribution, but the evidence suggests the iterative aggregation algorithm drives most of the improvement (since Glob, which barely decouples, also outperforms baselines). The lack of downstream task evaluation further limits the practical demonstration. With honest reframing and additional experiments, this could be a strong paper, but in its current form it overclaims relative to its evidence.

**Originality**: Above average. **Importance**: High. **Claims support**: Moderate (confounded). **Soundness**: Moderate. **Clarity**: Good. **Value**: Moderate.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>