- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes a hierarchical generative approach for Neural Architecture Search that can navigate an extremely large, general-purpose search space (~10^390). The method first learns a reversible latent space of micro cell designs using a Graph-VAE regularized by zero-cost (ZC) similarity, then uses a Conditional Continuous Normalizing Flow (CCNF) to generate "synonymous" high-performance cell variants from a reference, and finally trains a decoder-only transformer (GPT-Neo-125M) to produce macro architectures conditioned on user-specified FLOPs/params constraints. The key insight is to use ZC proxies not as rankers but as a clustering metric, and to amortize search cost through one-time pretraining of the generative hierarchy.

## Strengths

1. **Scalable hierarchy that dramatically reduces search space complexity**: Section 3.3 shows that clustering the micro design space and replacing individual cells with cluster identities shrinks the macro space from ~10^390 to ~10^78, making generative modeling of the full space feasible. This is a concrete and significant algorithmic contribution.

2. **Novel use of ZC vectors for clustering rather than ranking**: Section 3.1 (Eq. 2) defines a multidimensional ZC vector and uses GMM clustering to group designs by expected relative performance. This reframes ZC proxies from strict predictors to an organizational metric, enabling task-agnostic pretraining without ordered accuracy labels. The paper explicitly discusses the conceptual shift (lines 57-65).

3. **State-of-the-art ImageNet results among low-cost NAS methods**: Table 3 shows 78.3% top-1 accuracy at 450M FLOPs, surpassing other zero-cost/low-cost approaches (T-CET 78.0%, β-NAS 77.4%) while using only 30 search GPU hours (one-time pretraining). The method also achieves strong results at 600M and 1000M FLOPs budgets. Results are averaged over 3 searches (Section 4.2).

4. **Ablation confirming the hierarchy's benefit**: Table 2 shows Evo(T-CET) drops from 97.9% → 97.1% on CIFAR-10 when moving from ZenNet to the larger GraphNet space, while HL-Evo (using the learned hierarchy) reaches 98.3% with lower search cost. This progression (naïve Evo → HL-Evo → SG) isolates the benefit of each component.

5. **Amortized generation after one-time pretraining**: Section 4.1 and Table 2 show that after the one-time ~30 GPU-hour pretraining, generating architectures for new constraints takes minutes. This addresses the "cold start" problem in NAS and contrasts with methods that must re-run expensive search for each task.

6. **Generalization to diverse tasks beyond standard benchmarks**: Table 4 on NAS-Bench-360 shows the method improves over Wide-ResNet on 5/8 tasks and beats DASH (a dedicated NB360 method) on 4/8 tasks, all with zero task-specific feedback and lower search cost.

## Weaknesses

### Fatal

None.

### Major

1. **The CCNF validation on NATS-Bench-TSS (Table 1) lacks a clear methodology explanation, making the experiment hard to interpret.** The paper uses the best cell from NATS-Bench-TSS as a reference to evaluate CCNF-based sampling vs. naive neighbourhood sampling. NATS-Bench-TSS cells have a different structure (DARTS-style with 4 operation nodes, 5 operations) from the paper's GraphNet space (up to 6 operation nodes, 28 operations). The paper does **not explain how these reference cells are encoded into the G-VAE latent space**, nor whether the G-VAE (trained on a different distribution of graphs) can reliably encode/decode them. While this experiment is a supporting illustration rather than a core contribution, its unclear methodology weakens one of the paper's stated claims about CCNF-based synonym generation. The paper should either clarify the encoding procedure or replace this experiment with one performed entirely within the GraphNet space.

2. **The specific benefit of ZC-based clustering is not isolated via controlled ablation.** The paper's core motivation is that clustering micro designs by ZC similarity yields families useful for macro architecture search. However, no experiment measures whether this assumption holds. In Table 2, HL-Evo outperforms Evo(T-CET) on GraphNet, but this comparison conflates multiple changes: the hierarchical decomposition, the clustering, the CCNF, and the different search strategy. A controlled ablation that replaces ZC-based clusters with **random grouping** (or with clustering based on simple graph metrics like edit distance) while keeping everything else fixed would isolate whether the ZC-based clustering specifically drives the improvement. Without this, the paper's claim that "the informative organization of the search space" (Sec. 4.1) is responsible for the gains remains unsubstantiated by direct evidence.

### Minor

3. **Key numerical results lack variance reporting.** Table 1 shows single values without standard deviation across multiple runs. Table 4 (NB360) reports single values for 10 generated architectures without variance across repeated searches. The Section 4.2 ImageNet results are averaged over 3 searches, but this is not done for other experiments. Variance reporting is important to assess the stability of the method.

4. **The choice of the four ZC proxies is not ablated or justified.** Section 3.1 selects NASWOT, SNIP-SSNR, #params, and FLOPS as the ZC vector components, described as "common proxies." No analysis is provided on whether alternative choices, subsets, or weights would produce different clustering behavior or downstream performance. Given the method's heavy reliance on these proxies for organizing the entire search space, the sensitivity to this choice should be discussed.

5. **The SG conditioning mechanism (4-dimensional ZC vector → 125M-parameter transformer) is plausible but unverified.** Section 3.3 conditions the GPT-Neo-125M on a 4-dimensional ZC vector to produce 20-token macro sequences. The paper does not analyze whether the conditioning actually guides the output distribution (e.g., whether setting different FLOPs constraints produces measurably different macro architectures, or whether the conditioning collapses to a single region). An analysis showing that different y values produce distinct output distributions would strengthen the paper.

6. **The pretrained GPT-Neo-125M (trained on text) is fine-tuned for architecture sequences without analysis of domain mismatch.** The paper relies on a language-pretrained model for generating architectural sequences. No ablation compares this to a randomly initialized transformer of the same architecture, leaving open whether the language prior helps, hurts, or is irrelevant.

### Trivial

7. The paper occasionally has garbled text from PDF extraction (e.g., "rdeespoelnvdei tnhgi so, nb uwth iwceh fdaecsei gtnh" on line 122), but this is a parser artifact, not an author error.

## Nice-to-Haves

- **Replace the NATS-Bench-TSS experiment (Table 1):** Sample reference cells directly from the GraphNet space (e.g., from high-performing designs discovered during evolution) and compare CCNF-based sampling to naive latent-space sampling within GraphNet, reporting final accuracy on a fixed macro skeleton.
- **Ablation on the ZC vector composition:** Test whether performance changes when using different subsets of the four ZC proxies or when adding/removing proxies.
- **SG conditioning analysis:** Show histograms or t-SNE visualizations of generated macro-architecture properties (FLOPs, params) for different conditioning tokens y to demonstrate that conditioning is effective.
- **Randomly-initialized transformer comparison:** Ablate the benefit of starting from GPT-Neo-125M language pretraining vs. a randomly initialized transformer.
- **Report population size and evaluation count:** While these details are in Appendix C (stripped by the parser), making the evaluation count explicit in the main text would strengthen the paper.

## Removed Points

- **Cost implausibility (Critic's point 3):** The critic claimed 14 GPU hours is implausibly low for the HL-Evo given the space size. This is removed because (1) T-CET is a zero-cost proxy requiring only a forward pass per evaluation, making thousands of evaluations cheap; (2) The 14 GPU hours is the one-time ES pretraining cost, while Table 2's "Cost" column reports *search* cost (which is near 0 after pretraining); (3) The paper explicitly states "details of the HL-Evo algorithm can be found in App. C," which was stripped by the parser. Per the removal rules: missing appendix details are not valid weaknesses, and the critic's implausibility claim is based on a misunderstanding of the cost accounting.

- **Missing CCNF architecture details (g network, integrator, NFE):** These are implementation details that would be in the stripped appendix. Removed per the rule about missing appendix content.

- **Missing triplet loss weights/balancing:** Likely in the appendix. Removed per the same rule.

- **"Unfair comparison" with baselines on GraphNet:** The critic claimed running ZenNAS and ZiCo on GraphNet is unfair because their design choices (mutation operators) may not suit the larger space. This is removed because the comparison is fair and, if anything, *disadvantages* the author's method (the baselines have the same mutation operators they always use). The paper's point is precisely that naively applying existing methods to a larger space hurts performance, which the hierarchy recovers. Per the hard rule about asymmetry favoring the baseline.

- **Missing comprehensive survey of low-cost NAS approaches:** Removed per the rule about not mentioning missing related works.

- **Missing variance across architectures on NB360:** This is kept as Minor (point 3 above), not removed.

- **Strength 3 from Strength Finder about CCNF outperforming naive sampling:** Moved here because it conflicts with verified weakness #1 (the NATS-Bench validation is methodologically unclear). The strength may be valid but the experiment supporting it needs clarification.

- **Generic strengths dropped from Strength Finder:** The strength finder claimed "this paper addressed an important problem" and "this paper targeted an interesting question" — these are generic and removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify or replace the NATS-Bench-TSS experiment.** Either provide a detailed explanation of how NATS-Bench cells are mapped to the G-VAE's input representation, or replace Table 1 with an experiment entirely within the GraphNet space (e.g., using high-performing cells discovered during evolution as references).
2. **Add a controlled ablation for the ZC-based clustering.** Compare HL-Evo with ZC-based clusters to HL-Evo with random clusters (of the same size) while keeping the CCNF and hierarchical search fixed. This would directly test whether the ZC clustering drives the improvement.
3. **Report standard deviations or confidence intervals** for all key numerical results (Tables 1, 4), and clarify the number of independent runs for each experiment.
4. **Discuss sensitivity to the choice of ZC proxies** or add a small ablation in the appendix.
