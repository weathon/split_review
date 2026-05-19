- Decision: Accept
- Avg Score: 4.33
- Scores: 5, 3, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes UNITIGBIN, a metagenomic contig binning tool that operates directly on unitig-level assembly graphs (rather than simplified contig-level graphs) using graph neural networks while incorporating heterophilous constraints from single-copy marker genes. The framework consists of a Learning stage (diffusion encoder-decoder with triplet Gaussian constraint optimization and p-batch parallelization) and a Binning stage (matching, label propagation with constraint penalties, and local refining). Experiments on 12 synthetic and real datasets assembled by metaSPAdes and metaFlye show substantial improvements over eight baselines, including a 45.8% gain in high-quality bins on metaFlye real datasets.

## Strengths

1. **First GNN designed for unitig-level assembly graphs in metagenomic binning:** The paper explicitly claims and supports that prior graph-based binners (GraphMB, RepBin, MetaCoAG, CCVAE) all operate on contig-level graphs reconstructed from the original assembly graph, whereas UNITIGBIN directly models the unitig-level graph (Section 1, Section 2). This is a clear differentiator.

2. **Consistently strong empirical results across multiple datasets:** On metaSPAdes-assembled simulated data (Table 1), UNITIGBIN achieves 76 HQ bins on Sim100G vs. 69 for the best baseline (MetaCoAG). On six real metaFlye-assembled WWTP datasets (Figure 4), UNITIGBIN produces 1,775 bins meeting completeness >90% & contamination <5%, compared to a maximum of 962 for any baseline — a 45.8% gap. The improvement is consistent across all datasets, not cherry-picked.

3. **Ability to bin short contigs (<1,000 bp):** The paper demonstrates on Sim20G (Table 2) that UNITIGBIN achieves a sequence-level F1 of 0.952 versus 0.632 for the next-best baseline (MaxBin2), attributed in part to its ability to handle short contigs that other tools discard (Section 4.1).

4. **Novel combination of constraint handling techniques:** The method introduces several non-trivial technical components: **(a)** a KL-divergence-based triplet ranking loss that enforces heterophilous constraints using Gaussian embeddings (Eq. 3); **(b)** a p-Batch strategy for scaling GNN training to million-node unitig graphs while preserving contig completeness (Section 3.1.3); **(c)** a greedy Matching algorithm that initializes bins without requiring the number of species (Section 3.2); and **(d)** a label propagation objective with an explicit constraint penalty term (Eq. 5).

5. **Ablation study isolating component contributions:** Figure 6 demonstrates that removing disentangling, sampling, constraints, or p-batch each degrades performance on Sim100G, providing evidence that the proposed modules are individually effective.

## Weaknesses

### Major

- **Missing within-framework ablation of unitig-level vs. contig-level graphs.** The paper's core motivation is that unitig-level assembly graphs preserve connectivity information lost in contig-level simplification. However, the ablation study (Figure 6) never compares UNITIGBIN's pipeline on a contig-level graph created from the same unitig graph (e.g., using the conversion strategy of GraphBin or GraphMB). Without this control, the improvements over baselines cannot be specifically attributed to the unitig-level graph — they could arise from the diffusion encoder, triplet loss, p-batch strategy, Matching/Refining algorithms, or the constraint handling. This is the central methodological gap: the paper claims one thing as its primary novelty but never isolates it experimentally.

- **Short-contig comparison is not apples-to-apples.** The paper emphasizes that UNITIGBIN bins contigs shorter than 1,000 bp that baselines discard, and reports superior F1 scores (Table 2) on the full contig set. If baselines filter out short contigs, they are evaluated on a smaller, easier subset (longer contigs have more reliable features), while UNITIGBIN takes on harder cases. The paper should report results on **(i)** the subset of contigs >1,000 bp for all tools and **(ii)** short contigs separately, to isolate whether the gains reflect a genuinely better method or simply a different task definition. This issue inflates the apparent performance gap.

### Minor

- **Triplet loss form is unusual and unablated.** The constraint loss (Eq. 3) uses a square-exponential form: \([D_{KL}(\mathcal{N}_k\|\mathcal{N}_i)]^2 + \exp[-D_{KL}(\mathcal{N}_j\|\mathcal{N}_i)]\). The paper cites LeCun et al. (2006) but that reference concerns energy-based models, not this specific combination. No ablation compares this loss against a standard triplet margin loss or contrastive loss. Given that constraints are a central design component, the sensitivity of results to this specific formulation is unclear.

- **No repeated trials or variance reporting for deep learning methods.** CheckM-based results on real data (Figure 4) and the ablation study (Figure 6) appear to be single-run evaluations. Deep learning methods (VAMB, GraphMB, CCVAE, and UNITIGBIN itself) have known variance due to initialization and training stochasticity. Reporting standard deviations or at minimum stating the number of runs would strengthen confidence in the reported improvements.

- **Magnitude of improvement on Sim20G warrants more discussion.** The sequence-level F1 gap (0.952 vs. 0.632 for the next-best) is very large. The paper attributes this to short-contig binning but does not quantitatively analyze how much of the gap remains when restricting to contigs >1,000 bp. A brief analysis would help the reader understand the sources of this dramatic improvement.

### Trivial

- **Parameter sensitivity results are deferred to appendix.** The main text (Section 4.3) states that UNITIGBIN shows low sensitivity to hyperparameters (d, α, τ, λ₁, λ₂) but provides no summary values (ranges tested, extent of variation). A brief statement in the main text would improve readability.

## Nice-to-Haves

- **Alternative evaluation metric for real datasets.** Although the paper partially addresses the circularity concern by using FragGeneScan+HMMER (not CheckM) for constraint extraction while using CheckM for evaluation, an additional metric not based on single-copy marker genes (e.g., alignment to reference genomes for datasets where available) would further strengthen the real-data results.
- **Controlled experiment for short contigs:** Run all tools on a common contig set (including short contigs) and report how many short contigs each tool successfully bins, along with per-length-bin quality.
- **Ablation of the triplet loss form** against a standard margin-based triplet loss to demonstrate the choice is not arbitrary.
- **Visualization of the p-Batch strategy** to clarify the batching procedure.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *Speculative concern about graph disentangling robustness to assembly errors:* The harsh critic raises that "not all graph edges reflect homophily (e.g., repetitive regions or assembly errors)" without evidence that this causes problems in UNITIGBIN. This is speculative and not grounded in a specific result from the paper.
- *Criticism about algorithmic details relegated to appendix:* The harsh critic faults the paper for missing Matching pseudocode, Refining details, and p-Batch specifics in the main text, stating these are "relegated to the appendix." Following the meta-review rules, content stripped by the parser is assumed to exist in the original submission; this criticism reflects an artifact of the review process, not an author error.
- *"First use of GNN" framing criticism:* The harsh critic suggests the claim should be softened. However, the paper already qualifies it with "To the best of our knowledge" (Section 1), which is appropriate for a novelty claim.
- *Speculative connection between ablation result and circularity:* The critic states "the largest gain appears to come from adding constraints... consistent with the circularity concern." This inference connects two separate observations speculatively without evidence and is not a standalone weakness.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the paper lacks a within-framework ablation (unitig vs. contig graph) is the most insightful cross-cutting point, as it correctly identifies a gap between the paper's central motivation and its experimental support. The strength finder's emphasis on the unusually large and consistent performance gap across six real metaFlye datasets provides the counterpoint: regardless of attribution, the method empirically outperforms existing tools by a wide margin.

## Suggestions

1. **Add the critical ablation:** Construct a contig-level graph from the unitig graph (using the conversion approach of GraphBin or GraphMB) and run UNITIGBIN's full pipeline on it. Compare to the unitig-level version. If the unitig version outperforms, the central claim is supported; if not, the narrative should be revised to emphasize the algorithmic contributions rather than the graph level.
2. **Control the short-contig comparison:** Report per-tool results on (a) contigs >1,000 bp only and (b) short contigs only, alongside the full-set results. This will clarify whether the performance advantage is driven by handling short contigs or by better binning of all contigs.
3. **Ablate the triplet loss:** Replace the square-exponential loss with a standard triplet margin loss and report whether the results change meaningfully.
4. **Report variance:** State the number of random seeds used and report standard deviations for main results, or at minimum clarify which results are single-run.
